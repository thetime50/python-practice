# -*- coding: utf-8 -*-
import re
import sys
import time
import os
import threading

def md_add_toc_list(fname):
	f = open(fname, 'r+')
	dat = f.readlines()

	toc_start = None
	for i, sti in enumerate(dat):
		if re.match('^\s*\[toc\]\s*$', sti, re.I):
			toc_start = i
			break
	if toc_start == None or toc_start == len(dat) - 1:
		f.close()
		return
	cnt = 0
	for i in dat[toc_start + 1:]:
		if re.match('^\s*- \[[^\]]*\]\(#[^)]*\)$', i) == None:
			break
		cnt += 1
	if toc_start + cnt == len(dat) - 1:
		f.close()
		return
	toc_end = None
	if re.match('^\s*\[tocend\]\s*$', dat[toc_start + cnt + 1], re.I):
		toc_end = toc_start + cnt + 1

	toc_list = []
	for i in dat:
		if re.match('#+ ', i):
			tli = i.split(' ', 1)
			hn = len(tli[0])
			hstr = tli[1].strip()
			toc_list.append('%s- [%s](#%s)\n' % ('  ' * hn, hstr, hstr))

	f.seek(0, 0)
	f.writelines(dat[:toc_start + 1])
	f.writelines(toc_list)
	if not toc_end:
		f.write('[tocend]\n\n')
		toc_end = toc_start + 1
	f.writelines(dat[toc_end:])
	f.close()


class fileSubstrFliter_C:
	def __init__(self, path_list, substr, filesmax):
		self._substr = substr.lower()
		self._filesmax = filesmax
		self.md_list = []
		self._exit=False
		if type(path_list) == type([]):
			pl = path_list
		elif type(path_list) == type(''):
			pl = [path_list]
		else:
			pl = []
		pl = [os.path.normpath(i) for i in pl]
		self._path_list_process(self.md_list, pl)

	def _ismd(self, sti, substr):
		return os.path.isfile(sti) and os.path.splitext(sti)[1].lower() == substr

	def _path_list_process(self, md_list, path_list):
		if self._exit:
			return
		for i in path_list:
			if self._ismd(i, self._substr):
				if len(md_list) >= self._filesmax:
					print('\033[1;32;m warning \033[0m!file is too many:',len(md_list))
					print('current file:',i)
					cont = input('Dou you wanna continue?(yes)')
					if cont=='yes':
						self._filesmax+=500
					else:
						del md_list[:]
						self._exit=True
						break
				md_list.append(i)
		if self._exit:
			return
		for i in path_list:
			if os.path.isdir(i):
				subpath_list = os.listdir(i)
				subpath_list = [os.path.join(i, f) for f in subpath_list]
				self._path_list_process(md_list, subpath_list)

###############################################################################
##thread
###############################################################################
class secureIter_C(object):
	def __init__(self,li=[]):
		self.lock=threading.Lock()
		self._it=iter(li)
	def __iter__(self):
		return self
	def __next__(self):
		self.lock.acquire()
		try:
			t=next(self._it)
		finally:
			self.lock.release()
		return t

class securefun_C():
	def __init__(self,fun):
		self._lock=threading.Lock()
		self._fun=fun
	def __call__(self, *args, **kwargs):
		self._lock.acquire()
		ret = self._fun( *args, **kwargs)
		self._lock.release()
		return ret

s_print=securefun_C(print)

class addTocListThread_C(threading.Thread):
	def __init__(self,id,file_name_iter):
		#threading.Thread.__init__(name='addTocListThread %d'%(self.ident))
		threading.Thread.__init__(self)
		self._id=id
		self.setName('atlt %d'%(self._id))
		self._file_name_iter=file_name_iter

	def run(self):
		for i in self._file_name_iter:
			s_print(self.getName()+'| file:',i)
			md_add_toc_list(i)

class threadList_c():
	def __init__(self,thread_c,cnt, *args, **kwargs):
		self.thread_list=[]
		for i in range(cnt):
			self.thread_list.append(thread_c(i,*args, **kwargs))
	def start(self):
		for i in self.thread_list:
			i.start()
	def join(self):
		for i in self.thread_list:
			i.join()


###############################################################################
##main
###############################################################################
too_many_file = 50
thread_cnt=3
#fsf = fileSubstrFliter_C(sys.argv[1:], '.md', too_many_file)
fsf = fileSubstrFliter_C('E:\\Users\\Desktop\\Note', '.md', too_many_file)
for i in fsf.md_list:
	s_print(i)

sfsf = secureIter_C(fsf.md_list)

toc_thread_list=threadList_c(addTocListThread_C,thread_cnt,sfsf)
toc_thread_list.start()
toc_thread_list.join()

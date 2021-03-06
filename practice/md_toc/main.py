# -*- coding: utf-8 -*-
import re
import chardet
import sys
import time
import os
import threading


def md_add_toc_list(fname):
	f = open(fname, 'rb')
	dect = chardet.detect(f.read())
	f.close()
	# s_print(threading.current_thread().getName() + \
	#		'|\033[1;36;m info \033[0m! ', dect)
	if dect['encoding'] is None or dect['confidence'] < 0.8:
		s_thindPrint(1, 'file detect fail:\n\t', fname, '\n\t', dect)
	# return
	f = open(fname, 'r+', encoding=dect['encoding'])
	dat = f.readlines()

	toc_start = None
	for i, sti in enumerate(dat):
		if re.match('^\s*\[toc\]\s*$', sti, re.I):
			toc_start = i
			break
	if toc_start is None:
		f.close()
		return
	cnt = 0
	for i in dat[toc_start + 1:]:
		if re.match('^\s*- \[[^\]]*\]\(#[^)]*\)$', i) == None:
			break
		cnt += 1
	empty_len = 0
	for i in dat[toc_start + cnt + 1:]:
		if re.match('^\s*$', i) == None:
			break
		empty_len += 1
	toc_end = None
	if toc_start + cnt + empty_len < len(dat) - 1:
		if re.match('^\s*\[tocend\]\s*$', dat[toc_start + cnt + empty_len + 1], re.I):
			toc_end = toc_start + cnt + empty_len + 1

	toc_list = []
	link_list=[]
	for i in dat:
		if re.match('#+ ', i):
			tli = i.split(' ', 1)
			hn = len(tli[0])
			hstr = tli[1].strip()
			link = link_modify = hstr.replace(' ', '-')
			mod_num = 0
			while link_modify in link_list:
				mod_num += 1
				link_modify = link + '-%d' % (mod_num)
			link_list .append(link_modify)
			toc_list.append('%s- [%s](#%s)\n' % ('  ' * hn, hstr, link_modify))

	f.seek(0, 0)
	f.writelines(dat[:toc_start])
	f.write('[TOC]\n')
	f.writelines(toc_list)
	f.write('\n[TOCEND]\n')
	if not toc_end:
		# f.write('\n')
		toc_end = toc_start
	f.writelines(dat[toc_end + 1:])
	f.truncate()
	f.close()


class fileSubstrFliter_C:
	def __init__(self, path_list, substr, filesmax):
		self._substr = substr.lower()
		self._filesmax = filesmax
		self.md_list = []
		self._exit = False
		if type(path_list) == type([]):
			pl = path_list
		elif type(path_list) == type(''):
			pl = [path_list]
		else:
			pl = []
		pl = [os.path.normpath(i) for i in pl]
		self._path_list_process(self.md_list, pl)

	def _is_subname(self, sti, subname):
		return os.path.isfile(sti) and os.path.splitext(sti)[1].lower() == subname

	def _path_list_process(self, md_list, path_list):
		if self._exit:
			return
		for i in path_list:
			if self._is_subname(i, self._substr):
				if len(md_list) >= self._filesmax:
					print(getInfoHead(2) + 'file is too many:', len(md_list))
					print('current file:', i)
					cont = input('Dou you wanna continue?(yes)')
					if cont == 'yes':
						self._filesmax += 500
					else:
						del md_list[:]
						self._exit = True
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
	def __init__(self, li=[]):
		self.lock = threading.Lock()
		self._it = iter(li)

	def __iter__(self):
		return self

	def __next__(self):
		self.lock.acquire()
		try:
			t = next(self._it)
		finally:
			self.lock.release()
		return t


class securefun_C():
	def __init__(self, fun):
		self._lock = threading.Lock()
		self._fun = fun

	def __call__(self, *args, **kwargs):
		self._lock.acquire()
		ret = self._fun(*args, **kwargs)
		self._lock.release()
		return ret


s_print = securefun_C(print)


def getInfoHead(itype):
	head_list = [
		'',
		'\033[1;36;m info \033[0m',
		'\033[1;32;m warning \033[0m',
		'\033[1;31;m error \033[0m'
	]
	if type(itype) != type(1) or itype not in range(len(head_list)):
		itype = 0
	return head_list[itype]


def s_thindPrint(head, *args, **kwargs):
	if type(head) != type(''):
		head = getInfoHead(head)
	s_print(threading.current_thread().getName() + head, *args, **kwargs)


class addTocListThread_C(threading.Thread):
	def __init__(self, id, file_name_iter):
		threading.Thread.__init__(self)
		self._id = id
		self.setName('atlt %d' % (self._id))
		self._file_name_iter = file_name_iter

	def run(self):
		for i in self._file_name_iter:
			s_print(self.getName() + '| file:', i)
			try:
				md_add_toc_list(i)
			except:
				for ei in sys.exc_info():
					s_thindPrint(3, ei)
				s_thindPrint(3, i)


class threadList_C():
	def __init__(self, thread_c, cnt, *args, **kwargs):
		self.thread_list = []
		for i in range(cnt):
			self.thread_list.append(thread_c(i, *args, **kwargs))

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
thread_cnt = 3
fsf = fileSubstrFliter_C(sys.argv[1:], '.md', too_many_file)
# fsf = fileSubstrFliter_C('E:\\Users\\Desktop\\test', '.md', too_many_file)
s_print('Markdowm file:', len(fsf.md_list))
for i in fsf.md_list:
	s_print(i)

s_print('add tod:')

sfsf = secureIter_C(fsf.md_list)

toc_thread_list = threadList_C(addTocListThread_C, thread_cnt, sfsf)
toc_thread_list.start()
toc_thread_list.join()

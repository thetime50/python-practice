# -*- coding: utf-8 -*-
import re
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
	def next(self):
		self.lock.acquire()
		try:
			t=next(self._it)
		finally:
			self.lock.release()
		return t

class securefun_C():
	pass
###############################################################################
##main
###############################################################################
too_many_file = 50
fsf = fileSubstrFliter_C(['E:/Users/Desktop/Atom'], '.md', too_many_file)
for i in fsf.md_list:
	print(i)

sfsf = secureIter_C(fsf.md_list)
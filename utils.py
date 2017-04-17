import sys;reload(sys);sys.setdefaultencoding('utf-8')
import common

def print_log(sth):
	with open(common.LOG_PATH, 'a') as f:
		map(f.write, sth)
		f.write('\n')
		f.close()

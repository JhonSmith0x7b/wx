import sys;reload(sys);sys.setdefaultencoding('utf-8')
import common

def print_log(str):
	with open(common.LOG_PATH, 'a') as f:
		f.write(str)
		f.close()
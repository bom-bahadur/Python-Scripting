#!/usr/bin/env python

'''
To define function named 'run_re()' with regular expession use cases. 
'''

import re

def run_re():
	pattern = 'pDq'
	infile = open('large_re_file.txt', 'r')
	match_count = 0
	lines = 0
	for line in infile:
		match = re.search(pattern, line)
		if match:
			match_count += 1
		lines += 1
	return (lines, match_count)

if __name__ == "__main__":
	lines, match_count = run_re()
	print 'LINES::', lines
	print 'MATCHES::', match_count

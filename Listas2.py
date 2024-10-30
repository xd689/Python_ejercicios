#!/usr/bin/env python
# -*- coding: utf-8 -*-
def main(args):
	a=[]
	a.insert(0, input("Dame la asignatura 1: "))
	a.insert(1, input("Dame la asignatura 2: "))
	a.insert(2, input("Dame la asignatura 3: "))
	a.insert(3, input("Dame la asignatura 4: "))
	a.insert(4, input("Dame la asignatura 5: "))
	a.sort()
	print(a)
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
	from decimal import Decimal
	a=[("Lengua", Decimal('8.5')),("Mates", Decimal('6.7')),("Ciencia", Decimal('9.85')),("Historia", Decimal('7.3')),("Física", Decimal('6.5'))]
	i= a.sort()
	print("LAS ASIGNATURAS INTRODUCIDAS CON SUS NOTAS\n")
	print("==========================================\n")
	for i in a:
		print(i)
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))

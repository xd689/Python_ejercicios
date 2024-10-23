def main(args):
	namekiano=(" Bardocka "," Vergetta "," Son Gohanda "," Gokú ")
	for i in range(len(namekiano)):
		padre=namekiano[i]
		for j in range(len(padre)):
			rey=padre[j]
			for k in range(len(rey)):
				print(rey[k])
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

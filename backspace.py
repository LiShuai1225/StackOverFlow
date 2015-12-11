#http://stackoverflow.com/questions/34217871/why-print-1-x08-results-1-meanwhile-print-1-x082-results-2/34218873#34218873
#2015/12/11 16:25:21
if __name__ == "__main__":
	print "1\x08"
	print "1\x082"

	f = open("1.txt", "w")
	f.write("1\x08\x082")
	f.close();

	f = open("1.txt", "r")
	str = f.readlines( )
	print len(str), str
	for s in str:
		print "s=|" + s + "|"
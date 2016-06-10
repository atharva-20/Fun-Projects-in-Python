
import requests


book_number = ["%03d" % i for i in range(2,101)]   											#Because the names were grammar001 instead of grammar1

print " \n \n 	This code is used to download pdf from the specified website"
print "\n"

for number in book_number: 																	#Every book from 001 to 100
	links = ['http://harry.dw.com/resources/pdf/grammar/en/grammar'+str(number)+'.pdf']		#Put your uniform URL here.

	print "Downloading book: " + str(number) + " ...... ",
	for link in links:
		book_name = link.split('/')[-1]														#Take the book name from the URL itself by listing last item
		
		with open(book_name, 'wb') as book:													#Open book with name in write-binary
			a = requests.get(link, stream=True)												#Requests 

			for block in a.iter_content(512):												#Block here indicates chunck of data, if available write or
				if not block:																#be left alone.
					break

				book.write(block)

	print"complete \n"
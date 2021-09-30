
def encrypt_file(filename,output_file):
	try:
		f = open(filename, 'r')
		words = []
		words = f.read().split("\n")
		f.close()
		reversed_words = []
		for word in words:
			reversed_word = ""
			for i in reversed(range(len(word))):
				reversed_word += word[i]
			reversed_words.append(reversed_word)
		return reversed_words
		try:
			r = open(output_file, 'w')
			for i in reversed_words:
				enc = i + "\n"
				r.write(enc)
			r.close()
		except:
			print("Проверьте правильность написания названия файла: "+output_file)
	except:
		print("Проверьте правильность написания названия файла: "+filename)

encrypt_file("worsds.txt","words_ecrypted.txt")

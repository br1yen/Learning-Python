def enigma(input, output, mode):
	encrypt = str.maketrans('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz','EeCcDdFfIiGgKkZzOoLlMmNnPpXxUuQqRrVvTtJjAaWwYyBbHhSs')
	decrypt = str.maketrans('EeCcDdFfIiGgKkZzOoLlMmNnPpXxUuQqRrVvTtJjAaWwYyBbHhSs','AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz')
	infile = open(input, 'r')
	outfile = open(output, 'w')
	lines = 0
	words = 0
	chars = 0
	if mode == 0:
		for line in infile:
			lines += 1
			words += len(line.split())
			chars += len(line.replace("\n",""))
			translated = line.translate(encrypt)
			outfile.write(translated)
		print("Your encrypted file is available in: " + output)
	elif mode == 1:
		for line in infile:
			lines += 1
			words += len(line.split())
			chars += len(line.replace("\n",""))
			translated = line.translate(decrypt)
			outfile.write(translated)
		print("Your decrypted file is available in: " + output)
	else:
		print("Input a proper number for operation.")
	infile.close()
	outfile.close()
	return(lines, words, chars)
	
input_path = input('What is the path of your original file? ')
output_path = input('Where do you want your new file? ')
user_mode = eval(input('If you are encrypting a file, type 0, but if you are decrypting a file, type 1: '))

l,w,c = enigma(input_path, output_path, user_mode)
print(f'Your original file has {l} line(s), {w} word(s), and {c} character(s).')




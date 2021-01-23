file = open("Monkey.obj", "r");
file.readline();
file.readline();
file.readline();
file.readline();
for linea in file:
	linea = linea.split();
	if linea[0] == 'v':
		print linea;
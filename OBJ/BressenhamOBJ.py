#Miranda Higuera Isaac Uriel
import math;
def setPixel(x, y, red, green, blue):
	pixeles[int(y)][int(x)] = [red,green,blue];
	return;
def makeFile(nombre):
	file = open(nombre,"wb+");
	file.write(header);
	for y in pixeles:
		for red,green,blue in y:
			file.write(b"%c%c%c"%(red,green,blue));
	file.close();
	return;
def leerVertices(archivo):
	file = open(archivo, "r");
	vertices = list();
	for linea in file:
		linea = linea.split();
		if linea[0] == "v":
			vertices.append([float(linea[1]),float(linea[2]),float(linea[3])]);
	file.close();
	return vertices;
def leerCaras(archivo):
	file = open(archivo, "r");
	caras = list();
	cara = list();
	for linea in file:
		linea = linea.split();
		if linea[0] == "f":
			linea.pop(0);
			for vertice in linea:
				vertice = vertice.split("/");
				cara.append(int(vertice[0]));
			caras.append(cara);
			cara = [];
	file.close();
	return caras;
def drawLine(x1, y1, x2, y2, red, green, blue):
	setPixel(x1,y1, red, green, blue);
	setPixel(x2,y2, red, green, blue);
	if x1>x2:
		k=x2;
		x2=x1;
		x1=k;
		k=y2;
		y2=y1;
		y1=k;
	if y2>=y1 and x2>=x1:		
		x=x1;
		y=y1;
		dx = abs(x2-x1);#250
		dy = abs(y2-y1);#250
		#dx = 1000, dy = 500
		if dx>=dy:
			avR = 2*dy;#1000
			avI=2*dy-2*dx;#-1000
			p = 2*dy-dx;#0
			while x<x2:
				if p<0:#F
					x+=1;#
					p=p+avR;
				else:
					x+=1;
					y+=1;
					p+=avI;
				setPixel(x,y,red, green, blue);
		elif dy>dx:
			avR = 2*dx;#1000
			avI=2*dx-2*dy;#-1000
			p = 2*dx-dy;#0
			while y<y2:#0
				if p<0:#F
					y+=1;
					p+=avR;
				else:
					x+=1;#1
					y+=1;#1
					p+=avI;#
				setPixel(x,y,red, green, blue);
	elif y1>y2 and x2>=x1:#1-1, 750,250
		x=x1;
		y=y1;
		dx = abs(x2-x1);
		dy = abs(y2-y1);
		if dx>=dy:
			avR = 2*dy;#1000
			avI=2*dy-2*dx;#-1000
			p = 2*dy-dx;#0
			while x<x2:
				if p<0:#F
					x+=1;#
					p=p+avR;
				else:
					x+=1;
					y-=1;
					p+=avI;
				setPixel(x,y,red, green, blue);
		elif dy>dx:
			avR = 2*dx;#1000
			avI=2*dx-2*dy;#-1000
			p = 2*dx-dy;#0
			while y>=y2:#0
				if p<0:#F
					y-=1;
					p+=avR;
				else:
					x+=1;#1
					y-=1;#1
					p+=avI;#
				setPixel(x,y,red, green, blue);
	return;
def makePositive(vertices):
	minX = 0;
	minY = 0;
	minZ = 0;
	maxX= 0;
	maxY = 0;
	maxZ = 0;
	for x,y,z in vertices:
		if x>maxX:
			maxX = x;
		if x<minX:
			minX = x;
		if y>maxY:
			maxY = y;
		if y<minY:
			minY = y;
		if z>maxZ:
			maxZ = z;
		if z<minZ:
			minZ = z;
	for v in vertices:
		v[0]+=abs(minX);
		v[1]+=abs(minY);
		v[2]+=abs(minZ);
	return vertices;
def getMaxFactor(vertices):
	minX = 0;
	minY = 0;
	minZ = 0;
	maxX= 0;
	maxY = 0;
	maxZ = 0;
	for x,y,z in vertices:
		if x>maxX:
			maxX = x;
		if x<minX:
			minX = x;
		if y>maxY:
			maxY = y;
		if y<minY:
			minY = y;
		if z>maxZ:
			maxZ = z;
		if z<minZ:
			minZ = z;
	maxDefinitivo = maxX;
	if maxY > maxDefinitivo: maxDefinitivo = maxY;
	if maxZ > maxDefinitivo: maxDefinitivo = maxZ;
	maxFactor  = math.floor(1080/maxDefinitivo);
	return maxFactor;
def adjustSize(vertices):
	maxFactor = getMaxFactor(vertices);
	for v in vertices:
		v[0]=int(round(v[0]*maxFactor));
		v[1]=int(round(v[1]*maxFactor));
		v[2]=int(round(v[2]*maxFactor));
	return vertices;
def scalate(vertices, factor):
	maxFactor = getMaxFactor(vertices)
	if factor<=maxFactor:
		for v in vertices:
			v[0]=int(round(v[0]*factor));
			v[1]=int(round(v[1]*factor));
			v[2]=int(round(v[2]*factor));
	return vertices;
def translate(vertices, xt, yt, zt):
	for x,y,z in vertices:
		if x+xt<0 or y+yt<0 or z+zt<0:
			print("Translation out of index;");
			return;
	for vertice in vertices:
		vertice[0]+=xt;
		vertice[1]+=yt;
		vertice[2]+=zt;
	return vertices;
def center(vertices):
	minX = 0;
	minY = 0;
	minZ = 0;
	maxX= 0;
	maxY = 0;
	maxZ = 0;
	for x,y,z in vertices:
		if x>maxX:
			maxX = x;
		if x<minX:
			minX = x;
		if y>maxY:
			maxY = y;
		if y<minY:
			minY = y;
		if z>maxZ:
			maxZ = z;
		if z<minZ:
			minZ = z;
	medioX = minX + ((maxX-minX)/2);
	medioY = minY + ((maxY-minY)/2);
	medioZ = minZ + ((maxZ-minZ)/2);
	vertices = translate(vertices, 959-medioX, 539-medioY, 539-medioZ);
	#Para X,Y X=1920 Y=1080
	#Para Z,Y Z=1920 y=1080
	#Para X,Z X=1920 Z=1080
	return vertices;
def graficarXY(caras):
	for cara in caras:
		v1=(cara[0]-1);
		v2=(cara[(len(cara)-1)]-1);
		drawLine(vertices[v1][0],vertices[v1][1],vertices[v2][0],vertices[v2][1],255,255,255);
		i=0;
		while i < (len(cara)-1):
			v1=(cara[i]-1);
			v2=(cara[i+1]-1);
			drawLine(vertices[v1][0],vertices[v1][1],vertices[v2][0],vertices[v2][1],255,255,255);
			i+=1;
	return;
def graficarZY(caras):
	for cara in caras:
		v1=(cara[0]-1);
		v2=(cara[(len(cara)-1)]-1);
		drawLine(vertices[v1][2],vertices[v1][1],vertices[v2][2],vertices[v2][1],255,255,255);
		i=0;
		while i < (len(cara)-1):
			v1=(cara[i]-1);
			v2=(cara[i+1]-1);
			drawLine(vertices[v1][2],vertices[v1][1],vertices[v2][2],vertices[v2][1],255,255,255);
			i+=1;
	return;	
def graficarZX(caras):
	for cara in caras:
		v1=(cara[0]-1);
		v2=(cara[(len(cara)-1)]-1);
		drawLine(vertices[v1][0],vertices[v1][2],vertices[v2][0],vertices[v2][2],255,255,255);
		i=0;
		while i < (len(cara)-1):
			v1=(cara[i]-1);
			v2=(cara[i+1]-1);
			drawLine(vertices[v1][0],vertices[v1][2],vertices[v2][0],vertices[v2][2],255,255,255);
			i+=1;
	return;
height = 1080;
width = 1920;
archivo = "cow-nonormals.obj";
header = "P6\n "+str(width)+" "+str(height)+"\n255\n";
pixeles = [[[0,0,0] for x in xrange(width)]for y  in xrange(height)];
vertices = leerVertices(archivo);
vertices = makePositive(vertices);
vertices = adjustSize(vertices);
vertices = center(vertices);
caras = leerCaras(archivo);
graficarXY(caras);
makeFile("cowXY.ppm");
pixeles = [[[0,0,0] for x in xrange(width)]for y  in xrange(height)];
graficarZY(caras);
makeFile("cowZY.ppm");
pixeles = [[[0,0,0] for x in xrange(width)]for y  in xrange(height)];
graficarZX(caras);
makeFile("cowZX.ppm");
def setPixel(x, y, red, green, blue):
	pixeles[int(y)][int(x)] = [red,green,blue];
	return;
def makeFile():
	file = open("BresenhamFHD.ppm","wb+");
	file.write(header);
	for y in pixeles:
		for red,green,blue in y:
			file.write("%c%c%c"%(red,green,blue));
	file.close();
	return;
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
		print(dx,dy);
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
			print
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
height = 1080;
width = 1920;
header = "P6\n "+str(width)+" "+str(height)+"\n255\n";
pixeles = [[[0,0,0] for x in xrange(width)]for y  in xrange(height)];
#Lineas para formar octeto
drawLine(500,500,750,0,255,87,51);
drawLine(500,500,1000,250,215,189,226);
drawLine(500,500,1000,750,255,255,255);
drawLine(500,500,750,1000,255,255,255);
drawLine(500,500,250,1000,255,87,51);
drawLine(500,500,0,750,215,189,226);
drawLine(500,500,0,250,255,255,255);
drawLine(500,500,250,0,255,255,255);
#Lineas formando octagono
drawLine(250,1,750,1,255,87,51);
drawLine(750,0,1000,250,215,189,226);
drawLine(1000,250,1000,750,84,153,199);
drawLine(1000,750,750,1000,25,188,156);
drawLine(750,1000,250,1000,255,255,255);
drawLine(250,1000,0,750,255,255,255);
drawLine(1,750,1,250,255,255,255);
drawLine(0,250,250,0,255,255,255);
makeFile();
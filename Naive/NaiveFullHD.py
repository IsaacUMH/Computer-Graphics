def setPixel(x, y, red, green, blue):
	pixeles[int(y)][int(x)] = [red,green,blue];
	return;
def drawLine(x1, y1, x2, y2, red, green, blue):
	if y2<=y1 and x1>x2:
		aux = y2;
		y2 = y1;
		y1 = aux;
		aux = x2;
		x2 = x1;
		x1 = aux;
	elif y2>=y1 and x1>x2:
		aux = y2;
		y2 = y1;
		y1 = aux;
		aux = x2;
		x2 = x1;
		x1 = aux;
	if y2>=y1 and x2>=x1:
		if x2==x1:
			m=1000000;
		else:
			m = float(y2-y1)/float(x2-x1);
		if m<=1 and m>=0:
			x=x1;
			while (x<=x2):
				y=round(x*m)+(y1-m*x1);
				setPixel(x,y,red,green,blue);
				x+=1;	
			return;
		elif m>1:
			y = y1;
			while(y<=y2):
				x=round(y/m) + (x1-y1/m);
				setPixel(x,y,red,green,blue);
				y+=1;	
			return;
	elif(y1>=y2 and x2>=x1):
		if x1==x2:
			m=-1000000;
		else:
			m = (float(y2-y1)/float(x2-x1));
		if m>=-1 and m<0:
			x=x1;
			while (x<=x2):
				y=round(x*m)+(y1-m*x1);
				setPixel(x,y,red,green,blue);
				x+=1;	
			return;
		elif m<(-1):
			y = y1;
			while(y>=y2):
				x=round(y/m) + (x1-y1/m);
				setPixel(x,y,red,green,blue);
				y-=1;	
			return;

def makeFile():
	file = open("NaiveFHD.ppm","wb+");
	file.write(header);
	for y in pixeles:
		for red,green,blue in y:
			file.write("%c%c%c"%(red,green,blue));
	file.close();
	return;
height = 1080;
width = 1920;
header = "P6\n "+str(width)+" "+str(height)+"\n255\n";
pixeles = [[[0,0,0] for x in xrange(width)]for y  in xrange(height)];
drawLine(250,1,750,1,255,87,51);
drawLine(750,0,1000,250,215,189,226);
drawLine(1000,250,1000,750,84,153,199);
drawLine(1000,750,750,1000,25,188,156);
drawLine(750,1000,250,1000,255,255,255);
drawLine(250,1000,0,750,255,255,255);
drawLine(1,750,1,250,255,255,255);
drawLine(0,250,250,0,255,255,255);
makeFile();
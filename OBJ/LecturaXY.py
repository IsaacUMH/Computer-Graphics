file = open("Monkey.obj", "r");
file.readline();
file.readline();
file.readline();
file.readline();
vertices = list();
for linea in file:
	linea = linea.split();
	if linea[0] == "v":
		vertices.append([float(linea[1]),float(linea[2]),float(linea[3])]);
file.close();
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
factorMultiplicativo  = round (1080/maxDefinitivo);
for v in vertices:
	v[0]=int(round(v[0]*factorMultiplicativo));
	v[1]=int(round(v[1]*factorMultiplicativo));
	v[2]=int(round(v[2]*factorMultiplicativo));
print (len(vertices[0]));
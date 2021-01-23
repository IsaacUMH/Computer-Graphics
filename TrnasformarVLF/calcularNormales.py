#Miranda Higuera Isaac Uriel
import struct;
def leerVLF(archivo):
	file = open(archivo, "rb");
	vertices = list();
	edges = list();
	triangulos = list();
	linea = file.readline().split();
	i=0;
	while i<int(linea[0]):
		x = struct.unpack('f',file.read(4))[0];
		y = struct.unpack('f',file.read(4))[0];
		z = struct.unpack('f',file.read(4))[0];
		vertices.append([x,y,z])
		i+=1;
	
	i=0;
	while i<int(linea[1]):
		ini = struct.unpack('i',file.read(4))[0];
		fin = struct.unpack('i',file.read(4))[0];
		edges.append([ini,fin]);
		i+=1;

	i=0;
	while i<int(linea[2]):
		e1 = struct.unpack('i',file.read(4))[0];
		e2 = struct.unpack('i',file.read(4))[0];
		e3 = struct.unpack('i',file.read(4))[0];
		triangulos.append([e1,e2,e3]);
		i+=1;
	
	datos = [vertices,edges,triangulos];
	return datos;
def calcularNormales(triangulos, edges, vertices):
	normales = list();
	for triangulo in triangulos:
		#A va a ser igual al vector1 menos el vector0
		#B va a ser igual al vector2 menos el vector1
		e0 = edges[triangulo[0]];
		e1 = edges[triangulo[1]];
		v0 = vertices[e0[0]-1]
		v1 = vertices[e0[1]-1]
		v2 = vertices[e1[0]-1]
		v3 = vertices[e1[1]-1]
		A = [v1[0]-v0[0],v1[1]-v0[1],v1[2]-v0[2]];
		B = [v3[0]-v2[0],v3[1]-v2[1],v3[2]-v2[2]];
		i=0;
		j=1;
		k=2;
		normal = [(A[j]*B[k]-A[k]*B[j]),A[k]*B[i]-A[i]*B[k],A[i]*B[j]-A[j]*B[i]];
		normales.append(normal);
	return normales;
archivo = "Monkey.vlf"
datos = leerVLF(archivo);
vertices = datos[0];
edges = datos[1];
triangulos = datos[2];
normales=calcularNormales(triangulos, edges, vertices);
print (normales);
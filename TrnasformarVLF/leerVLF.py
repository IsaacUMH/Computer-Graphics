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
archivo = "Monkey.vlf"
datos = leerVLF(archivo);
vertices = datos[0];
edges = datos[1];
triangulos = datos[2];
print (vertices);
print (edges);
print (triangulos);
#Miranda Higuera Isaac Uriel
import math;
import struct;
import sys;
def escribirArchivo(archivo, vertices,edges,triangulos):
	file = open(archivo, "w+");
	i=0;
	file.write("%s %s %s\n" % (len(vertices),len(edges),len(triangulos)));
	for vertice in vertices:
		file.write("%s\n"%(vertice));
	for edge in edges:
		file.write("%s\n"%(edge));
	for triangulo in triangulos:
		file.write("%s\n"%(triangulo));
	file.close();
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
def obtenerEdges(caras):
	edge = list();
	edges = list();
	coordenadas = list();
	for cara in caras:#Aqui recupero cada cara
		#edges va a contener el indice de cada par de vertices que se unen.
		edge = [];
		edge.append(cara[len(cara)-1]);
		edge.append(cara[0]);
		edges.append(edge);
		i = 0;
		while i<(len(cara)-1):
			edge = [];
			edge.append(cara[i]);
			edge.append(cara[i+1]);
			edges.append(edge);
			i+=1;
	return edges;
def transformarCaras(caras):#El objetivo de esta funcion es convertir caras de poligonos en triangulos
	triangulos = list();
	trinagulo = list();
	for cara in caras:
		if len(cara)>3:
			i=0;
			while i<(len(cara)-2):
				triangulo = [];
				triangulo.append(cara[0])
				triangulo.append(cara[i+1]);
				triangulo.append(cara[i+2]);
				triangulos.append(triangulo);
				i+=1;
		else:
			triangulos.append(triangulo);
	return triangulos;
def calcularNormales(caras,vertices):
	normales = list();
	for cara in caras:
		#A va a ser igual al vector1 menos el vector0
		#B va a ser igual al vector2 menos el vector1
		p0 = vertices[cara[0]-1];
		p1 = vertices[cara[1]-1];
		p2 = vertices[cara[2]-1];
		i=0;
		j=1;
		k=2;
		A = [p1[i]-p0[i],p1[j]-p0[j],p1[k]-p0[k]]
		B = [p2[i]-p0[i],p2[j]-p0[j],p2[k]-p0[k]]
		normal = [(A[j]*B[k]-A[k]*B[j]),A[k]*B[i]-A[i]*B[k],A[i]*B[j]-A[j]*B[i]];
		normales.append(normal);
	return normales;
def asignarEdges(edges):
	triangulos = list();
	triangulo = list();
	i = 0;
	while i<len(edges)/3:
		j=0;
		triangulo = [];
		while j<3:
			triangulo.append(i*3+j)
			j+=1;
		triangulos.append(triangulo);
		i+=1;
	return triangulos;
archivo = "Monkey.obj";
vlf = "Monkey.txt";
caras = leerCaras(archivo);
caras = transformarCaras(caras);
vertices = leerVertices(archivo);
edges = obtenerEdges(caras);
triangulos = asignarEdges(edges);
escribirArchivo(vlf,vertices, edges,triangulos);
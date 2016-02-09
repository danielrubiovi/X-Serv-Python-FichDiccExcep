#!/usr/bin/python
# -*- coding: utf-8 -*-

fich = open ("/etc/passwd", 'r')
lineas = fich.readlines()
dicc = {}

for line in lineas:
	lista_lineas = line.split(':')
	clave = lista_lineas[0]
	valor_shell = lista_lineas[-1][:-1]
	dicc[clave] = valor_shell
print "El valor de 'root':", dicc['root']

try:
	print "El valor de 'imaginario':", dicc['imaginario']
except KeyError:
	print "Clave no encontrada en la biblioteca"

print "\nNumero de lineas:", len(lineas)

	


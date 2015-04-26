__author__ = 'kevin'

class nodoB(object):
	def __init__(self):
		self.ramas = [None, None, None, None, None]
		self.carpetas = [None, None, None, None]
		self.size = 0

class carpeta(object):
	def __init__(self, nombre):
		self.nombre = nombre
		self.arbol = arbolB()

class arbolB(object):
	def __init__(self):
		self.raiz = None

	def vacio(self, raiz):
		return raiz==None


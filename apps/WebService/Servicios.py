__author__ = 'kevin'

class nodoUsuarios(object):
	def __init__(self, email, password):
		self.email = email
		self.password = password
		self.sig = None
		self.ant = None

class listaUsuarios(object):
	def __init__(self, cabeza=None, cola=None):
		self.cabeza = cabeza
		self.cola = cola

	def insertar(self, email, password):
		nodo = nodoUsuarios(email, password)
		if self.cabeza==None:
			self.cabeza = nodo
			self.cola = nodo
		else:
			self.cola.sig = nodo
			nodo.ant = self.cola
			self.cola = nodo

	def getCabeza(self):
		return self.cabeza

	def login(self, nodo, email, password):
		if nodo != None :
			if (nodo.email == email) and (nodo.password == password):
				return True
			else:
				self.login(nodo.sig, email, password)
		return False

	def obtenerNodo(self, nodo, email, password):
		if nodo != None:
			if (nodo.email == email) and (nodo.password == password):
				return nodo
			else:
				self.login(nodo.sig, email, password)
		return None

	def diagrama(self):
		return  "digraph G {" + self.grphviz(self.cabeza)+"}"

	def grphviz(self, nodo):
		text = ""
		if nodo != None:
			text = text + "u"+nodo.email.replace("@", "").replace(".", "")+" [label = \""+nodo.email+"\" ] ;" + self.grphviz(nodo.sig)
			if nodo.sig != None:
				text = text + "u"+nodo.email.replace("@", "").replace(".", "")+"->u"+nodo.sig.email.replace("@", "").replace(".", "")+";"
			if nodo.ant != None:
				text = text + "u"+nodo.email.replace("@", "").replace(".", "")+"->u"+nodo.ant.email.replace("@", "").replace(".", "")+";"
		return text

lista = listaUsuarios()

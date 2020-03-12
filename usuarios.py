from pickle import *

FILE_PATH = "usuarios.txt"

def buscar(list, filter):
    for x in list:
        if filter(x):
            return x
    return False

class Usuario:
	def __init__(self, correo: str, pwd: str, nombre: str, apellido: str, admin: bool):
		self.correo = correo
		self.pwd = pwd
		self.nombre = nombre
		self.apellido = apellido
		self.admin = admin

def leerUsuarios():
	try:
		f = open(FILE_PATH,"rb")
		return load(f)
	except:
		return [
			Usuario("admin@admin.com", "1234", "admin", "admin", True)
		]
	
def registrarUsuario(usuario, usuarios):
	usuarios.append(usuario)
	guardarUsuarios(usuarios)
	return usuario
	
	
def guardarUsuarios(usuarios):
	f = open(FILE_PATH,"wb")
	dump(usuarios, f)

def login(correo: str, pwd: str):
	return buscar(leerUsuarios(), lambda usuario: usuario.correo == correo and usuario.pwd == pwd)

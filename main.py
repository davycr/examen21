import usuarios as _usuarios
import calculadora
import os

def cls():
	os.system('cls')

def registrar():
	cls()
	
	usuarios = _usuarios.leerUsuarios()
	
	nombre = input("Ingrese su nombre: ")
	apellido = input("Ingrese su apellido: ")
	correo = input("Ingrese su correo: ")
	while _usuarios.buscar(usuarios, lambda u: u.correo == correo):
		correo = input("Ya existe un usuario con ese correo, intente nuevamente: ")
	pwd = input("Ingrese su contraseña: ")
	
	nuevo = _usuarios.Usuario(correo, pwd, nombre, apellido, False)
	
	_usuarios.registrarUsuario(nuevo, usuarios)
	return nuevo
	
def verUsuarios():
	cls()
	for index, usuario in enumerate(_usuarios.leerUsuarios()):
		print("%i.- %s %s - %s" % (index, usuario.nombre, usuario.apellido, usuario.correo))
	print()
	input("Ingrese una tecla para continuar...")
	
def login():
	cls()
	
	usuarios = _usuarios.leerUsuarios()
	
	correo = input("Ingrese su correo: ")
	pwd = input("Ingrese su contraseña: ")
	
	usuario = _usuarios.login(correo, pwd)
	
	if not usuario:
		print()
		input("¡No existe un usuario con esos datos!")
	
	return usuario

def main():
	salir = False
	usuario = False
	while not salir:
		cls()
		
		if usuario:
			print("¡Bienvenido, %s %s!" % (usuario.nombre, usuario.apellido) )
			print("1.- Calculadora")
			print("2.- Cerrar sesión")
		else:
			print("¡Bienvenido!")
			print("1.- Registrarse")
			print("2.- Iniciar sesión")
		if usuario and usuario.admin:
			print("3.- Ver usuarios")
			print("4.- Salir")
		else:
			print("3.- Salir")
		print()
		opcion = int(input("Ingrese una opción: "))
		if opcion == 1:
			if usuario:
				calculadora.main()
			else:
				usuario = registrar()
		elif opcion == 2:
			if usuario:
				usuario = False
			else:
				usuario = login()
		elif opcion == 3:
			if usuario and usuario.admin:
				verUsuarios()
			else:
				salir = False
				break
		elif opcion == 4:
			if usuario and usuario.admin:
				salir = False
				break
	
	return 0

if __name__ == '__main__':
	main()

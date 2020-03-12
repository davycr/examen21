from main import cls

def sumar(x, y):
   return x + y
   
def restar(x, y):
   return x - y
   
def multiplicar(x, y):
   return x * y
   
def dividir(x, y):
   return x / y

def main():
	salir = False
	while not salir:
		cls()
		print("Operaciones:")
		print()
		print("1.- Suma")
		print("2.- Resta")
		print("3.- Multiplicacion")
		print("4.- Division")
		print()
		print("5.- Salir")
		print

		opcion = input("Elige una operacion: ")
		
		if opcion == '5':
			salir = True
			break
			
		
		print()

		num1 = int(input("Primer numero: "))
		num2 = int(input("Segundo numero: "))
		
		print()
		
		if opcion == '1':
			print(num1, "+" ,num2, "=", sumar(num1, num2))
		elif opcion == '2':
			print(num1, "-", num2, "=", restar(num1, num2))
		elif opcion == '3':
			print(num1, "*", num2, "=", multiplicar(num1, num2))
		elif opcion == '4':
			try:
				print(num1, "/", num2, "=", dividir(num1, num2))
			except:
				print("No se puede dividir entre 0.")
		else:
			print("Ingrese una operación válida.")	
		input()


from os import link
from single_linked_list import SingleLinkedList as SLL
from double_linked_list import DoubleLinkedList as DLL
from colorama import*

init()

def input_integer(mensaje):
    while True:
        try:
            integer = int(input(mensaje))
            return integer
        except:
            print('Se esperaba un valor numerico')

def insert_menu(linked_list):
    while True:
        print(Fore.GREEN + '1. Al inicio\n2. Al final\n3. En una posición especifica\n')
        choose = input_integer('--> ')
        value = input_integer('Insertar con valor? --> ')
        if choose == 1:
            print(linked_list.unshift(value))
            break
        elif choose == 2:
            print(linked_list.push_back(value))
            break
        elif choose == 3:
            index = input_integer('Insertar nodo en la posición? --> ')
            print(linked_list.insert_node(index, value))
            break
        else:
            print(Fore.RED + 'Opcion invalida, por favor vuelve a ingresar una opción\n')

def remove_menu(linked_list):
    while True:
        print(Fore.GREEN + '1. Al inicio\n2. Al final\n3. En una posición especifica\n')
        choose = input_integer('--> ')
        if choose == 1:
            print(linked_list.shift_node())
            break
        elif choose == 2:
            print(linked_list.pop_node())
            break
        elif choose == 3:
            index = input_integer('Eliminar nodo en la posición? --> ')
            print(linked_list.remove_node(index))
            break
        else:
            print(Fore.RED + 'Opcion invalida, por favor vuelve a ingresar una opción\n')

def validation_menu(linked_list):
    while True:
        print(Fore.GREEN + '1. Punto 5\n2. Punto 6\n')
        choose = input_integer('--> ')
        if choose == 1:
            if isinstance(linked_list,DLL):
                index = input_integer('Actualizar posicion? --> ')
                value = input_integer('Actualizar con valor? --> ')
                print(linked_list.update_value_square(index,value))
            else:
                print(Fore.RED + 'Opcion no disponible para listas simples')
            break
        elif choose == 2:
            linked_list.especial_reverse()  
            linked_list.print_values()
            break
        else:
            print(Fore.RED + 'Opcion invalida, por favor vuelve a ingresar una opción\n')



def sub_menu(linked_list):
    print(Fore.GREEN + 'Ingresa por consola la letra que corresponda según la opción a elegir:\n')
    while True:
        print(Fore.GREEN + 'a. Añadir nodo\nb. Eliminar nodo\nc. Consultar valor contenido en el nodo\nd. Modificar valor de nodo\ne. Invertir toda la lista\nf. Validación especial\ng. imprimir lista\nh. Volver\n')
        choose = input('--> ')
        if choose == 'a':
            insert_menu(linked_list)
            input()
        elif choose == 'b':
            remove_menu(linked_list)
            input()
        elif choose == 'c':
            index = input_integer('consultar valor en la posicion? --> ')
            print(linked_list.get_value_at(index))
            input()
        elif choose == 'd':
            index = input_integer('Cambiar valor en la posicion? --> ')
            new_value = input_integer('nuevo valor? --> ')
            print(linked_list.update_value(index,new_value))
            input()
        elif choose == 'e':
            linked_list.reverse()
            linked_list.print_values()
            input()  
        elif choose == 'f':
            validation_menu(linked_list)
            input()
        elif choose == 'g':
            linked_list.print_values()
            input()
        elif choose == 'h':
            print('\n\n')
            display_menu()
            break
        else:
            print(Fore.RED + 'Opcion invalida, por favor vuelve a ingresar una opción\n')
            input()


def display_menu():

    print(Fore.BLUE + '\n\n\t\tBienvenido al menu de linked list!\n\n')
    print(Fore.WHITE + 'Ingresa por consola la letra que corresponda según la opción a elegir:\n')
    print(Fore.RED + 'a. Listas simplemente enlazadas\nb. Listas doblemente enlazadas\nc. Salir (cancela la ejecución del programa)\n')
    while True:
        choose = input('--> ')
        if choose == 'a':
            single_linked_list = SLL()
            sub_menu(single_linked_list)
            break
        elif choose == 'b':
            double_linked_list = DLL()
            sub_menu(double_linked_list)
            break
        elif choose == 'c':
            print(Fore.WHITE + 'Esos es todo entonces, Hasta luego!')
            break
        else:
            print(Fore.RED + 'Opcion invalida, por favor vuelve a ingresar una opción\n')
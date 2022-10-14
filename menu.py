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



def sub_menu(linked_list):
    print(Fore.GREEN + 'Ingresa por consola la letra que corresponda según la opción a elegir:\n')
    while True:
        print('a. Añadir nodo\nb. Eliminar nodo\nc. Consultar valor contenido en el nodo\nd. Modificar valor de nodo\ne. Invertir toda la lista\nf. Validación especial\ng. salir\n')
        choose = input('--> ')
        if choose == 'a':
            index = input_integer('Insertar nodo en la posición? --> ')
            value = input_integer('Insertar con valor? --> ')
            linked_list.insert_node(index, value)
            input()
        elif choose == 'b':
            index = input_integer('Eliminar en la posición? --> ')
            linked_list.remove_node(index)
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
            print(Fore.RED + 'Opcion disponible en proximas versiones')
            input()
        elif choose == 'g':
            print(Fore.WHITE + 'Esos es todo entonces, Hasta luego!')
            break
        else:
            print(Fore.RED + 'Opcion invalida, por favor vuelve a ingrasar una opción\n')
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
            print(Fore.RED + 'Opcion invalida, por favor vuelve a ingrasar una opción\n')
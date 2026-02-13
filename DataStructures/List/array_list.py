def new_list():
# Crea una lista en forma de diccionario.
    newlist= { 
            'elements': [],
            'size': 0,
            }
    return newlist

def get_element(my_list, index):
# Devuelve el elemento en la posición dada por index.
        return my_list['elements'][index]

def is_present(my_list, element, cmp_function):

    size = my_list["size"]
    if size > 0:
        for keypos in range(0, size):
            info = my_list["elements"][keypos]

            if cmp_function(element, info) == 0:
                return keypos
    return -1
 
def add_first(my_list, element):
        
        my_list['elements'].insert(0, element)
        my_list['size'] += 1
        return my_list

def add_last(my_list, element):
        
        my_list['elements'].append(element)
        my_list['size'] += 1
        return my_list

def size(my_list):
        return my_list['size']

def first_element(my_list):
        
    if my_list["size"] == 0:
        return None
    return my_list["elements"][0]

def is_empty(my_list):
        
    return my_list["size"] == 0

def last_element(my_list):
        
    if my_list["size"] == 0:
        return None
    return my_list["elements"][my_list["size"] - 1]

def delete_element(my_list, index):
        
    if index >= 0 and index < my_list["size"]:
        my_list["elements"].pop(index)
        my_list["size"] -= 1
    return my_list

def remove_first(my_list):
        
    if my_list["size"] > 0:
        element = my_list["elements"].pop(0)
        my_list["size"] -= 1
        return element
    return None

def remove_last(my_list):
        
    if my_list["size"] > 0:
        element = my_list["elements"].pop()
        my_list["size"] -= 1
        return element
    return None

def insert_element(my_list, element, index):
    
    if index >= 0 and index <= my_list["size"]:
        my_list["elements"].insert(index, element)
        my_list["size"] += 1
    return my_list

def change_info(my_list, index, new_info):
    if index >= 0 and index < my_list["size"]:
        my_list["elements"][index] = new_info
    return my_list

def exchange(my_list, index1, index2):
        
    if (index1 >= 0 and index1 < my_list["size"] and
        index2 >= 0 and index2 < my_list["size"]):
        temp = my_list["elements"][index1]
        my_list["elements"][index1] = my_list["elements"][index2]
        my_list["elements"][index2] = temp
    return my_list
# acá use IA para hacer el exchange, pero no se si es correcto, por eso lo dejo comentado.
def sub_list(my_list, pos, num_elements):
        
    nueva = new_list()
    if pos >= 0 and pos < my_list["size"] and num_elements > 0:
        i = pos
        contador = 0
        while i < my_list["size"] and contador < num_elements:
            nueva["elements"].append(my_list["elements"][i])
            nueva["size"] += 1
            i += 1
            contador += 1
    return nueva
                         
def new_list():
    newlist= { 
            "first": None,
            "last": None,
            "size": 0
            }
    return newlist

def is_empty(my_list):
        if my_list["size"] == 0:
                return True
        else:
                return False
        
def size(my_list):
        return my_list["size"]

def add_first(my_list, element):
        nuevo_elemento = {"info": element, "next": my_list["first"]}
        my_list["first"] = nuevo_elemento
        if my_list["size"] == 0:
                my_list["last"] = nuevo_elemento
                my_list["size"] += 1
        return my_list

def add_last(my_list, element):
        new_element = {"info": element, "next": None}
        if my_list["size"] == 0:
                my_list["first"] = new_element
                my_list["last"] = new_element
        else:
                my_list["last"]["next"] = new_element                           
                my_list["last"] = new_element
        my_list["size"] += 1
        return my_list

def first_element(my_list):
        if is_empty(my_list):
                raise Exception('IndexError: list index out of range')
        return my_list["first"]["info"]

def last_element(my_list):
        if is_empty(my_list):
                raise Exception('IndexError: list index out of range')
        return my_list["last"]["info"]

def get_element(my_list, pos):
        searchpos=0
        node=my_list["first"]
        while searchpos<pos:
                node=node["next"]
                searchpos+=1
                return node["info"]
        
def delete_element(my_list, pos):
        if pos < 0 or pos >= size(my_list):
                raise Exception('IndexError: list index out of range')
        if pos == 0:
                my_list["first"] = my_list["first"]["next"]
        if my_list["size"] == 1:
            my_list["last"] = None
        else:
                y = my_list["first"]
                for i in range(pos - 1):
                        y = y["next"]
                eliminado = y["next"]
                eliminado["next"] = eliminado["next"]
                if pos == my_list["size"] - 1:
                        my_list["last"] = y
                        
def remove_first(my_list):
        if is_empty(my_list):
                raise Exception('IndexError: list index out of range')
        primera_info = my_list["first"]["data"]
        my_list["first"] = my_list["first"]["next"]
        if my_list["size"] == 1:
                my_list["last"] = None
                my_list["size"] -= 1
        return primera_info

def remove_last(my_list):
        last_data = my_list["last"]["data"]
        if my_list["size"] == 1:
                my_list["first"] = None
                my_list["last"] = None
        else:
                x = my_list["first"]
                while x["next"] != my_list["last"]:
                        x = x["next"]
                x["next"] = None
                my_list["last"] = x
        my_list["size"] -= 1
        return last_data

def insert_element(my_list, element, pos):
        if pos < 0 or pos > size(my_list):
                raise Exception('IndexError: list index out of range')
        nuevo = {"data": element, "next": None}
        if pos == 0:
                nuevo["next"] = my_list["first"]
                my_list["first"] = nuevo
                if my_list["size"] == 0:
                 my_list["last"] = nuevo
        else:
                ahora = my_list["first"]
                for i in range(pos - 1):
                        ahora = ahora["next"]
        nuevo["next"] = ahora["next"]
        ahora["next"] = nuevo
        if pos == my_list["size"]:
            my_list["last"] = nuevo
        my_list["size"] += 1
        return my_list

def default_function(element_1, element_2):
        if element_1 < element_2:
                return -1
        elif element_1 == element_2:
                return 0
        else:
                return 1
        
def is_present  (my_list, element, cmp_function):
        is_in_array = False 
        temp= my_list["first"]
        count = 0
        while not is_in_array and temp is not None: 
                if cmp_function(element, temp["info"]) == 0:
                        is_in_array = True 
                else:
                        temp - temp ["next"]
                        count += 1
        if not is_in_array:
                count = -1
        return count

def change_info(my_list, pos, new_info):
        if is_empty(my_list):
                raise Exception('IndexError: list index out of range')
        if pos < 0 or pos >= my_list["size"]:
                raise Exception('IndexError: list index out of range')
    
        temp = my_list["first"]
        for i in range(pos):
                temp = temp["next"]
        temp["info"] = new_info
        return my_list

def exchange(my_list, pos_1, pos_2):
        if is_empty(my_list):
                raise Exception('IndexError: list index out of range')
        if (pos_1 < 0 or pos_1 >= my_list["size"] or 
        pos_2 < 0 or pos_2 >= my_list["size"]):
                raise Exception('IndexError: list index out of range')
        nodo1 = my_list["first"]
        for _ in range(pos_1):
                nodo1 = nodo1["next"]
        node1 = my_list["first"]
        for _ in range(pos_2):
                nodo2 = nodo2["next"]
        nodo1["info"], nodo2["info"] = nodo2["info"], nodo1["info"]
        return my_list

def sub_list(my_list, pos, num_elements):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    total_size = my_list["size"]
    if pos < 0 or num_elements < 0 or pos + num_elements > total_size:
        raise Exception('IndexError: list index out of range')
    nueva_lista = nueva_lista()
    p = my_list["first"]
    for i in range(pos): 
            p = p["next"]
    for i in range(num_elements):
            add_last(nueva_lista, p["info"])
            p = p["next"]
    return nueva_lista

def  to_py_list(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    py_lista = []
    t = my_list["first"]
    while t is not None:
        py_lista.append(t["info"])
        t = t["next"]
    return py_lista

        

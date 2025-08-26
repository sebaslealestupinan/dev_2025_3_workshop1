class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        
        listaInvertida= []

        for n in range(len(lista) -1, -1, -1):
                
                listaInvertida.append(lista[n])                

        return listaInvertida
    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """

        resultadBusqueda = -1
    
        if len(lista) > 0:

            for i in range (len(lista)-1):
                
                if elemento == lista[i] and resultadBusqueda == -1:
                     
                     resultadBusqueda = i
        
        return resultadBusqueda
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        
        indice = len(lista) -1

        for r in range(indice):
                
                inicio= r+1

                while inicio <= indice:

                        if lista[r] == lista[inicio] and type(lista[r]) == type(lista[inicio]):
                                del lista[inicio]
                                indice-=1
                        else: 
                                inicio+=1

                        
        return lista
    
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        nuevaLista=[]

        if len( lista1) == 0:

               nuevaLista= lista2

        elif len(lista2) == 0:

               nuevaLista=lista1

        else:               

            #indi= (len( lista1)-1) + ( len(lista2) -1)
        
            cont= 0
        
            while cont +1 <= len( lista1):
               
                    if lista1[cont] > lista2[cont]:
                       
                           nuevaLista.append(lista2[cont])
                           #cont += 1
                           nuevaLista.append(lista1[cont])

                    elif lista2[cont] == lista1[cont]:
                       
                           nuevaLista.append(lista1[cont])
                           #cont += 1 
                           nuevaLista.append(lista2[cont])

                    else:
                           nuevaLista.append(lista1[cont])
                           #cont += 1
                           nuevaLista.append(lista2[cont])
                    cont+=1
                
        return nuevaLista
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        if not lista:
                return lista
        else:
                
            rotaciones = 0

            ultimo= len(lista)-1

            while rotaciones < k:
                
                lista.insert(0, lista[ultimo])

                del lista[ultimo+1]

                rotaciones += 1

            return lista
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
                
        N_faltante=1

        while N_faltante-1 < len(lista) and N_faltante == lista[N_faltante-1]:
                        
                    N_faltante+=1
                    

        return N_faltante
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        respuesta= True

        if conjunto1 == []:
              return respuesta
        
        else: 
              cont= 0
              while respuesta ==  True  and cont < len(conjunto1):
                    
                    if conjunto1[cont] not in conjunto2:
                          
                          respuesta= False
                    else:
                          cont+=1
              return respuesta
                    
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pil= []

        def push (valor):
              pil.append(valor)

        def pop ():
              
              if pil:
                    return pil.pop()
              return None
        
        def peek():
               
               if pil:
                     return pil[-1]
               return None
        def is_empty():
              return len(pil) == 0
        
        return {
              
              "push": push,  "pop": pop,
              "peek": peek,  "is_empty": is_empty
        }
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        cola = []

        def enqueue(elemento):
              cola.append(elemento)

        def dequeue():
              if not is_empty():
                    return cola.pop(0)
              return None
        def peek():
              if cola:
                    return cola[0]
              return None
        def is_empty():
              return len(cola) == 0
        
        return {
              "enqueue" : enqueue,
              "dequeue" : dequeue,
              "peek" : peek,
              "is_empty": is_empty
        }
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass
class Node(object):
    def __init__(self, conteined_object=None, next=None):
        self.conteined_object=conteined_object
        self.next=next

class MyQueue(object):
    def __init__(self, head = None):
        self.head=Node(conteined_object=head, next=None)
        self.end_of_queue=self.head

    def add(self, element):
        """
        добавить элемент в конец очереди
        """
        if self.head.conteined_object==None:
            self.head.conteined_object=element
        else:
            self.end_of_queue.next=Node(element,None)
            self.end_of_queue=self.end_of_queue.next


    def remove(self):
        """
        удалить элемент из начала очереди
        """
        if self.head == self.end_of_queue:
            self.head=Node()
        else:
            self.head=self.head.next


    def clear(self):
        """
        очистить очередь
        """
        self.__init__()

    def to_list(self):
        """
        преобразовать очередь в список
        """
        result_array=[]
        current_element=self.head
        while current_element.next != None:
            result_array.append(current_element.conteined_object)
            current_element=current_element.next
        if current_element.conteined_object !=None: result_array.append(current_element.conteined_object)
        return result_array

class Country(object):
    def __init__(self, name: str, capital: str, population: int):
        self.name=name
        self.capital=capital
        self.population=population

    def __str__(self):
        return f"Страна - {self.name}; Столица - {self.capital}; Население - {self.population}"


if __name__=="__main__":
    int_array=[1,5,3,7,123,64]
    Country_array=[
    Country('Russia', 'Moscow', 140000000),
    Country('Belarus', "Minsk", 9400000),
    Country('France', 'Paris', 67000000)
    ]
    int_queue=MyQueue()
    Country_queue=MyQueue()
    for i in int_array:
        int_queue.add(i)

    for i in Country_array:
        Country_queue.add(i)

    print(int_queue.to_list())
    print([str(c) for c in Country_queue.to_list()])

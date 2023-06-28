#!/usr/bin/python3
"""define a class node"""


class Node:
    """represent the node class"""
    def __init__(self, data, next_node=None):
        """define a node
        Args:
        data-> the data that will be printed
        next_node-> the node that will point to next data
        """
        self.data = None
        self.next_node = None
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """return itself"""
            return (self._data)

        @data.setter
        def data(self, value):
            """init func data
            Args:
                value-> the nw value
            """
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self._data = value

        @property
        def next_node(self):
            """return itself"""
            return (self._next_node)

        @next_node.setter
        def next_node(self, value):
            if value is not None and not isinstance(value, next_node):
                raise TypeError("next_node must be a Node object")
            self._next_node = value


"""define a class singlylinked list"""


class SinglyLinkedList:
    """representation of the linked list class"""
    def __init__(self):
        """initi func"""
        self.__head = None

    def sorted_insert(self, value):
        """insert node to linked list in order
        Args:
        value -> the value to be insrted
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """define the print of linked list"""
        value = []
        tmp = self.__head
        while tmp is not None:
            value.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(value))


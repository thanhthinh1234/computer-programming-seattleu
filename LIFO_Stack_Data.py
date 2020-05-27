"""
Author: Thinh Mai
Date: 03/17/2019
Purpose: Final Exam - Question 1

"""

#there are some parts I re-use what I submitted for Single Linked List and Doubly Linked List Assignments

class Element:
    def __init__(self,value):
        self.value = value
        self.nextElement = None

#Create class Stack under principle of LIFO

class Stack:

    #I think this is the single linked list reversed, so I do not use __end, everything added will be push to the end
    def __init__(self):
        self.__begin = None

    #as mentioned above, no __end needed
    def append(self, newElement):
        if self.__begin is None:
            self.__begin = newElement

        else:
            self.__begin.nextElement = newElement

    #checking to see if stack is empty
    def stack_empty(self):
        if self.__begin == None:
            return True
        else:
            return False

    """
    The behavior is to take a value (like say an integer 10) and place it on the top of the stack
    """
    def push(self, value):
        if self.__begin == None:
            self.__begin = Element(value)

        else:
            newElement = Element(value)
            newElement.nextElement = self.__begin
            self.__begin = newElement


    """
    The behavior is to return the top items value on the stack. If the stack is empty to return None
    And also remove the top items
    """

    def pop(self):

        #if stack is empty, return None
        if self.stack_empty():
            return None

        else:

            top_element = self.__begin
            self.__begin = self.__begin.nextElement
            top_element.nextElement = None
            return top_element.value

    """
    To look within the stack and see if the value exists and return the position in the stack for that item. If the item does not exist return 0
    """

    def peek(self, value):
        currentElement = self.__begin
        element_id = 1
        results = []

        while currentElement != None:
            if currentElement.value == value:
                results.append(element_id)

            currentElement = currentElement.nextElement
            element_id += 1

        if len(results) == 0:
            return 0
        else:
            return "The search element: {} found at the position(s): {}".format(value, results)

    """
    Method to print the values in the Stack in the order they will be returned.
    """
    def print(self):

        iterator_Element = self.__begin
        if self.stack_empty():
            print("Stack Is Empty")

        else:
            while (iterator_Element != None):
                print(iterator_Element.value, ",", end=" ")
                iterator_Element = iterator_Element.nextElement
            return


#Testing
testStack = Stack()

testStack.push(100)
testStack.push(200)
testStack.push(300)
testStack.push(400)

# Print the values in Stack order, separated by commas
testStack.print()

# Search given value with the stack and return its position
print("\n" + str(testStack.peek(400)))

#Remove top items, then remove it
testStack.pop()
testStack.print()

#Lab #6
#Due Date: 02/08/2019, 11:59PM
########################################
#                                      
# Name: Stephen D'Amico 
# Collaboration Statement: I worked alone on this assignment.           
#
########################################


class Vector:
    '''
        >>> Vector([1,2])+Vector([5])
        'Error - Invalid dimensions'
        >>> Vector([1,2])+Vector([5,2])
        Vector([6, 4])
        >>> Vector([1,2])-Vector([5,2])
        Vector([-4, 0])
        >>> Vector([1,2])*Vector([5,2])
        9
        >>> x=Vector([2,4,6])
        >>> y=Vector([2,4,6])
        >>> c=x+y-plus sign calls add
        >>> type(c)
        <class 'LAB6.Vector'>
        >>> print(c)
        Vector([4, 8, 12])
        >>> x==y
        True
        >>> x-Vector([1,2])
        'Error - Invalid dimensions'
        >>> x+5
        'Error - Invalid operation'
        >>> x*y
        56
        >>> x*5
        Vector([10, 20, 30])
        >>> 5*x
        Vector([10, 20, 30])
    '''
    # --- Your code starts here
    def __init__(self, vector_list):
        self.vector = vector_list

    def __add__(self,other):
        if len(self.vector) == len(other.vector):
            l1 = []
            for i in range(len(self.vector)): 
                l1.append(self.vector[i]+other.vector[i])
            return Vector(l1)
        else: 
            return "Error - Invalid dimensions"
    def __sub__(self, other):
        if len(self.vector) == len(other.vector):
            l1 = []
            for i in range(len(self.vector)):
                l1.append(self.vector[i]- other.vector[i])
            return Vector(l1)
        else: 
            return "Error - Invalid dimensions"
    def __mul__(self, other):
        if len(self.vector) == len(other.vector):
            l1 = []
            for i in range(len(self.vector)):
                l1.append(self.vector[i]* other.vector[i])
            return sum(l1)
        elif type(self.vector) == list and type(other.vector) == float or int:
            l1= []
            for i in range(len(self.vector)):
                l1.append(self.vector[i]*other.vector)
            return Vector(l1)
        else: 
            return "Error - Invalid dimensions"
    def __eq__(self, other): 
        if len(self.vector) == len(other.vector):
            for i in range(len(self.vector)): 
                if self.vector[i] == other.vector[i]:
                    continue
                else: 
                    return False
            return True 
        else: 
            return "Error - Invalid dimensions"
    def __repr__(self):
        if type(self) == Vector:
            return "Vector({})".format(self.vector)
        else: 
            return "{}".format(self.vector)




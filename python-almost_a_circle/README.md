hlbrtn almost a circle project
steps

Write the first class Base
Write the class Rectangle that inherits from Base
Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded)
Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance
Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here
Update the class Rectangle by overriding the str method so that it returns \[Rectangle\] instance
Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y
Update the class Rectangle by adding the public method def update(self, \*args): that assigns an argument to each attribute
Update the class Rectangle by updating the public method def update(self, \*args): by changing the prototype to update(self, \*args, kwargs) that assigns a key/value argument to attributes
Write the class Square that inherits from Rectangle
Update the class Square by adding the public getter and setter size
Update the class Square by adding the public method def update(self, \*args, kwargs) that assigns attributes
Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle
Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square
Update the class Base by adding the class method def savetofile(cls, listobjs): that writes the JSON string representation of listobjs to a file
Update the class Base by adding the static method def fromjsonstring(jsonstring): that returns the list of the JSON string representation jsonstring
Update the class Base by adding the class method def create(cls, dictionary): that returns an instance with all attributes already set
Update the class Base by adding the class method def loadfromfile(cls): that returns a list of instances

#import another_module
import turtle
from xml.dom.minidom import ProcessingInstruction

from prettytable import PrettyTable

#print(another_module.another_variable)

#from turtle import Turtle , Screen
#timmy = Turtle()  #create new object from a blueprint
#print(timmy)
#timmy.shape("turtle")
#timmy.color("DeepPink")#call methods associated with object
#timmy.forward(100)

#my_screen = Screen()
#print(my_screen.canvheight)#tap into its attributes by using object_name.attribute same as having variable
#my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"]) # methods
table.add_column("Type",["Electric","Water","Fire"])
table.add_row(["Dodo","Water"])
table.align = "r" #attributes
table.border = True
print(table)


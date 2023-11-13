# This Python code gathers the following information from IFC models:

- Total number of walls, doors, and windows
- Total area of all walls
- Total price of all walls, doors, and windows
- Percentage of each element type

## Imports:

The code begins by importing the ifcopenshell library. This library provides a Python interface for reading and writing IFC models.
https://github.com/kristianedstrom/Group-11/blob/8a5a55e8f38c3734f1f0ab286a0fc046199cbaeb/Assignments/A3/Remodel.py#L1



## Specifying the IFC model path:

The code then specifies the path to the IFC model that is to be analyzed. This can be done by passing the path to the model as an argument to the script, or by hardcoding the path into the script. The file path will be changed by you from what type of IFC model you are using and where you have it stored on your computer.
The code also opens the IFC model so we can gather information about differend properties and components.
https://github.com/kristianedstrom/Group-11/blob/8a5a55e8f38c3734f1f0ab286a0fc046199cbaeb/Assignments/A3/Remodel.py#L4-L8

If Your IFC file fails to open the code the sqript will exit and the bottom code vil display an error message.
https://github.com/kristianedstrom/Group-11/blob/8a5a55e8f38c3734f1f0ab286a0fc046199cbaeb/Assignments/A3/Remodel.py#L84-L85


## Initialize variables

This is to store total price, door count, window count, wall count, and wall area
https://github.com/kristianedstrom/Group-11/blob/8a5a55e8f38c3734f1f0ab286a0fc046199cbaeb/Assignments/A3/Remodel.py#L10-L17


## IFC classes and price library

Define which IFC classes you want to measure and gather information about (in this example IfcWindow, IfcDoor and IfcWall), and define the price per unit of IFC class that you gather. This is where you change the price which it determined by marked values.
https://github.com/kristianedstrom/Group-11/blob/8a5a55e8f38c3734f1f0ab286a0fc046199cbaeb/Assignments/A3/Remodel.py#L19-L27


## Loop

Now the code will loop through all the units in each IFC class to gather information about all the IFC classes your want to measure. This can be done with multiple classes by just copying it and changing the class directory.
https://github.com/kristianedstrom/Group-11/blob/8a5a55e8f38c3734f1f0ab286a0fc046199cbaeb/Assignments/A3/Remodel.py#L29-L46

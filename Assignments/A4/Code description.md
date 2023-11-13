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



## Loop for calculation

Now the code will loop through all the units in each IFC class to gather information about all the IFC classes your want to measure. This can be done with multiple classes by just copying it and changing the class directory. This loop will also calculate the prices of all the IFC classes that you are going through based on the price library defined earlier.
https://github.com/kristianedstrom/Group-11/blob/8a5a55e8f38c3734f1f0ab286a0fc046199cbaeb/Assignments/A3/Remodel.py#L30-L51


## Wall area

To gather the wall area, the dimentions of the walls in the model must first be defined. Thats what the first two lines do.(remember to change your "height-" and "width-properties" with the actual property names of your IFC model.
The total wall area is then calculated by multiplying height and width.
https://github.com/kristianedstrom/Group-11/blob/8a5a55e8f38c3734f1f0ab286a0fc046199cbaeb/Assignments/A3/Remodel.py#L55-L60


## Calculations

The code uses a price library to calculate the price of each wall, door, and window element in the IFC model. The script then sums the prices of all of the elements to get the total price:
https://github.com/kristianedstrom/Group-11/blob/8a5a55e8f38c3734f1f0ab286a0fc046199cbaeb/Assignments/A3/Remodel.py#L63

As well as the total of elements in the model we are measuring:
https://github.com/kristianedstrom/Group-11/blob/8a5a55e8f38c3734f1f0ab286a0fc046199cbaeb/Assignments/A3/Remodel.py#L66

The code divides the number of each element type by the total number of elements in the model and multiplies the result by 100 to get the percentage of each element type.
https://github.com/kristianedstrom/Group-11/blob/8a5a55e8f38c3734f1f0ab286a0fc046199cbaeb/Assignments/A3/Remodel.py#L69-L71


## Results

Once the code has gathered all of the information from the IFC model, it prints the following results to the console:

- Total number of walls, doors, and windows: This information provides an overview of the composition of the IFC model.
- Total area of all walls: This information can be used to estimate the cost of materials and labor for constructing the walls.
- Total price of all walls, doors, and windows: This information can be used to estimate the overall cost of constructing the building represented by the IFC model.
- Price per square meter of wall: This information can be used to compare the cost of constructing walls in different buildings.
- Percentage of each element type: This information provides insights into the relative importance of different element types in the IFC model.
https://github.com/kristianedstrom/Group-11/blob/8a5a55e8f38c3734f1f0ab286a0fc046199cbaeb/Assignments/A3/Remodel.py#L74-L82

Once printed, the output of the script will look something like this:
- Total Wall Count: 100 (50.00%)
- Total Wall Area: 1000.00 square meters
- Total Price Walls: DKK 300000.00
- Price per square meter of wall: DKK 300.00
- Total Door Count: 50 (25.00%)
- Total Price Doors: DKK 100000.00
- Total Window Count: 50 (25.00%)
- Total Price Windows: DKK 50000.00
- Total Price: DKK 450000.00

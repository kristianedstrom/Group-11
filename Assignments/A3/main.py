import ifcopenshell

# Specify the path to your IFC model
ifc_file_path = r"C:\Users\krist\OneDrive\Dokumenter\Assignments BIM\model\LLYN - ARK.ifc"

# Open the IFC model
model = ifcopenshell.open(ifc_file_path)

# Initialize variables to store total price, door count, window count, wall count, and wall area
total_price = 0
total_door_count = 0
total_window_count = 0
total_wall_count = 0
total_wall_area = 0  # in square meters

# Create a price library
price_library = {
    "IfcWindow": 7000.0,  # Price per unit for IfcWindow
    "IfcDoor": 4500.0,    # Price per unit for IfcDoor
    "IfcWall": 20000.0,    # Price per unit for IfcWall
}

# Get all elements of the specified types
elements_by_type = model.by_type("IfcWindow", "IfcDoor", "IfcWall")

# Iterate over all elements and calculate the total price, door count, window count, wall count, and wall area
for element in elements_by_type:

    # Get the element type
    element_type = element.is_a()

    # Count doors, windows, and walls
    if element_type == "IfcWindow":
        total_window_count += 1
    elif element_type == "IfcDoor":
        total_door_count += 1
    elif element_type == "IfcWall":
        total_wall_count += 1

        # Calculate the wall area based on height and width
        height = element.get_info().get("YourHeightProperty", 3.0)
        width = element.get_info().get("YourWidthProperty", 8.0)
        wall_area = height * width
        total_wall_area += wall_area

    # Calculate the total price based on the element type and price library
    if element_type in price_library:
        total_price += price_library[element_type]

# Print the results
print(f"Total Price: DKK {total_price:.2f}")
print(f"Total Door Count: {total_door_count}")
print(f"Total Window Count: {total_window_count}")
print(f"Total Wall Count: {total_wall_count}")
print(f"Total Wall Area: {total_wall_area:.2f} square meters")

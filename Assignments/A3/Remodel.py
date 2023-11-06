import ifcopenshell

# Specify the path to your IFC model
ifc_file_path = r"C:\Users\marcu\OneDrive - NTNU\Dokumenter\5. semester) DTU\41934 Advanced Building Information Modeling\Assignment\LLYN - ARK (6).ifc"

try:
    # Open the IFC model
    model = ifcopenshell.open(ifc_file_path)

    # Initialize variables to store total price, door count, window count, wall count, and wall area
    total_price_walls = 0
    total_price_doors = 0
    total_price_windows = 0
    total_door_count = 0
    total_window_count = 0
    total_wall_count = 0
    total_wall_area = 0  # in square meters

    # Define the IFC classes you want to consider (IfcWindows, IfcDoor, IfcWall)
    ifc_classes_to_measure = ["IfcWindow", "IfcDoor", "IfcWall"]

    # Placeholder for a price library (you need to populate this with actual prices)
    price_library = {
        "IfcWindow": 7000.0,  # Price per unit for IfcWindow
        "IfcDoor": 4500.0,    # Price per unit for IfcDoor
        "IfcWall": 20000.0,    # Price per unit for IfcWall
    }

    # Loop through the specified IFC classes
    for ifc_class in ifc_classes_to_measure:
        elements = model.by_type(ifc_class)

        for element in elements:
            # Count doors, windows, and walls
            if ifc_class == "IfcWindow":
                total_window_count += 1
                if ifc_class in price_library:
                    price_per_unit = price_library[ifc_class]
                    total_price_windows += price_per_unit
            elif ifc_class == "IfcDoor":
                total_door_count += 1
                if ifc_class in price_library:
                    price_per_unit = price_library[ifc_class]
                    total_price_doors += price_per_unit
            elif ifc_class == "IfcWall":
                total_wall_count += 1

                # Calculate the price based on unit price from the price library (customize based on your model)
                if ifc_class in price_library:
                    price_per_unit = price_library[ifc_class]
                    total_price_walls += price_per_unit

                    # Calculate the wall area based on height and width
                    # Replace "YourHeightProperty" and "YourWidthProperty" with the actual property names from your IFC model
                    height = element.get_info().get("YourHeightProperty", 3.0)
                    width = element.get_info().get("YourWidthProperty", 8.0)

                    # Calculate the wall area in square meters and add it to the total wall area
                    wall_area = height * width
                    total_wall_area += wall_area

    # Calculate the total price by adding prices of walls, doors, and windows
    total_price = total_price_walls + total_price_doors + total_price_windows

    # Calculate the total number of elements in the model
    total_elements = total_wall_count + total_door_count + total_window_count

    # Calculate the percentage of each element type
    percentage_walls = (total_wall_count / total_elements) * 100
    percentage_doors = (total_door_count / total_elements) * 100
    percentage_windows = (total_window_count / total_elements) * 100

    # Print the results
    print(f"Total Wall Count: {total_wall_count} ({percentage_walls:.2f}%)")
    print(f"Total Wall Area: {total_wall_area:.2f} square meters")
    print(f"Total Price Walls: DKK {total_price_walls:.2f}")
    print(f"Price per square meter of wall: DKK {total_price_walls / total_wall_area:.2f}")
    print(f"Total Door Count: {total_door_count} ({percentage_doors:.2f}%)")
    print(f"Total Price Doors: DKK {total_price_doors:.2f}")
    print(f"Total Window Count: {total_window_count} ({percentage_windows:.2f}%)")
    print(f"Total Price Windows: DKK {total_price_windows:.2f}")
    print(f"Total Price: DKK {total_price:.2f}")

except Exception as e:
    print(f"An error occurred: {str(e)}")

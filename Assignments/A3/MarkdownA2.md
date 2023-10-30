### Assignment 2) Group 11

## Q: Describe the use case you have chosen.

Use Case:  Calculate the total price of the building, as well as the costs for each separate component of the structure.

## Q: Who is the use case for?

**For:**  This use case is intended for a diverse range of participants within the construction industry, encompassing architects, quantity surveyors, and building proprietors. It is tailored to serve professionals engaged in the planning, cost estimation, and administration of construction projects. Consequently, it will be employed during the project's planning phase while also facilitating the generation of a pricing proposal for the client.

## Q: What disciplinary (non BIM) expertise did you use to solve the use case?

**Expertise Used:**  To effectively implement this use case, a combination of specific skills is essential, including: -  **Quantity Surveying:**  Proficiency in measuring and quantifying building elements, as well as the final outcome. -  **Cost Estimation:**  Adeptness in estimating the costs associated with construction materials and components, as well as the overall profit margin.

## Q: What IFC concepts did you use in your script (or would you use in the rest of the tool)?

**IFC Concepts:**  This use case relies on several IFC concepts, which are: -  **Building Elements:**  We focus on specific building elements represented in the IFC model, including IfcWindow, IfcDoor, and IfcWall. We choose to focus on these, to show an example of how it can be done. -  **Property Sets:**  Property sets within the IFC model store essential information about building components, such as prices and quantities. This information is essential for the entire model. - We also tried to use "Q_AREA" to find the right amout of squaremeters, but it did not work. When we tried this, the script just printed 0,00 squaremeters, and it did not change the results. Therefor, we decided to set an example size of the walls, and used this in the calculations.

## Q: What disciplinary analysis does it require?

**Analysis Required:**  It is important to combine different information to achieve a complete analysis. To achieve the goals of this use case, the following analyses are necessary: -  **Quantity Takeoff:**  The process of quantifying the number and dimensions of building components. -  **Price Estimation:**  Determining the cost of each component based on price information stored in property sets. -  **Area Calculation:**  Calculating the total area of specific building elements, such as walls.

##Q: What building elements are you interested in?

**Building Elements:**  The whole case include every building elements in the building, but we only focus on three primary building elements: -  **Windows:**  Calculation of the total number of windows and their associated costs. We retrieve the number of windows in the building and find the price of these. -  **Doors:**  Quantifying the number of doors and their cost. Similar process to windows. -  **Walls:**  Determining the total area and cost of walls. In this case, we need to read out the total area, and not the total number of units.

##Q: What (use cases) need to be done before you can start your use case?

**Preconditions:**  The successful execution of this use case depends on the following conditions: - Availability of a complete and accurate IFC model of the building. Which is well done and carefully planned. - Property sets associated with building elements, containing relevant price and quantity information. This is very omportant for the model to work.

##Q: What is the input data for your use case?

**Input Data:**  The essential input data for this use case includes: - An IFC Model of the Building: This serves as the digital representation of the building's components. By having access to this file, you have a good starting point for calculating quantities. - Property Sets with Price Information: These property sets contain price data for individual building elements. - Quantity Information: Data on quantities, as length and width of building elements, and number of various components in the building such as doors and windows.

##Q: What other use cases are waiting for your use case to complete?

**Dependent Use Cases:**  This use case does not have direct dependencies on other use cases, but it may provide data that could be used in subsequent use cases, such as cost estimation for the entire building project.

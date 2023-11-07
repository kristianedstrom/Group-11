## BIM Execution Plan (BEP)

**Project:** Building Cost Calculation

**Client:** Unknown

**Date:** 2023-11-06

**1. Project Overview**

This project involves developing a BIM use case to calculate the total price of the building, as well as the costs for each separate component of the structure. The use case will be implemented using Python and IfcOpenShell.

**2. BIM Roles and Responsibilities**

The following BIM roles and responsibilities have been defined for this project:

* **Developer:** Responsible for developing the Python script to calculate the building cost.
* **BIM Manager:** Responsible for coordinating the BIM process and ensuring compliance with the BEP.
* **Quantity Surveyor:** Responsible for providing quantity and cost data for the building elements.

**3. BIM Software**

The following BIM software will be used for this project:

* IfcOpenShell
* Python
* BlenderBIM

**4. BIM Process**

The following BIM process will be followed for this project:

1. **Requirements Gathering:** The developer and BIM manager will meet with the quantity surveyor to gather the requirements for the use case.
2. **Use Case Development:** The developer will develop the Python script to calculate the building cost.
3. **Use Case Testing:** The BIM manager and quantity surveyor will test the use case to ensure that it is working correctly.
4. **Use Case Deployment:** The developer will deploy the use case to the BIM team.

**5. BIM Deliverables**

The following BIM deliverables will be produced for this project:

* Python script to calculate the building cost
* User documentation for the Python script

**6. BIM Standards**

The following BIM standards will be followed for this project:

* ISO 19650

**7. BIM Schedule**

The following BIM schedule has been developed for this project:

| Task | Start Date | End Date |
|---|---|---|
| Requirements Gathering | 2023-11-07 | 2023-11-09 |
| Use Case Development | 2023-11-10 | 2023-11-14 |
| Use Case Testing | 2023-11-15 | 2023-11-16 |
| Use Case Deployment | 2023-11-17 | 2023-11-18 |

**8. BIM Communication Plan**

The following BIM communication plan has been developed for this project:

* Weekly BIM coordination meetings will be held to discuss the project progress and any issues.
* The BIM manager will be responsible for communicating with the client and other stakeholders on the project status.

**9. BIM Risk Management Plan**

The following BIM risk management plan has been developed for this project:

| Risk | Mitigation Strategy |
|---|---|---|
| Inaccurate input data | The BIM manager will review the input data for accuracy before it is used in the use case.
| Script errors | The developer will thoroughly test the script to identify and fix any errors.
| Communication delays | Weekly BIM coordination meetings will be held and the BIM manager will be responsible for communicating with the client and other stakeholders on the project status.

**10. BIM Change Management Plan**

Any changes to the project scope or schedule will be communicated to the BIM manager and approved by the client before being implemented.

**11. BIM Closeout Plan**

Once the project is complete, the BIM manager will archive the project files for future reference.

**BEP Approvals**

# The report
### 3A: Analyze Use Case

**Goal:** The goal of the cost estimation tool/workflow is to streamline and automate the calculation of the total project cost as well as the costs for individual building components within the construction project.

**Model Use (BIM Uses):** Referencing the BIM uses outlined in the provided documentation, this tool aligns with the core principles of Building Information Modeling (BIM) in the following ways:
  
- **Quantitative Analysis:** The tool facilitates a detailed quantitative analysis of building elements, such as doors, windows, and walls, enabling accurate cost estimation, a fundamental aspect of BIM processes.
  
- **Information Management:** By integrating property sets and IFC models, the tool ensures efficient information management aligned with BIM principles, essential for accurate cost estimation in construction projects.

- **Workflow Automation:** The workflow automates the process of calculating costs, aligning with the automation principle of BIM to streamline and optimize project management and planning.

This analysis demonstrates how the tool aligns with the fundamental aspects of BIM, specifically addressing quantitative analysis, information management, and workflow automation to achieve accurate and efficient cost estimation within construction projects.

### 3B: Propose a (Design for a) Tool / Workflow

#### Process Description:

The proposed tool is designed to create a streamlined process for accurate cost estimation in construction projects, aligning with BIM principles and ISO 19650 standards. The workflow involves several key steps:

1. **Data Input:**
   - Users upload the IFC model and relevant property sets into the tool, which serves as the basis for cost calculations.

2. **Automated Analysis:**
   - The tool automatically reads and interprets the IFC model, extracting vital data related to building elements such as walls, doors, and windows.

3. **Property Set Examination:**
   - Extracts price and quantity information from the property sets associated with various building elements, allowing for accurate cost estimations.

4. **Cost Estimation:**
   - Utilizing the gathered data, the tool calculates costs for individual elements and the total project cost based on predefined pricing and quantities, ensuring compliance with ISO 19650 standards.

5. **Visualization and Reporting:**
   - Generates visual representations, such as charts or graphs, showcasing the cost breakdown for each building element and the overall project. Additionally, a detailed report is generated for documentation purposes.

6. **Validation and Compliance Checks:**
   - Executes checks to ensure the accuracy and compliance of the data with ISO 19650 standards, highlighting any discrepancies for review and verification.

This tool's process ensures a systematic approach to cost estimation by leveraging the BIM model and property sets, thereby automating calculations and fostering adherence to industry standards for reliable and accurate cost estimation in construction projects.

### 3D: Value

#### Business Value:

The proposed cost estimation tool presents several potential improvements and value for our business or employer:

- **Time Efficiency:** By automating the process of cost estimation through the use of the BIM model and property sets, the tool significantly reduces the time required for manual calculations. This time efficiency translates into improved productivity, enabling employees to focus on more strategic planning and decision-making aspects of construction projects.

- **Enhanced Cost Control:** The tool's accurate and automated cost estimations ensure improved cost control and planning. This not only aids in better project budgeting but also mitigates the risks associated with inaccurate cost projections, leading to more informed decision-making and resource allocation.

- **Optimized Resource Utilization:** Accurate cost estimations reduce the chances of over or underestimation of material requirements. This optimization in resource utilization contributes to cost savings and more efficient project management, thereby benefiting the company's bottom line.

#### Societal Value:

The tool's impact extends beyond the company and provides value to society:

- **Reduced Material Wastage:** Accurate estimations of material requirements mitigate the likelihood of over-ordering, reducing unnecessary material wastage in construction projects. This aligns with sustainability goals by promoting responsible resource usage and reducing the environmental impact of construction activities.

- **Sustainability and Environmental Impact:** By minimizing material waste and optimizing resource utilization, the tool contributes to a more sustainable construction industry. This reduction in waste aids in lowering the environmental footprint, aligning with global sustainability initiatives and promoting responsible construction practices.

This tool not only benefits the business by improving efficiency and cost control but also contributes positively to societal and environmental aspects by promoting sustainability and responsible resource management in the construction industry.



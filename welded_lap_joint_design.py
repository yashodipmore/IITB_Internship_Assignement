# Import necessary libraries
import math

# Constants for material properties (yield strengths in MPa)
MATERIAL_GRADES = {
    "E250": 250,
    "E275": 275,
    "E300": 300,
    "E350": 350,
    "E410": 410
}

# Function to design a welded lap joint
def design_lap_joint(P, w, t1, t2):
    """
    Design a welded lap joint for two plates.
    
    Parameters:
        P (float): Tensile force in kN
        w (float): Width of the plates in mm
        t1 (float): Thickness of plate 1 in mm
        t2 (float): Thickness of plate 2 in mm
    
    Returns:
        dict: A dictionary containing the design outputs
    """
    # Step 1: Select the plate grade with the lowest yield strength
    plate_grade = min(MATERIAL_GRADES, key=MATERIAL_GRADES.get)
    yield_strength = MATERIAL_GRADES[plate_grade]  # in MPa
    
    # Step 2: Calculate the required weld size (assume weld size = plate thickness)
    weld_size = min(t1, t2)  # in mm
    
    # Step 3: Calculate the weld length
    # Weld strength = weld_size * weld_length * yield_strength
    # Required weld strength >= P * 1000 (convert kN to N)
    required_weld_strength = P * 1000  # in N
    weld_length = required_weld_strength / (weld_size * yield_strength)  # in mm
    
    # Round up the weld length to the nearest whole number
    weld_length = math.ceil(weld_length)
    
    # Step 4: Calculate the connection strength
    connection_strength = weld_size * weld_length * yield_strength / 1000  # in kN
    
    # Step 5: Calculate the efficiency of the connection
    efficiency = connection_strength / P
    
    # Step 6: Calculate the length of the connection
    # Assume the connection length is equal to the weld length
    connection_length = weld_length
    
    # Step 7: Prepare the output
    output = {
        "Weld Size (mm)": weld_size,
        "Weld Material Grade": plate_grade,
        "Weld Length (mm)": weld_length,
        "Connection Strength (kN)": connection_strength,
        "Yield Strength Plate 1 (MPa)": yield_strength,
        "Yield Strength Plate 2 (MPa)": yield_strength,
        "Length of Connection (mm)": connection_length,
        "Efficiency": efficiency
    }
    
    return output

# Example usage
if __name__ == "__main__":
    P = 500  # Tensile force in kN
    w = 200  # Width of the plates in mm
    t1 = 10  # Thickness of plate 1 in mm
    t2 = 12  # Thickness of plate 2 in mm
    
    result = design_lap_joint(P, w, t1, t2)
    for key, value in result.items():
        print(f"{key}: {value}")
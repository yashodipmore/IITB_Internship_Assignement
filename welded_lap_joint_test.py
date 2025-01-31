import unittest
from welded_lap_joint_design import design_lap_joint

class TestLapJointDesign(unittest.TestCase):
    def test_design_lap_joint(self):
        # Test case 1
        P = 500  # kN
        w = 200  # mm
        t1 = 10  # mm
        t2 = 12  # mm
        
        result = design_lap_joint(P, w, t1, t2)
        
        # Check if connection strength is greater than tensile force
        self.assertGreaterEqual(result["Connection Strength (kN)"], P)
        
        # Check if efficiency is near 1
        self.assertAlmostEqual(result["Efficiency"], 1.0, delta=0.1)
        
        # Check if weld length is positive
        self.assertGreater(result["Weld Length (mm)"], 0)

# Run the unit tests
if __name__ == "__main__":
    unittest.main()
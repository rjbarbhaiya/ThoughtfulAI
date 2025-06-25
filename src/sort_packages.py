import argparse
    
"""
sort_packages.py

This module provides functionality to sort packages into categories based on their dimensions and mass.

Rules:
- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³
  or if any of its dimensions is greater than or equal to 150 cm.
- A package is **heavy** if its mass is greater than or equal to 20 kg.

Categories:
- **STANDARD**: Not bulky and not heavy.
- **SPECIAL**: Bulky or heavy (but not both).
- **REJECTED**: Both bulky and heavy.

Functions:
- sort(width, height, length, mass): Returns the category for the given package.

Usage:
    python src/sort_packages.py <width> <height> <length> <mass>
"""

class Package:
    """
    Represents a package with dimensions and mass, and provides methods to determine its category.

    Args:
        height (float): Height of the package in cm.
        width (float): Width of the package in cm.
        length (float): Length of the package in cm.
        mass (float): Mass of the package in kg.

    Raises:
        TypeError: If any input is not numeric.
        ValueError: If any input is not positive.
    """
    ##Units: length in cm, mass in kg
    def __init__(self, height:float, width:float, length:float, mass:float):
        try:
            self.height = float(height)
            self.width = float(width)
            self.length = float(length)
            self.mass = float(mass)
        except ValueError:
            raise TypeError("All inputs must be numeric")
        
        if any(v <= 0 for v in [self.height, self.width, self.length, self.mass]):
            raise ValueError("All dimensions and mass must be positive.")
        
        self.volume = self.height * self.width * self.length

    def isBulky(self) -> bool:
        """
        Determines if the package is bulky.

        Returns:
            bool: True if the package is bulky, False otherwise.
        """
        return self.volume >= 1000000.0 or max(self.height, self.length, self.width) >= 150.0

    def isHeavy(self) -> bool:
        """
        Determines if the package is heavy.

        Returns:
            bool: True if the package is heavy, False otherwise.
        """
        return self.mass>20.0
    
    def sortPackage(self) -> str:
        """
        Determines the category of the package.

        Returns:
            str: "STANDARD", "SPECIAL", or "REJECTED"
        """
        if self.isBulky() and self.isHeavy():
            return "REJECTED"
        elif self.isBulky() or self.isHeavy():
            return "SPECIAL"
        else:
            return "STANDARD"
        
def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sorts a package into a category based on its dimensions and mass.

    Args:
        width (float): Width of the package in cm.
        height (float): Height of the package in cm.
        length (float): Length of the package in cm.
        mass (float): Mass of the package in kg.

    Returns:
        str: The category ("STANDARD", "SPECIAL", or "REJECTED").
    """
    return Package(height, width, length, mass).sortPackage()

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Sort packages based on dimensions and mass.")
    parser.add_argument("width", type=float, help="Width of the package in cm")
    parser.add_argument("height", type=float, help="Height of the package in cm")
    parser.add_argument("length", type=float, help="Length of the package in cm")
    parser.add_argument("mass", type=float, help="Mass of the package in kg")

    args = parser.parse_args()
    result = sort(args.width, args.height, args.length, args.mass)
    print(result)
    

    

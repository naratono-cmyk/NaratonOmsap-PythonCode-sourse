print("Now try these exercises:")
print()
print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()



#input
radius = float(input("Enter you radius"))
use = 3.14159
#process
area = (use*radius**2)
circumference = (2*use*radius)
#output
print(f"calculation area =(π*r²) {area}={use}*{radius}**2")




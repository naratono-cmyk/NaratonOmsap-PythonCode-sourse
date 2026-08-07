# Example 3: Mathematical function
def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

###############################################
######ตัวอย่างสร้างfuntion สำหรับคำนวณสามเหลี่ยม######
###############################################

def calculate_trianagel_area(height,base):
    """Calculates and displays triangle area"""
    area = 0.5 * height * base
    print(f"Triangel with height {height} and base {base}")
    print(f"Area = {height} × {base} = {area}")
    print()

print("Calculating traingle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

###############################################
###จากตัวอย่าง ใฟ้สร้างfuntion สำหรับคำนวณเพทใวงกลม###
###############################################

def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

#--------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------#



# Example 1: Function that returns a value
def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    result = a + b
    return result

print("Using functions that return values:")
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 7)
print(f"5 + 3 = {sum1}")
print(f"10 + 7 = {sum2}")
print(f"Sum of both results: {sum1 + sum2}")
print()


# Example 2: Function returning multiple values
def get_circle_info(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

print("Circle calculations:")
radius = 5
area, circumference = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()

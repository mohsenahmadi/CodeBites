#Given a point represented as (x, y) and a rectangle defined by its top-left corner (x1, y1) 
# and bottom-right corner (x2, y2), write code to determine if the point lies inside or on the 
# boundary of the rectangle. Assume the rectangle sides are parallel to the axes.

# Inputs
point = (3, 4)
rectangle = (2, 3, 5, 6)  # Top-left: (2, 3), Bottom-right: (5, 6)

# Extract coordinates
x, y = point
x1, y1, x2, y2 = rectangle

# Check if the point lies within the rectangle's bounds
if x1 <= x <= x2 and y1 <= y <= y2:
    print("The point lies inside or on the boundary of the rectangle.")
else:
    print("The point lies outside the rectangle.")


import math
# ------------------ CLASS POINT ------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# ------------------ CLASS RECTANGLE ------------------
class Rectangle:
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner   


# ------------------ CLASS CIRCLE ------------------
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


# ------------------ HÀM KIỂM TRA ------------------

def point_in_circle(circle, point):
    dx = point.x - circle.center.x
    dy = point.y - circle.center.y
    distance = math.sqrt(dx**2 + dy**2)

    return distance <= circle.radius


def rect_in_circle(circle, rect):
    p1 = rect.corner
    p2 = Point(rect.corner.x + rect.width, rect.corner.y)
    p3 = Point(rect.corner.x, rect.corner.y + rect.height)
    p4 = Point(rect.corner.x + rect.width, rect.corner.y + rect.height)

    return (point_in_circle(circle, p1) and
            point_in_circle(circle, p2) and
            point_in_circle(circle, p3) and
            point_in_circle(circle, p4))


def rect_circle_overlap(circle, rect):
    p1 = rect.corner
    p2 = Point(rect.corner.x + rect.width, rect.corner.y)
    p3 = Point(rect.corner.x, rect.corner.y + rect.height)
    p4 = Point(rect.corner.x + rect.width, rect.corner.y + rect.height)

    return (point_in_circle(circle, p1) or
            point_in_circle(circle, p2) or
            point_in_circle(circle, p3) or
            point_in_circle(circle, p4))


# ------------------ TEST ------------------

# Tạo circle: tâm (150, 100), bán kính 75
center = Point(150, 100)
circle = Circle(center, 75)

# Test point
p = Point(160, 110)
print("Point in circle:", point_in_circle(circle, p))

# Test rectangle
rect = Rectangle(50, 30, Point(140, 90))
print("Rect in circle:", rect_in_circle(circle, rect))
print("Rect overlap circle:", rect_circle_overlap(circle, rect))
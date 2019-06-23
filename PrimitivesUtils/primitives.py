import numpy as np

def calc_triangle_determ(pt1, pt2, pt3):

	triangle_array = np.array( [[pt1[0], pt1[1], 1],
								[pt2[0], pt2[1], 1],
								[pt3[0], pt3[1], 1] ])
	return np.linalg.det(triangle_array)

# def calc_triangle_determ(pt1, pt2, pt3):
# 	part_one = pt1[0] * (pt2[1] - pt3[0])
# 	part_two = pt1[1] * (pt2[1] - pt3[1])
# 	part_three = ((pt2[0] * pt3[1]) - (pt3[0] * pt2[1]))
# 	return (part_one - part_two + part_three ) * .5

# int calcDeterminantForTriangle(Point p1, Point p2, Point p3) {
# 	int partOne = p1.x * (p2.y - p3.y);
# 	int partTwo = p1.y * (p2.x - p3.x);
# 	int partThree = ((p2.x * p3.y)  - (p3.x * p2.y));
# 	return (partOne - partTwo + partThree) * .5;
# }
def calc_triangle_area():
	return None

def turned_left(pt1, pt2, pt3):
	return calc_triangle_determ(pt1, pt2, pt3) < 0

def turned_right(pt1, pt2, pt3):
	return calc_triangle_determ(pt1, pt2, pt3) > 0

def turned_straight(pt1, pt2, pt3):
	return calc_triangle_determ(pt1, pt2, pt3) == 0

def msg_me():
	print("tits")
import tkinter
import os
import sys
import pyautogui
import math
import pdb
import pdb; 
sys.path.append(os.getcwd() +  "/../PrimitivesUtils")

import primitives
import utils

DEFAULT_FONT = ('Helvetica', 20)
RADIUS_SIZE = 3


class GrahamScanApplication:
	def __init__(self):
		self.all_pts = {}

		self._root_window = tkinter.Tk()
		
		self._button1 = tkinter.Button(master = self._root_window, text = 'Button 1',
			font = DEFAULT_FONT, command = self.do_graham_scan)

		self._button1.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
		
		
		self._button2 = tkinter.Button(master = self._root_window, text = 'Button 2',
			font = DEFAULT_FONT, command = self.check_prim)

		self._button2.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.E)
		

		self._canvas = tkinter.Canvas(
            master = self._root_window, background = '#ffffff')

		self._canvas.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 10,
        	sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

		self._canvas.bind("<Button-1>", self._on_canvas_left_click)
		self._canvas.bind("<Button-2>", self._on_canvas_middle_click)
		self._canvas.bind("<Button-3>", self._on_canvas_right_click)
		self._root_window.bind("<Return>", self.do_graham_scan_event)


		self._root_window.rowconfigure(0, weight = 0)
		self._root_window.rowconfigure(1, weight = 3)
		self._root_window.columnconfigure(0, weight = 1)
		self._root_window.columnconfigure(1, weight = 1)
		
	# def _get_mouse_relative_position(self):
	# 	x = self._root_window.winfo_pointerx()
	# 	y = self._root_window.winfo_pointery()
	# 	abs_coord_x = self._root_window.winfo_pointerx() - self._root_window.winfo_rootx()
	# 	abs_coord_y = self._root_window.winfo_pointery() - self._root_window.winfo_rooty()
	# 	return (abs_coord_x, abs_coord_y)

	def check_prim(self):
		print("Left Turn:", primitives.turned_left(
			self.all_pts[1], self.all_pts[2], self.all_pts[3]))

	def do_graham_scan(self):
		all_pts_sorted = sorted(list(set(self.all_pts.values())))
		stack = []
		print(len(all_pts_sorted), all_pts_sorted)
		i = 0
		#pdb.set_trace()
		while i < len(all_pts_sorted):
			while(len(stack) >= 2):
				prev1, prev2 = stack[-2:]
				if(primitives.turned_left(prev1, prev2, all_pts_sorted[i])):
					stack.pop()
				else:
					break
			stack.append(all_pts_sorted[i])
			i+=1
		self.draw_lines(stack)
		return stack

	def do_graham_scan_event(self, event):
		self.do_graham_scan()

	def draw_lines(self, stack):
		for i in range(len(stack)-1):
			self._canvas.create_line(stack[i][0],stack[i][1],stack[i+1][0],stack[i+1][1])

	def _on_canvas_left_click(self, event):
		canvas_id = self._canvas.create_oval(event.x-RADIUS_SIZE, event.y-RADIUS_SIZE,
			event.x+RADIUS_SIZE, event.y+RADIUS_SIZE, fill="black")
		self.all_pts[canvas_id] = (event.x, event.y)
		
	def _on_canvas_middle_click(self, event):
		print(self.all_pts)

	def _on_canvas_right_click(self, event):
		for i, pos in self.all_pts.items():
			if(math.sqrt((pos[0] - event.x) ** 2 + (pos[1] - event.y) ** 2) < RADIUS_SIZE):
				self._canvas.delete(i)

	def run(self):
		self._root_window.geometry("1200x800")
		self._root_window.mainloop()

if __name__ == '__main__':
    GrahamScanApplication().run()


# point.py

#
# >>> import point
# >>> p1 = point.from_frac(0.5, 0.6)
# >>> p1
# <point.Point object ...>
# >>> p1.frac()
# (0.5, 0.6)
# >>> p1.pixel(1000, 800)
# (500, 480)
# >>> p2 = point.from_pixel(400, 600, 800, 800)
# >>> p2.frac()
# (0.5, 0.75)
# >>> p2.pixel(2000, 2000)
# (1000, 1500)





# std::pair<Point, Point> getTheTwoPreviousNumsFromStack(std::stack<Point> & allPts) {
# 	std::pair<Point, Point> toRet;
# 	toRet.first = allPts.top(); //middle
# 	allPts.pop();
# 	toRet.second = allPts.top();//first
# 	allPts.push(toRet.first);
# 	return toRet;
# }


	# def do_graham_scan(self):
	# 	all_pts_sorted = sorted(list(set(self.all_pts.values())))
	# 	stack = []
	# 	for pos in all_pts_sorted:
	# 		while(len(stack) >= 2):
	# 			prev1, prev2 = stack[-2:]
	# 			if(primitives.turned_left(prev1, prev2, pos)):
	# 				print()
	# 				stack.pop()
	# 			else:
	# 		stack.append(pos)
	# 				break
	# 	print(stack)
	# 	return stack



# std::stack<Point> performGrahamScanUpperHull(std::vector<Point> allCoords, sf::RenderWindow & window) {
# 	std::cout << "Performing Graham Scan" << std::endl;
# 	std::stack<Point> allPts;
# 	std::sort(allCoords.begin(), allCoords.end());
# 	allCoords.erase( unique( allCoords.begin(), allCoords.end() ), allCoords.end() );

# 	printVectorOfPairs(allCoords);
# 	Point prev;
	

	
# 	for(int i = 0; i < allCoords.size(); ++i) {
# 		while (allPts.size() >= 2) {
# 			std::pair<Point, Point> prevTwoPoints = getTheTwoPreviousNumsFromStack(allPts);
# 			std::cout << "Area of Tri: " << calculateAreaOfTriangle(prevTwoPoints.second, revTwoPoints.first, allCoords[i]) << std::endl;
# 			if( turnedLeft(prevTwoPoints.second, prevTwoPoints.first, allCoords[i])) {
# 				allPts.pop();
# 			} else {
# 				break;
# 			}
# 		}
# 		allPts.push(allCoords[i]);
# 	}
# 	printStack(allPts);
# 	return allPts;
# }
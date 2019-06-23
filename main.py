# import tkinter
# import PrimitivesUtils.primitives as geoutils
# import GrahamScan.graham as gs

# _BUTTON_PRESSED_TEXT = "Hi"
# _BUTTON_HOVER_TEXT = "Almost there"
# _BUTTON_NORMAL_TEXT = "Press pls"


# def close_wind(root) -> None:
# 	root.destroy()

# def b_pressed() -> None:
# 	print(_BUTTON_PRESSED_TEXT)

# def on_mouse_entered_button(event: tkinter.Event) -> None:
#     event.widget['text'] = _BUTTON_HOVER_TEXT



# def on_mouse_exited_button(event: tkinter.Event) -> None:
#     event.widget['text'] = _BUTTON_NORMAL_TEXT


# def main():
# 	geoutils.msg_me()
# 	root = tkinter.Tk()
# 	b1 = tkinter.Button(master = root, text = _BUTTON_NORMAL_TEXT, font = ('Helvetica', 20), command = b_pressed)
# 	b1.pack()
# 	b1.bind('<Enter>', on_mouse_entered_button)
# 	b1.bind('<Leave>', on_mouse_exited_button)

# 	root.mainloop();

# def main_two():
# 	crack = gs.GrahamScanApplication();
# 	crack.run()

# if __name__ == "__main__":
# 	main_two()



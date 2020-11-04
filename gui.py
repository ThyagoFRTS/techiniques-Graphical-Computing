# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 15:04:38 2020

@author: RuiRui
"""

import tkinter as tk
import project_image as pi


def create_window():
	main_window = tk.Tk()
	main_window.title("The ultimate PROGRAM")
	main_window.geometry("700x500+50+50")
	return main_window


def main():
	main_window = create_window()
	original_image = pi.create_image()
	img = pi.create_image()


	scale = tk.Entry(main_window)
	scale.insert(0,"1")
	rotate = tk.Entry(main_window)
	rotate.insert(0,"0")
	flip = tk.Entry(main_window)
	flip.insert(0,"0")
	horizontal = tk.Entry(main_window)
	horizontal.insert(0,"0")
	vertical = tk.Entry(main_window)
	vertical.insert(0,"0")


	tk.Label(text="multiply by ").grid(row = 1,column = 1)
	tk.Label(text="+/- angle").grid(row = 2,column = 1)
	tk.Label(text="flip Horiz=1 Verti=0").grid(row = 3,column = 1)
	tk.Label(text="Verti +-(px)").grid(row = 4,column = 1)
	tk.Label(text="Horiz +-(px)").grid(row = 4,column = 3)


	scale.grid(row = 1,column = 2)
	rotate.grid(row = 2,column = 2)
	flip.grid(row = 3,column = 2)
	horizontal.grid(row = 4,column = 2)
	vertical.grid(row = 4,column = 4)


	btn1 = tk.Button(main_window, text = "view original image",command = lambda: pi.show_image(original_image))
	btn2 = tk.Button(main_window, text = "scale image",command = lambda: pi.scale_image(img,float(scale.get())))
	btn3 = tk.Button(main_window, text = "rotate image",command = lambda: pi.rotate_image(img,float(rotate.get())))
	btn4 = tk.Button(main_window, text = "flip image",command = lambda: pi.flip_image(img,int(flip.get())))
	btn5 = tk.Button(main_window, text = "translate image",command = lambda: pi.translate_image(img,
																								float(horizontal.get()),
																								float(vertical.get())
																									))

	btn1.grid(row = 0,column = 0)
	btn2.grid(row = 1,column = 0)
	btn3.grid(row = 2,column = 0)
	btn4.grid(row = 3,column = 0)
	btn5.grid(row = 4,column = 0)


	main_window.mainloop()


if __name__ == "__main__":
	print("===========LOADING===========")
	print("By Thyago on today")
	main()
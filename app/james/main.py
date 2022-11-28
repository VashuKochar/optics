from tkinter import Tk, TclError, ttk, W, StringVar, Frame, Label, Entry, Checkbutton, Button, OptionMenu, IntVar, DoubleVar, BooleanVar, Scrollbar
import numpy as np
from PIL import ImageTk, Image
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# Use TkAgg in the backend of tkinter application
matplotlib.use('TkAgg')

from model import vaccumRabiOscillations, wignerFunctions

def create_heading_frame(container: Frame, title:str):
	frame = Frame(container)
	
	Label(frame, text=title, font=('Times', 30)).grid(column=0, row=0, sticky=W)
	
	return frame

def create_atom_input_frame(container: Frame):
	frame = Frame(container)
	
	# Atomic Frequency
	atom_frequency = DoubleVar(container.master.master, name="atom_frequency", value = 1.0 * 2 * np.pi)
	Label(frame, text=r'Atomic frequency: ').grid(column=0, row=0, sticky=W)
	atom_frequency_box = Entry(frame, width=30, textvariable=atom_frequency)
	atom_frequency_box.focus()
	atom_frequency_box.grid(column=1, row=0, sticky=W)
	
	# Atomic Dissipation rate
	atom_dissipation = DoubleVar(container.master.master, name="atom_dissipation", value=0.05)
	Label(frame, text=r'Atomic dissipation rate: ').grid(column=0, row=1, sticky=W)
	atom_dissipation_rate = Entry(frame, width=30, textvariable=atom_dissipation)
	atom_dissipation_rate.grid(column=1, row=1, sticky=W)
	
	# Atom initial state
	atom_states = [0,1]
	atom_initial_state = IntVar(container.master.master, name="atom_init",value=1)
	Label(frame, text=r'Atomic initial state: ').grid(column=0, row=2, sticky=W)
	atom_dissipation_drop = OptionMenu(frame, atom_initial_state, *atom_states)
	atom_dissipation_drop.grid(column=1, row=2, sticky=W)
	
	return frame



def create_cavity_input_frame(container: Frame):
	frame = Frame(container)
	
	cavity_frequency = DoubleVar(container.master.master, name="cavity_frequency")
	cavity_frequency.set(1.0 * 2 * np.pi)
	Label(frame, text=r'Cavity frequency: ').grid(column=0, row=0, sticky=W)
	cavity_frequency_box = Entry(frame, width=30, textvariable=cavity_frequency)
	cavity_frequency_box.grid(column=1, row=0, sticky=W)
	
	cavity_dissipation = DoubleVar(container.master.master, name="cavity_dissipation")
	cavity_dissipation.set(0.005)
	Label(frame, text=r'Cavity dissipation rate: ').grid(column=0, row=1, sticky=W)
	cavity_dissipation_box = Entry(frame, width=30, textvariable=cavity_dissipation)
	cavity_dissipation_box.grid(column=1, row=1, sticky=W)
	
	# No of cavity states
	no_of_cavity_states = 15
	
	# Cavity initial state
	cavity_states = range(no_of_cavity_states)
	cavity_initial_state = IntVar(container.master.master, name="cavity_init",value=0)
	Label(frame, text=r'Cavity initial state:').grid(column=0, row=2, sticky=W)
	atom_dissipation_drop = OptionMenu(frame, cavity_initial_state, *cavity_states)
	atom_dissipation_drop.grid(column=1, row=2, sticky=W)
	
	return frame
	
def create_model_input_frame(container: Frame):
	frame = Frame(container)
	
	coupling_constant = DoubleVar(container.master, name="coupling", value=0.05 * 2 * np.pi)
	Label(frame, text=r'Coupling constant (g):').grid(column=0, row=0, sticky=W)
	couplingBox = Entry(frame, width=30, textvariable=coupling_constant)
	couplingBox.grid(column=1, row=0, sticky=W)
	
	thermal_excitation = DoubleVar(container.master, name="thermal", value=0.0)
	Label(frame, text=r'Avg thermal excitation: ').grid(column=0, row=1, sticky=W)
	thermal_excitation_box = Entry(frame, width=30, textvariable=thermal_excitation)
	thermal_excitation_box.grid(column=1, row=1, sticky=W)
	
	Label(frame, text=r'Approximations').grid(column=0, row=2, sticky=W)
	rotating_wave = BooleanVar(container.master, name="rwa", value=True)
	rotating_wave_checkbox = Checkbutton(frame, text=r'Rotating wave approximation: ', variable=rotating_wave, onvalue=True, offvalue=False, width=30)
	rotating_wave_checkbox.grid(column=1, row=2, sticky=W)
	
	return frame
	

def create_input_frame(container):

	frame = Frame(container)
	
	atom_frame = create_atom_input_frame(frame)
	atom_frame.grid(column=0, row=0)
	
	cavity_frame = create_cavity_input_frame(frame)
	cavity_frame.grid(column=1, row=0)
	
	model_frame = create_model_input_frame(frame)
	model_frame.grid(column=2, row=0)
	
	# Padding
	for widget in frame.winfo_children():
		widget.grid(padx=5, pady=5)

	return frame

def create_x_input_frame(container: Frame):
	frame = Frame(container)
	
	x = DoubleVar(container.master, name="mod_x", value=3)
	Label(frame, text=r'|x|:').grid(column=0, row=0, sticky=W)
	xBox = Entry(frame, width=30, textvariable=x)
	xBox.grid(column=1, row=0, sticky=W)
	
	x_steps = IntVar(container.master, name="no_x", value=200)
	Label(frame, text=r'No of X: ').grid(column=0, row=1, sticky=W)
	x_steps_box = Entry(frame, width=30, textvariable=x_steps)
	x_steps_box.grid(column=1, row=1, sticky=W)
	
	return frame

def create_t_input_frame(container: Frame):
	frame = Frame(container)
	
	t = DoubleVar(container.master, name="t_end", value=25)
	Label(frame, text=r't:').grid(column=0, row=0, sticky=W)
	tBox = Entry(frame, width=30, textvariable=t)
	tBox.grid(column=1, row=0, sticky=W)
	
	t_steps = IntVar(container.master, name="no_t", value=101)
	Label(frame, text=r'No of T: ').grid(column=0, row=1, sticky=W)
	t_steps_box = Entry(frame, width=30, textvariable=t_steps)
	t_steps_box.grid(column=1, row=1, sticky=W)
	
	return frame

def create_system_frame(container: Tk):
	frame = Frame(container)

	x_frame = create_x_input_frame(frame)
	x_frame.grid(column=0, row=0)
	
	t_frame = create_t_input_frame(frame)
	t_frame.grid(column=1, row=0)

	for widget in frame.winfo_children():
		widget.grid(padx=5, pady=5)

	return frame

def create_button_frame(container: Tk):
	frame = Frame(container)

	Button(frame, text='Recalculate model', command=lambda: calculate(container)).grid(column=0, row=0)

	for widget in frame.winfo_children():
		widget.grid(padx=5, pady=5)

	return frame

def calculate(container: Tk):
	print("Calculating vacuum rabi oscillations")
	atom_frequency = float(container.getvar(name="atom_frequency"))
	atom_dissipation = float(container.getvar(name="atom_dissipation"))
	atom_init = int(container.getvar(name="atom_init"))
	cavity_frequency = float(container.getvar(name="cavity_frequency"))
	cavity_dissipation = float(container.getvar(name="cavity_dissipation"))
	cavity_init = int(container.getvar(name="cavity_init"))
	couple = complex(container.getvar(name="coupling"))
	thermal = float(container.getvar(name="thermal"))
	rwa= bool(container.getvar(name="rwa"))
	X_START = -abs(float(container.getvar(name="mod_x")))
	X_END = abs(float(container.getvar(name="mod_x")))
	X_STEPS = abs(int(container.getvar(name="no_x")))
	T_END = float(container.getvar(name="t_end"))
	T_STEPS = int(container.getvar(name="no_t"))
	tinterest = [0.0, 5.0, 15.0, 25.0]
	
	print("Atomic frequency: ",atom_frequency)
	print("Atomic Dissipation: ",atom_dissipation)
	print("Atomic Initial state: ",atom_init)
	print("Cavity frequency: ",cavity_frequency)
	print("Cavity Dissipation: ",cavity_dissipation)
	print("Cavity Initial state: ",cavity_init)
	print("Coupling constant: ",couple)
	print("Average thermal excitation: ",thermal)
	print("RWA: ",rwa)
	
	print("X: ",X_START, " ",X_END, " (",X_STEPS,")")
	print("T: ",0, " ",T_END, " (",T_STEPS,")")
	
	fig_size = (8, 4)
	f1 = plt.figure(figsize=fig_size)
	
	f1 = vaccumRabiOscillations(no_of_cavity_states=15, cavity_frequency=cavity_frequency, cavity_dissipation=cavity_dissipation, cavity_initial_state=cavity_init, no_of_atom_states=2, atom_frequency=atom_frequency, atom_dissipation=atom_dissipation, atom_initial_state=atom_init, coupling=couple,avg_thermal_excitation=thermal,rwa=rwa, T_END=T_END, T_STEPS=T_STEPS, fig=f1)
	canvas1 = FigureCanvasTkAgg(f1,master = container)
	# canvas1.draw()
	canvas1.get_tk_widget().grid(column=0, row=4)

	f2 = plt.figure(figsize=fig_size)
	f2 = wignerFunctions(no_of_cavity_states=15, cavity_frequency=cavity_frequency, cavity_dissipation=cavity_dissipation, cavity_initial_state=cavity_init, no_of_atom_states=2, atom_frequency=atom_frequency, atom_dissipation=atom_dissipation, atom_initial_state=atom_init, coupling=couple,avg_thermal_excitation=thermal,rwa=rwa,X_END=X_END, X_START=X_START, X_STEPS=X_STEPS, T_END=T_END, T_STEPS=T_STEPS,tinterest=tinterest, fig=f2)
	canvas2 = FigureCanvasTkAgg(f2,master = container)
	# canvas2.draw()
	canvas2.get_tk_widget().grid(column=0, row=5)

	# creating the Matplotlib toolbar
	# toolbarFrame = Frame(master=container)
	# toolbarFrame.grid(column=0, row=5, sticky="w")
	# toolbar = NavigationToolbar2Tk(canvas1,toolbarFrame)
	# toolbar.update()
 
title = "Jaynes-Cummings model"
height = 1000
width = 1000

root = Tk()

root.title(title)
root.geometry(f'{height}x{width}')
# layout on the root window
# root.columnconfigure(0, weight=4)
# root.columnconfigure(1, weight=1)

head_frame = create_heading_frame(root, title)
head_frame.grid(column=0, row=0)

input_frame = create_input_frame(root)
input_frame.grid(column=0, row=1)

button_frame = create_system_frame(root)
button_frame.grid(column=0, row=2)

button_frame = create_button_frame(root)
button_frame.grid(column=0, row=3)

#ADDING A SCROLLBAR
myscrollbar=Scrollbar(root,orient="vertical")
myscrollbar.grid(column=1, rowspan = 3)

root.mainloop()
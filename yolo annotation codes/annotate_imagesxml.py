import os

import matplotlib.pyplot as plt

import cv2

from matplotlib.widgets import RectangleSelector


img = None

topleft = []

bottomright = []

object_list = []

image_folder = '/home/mayank/potholes/pothole_image_data/MyDataset/train/mayank/'

saveddir = '/home/mayank/potholes/pothole_image_data/MyDataset/train/mkannotations'

obj = 'potholes'

def onkeypress(event):
    global object_list
    global topleft
    global bottomright
    global img
    if event.key == 'q':
        print(topleft,bottomright)
        topleft =[]
        bottomright =[]
        img = None
        plt.close()

def line_select_callback(clk, rls):
    #  print(clk.xdata, clk.ydata)
    global topleft
    global bottomright
    topleft.append((int(clk.xdata), int(clk.ydata)))
    bottomright.append((int(rls.xdata), int(rls.ydata)))
    object_list.append(obj)

def toggle_selector(event):
    toggle_selector.RS.set_active(True)

if __name__ == "__main__":
    for n, image_file in enumerate(os.scandir(image_folder)):
        img = image_file
        fig,ax = plt.subplots(1)
        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(250,120,1280,1024)
        image = cv2.imread(image_file.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ax.imshow(image)
        toggle_selector.RS = RectangleSelector(
            ax, line_select_callback,
            drawtype='box', useblit= True,
            button=[1], minspanx=5,minspany=5,
            spancoords='pixels', interactive=True
        )
        bbox = plt.connect("key_press_event", toggle_selector)
        key = plt.connect('key_press_event',onkeypress)
        plt.show()

import dearpygui.dearpygui as dpg
import numpy as np
import math

dpg.create_context()


with dpg.window(tag="Main"):
    dpg.add_child_window(tag='Params', parent='Main')

    dpg.add_child_window(tag='Disp', parent='Main')
   

dpg.set_primary_window('Main', True)
dpg.create_viewport(title='Sin_Gen', width=700, height=500, min_width=700, min_height=500)
dpg.setup_dearpygui()
dpg.show_viewport()

cor_y = 10
cor_x = 16
while dpg.is_dearpygui_running():
    w = dpg.get_item_width('Main')
    dpg.set_item_width('Params', w - cor_x)
    dpg.set_item_width('Disp', w - cor_x)
    h = dpg.get_item_height('Main')
    dpg.set_item_height('Params', int(h) * 0.3 - cor_y)
    dpg.set_item_height('Disp', int(h) * 0.7 - cor_y)
    dpg.render_dearpygui_frame()

dpg.destroy_context()
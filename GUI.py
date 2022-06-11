import dearpygui.dearpygui as dpg
import numpy as np
import math

dpg.create_context()
### CREATE DEFAULT SINE WAVE
global x
x = np.linspace(0, 1000 - 1, 1000)
amp = 1
freq = 1
ph = 0
wave = amp * np.sin(2 * np.pi * x * freq / len(x) + math.radians(ph))

def update_data():
    amp = dpg.get_value('slider')
    freq = dpg.get_value('slider2')
    ph = dpg.get_value('slider3')
    wave = amp * np.sin(2 * np.pi * x * freq / len(x) + math.radians(ph))
    dpg.set_value('series_tag', [x, wave])
    dpg.set_item_label('series_tag', "sin(x)")

with dpg.window(tag="Main"):
    ### WINDOW FOR SLIDERS
    dpg.add_child_window(tag='Params', parent='Main')
    ### SLIDERS TO CONTROLE PARAMS OF SIN
    dpg.add_slider_float(tag='slider', parent='Params', label='amp', min_value=0.0, max_value=1, default_value=1,
                         callback=update_data)
    dpg.add_slider_float(tag='slider2', parent='Params', label='freq', min_value=0.0, max_value=100, default_value=1,
                         callback=update_data)
    dpg.add_slider_float(tag='slider3', parent='Params', label='ph', min_value=0.0, max_value=360, default_value=0,
                         callback=update_data)
    ### WINDOW FOR PLOT
    dpg.add_child_window(tag='Disp', parent='Main')
    ### PLOT TO DISPLAY SIN WAVE
    with dpg.plot(label="Sin", height=-1, width=-1, parent='Disp'):
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label="# of points")
        dpg.add_plot_axis(dpg.mvYAxis, label="Amp", tag="y_axis")
        dpg.add_line_series(x, wave, label="sin(x)", parent="y_axis", tag="series_tag")

dpg.set_primary_window('Main', True)
dpg.create_viewport(title='Sin_Gen', width=700, height=500, min_width=700, min_height=500)
dpg.setup_dearpygui()
dpg.show_viewport()

cor_y = 10
cor_x = 16
while dpg.is_dearpygui_running():
    ### AUTOSCALING 
    w = dpg.get_item_width('Main')
    dpg.set_item_width('Params', w - cor_x)
    dpg.set_item_width('Disp', w - cor_x)
    dpg.set_item_pos('slider', (10, int((dpg.get_item_height('Params') - 20) * 0.1)))
    dpg.set_item_pos('slider2', (10, int((dpg.get_item_height('Params') - 20) * 0.5)))
    dpg.set_item_pos('slider3', (10, int((dpg.get_item_height('Params') - 20) * 0.9)))
    w = dpg.get_item_width('Params')
    dpg.set_item_width('slider', w * 0.92)
    dpg.set_item_width('slider2', w * 0.92)
    dpg.set_item_width('slider3', w * 0.92)
    h = dpg.get_item_height('Main')
    dpg.set_item_height('Params', int(h) * 0.3 - cor_y)
    dpg.set_item_height('Disp', int(h) * 0.7 - cor_y)
    dpg.render_dearpygui_frame()

dpg.destroy_context()
import dearpygui.dearpygui as dpg
import sep_texts


dpg.create_context()
dpg.create_viewport(width=400, height=300)


with dpg.window(label='separador de textos', width=400, height=300):
    dpg.add_text("digite o texto para ser separado abaixo:")
    dpg.add_input_text(tag='input_text')
    dpg.add_button(label='inserir', callback=sep_texts.main)
    
    dpg.add_text("apagar os arquivos de texto:", pos=[10, 114])
    dpg.add_button(label='apagar', pos=[6, 139], callback=sep_texts.delete_all_files)
    
    dpg.add_text("limpar os arquivos de texto:", pos=[10, 178])
    dpg.add_button(label='limpar', pos=[6, 203], callback=sep_texts.erase_all_files)
    
    
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


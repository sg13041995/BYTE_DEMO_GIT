from view import View
from model import Model

def run_the_app():
    view_object = View()
    
    view_object.greet()
    
    file_name = view_object.ask_filename()
    file_content = view_object.ask_content()
    
    
    model_object = Model(filename=file_name,content=file_content)
    
    model_object.create()
    status = model_object.write()
    
    if (status == 200):
        view_object.show_success()
        
        file_data = model_object.read()
        view_object.display_data(file_data)
        
    else:
        view_object.show_failed()
        
    
    
import view
import import_info
import data_mod





def main_func():
    """Основной модуль"""
    a = view.interaction()
    if a[1] == 1:
        import_info.create_data(a[0])
    if a[1] == 2:
        view.res_find(data_mod.get_data(a[0]))
    # if a[1] == 3:
    #     delete_contact.        
    # if a[1] == 4:      
    # if a[1] == 5:  
    #     remove_contact.


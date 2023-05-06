import sched, time
from thonny import get_workbench
from thonny.languages import tr
from logging import getLogger

get_workbench().set_default("general.Enregistrement_automatique",True)
logger = getLogger(__name__)

#logger.exception("dddddd")

def toggle_autosave():
    if get_workbench().get_option("general.Enregistrement_automatique")==False:
        get_workbench().set_option("general.Eregistrement_automatique",True)
    else:
        get_workbench().set_option("general.Enregistrement_automatique",False)



def save_current(): 
    logger.info("entering save_current")
    get_workbench().after(10000 , save_current)
    # schedule the next call first
    #scheduler.enter(2, 1, save_current, (scheduler,))
    try:
        editor = get_workbench().get_editor_notebook().get_current_editor()
    except:
        return
    logger.info("editor exists")

    filename = editor.get_filename(False)
    if not filename:
        return
    logger.info("filename exists")
    if editor.is_modified() and  get_workbench().get_option("general.Enregistrement_automatique"):
        filename = editor.save_file()
    

def load_plugin():
    
    get_workbench().add_command(
        "toggle_autosave",
        "file",
        tr("Enregistrement automatique"),
        flag_name="general.Enregistrement_automatique",
        handler=toggle_autosave
    )
    logger.info("running save_current")
    save_current()
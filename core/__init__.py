from . import context
from .blender import operators, ui, ui_context, user_pref, keymap

def startup():
    """Called when the app starts, initializes the core components."""
    user_pref.register()
    
    context.startup()
    
    operators.register()
    ui.register()
    ui_context.register()
    keymap.register()
    
def shutdown():
    """Called when the app shuts down, cleans up the core components."""
    ui.unregister()
    ui_context.unregister()
    operators.unregister()
    keymap.unregister()
    
    context.shutdown()
    
    user_pref.unregister()
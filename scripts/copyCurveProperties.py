#Script usado para copiar as propriedades de uma determinada curva para outra/s

import bpy

active_obj = bpy.context.object

for obj in bpy.context.selected_objects:
    if obj != active_obj:
     
	#propriedades copiadas
        obj.data.dimensions = active_obj.data.dimensions
        
        obj.data.extrude = active_obj.data.extrude
        
        obj.data.fill_mode = active_obj.data.fill_mode
        
        obj.data.bevel_depth = active_obj.data.bevel_depth
                
        
        
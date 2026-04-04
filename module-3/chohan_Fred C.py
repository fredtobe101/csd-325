mat = bpy.data.materials.new(name="BlackBoltSuit")
mat.use_nodes = True
nodes = mat.node_tree.nodes
nodes["Principled BSDF"].inputs['Base Color'].default_value = (0.02, 0.02, 0.08, 1) # dark blue/black
nodes["Principled BSDF"].inputs['Metallic'].default_value = 0.8
for obj in bpy.context.selected_objects:
    if obj.type == 'MESH':
        obj.data.materials.append(mat)
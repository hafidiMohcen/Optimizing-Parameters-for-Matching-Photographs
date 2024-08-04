import bpy
import json
import os

def read_parameters_from_file(file_path):
    with open(file_path, 'r') as file:
        params = json.load(file)
    print("Parameters read: ", params)
    return params

def update_float_parameter(current_parameter_str, params, node_group):
    if current_parameter_str in params:
        if current_parameter_str in node_group.inputs:
            print( current_parameter_str," input found. Current value:", node_group.inputs[current_parameter_str].default_value)
            node_group.inputs[current_parameter_str].default_value = params[current_parameter_str]
            print(current_parameter_str," input updated to:", params[current_parameter_str])
        else:
            print(current_parameter_str," input not found.")    

def update_vector_parameter(current_parameter_str, params, node_group):
    if current_parameter_str in params:
        if current_parameter_str in node_group.inputs:
            print( current_parameter_str," input found. Current value:", node_group.inputs[current_parameter_str].default_value)
            node_group.inputs[current_parameter_str].default_value = tuple(params[current_parameter_str])
            print(current_parameter_str," input updated to:", params[current_parameter_str])
        else:
            print(current_parameter_str," input not found.")    


def update_material_parameters(params):
    mat = bpy.data.materials.get('basicWoodMat')
    if not mat:
        print("Material not found.")
        return
    print("Material found.")

    node_group = None
    for node in mat.node_tree.nodes:
        if node.type == 'GROUP' and (node.node_tree.name == 'basicWoodNodeGroupN' or node.label == 'basicWoodNodeGroupL'):
            node_group = node
            break
    
    if not node_group:
        print("Node group not found.")
        return
    print("Node group found.")


    current_parameter_str = 'woodAge'
    update_float_parameter(current_parameter_str, params, node_group)

    current_parameter_str = 'waveDistortion'
    update_float_parameter(current_parameter_str, params, node_group)

    current_parameter_str = 'knotPosition'
    update_vector_parameter(current_parameter_str, params, node_group)



file_path = 'parameters.json'
parameters = read_parameters_from_file(file_path)
update_material_parameters(parameters)

blend_file_path = bpy.data.filepath
directory = os.path.dirname(blend_file_path)
output_path = os.path.join(directory, 'imageOut.png')
bpy.context.scene.render.filepath = output_path
print("Rendering to:", output_path)

bpy.ops.render.render(write_still=True)

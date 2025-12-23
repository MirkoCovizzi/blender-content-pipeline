import bpy
import sys
import os

print("\nDefold Pipeline: Split GLTF")
print("-------------------------------")

def split_gltf(path, outpath):
    bpy.ops.object.delete()
    bpy.ops.import_scene.gltf(filepath = path)

    os.makedirs(outpath, exist_ok=True)

    for x in bpy.context.scene.objects:
        if not x.type == 'MESH':
            continue
        bpy.ops.object.select_all(action='DESELECT')
        x.select_set(True)
        file_path = os.path.join(outpath, "{}.gltf".format(x.name))

        # Blender Python API >= 4.2.0 does not support `export_colors` input parameter
        if bpy.app.version[0] * 10 + bpy.app.version[1] >= 42:
            bpy.ops.export_scene.gltf(filepath         =  file_path,
                                      use_selection    = True,
                                      export_format    = 'GLB',
                                      export_materials = 'NONE',
                                      export_tangents  = True)
        else:
            bpy.ops.export_scene.gltf(filepath         =  file_path,
                                      use_selection    = True,
                                      export_format    = 'GLB',
                                      export_materials = 'NONE',
                                      export_tangents  = True,
                                      export_colors    = True)

gltf_src = sys.argv[-2]
gltf_out = sys.argv[-1]

split_gltf(gltf_src, gltf_out)

print("-------------------------------")

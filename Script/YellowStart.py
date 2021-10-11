import unreal
import random 
import time
import AssetFunctions


#Load Textures and Static Mesh
texture_D_task = AssetFunctions.buildImportTask('D:/Users/Efren/Documents/GitHub/TVProject2/ToImport/Textures/T_YellowObject_01_D.TGA', '/Game/YellowObjects/Assets/Textures')
texture_N_task = AssetFunctions.buildImportTask('D:/Users/Efren/Documents/GitHub/TVProject2/ToImport/Textures/T_YellowObject_01_N.TGA', '/Game/YellowObjects/Assets/Textures')
texture_PRB_task = AssetFunctions.buildImportTask('D:/Users/Efren/Documents/GitHub/TVProject2/ToImport/Textures/T_YellowObject_01_PBR.TGA', '/Game/YellowObjects/Assets/Textures')
static_mesh_task = AssetFunctions.buildImportTask('D:/Users/Efren/Documents/GitHub/TVProject2/ToImport/Meshes/YellowObject.FBX', '/Game/YellowObjects/Assets/Meshes', AssetFunctions.buildStaticMeshImportOptions())

#AssetFunctions.executeImportTasks([texture_D_task, texture_N_task, texture_PRB_task, static_mesh_task])
#AssetFunctions.executeImportTasks([static_mesh_task])


#instances of unreal classes
system_lib = unreal.SystemLibrary()
editor_util = unreal.EditorUtilityLibrary()
editor_level_lib = unreal.EditorLevelLibrary()
string_lib = unreal.StringLibrary()

#get all actors
actors = editor_level_lib.get_all_level_actors()

for actor in actors:
    actor_name = system_lib.get_object_name(actor)

    #check if is BP_PlanarProjection
    if string_lib.contains(actor_name,"BP_PlanarProjection", use_case=False):
        bp_gc = unreal.load_object(None, "/Game/YellowObjects/Blueprints/BP_PlanarProjection.BP_PlanarProjection_C")
        bp_cdo = unreal.get_default_object(bp_gc)
        #bp_cdo.set_editor_property("ClipPath", "./Movies/Clip1")
        bp_cdo.set_editor_property("YellowObjectNum",2)
        bp_cdo.set_editor_property("bBackground", 1)
        bp_cdo.set_editor_property("bMask", 0)
        bp_cdo.set_editor_property("bLight1", 1)
        bp_cdo.set_editor_property("bLight2", 1)
        bp_cdo.set_editor_property("bRotate", 0)
        bp_cdo.set_editor_property("Rotation_X", 0)
        bp_cdo.set_editor_property("Rotation_Y", 0)
        bp_cdo.set_editor_property("Rotation_Z", 0.0)
        bp_cdo.set_editor_property("bCustomPosition", 1)
        bp_cdo.set_editor_property("Position_X", 0)
        bp_cdo.set_editor_property("Position_Y", 30)
        bp_cdo.set_editor_property("Position_Z", -10)
        bp_cdo.set_editor_property("bScale", 1)
        bp_cdo.set_editor_property("Scale_X", 0.7)
        bp_cdo.set_editor_property("Scale_Y", 0.7)
        bp_cdo.set_editor_property("Scale_Z", 0.7)
        bp_cdo.set_editor_property("bLightsRotation", 1)
        bp_cdo.set_editor_property("LightRotation_X", 1)
        bp_cdo.set_editor_property("LightRotation_Y", 1)
        bp_cdo.set_editor_property("LightRotation_Z", 1)
        bp_cdo.set_editor_property("bAnimateObject", 0)
        bp_cdo.set_editor_property("AnimStartPosition_X", 0)
        bp_cdo.set_editor_property("AnimStartPosition_Y", -10)
        bp_cdo.set_editor_property("AnimStartPosition_Z", 0)
        bp_cdo.set_editor_property("AnimEndPosition_X", 0)
        bp_cdo.set_editor_property("AnimEndPosition_Y", 40)
        bp_cdo.set_editor_property("AnimEndPosition_Z", 10)
        bp_cdo.set_editor_property("AnimIncrease", 0.005)
            
time.sleep(1)
unreal.EditorLevelLibrary.editor_play_simulate()

#unreal.SystemLibrary.quit_editor()

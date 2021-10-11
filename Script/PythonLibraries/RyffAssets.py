import unreal
import AssetFunctions


def importMyAssets_EXAMPLE():
    texture_D_task = AssetFunctions.buildImportTask('D:/Users/Efren/Documents/GitHub/TVProject2/ToImport/Textures/T_YellowObject_01_D.TGA', '/Game/YellowObjects/Assets/Textures')
    texture_N_task = AssetFunctions.buildImportTask('D:/Users/Efren/Documents/GitHub/TVProject2/ToImport/Textures/T_YellowObject_01_N.TGA', '/Game/YellowObjects/Assets/Textures')
    texture_PRB_task = AssetFunctions.buildImportTask('D:/Users/Efren/Documents/GitHub/TVProject2/ToImport/Textures/T_YellowObject_01_PBR.TGA', '/Game/YellowObjects/Assets/Textures')
    static_mesh_task = AssetFunctions.buildImportTask('D:/Users/Efren/Documents/GitHub/TVProject2/ToImport/Meshes/YellowObject.FBX', '/Game/YellowObjects/Assets/Meshes', AssetFunctions.buildStaticMeshImportOptions())
    
    #print AssetFunctions.executeImportTasks([texture_D_task, texture_N_task, texture_PRB_task, static_mesh_task])
    #print AssetFunctions.executeImportTasks([static_mesh_task])
    
    AssetFunctions.executeImportTasks([texture_D_task, texture_N_task, texture_PRB_task, static_mesh_task])
    AssetFunctions.executeImportTasks([static_mesh_task])
    #unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([texture_D_task])
    
    #sound_task = AssetFunctions.buildImportTask('C:/Path/To/Assets/Sound.WAV', '/Game/Sounds')
    #skeletal_mesh_task = AssetFunctions.buildImportTask('C:/Path/To/Assets/SkeletalMesh.FBX', '/Game/SkeletalMeshes', AssetFunctions.buildSkeletalMeshImportOptions())
    #animation_task = AssetFunctions.buildImportTask('C:/Path/To/Assets/Animation.FBX', '/Game/Animations', AssetFunctions.buildAnimationImportOptions('/Game/SkeletalMeshes/SkeletalMesh'))
    #print AssetFunctions.executeImportTasks([texture_task, sound_task, static_mesh_task, skeletal_mesh_task])
    
    # Not executing the animation_task at the same time of the skeletal_mesh_task because it look like it does not work if it's the case. Pretty sure it's not normal.
    
    #print AssetFunctions.executeImportTasks([animation_task])

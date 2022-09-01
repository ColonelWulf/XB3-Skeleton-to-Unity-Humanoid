import bpy

RenameTable = [
["J_hip","Hip"],
["J_spine_A","Spine"],
["J_spine_B","Chest"],
["J_shoulder_A_L","Left shoulder"],
["J_arm_A_L","Left arm"],
["J_elbow_L","Left elbow"],
["J_hand_L","Left wrist"],
["J_shoulder_A_R","Right shoulder"],
["J_arm_A_R","Right arm"],
["J_elbow_R","Right elbow"],
["J_hand_R","Right wrist"],
["J_neck","Neck"],
["J_head","Head"],
["J_thighs_L","Left leg"],
["J_thighs_R","Right leg"],
["J_leg_L","Left Knee"],
["J_leg_R","Right Knee"],
["J_foot_L","Left ankle"],
["J_foot_R","Right ankle"]
]
ReparentTable = [
["Left elbow","Left arm"],
["J_little_A_L","Left wrist"],
["J_ring_A_L","Left wrist"],
["Right elbow","right arm"],
["J_little_A_R","Right wrist"],
["J_ring_A_R","Right wrist"],
["Head","Neck"],
["Spine","Hip"],
]

CurrentArmature = bpy.context.active_object.data

for x in RenameTable:
    CB = CurrentArmature.edit_bones.get(x[0])
    if CB:
        CB.name = x[1]
for x in ReparentTable:
    CB = CurrentArmature.edit_bones.get(x[0])
    DB = CurrentArmature.edit_bones.get(x[1])
    if CB and DB:
        CB.parent = DB
        
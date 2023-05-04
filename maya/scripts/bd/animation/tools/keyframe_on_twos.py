import maya.cmds as cmds
import maya.mel as mel


def set_keyframes_every_two_frames(remove_in_between_keys=True):
    # Get the selected objects
    selected_objects = cmds.ls(selection=True)

    if not selected_objects:
        cmds.warning("No objects selected. Please select objects to set keyframes.")
        return

    # Get the active time control
    time_control = mel.eval(
        "global string $gPlayBackSlider; string $tempString = $gPlayBackSlider;"
    )

    # Get the start and end frames of the selected timeline region
    selected_range = cmds.timeControl(time_control, query=True, rangeArray=True)
    selected_start = selected_range[0]
    selected_end = selected_range[1]

    # Set keyframes every 2 frames for the selected objects and remove in-between keys if the option is set
    for obj in selected_objects:
        for frame in range(int(selected_start), int(selected_end) + 1):
            if (frame - int(selected_start)) % 2 == 0:
                cmds.currentTime(frame)
                cmds.setKeyframe(obj, insert=True)
            elif (
                remove_in_between_keys
                and cmds.keyframe(
                    obj, time=(frame, frame), query=True, keyframeCount=True
                )
                > 0
            ):
                cmds.cutKey(obj, time=(frame, frame))

        cmds.keyTangent(obj, outTangentType="step", t=(selected_start, selected_end))

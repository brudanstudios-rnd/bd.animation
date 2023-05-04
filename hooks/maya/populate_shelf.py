from maya import cmds

from bd.animation.tools.keyframe_on_twos import set_keyframes_every_two_frames


def _add_shelf_buttons(shelf, logger):
    if not shelf.endswith("BDAnimation"):
        return

    cmds.shelfButton(
        label="Keyframe On Twos",
        image="keyframe_on_twos.svg",
        parent=shelf,
        command=set_keyframes_every_two_frames,
        sourceType="python",
    )


def register(registry):
    registry.add_hook("bd.maya.add_shelf_buttons", _add_shelf_buttons)

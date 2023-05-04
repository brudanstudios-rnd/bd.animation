name = "bd.animation"

version = "0.0.1"

build_command = "python -m rezutil build {root} --ignore backup"
private_build_requires = ["rezutil"]

requires = []


def commands():
    if ".maya" in request:
        env.BD_HOOKPATH.prepend("{root}/hooks/maya")
        env.MAYA_SCRIPTS_PATH.append("{root}/maya/scripts")
        env.PYTHONPATH.prepend("{root}/maya/scripts")
        env.XBMLANGPATH.append("{root}/maya/icons")

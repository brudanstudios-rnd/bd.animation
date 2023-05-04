from bd.shelf import create_shelf


def _create_animation_shelf(is_batch, logger):
    if is_batch:
        return

    logger.info("Creating BDAnimation shelf...")
    create_shelf("BDAnimation", logger)


def register(registry):
    registry.add_hook("bd.maya.userSetup.post_execute", _create_animation_shelf)

import stactools.core

from stactools.sentinel3.stac import create_item

__all__ = ["create_item"]

stactools.core.use_fsspec()


def register_plugin(registry):
    from stactools.sentinel3 import commands

    registry.register_subcommand(commands.create_sentinel3_command)


__version__ = "0.4.1"

import pystac
from .product_extension import PRODUCT_EXTENSION_HOOKS 

pystac.extensions.hooks.register_extension(PRODUCT_EXTENSION_HOOKS)
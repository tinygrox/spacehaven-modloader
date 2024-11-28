
import os
import shutil
from zipfile import ZipFile

import click
import ui.log

PATCHABLE_XML_FILES = [
    'library/haven',
    'library/texts',
    'library/animations',
    'library/textures',
]

PATCHABLE_CIM_FILES = ["library/%d.cim" % i for i in range(24)]

def extract(jarPath, corePath):
    """Extract library files from spacehaven.jar"""
    # ui.log.updateBackgroundState("Extracting game files")
    ui.log.updateBackgroundState("正在提取游戏文件")

    if not os.path.exists(corePath):
        os.mkdir(corePath)

    ui.log.log("  Extracting library from {} to {}...".format(jarPath, corePath))
    with ZipFile(jarPath, "r") as spacehaven:
        for file in set(spacehaven.namelist()):
            if file.startswith("library/") and not file.endswith("/"):
#                ui.log.log("    {}".format(file))
                spacehaven.extract(file, corePath)


def patch(jarPath, corePath, resultPath, extra_assets = None):
    """Patch spacehaven.jar with custom library files"""

    original = ZipFile(jarPath, "r")
    patched = ZipFile(resultPath, "w")
    
    # ui.log.updateBackgroundState("Merging vanilla files")
    ui.log.updateBackgroundState("正在合并原版文件")
    
    update_files = PATCHABLE_XML_FILES + PATCHABLE_CIM_FILES
    for file in set(original.namelist()):
        if not file.endswith("/") and not file in update_files:
            patched.writestr(file, original.read(file))
    
    original.close()
    
    # ui.log.updateBackgroundState("Merging modded files")
    ui.log.updateBackgroundState("正在合并已Mod的文件")
    
    if extra_assets:
        update_files += extra_assets
    for file in update_files:
        ui.log.log("  Merging modded {}...".format(file))
        patched.write(os.path.join(corePath, file.replace('/', os.sep)), file)

    patched.close()


import os

import ui.log

import loader.assets.annotate
import loader.assets.explode
import loader.assets.library


def extract(jarPath, corePath):
    """Extract and annotate game assets"""

    ui.log.log("Running extract & annotate")

    # ui.log.updateBackgroundState("Extracting game files")
    ui.log.updateBackgroundState("正在提取游戏文件")
    loader.assets.library.extract(jarPath, corePath)

    # ui.log.updateBackgroundState("Unpacking textures")
    ui.log.updateBackgroundState("正在解包贴图")
    loader.assets.explode.explode(corePath)

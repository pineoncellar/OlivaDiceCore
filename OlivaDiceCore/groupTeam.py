import OlivOS
import OlivaDiceCore

import json
import os


def releaseDir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

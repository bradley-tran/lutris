import os
import shutil

from lutris.util.wine.dll_manager import DLLManager
from lutris.util import system
from lutris.util.log import logger

class cncDdrawManager(DLLManager):
    name = "cnc-ddraw"
    human_name = "cnc-ddraw"
    managed_dlls = ("dxgi", "ddraw")
    managed_appdata_files = ["cnc_ddraw/ddraw.ini", "cnc_ddraw/cnc-ddraw config.exe"]
    releases_url = "https://api.github.com/repos/FunkyFr3sh/cnc-ddraw/releases"
    proton_compatible = True

    def enable(self):
        if not self.dll_exists("ddraw"):
            logger.warning("ddraw.dll not found!")
            directory = os.path.join(self.path, "x32")
            if not os.path.exists(directory):
                os.makedirs(directory)
            shutil.copy(os.path.join(self.path, "ddraw.dll"), directory)

        super().enable()

    def enable_dll(self, system_dir, arch, dll_path):
        super().enable_dll(system_dir, arch, dll_path)

        dll_dir = os.path.dirname(dll_path)
        source_dir = os.path.dirname(dll_dir)
        source_ini = os.path.join(source_dir, "ddraw.ini")
        if system.path_exists(source_ini):
            wine_file_path = os.path.join(system_dir, "ddraw.ini")
            if system.path_exists(wine_file_path):
                if not os.path.islink(wine_file_path):
                    # Backing up original version (may not be needed)
                    shutil.move(wine_file_path, wine_file_path + ".orig")
                else:
                    os.remove(wine_file_path)
            system.create_symlink(source_ini, wine_file_path)

        logger.warning("source_ini: %s, wine_file_path: %s", source_ini, wine_file_path)

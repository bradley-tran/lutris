from lutris.util.wine.dll_manager import DLLManager


class cncDdrawManager(DLLManager):
    name = "cnc_ddraw"
    human_name = "cnc-ddraw"
    managed_dlls = (
        "ddraw",
    )
    managed_appdata_files = ["cnc_ddraw/ddraw.ini"]
    releases_url = "https://api.github.com/repos/FunkyFr3sh/cnc-ddraw/releases"
    proton_compatible = True

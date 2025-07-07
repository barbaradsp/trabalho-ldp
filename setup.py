import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("main.py", base=base, target_name="Platformer.exe")]

build_options = {
    "packages": ["pygame"],
    "include_files": ["asset/"],
    "excludes": []
}

setup(
    name="Platformer",
    version="1.0",
    description="Meu jogo de plataforma 2D",
    options={"build_exe": build_options},
    executables=executables
)

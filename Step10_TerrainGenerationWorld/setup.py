import sys
import os
from cx_Freeze import setup, Executable

# Files and folders to include
files = [
    "images/icon.ico",
    "images/bg.png",               # Add bg.png explicitly
    'assets/',
    'meshes/',
    'shaders/',
    'world_objects/',
    'font/'
    'images/',                     # Already includes all other image files
    'camera.py',
    'frustum.py',
    'main.py',
    'noise.py',
    'player.py',
    'scene.py',
    'settings.py',
    'setup.py',
    'shader_program.py',
    'terrain_gen.py',
    'textures.py',
    'voxel_handler.py',
    'world.py'
]

# Target executable definition
target = Executable(
    script="pyvoxel.py",
    base="Win32GUI",
    icon="images/icon.ico"
)

# Setup configuration
setup(
    name="PYVOXEL",
    version="1.0",
    description="Voxel world",
    author="Shubhayu",
    options={"build_exe": {"include_files": files}},
    executables=[target]
)

import os
from pathlib import Path
import json

package_name = "mongodb_connector"

list_of_files = [".github/workflows/ci.yaml",
   "src/__init__.py",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/mongo_crud.py", 
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/unit/unit.py",
   "tests/integration/__init__.py",
   "tests/integration/int.py",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "experiments/experiments.ipynb" ]


for path in list_of_files:
    file_path = Path(path)
    dirpath , filename = os.path.split(file_path)

    if dirpath != "":
        os.makedirs(dirpath, exist_ok=True)
    
    if not os.path.exists(file_path):
        f = open(file_path,'w')
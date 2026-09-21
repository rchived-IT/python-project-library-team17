"""
Sets up the folder structure for the Library Management System project
(python-project-library-team17), matching the IT0206 course handbook's
expected layout (Section 8).

Usage:
  1. Place this file in the root of your cloned repo folder.
  2. Run:  python setup_structure.py
  3. Then: git add . && git commit -m "Set up project folder structure" && git push
"""

import os

folders = [
    "src/models",
    "src/repositories",
    "src/controllers",
    "src/views",
    "src/services",
    "src/exceptions",
    "src/utils",
    "database",
    "data/imports",
    "tests",
    "docs",
    "logs",
]

# Folders that need an __init__.py to be treated as Python packages
python_packages = [
    "src/models",
    "src/repositories",
    "src/controllers",
    "src/views",
    "src/services",
    "src/exceptions",
    "src/utils",
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    # Git doesn't track empty folders, so add a placeholder
    gitkeep_path = os.path.join(folder, ".gitkeep")
    if not os.path.exists(gitkeep_path):
        open(gitkeep_path, "w").close()
    print(f"Created: {folder}/")

for pkg in python_packages:
    init_path = os.path.join(pkg, "__init__.py")
    if not os.path.exists(init_path):
        open(init_path, "w").close()
    print(f"Added:   {pkg}/__init__.py")

# Top-level starter files (only created if they don't already exist)
starter_files = {
    "src/main.py": '"""Application entry point / menu loop."""\n\n\ndef main():\n    print("Library Management System")\n\n\nif __name__ == "__main__":\n    main()\n',
    "src/config.py": '"""App configuration & constants."""\n',
    "database/schema.sql": "-- CREATE TABLE statements go here\n",
    "requirements.txt": "",
}

for path, content in starter_files.items():
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write(content)
        print(f"Created: {path}")
    else:
        print(f"Skipped (already exists): {path}")

print("\nDone. Review the structure, then run:")
print('  git add . && git commit -m "Set up project folder structure" && git push')

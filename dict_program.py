# Python Program to safely Create a Nested Directory

from pathlib import Path

Path("I:/Python/new_dict/demo_dict").mkdir(parents=True, exist_ok=True)

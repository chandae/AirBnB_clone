#!/usr/bin/python3
# __init__.py

from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
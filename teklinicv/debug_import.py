import sys
import traceback

try:
    from teklinicv.cli.app import app
    print("Import successful!")
except Exception:
    traceback.print_exc()

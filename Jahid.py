import os, sys
os.system('git pull')
try:
    __import__("KING").Main()
except Exception as e:
    exit(str(e))

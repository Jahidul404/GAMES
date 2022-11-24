import os, sys
os.system('git pull')
try:
    __import__("FIRE").Main()
except Exception as e:
    exit(str(e))

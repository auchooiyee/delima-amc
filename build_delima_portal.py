import os
import json

dirs = [
    'assets/css',
    'assets/js',
    'assets/images',
    'assets/data',
    'pages',
    'google-sites-guide/embed-widgets'
]
for d in dirs:
    os.makedirs(d, exist_ok=True)

print("Directories verified!")

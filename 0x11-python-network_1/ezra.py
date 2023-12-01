#!/usr/bin/python3
""" this is ethiopia """

import shutil
import tempfile
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name) as html:
    pass
print (html)

LUA_HERDER = """-- by iElden
local LSM = LibStub("LibSharedMedia-3.0")\n
"""

import os

ls = []
for i in os.listdir("sounds"):
    name = i.removesuffix('.ogg').replace('_', ' ').capitalize()
    ls.append(fr"""LSM:Register("sound", "|cfffe7b2c{name}|r", [[Interface\Addons\EldenSound\sounds\{i}]])""")
with open("EldenSound.lua", 'w') as fd:
    fd.write(LUA_HERDER + '\n'.join(ls))
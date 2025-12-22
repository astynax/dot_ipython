print("loading plumbum: local, FG, BG")
from plumbum import local, FG, BG

print("loading rich: rprint, inspect")
from rich import print as rprint, inspect

print("loading icecream: ic")
from icecream import install as _icecream_install
# adds `ic` to the `builtins` module
_icecream_install()

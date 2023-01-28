from pathlib import Path
from .. import util

def run():
   util.cd(Path(__file__).parent)
   util.shell("../../loafer dummy")
   code, out = util.shell("./TheExpectedTestOutputDir/dummy/dummy")
   # see dummy.c
   assert code == 42
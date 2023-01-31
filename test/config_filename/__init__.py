from pathlib import Path
from .. import util

def run():
    util.cd(Path(__file__).parent)
    util.command_expect_output("../../loafer -C my_config_file.xml foo", "foo")

from pathlib import Path
from .. import util

def testcase_build_main1():
   util.shell("rm -rf ./out")
   util.shell("../../loafer -l main1")
   util.command_expect_output("out/main1/main1", "", 40)

def testcase_build_main2():
   util.shell("rm -rf ./out")
   util.shell("../../loafer -l main2")
   util.command_expect_output("out/main2/main2", "", 20)

def testcase_script_with_requires():
   util.shell("rm -rf ./out")
   util.command_expect_output("../../loafer prereq_main1_add1", "41\n")

def run():
   util.cd(Path(__file__).parent)
   testcase_build_main1()
   testcase_build_main2()
   testcase_script_with_requires()
from pathlib import Path
from .. import util


def testcase_scripts_by_tag():
    util.command_expect_output("../../loafer abcd_tag", "abcd")


def testcase_scripts_by_req_tag():
    util.command_expect_output("../../loafer reqs_abcd", "abcdreqs_abcd")


def testcase_requires_chain_b():
    util.command_expect_output("../../loafer rb", "rarb")


def testcase_requires_chain_c():
    util.command_expect_output("../../loafer rc", "rarbrc")


def run():
    util.cd(Path(__file__).parent)
    testcase_scripts_by_tag()
    testcase_scripts_by_req_tag()
    testcase_requires_chain_b()
    testcase_requires_chain_c()

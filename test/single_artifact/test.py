from pathlib import Path
from .. import util

def testcase_dry_compile():
   util.command_expect_output(
      "../../loafer --dry-run --compile foo",

      "gcc -c foo.c -o out/foo/foo.o\n"
   )

def testcase_dry_link():
   util.command_expect_output(
      "../../loafer --dry-run --link foo",

      "gcc -c foo.c -o out/foo/foo.o\n"
      "gcc -o out/foo/foo out/foo/foo.o\n"
   )

def testcase_dry_run():
   util.command_expect_output(
      "../../loafer --dry-run --run foo",

      "gcc -c foo.c -o out/foo/foo.o\n"
      "gcc -o out/foo/foo out/foo/foo.o\n"
      "out/foo/foo\n"
   )

def testcase_run():
   util.shell("rm -rf ./out")
   util.shell("../../loafer foo")
   util.command_expect_output("./out/foo/foo", "This is the expected output\n", 42)

def run():
   util.cd(Path(__file__).parent)
   testcase_dry_compile()
   testcase_dry_link()
   testcase_dry_run()
   testcase_run()
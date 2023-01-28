from pathlib import Path
from .. import util

def testcase_dry_compile():
   code, out = util.shell("../../loafer --dry-run --compile foo")
   expected = (
      "gcc -c foo.c -o out/foo/foo.o\n"
   )
   assert out == expected

def testcase_dry_link():
   code, out = util.shell("../../loafer --dry-run --link foo")
   expected = (
      "gcc -c foo.c -o out/foo/foo.o\n"
      "gcc -o out/foo/foo out/foo/foo.o\n"
   )
   assert out == expected

def testcase_dry_run():
   code, out = util.shell("../../loafer --dry-run --run foo")
   expected = (
      "gcc -c foo.c -o out/foo/foo.o\n"
      "gcc -o out/foo/foo out/foo/foo.o\n"
      "out/foo/foo\n"
   )
   assert out == expected

def testcase_run():
   util.shell("rm -rf ./out")
   util.shell("../../loafer foo")
   code, out = util.shell("./out/foo/foo")
   # see foo.c
   assert code == 42
   assert out == "This is the expected output\n"

def run():
   util.cd(Path(__file__).parent)
   testcase_dry_compile()
   testcase_dry_link()
   testcase_dry_run()
   testcase_run()
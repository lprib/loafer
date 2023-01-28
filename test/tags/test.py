from pathlib import Path
from .. import util

def build_applied_to_all():
   util.command_expect_output(
      "../../loafer -d appliedToAll",

      "gcc -c art1.c -o out/art1/art1.o cfall cf1 cfglobal\n"
      "gcc -o out/art1/art1 out/art1/art1.o lfall lf1 lfglobal\n"
      "out/art1/art1\n"
      "gcc -c art2.c -o out/art2/art2.o cfall cfart23tag cf2 cfglobal\n"
      "gcc -o out/art2/art2 out/art2/art2.o lfall clart23tag lf2 lfglobal\n"
      "out/art2/art2 runflag2and3\n"
      "gcc -c art3.c -o out/art3/art3.o cfall cfart23tag cf3 cfglobal\n"
      "gcc -o out/art3/art3 out/art3/art3.o lfall clart23tag lf3 lfglobal\n"
      "out/art3/art3 runflag2and3\n"
   )

def build_art3():
   util.command_expect_output(
      "../../loafer -d art3",

      "gcc -c art3.c -o out/art3/art3.o cfall cfart23tag cf3 cfglobal\n"
      "gcc -o out/art3/art3 out/art3/art3.o lfall clart23tag lf3 lfglobal\n"
      "out/art3/art3 runflag2and3\n"
   )

def build_applied_to_art_23():
   util.command_expect_output(
      "../../loafer -d appliedToArt23",

      "gcc -c art2.c -o out/art2/art2.o cfall cfart23tag cf2 cfglobal\n"
      "gcc -o out/art2/art2 out/art2/art2.o lfall clart23tag lf2 lfglobal\n"
      "out/art2/art2 runflag2and3\n"
      "gcc -c art3.c -o out/art3/art3.o cfall cfart23tag cf3 cfglobal\n"
      "gcc -o out/art3/art3 out/art3/art3.o lfall clart23tag lf3 lfglobal\n"
      "out/art3/art3 runflag2and3\n"
   )

def run():
   util.cd(Path(__file__).parent)
   build_applied_to_all()
   build_art3()
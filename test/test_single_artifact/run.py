import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import test_common

test_common.shell("../../loafer -d test")
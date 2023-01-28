import subprocess
import sys

import test.single_artifact.test
import test.out_dir.test
import test.tags.test

test.single_artifact.test.run()
test.out_dir.test.run()
test.tags.test.run()
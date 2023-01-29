import subprocess
import sys

import test.single_artifact
import test.out_dir
import test.tags

test.single_artifact.run()
test.out_dir.run()
test.tags.run()
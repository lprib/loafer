import test.config_filename
import test.out_dir
import test.requires_chain
import test.single_artifact
import test.src_inc_script
import test.tags

# TODO verbose mode that can be easily turned on !
if __name__ == "__main__":
    test.config_filename.run()
    test.out_dir.run()
    test.requires_chain.run()
    test.single_artifact.run()
    test.src_inc_script.run()
    test.tags.run()
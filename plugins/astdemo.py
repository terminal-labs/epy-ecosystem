import uuid
import shutil

class Plugin:
    def process(self, apppath, outputdir):
        print("using mock plugin")
        shutil.copytree(apppath, outputdir)

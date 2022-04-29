import shutil
import uuid

from jobrunner.core import echo

class Plugin:
    def process(self, apppath, outputdir):
        print("using echo plugin")
        name ="raycaster"
        uuid_name = uuid.uuid4().hex
        jobid = 8
        echo(name, uuid_name, jobid, "loopback")

import shutil
import time
import uuid

import requests, zipfile, io
import requests

from jobrunner.core import send_to_runner, call_runner_track
from jobrunner.progressengine import updt

class Plugin:
    def process(self, apppath, outputdir):
        def __get_status():
            r = requests.get('http://127.0.0.1:8080/status/' + uuid_name)
            message = r.json()
            runs = message["runs"]
            count = message["count"]
            return runs, count
        print("using joblight plugin")
        name ="raycaster"
        #uuid_name = uuid.uuid4().hex
        uuid_name = "211edb17fcf94d5eb844f362d0dfe07a"
        print(uuid_name)
        jobid = 8
        send_to_runner(apppath, uuid_name, jobid)
        message = call_runner_track(uuid_name)

        uuid_name = message["uuid_name"]

        runs, count = __get_status()
        updt(runs, count)
        while count <= runs - 1:
            runs, count = __get_status()
            updt(runs, count)
            time.sleep(1)

        r = requests.get('http://127.0.0.1:8080/prepdelivery/' + uuid_name)
        message = r.json()


        r = requests.get('http://127.0.0.1:8080/builds/' + uuid_name)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("output")

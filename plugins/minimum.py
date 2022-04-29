import uuid
import shutil
from pathlib import Path

class Plugin:
    def process(self, apppath, outputdir):
        def __init():
            print("using minimum plugin")
            uuid_name = uuid.uuid4().hex
            print(uuid_name)
            return uuid_name

        def __prep_process(uuid_name):
            processes_dir = ".tmp/processes"
            process_dir = processes_dir + "/" + uuid_name
            Path(processes_dir).mkdir(parents=True, exist_ok=True)
            return process_dir

        def __convert(uuid_name, process_dir):
            print("doing things")

        def __start_process(uuid_name, process_dir):
            shutil.copytree(apppath, process_dir)

        def __finish_process(uuid_name, process_dir):
            shutil.copytree(process_dir, "output/" + uuid_name)

        uuid_name = __init()
        process_dir = __prep_process(uuid_name)
        __start_process(uuid_name, process_dir)
        __convert(uuid_name, process_dir)
        __finish_process(uuid_name, process_dir)

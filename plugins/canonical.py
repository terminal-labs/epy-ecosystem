from epython.plugin_helpers import init, prep_process, start_process, finish_process

class Plugin:
    def process(self, apppath, outputdir):
        def __init():
            return init()

        def __prep_process(uuid_name):
            return prep_process(uuid_name)

        def __start_process(apppath, process_dir):
            start_process(apppath, process_dir)

        def __finish_process(uuid_name, process_dir):
            finish_process(uuid_name, process_dir)

        def __convert(uuid_name, process_dir):
            print("doing things")

        uuid_name = __init()
        process_dir = __prep_process(uuid_name)
        __start_process(apppath, process_dir)
        __convert(uuid_name, process_dir)
        __finish_process(uuid_name, process_dir)

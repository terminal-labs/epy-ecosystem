import uuid

class Plugin:
    def process(self, apppath, outputdir):
        print("using mock plugin")
        uuid_name = "211edb17fcf94d5eb844f362d0dfe07a"
        print(uuid_name)
        print("move input dir to .tmp/processes/211edb17fcf94d5eb844f362d0dfe07a")
        print("do things to the dir in the processes dir")
        print("export your work to the output dir")

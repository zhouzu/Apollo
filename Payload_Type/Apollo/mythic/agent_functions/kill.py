from CommandBase import *
import json


class KillArguments(TaskArguments):

    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {
            "pid": CommandParameter(name="PID", type=ParameterType.Number)
        }

    async def parse_arguments(self):
        if len(self.command_line) == 0:
            raise Exception("No PID given.")
        if self.command_line[0] == "{":
            self.load_args_from_json_string(self.command_line)
        else:
            try:
                int(self.command_line)
            except:
                raise Exception("Failed to parse integer PID from {}".format(self.command_line))
            self.add_arg("pid", int(self.command_line), ParameterType.Number)
        

class killCommand(CommandBase):
    cmd = "kill"
    needs_admin = False
    help_cmd = "kill [pid]"
    description = "Kill a process specified by [pid]"
    version = 1
    is_exit = False
    is_file_browse = False
    is_process_list = False
    is_download_file = False
    is_upload_file = False
    is_remove_file = False
    author = "@djhohnstein"
    argument_class = KillArguments
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass
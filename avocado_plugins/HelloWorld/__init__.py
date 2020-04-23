from avocado.core.output import LOG_JOB
from avocado.core.plugin_interfaces import CLICmd


class HelloWorld(CLICmd):

    name = 'hello'
    description = 'The classical Hello World! plugin example.'

    def run(self, args):
        LOG_JOB.info(self.description)

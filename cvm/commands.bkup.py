class BaseCommand:
    name = None
    description = None
    aliases = []

    def __init__(self, subparser):
        parser = subparser.add_parser(self.name, aliases=self.aliases)
        self.add_arguments(parser)
        parser.set_defaults(action=self.handle)
    
    def handle(self, *args, **kwargs):
        raise NotImplementedError

    def add_arguments(self, parser):
        raise NotImplementedError

class Init(BaseCommand):
    name = 'init'
    aliases = ['i']

    def handle(self, args):
        print("I AM IN INIT")
    
    def add_arguments(self, parser):
        parser.add_argument('--foo')

class Status(BaseCommand):

    name = 'status'
    description = 'wat it be doing'
    aliases = ['s']

    def handle(self, args):
        print("I AM IN STATUS")
    
    def add_arguments(self, parser):
        parser.add_argument('--bar')
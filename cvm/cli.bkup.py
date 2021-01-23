import argparse
from cvm import commands

def default_action(args):
    print(args)

def main():

    parser = argparse.ArgumentParser('cvm')
    parser.add_argument(
        '--version',
        action='store_true',
        help='Shows the current version'
    )
    parser.set_defaults(action=default_action)

    subparser = parser.add_subparsers(dest='cmd')

    commands.Init(subparser)
    commands.Status(subparser)

    args = parser.parse_args()
    args.action(args)
    


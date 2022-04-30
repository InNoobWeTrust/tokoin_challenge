from argparse import ArgumentParser, Namespace
from pytermgui.pretty import print


def parse_arguments() -> Namespace:
    """Parse command line arguments"""

    parser = ArgumentParser()
    parser.add_argument('-m', '--mode', help='Search mode', choices=['user', 'ticket', 'organization'])
    parser.add_argument('-s', '--term', help='Search term')
    parser.add_argument('-f', '--field', help='Field to search for')

    return parser.parse_args()

def main():
    args = parse_arguments()
    print(f'Script works. Arguments: ', end='');
    print(args)

"""
nvimex

Usage:
    nvimex <command>
    nvimex <command> [<args> ...] [-a <address>] [-w]

Arguments:
    <command> The neovim command to run.
    <args>    The args for the command

Options:
    -h, --help               Show this screen
    -a <address> --address=<address>   Sets the neovim instance [default: $NVIM_LISTEN_ADDRESS]
    -w --wipe-current  Wipes current buffer after execution.
"""

from os import environ
from docopt import docopt

from neovim import attach


def main():
    arguments = docopt(__doc__)

    address = arguments['--address']

    if address == '$NVIM_LISTEN_ADDRESS':
        address = environ.get('NVIM_LISTEN_ADDRESS')

    if not address:
        exit('No neovim instance found')

    nvim = attach('socket', path=address)
    last_buffer = nvim.current.buffer.number

    command = [arguments['<command>']] + arguments['<args>']

    output = nvim.command_output(' '.join(command))

    if arguments['--wipe-current']:
        nvim.command('bw! %s' % last_buffer)

    return output


if __name__ == '__main__':
    print main()

import argparse
from typing import TextIO
from commands import *
from constants import *
from registry import Registry


"""
Program to automate the process of adding and removing software packages. This program generates an output text
in response to an input file containing a set of instructions

"""
__author__ = "Jorge Arévalo"
__version__ = "0.1.0"
__maintainer__ = "Jorge Arévalo"
__email__ = "jorgeas80@gmail.com"
__status__ = "Alpha"


def handle_args():
    """
    Handle input arguments
    """
    parser = argparse.ArgumentParser(
        description="Dependency manager"
    )
    parser.add_argument(
        dest="file_name",
        type=str,
        help="Input file path"
    )

    return parser.parse_args()


def freadline(fp: TextIO, cb: CommandBuilder, fixed_length=FIXED_LINE_LENGTH) -> BaseCommand:
    """
    Function to read a row from the source file and transform it in a command plus an optional list of arguments.
    @param fp: File pointer
    @returns a command instance
    """
    line_read = fp.readline().split()

    if not line_read:
        raise StopIteration

    if len(line_read) > fixed_length:
        line_read = line_read[0:fixed_length]

    # No type validation here, command should include type validation
    command_name = line_read[0].upper()
    command_item = line_read[1] if len(line_read) > 1 else None
    command_args = line_read[2:] if len(line_read) > 2 else None

    # Build the command
    cmd = cb(command_name, command_item, command_args)

    return cmd


class CommandFileReader:
    """
        Reader over a file with the expected command syntax. Built as iterator, to avoid problems with big files
    """

    def __init__(self, fp, **kwargs):
        self.fp = fp
        self.cb = kwargs.get('cb') or CommandBuilder()

    def __iter__(self):
        return self

    def _freadline(self):
        return freadline(self.fp, self.cb)

    def __next__(self):
        return self._freadline()


class CommandExecutor:
    def __init__(self, **kwargs):
        self.reg = kwargs.get('reg') or Registry()
        self.installed_packages = kwargs.get('installed_packages') or list()

    def install_package(self, pkg: str):
        # Package has no deps, just add it to installed packages
        if pkg not in self.reg.keys():
            self.installed_packages.append(pkg)
        # Package contains deps. So, install them first
        else:
            for dep in self.reg.get(pkg):
                self.install_package(dep)

        print(f"\t{pkg} successfully installed")

    def remove_package(self, pkg: str):
        # Package is still needed. Cannot be removed
        for cmd, deps in self.reg.items():
            if pkg in deps:
                print(f"{pkg} is still needed")
                return
        # Package is not a dep for any other one. It can be safely removed
        else:
            self.installed_packages.remove(pkg)
            print(f"{pkg} successfully removed")
            # Now check its dependencies
            if pkg in self.reg.keys():
                for subpkg in self.reg[pkg].deps:
                    if subpkg in self.installed_packages:
                        self.remove_package(subpkg)

    def execute(self, cmd: BaseCommand) -> str:
        # Set dependency list for this item
        if isinstance(cmd, DependCommand):
            # TODO: Check for circular deps (maybe in Registry class)
            self.reg[cmd.item] = set(cmd.deps)
        # List existing items
        elif isinstance(cmd, ListCommand):
            for pkg in self.installed_packages:
                print(f"\t{pkg}")
        elif isinstance(cmd, RemoveCommand):
            if cmd in self.installed_packages:
                self.remove_package(cmd.item)
        elif isinstance(cmd, InstallCommand):
            if cmd in self.installed_packages:
                print(f"\t{cmd} is already installed")
            else:
                self.install_package(cmd.item)
        # End, do nothing
        elif isinstance(cmd, EndCommand):
            pass
        else:
            raise Exception(f"Unknown command {cmd}")


if __name__ == "__main__":
    args = handle_args()

    fp = open(args.file_name, "r")
    command_file_reader = CommandFileReader(fp)
    command_executor = CommandExecutor()

    for command in command_file_reader:
        # First echoes the command
        print(command)

        # Now execute it
        command_executor.execute(command)

    fp.close()


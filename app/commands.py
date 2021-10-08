from typing import List
from dataclasses import dataclass


@dataclass
class BaseCommand:
    name: str
    # TODO: uppercase validation for name


@dataclass
class ListCommand(BaseCommand):
    def __init__(self):
        self.name = "LIST"


@dataclass
class InstallCommand(BaseCommand):
    item: str

    def __init__(self, **kwargs):
        self.name = "INSTALL"


@dataclass
class RemoveCommand(BaseCommand):
    item: str

    def __init__(self, item_value):
        self.name = "REMOVE"
        self.item = item_value


@dataclass
class EndCommand(BaseCommand):
    def __init__(self):
        self.name = "END"


@dataclass
class DependCommand(BaseCommand):
    item: str
    deps: List[str]

    def __init__(self, item_value, deps_value):
        self.name = "DEPEND"
        self.item = item_value
        self.deps = deps_value


# Rusty builder
class CommandBuilder:
    def __call__(self, cmd: str, item: str, deps: List[str] = None):
        if cmd.upper() == 'LIST':
            return ListCommand()
        elif cmd.upper() == 'END':
            return EndCommand()
        elif cmd.upper() == 'INSTALL':
            return InstallCommand(item)
        elif cmd.upper() == 'REMOVE':
            return RemoveCommand(item)
        elif cmd.upper() == 'DEPEND':
            return DependCommand(item, deps)
        else:
            raise Exception('Wrong command')

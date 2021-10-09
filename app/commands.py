from typing import List
from dataclasses import dataclass


@dataclass
class BaseCommand:
    name: str

    def __str__(self):
        return self.name.upper()


@dataclass
class ListCommand(BaseCommand):
    def __init__(self):
        self.name = "LIST"


@dataclass
class InstallCommand(BaseCommand):
    item: str

    def __init__(self, item_value):
        self.name = "INSTALL"
        self.item = item_value

    def __str__(self):
        return f"{self.name.upper()} {self.item}"


@dataclass
class RemoveCommand(BaseCommand):
    item: str

    def __init__(self, item_value):
        self.name = "REMOVE"
        self.item = item_value

    def __str__(self):
        return f"{self.name.upper()} {self.item}"


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

    def __str__(self):
        return f"{self.name.upper()} {self.item} {' '.join(self.deps)}"


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

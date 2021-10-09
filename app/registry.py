from typing import MutableMapping, Iterator


class Registry(MutableMapping[str, set]):
    store: MutableMapping[str, set]

    def __init__(
        self,
        store: MutableMapping[str, set] = None
    ):
        self.store = store or {}

    def __getitem__(self, k: str) -> set:
        return self.store[k]

    def __len__(self) -> int:
        return len(self.store)

    def __iter__(self) -> Iterator[str]:
        return iter(self.store)

    def __setitem__(self, key: str, value: set):
        self.store[key] = value

    def __delitem__(self, key: str):
        del self.store[key]

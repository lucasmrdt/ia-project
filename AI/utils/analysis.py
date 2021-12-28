from typing import DefaultDict, Iterable


class _Analysis():
    count = DefaultDict(int)

    def count_iterations(self, name, iterable: Iterable):
        for it in iterable:
            self.count[name] += 1
            yield it

    def get_count(self, name):
        return self.count[name]

    def reset_count(self, name):
        self.count[name] = 0

    def reset_all(self):
        self.count = DefaultDict(int)

    def get_all_counts(self):
        return sum(self.count.values())


Analysis = _Analysis()

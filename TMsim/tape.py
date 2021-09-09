class Tape:

    moves = {'S': lambda head: head,
             'R': lambda head: head+1,
             'L': lambda head: head-1}

    def __init__(self):
        self.head = 0
        self.cells = {self.head-1: '_',
                      self.head: '>',
                      self.head+1: '_'}

    def __repr__(self):
        symbols = [self.cells[i] if i != self.head else '|' + self.cells[i]
                   for i in range(self.min_head, self.max_head+1)]
        return '..|' + '|'.join(symbols) + '|..'

    @property
    def min_head(self):
        return min(list(self.cells.keys()))

    @property
    def max_head(self):
        return max(list(self.cells.keys()))

    def _blank_first_cell(self):
        first = self.min_head
        if self.cells[first] != '_':
            self.cells[first-1] = '_'

    def _blank_last_cell(self):
        last = self.max_head
        if self.cells[last] != '_':
            self.cells[last+1] = '_'

    def move(self, key):
        self.head = self.moves[key](self.head)

    def read(self):
        return self.cells[self.head]

    def write(self, symbol):
        self.cells[self.head] = symbol
        self._blank_first_cell()
        self._blank_last_cell()

from TMsim.parsing import parse_text, get_delta_dict
from TMsim.tape import Tape


class TuringMachine:

    init_state = 'Qinit'
    halt_states = {'Qhalt', 'Qaccept', 'Qreject'}

    def __init__(self, num_tapes, alphabet, states, transition_func):
        self.num_tapes = num_tapes
        self.alphabet = alphabet
        self.states = states
        self.transition_func = transition_func
        self._initialize()

    def __repr__(self):
        class_name = self.__class__.__qualname__
        params = list(self.__init__.__code__.co_varnames)
        params.remove('self')
        params.remove('transition_func')
        args = '\n'.join([f'\t{key} = {getattr(self, key)}' for key in params])
        return f'{class_name}(\n{args}\n)'

    @classmethod
    def from_txt(cls, filepath):
        with open(filepath) as file:
            lines = file.readlines()
        num_tapes, alphabet, states, transitions = parse_text(lines)
        transition_func = get_delta_dict(transitions, alphabet)
        return cls(num_tapes=num_tapes, alphabet=alphabet, states=states,
                   transition_func=transition_func)

    def _initialize(self):
        self._check_symbols()
        self._check_init_state()
        self.state = self.init_state
        self.steps = 0
        self.tapes = self._init_tapes()

    def _check_symbols(self):
        for symbol in {'>', '_'}:
            if symbol not in self.alphabet:
                raise ValueError(
                    f'The required symbol "{symbol}" is not in the alphabet!')

    def _check_init_state(self):
        if self.init_state not in self.states:
            raise ValueError(
                f'The required state "{self.init_state}" is not in the set of states!')

    def _init_tapes(self):
        empty_tapes = [Tape() for i in range(self.num_tapes)]
        return empty_tapes

    def load_input(self, string):
        for s in string:
            self.tapes[0].move(key='R')
            self.tapes[0].write(s)
        self.tapes[0].head = self.tapes[0].min_head+1

    def get_config(self):
        config = (self.state,)
        for tape in self.tapes:
            config += (tape.read(),)
        return config

    def execute(self, instructions):
        self.state = instructions[0]
        k = 1+self.num_tapes
        symbols = instructions[1:k]
        moves = instructions[k:]
        for i, s, m in zip(range(self.num_tapes), symbols, moves):
            self.tapes[i].write(symbol=s)
            self.tapes[i].move(key=m)

    def make_step(self):
        config = self.get_config()
        instructions = self.transition_func[config]
        self.execute(instructions)

    def run(self):
        while self.state not in self.halt_states:
            self.make_step()
            self.steps += 1

    def show_state(self, prefix=''):
        print(f'{prefix}state = {self.state}')

    def show_input(self):
        self.show_state(prefix='init_')
        print(f'input = {self.tapes[0]}')

    def show_output(self):
        self.show_state(prefix='final_')
        print(f'output = {self.tapes[-1]}')
        print(f'num_steps = {self.steps}')


if __name__ == '__main__':

    filepath = './../codes/1tape_inverse.txt'
    TM = TuringMachine.from_txt(filepath)

    input_string = '00011101'
    TM.load_input(input_string)

    TM.show_input()
    TM.run()
    TM.show_output()

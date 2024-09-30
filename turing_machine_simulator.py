"""
Simulating a Turing Machine
"""

class TuringMachine():

    """A virtual Turing Machine"""

    def __init__(self, alphabet, external_alphabet, states, transition_function):
        """initialize a TM from required data

        :alphabet: a list of symbols.
        :external_alphabet: a list of symbols.
        :states: a dictionary of states, keys for indexing, values for description.
        :transition_function: a dictionary, keys as (state, symbol), values as (state, symbol, movement)

        """
        self._alphabet = alphabet
        self._external_alphabet = external_alphabet
        self._states = states
        self._transition_function = transition_function
        self._tape = []
        self._current_state = 'q0'
        self._current_head = 0
        self._ifhalt = False
        self._step_counter = 0
        # add an initial state if not given by the user
        if 'q0' not in self._states:
            self._states['q0'] = 'initial state'
        # add a blank symbol if not given by the user
        if '' not in self._alphabet:
            self._alphabet.append('')
        
    def run_one_step(self):
        """run the TM for one step. 
        Check before running: if transition function not defined, then halt.
        Check when running: if the head bumps into the left boundary, then halt.

        """
        self._step_counter += 1
        print('Run step ' + str(self._step_counter) + ' at', end = '\n')
        print('State: ', self._current_state, end = '\n')
        print('Head: ', self._current_head, end = '\n')
        print('On tape: ', self._tape, end = '\n')
        # read symbol from current head 
        # If current head not on the tape list, expand the list
        symbol_read = ''
        if self._current_head < len(self._tape):
            symbol_read = self._tape[self._current_head]
        else:
            self._tape.append('')
        function_key = (self._current_state, symbol_read)
        if not function_key in self._transition_function:
            self._ifhalt = True
            print('Transition function undefined, TM halts.', end = '\n')
        else:
            (self._current_state, symbol_write, move) = self._transition_function[function_key]
            self._tape[self._current_head] = symbol_write
            self._current_head += move
            if self._current_head < 0:
                self._ifhalt = True
                print('Head bumps into left boundary, TM halts.', end = '\n')
            
    def run_machine(self, input_string):
        """Run the TM on an input string

        :input_string: a list
        :returns: the output of the machine
        """
        self._tape = input_string
        while not self._ifhalt:
            self.run_one_step()
            print('\n')
        print('The TM halts after ' + str(self._step_counter) + ' steps.', end = '\n')
        output_string = []
        for a in self._tape:
            if a not in self._external_alphabet:
                break
            output_string.append(a)
        print('Output: ', output_string)
        return output_string

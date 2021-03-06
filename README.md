# TMsimulator (in Python)

## What is a Turing machine?
A Turing machine is a mathematical model of computation that defines an abstract machine which manipulates symbols on a tape (or multiple tapes) according to a finite set of rules.
Despite the model's simplicity, given any computer algorithm, a Turing machine is always capable of simulating that algorithm's logic.

The Turing machine model can be formally described as a triple <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;(\Gamma,&space;Q,&space;\delta)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;(\Gamma,&space;Q,&space;\delta)" title="(\Gamma, Q, \delta)" /></a>:
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\Gamma" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\Gamma" title="\Gamma" /></a> is the alphabet, namely a finite set of symbols to read and write on the tapes (including the start symbol `>` and the blank symbol `_`);
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Q" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;Q" title="Q" /></a> is a finite set of machine's states (including the initial state `Qinit` and the final state `Qhalt`);
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\delta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\delta" title="\delta" /></a> is the transition function, namely a finite set of instructions the machine has to execute during the computation.

The machine operates on infinite memory tapes divided into discrete cells.
Each tape's head represents the position in that tape and it reads the symbol in the corresponding cell.
Then, based on the read symbol and the machine's present state, the TM executes the instruction according to the user-specified transitions function <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\delta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\delta" title="\delta" /></a>: for instance, the TM writes a symbol (e.g. the digit `0` or `1` taken from the alphabet <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\Gamma" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\Gamma" title="\Gamma" /></a>) in that cell and it either moves the tapes' heads one cell left (`L`) or right (`R`) or stay in the same (`S`).
Then, the process starts again and the TM proceeds iteratively to another instruction until the halting state is reached and the computation ends.

## The programming language
To explain how the Turing machine programming language works, we start from the following simple example:

```
NUM_TAPES = 1

ALPHABET = {0, 1, >, _}

STATES = {Qinit, Q1, Q2, Qhalt}

TRANSITION_FUNC =
(Qinit, >) --> (Q1, >, S)
(Q1, >) --> (Q1, >, R)
(Q1, 0) --> (Q1, 0, R)
(Q1, 1) --> (Q1, 1, R)
(Q1, _) --> (Q2, _, S)
(Q2, _) --> (Q2, _, L)
(Q2, 0) --> (Q2, 1, L)
(Q2, 1) --> (Q2, 0, L)
(Q2, >) --> (Qhalt, >, S)
```
This is the code (can be in a standard text file) for programming the Turing machine to compute the inverse of a binary string (e.g. from the input '000101',get the output '111010').

We start by passing the number of tapes in the machine (just 1 in this case).
Then we provide the alphabet (in this case containing just the digits `0` and `1`, and the start/blank symbols) and the set of machine's states needed in the computation.
Finally, we also define the transition function writing down each single instruction to be performed by the machine.

As an example, consider the first line:
```
(Qinit, >) --> (Q1, >, S)
```
This instruction can be interpreted as follows: "if the machine's present state is `Qinit` and the tape's head reads the symbol `>`, then (-->) change the machine's state to `Q1`, write the symbol `>` in the current cell, and stay (`S`) in the same cell (don't move the head)".


## Notes
- each empty tape is initialized as `..|_||>|_|..`, where we have an infinite sequence of blank symbols `_`, the start symbol `>` and the head placed over it (represented by the double vertical bar `||`);
- if `x` is the input string and `y` is the output string, the computation has to start in the configuration `..|_||>|x|_|..` in the input tape and finish in the configuration `..||>|y|_|`in the output tape;
- it is possible to use the symbol `*` in the transition function definition (even if it is not in the alphabet) to mean "whatever symbol in <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\Gamma" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\Gamma" title="\Gamma" /></a>".
- besides the halting state `Qhalt`, the TM terminates the computation also when it reaches one of the states `Qaccept` or `Qreject`: these states are used when the problem to be solved by the machine is to decide wheter the input string satisfies or not a particular property (e.g. accept only the binary string <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;s&space;\in&space;\{0,1\}^*" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;s&space;\in&space;\{0,1\}^*" title="s \in \{0,1\}^*" /></a> such that the number of 0s is equal to the number of 1s).

## Examples
To see a basic but complete working example about how to use the TM simulator, the Jupyter notebook [example.ipynb](https://github.com/SimoneGasperini/TMsimulator/blob/master/example.ipynb) is available in the repository.

For more code examples about how to program TMs to solve simple tasks, look in the [codes](https://github.com/SimoneGasperini/TMsimulator/tree/master/codes) directory of the repository.

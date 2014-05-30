*State Machines* keep track of the history of their inputs and use that history to calculate their output. In theory the history might not actually be used, but in the general vision of what a state machine is the history plus input gives output is the idea. Stat machines are useful in the modeling of a variety of systems.

State machines can execute in *continuous* or *discrete* time steps. In teh continuous case differential equations are used.

A state machine has a set of inputs S and maps those to a set of outputs O. However, you don't actually tend to keep track of the entire S. For example if a state machine was built to accumulate a counter, the state would be the sum of s and would be incremented by the input.
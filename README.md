# maze_flow

MAZE USING REINFORCEMENT LEARNING

In this project we use the Bellman equation which uses the state value function which is based on the concept of Dynamic Programming.

\[V(s) = \max(R(s, a) + \gamma V(s'))\]

- \(V(s)\): State value function of the current state
- \(V(s')\): State value function of the next state
- \(R(s, a)\): Reward obtained upon performing action \(a\) from state \(s\)
- \(\gamma\): Discount factor (It is a hyperparameter that determines the amount of importance we give to future rewards)


# maze_flow

MAZE USING REINFORCEMENT LEARNING

In this project we use the Bellman equation which uses the state value function which is based on the concept of Dynamic Programming.

\[V(s) = max(R(s, a) + gamma *V(s'))]

- \(V(s)\): State value function of the current state
- \(V(s')\): State value function of the next state
- \(R(s, a)\): Reward obtained upon performing action \(a\) from state \(s\)
- \(gamma\): Discount factor (It is a hyperparameter that determines the amount of importance we give to future rewards)

![image](https://github.com/fuggi11/maze_flow/assets/146570895/185d9da6-3989-44d8-b6b6-d17358a6158a)
WHITE: Agent   GREEN:Final Destination  BLUE:Wall  RED:Danger

VISUALIZATION OF VALUE FUNCTION MATRIX
![visualization](https://github.com/fuggi11/maze_flow/assets/146570895/67a20b2c-23fd-492e-a15d-4c5a20630826)
We visualize the matrix using the matplotlib library.The agent must move in the direction of more heat colour in order to reach the destination

RESULT
![gid2](https://github.com/fuggi11/maze_flow/assets/146570895/afe519cc-35ac-40ef-bd3d-1a71488579d7)
The purple blocks trace the pathway to the destination

PREREQUISITES:
Numpy
Pygame
Matplotlib


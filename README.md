# robotics

# Sokoban Puzzle Solver

## Overview

This project is dedicated to solving the Sokoban puzzle, represented as a grid containing various elements. The puzzle is loaded from an external file, and the state of the puzzle is constructed based on its configuration.

## Puzzle Elements
- **Walls (X)**: Impassable obstacles.
- **Goals (.)**: Target locations where diamonds should be placed.
- **Diamonds ($)**: The items that need to be pushed onto the goals.
- **Player (@)**: Represents the user-controlled entity.
- **Completed Diamonds (*)**: Indicates a diamond successfully placed on a goal.

## Goal State
The aim is to push all diamonds onto goals. For a successful solution:
- Every goal should be occupied by a diamond.
- Diamonds must be on distinct goal coordinates.

## Planning & Solution
The core of this project is the planning process to find a sequence of actions transitioning from the initial state to the goal state. We utilize a Breadth-First Search (BFS) algorithm to explore potential states, guaranteeing the shortest path to the goal.

Each action during BFS exploration is logged. This includes the player's movements and if a diamond is being pushed. Possible moves are represented by: 
- **'u'**: Up
- **'d'**: Down
- **'l'**: Left
- **'r'**: Right 

When a diamond is pushed, the move is appended with a 'p'. For example, a solution might look like `"u", "lp", "r", "d", "l", "up"`, indicating both player moves and diamond pushes.

Once the solution is found, it's printed on the console, providing a sequence of actions to solve the Sokoban puzzle. This serves as a guide for our robot's behaviors.


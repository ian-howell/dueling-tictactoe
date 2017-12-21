Dueling Tic-Tac-Toe
===================

This is a test project for learning some basic AI techniques, as well as
creating a groundwork for playing 2 AIs against eachother.

## Getting started

### What you'll need

* Python3

And that should be it

### How to use it

To run the AI, use the `./run.py` command. This will begin a game with an AI.
The player will control the Xs (and thus will go first), and the AI will
control the Os. Upon beginning the game, the user will see nothing but their
blinking cursor. At this point, the AI expects the user to enter a number from
0 to 8 inclusive. These numbers correspond to the positions on the Tic-Tac-Toe
board, such that the top-left cell is 0, the cell to its right is 1, and the
bottom-right cell is 8. Once the user has entered his selection, the AI will
then make his own selection, which will be output to the screen. When the game
ends (whether because someone won or there was a draw), then program will
abruptly end. Determining the winner can be done by physically drawing a
Tic-Tac-Toe board and replaying the responses.

As of this writing, the interface is very dry. This is by design, and it
will probably not see any improvements. I chose to do it this way to make the
AI design easier. If the script only ever expects a number and responds with a
number, then it is very easy to make it play against itself.

**To make the AI play against itself**, simply run `./duel.py`. This will invoke
2 subprocesses, which will play against each other. Upon completion, the
scripts will spit out 2 files. The first is called `results.txt`, and it
contains the final board configuration, as well as a statement of who won. The
second is a file called `log.txt`. It details the order in which moves were
made. If there is a `log.txt` file in the main directory, the user can run the
command `vis.py` to see a visualization of the gameplay.

Seq4SimPyLC is a sequence level control for SimPyLC
---------------------------------------------------

Here is the original project:
https://github.com/QQuick/SimPyLC/

Installation
------------

Installation for Windows, Linux is described in:
https://github.com/QQuick/SimPyLC/blob/master/simpylc/simpylc_howto.pdf

Usage
-----

1. Go to directory SimPyLC/simulations/one_armed_robot
2. Replace "world.py" and "control.py" and add this "sequence.py"
3. Click on world.py (or run world.py from the command line) - requires Python 3.10 installed
4. Force the "go" bit in the movement control
5. The one arm robot torso will then follow 3 predefined angles
6. "Reset" bit repeats the whole sequence

The robot is still very slow, but this makes it easier to follow the processes.

I might also try the suggested procedure to implement such a bang-bang control. 
You can find a good description in "SimPyLC_HowTo"

https://github.com/JEGGEgit/Seq4SimPyLC/demo/seq4simplctorsoangles.gif










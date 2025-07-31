Seq4SimPyLC is a sequence level control for SimPyLC
---------------------------------------------------

Here is the original project:
https://github.com/QQuick/SimPyLC/

Installation
------------

Installation for Windows, Linux is described in:
**"SimPyLC_HowTo"**
https://github.com/QQuick/SimPyLC/blob/master/simpylc/simpylc_howto.pdf

Usage
-----

1. Go to directory SimPyLC/simulations/one_armed_robot
2. Replace "world.py" and "control.py" and add this "sequence.py"
3. Click on world.py (or run world.py from the command line) - requires Python 3.10 installed
4. Force the "go" bit in the movement control
5. The one arm robot torso will then follow 3 predefined angles
6. "Reset" bit repeats the whole sequence

Demo
----

The robot torso movement is still very slow and has a lot of overshoot, but this makes it easier to follow the processes. 
And this is what it looks like:

![alt text](https://github.com/JEGGEgit/Seq4SimPyLC/blob/main/demo/seq4simplctorsoangles.gif?raw=true)
https://github.com/JEGGEgit/Seq4SimPyLC/blob/main/demo/seq4simplctorsoangles.gif

I might also try the suggested procedure to implement such a bang-bang control. 
You can find a good description in **"SimPyLC_HowTo"**

Notes
-----

The GUI operation as described (Mouse Wheel and PageUP/Dwn) didn't work for me. I'm running the simulation on Windows 10 64-bit (1511) with Python 3.10 32-bit.

And yes, in real life, I'm an old-school PLC programmer. I do simulations directly on the manufacturer's development environment, including Omron's Sysmac Studio.

But I also like Python and I like this concept of **SimPyLC** using Python with OpenGL visualisation.

- Enjoy What You Do -
- 














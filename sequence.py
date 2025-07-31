'''
====== Legal notices

Copyright (C) 2025 - JEGGE engineering @mje

This program is free software.
You can use, redistribute and/or modify it, but only under the terms stated in the QQuickLicense.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY, without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the QQuickLicense for details.

The QQuickLicense can be accessed at: http://www.qquick.org/license.html

__________________________________________________________________________


 THIS PROGRAM IS FUNDAMENTALLY UNSUITABLE FOR CONTROLLING REAL SYSTEMS !!

__________________________________________________________________________

It is meant for training purposes only.

Removing this header ends your license.
'''

import simpylc as sp

class Sequence (sp.Module):
    def __init__ (self):
        sp.Module.__init__ (self)
        
        self.page ('sequence control')
                      
        self.group ('torso setpoints', True)
        self.torAngSet01 = sp.Register (-45)        # simplified setpoints
        self.torAngSet02 = sp.Register (45)
        self.torAngSet03 = sp.Register (0)

        self.group ('current steps', True)
        self.torAngSet = sp.Register ()             # current setpoint
        self.Step_Nr = sp.Register ()               # current step
        self.RoundNr = sp.Register ()               # simplified feedback
 
        self.group ('sequence control', True)
        self.reset = sp.Marker ()
        self.resetPulse = sp.Oneshot ()
        self.torRound = sp.Marker ()
        self.torRoundPulse = sp.Oneshot ()
        self.torRoundTime = sp.Register (10.0)
        self.torRoundPeriod = sp.Register ()

 
    def input (self):
        self.part ('control feedback')
        self.torRound.mark (sp.world.control.torRound) # from control @mje
        
    def sweep (self):
        self.part ('torso sequence')       
        self.torRoundPeriod.set (self.torRoundPeriod + sp.world.period, self.torRound, 0)
        self.torRoundPulse.trigger (self.torRoundPeriod > self.torRoundTime)
        self.RoundNr.set (self.RoundNr + 1, self.torRoundPulse)

        self.resetPulse.trigger (self.reset)
        self.torRoundPeriod.set (0, self.resetPulse)
        self.RoundNr.set (0, self.resetPulse)

        self.Step_Nr.set (0, self.resetPulse)
         
        self.Step_Nr.set (1, self.Step_Nr == 0 and self.RoundNr == 1)
        self.Step_Nr.set (2, self.Step_Nr == 1 and self.RoundNr == 2)
        self.Step_Nr.set (3, self.Step_Nr == 2 and self.RoundNr == 3)

        self.torAngSet.set (self.torAngSet01, self.Step_Nr == 0)
        self.torAngSet.set (self.torAngSet02, self.Step_Nr == 1) 
        self.torAngSet.set (self.torAngSet03, self.Step_Nr == 2)
         
# EOF        
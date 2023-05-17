import numpy as np

class tone:
    def __init__(self,f,volume=1,t0=0,sustain=100,attack=0,release=0):
        t1=t0+attack
        t2=t1+sustain
        t3=t2+release
        def g(t):
            if t<t0:
                return 0
            elif t<t1:
                return f(t)*volume*(t-t0)
            elif t<t2:
                return f(t)*volume
            elif t<t3:
                return f(t)*volume*(t3-t)/release
            else:
                return 0
        self.f=g

    def get_f(self):
        return self.f

    def __add__(self,othertone):
        f=lambda t:self.get_f(t)+othertone.get_f(t)
        return tone(f)

import numpy as np

class tone:
    def __init__(self,f,volume=1,t0=0,sustain=20,attack=0,release=0):
        self.volume=volume
        self.f=f
        self.t0=t0
        self.t1=self.t0+attack
        self.t2=self.t1+sustain
        self.t3=self.t2+release

    def get(self,t):
        if t<self.t0:
            return 0
        elif t<self.t1:
            return self.f(t)*self.volume*(t-self.t0)
        elif t<self.t2:
            return self.f(t)*self.volume
        elif t<self.t3:
            return self.f(t)*self.volume*(self.t3-t)/release
        else:
            return 0

    def __add__(self,othertone):
        f=lambda t:self.get(t)+othertone.get(t)
        return tone(f)

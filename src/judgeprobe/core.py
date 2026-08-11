from __future__ import annotations
from dataclasses import dataclass
from typing import Callable

@dataclass(frozen=True)
class Pair:
    prompt:str
    a:str
    b:str

@dataclass(frozen=True)
class AuditResult:
    samples:int
    position_flip_rate:float
    a_win_rate:float
    b_win_rate:float
    tie_rate:float

def audit(judge:Callable[[str,str,str],str],pairs:list[Pair])->AuditResult:
    flips=aw=bw=ties=0
    for p in pairs:
        first=judge(p.prompt,p.a,p.b)
        swapped=judge(p.prompt,p.b,p.a)
        canonical_swapped={'A':'B','B':'A','TIE':'TIE'}[swapped]
        flips += first!=canonical_swapped
        aw += first=='A'; bw += first=='B'; ties += first=='TIE'
    n=max(1,len(pairs))
    return AuditResult(len(pairs),flips/n,aw/n,bw/n,ties/n)

def length_preferring_judge(prompt:str,a:str,b:str)->str:
    if len(a)==len(b):return 'A'  # deterministic tie-break exposes position bias too
    return 'A' if len(a)>len(b) else 'B'


def wilson_interval(successes:int,n:int,z:float=1.96)->tuple[float,float]:
    if n<=0:return (0.0,0.0)
    phat=successes/n; denom=1+z*z/n
    centre=(phat+z*z/(2*n))/denom
    margin=z*((phat*(1-phat)/n+z*z/(4*n*n))**.5)/denom
    return (max(0.0,centre-margin),min(1.0,centre+margin))

def position_bias_ci(judge:Callable[[str,str,str],str],pairs:list[Pair])->tuple[float,float]:
    r=audit(judge,pairs); return wilson_interval(round(r.position_flip_rate*len(pairs)),len(pairs))

def length_preference(judge:Callable[[str,str,str],str],pairs:list[Pair])->float:
    eligible=wins=0
    for p in pairs:
        if len(p.a)==len(p.b):continue
        eligible+=1; pick=judge(p.prompt,p.a,p.b)
        wins += (pick=='A' and len(p.a)>len(p.b)) or (pick=='B' and len(p.b)>len(p.a))
    return wins/max(1,eligible)

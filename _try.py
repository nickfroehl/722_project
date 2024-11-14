import pddlgym
from pddlgym.determinization import *
from pddlgym_planners.ff import FF
env = pddlgym.make("PDDLEnvRoboroom_nd-v0")
det_domain, d2nd = singlemax(env.domain)
obs,dbg = env.reset()
unit_planner = FF()
plan = unit_planner(det_domain,obs)

act0 = plan[0]
#print(f"act0: {act0}\n")
key0 = list(d2nd.keys())[0]
#print(f"key0: {key0}\n")
val0 = list(d2nd.values())[0]
#print(f"val0: {val0}\n")

# test if my patch to make pddlgym ACTUALLY support Probabilistic Effects finally works
obs,reward,done,trunc,dbg = env.step(act0)
# it does work! interesting enough, _select_operator already appears to take care of what I thought I'd need d2nd for
#       that said, I expect that if I ever determinize in a manner which generates separate action NAMES, e.g. move --> move1,move2, then I'll need to actually use d2nd and modify the NAME of the actions





import sys, os, shutil
import pddlgym
import pddlgym.determinization
from pddlgym_planners.ff import FF
from pddlgym_planners.planner import PlanningFailure
import rff_lib

### SETUP
#### CONSTS/MODE
istest = False
kwargs = {'operators_as_actions' : True, 'dynamic_action_space' : True}
determinize = pddlgym.determinization.singlemax
#### PROBLEM
domain_basename = "robowalk"
domain_ndname = f"{domain_basename}_nd"
nd_gym_name = f"PDDLEnv{domain_ndname.capitalize()}-v0"
# EXPECT THAT nd_gym_name WAS PREREGISTERED IN CURRENT_GYMDIR'S __init__.py
problem_idx = 0
domain_detname = f"{domain_basename}_det_{determinize.__name__}"
det_gym_name = f"PDDLEnv{domain_detname.capitalize()}-v0"

### OPERATION

# initialize the nondeterministic domain as a Gym environment
nd_env = pddlgym.make(nd_gym_name)
# perform a NON-in-place determinization of the domain, using the "singlemax" strategy
det_domain, d2nd = determinize(nd_env.domain, in_place=False)
# now, we have a determinized version, while 'nd_env' retains the original, probabilistic domain

# write the determinized domain out to a PDDL file
dstdir = "test_gymdir_1/pddl/"
det_domain.write(f"{dstdir}{domain_detname}.pddl")

# copy over the issue/problem (initial state) files. they should all be compatible
#   for now, assume no problem files are nondeterministic -- only the domain
srcproblemdir = f"{dstdir}{domain_ndname}/"
dstproblemdir = f"{dstdir}{domain_detname}/"
if not os.path.exists(dstproblemdir):
    os.makedirs(dstproblemdir)
for problemfilename in os.listdir(srcproblemdir):
    srcpath = os.path.join(srcproblemdir, problemfilename)
    dstpath = os.path.join(dstproblemdir, problemfilename)
    shutil.copy2(srcpath, dstpath)

# register this new determinized domain with PDDLGym
pddlgym.register_pddl_env(domain_detname, istest, kwargs)
# instantiate it
det_env = pddlgym.make(det_gym_name)

# prepare initial conditions
nd_env.fix_problem_index(problem_idx)
det_env.fix_problem_index(problem_idx)
nd_state,_ = nd_env.reset()
det_state,_ = det_env.reset()
assert(det_state == nd_state)

#print(f"det_domain.__dict__: {det_domain.__dict__}\n")
#print(f"det_env.domain.__dict__: {det_env.domain.__dict__}\n")

# Run single instance of unit planner
unit_planner = FF()
try:
    plan = unit_planner(det_domain,nd_state)
except PlanningFailure:
    print("Failure! Initial state is unsolveable.")
    sys.exit(1)

# Attempt to run plan; fail if ever diverges
done = False; i = 0
# l = nd_env.get_all_possible_transitions(plan[0], True)

"""
while not done:
    #print("do nd")
    nd_state,nd_reward,done,_,_ = nd_env.step(plan[i])
    #print("do det")
    det_state,det_reward,_,_,_ = det_env.step(plan[i])
    if (nd_state != det_state) or (nd_reward != det_reward):
        print(f"Execution diverged from plan at action #{i}: {plan[i]}!")
        # Set the state of the determinized environment equal to that of the true execution from the nondeterminized environment
        det_env.set_state(nd_state)
        # FF-Replan: attempt to re-plan
        print("Replanning...")
        try:
            plan = unit_planner(det_domain,nd_state)
        except PlanningFailure:
            print("Failure! Reached unsolveable state.")
            sys.exit(1)
        i = -1  # +1 at end of loop will reset us to 0
    i += 1

if (done):
    print("FF-Replan succeeded! Next, let's try RFF")
"""
nd_state,_ = nd_env.reset()
policy = rff_lib.rff(nd_state, det_env, nd_env, unit_planner)

print(f"RFF Planning finished: {policy}")
nd_state,_ = nd_env.reset()
done = False
while not done:
    if nd_state in policy:
        action = policy[nd_state]
        if action is None:
            print(f"Reached unsolveable state {nd_state} with RFF!")
            sys.exit(1)
        nd_state,nd_reward,done,_,_ = nd_env.step(action)
    else:
        print(f"Reached unknown state {nd_state} with RFF!")
        sys.exit(1)

print("RFF succeeded!")

### NOTES
# my determinization does work. interesting enough, _select_operator already appears to take care of what I thought I'd need d2nd for
#       that said, I expect that if I ever determinize in a manner which generates separate action NAMES, e.g. move --> move1,move2, then I'll need to actually use d2nd and modify the NAME of the actions





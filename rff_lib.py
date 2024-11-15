from collections import deque
from copy import deepcopy

# lib rff

N_ROLLOUTS = 50
DEPTH = 20
THRESH = 0.05
MAX_ITERS = 50

def rollout(s0, policy, nd_gym):
    lphi = 0.0
    for _ in range(N_ROLLOUTS):
        nd_gym.set_state(s0)
        state = s0
        done = False
        for i in range(DEPTH):
            if done or state not in policy:
                break
            state,_,done,_,_ = nd_gym.step(policy[state])
        if i< DEPTH and not done:  # left the policy
            lphi += 1
    return lphi / N_ROLLOUTS

def iteration(Q, policy, planner, det_gym, nd_gym):
    Q2 = deque()
    while Q:
        s = Q.popleft()
        try:
            plan = planner(det_gym.domain, s)
        except PlanningFailure:
            policy[s] = None
            continue
        #path = plan2path(s,policy,det_gym) # [(state,action)]
        s2 = s
        det_gym.set_state(s)
        for a in plan:
            if s2 not in policy:
                policy[s2] = a
            s2,_,_,_,_ = det_gym.step(policy[s2])
            nd_gym.set_state(s)
            for trans in nd_gym.get_all_possible_transitions(a):
                s3 = trans[0][0]
                if s3 not in policy and s3 not in Q and s3 not in Q2:
                    Q2.append(s3)
    return Q2

def rff(s0, det_gym, nd_gym, planner):
    # load, compute s0, or get it param idk

    Q = deque()
    pi = {}
    
    Q.append(s0)
    """
    There is no single coherent definition for RFF.
    The algorithm from the original publication is nonsense -- the loops don't work.
    The version provided in the textbook is a logical extension of the idea but cites no sources on any of the developments of the idea.
    So I'm taking liberties for ease of implementation.
    """
    i = 0
    while i < MAX_ITERS and Q:
        Q = iteration(Q, pi, planner, det_gym, nd_gym)
        p = rollout(s0, pi, nd_gym)
        if p < THRESH:
            break
        i += 1
        
    return pi

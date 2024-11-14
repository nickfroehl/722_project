"""
PDDL Determinization
by various methods
"""
from pddlgym.structs import (Type, Predicate, Literal, LiteralConjunction,
                             LiteralDisjunction, Not, Anti, ForAll, Exists,
                             ProbabilisticEffect, TypedEntity, ground_literal,
                             DerivedPredicate, NoChange)
import copy

"""
def singlemax(domain, return_copy=True):
    if return_copy:
        out = copy.deepcopy(domain)
    else:
        out = domain
    for op in out.operators.values():
        while isinstance(op.effects, ProbabilisticEffect):
            op.effects = op.effects.max()
    
    out.is_probabilistic = False
    return out


"""
def singlemax(domain, in_place=False):
    if in_place:
        out = domain
    else:
        out = copy.deepcopy(domain)
        det2ndet = {}   # mapping from determinized actions to original actions
    for op in out.operators.values():
        val = copy.deepcopy(op)  # value to which det2ndet shall resolve: the original nondeterministic operation
        while isinstance(op.effects, ProbabilisticEffect):
            op.effects = op.effects.max()
        key = op    # new determinized value
        if not in_place:
            det2ndet[key] = val
    out.is_probabilistic = False
    return (out if in_place else (out,det2ndet))
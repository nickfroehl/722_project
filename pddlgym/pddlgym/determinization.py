"""
PDDL Determinization
by various methods
"""
from pddlgym.structs import (Type, Predicate, Literal, LiteralConjunction,
                             LiteralDisjunction, Not, Anti, ForAll, Exists,
                             ProbabilisticEffect, TypedEntity, ground_literal,
                             DerivedPredicate, NoChange)
import copy

def singlemax_inplace_effect(eff):
    if isinstance(eff, LiteralConjunction):
            for i,lit in enumerate(eff.literals):
                eff.literals[i] = singlemax_inplace_effect(lit)
    if isinstance(eff, ProbabilisticEffect):
        eff = singlemax_inplace_effect(eff.max())
    return eff

def singlemax(domain, in_place=False):
    if in_place:
        out = domain
    else:
        out = copy.deepcopy(domain)
        det2ndet = {}   # mapping from determinized actions to original actions
    for op in out.operators.values():
        val = copy.deepcopy(op)  # value to which det2ndet shall resolve: the original nondeterministic operation
        
        # "inplace", but "this" might be a clone
        op.effects = singlemax_inplace_effect(op.effects)
        
        key = op    # new determinized value
        if not in_place:
            det2ndet[key] = val
    out.is_probabilistic = False
    return (out if in_place else (out,det2ndet))
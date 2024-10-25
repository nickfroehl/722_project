import pddlgym
from .rendering import *

# register each PDDL env
for env_name, kwargs in [
        ("sokoban", {'render' : sokoban_render})
]:
    other_args = {
        "raise_error_on_invalid_action": False,
    }
    kwargs.update(other_args)
    for is_test in [False, True]:
        pddlgym.register_pddl_env(env_name, is_test, kwargs)

# Custom environments
# NONE
import pddlgym
#from .rendering import *   # no rendering needed here

# register each PDDL env
for env_name, kwargs in [
        ("simple", {'operators_as_actions' : True,
                    'dynamic_action_space' : True}),
        ("roboroom_nd", {'operators_as_actions' : True,
                    'dynamic_action_space' : True}),
]:
    other_args = {
        "raise_error_on_invalid_action": False,
    }
    kwargs.update(other_args)
    for is_test in [False, True]:
        pddlgym.register_pddl_env(env_name, is_test, kwargs)

# Custom environments
# NONE
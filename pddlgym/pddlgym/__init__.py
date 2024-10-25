"""Gym environment registration"""

from . import core
from . import structs
from . import spaces

import matplotlib
# matplotlib.use("Agg")
from gym.envs.registration import register
import gym

import os, sys
import importlib

# by default, launch with the rendering, pddls, etc. of localdir
DEFAULT_GYMDIR = os.path.dirname(os.path.realpath(__file__))

# get env var CURRENT_GYM if it exists; otherwise, use the default
def current_gymdir():
    _current_gymdir = os.getenv("CURRENT_GYMDIR")
    return DEFAULT_GYMDIR if _current_gymdir is None else os.path.realpath(_current_gymdir)


# Save users from having to separately import gym
def make(*args, **kwargs):
    # env checker fails since obs is not an numpy array like object
    return gym.make(*args, disable_env_checker=True, **kwargs)

def register_pddl_env(name, is_test_env, other_args):
    dir_path = os.path.join(current_gymdir(), "pddl")
    domain_file = os.path.join(dir_path, "{}.pddl".format(name.lower()))
    gym_name = name.capitalize()
    problem_dirname = name.lower()
    if is_test_env:
        gym_name += 'Test'
        problem_dirname += '_test'
    problem_dir = os.path.join(dir_path, problem_dirname)

    register(
        id='PDDLEnv{}-v0'.format(gym_name),
        entry_point='pddlgym.core:PDDLEnv',
        kwargs=dict({'domain_file' : domain_file, 'problem_dir' : problem_dir,
                     **other_args}),
    )

# import `__init__.py` from `current_gymdir()` if non-default, else run this default

if current_gymdir() != DEFAULT_GYMDIR:
    print(f"Using $CURRENT_GYMDIR: {current_gymdir()}")
    
    """
    assert os.path.exists(current_gymdir()), "ERROR: Path $CURRENT_GYMDIR does not exist!"

    # I hate importlib; apparently importing from a path isn't possible because of namespace management
    # INCORRECT: importlib.import_module(current_gymdir()) # execute __init__.py therein

    renderingdir = os.path.join(current_gymdir(), "rendering")
    if os.path.exists(renderingdir):
        # importlib equivalent of 'from pddlgym.rendering import *'
        # INCORRECT: rendering = importlib.import_module(renderingdir)
        renderingspec = importlib.util.spec_from_file_location("rendering", os.path.join(renderingdir, "__init__.py"))
        rendering = importlib.util.module_from_spec(renderingspec)
        # Add it to sys.modules
        sys.modules["rendering"] = rendering
        renderingspec.loader.exec_module(rendering)

        for attrib,v in vars(rendering).items():
            print(f"attrib: {attrib}")
            globals()[attrib] = v
    else:
        print("WARNING: no subdirectory `rendering` of $CURRENT_GYMDIR; no rendering will be possible.")

    # Try to import the module AFTER rendering has already been resolved

    """
    # NONE OF THIS IS NECESSARY, JUST IMPORT RENDERING RELATIVELY IN YOUR __init__.py!

    """IMPORT GYMDIR"""
    # Create a module spec
    spec = importlib.util.spec_from_file_location("gymdir", os.path.join(current_gymdir(), "__init__.py"))
    # Create a module from the spec
    module = importlib.util.module_from_spec(spec)
    sys.modules["gymdir"] = module
    # Execute the module to load it
    spec.loader.exec_module(module)
    

else:   # execute default gymdir's initialization
    print(f"Using default gymdir: {DEFAULT_GYMDIR}")
    from . import tests
    from pddlgym.rendering import * # run default renderingdir's __init__

    """
    LOGIC TO REPLICATE IN ANY NON-DEFAULT $CURRENT_GYMDIR __init__.py,
    FOR ALL PDDL DEFINITIONS OF THAT GYMDIR
    """
    # START
    for env_name, kwargs in [
            ("gripper", {'operators_as_actions' : True,
                        'dynamic_action_space' : True}),
            ("easygripper", {'operators_as_actions' : True,
                            'dynamic_action_space' : False}),
            ("onearmedgripper", {'operators_as_actions' : True,
                                'dynamic_action_space' : False}),
            ("tinyonearmedgripper", {'operators_as_actions' : True,
                                    'dynamic_action_space' : False}),
            ("lifelong_tiny_gripper", {'operators_as_actions' : True,
                                    'dynamic_action_space' : False}),
            ("rearrangement", {'render' : rearrangement_render}),
            ("sokoban", {'render' : sokoban_render}),
            ("minecraft", {'render' : minecraft_render}),
            ("depot", {'operators_as_actions' : True,
                    'dynamic_action_space' : True}),
            ("baking", {}),
            ("blocks", {'render' : blocks_render}),
            ("derivedblocks", {'render' : blocks_render}),
            ("toomanyblocks", {'render' : blocks_render}),
            ("lifelong_blocks6", {'render' : blocks_render}),
            ("travel", {}),
            ("doors", {'render' : doors_render}),
            ("casino", {}),
            ("hanoi", {'render' : hanoi_render}),
            ("hanoi_operator_actions", {'render' : hanoi_render,
                                        'operators_as_actions' : True,
                                        'dynamic_action_space' : True}),
            ("tsp", {'render' : tsp_render}),
            ("tsp_operator_actions", {'render' : tsp_render,
                                    'operators_as_actions' : True,
                                    'dynamic_action_space' : True}),
            ("slidetile", {'render' : slidetile_render}),
            ("elevator", {}),
            ("ferry", {}),
            ("meetpass", {}),
            ("footwear", {'operators_as_actions' : True,
                        'dynamic_action_space' : True}),
            ("easyblocks", {'render' : blocks_render}),
            ("conditionalblocks", {'render' : blocks_render}),
            ("conditionalferry", {}),
            ("blocks_operator_actions", {'render' : blocks_render, 
                                        'operators_as_actions' : True,
                                        'dynamic_action_space' : True}),
            ("generated_blocks", {'render' : blocks_render, 
                                'operators_as_actions' : True,
                                'dynamic_action_space' : True}),
            ("blocks_medium", {'render' : blocks_render, 
                            'operators_as_actions' : True,
                            'dynamic_action_space' : True}),
            ("manyblocksnopiles", {'render' : blocks_render, 
                                'operators_as_actions' : True,
                                'dynamic_action_space' : True}),
            ("manyexplodingblockssmallpiles", {'render' : blocks_render,
                                            'operators_as_actions' : True,
                                            'dynamic_action_space' : True}),
            ("manyblockssmallpiles", {'render' : blocks_render, 
                                    'operators_as_actions' : True,
                                    'dynamic_action_space' : True}),
            ("manyblockssmallpilesnoclear", {'render' : blocks_render, 
                                    'operators_as_actions' : True,
                                    'dynamic_action_space' : True}),
            ("manyblockssmallpilesnohand", {'render' : blocks_render, 
                                    'operators_as_actions' : True,
                                    'dynamic_action_space' : True}),
            ("manyblockssmallpilesnoclearhand", {'render' : blocks_render, 
                                    'operators_as_actions' : True,
                                    'dynamic_action_space' : True}),
            ("quantifiedblocks", {'render' : blocks_render, 
                                'operators_as_actions' : True,
                                'dynamic_action_space' : True}),
            ("quantifiedblocks2", {'render' : blocks_render, 
                                'operators_as_actions' : True,
                                'dynamic_action_space' : True}),
            ("quantifiedblocks3", {'render' : blocks_render, 
                                'operators_as_actions' : True,
                                'dynamic_action_space' : True}),
            ("equalityblocks", {'operators_as_actions' : True,
                                'dynamic_action_space' : True}),
            ("equalityblocks2", {'operators_as_actions' : True,
                                'dynamic_action_space' : True}),
            ("manygrid", {'operators_as_actions' : True,
                        'dynamic_action_space' : True}),
            ("manylogistics", {'operators_as_actions' : True,
                            'dynamic_action_space' : True}),
            ("manymiconic", {'operators_as_actions' : True,
                            'dynamic_action_space' : True}),
            ("manygripper", {'operators_as_actions' : True,
                            'dynamic_action_space' : True}),
            ("manyferry", {'operators_as_actions' : True,
                        'dynamic_action_space' : True}),
            ("movie", {'operators_as_actions' : True,
                    'dynamic_action_space' : True}),
            ("glibblocks", {'render' : blocks_render}),
            ("glibrearrangement", {'render' : rearrangement_render}),
            ("glibdoors", {'render' : doors_render}),
            ("tireworld", {'render' : tireworld_render}),
            ("manytireworld", {'render' : tireworld_render,
                            'operators_as_actions' : True,
                            'dynamic_action_space' : True}),
            ("fridge", {'operators_as_actions' : True,
                        'dynamic_action_space' : True}),
            ("snake", { 'render' : snake_render,
                    'operators_as_actions' : True,
                    'dynamic_action_space' : True}),
            ("river", {}),
            ("explodingblocks", {'render' : exploding_blocks_render}),
            ("newspapers", {'operators_as_actions' : True,
                            'dynamic_action_space' : True}),
            ("easynewspapers", {'operators_as_actions' : True,
                            'dynamic_action_space' : True}),
            ("trapnewspapers", {'operators_as_actions' : True,
                            'dynamic_action_space' : True}),
            ("hiking", {'operators_as_actions' : True,
                        'dynamic_action_space' : True,
                        'render' : hiking_render}),
            ("maze", {'operators_as_actions' : True,
                    'dynamic_action_space' : True,
                    'render' : maze_render}),
            ("spannerlearning", {'operators_as_actions' : True,
                                'dynamic_action_space' : True}),
            ("navigation1", { 'render': lambda obs: navigation_render(obs, make("PDDLEnvNavigation1-v0").domain) }),
            ("navigation2", { 'render': lambda obs: navigation_render(obs, make("PDDLEnvNavigation2-v0").domain) }),
            ("navigation3", { 'render': lambda obs: navigation_render(obs, make("PDDLEnvNavigation3-v0").domain) }),
            ("navigation4", { 'render': lambda obs: navigation_render(obs, make("PDDLEnvNavigation4-v0").domain) }),
            ("navigation5", { 'render': lambda obs: navigation_render(obs, make("PDDLEnvNavigation5-v0").domain) }),
            ("navigation6", { 'render': lambda obs: navigation_render(obs, make("PDDLEnvNavigation6-v0").domain) }),
            ("navigation7", { 'render': lambda obs: navigation_render(obs, make("PDDLEnvNavigation7-v0").domain) }),
            ("navigation8", { 'render': lambda obs: navigation_render(obs, make("PDDLEnvNavigation8-v0").domain) }),
            ("navigation9", { 'render': lambda obs: navigation_render(obs, make("PDDLEnvNavigation9-v0").domain) }),
            ("navigation10", { 'render': lambda obs: navigation_render(obs, make("PDDLEnvNavigation10-v0").domain) }),
            ("visit_all", {'render' : visit_all_render,
                        'operators_as_actions': True,
                        'dynamic_action_space': True}),
    ]:
        other_args = {
            "raise_error_on_invalid_action": False,
        }
        kwargs.update(other_args)
        for is_test in [False, True]:
            register_pddl_env(env_name, is_test, kwargs)


    # Custom environments
    for level in range(1, 8):
        register(
            id=f'SearchAndRescueLevel{level}-v0',
            entry_point=f'pddlgym.custom.searchandrescue:SearchAndRescueEnv',
            kwargs={'level' : level, 'test' : False, 'render_version' : 'slow'},
        )
        register(
            id=f'SearchAndRescueLevel{level}Test-v0',
            entry_point=f'pddlgym.custom.searchandrescue:SearchAndRescueEnv',
            kwargs={'level' : level, 'test' : True, 'render_version' : 'slow'},
        )
        register(
            id=f'PDDLSearchAndRescueLevel{level}-v0',
            entry_point=f'pddlgym.custom.searchandrescue:PDDLSearchAndRescueEnv',
            kwargs={'level' : level, 'test' : False, 'render_version' : 'slow'},
        )
        register(
            id=f'PDDLSearchAndRescueLevel{level}Test-v0',
            entry_point=f'pddlgym.custom.searchandrescue:PDDLSearchAndRescueEnv',
            kwargs={'level' : level, 'test' : True, 'render_version' : 'slow'},
        )

    register(
        id='SmallPOSARRadius1-v0',
        entry_point='pddlgym.custom.searchandrescue:SmallPOSARRadius1Env',
    )

    register(
        id='SmallPOSARRadius0-v0',
        entry_point='pddlgym.custom.searchandrescue:SmallPOSARRadius0Env',
    )

    register(
        id='POSARRadius1-v0',
        entry_point='pddlgym.custom.searchandrescue:POSARRadius1Env',
    )

    register(
        id='POSARRadius1Xray-v0',
        entry_point='pddlgym.custom.searchandrescue:POSARRadius1XrayEnv',
    )

    register(
        id='POSARRadius0-v0',
        entry_point='pddlgym.custom.searchandrescue:POSARRadius0Env',
    )

    register(
        id='POSARRadius0Xray-v0',
        entry_point='pddlgym.custom.searchandrescue:POSARRadius0XrayEnv',
    )


    register(
        id='SmallMyopicPOSAR-v0',
        entry_point='pddlgym.custom.searchandrescue:SmallMyopicPOSAREnv',
    )

    register(
        id='TinyMyopicPOSAR-v0',
        entry_point='pddlgym.custom.searchandrescue:TinyMyopicPOSAREnv',
    )

    # END


# Ignore certain files for pdoc documentation generation.
__pdoc__ = {'downward_translate': False, 'procedural_generation': False}


# Orchestrating FF Planning for Probabilistic PDDL (PPDDL) Planning Problems, plus Gymnasium simulation via PDDLGym 

### Components
- PDDLGym (modified)
- FF Planner v2.3 (patched to compile, logic unchanged)
- PDDLGym_Planners (modified)

### Installation
- Ubuntu 24.04 (or whichever works)
- Python 3.12 (or whichever works)
- `apt install`:
    - pip
    - python3-venv
    - build-essential
    - libjpeg-dev
    - zlib1g-dev
    - possibly any of the following: libfreetype6-dev liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev libtiff5-dev
    - flex
    - bison
- In //pddlgym: `pip install -e .`
- In //pddlgym_planners: `pip install -e .`
- In //FF-v2.3: `make`

### Environment Control
- PATH: make 'ff' and/or 'fd' resolveable
- CURRENT_GYMDIR: any directory which contains the following:
> when unspecific, the default gymdir of the `pddlgym` directory is used
    - `__init__.py` which registers all desired Gym environments
    - dir `pddl` containing each `<domain>.pddl` and, foreach <domain>, subdir `<domain>` containing problem files `<problem>.pddl`
    - (optional) dir `rendering` and subdir `assets`
    - (optional) dir `tests`
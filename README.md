# Orchestrating FF Planning for Probabilistic PDDL (PPDDL) Planning Problems, plus Gymnasium simulation via PDDLGym 

### Components
- PDDLGym (modified)
    - Origin: https://github.com/tomsilver/pddlgym/commit/01c133a6707c51e570582794b27b33f9adcafd56
- FF Planner v2.3 (patched to compile, logic unchanged)
    - Origin: https://web.archive.org/web/20240604122952/https://fai.cs.uni-saarland.de/hoffmann/ff/FF-v2.3.tgz
- PDDLGym_Planners (modified)
    - Origin: https://github.com/ronuchit/pddlgym_planners/commit/d552c8a75a50a47f5ad46b1b55194254995331b2

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
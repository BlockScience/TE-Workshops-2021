from datetime import datetime
import numpy as np
from .sys_params import initial_conditions_l

# Genesis States
genesis_states = []
for initial_conditions in initial_conditions_l:
    genesis_states.append({
    'supply': initial_conditions['S0'],
    'price': initial_conditions['P0'],
    'reserve': initial_conditions['R0'],
    'spot_price': initial_conditions['P0'],
    'output_price': initial_conditions['P0'],

    })

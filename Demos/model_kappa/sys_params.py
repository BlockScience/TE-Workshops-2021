# Model parameters
from .parts.utils import *

hatch_raise = 100000 # fiat units
hatch_price = .1 #fiat per tokens
theta = .5 #share of funds going to funding pool at launch

R0 = hatch_raise*(1-theta) # initial reserve
S0 = hatch_raise/hatch_price # initial supply



kappas = []
invariant_l = []

initial_conditions_l = []
for kappa in [2, 3]:
    V0 = invariant(R0,S0,kappa) 
    P0 = spot_price(R0, V0, kappa)

    initial_conditions = {
        'R0':R0,
        'S0':S0,
        'V0':V0,
        'P0':P0   
    }
    kappas.append(kappa)
    invariant_l.append(V0)
    initial_conditions_l.append(initial_conditions)

sys_params = {
    'kappa': kappas,
    'invariant': invariant_l,
    'dust' : [10**-8],
    'rule' : ['martin', 'martin'],
    'dP' : ['N/A', 'NA'],
    'sigma': [.1*(.5**(10)), .1*(.5**(10))],
    'period': ['N/A', 'N/A'],
    'phi': [0], #phi for exiting funds
    'beta': [0.9], #beta is param for armijo rule
}

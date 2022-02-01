# Script with all inputs for self-similar code

import numpy as np

################################################################################
## Normalisation constants
################################################################################

Z = 1
mi = 1.67e-24
N0 = 4.73218e20
T0 = 158.489
H0 = np.sqrt(16.0 * np.pi * N0 * T0 * 1.6e-12)
B0 = 10.0 * H0

################################################################################
## Boundary conditions (check r(u) in calculate.py)
################################################################################

h_negative_inf = 0.0
h_positive_inf = B0/H0
n_negative_inf = 30#1.0 + h_positive_inf**2
n_positive_inf = 1.0
v_positive_inf = 0.0
v_negative_inf = 0.0

################################################################################
## Shooting optimisation settings
################################################################################

optimise = True
estimate = [ 3.4472705311267067 , 4.849781474625785 , 2.919579679123567 , 6.061726489404166 , 0.025320444236817535 ]
tol_value = 1e-5
optimise_f_stop = 30
optimise_r_stop = -30
damping = 1.0
h_val = 1.0e-6

################################################################################
## Values for full calculation
################################################################################
min_value = -30
max_value = 30

################################################################################
## Behaviour switches
################################################################################

no_variation_of_coul = False # switch to control if Coulomb log should be calculated self-consistently
ohmic = True # switch to control if we should allow Ohmic heating
ettings = True # switch to control if we should switch off Ettingshausen effect
l_unmagnetised = False

################################################################################
## General switches
################################################################################

method = "BDF" # switch for integration method, "BDF" works best
high_resolution = False # calculate using a fixed small step size
high_res_value = 0.03

################################################################################
## Data output
################################################################################
save_data = True
save_data_path = "data/test_problem_temp_gradient/all_terms/"
plot_real_values = True
plot = True
plotxmin = -5
plotxmax = 5.0
time = 1.0e-9 # physical time in s to plot the profiles for
output_as_Chimera = True # output data in a suitable way for Chimera to use
stylefile = "C:/Users/gf715/OneDrive - Imperial College London/style_files/aidan.mplstyle"

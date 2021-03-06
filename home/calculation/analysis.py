from statsmodels.stats.proportion import proportions_ztest, proportion_confint
from statsmodels.stats import weightstats as stests
from statsmodels.stats.power import TTestIndPower
from scipy import optimize
import pandas as pd

from home.calculation.generator import *

def analyze(prob_1, prob_2):
    ab_test = generate_file(prob_1, prob_2)

    var1 = ab_test[ab_test['variant'] == 0].values[:,1]
    var2 = ab_test[ab_test['variant'] == 1].values[:,1]

    sample_size1 = var1.sum()
    sample_size2 = var2.sum()
    total_sample_size = sample_size1 + sample_size2

    ztest_var1, propability_value_var1 = stests.ztest(x1=var1, x2=var2)
    sample_size = total_sample_size
    alpha = 0.05
    power = 0.3
    power_analysis = TTestIndPower()

    def f(effect_size):
        return power_analysis.solve_power(effect_size=effect_size, power=power, alpha = alpha) - sample_size

    effect_size1 = 'Maximum detectable effect size: {0:.2f}'.format(optimize.root_scalar(f, bracket=[0.01, 1.0]).root)

    # not using this one (only one variant)
    sample_size = sample_size2
    alpha = 0.05
    power = 0.3
    power_analysis = TTestIndPower()

    ztest_var2, propability_value_var2 = stests.ztest(var2)
    effect_size2 = 'Maximum detectable effect size: {0:.2f}'.format(optimize.root_scalar(f, bracket=[0.01, 1.0]).root)
    
    return prob_1, ztest_var1, propability_value_var1, effect_size1, prob_2, ztest_var2, propability_value_var2, effect_size2, sample_size1, sample_size2, ab_test, total_sample_size, power

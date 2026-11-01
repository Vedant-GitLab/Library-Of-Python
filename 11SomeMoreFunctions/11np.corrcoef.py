#corrcoef = correlation coefficient,its range is -1 to 1, if correlation is 0 then there is no relation between x and y, if 1 so they are positively corelated with eachother, if -1 then it is negativelt correlated.
#Return Pearson product-moment correlation coefficients.

import numpy as np
salary= np.array([20000,40000,25000,35000,60000])
experience = np.array([1,3,2,4,2])
print(salary)
print(experience)
correlation_coefficient = np.corrcoef(salary,experience)
print(correlation_coefficient)
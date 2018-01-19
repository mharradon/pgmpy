# Generate data
import numpy as np
import pandas as pd

from pgmpy.models import BayesianModel

x = np.array([0] * 30 + [1] * 70) # Representing heads by 0 and tails by 1
y = np.array([0] * 50 + [1] * 50)
intervene_y = np.array([0] * 50 + [1] * 50) # Intervene y to make all heads, so y should actually be 0 with 100% probability

data = pd.DataFrame(np.array([x,y]).T, columns=['x','y'])
intervene = pd.DataFrame(y, columns=['y'])

model = BayesianModel()
model.add_nodes_from(['x','y'])

model.add_edge('x','y')

model.fit(data)

print('Non intervened model:')
print(model.cpds[1])

# Need to make all nan all parents of intervened nodes in data
# Not quite correct, but at least all data is valid
def intervened_data(model,data,intervene):
  data_out = data.copy()
  for k,intervene_col in intervene.items():
    parents = list(model.get_parents(k))
    intervened = np.argwhere(intervene_col)
    data_out.loc[intervened.flatten(),parents] = float('nan')
  return data_out

data = intervened_data(model,data,intervene)

model.fit(data)

print('Intervened model:')
print(model.cpds[1])

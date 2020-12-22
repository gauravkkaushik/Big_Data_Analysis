import pandas as pd
import numpy as np

#pairs of non directional graph pair set
data1 = {'A':[1,1,1,2,2,3,3,3,3],
'B':[2,3,4,3,5,4,5,6,7]
        }

ABdf = pd.DataFrame.from_dict(data1)

data2 = {'B':[1,1,1,2,2,3,3,3,3],
'C':[2,3,4,3,5,4,5,6,7]
        }

BCdf = pd.DataFrame.from_dict(data2)

#join both DFs

joinDF = pd.merge(ABdf,BCdf,how='inner',on = 'B')

x = joinDF.groupby(['A','C']).count().reset_index()
print(x[x.A ==1])

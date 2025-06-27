
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tips = sns.load_dataset('tips')

# sns.scatterplot(x=tips['tip'], y=tips['size'])
# sns.boxplot(tips['tip'])
# pd.crosstab(index=tips['total_bill'], columns=tips['tip'])
# sns.pairplot(tips)

tips.corr()

# plt.show()
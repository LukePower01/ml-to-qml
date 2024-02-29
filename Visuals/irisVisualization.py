import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris_data = load_iris()
features = iris_data.data

iris_data = load_iris()
df = pd.DataFrame(features, columns=iris_data.feature_names)
df['class'] = pd.Series(iris_data.target)

sns.pairplot(df, hue='class', palette='tab10')
print('done')


plt.show()
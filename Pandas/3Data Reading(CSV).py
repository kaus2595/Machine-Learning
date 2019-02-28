import pandas as pd

housing_data = pd.read_csv("K:\Machine Learning\Pandas\california_housing_train.csv")

# describe() function provide intresting statistics
print("Describe function")
housing_data_describe = (housing_data.describe())
print(housing_data_describe)

#head() function display the first few records of the dataFrame
print("Head function")
housing_data_head = housing_data.head()
print(housing_data_head)

#hist() function makes the histogram graph of the asked column
print("Hist function")
housing_data_hist = housing_data.hist('housing_median_age')
housing_data_hist.savefig()
housing_data_hist.show()
print(housing_data_hist)
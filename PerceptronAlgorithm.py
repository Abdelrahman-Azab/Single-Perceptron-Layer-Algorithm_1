from sklearn.preprocessing import LabelEncoder
import pandas as pd


def read_data(path):
    data = pd.read_csv(path)
    data.to_csv()
    lbl = LabelEncoder()
    lbl.fit(data["Class"].values)
    data["Class"] = lbl.transform(list(data["Class"].values))
    return data


def perceptron_Algorithm(dataset, feature1, feature2, class1, class2, learning_rate, epochs, bias):
   print(dataset, feature1, feature2, class1, class2, learning_rate, epochs, bias)
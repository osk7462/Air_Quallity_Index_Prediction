import csv
import pandas as pd
from sklearn.model_selection import train_test_split
import Variables


def split_data(filename,train,test,header):
    dataset = pd.read_csv(filename)
    x = dataset.iloc[ : ,:11].values

    x_train,x_test = train_test_split(x,test_size=0.15, random_state=0)
    with open(train, "w") as train:
        csv_writer = csv.writer(train, dialect="excel")
        csv_writer.writerow(header)
        for rows in x_train:
            row = []
            for data in rows:
                row.append(data)
            csv_writer.writerow(row)


    with open(test, "w") as test:
        csv_writer = csv.writer(test, dialect='excel')
        csv_writer.writerow(header)
        for rows in x_test:
            row = []
            for data in rows:
                row.append(data)
            # print(row)
            csv_writer.writerow(row)


if __name__ == '__main__':
    header_for_pollutant = Variables.header_for_pollutant
    header_for_pollutant.append("Air_Quality_Index")
    header_for_pollutant.append('AQI_Category')
    path_for_pollutant = Variables.path_for_pollutant_data
    header_for_met = Variables.header_for_metereological
    path_for_met = Variables.path_for_metereological_data
    split_data(path_for_met+"met_data_without_missing_values.csv",path_for_met+"train.csv",\
               path_for_met+"test.csv",header_for_met)
    split_data(path_for_pollutant+"data_with_aqi.csv", path_for_pollutant+"train.csv",\
               path_for_pollutant+"test.csv",header_for_pollutant)


import csv
import pandas as pd
from sklearn.preprocessing import Imputer
import Variables



def create_csv():
    with open(path+"/AQI.txt", "r") as my_file:
        i = 0
        with open(path+"ORIGINAL_AQI_DATA.csv", "w") as my_csv:
            csv_writer = csv.writer(my_csv, dialect="excel")
            for line in my_file:
                line=line.split("\t")
                if i == 0:
                    i += 1
                    csv_writer.writerow(header)
                elif i == 1:
                    data = line[1: ]
                    new_data = []
                    column = 0
                    for single_data in data:
                        if column < 2:
                            new_data.append(single_data)
                        elif single_data is "":
                            single_data = "NaN"
                            new_data.append(single_data)
                        elif single_data == '\n':
                            osk = ""
                        else:
                            one_data = float(single_data)
                            new_data.append(one_data)
                        column += 1
                    csv_writer.writerow(new_data)



def missing_values(filename):   # func to take care of missing values in data set
    data_set = pd.read_csv(filename)
    data = data_set.iloc[:, 2: ].values
    imputer = Imputer(missing_values="NaN",strategy="median", axis=0)
    imputer = imputer.fit(data)
    data = imputer.transform(data)
    return data


def from_to_time(file_with_missing_values):
    from_time = pd.read_csv(file_with_missing_values, usecols=["From Date"])
    to_time = pd.read_csv(file_with_missing_values, usecols=["To Date"])
    from_time = from_time.values.tolist()
    to_time = to_time.values.tolist()
    return from_time, to_time


def creating_csv_without_missing_data(file_with_missing_values,file_without_missing_values,header):
    with open(file_without_missing_values, "w") as my_csv:
        csv_writer = csv.writer(my_csv, dialect="excel")
        csv_writer.writerow(header)
        data = missing_values(file_with_missing_values)
        from_time, to_time = from_to_time(file_with_missing_values)
        size = len(data)
        i = 0
        while i < size:
            row = []
            for single_value in from_time[i]:
                row.append(single_value)
            for single_value in to_time[i]:
                row.append(single_value)
            for single_value in data[i]:
                row.append(single_value)
            csv_writer.writerow(row)
            i += 1



if __name__ == '__main__':
    header = Variables.header_for_pollutant
    path = Variables.path_for_pollutant_data
    file_with_missing_values = path + "ORIGINAL_AQI_DATA.csv"
    file_without_missing_values = path + "AQI_DATA_WITHOUT_MISSING_VALUES.csv"
    create_csv()
    creating_csv_without_missing_data(file_with_missing_values,file_without_missing_values,header)

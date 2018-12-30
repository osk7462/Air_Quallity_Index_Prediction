import csv
import Data_preprocessing
import Variables


def main(file_with_missing_values,path):
    with open(file_with_missing_values, "w") as my_csv:
        csv_writer = csv.writer(my_csv,dialect="excel")
        csv_writer.writerow(header)
        with open(path+"combined_metereological_data.txt", "r") as met_data:
            count_line = 0
            for line in met_data:
                if count_line != 0:
                    line = line.split(",")
                    i = 0
                    row = []
                    while i < len(line):
                        if i < 2:
                            row.append(line[i])
                        elif 2 <= i < (len(line) - 1):
                            if line[i] != "-":
                                row.append(float(line[i]))
                            else:
                                row.append("NaN")
                        i += 1
                    csv_writer.writerow(row)
                count_line += 1


if __name__ == '__main__':
    header = Variables.header_for_metereological
    path = Variables.path_for_metereological_data
    file_with_missing_values = path+"met_data.csv"
    file_without_missing_values = path + "met_data_without_missing_values.csv"
    main(file_with_missing_values,path)
    Data_preprocessing.creating_csv_without_missing_data(file_with_missing_values,file_without_missing_values,header)

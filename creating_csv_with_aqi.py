import pandas as pd
import AQI_calculation
import csv
import Variables


def calculating_aqi(data_without_missing_values):
    pm2_data = pd.read_csv(data_without_missing_values, usecols=["PM2.5 (ug/m3)"]).values.tolist()
    pm10_data = pd.read_csv(data_without_missing_values, usecols=["PM10 (ug/m3)"]).values.tolist()
    co_data = pd.read_csv(data_without_missing_values, usecols=["CO (mg/m3)"]).values.tolist()
    nh3_data = pd.read_csv(data_without_missing_values, usecols=["NH3 (ug/m3)"]).values.tolist()
    no2_data = pd.read_csv(data_without_missing_values, usecols=["NO2 (ug/m3)"]).values.tolist()
    ozone_data = pd.read_csv(data_without_missing_values, usecols=["Ozone (ug/m3)"]).values.tolist()
    so2_data = pd.read_csv(data_without_missing_values, usecols=["SO2 (ug/m3)"]).values.tolist()
    aqi = []
    for i in range(len(pm2_data)):
        column = []
        single_column = AQI_calculation.calculate_pm2_aqi(pm2_data[i])
        column.append(single_column)
        single_column = AQI_calculation.calculate_pm10_aqi(pm10_data[i])
        column.append(single_column)
        single_column = AQI_calculation.calculate_CO_aqi(co_data[i])
        column.append(single_column)
        single_column = AQI_calculation.calculate_SO2_aqi(so2_data[i])
        column.append(single_column)
        single_column = AQI_calculation.calculate_NH3_aqi(nh3_data[i])
        column.append(single_column)
        single_column = AQI_calculation.calculate_NO2_aqi(no2_data[i])
        column.append(single_column)
        single_column = AQI_calculation.calculate_O3_aqi(ozone_data[i])
        column.append(single_column)
        aqi.append(column)
    return aqi


def creating_csv(filename,header,data_with_aqi): # creating a csv file with Air Quality Index data in it
    with open(filename, "r") as my_csv:
        csv_reader = csv.reader(my_csv)
        data = []
        i=0
        for line in csv_reader:
            if i is 0:
                i += 1
            else:
                data.append(line)

        with open(data_with_aqi, "w") as aqi_file:
            csv_writer = csv.writer(aqi_file, dialect="excel")
            csv_writer.writerow(header)
            i = 0
            aqi = calculating_aqi(filename)
            for single_row in data:
                row = []
                for column in single_row:
                    row.append(column)
                row.append(max(aqi[i]))
                if 0 <= max(aqi[i]) <= 100:
                    row.append(1)
                elif 101 <= max(aqi[i]) <= 200:
                    row.append(2)
                elif 201 <= max(aqi[i]) <= 300:
                    row.append(3)
                elif 301 <= max(aqi[i]):
                    row.append(4)
                i += 1
                csv_writer.writerow(row)



if __name__ == '__main__':
    header = Variables.header_for_pollutant
    header.append('Air_Quality_Index(AQI)')
    header.append('AQI Category')
    path = Variables.path_for_pollutant_data
    data_without_missing_values = path + "AQI_DATA_WITHOUT_MISSING_VALUES.csv"
    data_with_aqi = path + "data_with_aqi.csv"
    creating_csv(data_without_missing_values,header,data_with_aqi)

import Data_extracion
import Variables


def get_month_name_days(month):
    if month == 1:
        month_name = "jan"
    elif month == 2:
        month_name = "feb"
    elif month == 3:
        month_name = "mar"
    elif month == 4:
        month_name = "apr"
    elif month == 5:
        month_name = "may"
    elif month == 6:
        month_name = "june"
    elif month == 7:
        month_name = "july"
    elif month == 8:
        month_name = "aug"
    elif month == 9:
        month_name = "sept"
    elif month == 10:
        month_name = "oct"
    elif month == 11:
        month_name = "nov"
    elif month == 12:
        month_name = "dec"
    return month_name



def main(path,header):
    with open(path+"combined_metereological_data.txt","w") as met_data:
        met_data.writelines(header)
        for year in range(2015,2019,1):
            for month in range(1,13):
                month_name = get_month_name_days(month)
                file = "Data/met_data"+"/" + str(year) +"/" + month_name
                try:
                    data = Data_extracion.extract(file)
                    for row in data:
                        line = ""
                        line = "{}-{}-{}-00:00".format(int(row[0]),month_name,year)+","+\
                                "{}-{}-{}-00:00".format((int(row[0])+1),month_name,year)+","
                        for index in range(1,10):\
                            line += row[index] + ","
                        line+="\n"
                        met_data.writelines(line)
                except FileNotFoundError:
                    pass


if __name__ == '__main__':
    header = Variables.header_for_metereological
    header = ",".join(header)
    header += "\n"
    path = Variables.path_for_metereological_data
    main(path,header)

import Classifiers
import read_online_data
import Variables
import pandas as pd


def get_data(path_for_pollutant,path_for_metereological):
    met_train =  pd.read_csv(path_for_metereological+"train.csv", usecols=[
        'T', 'TM', 'Tm', 'SLP', 'H','PP', 'VV', 'V', 'VM'])
    met_test = pd.read_csv(path_for_metereological+"test.csv",usecols=[
        'T', 'TM', 'Tm', 'SLP', 'H', 'PP', 'VV', 'V', 'VM'])

    met_train = met_train.values
    met_test = met_test.values

    aqi_train = pd.read_csv(path_for_pollutant+"train.csv",usecols=['AQI_Category'])
    aqi_test = pd.read_csv(path_for_pollutant+"test.csv",usecols=['AQI_Category'])

    aqi_test = aqi_test.values
    aqi_train = aqi_train.values
    return met_train,met_test,aqi_train,aqi_test



def main(met_train,met_test,aqi_train,aqi_test,test):
    while True:
        ch = int(input("\n\nchose among the following classifier\n"
                       "1.Rnadom Forrest\n"
                       "2.K-NN\n"
                       "3.SVM\n"
                       "4.Decision Tree\n"
                       "5.exit\n"))
        if ch == 1:
            model, accuracy = Classifiers.Random_Forest_Classifier(met_train,met_test,aqi_train,aqi_test)
            print(model.predict(test))
            print(accuracy)

        elif ch == 2:
            model, accuracy = Classifiers.KNN(met_train,met_test,aqi_train,aqi_test)
            print(model.predict(test))
            print(accuracy)

        elif ch == 3:
            model, accuracy = Classifiers.SVM(met_train,met_test,aqi_train,aqi_test)
            print(model.predict(test))
            print(accuracy)
        elif ch == 4:
            model, accuracy = Classifiers.Decision_tree(met_train,met_test,aqi_train,aqi_test)
            print(model.predict(test))
            print(accuracy)

        elif ch == 5:
            break






if __name__ == '__main__':
    path_for_pollutant = Variables.path_for_pollutant_data
    path_for_metereological = Variables.path_for_metereological_data
    met_train,met_test,aqi_train,aqi_test = get_data(path_for_pollutant,path_for_metereological)
    test_data = read_online_data.get_data()
    test = []
    test.append(test_data)
    main(met_train, met_test, aqi_train, aqi_test, test)

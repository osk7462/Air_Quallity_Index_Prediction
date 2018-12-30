import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import sklearn.metrics as mt
from sklearn.tree import DecisionTreeRegressor
import pandas as pd
import numpy as np
import Variables
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor,NearestNeighbors


def KNR(path_for_pollutant,path_for_metereological):
    met_train =  pd.read_csv(path_for_metereological+"train.csv", usecols=[
        'T', 'TM', 'Tm', 'SLP', 'H','PP', 'VV', 'V', 'VM']).values
    met_test = pd.read_csv(path_for_metereological+"test.csv",usecols=[
        'T', 'TM', 'Tm', 'SLP', 'H', 'PP', 'VV', 'V', 'VM']).values

    # PM10 (ug/m3),PM2.5 (ug/m3),CO (mg/m3),Air_Quality_Index(AQI)

    aqi_train = pd.read_csv(path_for_pollutant+"train.csv",usecols=['AQI_Category']).values
    aqi_test = pd.read_csv(path_for_pollutant+"test.csv",usecols=['AQI_Category']).values


    # sc_x = StandardScaler()
    # met_train = sc_x.fit_transform(met_train)
    # met_test = sc_x.transform(met_test)
    #
    # sc_y = StandardScaler()
    # aqi_train = sc_y.fit_transform(aqi_train)

    from sklearn.preprocessing import PolynomialFeatures

    # x_poly = PolynomialFeatures(degree=)
    # met_train = x_poly.fit_transform(met_train)
    # met_test = x_poly.fit_transform(met_test)
    #
    # aqi_train = x_poly.fit_transform(aqi_train)
    # aqi_test = x_poly.fit_transform(aqi_test)
    # print(aqi_test)

    #
    # from sklearn.tree import DecisionTreeRegressor
    # model = DecisionTreeRegressor(max_depth=4)
    # model.fit(met_train, aqi_train)
    # print(mt.mean_squared_log_error(aqi_test,model.predict(met_test))*100)

    # from sklearn.linear_model import LinearRegression
    # model = LinearRegression()
    # model.fit(met_train,aqi_train)
    # print(mt.r2_score(aqi_test, model.predict(met_test))*100)


    from sklearn.neighbors import KNeighborsClassifier
    max1 = []
    j = 100
    for i in range(1,100,1):
        knn = KNeighborsClassifier(n_neighbors=10,algorithm='auto',leaf_size=i)
        knn.fit(met_train,aqi_train)
        j -= 1
        print(mt.accuracy_score(aqi_test,knn.predict(met_test))*100)
        max1.append(mt.accuracy_score(aqi_test,knn.predict(met_test))*100)
    print(max1.index(max(max1)))


    # from sklearn.naive_bayes import GaussianNB
    # model = GaussianNB()
    # model.fit(met_train, aqi_train)
    # print(mt.accuracy_score(aqi_test,model.predict(met_test))*100)

    # 67%
    # from sklearn.tree import DecisionTreeClassifier
    # model = DecisionTreeClassifier(criterion='gini', random_state=0)
    # model.fit(met_train, aqi_train)
    # print(mt.accuracy_score(aqi_test,model.predict(met_test))*100)
    #
    #

    # j = 1
    # for i in met_test:
    #     from sklearn.ensemble import RandomForestClassifier
    #     model = RandomForestClassifier(n_estimators=205,criterion='gini',random_state=0)
    #     model.fit(met_train, aqi_train)
    #     print("{}\t{}".format(j,model.predict([i])))
    #     j += 1
    # print(mt.accuracy_score(aqi_test, model.predict(met_test))*100)





    # 74%
    # max1 = []
    # from sklearn.svm import SVC
    # for i in range(1,100,1):
    #     model = SVC(kernel='rbf', random_state=0)
    #     model.fit(met_train, aqi_train)
    #     print(mt.accuracy_score(aqi_test,model.predict(met_test))*100)
    #     max1.append(mt.accuracy_score(aqi_test,model.predict(met_test)*100))
    #     break
    # print(max1.sort())



#knn done 43%

    # max1 = []
    # from sklearn.ensemble import RandomForestRegressor
    # for j in range(1,100,1):
    #     k = 100
    #     for i in range(1,100,1):
    #         model = RandomForestRegressor(n_estimators=i,random_state=k)
    #         k-=1
    #         model.fit(met_train, aqi_train)
    #         print(mt.r2_score(aqi_test,model.predict(met_test))*100)
    #         max1.append(mt.r2_score(aqi_test,model.predict(met_test))*100)
    #     max1.sort()
    #     print(max1)
    #     break






    # 77% accuracy when p = 86 and n_neigbors = 15
    # j = 100;
    # max1 = []
    # for i in range(1,100,1):
    #     from sklearn.neighbors import KNeighborsClassifier
    #     model = KNeighborsClassifier(n_neighbors=i,metric='minkowski',p=j)
    #     j -= 1
    #     model.fit(met_train,aqi_train)
    #     print(mt.accuracy_score(aqi_test,model.predict(met_test))*100)
    #     # print(model.predict(met_test))
    #     max1.append(mt.accuracy_score(aqi_test,model.predict(met_test))*100)
    # print(max(max1))

    # plt.plot(np.array(np.arange(1,231,1)), pm2_predicted,color ='green')
    # plt.plot(np.array(np.arange(1,231,1)),aqi_test,color='red')
    # plt.show()


if __name__ == '__main__':
    path_for_pollutant = Variables.path_for_pollutant_data
    path_for_metereological = Variables.path_for_metereological_data
    KNR(path_for_pollutant,path_for_metereological)

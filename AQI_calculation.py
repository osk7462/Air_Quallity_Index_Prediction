
''''
    the formula for calculating aqi is:

    I = (((Ihigh - Ilow)/Chigh-Clow))*(C-Clow)) + ILow

    where,
    I = the air quality index
    C = the pollutant concentration,
    Clow = the concentration breakpoint that is ≤ C
    Chigh = the concentration breakpoint that is ≥ C
    Ilow = the index breakpoint corresponding to Clow
    Ihigh = the index breakpoint corresponding to Chigh
'''


# calculating Air Quality Index using to PM 2.5

def calculate_pm2_aqi(value):
    value = int(value[0])
    I = 0
    if value >= 0 and value <= 30:
        Clow = 0
        Chigh = 30
        Ilow = 0
        Ihigh = 50
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 31 and value <= 60:
        Clow = 30
        Chigh = 60
        Ilow = 51
        Ihigh = 100
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 61 and value <= 90:
        Clow = 61
        Chigh = 90
        Ilow = 101
        Ihigh = 200
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 91 and value <= 120:
        Clow = 91
        Chigh = 120
        Ilow = 201
        Ihigh = 300
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 121 and value <= 250:
        Clow = 121
        Chigh = 250
        Ilow = 301
        Ihigh = 400
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value > 251 :
        Clow = 251
        Chigh = value
        Ilow = 401
        Ihigh = 500
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow
    return int(I)


# calculating Air Quality Index using PM10

def calculate_pm10_aqi(value):
    value = int(value[0])
    if value >= 0 and value <= 50:
        Clow = 0
        Chigh = 50
        Ilow = 0
        Ihigh = 50
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 51 and value <= 100:
        Clow = 51
        Chigh = 100
        Ilow = 51
        Ihigh = 100
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 101 and value <= 250:
        Clow = 101
        Chigh = 250
        Ilow = 101
        Ihigh = 200
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 251 and value <= 350:
        Clow = 251
        Chigh = 350
        Ilow = 201
        Ihigh = 300
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 351 and value <= 430:
        Clow = 351
        Chigh = 430
        Ilow = 301
        Ihigh = 400
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value > 430 :
        Clow = 430
        Chigh = value
        Ilow = 401
        Ihigh = 500
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow
    return int(I)

# calculate AQI using CO


def calculate_CO_aqi(value):
    value = value[0]
    I = 0
    if value >= 0 and value <= 1:
        Clow = 0
        Chigh = 1
        Ilow = 0
        Ihigh = 50
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value > 1.0 and value <= 2.0:
        Clow = 1.1
        Chigh = 2.0
        Ilow = 51
        Ihigh = 100
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 2.1 and value < 10:
        Clow = 2.1
        Chigh = 10
        Ilow = 101
        Ihigh = 200
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 10.1 and value < 17:
        Clow = 10.1
        Chigh = 17
        Ilow = 201
        Ihigh = 300
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 17 and value < 34:
        Clow = 17
        Chigh = 34
        Ilow = 301
        Ihigh = 400
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 34 :
        Clow = 34
        Chigh = value
        Ilow = 401
        Ihigh = 500
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow
    return int(I)


# calculate AQI using SO2


def calculate_SO2_aqi(value):
    value = int(value[0])
    if value >= 0 and value <= 40:
        Clow = 0
        Chigh = 40
        Ilow = 0
        Ihigh = 50
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 41 and value <= 80:
        Clow = 41
        Chigh = 80
        Ilow = 51
        Ihigh = 100
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 81 and value <= 380:
        Clow = 81
        Chigh = 380
        Ilow = 101
        Ihigh = 200
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 381 and value <= 800:
        Clow = 381
        Chigh = 800
        Ilow = 201
        Ihigh = 300
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 801 and value < 1600:
        Clow = 801
        Chigh = 1600
        Ilow = 301
        Ihigh = 400
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 1600 :
        Clow = 1600
        Chigh = value
        Ilow = 401
        Ihigh = 500
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow
    return int(I)


# calculate AQI using NH3


def calculate_NH3_aqi(value):
    value = value[0]
    if value >= 0 and value <= 200:
        Clow = 0
        Chigh = 200
        Ilow = 0
        Ihigh = 50
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 201 and value <= 400:
        Clow = 201
        Chigh = 400
        Ilow = 51
        Ihigh = 100
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 401 and value <= 800:
        Clow = 401
        Chigh = 800
        Ilow = 101
        Ihigh = 200
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 801 and value < 1200:
        Clow = 801
        Chigh = 1200
        Ilow = 201
        Ihigh = 300
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 1200 and value <= 1800:
        Clow = 1201
        Chigh = 1800
        Ilow = 301
        Ihigh = 400
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value > 1800 :
        Clow = 1800
        Chigh = value
        Ilow = 401
        Ihigh = 500
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow
    return int(I)

# calculate AQI using NO2


def calculate_NO2_aqi(value):

    value = int(value[0])
    if value >= 0 and value <= 40:
        Clow = 0
        Chigh = 40
        Ilow = 0
        Ihigh = 50
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 41 and value <= 80:
        Clow = 41
        Chigh = 80
        Ilow = 51
        Ihigh = 100
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 81 and value <= 180:
        Clow = 81
        Chigh = 180
        Ilow = 101
        Ihigh = 200
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 181 and value <= 280:
        Clow = 181
        Chigh = 280
        Ilow = 201
        Ihigh = 300
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 281 and value <= 400:
        Clow = 281
        Chigh = 400
        Ilow = 301
        Ihigh = 400
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value > 400 :
        Clow = 400
        Chigh = value
        Ilow = 401
        Ihigh = 500
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow
    return int(I)

# calculate AQI using O3


def calculate_O3_aqi(value):

    value = int(value[0])
    if value >= 0 and value <= 50:
        Clow = 0
        Chigh = 50
        Ilow = 0
        Ihigh = 50
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 51 and value <= 100:
        Clow = 51
        Chigh = 100
        Ilow = 51
        Ihigh = 100
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 101 and value <= 168:
        Clow = 101
        Chigh = 168
        Ilow = 101
        Ihigh = 200
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 169 and value <= 208:
        Clow = 169
        Chigh = 208
        Ilow = 201
        Ihigh = 300
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value >= 209 and value <= 748:
        Clow = 209
        Chigh = 748
        Ilow = 301
        Ihigh = 400
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow

    elif value > 748 :
        Clow = 748
        Chigh = value
        Ilow = 401
        Ihigh = 500
        C = value
        I = (((Ihigh - Ilow)/(Chigh - Clow))*(C - Clow)) + Ilow
    return int(I)


def kelvin_to_celsius(kelvin_temp):

    KELVIN_OFFSET = 273.15

    celsius = kelvin_temp - KELVIN_OFFSET

    return celsius

def meters_per_second_to_mph(ms_speed):
    
    MS_TO_MPH = 2.23694

    mph = ms_speed * MS_TO_MPH

    return mph

def meters_per_second_to_knots_per_hour(ms_speed):

    MS_TO_KN = 1.94384

    knots_per_hour = ms_speed * MS_TO_KN

    return knots_per_hour

def knots_per_hour_to_mph(knots_speed):

    KN_TO_MPH = 1.15078

    mph = knots_speed * KN_TO_MPH

    return mph

def mph_to_knots_per_hour(mph):

    MPH_TO_KN = 0.868976

    knots_per_hour = mph * MPH_TO_KN

    return knots_per_hour
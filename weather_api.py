# Python program to find current temp of city requested by user

# import required modules
import requests, json, pytemperature

# Enter your API key here
api_key = "<api_key>"
# Give city name
city_name = input("Where are you? : ")

def get_weather(key, city_name):
    # url used to make request
    url = "http://api.openweathermap.org/data/2.5/weather?appid={}&q={}".format(key, city_name)
    # get method of requests module
    # return response object
    response = requests.get(url)
    # json method of response object
    # convert json formatted data into
    # python format data
    json_weather_output = response.json()
    return json_weather_output

# Uncomment this line for testing of nicely formatted json output
#print(json.dumps(get_weather(key=api_key, city_name=city_name), indent=4))

# json_weather_output contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found ref link: https://openweathermap.org/faq
def main():
    if get_weather(key=api_key, city_name=city_name)["cod"] != "404":

        # store the value of "main"
        # key in variable key_store
        key_store = get_weather(key=api_key, city_name=city_name)["main"]

        # store the value corresponding
        # to the "temp" key of key_store
        current_temperature = key_store["temp"]
        converted_temperature = pytemperature.k2f(current_temperature)

        # print temp of city
        print(city_name + ' weather: ' + str(converted_temperature) + " degrees in Fahrenheit")

    else:

        print(" City Not Found ")

main()

import requests

API_KEY = "e47c6513ad74f8b562e9132a4660265c"


def get_data(place, forecast_days, kind=None): 
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url) 
    data = response.json() 
    filtered_data = data["list"] 
    nr_values = 8 * forecast_days 
    filtered_data = filtered_data[:nr_values] 
    if kind == "Temperature": 
        filtered_data = [dict["main"]["temp"]/10 for dict in filtered_data] 
    if kind == "Sky": 
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data 

if __name__=="__main__": 
    print(get_data(place="Tokyo", forecast_days=1, kind="Temperature"))
    # get_data(place="Tokyo", forecast_days=1)

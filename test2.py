import requests


Config = {
    'darkskykey': '6d578ce3886749328597bb9917f15076',
    'googlekey' :"AIzaSyCAVaRUWKRYQc96EU3RFGro_D8qq6WCRSY"

}



def call_google(origin, destination, googlekey):
    PARAMS = {
        "origin": origin,
        "destination": destination,
        "key": googlekey,
    }
    URL = "https://maps.googleapis.com/maps/api/directions/json"
    # print(PARAMS)
    res = requests.get(url=URL, params=PARAMS)
    data = res.json()
    # print(data)
    # parse json to retrieve all lat-lng
    waypoints = data["routes"][0]["legs"]
    
    lats = []
    longs = []
    google_count_lat_long = 0

    # find cluster of interest from google api route
    for leg in waypoints:
        for step in leg["steps"]:
            start_loc = step["start_location"]
            # print("lat: " + str(start_loc['lat']) + ", lng: " + str(start_loc['lng']))
            lats.append(start_loc["lat"])
            longs.append(start_loc["lng"])
            google_count_lat_long += 1

    lats = tuple(lats)
    longs = tuple(longs)
    # print("total waypoints: " + str(google_count_lat_long))

    return lats, longs, google_count_lat_long


print(call_google("Colombo","Kurunegala",googlekey=Config['googlekey']))


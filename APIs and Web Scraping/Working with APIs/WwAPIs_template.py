
# coding: utf-8

# #Working with Data Sources

# ##Working with APIs

# ###1: What's an API?

# APIs are used to dynamically query and retrieve data. They provide a language whereby a client can retrieve information quickly and effectively. Reddit, Spotify, Twitter, Facebook, and many other companies provide APIs that enable developers to access a wealth of information stored on their servers.
# 
# In this mission, we'll be querying a simple API to retrieve data about the International Space Station (ISS). Using an API will save us time and effort over doing all the computation ourselves.

# ###2: Requests

# APIs are hosted on web servers. When you type in www.google.com in your browser's address bar, your computer is actually asking the www.google.com server for a webpage, which it then returns to your browser.
# 
# APIs work much the same way, except instead of your web browser asking for a webpage, your program asks for data. This data is usually returned in json format.
# 
# In order to get the data, we make a request to the webserver that we want to get data from. The server then replies with our data. In python, we use the requests library to do this.

# ###3: Type of requests

# There are many different types of requests. The most commonly used one, a GET request, is used to retrieve data. We'll get into the other types in later missions.
# 
# We can use a simple GET request to retrieve information from the OpenNotify API (http://open-notify.org/).
# 
# OpenNotify has several API endpoints. An endpoint is a server route that is used to retrieve different data from the API. For example, the /comments endpoint on the Reddit API might retrieve information about comments, whereas the /users endpoint might retrieve data about users.
# 
# The first endpoint we'll look at on OpenNotify is the iss-now.json endpoint. This endpoint gets the current latitude and longitude position of the International Space Station. As you can see, retrieving this data isn't a great fit for a dataset, because it involves some calculation on the server.
# 
# You can see a listing of all the endpoints on OpenNotify (http://open-notify.org/Open-Notify-API/).

# ####Instructions

# You can get the status code of the response from response.status_code. Assign the status code to the variable status_code.

# In[3]:

import requests

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")
status_code = response.status_code

print status_code


# ###4: Status codes

# The request we just made had a status code of 200. Status codes are returned with every request that is made to a web server. Status codes indicate information about what happened with a request. Here are some codes that are relevant to GET requests:
# - 200 -- everything went okay, and the result has been returned (if any)
# - 301 -- the server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
# - 401 -- the server thinks you're not authenticated. This happens when you don't send the right credentials to access an API (we'll talk about this in a later mission).
# - 400 -- the server thinks you made a bad request. This can happen when you don't send along the right data, among other things.
# - 403 -- the resource you're trying to access is forbidden -- you don't have the right permissions to see it.
# - 404 -- the resource you tried to access wasn't found on the server.

# ####Instructions

# Make a GET request to http://api.open-notify.org/iss-pass. Assign the status code of the response to status_code.

# In[5]:

import requests

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")
status_code = response.status_code

print status_code


# ###5: Hitting the right endpoint

# iss-pass wasn't a valid endpoint, so we got a 404 status code in response. We forgot to add .json at the end, as the API documentation states.

# ####Instructions

# Make a GET request to http://api.open-notify.org/iss-pass.json. Assign the status code of the response to status_code.

# In[6]:

import requests

response = requests.get("http://api.open-notify.org/iss-pass.json")
status_code = response.status_code

print status_code


# ###6: Query parameters

# You'll see that in the last example, we got a 400 status code, which indicates a bad request. If you look at the documentation for the OpenNotify API, we see that the ISS Pass (http://open-notify.org/Open-Notify-API/ISS-Pass-Times/) endpoint requires two parameters. 
# 
# The ISS Pass endpoint returns when the ISS will next pass over a given location on earth. In order to compute this, we need to pass the coordinates of the location to the API. We do this by passing two parameters -- latitude and longitude.
# 
# We can do this by adding an optional keyword argument, params, to our request. In this case, there are two parameters we need to pass:
# - lat -- The latitude of the location we want.
# - lon -- The longitude of the location we want.
# 
# We can make a dictionary with these parameters, and then pass them into the function.
# 
# We can also do the same thing directly by adding the query parameters to the url, like this: http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74.
# 
# It's almost always preferable to setup the parameters as a dictionary, because requests takes care of some things that come up, like properly formatting the query parameters.

# ####Instructions

# Get a response for the latitude 37.78 and the longitude -122.41 (the coordinates of San Francisco). Get the content of the response with response.content. Assign the content to the variable content.

# In[7]:

# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Print the content of the response (the data the server returned).
print response.content

# This gets the same data as the command above.
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
print response.content

parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
content = response.content


# ###7: JSON Format

# You may have noticed that the content of the response earlier was a string. Strings are the way that we pass information back and forth to APIs, but it's hard to get the information we want out of them. How do we know how to decode the string that we get back and work with it in python?
# 
# Luckily, there's a format called JavaScript Object Notation (JSON). JSON is a way to encode data structures like lists and dictionaries to strings that ensures that they are easily readable by machines. JSON is the primary format in which data is passed back and forth to APIs.
# 
# Python has great JSON support, with the json library. We can both convert lists and dictionaries to JSON, and convert strings to lists and dictionaries. In the case of our ISS Pass data, it is a dictionary encoded to a string in JSON format.
# 
# The json library has two main methods:
# - dumps -- Takes in a python object, and converts it to a string.
# - loads -- Takes a json string, and converts it to a python object.

# ####Instructions

# Load the fast_food_franchise_string string. Assign the result to fast_food_franchise_2.

# In[9]:

# Import the json library
import json

# Make a list of fast food chains.
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
print type(best_food_chains)

# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)
print type(best_food_chains_string)

# Convert best_food_chains_string back into a list
print type(json.loads(best_food_chains_string))

# Make a dictionary
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print type(fast_food_franchise_string)

fast_food_franchise_2 = json.loads(fast_food_franchise_string)


# ###8: Getting JSON from a request

# You can get the content of a response as a python object by using the .json() method on the response.

# Instructions

# Get the duration value of the first pass of the ISS over San Francisco (this is the duration key of the first dictionary in the response list). Assign the value to first_pass_duration.

# In[10]:

import requests

# Make the same request we did 2 screens ago.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object. Verify that it's a dictionary.
data = response.json()
print type(data)
print data

first_pass_duration = data["response"][0]["duration"]


# ###9: Content type

# The server doesn't just send a status code and the data when it generates a response. It also sends metadata containing information on how the data was generated and how to decode it. This is stored in the response headers. We can access this with the .headers property of a response.
# 
# The headers will be shown as a dictionary. Within the headers, content-type is the most important key for now. It tells us the format of the response, and how to decode it. For the OpenNotify API, the format is json, which is why we could decode it with json earlier.

# ####Instructions

# Get content-type from response.headers. Assign the content type to the content_type variable.

# In[11]:

# Headers is a dictionary
print response.headers

content_type = response.headers["content-type"]


# ###10: Finding the number of people in space

# OpenNotify has one more API endpoint, astros.json. It tells you how many people are currently in space. The format of the responses can be found here (http://open-notify.org/Open-Notify-API/People-In-Space/).

# In[13]:

import requests

# Call the API here.
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

in_space_count = data["number"]
print in_space_count


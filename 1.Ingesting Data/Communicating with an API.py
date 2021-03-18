# Fill in the correct API key.
# Create the URL of the web API by completing the template URL above. You need to pass the endpoint first and then the API key.
# Use that URL in the call to requests.get() so that you may see what more the API can tell you about itself.
endpoint = "http://localhost:5000"

# Fill in the correct API key
api_key = "scientist007"

# Create the web API’s URL
authenticated_endpoint = "{}/{}".format(endpoint, api_key)

# Get the web API’s reply to the endpoint
api_response = requests.get('http://localhost:5000/scientist007').json()
pprint.pprint(api_response)


# Take a look at the output in the console from the previous step. 
# Notice that it is a list of endpoints, each containing a description of the content found at the endpoint and the template for the URL to access it. 
# The template can be filled in, like you did in the previous step.
# Complete the URL that should give you back a list of all shops that were scraped by the marketing team.
endpoint = "http://localhost:5000"

# Fill in the correct API key
api_key = "scientist007"

# Create the web API’s URL
authenticated_endpoint = "{}/{}".format(endpoint, api_key)

# Get the web API’s reply to the endpoint
api_response = requests.get(authenticated_endpoint).json()
pprint.pprint(api_response)

# Create the API’s endpoint for the shops
shops_endpoint = "{}/{}/{}/{}".format(endpoint, api_key, "diaper/api/v1.0", "shops")
shops = requests.get(shops_endpoint).json()
print(shops)


# Take a look at the output in the console from the previous step. The shops variable contains the list of all shops known by the web API.
# From the shops variable, find the one that starts with the letter “D”. 
# Use it in the second (templated) url that was shown by the call to pprint.pprint(api_response), to list the items of this specific shop. 
# You must use the appropriate url endpoint, combined with the http://localhost:5000, similar to how you completed the previous step.
endpoint = "http://localhost:5000"

# Fill in the correct API key
api_key = "scientist007"

# Create the web API’s URL
authenticated_endpoint = "{}/{}".format(endpoint, api_key)

# Get the web API’s reply to the endpoint
api_response = requests.get(authenticated_endpoint).json()
pprint.pprint(api_response)

# Create the API’s endpoint for the shops
shops_endpoint = "{}/{}/{}/{}".format(endpoint, api_key, "diaper/api/v1.0", "shops")
shops = requests.get(shops_endpoint).json()
print(shops)

# Create the API’s endpoint for items of the shop starting with a "D"
items_of_specific_shop_URL = "{}/{}/{}/{}/{}".format(endpoint, api_key, "diaper/api/v1.0", "items", "DM")
products_of_shop = requests.get(items_of_specific_shop_URL).json()
pprint.pprint(products_of_shop)

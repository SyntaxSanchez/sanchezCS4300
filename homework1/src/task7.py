# Task7
# Sebastian Sanchez
# CS4300

import requests

# Function to get gitHub usernames using the public github API
def githubUser(username):

    # contruct the API endpoint URL
    url = f"https://api.github.com/users/{username}"
    # send a GET request to the Github API
    response = requests.get(url)

    # if the request is successful it'll send (status code 200)
    # return user data as a dictionary
    # return none if user was not found or error occurred
    if response.status_code == 200:
        return response.json()
    else:
        return None

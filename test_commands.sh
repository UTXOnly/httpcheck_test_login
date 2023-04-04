#!/bin/bash

curl -X POST -c cookies.txt -d "username=user1&password=password1" http://127.0.0.1:8000/login


#This curl command sends a POST request to the /login endpoint with the username and password included in the request body as form data. The response from the server includes a cookie that marks the user as authenticated.
#
#To test the /protected endpoint, you can use the cookies saved in the cookies.txt file to authenticate the request:
#
curl -X GET -c cookies.txt -b cookies.txt http://127.0.0.1:8000/protected

#This curl command sends a GET request to the /protected endpoint with the cookies saved in cookies.txt included in the request headers. If the cookies are valid and mark the user as authenticated, the server will respond with the protected content. Otherwise, it will redirect the user to the login page.
def Hellos():
    print("Hello World")

Hellos()


#author @tekraze

import falcon
import requests

class Hello:
    def on_get(self, req, resp):
        # we just send back a string here
        resp.media = 'hello'

class HelloJSON:
    def on_get(self, req, resp):
        # we just send back a string here
        resp.media = {'greet': 'hello'}
        
class JSONfromURL:
    def on_get(self, req, resp):
      
        # here we get data from url and then send it back as a response
      
        fakeUsersAPIUrl = 'https://jsonplaceholder.typicode.com/users'
        
        usersRequest = requests.get(fakeUsersAPIUrl)
        
        usersResponse = usersRequest.json()
        
        usersRequest.close()

        resp.media = usersResponse
        
class JSONfromURLChange:
    def on_get(self, req, resp):
      
        # here we get data from url and then send it back as a response
      
        fakeUsersAPIUrl = 'https://jsonplaceholder.typicode.com/users'
        
        usersRequest = requests.get(fakeUsersAPIUrl)
        
        usersResponse = usersRequest.json()
        
        usersRequest.close()
        
        # here we additionally create new data and send back to show how manipulation works
        
        # to hold new data
        newDataArray = []

        print(type(usersResponse))
  
        for key in usersResponse[:10]: ## to just get n items instead of whole list
            newData = {}
            newData['serial'] = key['id']
            newData['name'] = key['name']
            newDataArray.append(newData)

        resp.media = newDataArray

middle = falcon.CORSMiddleware(
    allow_origins="*"
)
print("Hello World")

api = falcon.App(middleware=middle)

api.add_route('/greet', Hello())
api.add_route('/greet-json', HelloJSON())
api.add_route('/json-from-url', JSONfromURL())
api.add_route('/json-from-url-change', JSONfromURLChange())


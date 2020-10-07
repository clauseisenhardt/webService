import cherrypy
import cherrypy_cors

import pandas as pd
import myprocessor
p = myprocessor.MyProcessor()

class MyWebService(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def process(self):
        data = cherrypy.request.json
        df = pd.DataFrame(data)
        output = p.run(df)
        return output.to_json()
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def listFiles(self):
        print("listFiles BEGIN!")
        if cherrypy.request.method == 'OPTIONS':
            print("listFiles OPTIONS!")
            # This is a request that browser sends in CORS prior to
            # sending a real request.

            # Set up extra headers for a pre-flight OPTIONS request.
            cherrypy_cors.preflight(allowed_methods=['GET'])

        if cherrypy.request.method == 'GET':
            print("listFiles GET!")
            output = p.listFiles("/data")
            print("File list: " + output)
            print("listFiles END!")
            return output
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def listFolders(self):
        print("listFiles BEGIN!")
        if cherrypy.request.method == 'OPTIONS':
            print("listFolders OPTIONS!")
            cherrypy_cors.preflight(allowed_methods=['GET'])

        if cherrypy.request.method == 'GET':
            print("listFolders GET!")
            output = p.listFolders("/data")
            print("File listFolders: " + output)
            print("listFolders END!")
            return output

    def __OPTIONS(self):
        cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"
        cherrypy.response.headers["Access-Control-Max-Age"] = "86400"
        cherrypy.response.headers["Access-Control-Allow-Headers"] = \
        "X-Mobile, Authorization, Origin, X-Requested-With, Content-Type, Accept"
        cherrypy.response.headers["Content-Type"] = \
        "application/json; charset=utf-8"
        return ''

if __name__ == '__main__':
    print ("Hallo!")
    
    config = {
        'global': {
        'server.socket_host':'0.0.0.0',
        'server.socket_port':8081, 
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'cors.expose.on': True
        }
        ,
        '/favicon.ico': {
            'tools.staticfile.on': True,
            'tools.staticfile.filename': '/path/to/myfavicon.ico'
        }
    }
    cherrypy_cors.install()
    cherrypy.quickstart(MyWebService(),'/', config)


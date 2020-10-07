
from os import listdir
from os.path import isfile, isdir, join

class MyProcessor:     
    def run(self, df):        
        return df.agg(['mean', 'min', 'max'])

    def listFiles(self, filepath):
        onlyfiles = [f for f in listdir(filepath) if isfile(join(filepath, f))]
        import json
        return json.dumps(onlyfiles)

    def listFolders(self, filepath):
        onlyfolders = [f for f in listdir(filepath) if isdir(join(filepath, f))]
        import json
        return json.dumps(onlyfolders)

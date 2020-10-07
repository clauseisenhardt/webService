class MyProcessor:     
    def run(self, df):        
        return df.agg(['mean', 'min', 'max'])

    def listFiles(self, filepath):
        from os import listdir
        from os.path import isfile, join
        onlyfiles = [f for f in listdir(filepath) if isfile(join(filepath, f))]
        import json
        return json.dumps(onlyfiles)

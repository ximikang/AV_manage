import os
import json
def readjson():
    #logjson = json.dumps(log)
    with open(os.path.join(os.getcwd(),'log.josn'),'r',encoding = 'utf-8') as f:
        logjson = f.read()
        return logjson

def rerename(logs):
    for index,log in enumerate(logs):
        try:
            os.renames(log[1],log[0])
        except:
            print('ERROR:',log)
if __name__ == "__main__":
    logjson = readjson()
    log = json.loads(logjson)
    rerename(log)

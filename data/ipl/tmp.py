import json
import sys
f = open(sys.argv[1], "r")
x = f.read()
f.close()
x = json.JSONDecoder().decode(x)
#print json.dumps(x, indent=4, separators=(',', ': '))

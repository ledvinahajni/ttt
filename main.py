import urllib.request
import json

ttt_valasz = urllib.request.urlopen("https://tturak.hu/api/hikeoccasion/list?from=1642969163.143&to=1643669999.999").read()
ttt_valasz_jsonbe_parseolva = json.loads(ttt_valasz)
print(ttt_valasz_jsonbe_parseolva)

print(ttt_valasz_jsonbe_parseolva[0]["id"])
print(ttt_valasz_jsonbe_parseolva[0]["displayName"])
print(ttt_valasz_jsonbe_parseolva[0]["routes"])

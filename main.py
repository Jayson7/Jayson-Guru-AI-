from http import client
import wolframalpha
import wikipedia

app_id = "G4UAUE-K5JX8XPVYX"
client = wolframalpha.Client(app_id)

res = client.query("who is the president of the United States?")
print(next(res.results).text)
from http import client
import wolframalpha
import wikipedia

app_id = "your wolframalpha app id"
client = wolframalpha.Client(app_id)





# res = client.query("who is the president of the United States?")
# res = client.query("what is the result of 2000 * 3420199")
res = client.query("who is the muhammad buhari?")

for pod in res.pods:
    for sub in pod.subpods:
        print(sub.plaintext)


        
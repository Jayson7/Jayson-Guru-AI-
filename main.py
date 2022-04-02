from http import client
import wolframalpha #
import wikipedia # to answer proled queries
import re #to check for words
import PySimpleGUI as sg

app_id = "G4UAUE-K5JX8XPVYX"
client = wolframalpha.Client(app_id)



re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search



# res = client.query("who is the president of the United States?")
# res = client.query("what is the result of 2000 * 3420199")
res = client.query("who is the muhammad buhari?")

for pod in res.pods:
    for sub in pod.subpods:
        print(sub.plaintext)


        
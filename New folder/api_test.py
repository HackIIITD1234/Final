import http.client

conn = http.client.HTTPSConnection("wikipedia-api1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "8e0aae87ccmsh55220e1c9dcbd2ap189479jsnad8acaebd1d3",
    'x-rapidapi-host': "wikipedia-api1.p.rapidapi.com"
}

enter = "flying"

conn.request("GET", f"/get_summary?q={enter}&lang=en&sentences=3", headers=headers)

res = conn.getresponse()
data = res.read()

print(type(dict(data.decode("utf-8"))))
print(data.decode("utf-8"))
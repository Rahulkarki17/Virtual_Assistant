import wolframalpha

input = raw_input("Question: ")
app_id = "E74WH6-4UQ65HU9KA"
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print(answer)

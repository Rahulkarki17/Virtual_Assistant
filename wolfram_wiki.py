import wikipedia
import wolframalpha

while True:
    input = raw_input("Q: ")

    try:
        #wolframalpha
        app_id = "E74WH6-4UQ65HU9KA"
        client = wolframalpha.Client(app_id)
        res = client.query(input)
        answer = next(res.results).text
        print(answer)
    except:
        #wikipedia 
        print(wikipedia.summary(input, sentences=2).encode("utf-8"))
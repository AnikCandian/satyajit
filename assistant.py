import wolframalpha
import requests

while True:
    user_input = input("Hello. What do you require? ")
    app_id = "HUPPT9-GYQX8AELK5"
    client = wolframalpha.Client(app_id)
    asking_prefix = "what is "
    asking_prefix1 = "what are "
    truth_arr = []
    verifier = 0
    for x in range(0, len(asking_prefix) - 1):
        if len(user_input) >= len(asking_prefix):
            if user_input[x] == asking_prefix[x]:
                truth_arr.append(True)
    for x in range(0, len(truth_arr) - 1):
        if truth_arr[x] != False:
            verifier  += 1
    if verifier != 6:
        for x in range(0, len(asking_prefix1) - 1):

            if len(user_input) >= len(asking_prefix1):
                if user_input[x] == asking_prefix1[x]:
                    truth_arr.append(True)
    if len(truth_arr) >= 6:
        answer = client.query(user_input)
        res = next(answer.results).text
        print(res)
    

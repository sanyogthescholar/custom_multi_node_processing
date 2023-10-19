from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def compute():
    #calculate the sum of the numbers from 1 to the number received as "data"
    #print(request.get_json())
    data = int(request.args.get("data"))
    print(data)
    #print(data)
    return Response(str(calculate(data)), status = 200)

def calculate(data):
    return sum(range(1, data + 1))

app.run(port = 5001, debug = True)
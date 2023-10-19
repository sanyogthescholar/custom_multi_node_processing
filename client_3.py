from flask import Flask, request, Response
from logic import calculate

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def compute():
    #calculate the sum of the numbers from 1 to the number received as "data"
    #print(request.get_json())
    data = int(request.args.get("data"))
    print(data)
    #print(data)
    return Response(str(calculate(data)), status = 200)


app.run(port = 5002, debug = True)
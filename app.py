from flask import Flask, request, abort

import requests

from flask import Flask, request
app = Flask(__name__)
 
@app.route('/hook', methods=['POST', "GET"])
def webhook():
   if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
       if not request.args.get("hub.verify_token")== "EAAIR4BemWYEBAKu9ZBIbfyvZBwvojGjtHxtmbIiKODdSxacnWnV2ZAX1k2BKyncp1VcfZAeSYDxbaWmiZBwhSOEUZCnwGbZBfUSWODzRZAcZCKtWZAsXuMmmILkjOlZCDzyLK3ZBZCuSGjFR07eUKARGHDHIZAsLlB3O45sCIlvUSMxvkDiYccJKYri785dRMHqHTs6ZBTlNZAuQkNaImQZDZD":
           return "Verification token missmatch", 403
       return request.args['hub.challenge'], 200
   return "Hello world", 200
 
if __name__ == "__main__":
   app.run(debug=True)
  
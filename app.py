from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        trans_key = request.form.get("wallet_address")
        if trans_key:
            # Redirect to the /transaction/<id> route with the transaction key
            return redirect(f"/transaction/{trans_key}")
        else:
            return "Transaction Key is missing!", 400
    return render_template("index.html")

@app.route("/transaction/<id>", methods=["GET"])
def transaction_page(id):
    try:
        trans_key = id
        url = f"https://blockchain.info/rawtx/{trans_key}"
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for 4xx/5xx errors
        
        trans_data = response.json()

        # Extract "from" (inputs) and "to" (outputs) addresses, handling missing data gracefully
        inputs = trans_data.get("inputs", [])
        outputs = trans_data.get("out", [])
        
        transaction_info = {
            "from": [inp["prev_out"].get("addr", "Unknown") for inp in inputs if inp.get("prev_out")],
            "to": [out.get("addr", "Unknown") for out in outputs],
            "value": [out.get("value", 0) for out in outputs],
            "time": trans_data.get("time", "Unknown")
        }
        
        print(transaction_info)

        return render_template("trans.html", transaction_info=transaction_info, zip=zip, txid=id)

    except requests.exceptions.RequestException as e:
        return f"Error fetching transaction data: {str(e)}", 500
    except KeyError as e:
        return f"Error parsing transaction data, missing key: {str(e)}", 500

@app.route("/analyze/<id>")
def transaction_analyze_page(id):
    data = id
    return render_template("main.html", id=id)


app.run(debug=True)

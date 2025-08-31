from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["message"]
        
        # Simple bot logic (abhi basic)
        if "hello" in user_input.lower():
            response = "Hi there! How can I help you?"
        elif "bye" in user_input.lower():
            response = "Goodbye! Have a nice day!"
        else:
            response = "Sorry, I didn't understand that."
            
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)

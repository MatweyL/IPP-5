from flask import Flask


app = Flask(__name__)


@app.get("/v1/contact")
def get_contacts():
    return


@app.post("/v1/contact")
def create_contact():
    return


@app.delete("/v1/contact")
def delete_all_contacts():
    return


@app.get("/v1/contact/<int:uid>")
def get_contact(uid: int):
    return


@app.delete("/v1/contact/<int:uid>")
def delete_contact(uid: int):
    return


@app.put("/v1/contact/<int:uid>")
def update_contact(uid: int):
    return

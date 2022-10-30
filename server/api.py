from flask import Flask, jsonify, request

from crud import ContactsCRUD
from models import Contact

app = Flask(__name__)
crud = ContactsCRUD()


@app.get("/v1/contact")
def get_contacts():
    return jsonify(crud.read_all()), 200


@app.post("/v1/contact")
def create_contact():
    contact_dict = request.json()
    contact = Contact(**contact_dict)
    return jsonify(crud.create(contact)), 200


@app.delete("/v1/contact")
def delete_all_contacts():
    return jsonify(crud.delete_all()), 200


@app.get("/v1/contact/<int:uid>")
def get_contact(uid: int):
    contact = crud.read(uid)
    return jsonify(contact), 200 if contact else 404


@app.delete("/v1/contact/<int:uid>")
def delete_contact(uid: int):
    contact = crud.delete(uid)
    return jsonify(contact), 200 if contact else 404


@app.put("/v1/contact/<int:uid>")
def update_contact(uid: int):
    contact_dict = request.json()
    contact = Contact(**contact_dict)
    contact.id = uid
    updated_contact = crud.update(contact)
    return jsonify(updated_contact), 200 if update_contact else 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

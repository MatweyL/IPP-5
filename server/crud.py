from typing import List, Optional

from mongoengine import connect
from pymongo import MongoClient

from models import Contact


class ContactsCRUD:

    def __init__(self):
        self.client: MongoClient = connect(db="contacts", host="mongo", port=27017, username="root", password="example")
        self.db = self.client["contacts"]

    def create(self, contact: Contact) -> Contact:
        contact = contact.save()
        return contact.to_json()

    def read(self, uid) -> Optional[Contact]:
        try:
            contact = Contact.objects.get(id=uid)
            contact = contact.to_json()
        except Contact.DoesNotExist:
            contact = None
        return contact

    def read_all(self) -> List[Contact]:
        return [c.to_json() for c in Contact.objects]

    def update(self, contact: Contact) -> Optional[Contact]:
        try:
            old_contact = Contact.objects.get(id=contact.id)
        except Contact.DoesNotExist:
            old_contact = None
        if old_contact is not None:
            contact = contact.save()
            return contact.to_json()
        else:
            return None

    def delete(self, uid) -> Optional[Contact]:
        try:
            contact = Contact.objects.get(id=uid)
        except Contact.DoesNotExist:
            contact = None
        if contact is not None:
            contact.delete()
            return contact.to_json()
        else:
            return None

    def delete_all(self) -> List[Contact]:
        contacts = self.read_all()
        Contact.drop_collection()
        return contacts


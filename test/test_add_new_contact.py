# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.contact import Contact

def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="ivan", middlename="romanovich", lastname="petrov", address="Sadovaya13", mobile="89876543210"))
    app.session.logout()

def test_add_new_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", address="", mobile="12341234"))
    app.session.logout()

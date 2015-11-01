#!/usr/bin/env python
#
# Copyright 2014 Jacek Marchwicki <jacek.marchwicki@gmail.com>

__author__ = 'Jacek Marchwicki <jacek.marchwicki@gmail.com>'

from google.appengine.ext import ndb

class Click(ndb.Model):
    button = ndb.IntegerProperty(required=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True, required=True)

class Clicks(ndb.Model):
    button = ndb.IntegerProperty(required=True)
    count = ndb.IntegerProperty(required=True)

    @staticmethod
    def get_by_button(button):
        clicks = Clicks.query(Clicks.button == button).get()
        if clicks is None:
            clicks = Clicks(
                button=button,
                count=0)
            clicks.put()
        return clicks

    def increment(self):
        self.count += 1

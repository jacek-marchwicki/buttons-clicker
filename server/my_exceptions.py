#!/usr/bin/env python
#
# Copyright 2014 Jacek Marchwicki <jacek.marchwicki@gmail.com>

__author__ = 'Jacek Marchwicki <jacek.marchwicki@gmail.com>'


class JsonException(Exception):
    def __init__(self, message="Not found", payload=None, status_code=400):
        Exception.__init__(self)
        self.message = message
        self.payload = payload
        self.status_code = status_code

    def to_dict(self):
        response = dict(self.payload or ())
        response['message'] = self.message
        return response

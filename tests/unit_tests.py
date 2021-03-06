#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Resolver
    ~~~~~

    copyright: (c) 2014 by Halfmoon Labs, Inc.
    copyright: (c) 2015 by Blockstack.org

This file is part of Resolver.

    Resolver is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Resolver is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Resolver. If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys
import requests
import json
import unittest

# Hack around absolute paths
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(current_dir + "/../")

sys.path.insert(0, parent_dir)

from server.resolver import app

VERSION = '1'

c = app.test_client()


def build_url(api_endpoint):

    return '/v' + VERSION + '/' + api_endpoint


def get_profile(username):

    url = build_url('users/' + username)

    r = c.get(url)

    return json.loads(r.data)


class ResolverTestCase(unittest.TestCase):

    def tearDown(self):
        pass

    def test_connectivity(self):
        """ Check connection to resolver
        """
        html = ''

        try:
            reply = c.get('/')
            html = reply.data
        except Exception as e:
            pass

        self.assertIn('Welcome to this resolver', html, msg="resolver is not online")

    def test_valid_profiles(self):
        """ Check valid profiles
        """

        usernames = ['fredwilson', 'davidlee']

        for username in usernames:

            reply = get_profile(username)

            profile = reply[username]['profile']

            verifications = reply[username]['verifications']

            self.assertIsInstance(profile, dict, msg="data not properly formatted")

            self.assertIn('name', profile, msg="name not in data")

            self.assertGreater(len(verifications), 0, msg="no varifications found")

    def test_invalid_profiles(self):
        """ Check invalid profiles
        """

        usernames = ['ben']

        for username in usernames:

            reply = get_profile(username)[username]

            self.assertIn('error', reply, msg="resolver didn't give error on invalid profile")

    def test_invalid_profiles(self):
        """ Check unregistered usernames
        """

        usernames = ['gfegef7ev79efv9ev23t4fv']

        for username in usernames:

            reply = get_profile(username)

            self.assertIn('error', reply, msg="resolver didn't give error on unregistered profile")


if __name__ == '__main__':

    unittest.main()
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

# JSON-RPC Resolver w/ MongoDB

import sys
import os

SERVER_PORT = 8080
VALID_BLOCKS = 36000

from SocketServer import ThreadingMixIn
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

# hack around absolute paths
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(current_dir + "/../../")

sys.path.insert(0, parent_dir)

from server.resolver import profiles, namespaces


class SimpleThreadedJSONRPCServer(ThreadingMixIn, SimpleJSONRPCServer):
    pass


def get_profile(username):
    profile = profiles.find_one({"username": username})['profile']

    return profile


def get_namespace():

    namespace = namespaces.find_one({"blocks": VALID_BLOCKS})

    return namespace['profiles']


def main():
    server = SimpleThreadedJSONRPCServer(('localhost', SERVER_PORT))
    server.register_function(get_profile)
    server.register_function(get_namespace)
    server.serve_forever()


if __name__ == '__main__':
    main()

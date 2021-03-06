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

import logging
log = logging.getLogger()

DEBUG = True

DEFAULT_PORT = 5000
DEFAULT_HOST = '0.0.0.0'
MEMCACHED_PORT = 11211
MEMCACHED_SERVER = '127.0.0.1'

RECENT_BLOCKS = 100
VALID_BLOCKS = 36000
REFRESH_BLOCKS = 25

DEFAULT_NAMESPACE = "id"

try:
    from config_local import *
except:

    log.debug('config_local.py not found, using default settings')

    MEMCACHED_TIMEOUT = 12 * 60 * 60
    USERSTATS_TIMEOUT = 60 * 60
    MEMCACHED_ENABLED = False

    try:
        MEMCACHED_USERNAME = os.environ['MEMCACHEDCLOUD_USERNAME']
        MEMCACHED_PASSWORD = os.environ['MEMCACHEDCLOUD_PASSWORD']
    except:
        try:
            MEMCACHED_USERNAME = os.environ['MEMCACHIER_USERNAME']
            MEMCACHED_PASSWORD = os.environ['MEMCACHIER_PASSWORD']
        except:
            MEMCACHED_USERNAME = None
            MEMCACHED_PASSWORD = None

    try:
        MEMCACHED_SERVERS = os.environ['MEMCACHEDCLOUD_SERVERS'].split(',')
    except:
        try:
            MEMCACHED_SERVERS = os.environ['MEMCACHIER_SERVERS'].split(',')
        except:
            memcached_server = MEMCACHED_SERVER + ':' + str(MEMCACHED_PORT)
            MEMCACHED_SERVERS = [memcached_server]

    # --------------------------------------------------

    try:
        BLOCKSTORED_SERVER = os.environ['BLOCKSTORED_SERVER']
        BLOCKSTORED_PORT = os.environ['BLOCKSTORED_PORT']
        DHT_MIRROR = os.environ['DHT_MIRROR']
        DHT_MIRROR_PORT = os.environ['DHT_MIRROR_PORT']
    except:
        log.debug("Blockstored or DHT-mirror not configured properly")
        exit(1)

    # --------------------------------------------------
    try:
        API_USERNAME = os.environ['API_USERNAME']
        API_PASSWORD = os.environ['API_PASSWORD']
    except:
        API_USERNAME = API_PASSWORD = ''

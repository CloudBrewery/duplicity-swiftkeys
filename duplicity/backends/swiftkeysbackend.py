# Copyright 2015 (c) Cloud Brewery Inc.
#
# This file is part of duplicity.
#
# Duplicity is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# Duplicity is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with duplicity; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import os

import duplicity.backend
from duplicity import log
from duplicity.errors import BackendException

import swiftclient.client
from swiftclient.client import HTTPConnection as _HTTPConnection


class ContainerKeyHTTPConnection(_HTTPConnection):

    def _request(self, *args, **kwargs):
        kwargs['headers']['X-Container-Meta-Full-Key'] = \
            os.environ['SWIFT_CONTAINER_FULL_TOKEN']
        kwargs['headers'].pop('X-Auth-Token', None)
        kwargs['headers'].pop('x-auth-token', None)
        return _HTTPConnection._request(self, *args, **kwargs)


swiftclient.client.HTTPConnection = ContainerKeyHTTPConnection


class SwiftKeysBackend(duplicity.backend.Backend):
    """
    A Backend for Swift using Container Keys
    """
    def __init__(self, parsed_url):

        from swiftclient import Connection, ClientException

        self.resp_exc = ClientException
        conn_kwargs = {}
        if 'SWIFT_CONTAINER_FULL_TOKEN' not in os.environ:
            raise BackendException('SWIFT_CONTAINER_FULL_TOKEN environment '
                                   'variable not set.')
        if 'SWIFT_STORAGE_URL' not in os.environ:
            raise BackendException('SWIFT_STORAGE_URL environment variable '
                                   'not set.')

        self.container_full_token = os.environ['SWIFT_CONTAINER_FULL_TOKEN']
        self.swift_storage_url = os.environ['SWIFT_STORAGE_URL']

        conn_kwargs['preauthurl'] = self.swift_storage_url
        conn_kwargs['preauthtoken'] = 'discarded'

        self.container = parsed_url.path.lstrip('/')

        self.conn = Connection(**conn_kwargs)

    def _error_code(self, operation, e):
        if isinstance(e, self.resp_exc):
            if e.http_status == 404:
                return log.ErrorCode.backend_not_found

    def _put(self, source_path, remote_filename):
        self.conn.put_object(self.container, remote_filename,
                             file(source_path.name))

    def _get(self, remote_filename, local_path):
        headers, body = self.conn.get_object(self.container, remote_filename)
        with open(local_path.name, 'wb') as f:
            for chunk in body:
                f.write(chunk)

    def _list(self):
        headers, objs = self.conn.get_container(self.container)
        return [o['name'] for o in objs]

    def _delete(self, filename):
        self.conn.delete_object(self.container, filename)

    def _query(self, filename):
        sobject = self.conn.head_object(self.container, filename)
        return {'size': int(sobject['content-length'])}


duplicity.backend.register_backend("swiftkeys", SwiftKeysBackend)

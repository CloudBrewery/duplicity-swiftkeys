#!/bin/bash
#
# Copyright 2002 Ben Escoto <ben@emerose.org>
# Copyright 2007 Kenneth Loafman <kenneth@loafman.com>
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

SUDO=sudo

cd `dirname $0`
pwd

if [ ! -e $1 ]; then
    echo "No test named $1"
    exit 1
fi

cd ../duplicity
./compilec.py
cd -

${SUDO} tar xzf testfiles.tar.gz

for v in 2.3 2.4 2.5 2.6; do
    if [ -e /usr/bin/python$v ]; then
        echo "Running tests for python$v"
        echo "========== Running $1 =========="
        ${SUDO} python$v -u $1 -v 2>&1 | grep -v "unsafe ownership"
    fi
done

${SUDO} rm -rf testfiles tempdir temp2.tar

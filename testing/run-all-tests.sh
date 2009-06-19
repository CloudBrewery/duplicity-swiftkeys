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

#${SUDO} tar xzf testfiles.tar.gz

for v in 2.3 2.4 2.5 2.6; do
    if [ -e /usr/bin/python$v ]; then
        LOG=run-all-tests-$v.log
        rm -f $LOG

        echo "========== Compiling librsync for python$v ==========" | tee -a $LOG
        pushd ../duplicity
        python$v ./compilec.py
        popd

        echo "Running tests for python$v" | tee -a $LOG
        for t in `cat alltests`; do
            echo "========== Running $t ==========" | tee -a $LOG
            ${SUDO} python$v -u $t -v 2>&1 | grep -v "unsafe ownership" | tee -a $LOG
            echo | tee -a  $LOG
            echo | tee -a  $LOG
        done
    fi
done

#${SUDO} rm -rf testfiles tempdir temp2.tar

# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright 2002 Ben Escoto <ben@emerose.org>
# Copyright 2007 Kenneth Loafman <kenneth@loafman.com>
#
# This file is part of duplicity.
#
# Duplicity is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3 of the License, or (at your
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

"""Store global configuration information"""

import socket, sys

# The current version of duplicity
version = "$version"

# The name of the current host, or None if it cannot be set
hostname = socket.getfqdn()

# The main local path.  For backing up the is the path to be backed
# up.  For restoring, this is the destination of the restored files.
local_path = None

# Set to the Path of the archive directory (the directory which
# contains the signatures and manifests of the relevent backup
# collection.
archive_dir = None

# Restores will try to bring back the state as of the following time.
# If it is None, default to current time.
restore_time = None

# If set, restore only the subdirectory or file specified, not the
# whole root.
restore_dir = None

# The backend representing the remote side
backend = None

# If set, the Select object which iterates paths in the local
# source directory.
select = None

# Set to GPGProfile that will be used to compress/uncompress encrypted
# files.  Replaces encryption_keys, sign_key, and passphrase settings.
gpg_profile = None

# If true, filelists and directory statistics will be split on
# nulls instead of newlines.
null_separator = None

# number of retries on network operations
num_retries = 5

# Character used like the ":" in time strings like
# 2002-08-06T04:22:00-07:00.  The colon isn't good for filenames on
# windows machines.
time_separator = ":"

# If this is true, only warn and don't raise fatal error when backup
# source directory doesn't match previous backup source directory.
allow_source_mismatch = None

# If set, abort if cannot do an incremental backup.  Otherwise if
# signatures not found, default to full.
incremental = None

# If set, print the statistics after every backup session
print_statistics = 1

# If set, use short (< 30 char) filenames for all the remote files.
short_filenames = 0

# If set, forces a full backup if the last full backup is older than
# the time specified
full_force_time = None

# Used to confirm certain destructive operations like deleting old
# files.
force = None

# If set, signifies time in seconds before which backup files should
# be deleted.
remove_time = None

# If set, signifies the number of backups chains to keep when perfroming
# a --remove-all-but-n-full.
keep_chains = None

# Don't actually do anything, but still report what would be done
dry_run = False

# If set to false, then do not encrypt files on remote system
encryption = 1

# volume size. default 25M
volsize = 25*1024*1024

# Working directory for the tempfile module. Defaults to /tmp on most systems.
temproot = None

# network timeout value
timeout = 30

# FTP data connection type
ftp_connection = 'passive'

# Protocol for webdav
webdav_proto = 'http'

# Asynchronous put/get concurrency limit
# (default of 0 disables asynchronicity).
async_concurrency = 0

# Whether to use "new-style" subdomain addressing for S3 buckets. Such
# use is not backwards-compatible with upper-case buckets, or buckets
# that are otherwise not expressable in a valid hostname.
s3_use_new_style = False

# Whether to create European buckets (sorry, hard-coded to only
# support european for now).
s3_european_buckets = False

# Whether to use the full email address as the user name when
# logging into an imap server. If false just the user name
# part of the email address is used.
imap_full_address = False

# Whether the old filename format is in effect.
old_filenames = False

# Wheter to specify --use-agent in GnuPG options
use_agent = False


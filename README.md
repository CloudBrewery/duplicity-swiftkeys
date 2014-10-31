# Notes

This is a fork of duplicity, which adds a `swiftkeys://` storage backend
that supports Swift Container Keys
(https://www.clouda.ca/blog/tech/dash/bulk-storage-container-api-keys/). For
more the original project information, check the announcement blog post
(https://www.clouda.ca/blog/general/using-bulk-storage-container-keys-with-duplicity/)

# Installation

If you have not downloaded it yet, you can grab the latest stable version from
the repo archive page, and continue using the regular install steps below.

```
    wget https://bitbucket.org/clouda/duplicity/get/321.tar.gz 
    tar -zxvf 321.tar.gz
    cd duplicity-swiftkeys-xxx/
```

Thank you for trying duplicity.  To install, run:

```
    pip install python-swiftclient lockfile
    python setup.py install
```

# Usage

```
    export SWIFT_STORAGE_URL="https://<swift-endpoint>/v1/AUTH_<tenant_id>" 
    export SWIFT_CONTAINER_FULL_TOKEN="<full-XXXX-token>"
    duplicity <backup_path> swiftkeys://<container_name>
```

You can get your tenant\_id filled bulk storage URL from the Dashboard under 
API Access and listed as Object Store.


# Requirements

 * Python v2.6 or later
 * librsync v0.9.6 or later
 * GnuPG v1.x for encryption
 * python-lockfile for concurrency locking
 * for scp/sftp -- python-paramiko and python-pycryptopp
 * for ftp -- lftp version 3.7.15 or later
 * Boto 2.0 or later for single-processing S3 or GCS access (default)
 * Boto 2.1.1 or later for multi-processing S3 access
 * Boto 2.7.0 or later for Glacier S3 access
 * python-urllib3 for Copy.com access

If you install from the source package, you will also need:

 * Python development files, normally found in module 'python-dev'.
 * librsync development files, normally found in module 'librsync-dev'.


A NOTE ON GnuPGInterface.py AND MULTIPLE GPG PROCESSES:

GnuPGInterface is used to access GPG from duplicity.  The original
works quite well and has no bugs, however, we have patched the one
used in duplicity.  Why?  Duplicity is not perfect, yet, and has a
problem when handling long chains of incremental backup or restore
operations.  The problem is that the waitpid() call only happens
after all the iterations complete, and with a long chain, that can
be a long while.  Unless the waitpid() call is made, the child process
remains active.  Duplicity's GnuPGInterface is patched to start an
immediate threaded waitpid() for each GPG task, thus harvesting the
task and freeing it's resources in a timely manner.  This does not
affect the operation of duplicity, merely frees resources on time.

Why the note?  Some package maintainers remove duplicity's GnuPGInterface
in error, obviously unknowing of this issue and patch duplicity to use
the old unmaintained unpatched GnuPGInterface interface again.
So, if you have the problem that lots of GPG tasks are hanging around,
check and see if this has been done in your distro, and if so, report this
matter as a bug to the distro or package maintainer.

As of october 2012 we pull the handbrake and refactor our code and rename
the class to gpginterface in the hope that package maintainers will stumble
over it and stop this problematic behaviour for good.


# Help

For more information see the duplicity home page at:

  http://www.nongnu.org/duplicity

or post to the mailing list at

  http://mail.nongnu.org/mailman/listinfo/duplicity-talk/

If there is an issue with the storage backend, you can log a bug on the
project at

  https://github.com/cloudbrewery/duplicity-swiftkeys/issues

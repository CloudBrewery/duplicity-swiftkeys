#!/bin/bash

# must be in root of BZR project
cd /home/ken/workspace/duplicity-src

# make changelog
bzr log -v > Changelog.GNU

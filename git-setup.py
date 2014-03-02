#!/bin/bash
# git-setup.py

name=""
version=""
description=""
username=`git config user.name`
email=`git config user.email`
magic="#!/usr/bin/env python2"
copyright="Copyright (C) `date '+%Y'`, $username"

dest="$(git rev-parse --show-toplevel)"

[ ! -e $dest/setup.py ] && cat << EOF > $dest/setup.py
${magic}
#${copyright}
# -*- coding: utf-8 -*-
import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name=$name,
        version=$version,
        description=$description,
        author=$username,
        author_email=$email,
        install_requires = [
        ],
        include_package_data=True,
    )
EOF

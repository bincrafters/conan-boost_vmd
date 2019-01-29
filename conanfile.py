#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/testing")

class BoostVmdConan(base.BoostBaseConan):
    name = "boost_vmd"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_vmd"
    lib_short_names = ["vmd"]
    header_only_libs = ["vmd"]
    b2_requires = ["boost_preprocessor"]

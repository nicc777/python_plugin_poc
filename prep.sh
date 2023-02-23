#!/usr/bin/env bash

rm -frR /tmp/test_plugin
rm -frR /tmp/second_test_plugin

mkdir /tmp/test_plugin
touch /tmp/test_plugin/__init__.py
cp -vf exp_plugin_code/my_plugin.py /tmp/test_plugin

mkdir /tmp/second_test_plugin
touch /tmp/second_test_plugin/__init__.py
cp -vf exp_plugin_code2/my_second_plugin.py /tmp/second_test_plugin
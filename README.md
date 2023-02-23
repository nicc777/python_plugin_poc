# POC For a Python Plugin Framework

> **Warning**
> This is just an experiment. Not te be used in production

> **Note**
> Current status: Not yet fully functional

This experiment looks at how a plugin framework could work at it's most basic level.

The application will load a custom plugin from the file `/tmp/test_plugin/my_plugin.py`, which in turn implements a base class from our application.

Quick run (assuming the repository is freshly cloned):

```shell
python3 -m venv venv
. venv/bin/activate
sh prep.sh
pip3 install build
python3 -m build
```

In a separate terminal window:

```shell
pip3 uninstall plugin-poc -y && pip3 install --user /path/to/python_plugin_poc/dist/plugin_poc-0.0.1.tar.gz
plugin_poc
```

# Further Reading and Helpful Links

The solution was implemented with hints/suggestions/answers from:

* https://stackoverflow.com/questions/55067166/in-python-how-do-i-get-the-list-of-classes-defined-within-a-particular-file
* https://stackoverflow.com/questions/3352258/dynamic-class-instantiation-in-python
* https://stackoverflow.com/questions/49434118/python-how-to-create-a-class-object-using-importlib



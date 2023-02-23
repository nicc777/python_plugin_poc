# POC For a Python Plugin Framework

> **Warning**
> This is just an experiment. Not te be used in production

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

The expected output should be something like this:

```text
INFO    : Plugin "Dummy" loaded
INFO    : Executing initial tasks for Dummy
INFO    : Current values: {'random_word_length': 100, 'random_word': 'wX4nlnb8ATIxLWsMZKEL08FWveC0K4iQLGSMnBHxJH1WYKTpD1eaC1sDeOu9iVGGjAevu11IG5kPGv7R5YJbCH67J0y3t0liWkg8'}
DEBUG   : current_word=wX4nlnb8ATIxLWsMZKEL08FWveC0K4iQLGSMnBHxJH1WYKTpD1eaC1sDeOu9iVGGjAevu11IG5kPGv7R5YJbCH67J0y3t0liWkg8
DEBUG   : slice_size=12
DEBUG   : POST PROCESSING: current_word=wX4nlnb8ATIx
INFO    : Current values: {'random_word_length': 100, 'random_word': 'wX4nlnb8ATIx'}
INFO    : files=['__init__.py', 'my_plugin.py']
INFO    :    inspecting file "__init__.py"
INFO    :    inspecting file "my_plugin.py"
INFO    :       module_name=my_plugin
INFO    :          ---------------------------------------
INFO    :          name:       AppPluginBase
INFO    :          ---------------------------------------
INFO    :          name:       GenericLogger
INFO    :          ---------------------------------------
INFO    :          name:       MyPlugin
INFO    : Plugin "MyPlugin" loaded
INFO    : Executing initial tasks for MyPlugin
INFO    :          ---------------------------------------
INFO    :          name:       PluginExecutionResult
INFO    :          ---------------------------------------
INFO    :          name:       Plugins
INFO    :          ---------------------------------------
INFO    :          name:       ValuesAPI
INFO    : Registered classes: ['dummy', 'myplugin']
INFO    : files=['my_second_plugin.py', '__init__.py']
INFO    :    inspecting file "my_second_plugin.py"
INFO    :       module_name=my_second_plugin
INFO    :          ---------------------------------------
INFO    :          name:       AppPluginBase
INFO    :          ---------------------------------------
INFO    :          name:       GenericLogger
INFO    :          ---------------------------------------
INFO    :          name:       MySecondPlugin
INFO    : Plugin "MySecondPlugin" loaded
INFO    : Executing initial tasks for MySecondPlugin
INFO    :          ---------------------------------------
INFO    :          name:       PluginExecutionResult
INFO    :          ---------------------------------------
INFO    :          name:       Plugins
INFO    :          ---------------------------------------
INFO    :          name:       ValuesAPI
INFO    :    inspecting file "__init__.py"
INFO    : Registered classes: ['dummy', 'myplugin', 'mysecondplugin']
INFO    : Retrieved keys from current values cache: ['random_word_length', 'random_word']
INFO    : Current values: {'random_word_length': 100, 'random_word': 'wX4nlnb8ATIx', 'test': ['random_word_length', 'random_word']}
```

# Further Reading and Helpful Links

The solution was implemented with hints/suggestions/answers from:

* https://stackoverflow.com/questions/55067166/in-python-how-do-i-get-the-list-of-classes-defined-within-a-particular-file
* https://stackoverflow.com/questions/3352258/dynamic-class-instantiation-in-python
* https://stackoverflow.com/questions/49434118/python-how-to-create-a-class-object-using-importlib



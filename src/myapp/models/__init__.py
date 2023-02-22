import copy
import importlib, os, inspect
import sys


class GenericLogger:

    def info(self, message):
        print('INFO    : {}'.format(message))

    def debug(self, message):
        print('DEBUG   : {}'.format(message))

    def warning(self, message):
        print('WARNING : {}'.format(message))

    def warn(self, message):
        self.warning(message=message)

    def error(self, message):
        print('ERROR   : {}'.format(message))


def get_modules_in_package(target_dir: str, logger: GenericLogger=GenericLogger()):
    # package_name = target_dir.split(os.sep)[-1]
    # logger.info('package_name={}'.format(package_name))
    files = os.listdir(target_dir)
    logger.info('files={}'.format(files))
    base_path = '{}'.format(
        '/'.join(target_dir.split('/')[1:-1])
    )
    # sys.path.insert(0,base_path)
    sys.path.insert(0,target_dir)
    logger.info('sys.path={}'.format(sys.path))
    for file in files:
        logger.info('   inspecting file "{}"'.format(file))
        if file not in ['__init__.py', '__pycache__']:
            if file[-3:] != '.py':
                logger.info('      IGNORED')
                continue

            file_name = file[:-3]
            # module_name = package_name + '.' + file_name
            module_name = file_name
            logger.info('      module_name={}'.format(module_name))
            for name, cls in inspect.getmembers(importlib.import_module(module_name), inspect.isclass):
                logger.info('         name:       {}'.format(name))
                logger.info('         cls:        {}'.format(cls))
                logger.info('         type:       {}'.format(type(cls)))
                logger.info('         cls.module: {}'.format(cls.__module__))
                if cls.__module__ == module_name:
                    yield cls


class ValuesAPI:

    def __init__(self):
        self.value_resolvers = dict()
        self.value_cache = dict()

    def add_value_resolver(self, resolver_name: str, resolver_function):
        self.value_resolvers[resolver_name] = resolver_function

    def resolve_value(self, resolver_name, params:dict=None, use_current_cache_as_params: bool=False, use_current_cache_as_params_if_params_arg_is_none: bool=True):
        final_params = dict()
        if params is None:
            if use_current_cache_as_params_if_params_arg_is_none is True:
                final_params = copy.deepcopy(self.value_cache)
        if use_current_cache_as_params:
            if params is not None:
                if isinstance(params, dict):
                    t = copy.deepcopy(self.value_cache)
                    final_params = {**params, **t}
                else:
                    final_params = copy.deepcopy(self.value_cache)
            else:
                final_params = copy.deepcopy(self.value_cache)
        if resolver_name not in  self.value_cache:
            self.value_cache[resolver_name] = self.value_resolvers[resolver_name](**final_params)
    
    def set_value(self, resolver_name: str, value: object):
        self.value_cache[resolver_name] = value

    def get_value(self, resolver_name: str, default_value: str=None):
        if resolver_name not in self.value_cache:
            if resolver_name not in self.value_resolvers:
                return default_value
            self.resolve_value(resolver_name=resolver_name, params=copy.deepcopy(self.value_cache))
        return copy.deepcopy(self.value_cache[resolver_name])


class PluginExecutionResult:

    def __init__(self, plugin_name: str, execution_reference: str=None):
        self.plugin_name = plugin_name
        self.execution_reference = execution_reference
        self.result = None

    def set_result(self, result: object):
        self.result = result


class AppPluginBase:

    def __init__(self, kind: str, logger=GenericLogger()):
        self.logger = logger
        self.kind = kind
        logger.info('Plugin "{}" loaded'.format(self.__class__.__name__))
        self.post_init_tasks()

    def post_init_tasks(self, parameters: dict=dict()):
        """Override this as needed
        """
        pass

    def exec(self, values_api: ValuesAPI, execution_reference: str, parameters: dict=dict())->PluginExecutionResult:
        self.logger.warning('This method must be implemented by the user')        
        return PluginExecutionResult(plugin_name=self.__class__.__name__, execution_reference=execution_reference).set_result(result=Exception("Not yet implemented by user"))


class Plugins:

    def __init__(self, values_api: ValuesAPI, logger: GenericLogger=GenericLogger()):
        self.plugin_register = dict()
        self.values_api = values_api
        self.logger = logger

    def register_plugin(self, plugin: AppPluginBase):
        if isinstance(plugin, AppPluginBase) is False:
            raise Exception('Incorrect Base Class')
        self.plugin_register[plugin.kind] = plugin

    def load_plugin_from_file(self, plugin_file_path: str):
        for returned_class in get_modules_in_package(target_dir=plugin_file_path, logger=self.logger):
            self.logger.info('> cls.__class__:       {}'.format(returned_class.__class__))
            self.logger.info('> returned_class name: {}'.format(returned_class.__class__.__name__))
            # if isinstance(returned_class, AppPluginBase):
            #     self.register_plugin(plugin=returned_class(kind=returned_class.__class__.__name__, logger=self.logger))
        self.logger.info('Registered classes: {}'.format(list(self.plugin_register.keys())))
        
    def execute(self, kind: str, execution_reference: str, parameters:dict=dict(), store_result_in_values_api: bool=True)->PluginExecutionResult:
        if kind not in self.plugin_register:
            raise Exception('No plugin handler for "{}" kind found'.format(kind))
        result = self.plugin_register[kind].exec(values_api=copy.deepcopy(self.values_api), execution_reference=execution_reference, parameters=parameters)
        if store_result_in_values_api:
            self.values_api.set_value(resolver_name='{}'.format(execution_reference), value=result.result)
        return result


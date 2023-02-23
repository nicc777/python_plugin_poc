from myapp.models import *


class MyPlugin(AppPluginBase):

    def __init__(self, kind: str, logger=GenericLogger()):
        super().__init__(kind, logger)

    def post_init_tasks(self, parameters: dict=dict()):
        self.logger.info('Executing initial tasks for {}'.format(self.__class__.__name__))
        self.properties = {
            'internal_value': 'This is the value stored within MyPlugin'
        }
        self.version = 'v0.2'
        self.logger.info('   Version set to {}'.format(self.version))

    def exec(self, values_api: ValuesAPI, execution_reference: str, parameters: dict=dict(), function_get_plugin_by_kind: object=None)->PluginExecutionResult:
        result = PluginExecutionResult(plugin_name=self.__class__.__name__, execution_reference=execution_reference)
        result.set_result(result=list(values_api.value_cache.keys()))
        self.logger.info('[{}:{}] result.result: {}'.format(self.kind, self.version, result.result))
        return result


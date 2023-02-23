from myapp.models import *


class MySecondPlugin(AppPluginBase):

    def __init__(self, kind: str, logger=GenericLogger()):
        super().__init__(kind, logger)

    def post_init_tasks(self, parameters: dict=dict()):
        self.logger.info('Executing initial tasks for {}'.format(self.__class__.__name__))
        self.version = 'v0.1'
        self.logger.info('   Version set to {}'.format(self.version))

    def exec(self, values_api: ValuesAPI, execution_reference: str, parameters: dict=dict(), function_get_plugin_by_kind: object=None)->PluginExecutionResult:
        result = PluginExecutionResult(plugin_name=self.__class__.__name__, execution_reference=execution_reference)
        value = None
        try:
            value = function_get_plugin_by_kind(kind='MyPlugin').get_property_value(property_reference='internal_value')
        except:
            value = 'Failed to retrieve the property from MyPlugin'
        result.set_result(result=value)
        self.logger.info('Retrieved keys from current values cache: {}'.format(result.result))
        return result


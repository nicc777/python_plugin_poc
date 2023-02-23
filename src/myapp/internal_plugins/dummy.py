from myapp.models import *


class Dummy(AppPluginBase):

    def __init__(self, kind: str, logger=GenericLogger()):
        super().__init__(kind, logger)

    def post_init_tasks(self, parameters: dict=dict()):
        self.logger.info('Executing initial tasks for {}'.format(self.__class__.__name__))

    def exec(self, values_api: ValuesAPI, execution_reference: str, parameters: dict=dict(), function_get_plugin_by_kind: object=None)->PluginExecutionResult:
        current_word = values_api.get_value(resolver_name='random_word', default_value='not-found')
        self.logger.debug('current_word={}'.format(current_word))
        slice_size = 12
        if 'slice_size' in parameters:
            slice_size = int(parameters['slice_size'])
        self.logger.debug('slice_size={}'.format(slice_size))
        if len(current_word) > slice_size:
            current_word = current_word[0:slice_size]
        result = PluginExecutionResult(plugin_name=self.__class__.__name__, execution_reference=execution_reference)
        result.set_result(result=current_word)
        self.logger.debug('POST PROCESSING: current_word={}'.format(current_word))
        return result


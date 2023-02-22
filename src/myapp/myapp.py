import random, string
from myapp.models import *
from myapp.internal_plugins.dummy import Dummy

logger = GenericLogger()

def random_word(random_word_length: int=16):
    letters = '{}{}{}'.format(
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits
    )
    return ''.join(random.choice(letters) for i in range(random_word_length))


values_api = ValuesAPI()
values_api.add_value_resolver(resolver_name='random_word', resolver_function=random_word)
values_api.set_value(resolver_name='random_word_length', value=100)
values_api.resolve_value(resolver_name='random_word', use_current_cache_as_params=True)
plugin_manager = Plugins(values_api=values_api, logger=logger)
plugin_manager.register_plugin(plugin=Dummy(kind='Dummy', logger=logger))


my_plugin_path = '/tmp/test_plugin'


def main():
    logger.info('Current values: {}'.format(values_api.value_cache))
    plugin_manager.execute(kind='Dummy', execution_reference='random_word', parameters=dict(), store_result_in_values_api=True)
    logger.info('Current values: {}'.format(values_api.value_cache))

    plugin_manager.load_plugin_from_file(plugin_file_path=my_plugin_path)
    plugin_manager.execute(kind='MyPlugin', execution_reference='test', parameters=dict(), store_result_in_values_api=True)
    logger.info('Current values: {}'.format(values_api.value_cache))


if __name__ == '__main__':
    main()


from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import pytest

from ....plugins.modules import get_servers as my_module
from .commun_test import AnsibleFailJson, \
    set_module_args, AnsibleExitJson, module_mock


def test_module_args_validation_enviroment(module_mock):
    set_module_args({
        'username': os.environ.get('HAIINV_USER_TEST'),
        'password': os.environ.get('HAIINV_PASSWORD_TEST'),
        'url': 'https://sliphup.github.io/json_rest_examples/prueba.json',
        'techgroups': 'lab_test_rh_1',
        'environment': 'previous'
    })
    with pytest.raises(AnsibleExitJson) as result:
        my_module.main()
    assert result.value.args[0]['changed'] is False
    assert len(result.value.args[0]['hosts']) > 0


def test_module_args_validation_enviroment_error(module_mock):
    set_module_args({
        'username': os.environ.get('HAIINV_USER_TEST'),
        'password': os.environ.get('HAIINV_PASSWORD_TEST'),
        'url': 'https://sliphup.github.io/json_rest_examples/prueba.json'
    })
    with pytest.raises(AnsibleFailJson) as result:
        my_module.main()

    assert result.value.args[0]['failed'] is True

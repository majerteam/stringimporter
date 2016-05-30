import pytest


_CLS_NAMES = (
    'FooBar',
    'NimporteQuoi',
    'IrgendWas',
)
_OBJ_NAMES = (
    'antigone',
    'barnabe',
    'cassandra',
    'demosthene',
)
_MOD_NAMES = (
    'charybde',
    'scylla',
)


@pytest.fixture(scope="session", params=_CLS_NAMES)
def cls_name(request):
    return request.param


@pytest.fixture(scope="session", params=_OBJ_NAMES)
def obj_name(request):
    return request.param


@pytest.fixture(scope="session", params=_MOD_NAMES)
def mod_name(request):
    return request.param

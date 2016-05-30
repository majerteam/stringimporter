import stringimporter
from .fixtures import cls_name, obj_name, mod_name


_MODULE_TEMPLATE = """
class {0}:
    def __init__(self, name):
        self.name = name


def some_function():
    return {0}('{1}')
"""


def test_importer(cls_name, obj_name, mod_name):
    pycode = _MODULE_TEMPLATE.format(cls_name, obj_name)

    path = "/path/to/file.py"

    loader, mymodule = stringimporter.import_str(
        mod_name, pycode, filename=path
    )

    value = mymodule.some_function()
    assert repr(type(value)) == "<class '{}.{}'>".format(mod_name, cls_name)
    assert value.name == obj_name

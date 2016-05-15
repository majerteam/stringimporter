stringimporter
==================

let's you import raw string as real Python modules

How to use
==========

You can read the tests (in tests directory) or copy the following code.

.. code-block:: python

    import stringimporter

    module_from_thin_air = """
    def multiply_by_2():
        return lambda x: 2*x"""

    loader, mymodule = stringimporter.import_str(module_from_thin_air, 'yihaaa')

    hello_2 = mymodule.multiply_by_2("hello ")

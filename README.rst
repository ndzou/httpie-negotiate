httpie-negotiate
===========

SPNEGO (GSS Negotiate) auth plugin for `HTTPie <https://github.com/jkbr/httpie>`_, based on Jakub's httpie-ntlm example.


Installation
------------

.. code-block:: bash

    $ pip install httpie-negotiate


You should now see ``negotiate`` under ``--auth-type`` in ``$ http --help`` output.


Usage
-----

You need to have a valid Kerberos principal, run kinit first if necessary.

.. code-block:: bash

    $ http --auth-type=negotiate --auth : https://example.org


Kerberos mutual authentication is REQUIRED by default and is recommended.
If you strictly require mutual authentication to be OPTIONAL or DISBALED, then you can use the ``HTTPIE_KERBEROS_MUTUAL`` environment variable.

.. code-block:: bash

   $ HTTPIE_KERBEROS_MUTUAL=OPTIONAL http --auth-type=negotiate --auth : https://example.org
   $ HTTPIE_KERBEORS_MUTUAL=DISABLED http --auth-type=negotiate --auth : https://example.org


You can also use `HTTPie sessions <https://github.com/jkbr/httpie#sessions>`_:

.. code-block:: bash

    # Create session
    $ http --session=logged-in --auth-type=negotiate --auth : https://example.org

    # Re-use auth
    $ http --session=logged-in POST https://example.org hello=world


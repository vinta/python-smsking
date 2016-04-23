python-smsking
==============

A simple Python wrapper for `簡訊王 <https://kotsms.com.tw/>`_ API.

Installation
============

.. code-block:: bash

    $ pip install smsking

Usage
=====

.. code-block:: py

    from smsking import SMSKingAPIClient

    smsking_api = SMSKingAPIClient(
        username='YOUR_USERNAME',
        password='YOUR_PASSWORD',
    )
    smsking_api.send_sms('0912345678', 'YOUR MESSAGE')

References
==========

- `簡訊王：全功能進階技術介接 - 簡訊 API <https://www.kotsms.com.tw/index.php?selectpage=pagenews&kind=4&viewnum=238>`_

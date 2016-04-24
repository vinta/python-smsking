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

    smsking_api = SMSKingAPIClient('YOUR_USERNAME', 'YOUR_PASSWORD')
    smsking_api.send_sms('0912345678', '必須在三天內把這封簡訊轉寄給你的三個朋友，否則你就會一直遇到 UnicodeDecodeError')

References
==========

- `簡訊王：全功能進階技術介接 - 簡訊 API <https://www.kotsms.com.tw/index.php?selectpage=pagenews&kind=4&viewnum=238>`_

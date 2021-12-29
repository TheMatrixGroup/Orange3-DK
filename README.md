Orange3 DynamiKontrol Add-on
======================

Control DynamiKontrol motor modules on Orange3.

https://dk.m47rix.com

| DK Angle | DK Speed |
| --- | --- |
| <img src="https://dk.m47rix.com/static/assets/img/dynamikontrol/angle_07.png" width="400px"> | <img src="https://dk.m47rix.com/static/assets/img/dynamikontrol/speed_01.png" width="400px"> |

Installation
------------

```Orange3-DK```

Development
------------

To register this add-on with Orange, but keep the code in the development directory (do not copy it to 
Python's site-packages directory), run

    pip install -e .

Documentation / widget help can be built by running

    make html htmlhelp

from the doc directory.

Usage
-----

After the installation, the widget from this add-on is registered with Orange. To run Orange from the terminal,
use

    orange-canvas

or

    python -m Orange.canvas

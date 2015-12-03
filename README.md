# KaeruBoilerplate
Boilerplate files for myself

## Install
```sh
./boilerinstall
```
This script loads "kaeru_package.json". Then download with 'git clone' and install to 'res/' directory.

## Usage
```sh
$ ./boiler html5
<html>
    <head>
        <style>
        </style>
    </head>
    <body>
    </body>
</html>
```

```sh
$ ./boiler django/test
from django.test import TestCase


class FooTestCase(TestCase):
    def setUp(self):
        pass

    def test_(self):
        self.fail()
```

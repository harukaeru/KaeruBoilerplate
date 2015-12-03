# KaeruBoilerplate
Boilerplate files for myself

## Install
```sh
$ ./boilerinstall
```
This script loads "kaeru_package.json". Then download with 'git clone' and install to 'res/' directory.

If "kaeru_package.json" is the following, 
```json
{
    "django": "https://github.com/harukaeru/django"
}
```

this script will run the following command.

```sh
$ git clone https://github.com/harukaeru/django res/django

 or 

$ cd res/django; git pull
```

## Usage
```html
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

```python
$ ./boiler django/test
from django.test import TestCase


class FooTestCase(TestCase):
    def setUp(self):
        pass

    def test_(self):
        self.fail()
```

# Table of contents

* [Table of contents](#table-of-contents)
  * [Pre-req](#pre-req)
  * [Upload process](#upload-process)

## Pre-req

* Register an account with (pypi.org)[https://pypi.org]
* Register an account with (Test Pypi)[https://test.pypi.org]
* Install twine with `pip install twine`

## Upload process

* Build your release candidate with:

```bash
python setup.py sdist bdist_wheel
```

* Using a test repository

```bash
twine upload --repository testpypi dist/*
```

will upload to `https://test.pypi.org/project/<sampleproject>`

* Upload the package with

```bash
twine check dist/* # Check for errors/warnings
twine upload dist/*
```

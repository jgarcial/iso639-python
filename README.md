iso639
======
A simple (really simple) library for working with ISO639-3 language codes.
Tested for Python 2.7 & 3.4.

Includes data from Congress library: http://www.loc.gov/standards/iso639-2/php/code_list.php (+ updates)

Installation
------------
The easiest way is using `pip`:

    pip install iso639_3

If you are using Fedora 24+, you can install iso639 using dnf:

    dnf install python2-iso639_3
    # or
    dnf install python3-iso639_3

Thanks, unknown Fedora packagers :-)

Alternatives
------------
* **pycountry**: https://bitbucket.org/flyingcircus/pycountry - a more-featured package
* **iso639**: https://github.com/noumar/iso639 - another package with the same name

Example usage
-------------

```python
import iso639_3

>>> iso639_3.to_name('sv')
u'Swedish'

>>> iso639_3.to_native('sv')
u'svenska'
```

For more examples, see doctests in the source code.

Acknowledgments
---------------
@hosford42 - adding the native language support

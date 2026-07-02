import os
import codecs

# Python 3.4+ compatibility
if 'unicode' not in dir():
    unicode = str


__version__ = '0.2.5'


class NonExistentLanguageError(RuntimeError):
    pass


def find(
    whatever=None, language=None, iso639_1=None, iso639_2=None,
    iso639_3=None, native=None, spanish=None, french=None,
    russian=None, arabic=None, chinese=None, english=None
):
    """
    Find a language entry matching a given criterion.
    Priority when no specific key is provided:
        1. ISO codes (639-1, 639-2, 639-3)
        2. Names (english, native, spanish, french, russian, arabic, chinese)
    """

    # 1. If 'whatever' is provided → search in *all* fields
    if whatever:
        keys = [
            'iso639_1', 'iso639_2_b', 'iso639_2_t', 'iso639_3',
            'name', 'native', 'spanish', 'french', 'russian',
            'arabic', 'chinese', 'english'
        ]
        val = whatever

    # 2. Specific fields (explicit parameters)
    elif iso639_1:
        keys = ['iso639_1']
        val = iso639_1
    elif iso639_2:
        keys = ['iso639_2_b', 'iso639_2_t']
        val = iso639_2
    elif iso639_3:
        keys = ['iso639_3']
        val = iso639_3
    elif language:
        keys = ['name']
        val = language
    elif native:
        keys = ['native']
        val = native
    elif spanish:
        keys = ['spanish']
        val = spanish
    elif french:
        keys = ['french']
        val = french
    elif russian:
        keys = ['russian']
        val = russian
    elif arabic:
        keys = ['arabic']
        val = arabic
    elif chinese:
        keys = ['chinese']
        val = chinese
    elif english:
        keys = ['english']
        val = english

    # 3. NOTHING provided → find best match
    #    Priority: codes first, then names
    else:
        raise ValueError("Invalid search criteria (no search term provided).")

    val = str(val).lower()

    for key in keys:
        for item in data:
            field = item.get(key)
            if val in [p.strip().lower() for p in field.split(',')]:
                return item

    return None


def is_valid639_1(code):
    """Whether code exists as ISO 639-1 code.

    >>> is_valid639_1("swe")
    False
    >>> is_valid639_1("sv")
    True
    """
    if len(code) != 2:
        return False
    return find(iso639_1=code) is not None


def is_valid639_2(code):
    """Whether code exists as ISO 639-2 code.

    >>> is_valid639_2("swe")
    True
    >>> is_valid639_2("sv")
    False
    """
    if len(code) != 3:
        return False
    return find(iso639_2=code) is not None


def is_valid639_3(code):
    """Whether code exists as ISO 639-3 code.

    >>> is_valid639_3("swe")
    True
    >>> is_valid639_3("sv")
    False
    """
    if len(code) != 3:
        return False
    return find(iso639_3=code) is not None


def to_iso639_1(key):
    """Find ISO 639-1 code for language specified by key.

    >>> to_iso639_1("swe")
    u'sv'
    >>> to_iso639_1("English")
    u'en'
    """
    item = find(whatever=key)
    if not item:
        raise NonExistentLanguageError('Language does not exist.')
    return item[u'iso639_1']


def to_iso639_2(key, type='B'):
    """Find ISO 639-2 code for language specified by key.

    :param type: "B" - bibliographical (default), "T" - terminological

    >>> to_iso639_2("German")
    u'ger'
    >>> to_iso639_2("German", "T")
    u'deu'
    """
    if type not in ('B', 'T'):
        raise ValueError('Type must be either "B" or "T".')
    item = find(whatever=key)
    if not item:
        raise NonExistentLanguageError('Language does not exist.')
    if type == 'T' and item[u'iso639_2_t']:
        return item[u'iso639_2_t']
    return item[u'iso639_2_b']


def to_iso639_3(key):
    """Find ISO 639-3 code for language specified by key.

    >>> to_iso639_3("sv")
    u'swe'
    >>> to_iso639_3("English")
    u'eng'
    """
    item = find(whatever=key)
    if not item:
        raise NonExistentLanguageError('Language does not exist.')
    return item[u'iso639_3']


def to_name(key):
    """Find the English name for the language specified by key.

    >>> to_name('br')
    u'Breton'
    >>> to_name('sw')
    u'Swahili'
    """
    item = find(whatever=key)
    if not item:
        raise NonExistentLanguageError('Language does not exist.')
    return item[u'name']


def to_english(key):
    """Find the English name for the language specified by key.

    >>> to_name('br')
    u'Breton'
    >>> to_name('sw')
    u'Swahili'
    """
    return to_name(key)


def to_spanish(key):
    """Find the Spanish name for the language specified by key.

    >>> to_spanish('eng')
    u'Inglés'
    >>> to_spanish('deu')
    u'Alemán'
    """
    item = find(whatever=key)
    if not item:
        raise NonExistentLanguageError('Language does not exist.')
    return item[u'spanish']


def to_french(key):
    """Find the French name for the language specified by key.

    >>> to_french('eng')
    u'Anglais'
    >>> to_french('deu')
    u'Allemand'
    """
    item = find(whatever=key)
    if not item:
        raise NonExistentLanguageError('Language does not exist.')
    return item[u'french']


def to_russian(key):
    """Find the Russian name for the language specified by key.

    >>> to_russian('eng')
    u'Английский'
    >>> to_russian('deu')
    u'Немецкий'
    """
    item = find(whatever=key)
    if not item:
        raise NonExistentLanguageError('Language does not exist.')
    return item[u'russian']


def to_chinese(key):
    """Find the Chinese name for the language specified by key.

    >>> to_chinese('eng')
    u'英语'
    >>> to_chinese('deu')
    u'德语'
    """
    item = find(whatever=key)
    if not item:
        raise NonExistentLanguageError('Language does not exist.')
    return item[u'chinese']


def to_arabic(key):
    """Find the Arabic name for the language specified by key.

    >>> to_chinese('eng')
    u'إنجليزي'
    >>> to_chinese('deu')
    u'ألمانية'
    """
    item = find(whatever=key)
    if not item:
        raise NonExistentLanguageError('Language does not exist.')
    return item[u'arabic']


def to_native(key):
    """Find the native name for the language specified by key.

    >>> to_native('br')
    u'brezhoneg'
    >>> to_native('sw')
    u'Kiswahili'
    """
    item = find(whatever=key)
    if not item:
        raise NonExistentLanguageError('Language does not exist.')
    return item[u'native']


def _load_data():
    def parse_line(line):
        data = line.strip().split('|')
        return {
            u'iso639_2_b': data[0],
            u'iso639_2_t': data[1],
            u'iso639_3': data[2],
            u'iso639_1': data[3],
            u'name': data[4],
            u'english': data[4],
            u'native': data[5],
            u'spanish': data[6],
            u'french': data[7],
            u'russian': data[8],
            u'arabic': data[9],
            u'chinese': data[10],
        }

    data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'languages_utf-8.txt')
    with codecs.open(data_file, 'r', 'UTF-8') as f:
        data = [parse_line(line) for line in f]
    return data


data = _load_data()

import typing

# $ python -X importtime 6-performance-typing.py
# import time: self [us] | cumulative | imported package
# import time:       149 |        149 | zipimport
# import time:       725 |        725 | _frozen_importlib_external
# import time:        95 |         95 |     _codecs
# import time:      3340 |       3435 |   codecs
# import time:      1318 |       1318 |   encodings.aliases
# import time:      6418 |      11170 | encodings
# import time:       580 |        580 | encodings.utf_8
# import time:        98 |         98 | _signal
# import time:       641 |        641 | encodings.latin_1
# import time:        87 |         87 |     _abc
# import time:      2680 |       2766 |   abc
# import time:      2491 |       5257 | io
# import time:       174 |        174 |       _stat
# import time:      1903 |       2077 |     stat
# import time:       596 |        596 |       genericpath
# import time:      2421 |       3016 |     ntpath
# import time:      1323 |       1323 |     _collections_abc
# import time:      3913 |      10327 |   os
# import time:       802 |        802 |   _sitebuiltins
# import time:       111 |        111 |   _winapi
# import time:      1328 |       1328 |   sitecustomize
# import time:      7211 |      19778 | site
# import time:        93 |         93 |       _operator
# import time:      4111 |       4204 |     operator
# import time:       673 |        673 |     keyword
# import time:        72 |         72 |       _heapq
# import time:      1485 |       1557 |     heapq
# import time:       544 |        544 |     itertools
# import time:       906 |        906 |     reprlib
# import time:       109 |        109 |     _collections
# import time:      7517 |      15506 |   collections
# import time:       958 |        958 |   collections.abc
# import time:        76 |         76 |       _functools
# import time:      2812 |       2888 |     functools
# import time:      1967 |       4855 |   contextlib
# import time:       671 |        671 |       types
# import time:      2231 |       2902 |     enum
# import time:       104 |        104 |       _sre
# import time:      1283 |       1283 |         sre_constants
# import time:      3518 |       4800 |       sre_parse
# import time:      2507 |       7411 |     sre_compile
# import time:       227 |        227 |     _locale
# import time:       692 |        692 |     copyreg
# import time:      5729 |      16959 |   re
# import time:      6337 |      44613 | typing
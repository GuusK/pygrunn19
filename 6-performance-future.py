from __future__ import annotations

# $ python -X importtime 6-performance-future.py
# import time: self [us] | cumulative | imported package
# import time:       184 |        184 | zipimport
# import time:       716 |        716 | _frozen_importlib_external
# import time:       104 |        104 |     _codecs
# import time:      2436 |       2540 |   codecs
# import time:      1306 |       1306 |   encodings.aliases
# import time:      7027 |      10871 | encodings
# import time:       785 |        785 | encodings.utf_8
# import time:        98 |         98 | _signal
# import time:       953 |        953 | encodings.latin_1
# import time:        76 |         76 |     _abc
# import time:      1725 |       1801 |   abc
# import time:      1753 |       3553 | io
# import time:       379 |        379 |       _stat
# import time:      2243 |       2621 |     stat
# import time:       786 |        786 |       genericpath
# import time:      3057 |       3842 |     ntpath
# import time:      1421 |       1421 |     _collections_abc
# import time:      5550 |      13433 |   os
# import time:       669 |        669 |   _sitebuiltins
# import time:       108 |        108 |   _winapi
# import time:      1586 |       1586 |   sitecustomize
# import time:      7842 |      23636 | site
# import time:      1458 |       1458 | __future__

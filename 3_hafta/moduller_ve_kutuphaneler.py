### Moduller Ve Kutuphaneler ###

# Modul Nedir ?

"""
Bir modulu bir kod kutuphanesi olarak dusunebiliriz.

Uygulamamiza dahil etmek istedigimiz bir dizi islev iceren bir 
dosya.

"""

# Modul Turleri

"""
- kendi hazirladigimiz moduller
- hazir moduller:
    - standart kutuphane modulleri:python gelistiriciler tarafindan
    - ucuncu sahis moduller:baskalari tarafindan(pypi.org sitesinde modul havuzu)

pip install package_name

"""

# Hazir Modul Kullanimi

import math      # math modulunu dahil etme

print(dir(math))  # math modulundeki fonksiyonlar

"""
['__doc__', '__loader__', '__name__', '__package__',
 '__spec__', 'acos', 'acosh', 'asin', 'asinh', 
 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb',
 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e',
 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 
 'factorial', 'floor', 'fmod', 'frexp', 'fsum',
 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 
 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm',
 'ldexp', 'lgamma', 'log', 'log10', 'log1p',
 'log2', 'modf', 'nan', 'nextafter', 'perm', 
 'pi', 'pow', 'prod', 'radians', 'remainder',
 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh',
 'tau', 'trunc', 'ulp']

"""

help(math)  # daha fazla bilgi alma

help(math.factorial)  # bir fonksiyon hakkinda daha fazla bilgi alma

print(math.factorial(4))  # kullanimi

import math as islem   # math yerine islem ile cagirma

from math import *   # math modulunden tum fonksiyonlari import et.

from math import factorial,sqrt  # modulden istedigimiz metodlari import etme


from random import *  # random modulunu kullanma

print(randint(4, 40))  # random integer sayi uretme

print(uniform(3, 7))  # random ondalikli sayi





























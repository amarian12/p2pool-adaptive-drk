from distutils.core import setup, Extension

x11_hash_module = Extension('x11_hash',
                               sources = ['x11module.c',
                                          'x11.c',
										  'sha3/blake.c',
										  'sha3/bmw.c',
										  'sha3/groestl.c',
										  'sha3/skein.c',
										  'sha3/jh.c',
										  'sha3/keccak.c',
										  'sha3/luffa.c',
										  'sha3/cubehash.c',
										  'sha3/shavite.c'
										  'sha3/simd.c',
										  'sha3/echo.c'],

                               include_dirs=['.', './sha3'])

setup (name = 'x11_hash',
       version = '1.0',
       description = 'x11 Hashing Module For Python',
       ext_modules = [x11_hash_module])

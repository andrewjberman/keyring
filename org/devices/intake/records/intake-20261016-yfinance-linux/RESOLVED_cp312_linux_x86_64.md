# Intake resolve: one exact wheel file per closure member

Written by `org/devices/intake/intake_fetch.py resolve` (schema intake-resolve/1). Target cp312-linux_x86_64; closure `closure_cp312_linux_x86_64_yfinance.json`; index base `https://pypi.org`.

Nothing was downloaded and nothing was installed. Each row is the index's own published file name, digest and size.

`INTAKE-RESOLVE target=cp312-linux_x86_64 members=17 chosen=16 no_wheel=1 requests=17 ok=False new_members=0 specifier_mismatches=0 host_conflicts=0`

| # | Member | Version | Outcome | File name | sha256 | Size | Reason |
|---|---|---|---|---|---|---|---|
| 1 | beautifulsoup4 | 4.14.3 | CHOSEN | beautifulsoup4-4.14.3-py3-none-any.whl | 0918bfe44902e6ad8d57732ba310582e98da931428d231a5ecb9e7c703a735bb | 107721 | rule 1: pure py3-none-any |
| 2 | certifi | 2026.1.4 | CHOSEN | certifi-2026.1.4-py3-none-any.whl | 9943707519e4add1115f44c2bc244f782c0249876bf51b6599fee1ffbedd685c | 152900 | rule 1: pure py3-none-any |
| 3 | curl_cffi | 0.13.0 | CHOSEN | curl_cffi-0.13.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl | 8eb4083371bbb94e9470d782de235fb5268bf43520de020c9e5e6be8f395443f | 8328585 | rule 3: other fitting tag, glibc 2.17 |
| 4 | frozendict | 2.4.7 | CHOSEN | frozendict-2.4.7-py3-none-any.whl | 972af65924ea25cf5b4d9326d549e69a9a4918d8a76a9d3a7cd174d98b237550 | 16264 | rule 1: pure py3-none-any |
| 5 | idna | 3.11 | CHOSEN | idna-3.11-py3-none-any.whl | 771a87f49d9defaf64091e6e6fe9c18d4833f140bd19464795bc32d966ca37ea | 71008 | rule 1: pure py3-none-any |
| 6 | multitasking | 0.0.12 | NO-WHEEL | - | - | - | SDIST-ONLY |
| 7 | numpy | 2.4.2 | CHOSEN | numpy-2.4.2-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl | 9e35d3e0144137d9fdae62912e869136164534d64a169f86438bc9561b6ad49f | 16619782 | rule 2: cp312 manylinux glibc 2.28 |
| 8 | pandas | 2.3.3 | CHOSEN | pandas-2.3.3-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl | b3d11d2fda7eb164ef27ffc14b4fcab16a80e1ce67e9f57e19ec0afaf715ba89 | 12362693 | rule 2: cp312 manylinux glibc 2.28 |
| 9 | peewee | 4.0.0 | CHOSEN | peewee-4.0.0-py3-none-any.whl | 6de14ff11ab50c3152dc1d4e12628c1b28c1e03ff4e4213e463429bfcd7340b6 | 139317 | rule 1: pure py3-none-any |
| 10 | platformdirs | 4.9.2 | CHOSEN | platformdirs-4.9.2-py3-none-any.whl | 9170634f126f8efdae22fb58ae8a0eaa86f38365bc57897a6c4f781d1f5875bd | 21168 | rule 1: pure py3-none-any |
| 11 | protobuf | 6.33.5 | CHOSEN | protobuf-6.33.5-py3-none-any.whl | 69915a973dd0f60f31a08b8318b73eab2bd6a392c79184b3612226b0a3f8ec02 | 170687 | rule 1: pure py3-none-any |
| 12 | pytz | 2025.2 | CHOSEN | pytz-2025.2-py2.py3-none-any.whl | 5ddf76296dd8c44c26eb8f4b6f35488f3ccbf6fbbd7adee0b7262d43f0ec2f00 | 509225 | rule 1: pure py3-none-any |
| 13 | requests | 2.32.5 | CHOSEN | requests-2.32.5-py3-none-any.whl | 2462f94637a34fd532264295e186976db0f5d453d1cdd31473c85a6a161affb6 | 64738 | rule 1: pure py3-none-any |
| 14 | soupsieve | 2.8.3 | CHOSEN | soupsieve-2.8.3-py3-none-any.whl | ed64f2ba4eebeab06cc4962affce381647455978ffc1e36bb79a545b91f45a95 | 37016 | rule 1: pure py3-none-any |
| 15 | tzdata | 2025.3 | CHOSEN | tzdata-2025.3-py2.py3-none-any.whl | 06a47e5700f3081aab02b2e513160914ff0694bce9947d6b76ebd6bf57cfc5d1 | 348521 | rule 1: pure py3-none-any |
| 16 | websockets | 16.0 | CHOSEN | websockets-16.0-py3-none-any.whl | 1637db62fad1dc833276dded54215f2c7fa46912301a24bd94d45d46a011ceec | 171598 | rule 1: pure py3-none-any |
| 17 | yfinance | 1.2.0 | CHOSEN | yfinance-1.2.0-py2.py3-none-any.whl | 1c27d1ebfc6275f476721cc6dba035a49d0cf9a806d6aa1785c9e10cf8a610d8 | 130247 | rule 1: pure py3-none-any |

## Re-check lines (STOP and OK lines for the CTO; nothing here is fixed by the tool)

- HOST-OK cffi host 2.1.1 meets curl_cffi >=1.12.0
- HOST-OK charset-normalizer host 3.5.1 meets requests <4,>=2
- HOST-OK pycparser host 3.0 meets none-from-chosen-parents
- HOST-OK python-dateutil host 2.9.0.post0 meets pandas >=2.8.2
- HOST-OK six host 1.17.0 meets none-from-chosen-parents
- HOST-OK typing_extensions host 4.16.0 meets beautifulsoup4 >=4.0.0
- HOST-OK urllib3 host 2.8.0 meets requests <3,>=1.21.1
- NO-METADATA certifi==2026.1.4 requires_dist absent from the release document
- NO-METADATA frozendict==2.4.7 requires_dist absent from the release document
- NO-METADATA numpy==2.4.2 requires_dist absent from the release document
- NO-METADATA platformdirs==4.9.2 requires_dist absent from the release document
- NO-METADATA protobuf==6.33.5 requires_dist absent from the release document
- NO-METADATA pytz==2025.2 requires_dist absent from the release document
- NO-METADATA soupsieve==2.8.3 requires_dist absent from the release document
- NO-METADATA tzdata==2025.3 requires_dist absent from the release document
- NO-METADATA websockets==16.0 requires_dist absent from the release document


# CTO check 8 -- NFRA_CTLPLN package intake, batch intake-20261016-yfinance-linux (17 files): SIGNED

**Author:** `1.0.0_SA_CTO`, 2026-10-16 ~07:4xZ.
**Records read:** the 17 `*.check.json` records in `org/devices/intake/records/intake-20261016-yfinance-linux/` (merge e0b9a21bc0),
summarised per wheel, plus the issuer's `YFINANCE_BATCH_CHECK6_FINDINGS_READ.md`.
**Approval it rests on:** `CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_YFINANCE_LINUX_20261016.md` and addenda 1-3 (@828fc2092c,
@1fb283d47c, @e8beef9100). Target: dell2's IRPT_ANLREQ resident host (CPython 3.12, linux x86_64, glibc 2.34).

## What checks 1 to 7 show, read from the records

| check | result over 17 wheels |
|---|---|
| 1 sha256 and size equal the index's published values | 17 of 17 passed; each also equals the addendum-1/2 value |
| 2 name, version and tags equal the approved line | 17 of 17 passed |
| 3 the version already runs on this laptop | 16 passed; multitasking 0.0.13 not applicable (0.0.12 is installed) |
| 4 release age and history | 17 passed; youngest multitasking 0.0.13 at 176 days with 12 earlier releases; the rest are 237-570 days old with 37-222 earlier releases |
| 5 build attestation | 7 present and passed (certifi, idna, numpy, platformdirs, pytz, soupsieve, tzdata); 10 not applicable (no attestation published) |
| 6 every `.py` file compared with the installed copy | 12 passed, multitasking not applicable, 4 FAILED: curl_cffi, numpy, pandas, websockets |
| 7 on-access scanner left the file unchanged | 17 of 17 passed |

Batch dependency read: multitasking 0.0.13 declares 0 new dependencies; 0 host conflicts.

## Check 6's four failures, read in full by this seat (not a spot read)

Every `.py` file in the four wheels was compared with the laptop's installed copy, after normalising the installed copy's CRLF
line endings (scratchpad script, read-only):

| wheel | .py files | identical | line endings only | still different | what the remaining difference is |
|---|---|---|---|---|---|
| websockets 16.0 | 48 | 2 | 46 | 0 | -- |
| curl_cffi 0.13.0 | 17 | 1 | 16 | 0 | -- |
| pandas 2.3.3 | 1,415 | 1,414 | 0 | 1 | `pandas/__init__.py`: the Windows copy alone carries a 12-line `# start delvewheel patch` block (`os.add_dll_directory(...pandas.libs)`); nothing else differs |
| numpy 2.4.2 | 406 | 13 | 391 | 2 | `numpy/__init__.py`: the same Windows-only delvewheel block. `numpy/__config__.py`: build metadata only (compiler msvc vs gcc 14.2.1, system windows vs linux, the CI build paths, OpenBLAS MAX_THREADS 24 vs 64) |

So every difference is accounted for by the Windows-versus-Linux build: line endings, the Windows DLL-loader patch, and the
recorded build configuration. No `.py` differs in any other way.

## What they leave, accepted for this one delivery

- **Compiled files are not compared** (numpy 20, pandas 44, curl_cffi 1 native libraries). numpy's attestation ties its file to
  the project's own build pipeline; pandas and curl_cffi publish none. Their long release histories (118 and 101 earlier releases)
  and the published-digest match (check 1) are the remaining assurance.
- **A taken-over maker account** is ruled out only where an attestation exists (7 of 17).
- **Check 7** does not show that the scanner inspected the files (FWD-17's limit stands).

**Why these are accepted:**
- these are mainstream, long-lived packages;
- the use is one library set for one Opal-internal host, installed by dell2 under its own never-widen pair after delivery;
- nothing is added to `requirements.txt`.

A wider use is a new batch.

## Files covered by this signature (batch intake-20261016-yfinance-linux)

```
beautifulsoup4-4.14.3-py3-none-any.whl
certifi-2026.1.4-py3-none-any.whl
curl_cffi-0.13.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
frozendict-2.4.7-py3-none-any.whl
idna-3.11-py3-none-any.whl
multitasking-0.0.13-py3-none-any.whl
numpy-2.4.2-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl
pandas-2.3.3-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl
peewee-4.0.0-py3-none-any.whl
platformdirs-4.9.2-py3-none-any.whl
protobuf-6.33.5-py3-none-any.whl
pytz-2025.2-py2.py3-none-any.whl
requests-2.32.5-py3-none-any.whl
soupsieve-2.8.3-py3-none-any.whl
tzdata-2025.3-py2.py3-none-any.whl
websockets-16.0-py3-none-any.whl
yfinance-1.2.0-py2.py3-none-any.whl
```

## Signature

**CHECK 8 SIGNED -- release, pack and Taildrop to dell2 may proceed for these 17 files.** `1.0.0_SA_CTO`

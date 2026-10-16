# CTO approval to FETCH -- NFRA_CTLPLN package intake, batch intake-20261016-yfinance-linux (17 lines)

**Author:** `1.0.0_SA_CTO`, 2026-10-16 ~06:1xZ.
**Ruling it serves:** `CTO_RULING_XB983C_YFINANCE_LINUX_CLOSURE_20261016.md` @5740f0d341 (dell2's IRPT_ANLREQ resident host,
`2.0.0_SA_COO~G2`).
**Closure:** `org/devices/intake/closure_cp312_linux_x86_64_yfinance.json` (CT-ar-1, merge 97477e8786).
- 24 members; 0 conflicts.
- 7 left out as host-satisfied, read against the host's pydeps: cffi, charset-normalizer, pycparser, python-dateutil, six,
  typing_extensions, urllib3.
- 17 to fetch.

**Requests:** the nine UNKNOWN members were decided APPROVED by this seat at ~06:1xZ (REQ-20261016T0606xx-{certifi, frozendict,
idna, multitasking, peewee, platformdirs, protobuf, soupsieve, tzdata}). The other eight read APPROVED from `requirements.txt`.

**Second approver:** `1.0.0_SA_CTO~DELL2` approves the same 17 lines (his msg 9075). The fetch waits for both.

## The approved lines (name==version)

```
intake-20261016-yfinance-linux
yfinance==1.2.0
beautifulsoup4==4.14.3
certifi==2026.1.4
curl_cffi==0.13.0
frozendict==2.4.7
idna==3.11
multitasking==0.0.12
numpy==2.4.2
pandas==2.3.3
peewee==4.0.0
platformdirs==4.9.2
protobuf==6.33.5
pytz==2025.2
requests==2.32.5
soupsieve==2.8.3
tzdata==2025.3
websockets==16.0
```

## Conditions

1. **Target wheels:** CPython 3.12, linux x86_64, manylinux at or below glibc 2.34, or a pure `py3-none-any` wheel. The closure's
   versions were read from the laptop's Windows installs, so Linux availability is UNREAD.
   - The issuer's index-metadata cell reads the exact wheel file name for each line before ANY download.
   - This seat then adds those 17 file names to this file as ADDENDUM 1. The fetch matches the addendum, not this section.
2. **The six compiled members** (curl_cffi, numpy, pandas, protobuf, websockets; cffi is host-satisfied) are the risk.
   - A line with no matching wheel is a STOP back to this seat.
   - Never a source build. Never a silent version change.
3. **Re-check the host-satisfied set against the Linux metadata:** a fetched member whose requirement the host's version no
   longer meets is a STOP.
4. Nothing is added to `requirements.txt`. Delivery ends at the release folder and a Taildrop to dell2 (ruling term 4).
5. Check 8 is signed once, for the batch, after the per-wheel check records are read in full.

**APPROVED TO FETCH, subject to ADDENDUM 1 and the dell2 CTO's approval** -- `1.0.0_SA_CTO`

## ADDENDUM 1 (~06:4xZ): the exact wheels, from the issuer's resolve (`RESOLVED_cp312_linux_x86_64.md` @c347d4e52e)

The resolve made 17 release-document reads at pypi.org, every one returning 200, and downloaded nothing. It found 0 new members,
0 specifier mismatches and 0 host conflicts; 7 of 7 host-satisfied members read HOST-OK. **The fetch matches these 16 file
names and sha256 values exactly:**

```
intake-20261016-yfinance-linux
beautifulsoup4-4.14.3-py3-none-any.whl
certifi-2026.1.4-py3-none-any.whl
curl_cffi-0.13.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
frozendict-2.4.7-py3-none-any.whl
idna-3.11-py3-none-any.whl
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

The sha256 for each is the resolve table's value; check 1 compares against it.

Every glibc tag is at most 2.28, under the host's 2.34. The nine NO-METADATA rows are accepted: the closure was computed from
installed METADATA, not from the index documents, so their dependencies were read there.

**multitasking (the STOP):** 0.0.12 publishes only a source archive. This seat does NOT accept a source build. It approves a
version change by this rule, stated here so that it is not silent:
- The issuer reads multitasking's project document (one more index read, no download).
- It chooses the HIGHEST version >= 0.0.7 that publishes a `py3-none-any` (or `py2.py3-none-any`) wheel.
- It files a request for that exact version, which this seat decides on sight.
- The chosen file name is added as ADDENDUM 2.
- If no version has a wheel, it comes back to this seat. Building a wheel from the source archive is a separate decision and is
  not approved.

## ADDENDUM 2 (~06:4xZ): multitasking, by addendum 1's rule

`REQ-20261016T063809Z-multitasking` was decided APPROVED. The issuer read the project document (one request, 200): 0.0.13 is the
highest version >= 0.0.7 that publishes a wheel (0.0.11 also has one; 0.0.12 and below publish only source). It was uploaded
2026-04-23. The 17th line:

```
multitasking-0.0.13-py3-none-any.whl   sha256 ec9243af140c67bfe52dc98d7173c294512735a88e8425c458b250db99dc2b48   16380 bytes
```

**Condition:** this version is newer than the laptop's 0.0.12, so its own dependencies are unread. Check 6 reads the wheel's
METADATA `Requires-Dist`, and any dependency not already in the closure or on the host is a STOP back to this seat.

The batch is now 17 lines. The fetch waits only on `1.0.0_SA_CTO~DELL2`'s approval of these 17.

## ADDENDUM 3 (~07:1xZ): the exact name==version line the fetch tool matches

The fetch tool matches an exact `name==version` string, and addendum 2 named 0.0.13 only inside a file-name row, so the tool
refused it (`2.0.0_SA_COO~C` msg 109638). The approved line is:

```
multitasking==0.0.13
```

It SUPERSEDES the `multitasking==0.0.12` line in "The approved lines" above. 0.0.12 is source-only and is NOT approved for fetch.

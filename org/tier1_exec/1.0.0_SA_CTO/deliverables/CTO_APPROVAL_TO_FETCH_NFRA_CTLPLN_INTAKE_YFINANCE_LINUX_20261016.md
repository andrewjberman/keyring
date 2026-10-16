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

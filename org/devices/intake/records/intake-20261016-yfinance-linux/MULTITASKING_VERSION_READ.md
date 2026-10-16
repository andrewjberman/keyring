# multitasking: which version publishes a wheel (read by 2.0.0_SA_COO~C, 2026-10-16 ~06:38Z)

**Why:** `RESOLVED_cp312_linux_x86_64.md` reads `multitasking==0.0.12` as `NO-WHEEL SDIST-ONLY`. The CTO's addendum 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_YFINANCE_LINUX_20261016.md` @828fc2092c, msg 109629) ruled: read the project document and choose the highest version >= 0.0.7 that publishes a `py3-none-any` or `py2.py3-none-any` wheel; file a request for that exact version. yfinance 1.2.0 requires `multitasking>=0.0.7`.

**The read:** ONE request, `GET https://pypi.org/pypi/multitasking/json`, through `intake_fetch.Fetch.get_json` (the tool's closed host set and size limits), status 200. No file was downloaded and nothing was installed.

| version | files | wheels (not yanked) |
|---|---|---|
| 0.0.13 | 2 | `multitasking-0.0.13-py3-none-any.whl` |
| 0.0.12 | 1 | none (source archive only) |
| 0.0.11 | 2 | `multitasking-0.0.11-py3-none-any.whl` |
| 0.0.10 | 1 | none |
| 0.0.9 | 1 | none |
| 0.0.8 | 1 | none |
| 0.0.7 | 1 | none |

**Chosen by the rule:** `multitasking==0.0.13`, `multitasking-0.0.13-py3-none-any.whl`, 16380 bytes, sha256 `ec9243af140c67bfe52dc98d7173c294512735a88e8425c458b250db99dc2b48`, uploaded 2026-04-23, `requires_python` not set, not yanked. It is NEWER than the laptop's installed 0.0.12, so it is a version change the CTO's addendum ruled; its own dependencies are unread (the release document was not requested: the resolve tool's gate names only approved lines).

**Request filed:** `REQ-20261016T063809Z-multitasking` (multitasking==0.0.13), status `REQUESTED` after filing.

# Y-3 V1 and the control run, 2026-10-03 00:10Z-00:32Z -- outcome

**Seat:** `2.0.0_SA_COO~Y`. **Packet:** `Y3/NEVER_WIDEN_SIGNOFF_PACKET_Y3_20261002.md` (CTO half batch 194).
**Claim words:** `measured` = read this session; `inferred` = from evidence, not observed.

## The runs (measured)

| run | request | what happened |
|---|---|---|
| V1-a 00:10Z | `REQ-66e9fe1a..`: Multi-Comp `[opal_ultra_long_term, IWM]` on the 12.03 file (AAPL, VNQ) | upload NORMALIZED; submission accepted with IWM (QUEUED). Job: template GET 200 (set_cookie 1); securities_info 200, IWM verified 1 of 1; holdings_upload POST **403 text/plain 76 B**, no WAF action -> ATTENTION `VENDOR_UPLOAD_REFUSED` |
| V1-b 00:20Z | `UP-fbd4732c..`: AAPL+TIMXX, upload only | `IRPT_RESIDENT_RESOLVE_FUNDS matched=0 gated=1 features=mutualFundDataUSA=1` -- S284 MEASURED (row S287) |
| control 00:31Z | `REQ-06185d70..`: Overview on the same 12.03 file, NO ETF (no identity read) | upload NORMALIZED; job: template GET **403 text/plain 76 B**, no WAF -> `IRPT_RESIDENT_EVICTION verdict=EVICTED`; the job's one refresh (headless capture) -> `CAPTURE_FAILED:AUTH_FAILED:NO_AUTHENTICATED_PROBE`; message retained, refresh spent |

## What it shows

- **S285's 403 is the SESSION, not Y-3 (measured).** The control ran no identity read and met the identical 403 on its
  very first vendor request. The resident classes that 403 as an eviction. The stored session
  (`ycharts/session/current`, fence 23, captured 2026-10-02 09:45:43Z) no longer authenticates, and the resident's own
  re-capture cannot sign in.
- **Y-3 itself (measured):** the submission admits IWM, and the resident's identity read verifies it on the first read.
  READY was not reached because the session died between the identity read and the upload. ULT has still never run to
  READY.
- **Not determined:** what evicted the session at about 00:10Z. Possibilities: its age (about 14.5 h), a browser sign-in
  elsewhere with the same login (row S233's hazard), or the vendor's own action. The identity GET was a 200 just before
  the 403.

## Traffic

STOPPED after the control. The control's retained message can make at most one more template GET (403). Its
session_refresh intent is already claimed, so it then ends ATTENTION `SESSION_REFRESH_ALREADY_USED`, with no second
sign-in.

**Remedy:** a session re-capture -- the attended sign-in (option A, `SIGNIN_A` packet section 4) at Andrew's time,
queue 0/0. Then Y-3's READY (V1-a again) and Case A's Y-5 runs.

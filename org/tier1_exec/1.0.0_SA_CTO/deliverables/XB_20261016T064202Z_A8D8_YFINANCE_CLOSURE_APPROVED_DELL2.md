# XB-20261016T064202Z-a8d8 -- dell2 CTO: the yfinance==1.2.0 Linux cp312 closure (17 wheels to fetch) APPROVED

**Seat:** `1.0.0_SA_CTO~DELL2`, 2026-10-16 ~06:5xZ. **Asked by:** `2.0.0_SA_COO~C` (laptop, NFRA_CTLPLN round 27), body
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/XB_YFINANCE_R27_DELL2_CTO_APPROVAL.md`. Closure file
`org/devices/intake/closure_cp312_linux_x86_64_yfinance.json`: 24 members, conflicts 0, unparsed 0, unknown 0.

## Read by this seat

- **The 24 members** (name==version), compared against the workspace pins in `requirements.txt`. Every member the workspace pins is at the
  SAME version: numpy 2.4.2, pandas 2.3.3, requests 2.32.5, pytz 2025.2, urllib3 2.6.3, beautifulsoup4 4.14.3, websockets 16.0, curl_cffi 0.13.0,
  yfinance 1.2.0. No member contradicts a workspace pin.
- **The 7 satisfied by the host's pydeps,** two at newer versions than the closure computed (cffi 2.1.1 against 2.0.0, charset-normalizer
  3.5.1 against 3.4.4). Both are inside their dependents' ranges as the closure resolver reads them, so they are not refetched.
- **multitasking 0.0.13 instead of 0.0.12:** the wheel-only rule, because 0.0.12 is source-only. Accepted, under the laptop CTO's rule.

## Approval

**APPROVED: the 17 wheels named in addenda 1 and 2, by exact file name, sha256 and size.** Wheels only. A source build, a different
version or a different file is NOT approved and is a STOP.

**Conditions:**
- The laptop's per-wheel checks 1-7 and the laptop CTO's check 8 pass before the Taildrop.
- `0.0.0_AB_MSTR~DELL2` collects the files, and every sha256 is re-checked on dell2.
- The install into the resident host's `pydeps` goes under its own never-widen pair (`~G2` packet, AQ2 applier), which this seat signs,
  with an import check of `yfinance`, `pandas` and `numpy` through the resident interpreter.
- **Named, not a stop:** nine members' index documents list no dependencies, so their own dependencies are unread. The pydeps pair's
  import check is the guard for that.

-- `1.0.0_SA_CTO~DELL2`

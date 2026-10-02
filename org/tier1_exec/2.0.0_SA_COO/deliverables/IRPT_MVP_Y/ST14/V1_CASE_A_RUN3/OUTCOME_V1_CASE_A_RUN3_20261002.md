# st14 V1 -- Case A run 3 (Y-1 from the page), 2026-10-02 23:24Z -- outcome

**Seat:** `2.0.0_SA_COO~Y`. **Packet:** `ST14/NEVER_WIDEN_SIGNOFF_PACKET_ST14_20261002.md` (CTO half batch 188).
**Run:** `2.0.0_SA_COO~D`'s `yh-submit-case.mjs --queue-empty`, the easy file (sha256 500837992a3b9caa), Cottonwood.
**Claim words:** `measured` = read this session; `inferred` = from code and evidence, not observed.

## What happened (measured)

| time (Z) | what | evidence |
|---|---|---|
| 23:24:44 | upload POST with `selected_tenant` answers RESOLVING, `UP-f0d8aead..` | ~D msg 104452; `BACKEND_JOIN_20261002.json` (server 708 ms; 20.2 s queued in the browser) |
| 23:25:09 | resident: `IRPT_RESIDENT_RESOLVE_FUNDS matched=1 refused=0 causes=-`, then `RESOLVE state=READY` | journal watch; ONE securities_info read, no WAF challenge |
| 23:25:09 | NORMALIZATION: NEEDS_CORRECTION, reason TEMPLATE_FINDINGS, ONE finding: row 100 (TIMXX) col A `TICKER_CHECK_UNAVAILABLE` | irpt-requests row, read 23:2xZ |
| 23:25:19 | the page's re-post reads NEEDS_CORRECTION; no submission | ~D msg 104452 |

## Grade against the packet's V1

- **S279's defect is FIXED (measured).** The same file failed AS A WHOLE at 19:04Z (`RESOLVE_RETRY_EXHAUSTED` after four
  reads). It now resolves on the first read in about 2 s, and every other row of 99 is accepted. The one row that
  cannot be used is named: row 100, column A. The first lookup met no WAF challenge.
- **V1's criterion is NOT met (measured):** the upload is not NORMALIZED with `M:TIMXX`. No report was generated.
- **Cause of row 100 (inferred, not observed).** The resolver attributed YCharts' `M:TIMXX` row to TIMXX (`matched=1`),
  and the row's display id, ids and fields verified (`refused=0`). The freeze still names it `TICKER_CHECK_UNAVAILABLE`.
  The only path in code that leaves a verified, attributed fund row unusable is a non-empty `features_needed`:
  `PROVIDER_ENTITLEMENT_UNVERIFIED`, state UNAVAILABLE (`intake/security_resolution.py`, the entitlement branch). That
  is the shape the CRO capture shows for funds (`M:BREIT.S` needs `evergreenFundData`). Opal's YCharts account would
  then lack the data feature that fund needs.
- **Not determinable without another vendor read:** which feature. The resident keeps no receipt and caches no
  UNAVAILABLE answer. st14's journal counts an entitlement-gated row as `matched`, which it should name separately
  (fix below). Per batch 188, a different shape is recorded, not retried.

## What follows

1. **Journal, next packet (Y-3's):** count an entitlement-gated fund row as `gated=` and name it on the resolve line, so
   the next run measures it instead of inferring it.
2. **The row's words:** an entitlement-gated row reads `TICKER_CHECK_UNAVAILABLE` / REPLACE_FILE. It is a real security
   YCharts will not price for this account. Y-5's user-named proxy is the remedy a user can act on; a named code
   (an entitlement) belongs with that packet.
3. **Case A as a file:** it reaches READY only once TIMXX is proxied (Y-5), dropped by the user, or entitled on the
   account (Andrew's, a vendor-account question).

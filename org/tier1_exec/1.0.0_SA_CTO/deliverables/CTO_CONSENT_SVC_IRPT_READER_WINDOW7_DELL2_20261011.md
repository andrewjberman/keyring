# CTO consent -- svc-irpt secret-reader WINDOW 7 for dell2 (one re-read of REQ-5e4149d2's status job with the date header)

From 1.0.0_SA_CTO (laptop), 2026-10-11 ~05:2xZ, on 0.0.0_AB_MSTR msg 108220 (dell2 2.0.0_SA_COO~G2 msg 4157;
1.0.0_SA_CTO~DELL2 msg 4152 rules the re-read; IRPT_YCDGEN.TO-APPLY-sr2 @0d42c732d3 at 0.7.0_AE_CloudOps~YC2).

## Consent: YES, on WINDOW 6's terms exactly, with NO start hold

Terms, policy files, executor, blast radius and steps: `CTO_CONSENT_SVC_IRPT_READER_WINDOW6_DELL2_20261011.md`, except:
- No start condition: irpt-status still reads `6idtFvAm` (window 6's release); the put happens on this consent.
- Expected use: ONE GET (the status job re-read with `X-IRPT-Status-Dates: prospect-v1`, which the 04:52:49Z read omitted).
- Close: G2's R-done via MSTR, or PUT TIME + 30 minutes, whichever first. PUT TIME to MSTR for G2 FIRST after the read-back.

Executor `0.7.0_AE_CloudOps~CTL` (live), window 7 appended to TO-APPLY-30 as windows 2-6 were. This file is the GO.

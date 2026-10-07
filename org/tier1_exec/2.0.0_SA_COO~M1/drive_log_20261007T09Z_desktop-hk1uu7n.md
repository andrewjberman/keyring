# /canonical-drive -- 2.0.0_SA_COO~M1 on dell1 -- 2026-10-07 08Z-09Z

Scope: MDPF_SECCLASS (DIRECTED, 10m). Lease FULL each tick. Limb L7, round 8.

| tick (UTC) | TOs terminal | outcome |
|---|---|---|
| ~08:4xZ | 1/18 | (1) drained TO-SC-e30 (7ab55c330b); LGIC amendment to e28/e31 (d32d35cd3f); slot ~26 re-seated on e31 |
| ~08:5xZ | 5/18 | (1) drained e25, e23, e24; e21 ruled (W21-S2, 67020c3473); e35 COO half signed (fac4c6afba); ruff drift to MSTR~DELL1 |
| ~09:0xZ | 8/18 | (1) e35 CTO half REFUSED -> option (B): e38 widened to the 46-file census (71eff11201); e26 drained; e33 ruled (W23-S4, 1910d1f20f) |
| ~09:1xZ | 9/18 | (1) row S49 (a worker's PyPI download) filed, reported; e21 COO half option (b) (84362009e7); e36 done, held |
| ~09:2xZ | 14/18 | (1) e40, e27, e33 drained; e21 CTO half signed (59cfbf169b), publish refused by owned-paths lane -> grant asked; e31 merged (ff5d651f2b) after reading the push gate's shipped set |

Decisions closed this hour:
- Shipped-file rule for the round branch: nothing that the pre-push deploy gate uploads (`safe_deploy_core.py` gold trees and the
  three `lib/_shared` members) enters `coo-m1-secclass-r8` until its halves sign; measured at ff5d651f2b: 0 of 78 files in range.
- Held off the branch: e21 (both halves signed; publishes alone from origin once the lane grant lands), e35/e36/e37 (uploads ordered
  after e38 by the issuer's choice of the CTO's option B).
- Workers cannot be resumed after they finish: each next order re-seats the slot with its inherited commits named.

Armed: S46 (seed hazard; the CTO half for option (b) authorizes no seed run), S49 (egress; every later spawn forbids installs).

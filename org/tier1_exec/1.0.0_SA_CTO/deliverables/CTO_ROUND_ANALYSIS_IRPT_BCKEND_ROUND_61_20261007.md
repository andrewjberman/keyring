# IRPT_BCKEND -- ROUND ANALYSIS, round 61 (sweep 10)

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~09:4xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES. This answers `3.0.0_SA_CVO`'s slug (msg 275):
REMEDIATION_v21 @bc794d2770. 16 rows: 10 dismissed, 6 OPEN. Closed in place: S335, S347, S339 (disarmed), S320, S338. ARMED after:
S334, W127-S1 and S352 (BLOCKING). The rounds 47-60 analysis (@e363a194ed) still holds except where this file changes it.

## 1. Outcome state -- 0 of 12 REALIZED (unchanged)

Round 61 drained its code (IB-pr-329..334) and closed E-Y1..E-Y3. No outcome turned, because the release that serves E-P5 and E-P6
(the directory release) is not yet applied. Its two halves are now given: COO @0c3d443030, CTO @74e91285b4. FWD-7 is graded when that
release's real runs 3(a)-3(c) are read.

## 2. Dispositions

| row | disposition | owner | closes on |
|---|---|---|---|
| S348, S357, W136-S1 | Close with the round-61 directory release. The CTO half pins `handler.py` back (S357) and requires the two-instrument consumer census before the build (W136-S1). S348 closes on run 3(a) | `~P2` | the release's legs and its after-reads (firm-bucket reads as laptop FILES) |
| S352 (BLOCKING) | Ruled (a): a laptop read delivered as a FILE (msg to `~M2` 08:50Z). The first read is in (@e9993e95fa); the second, with the amended reader (S356), is relayed (msg 263) | `~M2` | `~M2` grades E-M1 on the second FILE. S352 disarms when FWD-5 is graded from it, or when NFRA_CTLPLN round 4 admits the dell2 read |
| S356 | The issuer amended its own reader (Andrew-direct 2026-09-24: an issuer amends its own criteria). No ruling needed | `~M2` | the second read |
| W137-S1 | FWD-2's gated arms: one fixture per gated route can be built now. The run that grades FWD-2 needs the test principal Andrew names (rounds 47-60 analysis, section 6, act 2) | `~P2` builds the fixtures; Andrew names the principal | FWD-2's full run |
| W127-S1 | IB-pr-332's build passes the parity gate. The disarm row is owed | `~P2` | `~P2` files the disarm row citing that build |
| S334 | Unchanged: the laptop's (shared tooling) | laptop `1.0.0_SA_CTO` | -- |

## 3. The ENRICHMENT LIST -- round 62, one issuance per workstream

### ~P -> `2.0.0_SA_COO~P2` (4 items, besides the directory release already signed)

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E-P8 | **The custodian-key seam holds no 'None'** (IRPT_CUSTDY row W5-S1) | (1) `_ids/data/custodian_key_seam.json` carries no value equal to the string `None` (826 today), and a test fails on the file as it stands; (2) `ids.py` treats a `None` string as unmapped beside its `is not None` guard (`:387-388`), with a test; (3) the file's writer is named, or "not in the repo" is filed as a row | LOCAL |
| E-P9 | **The export takes a client report** (IRPT_CUSTDY W4-S1, ruled (a) @822468e309; a1-a4) | (1) submit-export resolves, grants and freezes a client-report document reference into the bundle, as IB-pr-281 did for ANALYSIS, with tests; (2) the render host dispatches a `client-report` kind and REFUSES an unknown template name (`render_export.cjs:240`; today an unknown name renders PERFORMANCE), with a test of each; (3) the portal print package lists the kind and its schemaVersion. The page part waits on dell2's portal toolchain (relayed 09:39Z) | LOCAL |
| E-P10 | **One fixture per gated route** (W137-S1, FWD-2) | (1) the route census of `/api/scoped/` investor-reporting routes is printed with its count; (2) each gated route has a fixture for the allowed and the denied principal class; (3) the battery runs green on the fixtures | LOCAL |
| E-P11 | **The W127-S1 disarm** | (1) the disarm row cites IB-pr-332's build and its parity-gate pass | LOCAL |

E-P9's served release is a later packet with its own halves. E-P8 is independent. Fan-out 3.

### ~Y -> `2.0.0_SA_COO~Y2` (1 item)

| # | item | criteria | risk |
|---|---|---|---|
| E-Y4 | **Drop fixtures/har from irpt-ycharts-generate's files[]** (ruled msg to `~Y2` 09:01Z) | (1) a trace of every reader over the package at the pin (any open, not only imports) shows no runtime reader; (2) the built package has no fixtures/har member and the repo tests still pass; (3) a planted runtime open is caught by the trace | LOCAL |

It rides the function's next release (`~G2`'s resident build if that is the one).

### ~M -> `2.0.0_SA_COO~M2`

No new cut. E-M1 is graded on the second laptop FILE.

-- 1.0.0_SA_CTO~DELL2

# C2 orphan-reap deploy completion ledger -- CLOSED

Opened 20260714T0758Z, closed 20260714T081xZ, by 0.6.2_AE_PartnerETL. Chain finished in-session per NEVER#6.

**Authority chain:** Andrew verbatim GO ("Go for sure on 1.)", ~05:5xZ ET, relayed COO 060839Z) + CTO
grant-gate PASS at his source read of 2d2b13705 + COO re-confirm 075027Z (crash adjudicated: pre-crash
gate-pass governs) + CTO no-objection 075236Z (in-window). Key list bound at git blob
f5ead206452c237a9d07713eaacfa0a8e50bc33f (@ 2cc0f8fee), checkout re-verified 2,269 keys / 0 stray.

| Leg | Target | Proof | Closed |
|---|---|---|---|
| L1 tf-apply | opal-c2-orphan-reap-role + inline policy | safe-apply 2/0/0; post-apply plan "No changes"; role ARN output live | 0800Z |
| L2 exercise | 22a simulate matrix | 11 calls, one --resource-arns each, positive control isolated: orphan-first + orphan-last DeleteObject=allowed; typed-assets/typed-positions/schwab-key/bd-plane/cot-plane/inf-Door6 = explicitDeny; GetObject/PutObject on orphan = implicitDeny; conditioned ListBucket(prefix ctx) = allowed | 0803Z |
| L3 data-op | reap 2,269 pinned keys | dry-run then --execute: snapshot total=6,909 flat=2,269 typed=4,640 (run-time enumerated); SET IDENTITY asserted (symmetric diff empty); deleted=2,269 markers=2,269 errors=0; post flat=0, typed SET unchanged (4,640). Transcript: org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/C2_ORPHAN_REAP_TRANSCRIPT_20260714.txt; script: c2_orphan_reap.py (same dir) | 0805Z |
| L4 tf-apply | grant REMOVAL | tf file deleted + committed; plan 0/0/2; safe-apply "2 destroyed"; post plan "No changes"; closure evidence: get-role=NoSuchEntity AND simulate-principal-policy=NoSuchEntity (the principal itself no longer exists -- STRONGER than the ruled implicitDeny form, recorded so the absent implicitDeny output is not read as a skipped step) + former-orphan key absent from current listing | 0812Z |
| L5 handoff | 0.7.0 guard re-run | ping 080528Z delivered; his ACK 081133Z: mirror re-invoke dispatched 08:07Z async, expects orphan_class 2269->0 / missing=0 / alien=0; tightened C2 close to COO, CC me. 30 cot markers NOT touched (his baseline-30 stays honest) | 0811Z (result async, his lane) |

**Semantics for the record (CTO):** versioned-without-expiry bucket -- the deletes wrote MARKERS; corrupt
bytes persist as noncurrent versions BY DESIGN; the guard reads current listings, 0 = success.

# CTO half -- MDPF_SECCLASS SC-e-76, Black Diamond reads the canonical NAME:: row when the identity chain cannot place a position -- SIGNED WITH CONDITIONS

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-08 ~19:4xZ. **Request:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_NAME_KEY_LOOKUP_20261008.md`
(COO half SIGNED by `2.0.0_SA_COO~M1` @ff248f0bc7; msg 1104). Row D1-S11, the trace @3d9077bdc5, round 15.

## Blast radius signed

- **Code:** `s3://opal-data-bd/code/gold/lib/etf_classifier.py`, one object. Rollback target VersionId `ui9A4u.YluQQJKJVvwGAfTkK8frV5LFs`.
- **Bundle side effect:** the deploy also re-ships three `_shared` members. Two are byte-identical. The third,
  `etf_classification_scheduled.py`, differs: it carries e65b's change.
- **Data, at the next BD gold fire:** the files C_06, D_03 and D_04 already write. In content, only blank-ticker positions the chain could
  not place move out of `unclassified`. The candidate is 764 securities and $132.56M, moving firm unclassified from 6.94 pct to about
  0.38 pct. No ticker position and no chain-placed position moves. `etf-classifications` is read only.

## Read at signing

- Writers of the served BD class: N = 3 (C_06, D_03, D_04), each calls `classify_with_identity`. The change reaches all three, and the
  control tests pin that a ticker, CASH_USD or chain-placed position returns exactly what it returned before.
- Both branches covered: (a) the fire loads the lib, and the classes land as in the candidate table; (b) no fire, nothing served moves.
- The classes that land are the table's. Shield and buffered notes land as `structured`, consistent with the amended D1-S11 acceptance.
  The open question to Andrew on the 21 liquid-alternative mutual funds concerns SC-e-77's row set, not this lookup. If he moves them,
  the move happens in the table and this lib reads it.

## Conditions

1. **Bundle option (b) is accepted for this deploy only**, on three inert precedents today (rows D1-S12/S13: 0 BD invocations in each
   window, with a positive control). Re-copy `etf_classification_scheduled.py` to ETag 3f1e6be8 within 2 minutes of the deploy, then
   read the BD dispatch Lambdas' invocations across that window and put the count in the ledger. A non-zero count is a STOP-and-report
   to this seat. Option (b) is not a standing permission: the laptop `4.0.0_SA_CRO~B` fix removes the need for it.
2. Before the 23:00Z fire, record in the ledger the pre-fire VersionIds of `platinum/firm/mix_summary.json` and
   `gold/views/mix_daily_summary.json` (versioning Enabled, measured 19:1xZ).
3. Leg G closes on the served `mix_summary.json` read after the fire: the unclassified share, printed beside the candidate's 0.38 pct and
   the 5.0 pct limit. A share above 5.0 pct is a finding to this seat, not a close.

**SIGNED** (with conditions 1-3) -- `1.0.0_SA_CTO~DELL1`.

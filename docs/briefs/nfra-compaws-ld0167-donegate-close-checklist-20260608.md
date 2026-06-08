# NFRA_COMPAWS — LD-0167 done-gate close checklist (pre-staged)

**Author:** 1.0.0_SA_CTO · 2026-06-08 · for COO (zero-delay close when the 13th cert lands).
**Trigger:** CVO posts the **13/13 CVO-INDEPENDENT** cert tally (all 13 classes F1 ≥95% + brittleness PASS — not
AE self-grade). Currently 10/13; remaining = StepFunctions (re-cert in CVO inbox, nested-walk fixed v0.6), IAM, SNS.

| # | Step | Owner | Detail |
|---|---|---|---|
| 1 | **Cert tally signed** | CVO | Authoritative 13/13 scorecard (per-class F1 + brittleness), the close TRIGGER. |
| 2 | **Schema → v1.0** | CTO | Bump `NFRA_COMPAWS_SCHEMA.md` v0.6 → **v1.0** (the 13-class taxonomy is now certified-canonical; the hand-audit fixtures become the regression baseline). |
| 3 | **First snapshot-archive** | AE | Run `comp-aws snapshot` (PRD §6a) — **run it AT 13/13**, not deferred: the certified-complete graph IS the regression-fixture baseline. Tarball → `s3://opal-313476888478-globgrph/snapshots/` (TF-commit-stamped). |
| 4 | **Absorption confirm** | AE | Verify comp-lambdamap Phase-2 + comp-iam are folded into comp-aws (no double-build, per PRD). |
| 5 | **Registry update** | COO | `NFRA_COMPAWS.json` phase → "13/13 CVO-CERTIFIED — LD-0167 done-gate MET; awaiting MSTR /verify-channel closeout." **status STAYS `active`** until MSTR closes (the tool persists; build-done ≠ project-closed). |
| 6 | **MSTR notify + ledger** | CTO→MSTR | Notify MSTR the done-gate is MET (cite the CVO 13/13 scorecard). MSTR authors the LD-0167 close entry + runs the **/verify-channel project-level closeout** (the LD-0167 bar: CVO-independent F1≥95%/class + brittleness, MSTR-held). |
| 7 | **Project close** | MSTR/COO | ON MSTR closeout: REGISTRY row → Completed section; `NFRA_COMPAWS.json` status → `complete`. comp-aws persists as a standing comp-* tool (indexed in comp-tools.yaml). |

**Notes:** (a) The held security-posture findings (deletion_protection, imdsv2-optional, unmanaged-compute, the
PUBLIC/CROSS_ACCOUNT grants if any) do NOT block the cert — they're cataloged-held, surfaced for the separate Andrew
posture review. (b) NFRA_GLOBGRPH consumes the certified comp-aws derive — 13/13 firms its P1 input but is a
separate project (no coupling at close). (c) GLDINC/COSTAWS unaffected.

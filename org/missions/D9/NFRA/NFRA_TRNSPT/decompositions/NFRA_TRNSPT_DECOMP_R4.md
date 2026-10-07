# NFRA_TRNSPT decomposition -- ROUND 4 (2026-10-07, issuer 2.0.0_SA_COO~T2, dell2)

Cut on 1.0.0_SA_CTO~DELL2's round-3 analysis
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_3_20261007.md` @c2b5eb89a4 (msg 680: "round 4 =
C1, C2, C3, T1"; section 4 is the enrichment list for ONE issuance). Round 3 was the FAST round (2.0.0_SA_COO~D, STATUS.md), so it
has no decomposition file of its own; this file is numbered by round. PRD `org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md`
v0.1, ADMITTED (`prd-signoff.py status`), ENDPOINT unchanged. The project was placed on dell2 whole (analysis header; laptop
`1.0.0_SA_CTO` msgs 106273/106287).

**The rectangle is the analysis's section-4 list. FWD-7's positive arm is the thread-breaking item: C1 and C2 exist to make C3
possible and gradeable from dell2.**

| cell | item (analysis s.4) | outcome | status | placement | risk | worker_class | depends on (observed completion) |
|---|---|---|---|---|---|---|---|
| `TR-w-4` | C1: `mail_handler.py` accepts `WINDOW_DAYS` 1..120 and lists it as spans of at most 31 days; default 7 | FWD-7 | NOT-EVALUATED | dell2 worker | WORLD (path floor: the Lambda handler; nothing applied) | worker-light | -- |
| `TR-l-4` | C2: one `MAIL-PULL-FIRE` line per fire, counts only | FWD-7 | NOT-EVALUATED | dell2 worker | WORLD (path floor; nothing applied) | worker-light | TR-w-4 (same file, same slot) |
| `TR-r-4` | T1: `/hx/transcripts` release state and gate G-TEAMS-TX, measured from the repo record | FWD-1 | NOT-EVALUATED | dell2 worker | LOCAL | worker-light | -- |
| `TR-p-4` | C3: the driven positive arm -- one SCHEDULED fire with a window reaching 2026-08-11, then back to 7 | FWD-7 | NOT-EVALUATED | ISSUER (a served apply; no worker holds an apply) | SERVED | -- | TR-w-4, TR-l-4 drained, both sign-off halves |

Status vocabulary: NOT-EVALUATED / BUILT / SERVED / REALIZED.

**Chains.** A = TR-w-4 -> TR-l-4 (slot ~1; both write `mail_handler.py`, so one queue). B = TR-r-4 (slot ~2). TR-p-4 is the
issuer's act after chain A drains. Fan-out 2 of 2 worker chains, cap 8.

**Write sets (disjoint across slots).**
- TR-w-4: `infra/aws/lambda/transcripts-pull/mail_handler.py`, `data/transcripts/scripts/tests/test_mail_window_spans.py` (new),
  `data/transcripts/scripts/tests/test_mail_pull_handler.py` (its 1..31 bound test moves to 1..120), the docstring line in
  `infra/aws/terraform/transcripts/mail_pull.tf` is NOT touched (the env value stays "7").
- TR-l-4: `infra/aws/lambda/transcripts-pull/mail_handler.py`, `data/transcripts/scripts/tests/test_mail_fire_line.py` (new).
- TR-r-4: its deliverables folder only (`R4_TRANSCRIPTS_ROUTE_RECORD.md`).
- TR-p-4: `infra/aws/terraform/transcripts/mail_pull.tf` (`WINDOW_DAYS` only), the change-management entry, the issuer's
  deliverables. The channel file is append-only and shared.

**TR-p-4, the issuer's act (not a task order: the L6 gate refuses `<issued_to>` naming a Tier-1 seat, and the act is a served
apply).** After chain A merges and the drain suite is green:
1. Open the change-management entry; the CTO and COO never-widen halves name ONE key (the function's environment `WINDOW_DAYS`),
   rollback `WINDOW_DAYS=7`, and both branches (the fire lands the 2026-08-11 message; or it lands nothing, and then the criterion is
   listed as the cause to read). Bronze already holding it is not a branch: 0 `outlook` bronze objects since 10-02 (24 total, ~T2
   census 2026-10-07T14:3xZ).
2. Apply the code (C1, C2) and `WINDOW_DAYS` reaching 2026-08-11 (>= 58 days on the fire's date) through `safe-apply`; which machine
   applies is decided at the act, under the rule that a Dell writes no Lambda permission (this apply changes code and one
   environment value, no `aws_lambda_permission`).
3. Grade on the next 23:30Z SCHEDULED fire: (1) its `MAIL-PULL-FIRE` line in CloudWatch reads `landed>=1`, and the invocation is
   EventBridge's; (2) a laptop FILE via the fenced-read path (analysis s.3) shows bronze hashes equal the sidecar's and the silver
   row's `held_out`, counts only; (3) `WINDOW_DAYS` returned to 7 and the following fire's line reads `window_days=7`.

**Carried, not cut (analysis s.5):** the placement carrier (laptop's, via 0.0.0_AB_MSTR~DELL2); the 14 flagged words (Andrew);
row S11 (NFRA_OPLGTW); FWD-8's second reader (Andrew); Kimi K3 (no call before C-WIPE-GATE). The CVO's grade of the FAST round's
pins rides this round's compile.

## Rule 24 record

- **MECE over a declared domain.** Domain: analysis section 4, items C1, C2, C3, T1. By subtraction: C1 = TR-w-4; C2 = TR-l-4;
  C3 = TR-p-4 (issuer); T1 = TR-r-4. Remainder: none. Section 5 is carried by its own words.
- **Same grain.** One cell per item; the served act is the issuer's.
- **Intent coherence.** w widens the reach, l makes a fire gradeable without a store read, p drives the positive arm, r answers
  FWD-1's precondition.
- **State coherence.** No worker cell applies Terraform, grants a principal, calls the gateway, reads the transcripts store or calls a
  vendor model. Only TR-p-4 moves served state, and only `WINDOW_DAYS` and the function code.

## Battery (enrichment round)

- `comp-schedule`: DECLARED-NOT-APPLICABLE to the worker cells; TR-p-4 rides the existing 23:30Z rule unchanged.
- `comp-iam`: NOT RUN for the worker cells (no bucket write, no grant). Measured instead: `cloudops-dell2-agent-user` is refused
  `kms:Decrypt` on the transcripts key (2026-10-07T14:2xZ), and the laptop rules it stays refused (analysis s.3). TR-l-4 exists so
  TR-p-4 is graded from the log, not the store.
- Deployed layout (CTO rule 103374): TR-w-4 and TR-l-4 change a module the Lambda bundle ships, so TR-w-4 carries the bundle import
  check (`r2_bundle_import_check.py`, base: PASS, BUNDLE-IMPORT-OK files=48).
- Drain checks (not on any face): `r2_suite_check.py` (SUITE-GREEN) once after chain A merges; `commit-gate.sh` on the touched `.py`.

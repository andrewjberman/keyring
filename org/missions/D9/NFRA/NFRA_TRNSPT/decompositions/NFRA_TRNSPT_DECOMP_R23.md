# NFRA_TRNSPT decomposition -- ROUND 23 (2026-10-11, issuer 2.0.0_SA_COO~T2, dell2, box/dell2)

Cut on `1.0.0_SA_CTO~DELL2` msg 4299, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_23_20261011.md`
@b8a07a7e17, section 4, the ENRICHMENT LIST: "(1) The mail pull onto the root's one zip ... (2) `readers.auto.tfvars` from applied state,
and the header ... (3) The four Monday meetings, another route ... (4) `read_refused` in the handler's totals and log line;
`test_eod_voice.py` collects ... (5) Monday's fire, read." And: "Items 2, 3 and 4 are independent and start now. Item 1's packet comes
to this seat. Each build order carries at most three mechanical criteria."

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-mp-23` | (1) the mail pull re-applied, code only, onto the Teams pull's live package (FETCHED, not rebuilt), targeted at `aws_lambda_function.mail_pull`, under its own CTO + COO pair; one driven invoke of the mail pull graded against its last scheduled run. Disarms row D2-S22 (read 1: three functions, one digest) | FWD-7 | ISSUER packet + pair, applier `0.7.0_AE_CloudOps~TR2` (workstream `mailpull`) | WORLD | -- | the issuer's packet, then the CTO half |
| `TR-tv-23` | (2) a committed `infra/aws/terraform/transcripts/readers.auto.tfvars` holding exactly the second-reader role's live trust, READ from applied state; the variable keeps no default; `readers.tf`'s header states the applied state (D2-S17, D2-S20); proof a plan of the reader resources with 0 changes | FWD-8 | applier `0.7.0_AE_CloudOps~TR2` (workstream `readervars`; the path is the AE lane's) | LOCAL | -- | -- |
| `TR-om-23` | (3) the four Monday meetings (2026-04-10, 04-13, 05-04, 06-01) looked for by another route: the organizer's OneDrive and the meeting's SharePoint site, through the gateway's file tools; found or not per date, with the path and the tool that answered. No landing | FWD-3 | ISSUER (read-only; the gateway tools live in the issuer's session) | LOCAL | -- | -- |
| `TR-tt-23` | (4) `read_refused` in `pull.totals` and in the `PULL-DRY` line, with the two tests that pin the totals edited in the same cell; `test_eod_voice.py` collects | FWD-2 | dell2 worker (workstream `totals`) | LOCAL | worker-light | -- |
| `TR-mf-23` | (5) Monday's scheduled fire, read: `run.json` per-series counts with the REPORT line beside it; `Max Memory Used` on a run that lands a transcript is the first measured peak (above 768 MB is a row). Closes row D2-S16 | FWD-1, FWD-2 | ISSUER (read-only) | SERVED | -- | the 2026-10-12 13:00Z fire (event; a read that is owed, not a wait) |

**Chains.** A = TR-tt-23 (worker). B = TR-tv-23 -> TR-mp-23 (one applier lane, in that order: the tfvars removes the hand-supplied
variable before the next apply on this root). C = TR-om-23 (issuer). D = TR-mf-23 (issuer, event). Fan-out: 2 of 2 seat chains spawned
now (A to a worker, B to the applier), cap 8; C starts now in the issuer's own session.

**Issuer rulings.**
(1) TR-mp-23's order is cut STAGED in this issuance. Its GO carries the CTO half's conditions and follows the issuer's packet (the member
diff of the mail pull's deployed zip against the Teams pull's, the mail handler's import closure against the changed set, the key
producers equal, the rollback to the kept zip).
(2) TR-tv-23: `infra/aws/terraform/.gitignore:5` ignores `*.auto.tfvars`. The CTO ruled a COMMITTED file, so the cell adds one negation
line for this one path; it does not un-ignore the pattern.
(3) TR-om-23 opens no transcript body: file names, paths, sizes and dates only.
(4) TR-tt-23 adds a key to the totals dict and a field to the dry line; it changes no outcome and no counter's meaning.

## Rule 24 record

Domain: the analysis's section 4, five items.
- (1) = TR-mp-23. (2) = TR-tv-23. (3) = TR-om-23. (4) = TR-tt-23. (5) = TR-mf-23.

Remainder: none. Carried and not cut (section 5 of the analysis, Andrew's acts): the Research Meeting SharePoint folder's link; the
ADMITTED read as Opal_Terminal (FWD-8, parked); his Monday read through the FWD-5 role; a past meeting he names.

## Battery

`org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R23_CHECKS/r23_checks.py` at base:
- `tt23`: `R23-TT23-FAIL missing test_totals_carry_read_refused, test_dry_line_prints_read_refused`
- `tv23`: `R23-TV23-FAIL absent: infra/aws/terraform/transcripts/readers.auto.tfvars`
- `mp23`: `R23-MP23-FAIL 2 distinct digests across 3 functions` (teams AI4UQD0M, mail VGIq85Xx, commentary AI4UQD0M)

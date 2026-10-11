# TCKT_VNEXT decomposition -- ROUND 3, 2026-10-11, issuer 2.0.0_SA_COO~V2, dell2

**Authority:** the CTO's round-3 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_TCKT_VNEXT_ROUND_3_20261011.md`
@f1c513af8e (msg 4661), section 3, answering the round-2 slug `ledger/L10_SLUG_R2.md` @5047fa86e6; and the ruling
`CTO_RULING_TCKT_VNEXT_R2_TR1_RUN3_GENERATION_HOP_AND_FOURTH_RUN_20261011.md` with its CORRECTION. No PRD addendum. FWD-1 is NOT
REALIZED, so round 3 is still a thread round; its thread cell cannot be cut yet.

| cell | builds | list item | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `R3-tr-1` | the FOURTH run of the FWD-1 journey, under a NEW never-widen pair, with the runner at `8838ec4313` (blob `3199fd8a`). It also exercises the live arms of item 3 (the report route's id check, the package route's coded answers, the Open report page against a real report) | 1, 3 | FWD-1 | NOT-EVALUATED | ISSUER + applier seat | WORLD | -- | (i) the resident release st30 is live and its S2 after-read (one ticket-bound request reaching READY) passes; (ii) one dead letter has been read with no delete and its reason stated; (iii) the CTO's word on how long the identity row outlives the token (the worker re-reads the actor's row at job start, `resident_worker.py:696-717`). **Not cut in this issuance** |
| `R3-id-1` | run 3's accepted request under `49financial`: its `REQ-` id and job state, recorded in `deliverables/2.0.0_SA_COO~V2/R2_RUN/R2_TR1_RUN3_RESULT.md`; closes CTO condition 5 of the spent pair | 2 | FWD-1 (record) | NOT-EVALUATED | ISSUER (a record of `2.0.0_SA_COO~G2`'s batch read) | LOCAL | -- | that seat's batch window. **An issuer record, not an order** |
| `R3-sm-1` | the deploy record the round-2 applies never wrote: `infra/aws/lambda/ci/lambda-source-map.json`, entry `opal-ticket-api`, recorded by `record-terraform-deploy.sh` so that it names the live build (rows D2-S25, D2-S28) | 4 (precondition) | FWD-1 (instrument) | NOT-EVALUATED | applier seat | LOCAL by act (a git record; no AWS write), WORLD by path floor | -- | -- |
| `R3-pc-1` | the clamp precheck decides the ticket host from the source map's entry, the recorded commit's file and the deployed member's CONTENT (the clamp's helpers defined and called by the seven handlers), with no typed list of allowed builds. Code and tests only | 4 | FWD-1 (instrument) | NOT-EVALUATED | dell2 worker, slot ~13 | WORLD by path floor (it reads `infra/`); nothing applied | worker | -- (its LIVE read needs `R3-sm-1`; the build does not) |

**Item 5** (`round-close-check` and flat-folder orders) is filed to `0.0.0_AB_MSTR~DELL2` for the tool's owner (msg sent 10:05Z);
no cell. **Item 6** (carried from round 1) is cut after the thread runs, by your list's own words.

**Chains (M = 3):** {`R3-tr-1`}; {`R3-id-1`}; {`R3-sm-1` -> the live read of `R3-pc-1`}. `R3-pc-1`'s build shares no file with
`R3-sm-1`. **Fan-out now: 1 worker of 3 chains, cap 8**, plus one applier order.

**Write sets (disjoint):** `R3-pc-1` its own deliverables folder. `R3-sm-1` `infra/aws/lambda/ci/lambda-source-map.json` only.

## Rule 24 record

- **MECE over the analysis's section 3.** Domain: its six numbered items. By subtraction: item 1 -> `R3-tr-1`; item 2 ->
  `R3-id-1`; item 3 -> exercised by `R3-tr-1` (the analysis says "by the fourth run and not by separate acts"); item 4 ->
  `R3-sm-1` + `R3-pc-1`; item 5 -> a filing, done; item 6 -> not this issuance. Nothing of section 3 is uncovered.
- **Why item 4 is two cells.** The analysis says the precheck reads the source map's recorded hash. This seat read the map
  (2026-10-11 ~10:1xZ): the `opal-ticket-api` entry holds `artifact_sha256 ywAvsfx...` and `last_deployed_at 2026-10-07`, three
  deploys behind the live `t1EoiJRZ...`. The round-2 apply orders never ran the recorder and never granted its path; that
  omission was this issuer's. A precheck that reads the map is only as good as the record, so the record is its own cell.
- **State coherence: what no cell moves.** No Lambda, no route, no IAM, no identity, no ticket. `R3-sm-1` moves one JSON entry in
  git. The 8 dead letters are not touched by this project.

## Battery

comp-schedule, comp-iam: DECLARED-NOT-APPLICABLE for both cut cells (no schedule, no IAM). comp-adversary: the adversarial arms of
`R3-pc-1` are its refusal tests (a live build the map does not name; a member that is not the recorded commit's file; a clamp
helper removed; a handler that stops calling the clamp). `comp-blast` on `lambda-source-map.json` is owed by the applier before
its write (the file has other readers: `verify-local.sh`, the drift check).

Dry-run at the base (box/dell2, 2026-10-11 ~10:2xZ): pc-rules and pc-hosts FAIL absent, as expected.

## ADDENDUM 1 (2026-10-11 ~10:2xZ) -- round 3 gains the runner cell, by CTO rulings msg 4676 and msg 4696

The worker re-reads the accepted submitter's PROFILE row when a generation job starts (`resident_worker.py:696-717`), and the runner
deleted that row after the token's `exp`. The CTO ruled the row lives two hours after the submission, flat, with the token's expiry
unchanged and no job-state read after expiry. Also changed since the issuance (CTO msg 4683): `R3-tr-1`'s first condition is "the
resident release st30 is installed and its V1 is green"; the run is that release's S2 read and calls the YCharts producer once.

| cell | builds | list item | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `R3-rn-1` | the runner: after an ACCEPTED submission the row is left in place, the run exits with a distinct code, and a second invocation deletes the row no earlier than two hours after the submission and updates the same trace; the trace records the last job state read before expiry. A run with no accepted submission deletes after `exp` as before | rulings 4676, 4696 | FWD-1 | NOT-EVALUATED | dell2 worker, slot ~8 | WORLD by path floor (reads `infra/`); nothing applied | worker | -- |

**Edge added:** `R3-rn-1` -> `R3-tr-1`. Write set: the slot's own `fwd1_runner/` folder, shared with no other open order.

Dry-run at the base: rn-row FAIL (missing tests) and rn-regress FAIL (50 passed, below 56), as expected.

## ADDENDUM 2 (2026-10-11 ~12:5xZ) -- round 3 gains the report-id cell, by CTO ruling msg 4921

The read-only hop trace of IRPT_ANLREQ (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/trace/FWD1_HOP_TRACE.md`,
hop 16, row IRPT_ANLREQ-D2-W52-S5) found that nothing records `report_ref` on a ticket filed by the form's one-step sequence: the
ticket service writes it at create only for the commentary service, and on the report path only for the assignee of an in_progress
ticket. The page's Open controls need it. The CTO ruled one build cell here, after a code read; this seat read
`infra/aws/lambda/ticket_center/lambda_function.py` (sha256 prefix cf10e19e) at lines 112, 627-632 and 1339-1389 and confirms it,
as did `2.0.0_SA_COO~Y2` (msg 4928).

**The issuer's design, stated so the deploy pair can refuse it:** the report path also admits the ticket's CREATOR, on its own
analysis-request ticket that is not completed, carries an attachment and has no report recorded; once. The one-step form holds the
service-issued id at that moment. The alternative, the packager's post setting it, was not taken: it waits on hops 9 to 14 and its
`report_ref` string has no fixed shape in this service.

| cell | builds | list item | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `R3-rf-1` | the ticket service's report path admits the creator of a one-step analysis-request ticket, write-once, with a named refusal code; six tests | CTO msg 4921 item 2 | FWD-1 | cut | one order, workstream RF | WORLD (path floor; nothing is applied) | worker | none |

No edge. Write set: `infra/aws/lambda/ticket_center/lambda_function.py` and one new test file, shared with no other open order.
NOT in this cell: the deploy (its own packet and pair), and the portal form's call to this path after its analysis post (named to
the CTO as the hookup this cell needs; the form is another project's write surface).

Dry-run at the base: rf-filer FAIL (absent test file) and rf-regress FAIL (161 passed, below 167), as expected.

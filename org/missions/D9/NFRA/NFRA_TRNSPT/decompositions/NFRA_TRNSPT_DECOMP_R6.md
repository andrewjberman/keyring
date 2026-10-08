# NFRA_TRNSPT decomposition -- ROUND 6 (2026-10-08, issuer 2.0.0_SA_COO~T2, dell2)

Cut on 1.0.0_SA_CTO~DELL2's round-5 analysis
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_5_20261008.md` @a8931c9d12 (msg 1453; section 3 is the
enrichment list for ONE issuance). PRD `prd/NFRA_TRNSPT_PRD.md` v0.2, ENDPOINT unchanged.

| cell | item (analysis s.3) | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|
| `TR-e-6` | E1: D2-S2 -- was the 2026-08-11 message listed, and which admission test failed; the deciding data-asset row; data gap or rule gap | FWD-7 (residue D2-S2) | NOT-EVALUATED | ISSUER (a live gateway read; no worker holds a route) | LOCAL | -- | -- |
| `TR-f-6` | E2: FWD-4's completeness record -- for each of the 4 series and each occurrence over the last 120 days, "here" or exactly one cause | FWD-4 | NOT-EVALUATED | dell2 worker (builder + test) then ISSUER (live inputs + the record) | LOCAL | worker | -- |

Status vocabulary: NOT-EVALUATED / BUILT / SERVED / REALIZED.

**Chains.** A = TR-f-6 (slot ~1). TR-e-6 is the issuer's act. No edge. Fan-out 1 of 1 worker chain, cap 8.

**Write sets.** TR-f-6: `data/transcripts/scripts/teams/completeness.py` (new), `data/transcripts/scripts/tests/test_completeness.py`
(new), `data/transcripts/scripts/tests/fixtures/completeness/inputs.json` (new). The issuer: its deliverables, the record file at close.

**Issuer rulings inside this decomposition (rule 27 L6).**
1. **E1 cannot be read from the run record.** `run.json` of `20261007T233013Z` holds totals only (`pull.run`,
   `data/transcripts/scripts/outlook/pull.py:134-190`: a non-admitted candidate adds to `near_miss` / `not_landed_not_admitted` and
   nothing else); no message id and no per-test flag is kept for a message that was not admitted. Row NFRA_TRNSPT-D2-S2 already says so
   ("the run record cannot say whether that message was listed and classified a near miss"). Row NFRA_TRNSPT-D2-S3 records the
   spec/world gap. **The deciding read is a re-classification:** the issuer lists the 2026-08-10..2026-08-12 UTC span for the pull's own
   sender table through the gateway (`gateway_mail.HxMailClient`), fetches each listed message and its attachment list exactly as the
   pull does, runs `criterion.classify` with `criterion.load_tables()`, and records per message ONLY: received date, sender index,
   `sender_ok`, `client_recipient`, `ycharts_pdf`, `trade_update_excluded`, `ingest`. No subject, address, name or body. The deciding
   data-asset row is named by table and position (author table / client-domain table / detection rule), never by value.
2. **E2 splits into the builder (a worker) and the record (the issuer).** The occurrence source (the calendar) and Microsoft's
   transcript listing are reachable only through the interactive gateway tools in the issuer's session; the gateway's headless Teams
   route allowlists `/me` and chat paths only (`infra/aws/ec2/opal-gateway/app/teams_route.py:73-78`). The worker builds and tests the
   builder against a fixture; the issuer collects the live inputs as dates and ids only and runs it at close. Criteria (1) and (2) of
   the analysis grade at close on the live record; criterion (3) is the worker's test.
3. **"expired" needs evidence of prior existence.** No retention figure is guessed: an occurrence is `expired` only when an input
   names it as once listed (e.g. the L1 brief's 34-listed / 30-retrieved census) and it is no longer listed and not in bronze; with no
   such evidence it is `never_recorded`.
4. **The Research Team Meeting is not on Andrew's calendar** (he is not invited; OG-tx-2 reach run 403). Its occurrences come from the
   series' own transcript listing where one exists, else the series is recorded `refused` with that source.

**Carried, not cut:** the allowlist load (NFRA_OPLGTW, waited on); C3 ledger L5 (the 2026-10-08T23:30Z fire reads `window_days=7`).

## Rule 24 record

- **MECE over a declared domain.** Domain: analysis section 3, E1 and E2. E1 = TR-e-6 (issuer). E2 = TR-f-6 (worker builder +
  criterion 3; issuer record + criteria 1-2). Remainder: none.
- **Same grain.** One cell per item.
- **Intent coherence.** e decides D2-S2's cause; f makes FWD-4 answerable.
- **State coherence.** No cell writes to the transcripts store, applies Terraform or changes the gateway. The cause vocabulary is the
  PRD's FWD-4 ACCEPT line (here / never recorded / expired / refused) plus `not_allowlisted`, which the analysis adds.

## Battery

- `comp-schedule`, `comp-iam`: DECLARED-NOT-APPLICABLE for the worker (no AWS call). The issuer's E1 read uses secret
  `gateway/mail/bearer` (first read already reported, msg to MSTR 2026-10-08T18:09Z).
- Checks `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R6_CHECKS/r6_checks.py`, dry-run at base CLOUD 94d866956b: f6-build
  FAIL (absent), f6-test FAIL (absent).

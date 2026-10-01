# NFRA_TRNSPT round 1 -- drain-end packet (L7 close, for 3.0.0_SA_CVO's L8 compile)

Issuer `2.0.0_SA_COO~T`, 2026-09-30 ~19:2xZ. Issuance @81e350ba0a. Decomposition
`org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP.md` (12 cells, 4 chains). Channel
`org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md`. Every figure below was read at CLOUD
after the last drain (0225e80b2f and later), not taken from a worker's report.

## 1. Orders: 12 of 12 terminal, 12 of 12 proof instances VALID at CLOUD

| order | cell | risk | worker | proof-of-spec-check at CLOUD | drained in |
|---|---|---|---|---|---|
| TO-TR-t2 bronze lander | TR-t-2 | LOCAL | ~1 | rc 0 | 26bc60a8cf (chain A) |
| TO-TR-t1 pull job | TR-t-1 | LOCAL | ~1 | rc 0 | 26bc60a8cf |
| TO-TR-i1 schedule + principal, DESIRED | TR-i-1 | WORLD | ~1 | rc 0 | 26bc60a8cf |
| TO-TR-t3 silver parse | TR-t-3 | SERVED | ~2 | rc 0 | b9b933859f (chain B) |
| TO-TR-t4 reader route | TR-t-4 | SERVED | ~2 | rc 0 (AC3 judgment) | b9b933859f |
| TO-TR-t5 thread trace | TR-t-5 | SERVED | ~2 | rc 0 | b9b933859f |
| TO-TR-g1 registry rows | TR-g-1 | WORLD | ~3 | rc 0 | fed423d013 (chain C) |
| TO-TR-b1 mail criterion + bronze | TR-b-1 | SERVED | ~3 | rc 0 | fed423d013 |
| TO-TR-a1 data assets | TR-a-1 | LOCAL | ~4 | rc 0 | 8e22dc9ddb (chain D) |
| TO-TR-w1 silver wipe | TR-w-1 | SERVED | ~4 | rc 0 | 8e22dc9ddb |
| TO-TR-k1 gold contract | TR-k-1 | SERVED | ~4 | rc 0 | 8e22dc9ddb |
| TO-TR-q1 slicer | TR-q-1 | LOCAL | ~4 | rc 0 | 0225e80b2f |

## 2. What the CVO grades (L9)

- **One JUDGMENT criterion:** `TR1-t4-AC3` (FWD-5 ACCEPT: an analyst gets what was said about one company without opening a
  file). Recorded by the worker, no verdict: `read_meeting.py --series monday_meeting --date 2026-09-28 --grep Goldman` ->
  header `MEETING monday_meeting 2026-09-28 turns=290 speakers=7 transcripts=1`, then 2 matching turns of 290. Grade it on the
  real run (the silver parquet below), never on the markup.
- **SERVED cells** (t-3, t-4, t-5, b-1, w-1, k-1): graded on the real runs in section 3.
- **WORLD cells:** `TR-g-1` is WORLD only by the gate's path floor for `infra/` (records; nothing applied). `TR-i-1` is a Terraform
  PLAN only (`9 to add, 0 to change, 0 to destroy`); nothing was applied and no change-management entry was opened, because
  nothing landed. Its apply is a later release under CTO+COO halves, after site Z lands S04/S05.

## 3. The issuer's real runs at close

**FWD-1 (the transcripts thread) -- REAL, VALID.** `data/transcripts/scripts/teams/thread_trace.py --series monday_meeting
--transcript MM-20260928-0858 --date 2026-09-28 --negative-date 2026-09-27` at CLOUD 3aeef0edf8, run by this seat:
`THREAD-TRACE hops=3 no_person=true negative_arm=NOT-HELD`; the issuer validator reads `TRACE-VALID`. Artifact:
`org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R1_ISSUER_THREAD_TRACE_MM-20260928-0858.json`.

| hop | seconds | line |
|---|---|---|
| land-probe | 3 | bronze held and byte-true: 3 objects, `.vtt` 59,266 bytes, sha256 matches the sidecar |
| parse | 7 | `SILVER-WRITTEN unparsed=0 rows=290 speakers=7`, key `s3://opal-data-transcripts/teams/transcripts/silver/monday_meeting/date=2026-09-28/MM-20260928-0858.parquet` (SSE-KMS under the transcripts key) |
| read | 3 | `MEETING monday_meeting 2026-09-28 turns=290 speakers=7 transcripts=1` |
| negative arm | -- | 2026-09-27 -> `NOT-HELD cause=not_in_bronze`, exit 4 |

Stated limit: hops 1-2 (the scheduled pull through the gateway) are NOT exercised. The gateway has no transcript tools yet (S04)
and the stored sign-in's lifetime is unmeasured (S05); both are NFRA_OPLGTW's, relayed to site Z by 1.0.0_SA_CTO (103271). The
pull job is built against the spec's shapes with a fixture transport and a stub HTTP transport.

**FWD-7 (the communications thread, in test) -- REAL RUN BROKE AT ITS FIRST REAL INPUT.** Two real Manav messages, copied
byte-identical from harness-persisted `read_email` outputs, plus their `list_email_attachments` results, in a replay directory
OUTSIDE the repo (`C:/Users/AndrewBerman/Desktop/NFRA_TRNSPT_SAMPLE_LOCAL/r1`, client PII). `outlook/pull.py --replay ... --dry-run`
raises in `criterion.classify`: the real tool returns the Graph envelope `{"value": [...]}`, while the issuer's BRONZE CONTRACT said
a bare list (row S9, the issuer's error). Nothing was landed. Measured read-only with the envelope unwrapped: both messages are
`sender_ok=true client_recipient=true recipient_firm=49financial ycharts_pdf=false near_miss=true ingest=false` -- their only
non-inline attachments are `application/octet-stream` images, no PDF. So silver, gold and the slicer have no real row to run on
this round; each is proven on synthetic input only (the planted-token wipe gate passes 8 of 8 at CLOUD).

## 4. Hygiene at the drain (repo-wide checks moved off the faces)

- `ruff` clean over `data/transcripts/scripts` and the Lambda; `py_compile` clean; `terraform fmt -check` clean.
- The combined test suite is RED: `python -m pytest data/transcripts/scripts/tests` in one process -> 22 failed / 30 passed at
  275b43af6a. Every file but two passes alone. Causes, each a row for the round-2 repair cell: S6 (a CRLF-dependent fixture split),
  S7 (the teams and outlook packages shadow each other's bare `land_bronze` and `pull` modules), S8 (the chain A x B seam: the pull
  job's fakes lack `list_objects_v2` now that the silver parser sits beside it). S10 is the chain C x D seam (the criterion never
  reads the ruled authors table).

## 5. Rows (channel at CLOUD)

Seat rows S1-S3, S5-S10; the CVO's S4; worker rows W1-S1..S5, W2-S1, W3-S1..S2, W4-S1..S12. BLOCKING rows are all cleared: the
index drift (W1-S1, W2-S1, W3-S1, W4-S4) by 17ad3ea043; the naming gate's registry refusal (W4-S11, the CVO's S4) by
1.0.0_SA_CTO's validator fix b5dc2e63d1 and 4.0.0_SA_CRO's display names 224058ea3f; the name-list fetch (W4-S1) by the PyPI
`names` library under Andrew's word. S1 is closed by S5 on the CTO's ruling 103271.

## 6. What round 2 should carry (the issuer's reading; the CTO's analysis decides)

1. **Thread-breaking first:** the FWD-7 real input (S9) and the criterion's table read (S10); then a real bronze landing of the
   recorded sample.
2. **One batched repair cell:** S6, S7, S8.
3. The CTO's issuer rule of 103374 applies from the next issuance: a cell that changes a runner-deployed script's imports proves
   the import in the deployed layout. TR-i-1's Lambda bundle imports the teams modules top-level (S7), so it is in scope.
4. Enrichment per PRD section 3 (the Research Meeting refusal, the other archetypes, backfill, the completeness table, the second
   reader), gated on site Z's S04/S05/S12 for anything that pulls.
5. Measured this round for the analysis: the `irpt-requests` table (1,102 items scanned) carries no Generate composition fields;
   they sit behind `analysis.record` `composition_ref` (W4-S10), so the slicer's real replay needs that read.

Push state at writing: LOCAL (this seat never pushes).

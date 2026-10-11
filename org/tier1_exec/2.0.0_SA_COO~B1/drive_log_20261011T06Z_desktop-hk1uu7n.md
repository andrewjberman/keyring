# /canonical-drive log -- 2.0.0_SA_COO~B1 (dell1), ADVI_FIRMBKTS round 2 close then round 3 issued, 2026-10-11 05Z-06Z

**archetype:** COORDINATE

Loop: none armed (one `/canonical-drive ADVI_FIRMBKTS` tick, then `/dispatch ADVI_FIRMBKTS`; no live row in
`org/ref/LIVE_ARMS.md` names this lane).

| UTC | limb | project/round | TOs t/T | cells c/F | thread | act fired |
|---|---|---|---|---|---|---|
| 05:2xZ | L10 -> L5 | ADVI_FIRMBKTS 2 -> 3 | 7/7 | -- | n | the CTO's round-2 analysis (msg 3521) in hand with the CVO's slug (msg 3519, ADJUDICATION_v3 MAY-CLOSE): RULE the rows owed to this seat, cut round 3 |
| 05:3xZ-06:2xZ | L5 | ADVI_FIRMBKTS 3 | 0/11 | 0/11 | n | measured at the cut (L5_FACTS): compare instrument defect, 89 FAULT groups, F4 own-firm route, 11 served classes and their writers, the advTenant remedy unbuilt, one `BD_S3_BUCKET` value for every read and write of the gold scripts; decomposition v3 `576d421c27`; nine checks, each proved at base and on a reference, fixture or mutant |
| 06:2xZ | L6 | ADVI_FIRMBKTS 3 | 0/11 | 0/11 | n | ONE issuance `576e574de4`: 11 orders, dep_stage EXECUTING; the gate refused once (four staged orders' lens lines named "TO BE RUN", not a disposition), fixed, landed |
| 06:3xZ | L7 | ADVI_FIRMBKTS 3 | 0/11 | -- | n | seven workers spawned (~11, ~12, ~13 reader A, ~14 reader B, ~15, ~16, ~17); four window acts STAGED |

## Measured

- Compare instrument: a reference build reads DEST equal 52,910 of 52,910 and SOURCE changed 36,742, then 40,948 minutes
  later (the daily producers' window was open). Round 2's "changed 1" was a pre-window reading.
- F4: the issuer's dry-run command reads OWN 431 bytes (refused only where the identity grants nothing): the cell is
  feasible; its order re-runs it.
- Producers: one environment value (`BD_S3_BUCKET`, `lib/config.py:14`) carries every gold read and write, 42 importers.
  The repoint's form is therefore read from `FB-f-6`, and `FB-f-9` is staged.
- The advTenant Rule-24 record the config header cites does not exist at HEAD.

## Defects in this tick's row, stated

- The staged orders were first written with lens lines reading "TO BE RUN"; the gate wants a disposition. The same lines
  are now a measured `RUN` where a measurement exists (the deploy chain and the S3 actions simulate `allowed` for the
  caller) and a `DECLARED-NOT-APPLICABLE` with its reason where the check does not exist until the amendment.
- Faces for five of the seven spawned workers are read from the worktree's order file by line range (above the record
  face), not pasted into the prompt as the skill's Step 4 says: a deviation, taken to avoid transcription error; the two
  readers' faces are pasted because their directories carry no checkout.
- The readers are not committers: the issuer ingests their answers and writes their proof instances (a design departure
  from the worker definition, stated on both orders).

## Left open

- Waiting on: the seven workers' reports; the issuer's ingest and close of `FB-f-3` and `FB-f-4`; then `r3_agree.py`.
- Staged acts need, in order, their pairs, change-management entries and amendments: `FB-f-8` after `FB-f-7`; `FB-f-9`
  after the census; `FB-f-10` after `FB-f-1` and act 2; `FB-f-11` after acts 1-3.
- A lane for the AE seat that deploys (`0.7.0_AE_CloudOps~<lane>`) is not seated.
- `wk-firmbkts-4` and `-9`: still held by the submodule disagreement (round 2 log).
- Push state: LOCAL on `box/dell1`.

## Compiler Tools

| tool | result |
|---|---|
| `comp-pipescript io D_04 --pipeline bd-gold` | 22 writes and 29 reads for one script; showed the bucket is one constant |
| `comp-find` | three rail denials (R1, R6) answered by the comp-find forms; one 120 s timeout moved to background |
| `to-pipeline-gate.py` | REFUSED 9 violations (lens dispositions), then admitted; coverage not graded at ROUND_CLOSE |
| `proof-of-spec-check.py`, `round-close-check.py` | used at the round-2 close; see the 05Z log |
| `iam:SimulatePrincipalPolicy` | allowed on the caller's own ARN for 5 deploy actions and 6 S3 actions; refused for roles (L5_FACTS section 2) |
| gap | `bun install --frozen-lockfile` is needed before the response guard's suite runs; no tool says so |

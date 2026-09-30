# Never-widen sign-off packet -- the resident st4 -> st5: IB-yr-231's two journal lines (S218's precondition)

**For:** `1.0.0_SA_CTO` (CTO half, msg 103099 asks for this packet; the CRO's half is the CTO's call to route).
**Author and operator:** `2.0.0_SA_COO~P`, 2026-09-30 ~02:5xZ.
**Asked by:** `2.0.0_SA_COO~Y` 103043 / 103059 (arms file
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/S218_STEP2_DISCRIMINATING_READ_ARMS_20260929.md`).
**Ledger:** `irpt-resident-st5-yr231-20260930` (U1 open, D1 open; opened @083fe80667).

This packet is st4's (`NEVER_WIDEN_SIGNOFF_PACKET_RESIDENT_ST4_20260929.md`, blob 4f34a600, both halves; D1 closed
20260929T123158Z) with the deltas below. Every unnamed section reads as st4's, including the install script's own
limbs (10 member shas, the factory pre-check, stop only on an empty queue, automatic rollback to the prior root).
The CTO's void half `4d8cc11` (a Lambda rebuild) is not this act: no Lambda, IAM, queue or schema moves.

## 1. What ships

| change | commit | file |
|---|---|---|
| IB-yr-231: the resident prints one closed-token line per matched eviction verdict (`IRPT_RESIDENT_EVICTION verdict=<NAME> job=<id>`) and one per job ending ATTENTION (`IRPT_RESIDENT_ATTENTION code=<code> job=<id>`) | 7fc1a123f0 | resident_worker.py |

`git diff 0357fc7e08 7fc1a123f0` on the file: +16 / -1. Commits touching the file between st4's pin and HEAD: exactly
one (7fc1a123f0); the blob at 7fc1a123f0 equals the blob at HEAD (583c12db). The one deleted line is the `if` that
now reads `verdict = ...; if verdict is not None:` (same predicate). `eviction_verdict` returns None or a dict
(`ycharts/session/broker.py:327-335`), so the added `verdict.get("reason")` cannot fault on a non-dict.

## 2. The one move -- `fe64236bbb-st4` -> `fe64236bbb-st5`

- Built by `build_resident_package.py` (deliverables/IRPT_MVP_P) at `--pin fe64236bbb`, st4's 12 overrides unchanged
  except `resident_worker.py` re-pinned 0357fc7e08 -> 7fc1a123f0; core state serial 5.
- **SUMS vs st4: 225/225 keys, none added or removed. Exactly two differ:** `ycharts/generate/resident_worker.py`
  (5288ff5a -> 8d1f5431) and `reports/resident_bindings.json` (a4fcccf7 -> e1a159f7, provenance only). Tar member
  names equal st4's (266).
- Tar sha256 `7199892013a9e3e4a05447f229dd8923bb8ab15c25446faa5cabdc5ef79ac015`, 731,610 bytes, at
  `ec2/investor-reporting-ycharts/resident/irpt-resident-fe64-st5.tar.gz` (bucket
  `opal-313476888478-lambda-artifacts`), S3 version `vJOIoCTh5mGuWbbLmMd43INv3t3FnEQ5`, a NEW key (HeadObject was 404
  before the put); read back by version: sha equal. The st4 key is untouched.
- `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/resident_host_install_st5_20260930.sh` (sha256 prefix 94ac5388)
  is st4's script with 10 lines changed: NEW/OLD roots, KEY, WANT_TAR, WANT_WORKER, three comment lines, the worker error
  text, the ledger slug and the receipt date. All 10 member pins read against the built package: 10 of 10 equal.
  `bash -n` OK. It rolls back to `fe64236bbb-st4`.

## 3. Blast radius -- both branches

Writers of an Analysis job's outcome: **1**, `ResidentGenerationWorker` (unchanged from st4). The change adds no writer
and no outcome path; it adds two `print` calls.

- **A job with no eviction and no ATTENTION ending (unchanged):** no new line; every byte written to the job store, the
  queue and S3 is the same as st4's.
- **A status failure that matches an eviction verdict (moves, journal only):** one `IRPT_RESIDENT_EVICTION` line naming
  the verdict, then `refresh_session()` and `step()` exactly as before. The predicate is the same expression. A second
  eviction in one job prints a second line and still ends `SESSION_REFRESH_ALREADY_USED` (the control ~Y ran).
- **A job ending ATTENTION (moves, journal only):** one `IRPT_RESIDENT_ATTENTION` line, then `put_state(ATTENTION)`
  with the same body. The line is built by `named_line`, which admits only `[A-Z][A-Z0-9_:]{0,63}` names and the job id
  pattern, and prints `?` otherwise: no vendor text, no exception body.
- **Unchanged:** `claim_intent`, `request_budget`, SESSION_REFRESH_ALREADY_USED, certification, publication, every
  non-Analysis path. No Lambda, IAM, queue, schema or portal contract moves.
- **Reachable:** Analysis submissions; the first real reach is ~Y's one-job read on a cold resident (S218 step 2).
- **Not claimed:** that a live journal read shows the lines; that is the read the arms file names, not this act's proof.

## 4. Apply protocol

1. ~Y runs its gates on the BUILT st5 (S3 version vJOIoCTh) and records the result in the ledger before the SSM run
   (the CRO's st3 condition, carried). Not yet run.
2. The half(s) at HEAD naming this file's blob.
3. LIVE before-read: running root `fe64236bbb-st4`, queue 0/0 (script line 1 of the queue check, stop on non-empty).
4. SSM run of the install script; running root and member shas read back; polls; 0 Tracebacks.
5. The one-job read is ~Y's, on its own window.

**Rollback per key:** the resident root `fe64236bbb-st4` stays on the host; the cutover receipt is copied to
`cutover_receipt.fe64236bbb-st4.json` before the write; the script restores it automatically on a failed factory,
a non-empty queue, a non-zero install, an inactive unit, no polls, or a Traceback.

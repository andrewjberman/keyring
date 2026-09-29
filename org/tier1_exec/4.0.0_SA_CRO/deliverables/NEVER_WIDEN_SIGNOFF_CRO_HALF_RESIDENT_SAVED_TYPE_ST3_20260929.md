# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- the resident st2 -> st3: a saved portfolio type other than fixed refuses a tolerated setting before generation (TO-IB-yr-1)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_RESIDENT_SAVED_TYPE_ST3_20260929.md`
blob `17661cbe` (at `03cccc5a37`, at HEAD, and on disk; read 2026-09-29 ~01:5xZ).
- **Word diff:** a new packet for a new act (one resident move). Its apply protocol is st2's (this seat's half
  `NEVER_WIDEN_SIGNOFF_CRO_HALF_GENERATE_RESIDENT_GRANT_20260928.md`, D2) with the roots and shas changed.
- **Asked by:** 2.0.0_SA_COO~P, msg 102534. **Other half:** 1.0.0_SA_CTO. This seat is not in the act.

## VERDICT: SIGNED on blob 17661cbe, with one condition and one named item

The move narrows: a job that today generates a report on a tolerated setting for a non-fixed saved portfolio stops
before generation with a named reason. Nothing else changes; a job without the new field proceeds as today.

### The code, read at its lines

`git diff 12a67ed5ee ec8f69f718` on the two files: 7 insertions, 1 deletion, as the packet says.
- `recipe.py:699`: `step_read_back` returns `saved_portfolio_type = effective.get("model_portfolio_type")` only when
  `settings_source == "saved_portfolio"`, else `None`.
- `resident_worker.py:203-209`: the read-back checkpoint keeps that field; the rule fires only when a row is tolerated
  AND the saved type is present AND it is not `fixed`, raising `WorkerAttention("TOLERANCE_REQUIRES_STATIC")` before
  `step_validate`. The boundary already names that attention.
- **The two spellings agree.** The pre-existing PDF-time check (`resident_worker.py:262-276`, unchanged since
  `12a67ed5ee`) tests the vendor's PRINTED type against `"Static"` (`extract.PORTFOLIO_TYPES = ("Static", "Dynamic")`).
  The new check tests the saved portfolio's API type against `"fixed"`, which is the vendor's own route vocabulary for a
  static portfolio (`/model_portfolios/fixed/` in the replay fixtures, `test_resident_worker.py:293,306`). An absent
  type reads `None` and proceeds, so an unexpected spelling can only fall to branch B, never widen branch A.
- `git diff --stat ec8f69f718 HEAD` on the two files is empty: HEAD carries exactly these bytes.

### The artifact, read here on its own bytes

- **Bytes:** `s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-ycharts/resident/irpt-resident-fe64-st3.tar.gz`
  VersionId `vDS2rcSqdOEi...` (01:43:22Z) hashes to `26769a3790...` (730,085 bytes); st2's `2ZLL.I5jJuTC...` hashes to
  `f681024b7f...`. Both hold 226 file members.
- **Census st2 -> st3:** four members differ: `ycharts/generate/recipe.py` (`982d8171` -> `4fde9ac9`),
  `ycharts/generate/resident_worker.py` (`9b2dbd18` -> `95f79dad`), `reports/resident_bindings.json` (generated_at) and
  `SHA256SUMS`. The two `.py` members hash equal to the repo's files at `ec8f69f718`.
- **The install script** `resident_host_install_st3_20260929.sh` (sha `87c70e76`) diffed against st2's: only the
  ledger comment, NEW/OLD roots, KEY, the three WANT shas, the two error strings and the receipt's written_at/ledger
  change; the 10-member check, the factory pre-check, the empty-queue stop, the 30 s Traceback watch and the automatic
  rollback to st2 are byte-for-byte st2's.

### The rule, exercised on the bytes that move (this seat's own run)

~Y's harness `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R19_CHECKS/test_r19_y1_pregen_static.py` (the proof's
Y19-1-AC1/AC2, built on `test_resident_worker.py`'s own replay world) was run twice:

| bytes under test | not_fixed (`dynamic`, tolerated) | fixed | absent |
|---|---|---|---|
| st3 (repo HEAD, byte-equal to the tar's two members) | PASS: ATTENTION, no generate POST, no download | PASS: READY | PASS: READY |
| st2 (a copy of the tree with the st2 tar's two members overlaid; negative control) | **FAIL: READY** -- the vendor generated first | PASS: READY | PASS: READY |

So the test tells the two builds apart on exactly the arm that moves, and the two control arms hold on both.

### Blast radius, read from the producer's own rule

- **One writer** of the job outcome, `ResidentGenerationWorker`; its rule at `:200-215`.
- **Branch A (moves):** settings from a saved portfolio, at least one tolerated read-back row (today only
  `level_as_of_type`), saved type present and not `fixed`. Before: generation on the tolerated value. After: ATTENTION
  `TOLERANCE_REQUIRES_STATIC`, no report, no PDF, no publication.
- **Branch B (unchanged):** every other job, including one resumed from an st2 checkpoint (no field, reads `None`).
- **Population today:** the live queue holds no such job -- `irpt-jobs` (8 items) and `irpt-requests` (325 items) carry no
  read-back checkpoint with a tolerated row; window 15's own tolerated case ran on a Static portfolio and stays READY
  on the printed-type check.
- **Not moved:** irpt-ycharts-generate (`AdE17rT6`, it imports `recipe` only for `load_templates()`), every table, IAM,
  queue and schedule; the checkpoint gains one key.
- **Rollback per key:** the st2 root stays on the host; the receipt is copied aside before the write; the script rolls
  back on rc != 0, an inactive unit, no poll, or a Traceback within 30 s.

### Condition (D1): ~Y's four gates PASS on the built st3 is posted before step 4, and the install's own read-back is the proof

- The packet's step 1 (~Y's gates on S3 version `vDS2rcSq`) is a precondition of the install, not of this signature;
  this half asks that ~Y's PASS is in the ledger before the SSM run.
- BEFORE: the running root reads `fe64236bbb-st2` and the queue 0/0 (script line 1). AFTER: the running root reads
  `fe64236bbb-st3`, the 10 member shas read back (recipe `4fde9ac9`, worker `95f79dad`), the unit polls, 0 Tracebacks.
  Any other outcome is the script's own rollback to st2, same turn.
- The first live exercise of branch A is window 21's Y bodies (the packet's own note: a `TOLERANCE_REQUIRES_STATIC`
  stop there is a named terminal state, not a window failure).

### Named item (not a refusal ground)

The repo carries no unit test for the new rule: `test_resident_worker.py` at HEAD tests only the PDF-time check, and
`ec8f69f718` added none (the task order made it optional; the proof-of-spec's declared exclusion records why). The
R19 harness under `IRPT_MVP_Y/R19_CHECKS/` is the only test of the pre-generation gate. It is worth moving beside the
suite so the next change to `resident_worker.py` runs it by default.

## What this half signs against

- Packet blob `17661cbe`; commit `ec8f69f718` (build `0a1fc245cb`); ledger `irpt-resident-saved-type-st3-20260929`.
- Artifact `26769a3790` (S3 `vDS2rcSq`), its 226-member census against st2 `f681024b7f`, the install script `87c70e76`.
- The blast radius above: branch A only, branch B unchanged, no other surface moves, rollback to the retained st2 root.

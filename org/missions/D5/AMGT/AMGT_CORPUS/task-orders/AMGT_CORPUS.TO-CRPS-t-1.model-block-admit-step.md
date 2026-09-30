# AMGT_CORPUS task order -- `CRPS-t-1` -- ROUND 18: registered names with no model block get pulled -- a population mode on `model_block_pull.py`, run as a step of the scheduled induction; it refuses loudly when the terminal is not signed in

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-t-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the build adds a step to an existing (unregistered) trigger entry; no schedule is registered or changed here (the registration is the issuer's cell t-4 under a pair).
comp-iam: DECLARED-NOT-APPLICABLE -- S3 list reads only in the worker's runs; the pull's writes are the fire's, under t-4's pair.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 18. Serves **a newly registered name's served model block (round-17 analysis ruling 1)**.

## 1. THE CELL -- `CRPS-t-1`

**Where this came from.** The round-17 census (`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/MODEL_BLOCK_CENSUS_ROUND17.json`)
read `admits_new_registrations False`: `integrations/bloomberg/research/model_block_pull.py` needs `--securities` (at most 3, no
population default), and every caller names tickers by hand. Hitachi 6501 JP was pulled by hand. The CTO ruled
(`org/missions/D5/AMGT/AMGT_CORPUS/ledger/ROUND_ANALYSIS.round17.md` s.2 ruling 1): the producer exists, so only its POPULATION
is missing. The mode runs as a STEP of the scheduled induction, after registration (one schedule, not two).

**RULED -- what you build:**
1. **A new stage `admit` in `model_block_pull.py`:**
   `python integrations/bloomberg/research/model_block_pull.py admit [--dry-run]`, with no `--securities`. Keep `--securities`
   required for every other stage. The stage runs in this order:
   1. The population: every security the live research library resolves through the served crosswalk
      (`lib.research.corpus.backlog.build(lib.research.corpus.library.library_root())`, records with a `security_key`).
      "Without a block" means no `derived/model_block/<key>/` object in the producer's own bucket, using the SAME key form the
      producer writes.
   2. It prints ONE line FIRST: `admit population registered <N> without_block <K>`.
   3. With `--dry-run`: it prints `admit population registered <N> without_block <K> pulled 0 bloomberg_calls 0` as its closing
      line and makes no vendor call.
   4. Without `--dry-run`, if K > 0:
      - It first opens a DAPI session through the estate client (`integrations/bloomberg/mcp/blp_client.py`).
      - If that fails, it prints `REFUSED: Bloomberg DAPI not reachable -- sign in per integrations/bloomberg/READ_HERE.md
        section 2` and returns rc 4. It never exits 0, and never reads as an empty population.
      - Otherwise it runs the existing `stage_pull` then `stage_derive` for each name, in batches of at most 3 (the F2/G-24
        cap), and closes with `admit population registered <N> without_block <K> pulled <P> bloomberg_calls <C>`.
2. **`lib/research/corpus/induction_scheduled.py`:** the `fire` mode runs the admit step AFTER `induction_run` returns.
   `dry-run` runs `admit --dry-run`. Either mode prints `induction_scheduled step model_block_admit rc <n>`, and the closing
   line stays last.
3. **`integrations/bloomberg/research/tests/test_model_block_admit.py`** (new, offline): uses a stub S3 listing plus the
   crosswalk and library env overrides that the corpus tests use.
   - (a) One planted registered name without a block, with pull and derive stubbed: exactly that name is pulled, and
     population is printed before any pull.
   - (b) The session open forced to fail: rc != 0, the `REFUSED ... READ_HERE.md` line appears, and population is printed
     first.
   - Then `print()` ONE line exactly: `t1 refuses_loudly True rc_nonzero True names_surface True population_printed_first True
     planted_pulled 1`.
4. **`lib/research/corpus/tests/test_induction_schedule.py`:** add a test (keep the existing one green) that drives
   `induction_scheduled --mode dry-run` and asserts the step order. It prints ONE line exactly:
   `t1 scheduled_steps registration,model_block_admit`.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/test_model_block_admit.py
lib/research/corpus/induction_scheduled.py
lib/research/corpus/tests/test_induction_schedule.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-t-1.model-block-admit-step.md
</paths>

READ-ONLY: every other file in the repository, every S3 object, the research library, the Task Scheduler. Scratch `.scratch/t1/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible.
- NO vendor call. Never run `admit` or `pull` or `derive` without `--dry-run` against the real DAPI or S3. Never open a blpapi
  session outside a test's stub.
- NO S3 write. NO Scheduled Task.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-t-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round18/t1_AC1.sh</invocation><expect>(?m)^admit population registered 96 without_block 0 pulled 0 bloomberg_calls 0$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-t-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round18/t1_AC2.sh</invocation><expect>(?m)^t1 refuses_loudly True rc_nonzero True names_surface True population_printed_first True planted_pulled 1$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-t-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round18/t1_AC3.sh</invocation><expect>(?m)^t1 scheduled_steps registration,model_block_admit$</expect></criterion>
</proof_of_spec>

- AC1: the live population, dry-run (96 registered, 0 without a block since Hitachi's pull). AC2: the refusing transport and the
  planted name, offline. AC3: the step order on the scheduled path.

## 6. WHEN YOU ARE DONE
1. Write the instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-t-1.model-block-admit-step.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you
   changed plus the instance.
4. Report ONCE: each AC line, the key form the population check used, and the new stage's exact CLI.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-17 analysis s.4 cell 1 @`50a4593cba` (msg 26826). The checks were dry-run at base CLOUD `9dc713f359`:
- t1_AC1 FAIL (`usage: ... --securities` -- no `admit` stage);
- t1_AC2 FAIL (no tests ran);
- t1_AC3 FAIL (no `t1 scheduled` line).

The fire of this step goes under t-4's pair.
<risk>LOCAL</risk>
<status>pending</status>
<round>18</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<status>complete</status>

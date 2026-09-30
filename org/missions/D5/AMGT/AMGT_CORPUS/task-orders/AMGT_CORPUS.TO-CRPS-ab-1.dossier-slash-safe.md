# AMGT_CORPUS task order -- `CRPS-ab-1` -- ROUND 26: the dossier's model-block readers through `slash_safe_key` (row `Z-S71`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ab-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface (the dossier writes are a later issuer act under a pair).
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 26. Serves **every dossier built for a slash-bearing name**.

## 1. THE CELL -- `CRPS-ab-1`

**Where this came from (row `AMGT_CORPUS-Z-S71`, ARMED).** The model blocks of the slash-bearing names now live at ENCODED keys:
`derived/model_block/BP-SLASH-_LN_Equity/<stamp>/model_block.json`, per `lib.research.identity.crosswalk.slash_safe_key`. The raw-slash
copies `derived/model_block/BP/_LN_Equity/...` were KEPT and hold only the 2026-09-25 blocks.

`lib/research/corpus/dossier.py` still builds its model-block prefix from the raw identity at about `:927` and `:966`
(`base = "%s%s/" % (MODEL_BLOCK_POOL_PREFIX, security_key)`). So `dossier.current_inputs("BP/_LN_Equity")` names the kept 09-25 copy,
and `write_one` sees no change after a re-derive.

**RULED -- what you build:**
1. Every per-security model-block path in `dossier.py` goes through `crosswalk.slash_safe_key(security_key)`. That is the encoded form,
   and it is byte-identical for a slash-free key.
   - The identity inside the document keeps its slash.
   - Do not read both forms: the encoded key is the one the producer writes today (`model_block_pull.stage_derive`), and the raw copies
     are stale by construction.
2. **Tests:** `lib/research/corpus/tests/test_dossier_slash_safe_round26.py` (new):
   - a slashed key resolves the encoded prefix;
   - a slash-free key resolves a byte-identical prefix;
   - no network (stub the S3 listing).
3. Do NOT call `write_one` or any S3 write. Do NOT touch any other file.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_slash_safe_round26.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-ab-1.dossier-slash-safe.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ab-1.dossier-slash-safe.md
</paths>

READ-ONLY: every other file, every S3 object. Scratch `.scratch/ab1/`. Your worktree is a SPARSE checkout; never disable it.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible.
- NO vendor call, NO S3 write.
- Any long-running script runs from a NAMED file with `python -u`.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ab-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round26/ab1_AC1.sh</invocation><expect>(?m)^ab1 bp_reads encoded bp_newest True ng_reads encoded ng_newest True control_unchanged True$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ab-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round26/ab1_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: the checker calls `dossier.current_inputs` itself.
  - BP and NG must name model blocks at the ENCODED key, including the newest encoded stamp.
  - `TSM_US_Equity`'s inputs must be byte-identical to the base the issuer recorded at the cut.
- AC2: your tests.

## 6. WHEN YOU ARE DONE
1. Write the instance at the proof path in section 3.
2. Run `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` AFTER your final commit, and pin each
   artifact row to the commit whose BYTES you graded (verify with `git show <pin>:<path>`). It must return rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file, and commit.
4. Report ONCE: each AC line, and the lines you changed (file:line).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-25 analysis ruling 1 and enrichment item 1 @`19207dfb83` (msg 27357). Dry-run at base CLOUD `ae1c849af1`: ab1_AC1
FAIL as designed (`ab1 bp_reads raw bp_newest False ng_reads raw ng_newest False control_unchanged True`); ab1_AC2 FAIL (no tests).
<risk>LOCAL</risk>
<status>pending</status>
<round>26</round>
<slot>~1</slot>
<fabric>site-z</fabric>

<status>complete</status>

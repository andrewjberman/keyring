# AMGT_CORPUS task order -- `CRPS-s-1` -- ROUND 17: which registered names carry a model block, and does its producer admit a name registered after its population was fixed (Hitachi) -- a read-only census

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-s-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only census; no schedule or deploy surface is touched (a producer's trigger is READ, never changed).
comp-iam: DECLARED-NOT-APPLICABLE -- S3 list/get reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 17. Serves **the served read of a newly registered name (row `Z-W173-S5`, Hitachi 6501 JP)**.

## 1. THE CELL -- `CRPS-s-1`

**Where this came from.** AMGT_RESAPP's round-49 analysis (`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round49.md`,
ruling 4) found Hitachi 6501 JP (registered 2026-09-29 as `6501_JP_Equity`, crosswalk `crosswalk/v1/2026-09-29.json`) identified
but WITHOUT a model block, so the deployed export refuses it. This project's round-16 analysis
(`org/missions/D5/AMGT/AMGT_CORPUS/ledger/ROUND_ANALYSIS.round16.md` s.4 cell 1) routes the admission here, census first.

The model-block writer is `integrations/bloomberg/research/model_block_pull.py`:
- Stage `pull` lands raw objects at `bloomberg/harvest/bronze/{refdata,histdata,bestdata}/security_key=<safe>/<stamp>.json`.
- Stage `derive` lands `derived/model_block/<security_key>/<stamp>/model_block.json`.
- `--securities` is REQUIRED (at most 3 per call, with no population default). So which names get a block is decided by
  whoever CALLS it.

**RULED -- what you build:** `MODEL_BLOCK_CENSUS_ROUND17.json` + `.md` in your deliverables, read-only.
1. **The population:** every folder in the live research library, resolved through the served crosswalk. Use
   `lib.research.corpus.backlog.build(lib.research.corpus.library.library_root())`, whose records carry `folder` and
   `security_key`. `"denominator"` is its `folders_read` (96 at the cut).
2. **One row per folder:** `{"security_key", "folder", "model_block": "present"|"absent", "latest_stamp": <stamp or null>,
   "evidence": <the S3 listing prefix read, or the reason>}`.
   - Present means at least one `derived/model_block/<security_key>/<stamp>/model_block.json` exists, read by S3 list in the
     bucket the producer writes. Find the bucket from the producer's own constants and name it in the file.
   - Use the key form the producer writes: check its handling of `/` keys such as `BP/_LN_Equity` against
     `lib/research/identity/crosswalk.py` `slash_safe_key`.
   - `latest_stamp` is null exactly when the block is absent.
3. **`"producer"`:** `{"writer": "integrations/bloomberg/research/model_block_pull.py", "invoked_by": [<every caller or trigger
   found, with path:line>], "population_source": <what decides the --securities list, with path:line>,
   "admits_new_registrations": true|false, "evidence": [<path:line reads and census commands>]}`.
   - `admits_new_registrations` is true only if some caller derives its list from the CURRENT crosswalk or registrations, so
     that a name registered today would be pulled with no manual act.
   - Search with `comp-find` / `git grep` for `model_block_pull`, and list the Scheduled Tasks the repo's registration scripts
     name.
4. **The `.md`:** the counts, the absent names, the producer chain, and the ONE exercising act that would give Hitachi a block
   (who runs what). An act is driven on demand, never a wait. Do NOT run it: a pull is a vendor call and a served write, which
   is the issuer's act under a pair.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/MODEL_BLOCK_CENSUS_ROUND17.json
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/MODEL_BLOCK_CENSUS_ROUND17.md
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-s-1.model-block-census.md
</paths>

READ-ONLY: every other file in the repository, every S3 object, the research library, the Task Scheduler. Scratch `.scratch/s1/`.

## 4. BOUNDS
- Pure ASCII, LF.
- NO vendor call: never run `model_block_pull.py pull`, `derive`, or anything under `integrations/bloomberg/` that opens a
  blpapi session.
- NO S3 write and NO code change.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k),
  with `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-s-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round17/s1_AC1.sh</invocation><expect>(?m)^s1 census names 96 present \d+ absent \d+ rows_valid 96 hitachi absent$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-s-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round17/s1_AC2.sh</invocation><expect>(?m)^s1 producer writer integrations/bloomberg/research/model_block_pull\.py invoked_by_n \d+ population_source_named True admits_new_registrations (True|False) evidence_n [1-9]\d*$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-s-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round17/s1_AC3.sh</invocation><expect>(?m)^paths_outside_grant 0$</expect></criterion>
</proof_of_spec>

- AC1: the census rows over the live library, 96 of 96 valid, with Hitachi absent as measured by RESAPP. AC2: the producer
  chain named with evidence. AC3: the bound.

## 6. WHEN YOU ARE DONE
1. Write the instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-s-1.model-block-census.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you
   changed plus the instance.
4. Report ONCE: each AC line, the absent names, the producer chain, and the exercising act for Hitachi.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-16 analysis s.4 cell 1 @`61ed59c609` (msg 26772). The checks were dry-run at base CLOUD `c467c34342`:
- s1_AC1 FAIL (`s1 census MISSING`);
- s1_AC2 FAIL (`s1 census MISSING`);
- s1_AC3 PASS (`paths_outside_grant 0`).

If AC2 reads `admits_new_registrations False`, the fix (a caller that admits new registrations, through the same scripted pull
under R-21) is the next cell. Hitachi's own pull is a served write under its own pair.
<risk>LOCAL</risk>
<status>pending</status>
<round>17</round>
<slot>~1</slot>
<fabric>site-z</fabric>

# AMGT_CORPUS task order -- `CRPS-t-3` -- ROUND 18: which key form each model-block READER uses, and does any read `BP/` or `NG/` as ABSENT (row `Z-S64`) -- a read-only census

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-t-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only census.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 list/get reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`**, slot `~3` of round 18. Serves **the served read of the two slash-keyed names (`BP/ LN`, `NG/ LN`)**.

## 1. THE CELL -- `CRPS-t-3`

**Where this came from.** Row `AMGT_CORPUS-Z-S64`: the model-block WRITER (`integrations/bloomberg/research/model_block_pull.py`)
puts slash tickers under a LITERAL `/` key -- `s3://opal-data-harvest/derived/model_block/BP/_LN_Equity/...` (6 objects), 0
under the slash-safe form `BP-SLASH-_LN_Equity` -- and never calls `lib/research/identity/crosswalk.py`'s `slash_safe_key`. The
CTO ruled (`org/missions/D5/AMGT/AMGT_CORPUS/ledger/ROUND_ANALYSIS.round17.md` s.2 ruling 3): no re-key (an existing pipeline
reaches key conformance through its own migration); the only question now is whether any READER uses a different key form than
the writer and so reads BP / NG as ABSENT -- a served defect -- or none does.

**RULED -- what you build:** `MODEL_BLOCK_READERS_ROUND18.json` + `.md` in your deliverables, read-only.
1. Every reader of `derived/model_block/` in the repository (search `comp-find` / `git grep` for `model_block` over `lib/`,
   `integrations/` and `infra/`, including Lambda sources under `infra/`; the `portal/` submodule is out of scope), with the denominator of files
   searched and hits.
2. One row per reader: `{"reader": "<path>:<line>", "key_form": "raw_slash"|"slash_safe"|"other:<desc>", "reads_bp": "OK"|"ABSENT"|"NOT_APPLICABLE", "evidence": "<the exact code that builds the key, and your read-only exercise>"}`. `reads_bp` is measured: call the reader's own key builder (or the function that reads) for `BP/_LN_Equity` and `NG/_LN_Equity` against the live bucket, read-only; `NOT_APPLICABLE` only for a reader that never takes a slash key (say why).
3. `"denominator"` = the number of reader rows. The `.md`: the table, and for any `ABSENT` the served surface that shows it (an API route or page).

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/MODEL_BLOCK_READERS_ROUND18.json
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/MODEL_BLOCK_READERS_ROUND18.md
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-t-3.model-block-reader-census.md
</paths>

READ-ONLY: every other file, every S3 object. Scratch `.scratch/t3/`.

## 4. BOUNDS
- Pure ASCII, LF. NO vendor call, NO S3 write, NO code change, NO Lambda invocation that writes. A deployed-function read is `/thesis`-style read-only only if a reader is only reachable that way.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W3-S<k>` (next free k), `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-t-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round18/t3_AC1.sh</invocation><expect>(?m)^t3 readers [1-9]\d* rows_valid [1-9]\d* all_valid True key_forms \S+ bp_absent \d+$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-t-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round18/t3_AC2.sh</invocation><expect>(?m)^paths_outside_grant 0$</expect></criterion>
</proof_of_spec>

- AC1 the reader census, every row valid with its measured BP read; AC2 the bound.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-t-3.model-block-reader-census.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` rc 0.
3. Append a new status tag reading complete at the END of this order file only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: each AC line, the readers table, and any ABSENT with its served surface.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-17 analysis s.4 cell 3 @`50a4593cba`. Checks dry-run at base CLOUD `9dc713f359`: t3_AC1 FAIL (`t3 census MISSING`); t3_AC2 PASS (`paths_outside_grant 0`).
<risk>LOCAL</risk>
<status>pending</status>
<round>18</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<status>complete</status>

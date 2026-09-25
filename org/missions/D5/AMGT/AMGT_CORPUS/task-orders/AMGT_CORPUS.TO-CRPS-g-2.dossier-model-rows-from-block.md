# AMGT_CORPUS task order -- `CRPS-g-2` -- ROUND 5: the dossier's Model rows read the served Model block, name it among their inputs, and derive every absent reason from the data -- the constant "not authorized" reason is removed

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-g-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates (G-3 CTO, G-7 POD4), 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell writes nothing to S3 (the probe is read-only); the dossier write is the issuer's drain act.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 5. Serves **FWD-12**'s dossier half (row `Z-S36`).

## 1. THE CELL -- `CRPS-g-2`

**Where this came from.** `lib/research/corpus/dossier.py`'s `_model_rows` builds one row per mnemonic from the typecast's
shared core and the sector template's KPI set, and writes `figure: {"value": null, "absent": FIGURE_ABSENT_REASON}` on EVERY
row, where `FIGURE_ABSENT_REASON = "Bloomberg figure pull not authorized (R-16 V3)"` (`:117`). It reads no Model block. The
round-4 production run wrote 94 dossiers carrying 9,471 rows and 0 values, while 89 derived Model blocks with figures are now
served (`derived/model_block/<safe key>/<stamp>/model_block.json`, newest stamp wins, read by
`lib/research/api/scoped_amgt.py` `read_model_block`). A constant reason cannot know when its cause has gone, and this one is
now false.

**RULED -- what you build:**
- `_model_rows` reads the NEWEST derived Model block for the dossier's security key by the same selection rule the served reader
  uses (read that rule from `scoped_amgt`; do not invent a different one). For each row's mnemonic, the figure is the block's
  figure for that mnemonic at its latest closed fiscal year (or its header / FY1 forecast figure when the mnemonic lives there),
  carrying `value`, `unit`, `fiscal_year` (or `fiscal_period`), `source`, and the block's stamp.
- A row with no figure carries an absent reason DERIVED at the point of absence: the block's own `unresolved` record for that
  mnemonic when one exists; otherwise `"no derived Model block for <key>"` or `"mnemonic <m> not carried by the Model block"`.
  `FIGURE_ABSENT_REASON` is deleted; no row's reason is a module constant.
- The dossier's `inputs` list names the block object it read (key + sha256), so its content hash moves when the block does.
- `python -m lib.research.corpus.dossier --model-rows-probe --key <security_key>`: read-only, builds that key's `model_rows` in
  memory, writes nothing, prints `model_rows <n> with_value <v> absent <a> constant_reasons <c> inputs_model_block <s3 uri|none>`.
- `tests/test_dossier_model_rows.py` (fake client): rows fill from a fixture block; a missing block and a missing mnemonic each
  yield their derived reason; the block is named in `inputs`; the constant is gone.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_model_rows.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-g-2.dossier-model-rows-from-block.md
</paths>

READ-ONLY: every other `lib/research/` module, `integrations/bloomberg/`. Scratch `.scratch/g2/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO S3 write (never run `dossier --write` for real), NO change to any dossier field
  other than `model_rows` and `inputs`.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W2-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-g-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round5/g2_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-g-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round5/g2_AC2.sh</invocation><expect>model_rows \d+ with_value [1-9]\d* absent \d+ constant_reasons 0 inputs_model_block s3://opal-data-harvest/derived/model_block/</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-g-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round5/g2_AC3.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe on a live key: its Model rows carry values from the served block, no constant
  reason, and the block named; AC3 the bound: the corpus suite still passes.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-g-2.dossier-model-rows-from-block.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-4 analysis s.8 item 2 and R-3 @`2f9b10b7d3`; row `Z-S36`. The drain writes dossiers AFTER g-1's
re-derive so rows read guarded blocks. Checks dry-run at the base: AC1 FAIL (no such file), AC2 FAIL (no probe), AC3 bound.

<risk>SERVED</risk>
<status>pending</status>
<round>5</round>
<slot>~2</slot>
<fabric>site-z</fabric>

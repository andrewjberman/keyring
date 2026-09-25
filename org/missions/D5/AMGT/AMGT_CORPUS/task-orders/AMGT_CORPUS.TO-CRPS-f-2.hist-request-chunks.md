# AMGT_CORPUS task order -- `CRPS-f-2` -- ROUND 4: the Model-block history request is split into requests of at most 25 fields and merged by date, and the Bloomberg client can raise a request-level error instead of returning an empty result; NO vendor call in this cell

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-f-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates (G-3 CTO, G-7 POD4), 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell writes nothing to S3 and calls no vendor; the pull is the issuer's drain act.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 4. Serves **FWD-12** (the Model rows carry the 22 added mnemonics).
**First read `integrations/bloomberg/READ_HERE.md`.** NEVER call Bloomberg, NEVER open a blpapi session, NEVER run the puller
without `--dry-run`. Your tests use a FAKE session; the module must import without blpapi.

## 1. THE CELL -- `CRPS-f-2`

**Where this came from.** `integrations/bloomberg/research/model_block_pull.py` sends ONE `HistoricalDataRequest` carrying all of
`HIST_FIELDS` (39 names since round 3 added 16). A live pull on 2026-09-25 returned `{}` history for every security while the
reference and forecast requests returned content. In `integrations/bloomberg/mcp/blp_client.py`, `historical_data`'s `handle()`
returns early for any message without `securityData`, so a request-level `responseError` is never read and the call returns
`{}` with no error. MEASURED: the dropped error (the code). INFERRED, not measured: that 39 fields exceeds the service's
per-request field limit (commonly 25). This cell fixes the measured defect and guards the inferred one; the issuer's first live
batch after the drain is the measurement.

**RULED -- what you build:**
- `model_block_pull.py`: a module constant `HIST_FIELDS_PER_REQUEST = 25`. The history stage sends `ceil(len(HIST_FIELDS)/25)`
  historical requests (field order preserved: the first 25, then the rest) for the SAME securities, window and periodicity, and
  merges the returned rows by (security, date) into ONE result of today's shape `{security: [{"date": ..., field: value, ...}]}`
  (a date seen in any chunk appears once, carrying every field any chunk returned for it). The raw `histdata` landing stays ONE
  object per stamp in that shape. The pull log records the per-chunk field lists.
- `--dry-run` prints, for each security, one line per historical chunk:
  `DRY-RUN PULL: <security> -> would send HistoricalDataRequest chunk <i> of <n> fields=<k>` (then its existing lines).
- `blp_client.historical_data` gains `on_response_error="ignore"`. `"ignore"` is TODAY'S behaviour, byte for byte (every
  existing caller is unchanged). `"raise"`: a message carrying `responseError` raises `BlpResponseError(<category>: <message>)`
  (a new exception class in `blp_client.py`). The puller's history stage passes `"raise"`, so a rejected request stops that
  security's pull loudly instead of landing `{}`.
- `tests/test_hist_request_chunks.py` (fake session, no network): 39 fields -> 2 requests of 25 and 14, order preserved; rows
  merged by date across chunks; a `responseError` message raises under `"raise"` and returns `{}` under `"ignore"` (the default);
  the module imports without blpapi.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/mcp/blp_client.py
integrations/bloomberg/research/tests/test_hist_request_chunks.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-f-2.hist-request-chunks.md
</paths>

READ-ONLY: everything else under `integrations/bloomberg/`, `lib/research/`. Scratch `.scratch/f2/`. Your deliverables dir:
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/`. The puller runs as a script with the repo on `PYTHONPATH`.

## 4. BOUNDS
- Pure ASCII source, LF, Python 3.9-compatible. NO vendor call, NO S3 write, NO change to any field list, basis text, cap
  (`--securities` at most 3), landing address or derive rule. `blp_client`'s default behaviour must not change for any caller.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W2-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-f-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round4/f2_AC1.sh</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-f-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round4/f2_AC2.sh</invocation><expect>(?s)HistoricalDataRequest chunk 1 of 2 fields=25.*HistoricalDataRequest chunk 2 of 2 fields=14.*DRY RUN PULL DONE: 1 of 1 securities planned, 0 written</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-f-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round4/f2_AC3.sh</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-f-2" judgment="true"/>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe: the puller's own dry run states two historical requests of 25 and 14; AC3 the
  bound: the whole Bloomberg research test suite still passes.
- **AC4 (JUDGMENT, the CVO's, graded at L9 on the issuer's REAL run after the drain -- never by you, and nothing for you to
  produce):** for three named keys (one that served a block before round 3, two that did not), the derived Model block's 16 added
  history fields beside the team's own model workbook for that name: do the figures agree in sign, scale and fiscal year, and is
  every absent field absent WITH a reason?

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-f-2.hist-request-chunks.proof_of_spec.json`
   (the shape of your e-1 instance in that dir; AC4 carried as a judgment row with no grade).
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if AC1-AC3 pass; commit the files you changed plus the instance.
4. Report ONCE: AC2's chunk lines.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-3 analysis s.7 item 2 and s.3 (the ONE judgment criterion) @`eaed38bac0`; row `Z-S29`. The drain's pull
runs a probe batch of 3 first and READS the raw histdata for rows before the other 29 batches (decomposition s.5 item 2); a probe
that still returns nothing, or raises `BlpResponseError`, stops the pull and becomes a row. The derive runs under pair COO
`2a3319e5ae` / CTO `35e4cb93ef` (re-affirmed msg 25799). The file `blp_client.py` is the estate's shared client, granted by
`<paths>` for this order only, default behaviour frozen. Checks dry-run at the base: AC1 FAIL (no such test file), AC2 FAIL (one
request of 39), AC3 bound -- recorded in the issuance commit.

<risk>WORLD</risk>
<status>pending</status>
<round>4</round>
<slot>~2</slot>
<fabric>site-z</fabric>

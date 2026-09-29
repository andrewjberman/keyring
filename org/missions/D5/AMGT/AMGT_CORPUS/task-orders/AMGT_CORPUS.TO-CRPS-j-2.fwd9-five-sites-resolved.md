# AMGT_CORPUS task order -- `CRPS-j-2` -- ROUND 8: FWD-9's code census reads zero unresolved write sites, because the code's own write roots become statically resolvable

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-j-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface.
comp-iam: DECLARED-NOT-APPLICABLE -- no cloud act.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 8. Serves **FWD-9**: *"a census of the project's own code prints
zero write, move, delete or open-for-write calls against any path under the library root, with the denominator of files
scanned"* -- today the census cannot place five sites and exits rc 1.

## 1. THE CELL -- `CRPS-j-2`

**Where this came from.** `python -m lib.research.corpus.readonly_proof --code-census` walks every `.py` under
`lib/research/corpus/` and classifies each write-like call's target by `_origin` into `library` / `outside-library` (SAFE) /
`unknown` / `tmp-fixture`. A target whose origin is `unknown` is an `unresolved` site and makes the census exit 1. At HEAD it
prints `tristate library 0 unresolved 5 clear 45` and these five:

```
unresolved_site induction_run.py:462 os.makedirs origins ['unknown']
unresolved_site induction_run.py:464 open origins ['unknown']
unresolved_site induction_run.py:688 os.makedirs origins ['unknown']
unresolved_site induction_run.py:690 open origins ['unknown']
unresolved_site key_glob_census.py:199 plant_path.write_text origins ['unknown']
```

The mechanisms, read from `_origin` in `lib/research/corpus/readonly_proof.py`:
- **`key_glob_census.py:199`** (`run_plant`, the planted positive control behind `--plant`): the plant writes into
  `tempfile.TemporaryDirectory(prefix=...)` bound by `with ... as tmp`. `_origin` classifies `tempfile.mkdtemp(...)` and
  `tempfile.gettempdir()` calls as SAFE; a `TemporaryDirectory` context binding is not classified, so `tmp` reads `unknown`.
- **`induction_run.py` :462/:464 (in `run`) and :688/:690 (in `write_readback`)**: the target is
  `deliverables_dir = deliverables_dir or DELIVERABLES_DIR` -- a caller-supplied parameter joined in a `BoolOp`; a parameter
  is statically unknown, whatever the module constant `DELIVERABLES_DIR` resolves to.

**RULED -- what you build (resolve in the CODE; the census is not changed):**
- `readonly_proof.py` is NOT edited -- no new origin class, no new exemption (the CTO's round-7 analysis: "needs no census
  schema change").
- **The plant:** its temp root comes from a form the census already classifies SAFE (`tempfile.mkdtemp(...)`), and it is
  removed afterwards (any removal call must also resolve SAFE). `python -m lib.research.corpus.key_glob_census --plant`
  still prints `plant_flagged 1`.
- **`induction_run.py`:** the write roots become statically resolvable. The written files stay where they are written today
  by default (`DELIVERABLES_DIR`). Tests that pass a temp `deliverables_dir` today instead redirect the module constant
  (e.g. `monkeypatch.setattr(induction_run, "DELIVERABLES_DIR", str(tmp_path))`) or an equivalent the census resolves.
  Update each caller you change (read them first: `run(...)` and `write_readback(...)` call sites across
  `lib/research/corpus/`, including tests). Behaviour at the CLI is unchanged.
- Measure after: the five sites read `clear`, no new site appears, `library 0`, rc 0.

## 3. SURFACES

<paths>
lib/research/corpus/key_glob_census.py
lib/research/corpus/induction_run.py
lib/research/corpus/tests/test_key_glob_census.py
lib/research/corpus/tests/test_induction_run.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-j-2.fwd9-five-sites-resolved.md
</paths>

READ-ONLY: every other file, including `lib/research/corpus/readonly_proof.py`. Scratch `.scratch/j2/`. If a caller you must
change lives outside `<paths>`, STOP and file a row naming it.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. No S3 access, no vendor call, no `--fire` or `--write` of any module; never run
  `readonly_proof --negative-control` (it copies the whole library to system temp).
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W2-S<k>`,
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-j-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round8/j2_AC1.sh</invocation><expect>j2 tristate_unresolved 0 library 0 rc 0</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-j-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round8/j2_AC2.sh</invocation><expect>(?m)^plant_flagged 1$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-j-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round8/j2_AC3.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
</proof_of_spec>

- AC1 the built behaviour (the census itself, on the real package); AC2 the control: the plant still flags (a moved plant that
  stops flagging would fake AC1); AC3 the bound: the four touched test modules pass.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-j-2.fwd9-five-sites-resolved.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC1's line and the census's `files_scanned` / `write_like_calls` before and after.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-7 analysis s.3 + s.5 item 2 @`03327ebbf9`. Checks dry-run at the base @`e3fd90cb63`: AC1 FAIL
(`j2 tristate_unresolved 5 library 0 rc 1`), AC2 PASS (`plant_flagged 1`), AC3 PASS (152 passed).

<risk>LOCAL</risk>
<status>complete</status>
<round>8</round>
<slot>~2</slot>
<fabric>site-z</fabric>

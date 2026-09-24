# AMGT_CORPUS task order -- `CRPS-e-1` -- ROUND 3: the induction admits a CURATED EVIDENCE TABLE (the 40-folder calls made on Andrew's word) beside the report-text rule, calls all 40 (the builder attaches a folder onto a no-folder MEASURED record since e640337205), and takes a deliverables_dir

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-e-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates (C1=23 C2=5 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell writes nothing to S3; the fire is the issuer's drain act under a pair.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 3. Serves **FWD-19** (identity for the 40 folders the crosswalk still
carries UNRESOLVED). Never run the real `add_security` in any mode (its `--dry-run` still calls Bloomberg); every exercise here
goes through the module's own injected fake `call`.

## 1. THE CELL -- `CRPS-e-1`

**Where this came from.** `lib/research/corpus/induction_run.py` (round 2, amendments 1-3) fires ONE `add_security --batch` call
per run over the rows `induction_request` classifies EVIDENCED from report text. Today 40 folders read NO_EVIDENCE / AMBIGUOUS /
DISAGREEMENT there. On Andrew's word (2026-09-24 ~16:5xZ, *"go look right now and make a call"*), the issuer read every document
in those 40 folders and called each one: `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/UNRESOLVED40_CALLS_20260924.json`
(40 rows: `folder`, `root`, `cc`, `bloomberg`, `tier`, `basis`, `action` = `register` (35) or `associate` (5: Copa, Uber, QXO,
Bunzl -> BZLFY US, UMG -> UNVGY US -- keys the pool already carries as MEASURED records with no folder). Since CLOUD @e640337205 `add_security`'s own
collision rule ENRICHES such a key (attaches the folder) instead of refusing, so ALL 40 rows are called; `action` travels into the
read-back as `association_expected` and changes nothing about the call.

**RULED -- what you build (`induction_run.py`, its tests):**
- `--evidence <path>` on `--dry-run` and `--fire`: a JSON evidence table, this shape. For every row of the fresh request whose
  `folder` the table names, the EFFECTIVE state becomes `EVIDENCED` with `root`/`cc` from the table (overriding NO_EVIDENCE,
  AMBIGUOUS and DISAGREEMENT -- the table IS the third source the classifier lacked), the row's `reason` becomes
  `evidence table <tier>: <basis>` (cited, never silent); every table row is placed in the batch (a row with `action`
  `associate` carries `association_expected: true` in the read-back). A folder the table does not name
  keeps the classifier's own state. Rows keep the classifier's raw `state` in the read-back beside an `effective_state` and
  an `evidence_source` (`report-text` | `evidence-table`).
- The totals line is unchanged from round 2: `population P evidenced E ambiguous A disagreement D other O called C registered R
  already_registered K refused F errors X bloomberg_calls B batch_calls Q pool_puts U sum P` with `C = E`.
- `run()` and `write_readback()` take a `deliverables_dir` argument defaulting to `DELIVERABLES_DIR`; every test passes
  `tmp_path` so no test writes into the real deliverables dir (round 2's committed batch file was a test fixture, row Z-S15).
- A malformed table (not a list under `rows`, a row without `folder`/`root`/`cc`/`action`, an `action` off {register, associate})
  is REFUSED before any row is classified, rc 2, printed.

## 3. SURFACES

<paths>
lib/research/corpus/induction_run.py
lib/research/corpus/tests/test_induction_run.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-e-1.curated-evidence-induction.md
</paths>

READ-ONLY: `lib/research/corpus/induction_request.py`, `lib/research/identity/add_security.py`, `lib/research/identity/crosswalk.py`,
the evidence table. Scratch `.scratch/e1/`. Your deliverables dir: `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/`.

## 4. BOUNDS
- Pure ASCII source, LF, Python 3.9-compatible. Tests offline under the existing poison, the fake `call` covering the held path.
- No vendor call, no S3 write, no library write; the dry run lists the library through `induction_request`'s readers only.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W2-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-e-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round3/e1_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ deselected)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-e-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round3/e1_AC2.sh</invocation><expect>population (\d+) evidenced 40 ambiguous 0 disagreement 0 other \d+ called 40 registered \d+ already_registered \d+ refused \d+ errors \d+ bloomberg_calls 0 batch_calls 1 pool_puts 0 sum \1\b</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-e-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round3/e1_AC3.sh</invocation><expect>(?s)REFUSED: --fire requires OPAL_INDUCTION_FIRE=1.*bloomberg_calls 0\b</expect></criterion>
</proof_of_spec>

- AC1 the built behaviour (the evidence path, the deliverables_dir); AC2 the seam probe against the REAL backlog with the REAL
  table: 40 evidenced, 40 called, the calls faked; AC3 the bound the fire sits behind, unchanged.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-e-1.curated-evidence-induction.proof_of_spec.json`
   (keep the shape of your d-5 instance in that dir).
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance and the dry-run
   read-back JSON (written to your deliverables dir by the new argument).
4. Report ONCE: the AC2 totals line, the five `association_expected` rows, and the AC3 refusal line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER AMENDMENT 1 (2026-09-24 ~19:0xZ, before the spawn):** the evidence table was read against the served pool: Bunzl and UMG
now call the US lines the universe already MEASURES (BZLFY, UNVGY), QXO associates, SLB registers (35 register, 5 associate; totals
40 unchanged, so AC2's expect is unchanged). Graded by: GATE (viii) (the order declares `<placeholders>`); no other limb grades a
modification.

**ISSUER AMENDMENT 2 (2026-09-24 ~19:4xZ):** AC1's expect admits pytest's `-k`-filtered summary (`N passed, M deselected in`), which the as-cut pattern could never match (row AMGT_CORPUS-Z-W3-S4, found by `0.9.0_WK_AMGT_CORPUS~3`); at the base the check still FAILS (0 passed). Graded by: GATE (viii) (the order declares `<placeholders>`); no other limb grades a modification.

**ISSUER NOTES:** the FIRE is the issuer's drain act under a fresh never-widen pair (decomposition v3.0 s.5 duty 2): `OPAL_INDUCTION_FIRE=1
python -m lib.research.corpus.induction_run --fire --as-of <today> --evidence <table>` once, read-back recorded; the 5 association rows
are ENRICHED by add_security's own rule since e640337205 (msg 25707), so one batch covers all 40. The table is Andrew's pick delegated to the issuer's read (record @`090ffea`); the CVO's
standing ruling on picks is not widened by this cell. Checks dry-run at the base before the cut: AC1 FAIL (no such tests), AC2 FAIL
(unrecognized `--evidence`), AC3 PASS (the bound) -- recorded in the issuance commit.

<risk>SERVED</risk>
<status>pending</status>
<round>3</round>
<slot>~2</slot>
<fabric>site-z</fabric>

# TO ADVI_COTBKF.TO-CB-at-1.writer-input-resolution -- round 46 CB-at-1: the cot price writer resolves its inputs beside itself first; the census prints each path

<to_id>ADVI_COTBKF.TO-CB-at-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~73</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>46</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-at-1` (`decompositions/ADVI_COTBKF_DECOMP.round46.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-as-1

---

## WORKER FACE

### THE CELL

Cottonwood's price writer `data/cot/scripts/gold/build_canonical_prices_v2.py` stamps `source_firm` on every row from each input's
address. It is deployed with a pinned `scopes.json` beside it at `s3://opal-data-cot/code/gold/`. The gold run syncs only that prefix
and runs the writer from there.

The writer's REPO-FILE inputs resolve through `Path(__file__).resolve().parents[3]` (line ~189). That is the repo root only when run
from the repo; from `code/gold/` those inputs stamp `absent`. It also does `from lib.ticker_overrides import ...` (line ~59), whose
behaviour from `code/gold/` is unmeasured.

The census `data/assets/scripts/silver/commonwealth_cot_price_rewrite.py --source-firm-only` grades the served price rows. It has a
stale-pin check (round 44), and round 45 is removing its split literals.

**CTO ruling (ADDENDUM 19 @47529c9d9e).**
- Every input the writer reads resolves FIRST beside the module, then at the repo root.
- Each input's resolved path is printed in the census.
- Any further repo-file input ships beside the writer under its own pair.
- A census reading `absent` because of path resolution is a failure of this cell.

**Your item.** Code and tests only. No deploy, no S3 write.

1. **Writer: one resolver for every repo-file input.**
   - Resolve `Path(__file__).parent/<name>` first, then `<repo root>/<repo path>`.
   - It records, per input: the name, the role, the resolved path or `unresolved`, the firm, and `how`
     (`beside_module` / `repo_root` / `unresolved`).
   - Apply it to `lib/ticker_overrides` too, both for the firm stamp and for the import. Measure what happens today from a directory
     with no `lib/`, and report it.
   - An input unresolved at both places reads `absent` (a WARN prints), never the own firm.
2. **Writer: record the resolution table** in the output parquet's schema metadata under one key, e.g. `opal_input_resolution`, as
   JSON. No other column or schema change.
3. **Census:** in `--source-firm-only`, after the pin check, read each key's parquet metadata and print one line per input:
   `INPUT name=<n> role=<r> path=<p> how=<h> firm=<f>`.
   - A key with no `opal_input_resolution` prints `INPUT-RESOLUTION absent` and counts as NOT-CLEAN.
   - Today's 38 keys print that, which is expected.
4. **Tests.** Assert each of the following, then commit the new assertions ALONE first; they must fail at the base.
   - (a) With the writer copied ALONE plus `scopes.json` and `ticker_overrides.py` into a temp dir, every input resolves
     `beside_module`.
   - (b) In the repo, the inputs resolve via `repo_root` where nothing is beside the module.
   - (c) With neither present, the input reads `unresolved` / `absent`.
   - (d) The metadata key is present, and the census prints the INPUT lines from it.
   - (e) The existing source-firm and pin-check tests stay green.

LAST line of the new test module's summary: `pytest` passed. In your report, also give the list of repo-file inputs found, with
which of them must ship beside the writer.

### ACCEPTANCE

<criterion id="CB46at1-AC1" cell_refs="CB-at-1"><invocation>python -m pytest data/cot/scripts/gold/tests/test_canonical_prices_input_resolution.py -q</invocation><expect>passed</expect></criterion>
`CB46at1-AC1` -- assertions (a)-(d) pass. The new ones were committed alone first and failed at the base.

<criterion id="CB46at1-AC2" cell_refs="CB-at-1" judgment="true"/>
`CB46at1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded:
- beside-module first, then repo root, for EVERY repo-file input, the import included;
- unresolved is never the own firm;
- the census prints each resolved path from the served file's own metadata.

<expected_criteria>CB46at1-AC1,CB46at1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **START ONLY AFTER CB-as-1 has drained.** It edits `commonwealth_cot_price_rewrite.py` too. The issuer spawns you then. Base your
  worktree on that drain.
- **Code and tests only.** No S3 write and no deploy. Both suites stay green: `data/cot/scripts/gold/tests` and
  `data/assets/scripts/silver/tests`.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W73-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/cot/scripts/gold/build_canonical_prices_v2.py
data/cot/scripts/gold/tests/test_canonical_prices_input_resolution.py
data/assets/scripts/silver/commonwealth_cot_price_rewrite.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round46.md</decomp_doc> (round 46), cell `CB-at-1`.
<owned_cells>CB-at-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB46at1-AC1, CB46at1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~73/ADVI_COTBKF.TO-CB-at-1.writer-input-resolution.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB46at1-AC1,CB46at1-AC2` BEFORE the flip. Mechanical: CB46at1-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the pytest lines (the new test and both suites); the repo-file inputs found and which must ship beside the writer; what the
`lib.ticker_overrides` import does from a bare directory today; commits, with the test-alone commit first.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a code change; the writer runs only on a manual silver-prep, and its redeploy is a later SERVED cell.
comp-iam: DECLARED-NOT-APPLICABLE no AWS act.
comp-adversary: RUN -- the test alone first; beside-module before repo-root for every input, the import included; unresolved never the own firm; the resolution recorded in the output and read back by the census; BLIND: a writer input read only at runtime through another module (named in the report).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 19 @47529c9d9e (msg 3547); row D2-S62.

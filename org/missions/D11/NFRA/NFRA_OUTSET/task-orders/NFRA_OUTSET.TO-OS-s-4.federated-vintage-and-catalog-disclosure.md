# TO NFRA_OUTSET.TO-OS-s-4 -- every comp-heat federated answer carries the catalogs joined and each one's BUILD time -- the ARTIFACT's vintage, never the query's clock

<to_id>NFRA_OUTSET.TO-OS-s-4</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.9.0_WK_NFRA_OUTSET~1</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete -- 2026-09-05 ~06:0xZ, flipped by the ASSIGNEE `0.9.0_WK_NFRA_OUTSET~1` on branch `wk-OUTSET-1` (LOCAL, never pushed), after and only after the proof validated. CRITERIA: 2 MECHANICAL PASS-by-output, 1 JUDGMENT RECORDED with NO verdict (`O4-AC3`, graded by `3.0.0_SA_CVO` at L9). `O4-AC1` -> `timeout 120 .tools/comp-heat federated --budget 120` rc=0, deciding line `VINTAGE: 2 catalog(s) joined (code_heat, iceberg), 2 table(s), 1 measured / 1 UNREAD -- the ARTIFACT's build time, never the query's clock`, with `code_heat.globgrph.code_heat build_time=2026-07-16T03:40:46Z claim=measured age=51.1d` and its instrument line, and `iceberg.globgrph.graph_nodes build_time=UNREAD claim=absent` with a reason naming the prefix and why a partial listing cannot yield a max; 3 of 3 runs identical on every non-clock field. `O4-AC2` -> `python .tools/tests/test_os4_federated_vintage.py` rc=0, `OS4-FEDERATED-VINTAGE BATTERY: 9/9 PASS (denominator 9; 8 offline, 1 live-bounded, 0 Trino queries dispatched)`; the RED mutant the criterion names replaces the artifact build time with the QUERY CLOCK in a temporary engine copy outside the repo and is caught by the 51.1-day gap. `O4-AC3` -> RECORDED: `iceberg.globgrph.graph_nodes` cannot report a build time in-band; 5 of 5 candidate resolution paths checked and closed (not in Glue, no version-hint.text, no snap_ingest pointer, Nessie in-VPC only, object plane resolvable but 183,447 objects / 25-37 s to list completely); the value DOES exist out of band at 2026-09-05T02:11:10Z, so the join's two sides differ in age by roughly 51 days. LIVE-PLANE DISCIPLINE: 0 Trino queries dispatched (every invocation ran below the tool's own 200 s floor and the battery ASSERTS the refusal text rather than assuming it); no budget was raised to make anything pass; AWS reads only (glue GetTable/GetTables/GetDatabases, s3 ListBucket, one HeadObject); the new disclosure costs ~4-5 s per call. A live read is not reproducible the way a git count is -- every reading here carries its vintage, 2026-09-05 ~05:0x-05:5xZ, and the iceberg row's varying `scanned` count is printed rather than smoothed. THE TRAP THE DESIGN ANSWERS: `glue get-table` reports UpdateTime `2026-06-29T20:34:47Z` for `code_heat` while the parquet under its own StorageDescriptor.Location was written `2026-07-16T03:40:46Z` -- 16.3 days apart -- so Glue is used ONLY to resolve a LOCATION here and never as a time source, and battery arm B is built on that disagreement. Per the OS-s-8 lesson: every field read was proven non-empty against the live producer first, and the `<table>_<uuid>/` convention join is proven NON-ZERO on a case known to exist (`graph_nodes` -> 1 of 11) with a 0-match negative control beside it. COMMITS (LOCAL on `wk-OUTSET-1`): `8e5e67e649` code + battery + rows, `9ecf665da4` deliverables + regenerated `06_current_state` pair, plus this flip. ROWS: `NFRA_OUTSET-W1-S12` (OBSERVATION/INERT -- OS-s-2's battery arm F de-flaked on the issuer's own conditional instruction, flake REPRODUCED first and the fix FALSIFIED under the producing condition); `NFRA_OUTSET-W1-S13` (OBSERVATION/ARMED, disarm_owner `2.0.0_SA_COO` -- this worker ran the MAIN workspace's drained copy of a battery and wrote one scratch file there because `cd X && A & B` backgrounds the `cd`; blast radius measured, the stray file deliberately NOT deleted since that tree is outside this grant); `NFRA_OUTSET-W1-S14` (OBSERVATION/ARMED on growth -- 20,374 unexpired Iceberg snapshot metadata files are why the graph side cannot be dated in-band, and that number rises with every derive run). Result: `../deliverables/0.9.0_WK_NFRA_OUTSET~1/federated-vintage-and-catalog-disclosure.result.md`; proof: `../deliverables/0.9.0_WK_NFRA_OUTSET~1/NFRA_OUTSET.TO-OS-s-4.federated-vintage-and-catalog-disclosure.proof_of_spec.json`, `python .tools/proof-of-spec-check.py <instance> O4-AC1,O4-AC2,O4-AC3` -> VALID rc=0, 0 violations, read POST-COMMIT against the committed bytes at `9ecf665da4`. GO paired at cut (the spawn IS the GO for a worker face; a seat order is dispatched by its issuance). Authority: PRD v0.1 @`7fb59f239b` RATIFIED on Andrew's "all approved" (FWD-1..FWD-8) @`26da5ec0fa`; decomposition v0.1 @`6f1655f376`; Andrew-direct at this terminal 2026-09-04 ~15:5xZ, VERBATIM: "youre clear, first write every single task order" then "proceed with internal fan out".</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.1 @`7fb59f239b` (s.7 row OS-s-4; s.4 the bar; s.6 the rulings) · **Decomp cell:** `OS-s-4` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.1 @`6f1655f376`) · **outcome_ref:** FWD-2 · **verb:** fix · **depends_on:** OS-s-1

---

## THE CELL

OS-s-4 (PRD s.7): `federated` runs rc 0 in 86 s over a 374-file histogram with NO vintage line and NO catalog list.

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/federated-vintage-and-catalog-disclosure.result.md` -- the result document: what you measured, what you changed, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9, and a PASS or FAIL written on one is INVALID.

<criterion id="O4-AC1" cell_refs="OS-s-4"><invocation>.tools/comp-heat federated --budget 120</invocation><expect>VINTAGE</expect></criterion>
`O4-AC1` -- the federated answer carries a VINTAGE line naming each catalog joined and its build time.

<criterion id="O4-AC2" cell_refs="OS-s-4"><invocation>python .tools/tests/test_os4_federated_vintage.py</invocation><expect>PASS</expect></criterion>
`O4-AC2` -- a battery with a RED mutant printing the QUERY clock instead of the artifact build time -- the exact distinction this cell exists for.

<criterion id="O4-AC3" cell_refs="OS-s-4" judgment="true"/>
`O4-AC3` -- RECORD whether any joined catalog cannot report a build time, and what the answer prints in that case (UNREAD with its reason, never a default). Evidence only. NO VERDICT.

<expected_criteria>O4-AC1, O4-AC2, O4-AC3</expected_criteria>

## BOUNDS

- **Your write surface is the `<paths>` block below and nothing else.** A path you need that it does not name is a CUT DEFECT: file a BLOCKING row and stop that criterion. It is never an override.
- **EVERY invocation is bounded.** You run each under `timeout 120` and a timeout is RECORDED AS THE OUTPUT -- so an unbounded command yields a criterion whose evidence is the word "timeout". Use a tool's own `--budget`/`--limit`; never name a whole-corpus sweep.
- **No new dependency. No second implementation.** PRD s.5 is out of scope and truthful non-application is not work.
- **NEVER-AUTO-DELETE (PRD R-5, absolute):** nothing is removed by a tool; a candidate list is advisory.
- **No alarm, monitor, freshness-checker or SNS** (standing moratorium).
- **A spec-vs-world divergence is a ROW** at `org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `NFRA_OUTSET-W<n>-S<k>` for a worker (`<n>` = your slot) and `NFRA_OUTSET-S<k>` for a seat -- append, cite `path@commit`, never edit an existing row, keep working.
- **NEVER `git push`**, under this or any order. Report push state as MEASURED (`git ls-remote`).

<paths>
.tools/comp-heat
org/modules/heatmap/
.tools/tests/
org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/
org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md
infra/system/06_current_state.json
infra/system/06_current_state.md
</paths>

⛔ **`infra/system/06_current_state.{json,md}` GRANTED because this cell's `<paths>` TRIGGER THE COMP-SYSTEM GATE, not because the cell edits them.** `safe-commit.sh:789` fires `comp-system --gate --changed` on any pathspec matching `.tools/comp-`, `org/modules/graph/` or the DS deliverables tree, and BLOCKS at `:837` when `06_current_state` is stale -- so the assignee must be able to regenerate and COMMIT that pair or it can edit its surface and then not land it. Added at the drain by the issuer, generalising row `NFRA_OUTSET-W1-S5` from `OS-s-1` to every face in the population that shares the trigger. **A `<paths>` block must name what the GATES require, not only what the CELL touches.**

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> @`6f1655f376` (v0.1), cell `OS-s-4`.
<owned_cells>OS-s-4</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance -- the gate ledger read once for this issuance and quoted in the issuance commit; 0 armed gates name NFRA_OUTSET, comp-heat or the estate-report runner.
comp-iam: DECLARED-NOT-APPLICABLE for a repo-surface cell (no principal, policy or resource is read or changed); ON OS-s-6 and OS-s-7 it is the cell's own instrument and is RUN there.
comp-adversary: DECLARED-NOT-APPLICABLE -- this order is a FRESH CUT with no prior artifact to validate against; comp-adversary composes a validator-context declaration for an existing deliverable, and the first artifact this cell produces is the one it would read. It is the ASSIGNEE's instrument at report time, not the issuer's at cut.
lane: the `<paths>` block above IS the grant (RULING 1, Andrew 2026-09-04 ~04:58Z) -- a worker serial is admitted to exactly these paths while this order is NON-TERMINAL at HEAD, and to its own deliverables folder by the tree convention.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `O4-AC1`, `O4-AC2`, `O4-AC3`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/NFRA_OUTSET.TO-OS-s-4.federated-vintage-and-catalog-disclosure.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> O4-AC1,O4-AC2,O4-AC3` BEFORE the complete flip, which the assignee commits itself.
⛔ **A `complete` flip WITHDRAWS YOUR OWN GRANT** (the grant is read from a NON-TERMINAL order): flip only when every MECHANICAL criterion PASSES. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (serial / TO / branch / HEAD; BLOCKING; CRITERIA with each invocation and its deciding line; PROOF with rc; ROWS; COMMITS; NEXT). You cannot send or receive messages -- anything you would ask is a surprise row.

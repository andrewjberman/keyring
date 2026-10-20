# NFRA_MCPINDEX task order -- `MX-w-6` -- generated `serves` is the TRACED set: a catalog row counts for a tool only when the row's vendor is the vendor of the source that reaches it, so the generator can REMOVE a pair the code does not reach

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round24-GATEWAY.md</decomp_doc>
<owned_cells>MX-w-6</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-w-6.serves-traced</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~82</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; an edit to one existing script and one new test file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (AC1 and AC3 FAIL at the base; AC2 FAILs on its removed-pair arm only) and the planted fixture arms inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-w-6` (round 24, workstream GATEWAY; PRD v0.19 FWD-23; CTO round-23 analysis `ledger/ROUND_ANALYSIS.round23.md` item 6)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). The routing emitter `workflows/gateway_battery/routing_table.py` (merged, round 23) writes `gateway_serves/1` with `--serves-out`: for each census tool that has a source set, the (vendor, firm) pairs the tool serves, the catalog's current pairs, and the `added` and `removed` lists. The CTO's analysis says the generated `serves` is correct to withhold from the catalog because it over-approximates: on the 7 tools that carry `serves` today it removed nothing. The cause is one line: a catalog row matches a source by bucket and a prefix that is a prefix of the other, so a source with a coarse or empty prefix over a bucket matches the rows of EVERY vendor in that bucket, and all their pairs land in `serves`. You EDIT the script and add one new test file; you change only the pair selection of the serves generator.

**What to build.** In `build_serves` of `workflows/gateway_battery/routing_table.py` (the loop over `sources[name]`), apply the TRACED rule below. Read the script first. Add `workflows/gateway_battery/tests/test_routing_serves.py` with at least 4 tests of your own. Nothing else changes: the ROUTING table (counts, verdicts, classes, the three `--plant` modes, the output bytes) must stay byte-identical, the `SERVES` stdout line keeps its format, and the existing `tests/test_routing_table.py` must keep passing unchanged.

The current code of the generator's loop (quoted from the merged file):

```
        generated = set()
        for src in sources[name]:
            matched = [r for r in rows if s3_matches(r, src)]
            if matched:
                generated.update((r["vendor"], r["firm"]) for r in matched)
            else:
                generated.add((norm(src["vendor"]), UNRESOLVED_FIRM))
```

### The contract (verbatim from the decomposition; it is the whole specification)

**W6 SERVES** In `routing_table.py`, `--serves-out` writes the TRACED set: a catalog row contributes its (vendor, firm) to a tool only when some `s3` source of the tool matches the row by bucket and prefix (the link rule) AND the row's `vendor` equals the source's `vendor`. A source that matches rows of a vendor it does not carry (a coarse or empty prefix over a bucket) contributes nothing for them. The unresolved pair rule (a non-matching source contributes (the source's vendor, `unresolved`)) is unchanged. `added` and `removed` are computed as before, so `removed` is non-empty when the catalog claims a pair the trace does not reach. Round-23 behavior of `ROUTING` (counts, verdicts, classes, the three `--plant` modes) is byte-identical on the round-23 fixtures and the live table.

The round-23 serves paragraph this edits (for reference): `serves` (generated) is the set of (`vendor`, `firm`) of every catalog row (table rows only) that one of the tool's `s3` sources matches, by the same bucket and prefix rule as the link check; a source with no matching row contributes (the source's `vendor`, `unresolved`). `current` is the `serves` list of the tool's row in the catalog's top-level `tool_index` list; no row or no `serves` is an empty list. `added` is generated minus current, `removed` is current minus generated; `changed` counts the tools with either list non-empty.

### The two silences the issuer has settled (follow them)

1. The unresolved rule fires only when NO catalog row matches the source by bucket and prefix. A source that matches rows but none of them carries the source's vendor contributes NOTHING (neither a row pair nor an unresolved pair): the tool's entry is still written, with `serves` possibly empty.
2. A row whose `vendor` is empty or missing matches no source vendor, so it contributes nothing (the vendor comparison is on the normalised string, `norm`, that the script already has).

### Inputs you read (you do NOT edit them)

- The merged script `workflows/gateway_battery/routing_table.py` and its tests `workflows/gateway_battery/tests/test_routing_table.py` (the model for a test file: scripts are run by path as subprocesses on small inputs written inside the test with `tmp_path`).
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/fixtures/w6_census.json`, `w6_catalog.yaml` and `w6_sources.json`: the criterion AC1's fixture (6 tools, 3 catalog rows of 3 vendors in 2 buckets).
- For criterion AC2 the real inputs it runs on: the round-22 census, the catalog `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, the six source-set files `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~71/source_sets_assets.json` through `~76/source_sets_m365.json`, and the committed round-23 outputs `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/evidence/ROUTING_TABLE_20261019.json` and `GATEWAY_SERVES_20261019.json`. If any is absent in your worktree, `git sparse-checkout add` its folder (the only sparse change you may make).

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree already carries the sparse folders `workflows/gateway_battery`, `workflows/gateway_battery/tests`, `workflows/atom_decomposition` and `infra/aws/ec2/opal-gateway/app`.
1. Read `routing_table.py` (`s3_matches`, `build_serves`, `norm`, `UNRESOLVED_FIRM`) and `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w6_check.py` (the executable form of this section; read what each arm grades). Make the one change in `build_serves`, then the test file: at least 4 tests of your own, on small catalogs and source sets you write inside the test (not the issuer's fixtures; those are the criteria's). They cover at least: a coarse-prefix source over a two-vendor bucket keeps only the source's vendor and `removed` carries the other; an exact prefix of the right vendor is unchanged; a source whose vendor no matched row has contributes nothing; a source with no matching row stays `(vendor, unresolved)`.
2. Run the three criteria in section 4 until each prints `RESULT: PASS`.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, `members.yaml`, `pending_members.yaml`, the catalog or its row files, the emitter (`emit_catalog_v02.py`), any file under `infra/`, the PRD, the round-23 evidence, or any other file under `workflows/`. No AWS call, no network call, no grant, no deploy, no push. Do NOT regenerate or overwrite `GATEWAY_SERVES_20261019.json`: the criteria write their outputs under a temporary directory.
2. Python 3.9, standard library plus `yaml` (PyYAML, installed) only. ASCII only in code, comments, strings, output and data files. No type syntax newer than 3.9 (no `X | Y` annotations, no `match`). The commit gate runs `py_compile`, the naming gate and `ruff` for py39.
3. No tool name, channel id, firm or vendor is typed as a whole-string literal in the script (`UNRESOLVED_FIRM` and the contract's fixed words are fine); tests under `tests/` and data files are exempt.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output (no new key in `gateway_serves/1`, no new option).
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w6.AC1.sh`, `.AC2.sh` and `.AC3.sh` (they run `w6_check.py` in the same folder). Do not edit any of them. AC2 also runs the round-23 `r1.AC1` and `r1.AC2` through `round23/checks/h_check.py`; if the TRACED rule makes one of their arms fail, REFUSE that criterion and report the arm text and your measurement (the issuer settles the contract; do not change an `r1` check or fixture).
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/gateway_battery/routing_table.py
workflows/gateway_battery/tests/test_routing_serves.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~82/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-w-6.serves-traced.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W82-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-w-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w6.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; on the fixture the coarse-prefix source over a two-vendor bucket serves only its own vendor and the other pair is REMOVED; an exact prefix is unchanged; a coarse source of the other vendor adds and removes; a source with no matching row stays unresolved; a source whose vendor no matched row has contributes nothing; the counts read tools=6 changed=5; two runs give the same bytes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-w-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w6.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; the round-23 r1.AC1 and r1.AC2 still PASS; the live routing table is byte-identical to the committed round-23 table; for every one of the 127 tools the traced serves set is a subset of the round-23 serves, and at least one tool that carries serves today now has a removed pair -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-w-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w6.AC3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (pytest rc=0, at least 4 passed) for `test_routing_serves.py` -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~82/NFRA_MCPINDEX.TO-MX-w-6.serves-traced.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 24, workstream GATEWAY, worker ~82. Source: the CTO's round-23 analysis (`1.0.0_SA_CTO~Z`, 2026-10-20) item 6 and PRD v0.19 @7c42c0c743. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round24-GATEWAY.md` (contract R24.3 W6, frozen at the cut). Base dry-runs 2026-10-20: `w6.AC1` FAIL (3 of 9 arms ok), `w6.AC2` FAIL on its last arm only (6 of 7 ok: r1.AC1, r1.AC2, the live table and the subset arm pass at the base; no tool has a removed pair), `w6.AC3` FAIL (test file absent). The issuer's scratch reference (a one-line change of the merged script plus four tests, outside the repository) passes all three. On the live inputs the reference leaves the routing table byte-identical, makes the serves a subset of the round-23 file, and removes `schwab/49financial` from `client_resolve_account`; 52 tools with no vendor-bearing row now carry an empty `serves` where round 23 carried an `("", "")` pair, which is the intended effect of silence 2. The `r1` fixture serves arms (tS1, tC1, tM1) are consistent with the rule (every matching source there carries its rows' vendor). Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>24</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

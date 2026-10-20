# NFRA_MCPINDEX task order -- `MX-z-4` -- decide, for the two tools still refused as member (b), a new catalog row it reads or a (c) reason, grounded in the traced source sets

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round26-GATEWAY.md</decomp_doc>
<owned_cells>MX-z-4</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-z-4.coverage-two</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~93</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one JSON data file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base) and the planted mutants inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-z-4` (round 26, workstream GATEWAY; PRD v0.19 FWD-23 coverage; CTO round-25 analysis, round-26 list item 4)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). FWD-23 asks that every tool of the gateway census is indexed by the catalog. After round 25 the coverage gate over the 14 channels still refuses two tools as member (b), both owned by `NFRA_MCPINDEX`, both in the channel `opal_discover`:

- `opal_describe`
- `opal_discover`

**What to build.** `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~93/coverage_two.json`, one item for each of these two tools, exactly these and each once.

### The contract (verbatim from the decomposition; it is the whole specification)

**Z4 COVERAGE TWO** `coverage_two.json`, schema `gateway_coverage_two/1`: `{"schema","items":[{"tool","disposition":"row"|"c","row":null|{"entity","bucket","prefix","vendor","firm"},"reason":str,"cite":"<path>:<line>"}]}`. One item for each of the two refusals of `COVERAGE_r25_candidate_c.json` (`opal_describe`, `opal_discover`), exactly those. `row`: a catalog row the tool reads, `entity` unique and not already in the catalog, `bucket`/`prefix` overlapping an `s3` source of the tool's source set (`source_sets_integrations.json`), `vendor` in the allowed vocabulary; `c`: the tool reads no data a row can describe, `reason` of at least eight ASCII words and an existing `cite`. Read the two tools' code (`app/integrations/opal_discover/integration.py`) and the catalog rows `DATA_CATALOG.yaml` already holds for the portal datasets they describe before choosing.

What the check adds to that text (so you are not surprised): every item, row or c, carries a `reason` of at least eight ASCII words and a `cite` that resolves (`<path>:<line>`, a file in the repository or under `infra/aws/ec2/opal-gateway/`, and a line that exists); a `row` item's `entity` is lower-case words with underscores, not in the catalog and not used by another item, its `bucket` and `prefix` overlap an `s3` source of the tool (a prefix that starts with, or is started by, the source's prefix), its `vendor` is one of the catalog's vendors or opal, ycharts, microsoft, bloomberg, other, and `firm` is a string; any entity-looking word in a `reason` (a word starting `portal_`, `opal_data_`, `harvest_`, `dynamodb_` or `silver_`) must be a real catalog entity, a gateway tool name or a catalog section name (`portal_datasets`, `silver_datasets`, `harvest_datasets`).

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/evidence/COVERAGE_r25_candidate_c.json`: `refusals[]` with `class` tool_member_b, `channel`, `subject` (the tool) and `detail` (the owner).
- the source set of the two tools: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~75/source_sets_integrations.json` (`source_sets/1`, `tools[]` of `{tool, vendors, sources:[{kind, bucket, prefix, vendor, cite}]}`). Both tools carry two sources: a `store` source (the runtime catalog `app/refs/DATA_CATALOG.yaml`, vendor gateway, cite `app/integrations/opal_discover/integration.py:194`) and an `s3` source (bucket `opal-data-portal-v2`, prefix empty, vendor opal, cite `app/integrations/opal_discover/integration.py:398`).
- the catalog `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` (read-only): sections `silver_datasets`, `portal_datasets` and `harvest_datasets` are the rows, each with `entity`, `bucket`, `prefix`, `vendor` and a `table`/note; the catalog's own top-level `bucket` is `opal-data-portal-v2`; `portal_datasets` holds five rows (`portal_etfs_positioning`, `portal_mdpf_account_distribution`, `portal_mdpf_aggregate_aua`, `portal_mdpf_aum_metrics`, `portal_mdpf_model_benchmarks`).
- the gateway source under `infra/aws/ec2/opal-gateway/app/` (read-only): `app/integrations/opal_discover/integration.py` (the two tools `opal_discover` and `opal_describe`, `discover()` at line 808, `_served_object` near line 390, the loader of the one catalog near line 190).
- the precedent of round 24, the same question for 34 other tools: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~81/coverage_rows.json` (35 items `c`, 1 `row`). There a tool whose data is ALREADY described by catalog rows took `c`, its `reason` naming those rows' entities (the issuer then links them as member (a) at the drain, the CTO's ruling of 2026-10-20); a `row` was written only for an object family no existing row describes.

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree may lack `infra/aws/ec2/opal-gateway/app`, `workflows/atom_decomposition` and `workflows/gateway_battery`; the issuer pre-adds them, and `git sparse-checkout add infra/aws/ec2/opal-gateway/app workflows/atom_decomposition workflows/gateway_battery` is the only sparse change you may make (do it first if a path above is missing).
1. Read `app/integrations/opal_discover/integration.py`: what each tool reads (the one runtime catalog; for a dataset it describes, the single served object of the catalog row it matched, from the catalog's bucket), and which catalog rows already describe that data. Decide per tool:
   - the data the tool reads is described by existing catalog rows (the portal rows, the rows of the catalog's bucket) or is the catalog itself, and no object family it reads lacks a row: disposition `c`, `row` null, `reason` at least eight ASCII words saying so and naming the existing rows' entities you relied on, `cite` the line of the read;
   - some object family the tool reads is described by NO row: disposition `row`, one row (`entity` new, `bucket` and `prefix` overlapping the tool's `s3` source, `vendor` in the vocabulary, `firm` a string), `reason` saying what the family holds, `cite` the line that reads it.
   The check does not choose for you; it enforces that whatever you choose is grounded. Where the two tools share one family, the first (`opal_describe`) takes `row` and `opal_discover` takes `c` naming that entity.
2. Write the file with the Write tool (JSON, `indent=1`, ASCII), then run both criteria until each prints `RESULT: PASS`. Read `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z4_check.py` for exactly what each arm grades.
3. Then spot-check yourself: re-read the cited lines and the catalog rows you named, and fix any that is wrong. The issuer reads the choice at the drain.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's checks or decomposition, `members.yaml`, `pending_members.yaml`, the catalog or its row files, the source-set files, the emitter (`emit_catalog_v02.py`), any file under `infra/` or `app/`, the PRD, or any other file under `workflows/`. No AWS call, no network call, no grant, no deploy, no push.
2. ASCII only in the data file. You write one data file and no code.
3. The data file is JSON written with the Write tool, `indent=1`, ASCII.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit). If the naming gate prints NAMING ERROR for a folder missing from the sparse cone and the commit still lands, say so in a surprise row (id form below); do not refile a row another worker of the round already filed.
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z4.AC1.sh` and `.AC2.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z4_check.py`). Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~93/coverage_two.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~93/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-z-4.coverage-two.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W93-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-z-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z4.AC1.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~93/coverage_two.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line (2 tools in scope); the schema; exactly the 2 refused tools, each once, each with a disposition row or c, a row object only for a row item (row null for c), a non-empty ASCII reason and a cite; the planted mutants (a tool dropped, a tool twice, a foreign tool, a wrong schema, a bad disposition, a row item without a row object, a c item that carries a row, a non-ASCII reason) are each refused -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-z-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z4.AC2.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~93/coverage_two.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line; every item has a reason of at least eight ASCII words that names only real catalog entities and a cite that resolves to an existing file and line; every row item has a new unique entity, a bucket and prefix that overlap an s3 source of the tool, and a vendor in the vocabulary; the planted mutants (an entity already in the catalog, a bucket no source names, a vendor outside the vocabulary, two items with one entity, a three-word reason, a cite to a missing file, a cite past the end of the file, a reason that names an entity the catalog lacks) are each refused for the planted defect -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~93/NFRA_MCPINDEX.TO-MX-z-4.coverage-two.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you chose per tool (row or c) and why in one line each; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 26, workstream GATEWAY, worker ~93. Source: the CTO's round-25 analysis `ledger/ROUND_ANALYSIS.round25.md` (`1.0.0_SA_CTO~Z`, 2026-10-20 ~18:1xZ) round-26 list item 4 (the 2 remaining coverage refusals: a row each, or (c) with its reason) and PRD v0.19 @7c42c0c743. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round26-GATEWAY.md` (the contract R26.3 Z4 is frozen at the cut). Base dry-runs 2026-10-20: `z4.AC1 base: FAIL as expected` and `z4.AC2 base: FAIL as expected` (the deliverable is absent). Scratch reference files (not committed, built outside the repository): one with two (c) items naming the existing portal rows, one with a row item for `opal_describe` and (c) for `opal_discover`; both pass `z4.AC1` (10 of 10 arms) and `z4.AC2` (10 of 10 arms), so the row and the c branches both run; the mutants of AC2 are planted from the data present (when the file holds no row item, a c item is turned into a row-form copy), each is checked to be refused for the planted defect itself and not for another reason. The checks prove shape, uniqueness and grounding in the traced sources and the catalog, not that a (c) judgment is right, which the issuer reads at the drain. LIKELY ANSWER (not enforced): both tools read the ONE catalog and the served object of a row the catalog already holds (the five `portal_datasets` rows, the rows of the catalog's bucket), so `c` naming those rows, as round 24 ruled for the 32 tools whose data existing rows describe; the issuer links them as member (a) at the drain. The sparse-cone first step is in the face because round 24's workers lacked the folders; the checks read with `errors="replace"` (a commit-gate rule for log/catalog-named files).

<status>issued</status>
<round>26</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>

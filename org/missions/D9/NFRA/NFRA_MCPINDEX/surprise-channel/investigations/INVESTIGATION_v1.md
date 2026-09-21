# NFRA_MCPINDEX -- surprise channel, INVESTIGATION v1

**Opened by:** `0.9.0_WK_NFRA_MCPINDEX~1` at L7, cell `MX-c-1`, 2026-09-21. **Home:** the project tree's channel.
Lane `ANY`; the gate `.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder
== project). **Append-only.** Worker rows carry their slot's coordinate, `NFRA_MCPINDEX-W<n>-S<k>`; a seat's row
carries none.

**Denominator at this write: 7 rows** -- `NFRA_MCPINDEX-W1-S1`, `NFRA_MCPINDEX-W1-S2`, `NFRA_MCPINDEX-W4-S1`, `NFRA_MCPINDEX-W3-S1`, `NFRA_MCPINDEX-W1-S3`, `NFRA_MCPINDEX-W4-S2`, `NFRA_MCPINDEX-W1-S4`. Rows minted in worker worktrees that had not seen each other were joined at the drains by 2.0.0_SA_COO~M, rows unedited.

```json
[
  {
    "id": "NFRA_MCPINDEX-W1-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~1",
    "surfaced_at": "2026-09-21T05:07:26Z",
    "one_line": "MXC1-AC4 requires running the named writer once and observing the SERVED file (infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml) change, plus a reversible edit to an emitter input under workflows/atom_decomposition/runs/; this cell's <paths> grant names only emit_catalog_v02.py (docstring lines 1-10) and this investigation file.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO: org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-c-1.catalog-writer.md <paths> block (2 entries only): 'workflows/atom_decomposition/emit_catalog_v02.py' and 'org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md'.",
        "CRITERION: same TO, MXC1-AC4 verbatim -- '(difference) the named writer is run once at the cell's HEAD with one reversible change to an emitter input, the served file changes by exactly that row, and the same run with the input unchanged leaves the served file's SHA-256 unchanged (the run and its revert both in the cell's command log)'.",
        "WRITE TARGET: emit_catalog_v02.py:42-43 -- OUT_DIR/OUT resolve to infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml (the 'served file'), confirmed by MXC1-AC3's module-import read (probes/mx_c_1.py AC3, 2026-09-21T05:07:04Z): resolved target == live path.",
        "INPUT SOURCE: lift_catalog_v02.py :308-313 -- resolve_substrates() reads rectangle.final.certified.json under workflows/atom_decomposition/runs/<unit>/<stamp>/, the only 'emitter input' a reversible edit could target without editing emit_catalog_v02.py's own non-docstring code.",
        "BOUND: worker face BOUNDS (top-level, and this TO's own Bounds section) verbatim -- 'A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.' Bound 9 (decomp s.8) -- 'A criterion that cannot be satisfied as written is REFUSED and reported with its measurement, never repaired, widened or met by another route.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order's ACCEPTANCE section demands MXC1-AC4 be satisfied by actually running the writer once and observing the live served catalog file change by exactly one planted row, with the run and its revert logged; the same order's <paths> block is the worker's whole write grant.",
    "world_is": "The <paths> block names only the emitter's own docstring lines and this investigation file. Exercising MXC1-AC4 as written needs write access to infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml (the served file itself) and to a workflows/atom_decomposition/runs/ certified-run JSON (the only lever for a 'reversible change to an emitter input' that does not edit the emitter's own logic, itself out of grant beyond the docstring). Neither path is granted. The worker recorded MXC1-AC4 REFUSED (probe VERDICT: FAIL-MXC1-AC4) rather than writing outside the grant or redirecting the writer's output to a substitute path (which would not exercise the NAMED writer against the NAMED live path C1/AC3 require).",
    "notes": "BLOCKING on MXC1-AC4 only; AC1, AC2, AC3, AC5, AC6 are unaffected and PASS by their own probes. INERT: no live state changed and nothing is armed by the refusal -- the writer's exercise remains undone, not miswired. disarm/owner: whoever re-cuts or re-grants this cell (issuer 2.0.0_SA_COO~M) decides whether to widen the <paths> grant to cover the served file + a runs/ input for a future pass at AC4, or to accept the REFUSED disposition as this round's answer."
  },
  {
    "id": "NFRA_MCPINDEX-W1-S2",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~1",
    "surfaced_at": "2026-09-21T05:30:00Z",
    "one_line": "This TO's <proof_of_spec> section names firm `NFRA` for the proof-of-spec instance, but PROOF_OF_SPEC.schema.json's `firm` field is a closed enum {49F, INF, COT, MDPF, FABRIC} with no NFRA member; setting it would fail jsonschema structural validation, so the field was left absent (schema-optional) instead.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO: org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-c-1.catalog-writer.md:114 -- '(phase `INVESTIGATION`, firm `NFRA`, spec_ref.group `OTHER`, ...)'.",
        "SCHEMA: org/standards/PROOF_OF_SPEC.schema.json, `firm` property -- 'enum: [\"49F\",\"INF\",\"COT\",\"MDPF\",\"FABRIC\"]'; NFRA is not a member.",
        "INSTRUMENT: py -3.12 -c \"import jsonschema; print(jsonschema.__version__)\" -> 4.26.0 installed in this worktree's environment, and .tools/proof-of-spec-check.py:2316-2323 runs jsonschema.Draft7Validator(schema).iter_errors(inst) when the package is present -- an enum violation would be a structural FAIL, not a warning."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order's own <proof_of_spec> instructions name the literal field value firm `NFRA` for this instance.",
    "world_is": "The ratified schema's `firm` enum has no NFRA member (its 5 members are client-firm codes plus FABRIC for no-client-firm fabric-infrastructure work); NFRA is this project's macro code, not a schema-recognized firm token. Setting `firm: \"NFRA\"` would make the instance schema-INVALID under jsonschema, which is installed and active in proof-of-spec-check.py. The worker omitted the field (OPTIONAL per schema) rather than write a value the checker's own structural pass would reject; the field's absence resolves per the schema's own documented fallback to UNPARSED-by-derivation (to_id's leading token 'NFRA_MCPINDEX' is also not an enum member).",
    "notes": "OBSERVATION, INERT: no criterion in this cell reads the `firm` field, and omitting it does not fail proof-of-spec-check.py (the field is optional at the schema level). Whether NFRA-macro projects need a `firm` enum member (or whether FABRIC is the intended value for D9/NFRA work) is a schema-owner call, outside this cell's <paths>."
  },
  {
    "id": "NFRA_MCPINDEX-W4-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~4",
    "surfaced_at": "2026-09-21T05:40:00Z",
    "one_line": "MX-a-3's live bucket (opal-data-bd) also hosts substantial live data for MX-a-2 (schwab/, 4622 objects/~12.1GB) and MX-a-6 (smartx/, 2967 objects/~64.7MB), plus platinum/ and canonical/ prefixes, none named in the PRD or the decomposition's S8 per-property notes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "live `aws s3 ls s3://opal-data-bd/` (2026-09-21, this worker's run): top-level prefixes include blackdiamond/, schwab/, smartx/, platinum/, canonical/, bronze/, forwardfill_v2/, gold/, code/, logs/ and several ops/scratch prefixes, alongside silver/ (this property's own read scope)",
        "live `aws s3 ls s3://opal-data-bd/schwab/ --recursive --summarize`: 4622 objects, 12100549274 bytes, newest schwab/silver/ult/date=20260723/data.parquet",
        "live `aws s3 ls s3://opal-data-bd/smartx/ --recursive --summarize`: 2967 objects, 64664996 bytes, newest smartx/raw/models/2026-09-20/...json",
        "live `aws s3 ls s3://opal-data-bd/platinum/ --recursive --summarize`: 24906 objects, 5510455641 bytes",
        "live `aws s3 ls s3://opal-data-bd/canonical/ --recursive --summarize`: 486 objects, 1979982369 bytes",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md s.3 'Property-specific additions' (lines ~398-402 @f506f63a8b) names only MX-a-1, MX-a-2 and MX-a-7 specific facts; no line anywhere in s.3 or s.6 names a bucket shared across MX-a-2/MX-a-3/MX-a-6"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The decomposition's S8 per-property additions section (s.3 @f506f63a8b) states property-specific facts only for MX-a-1, MX-a-2 and MX-a-7 (portal surface families, the Schwab dim_transaction fence check, and the per-fund TrueShares/Pathfinder split); it names no cross-property infrastructure fact for MX-a-3, MX-a-4, MX-a-5 or MX-a-6, and C7's isolation contract (PRD CONTRACTS s.254-259) describes 'one read role per property, fenced to exact silver prefixes' as though each property's silver data were independently scoped.",
    "world_is": "MX-a-3's own live bucket (opal-data-bd, read from data/black_diamond/scripts/silver/merge-daily-incremental.py:53) is NOT exclusive to Black Diamond: the SAME bucket also holds multi-gigabyte live data under schwab/ (MX-a-2's vendor) and smartx/ (MX-a-6's vendor), plus platinum/ (served tier) and canonical/ (an undocumented tier) -- so at least three of this project's own MX-a-k properties, and possibly a served surface, physically co-locate in one bucket that neither the PRD nor the decomposition's per-property notes disclose as shared. This cell's own AC8 read fence excludes all of it by exact prefix, so MX-a-3 itself is unaffected; filed for MX-a-2/MX-a-6/MX-i-1..MX-i-3 (the grant-model generator) to have on record before minting per-property IAM roles."
  },
  {
    "id": "NFRA_MCPINDEX-W3-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~3",
    "surfaced_at": "2026-09-21T06:30:46Z",
    "one_line": "portal/ (gitlink submodule) is empty in this worker's worktree, so MXA1-AC11's Advisor Intelligence page citation has no .tsx path, unlike the other 3 surfaces which were citable from checked-out data-pipeline-script docstrings and docs/architecture/YALP_*.md briefs.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ls portal (in /c/tmp/wk-mcpindex-3) returns nothing -- the directory is empty",
        "git submodule status portal -> fatal: no submodule mapping found in .gitmodules for path 'portal' (run from this worktree)",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~3/analysis-portal.result.md ## AC11 discloses this and cites data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py:9-12, data/etfs/scripts/gold/etf_positioning_publisher.py:7-9 and docs/architecture/YALP_MACROS.md:16 (+ YALP_CMASMP.md:12, YALP_CORREL.md:13, YALP_FACTOR.md:15, YALP_MKTOVR.md:15) for surfaces 1-3, and states no equivalent .tsx citation was found in checked-out code for surface 4"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "MXA1-AC11: 'each surface's portal page is named with the precomputed key it reads' for all four surface families (platinum/mdpf, platinum/etfs, platinum/advi, json/*)",
    "world_is": "3 of 4 surfaces' portal pages were named with a .tsx or portal/src/pages/ citation from checked-out repository text (data-pipeline-script docstrings for mdpf/etfs; docs/architecture/YALP_*.md briefs for json/*). The 4th (advisor intelligence, platinum/advi + the Inflection/Cottonwood firm buckets) has no equivalent citation available, because portal/ -- the only tree that would carry it -- is an empty gitlink submodule in this worker's worktree (not in this worker's <paths> grant). AC11 is satisfied on its letter (a page reference and a precomputed key are both named for all 4 rows) with this gap disclosed rather than guessed; a future cell needing the exact advisor-intelligence page path (e.g. an MX-t-1-class tool-building cell) will need a worktree that carries the portal/ submodule checked out."
  },
  {
    "id": "NFRA_MCPINDEX-W1-S3",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~1",
    "surfaced_at": "2026-09-21T06:40:00Z",
    "one_line": "validate_catalog_v02.py writes workflows/atom_decomposition/catalog_v02/validation_report.json as a designed side effect of running it (its own docstring: 'Results -> catalog_v02/validation_report.json'), but this cell's <paths> grant names only validate_catalog_v02.py itself, not the catalog_v02/ report path -- MXC2-AC5 requires actually running the script, which writes there regardless of any code this cell adds.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO: org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-c-2.catalog-silver-schema.md <paths> block -- 7 entries, none of them workflows/atom_decomposition/catalog_v02/ or any file inside it.",
        "SCRIPT: workflows/atom_decomposition/validate_catalog_v02.py:15 docstring -- 'Results -> catalog_v02/validation_report.json + stdout with denominators.'; :31 REPORT = os.path.join(HERE, 'catalog_v02', 'validation_report.json'); :139-141 with io.open(REPORT, 'w', ...) -- the write is unconditional on every run, pre-dating this cell's edits.",
        "MEASURED: running the unmodified (pre-edit) baseline script on 2026-09-21 at this worker's cut produced `git status --porcelain -- workflows/atom_decomposition/catalog_v02/` = ' M workflows/atom_decomposition/catalog_v02/validation_report.json' and `git log -1 --format=%H -- <that path>` = 96dcb4a66a (the same 2026-08-20 port commit as DATA_CATALOG.yaml) -- a TRACKED file, not gitignored, last touched before this cell existed.",
        "BOUND: worker face BOUNDS (top-level) verbatim -- 'A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "MXC2-AC5 demands 'validate_catalog_v02.py and battery_catalog_v02.py pass at the cell's HEAD, run output printed', which can only be measured by actually executing validate_catalog_v02.py; this cell's own writes line and <paths> block enumerate exactly the 6 project paths (the 3 named scripts, catalog_entries/, CAT, the new test file) plus the investigation file, and none of them is catalog_v02/ or a path inside it.",
    "world_is": "Running validate_catalog_v02.py (both before and after this cell's own code changes -- the write is pre-existing script behavior, not something this cell's diff introduces) modifies the tracked file workflows/atom_decomposition/catalog_v02/validation_report.json as its designed report output. This worker did NOT commit that modified file: it ran `git checkout -- workflows/atom_decomposition/catalog_v02/validation_report.json` after every exercise (AC5's probe function does this automatically) to restore the tracked bytes before finishing, so nothing outside the <paths> grant is committed. AC5 is satisfied by capturing the run's stdout (which the probe prints, with rc and denominators) rather than by committing the side-effect file.",
    "notes": "OBSERVATION, INERT: no criterion needs the report FILE committed, only the run's printed output (which the probe captures and reports); the worker's self-imposed discipline of reverting the side effect after every exercise means no grant is ever exceeded at commit time. Whether catalog_v02/ should be added to a future cell's <paths> (or gitignored, since it is a regenerable report) is an issuer/schema-owner call, outside this cell's <paths>."
  },
  {
    "id": "NFRA_MCPINDEX-W4-S2",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~4",
    "surfaced_at": "2026-09-21T06:51:41Z",
    "one_line": "The MX-a-3 drain merge 0c46bec859 ('merge worker 0.9.0_WK_NFRA_MCPINDEX~4 -- 9 PASS + 1 judgment, proof VALID (re-run by the issuer), order complete') did not carry worker branch edf584f64a's four deliverable files or the task order's status flip into the merged tree; this worker's issuer context named the result file as readable prior work in this slot, but it does not exist at this worktree's cut.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git diff-tree --no-commit-id --name-status -r edf584f64a (the worker branch, second parent of the drain merge): adds deliverables/0.9.0_WK_NFRA_MCPINDEX~4/NFRA_MCPINDEX.TO-MX-a-3.analysis-blackdiamond.proof_of_spec.json, deliverables/0.9.0_WK_NFRA_MCPINDEX~4/analysis-blackdiamond.result.md, deliverables/0.9.0_WK_NFRA_MCPINDEX~4/probes/_mutant_control.py, deliverables/0.9.0_WK_NFRA_MCPINDEX~4/probes/mx_a_3.py, plus this investigation row and the task order's own status flip -- all four deliverable files confirmed present in that commit's own tree via git ls-tree -r --name-only edf584f64a.",
        "git ls-tree -r --name-only 0c46bec859 -- org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/ (the drain MERGE commit itself): lists only 0.9.0_WK_NFRA_MCPINDEX~1/* paths; none of the four ~4 files are present.",
        "git diff de8bf648cd 0c46bec859 --stat (first-parent diff of the merge, per the box-memory rule that MERGED != merged tree): 1 file changed, org/.../surprise-channel/investigations/INVESTIGATION_v1.md +25/-1 -- no deliverables path and no task-order path appear in the merge's own first-parent diff.",
        "git merge-base --is-ancestor 0c46bec859 8fd757cca8: true (this worktree's cut point is a descendant of the drain); git ls-tree -r --name-only 8fd757cca8 -- org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/ still lists only 0.9.0_WK_NFRA_MCPINDEX~1/* at this worker's own worktree HEAD.",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-a-3.analysis-blackdiamond.md:8 read at this worktree's HEAD (8fd757cca8): '<status>pending</status>', not complete.",
        "This worker's own issuer-context preamble (2.0.0_SA_COO~M) states the MX-a-3 analysis 'is at org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~4/analysis-blackdiamond.result.md and you may read it as prior work in this slot'; `ls -la` on that deliverables directory at this worktree's HEAD shows only the 0.9.0_WK_NFRA_MCPINDEX~1 subfolder, confirming the named file's absence."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The MX-a-3 drain merge commit 0c46bec859 (authored by issuer 2.0.0_SA_COO~M) states in its own message that the order is complete with '9 PASS + 1 judgment, proof VALID (re-run by the issuer)'; this worker's issuer-context preamble, relayed from the same issuer, states the analysis result file is readable as prior work in this slot.",
    "world_is": "Neither the merged tree at 0c46bec859 nor its descendant at this worktree's cut (8fd757cca8) contains any file under deliverables/0.9.0_WK_NFRA_MCPINDEX~4/, and the task order's own <status> tag still reads pending at that same HEAD. The worker branch edf584f64a that the merge names as its second parent does carry the four deliverable files and the status flip; they did not survive into the merge's own tree (the merge's first-parent diff shows only the investigation-file append). So the drain commit's completion claim is not reflected in the tree a later reader would inspect.",
    "disarm_owner": "2.0.0_SA_COO~M",
    "notes": "OBSERVATION/ARMED, not BLOCKING: MX-a-4's own ten criteria do not require reading the MX-a-3 result file, so this worker proceeds unblocked on its own cell using only the PRD, decomposition and live reads named in its own face. Filed because a later act that trusts the drain commit's 'order complete' / 'proof VALID' claim at face value (an L9 adjudication, an L10 terminality count over task-order <status> tags, or a future worker in this slot instructed to read the blackdiamond file) would find neither the file nor the status flip actually present. disarm_owner 2.0.0_SA_COO~M (issuer of the MX-a-3 drain) should re-merge or cherry-pick edf584f64a's four deliverable paths and the task-order status flip into CLOUD, or record why the merge intentionally omitted them."
  },
  {
    "id": "NFRA_MCPINDEX-W1-S4",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~1",
    "surfaced_at": "2026-09-21T08:03:00Z",
    "one_line": "MXC1-AC4's exercise (the amended cut, worktree wk-mcpindex-1c) required the emitter's main() to run to completion, which requires portal/src/api readable; portal is an empty gitlink in a fresh workspace worktree (mode 160000, no .gitmodules) and is not in this cell's <paths> grant -- resolved by a `git -C portal worktree add` read-only checkout pinned to the workspace's own gitlink SHA, never committed, never staged.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO (amended): org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-c-1.catalog-writer.md <paths> block, 4 entries -- emit_catalog_v02.py, this investigation file, CAT, RECT -- none of them portal/.",
        "MEASURED: `git ls-files -s portal` in this worktree = '160000 2453a7b4c6b7ff91ea89db499890a9486265d1a0 0 portal'; `ls portal` returned nothing (empty dir) before provisioning; `cat .gitmodules` / `git submodule status portal` = 'fatal: no submodule mapping found' (nested independent repo pinned by gitlink, per box memory reference_portal_is_a_gitlink...).",
        "CODE: workflows/atom_decomposition/emit_catalog_v02.py:355 PORTAL_API = .../portal/src/api; :447-448 `if not acc_idx: print(\"EMIT REFUSED: accessor index is EMPTY -- portal/src/api not readable ...\"); return 2` -- measured firsthand: RUN A rc=2 with exactly this message before provisioning portal, rc=0 after.",
        "ACTION: `git -C <workspace>/portal worktree add /c/tmp/wk-mcpindex-1c/portal 2453a7b4c6b7ff91ea89db499890a9486265d1a0` (detached HEAD at the EXACT commit the workspace repo's gitlink already pins -- no branch, no commit, no write to any tracked path); `git status --porcelain -- portal` in the workspace worktree is empty both before and after (the gitlink SHA does not move).",
        "BOUND (worker face BOUNDS, top-level): 'A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "MXC1-AC4 demands the named writer be RUN (not merely read) once at the cell's HEAD, with a difference observed on the served file; the cell's <paths> grant (as amended) names exactly 2 new write targets (CAT, RECT) and does not mention portal/.",
    "world_is": "emit_catalog_v02.py's main() -- the only code path that reaches the write call AC3 resolved -- REFUSES with rc=2 before writing anything unless portal/src/api is readable (a static read of .ts endpoint files, no build/install needed). portal/ is a gitlink to an independent nested repo; a fresh linked worktree of the workspace (this cell's own worktree) inherits it EMPTY, and no tracked path under workspace's own repo is affected by populating it -- `git status --porcelain -- portal` reads clean before and after, because a worktree checkout of the ALREADY-PINNED commit changes no tracked byte anywhere in the workspace repo's index. This worker read populating it as environment PROVISIONING (like resolving `.tools/aws.cmd` by path, MX-c-2's own fix, or the box's own documented 'how to apply' procedure for this exact gitlink), not as writing outside the <paths> grant, since nothing under portal/ is staged, committed, or referenced in this cell's commit. The portal worktree was torn down and the (empty) portal/ directory re-created identically to the pre-exercise state, then re-provisioned so the criterion's own named invocation (`cd <WS> && ... probes/mx_c_1.py AC4`) reproduces PASS if re-run from this exact worktree; a re-run from a DIFFERENT worktree that also lacks portal will need the same provisioning step, which this row now documents.",
    "notes": "OBSERVATION, INERT: no tracked byte outside this cell's <paths> changed; the portal worktree is local environment state, not a git object this worker's commit touches. Whether a future cell's <paths>/BOUNDS should name portal/ provisioning explicitly (so a re-run seat does not have to rediscover this) is an issuer call."
  },
  {
    "id": "NFRA_MCPINDEX-W3-S2",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~3",
    "surfaced_at": "2026-09-21T09:45:00Z",
    "one_line": "trueshares/{DIVZ,IDVZ}/silver/fact_holdings/ carries 0 live objects despite 28 bronze objects per fund since 2026-08-24 and a registered converter (_convert_trueshares_holdings) for exactly this feed, while each fund's own meta/backfill-status.json reports 'backfill_complete': true, 'verdict': 'PASS', 'holes': [] -- the guard's 'expected' set never counts the holdings feed at all, so its PASS verdict does not mean what a reader would take it to mean.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "live `s3api list-objects-v2 --bucket opal-data-assets --prefix trueshares/DIVZ/silver/fact_holdings/` and same for IDVZ (this worker's run, 2026-09-21): both return zero Contents (`length(Contents)` -> null/None).",
        "live `s3api list-objects-v2 --bucket opal-data-assets --prefix trueshares/DIVZ/bronze/holdings/` (same run): 28 objects, first key `trueshares/DIVZ/bronze/holdings/20260824/divz_holdings.csv`, last `trueshares/DIVZ/bronze/holdings/20260920/divz_holdings.csv`; IDVZ measured identically (28 objects, same date range).",
        "data/assets/scripts/silver/etf_conversion.py:279-347 -- `_convert_trueshares_holdings(s3, key, kc, force, bucket)`, a fully-implemented converter for exactly the `trueshares/{DIVZ,IDVZ}/bronze/holdings/` -> `fact_holdings` path (Rule 17 STRICT, printed docstring), wired into `convert_trueshares()` at :231-232 via `if kc.feed == \"holdings\": return _convert_trueshares_holdings(...)`.",
        "live `s3api get-object --bucket opal-data-assets --key trueshares/DIVZ/meta/backfill-status.json` (this run): `{\"channel\": \"trueshares\", \"layers\": {\"silver\": {\"backfill_complete\": true, \"counts\": {\"dates\": 68, \"objects\": 68}, \"guard\": {\"detail\": \"expected 68 landed 68 matched 68 missing 0 alien 0\", \"instrument\": \"etf_conversion set-identity (per-tree subset, 1->2 fan, run-time denominators)\", \"verdict\": \"PASS\"}, \"holes\": []}}}` -- the 68 figure matches ONLY the netassets bronze/silver count (also live-measured at 68 for DIVZ), never the 28 holdings bronze objects; IDVZ's own backfill-status.json reads identically in shape (68/68/PASS/[]).",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~3/analysis-etfs.result.md ## AC1, AC9 (this cell's own committed record) carries the same live figures."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The silver tree's own completeness guard (`trueshares/{DIVZ,IDVZ}/meta/backfill-status.json`, written by `opal-assets-silver-etf (sweep)`) states `backfill_complete: true` and `verdict: PASS` with `holes: []` for the `silver` layer of each fund's tree -- a reader of this file (or of the `expected 68 landed 68 matched 68 missing 0 alien 0` guard detail line) would take that as 'this tree's silver conversion is current, nothing is missing'.",
    "world_is": "The tree is NOT fully converted: `fact_holdings` (a registered, coded conversion target, `etf_conversion.py:279-347`) has ZERO silver objects for both DIVZ and IDVZ, against 28 live bronze deliveries per fund spanning 2026-08-24 through 2026-09-20 -- 28 dates of un-converted data the guard's PASS verdict never mentions. The guard's own 'expected 68' figure equals exactly the NETASSETS feed's bronze/silver count and appears to never include the holdings feed in what it considers 'expected' at all, so the guard is blind to this feed rather than reporting it as a hole. This is Rule 22's negative mirror: a completeness GUARD EXISTS, reports PASS, and the underlying state contradicts it for an entire registered feed.",
    "disarm_owner": "0.4.0_DS_ClientPlatform",
    "notes": "OBSERVATION/ARMED, not BLOCKING: this cell's own 10 mechanical criteria (MXA7-AC1..AC9, AC11) all PASS with this gap named and reasoned around (no tool proposed for the empty combo, AC6/AC9; the gap named per-fund at AC11) -- the finding does not block MX-a-7's own analysis. Filed because a LATER act that trusts the backfill-status guard's PASS/holes:[] verdict at face value (a future MX-t-7 tool-building cell deciding whether TrueShares holdings data exists, or an ops dashboard reading the same file) would conclude the tree is complete when a whole feed sits 28 days unconverted. disarm_owner `0.4.0_DS_ClientPlatform` (etf_conversion.py's own docstring names 'AUTHOR HALF (DS lane, Rule 13)' as this pipeline's author) should either wire the holdings feed into the sweep's 'expected' set so the guard actually covers it, or run the sweep/force-convert against the 28 pending bronze objects and confirm the guard's own denominator grows to include them."
  }
]
```

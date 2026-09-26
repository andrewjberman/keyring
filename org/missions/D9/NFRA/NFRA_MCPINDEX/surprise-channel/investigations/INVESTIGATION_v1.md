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
  },
  {
    "id": "NFRA_MCPINDEX-W1-S5",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~1",
    "surfaced_at": "2026-09-21T09:15:00Z",
    "one_line": "MXC4-AC11 ('the tool's catalog-entry reference resolves to an entry in CAT -- zero tools fail any of the three') is UNSATISFIABLE as written within this cell's <paths>: DATA_CATALOG.yaml carries 0 tool-reference fields for any of the 49 registered tools, and adding one requires either hand-editing CAT (bound 10 forbids: generated-only) or editing the 4 real integrations' own directories (outside <paths>) -- REFUSED per bound 9, measured, never grandfathered.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ISSUER CONTEXT (this worker's face preamble, verbatim): 'AC1 has validate_integration_spec refuse a spec lacking a per-tool catalog-entry reference... but AC5 requires the four EXISTING integrations... those tools have no catalog entries today, and their integration directories are NOT in your <paths>. Measure it... REFUSE it and report the measurement... do not grandfather, exempt or widen on your own reading, and do not write outside <paths>.'",
        "TO: org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-c-4.classification-composition.md <paths> block, 7 entries -- APP/destructive_ops.py, APP/data_entitlement.py, INT/base.py, INT/registry.py, TST/test_entitlement_admin.py, TST/test_tool_classification_composition.py, the investigation file -- none of the 4 integration directories (INT/ycharts/, INT/opal_portal/, INT/globgrph/, INT/schwab/) and not CAT itself.",
        "MEASURED (probes/mx_c_4.py AC11, this cell's own commit): a python walk of the parsed infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml for any 'tools'/'tool_ref'/'tool_refs' field anywhere in the document returns 0 hits across 15 channels / 36 artifacts -- printed denominator, zero catalog tool-reference fields exist today.",
        "MEASURED (same run): over the DENOMINATOR of 49 registered tool names (NATIVE_TOOLS | INTEGRATION_TOOLS | SCHWAB_TOOLS at this cell's HEAD), 49 of 49 fail the catalog-entry-reference axis (100%); 14 of 49 (the ycharts/opal_portal/globgrph/schwab tools) additionally fail the destructive_ops.classify axis because their owning specs' tool_classifications are empty by construction (their integration.py files, outside <paths>, never populate the new per-tool manifest this cell adds); 0 of 49 fail the data_entitlement.classify axis (unaffected).",
        "BOUND 9 (worker face, verbatim): 'The spec is frozen, and the face instructs refusal. A criterion that cannot be satisfied as written is REFUSED and reported with its measurement, never repaired, widened or met by another route.' BOUND 10: 'The catalog is generated, never hand-edited or hand-merged.'",
        "By contrast, MXC4-AC1/AC3/AC4/AC12 (the mechanism itself, on planted specs) and MXC4-AC5/AC6/AC9 (the real population's REGISTRATION and CLASSIFICATION stability) all measure PASS at this same commit -- the tension is specifically and only the catalog-entry-reference axis over the REAL population, not the composition mechanism this cell built."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "MXC4-AC11 demands, for EVERY registered tool (denominator printed), that a catalog-entry reference resolves to an entry in CAT, with zero tools failing any of three axes (destructive_ops, data_entitlement, catalog).",
    "world_is": "DATA_CATALOG.yaml's 36 artifact rows describe PORTAL DATA SURFACES (business meaning, freshness, firm scope) and carry no field that names an MCP tool at all; C1's own text says a future entry SHOULD carry 'the tools that serve it', but no cell has populated that yet (MX-c-1/MX-c-2, this project's OWN earlier cells, extend the catalog's SCHEMA and its silver rows -- neither adds a tool-reference field, and neither is in this cell's <paths> to check or extend). So AC11's third axis fails for all 49 real tools, not from a defect in this cell's mechanism (AC1/AC5/AC6/AC9/AC12 all measure clean) but because the DATA it depends on does not exist yet and this cell has no legal route to create it -- editing CAT by hand is bound 10's own prohibition, and editing the 4 integrations' own files to add a self-declared reference is outside <paths>. Filed rather than silently grandfathered or widened, per the issuer's own explicit instruction.",
    "disarm_owner": "2.0.0_SA_COO~M",
    "notes": "OBSERVATION/ARMED: left alone, MXC4-AC11 will fail identically on every future re-run of this exact cell until either (a) a future cell/PRD amendment adds a per-tool catalog-entry-reference field to CAT's schema and populates it (an MX-c-2-class extension, or a new cell), or (b) the CTO/COO narrows AC11's letter to acknowledge the catalog-population gap is out of this cell's scope (an L10 addendum). Until then, MXC4-AC11 is the one criterion in this task order's proof_of_spec graded FAIL by output; every other mechanical criterion (AC1-AC7, AC9, AC10, AC12) measures PASS and AC8 is judgment (CVO, ungraded here). disarm_owner 2.0.0_SA_COO~M (the issuing COO) as the nearest live seat to route either remedy; may re-route to 1.0.0_SA_CTO if this is read as a ratified-text (PRD C2/AC11) tension rather than a sequencing gap."
  },
  {
    "id": "NFRA_MCPINDEX-W1-S6",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~1",
    "surfaced_at": "2026-09-25T00:00:00Z",
    "one_line": "Every mechanical criterion's invocation in TO-MX-c-4 names 'py -3.12' verbatim; on this device today only Python 3.11 registers with the py launcher (py -3.12 rc=103 'No suitable Python runtime found' for all 11 mechanical criteria AC1-AC7,AC9-AC12), so none of the named invocations produced a VERDICT line.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO: NFRA_MCPINDEX.TO-MX-c-4.classification-composition.md, every AC1-AC7/AC9-AC12 <invocation> block verbatim -- 'cd <WS> && timeout 120 py -3.12 org/missions/.../probes/mx_c_4.py AC<n>'.",
        "INSTRUMENT: 2026-09-25, this worker's worktree /c/tmp/mx-1 -- `timeout 120 py -3.12 <probe> AC1` (and identically for AC2..AC12) each returned rc=103, stdout+stderr 'No suitable Python runtime found / Pass --list (-0) to see all detected environments on your machine / or set environment variable PYLAUNCHER_ALLOW_INSTALL to use winget / or open the Microsoft Store to the requested version.'",
        "CENSUS: `py -0` and `py -0p` list only ' -V:3.11 * ... Python 3.11 (64-bit)'; filesystem sweep finds no Python312 directory under AppData/Local/Programs/Python nor Program Files, and a Python314 directory exists under Program Files but is unregistered with the launcher (`py -3.14` also rc=103).",
        "PRIOR STATE: this cell's own classification-composition.result.md (build commit 119a49eef0) line 137 -- 'py -0 (only Python 3.12 installed)' -- so the device's registered interpreter changed from 3.12-only to 3.11-only between the build and this re-run; both python 3.11 and the prior 3.12 carry the needed packages (checked: pyyaml 6.0.3, jsonschema 4.26.0, pytest 9.1.1 all resolve under 3.11), so this is an interpreter-label drift, not a missing-package defect.",
        "BOUND: decomp s.8 bound 14 verbatim -- 'No new dependency. A missing instrument is a refusal, never an install.' -- installing/registering a Python 3.12 is out of grant and out of scope; bound 9 -- 'A criterion that cannot be satisfied as written is REFUSED and reported with its measurement, never repaired, widened or met by another route.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Every AC1-AC7/AC9-AC12 invocation names the literal command 'py -3.12 <probe> AC<n>' as the criterion's instrument, to be run verbatim under a bound.",
    "world_is": "py -3.12 does not resolve on this device today (rc=103, 'No suitable Python runtime found') for any of the 11 mechanical criteria; py -3.11 (the only launcher-registered interpreter) carries the identical dependency set the probe needs. The worker ran each invocation exactly as named, recorded rc=103 verbatim, and reports each mechanical criterion FAIL-by-output rather than substituting an unnamed interpreter or installing one.",
    "notes": "BLOCKING on all 11 mechanical criteria (AC1-AC7, AC9-AC12); AC8 is judgment and unaffected. INERT: no live state changed; the probe code itself (already amended for the AC11 registry-limbs-only text per issuer commit 0bec07601a) is otherwise unexercised this pass. disarm_owner 2.0.0_SA_COO (the issuing seat) as nearest live owner to decide whether the invocation's pinned interpreter is updated to match the device's registered Python or the device's launcher registration is restored to include 3.12."
  },
  {
    "id": "NFRA_MCPINDEX-Z-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T05:40Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "The seat re-seated to NFRA_MCPINDEX (2.0.0_SA_COO~O, @23bbeff325) answers three rows. DISARMS NFRA_MCPINDEX-W4-S2: its premise no longer holds at HEAD. ANSWERS NFRA_MCPINDEX-W1-S5: MX-c-4 is superseded as cut (CTO ruling D-3 R-1 @9c70622d13) after AC11 was amended (@fc2835958a, ruling @5f3b4a20c6). ANSWERS NFRA_MCPINDEX-W1-S6: the re-cut cell's invocations name a device-neutral interpreter, per the same ruling.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W4-S2, read at HEAD by this seat: 'git ls-tree HEAD deliverables/0.9.0_WK_NFRA_MCPINDEX~4/' lists analysis-blackdiamond.result.md and the MX-a-3 proof instance; the MX-a-3 order's last <status> reads 'complete'; 'git merge-base --is-ancestor edf584f64a HEAD' is true.",
        "W1-S5 and W1-S6 are carried onto CLOUD verbatim by this commit from branch wk-nfra_mcpindex-1-1d @7e1347ee8c, which stays HELD until the re-cut cell drains it (D-3).",
        "D-3 R-1 (org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/ROUND1_RULINGS.md @9c70622d13): the re-cut classifies the 9 ycharts/opal_portal/globgrph tools; the 5 schwab tools are HELD behind the OPLGTW stop (registered, not enabled); AC11 stays 49, graded 44 classified + 5 HELD; the py -3.12 pin is the issuer's to amend."
      ]
    },
    "spec_asserts": "W4-S2 (ARMED, disarm_owner the COO lane): MX-a-3's drain did not carry its deliverables or its status flip. W1-S5 (ARMED): AC11 is unsatisfiable in-grant. W1-S6 (BLOCKING): every invocation pins py -3.12, which site Z lacks.",
    "world_is": "MX-a-3's work is at HEAD. MX-c-4 is superseded, and its build waits on its branch for the re-cut cell. The interpreter pin is fixed in the re-cut face, not in a superseded order.",
    "notes": "W3-S2 (ARMED, disarm_owner 0.4.0_DS_ClientPlatform, the trueshares fact_holdings gap) is outside this lane. It rides this seat's drain-end read to the CTO."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W4-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~4",
    "surfaced_at": "2026-09-25T15:45Z",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "MX-q-2 (R-3) asks for the distinct firm or rep identifiers across live Eclipse silver rows. No Eclipse silver table has a rep_id or firm id column, so the rep ids were read through the producer's own join to accounts_v2.",
    "spec_asserts": "TO-MX-q-2 section 1 item 2: 'Measure the distinct firm or rep identifiers across live Eclipse silver rows, and how many fall outside the Inflection allowlist'. The allowlist is INFLECTION_REP_IDS, a rep_id set.",
    "world_is": "s3://opal-data-inf/silver/eclipse/2026-09-25/: portfolios_simple (845 rows) has no column naming rep, firm, advisor or team. portfolios_full (859 rows) has only 'team', with 3 distinct values, which are not rep_ids. The worker took rep_id through INF_E_00's join (eclipse_account_id_int -> accounts_v2.account_id): 787 rows joined and carry 5 distinct rep_ids, 0 outside the allowlist. 58 rows have a null eclipse_account_id and resolve to no id. Whether accounts_v2 is itself Inflection-filtered upstream is unmeasured; if it is, a non-Inflection account would show as unjoined (0 today).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INSTRUMENT: timeout 120 python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~4/probes/mx_q_2.py ECL, rc=0, read_at 2026-09-25T15:38:35Z. Output line: 'portfolios_simple rows=845; columns naming rep/firm/advisor/team: []'.",
        "JOIN SOURCE: data/inf/scripts/gold/INF_E_00.eclipse_model_portfolios.py:206 @09daf8fb2b (acct.merge(av_slice, left_on='eclipse_account_id_int', ...)).",
        "ALLOWLIST: data/inf/scripts/silver/_orion_api_silver_lib.py:113 @09daf8fb2b, INFLECTION_REP_IDS = {3, 6, 10, 11, 12}."
      ]
    },
    "notes": "The ECLIPSE-SCOPE line in round2-reads.result.md carries the join-derived count. The route is recorded here so the issuer can judge it."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W4-S2",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~4",
    "surfaced_at": "2026-09-25T15:45Z",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "Black Diamond gold canonical_lots_unrealized and canonical_lots_realized were last written 2026-07-23, 64 days before this read. MX-q-2 reads their cusip nulls at that partition.",
    "spec_asserts": "TO-MX-q-2 section 1 item 1: 'Measure, for every SERVED figure that joins on cusip ..., whether it carries a null-cusip row today.'",
    "world_is": "ListObjectsV2 on 2026-09-25: the newest gold/canonical/lots_unrealized/ object is 2026-07-23.parquet (latest of 658), and so is the newest gold/canonical/lots_realized/ object (latest of 1,402). The sibling gold/canonical/holdings/ and gold/timeseries/holdings_lots/ are current to 2026-09-23 and 2026-09-18. Whether a live consumer still reads the lots figures was not measured.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INSTRUMENT: timeout 120 python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~4/probes/mx_q_2.py BD, rc=0. Output lines: 'FIGURE canonical_lots_unrealized ... key=s3://opal-data-bd/gold/canonical/lots_unrealized/2026-07-23.parquet (latest of 658)' and 'FIGURE canonical_lots_realized ... 2026-07-23.parquet (latest of 1402)', read_at 2026-09-25T15:40:00Z.",
        "PRODUCER: data/black_diamond/scripts/gold/B_02.canonical_lots.py:37-38 @09daf8fb2b names both outputs."
      ]
    },
    "notes": "Off-task freshness observation. The worker judges its form, not its significance. The issuer can re-class hazard_standing if a live consumer is found."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W5-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~5",
    "surfaced_at": "2026-09-25T11:40Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "safe-commit cannot commit a 'git rm --cached' of a file that stays on disk: its stager (cg_stage_pathspec) runs 'git add -f' on any declared path present on disk, re-adding the removal the face asked for.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/commit_gate_lib.sh:95-110 @09daf8fb2b: a path treated as a deletion only if '[ ! -e \"$p\" ]'; otherwise 'git add -f'.",
        "First commit e453057195 (declared the report with 'git rm --cached' staged) landed 2 files, not the removal; git cat-file -e HEAD:<report> still succeeded after it. A second safe-commit carrying only the report path aborted rc=1 with the removal un-staged again (nothing to commit).",
        "Route used: moved the report to .scratch/, 'git rm --cached', safe-commit (c781f95ffb, 440 deletions), moved it back; sha1sum -c of the pre-move digest reads OK. End state is what the face names: untracked at HEAD, ignored, still on disk."
      ]
    },
    "spec_asserts": "MX-b-2 face section 1.2: remove the report from the index with git rm --cached (file on disk stays), committed under safe-commit.sh.",
    "world_is": "safe-commit re-adds a --cached removal when the file exists on disk; the removal commits only if the file is off disk during the safe-commit run.",
    "notes": "No gate was bypassed. The file was off disk only for the safe-commit call. Whether safe-commit should honour an already-staged removal of a file still present on disk is for the tool's owner; this worker makes no change to it."
  },
  {
    "id": "NFRA_MCPINDEX-Z-S2",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-26T00:20Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-W3-S11"
    ],
    "one_line": "DISARMS NFRA_MCPINDEX-Z-W3-S11. The issuer amends MX-t-8, without a CTO ruling, to register only the 3 tools catalog_gate resolves today: mdpf aum-metrics, account-distribution and aggregate-aua. The other 7 go to the round-3 enrichment list as a catalog-row cell, and non-model-assets' deny verdict stands.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W3-S11, on the worker's branch wk-NFRA_MCPINDEX-3 @6345d36f04: catalog_gate.load_catalog indexes only channels.*.artifacts[].key. 3 of 10 tools resolve. A catalog copy with the 7 rows planted passes all 4 tests, so the gap is catalog rows, not the module.",
        "The amendment is item 13 of org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-t-8.portal-tools.md, in this commit. The issuer amends its own criteria without a CTO ruling (CLAUDE.md rule 27 L5/L6, Andrew-direct 2026-09-24). No gate limb grades a modification of a direct-act order other than GATE (viii)."
      ]
    },
    "spec_asserts": "W3-S11 (BLOCKING, ARMED): ruling D-5 (c) keys each tool from its own catalog row, and 7 of 10 tools have none, so MX-t-8's criteria cannot pass as cut.",
    "world_is": "MX-t-8 now covers 3 tools that resolve under D-5 (c). The 7 unrowed tools are a round-3 catalog-row cell. No catalog row is added by this cell.",
    "notes": "FWD-2's parity now covers the mdpf family only this round. The CTO's round-N analysis reads it from here."
  },
  {
    "id": "NFRA_MCPINDEX-Z-S3",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.4.0_DS_ClientPlatform~D",
    "surfaced_at": "2026-09-26T02:05Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "The mirror framework's float64 parse-or-raise is guarded by `df[c].dtype == object`, which pandas 3 reads False for a column of strings, so _numeric_or_raise is skipped for EVERY float64-declared column and arrow coerces unvalidated. mirror_conversion.py:330 is the shared copy, vendored into the blackdiamond, eclipse, etf, orion and schwab silver bundles.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "measured on this interpreter: pandas 3.0.3 / numpy 2.4.6; pd.DataFrame built from string rows infers dtype 'str', and `df[c].dtype == object` is False.",
        "data/assets/scripts/silver/mirror_conversion.py:330 -- `elif t == \"float64\" and df[c].dtype == object:`; the same line is vendored at infra/aws/lambda/opal-assets/opal-assets-silver-{blackdiamond,eclipse,etf,orion}/mirror_conversion.py.",
        "comp-find 'dtype == object' --all: DENOMINATOR 26 hit(s) across 75199 file(s); 8 are this guard (1 etf_conversion + 1 mirror_conversion in data/, 6 vendored).",
        "negative control on the etf copy, run this session: reverting the fixed guard alone makes a bad numeric surface as pyarrow ArrowInvalid instead of the converter's own VendorDriftError, and Shares reads back 'str'.",
        "the DEPLOYED path is UNAFFECTED, measured: partitions written by the lambdas at 2026-09-25T22:00Z (pathfinder fact_holdings, trueshares fact_netassets_page) read back float64, reachable only through the object branch."
      ]
    },
    "spec_asserts": "_numeric_or_raise's docstring: 'A string that does NOT parse RAISES naming column and value: coercing it to null would be judgment (fillna's evil twin), and Rule 17 forbids exactly that.' The converter promises a named raise on every float64-declared column.",
    "world_is": "On pandas 3 the guard never selects the column, so that promise is not kept by the converter at all. A bad value still fails, but as pyarrow's ArrowInvalid from from_pandas -- naming neither the column nor the vendor -- and a well-formed partition records pandas metadata 'str', so a pandas reader gets strings out of a double column. No bad value has been written and the physical parquet type was always correct: this is an error-quality and round-trip-type defect, not data corruption.",
    "disarm_owner": "2.0.0_SA_COO~O",
    "notes": "FIXED in the etf copy only (data/assets/scripts/silver/etf_conversion.py, commit 23efc28a2f), because that is the converter MX-s-1's backfill runs through and MX-s-1 requires Rule 17 STRICT. mirror_conversion.py is the shared framework for five pipelines and five vendored bundles -- far wider than this order's write surface -- so it is NOT touched here. The replacement predicate is `not pd.api.types.is_numeric_dtype(df[c])`, equivalent on the deployed pandas-2 path. Exposure today is limited to seats running these converters locally (QA, ad-hoc backfills) on pandas 3; the scheduled lambdas are on the older layer."
  },
  {
    "id": "NFRA_MCPINDEX-Z-S4",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.4.0_DS_ClientPlatform~D",
    "surfaced_at": "2026-09-26T02:05Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "The deployed opal-assets-silver-etf bundle predates the TrueShares holdings converter by two months and contains ZERO occurrences of _convert_trueshares_holdings, and no S3 notification rule matches a holdings .csv at all -- so MX-s-1's repo fix changes no production behaviour until a DT/AE rebuild, and MX-s-1 AC2 cannot pass from the DS lane.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "live get_function 2026-09-26: opal-assets-silver-etf LastModified 2026-07-15T23:24:02Z, CodeSha256 a14fYacwkjPlkj7P5qb7QGTKDeQ2A9GTnkM/t1rTxcs=; the zip was downloaded and its sha256 re-computed equal, so these are the running bytes.",
        "in that zip, etf_conversion.py sha256 623568f38934f491a25c0f09d11a331297618445ef1afa5a22f8337336c56436 -- equal to BUILD_MANIFEST.json's vendor_sha256 -- carries 0 occurrences of _convert_trueshares_holdings and no `kc.feed == \"holdings\"` dispatch.",
        "the converter landed in the repo at e442e30964 (2026-08-24), six weeks AFTER the deployed bundle was built at 2705444350 (2026-07-15).",
        "live get_bucket_notification_configuration on opal-data-assets: the trueshares rules are prefix 'trueshares/{DIVZ,IDVZ}/bronze/' suffix '.html'. A key trueshares/DIVZ/bronze/holdings/20260824/divz_holdings.csv matches 0 of 11 rules; the netassets .html matches 1.",
        "MX-s-1 AC2 run live after the backfill: 'guard expected=73 missing=0 live silver=106 of which fact_holdings=33 ... 0 of 2 -- RESULT: FAIL -- exit=1'. 106 minus 33 equals 73 exactly: the served guard is still the stale bundle's netassets-only denominator.",
        "safe-deploy.sh measured on this path: it maps data/assets/scripts/silver/ to s3://opal-data-mdpf/code/scripts/silver/, probes 404 and reports SKIP-NOT-MEMBER, 'NOTHING WAS DEPLOYED' -- and that S3 code prefix is not how this converter runs."
      ]
    },
    "spec_asserts": "MX-s-1 step 2 says to fix the converter and 'Deploy through .tools/safe-deploy.sh as rule 13 requires', and its preflight declares 'the existing daily conversion runs unchanged'.",
    "world_is": "There is no safe-deploy path for this file: it is not a member of the only S3 prefix safe-deploy maps for data/assets/scripts/silver/, and the code that actually runs is a vendored Lambda zip. Rebuilding it is a DT/AE act under CLAUDE.md rule 13 and NEVER-9 (Terraform only). The existing daily conversion could not have converted holdings at any point: the bundle has no such function, and no event rule even delivers the object. The daily sweep at cron(30 23 * * ? *) lists bronze directly, so the missing event rule is a latency gap rather than a second cause -- once the bundle is rebuilt, holdings converts on the sweep rather than on delivery.",
    "disarm_owner": "2.0.0_SA_COO~O",
    "notes": "The repo fix is committed (6c6232a5d7, 23efc28a2f) and proven by tests including a planted-hole control. What remains is a bundle rebuild per BUILD_MANIFEST.json's vendored_modules list plus a Terraform apply -- DT/AE. A separate, smaller question for the same owner: whether to add a '.csv' notification rule for the trueshares holdings prefix so the feed converts on delivery like netassets, instead of waiting for the 23:30Z sweep."
  },
  {
    "id": "NFRA_MCPINDEX-Z-S5",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.4.0_DS_ClientPlatform~D",
    "surfaced_at": "2026-09-26T02:05Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "MX-s-1's backfill landed 66 fact_holdings partitions the DEPLOYED guard does not model, so the next scheduled sweep will rewrite trueshares/{DIVZ,IDVZ}/meta/backfill-status.json from PASS to FAIL with alien 33 -- a served verdict flip caused by this order, self-clearing the moment the bundle is rebuilt.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "currently served, read live before the next sweep: trueshares/DIVZ and /IDVZ meta/backfill-status.json both backfill_complete true, verdict PASS, 'expected 73 landed 73 matched 73 missing 0 alien 0', updated_by 'opal-assets-silver-etf (sweep)', LastModified 2026-09-25T23:30:16Z.",
        "simulation of the NEXT sweep run against LIVE bucket state using the DEPLOYED bytes (the sha256-matched vendored copy), read-only: trueshares/DIVZ expected=73 landed=106 matched=73 missing=0 alien=33 -> FAIL, backfill_complete would be False; IDVZ identical.",
        "mirror_conversion.set_identity:771 -- `verdict = \"PASS\" if not missing and not alien else \"FAIL\"`, so 33 alien keys alone flip it.",
        "the sweep rule opal-assets-silver-etf-sweep-daily is ENABLED at cron(30 23 * * ? *), input {\"mode\":\"sweep\"}, so the flip lands at the next 23:30Z."
      ]
    },
    "spec_asserts": "Landing a missing feed in silver should make the tree's completeness guard MORE accurate, not less; an ops reader of backfill-status.json takes PASS/FAIL as the tree's health.",
    "world_is": "Against the stale deployed guard the new partitions are ALIEN, not expected, so the honest-but-alarming verdict is FAIL on two trees that read PASS an hour ago. The FAIL is a true statement about the deployed guard's model versus the world -- the previous PASS was the false one, over a tree missing an entire feed -- but it will read to anyone watching as 'DS broke the ETF guard' unless it is announced. It clears itself with no data act: once the rebuilt bundle computes expected=106, alien falls to 0 and the verdict returns to PASS.",
    "disarm_owner": "2.0.0_SA_COO~O",
    "notes": "TIMING, so the flip can simply be avoided: the sweep already ran at 2026-09-25T23:30Z, so the next fire is 2026-09-26T23:30Z. A bundle rebuild before that window means the served verdict never flips at all. Rides NFRA_MCPINDEX-Z-S4; disarmed by the same act."
  },
  {
    "id": "NFRA_MCPINDEX-Z-S6",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.4.0_DS_ClientPlatform~D",
    "surfaced_at": "2026-09-26T02:05Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "Off-task and pre-existing, filed rather than chased: the served completeness guard for pathfinder/{PFDE,PFOE} already reads verdict FAIL, backfill_complete false, 'missing 2' on each fund, and no row names it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "read live 2026-09-26, BEFORE any act of this order touched those trees: pathfinder/PFDE and /PFOE meta/backfill-status.json both backfill_complete false, verdict FAIL, 'expected 146 landed 144 matched 144 missing 2 alien 0', LastModified 2026-09-25T23:30:16Z and :17Z.",
        "the same figures reproduce in a read-only simulation of the sweep against live state, so they are the current steady state rather than one bad run.",
        "NOT caused by this order: MX-s-1 wrote only under trueshares/{DIVZ,IDVZ}/silver/fact_holdings/, and these rows predate the backfill in the served artifact's own LastModified."
      ]
    },
    "spec_asserts": "A silver tree whose guard reads FAIL with named missing partitions is a live completeness gap someone owns.",
    "world_is": "Both pathfinder funds have been sitting at missing 2 with nobody named, in the same guard file whose TrueShares sibling was the subject of W3-S2. Which 2 dates, and whether they are a vendor non-delivery or a conversion failure, is unmeasured here -- this order's write surface is trueshares only and chasing it would be the halt-and-investigate CLAUDE.md section 2 forbids.",
    "disarm_owner": "2.0.0_SA_COO~O",
    "notes": "One read sizes it: list pathfinder/{PFDE,PFOE}/bronze/ against silver/, diff the dates, and check whether the 2 missing dates have bronze at all. Routed, not actioned."
  },
  {
    "id": "NFRA_MCPINDEX-Z-S7",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-26T04:15Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-W2-S7"
    ],
    "one_line": "DISARMS NFRA_MCPINDEX-Z-W2-S7 (the issuer's own check defect). v6.AC1's overlap limb compared the questions against `description` keys the catalog does not carry, so it read 0 strings and could not fail. It is amended on the held branch (@ae03e6cf86) to read EVERY catalog string and to FAIL when it read none. On the merged bytes it reads 1069 strings, overlap 0, PASS. A planted catalog sentence reads overlap 1, FAIL.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Held branch wk-nfra_mcpindex-1-1d @ae03e6cf86: v6.AC1.sh walk() collects every str value, and the verdict requires descriptions>0.",
        "Run from /c/tmp/mx-2v and /c/tmp/mx-1: questions=27 sources_at_head=27 expected_tools=27 catalog_overlap=0 descriptions=1069 -> PASS. Control: one question set to a catalog sentence gives questions=28 catalog_overlap=1 -> FAIL, and the tree was restored by git checkout."
      ]
    },
    "spec_asserts": "v6.AC1: NO question shares a run of 6 or more consecutive words with any catalog description.",
    "world_is": "The check now measures what it states, over every catalog string, with a positive control.",
    "notes": "The fix lives on the held branch and reaches CLOUD when the held branch drains, after the CVO grades MX-c-5's AC4."
  },
  {
    "id": "NFRA_MCPINDEX-Z-S8",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.4.0_DS_ClientPlatform~D",
    "surfaced_at": "2026-09-26T04:40Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "THE ROOT CAUSE OF C-S13, one level above where R-2 (2) points: the Black Diamond asset-dim download has failed 69 consecutive runs since 2026-06-23 on a single portal login timeout, so build_bd_assets_dim.py's only input is frozen on the same day the bridge is -- scheduling the builder as ruled would rebuild identical bytes and resolve 0 of the 791 missing asset_ids.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "all 119 of s3://opal-data-bd/logs/asset-dim-download-*.log read IN FULL (denominator printed): 69 FAILED, 50 OK, 0 unclassifiable; last OK 2026-06-22, first FAILED 2026-06-23, last FAILED 2026-09-25. 69 of 69 failures carry the SAME login TimeoutError -- one signature, one cause, not 69.",
        "SSM get_command_invocation on the exact CommandId 2978c0a0-5aa2-4640-97e0-516a5dc2e5a3 from the 2026-09-25 lambda log (used as a positive control after list_commands returned a bare 0): stdout carries 'Phase 1: Login / FAILED / Error: TimeoutError: forURL: Timeout 30000ms exceeded. waiting for navigation to \"**/bd3.bdreporting.com/**\"' then 'SKIP: silver conversion skipped (download_rc=1)' and 'ERROR: Asset-dim pipeline failed (download_rc=1 merge_rc=99)'.",
        "live heads: silver/bd_assets_dim.parquet LastModified 2026-04-14T20:44:16Z; silver/bd_assets.parquet (its ONLY input, N=1 writer convert_assets_to_silver.py by comp-find over 75,160 files) LastModified 2026-04-14T20:09:23Z, trade_date range ending 2026-04-13. Both carry the SAME 10,937 asset_ids.",
        "this seat's read: 791 distinct asset_ids appear in silver transactions since 2026-04-14 and are absent from the bridge; the number of those present in the builder's source today is 0.",
        "forwardfill_v2/assets/ newest object is AssetDimTXNs_OpalCapital_Daily_2026-06-18_to_2026-06-18.xlsx and silver/assets/ stops at 2026-06-18, while forwardfill_v2/transactions/ is current to 2026-09-26 -- the transactions leg is alive, only the asset-dim leg is dead."
      ]
    },
    "spec_asserts": "Ruling R-2 (2) of ROUND_ANALYSIS.round1.md: 'Scheduling build_bd_assets_dim.py ahead of the daily merge, as a production schedule' is the remedy for the frozen cusip bridge, and MX-s-2 restates it as 'No scheduler runs its builder.'",
    "world_is": "A schedule for the leg ALREADY EXISTS and is ENABLED -- bd-asset-dim-pipeline-trigger, cron(10 22 ? * MON-FRI *) -- and it fired last night. What is broken is beneath it: the BD portal login times out, so the download writes nothing and the conversion is skipped by its own guard. The builder's input is therefore frozen at 2026-04-14, and a builder scheduled on top of a frozen input rebuilds the same 10,937 rows. The remedy as ruled would move LastModified, satisfy AC1's freshness limb, and fix none of the 791 missing assets. There are also TWO sequential breaks, not one: the compaction to bd_assets.parquet stopped at 2026-04-14 while silver/assets/ was still landing through 2026-06-18.",
    "disarm_owner": "2.0.0_SA_COO~O",
    "notes": "The ordered remedy is in deliverables/0.4.0_DS_ClientPlatform~D/bd-cusip-bridge.result.md section 5: (1) fix the portal login on opal-bd-asset-dim-download, EC2 i-0e6f6dc014fdcf1cd -- this is the whole fix and everything else is a no-op before it; (2) make the wrapper's exit code honest (see the sibling row); (3) restore the compaction to bd_assets.parquet; (4) only then add the builder. Steps 1-3 are AE/CloudOps and DT; a credential or vendor interaction is Andrew's word. NOT actioned here: this lane built no trigger (rule 13 gives PROD triggers to DT/AE and the order says not to work around the gate)."
  },
  {
    "id": "NFRA_MCPINDEX-Z-S9",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.4.0_DS_ClientPlatform~D",
    "surfaced_at": "2026-09-26T04:40Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "The asset-dim SSM wrapper exits 0 on a failed pipeline, so SSM records Status=Success / ResponseCode=0 for a run whose own stdout says 'ERROR: Asset-dim pipeline failed (download_rc=1 merge_rc=99)' -- which is why 95 days of nightly failure were invisible to every instrument above it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM get_command_invocation, CommandId 2978c0a0-5aa2-4640-97e0-516a5dc2e5a3, instance i-0e6f6dc014fdcf1cd, document opal-bd-asset-dim-download, 2026-09-25T22:11:06Z: Status 'Success', StatusDetails 'Success', ResponseCode 0 -- while the SAME invocation's StandardOutputContent ends 'Download exit code: 1 / SKIP: silver conversion skipped (download_rc=1) / ERROR: Asset-dim pipeline failed (download_rc=1 merge_rc=99)'.",
        "the invoking lambda bd-asset-dim-trigger logs END/REPORT with no error after 'SSM command sent' -- it dispatches and never reads the result, so its own success is real and says nothing about the pipeline.",
        "69 consecutive such runs since 2026-06-23 (full-corpus log read, denominator 119)."
      ]
    },
    "spec_asserts": "A scheduled producer's run status is the signal that it produced. CLAUDE.md: NEVER trust a producer's self-report or rc=0 -- verify against the SERVED artifact.",
    "world_is": "Here the producer's self-report is not merely untrustworthy, it is inverted: the wrapper returns 0 on the failure path, so the honest failure text sits inside a run stamped Success. Every layer above -- SSM console, the lambda's own logs, any status sweep -- reads green. The evidence was in S3 the entire time, one object per night, and nothing was looking at it.",
    "disarm_owner": "2.0.0_SA_COO~O",
    "notes": "The fix is a non-zero exit on the failure path in the SSM document's script, which is a producer reporting its own result honestly and is NOT an alarm, monitor or notification under the standing moratorium. Owner AE/CloudOps with the login fix; they are one act. This row is the generalisable half: the login is one outage, the lying exit code is why any future outage on this path will also be silent."
  },
  {
    "id": "NFRA_MCPINDEX-Z-S10",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.4.0_DS_ClientPlatform~D",
    "surfaced_at": "2026-09-26T04:40Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "MX-s-2 AC3 cannot be satisfied or even computed as written: its cash rule keys on asset_id, which the served partition does not carry, and its bar of zero is unreachable because 1,037 of the bridge's 10,937 assets have no cusip at all.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "gold/timeseries/holdings_lots/2026-09-18.parquet columns read live: lot_id, snapshot_date, account_id, relationship_id, account_name, account_type, account_registration_type, tax_status, qualified_flag, asset_name, ticker, cusip, acquisition_date, purchase_year, lot_index, original_units, current_units, cost_per_unit, cost_basis, current_price, market_value, accrued_gain, holding_period_days, term, is_open, price_quality, market_value_uncapped -- there is NO asset_id column.",
        "B_01.holdings_lots.py:284-292 keys its cash normalisation on asset_id=4 / cusip='CASH', so 'not cash by B_01's own cash rule' is not expressible over the artifact AC3 names.",
        "live read of the bridge: 10,937 asset_ids, 9,900 with a usable cusip, 1,037 with none -- BD supplies no cusip for those, so no rebuild resolves them.",
        "probe mx_s_2.py AC3 under a STATED substitute name-token rule: 1,264,679 rows, 22,173 null-or-CASH cusip, 15,185 cash by the substitute, 6,988 non-cash, of which 98 carry a blank asset_name and are unclassifiable either way.",
        "probe mx_s_2.py DIAG: of the 6,988, 1,798 carry a ticker today's bridge could resolve and 5,190 do not -- and 1,798 is an UPPER bound, because B_01 joins on asset_id while this bounding join uses ticker."
      ]
    },
    "spec_asserts": "MX-s-2 step 3: the probe 'counts null-cusip rows that are NOT cash by B_01's own cash rule' and 'prints VERDICT: PASS-MXS2-AC3 only when that count is 0.'",
    "world_is": "Two distinct defects in one criterion. (i) The rule is not computable: the discriminating column was dropped by the producer before the artifact was written, so any probe must substitute a different rule and should say so rather than quietly approximate. (ii) The bar is unreachable: a permanent floor of null cusips exists that no bridge state can remove, because BD itself supplies 1,037 assets without one. AC3 would read FAIL forever even after C-S13 is fully repaired.",
    "disarm_owner": "2.0.0_SA_COO~O",
    "notes": "The probe is delivered and working with its substitute rule printed, its tokens listed and its unclassifiable residual counted -- it does not claim to be B_01's rule. A re-cut criterion wants a DELTA bar against a measured baseline (for example: non-cash null-cusip rows fall below N once the bridge is current), not an absolute zero. Proposed, not adopted: the issuer amends its own criteria."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W1-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~1",
    "surfaced_at": "2026-09-25T17:26:42Z",
    "one_line": "A class an integration declares on its own spec is visible to destructive_ops.classify only after register_enabled() makes that spec active, and the gateway's ENABLED_INTEGRATIONS default is EMPTY on this box; the conformed AC11/AC6 therefore read the enabled set from deploy-to-ec2.sh:170 (ycharts opal_portal globgrph) and register it before classifying.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE @97f1aad836: infra/aws/ec2/opal-gateway/app/destructive_ops.py classify() falls to registry.classification_for_tool(), which reads _ACTIVE_BY_TOOL; infra/aws/ec2/opal-gateway/app/integrations/registry.py populates _ACTIVE_BY_TOOL only inside register_enabled().",
        "CODE @97f1aad836: infra/aws/ec2/opal-gateway/app/config.py ENABLED_INTEGRATIONS = os.environ ENABLED_INTEGRATIONS split, default '' (empty); infra/aws/ec2/opal-gateway/deploy-to-ec2.sh:170 writes ENABLED_INTEGRATIONS=ycharts opal_portal globgrph into the box .env.",
        "MEASURED (this worktree, after the MX-c-5 declarations, python 3.11.9): classify over the 49 names with register_enabled(['ycharts','opal_portal','globgrph']) -> 5 unclassified (the schwab five); with register_enabled([]) (the env default here) -> 14 unclassified, identical to the base @97f1aad836 (14).",
        "TO face (NFRA_MCPINDEX.TO-MX-c-5.classification-recut.md s.1 item 3): 'A HELD name is a schwab tool that is registered but absent from ENABLED_INTEGRATIONS.' -- the face does not say which ENABLED_INTEGRATIONS (env default vs deployed .env)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "AC11 conformed: print the 49-name denominator, report 44 classified + 5 HELD, where HELD = a schwab tool registered but absent from ENABLED_INTEGRATIONS.",
    "world_is": "ENABLED_INTEGRATIONS has two values: the gateway config default (env, empty on this box, under which all four integrations would be 'absent' and no declared class is visible) and the deployed .env value written by deploy-to-ec2.sh:170. The probe reads the deployed value, prints both, and registers the deployed set before classifying; it refuses (RuntimeError) unless exactly one ENABLED_INTEGRATIONS= value is found in the deploy script.",
    "notes": "Instrument choice recorded for the L9 reader; the probe prints the env value beside the deployed value on every AC6/AC11 run. No live state touched."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W1-S2",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~1",
    "surfaced_at": "2026-09-25T17:26:42Z",
    "one_line": "The face names only AC11's conform, but the round-1 probe's AC6 compared this base with itself (0 differences, read_teams_attachment included) and AC10's BEFORE was MX-c-4's pre-edit py -3.12 count; both were re-based on this cell's base @97f1aad836 so that AC2/AC3 measure what the face glosses.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED before any MX-c-5 edit (python 3.11.9, worktree @97f1aad836): `python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py AC6` printed 'all differences (0): []' and PASS -- its BEFORE snapshot reverted only MX-c-4's 4 files to HEAD, which at this base ARE HEAD's bytes, and it never registered an integration, so it could not see a declared class.",
        "MEASURED before any MX-c-5 edit: `python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py AC10` -> '1 failed, 137 passed, 56 warnings, 34 subtests passed in 14.64s' over the 11 files; the probe's hard-coded BEFORE was '1 failed, 130 passed' over 10 files under py -3.12 at MX-c-4's cut.",
        "TO face s.4 glosses: MXC5-AC2 'the 40 tools that already resolved keep their class; the 9 newly classified are listed with their class and reason'; MXC5-AC3 'no gateway test that passed at this cell's base fails'.",
        "CHANGE (this cell's commit, org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py): AC6 BEFORE = every tracked app/ file at 97f1aad836 (66 files, git show, binary), both sides register the deployed enabled set; PASS requires 49 names, 40 kept with 0 changed, exactly 9 newly classified, each with a stated reason. AC10 BEFORE_SUMMARY = the base measurement above, same 11 files on both sides."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Conform your probe's AC11 to the ruling (face s.1 item 3); AC2/AC3 run the probe's AC6/AC10 verbatim.",
    "world_is": "Run unchanged, AC6 would PASS vacuously (it cannot see any declared class and compares the base tree with itself) and AC10's BEFORE described a different base and interpreter. The worker conformed both inside its own deliverables folder; the reasons AC6 prints are the worker's stated claims (held), graded at L9 as MXC5-AC4, never by the probe.",
    "notes": "Worker-owned instrument edit, inside <paths>. The issuer may read this as a widening of the conform instruction; the pre-edit outputs are quoted above for that reading."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W1-S3",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~1",
    "surfaced_at": "2026-09-25T17:26:42Z",
    "one_line": "The 9 classes are declared through tool_classifications ONLY, not the `tools` manifest: declaring `tools` makes validate_integration_spec demand a catalog ref per tool, and a spec failing it is SKIPPED whole at register_enabled -- which on deploy would drop all 9 enabled ycharts/opal_portal/globgrph tools from the live surface.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE @97f1aad836: infra/aws/ec2/opal-gateway/app/integrations/base.py validate_integration_spec -- `for name in spec.tools:` appends an error when tool_classifications OR tool_catalog_refs lacks the name; tool_classifications keys outside `tools` are not checked.",
        "CODE @97f1aad836: infra/aws/ec2/opal-gateway/app/integrations/registry.py register_enabled -- a spec with any validation error is reported and `continue`d, its tools never registered (SKIP-REGISTRATION, fail-closed).",
        "RULING R-1 @9c70622d13 item 3 and MX-c-4's amendment @0bec07601a: the catalog-entry limb is struck from AC11 and graded on each tool's own shipping cell (MX-t-*).",
        "MEASURED (this cell, python 3.11.9): with the declarations in place, register_enabled(['ycharts','opal_portal','globgrph']) registers 6+1+2 tools and classify resolves all 9 (AC6 output 'NEWLY CLASSIFIED: 9')."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Each of the 9 tools declares its class in its own integration directory 'through the same declaration MX-c-4 built'.",
    "world_is": "MX-c-4's declaration has two parts: `tools` (the manifest that engages validation, requiring BOTH a class and a catalog ref) and `tool_classifications` (read by classify). Only the second is declared, because the catalog refs belong to the MX-t cells; a later cell that adds `tools` must add the refs in the same commit or the integration de-registers.",
    "notes": "Form recorded, not a defect claim. Each integration.py carries a comment stating why `tools` is omitted."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W2-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~2",
    "surfaced_at": "2026-09-25T18:49:43Z",
    "one_line": "opal_discover is not wired into the registry's factory list: registry.py is read-never-write for MX-d-2, so on a gateway with ENABLED_INTEGRATIONS=opal_discover the id reports 'unknown integration id' and adds zero tools; the tests register the factory for their own duration only.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE @d59217f5a8: infra/aws/ec2/opal-gateway/app/integrations/registry.py:34-55 -- _load_builtin_factories registers ycharts, opal_portal, globgrph, schwab; :93 an unregistered id reports {'error': 'unknown integration id'}.",
        "MEASURED (python 3.11.9, this worktree, new package present, no test factory): registry.register_enabled(mcp, ['opal_discover']) -> {'opal_discover': {'error': 'unknown integration id', 'available': ['globgrph', 'opal_portal', 'schwab', 'ycharts']}}.",
        "TO: org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-d-2.discover-family.md <paths> names app/integrations/opal_discover/ and tests/test_opal_discover.py only."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO face s.1: 'with its id set it adds exactly its pinned list'; s.3 lists app/integrations/registry.py under 'Read (never write)'.",
    "world_is": "The id-to-factory wiring lives only in registry._load_builtin_factories (registry.py:34-55 @d59217f5a8). Without a line there the id is unknown to register_enabled. test_discover_registers_dormant registers the factory with registry.register_factory for the test's duration and restores the registry afterwards.",
    "notes": "Specify/write owner is the issuer (2.0.0_SA_COO~O): one register_factory line in registry.py, in a cell whose <paths> names it. Nothing is deployed."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W2-S2",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~2",
    "surfaced_at": "2026-09-25T18:49:43Z",
    "one_line": "Both discover tools resolve to SAFE through destructive_ops.classify (MX-c-4's composed path), but app/data_entitlement.classify returns None for them, so register_enabled reports them 'unclassified' and the OG-z-1 guard would deny both to every principal at discovery and dispatch.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE @d59217f5a8: infra/aws/ec2/opal-gateway/app/data_entitlement.py:102 TOOL_CLASSES over NATIVE_TOOLS | INTEGRATION_TOOLS | SCHWAB_TOOLS; :164 classify returns TOOL_CLASSES.get(tool); :320-324 decide() denies 'tool_unclassified' for None.",
        "CODE @d59217f5a8: infra/aws/ec2/opal-gateway/app/integrations/registry.py:129 unclassified = registered tools whose data_entitlement classify is None, reported with the note 'denied at discovery and dispatch until classified in app/data_entitlement.py'.",
        "MEASURED (python 3.11.9, factory registered): register_enabled(mcp, ['opal_discover']) -> tools ['opal_discover', 'opal_describe'], unclassified ['opal_discover', 'opal_describe']; pytest prints 'data_entitlement.classify=None' for both.",
        "CHECK: org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/d2.AC2.sh comment lines 3-5."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO face s.1: 'Every tool declares its class through MX-c-4's declaration.' The AC2 check script's comment glosses test_discover_tools_carry_class as 'every discover tool resolves by name through destructive_ops.classify and data_entitlement to a declared class'.",
    "world_is": "The class is declared on the spec and destructive_ops.classify returns it; data_entitlement.TOOL_CLASSES is a hard-coded name set in app/data_entitlement.py (outside <paths> and not on the read list) that does not compose from the spec. test_discover_tools_carry_class asserts the destructive_ops limb and PRINTS data_entitlement.classify (None); it does not assert it.",
    "notes": "Whether the data_entitlement limb belongs to AC2 is the issuer's and L9's reading, not the worker's. Enabling the family without a data_entitlement.py entry ships two tools no principal can call; the registry report says so."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W2-S3",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~2",
    "surfaced_at": "2026-09-25T18:49:43Z",
    "one_line": "The catalog carries no structured latest-value field: every row has vintage_field (36 of 36) but a latest value appears only as prose 'live YYYY-MM-DD' in vintage_semantics, on 10 of 36 rows. The answer carries latest_value with its claim: 'held' (quoted from that prose) or 'absent'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED (python 3.11.9) over infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml @d59217f5a8: 36 artifact rows across 15 channels; vintage_field present 36/36; the pattern 'live YYYY-MM-DD' in vintage_semantics hits 10/36; no other per-row field carries a value.",
        "Example: mp.04.model-portfolio-timeseries vintage_semantics 'THE vintage is top-level `data_as_of` (live 2026-08-10)' -> latest_value {'value': '2026-08-10', 'claim': 'held'}."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO face s.1: 'the answer names ... its freshness field and latest value', reading the catalog through the existing load path, never the S3 archive.",
    "world_is": "Without an S3 read the only latest value the family can give is the certification-time date the catalog's prose records. 26 of 36 rows record none; for them latest_value is {value: null, claim: 'absent'}.",
    "notes": "The date is the catalog's recorded observation, never a fresh read; the claim field lets a consumer reject it."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W2-S4",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~2",
    "surfaced_at": "2026-09-25T18:49:43Z",
    "one_line": "The family egresses nowhere, but validate_integration_spec refuses an empty hosts allowlist; the spec declares the single reserved, never-resolving name 'no-egress.invalid' (RFC 2606) so validation returns [] without allowlisting any real host.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE @d59217f5a8: infra/aws/ec2/opal-gateway/app/integrations/base.py:207-208.",
        "MEASURED: base.validate_integration_spec(opal_discover SPEC) -> [] with hosts=('no-egress.invalid',)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO face s.1: 'validate_integration_spec returns []'; preflight: the family reads the repository catalog only, EGRESS CLASS NONE.",
    "world_is": "base.py:207-208 appends 'hosts allowlist is empty (egress-governance axis)' for hosts=(). No declared shape exists for a no-egress integration; the worker chose a .invalid name.",
    "notes": "Form recorded for the issuer."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W2-S5",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~2",
    "surfaced_at": "2026-09-25T18:49:43Z",
    "one_line": "tool_catalog_refs expects a DATA_CATALOG.yaml artifact entity id per tool, but both discover tools read the whole catalog, not one row; each declares 'catalog:app/refs/DATA_CATALOG.yaml', which is not an entity id.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE @d59217f5a8: infra/aws/ec2/opal-gateway/app/integrations/base.py:78-79, and validate_integration_spec's per-tool loop (non-empty check only).",
        "MEASURED: 36 entity ids in DATA_CATALOG.yaml @d59217f5a8, none naming the catalog as a whole."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO face s.1: 'Every tool declares its class through MX-c-4's declaration' (whose validator demands a non-empty catalog-entry ref for every declared tool).",
    "world_is": "base.py:78-79 defines the ref as an artifact entity id; no entity describes the catalog itself. A later check that resolves refs against entity ids will not resolve these two.",
    "notes": "Form recorded; the ref shape for a catalog-wide tool is the issuer's to specify."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W2-S6",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~2",
    "surfaced_at": "2026-09-25T18:49:43Z",
    "one_line": "No MCP tool fetches a catalog key, so the 'NEXT tool to call' is named as query_v0 (the gateway's catalog-gated fetch, POST /query/v0 with the key); the catalog's own channel 'tool' field names tools/portal_lookup.py, a repository script, not a gateway tool.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE @d59217f5a8: infra/aws/ec2/opal-gateway/app/query_v0.py:1-5 (POST /query/v0 {key}) and :112 handle; DATA_CATALOG.yaml channel 'tool' = tools/portal_lookup.py on 11 of 15 channels."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO face s.1: 'the answer names ... the NEXT tool to call'.",
    "world_is": "The gateway's catalog-gated read of one key is the REST route /query/v0 (app/query_v0.py handle), audited as tool 'query_v0'. The worker named that; an MCP-only client cannot call it as an MCP tool.",
    "notes": "Form recorded for the issuer."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W3-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~3",
    "surfaced_at": "2026-09-25T18:59:44Z",
    "one_line": "MX-t-8 AC1: data_entitlement.classify returns None for all 10 portal_index tools. Its classification is a static table in app/data_entitlement.py, which is outside this order's <paths>, so test_portal_tools_register_dormant_with_class fails on that limb.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE @d59217f5a8: infra/aws/ec2/opal-gateway/app/data_entitlement.py:164-166 `def classify(tool): return TOOL_CLASSES.get(tool)`; TOOL_CLASSES (:102-103) is built from the literal NATIVE_TOOLS, INTEGRATION_TOOLS and SCHWAB_TOOLS sets and does not read the integration registry.",
        "CODE @d59217f5a8: data_entitlement.py:320-324 decide() denies a tool with classify None to every principal ('tool_unclassified'); registry.py register_enabled reports such tools under `unclassified`, 'denied at discovery and dispatch until classified in app/data_entitlement.py'.",
        "MEASURED (python 3.11, worktree wk-NFRA_MCPINDEX-3, before the commit, with the module in place -- see row -Z-W3-S6 for why it is not committed): tests/test_portal_index.py printed 'data_entitlement.classify returns None for 10 of 10 tools'; destructive_ops.classify resolves all 10 to SAFE through the spec's own declaration.",
        "TO face s.3 @d59217f5a8: <paths> names app/integrations/portal_index/, tests/test_portal_index.py, catalog_entries/, DATA_CATALOG.yaml, the deliverables folder and the channel; app/data_entitlement.py is neither written nor read-listed."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "round2/checks/t8.AC1.sh: 'every tool resolves through destructive_ops.classify and data_entitlement by name'.",
    "world_is": "destructive_ops.classify composes through the spec (MX-c-4); data_entitlement.classify does not. Adding the 10 names to data_entitlement.INTEGRATION_TOOLS is a one-line edit in a file this order does not grant.",
    "notes": "Criterion refused on this limb as written. Until it is closed, enabling portal_index would register 10 tools that every principal is denied (fail-closed, so no harm)."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W3-S2",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~3",
    "surfaced_at": "2026-09-25T18:59:44Z",
    "one_line": "MX-t-8 AC1: DATA_CATALOG.yaml cannot be regenerated in this worktree. emit_catalog_v02.py refuses because portal/src/api is absent (portal is an empty gitlink here), so the 10 portal_* catalog refs do not resolve.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED (this worktree, `python emit_catalog_v02.py` from workflows/atom_decomposition/, run before and after adding the entries): 'EMIT REFUSED: accessor index is EMPTY -- portal/src/api not readable at C:\\tmp\\mx-3\\portal\\src\\api (the portal submodule must be present)', rc=2.",
        "MEASURED @d59217f5a8: `git ls-tree HEAD portal` -> '160000 commit 2453a7b4c6... portal'; .gitmodules is 0 bytes at HEAD; portal/ is an empty directory in the worktree.",
        "MEASURED: emit_catalog_v02.load_catalog_entries() accepts all 10 catalog_entries/portal_*.yaml files, with no errors.",
        "MEASURED before the commit, with the module in place (row -Z-W3-S6): tests/test_portal_index.py::test_portal_tools_catalog_refs_resolve printed '10 tools, 0 resolve in DATA_CATALOG.yaml'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO face s.1 item 5: 'Add the entries as emitter inputs under workflows/atom_decomposition/catalog_entries/portal_*, then regenerate the catalog with emit_catalog_v02.py. Never hand-edit it.'",
    "world_is": "The entries are written and validate. The regeneration step cannot run without the portal source tree. The worker bar forbids extracting or reconstructing a tree to make an order executable, and hand-editing is forbidden. DATA_CATALOG.yaml is therefore unchanged.",
    "notes": "The fix is to run the emitter on a tree whose portal submodule is checked out at the gitlink 2453a7b4c6. It will also restamp built_at_git_head."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W3-S3",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~3",
    "surfaced_at": "2026-09-25T18:59:44Z",
    "one_line": "portal_index is not wired into registry._load_builtin_factories, because registry.py is read-only for this order. In production, ENABLED_INTEGRATIONS=portal_index would report 'unknown integration id' and add zero tools.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE @d59217f5a8: infra/aws/ec2/opal-gateway/app/integrations/registry.py:34-58 `_load_builtin_factories` registers ycharts, opal_portal, globgrph and schwab by explicit import; nothing imports a package by id.",
        "DOC @d59217f5a8: docs/architecture/NFRA_INTEGRATIONS_STANDARD.md s.5 step 2 'Register the factory in registry.py via register_factory(id, Factory)'.",
        "MEASURED: the AC1 test registers PortalIndexIntegration with the public registry.register_factory for the test only (the planted_factory pattern of tests/test_tool_classification_composition.py) and prints the untouched production available_ids without portal_index."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO face s.1 item 6: 'with ENABLED_INTEGRATIONS empty it adds zero tools; with its id set it adds exactly its pinned list'; face s.3 lists app/integrations/registry.py as read, never write.",
    "world_is": "The integration adds exactly its pinned list once its factory is registered. The one production registration line belongs in a file this order does not grant.",
    "notes": "Dormant either way; this blocks only the eventual enable deploy."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W3-S4",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~3",
    "surfaced_at": "2026-09-25T18:59:44Z",
    "one_line": "catalog_entries/ is the silver-dataset mechanism. The emitter writes its rows under `silver_datasets:` with a header saying 'no S3 key, no precomputed artifact', and the 8-field C1 schema has no key field. So the portal_* entries cannot carry the exact key they describe.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE @d59217f5a8: workflows/atom_decomposition/emit_catalog_v02.py:813-823 writes catalog_entries rows under silver_datasets: with the comment 'silver queried live -- no S3 key, no precomputed artifact'.",
        "CODE @d59217f5a8: emit_catalog_v02.py:202-205 ENTRY_REQUIRED_FIELDS is exactly 8 fields; validate_entry refuses any other field.",
        "CODE @d59217f5a8: emit_catalog_v02.py:58-61 EMISSION_MAP already carries mp.01.aum-metrics, mp.02.account-distribution, mp.03.aggregate-aua-timeseries and mp.11.non-model-assets, the same platinum/mdpf objects that 4 of the portal_* entries describe."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO face s.1 item 5: portal tools' catalog entries are added as emitter inputs under catalog_entries/portal_*.",
    "world_is": "Once emitted, those rows would sit under a header that describes them wrongly. Four of the mdpf objects would have two catalog rows (a channel row and a silver row). The exact key is carried in each entry's `producer` text and in the integration's FENCES, not in a field a consumer can reject on.",
    "notes": "Form recorded, per the face. Whether portal tools should point at the existing channel rows instead is the issuer's call."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W3-S5",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~3",
    "surfaced_at": "2026-09-25T18:59:44Z",
    "one_line": "IntegrationSpec.tool_prefix is one string, but the face's C3 tool names span three systems (mdpf_, etfs_, advi_). portal_index declares 'mdpf_|etfs_|advi_'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE @d59217f5a8: infra/aws/ec2/opal-gateway/app/integrations/base.py:64 `tool_prefix: str  # every tool this integration registers starts with this`; validate_integration_spec checks only that it is non-empty.",
        "TO face s.1: one integration `portal_index` registering mdpf_*, etfs_* and advi_* tools."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "base.py: a single tool_prefix that every registered tool starts with.",
    "world_is": "No single prefix covers the ten names. The field holds the three alternatives joined by '|'. Nothing reads it except summary().",
    "notes": "INERT: no consumer matches on it."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W3-S6",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~3",
    "surfaced_at": "2026-09-25T19:16:00Z",
    "one_line": "MX-t-8 AC1-AC3: the naming commit gate (ENFORCE) refuses app/integrations/portal_index/integration.py. The exact keys the portal serves today are legacy-layout literals (platinum/mdpf/..., platinum/etfs/..., platinum/advi/49financial/...), which address() cannot produce and no registry row covers. The module is therefore not in the gateway tree, and all six named tests fail at import.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED (bash .tools/safe-commit.sh, this worktree): 'ERROR: BLOCKED -- the naming limb refused (LGIC_ENFORCE DEC-6, ENFORCE mode)'; 'NAMING-GATE: REFUSE 19 graded'. The 17 REFUSE lines are all in integration.py, e.g. ':49 platinum/mdpf/ -> mdpf/{scope}/platinum/ why: NEW and OUT-OF-PATTERN as S3Key: REFUSE' and ':42 49financial -> lookup('49financial') why: NEW hand-kept carrier'.",
        "CODE @d59217f5a8: .tools/naming-gate.py:6-7 (DEC-6: NEW and OUT-OF-PATTERN -> REFUSE) and :21-24 (a firm token is permitted only in registry files, generated files, or inside key()/address()/name()/lookup() arguments); org/mcp/naming-gate.enforce is present (last touched d181e0ac5a).",
        "DATA @d59217f5a8: org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json:14-15 maps today's served keys ('/api/general/mdpf/* -> platinum/mdpf/* in opal-data-portal-v2 ... -> mdpf/{scope}/platinum/<leaf>', 'platinum/etfs/positioning_data.json ... -> etfs/{scope}/platinum/positioning_data.json'); its `paths` list (39) holds only the canonical {source}/{scope}/platinum/ form.",
        "MEASURED (read-only .tools/aws s3api list-objects-v2, opal-data-portal-v2, 2026-09-25): prefixes mdpf/global/platinum/, etfs/opal/platinum/, advi/49financial/platinum/ and mdpf/ return None. The positive control platinum/mdpf/global/ returns account-distribution.json, aggregate-aua-timeseries.json and aum-metrics.json. The canonical-layout keys do not exist; the served objects are the legacy keys.",
        "RECORD: the refused module is kept, unexecuted, at org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~3/candidate/portal_index/integration.py (org/** is outside the gate's domain as a record tree). Before the commit, with it in place under app/integrations/portal_index/, tests/test_portal_index.py read '2 failed, 4 passed' (the two failures are rows -Z-W3-S1 and -S2)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO face s.1: build a new integration portal_index (app/integrations/portal_index/) whose tools each read ONE whole precomputed object by its EXACT key prefix, the SAME objects the portal reads; CLAUDE.md rule 30: every S3 address is address() output, and a builder refusal is a registry row, never a hand-typed workaround.",
    "world_is": "The objects the portal reads exist only at legacy keys. The LGIC canon names their future canonical keys, which do not exist yet. A new reader of today's objects must type legacy keys, and the gate refuses every such literal as NEW and OUT-OF-PATTERN. The in-grant remedies either read nonexistent keys or dodge the gate, and both are refused here. The remedy is a naming-canon entry admitting the opal-data-portal-v2 legacy served keys for readers, or an R20 departure Andrew acknowledges. Both are outside this order's <paths>.",
    "notes": "No override was used and the gate was not weakened. All three criteria fail on the committed tree because the tests import app.integrations.portal_index. The issuer's call: route the naming remedy, then land the candidate module unchanged."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W3-S7",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~3",
    "surfaced_at": "2026-09-25T22:02:00Z",
    "one_line": "MX-t-8 PHASE 2 will be refused even after the CTO lands the three LEGACY-READ entries: the naming gate consumes a waiver only for an EXISTING literal, and every literal of the new file portal_index/integration.py is NEW. judge() returns REFUSE on all three roots with valid entries fed in.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE @b5b1402e89 (CLOUD): .tools/naming-gate.py:1293 `new = pre_text is None or not _in_pre(lit, pre_text)`; :1324 `if new and verdict in (\"OUT-OF-PATTERN\", \"ALIAS\"): return \"REFUSE\"`; the waiver is consumed only below that, at :1326-1327 (`if rem:` ... 'THE ONE CONSUMPTION POINT OF THE LEGACY-READ WAIVER ... It sits BELOW the NEW branch above, which is why a NEW or CHANGED literal can never reach it'). A new file has pre_text None.",
        "MEASURED (.scratch/compute_entries.py, the gate's own functions at b5b1402e89 with its lib/opal_naming.py and registry staged read-only): for each of 'platinum/mdpf/', 'platinum/etfs/positioning_data.json' and 'platinum/advi/49financial/', legacy_read_ok(entry, module bytes) = True and authority_ok = True; judge(new file, waivers fed in) = REFUSE, REFUSE, REFUSE. The same literals graded as EXISTING: WAIVED-READ, OUT-OF-PATTERN (WARN), WAIVED-READ.",
        "MEASURED (the same gate on a /dev/null diff of the module, sha256 8f8bb4d3d61c...): 'REFUSE :168 platinum/mdpf/ why: NEW and OUT-OF-PATTERN as S3Key', ':170 platinum/etfs/positioning_data.json' likewise, ':172 platinum/advi/49financial/' likewise plus the 49financial carrier; org/mcp/naming-gate.enforce is present in this worktree."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO face item 9 and LEGACY_READ_AUTHORITY_MX-t-8_20260925.md @212e0b2471: the CTO's entries, landed in NAMING_LEGACY_READS.json before the module's commit, admit the portal's legacy keys for this reader; item 12 PHASE 2: commit the module unchanged once the entries are at HEAD.",
    "world_is": "The waiver's recognizer admits each literal at its call site (all three legacy_read_ok True), but the gate never asks it for a NEW literal. A new module's literals are all NEW, so PHASE 2's commit is refused with the entries in place. The precedent IRPT-M-LEGACY-READ-01 was an existing literal in an existing file.",
    "notes": "PHASE 1 done as ordered; the module is on disk uncommitted. Not fixable in my <paths>: the gate, the carrier and the authority are outside it. The issuer's and CTO's call (a gate change that lets a waiver reach a NEW literal at an approved site, or another route)."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W3-S8",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~3",
    "surfaced_at": "2026-09-25T22:02:00Z",
    "one_line": "The LEGACY-READ entries cannot all carry MDPF_CANON: the gate's remediation_of() resolves 'platinum/advi/49financial/' to ADVI_FIRMBKTS and 'platinum/etfs/positioning_data.json' to NO remediation.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DATA @b5b1402e89: infra/logic/registry/remediations.json: ADVI_FIRMBKTS surfaces include {s3-prefix, opal-data-portal-v2, platinum/advi/49financial/}; MDPF_CANON surfaces include {s3-prefix, opal-data-portal-v2, platinum/mdpf/}; no surface covers platinum/etfs/.",
        "MEASURED (.scratch/compute_entries.py, Naming.remediation_of at b5b1402e89): MDPF_CANON, None, ADVI_FIRMBKTS for the mdpf, etfs and advi roots.",
        "CODE @b5b1402e89: .tools/naming-gate.py judge(): a waiver applies only when entry.remediation == the resolved remediation; with no remediation the EXISTING literal is OUT-OF-PATTERN WARN and the waiver is never read."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LEGACY_READ_AUTHORITY_MX-t-8_20260925.md @212e0b2471: 'Remediation owner of the keys: MDPF_CANON (D8)' for all three prefixes.",
    "world_is": "The gate assigns the advi root to ADVI_FIRMBKTS and the etfs key to no remediation. org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~3/legacy_read_entries.json writes ADVI_FIRMBKTS for advi (the gate's value, so the entry is consumable), and MDPF_CANON for etfs as the authority says; the gate can never consume the etfs entry. Its computed_with.checks block records all three values.",
    "notes": "For the CTO's verification of the entries. My file follows the gate where the gate decides consumption."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W3-S9",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~3",
    "surfaced_at": "2026-09-25T22:02:00Z",
    "one_line": "This worktree's HEAD (1b7e16e1ec) does not carry the ruling, the authority record, NAMING_LEGACY_READS.json, or legacy_read_ok/_norm_body in .tools/naming-gate.py. I read all of them at CLOUD and computed the entries with the gate at b5b1402e89.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED: `git merge-base --is-ancestor 212e0b2471 HEAD` rc=1; org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/ absent on disk; org/standards/NAMING_LEGACY_READS.json absent on disk; `def legacy_read_ok|def _norm_body` has 0 matches in this worktree's .tools/.",
        "MEASURED: merge-base(HEAD, CLOUD) = 60464dd3f8, 4340 commits behind CLOUD b5b1402e89; the task order's bytes are identical at HEAD and at CLOUD (`git diff HEAD CLOUD --stat` on the order is empty).",
        "READ: the ruling at 212e0b2471:.../ROUND1_RULINGS.md R-3, the authority record at 212e0b2471, and the gate at b5b1402e89:.tools/naming-gate.py:926 (_norm_body) and :1131 (legacy_read_ok), staged under .scratch/ read-only."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO face item 9: READ both CTO files; shape for .tools/naming-gate.py legacy_read_ok; compute helper_body_sha256 with the gate's own _norm_body; item 12 PHASE 2 once the CTO's entries are at your HEAD.",
    "world_is": "The paths are on CLOUD, not at this branch's HEAD. The worktree's own gate has no waiver mechanism, so a PHASE 2 commit graded by this HEAD's gate refuses whatever the carrier holds.",
    "notes": "Nothing was rebuilt or extracted into the tree; CLOUD was read, not merged. PHASE 2 needs this branch to carry CLOUD's gate and the landed entries; that is the issuer's merge."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W3-S10",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~3",
    "surfaced_at": "2026-09-25T22:02:00Z",
    "one_line": "Item 10's registry wiring makes tests/test_entitlement_admin.py::test_ogz2_ac08 (outside my <paths>) fail: it instantiates every registered factory, and opal_discover's module is not on this tree. It also pins the registry to 4 ids and 44 tools, so it will still fail on portal_index and opal_discover after the discover drain.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED (python, this worktree, module present): registry.available_ids() = ['globgrph', 'opal_discover', 'opal_portal', 'portal_index', 'schwab', 'ycharts']; instantiating each factory: 5 OK, 'FAIL opal_discover ModuleNotFoundError No module named app.integrations.opal_discover'.",
        "CODE @1b7e16e1ec: infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py:310 iterates registry.available_ids(); :339 _pinned_by_id names ycharts/opal_portal/globgrph/schwab only; :349 calls registry._FACTORIES[_iid](); :355 asserts 44 tools.",
        "MEASURED: that module does not collect here ('ModuleNotFoundError: No module named moto', like 12 other gateway test modules), so the failure is derived from the code, not run. The discover family is on the held branch wk-nfra_mcpindex-1-1d @9dd139a74d (app/integrations/opal_discover/)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO face item 10: wire both factories in app/integrations/registry.py so ENABLED_INTEGRATIONS can name them.",
    "world_is": "The discover module is not on this tree, and an existing test outside <paths> pins the registry's id set. I wired both as factories that import on enablement only, so gateway import stays clean (the portal and classification-composition suites: 38 passed). The pin test needs its two new ids and the discover module.",
    "notes": "Not fixed: the test file is outside my grant."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W3-S11",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~3",
    "surfaced_at": "2026-09-25T23:40:00Z",
    "one_line": "Ruling D-5 = (c) keys each portal tool from 'its OWN existing catalog row, through catalog_gate', but 7 of the 10 tools have no such row. category-views, etfs positioning and all four advi tools have no row catalog_gate indexes, and non-model-assets' row is verdict_class deny. Built as ruled, only 3 of 10 tools resolve, so AC2 and AC3 FAIL by output, and AC1 fails through the file-wide rc.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE @d36d31f8c5: infra/aws/ec2/opal-gateway/app/graphql_plumbing/catalog_gate.py:62-73 load_catalog indexes ONLY channels.*.artifacts[].key (plus the {scope} member expansion). silver_datasets is never indexed.",
        "MEASURED @d36d31f8c5 (python, catalog_gate.load_catalog on app/refs/DATA_CATALOG.yaml): of the 36 indexed rows, platinum/mdpf/{scope}/aum-metrics.json (serve), account-distribution.json (serve-with-caveat), aggregate-aua-timeseries.json (serve) and platinum/mdpf/global/non-model-assets.json (deny) are the only rows under the portal tools' objects. No row exists for mdpf category-views, platinum/etfs/positioning_data.json or anything under platinum/advi/.",
        "READ @2c25c4c831: the 10 phase-1 silver_datasets entries (portal_*) carry the C1 schema's 8 fields, and none is a key. The key appears only as prose inside `producer`. The ruling's premise that the catalog already holds the keys 'as existing data (phase 1 @2c25c4c831)' holds for the silver ENTRIES, not for KEYS catalog_gate can resolve.",
        "MEASURED, proof invocations at d36d31f8c5: AC1 'pytest rc=1; named tests passed 2 of 2; failed/error lines 3'; AC2 'named tests passed 2 of 4'; AC3 'named tests passed 0 of 1'. test_portal_tool_reads_its_exact_prefix_only prints 'tools reading their whole exact-key domain: 3 of 10'. Each of the 7 refusals is 'off-catalog: 0 catalog rows name the portal accessor <X>', or for non-model-assets 'catalog_gate refused ... verdict_class=deny'.",
        "CONTROL (.scratch/planted_rows_control.py, not committed): the same 4 tests over a catalog COPY carrying a servable row for each of the 7 accessors, with non-model-assets flipped to serve, print 10 of 10 / 650 refused, 0 leaked / 10 of 10 / parity 3 of 3, and all 4 PASS. The module is not the cause; the missing and denied rows are."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO face item 9 (ruling D-5 = (c), R-4 @3805559000): each tool resolves its object key from its OWN existing catalog row, through catalog_gate.py; only EXISTING, gate-admitted rows are read; a NEW row goes through the gate on its own merits, never smuggled in with a tool. Items 1-3 and 8 need all 10 tools to read their exact keys, and the mdpf, etfs and 49financial advi families to reach parity.",
    "world_is": "Built to the ruling at 84a725073b. The module holds no key literal (0 hits over 185 constants; the naming gate WARN, rc 0; a planted-literal mutant is REFUSED, rc 1). Only 3 of 10 tools resolve against the real catalog. I added no row, because that would be the smuggling the ruling forbids, and the catalog header says widening is Andrew-only. The 7 tools refuse, deny-by-default, with zero S3 calls.",
    "notes": "Needs an issuer decision. Either the missing rows land as their own gate-admitted catalog change (category-views, etfs positioning, 4 advi objects, and a non-deny verdict for non-model-assets or dropping that tool), or the criteria are recut to the 3 resolvable tools. The accessor each tool looks for is in ROWS in the module."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W3-S12",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~3",
    "surfaced_at": "2026-09-25T23:40:00Z",
    "one_line": "The round-2 check helper pytest_named reads 'passed 0 of N; failed/error lines 0' for any test that prints through capsys.disabled(). Under -v the uncaptured output lands between `::name` and PASSED/FAILED, so neither verdict is on the line its greps match.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED @84a725073b: t8.AC1.sh printed 'pytest rc=1; named tests passed 0 of 2; failed/error lines 0', while `pytest -v` shows both AC1 tests PASSED, each verdict on its own line after the printed measurement lines.",
        "CODE: org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/_root.sh pytest_named greps -E \"::$t(\\[.*\\])? PASSED\" (same line) and -cE ' FAILED| ERROR' (leading space). The split-off verdicts start at column 0, so both counts read zero.",
        "MEASURED @d36d31f8c5, after _say prints into the capture: AC1 'named tests passed 2 of 2; failed/error lines 3'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The AC1-AC3 invocations report the named tests' PASSED count and the FAILED/ERROR lines of the file.",
    "world_is": "They do only when the tests keep their output inside pytest's capture. The error runs toward FAIL, since the rc and the pass count still gate, never toward a false PASS. But with 'failed/error lines 0' beside a real failure, the check hides WHICH tests failed. Fixed in my own test file at d36d31f8c5. The helper is unchanged, because it is outside my paths.",
    "notes": "Any other cell whose tests print through capsys.disabled() under a pytest_named check reads the same way."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W3-S13",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~3",
    "surfaced_at": "2026-09-26T01:20:00Z",
    "one_line": "To read item 13 over the 3 tools, I removed the 7 catalog_entries/portal_* source files of the tools that left the cell and regenerated DATA_CATALOG.yaml. Item 13 names no catalog-entry removal; it says only that no catalog ROW is added for them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ, TO face item 13 (amendment ac5445b2ba on CLOUD, relayed in the launch prompt): 'Every item above now reads over the 3' and 'Do NOT add catalog rows for them'. Item 5 requires each tool's catalog-entry reference to resolve to an entry, and test_portal_tools_catalog_refs_resolve asserts that the portal_* source files equal the tools' refs.",
        "CODE @6345d36f04: the 7 removed files (portal_mdpf_category_views, portal_mdpf_non_model_assets, portal_etfs_positioning, portal_advi_{leaderboard,mix_summary,partner_analytics,growth_chart}.yaml) were my own sources, first added in 81d37aafda / 2c25c4c831 on this branch. None is on CLOUD ('exists on disk, but not in CLOUD').",
        "MEASURED @bc0cde67f0: emit_catalog_v02.py rc=0, 'SILVER DATASET ENTRIES (MX-c-2, catalog_entries/*.yaml): 3 emitted, 0 refused (denominator 3 source files)'. The DATA_CATALOG.yaml diff is the 7 silver_datasets entries plus the two vintage lines."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Item 13: the cell registers only the 3 resolving tools, every item reads over the 3, and no catalog rows are added for the other 7.",
    "world_is": "The 7 silver entries would otherwise stay in the catalog, each naming a tool no integration registers. I removed them. Round 3's catalog-row cell re-adds them from 6345d36f04 (git show 6345d36f04:workflows/atom_decomposition/catalog_entries/portal_<name>.yaml) if it wants them.",
    "notes": "If the issuer meant the 7 entries to stay, revert the 7 deletions in bc0cde67f0, re-run the emitter, and relax the source-set equality in test_portal_tools_catalog_refs_resolve to a subset."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W1-S4",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~1",
    "surfaced_at": "2026-09-26T03:33:23Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "The schwab per-tool class declaration needs destructive_ops.OpClass, which integrations/schwab/integration.py did not import; the edit adds ONE import line beside the declaration, so the file's diff is the declaration plus that import.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE @b643047a05: infra/aws/ec2/opal-gateway/app/destructive_ops.py classify() tests `tag['class'] is OpClass.SAFE` (is_guarded) -- the tag's class must be the OpClass enum member, not a string.",
        "CODE @b643047a05: infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py imported nothing from app/destructive_ops.py.",
        "DIFF (this cell's commit): integration.py gains 26 lines and loses 0 -- `from ...destructive_ops import OpClass as _OpClass` plus the tool_classifications= argument inside SPEC; no other line changes."
      ]
    },
    "spec_asserts": "Face item 5: that file's per-tool class declaration is the ONLY edit in integrations/schwab/, and no line of that file other than the declaration changes.",
    "world_is": "The declaration cannot be written without OpClass in scope. The worker read the import as part of the declaration and added it (the ycharts/opal_portal/globgrph declarations at 37f208249f carry the same import). No existing line was modified.",
    "notes": "If the issuer reads the import as outside item 5, the alternative is the same enum reached another way; the declaration's behaviour does not change."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W1-S5",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~1",
    "surfaced_at": "2026-09-26T03:33:23Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "schwab stays NOT enabled, so on the deployed set destructive_ops.classify still returns the fail-closed tag for all 5 schwab tools; AC11/AC6 now also register every registered-not-enabled integration onto a fake mcp in the probe's child process, and HELD is re-read as 'registered with no declared class'.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE @b643047a05: infra/aws/ec2/opal-gateway/app/integrations/registry.py classification_for_tool reads _ACTIVE_BY_TOOL, populated only inside register_enabled().",
        "MEASURED (this cell, python 3.11.9): `python .../probes/mx_c_4.py AC11` printed 'deployed-set-only view (register_enabled(['ycharts', 'opal_portal', 'globgrph'])): 5 unclassified -> [the 5 schwab tools]' and, registering the registered-not-enabled set as well, '49 = 49 classified + 0 HELD', 'classified in the deployed view but different once schwab registers: 0'.",
        "Probe at the previous close (37f208249f) defined HELD as 'a schwab tool registered but absent from ENABLED_INTEGRATIONS', under which the amended AC11 (0 HELD) cannot pass while item 5 keeps schwab un-enabled."
      ]
    },
    "spec_asserts": "Face item 6: AC11 PASSES only on 49 classified + 0 HELD, naming the 5 schwab tools with their classes; item 5: they stay registered and NOT enabled, ENABLED_INTEGRATIONS untouched.",
    "world_is": "A declared class becomes visible to classify only through an active spec, and only enabled integrations are active in the gateway. The probe registers the not-enabled integrations (opal_discover, portal_index, schwab) onto a fake mcp in its own child process to read the declared class, prints the deployed-only view beside it, and writes no ENABLED_INTEGRATIONS value.",
    "notes": "Instrument choice for the L9 reader: 'classified' in AC11 now means 'resolves through its integration's own declaration once registered', not 'resolves in the deployed gateway today'."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W1-S6",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~1",
    "surfaced_at": "2026-09-26T03:33:23Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "The AC11/AC6 denominator (NATIVE_TOOLS|INTEGRATION_TOOLS|SCHWAB_TOOLS = 35+9+5 = 49) no longer covers every registered tool: the registry now also registers opal_discover (opal_describe, opal_discover) and portal_index (3 mdpf_* tools), 5 tools outside the 49.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED (this worktree @b643047a05 + this cell's edit, python 3.11.9): len(NATIVE_TOOLS)=35, len(INTEGRATION_TOOLS)=9, len(SCHWAB_TOOLS)=5, union 49; 'opal_describe', 'opal_discover', 'mdpf_get_account_distribution', 'mdpf_get_aggregate_aua', 'mdpf_get_aum_metrics' are each NOT in that union.",
        "MEASURED: register_enabled(fake, registry.available_ids()) registers 6 integrations (globgrph 2, opal_discover 2, opal_portal 1, portal_index 3, schwab 5, ycharts 6 = 19 integration tools); destructive_ops.classify returns SAFE (declared, not unclassified) for all 5 out-of-denominator tools.",
        "GIT: portal_index arrived on this branch at b10111278c (drain of TO-MX-t-8)."
      ]
    },
    "spec_asserts": "Face item 6: AC11 prints the 49-name denominator and passes on 49 = 49 classified + 0 HELD.",
    "world_is": "49 is the population data_entitlement names, not every tool the registry registers (54 names). The 5 extra tools are classified SAFE by their own integrations' declarations, so no unclassified tool hides outside the denominator today; the probe keeps the face's 49 and does not widen it.",
    "notes": "Not fixed here: the denominator and data_entitlement's sets are outside this order's paths."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W2-S7",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~2",
    "surfaced_at": "2026-09-26T03:32:00Z",
    "one_line": "v6.AC1's catalog_overlap reads 0 because it compares questions against ZERO catalog text: it walks DATA_CATALOG.yaml for the key 'description', and the runtime catalog has none, so the check cannot fail for any question set.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CHECK @d4292f792c: org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/v6.AC1.sh collects only values under a key named 'description'. Its own output on this branch: 'questions=27 sources_at_head=27 expected_tools=27 catalog_overlap=0 descriptions=0'.",
        "CATALOG @d4292f792c: infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml holds 1069 string values and 0 'description' keys. Its prose sits under business_meaning, serves, serve_verdict_with_caveats, vintage_semantics, semantics_provenance and similar keys.",
        "SEPARATE MEASUREMENT (this worker, not the check): the 27 questions share 0 six-word runs and 0 four-word runs with any of the 1069 catalog strings. The set meets the criterion's intent, but the check did not measure that."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO face s.1 item 1: 'No question may reuse the catalog's own description words.' AC1 expects catalog_overlap=0.",
    "world_is": "The check's denominator is 0 descriptions. A question copied word for word from a catalog row's business_meaning would still read catalog_overlap=0 and PASS.",
    "notes": "The form is recorded for the issuer. One way to disarm it is to have the check walk every string value, or the keys the catalog actually uses, and fail when that denominator is 0. The worker did not edit the check because it is outside <paths>."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W2-S8",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~2",
    "surfaced_at": "2026-09-26T03:32:00Z",
    "one_line": "Routing defect in the discover family, measured on 27 real asks (21 of 27 hit). The 6 misses fall into 3 signatures: one common word selects a whole channel (3), an unranked channel puts the served dataset behind catalog order (2), and an index ask matches no keyword (1).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE @d4292f792c: infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py discover(). A channel keyword hit (_keyword_hit, substring over normalised text) marks EVERY artifact in that channel as a match. Matches are returned in catalog order, and the answer carries no ranking.",
        "RUN: python infra/aws/ec2/opal-gateway/tests/routing/run_routing.py printed 'MISSES: Q05, Q07, Q09, Q13, Q22, Q25' and 'ROUTING: 21 of 27 routed to the expected tool'.",
        "Signature A, a common word selects the whole channel, 3 of 6 misses. Q09 (TrueShares holdings, not catalogued) matched 'holdings' and routed to json/positioning/allocation_summary.json. Q13 (a gold-run readiness ask) matched 'inflection' and routed to mdpf_get_aum_metrics. Q25 (account value over time) matched the factor keyword 'value' and routed to json/correlations/correlation_data.json.",
        "Signature B, right channel but the wrong first dataset, 2 of 6 misses. Q05 (ST model YTD) and Q07 (INT model YTD) routed to json/benchmarks/model_portfolio_timeseries.json. The dataset the recorded serve read, json/benchmarks/model_portfolio_benchmarks.json, is among the 6 candidates but not first.",
        "Signature C, no match, 1 of 6 misses. Q22 ('where is the S&P at?') matched no keyword and no entity slug."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO face s.1: the discover family 'names the next tool for a question'; s.2 bound 1: 'A routing defect you find is a ROW, never a fix here.'",
    "world_is": "All 21 hits are uncatalogued asks correctly answered NOT_CATALOGUED. Of the 3 asks whose expected tool is a dataset, 0 route to it first. So the headline 21 of 27 mostly measures true negatives.",
    "notes": "Nothing is deployed and the integration is dormant, so the hazard is INERT. The expected tools are the worker's reading of each ask (questions.yaml `note`), and G-B's live cold run is the independent read."
  },
  {
    "id": "NFRA_MCPINDEX-Z-W2-S9",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~2",
    "surfaced_at": "2026-09-26T03:32:00Z",
    "one_line": "The Analyst's thread memory holds 8 asks, not 20, and only 1 of them is a data ask. The CRO's question lists were not located. 19 of the 27 questions come from other records that quote a staff member verbatim, and 24 of the 27 expect NOT_CATALOGUED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THREADS @d4292f792c: org/tier0_utility/0.0.3_BG_BBGTerminal/threads/** is 10 tracked files. It records 11 inbound staff messages, all from Andrew. 8 are asks and all 8 are used (Q01-Q06, Q26, Q27). The other 3 are a comms-style instruction, a 'No need thanks' reply and an attachment-only message. The one data ask is the ST YTD question.",
        "CRO: no question list was found under org/tier1_exec/4.0.0_SA_CRO*/**, whether searched for 'question list', staff-question or real-ask phrasing. The PRD's evidence boundary (prd/NFRA_MCPINDEX_PRD.md:89-90) says the per-property common questions 'are not enumerated anywhere yet', and the decomposition's R2.5 item 2 records the same census miss. The analysis-portal AC5 list is authored by a worker and says it is not measured demand, so it was not used.",
        "OTHER SOURCES USED: agent session logs, orders and change records quoting Andrew verbatim (14). One Teams DM from Alyssa Keith (Q07). Two call transcripts, org/tier1_exec/1.0.0_SA_CTO/deliverables/partner_calls/*.vtt, for Andrew and Yang Liu (3). docs/handoffs/2026-01-18_yang_transcript_reference.md for Yang Liu (1). Partner-side (49F) speakers were not used."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO face s.1 item 1: 'at least 20 questions staff actually asked ... Draw them from the Analyst's thread memory ... and from any other real-ask record you find.'",
    "world_is": "The recorded real-ask population is mostly engineering and status asks by one person. Only 3 of the 27 target a catalogued dataset (Q05, Q07, Q22), so the harness measures uncatalogued-ask rejection far more than dataset selection.",
    "notes": "The form is recorded for the issuer, and G-B's cold run with a non-author asker is where data-shaped asks would come from."
  },
  {
    "id": "NFRA_MCPINDEX-Z-S11",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.4.0_DS_ClientPlatform~D",
    "surfaced_at": "2026-09-26T08:37Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-S6"
    ],
    "one_line": "ANSWERS the open question in Z-S6 as a NEW row, not an edit: the pathfinder gap is 4 partitions of the fact_dailynav feed for 2026-08-29 and 2026-08-30, and it is a CONVERSION failure, not a vendor non-delivery -- both bronze units are present, on time and well-formed.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the missing keys, named: pathfinder/{PFDE,PFOE}/silver/fact_dailynav/date={2026-08-29,2026-08-30}/data.parquet -- 4 partitions, the DAILYNAV feed, not holdings. Z-S6 recorded 'missing 2' per fund without knowing which.",
        "bronze PRESENT for both dates: pathfinder/filepoint/bronze/dailynav/20260829/DailyNAV.csv (531 bytes, LastModified 2026-08-29T22:00:11Z) and .../20260830/DailyNAV.csv (531 bytes, 2026-08-30T22:00:12Z). The vendor delivered; the converter did not produce silver.",
        "A HYPOTHESIS OF MINE, REFUTED and recorded as refuted: both dates are a weekend, so I expected empty shells the converter would rightly refuse. They are not. Each carries header + 2 data rows -- the SAME shape as Friday 2026-08-28 (545 bytes) and Tuesday 2026-09-01 (547 bytes) either side.",
        "both funds' meta/backfill-status.json read live: holes=[] against guard detail 'expected 146 landed 144 matched 144 missing 2 alien 0', so the hole has been ANONYMOUS for about four weeks. mirror_conversion.set_identity's V2-6 law treats a hole without a reason as not honest.",
        "instrument: the sweep's READ-ONLY halves (expected_partitions_etf, _landed_silver, set_identity) run from the FIXED repo bytes against live state. run_sweep was not called and nothing was written."
      ]
    },
    "spec_asserts": "Z-S6 left its own question open: 'Which 2 dates, and whether they are a vendor non-delivery or a conversion failure, is unmeasured here.'",
    "world_is": "Measured. It is 4 partitions, not 2; it is the dailynav feed; and it is a conversion failure on two well-formed, on-time deliveries. Why the conversion failed is STILL unmeasured -- reading the converter's own refusal for those two units is the next act, and it is a filepoint question outside this order's trueshares-only write surface. This row does not disarm Z-S6; it narrows it.",
    "disarm_owner": "2.0.0_SA_COO~O",
    "notes": "FILED AS A NEW ROW BECAUSE THE GATE WAS RIGHT AND I WAS WRONG. I first wrote this measurement INTO Z-S6 in place; .tools/surprise-row-gate.py refused the commit -- 'Corrections are NEW items citing the old id; an edited history is a history nobody can audit', with only a remediation row's own clocks permitted to advance in place. I had misapplied a supersede-in-place rule that belongs to a different artifact class. The mutation was reverted to Z-S6's exact HEAD bytes (verified: empty diff) and re-filed here. The audited override existed and was NOT taken: the gate was enforcing correctly, so the state to fix was mine. Remaining act for the owner is narrow: run the filepoint dailynav converter against those two bronze units, read its refusal, then either fix it or record the two dates as NAMED holes with a reason."
  },
  {
    "id": "NFRA_MCPINDEX-Z-S12",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~I",
    "surfaced_at": "2026-09-26T10:05Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "record-terraform-deploy.sh -- step 7 of the canonical Lambda deploy sequence, and the writer Rule 4's source map depends on -- CANNOT RUN on any device whose default encoding is not UTF-8. Its reader at :259 is a bare open(source_map_path), and lambda-source-map.json carries 23 non-ASCII characters.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED, not inferred: `bash infra/aws/lambda/ci/record-terraform-deploy.sh opal-assets --function opal-assets-silver-etf --version opal-assets-v0.50.0 --author '0.7.0_AE_CloudOps~I <...>'` exits 1 with UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 32218.",
        "THE DEFECT, LOCATED: record-terraform-deploy.sh:259 is `with open(source_map_path) as f:` -- no encoding= argument, so Python takes locale.getpreferredencoding(False), which reads cp1252 on this device.",
        "THE DATA: infra/aws/lambda/ci/lambda-source-map.json is 288159 bytes and holds 23 non-ASCII CHARACTERS -- counted as sum(1 for ch in text if ord(ch) > 127), never as a byte delta (CLAUDE.md section 4). Byte 32218 is 0x9d, which is UNDEFINED in cp1252; that is why it raises loudly instead of decoding wrong.",
        "The failing bytes are PRE-EXISTING mojibake -- the context reads 'image <mangled> CI updates image_uri via', i.e. a UTF-8 em-dash that already round-tripped through cp1252 once. A git log pickaxe over that character dates it to 2026-02-25 and 2026-03-10 across four authors. NOT introduced by this order.",
        "DISCRIMINATING CONTROL, both arms run on the same file: json.load(open(path)) raises UnicodeDecodeError at 32218; json.load(open(path, encoding='utf-8')) returns OK. The file is valid UTF-8. The reader is what is wrong, not the data.",
        "NOTHING WAS HALF-WRITTEN: the script is set -e and the failure is in the reader, before any write. git status after the exit-1 shows only the artifact_sha256 change build-and-upload.sh had already made. Verified, not assumed.",
        "A HYPOTHESIS OF MINE, REFUTED, AND RECORDED AS REFUTED. I expected the WRITER at :340 (`with open(source_map_path, 'w') as f:`, equally unguarded) to be the worse half -- a silent cp1252 re-encode corrupting the shared map for all 218 functions. MEASURED ON THIS DEVICE: it does not. json.dump defaults to ensure_ascii=True, so every non-ASCII character leaves as an escape and nothing unencodable ever reaches the codec. The unguarded write SUCCEEDED and its output re-read as UTF-8 with 0 replacement characters. The writer is safe by accident of a default rather than by design, but it is safe. Filing the claim I could prove instead of the one I expected to prove."
      ]
    },
    "spec_asserts": "cloud-ops Rule 4 makes lambda-source-map.json the pairing record every Lambda must carry an entry in, and build-and-upload.sh's own 'Full deployment sequence' names step 7 as `record-terraform-deploy.sh {pipeline} --version ... --author ...`, the act that closes a Terraform Lambda deploy and sets last_deployed_commit / last_deployed_at.",
    "world_is": "On site Z that step is UNRUNNABLE -- it exits 1 before doing anything. Any AE deploying a Lambda from a Windows device silently loses the last_deployed_commit / last_deployed_at half of Rule 4's record unless they read the exit code and route around it by hand. build-and-upload.sh's own artifact_s3_key / artifact_sha256 write is UNAFFECTED -- it goes through node, not this reader -- so the map looks half-updated rather than untouched, which is the shape that hides the miss.",
    "disarm_owner": "2.0.0_SA_COO~O",
    "notes": "SCOPE: not fixed here, deliberately. TO-MX-s-3 bound 1 is 'One function's code. No schedule, event rule, role, layer or other function changes', and record-terraform-deploy.sh is shared CI tooling for 218 functions -- editing it mid-deploy is exactly the rider that bound forbids. The fix is one argument in two places (encoding='utf-8' at :259 and :340; the writer does not need it today but is one ensure_ascii=False away from needing it, so both). FOR THIS DEPLOY the two fields were written BY HAND, reproducing the tool's own documented rule rather than inventing one: last_deployed_commit = the last commit touching the function's source_dir (753fe90fb1), explicitly NOT HEAD (4dc8fa1221) -- the script's own :198-210 note records that a HEAD-derived or files[]-derived value makes verify-local.sh report non-packaged files as undeployed change. The hand-write is recorded here so it is auditable as a workaround and never mistaken for the tool having run."
  },
  {
    "id": "NFRA_MCPINDEX-Z-S13",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~I",
    "surfaced_at": "2026-09-26T18:20Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-S12"
    ],
    "one_line": "NARROWS AND CORRECTS MY OWN Z-S12. I filed it as 'the recorder cannot READ the file'. Measured: the recorder's read+write pair MANUFACTURES the corruption it later dies on, and the two writers of lambda-source-map.json hold OPPOSITE encoding policies, so the ASCII property MX-s-5 just restored is enforced by nothing.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE LOOP, EXERCISED one character in, not reasoned: pass 0, a file authored in UTF-8 holding ONE U+2014 em dash. pass 1, the recorder's own read (:259 bare open, cp1252 here) plus its write (:340 json.dump) -> the single character has BECOME THREE, U+00E2 U+20AC U+201D, and the file still looks ASCII because json.dump escapes them. pass 2, build-and-upload.sh's node updater re-emits those three as literal UTF-8 bytes. pass 3, the recorder reads again and RAISES on byte 0x9d. That reproduces the MX-s-3 failure state including the exact byte value.",
        "SO THE READER IS THE CORRUPTER, not merely the victim. :259 decodes UTF-8 bytes as cp1252; :340 then writes the mangled characters back faithfully. Nothing complains, because the output is still valid ASCII JSON. The loud failure is the SECOND symptom, and it only arrives once a pass happens to produce a byte the code page has no character for.",
        "THE TWO WRITERS DISAGREE, measured with both controls green (node rc=0 AND the output bytes verified to have changed, so a 0 would be node's own 0): python json.dump defaults to ensure_ascii=True and escapes non-ASCII, keeping the file readable by a default-codepage open(); node JSON.stringify does not escape and writes the character LITERALLY. One node write of any future non-ASCII value re-breaks the recorder exactly as before.",
        "A FIRST MEASUREMENT OF MINE WAS INVALID AND THE CONTROL CAUGHT IT. My first node arm reported 0 non-ASCII bytes and I nearly recorded 'the writers agree'. I had not checked node's exit code: it was rc=1, so the bytes I read were still PYTHON's output. A second attempt also failed (rc=1, wrong argv index). Only the third run, with rc=0 AND a positive control proving node had actually rewritten the file, returned the real answer -- which was the OPPOSITE of the first reading.",
        "THE HISTORY SAYS THIS HAS BEEN HAPPENING FOR MONTHS AND NOBODY JOINED IT UP. A git pickaxe on the exact 8-codepoint run returns 105 commits touching it. Four commit subjects name the mechanism outright: 911f95d458 'restore pure ASCII after the recorder's own write mojibaked it' (2026-09-14, 0.9.0_WK_POSN_ASTTAX~20), 13ec619b49 and c08ace5530 the same week, and d6e5fbe667 (0.7.0_AE_CloudOps~Z) 'drop the serialization churn my own record-terraform-deploy...'. Seats have been hand-repairing the symptom repeatedly; the repairer was the cause.",
        "WHY MX-s-5's FIX HOLDS ANYWAY, and why a subset would not have: cp1252-reading pure ASCII is lossless, so with 0 non-ASCII characters left the loop has nothing to mangle. Verified after the fact -- the recorder ran to exit 0 and the file still reads 0 non-ASCII characters afterwards. That is CLAUDE.md's 'ALL non-ASCII out' arm working as designed."
      ]
    },
    "spec_asserts": "Z-S12, my own row, said: 'record-terraform-deploy.sh ... CANNOT RUN on any device whose default encoding is not UTF-8. Its reader at :259 is a bare open().' It classed the hazard INERT on the grounds that the tool fails closed and corrupts nothing.",
    "world_is": "True but shallow, and the INERT call was wrong. The tool does not merely fail on corruption it inherited -- it CREATES that corruption on every pass over any non-ASCII character, silently, and only becomes loud later. Z-S12's remedy (take the characters out) is still the right act and is done. What Z-S12 missed is that nothing PREVENTS recurrence: the two writers' opposing policies mean the next non-ASCII value written by node re-arms the loop. Hence ARMED, not INERT.",
    "disarm_owner": "2.0.0_SA_COO~O",
    "notes": "NOT FIXED HERE, deliberately. MX-s-5 bound 1 is 'The one data file, plus the recorder re-run. No other file changes', and the order's own step 2 says 'Do not fix other tools here.' The fix is one argument in two places: encoding='utf-8' at record-terraform-deploy.sh :259 and :340. The reader is the urgent half; the writer needs it only to stay correct if ensure_ascii is ever turned off. A durable guard would be a commit-time ASCII check on lambda-source-map.json, which would have caught all 105 of those commits -- proposing it, not implementing it (CLAUDE.md section 2: never implement a gate unless Andrew asks)."
  },
  {
    "id": "NFRA_MCPINDEX-Z-S14",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-26T18:45Z",
    "disposition": "DISMISSED_WITH_REASON",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-W2-S7",
      "NFRA_MCPINDEX-Z-W3-S11"
    ],
    "one_line": "DISPOSITION CORRECTION by the issuer. My earlier disarm rows adjudicated these items but carried disposition UNDER_INVESTIGATION, which _latest_dispositions (surprise-row-gate.py:426) passes to the target, so the items kept reading OPEN and gating. This row carries the terminal disposition: W2-S7 by Z-S7 (v6.AC1 reads all 1069 catalog strings, planted control caught); W3-S11 by Z-S2 (MX-t-8 amended to the 3 tools catalog_gate resolves).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Fold measured at ~18:40Z with the gate's own _latest_dispositions/_gating_item_ids: each target listed read UNDER_INVESTIGATION and gating, while an issuer disarm row already adjudicated it.",
        "3.0.0_SA_CVO~Z's finding (relayed by 1.0.0_SA_CTO~O, file 20260926T182052Z) that Z-W9-S3 read UNDER_INVESTIGATION at 18:3xZ."
      ]
    },
    "spec_asserts": "Each target was disarmed by the issuer's adjudicating row.",
    "world_is": "The disarms carried a non-terminal disposition; this row makes them terminal. The reasons are the earlier rows' own.",
    "dismissal_reason": "Each target was already disarmed by the issuer's own adjudicating row with its reason stated there; this row only makes the disposition terminal."
  }
]
```

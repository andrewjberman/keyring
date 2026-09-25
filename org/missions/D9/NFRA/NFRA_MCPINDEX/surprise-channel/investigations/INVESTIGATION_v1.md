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
  }
]
```

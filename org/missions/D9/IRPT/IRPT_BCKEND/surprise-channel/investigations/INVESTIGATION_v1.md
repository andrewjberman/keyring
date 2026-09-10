# IRPT_BCKEND -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Opened by:** `2.0.0_SA_COO~B` at the L6 issuance (seat rows; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`,
identity, folder == project, the allocator coordinate). Lane `ANY`.
**Id grammar:** a worker's row is `IRPT_BCKEND-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that
coordinate); a seat's row is `IRPT_BCKEND-S<k>`; the CVO's adjudication rows live in `../adjudications/` as
`IRPT_BCKEND-C-S<k>`. **Append-only during the round.** Never edit an existing row. **Denominator at this write:** 5 rows.
**Round 1 task orders:** 19, one per cell of `../../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, on four worker
slots (`0.9.0_WK_IRPT_BCKEND~1`, `~2`, `~3`, `~4`).

```json
[
  {
    "id": "IRPT_BCKEND-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-10T21:15:00Z",
    "one_line": "IB-s-1 / IB-s-12: the PRD's SURFACE MANIFEST homes the directory and holdings PLATINUM JSON in opal-data-portal-v2 -- but that bucket is the origin of CloudFront behavior 19 (/json-tiered/* -> S3 direct, NO auth Lambda) and behavior 18 (public-data-router). A client directory carries names and account identities; a holdings snapshot carries values. L5 re-homes both to the FIRM's own bucket (FIRM_BUCKET_MAP) under investor-reporting/, served ONLY through this project's scoped handlers after ResolvedScope, the same shape the firm-scoped AdvisorIntelligence data already uses (behaviors 2-4, 16, 27 via shared-advisor-router). Carried for the CTO's L10 read; the PRD row is overturned by the finding, not edited.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B (disarmed same turn: no order in this issuance writes to opal-data-portal-v2; IB-s-1 and IB-s-12 name the firm bucket in their faces and their <paths>)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-routes behaviors @8ace3a2596 -- behavior 19 '/json-tiered/* -> S3-opal-data-portal-v2-json (s3) -- direct, no Lambda' and behavior 18 '/api/general/json-tiered/* -> S3-opal-data-portal-v2-json [AUTH] [ROUTER] public-data-router'; behaviors 2-4, 16, 27 '-> S3-opal-data-bd (s3) [AUTH] [ROUTER] shared-advisor-router' for the firm-scoped AdvisorIntelligence data",
        "org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md SURFACE MANIFEST row 'opal-data-portal-v2 PLATINUM JSON via the publisher | write | B1, B12' @62301f71e0",
        "docs/briefs/investor-reporting-ir-bk-brief-20260910.md IV.2 'PLATINUM JSON via the publisher in opal-data-portal-v2' @2acf23d8fd -- the brief's proposal that the PRD carried",
        "CLAUDE.md s.5 'NEVER reference another firm's data from a pipeline tree -- BUCKET or KEY-PREFIX ... shared bucket -> key-prefix + IAM condition; per-firm buckets -> bucket-scoped Deny' @8ace3a2596"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD SURFACE MANIFEST: 'opal-data-portal-v2 PLATINUM JSON via the publisher | write | B1, B12 | existing publisher owner; this project's keys registered'.",
    "world_is": "opal-data-portal-v2 is served by two CloudFront behaviors, one of them with no auth Lambda at all (behavior 19). Any key written there is reachable without the edge validator. The firm-scoped precedent in the estate serves from the firm's bucket through the authenticated router.",
    "notes": "L5 resolution (decomposition v0.1.1 s.9 finding 1): IB-s-1 and IB-s-12 write to <firm bucket>/investor-reporting/... and are served only by this project's scoped handlers. If the CTO's L10 read prefers a different home, that is a PRD addendum and the two cells re-cut."
  },
  {
    "id": "IRPT_BCKEND-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-10T21:16:00Z",
    "one_line": "IB-s-15: the PRD names /api/scoped/investor-reporting/... routes under the partners-api CUSTOM authorizer, but no CloudFront behavior matches that prefix at HEAD (28 behaviors read; the nearest is /api/scoped/partners/* and the depth-1 /api/scoped/advisor-intelligence/* catch-all). A request to the new prefix falls to behavior 0 (/* -> the SPA, S3) and returns the portal shell with 200 -- not a 404. Routes alone are unreachable. IB-s-15 carries ONE new behavior in infra/aws/terraform/portal-auth/cloudfront-distribution.tf (-> APIGateway-portal, viewer-request auth-validator-edge), applied under its own NEVER-2 ledger entry.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-routes behaviors @8ace3a2596 -- 28 behaviors enumerated; 0 match /api/scoped/investor-reporting/*; behavior 0 '/* -> S3-opalinvest-portal (s3) -- default (SPA)'",
        "comp-find --name cloudfront-distribution.tf @8ace3a2596 -- 1 hit: infra/aws/terraform/portal-auth/cloudfront-distribution.tf",
        "infra/aws/terraform/partners-api/api-gateway.tf:15-31 @8ace3a2596 -- portal_api_id 7k3ed8px20, portal_authorizer naqxlm, the CUSTOM-auth route pattern the PRD cites",
        "python .tools/owned-paths-validate.py --check-agent on HEAD bytes @8ace3a2596 -- the file resolves to lane CLOUD_OPS_OR_ETL; a worker reaches it only through a non-terminal order's <paths> (ADHC_OWNPTH.005)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD B15 paths: '/api/scoped/investor-reporting/... routes under infra/aws/terraform/investor-reporting/' following the partners-api scoped layout.",
    "world_is": "The partners-api layout has TWO halves: API Gateway routes AND a CloudFront behavior per prefix. The PRD carried the first; the second lives in portal-auth and is the half that makes the prefix reachable.",
    "notes": "Carried into IB-s-15's face and <paths>. INERT: nothing serves on the prefix until the cell applies it."
  },
  {
    "id": "IRPT_BCKEND-S3",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-10T21:17:00Z",
    "one_line": "IB-s-6: the PRD (v0.3) marks the Graph/certificate mailbox reuse source UNRESOLVED. One inspect candidate exists in the estate that the brief did not name: infra/aws/ec2/opal-gateway/app/config.py declares Mail.Read (the gateway that reads Opal mail today; 82 files carry the token, this is the one DEF-band hit beside its .env.example). Handed to the cell to INSPECT and record -- what permission model, which app registration, whether restricted to one mailbox -- never to reuse on the strength of a token match.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-find 'Mail.Read' --files @8ace3a2596 -- 155 hits across 155,980 files; DEF band: infra/aws/ec2/opal-gateway/.env.example; SURFACED: infra/aws/ec2/opal-gateway/app/config.py",
        "comp-read infra/aws/lambda/ycharts-session-capture/index.mjs @8ace3a2596 -- 'Read {username, password} from ycharts/credentials'; browser login and cookie capture; no mail permission (the PRD v0.3 correction is right)",
        "org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md B6 row 'NONE VERIFIED -- the brief names no existing Graph/certificate mailbox implementation; the reuse source is UNRESOLVED until one is inspected' @62301f71e0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD B6 reuse column: NONE VERIFIED; the reuse source is UNRESOLVED until a Graph/certificate mailbox implementation is inspected.",
    "world_is": "A Graph mail reader exists at infra/aws/ec2/opal-gateway/ (the M365 gateway). Whether its grant shape fits a one-mailbox restricted Mail.Read is unmeasured.",
    "notes": "IB-s-6's Phase 1 inspects and records; the effective grant is VERIFIED or recorded UNVERIFIED with what was read. Nothing assumed."
  },
  {
    "id": "IRPT_BCKEND-S4",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-10T21:18:00Z",
    "one_line": "IB-s-1 / IB-s-12: both land gold runners under data/assets/scripts/gold/investor_reporting/, a CLAUDE.md rule-13 DS surface whose S3 code deploy runs through .tools/safe-deploy.sh. Whether a worker serial (0.9.0_WK_IRPT_BCKEND~2) passes that guard is UNMEASURED: RULING 1 grants the worker its order's <paths> for commits, and the deploy guard is a separate instrument with its own lane read. The ad-hoc QA run is unaffected (permitted for QA). A refusal at the production code deploy is a BLOCKING row on that criterion and rides the drain-end read.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B (the issuer: on a refusal the drain routes the deploy leg to the DS lane the guard names, or surfaces the grant to the registry grantor; nothing in this round bypasses the guard)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLAUDE.md rule 13 @8ace3a2596 -- 'DS owns commit->QA-deploy for data/*/scripts/{gold,silver,bronze}/*.py incl. aws s3 cp ... Enforced by .tools/safe-deploy.sh'",
        "python .tools/owned-paths-validate.py --check-agent 0.9.0_WK_IRPT_BCKEND~1 on HEAD bytes @8ace3a2596 -- data/assets/scripts/gold/investor_reporting/x.py resolves to lane CLOUD_OPS_OR_ETL for the commit plane; the deploy plane's guard is not this resolver",
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md s.3 @8ace3a2596 -- the precedent: the PRD's DS lane column became the <paths> grant at L6, and the deploy acts ran under NEVER-2 ledgers; no gold-script safe-deploy by a worker serial was exercised there"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD B1/B12 new home: data/assets/scripts/gold/investor_reporting/ (directory runner; holdings publisher); SURFACE MANIFEST: 'IRPT_BCKEND (DS lane rules apply to gold scripts)'.",
    "world_is": "The commit grant (RULING 1) and the deploy guard (rule 13 / safe-deploy.sh) are two instruments; the first is measured PERMIT-by-order, the second is unmeasured for a worker serial.",
    "notes": "The first production deploy attempt by ~2 is the measurement. Recorded before it happens so a refusal reads as a known hazard and not as a worker defect."
  },
  {
    "id": "IRPT_BCKEND-S5",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-10T21:19:00Z",
    "one_line": "IB-s-10: section extraction is to be certified against paired PDFs, and no real YCharts PDF exists in the estate (the private packet's PDF response bodies are absent; the four-page Opal export PDF is synthetic BD prior art). The cell builds the extractor and its certification harness against a SYNTHETIC PDF generated from the comparison field census with a DIFFERENCE control (one changed number fails certification); the real-PDF arm rides the specimens' arrival and the live generation on Andrew's per-use word, and is read at L10 on FWD-4 and FWD-8 both. The gap stays named, not filled.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/briefs/investor-reporting-ir-bk-brief-20260910.md IV.4 'PDF response bodies are absent. Real output examples for all three families ... still need proof' @2acf23d8fd",
        "org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md B10 fixtures column 'ACTUAL three-variant PDFs (STILL MISSING -- proof gap, named on FWD-4 and FWD-8)' @62301f71e0",
        "docs/research/investor_reporting_export_20260910/performance-export-review.pdf @8ace3a2596 -- present; the brief names it 'synthetic visual prior art, not a generated client artifact'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Endpoint FWD-4 PROOF: 'replay each approved variant end to end'; PRD B10 acceptance: 'text/table extraction certified with units, dates, page/coordinates'.",
    "world_is": "No approved-variant PDF exists to replay against. The mechanism can be proved on a synthetic specimen; the fidelity claim cannot, until specimens exist.",
    "notes": "Carried into IB-s-10's face. The CTO's L10 read grades FWD-4's real-PDF arm NOT_EVALUATED with this reason until the specimens land."
  },
  {
    "id": "IRPT_BCKEND-W1-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~1",
    "surfaced_at": "2026-09-10T21:54:10Z",
    "one_line": "IB-s-18: the task order's L5 note says the PATH_MANIFEST expands '27 reuse rows ... 5 new homes'. The PRD PATHS table at the pin carries 26 reuse rows and 5 new rows, 31 in total, expanding to 74 concrete tokens. The manifest was built from the PARSED table rather than the stated count, so it covers 74 of 74 tokens and the arithmetic in the face is off by one row, not the manifest. Nothing is blocked; recorded so a later reader who counts 27 does not conclude the manifest dropped a row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 62301f71e0:org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md -- PATHS table row-kind census: reuse=26, new=4, 'new (proposed, absent at inspection)'=1; 31 data rows in total",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-18.the-foundation-contracts-homes-manifest-roots.md @261c8d2080 -- 'every PRD PATHS row (27 reuse rows expanded to their files, 5 new homes)'",
        "infra/aws/lambda/investor-reporting/PATH_MANIFEST.json _meta.denominators -- prd_paths_rows 31, reuse 26, new 5, expanded_entries 74; the S18-AC1 battery arm (c) re-parses the table and reports 74 of 74 tokens covered"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO IB-s-18, THE CELL / What L5 adds: 'infra/aws/lambda/investor-reporting/PATH_MANIFEST.json: every PRD PATHS row (27 reuse rows expanded to their files, 5 new homes)'.",
    "world_is": "The PATHS table at 62301f71e0 carries 26 reuse rows and 5 new rows (4 'new' plus 1 'new (proposed, absent at inspection)'), 31 rows expanding to 74 tokens after comma-brace expansion. The '5 new homes' half is exact; the reuse count is one high.",
    "notes": "The manifest is generated from the parsed table, never from the count, so the deliverable is unaffected either way. Named because a reader auditing coverage against the face's number would look for a 27th reuse row that does not exist."
  },
  {
    "id": "IRPT_BCKEND-W1-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~1",
    "surfaced_at": "2026-09-10T21:54:10Z",
    "one_line": "IB-s-14 / IB-s-15 / IB-s-2: 12 of the 74 PATHS tokens are NOT READABLE from a worker's fresh worktree, by two different mechanisms. (1) THREE brand sources the PRD names as B14's brand authority -- deck_generation/brand/opal_brand_guidelines.pdf, deck_generation/brand_spec/brand.json and the official logo SVG under deck_generation/brand/logo_package/ -- are GITIGNORED at deck_generation/.gitignore:14-15, so they exist on the primary workspace and in NO fresh worktree or clone; a cell that resolves the logo by path will find nothing and its 'asset absent' branch will read like a real absence. (2) NINE portal tokens (three partner roles.ts, ModelPortfolios.tsx, PageSurfaceControl.tsx, four portal/src/api files) sit inside the portal SUBMODULE, a gitlink at 5907cbca98 with no checkout in this worktree. Recorded in the manifest as ABSENT_AT_PIN_GITIGNORED (3) and SUBMODULE_NOT_CHECKED_OUT (9) rather than as a flat absence, so no later cell converts either into 'the file does not exist'.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B (the issuer: IB-s-14's face names how the brand assets reach its worktree -- provisioned like .tools/terraform.exe, or resolved from their real home -- and IB-s-2 / IB-s-15 get the submodule checkout or read the portal sources at the gitlink; nothing in this cell needed them, so nothing is blocked today)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git check-ignore -v deck_generation/brand/opal_brand_guidelines.pdf -> deck_generation/.gitignore:15:brand/ ; deck_generation/brand_spec/brand.json -> deck_generation/.gitignore:14:brand_spec/ ; the logo SVG -> the same brand/ rule",
        "git ls-tree HEAD portal @261c8d2080 -> '160000 commit 5907cbca98eb091124e38a32debefa355c1d4376 portal' -- a gitlink; ls portal in /c/tmp/wk-irpt-1-1 returns an empty directory",
        "git cat-file -e 261c8d2080:deck_generation/engine/brand.py rc=0 -- the fourth brand token IS tracked, so the row is 3 of 4, not 4 of 4",
        "infra/aws/lambda/investor-reporting/PATH_MANIFEST.json presence_breakdown -- PRESENT_AT_PIN 44, SUBMODULE_NOT_CHECKED_OUT 9, NOT_A_REPO_PATH 15, ABSENT_AT_PIN_GITIGNORED 3, ABSENT_BY_DESIGN_NEW_HOME 3, summing to the 74-token denominator",
        "memory reference_a_gitignored_tool_binary_is_absent_in_every_fresh_worktree_and_the_path_substitute_repins_remote_state.md -- the same shape, already measured on .tools/terraform.exe"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD PATHS reuse rows at 62301f71e0 name 'deck_generation/brand/opal_brand_guidelines.pdf, deck_generation/brand_spec/brand.json, deck_generation/engine/brand.py, ... Opal-Capital-Logo-Full-Color.svg | B14 | brand authority; official logo' and the portal roles.ts / ModelPortfolios.tsx / portal/src/api rows, as sources later cells reuse.",
    "world_is": "3 of those 4 brand tokens are gitignored and absent from every fresh worktree; 9 portal tokens are inside an unchecked-out submodule. 12 of 74 tokens are unreadable where the worker that needs them will run, and both states look identical to a naive os.path.exists() check.",
    "notes": "IB-s-18 needed none of them, so this is not blocking today. The manifest distinguishes the two states from a true absence, which is the whole point of recording presence with a measured instrument rather than a boolean."
  },
  {
    "id": "IRPT_BCKEND-W2-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-10T23:00:54Z",
    "one_line": "IB-s-1: the face's reuse list writes the INF and COT identity runners as `runners_inf/a00_dim_account.py`, `runners_inf/a01_dim_relationship.py`, `runners_inf/runner_common.py` and `runners_cot/a01_dim_relationship.py` in a PATHS row whose other tokens all resolve under data/assets/scripts/gold/. All four are ABSENT there. They live in the per-firm trees data/inf/scripts/gold/runners_inf/ and data/cot/scripts/gold/runners_cot/, where they exist and are current. Read from the real homes and recorded in PATH_MANIFEST.json with a note on each row. NOT blocking: the sibling-token resolution the face intends is unambiguous once the tree is read. Named because an os.path.exists() against the implied prefix returns False, and a false absence on an identity source is how a directory silently loses a firm.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ls -f of the four implied paths under data/assets/scripts/gold/ @410f28f7db -- MISSING 4 of 4 (runners_inf/{a00_dim_account,a01_dim_relationship,runner_common}.py, runners_cot/a01_dim_relationship.py); the four 49F tokens in the same PRD row resolve there, EXISTS 4 of 4",
        "comp-find --name a00_dim_account.py --all @410f28f7db -- DENOMINATOR 3 hits across 32,100 files scanned: data/assets/scripts/gold/runners_49f/, data/cot/scripts/gold/runners_cot/, data/inf/scripts/gold/runners_inf/",
        "wc -l of the four real paths @410f28f7db -- EXISTS 4 of 4 (data/inf/.../a00_dim_account.py 101, a01_dim_relationship.py 96, runner_common.py 252; data/cot/.../a01_dim_relationship.py 173)",
        "data/inf/scripts/gold/runners_inf/runner_common.py:36 @410f28f7db -- SILVER_BUCKET = os.environ.get('INF_S3_BUCKET', 'opal-data-inf'); data/cot/scripts/gold/runners_cot/runner_common.py:41-42 @410f28f7db -- ASSETS_BUCKET / SILVER_PREFIX 'blackdiamond/cottonwood/silver/'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO IB-s-1 THE CELL, PRD row `paths: reuse`: \"`runners_49f/a01_dim_relationship.py`, `a06_dim_identity_crosswalk.py`, `d08_firm_ownership_map.py`, `bd49f_dim_portfolio_group.py`; `runners_inf/a00_dim_account.py`, `a01_dim_relationship.py`, `runner_common.py`; `runners_cot/a01_dim_relationship.py`\" -- one row whose resolved siblings sit under data/assets/scripts/gold/.",
    "world_is": "The 49F runners are under data/assets/scripts/gold/runners_49f/. The INF and COT runners are NOT siblings of them: they are under data/inf/scripts/gold/runners_inf/ and data/cot/scripts/gold/runners_cot/. The three firms each ship a module spelled `runner_common.py` with DIFFERENT bucket constants.",
    "notes": "SECOND-ORDER HAZARD, measured while fixing this: because all three firms name their harness `runner_common`, a bare `import runner_common` after a sys.path insert binds whichever firm imported FIRST and then serves 49F's GOLD_BUCKET to INF. Here it failed LOUD (AttributeError on list_api_dim_partitions) because the APIs differ; where two firms' APIs agree it would fail SILENTLY against the wrong bucket. directory_runner._import_runner loads each by file path under a unique module name and says why in its docstring. Any later cell importing more than one firm's runner family inherits this and should do the same."
  },
  {
    "id": "IRPT_BCKEND-W2-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-10T23:00:54Z",
    "one_line": "IB-s-1 / IB-s-18 contract: DirectoryEntry.schema.json types `ids.relationship_id` as bare {\"type\": \"string\"} while its OWN description for that property says \"an account-only entry carries null\". A null therefore FAILS the schema the description promises it satisfies -- measured, not reasoned: the first build emitted 263 account-only 49F entries with null and jsonschema rejected every one. Account-only entries are an EXPLICIT acceptance case of this cell, so the contradiction is on the acceptance path, not a corner. IB-s-1 omits the key instead (valid: relationship_id is absent from ids.required) and does not edit the contract, which is IB-s-18's surface and outside this order's <paths>. A FNTEND consumer reading `entry.ids.relationship_id === null` as the account-only tell will read `undefined` instead.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B (the issuer: the fix is a one-token contract edit -- [\"string\",\"null\"] -- owned by IB-s-18's surface, and it must land on BOTH sides at once because IRPT_FNTEND consumes this contract. Disarmed for THIS cell by omission: 5,062 of 5,062 emitted entries validate at 410f28f7db+, and the omitted-key form carries the same meaning under the schema as written.)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/_contracts/DirectoryEntry.schema.json @410f28f7db -- properties.ids.properties.relationship_id = {\"type\": \"string\", \"description\": \"... opaque relationship id; an account-only entry carries null\"}; properties.ids.required = [firm_id, client_id, account_ids] -- relationship_id is NOT required",
        "first live QA build 2026-09-10 ~22:3xZ -- jsonschema Draft202012Validator over 4,509 49F entries: 4,246 valid, 263 errors, every one '$.ids.relationship_id: None is not of type string'; the 263 are exactly the dim_relationship rows with mapped=false",
        "re-run after omitting the key -- 5,062 of 5,062 entries valid across three firms (49F 4,509 + INF 293 + COT 260)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "DirectoryEntry.schema.json ids.relationship_id description: \"opaque relationship id; an account-only entry carries null\"; and TO IB-s-1 acceptance arm (b): \"a fixture directory carrying ... an account-only entry ...\".",
    "world_is": "The property's TYPE is \"string\" with no null member, so the null the description prescribes is refused by the same file that prescribes it. The description and the type are both AUTHORITATIVE regions of a generated contract and they disagree.",
    "notes": "This is the contract-generation shape worth naming beyond this row: the schema is GENERATED from the PRD's CONTRACTS table and its descriptions QUOTE that table verbatim, but the TYPES are chosen by the generator. A generator that quotes its source into the description and infers the type separately can emit a file whose prose and whose validator disagree, and the IB-s-18 battery -- which checks that each description's quoted string APPEARS in the table -- passes on exactly that defect, because the quote is genuine. Worth one pass over the other ten contracts for the same pattern (a described-null on a bare-typed property); IB-s-1 did not do that pass, which is out of its cell."
  },
  {
    "id": "IRPT_BCKEND-W2-S3",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-10T23:00:54Z",
    "one_line": "IB-s-1 acceptance arm (c): the face names \"the 79 unmapped INF accounts carry a reason each\" and \"INF 874-of-953 identity fixture\". At the live vintage the INF population is 874 accounts of which 874 are IN-UNIVERSE and 874 are MAPPED: ZERO unmapped, and 953 is not the account count on any snapshot this cell read. The arm's own escape clause (\"or the live count with its denominator\") covers it, but 0 of 0 unmapped carrying a reason is a VACUOUS pass that renders identically to a real one. The battery therefore prints the vacuity out loud AND runs a constructed positive control (a frame with 3 unmapped accounts -> 3 of 3 carry a reason, both SELF-FAMILY reasons plus the EXCLUDED-LOUD roster reason exercised), so the reason machinery is graded on a population that exists.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "silver/api_dims/accounts_v2 snapshot_date=2026-09-10 read via data/inf/scripts/gold/runners_inf/runner_common.read_api_dim @410f28f7db -- 874 rows, 874 distinct account_id",
        "a00_dim_account.py IN-UNIVERSE predicate (rep_id in the representatives roster) applied to that frame -- 874 of 874 IN-UNIVERSE, 0 EXCLUDED-LOUD; the roster carries 19 rep_ids @ snapshot 2026-09-10",
        "a01_dim_relationship.py disposition applied -- MAPPED 874 of 874, SELF-FAMILY 0; household_rep_mapping carries 318 rows / 318 distinct households and the accounts reference 293 of them",
        "IB-s-1 battery arm (c) output 2026-09-10 -- 'INF live: unmapped 0 of 874 accounts; 0 of 0 unmapped carry a reason' + 'POSITIVE CONTROL: constructed INF frame with 3 unmapped accounts -> 3 of 3 carry a reason'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO IB-s-1, What L5 adds: \"the 79 unmapped INF accounts carry a reason each\"; fixtures/evidence: \"INF 874-of-953 identity fixture\"; acceptance arm (c): \"INF unmapped accounts each carry a reason (print `79 of 79` or the live count with its denominator)\".",
    "world_is": "INF accounts_v2 @2026-09-10 carries 874 accounts; 874 of 874 are in-universe and 874 of 874 are MAPPED. The unmapped population is EMPTY. 874 appears in the face's fixture as the NUMERATOR of 874-of-953, and it is the live DENOMINATOR -- which is the coincidence that makes this worth writing down rather than assuming the fixture simply aged.",
    "notes": "Two readings fit and this cell cannot separate them: (i) the fixture is stale and the 79 closed between its vintage and today, or (ii) 953 was a different population (a wider account universe before the rep-roster predicate, or a pre-v2 accounts endpoint) and 874 was always the in-universe count. Whoever grades FWD-1 should not read the live 0 as evidence that the gap-reasoning requirement was met -- it is untested by the live arm, which is why the positive control exists."
  },
  {
    "id": "IRPT_BCKEND-W2-S4",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-10T23:00:54Z",
    "one_line": "IB-s-1: the face attributes `match_method` / `match_as_of` / `in_0833_universe` to the 49F runner `a06_dim_identity_crosswalk`. That runner emits none of the three; its columns are smartx_allocation_uuid, smartx_account_uuid, schwab_account_number, account_id, in_account_universe, map_date, map_carried. The three named fields are the BD account xref's, written by data/assets/scripts/silver/bd49f_dim_conversion.resolve_bridge and landed at blackdiamond/49f/silver/dim_account_xref -- a path the same PRD row already names, so nothing is missing, only mis-attributed. Read from the xref and carried as RECONCILIATION PRIOR ART. Named because the two artifacts differ in KIND, not just in location: the crosswalk is a vendor-uuid join aid and the xref is a reconciliation between two custodial key spaces whose `unresolved` rows are reported in-band.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "gold/advi/dimensions/dim_identity_crosswalk/date=2026-09-09/data.parquet read 2026-09-10 -- 7,446 rows, columns [smartx_allocation_uuid, smartx_account_uuid, schwab_account_number, account_id, in_account_universe, schema_version, map_date, map_carried, source_pipeline, _ingested_at]; match_method 0 of 10, match_as_of 0 of 10, in_0833_universe 0 of 10",
        "blackdiamond/49f/silver/dim_account_xref/date=2026-09-09/data.parquet read 2026-09-10 -- 6,202 rows, columns include match_method, match_as_of, in_0833_universe (3 of 3 present)",
        "data/assets/scripts/silver/bd49f_dim_conversion.py:149 @410f28f7db -- XREF_SCHEMA carries (\"match_method\", _S), (\"match_as_of\", _S), (\"in_0833_universe\", _B); :282-305 resolve_bridge sets seed-xref / direct-acct10 / unresolved",
        "comp-find 'match_method|match_as_of|in_0833_universe' --all @410f28f7db -- 652 hits across 30,317 files; the DEF-band writer is bd49f_dim_conversion.py, and a06_dim_identity_crosswalk.py is not among the writers"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO IB-s-1, What L5 adds: \"49F: `a01_dim_relationship`, `a06_dim_identity_crosswalk` with `match_method`/`match_as_of`/`in_0833_universe`, `d08_firm_ownership_map`, `bd49f_dim_portfolio_group`\".",
    "world_is": "a06_dim_identity_crosswalk emits the SmartX allocation crosswalk and carries `in_account_universe` (a different field with a different denominator). The three named fields are emitted by bd49f_dim_conversion.py into dim_account_xref.",
    "notes": "Both artifacts are already in this order's reuse list, so the cell reads both and nothing is blocked. The distinction matters downstream: `in_account_universe` on the crosswalk is membership in the fact_acc universe, whereas `in_0833_universe` on the xref is membership in one custody master's universe. A consumer that treats them as the same predicate gets a different denominator without any error."
  }
]
```

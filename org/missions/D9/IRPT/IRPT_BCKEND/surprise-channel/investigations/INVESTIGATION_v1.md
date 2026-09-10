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
  }
]
```

# IRPT_BCKEND -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Opened by:** `2.0.0_SA_COO~B` at the L6 issuance (seat rows; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`,
identity, folder == project, the allocator coordinate). Lane `ANY`.
**Id grammar:** a worker's row is `IRPT_BCKEND-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that
coordinate); a seat's row is `IRPT_BCKEND-S<k>`; the CVO's adjudication rows live in `../adjudications/` as
`IRPT_BCKEND-C-S<k>`. **Append-only during the round.** Never edit an existing row. **Denominator at this write:** 12 rows (S1-S7, W1-S1..S5), COUNTED.
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
    "id": "IRPT_BCKEND-S6",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-10T22:25:00Z",
    "one_line": "DISARM of IRPT_BCKEND-W1-S2 (12 of 74 PATHS tokens unreadable from a fresh worktree) by its named owner, at the drain of IB-s-18: (1) the three gitignored brand sources (deck_generation/brand/opal_brand_guidelines.pdf, deck_generation/brand_spec/brand.json, the full-color logo SVG) are PROVISIONED by the issuer into slot ~4's worktree at the IB-s-14 hand-off, exactly as .tools/terraform.exe is provisioned into every slot, and the hand-off line says so; (2) the nine portal tokens are READ-ONLY pattern references for IB-s-2 and IB-s-15 (the PRD row: 'presentation vocabulary, not grants'; 'pattern reference only'), and those hand-off lines name the primary workspace's portal checkout path for the read -- no portal write is granted to any order in this round, so no portal worktree is cut. Both mechanisms are issuer acts at the spawn; no face is edited.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md row IRPT_BCKEND-W1-S2 @410f28f7db -- the worker's measurement: 3 gitignored brand tokens (deck_generation/.gitignore:14-15), 9 portal tokens inside the unchecked-out submodule",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/ IB-s-2, IB-s-14, IB-s-15 faces @261c8d2080 -- the only three orders whose PRD rows name those tokens; IB-s-14 as brand authority, IB-s-2 and IB-s-15 as read-only pattern references",
        "org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md s.5 @261c8d2080 -- '.tools/terraform.exe is gitignored and absent in a fresh worktree: the issuer provisions it into every slot's worktree at spawn' (the same mechanism, extended to the brand sources)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Row W1-S2: ARMED, disarm_owner 2.0.0_SA_COO~B -- 'IB-s-14's face names how the brand assets reach its worktree ... and IB-s-2 / IB-s-15 get the submodule checkout or read the portal sources at the gitlink'.",
    "world_is": "The faces are frozen mid-round and say nothing about provisioning; the issuer's hand-off line (the L7 identity line in the spawn prompt, an issuer artifact outside the face) is where the provisioning fact travels, and the provisioning itself is a copy into the slot's worktree before the spawn.",
    "notes": "Disarmed same turn as read (spine L7: an ARMED row is disarmed in the same turn by its named owner, and disarmed is not remediated). Carried for the CVO's L8 compile so the ARMED row reads resolved."
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
    "id": "IRPT_BCKEND-W1-S3",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~1",
    "surfaced_at": "2026-09-10T23:05:00Z",
    "one_line": "IB-s-17: safe-apply's FIRST identity gate (the HALTGT checkpoint) refused the apply fail-closed with 'IDENTITY UNRESOLVED' until org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial named the acting serial. OPAL_AGENT_SERIAL satisfies the SECOND gate only. That file is GITIGNORED (.gitignore:423), absent from a fresh worktree, and not in this order's <paths> -- but it has no commit plane at all, so the lane grant cannot express it and nothing written there can ever enter the repo. I wrote the one line the gate itself prescribes, in this worktree only, and the gate then admitted the apply on its DESIGNED worker path: it resolved 0.9.0_WK_IRPT_BCKEND~1 through a NON-TERMINAL task order issued_to it and scanned its ISSUER's inbox, printing 'worker 0.9.0_WK_IRPT_BCKEND~1 has no inbox; scanning its issuer 2.0.0_SA_COO~B'. So the gate ended up MORE protective, not bypassed: no override flag, no HALT_ACK, no TAGAUTHZ_OVERRIDE was used. THE COUPLING WORTH KNOWING: that admission holds only while a task order issued_to the worker is NON-TERMINAL, so a worker's own complete flip WITHDRAWS its apply grant -- every apply must precede the flip.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/safe-apply.sh run at 22:4xZ -> rc=3, banner 'HALT-GATE: IDENTITY UNRESOLVED -- BLOCKED (fail-closed)' with its own one-line remediation naming org/mcp/sessions/<id>.serial",
        ".tools/halt-gate-check.sh:130-140 @410f28f7db -- 'SPINE v3 WORKER (2026-09-04 ...): 0.9.0_WK_<CODE>~<n> has no home folder and a DIGIT lane, so the two checks below refused every worker and no L7 worker could safe-apply ... A worker is a REAL principal iff a NON-TERMINAL task order under <CODE> at HEAD is issued_to it ... the gate scans the inbox of the issuer that order names and a [STOP] to the issuer halts its workers' deploys. Fail-closed: no such order, no admission.'",
        "git check-ignore -v org/mcp/sessions/6e2c2caf-f95a-4a53-bb58-c9963d9f0a19.serial -> .gitignore:423:org/mcp/sessions/ ; git status --porcelain org/mcp/ prints nothing after the write",
        "the second apply run printed 'HALT-GATE: worker 0.9.0_WK_IRPT_BCKEND~1 has no inbox; scanning its issuer 2.0.0_SA_COO~B (a [STOP] to the issuer halts its workers)' and proceeded to the tag-authz gate",
        "memory reference_a_worker_subagent_in_a_fresh_worktree_fails_safe_applys_identity_gate_closed_export_opal_agent_serial_at_spawn.md -- the same class, already measured"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order's BOUNDS 4: '.tools/safe-apply.sh only, from a root whose state key is this cell's ... .tools/terraform.exe is provisioned in your worktree by the issuer'. The <paths> block is the write grant and names no identity file.",
    "world_is": "safe-apply cannot run at all until the session serial file exists. The issuer provisions .tools/terraform.exe into a worker worktree at spawn but not org/mcp/sessions/<session>.serial, and the two are the same class of provisioning: a gitignored file a fresh worktree cannot have.",
    "notes": "INERT: the gate fails CLOSED and loudly, with its own remedy printed, so the cost is one refused run per fresh worktree and never a wrong deploy. Cheapest disarm is for the issuer to write the .serial at spawn beside .tools/terraform.exe. Nothing was overridden: HALT_ACK and TAGAUTHZ_OVERRIDE were both unused, and org/git-author-override-audit.log carries no entry from this cell."
  },
  {
    "id": "IRPT_BCKEND-W1-S4",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~1",
    "surfaced_at": "2026-09-10T23:05:00Z",
    "one_line": "IB-s-17: the root .gitignore:206 carries '**/.terraform.lock.hcl', so this root's provider lock CANNOT be committed without a forced add -- while 35 sibling roots under infra/aws/terraform/ DO track one. The estate's rule and the estate's practice disagree, and the consequence for this cell is narrow but real: investor-reporting/core's provider versions (hashicorp/aws 5.100.0, hashicorp/local 2.9.1) are pinned only in this worktree, so a later apply of the SAME sources from a fresh worktree could resolve different provider versions than the ones that produced the applied plane. NOT FIXED HERE: `git add -f` would contradict the rule that is currently in force, and editing .gitignore is a neighbouring defect this order does not own.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git check-ignore -v infra/aws/terraform/investor-reporting/core/.terraform.lock.hcl -> .gitignore:206:**/.terraform.lock.hcl",
        "git ls-files 'infra/aws/terraform/*/.terraform.lock.hcl' | wc -l -> 35 tracked lock files (aaii-v2-bucket-lifecycle, astn-pipeline, bd-bucket-lifecycle, bd-pipeline, canonical-schwab-ec2, ...)",
        "terraform init output @410f28f7db worktree: 'Terraform has created a lock file .terraform.lock.hcl to record the provider selections it made above. Include this file in your version control repository so that Terraform can guarantee to make the same selections by default'",
        "the apply's own resolution: 'Installing hashicorp/aws v5.100.0', 'Installing hashicorp/local v2.9.1'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order's DELIVERABLE is the core root; the constraint in force is `~> 5.0` for aws, which is a RANGE, and the lock file is what turns a range into a pin.",
    "world_is": "The lock file exists in the worktree, is gitignored by a repo-wide rule, and 35 sibling roots nonetheless carry theirs in git -- so whichever way this root goes it is inconsistent with something.",
    "notes": "The applied plane is unaffected: the provider versions that produced it are recorded verbatim in this cell's ledger entry and in the apply transcript, so the vintage is not lost even though the pin is not committed. A seat that wants the pin has two coherent options -- force-add like the 35, or retire the ignore line -- and both are outside this order."
  },
  {
    "id": "IRPT_BCKEND-W1-S5",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~1",
    "surfaced_at": "2026-09-10T23:05:00Z",
    "one_line": "IB-s-18's S18-AC1 arm (d) asserts 'no .terraform/ directory and no terraform.tfstate* exists under any root' and its proof recorded '0 of 9 roots initialised'. IB-s-17 has now legitimately initialised core/, so re-running battery_ib_s_18.py IN THIS WORKTREE reads a FAIL that is not a defect -- the earlier cell's claim was true when made and this cell's job falsifies it. MEASURED MITIGATION, not assumed: .terraform/ is gitignored at infra/aws/terraform/.gitignore:1 and the backend is S3 so no local tfstate exists, and `git status --porcelain infra/aws/terraform/investor-reporting/core/` shows ONLY layout.json -- therefore a re-grade from a FRESH worktree of the merged branch still passes arm (d). The hazard is confined to a re-run in a worktree where core/ was initialised.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IB-s-18_S18-AC1_battery_output.txt @c4214773c9 -- 'STATE ON DISK: 0 `.terraform/` dir(s) and 0 `terraform.tfstate*` file(s) ... 0 of 9 roots initialised'",
        "git check-ignore -v infra/aws/terraform/investor-reporting/core/.terraform/ -> infra/aws/terraform/.gitignore:1:.terraform/",
        "git status --porcelain infra/aws/terraform/investor-reporting/core/ -> '?? layout.json' and nothing else, so nothing from init is visible to git",
        "the core root's backend is s3 (investor-reporting/core/tfstate), so terraform writes no local state file"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S18-AC1 arm (d): 'assert no `.terraform/` directory and no `terraform.tfstate*` exists under any root' -- graded PASS at c4214773c9 and merged at 410f28f7db.",
    "world_is": "The assertion is a POINT-IN-TIME property of a shared tree, not a property of the deliverable, and the very next cell in the same slot is the one specified to falsify it.",
    "notes": "Named so an L9 re-grade reads a FAIL correctly if anyone re-runs the older battery in a used worktree. The general shape is worth the issuer's attention: an acceptance arm that asserts the ABSENCE of a sibling cell's future work is falsified by that work landing, and only the gitignore is keeping this one from biting the normal re-grade path."
  },
  {
    "id": "IRPT_BCKEND-S7",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-10T23:28:00Z",
    "one_line": "EVERY L7 WORKER SPAWNED ON THIS FABRIC SINCE 22:43:03Z RUNS ON SONNET, NOT OPUS. .claude/agents/worker.md line 5 reads `model: sonnet` at HEAD since the merge b9ee1966cc (origin/SITEZ into CLOUD, 2026-09-10 18:43:03 -0400), while the file's own ruled note (1.0.0_SA_CTO @052aafbdf7) says this fabric runs `opus` and site Z runs `sonnet`, and Andrew-direct 2026-09-09 ~21:5xZ says 'All spawned workers for /canonical-flow should be subagents in the same session box using Opus with effort high'. The value on CLOUD was `opus` at 052aafbdf7 and 1d62717c65 (leg 1) and flipped to `sonnet` at b9ee1966cc -- the exact silent re-point the note predicts. For THIS project: slot ~1 (spawned 21:3xZ, resumed since) is on Opus; slots ~2 (IB-s-1) and ~4 (IB-s-11), spawned ~22:5xZ, were spawned under the flipped definition and are STOPPED and RESPAWNED by the issuer with the model set explicitly at the spawn; every later spawn in this round passes the model explicitly until the definition is repaired. The repair of the definition is not this lane's (the file is fabric law under the CTO's ruling and the integrator's merge); surfaced here for the CVO's L8 compile and the CTO's L10 read, and it reaches every COO lane spawning on this fabric, not only this project.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B for this project's spawns (disarmed same turn: the model is passed explicitly at every spawn in this round); 1.0.0_SA_CTO / 0.0.0_AB_MSTR for the definition itself (the per-fabric value at HEAD contradicts the CTO's own ruling in the same file)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log --first-parent -- .claude/agents/worker.md @6800337403 -- b9ee1966cc 2026-09-10 18:43:03 -0400 'Merge remote-tracking branch origin/SITEZ into CLOUD' carries `model: sonnet`; 1d62717c65 (leg 1) and 052aafbdf7 (the ruling) carry `model: opus`",
        ".claude/agents/worker.md:5,8-16 @6800337403 -- `model: sonnet` under the note 'This fabric (CLOUD) runs opus; site Z runs sonnet ... whoever merges second silently re-points the other fabric's entire worker population'",
        "ea764aecc6 0.0.0_AB_MSTR~Z 2026-09-10 13:52:35 -0400 'integrate: LEG 2, CLOUD -> SITEZ ... the SILENT MODEL FLIP WE BOTH PREDICTED ACTUALLY FIRED, arriving with ZERO conflicts because leg 1 had already resolved it' -- the integrators predicted it and it fired anyway on the return leg",
        "org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md L7 @6800337403 -- 'Its model is Opus at high effort, declared by the worker agent type's own definition ... never chosen per task order and never left to a per-spawn override' -- which is why an explicit per-spawn model is a DISARM and not a fix"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Spine v3 L7: the worker's model is Opus at high effort, declared by .claude/agents/worker.md; Andrew-direct 2026-09-09 ~21:5xZ: 'using Opus with effort high'.",
    "world_is": "At HEAD 6800337403 the definition declares `model: sonnet`; a spawn that trusts the definition runs a Sonnet worker on this fabric. Two of this project's four slots were spawned in that window.",
    "notes": "Issuer acts this turn: TaskStop on slots ~2 and ~4, respawn on their existing worktrees and branches with the model passed explicitly; slot ~3 and every hand-off likewise. No face edited. The ~2/~4 work done under the wrong model before the stop stays on their branches and is re-grounded by the respawned worker's first act; nothing is discarded by the issuer."
  },
  {
    "id": "IRPT_BCKEND-W3-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T00:30:14Z",
    "one_line": "THE OFFLINE PROOF OF THE YCHARTS SESSION LIBRARY RUNS WITHOUT A REAL BROWSER. TO-IB-s-8's L5 note specifies 'a local browser against the captured HAR flows ... through a replay server', and arm (a) of S8-AC1 grades the five surfaces against that replay. Playwright is NOT installed in this worktree (a require of it returns \"Cannot find module 'playwright'\"; node itself is v26.8.1 and present), and installing it is an npm install against the public registry -- egress off Opal infrastructure, which CLAUDE.md's Agent Autonomy section excludes from this seat's standing authority, and which would also be the one thing arm (e) exists to refuse. So ycharts_session.js takes its browser as an INJECTABLE PORT (opts.browser, default require('playwright').chromium) and tests/replay_browser.js implements that same shape over real loopback HTTP. WHAT THIS DOES PROVE: the library's own code paths run unmodified -- classifyScreen, the selector list, fillAndSubmit, the cookie jar handling, probeSession, the lease and fence logic, the bounded reacquisition -- against real HTTP responses carrying the MEASURED YCharts statuses. WHAT IT DOES NOT PROVE: anything about Chromium, JavaScript execution, rendering, a real WAF challenge, real cookie rotation, or the vision fallback (replay_browser.js's screenshot() THROWS rather than stubbing, so a vision path cannot pass unexercised). ARMED because 'arm (a) 5 of 5' reads, to a later cell or an L9 grader, exactly like 'the runner works in a browser'.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.9.0_WK_IRPT_BCKEND~3 -- DISARMED SAME TURN by naming the limit in the three places a reader will actually be standing: tests/replay_browser.js's header ('it is NOT Chromium'), infra/aws/ec2/investor-reporting-ycharts/README.md section 'What the offline proof cannot show', and the S8-AC3 judgment record in the proof-of-spec instance, which 3.0.0_SA_CVO grades at L9. The residual -- exercising the library in a real browser against the real site -- is the QUALIFIED LIVE ARM and belongs to 1.0.0_SA_CTO's L10 read on Andrew's per-use word, not to this order.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "node -e require('playwright') in /c/tmp/wk-irpt-1-3 -> \"PLAYWRIGHT-ABSENT: Cannot find module 'playwright'\"; node --version -> v26.8.1",
        "infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js @ff12d98c4d -- 'PORTS. Every outside edge is an injectable port with a lazy default' and defaultBrowserPort() = require(YC_PW_PATH || 'playwright').chromium",
        "infra/aws/ec2/investor-reporting-ycharts/tests/replay_browser.js @ff12d98c4d -- 'WHAT THIS IS NOT ... it is NOT Chromium' and ReplayPage.screenshot() throws rather than returning a stub",
        "CLAUDE.md Agent Autonomy @7d7f33569a -- 'Do NOT ask permission to read/write/build/test/commit ... Excluded: all egress off Opal infrastructure.'",
        "IB-s-8_S8-AC1_battery_output.txt arm (e) -- 'netguard: 0 external of 1 connection attempts during the suite' with a POSITIVE CONTROL at https://ycharts.com refused by netguard.js (guard_external 0 -> 1)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-s-8, 'What L5 adds' s.9: 'Proof of the library is OFFLINE: a local browser against the captured HAR flows ... through a replay server; no request leaves the machine.'",
    "world_is": "No browser is installed in this worktree and installing one is egress this order does not authorize. The proof runs the library against a Playwright-SHAPED loopback adapter, so it grades the library's mechanism and not a browser's behaviour.",
    "notes": "The shape is worth an issuer's attention beyond this cell: a cut that specifies a proof instrument the worktree does not carry, and whose installation is itself outside the worker's standing authority, will be met either by an honest substitute (this) or by a quiet egress. IB-s-9 hangs off this cell and meets the same wall the moment it needs a rendered page."
  },
  {
    "id": "IRPT_BCKEND-W3-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T00:30:14Z",
    "one_line": "THERE IS NO CAPTURED LOGIN FLOW ANYWHERE IN THIS CELL'S EVIDENCE, SO THE 'REPLAYED LOGIN FLOW' IN S8-AC1 ARM (a) IS MODELLED, NOT REPLAYED. Two separate facts, both measured. (1) The private packet is NOT in the worktree: docs/research/investor_reporting_ycharts_20260910/ contains exactly one file, profile_handoff.py -- the PROFILER, not the HARs it profiles -- so the three .har files and the six transcripts the TO names as fixtures cannot be read here at all. (2) The sanitized derivative that IS present, docs/briefs/sources/INVESTOR_REPORTING_YCHARTS_HAR_EVIDENCE_20260910.json, profiles three HARs of 220, 403 and 462 entries, and every one of the 16 profiled calls is a report_generation or a model-portfolio POST: all three captures are POST-AUTHENTICATION application sessions. profile_handoff.py:profile() only emits rows for /custom_pdf_reports/{id} and /model_portfolios/fixed/, so even the raw packet would have to be re-profiled to say anything about a sign-in. CONSEQUENCE: the replay's APP surface is grounded (measured routes and statuses, plus ycharts_client.py's probe route, its 200-and-only-200 predicate, its 403 'concurrent sign in' eviction discriminator and the three cookie names), but the sign-in PAGE, its form action and its DOM are a MODEL -- built on the Django shape that the csrftoken cookie and the X-CSRFToken header imply -- and the selector list ycharts_session.js tries is exactly the set that model satisfies. A green arm (a) therefore does not bound the risk that the real selectors differ. ARMED for the same reason as W3-S1 and for one more: the first live run is also the first test of those selectors.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.9.0_WK_IRPT_BCKEND~3 -- DISARMED SAME TURN by (i) writing the measured-versus-modelled split line by line into tests/replay_ycharts.js's header and into tests/fixtures/har_derived_routes.json's _meta.not_present field, which says 'NO LOGIN FLOW' in the fixture the replay actually loads; (ii) making acquireSession fail EXPLICITLY rather than silently when its selectors do not match ('sign-in form present but its fields are not addressable'), so a wrong selector on the live site is a named failure and not a hang; (iii) carrying it into the S8-AC3 judgment for 3.0.0_SA_CVO at L9. Closing it needs a capture of an actual YCharts sign-in, which is a LIVE VENDOR CALL and belongs to Andrew's per-use word via 1.0.0_SA_CTO at L10.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ls -la docs/research/investor_reporting_ycharts_20260910/ @7d7f33569a -> one file, profile_handoff.py (8685 bytes); no MANIFEST.json, no hars/, no transcripts",
        "docs/briefs/sources/INVESTOR_REPORTING_YCHARTS_HAR_EVIDENCE_20260910.json @7d7f33569a -- hars[].entry_count = [220, 403, 462]; every calls[] row has kind report_generation or holdings_upload or portfolio_create; distinct method+route pairs = 3, all POST /model_portfolios/* or POST /custom_pdf_reports/{id}",
        "docs/research/investor_reporting_ycharts_20260910/profile_handoff.py profile() @7d7f33569a -- rows are appended only for POST /custom_pdf_reports/<id> and POST /model_portfolios/fixed/*, so the emitted evidence CANNOT contain a login entry even if the raw HAR did",
        "infra/aws/ec2/investor-reporting-ycharts/tests/fixtures/har_derived_routes.json @ff12d98c4d -- _meta.not_present: 'NO LOGIN FLOW. All three HARs are post-authentication application sessions'",
        "infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py @7d7f33569a lines 41, 76-84, 162-164, 170-186 -- the probe route, the three cookie names, seat_evicted() and the 200-only predicate, which ARE measured and which the replay's authenticated surface is built from"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-s-8 S8-AC1 arm (a): 'acquireSession through the replayed login flow -> authenticated'; and the cell's fixtures row: 'six transcripts + manifest + three HARs (private packet, offline profile docs/research/investor_reporting_ycharts_20260910/profile_handoff.py)'.",
    "world_is": "The packet is not in the worktree, and the sanitized evidence that is present contains no sign-in traffic by construction. The login flow in the replay is a model; the app surface is measured.",
    "notes": "Worth the issuer's attention because the same fixtures row is cited by other cells: any cell that expects to read the HARs themselves will find only the profiler, and any cell that expects the evidence JSON to describe authentication will find it describes report generation."
  }
]
```

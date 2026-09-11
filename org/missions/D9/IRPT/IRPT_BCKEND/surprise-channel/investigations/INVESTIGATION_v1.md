# IRPT_BCKEND -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Opened by:** `2.0.0_SA_COO~B` at the L6 issuance (seat rows; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`,
identity, folder == project, the allocator coordinate). Lane `ANY`.
**Id grammar:** a worker's row is `IRPT_BCKEND-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that
coordinate); a seat's row is `IRPT_BCKEND-S<k>`; the CVO's adjudication rows live in `../adjudications/` as
`IRPT_BCKEND-C-S<k>`. **Append-only during the round.** Never edit an existing row. **Denominator at this write:** 16 rows, COUNTED not carried forward -- the MERGE of wk-irpt_bckend-1-4 and CLOUD resolved as a strict UNION of both sides (12 ours + 11 theirs, 7 shared); no row dropped, no id duplicated.
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
    "id": "IRPT_BCKEND-W4-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-10T23:18:00Z",
    "one_line": "IB-s-11 S11-AC1 arm (b) names `probe_performance.py` run offline over INVESTOR_REPORTING_PERFORMANCE_EVIDENCE_20260910.json, but that file carries RECEIPTS, FIELD SHAPES and VALIDATION AGGREGATES and no response bodies at all, and the probe does not read it -- the probe requires --input-dir holding three HAR captures (dashboard_exploration_bdpt1.har, bdpt2.har, orionpt2.har, 138 MB total) that live in Downloads, outside the repository, and its --output-dir must be under the repo's gitignored .runtime tree. So the named invocation cannot produce the named result on any machine that lacks the operator's Downloads folder. The bodies WERE recoverable here: the probe's own live output tree (.runtime/codex-seats/4.0.0_SA_CRO/performance-recon, named by the evidence's meta.raw_storage) holds all seven 200 bodies and the two zero-byte 401s, and 8 of 8 saved bodies hash EXACTLY to the matching http_receipts[].response_sha256. The cell therefore derived scrubbed fixtures from those bytes, committed them under the package, and the battery replays THEM -- so the arm is proven from the same bytes the evidence attests, without depending on an untracked folder.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/briefs/sources/INVESTOR_REPORTING_PERFORMANCE_EVIDENCE_20260910.json @410f28f7db -- top-level keys meta, captures, screenshots, http_receipts, validation, response_field_shapes, unverified, presentation_validation; no body field anywhere; meta.classification 'Sanitized source fingerprints, shapes, counts and receipts; no client identifiers, credentials or raw payloads'",
        "docs/research/investor_reporting_performance_20260910/probe_performance.py:165-176 @410f28f7db -- `--input-dir` required, FILES = {bd1: dashboard_exploration_bdpt1.har, bd2: dashboard_exploration_bdpt2.har, orion: orionpt2.har}, read via (args.input_dir / name).read_bytes(); parser.error unless output-dir is beneath repo/.runtime",
        "Glob '**/*.har' over the worktree: No files found -- 0 HAR captures are in the repository",
        "sha256 tie run by this worker: bd_114 0 bytes / bd_117 0 bytes / orion_252 2354 / orion_compact 5290686 / bd_refreshed_period 176999 / bd_refreshed_series 26918 / orion_daily 119975 / orion_value_check 3850 -- 8 of 8 equal to http_receipts[].response_sha256 and to response_bytes; the ninth receipt (bd_session_refresh) has no saved body because the probe never writes or digests a session-token response",
        "infra/aws/lambda/investor-reporting/performance/fixtures/FIXTURE_MANIFEST.json @de87f0976d -- 9 of 9 receipts accounted, 5 bodies committed, each carrying source_response_sha256 and fixture_sha256"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S11-AC1 arm (b): '`probe_performance.py` offline over the evidence JSON: the seven successful outcomes parse into `PerformanceReport` objects that validate'; the cell text names 'docs/research/investor_reporting_performance_20260910/probe_performance.py (offline)' as the fixtures/evidence.",
    "world_is": "The evidence JSON holds no bodies and the probe never opens it; the probe opens three HAR files that are not in the repository. The bodies exist only in an untracked .runtime tree on this one device.",
    "notes": "Not blocking and not escalated: the arm was met from the same bytes, tied by digest, and the derivation is now committed so it no longer depends on the untracked tree. The residue for the CVO is that any OTHER cell citing this evidence file for BODIES will find none -- IB-s-11's fixtures are the only committed carrier of those bytes in the estate."
  },
  {
    "id": "IRPT_BCKEND-W4-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-10T23:18:00Z",
    "one_line": "The task order's identity mechanism -- 'Every Bash call begins export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~4' -- does NOT satisfy safe-apply.sh's halt gate. `.tools/halt-gate-check.sh` resolves the principal ONLY from org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial or a sibling .orphan-cleaned marker, and it consults no environment variable at all, so the first safe-apply attempt exited 3 with 'HALT-GATE: IDENTITY UNRESOLVED -- BLOCKED (fail-closed)' and terraform was never invoked. The gate DOES know about spine-v3 workers (halt_gate_validate_serial admits 0.9.0_WK_*~[0-9]* by finding a non-terminal task order under the code issued_to the serial and scanning its ISSUER's inbox) -- the hole is one layer earlier, in resolution rather than validation. Unblocked by writing the serial file the gate's own banner prescribes. That path is NOT in this order's <paths>, and it is not a repository edit either: org/mcp/sessions/ is gitignored (.gitignore:423) and holds zero tracked files, so the write is per-session runtime state that cannot enter a commit.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B -- the issuer writes worker faces, and every future face whose cell carries a deploy needs the session-serial line beside the OPAL_AGENT_SERIAL line; this worker cannot edit another face and cannot edit its own",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/halt-gate-check.sh:52-92 @410f28f7db -- halt_gate_resolve_serial reads ${repo_root}/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial, then the ${sid}.${serial}.orphan-cleaned marker, then FAILS CLOSED; the legacy .comp-graph/.agent_context fallback is removed by Andrew-direct 2026-07-13 and no env var is consulted",
        ".tools/halt-gate-check.sh:135-165 @410f28f7db -- the SPINE v3 WORKER block: 0.9.0_WK_<CODE>~<n> is admitted iff a NON-TERMINAL task order under <CODE> at HEAD is issued_to it, and its STOPs are its issuer's",
        "first safe-apply invocation, verbatim rc=3: 'HALT-GATE: IDENTITY UNRESOLVED -- BLOCKED (fail-closed) ... FIX (one line -- use YOUR serial, incl. any ~lane suffix): printf %s\\n \"1.2.3_XX_Yourserial\" > \"org/mcp/sessions/6e2c2caf-f95a-4a53-bb58-c9963d9f0a19.serial\"'",
        "git check-ignore -v org/mcp/sessions/6e2c2caf-f95a-4a53-bb58-c9963d9f0a19.serial -> .gitignore:423:org/mcp/sessions/ ; git ls-files org/mcp/sessions/ -> 0 tracked files ; git status --porcelain org/mcp/ -> empty after the write",
        "memory reference_a_worker_subagent_in_a_fresh_worktree_fails_safe_applys_identity_gate_closed_export_opal_agent_serial_at_spawn.md -- the same trap, already measured on a previous worker"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "IDENTITY AND WORKTREE: 'Serial: 0.9.0_WK_IRPT_BCKEND~4. Every Bash call begins export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~4.' BOUNDS item 4: 'Deploys ... .tools/safe-apply.sh only'.",
    "world_is": "safe-apply has two identity surfaces and OPAL_AGENT_SERIAL satisfies only the commit-lane one. The apply surface reads a session-keyed file that no worker face tells a worker to write, so a worker whose cell carries a deploy is blocked on its first apply until it discovers the banner.",
    "notes": "ARMED because it recurs for every deploy-carrying cell in this round -- IB-s-1, IB-s-4, IB-s-6, IB-s-8, IB-s-9, IB-s-12, IB-s-13, IB-s-14, IB-s-15, IB-s-16, IB-s-17 all apply. Each will lose the same cycle. Cheapest disarm is one line in the face; the alternative (teaching the gate to read OPAL_AGENT_SERIAL) is a change to a safety gate and is not this worker's to make."
  },
  {
    "id": "IRPT_BCKEND-W4-S3",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-10T23:18:00Z",
    "one_line": "The deployed irpt-performance-adapter cannot carry two of its own dependencies, and neither remedy is inside this order's <paths>. (i) jsonschema is not in the AWS python3.12 runtime and infra/aws/lambda/ci/lambda-layer-map.json declares no layer providing it (0 hits for 'jsonschema' across the map's 180 lines), while a layer lives under infra/aws/lambda/layers/ -- not a granted path -- so the deployed function returns contract_validated=false with an absence naming the missing instrument rather than claiming a validation it did not perform. (ii) The bounded Black Diamond helpers the cell reuses (body_performance_period, requested_range_index and the four range builders) live in another Lambda's source_dir; packaging them means either a vendor step or a layer, and 'reusing an existing helper never widens its deployment' -- so the zip does not carry them and the deployed BD path degrades to date-labelled, UNCERTIFIED period cells with the loss recorded as a PARTIAL absence. In the worktree, where the battery and the 28 unit tests run, BOTH dependencies resolve and both are exercised: validation is mandatory and passes 3 of 3, and the request body is built by the estate's own function.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B -- a follow-on cell (or an amendment to a later face) owns the jsonschema layer and the helper packaging decision; both are write surfaces this order does not name",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-read infra/aws/lambda/ci/lambda-layer-map.json --enumerate 'jsonschema' @410f28f7db -- 0 hit(s) across 180 lines scanned",
        "python infra/aws/lambda/ci/import-closure-check.py infra/aws/lambda/investor-reporting/performance <7 modules> -> 'OK: import-closure -- 7 packaged .py file(s), every top-level import satisfied by package/stdlib/runtime/layer' -- jsonschema passes ONLY because normalize.py imports it inside the function, which the gate exempts by design",
        "infra/aws/lambda/investor-reporting/performance/normalize.py ValidationUnavailable @de87f0976d -- three outcomes, never two: validated / not-validated-with-a-named-missing-instrument / schema error",
        "infra/aws/lambda/investor-reporting/performance/bd_adapter.py HELPER_CANDIDATES and HelpersUnavailable @de87f0976d -- env pin, then a _vendor/ copy, then the repo path; no local restatement of the request body is offered as a fallback",
        "the order's <paths>: infra/aws/lambda/investor-reporting/performance/, infra/aws/terraform/investor-reporting/performance/, PATH_MANIFEST.json, change_management/, the sentinel, lambda-source-map.json -- infra/aws/lambda/layers/ and infra/aws/lambda/opal-assets/ are absent"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "DELIVERABLE: 'infra/aws/lambda/investor-reporting/performance/ (bd_adapter.py, orion_adapter.py, normalize.py, handler.py)'; THE CELL: 'Bounded helpers from opal-assets-bd49f-reporting-pull/lambda_function.py are reused (name the functions)'; BOUNDS 7: 'no served output is touched ... except where THIS order's cell says it ADDS a resource'.",
    "world_is": "A Lambda zip is closed over its own directory. Two dependencies the package needs at runtime live outside it, and both remedies (a layer, a vendor step into another Lambda's tree) are outside the write grant. Nothing in the criteria invokes the deployed function, so neither gap is reached by S11-AC1 or S11-AC2.",
    "notes": "Deliberately NOT worked around by copying the helper source into this package: two definitions of one vendor request body is the defect the reuse exists to prevent, and a copy would also be the over-vendoring the estate's own lazy-import note warns against. Both gaps are visible in the function's own output rather than silent."
  },
  {
    "id": "IRPT_BCKEND-W4-S4",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-10T23:18:00Z",
    "one_line": "The committed fixtures carry REAL client economic values -- market values around 63,000 USD, daily returns, fees and cash flows for one Black Diamond 49F account and one Orion Inflection household of two accounts -- with every IDENTIFIER pseudonymised (account name, account number, externalId, BD account and Account-level ids, Orion group names and groupEntityId, the Orion sessionId; 242 replacements across five files, verified by a leak check that fails the generator). The numbers are preserved EXACTLY because they ARE the evidence: the percent-vs-factor tie, the linked-factors-to-summary tie at 1e-13, the 210.68 USD value-shortcut mismatch and the 9x hierarchy overstatement all vanish under any perturbation. This goes one step beyond what the CRO chose to commit -- the evidence file's own meta.classification says 'no ... raw payloads' -- so the choice is surfaced rather than assumed. Black Diamond SEGMENT names (International, Large Cap Value, Cash, ...) are BD's standard asset classification, shared across every client of the tenant, and are kept.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/performance/fixtures/FIXTURE_MANIFEST.json @de87f0976d -- identifiers_replaced per file: 3 + 195 + 30 + 7 + 7 = 242; _scrub states exactly what was replaced and that every economic number is preserved",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/make_perf_fixtures.py leaked() @de87f0976d -- the generator RE-READS its own output and exits 1 if any original identifier survives; it did exit 1 on the first run (11 Segment classification ids) and the scrub was corrected to be level-aware rather than the check relaxed",
        "post-generation read of all five fixtures: every accountName/accountNumber/externalId/sessionId is SCRUBBED-*, every calculated-group name is SCRUBBED-NAME-* and every groupEntityId is 9000000xx",
        "docs/briefs/sources/INVESTOR_REPORTING_PERFORMANCE_EVIDENCE_20260910.json meta.classification @410f28f7db -- 'Sanitized source fingerprints, shapes, counts and receipts; no client identifiers, credentials or raw payloads'",
        "IB-s-11 BOUNDS item 6: 'a recorded fixture is scrubbed before it is committed'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "DELIVERABLE names 'fixtures/'; BOUNDS 6: 'No credential in any artifact, log, fixture or commit. Secrets are read by NAME at runtime; a recorded fixture is scrubbed before it is committed.'",
    "world_is": "'Scrubbed' is not defined in the order. Removing identifiers keeps every arm provable; removing or perturbing the magnitudes destroys the four arithmetic ties that ARE the proof. This worker read the bound as identifier-scrubbing and says so rather than letting the interpretation ride silently.",
    "notes": "No credential of any kind is in the fixtures (checked: no bd.identity, Bearer, access_token or Cookie string appears). If 3.0.0_SA_CVO reads the bound as magnitude-scrubbing too, the remedy is a single affine rescale of every dollar quantity in the generator -- returns and factors are scale-invariant, so only the value-shortcut arm's absolute dollar figure changes, and it would then be cited against a rescaled expectation rather than against the evidence's 210.68."
  }
]
```

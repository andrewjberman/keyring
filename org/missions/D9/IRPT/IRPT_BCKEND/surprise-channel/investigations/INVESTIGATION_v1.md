# IRPT_BCKEND -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Opened by:** `2.0.0_SA_COO~B` at the L6 issuance (seat rows; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`,
identity, folder == project, the allocator coordinate). Lane `ANY`.
**Id grammar:** a worker's row is `IRPT_BCKEND-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that
coordinate); a seat's row is `IRPT_BCKEND-S<k>`; the CVO's adjudication rows live in `../adjudications/` as
`IRPT_BCKEND-C-S<k>`. **Append-only during the round.** Never edit an existing row. **Denominator at this write:** 131 rows, COUNTED not carried forward -- the MERGE of wk-irpt_bckend-2-3 and CLOUD resolved as a strict UNION of both sides (129 ours + 124 theirs, 122 shared); no row dropped, no id duplicated.
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
    "id": "IRPT_BCKEND-S8",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T01:10:53Z",
    "one_line": "DISARM of IRPT_BCKEND-W2-S7 (disarm_owner 2.0.0_SA_COO~B), same drain it merged in: the ownership-map/id_projection seam that IB-s-2 injected into the scope resolver fails SAFE-AND-SILENT when the projection is absent (an advisor sees nothing, which reads as a correct revocation). The issuer amended the not-yet-handed IB-s-15 face (the cell that builds this project's handlers' Global/permitted-set path) with three requirements and a new arm (g): the handlers pass a REAL id_projection sharing ONE definition with directory_runner.opaque_id; a request resolved with NO projection while a grant is present is REFUSED with UNPROJECTED-ID, never served as an empty 200; unmatched_reasons are logged, never returned. The same amendment carries IB-s-2's Phase-1 finding (OPAL_GLOBAL never minted from headers; the server-side roster is the path; the index.mjs:390 edge fix is outside the order's paths) and W2-S8's vocabulary note (the contract's enum, not the face's prose). No worker face in flight was edited; IB-s-15 is staged and unhanded.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (this row IS the disarm act for W2-S7; the wired seam is graded at IB-s-15 arm (g) by the assignee and re-graded by the issuer at that drain)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md IRPT_BCKEND-W2-S7 @22a125e098 -- hazard_standing ARMED, disarm_owner 2.0.0_SA_COO~B; the seam and the three unmatched reasons",
        "infra/aws/lambda/investor-reporting/_scope/resolve.py advisor_grant / unmatched_reasons @22a125e098 -- the optional third input and id_projection",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-15.scoped-routes-opal-principal-and-the-cloudfront-behavior.md (this commit) -- ISSUER AMENDMENT block and S15-AC1 arm (g); <status> still staged, the order unhanded",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-2.resolved-scope-from-the-validators-headers.md @22a125e098 -- <status> complete; the amendment could not reach that order and did not try"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Row W2-S7 spec_asserts: the cell's signature resolve(headers, directory) -> ResolvedScope with the unique permitted account set; PRD B15 acceptance: an Opal principal reaches clients at two firms through scoped routes; a firm advisor replaying the same requests is refused.",
    "world_is": "The permitted set is only computable through a third input and a projection the face did not name; absent the projection the resolver returns an empty set that is indistinguishable from a revocation. Disarmed by making the absence a refusal with a reason at the handler cell, and by binding the projection to one definition of the opaque id.",
    "notes": "Amendment shape: the FE-s-2 / FE-s-5 shape (a not-yet-handed face amended by its issuer, recorded on the channel). Nothing in the decomposition changed; the cell's rectangle already covered the Global permitted-set path. Carried to L10: whether the one-line edge fix beside index.mjs:390 is worth a CLOUD_OPS_OR_ETL act in round 2 once the roster path is measured."
  },
  {
    "id": "IRPT_BCKEND-S9",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T01:57:50Z",
    "one_line": "DISARM of IRPT_BCKEND-W2-S9 and IRPT_BCKEND-W2-S10 (disarm_owner 2.0.0_SA_COO~B), the same drain they merged in (3cca035c66). W2-S9: the firm id has two spellings (registry id in X-Firm-Id and _keys; opaque id in DirectoryEntry and the _scope cross-firm filter) and a handler that joins on the header value serves an EMPTY population that reads as a revocation -- visible only at the join, invisible to every per-module test. W2-S10: _keys.KeyComponentRefused names the refused value in its message, so str(exc) anywhere is a disclosure of a client name or e-mail. The issuer amended the EIGHT un-handed faces (IB-s-4, 7, 9, 10, 14, 15, 16, sb-3) with one block and one acceptance arm: every handler wrapped by _authz.guard() with unguarded_routes() printed 0 of N; every firm-scoped read bound through _authz.FirmBinding with a non-reconciling binding REFUSED (FIRM_BINDING), never empty; no _keys exception text in any response, log, audit row or print, with a whole-envelope assertion. Two facts carried to L10 rather than fixed mid-round: the directory and performance handlers (IB-s-1, IB-s-11) merged BEFORE the wrapper existed -- a sequencing defect of the decomposition (s.1 said the library lands before the handlers ship; the chains did not enforce it) -- and IB-s-17's _keys exception text is a round-2 item on that cell's surface. The three in-flight faces (IB-s-12 on ~1, IB-s-6 on ~3, IB-s-13 on ~4) cannot be amended and are re-graded for the same two properties by the issuer at their drains.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (this row IS the disarm act for W2-S9 and W2-S10 on every un-handed cell; the merged handlers' unguarded state is measured at IB-sb-3 and carried to L10)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md IRPT_BCKEND-W2-S9, IRPT_BCKEND-W2-S10 @3cca035c66 -- both ARMED, disarm_owner 2.0.0_SA_COO~B",
        "infra/aws/lambda/investor-reporting/_authz/enforce.py @3cca035c66 -- guard(), FirmBinding, unguarded_routes(), the refusal reason built from parameter names",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-{4,7,9,10,14,15,16}.*.md and IRPT_BCKEND.TO-IB-sb-3.*.md (this commit) -- ISSUER AMENDMENT block + arm (amend); every <status> still staged, none handed",
        "org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md v0.1.1 s.1 @3cca035c66 -- 'this half is a shared dependency beneath every handler and must land BEFORE the handlers ship', while s.5's chains seat IB-s-1 and IB-s-11 ahead of IB-s-3"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Decomposition s.1 for IB-s-3: the enforcement library is a shared dependency beneath every handler and lands before the handlers ship. IB-s-3 bounds: client names are never keys; the wrapper never widens.",
    "world_is": "Two handlers shipped before the library; the library's own seams (firm-id spelling, refusal text) are only visible at the join and were found by the cell that made the join. Disarmed forward on every un-handed face; the merged handlers are measured at the replay and carried to L10.",
    "notes": "Amendment shape: FE-s-2 / FE-s-5 (not-yet-handed faces amended by the issuer, recorded on the channel). The decomposition is not edited mid-round; the sequencing defect is the issuer's own L5 finding for the round-2 recut."
  },
  {
    "id": "IRPT_BCKEND-S10",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T03:12:00Z",
    "one_line": "DISARM of IRPT_BCKEND-W1-S7 (ARMED) and IRPT_BCKEND-W1-S8 (BLOCKING), disarm_owner 2.0.0_SA_COO~B, the same drain they merged in (3bed36da5b). W1-S8: the rule-13 first-mint of this project's gold scripts has NO declared bundle in .tools/safe_deploy_core.py CODE_TREES (declared: accrual_bridge only), so both the ordinary push path (SKIP-NOT-MEMBER, W2-S5) and the guard's own explicit escape hatch (--mint-bundle) have no target; head-object on the served code prefix reads 404 for both scripts. The declaration is a DS-lane / tooling act outside every worker's grant and outside this round: the issuer carries it to L10 as a BLOCKING item with that owner, and the IB-s-4 face (the next cell on the directory root, un-handed) is amended so its first-mint arm records BLOCKED-BY-W1-S8 once, without a duplicate row. The schedules those cells apply target Lambda entries whose code Terraform ships by CodeSha256, so the product runs; what is absent is the shared-home copy of the gold scripts. W1-S7: the directory's opaque account ids resolve against the holdings join keys for 49financial (7,431 of 7,453) and for NEITHER other firm (0 of 790 INF, 0 of 946 COT) -- a raw-key selection difference inside directory_runner.build_inf/build_cot that IB-s-12 could not trace inside its budget. IB-s-4 re-builds the directory, so its face gains a Phase-1 trace (which raw key each firm's opaque_id derives from, file:line @ commit) and an arm (i) that prints per firm N of M snapshot ids resolved against the refreshed directory; no join is changed mid-round, the fact goes to the CTO at L10.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (this row IS the disarm act: W1-S8 becomes an L10 BLOCKING item owned by the DS lane / tooling owner; W1-S7 becomes IB-s-4's traced fact, graded at that drain)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md IRPT_BCKEND-W1-S7, IRPT_BCKEND-W1-S8, IRPT_BCKEND-W2-S5 @3bed36da5b",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_s_12.result.md @3bed36da5b -- the mint refusal and the 404 printed beside the three landed QA snapshots",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-4.directory-freshness-driven-on-a-controlled-clock.md (this commit) -- ISSUER AMENDMENT block + arm (i); <status> still staged, unhanded",
        "memory: feedback_a_decomposition_that_covers_every_code_cell_can_still_leave_the_deploy_step_unowned -- the shape, recurring: COMMITTED is not SERVED and the first-mint had no owner in the decomposition"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Rule 13: DS owns commit-to-QA-deploy for data/*/scripts/gold/*.py; safe-deploy.sh: first-mints stay explicit. IB-s-12 / IB-s-4 issuer amendment: the first-mint is attempted through the guard's explicit mechanism and verified by artifact.",
    "world_is": "The explicit mechanism has no declared target for this project's gold home, so no worker in this round can land the shared-home copy; the served code prefix reads 404 for both scripts while the Lambdas that run them are converged. The directory and holdings id spaces coincide for one firm of three.",
    "notes": "Two decisions recorded here rather than made silently: (1) the issuer does NOT declare the bundle mid-round -- it is a tooling edit under another lane and the only off-spec act available to this seat is a row; (2) IB-s-4's arm (h) is read as BLOCKED-BY-W1-S8 rather than re-filed, so the channel carries one BLOCKING row for one defect. Carried to L10 with the sequencing defect of S9 and the execution-role trust question of W3-S3."
  },
  {
    "id": "IRPT_BCKEND-S11",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T03:20:41Z",
    "one_line": "PRD MOVED TO v0.8 @d67e9813b5 MID-ROUND (v0.5 at 00:54Z, v0.6/v0.7/v0.8 through 03:09Z; 1.0.0_SA_CTO 95705 and 95751, information only) and the CTO left the amend-at-drain versus re-cut-in-round-2 decision to this lane. Decision, recorded: round 1 stays FROZEN on v0.4 @62301f71e0 for every cell's RECTANGLE and for every handed face; the ONE un-handed face whose cell the delta measures against live vendor behaviour -- IB-s-9, the YCharts generation chain -- is amended in the FE-s-2 / FE-s-5 shape with the v0.5 REST decision table and the v0.8 measured working contracts (upload field `holdings`; save fields `portfolio`/`items`; the full 201 payload vs the 404 minimal payload as a contract failure; fee 0 -> 422; empty sections legitimate; 26.76 s job budget; PDF via a separate unauthenticated client) as the SHAPES its replay transport records, plus one arm. Building IB-s-9 to the v0.4 row would have shipped a chain against a contract the estate has already measured to be wrong (the v0.4 row forbade inventing the upload field name that v0.8 now records). The B8 delta (session broker, isolated secret, fence, K3 controller) is NOT amended in: IB-s-8 is complete at 95a34541f8 on v0.4 and its delta, with B16/B17's, is round-2 material for the CTO's L10 analysis; the LIMB 6 gate refuses a NEW order against v0.8 until CRO and CVO re-sign, and no new order is cut here.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (the decision is this lane's by the CTO's own words; the re-sign of v0.8 is 4.0.0_SA_CRO's and 3.0.0_SA_CVO's; the round-2 recut of B8/B16/B17 is the L10 read)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/mcp/inbox/2.0.0_SA_COO/~B/read/20260911T005445Z_1.0.0_SA_CTO_INFORMATION__IRPT_BCKEND_PRD_is_at_v0.5_.md (msg 95705) and ...20260911T030903Z_..._v0.8_.md (msg 95751) -- 'the amend-at-drain versus re-cut-in-round-2 decision is the lane's'",
        "org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md @d67e9813b5 line 117 -- the B9 row with its (v0.5, SUPP IV.7/IV.8/III.2) and (v0.8, SUPP VI.5) additions, read by git show",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-9.the-ycharts-generation-chain-as-an-opal-async-job.md (this commit) -- ISSUER AMENDMENT block + arm (v0.8); <status> still staged, unhanded; PRD pin line unchanged at v0.4",
        "org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md (HEAD) -- mid-round the spec and the decomposition are frozen; the decomposition v0.1.1 is NOT edited by this amendment"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Spine v3: mid-round the spec AND the decomposition are FROZEN; the only off-spec act is a surprise row. CLAUDE.md L4-R: the L4 notifier withholds the COO delivery until CRO and CVO sign at the current prd_version.",
    "world_is": "The PRD advanced four versions during the round on Andrew's word at the CRO terminal; the delta is measured vendor behaviour that one un-handed cell would otherwise build against wrongly. The amendment carries measured shapes into that face without touching its rectangle, the decomposition or any handed face.",
    "notes": "Recorded so the CVO's L8 compile and the CTO's L10 read see the decision and its scope in one place: amended IB-s-9 only; IB-s-8 (complete), IB-s-16 and IB-s-17 (B16/B17 deltas) carried to round 2. The v0.8 cloud packet is named as read-only reuse, never as a write surface."
  },
  {
    "id": "IRPT_BCKEND-S12",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T03:24:38Z",
    "one_line": "PRD v0.9 @86bde3ea26 (1.0.0_SA_CTO 95756, Andrew-direct ~03:1xZ: the proven YCharts cloud chain is FWD-4's FIXED mechanism, same shape as the 09-10 runner-STYLE constraint) folded into the un-handed IB-s-9 face as one more line of the S11 amendment: the generation transport IS the packet's cloud_transport.py extended (B9 BUILDS ON it), never a parallel transport and never the stopped-host SSM dispatch as the primary path; the Lambda holds the fenced session by name and replays REST; EC2 capture and fencing are B8's (round 2) and are stubbed here; v0.9's arm (5) -- Comparison and Multi-Comparison replayed LIVE -- is a live vendor call and stays the L10 qualified read on Andrew's per-use word. Consequence for the round the issuer states plainly: IB-s-8 (complete on v0.4, the stopped-host runner) is now the wrong mechanism by Andrew's word and is a round-2 RECUT, not a repair; IB-s-9's rectangle (seven-step chain, offline proof) is unchanged and the cell is still handed after IB-s-7 merges.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (folded same turn; the B8 recut is the CTO's L10 analysis)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/mcp/inbox/2.0.0_SA_COO/~B/read/20260911T032054Z_1.0.0_SA_CTO_INFORMATION__IRPT_BCKEND_PRD_v0.9__86bde.md (msg 95756) -- 'the mechanism is FIXED, not a build choice'; 'B9 BUILDS ON cloud_transport.py; arm (5)'",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260911_031xZ_YCHARTS_CLOUD_PROOF_IS_THE_BACKEND_FLOW_FRONTRUNNER.md -- the record the CTO names",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-9.the-ycharts-generation-chain-as-an-opal-async-job.md (this commit) -- the v0.9 line inside the S11 amendment block; <status> still staged"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Decomposition v0.1.1 s.8 bound 1: NO LIVE VENDOR CALL is authorized by this document; a live arm is an express qualification read by the CTO at L10 on Andrew's per-use word. IB-s-9 L5 note (v0.4): a Lambda dispatching to the runner host over SSM when live.",
    "world_is": "Andrew fixed the mechanism as the browserless Lambda replay of a fenced session; the v0.4 SSM-dispatch primary path is superseded and IB-s-8's runner host is the wrong seat for it. The face now reads the Lambda replay as the primary path on the replay transport; nothing live is run in this round.",
    "notes": "Andrew's word reached this lane as a mechanism constraint through the CTO, not as a per-use live-call authorization; it is relayed at exactly that scope (CLAUDE.md s.2: never convert Andrew's word to one agent into a gate or a widening on another)."
  },
  {
    "id": "IRPT_BCKEND-S13",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T03:38:33Z",
    "one_line": "DISARM of IRPT_BCKEND-W3-S5 (ARMED; the worker disarmed it for its own cell and routed the fallback's meaning to the issuer). The issuer's (amend) arm of 812bbec0e9 named `routes.json` as the guard census's fallback for a cell that ships no handler, and that file is IB-s-15's deliverable (its face: route keys enumerated in routes.json so IB-sb-3 reads its denominator from a file) -- it does not exist before IB-s-15 lands, so for IB-s-7 the fallback was unsatisfiable and a naive reading would have printed a vacuous 0 of 0 as a pass. The worker's repair is adopted verbatim as the issuer's clarification on the six un-handed faces (IB-s-9, 10, 14, 15, 16, sb-3): the census is printed AS VACUOUS and the arm proves the CENSOR through two controls (an unguarded handler censused 1 of 1; the same handler wrapped 0 of 1); IB-s-15 and IB-sb-3 read the real file. Also carried: W3-S6 -- the face's and the PRD row's `needs-correction` is the contract's closed-enum `NEEDS_CORRECTION`; the contract's spelling is the one emitted.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (this row IS the disarm act; a cut defect of the issuer's own amendment, corrected on every face it can still reach)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md IRPT_BCKEND-W3-S5, IRPT_BCKEND-W3-S6 (this HEAD)",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-15.scoped-routes-opal-principal-and-the-cloudfront-behavior.md THE CELL -- 'Route keys ... enumerated in routes.json so the replay battery (IB-sb-3) reads its denominator from a file'",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_s_7.result.md (this HEAD) -- the vacuous census printed as such and the two controls",
        "the six faces (this commit) -- one sentence appended to the (amend) arm; every <status> still staged"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Issuer (amend) arm @812bbec0e9: 'Where this cell ships no handler, the same census runs over routes.json at the replay.' Memory: a gate called with an EMPTY input set returns a vacuous pass that reads as clean.",
    "world_is": "The named fallback object is a future artifact of another cell; for every handler-less cell handed before IB-s-15 the arm's only honest reading is the censor's own controls. The amendment named the right hazard and the wrong object.",
    "notes": "Adopted the worker's repair rather than inventing a second one; the faces already handed (IB-s-4 on ~2) carry the old sentence and are re-graded by the issuer at their drain under this reading."
  },
  {
    "id": "IRPT_BCKEND-S14",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T04:05:41Z",
    "one_line": "PRD v0.10 @3624e60def (1.0.0_SA_CTO 95780, 04:03Z) landed MINUTES AFTER IB-s-9 was handed to slot ~3 at 1f795d1f71: all three YCharts recipes proven live in one Lambda by the CRO on Andrew's word (VI.6 @72acd16e66), and B9 now BUILDS ON docs/research/investor_reporting_ycharts_variants_20260911/{recipe_contract.py,variant_worker.py,UI_CONTRACT.md,manifest.example.json} -- recipe selected from the comparison COUNT (0 Overview / 1 Comparison / 2-5 Multi), two wire shapes, one handler, duplicate re-delivery without a vendor call, input/account controls before vendor access, WAF refresh and unknown-mutation reconciliation the coordinator's. The face on the worker's branch cannot be amended (its grant is read from ITS HEAD), so the issuer sent the worker ONE supplement by the harness resume channel naming the packet as the reuse source to read FIRST and stating that the rectangle, criteria, paths and the no-live-call bound are unchanged; this row is the record of that supplement so the change is not only in a message. Carried to round 2, not amended in: B2's Generate resolver (server-only `resolved` half of the job envelope; IB-s-2 is complete), the AnalysisRequest browser-request half (IB-s-18's contracts are complete), and the v0.10 NOT-yet-proven list (public-ETF / mixed comparisons, the five-comparison maximum, percent uploads, real tenant entitlement, autonomous recovery, publication fencing).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (supplement sent same turn; the round-2 items are the CTO's L10 analysis after CRO/CVO re-sign v0.10)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/mcp/inbox/2.0.0_SA_COO/~B/read/20260911T040336Z_1.0.0_SA_CTO_INFORMATION__IRPT_BCKEND_PRD_v0.10__3624.md (msg 95780)",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-9.the-ycharts-generation-chain-as-an-opal-async-job.md @1f795d1f71 -- handed 03:4xZ; the v0.9 amendment already names the transport packet",
        "docs/research/investor_reporting_ycharts_variants_20260911/ (HEAD) -- the packet the supplement names as read-only reuse"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Spine v3 L7: the TO's WORKER FACE is the worker's whole context; a worker cannot be messaged. CLAUDE.md s.2: a broker message is never the carrier of an off-spec fact.",
    "world_is": "The issuer used the same harness resume channel that carries every hand-off to send one bounded supplement to a worker mid-order, because the PRD delta names a reuse source the cell would otherwise rebuild; the record of it is this row, and the worker's own report will say what it read.",
    "notes": "Stated as a deviation so the CVO can grade it at L8: the alternative (let the cell build on v0.9's packet alone and recut in round 2) was judged the more expensive correct path; the supplement adds a reuse source and changes no criterion."
  },
  {
    "id": "IRPT_BCKEND-S15",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T04:14:43Z",
    "one_line": "DISARM of IRPT_BCKEND-W2-S11 (ARMED, disarm_owner 2.0.0_SA_COO~B), the same drain it merged in: a THIRD id spelling -- HoldingsSnapshot namespaces account ids (`<firm>:acct:acc_...`) while DirectoryEntry carries the bare tail -- makes a naive join read 0 of N for all three firms and so hides W1-S7's real raw-key difference (INF, COT) behind a cosmetic prefix difference (every firm). Disarmed forward on the four un-handed faces that can join holdings to the directory (IB-s-14, IB-s-15, IB-s-16, IB-sb-3): normalise through the ONE normaliser IB-s-4 shipped (import, never a second strip) and print both counts per firm, as-written and after normalisation, so the two causes stay distinguishable. No join changed; the canonical spelling is the CTO's L10 read together with W1-S7. Residual carried: 17 of 5,873 49F ids (0.3 percent) unresolved after normalisation, unexplained.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (this row IS the disarm act; the canonical-spelling decision is L10's)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md IRPT_BCKEND-W2-S11, IRPT_BCKEND-W1-S7 (this HEAD)",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_s_4.result.md (this HEAD) -- arm (i): 5,856 of 5,873 / 0 of 790 / 0 of 946 after normalisation; the positive control that refused 0 of 3",
        "the four faces (this commit) -- one line inside the S9 amendment block; every <status> still staged"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD B1/B12 (v0.4): one opaque id space per firm minted by directory_runner.opaque_id; IB-s-12 L5 note: HoldingsSnapshot objects schema-valid against the contract.",
    "world_is": "Two artifacts of the same project spell one account id two ways (prefix vs bare), and a third firm-dependent difference sits beneath. The wrong conclusion is the cheaper one in both directions; the faces now force both counts to be printed.",
    "notes": "Third id-space finding this round after W2-S9 (registry vs opaque firm id) and W1-S7 (raw key per firm); the round-2 recut should carry ONE id-space table for the project, an L5 deliverable of this seat."
  },
  {
    "id": "IRPT_BCKEND-S16",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T04:59:17Z",
    "one_line": "L4 HAND-OFF RELEASED at PRD v0.13 @e6ba5d9878 with both L4-R sign-offs (1.0.0_SA_CTO 95827; the notifier's COO row went to the base inbox that has no session, so the lane message is the delivery). Round 1 stays frozen on v0.4 for every rectangle. Diffed v0.13 against v0.10 by candidate row: only B10 and B14 changed (v0.11, CRO R2), and the change is an AVAILABLE INPUT, not a new obligation -- the three synthetic vendor PDFs (Overview 23 pp / Comparison 31 pp / Multi-Comp 35 pp on synthetic portfolio 2332257) are RETAINED, KMS-encrypted, at s3://opal-data-ycharts/research/20260911/variants/.../report.pdf with SHA-256s in the packet's pdf_validation.json (measured: the repo packet holds receipts only, no PDF bytes; cleanup.json lists the PDFs among the retained artifacts). Folded into the two un-handed faces IB-s-10 and IB-s-14 in the FE-s-2 / FE-s-5 shape: the PDFs as input specimens beside the synthetic ones (hash-verified before use, labelled vendor_synthetic_holdings, an Opal S3 read and never a vendor call), one arm each (v0.11); every existing arm unchanged; real-client specimens remain the FWD-4/FWD-8 proof gap. v0.12/v0.13 (CRO R1, CVO C1) touch no candidate row this round still builds.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (folded same turn; the KMS/IAM readability of the research prefix under a worker serial is unmeasured until IB-s-10 runs and is bounded by the amendment's own refusal clause)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/mcp/inbox/2.0.0_SA_COO/~B/read/20260911T045421Z_1.0.0_SA_CTO_L4_HANDOFF_RELEASED__IRPT_BCKEND_PRD_v0..md (msg 95827)",
        "org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md @e6ba5d9878 rows B10, B14 -- the (v0.11, CRO R2) clauses; diff against @3624e60def by row in the issuer's scratch",
        "docs/research/investor_reporting_ycharts_variants_20260911/{pdf_validation.json,cleanup.json,README.md} (HEAD) -- the three SHA-256s, the retained-artifacts list, the S3 prefix",
        "the two faces (this commit) -- ISSUER AMENDMENT block + arm (v0.11); <status> still staged"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "IB-s-10 face (v0.4): 'No real YCharts PDF exists (row IRPT_BCKEND-S5)'; PRD v0.13 B10: 'AVAILABLE: the three SYNTHETIC vendor PDFs ... sufficient to BUILD and exercise the extractor'.",
    "world_is": "Row S5's premise (no real vendor PDF) is no longer true for synthetic holdings; it remains true for client holdings. The faces now carry both facts and grade the extractor on both kinds of input.",
    "notes": "The gate now admits a NEW IRPT_BCKEND order against v0.13; none is cut mid-round. The round-2 recut reads v0.13 whole."
  },
  {
    "id": "IRPT_BCKEND-S17",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T05:14:36Z",
    "one_line": "ISSUER RE-SEQUENCING at 05:1xZ on Andrew's question ('what's holding you up?'): the six remaining cells form ONE sequential chain through slot ~3 by the decomposition's edges (9 -> 10 -> 14 -> 16 -> 15 -> sb-3), so three slots idle while IB-s-9 runs. The edge IB-s-10 -> IB-s-14 exists for ONE arm, S14-AC1 (f) (the Analysis export renders IB-s-10's certified sections), and the IB-s-14 face ALREADY admits the fixture-sections path for it ('where IB-s-10's sections have landed on CLOUD; otherwise the fixture sections, and say which', arm (v0.11) at e34e09a88d), while its other six mechanical arms and its deploy depend on nothing un-merged (IB-s-13, IB-s-17 merged). IB-s-14 is therefore HANDED NOW to slot ~4 ahead of IB-s-10's merge: arm (f) and arm (v0.11) run on the fixture sections and SAY SO; the re-run on IB-s-10's real sections is IB-sb-3's replay (which already re-runs every deployed route) and is named there. The decomposition is not edited (frozen); the chain order is the issuer's L6 fan-out to re-derive, and this row is the record. The same reasoning does NOT free IB-s-16 (it consumes IB-s-9's job status shape and IB-s-14's receipts, both un-merged) or IB-s-15 (routes to Lambdas that do not exist yet).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (the fixture-vs-real sections distinction is printed by the worker and re-graded at the drain; the real-sections run lands at IB-sb-3)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md v0.1.1 s.5 (HEAD) -- edges IB-s-10 -> IB-s-14, IB-s-13 -> IB-s-14, IB-s-17 -> IB-s-14",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-14.export-bundle-freeze-render-worker-receipt.md @e34e09a88d -- arm (f) and arm (v0.11) with the fixture-sections clause; <status> staged with the cross-slot wait on IB-s-10 named",
        "ListAgents 05:1xZ -- one worker subagent running (slot ~3, IB-s-9, started ~1 h earlier); slots ~1, ~2, ~4 idle"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "IB-s-14 face <status>: 'becomes pending when the COO hands it over after IB-s-13 is terminal and merged AND IB-s-10 (slot ~3) is terminal and merged.' Spine v3 L6: fan-out derived from the decomposition's dependency chains.",
    "world_is": "The wait on IB-s-10 guards one arm that the face already lets run on fixtures; holding the whole cell for it idles a slot for hours. Handed early with the substitution stated; the real-sections arm is the replay's.",
    "notes": "Cost of being wrong: one arm re-run at IB-sb-3, which re-runs anyway. Cost of waiting: the export Lambda, its root, its ledger and six arms idle behind a sequential chain. Andrew's question was the trigger; the decision and its record are the issuer's."
  },
  {
    "id": "IRPT_BCKEND-S18",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T05:52:27Z",
    "one_line": "TWO ISSUER FACTS at the IB-s-9 drain (7799dcfb10), on Andrew's word 'keep it moving'. (1) RE-SEQUENCING, same shape as S17: IB-s-16 is handed to idle slot ~1 ahead of IB-s-14's merge. Its seven recovery arms are driven on the DEPLOYED jobs of IB-s-6, IB-s-9 and IB-s-12 (all merged and live) and IB-s-14 (in flight on slot ~4, re-sequenced itself); the arm(s) that target the export job run on a labelled in-process STAND-IN of the export worker and say so, and arm (e)'s manifest-completeness census is taken at this HEAD with the export cell's entries named as the known delta -- both re-measured at IB-sb-3's replay. IB-s-15 stays held: its routes target Lambdas that do not exist until IB-s-14 and IB-s-16 land. (2) AN ISSUER DEFECT, recorded so the record does not read better than what happened: during the IB-s-9 drain the shared index held another seat's open-deploy sentinel for 500 s, so the drain was run through a temporary linked worktree (guarded merge, same union, commit 53965f4f38) and CLOUD fast-forwarded to it; the ff failed because 0.7.0_AE_CloudOps had committed 36422d66d4 in between, and the failure was MASKED by a pipe (`git merge --ff-only ... 2>&1 | tail -2`, the banked pipeline-rc trap), so the chain continued, deleted the temp branch and the worker branch, and re-cut slot ~3 from the wrong tip. Both commits were still in the object store; the worker branch was restored at 183d5241d0, the drain re-run on the new tip (7799dcfb10, guarded, unions identical) and the ff checked by exit code. Nothing was lost; 53965f4f38 is an orphaned merge commit. Cost: ~10 minutes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (the stand-in arm is printed by the worker and re-graded at the drain; the ff-race procedure now checks rc without a pipe)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-16.operations-status-envelope-and-per-tenant-recovery.md (HEAD) -- L5 note: 'The seven recovery arms, driven on the DEPLOYED jobs of IB-s-6 (intake), IB-s-9 (generation), IB-s-12 (holdings) and IB-s-14 (export)'",
        "git log 7799dcfb10 -- parents b30839715c + 183d5241d0; 53965f4f38 orphaned (parents 5701c5c3ce + 183d5241d0)",
        "memory: reference_a_pipelines_exit_status_is_its_last_commands_so_cmd_pipe_tail_always_reads_rc_0 -- the banked trap this seat hit"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "IB-s-16 <status>: 'becomes pending ... after IB-s-6, IB-s-9, IB-s-12 and IB-s-14 are all terminal and merged.' CLAUDE.md Git: never compose the report of an act in the same call as the act; a pipeline's rc is its last command's.",
    "world_is": "Three of four target jobs are deployed; holding the whole cell for the fourth idles a slot behind a sequential chain. Handed with the substitution stated. The drain procedure had one pipe too many and it cost a re-run, not data.",
    "notes": "Andrew-direct 2026-09-11 ~05:2xZ: 'we can't get held up on this shit, keep it moving' -- the trigger for both re-sequencings (S17, S18); the substitutions are stated, not hidden, and the replay is where they are re-measured."
  },
  {
    "id": "IRPT_BCKEND-S19",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T06:54:42Z",
    "one_line": "DISARM-BY-CARRY of IRPT_BCKEND-W4-S9, W4-S10, W4-S12 and W4-S13 (all ARMED, disarm_owner 2.0.0_SA_COO~B) at the IB-s-14 drain. All four are product decisions outside every un-handed face's paths and outside this round: W4-S9 the deployed export worker cannot render (no headless browser in a python3.12 Lambda; egress refused) and says so explicitly -- the runtime choice (container image / browser layer / out-of-Lambda worker) is the CTO's L10 read and the first round-2 cell of FWD-8; W4-S10 the irpt-common layer carries 2 of 5 contracts and its rebuild is IB-s-13's surface (round 2, one line in build_layer.py plus a re-apply); W4-S12 a retry of a byte-identical bundle mints a new export_id because every PDF print engine stamps a date and /ID -- whether a retry reuses the receipt keyed on bundle_sha256 is the job-table owner's decision (IB-s-17's surface, round 2), and the stable identity of an export is the BUNDLE hash; W4-S13 four synthetic objects sit in the live evidence bucket under firms/49financial/generations/GENIBS14SYN/ with irpt-synthetic=true metadata -- an S3 delete needs a human's word and is not taken by this seat; carried to L10 with the keys so the CTO or Andrew can order the delete or relocation before any consumer reads that prefix as client evidence. Forward disarm: IB-s-15 and IB-sb-3 faces gain one line -- the export route is graded on the function's absence report, not on a render.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (this row IS the disarm act by carry; the four decisions are the CTO's L10 analysis, the S3 delete is Andrew's or the CTO's word)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md IRPT_BCKEND-W4-S9..S13 (this HEAD)",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_s_14.result.md (this HEAD) -- the absence report, the content-hash vs raw-digest print, the four object keys",
        "the two faces IB-s-15, IB-sb-3 (this commit) -- one line inside the S9 amendment block; <status> still staged"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD B14 (v0.4): render worker executing the counterpart's RenderPackage; download reauthorized even when the artifact exists. IB-s-14 S14-AC1 (a): the rendered PDF's content hash equal between render and retry.",
    "world_is": "The mechanism is proved locally and the deployed function honestly reports it cannot render; the round's evidence bucket carries four labelled synthetic exports. Nothing here is hidden; each item has a named owner past this seat.",
    "notes": "FWD-8 cannot grade REALIZED on this round's evidence: the rendering runtime is the gap, stated as such for the slug."
  },
  {
    "id": "IRPT_BCKEND-S20",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T07:35:25Z",
    "one_line": "ROUTING of IRPT_BCKEND-W3-S12 (ARMED; disarm_owner '2.0.0_SA_COO~B to route and IB-s-17's assignee to repair') at the IB-s-10 drain: `_keys.s3_evidence_key` lets a client display name or an e-mail address into a durable S3 key while its docstring claims the opposite and `cache_key` in the same module refuses both -- the asymmetric hazard is that an S3 key is logged everywhere and cannot be un-logged. Routed as the issuer's SECOND round-2 item on IB-s-17's surface (with the sanitised exception of W2-S10), and disarmed forward on the two un-handed faces (IB-s-15, IB-sb-3): every S3 key built or replayed passes a shape check before the grammar, and the replay censuses observed keys for name- or e-mail-shaped components with a hit as FAIL. Also carried from this drain: W3-S10 (undecoded cid glyphs in the vendor PDFs: `fi` reads `(cid:45)` on 89 of 89 pages and the same glyph maps differently across documents from one run -- the extractor refuses such tokens; the CVO's judgment item) and W3-S11 (the AnalysisReport contract requires `as_of_date` on every section item while the vendor Comparison and Multi date 34 of 81 and 51 of 108 rows only -- undated rows are held out and counted; one optional `date_claim` enum on IB-s-18's contract is the round-2 proposal).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (routing done; the repair is IB-s-17's round-2 surface, the contract field IB-s-18's, the glyph map the CVO's L9 read)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md IRPT_BCKEND-W3-S10, W3-S11, W3-S12 (this HEAD)",
        "infra/aws/lambda/investor-reporting/_keys/keys.py s3_evidence_key vs cache_key (this HEAD) -- the asymmetry the worker measured",
        "the two faces IB-s-15, IB-sb-3 (this commit) -- one line inside the S9 amendment block; <status> still staged"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "IB-s-3 bounds: client names are never keys. _keys.s3_evidence_key docstring: 'Each is validated by shape, so a client name cannot become a path.'",
    "world_is": "The cache key refuses a name; the S3 key accepts it. The docstring describes the cache key's behaviour on the S3 key's function. Forward-disarmed at the two consumers this round can still reach; repaired at the source in round 2.",
    "notes": "Third _keys finding of the round (W2-S10 exception text, W2-S9/W2-S11 id spellings around it, now W3-S12); the round-2 recut owes IB-s-17 one consolidated order."
  },
  {
    "id": "IRPT_BCKEND-S21",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T08:37:23Z",
    "one_line": "DISARM of IRPT_BCKEND-W1-S9 (ARMED, disarm_owner 2.0.0_SA_COO~B) -- an ISSUER DEFECT: the S15 amendment (902ea877dc) told four faces to normalise holdings account ids 'through the ONE normaliser IB-s-4 shipped under infra/aws/lambda/investor-reporting/directory/'. No such module exists; IB-s-4 normalised the `<firm>:acct:` prefix inside its own battery (battery_ib_s_4.py), and the issuer wrote the amendment from the worker's report rather than from the tree (a grader's restatement lending a claim it had not earned). IB-s-16 found it (function-name enumeration of directory/handler.py, refresh.py, expiry.py; git show 624a60e4fc --stat) and needed no such join. Measured now: the prefix is minted at holdings_snapshot.py:370 (49f), :486 (inf), :638 (cot) as `<firm>:acct:<opaque>` and nowhere else in the lambda tree (comp-find 'acct:' 7 hits of 260 files, 3 SURFACED, all in the runner). The two un-handed faces (IB-s-15, IB-sb-3) are corrected: strip exactly that grammar in one named function of the consumer's own, cite the three lines, print both counts. IB-s-14 and IB-s-16, already complete, carried the false sentence; neither made the join (IB-s-14 exports from fixture sections; IB-s-16 measured the absence), so no output is affected.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (corrected on every face it can still reach; the shared normaliser is a round-2 item alongside the id-space table of S15)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md IRPT_BCKEND-W1-S9 (this HEAD); IRPT_BCKEND-S15 @902ea877dc (the defective sentence)",
        "data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:370,486,638 (HEAD) -- the three mint sites",
        "comp-find 'acct:' over infra/aws/lambda/investor-reporting, the project's deliverables and the gold home: 7 hits across 260 files, 3 SURFACED (the runner), 0 in directory/",
        "the two faces (this commit) -- the sentence replaced in place; <status> still staged"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Seat row S15: 'normalise through the ONE normaliser IB-s-4 shipped under infra/aws/lambda/investor-reporting/directory/'. Memory: a grader's restatement lends credibility the claim has not earned.",
    "world_is": "The normaliser was a battery-local helper, not a shipped module; the amendment named a path that does not carry it. Corrected before either remaining consumer reads it.",
    "notes": "Issuer's own lapse, stated plainly: an amendment that names a path must be written from a read of the tree at HEAD, not from a report about it."
  },
  {
    "id": "IRPT_BCKEND-S22",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T09:22:01Z",
    "one_line": "ROUTING of IRPT_BCKEND-W2-S12 (BLOCKING, disarm_owner 2.0.0_SA_COO~B) at the IB-s-15 drain (ac2ee67133). IB-s-15's STOP fired correctly: the portal-auth plan reads 'Plan: 0 to add, 3 to change, 0 to destroy'. The issuer re-ran the plan read-only in the same worktree and CLASSIFIED the two foreign changes from the saved diff: (1) aws_cloudfront_function.spa_fallback -- a CRLF checkout artifact (26 CRLF on disk vs 0 in the HEAD blob; the banked fresh-worktree trap), which clears for any actor whose checkout renders the file LF; (2) aws_wafv2_web_acl.opal_cloudfront_protection -- three managed-rule blocks (common-rule-set p4, ip-reputation p3, known-bad-inputs p5) removed and re-added with EVERY value identical and the only difference an attribute hidden in state ('# (1 unchanged attribute hidden)' inside managed_rule_group_statement, absent from the config) -- a provider-normalisation diff under hashicorp/aws 5.100.0 (lock tracked), NOT intended drift; an apply would still issue UpdateWebACL on the WAF fronting all 27 behaviors. NEITHER is this project's: the root is lane CLOUD_OPS_OR_ETL and NEVER-1 puts a served-output move behind CTO+COO sign-off. Disposition: the ONE additive behavior stays committed and unapplied on CLOUD; the two-line remedy (declare the hidden attribute in the WAF config so the root plans clean, or apply the no-op under sign-off) belongs to the portal-auth root's owner, and the issuer puts the classified plan in front of 1.0.0_SA_CTO and 0.7.0_AE_CloudOps as information. FWD-2's EXERCISED bar therefore lacks the CloudFront -> edge leg this round; IB-sb-3 replays on API Gateway's invoke URL through the real naqxlm authorizer and names the boundary it could not cross. S15-AC1 stays FAIL, the order stays OPEN, and the round's L10 slug carries it as its second BLOCKING item.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (routed; the remedy is the portal-auth root owner's under CTO+COO sign-off; re-plan and apply of IB-s-15's behavior follows, no rework)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md IRPT_BCKEND-W2-S12 (this HEAD) -- the worker's measurement, get-distribution-config byte-identical before and after",
        "issuer's read-only re-plan in /c/tmp/wk-irpt-1-2 at 1d61219844 (scratch pa_plan_wk.txt): 'Plan: 0 to add, 3 to change, 0 to destroy'; the WAF block shows six rule blocks, three '-' and three '+', pairwise identical on name, priority, override_action count, managed_rule_group_statement name/vendor_name, visibility_config; '# (1 unchanged attribute hidden)' only on the removed side",
        "infra/aws/terraform/portal-auth/.terraform.lock.hcl (tracked): hashicorp/aws 5.100.0, constraint ~> 5.0",
        "CLAUDE.md NEVER-1: never move served output without never-widen sign-off (CTO+COO)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "IB-s-15 face: 'The CloudFront plan shows exactly ONE change or you STOP ... any other change in that plan is a STOP and a BLOCKING row.' PRD B15: an Opal principal reaches clients at two firms through scoped routes.",
    "world_is": "The routes are live behind the authorizer; the portal path to them is one unapplied behavior away, held by a foreign root's normalisation diff. Nothing served has moved. The replay measures what exists and names the leg it cannot exercise.",
    "notes": "Two BLOCKING items now carry to L10 with owners: W1-S8 (first-mint bundle, INFRA.TOOLS + DS) and W2-S12 (portal-auth root, CLOUD_OPS_OR_ETL under sign-off). Both are one act each for their owners; neither is a rework of this round's cells."
  },
  {
    "id": "IRPT_BCKEND-S23",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T09:37:45Z",
    "one_line": "DISARM of IRPT_BCKEND-W2-S12 (BLOCKING) by the CTO's ruling 95933 and both never-widen sign-off halves. 1.0.0_SA_CTO, as the gate over the portal-auth root (0.7.0_AE_CloudOps has no live session), measured in the shared tree: the CRLF half is closed at b9b3eafb6b (.gitattributes eol=lf for infra/aws/terraform/**/*.js); the WAF half is a hashicorp/aws 5.100.0 read-normalisation artefact (managed_rule_group_statement.version '' in the refreshed read vs null in config and state serial 173; everything else byte-identical by terraform show -json; live get-web-acl has no Version; CloudTrail shows no UpdateWebACL since the 09-03 opsec applies), recurring on every plan until the provider is bumped (CTO item 4, owner 0.7.0_AE_CloudOps, gate CTO, a D0 s.6 row). RULING: IB-s-15's bound is widened FOR THIS APPLY ONLY to 'one change plus the classified WAF no-op'. CTO half in 95933; COO half at org/tier1_exec/2.0.0_SA_COO~B/deliverables/NEVER_WIDEN_SIGNOFF_COO_HALF_IRPT_BCKEND_IB-s-15_CLOUDFRONT_20260911.md (blast radius and rollback per key, writers counted N=1, both outcome branches). The OPEN face is amended with the widened bound and the verifications the apply must print (27 -> 28 behaviors with the prior 27 in order; get-web-acl Rules identical LockToken excepted; the unauthenticated request now 401/403); slot ~2 is re-cut from a HEAD carrying b9b3eafb6b and the apply is handed back as IB-s-15's own act through safe-apply under a ledger entry citing the first.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (the COO half signed; the apply is the worker's under both halves; the provider bump is the CTO's D0 item)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/mcp/inbox/2.0.0_SA_COO/~B/read/20260911T093348Z_1.0.0_SA_CTO_IRPT_BCKEND-W2-S12_RULED__CTO___the_WAF_.md (msg 95933) -- the ruling, the CTO half, items 1-4",
        "b9b3eafb6b (CLOUD) -- .gitattributes: infra/aws/terraform/**/*.js text eol=lf",
        "org/tier1_exec/2.0.0_SA_COO~B/deliverables/NEVER_WIDEN_SIGNOFF_COO_HALF_IRPT_BCKEND_IB-s-15_CLOUDFRONT_20260911.md (this commit) -- the COO half",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-15.*.md (this commit) -- ISSUER AMENDMENT on the open face; <status> pending"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md NEVER-1: never move served output without never-widen sign-off (CTO+COO); a sign-off names the act's blast radius and counts the writers of the named property. IB-s-15 face: exactly ONE change or STOP.",
    "world_is": "The foreign change is a content-identical provider read artefact, pinned by three instruments; both halves are signed on the two keys the act may touch; the STOP condition stays armed for anything else in the plan.",
    "notes": "The bound's STOP produced exactly the classification the sign-off needed; widening it once, for one apply, under two signed halves is the mechanism working, not the bound bending."
  },
  {
    "id": "IRPT_BCKEND-S24",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T10:22:42Z",
    "one_line": "ROUND 1 TERMINAL at f8860a4a4b: 19 of 19 task orders read <status>complete with VALID instances re-graded by the issuer at each drain (denominator: 19 files under task-orders/). DISARM-BY-CARRY of IRPT_BCKEND-W1-S10 (ARMED, disarm_owner 2.0.0_SA_COO~B): IB-sb-3's real-file unguarded_routes() census reads 6 of 11 handler-bearing routes unguarded, not the 3 row S9 disclosed -- the three newly observed are POST /analysis (irpt-ycharts-generate, IB-s-9: job.py's own comment says it registers no route, written before routes.json existed, and IB-s-15 mapped the route to it anyway), GET /narrative/{reportId} (irpt-narrative, IB-s-13: no _authz import), GET /export/{exportId} (irpt-export-render, IB-s-14: the deployed handler implements only action=capabilities). None discloses protected data today, each for its own unrelated reason (a consent gate, a request shape with no identity, an absent operation), so the row is OBSERVATION; it is ARMED because that safety rests on each handler's own behaviour rather than on the wrapper. Every one of the six is a merged cell and outside every remaining face, so the issuer carries it to L10 as ONE round-2 item: `guard()` on the six routes, with IB-s-3's own S3-AC2 judgment ('the wrapper can be bypassed by a handler that forgets to use it') now measured at 6 of 11. The replay also measured the real CloudFront path live: 11 of 11 declared routes refuse unauthenticated (401 with the edge's own error), a forged bearer is refused, and a direct-to-API-Gateway bypass meets API Gateway's own 401 -- the origin-verify secret is a separately enforced gate. Authenticated replay on the real path remains not-run: no test-JWT-minting mechanism a worker may use without a human exists (stated on the instance, arm (a)).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (carried; the six-route guard is the first item of the round-2 recut of FWD-2; the test-principal mechanism is the CTO's L10 read)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md IRPT_BCKEND-W1-S10 (this HEAD)",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_sb_3.result.md @f8860a4a4b -- the 6 of 11 census, the 11 of 11 real-path refusals, the bypass probe",
        "grep -l '^<status>complete' over org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-*.md at f8860a4a4b: 19 of 19"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Issuer amendment @812bbec0e9: every handler this cell ships is wrapped by _authz.guard(); IB-s-3 S3-AC2: whether the wrapper can be bypassed by a handler that forgets to use it -- and how a reader would detect that.",
    "world_is": "The detector IB-s-3 shipped found what it was built to find: three handlers written before the route table existed were mapped to routes after the fact and never revisited. Measured, not repaired, at the last cell of the round.",
    "notes": "The drain is closed: every worktree removed, every branch merged, HEAD f8860a4a4b. The drain-end read to the CTO follows this commit; the slug is the CVO's."
  },
  {
    "id": "IRPT_BCKEND-S25",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T11:59:49Z",
    "one_line": "ROUND 2 ISSUED. On the CTO's round-1 analysis (ledger/ROUND_ANALYSIS.round1.md @0d57ceb2f9: 10 of 10 outcomes served, no addendum, 0 REALIZED, eight rulings) and the CVO's slug (REMEDIATION_v1.md @27e67fa6a5, 25 OPEN rows), the issuer cut decomposition v0.2 and ONE issuance of twelve task orders against PRD v0.13 @e6ba5d9878 (ADMITTED; the L6 gate read both L4-R halves SIGNED on every face): IB-rt-1 seam, IB-rt-2 guard the six + the test principal, IB-rt-3 one opaque-id normalizer + grain, IB-rt-4 typed keys + the exception path, IB-rt-5 the gold first-mint (issued to a DS lane, 0.4.0_DS_ClientPlatform~X, the rule-13 act the CTO's ruling 3(c) opened), IB-rt-6 the refresh builds, IB-rt-7 the holdings handler + attribution holdouts, IB-rt-8 the export worker renders, IB-rt-9 YCharts on the v0.9 mechanism, IB-rt-10 glyphs and dates, IB-rt-11 intake currency/unit controls, IB-rtb-1 the authenticated replay. Landed at 388b8199b8 and merged onto the moved tip at 7478fdf144 (the fast-forward lost a race; pull-merge, never rebase). Coverage: 10 of 10 outcomes, 8 of 8 rulings, 25 of 25 OPEN slug rows closed by a cell or carried by name (W1-S4, W3-S3 to CloudOps with the CTO as gate). Fan-out 5 of 10 chains: the four round-1 worker subagents RESUMED with context intact on IB-rt-3 (~1), IB-rt-1 (~2), IB-rt-4 (~3), IB-rt-8 (~4) from worktrees cut at 7478fdf144; the DS lane seated by /mstr-spawn for IB-rt-5. The round-1 ids are retained in the decomposition's id space so every round-1 instance still aligns. Two new bounds on every face: no self-wrapping harness as evidence; typed issued identifiers at every boundary. One gate note recorded honestly: the DS lane's pointer file in its own task_orders/ home reads as a task order to the announce-mode decomp-ref lint (no <issued_to>, no <decomp_ref>) -- it carries a pipeline-override line naming the tree face as the graded order; if the lint is armed to enforce, the pointer moves out of task_orders/ and the GO names the tree path alone.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (the issuer; the round-2 drain follows the round-1 procedure)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md v0.2 @388b8199b8 -- sections 0 (round 1 retained), 1 (the rectangle), 3 (chain read: 9 edges, 9 heads, 4 leaves, M=10, 4 components, depth 3), 5 (seating + fanout), 7 (battery), 9 (carries)",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-*.md and IRPT_BCKEND.TO-IB-rtb-1.*.md @388b8199b8 -- twelve faces; to-pipeline-gate OK 13 of 13 newly-added with <decomp_ref> and complete <preflight>; L4-R sign-offs OK at v0.13",
        "org/mcp/inbox/2.0.0_SA_COO/~B/read/20260911T111958Z_1.0.0_SA_CTO_ROUND-2_ANALYSIS_IRPT_BCKEND__0d57ceb2f9.md (msg 95954)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Spine v3 L10: the CTO answers with the ROUND-N ANALYSIS the COO recuts in ONE issuance; L6: ONE ISSUANCE covering every cell, fan-out derived from the chains and stated as fanout: data in the issuance commit.",
    "world_is": "The recut is one issuance of twelve cells against the admitted PRD, fanned to five seats including one DS lane for the act no worker may take; round 1's evidence is built on, not rebuilt.",
    "notes": "The DS lane spawn and its GO follow this row in the same turn; the round-2 drain, disarms and the drain-end read follow the round-1 procedure (seat rows continue at S26)."
  },
  {
    "id": "IRPT_BCKEND-S26",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T13:14:24Z",
    "one_line": "DISARM of IRPT_BCKEND-W2-S16 (BLOCKING, disarm_owner 2.0.0_SA_COO~B) by a CRITERION RE-CUT at IB-rt-1's first drain (0e60e9645b). The finding: the eleven v1 schemas are DOCUMENT contracts, two can never be an HTTP response (AnalysisRequest is a queue message; RenderPackage is the frontend's package -- W2-S17), and the six handlers answer in three ad-hoc envelopes, so RT1-AC1 (b) 'the response validates against the producer schema' read 0 of 11 and its remedy lies in handler directories the seam order does not grant. FOUR-PART TEST for the re-cut: (1) the criterion was a PROXY -- it measured handler conformance on the cell that publishes contracts; (2) the substance is preserved -- the seam cell now PUBLISHES the response contracts (responses/<operation>.response.schema.json, one envelope {contract_version, operation, firm_id, data, status?} with data the producer document; CONTRACT.md with a producer column, the operation<->route table as the one authority, the casing rule) and its paired test validates response and data, printing N of 11 conforming with BLOCKED-BY-W2-S16 per non-conforming operation and the token not withheld by that count; (3) the proof moves to the cell that OWNS the surface -- IB-rt-2 gains arm (g): 11 of 11 deployed handlers conform and the X-Contract-Version check is served; (4) nothing is widened -- v1 grows only before its own complete flip, no handler is edited by the seam cell, no schema is loosened. Also recorded: W2-S13 (11 consumer paths ROUTE_UNKNOWN; two orphan consumer operations, three orphan producer routes -- CONTRACT.md's table is the authority, the counterpart regenerates), W2-S14 (casing disjoint 194 snake vs 139 camel; the counterpart's client camelizes at the wire boundary, no meaning moves), W2-S15 (ops/status.py reaches AWS in-process; DEPLOYED-ONLY, graded at IB-rtb-1), W2-S17 (the eleventh schema is RenderPackage, producer FNTEND; W2-S16 stands as filed).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (re-cut applied on the open IB-rt-1 face and the staged IB-rt-2 face; slot ~2 resumed to finish IB-rt-1 on the re-cut arm)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md IRPT_BCKEND-W2-S13..S17 @0e60e9645b",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rt_1.result.md @0e60e9645b -- 7 of 8 arms, arm (b) 0 of 11, the three envelopes",
        "docs/contracts/investor-reporting/v1/ @0e60e9645b -- routes.json, 11 document schemas, CONTRACT.md (304 lines)",
        "memory: feedback_four_part_test_lets_a_coo_lane_recut_a_proxy_criterion_without_a_round_trip -- the standing authority applied",
        "the two faces (this commit): IB-rt-1 <status> pending with the re-cut arm (b); IB-rt-2 <status> staged with arm (g)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "IB-rt-1 RT1-AC1 (b) as cut: 'the response validates against the producer schema; print 11 of 11'. CTO ruling 1: a paired producer-to-consumer test per operation runs the real dispatcher against the consumer's request.",
    "world_is": "The contract artifact exists and is one carrier; the responses do not yet have a contract and the handlers do not yet conform. The seam cell defines the response; the guards cell, which deploys the handlers, makes them conform; the replay grades the deployed whole.",
    "notes": "The proxy-criterion shape recurs from round 1 (S13's routes.json fallback): a criterion that names an artifact another cell produces must name that cell. Carried for the round-2 analysis as an L5 lesson of this seat."
  },
  {
    "id": "IRPT_BCKEND-S27",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.4.0_DS_ClientPlatform~X",
    "surfaced_at": "2026-09-11T12:31:26Z",
    "one_line": "TO-IB-rt-5 grades on 'each of the 2 keys (2 of 2)', but the guard's bundle mechanism mints EXACTLY ONE S3 object -- the tar.gz at b['s3_key'] -- so a two-key denominator is not producible through the mandated mint path.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/safe_deploy_core.py mint_bundle(): one `aws s3 cp <tmp> s3://{b['bucket']}/{b['s3_key']}` and one head-object on that same single key; no loop over members at the upload step",
        ".tools/safe_deploy_core.py build_bundle_payload(): members are tar members INSIDE one gzip payload, not separate objects",
        "the accrual_bridge precedent this order says to copy is likewise ONE key: portal/gold/mdpf/_code/mdpf-accrual-bridge.tar.gz",
        "measured after the mint: list-objects-v2 on code/scripts/assets_gold/investor_reporting/ returns 1 object"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-5 DELIVERABLE: 'the two minted keys under s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/'; RT5-AC1(b): 'head-object on each of the 2 keys ... (2 of 2)'.",
    "world_is": "One bundle object is minted. The cell reports the achievable and strictly stronger denominator instead: 1 of 1 KEY verified (ETag == local md5) carrying 2 of 2 MEMBER sha stamps, each equal to sha256sum of its repo file. Minting two loose twins WOULD satisfy the literal text and is refused here: the X-iii design freezes the loose leg for a bundle member (CTO 2026-08-06 no-S3-roster-twin ruling), so the literal reading and the ratified design are in direct conflict.",
    "notes": "Not blocking: the cell completes and the evidence is stronger than the text asked for. What needs the issuer's pen is the acceptance TEXT, so a later reader does not grade this cell against a denominator the mechanism cannot emit."
  },
  {
    "id": "IRPT_BCKEND-S28",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.4.0_DS_ClientPlatform~X",
    "surfaced_at": "2026-09-11T12:31:26Z",
    "one_line": "The decomposition's literal 'sha_metadata_key: script-sha256' for BOTH bundle members collides inside build_bundle_payload and silently drops one member's sha; implemented literally it produces a stamp that verifies one file while reading as though it covered both.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/safe_deploy_core.py build_bundle_payload(): `shas[spec['sha_metadata_key']] = hashlib.sha256(data).hexdigest()` inside `for member_name in sorted(b['members'])` -- last write wins",
        "sorted member order is ['directory_runner.py', 'holdings_snapshot.py'], so directory_runner.py's sha is the one overwritten",
        "mint_bundle() then builds --metadata from that same dict, so the dropped sha never reaches S3 and its absence is not an error",
        "accrual_bridge, the shape this order says to copy, is per-member: script-sha256 + roster-authority-sha256"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "IRPT_BCKEND_DECOMP.md v0.2 s.2 and the TO's L5 note: members directory_runner.py and holdings_snapshot.py with `sha_metadata_key: script-sha256`.",
    "world_is": "As SHIPPED the collision does not exist: this cell declared distinct per-member keys (directory-runner-sha256, holdings-snapshot-sha256) and both stamps are verified on the served object. The ARMED hazard is the DECOMP TEXT, which still reads as a one-key instruction and would reintroduce the collision for any seat that re-derives the declaration from it -- including a future re-mint or a second bundle in this tree.",
    "notes": "Deviation from the face's literal text is deliberate and is named in the declaring commit. The face itself is not edited (spec FROZEN mid-round).",
    "disarm_owner": "2.0.0_SA_COO~B (owns the decomposition text); 1.0.0_SA_CTO gates .tools"
  },
  {
    "id": "IRPT_BCKEND-S29",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.4.0_DS_ClientPlatform~X",
    "surfaced_at": "2026-09-11T12:31:26Z",
    "one_line": "The guard's own self-test suites were ALREADY FAILING before this cell touched anything -- test_code_trees_invariant.py 3 of 18 and test_safe_deploy.py 7 of 14 -- so RT5-AC1(a)'s 'the guard's self-test and .tools/tests/ pass' is not achievable by any act inside this cell's bounds.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "baseline (pre-edit) `python .tools/test_code_trees_invariant.py` -> 'FAIL: 3/18 cases failed', rc=1; the three are the frozen PIPELINE_MAP comparison, which predates the advi tree added 2026-08-18",
        "baseline (pre-edit) `python .tools/test_safe_deploy.py` -> 'FAIL: 7/14 cases failed', rc=1; four are INDEX_MISSING (fixtures built outside the workspace) and three are 'EXCEPTION: Strings must be encoded before hashing'",
        "baseline .tools/tests/*.py run standalone: 47 PASS / 8 FAIL of 55; none of the 8 is a deploy test",
        "pytest over .tools/tests/ collects ZERO: test_fabric_check_classify.py raises SystemExit at import and takes the whole directory with it (INTERNALERROR, 'no tests ran')"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RT5-AC1(a): 'the guard's self-test and .tools/tests/ pass (counts printed)'; BOUNDS: 'the self-test run is the control'.",
    "world_is": "The suites fail at baseline for reasons this cell does not touch. The run is therefore used the way BOUNDS names it -- as a CONTROL: post-edit, test_code_trees_invariant.py output is BYTE-IDENTICAL to baseline and test_safe_deploy.py differs only by a tempdir nonce inside a pre-existing failure line. That identity is the discriminator that says a bundle addition moves neither PIPELINE_MAP nor VALID_LAYERS.",
    "notes": "Repairing either suite is outside this cell's bounds (the guard's other trees are untouched; the runners are not this cell's to edit either). The invariant suite is the live net under every future CODE_TREES edit and it is currently red, which is why this is ARMED rather than noted.",
    "disarm_owner": "1.0.0_SA_CTO (INFRA.TOOLS gate per safe_deploy_core.py's own header); 0.7.0_AE_CloudOps authored safe-deploy.sh"
  },
  {
    "id": "IRPT_BCKEND-S30",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.4.0_DS_ClientPlatform~X",
    "surfaced_at": "2026-09-11T12:31:26Z",
    "one_line": "The task order instructs a DS lane to mint row ids of the form IRPT_BCKEND-D-S<k>, which the ratified investigation-item schema REFUSES: the id pattern admits only the Z-, W<n>- and C- infixes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/surprise_channel/schemas/investigation_item.schema.json id pattern: ^[A-Z0-9_]+-(Z-)?(W[0-9]+-|C-)?S[0-9]+$ -- 'D-' matches no alternative and [A-Z0-9_]+ cannot absorb the hyphen",
        "re-tested directly: pattern.match('IRPT_BCKEND-D-S1') is False; pattern.match('IRPT_BCKEND-S1') is True",
        "all 71 ids already in this channel match the pattern (0 failures), so the pattern is enforced in practice, not merely declared",
        "the schema names the seat form as the correct one for a seat: '{PROJECT}-S{n} = a seat's row on the laptop fabric'; the W<n> form is gate-bound to a committing 0.9.0_WK_ worker's suffix, which this serial is not"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-5 BOUNDS 8: 'id IRPT_BCKEND-W<your slot>-S<k> (a DS lane mints IRPT_BCKEND-D-S<k>)'.",
    "world_is": "These rows use the valid seat form IRPT_BCKEND-S<k>, continuing the channel's shared seat sequence from its measured max at write time rather than from a read taken earlier in the session.",
    "notes": "Fails LOUD rather than silently -- a D- id is refused by the row gate at commit -- so the cost is a round trip, not a bad record. Flagged because the instruction sits in a face template that other DS lanes will be handed."
  },
  {
    "id": "IRPT_BCKEND-S31",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.4.0_DS_ClientPlatform~X",
    "surfaced_at": "2026-09-11T12:43:56Z",
    "one_line": "TO-IB-rt-5 contradicts itself: RT5-AC1(c) instructs a no-op CHANGE to a runner committed on the branch, while BOUNDS 1 of the same face says 'do not edit the runners'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-IB-rt-5 RT5-AC1(c): 'A no-op change to a runner committed on the branch runs the push gate and reads MEMBER / deployed or verified, never SKIP-NOT-MEMBER'",
        "TO-IB-rt-5 BOUNDS: 'Declare and mint; do not edit the runners.' and 'The DELIVERABLE names no runner edit'",
        "resolved without editing either runner: the gate's own --commit-range path was run over the two REAL commits that added them (3654197107 IB-s-1, 2dbc92e956 IB-s-12) -- the identical input that read SKIP-NOT-MEMBER in round 1",
        "both runs printed 'BUNDLE-ROUTED: <runner> -> bundle investor_reporting' with rc=0, and each run's sibling tests/*.py still printed 'SKIP-NOT-MEMBER ... 404' as an in-run negative control"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RT5-AC1(c) requires a new no-op commit touching a runner; BOUNDS 1 forbids editing a runner in this cell.",
    "world_is": "Both are satisfiable at once only because the repo already contains commits that touch the runners. The gate's commit-range path over those historical commits is the same code path a fresh no-op commit would exercise, and it is a STRICTLY better discriminator: the input is byte-identical to the one that produced the round-1 SKIP-NOT-MEMBER finding, so the before/after comparison holds the input fixed and varies only the declaration.",
    "notes": "Reported rather than silently resolved because the next seat handed this face template may take the literal path, edit a file another cell owns (IB-rt-3 / IB-rt-6 own the runners this round) and collide at the drain. No runner was edited by this cell."
  },
  {
    "id": "IRPT_BCKEND-S32",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.4.0_DS_ClientPlatform~X",
    "surfaced_at": "2026-09-11T12:57:01Z",
    "one_line": "Both round-1 batteries grade the first-mint by head-object on a LOOSE per-file key, so now that the mint has correctly landed as a BUNDLE they will read ABSENT / DEPLOY LEG BLOCKED -- a FALSE RED that says the opposite of what happened.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_s_4.py:320-324 -- key = SHARED_CODE_PREFIX + 'directory_runner.py'; head-object; landed = (rc == 0)",
        "deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_s_12.py:39,279-292 -- CODE_KEY = '.../holdings_snapshot.py'; artifact_landed = (rc_h == 0); and it probes --mint-bundle holdings_snapshot, a bundle NAME that does not exist (the declared bundle is investor_reporting, of which holdings_snapshot.py is a MEMBER), so bundle_declared stays False and deploy_blocked stays True",
        "measured after the mint: list-objects-v2 on code/scripts/assets_gold/investor_reporting/ returns 1 object, the tar.gz; head-object on the loose .../directory_runner.py key returns 404",
        "the 404 is CORRECT and PERMANENT by design: safe_deploy_core.py routes a bundle member away from the loose leg ('loose leg frozen 2026-08-11, X-iii') and the X-iii note states a member's loose S3 objects are deprecated-in-place, never updated"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Round 1's IB-s-4 and IB-s-12 encode 'SERVED' as 'the per-file key exists at the shared-home prefix'.",
    "world_is": "After IB-rt-5 the served shape is ONE hash-stamped bundle at that prefix and the per-file keys are frozen 404s. Re-running either round-1 battery therefore produces 'ABSENT' / 'DEPLOY LEG: BLOCKED' AFTER a successful first-mint, which reads as a regression and is the exact opposite of the world.",
    "notes": "Raised because L9 adjudication is the likeliest place to re-run a round-1 battery. The instrument that IS current for this surface is deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rt_5.py, which grades the bundle object and both member sha stamps. Not repaired here: those batteries belong to IB-s-4 / IB-s-12, not to this cell, and editing another cell's deliverable is outside these bounds.",
    "disarm_owner": "2.0.0_SA_COO~B (routes the correction to the owning cells IB-s-4 / IB-s-12); 3.0.0_SA_CVO reads it at L9"
  },
  {
    "id": "IRPT_BCKEND-S33",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T14:38:49Z",
    "one_line": "ROUND 2, SECOND DRAIN BATCH: four branches landed, two orders COMPLETE, one OPEN and routed, one COMPLETE then RE-OPENED on Andrew's word. (1) IB-rt-4 (slot ~3) merged OPEN at 98f756a90c: its withheld export apply was CORRECT and its premise (W3-S17) was WRONG -- the three resources its plan read as orphans left by IB-s-14 are IB-rt-8's, declared on that cell's branch at 1365a96fad and applied into the shared export state at 67aa231c29; git show 1beda4bf49 removes nothing. Route: the merge, not a destroy, a re-declare or a state rm; arm (e) completes at the merged tip (issuer amendment at 122206aab7, which also packages enforce.py for W3-S14, re-registers 6 of 6 for W3-S18, and rebuilds irpt-common from the tree for W4-S15). (2) IB-rt-5 (DS lane) merged COMPLETE at 86d2d0835f after its six rows were re-minted S27..S32 (the ids S25/S26 it had minted from a stale read were the issuer's); the CVO's pinned L9 review (IRPT_RT5_L9_REVIEW_20260911.md, C-S79..C-S81) graded RT5-AC2 PASS and found the battery's arm (a) predicate count-only (C-S80) -- the DS lane accepted four findings against its merged record in 95970; no merged row is edited, the CVO's rows carry the correction. (3) IB-rt-1 (slot ~2) merged COMPLETE at 8abcb1563b: v1 frozen at c22f179bbf with eleven response contracts; the census handed to IB-rt-2 (CONFORMS 0, 8 blocked of which 1 is the no-handler holdings route). (4) IB-rt-8 (slot ~4) merged COMPLETE at 790d948e98 through FIVE conflicts: the channel and PATH_MANIFEST as unions; export/handler.py, export/render.py and the export entry of lambda-source-map.json taken from IB-rt-8's side because rt-8 restructured the function into a controller and those bytes are what the function SERVES -- IB-rt-4's edits to the same two files are re-applied by IB-rt-4 on the controller structure at the merged tip (its amendment says so; nothing of IB-rt-4's is silently lost, it is named). Then RE-OPENED at 122206aab7 (complete -> pending) for ONE addendum arm (g): the four synthetic exports under firms/49financial/generations/GENIBS14SYN/attempts/1/exports/ deleted on Andrew-direct 13:4xZ 'yes on synthetic exports' (1.0.0_SA_CTO 95968), four literal keys, ledger before the act, 404 on 4 of 4 after, a fifth object a STOP. ROUTED ROWS: W4-S14 (the cloud render is HUMAN-GATED: the only host with a browser is irpt-ycharts-runner, held stopped by its own root) goes to 1.0.0_SA_CTO for Andrew's word on the README's option A, with the print-route session named as the second missing thing; W4-S16 (ExportReceipt has no attempt_id slot; a shared-contract change needs the counterpart's half) and W3-S15 (arm (c)'s except-handler denominator is narrower than 'every public reason'; the dataflow census) are carried to L10 by name; W3-S13 disarmed by its worker; W3-S16 and W2-S18 INERT for the CVO. ONE PROCESS FACT: a foreign commit (3b28cf1c6f) landed on the tip while the DS drain's merge was OPEN in the shared index; completing that merge would have staged a revert of it, so the merge was ABORTED and re-run from the moved tip. Two seat rows the DS lane vacated (S25, S26) remain the issuer's.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (the issuer; W4-S14 to the CTO for Andrew's word; W4-S16, W3-S15 carried to L10)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLOUD 98f756a90c (drain wk-irpt_bckend-2-3), 86d2d0835f (drain wk-irpt_bckend-2-ds), 8abcb1563b (drain wk-irpt_bckend-2-2), 790d948e98 (drain wk-irpt_bckend-2-4), 122206aab7 (four-face amendment; IB-rt-8 re-opened)",
        "git show 1beda4bf49 -- infra/aws/terraform/investor-reporting/export/ -- adds only; grep of the three resource names across the tree at 7478fdf144: 0 files; on wk-irpt_bckend-2-4 at 1365a96fad: iam.tf, lambda.tf, ssm.tf",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_RT5_L9_REVIEW_20260911.md; org/mcp/inbox/2.0.0_SA_COO/~B/read/20260911T140829Z_0.4.0_DS_ClientPlatform_X_IB-rt-5__the_CVO_is_right_on_four_counts.md (95970)",
        "org/mcp/inbox/2.0.0_SA_COO/~B/read/20260911T134833Z_1.0.0_SA_CTO_ANDREW_S_WORD_13_4xZ__yes_on_synthetic_e.md (95968); org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/RT8_synthetic_pdfs_inventory.md (four keys, 169,425 bytes)",
        "infra/aws/ec2/investor-reporting-export/README.md @790d948e98 -- the operator act, option A and option B"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Spine v3 L7: a worker's report is drained by the issuer, its rows dispositioned and its next order handed; L6: a mid-round amendment re-cuts a criterion under the standing authority and never widens the issuance; CLAUDE.md hard stops: an S3 delete needs a human's word, and the word arrived by name for four keys.",
    "world_is": "Round 2 stands at IB-rt-1, IB-rt-5 COMPLETE; IB-rt-8 COMPLETE on six arms and re-opened on a seventh; IB-rt-4 OPEN at the merged tip; IB-rt-3 in flight; IB-rt-2 handed; the rest staged. The export function's served bytes are IB-rt-8's controller and IB-rt-4 moves them forward at the merged tip.",
    "notes": "Slots ~2, ~3, ~4 re-cut at 122206aab7 and resumed in this turn (IB-rt-2; IB-rt-4 arm (e) then IB-rt-9; IB-rt-8 arm (g)). The DS lane's only order is drained; its seat is released by /mstr-kill after this row lands."
  },
  {
    "id": "IRPT_BCKEND-S34",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T15:17:40Z",
    "one_line": "ROUND 2, THIRD DRAIN: IB-rt-3 (slot ~1) merged COMPLETE at 2a42c9563f through four conflicts -- the channel and PATH_MANIFEST as unions, infra/aws/lambda/layers/irpt-common/build_layer.py as the UNION of both cells' manifest keys (IB-rt-8's modules/data and IB-rt-3's id_normalizer plus its carried_forward_members hand-copy of the peer's members), BUILD_MANIFEST.json from IB-rt-3's side because its :5 build is the live layer version at the drain. Row W1-S12 (BLOCKING: two cells publishing one layer, aws_lambda_layer_version REPLACES) is disarmed by routing, not by a rebuild here: IB-rt-7 (handed at df84a8a952, slot ~1) removes the carried block and rebuilds from the declared lists as its first act, and IB-rt-4's arm (e) rebuilds from the same tree -- whichever publishes second builds the same members, and each prints the version it read and the version it published. W1-S11 (a fourth id-shape disagreement in _scope/resolve.py, bare 24-hex vs acc_ prefix, reached only for an id the directory does not hold) and W1-S13 (arm (b)'s floor unreachable by construction: the joined set of two producers built from different upstream tables) are INERT for the CVO at L9. SECOND ANDREW'S WORD OF THE ROUND: 14:5xZ 'Yes ycharts runner may be started' (1.0.0_SA_CTO 95983) resolves W4-S14 by option A -- IB-rt-8 arm (a) is UNLOCKED at ffa98ac525: start irpt-ycharts-runner for the render, ssm irpt-export-render-run, return to the Terraform-declared stopped state, the ycharts root's header and output description amended in the same act to say a start FOR A RENDER is not the gated sign-in; no vendor act; a SESSION_ABSENT refusal is the recorded negative and the arm then reads SESSION-GATED naming IB-rtb-1. The DS lane 0.4.0_DS_ClientPlatform~X, its only order drained and IDLE by its own report (95980), is RELEASED by /mstr-kill on the already-dead path (its claude process was gone, no marker window, broker NOT REGISTERED; deregistered; audit line appended).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (the issuer)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLOUD 2a42c9563f (drain wk-irpt_bckend-2-1), df84a8a952 (IB-rt-7 handed), ffa98ac525 (IB-rt-8 arm (a) unlocked)",
        "org/mcp/inbox/2.0.0_SA_COO/~B/read/20260911T150157Z_1.0.0_SA_CTO_ANDREW_S_WORD_14_5xZ__Yes_ycharts_runner.md (95983)",
        "org/mcp/agent-spawn-audit.log (KILL line, 2026-09-11T15:17:40Z)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Spine v3 L7: the drain carries both sides of a shared write surface and names the cell that reconciles it; CLAUDE.md Agent Autonomy: a live vendor call needs Andrew's per-use word, and the word arrived by name for a start that is not a sign-in.",
    "world_is": "Round 2: IB-rt-1, IB-rt-3, IB-rt-5 COMPLETE; IB-rt-8 re-opened on two Andrew's-word arms (~4); IB-rt-4 at the merged tip (~3); IB-rt-2 (~2) and IB-rt-7 (~1) in flight; rt-6, rt-9, rt-10, rt-11, rtb-1 staged. Five worktrees to four; the DS seat released.",
    "notes": "Seat rows continue at S35."
  },
  {
    "id": "IRPT_BCKEND-S35",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T17:35:32Z",
    "one_line": "ROUND 2, DRAINS FOUR TO SIX AND THE MANAGED WIND-DOWN. (1) IB-rt-4 (slot ~3) merged COMPLETE at 3ed2c79443: arm (e) at the merged tip, the export root's baseline plan read No changes (W3-S17's three 'orphans' were IB-rt-8's), enforce.py/errors.py/resolve.py packaged (W3-S14 closed), triple equality 6 of 6 (W3-S18 closed), the layer NOT republished because the published zip already carried the union at the tip (measured member by member). Rows W3-S19 (disarmed by the worker), W3-S20 (closed by IB-rt-8's merge), W3-S21 (layer BUILD_MANIFEST disagrees with the published :5 -- superseded by the next rebuild), W3-S22 (two dispatch.py on one flat sys.path -- routed to slot ~2, which authored _authz/dispatch.py at 173349a652, to rename it). IB-rt-9 taken by the same slot (191547be34) and BLOCKED on W3-S23: the arm's 'legacy any-non-403 probes remaining: 0' names infra/aws/lambda/ycharts-session-probe/ and ycharts-session-capture/, outside its grant. RULED at bebcab6315: GRANTED, not scoped out -- a probe that reads a 400 as an authenticated session is the false green the v0.9 cutover exists to remove. (2) IB-rt-2 (slot ~2) merged OPEN at aef37711d3 on four BLOCKING rows, every one routed at bebcab6315: W2-S19 ops/ granted; W2-S24 the irpt-common layer granted under the rebuild-from-tree rule; W2-S22 resolved by sequence (IB-rt-4 landed first); W2-S21 split by owner (irpt-status and directory-search to rt-2, irpt-ycharts-generate's 7 of 25 never-existing build inputs to rt-9; the closed ledger entry claiming a byte-identical rebuild at a commit lacking the inputs is a RECORD defect carried to L10). W2-S23 CONTRACT_VERSION admitted to the closed reason set by amendment; W2-S25 ruled (a refusal is a StatusEnvelope, never a response-contract instance; v1 stays frozen); W2-S26/S27 in lane; W2-S20 retires the inherited '6 of 11' (11 of 11 unguarded at the cut). (3) IB-rt-8 (slot ~4) merged COMPLETE AGAIN at f20bebd15d through a temporary linked worktree (the shared index held another seat's open-deploy sentinel): arm (g) 4 of 4 synthetic exports deleted -- AS DELETE MARKERS on a versioned bucket (W4-S20: the noncurrent versions remain retrievable by VersionId; the unrecoverable per-version delete was NOT taken on a one-line yes; carried to Andrew via the CTO); arm (a) RAN on irpt-ycharts-runner (1 start, 1 send, 1 stop; host stopped on 5 of 5 sends) and reads SESSION-GATED -- the print route answered with a sign-in screen, so the remaining gate is IB-rtb-1's authenticated session (W4-S25); the network guard measured 2 foreign of 12 requests, both Google Fonts, 0 vendor (W4-S23: '0 external connections' is unachievable against the portal as built -- carried to IRPT_FNTEND and the CVO); W4-S21 the render host's evidence grant declared from the export root onto the ycharts runner role (recorded in the ycharts root's header by rt-9; the fold carried to L10); W4-S22 a portal origin the estate does not own carried in a deployed Lambda for two rounds (INERT). (4) IB-rt-10 RE-SEATED from slot ~3 to slot ~4 at bebcab6315 and flipped pending -- then NOT HANDED: at 17:30Z 0.0.0_AB_MSTR relayed Andrew-direct 'let all agents know that they need to let their workers finish but prepare for a reboot, so we're in a managed winddown' (95994). Nothing new starts: IB-rt-10's face reads pending on slot ~4 with no worker on it, and the successor session hands it (or re-seats it) after the reboot. Slots ~1 (IB-rt-7), ~2 (IB-rt-2), ~3 (IB-rt-9) were told to finish only what closes without opening a ledger, to commit early and often, and to leave a WIP_<order>_winddown.md for a successor. The successor log is org/tier1_exec/2.0.0_SA_COO~B/logs/2026-09-11/session_cooB_1515-1745Z_irpt_bckend_round2_drains_4_to_6_and_winddown.md.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (the issuer; the successor session reads the log named here first)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLOUD 3ed2c79443 (drain ~3), aef37711d3 (drain ~2), f20bebd15d (drain ~4 via coo-b-drain-tmp, fast-forwarded), bebcab6315 (three-face amendment; rt-10 re-seated)",
        "org/mcp/inbox/2.0.0_SA_COO/~B/read/20260911T173049Z_0.0.0_AB_MSTR_MANAGED_WINDDOWN__THIS_DEVICE__let_worke.md (95994)",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/RT8-g_delete_receipts.json (DeleteMarker true on 4 of 4); RT8-a_render_record.md (SESSION-GATED)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Spine v3 L7: the issuer drains, dispositions and hands; a worker's grant is its <paths> and a path it needs is a row the issuer answers by grant or by scope; Andrew-direct 17:1xZ: workers finish, nothing new starts, log and commit.",
    "world_is": "IRPT_BCKEND round 2 at bebcab6315: COMPLETE rt-1, rt-3, rt-4, rt-5, rt-8; OPEN rt-2 (~2), rt-7 (~1), rt-9 (~3), all under the wind-down caveat; rt-10 pending on ~4 with no worker; rt-6, rt-11, rtb-1 staged. Every drain landed; no merge is open; every worker worktree is at or after the amended tip.",
    "notes": "Seat rows continue at S36. The successor session: read the log first, drain the three WIP branches (wk-irpt_bckend-2-1, -2, -3 at /c/tmp/wk-irpt-2-{1,2,3}), then hand rt-10 (~4), rt-6 (~2 after rt-2), rt-11 (~3 after rt-9), rtb-1 (~1 last)."
  },
  {
    "id": "IRPT_BCKEND-S36",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T18:12:34Z",
    "one_line": "WIND-DOWN DRAINS. (1) IB-rt-2's wind-down branch (496a2767d2, slot ~2) landed at 5347f30b34: no ledger opened across two runs, arm (a) reads 0 of 11 unguarded across all six functions with the control firing 1 of 11, irpt-status at 3 of 3 triple equality with six absent build inputs REMOVED, and the order stays OPEN for a successor run -- W2-S28 (the rename's one importer lives in _contracts/, outside the grant) is GRANTED on the face; W2-S29 (directory-search and directory-refresh share a source dir) is RULED to a per-function files list. (2) IB-rt-7 (slot ~1) landed COMPLETE at 47522d2ba9: the live holdings route serves under the api root with 12 of 12 routes declared, holdouts visible and before == after to the cent on 3 of 3 firms, both clocks on every node, :acct: 0 of 127,071; the layer was NOT published because the live :5 already carried 9 of 9 declared members (W1-S14's 'record and repoint only' branch); W1-S16 (_authz.covers() admits any advisor id for an admin principal against its own docstring; no cross-firm bytes reachable today) is ROUTED to IB-rt-2's successor run, which holds _authz/. (3) A PROCESS SLIP, RECORDED AGAINST THIS SEAT: the first attempt at drain (1) was REFUSED by the row gate (another seat's commit landed while the merge was open, the conflict stages vanished, and a marker-laden channel was staged) and the cleanup chained after it -- `git worktree remove && git branch -D` -- ran anyway, deleting the un-merged branch. Row S18's lesson, again, one level up: a destructive step chained after a merge whose rc was not the chain's condition. The branch was restored from the object store (496a2767d2, nothing lost), the merge residue (three modified files and two untracked files, each verified byte-identical modulo CRLF to the branch) was cleared from the shared tree, and the drain re-run through a temporary linked worktree, then pull-merged when the fast-forward lost two races. Every cleanup in this session from here on is gated on `merge-base --is-ancestor <branch tip> HEAD`, never on the chain reaching it. (4) IN FLIGHT at this row: IB-rt-9 on slot ~3 only, under the wind-down caveat. IB-rt-10 held unhanded on ~4.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (the issuer; the successor session reads the wind-down log first)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLOUD 5347f30b34 (drain of coo-b-drain-tmp carrying 4d234193a8 = wk-irpt_bckend-2-2 @496a2767d2), 47522d2ba9 (drain wk-irpt_bckend-2-1 @b9a3fcc335)",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/WIP_IB-rt-2_winddown.md; deliverables/0.9.0_WK_IRPT_BCKEND~1/WIP_IB-rt-7_winddown.md",
        "the refused --continue's log: [surprise-corpus] REFUSED: 1 malformed block(s) -- the staged channel carried conflict markers"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md 14b and rule 27: a drain is graded on the merged index by safe-merge.sh and its remaining steps (remove the worktree, delete the branch) follow a LANDED merge; memory reference: a pipeline's rc is its last command's, so a chained cleanup must key on the merge's own outcome.",
    "world_is": "IRPT_BCKEND round 2 at 47522d2ba9: COMPLETE rt-1, rt-3, rt-4, rt-5, rt-7, rt-8; OPEN rt-2 (successor run), rt-9 (~3 in flight, wind-down); rt-10 pending on ~4 unhanded; rt-6, rt-11, rtb-1 staged.",
    "notes": "Seat rows continue at S37. The successor drains wk-irpt_bckend-2-3 when slot ~3 reports, then cold-starts rt-2, rt-9 (if open), rt-10, rt-6, rt-11, rtb-1 in fresh worktrees."
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
    "id": "IRPT_BCKEND-W1-S6",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~1",
    "surfaced_at": "2026-09-11T00:21:03Z",
    "one_line": "IB-s-5: the preflight declares 'this cell's role is graded at Phase 1 by `comp-iam service irpt-core` once its .tf exists and at Phase 2 by `comp-iam gaps`'. Both ran, after the apply, against the four real IAM role stubs and their attached per-firm prefix policies. Neither sees them: `comp-iam service irpt-core` returns 'No service matching', `comp-iam role irpt-core-firm-49financial` returns 'No role matching', and `comp-iam stats` reads 'IAM roles parsed: 191' UNCHANGED both before this order's apply and after it (231 live roles in the SAME apply's own comp-tagauthz sweep, which reads iam:GetAccountAuthorizationDetails directly -- a DIFFERENT, LIVE-plane instrument that DOES count them). comp-iam's static census is built by working BACKWARD from a Lambda function in infra/aws/lambda/ci/lambda-source-map.json or an EC2 instance profile to the role each one assumes (extract_iam.py's own docstring names lambda-source-map.json and *.tf role/policy blocks as its two inputs) -- a role stub with no Lambda or EC2 resource yet referencing it has no entry point into that walk, so it is INVISIBLE to the tool regardless of whether its permissions are correct, missing or over-broad. The preflight's own comp-iam BLIND SPOT line ('a GRANTED-BROAD wildcard cannot be falsified by a resource check') anticipated a narrower gap than this: the roles are not merely un-falsifiable for over-permission, they do not appear in the census AT ALL.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-iam service irpt-core (post-apply) -> 'No service matching \\'irpt-core\\''",
        "comp-iam role irpt-core-firm-49financial (post-apply) -> 'No role matching \\'irpt-core-firm-49financial\\''",
        "comp-iam stats (pre-apply, preflight @20:2xZ): 'IAM roles parsed: 191'; comp-iam stats (post-apply, this cell): 'IAM roles parsed: 191' -- identical despite 4 new aws_iam_role resources applied and confirmed live via 4 of 4 get-role calls in the IB-s-5 battery",
        "the same apply's own comp-tagauthz gate output: 'roles 231 ... derived from the account, one call: iam get-account-authorization-details' -- the LIVE plane counts 231 (up from 229 at IB-s-17's apply), confirming the roles exist and only the STATIC comp-iam census misses them",
        "org/modules/graph/extract_iam.py:9-10 docstring -- 'infra/aws/lambda/ci/lambda-source-map.json -- Lambda function -> source path' and 'infra/aws/terraform/*/iam.tf -- IAM role policies' named as its two data sources; TF_SCAN_ROOTS at :2105-2109 confirms a recursive rglob so directory depth is not the cause -- the entry point is the SERVICE (Lambda/EC2), never a bare aws_iam_role scan",
        "IRPT_BCKEND.TO-IB-s-5 preflight block: 'this cell's role is graded at Phase 1 by comp-iam service irpt-core once its .tf exists and at Phase 2 by comp-iam gaps -- both recorded in the instance'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO IB-s-5 preflight (comp-iam): 'ZERO investor-reporting roles exist on the DESIRED plane, so this cell's role is graded at Phase 1 by comp-iam service irpt-core once its .tf exists and at Phase 2 by comp-iam gaps -- both recorded in the instance.'",
    "world_is": "Once the .tf exists AND is applied, comp-iam service/role/stats still cannot see the four roles at all -- not a gap finding, an absence from the tool's own population -- because its census walks from a Lambda/EC2 service definition to its role, and no service yet assumes these role stubs (by design: this cell creates role stubs, not Lambda functions).",
    "notes": "INERT: no permission was granted incorrectly and nothing here is a security gap -- the per-firm S3 conditions were read back directly via get-role (trust policy) in the battery and via terraform plan (0 diff) for the full policy documents, so this cell's own claims are verified by OTHER instruments. The gap is that comp-iam's Phase 1/2 checks the preflight named cannot be the read that closes THIS cell -- they will become live the moment IB-s-6/9/13/14/16 attach a Lambda to one of these roles and name it in lambda-source-map.json, which is the natural point for a future cell's comp-iam gaps read to first see them."
  },
  {
    "id": "IRPT_BCKEND-W1-S7",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~1",
    "surfaced_at": "2026-09-11T02:49:44Z",
    "one_line": "IB-s-12: the first draft used the landed DirectoryEntry population (IB-s-1) as a HARD JOIN GATE for this cell's own custody joins, on the assumption that opaque_id(account, firm, raw) would resolve against the directory for all three firms the way it does for 49F. Measured empirically: it resolves 5 of 5 (then 7,431 of 7,453 at scale) for 49financial, but 0 of 790 for inflection and 0 of 946 for cottonwood -- the directory's opaque account ids for those two firms evidently derive from a raw key different from accounts_v2.account_id (INF) and fact_model_assignment.external_id (COT), which this cell did not trace to directory_runner.py's own build_inf/build_cot source selection within its time budget. Gating on the mismatch would have zeroed both firms' snapshots while reading as a genuine coverage failure rather than an identity-space mismatch. Changed BEFORE any apply: the directory intersection is now INFORMATIONAL ONLY (reported per firm in `manifest.directory_cross_check`, never a `continue`), and each firm's own natural silver-to-silver join is the resolved-scope population -- which is what reproduces the PRD's own 946-of-950 (COT) and 7,431-of-7,453 (49F, as the cross-check) dated figures.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B (whichever cell next needs a per-firm opaque-id cross-check between HoldingsSnapshot and DirectoryEntry for INF/COT should trace directory_runner.build_inf/build_cot's exact raw-key selection first; until then, no consumer should assume the directory and this cell's holdings population share an id space for those two firms)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "empirical check, this worktree: opaque_id('account','49financial', zfilled 10-digit fact_acc account_id) matches the real landed directory's account_ids set 5 of 5 sampled, then 7431 of 7453 at full scale",
        "empirical check: opaque_id('account','inflection', accounts_v2.account_id) matches 0 of 790; opaque_id('account','cottonwood', fact_model_assignment.external_id) matches 0 of 946, against the real landed directories in opal-data-inf and opal-data-cot respectively",
        "data/assets/scripts/gold/investor_reporting/holdings_snapshot.py build_49f/build_inf/build_cot manifest.directory_cross_check fields, this commit",
        "data/assets/scripts/gold/investor_reporting/directory_runner.py's own docstring names DIFFERENT authoritative identity sources per firm (49F dim_relationship/dim_account; INF accounts_v2 x representatives; COT fact_allocations Relationship ID) -- consistent with a per-firm raw-key choice this cell did not reverse-engineer for INF/COT"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO IB-s-12 decomposition note: 'unique actual custody population per resolved scope' implies a join against the resolved population IB-s-1/IB-s-2 establish.",
    "world_is": "The resolved-scope population this cell actually uses is each firm's OWN silver-to-silver join (SmartX account map for 49F, Eclipse accounts_v2 for INF, Rebalancer assignment for COT) -- not an intersection with the landed DirectoryEntry set, because that intersection is empirically empty for two of three firms.",
    "notes": "INERT for THIS cell's own acceptance: all three firms reconcile to the cent and reproduce the PRD's own dated figures using their own joins, which is the load-bearing evidence, not the directory cross-check. ARMED for anyone downstream who assumes the cross-check IS the join."
  },
  {
    "id": "IRPT_BCKEND-W1-S8",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~1",
    "surfaced_at": "2026-09-11T02:49:44Z",
    "one_line": "IB-s-12: the issuer amendment required attempting the rule-13 code deploy through the guard's explicit first-mint mechanism (`--mint-bundle`) rather than accepting the push-gate's rc=0/SKIP-NOT-MEMBER as a deploy. Measured: `.tools/safe-deploy.sh --mint-bundle holdings_snapshot` returns 'ERROR: no bundle named 'holdings_snapshot' declared (declared: ['accrual_bridge'])'. Declaring a bundle requires editing `.tools/safe_deploy_core.py` CODE_TREES, which is outside this order's `<paths>` grant (the file is not listed and is a shared DS-lane tool, not this project's). This is the SAME class row IRPT_BCKEND-W2-S5 named for IB-s-1's sibling script, one level deeper: not only does the ordinary push path SKIP-NOT-MEMBER, the EXPLICIT escape hatch the guard itself documents ('first-mints stay explicit/manual') has no declared target for this project at all. `head-object s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/holdings_snapshot.py` confirms 404 -- the artifact, not the exit code, is the oracle and it reads ABSENT.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B (a bundle declaration for the investor_reporting gold scripts in .tools/safe_deploy_core.py CODE_TREES, or a routing decision that these scripts belong to a different CODE_TREES entry entirely, is a DS-lane / tooling-owner act outside any IRPT_BCKEND worker's <paths>)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bash .tools/safe-deploy.sh --mint-bundle holdings_snapshot -> 'ERROR: no bundle named 'holdings_snapshot' declared (declared: ['accrual_bridge'])', exit code 0",
        "bash .tools/safe-deploy.sh --author '0.9.0_WK_IRPT_BCKEND~1 <...>' data/assets/scripts/gold/investor_reporting/holdings_snapshot.py -> 'SKIP-NOT-MEMBER [mdpf] ... probed s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/holdings_snapshot.py -> 404 ... OK: safe-deploy gate PASS -- 0 file(s) deployed; 1 SKIPPED (first-mint, 404). NOTHING WAS DEPLOYED.'",
        "aws s3api head-object --bucket opal-data-mdpf --key code/scripts/assets_gold/investor_reporting/holdings_snapshot.py -> 'An error occurred (404) when calling the HeadObject operation: Not Found'",
        "this order's own <paths> block names infra/aws/lambda/ci/lambda-source-map.json but NOT .tools/safe_deploy_core.py -- the file the fix would require editing is not in this order's grant",
        "row IRPT_BCKEND-W2-S5 (IB-s-1, the sibling script) already measured the SAME shape one layer shallower (the push-gate SKIP, not the --mint-bundle refusal specifically)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Issuer amendment (2.0.0_SA_COO~B, before this order was handed): 'read .tools/safe-deploy.sh's own header for the explicit first-mint mechanism it names and use it ... If the guard names a lane this serial cannot satisfy for the first-mint, that is a BLOCKING row on the deploying arm, not an override.'",
    "world_is": "The guard's explicit first-mint mechanism is --mint-bundle, and it requires a bundle declared in a file outside this order's <paths>. No lane this serial can reach satisfies the first-mint. S12-AC1 arm (f)'s code-deploy leg reads BLOCKED, exactly as the criterion's own text anticipates ('a refusal is printed verbatim, filed as a BLOCKING row, and this arm reads BLOCKED') -- the token IBS12-HOLDINGS-RECONCILED is not withheld for it, per that same text.",
    "notes": "Filed per the issuer amendment's own instruction. The data-landing half of arm (f) (head-object on each firm's QA latest.json) is unaffected and HELD; only the code-deploy half is blocked."
  },
  {
    "id": "IRPT_BCKEND-W1-S9",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~1",
    "surfaced_at": "2026-09-11T06:21:55Z",
    "one_line": "IB-s-16's hand-off (issuer amendment 812bbec0e9 + 902ea877dc, fact 4) asserts 'IB-s-4's one normaliser' strips the `<firm>:acct:` namespace prefix where a holdings id crosses the directory seam, and names it as living under infra/aws/lambda/investor-reporting/directory/. Measured: no such function exists anywhere under that path. Every top-level def in handler.py, refresh.py and expiry.py was enumerated (handler.py: normalize() is an unrelated lowercase-ASCII text-search folder used for search tokens, plus tokens/load_directory/etc; refresh.py: manifest_key, new_manifest, compute_delta, reason_for_delta, missed_business_dates, refresh_firm, serve_read, lambda_handler, _firm_ids_from_env; expiry.py: _as_date, resolve_calendar, age_in_trading_days, _source_of, evaluate, status_envelope, fallback_answer) -- none strips or normalises an account-id namespace prefix. `git show 624a60e4fc --stat` (IB-s-4's actual merged commit) confirms its file list is lambda-source-map.json, PATH_MANIFEST.json, directory/{expiry.py,refresh.py,tests/test_refresh_expiry.py,schedule.tf} plus deploy/proof/battery/investigation artifacts -- no normalizer file was ever added. Row IRPT_BCKEND-W2-S11 (which this amendment cites as disarmed by IB-s-4) names the SAME prefix ('<firm>:acct:') but its own grounding evidence never names a shipped normaliser function either -- it reads as a manual prefix-strip performed inline by whoever measured that row, not a shared library call.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B (a shared account-id namespace-prefix normaliser for the holdings/directory seam either needs to be built and declared as the ONE normaliser future cells import, or the amendment's citation needs correcting to point at wherever the prefix-strip logic actually lives; until then this cell builds its own minimal, clearly-labelled inline stripper for its own second-firm hash census rather than importing a function that does not exist, and that inline copy is NOT the shared normaliser the amendment describes)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-read/enumeration of every top-level `def` in infra/aws/lambda/investor-reporting/directory/handler.py, refresh.py and expiry.py at this worktree's HEAD (5fa4a113107af2d884a1fe101c135584852586e8) -- zero functions named or shaped like a namespace-prefix strip or account-id normaliser",
        "git show 624a60e4fc --stat -> file list is infra/aws/lambda/ci/lambda-source-map.json, infra/aws/lambda/investor-reporting/PATH_MANIFEST.json, infra/aws/lambda/investor-reporting/directory/{expiry.py,refresh.py,tests/test_refresh_expiry.py,schedule.tf} plus deploy-completion/proof-of-spec/battery/adversary-declaration/investigation artifacts -- no normalizer file",
        "handler.py's only def named normalize() is a lowercase-ASCII text-search token folder (used for search matching), unrelated to account-id namespaces -- read in full at this worktree's HEAD",
        "row IRPT_BCKEND-W2-S11's own grounding text (this file, this project) describes the `<firm>:acct:` prefix mismatch and a post-normalisation count but does not cite a shipped shared function as the mechanism used to strip it"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "IB-s-16 hand-off, fact (4): 'the second-firm hash census reads the firm buckets and the shared bucket under both prefixes, normalised through IB-s-4's one normaliser where an id crosses the holdings/directory seam, both counts printed.'",
    "world_is": "No such normaliser exists anywhere in the repo under infra/aws/lambda/investor-reporting/directory/ (or, by the same enumeration, anywhere else this cell's search reached) -- IB-s-4's actual merged commit (624a60e4fc) added expiry.py/refresh.py/schedule.tf/tests only. This cell proceeds by writing its own minimal, explicitly-labelled inline prefix-stripper (citing this row) for its own second-firm hash census, rather than importing a function that is not present.",
    "notes": "OBSERVATION, not BLOCKING: this cell can still satisfy its own acceptance criteria by building the minimal stripper inline and printing both as-written and after-normalisation counts, which is the literal ask. ARMED because a FUTURE cell that trusts the hand-off's citation and tries to `import` a shared normaliser from directory/ will fail, and because the underlying id-space mismatch for INF/COT (rows W1-S7, W2-S11) is a raw-key difference no prefix-stripper reconciles."
  },
  {
    "id": "IRPT_BCKEND-W1-S10",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~1",
    "surfaced_at": "2026-09-11T10:09:09Z",
    "one_line": "IB-sb-3's real-file unguarded_routes() census over routes.json (S13's real-file case) reads 6 of 11 handler-bearing routes unguarded, not the 3 the amendment names as the EXPECTED population (row S9: IB-s-1 directory x2, IB-s-11 performance). THREE MORE are unguarded but not disclosed anywhere: POST /api/scoped/investor-reporting/analysis (irpt-ycharts-generate, IB-s-9 -- its own job.py source comments 'THIS CELL REGISTERS NO ROUTE ... woken by irpt-generation, not reached through the edge', written before routes.json existed; routes.json (IB-s-15, landed after that comment) now maps this route TO this function anyway, and job.py was never revisited), GET /api/scoped/investor-reporting/narrative/{reportId} (irpt-narrative, IB-s-13 -- no _authz import at all, no disclaimer either), and GET /api/scoped/investor-reporting/export/{exportId} (irpt-export-render, IB-s-14 -- the deployed lambda_handler only implements action=capabilities; no separate guarded export-status operation exists in the codebase for this route at all). None of the three currently discloses protected data (ycharts-generate always refuses via a hard consent-env-var gate before looking at identity; narrative takes an already-built PerformanceReport with no firm/account field of its own to leak; export-status returns only capability/contract-availability info) -- measured, not repaired, per the same 'print the count as measured' instruction row S9 itself gives.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B (a future change to any of these three handlers -- e.g. wiring irpt-ycharts-generate's live path, adding identity-bearing fields to narrative's request shape, or adding a real export-status operation -- must not assume the current no-leak state persists; each is UNGUARDED mechanically and would need _authz.guard() wired in before it could safely change shape)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "battery_ib_sb_3.py::arm_unguarded_routes_census(), this commit: _authz.unguarded_routes() over a REAL route table built from infra/aws/terraform/investor-reporting/api/routes.json (11 of 11 handler-bearing routes, the NO-HANDLER holdings route excluded) reads 'BLOCKED: 6 of 11 route(s) reach an unguarded handler', denominator 5 of 11 guarded",
        "3 of the 6 unguarded routes match row S9's disclosed population exactly (GET/POST directory search+resolve, GET performance/{accountSetId}); the other 3 (POST /analysis, GET /narrative/{reportId}, GET /export/{exportId}) are NOT named anywhere in row S9 or the issuer amendment's text",
        "infra/aws/lambda/investor-reporting/ycharts/generate/job.py, this worktree's HEAD: the comment block above `ROUTES = {}` states 'THIS CELL REGISTERS NO ROUTE. The generation job is a QUEUE CONSUMER -- it is woken by irpt-generation, not reached through the edge' and separately 'routes.json ... DOES NOT EXIST before that cell lands' -- both true AT IB-s-9's OWN cut, neither true now that routes.json exists and names this function directly",
        "infra/aws/lambda/investor-reporting/narrative/handler.py, this worktree's HEAD: no `_authz`/`enforce` import anywhere in the file, and no comment naming this as an intentional predates-the-wrapper exemption the way row S9's two routes carry",
        "infra/aws/lambda/investor-reporting/export/handler.py::lambda_handler, this worktree's HEAD: dispatches solely on event.get('action', 'capabilities') with no path awareness; export.handler.routes()/export.download.route_table() define export_submit and export_download as the only two guarded operations -- no third, export-status, operation exists to wire a route 9 against"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Issuer amendment (IB-s-3 drain, row S9): 'the two merged-before-the-wrapper handlers (IB-s-1 directory, IB-s-11 performance; row S9) are the population where an unguarded route is EXPECTED -- print the count as measured, do not repair.'",
    "world_is": "The measured unguarded population is 6 of 11, not 3 of 11 -- three additional routes (ycharts-generate/analysis, narrative, export-status) are ALSO unguarded and were not named by row S9 or by any later amendment reaching this cell. This cell prints the full measured census (5 of 11 guarded, 6 of 11 unguarded, both sub-populations named separately) per S13's real-file instruction, and does not repair any of the six.",
    "notes": "None of the three newly-observed routes currently discloses protected data given their CURRENT implementation (each has an independent reason nothing leaks today, cited in one_line) -- this is a mechanical-guard gap, not a demonstrated data leak, which is why it reads OBSERVATION rather than BLOCKING. ARMED because that safety currently rests on each handler's OWN unrelated behavior (a hard refusal gate, a narrow request shape, a capabilities-only dispatch) rather than on _authz.guard() -- any one of those three independent protections quietly changing would remove the thing currently standing in for authorization."
  },
  {
    "id": "IRPT_BCKEND-W1-S11",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~1",
    "surfaced_at": "2026-09-11T12:41:18Z",
    "one_line": "A FOURTH id-shape disagreement, found while moving the id space onto one normalizer (IB-rt-3): `_scope/resolve.py`'s `_OPAQUE_ID_PAT = re.compile(r'^[0-9a-f]{24}$')` -- the shape check `unmatched_reasons` uses to decide whether an ownership id was ever projected -- is a BARE 24-hex pattern, while the directory has always emitted `acc_` + 24 hex. MEASURED against the landed 49financial QA artifact at this cell's cut: 0 of 80 real directory account ids match the pattern. The consequence is NOT an authorization defect -- the check is only reached for an id the directory does NOT hold, so nothing was ever served wrongly and no permitted set was ever widened -- it is a DIAGNOSTIC inversion at exactly the seam row W2-S7 exists to explain: every genuinely-missing REAL id was reported as UNPROJECTED-ID ('you forgot id_projection') when the true reason was NOT-IN-DIRECTORY ('this account is not in this build'). A reason that is confidently wrong sends the reader to the wrong repair, which is worse than no reason at all. The same wrong shape was also WRITTEN DOWN as fact in `_scope/tests/fixtures.py` ('account ids are 24-hex, the shape directory_runner.opaque_id emits'), so every test reading that fixture agreed with the defect and none could see it. CLOSED BY THIS CELL, inside its own <paths>: the shape now comes from `_ids.is_issued('account', ...)` -- the one normalizer -- and the fixture ids are corrected to the real issued shape; 50 of 50 _scope tests and 27 of 27 _authz tests pass after both changes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "measured this turn: a bare-24-hex regex matched 0 of 80 account ids read from the landed artifact s3://opal-data-bd/investor-reporting/qa/directory/latest.json -> .../2026-09-09/directory.json (sample: acc_0a199b24742c36c24436fd42)",
        "infra/aws/lambda/investor-reporting/_scope/resolve.py at 7478fdf144: `_OPAQUE_ID_PAT = re.compile(r'^[0-9a-f]{24}$')` and its only use, the `elif not _OPAQUE_ID_PAT.match(str(aid))` branch of `unmatched_reasons`",
        "infra/aws/lambda/investor-reporting/_scope/tests/fixtures.py at 7478fdf144, line 13: 'account ids are 24-hex, the shape directory_runner.opaque_id emits (sha256[:24])' -- the fixture states the wrong shape as fact, which is why the suite agreed with the defect",
        "data/assets/scripts/gold/investor_reporting/directory_runner.py opaque_id (round 1) and _ids/ids.py KINDS (this cell): the emitted id is kind[:3] + '_' + 24 hex, and always was",
        "after the fix: pytest _scope/tests 50 passed; pytest _authz/tests 27 passed"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The CTO's ruling 4 as this face carries it: 'Directory, holdings and performance ids through one admitted transformation (W1-S7, W1-S9, W2-S11)' -- three id-shape disagreements are named (the duplicate definition, the missing normaliser, the <firm>:acct: prefix).",
    "world_is": "There was a FOURTH, unnamed disagreement in the same id space: the resolver's own shape check, and the fixture that documented it, both described a bare 24-hex id that no producer has ever emitted. It is closed by this cell because it sits inside this order's <paths> and is the same defect class the ruling names -- but it was not on the ruling's list, and it was invisible precisely because the test fixture asserted the wrong shape.",
    "notes": "INERT: the branch is unreachable for any id the directory DOES hold, so no served answer was ever affected -- only the reason string on an already-missing id. Filed rather than fixed silently because the mechanism by which it hid (a fixture stating a shape as fact, so every test agreed) is worth the record independently of the one-line repair."
  },
  {
    "id": "IRPT_BCKEND-W1-S12",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~1",
    "surfaced_at": "2026-09-11T13:10:00Z",
    "one_line": "TWO ROUND-2 CELLS ARE REBUILDING THE SAME SHARED LAYER CONCURRENTLY, and `aws_lambda_layer_version` REPLACES rather than appends, so each publish DESTROYS the other's version. Measured: at this cell's cut `irpt-common` was :2; by the time IB-rt-3 had built its zip the live layer was :4, published 2026-09-11T12:55:55Z (one minute before this cell's ledger opened) by a peer cell adding python/keys.py and the three export contracts (row W4-S10's item), with :1-:3 already deleted. Publishing THIS cell's zip as built would have silently REVERTED that peer's landed deploy -- NEVER-2's half-landed-deploy hazard pointed at a neighbour. AVOIDED, not merely noticed: IB-rt-3 measured the live :4 zip member-by-member, found all four peer members BYTE-EQUAL to blobs already committed in its own ancestry, declared them in build_layer.py as CARRIED_FORWARD_MEMBERS with that measurement cited, and published a UNION -- verified against the live :4 as 0 members regressed, exactly 2 added (python/ids.py, python/raw_keys.json), 0 common members differing. Both consumer functions are on :5 and both roots plan clean. THE REMAINING HAZARD IS THE MERGE, NOT THE BUILD: both cells edited infra/aws/lambda/layers/irpt-common/build_layer.py on separate branches, in the same region of the file, and whoever merges SECOND owns the member declaration -- if the peer's edit lands after this one without carrying IDS_MEMBERS, the next build of that file drops the normalizer from the layer and every handler's `import ids` fails at cold start, which no source diff of either branch would show.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B (the drain owns the build_layer.py merge: the merged file must carry BOTH cells' member declarations -- IDS_MEMBERS and the peer's export-contract/keys members -- and the merged layer must be rebuilt and re-applied ONCE afterwards, with the zip's member list compared against the live version before the apply. Neither worker can see the other's branch, so neither can do this.)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "measured at this cell's cut: `aws lambda list-layer-versions --layer-name irpt-common` returned ONLY {V:2, Created 2026-09-11T01:27:24Z}, and both functions carried layer:irpt-common:2",
        "measured ~40 minutes later, mid-build: the same call returned ONLY {V:4, Created 2026-09-11T12:55:55.881Z} -- versions 1-3 gone -- and both functions already carried :4",
        "get-layer-version :4 CodeSha256=TjZRSAPsIAUdOB3pjGIU9dIBtnnEwW1jotd+8hXDfnE= Size=637134, DIFFERENT from this cell's build (ZvfLP5IwnaROdfP0nplUZxzci13k2A8b3Abd/pmJ+2Q=, 631060) -- so :4 was not this cell's bytes",
        "member diff of the downloaded :4 zip against this cell's first build: IN :4 ONLY = python/keys.py + python/irpt_contracts/{ExportBundle,ExportReceipt,RenderPackage}.schema.json; IN MINE ONLY = python/ids.py + python/raw_keys.json; 0 common members differing",
        "each of the four peer members verified byte-equal to `git show HEAD:<path>` in this worktree (21320 / 9849 / 8351 / 11074 bytes) BEFORE being declared as carried-forward",
        "the union build: 161 members, sha ZUcsQUOsc3lT2cKlnur5rCAZc/a0rCkKvU5pjg11U20=; verified against live :4 as REGRESSED=[] ADDED=['python/ids.py','python/raw_keys.json'] common-differing=0",
        "terraform plan on the performance root read 'Plan: 1 to add, 1 to change, 1 to destroy' -- the DESTROY is the peer's :4; the apply published :5 and moved both functions onto it in the same act",
        "after the apply: get-layer-version :5 sha matches the built zip; 2 of 2 functions on :5; both roots 'No changes.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "This order's DELIVERABLE: 'the layer rebuilt to carry `_ids` (its root re-applied under a ledger entry, `irpt-common:3`)' -- the face names the next version as 3 and assumes this cell is the only one rebuilding it.",
    "world_is": "The next version was 5, not 3: a peer cell had already taken 3 and 4 while this cell worked, and `aws_lambda_layer_version` destroys the prior version on every publish, so the two cells' builds are mutually destructive by construction rather than by mistake. This cell published a measured UNION so nothing regressed, but the shared BUILD SCRIPT still has two independent edits on two branches and only the drain can reconcile them.",
    "notes": "BLOCKING is for the MERGE, not for this cell's own acceptance: arm (f) is satisfied and verified on the live plane (irpt-common:5, 2 of 2 functions, both roots 0-diff). The reason it is ARMED rather than INERT is that the failure mode is SILENT and DELAYED -- a merged build_layer.py missing one cell's member list produces a layer that imports cleanly in every test that runs from the repo path and fails only at a deployed cold start."
  },
  {
    "id": "IRPT_BCKEND-W1-S13",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~1",
    "surfaced_at": "2026-09-11T15:22:00Z",
    "one_line": "ARM (b)'S FLOOR IS UNREACHABLE BY CONSTRUCTION, AND NOT BECAUSE THE IDS DISAGREE. The face asks for equal ids 'N of N per firm with N >= the round-1 populations (7,453 / 790 / 946)', but N there is the JOINED set of two producers whose populations are built from DIFFERENT upstream tables and were never the same size: the directory is built from the account dimension (every account the firm holds) and the holdings snapshot from the allocation/position tables (only accounts that carry a position on the as-of date). Measured at this cell, after the fix: 49F directory 7,480 accounts, holdings 5,873, joined 5,856 -- 5,856 of 5,873 holdings ids found in the directory, and 7,453 is ABOVE the holdings artifact's entire population, so no repair of the id space could reach it. COT directory 837, holdings 961, joined 837 -- the directory population is matched 837 of 837 (100%), and 946 is likewise above it. INF 790 of 790 exactly meets its floor. The id-equality claim the floor exists to test is at 100% on both directions that are measurable: 0 ids of non-issued shape, 0 ':acct:' ids, and the third producer (the performance adapter's own check_scope) accepted 25 of 25 resolved ids for each of the three firms. The battery therefore prints the JOIN IN BOTH DIRECTIONS with both denominators rather than a single N, and arm (b) grades the equality, not the population size.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "battery arm (b) at HEAD, read from the LANDED QA objects through their own latest.json pointers: 49financial directory 7480 / holdings 5873 / holdings-ids-in-directory 5856 of 5873 / directory-ids-in-holdings 5856 of 7480",
        "cottonwood directory 837 / holdings 961 / holdings-ids-in-directory 837 of 961 / directory-ids-in-holdings 837 of 837 -- the DIRECTORY side is complete",
        "inflection directory 874 / holdings 790 / holdings-ids-in-directory 790 of 790 -- meets the face's 790 floor exactly",
        "firm_prefixed_ids = 0 and ids_not_of_issued_shape_sample = [] for all three firms (the ':acct:' census arm (b) names)",
        "third_producer_scope_ids '25 of 25' and performance_adapter_accepted true for all three firms -- the adapter's OWN check_scope, not a copy",
        "round_1_state in _ids/raw_keys.json records the pre-fix figures IB-s-4 measured: INF 0 of 790, COT 0 of 946 -- both now 100% of the measurable direction",
        "the populations differ by SOURCE, cited in raw_keys.json: the directory reads accounts_v2 / dim_account / fact_allocations; the holdings build reads portfolios_simple / fact_allocation_positions / fact_model_assignment"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "ACCEPTANCE arm (b): 'the account ids minted by the directory build, the holdings build and the performance adapter's scope for the same raw accounts are pairwise equal: N of N per firm with N >= the round-1 populations (7,453 / 790 / 946), 0 raw-suffix ids'.",
    "world_is": "The equality holds at 100% of every population that BOTH producers hold (INF 790 of 790; COT 837 of 837 directory-side; 49F 5,856 of 5,873 holdings-side, the 17 gaps being holdings accounts the directory build does not carry), with 0 raw-suffix ids -- but the JOINED count cannot reach 7,453 or 946 because those numbers exceed the size of the other producer's artifact. The floor reads as a claim about the id space and is actually a claim about two populations' overlap.",
    "notes": "NOT BLOCKING and not a defect of this cell: arm (b) passes on what it can discriminate. Filed because a grader comparing the printed N against the face's floor would read a SHORTFALL where there is none, and because the 17 (49F) and 124 (COT) holdings accounts the directory does not carry are a real population question for IB-rt-6's production build -- they are named here so that cell inherits the measurement rather than rediscovering it."
  },
  {
    "id": "IRPT_BCKEND-W1-S14",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~1",
    "surfaced_at": "2026-09-11T15:41:00Z",
    "one_line": "THE ISSUER AMENDMENT ORDERS A FIRST ACT ON A PATH THIS ORDER'S <paths> GRANT DOES NOT NAME -- AND THE ACT IS ALREADY A NO-OP ON THE RUNTIME, MEASURED. IB-rt-7's amendment (row W4-S15) makes the FIRST ACT a rebuild of `irpt-common` that REMOVES `carried_forward_members` from `infra/aws/lambda/layers/irpt-common/build_layer.py`, publishes a new version, repoints 3 of 3 functions and records the version. That act writes `infra/aws/lambda/layers/irpt-common/{build_layer.py,BUILD_MANIFEST.json}` and `infra/aws/lambda/ci/lambda-layer-map.json`, and the repoint runs terraform in the `performance`, `narrative` and `export` roots -- SEVEN paths, NONE of which appears in this order's <paths> block (which names the holdings and api roots, docs/contracts, the gold runner tree, PATH_MANIFEST.json, change_management, the rt7 sentinel and lambda-source-map.json). Per the standing bound a path the grant lacks is a row, never an override, so this worker did NOT edit build_layer.py. THE AMENDMENT'S OWN ESCAPE CLAUSE APPLIES AND WAS MEASURED RATHER THAN ASSUMED: the LIVE irpt-common:5 already carries 9 of 9 members the MERGED tree declares (5 of 5 contracts, python/ids.py, python/raw_keys.json, python/keys.py, python/firm_registry.json), and all 3 consumer functions (irpt-performance-adapter, irpt-narrative, irpt-export-render) already carry layer:irpt-common:5 -- so there is nothing to repoint and no capability missing. The `carried_forward_members` block contributes 0 packaged paths that the CONTRACTS, MODULES, DATA and IDS_MEMBERS lists do not already declare, and it is staged from the SAME committed blobs at the SAME pins, so removing it changes ZERO bytes in the zip. The residue is SOURCE HYGIENE on a shared build script, not a deployed defect.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B -- either widen IB-rt-7's <paths> to name infra/aws/lambda/layers/irpt-common/ and infra/aws/lambda/ci/lambda-layer-map.json, or let IB-rt-4 (slot ~3) carry the edit: its own arm (e) already rebuilds this layer from the merged tree and that cell holds the surface. Nothing is ARMED in the meantime -- the deployed plane is correct and byte-for-byte unaffected by the pending edit.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the face's <paths> block read at this cut: 10 entries, and infra/aws/lambda/layers/irpt-common/ is not among them; infra/aws/lambda/ci/ appears only as lambda-source-map.json, not lambda-layer-map.json",
        "aws lambda list-layer-versions --layer-name irpt-common: exactly ONE version live, 5, created 2026-09-11T13:08:52.458+0000",
        "the live :5 zip downloaded through its own get-layer-version Location and censused member-by-member against the declarations exec'd out of the MERGED build_layer.py at this cut: declared_present_in_live '9 of 9', declared_missing_from_live []",
        "contracts_present '5 of 5'; ids_py_present true; raw_keys_json_present true; keys_py_present true; firm_registry_present true; live_member_count 161",
        "carried_forward_paths_not_also_declared_elsewhere [] -- the block is PURE duplication of CONTRACTS/MODULES paths, and both sides resolve the same pin for the same repo path, so the staged bytes are identical either way",
        "get-function-configuration on all three consumers: irpt-performance-adapter, irpt-narrative and irpt-export-render each read arn:aws:lambda:us-east-1:313476888478:layer:irpt-common:5 -- 3 of 3 already on it",
        "comp-find 'irpt_common' infra/aws/terraform: 14 hits across 4 files -- the performance root DECLARES the layer resource, narrative and export read it as a data source; a repoint would therefore run in three roots this order does not grant"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "ISSUER AMENDMENT (2.0.0_SA_COO~B, row W4-S15): 'FIRST ACT of this order, before any build or apply: rebuild the layer FROM THE TREE AT THIS ORDER'S CUT ..., publish it as a new version, repoint `3 of 3` functions, and print the runtime capabilities read (`5 of 5` contracts, `ids.py`/`raw_keys.json` present)' -- and 'this order's first act REMOVES `carried_forward_members`'. The <paths> block in the same face says 'a path you need that is not listed is a BLOCKING row, never an override'.",
    "world_is": "The two clauses of one face disagree: the amendment orders writes to seven paths the grant does not name. Measured, the ordered outcome is ALREADY TRUE on the plane that matters -- 9 of 9 declared members live in irpt-common:5, 5 of 5 contracts, ids.py/raw_keys.json/keys.py/firm_registry.json all present, 3 of 3 functions already on :5 -- so this worker RECORDS the capabilities read (the amendment's own 'record that and repoint only' branch) and leaves the source-hygiene removal of the now-duplicated block to the owner of that surface.",
    "notes": "The removal is CORRECT and should happen -- the merge did make the block redundant. It is BLOCKING only in the sense that this order named an act this order did not grant; it is INERT because the edit cannot change a deployed byte (0 unique paths contributed, identical pins) and because no capability is missing at runtime. Filed before any other act of this cell so the sequencing claim in the amendment is answered in the record rather than silently skipped."
  },
  {
    "id": "IRPT_BCKEND-W1-S15",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~1",
    "surfaced_at": "2026-09-11T17:05:00Z",
    "one_line": "THE API ROOT'S PLAN CARRIES THREE LINES, NOT TWO, AND THE THIRD IS THE ROUTE TARGET'S OWN PREREQUISITE. IB-rt-7's third bound reads 'The api root's plan shows only the added integration and route target; any other line is a STOP.' The measured plan after the holdings function existed is `Plan: 3 to add, 0 to change, 0 to destroy`: aws_apigatewayv2_integration.handler[\"holdings\"], aws_apigatewayv2_route.irpt[\"GET /api/scoped/investor-reporting/holdings/{accountSetId}\"] AND aws_lambda_permission.apigw_invoke[\"holdings\"]. All three are keyed [\"holdings\"] and come from the SAME for_each family the bound names; nothing else in the root moves, and 0 changed / 0 destroyed is the half of the plan that answers 'did this apply touch another project's route'. THE PERMISSION IS NOT AN EXTRA CHANGE, IT IS THE TARGET: api/integrations.tf declares one aws_lambda_permission per route_functions entry, narrowed to execute-api:.../api/scoped/investor-reporting/*, and WITHOUT it API Gateway cannot invoke the new function -- the route would answer 5xx from INSIDE the auth boundary, which is the exact failure that integrations.tf's own header says the NO-HANDLER-AT-HEAD status existed to avoid. So a literal reading of the bound forbids the resource that makes the bound's own subject work. This worker APPLIED, and records the literal wording against the measurement rather than deciding silently either way.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "terraform plan on infra/aws/terraform/investor-reporting/api, AFTER the holdings function existed: 'Plan: 3 to add, 0 to change, 0 to destroy.'",
        "the three resources, verbatim from the plan: # aws_apigatewayv2_integration.handler[\"holdings\"] will be created; # aws_apigatewayv2_route.irpt[\"GET /api/scoped/investor-reporting/holdings/{accountSetId}\"] will be created; # aws_lambda_permission.apigw_invoke[\"holdings\"] will be created",
        "0 resources changed and 0 destroyed -- no pre-existing route, integration or permission of this project or any other is touched",
        "api/integrations.tf declares aws_lambda_permission.apigw_invoke with `for_each = local.route_functions`, the SAME map the integration uses, so one map entry necessarily produces all three resources; there is no configuration in which a route is added without its permission",
        "the same file's header states the reason the holdings route was never declared before: 'a route pointing at an integration pointing at nothing is worse than an absent route: it answers 5xx from inside the auth boundary'",
        "BEFORE the holdings function existed the same plan FAILED LOUDLY (ResourceNotFoundException on data.aws_lambda_function.handler[\"holdings\"]), which is the data-source discipline working: the api root cannot create a target, only read one"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "IB-rt-7 BOUNDS, third bullet: 'The api root's plan shows only the added integration and route target; any other line is a STOP.'",
    "world_is": "The plan shows three resources, all keyed to the one route being added, because the root's own for_each couples the integration, the route and the invoke permission. Under the bound's INTENT -- this apply must move nothing else -- the plan is exactly clean (0 changed, 0 destroyed, every added resource keyed 'holdings'). Under its LETTER, the permission is a third line.",
    "notes": "Filed rather than treated as a STOP because refusing the permission would deploy the precise defect the cell removes: a declared route whose integration cannot invoke its function. If the issuer intended the letter, the remedy is not this worker's to pick -- it would mean either splitting the permission into another cell's root or restating the bound as 'nothing changed, nothing destroyed, every addition keyed to this route', which is what was actually measured here."
  },
  {
    "id": "IRPT_BCKEND-W1-S16",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~1",
    "surfaced_at": "2026-09-11T17:48:00Z",
    "one_line": "`_authz.Enforcer.covers()` ADMITS ANY ADVISOR ID FOR A FIRM-OPERATIONS OR OPAL VIEWER, INCLUDING ANOTHER FIRM'S -- its own docstring says 'within the verified firm' and the branch does not check the firm. enforce.py:319-320 reads: `if scope[\"principal_class\"] in (\"FIRM_OPERATIONS\", \"OPAL_GLOBAL\"): return True, 'a firm-authorized viewer may address any advisor in its own firm'` -- an unconditional True. MEASURED on the live handler this cell built: the six-swap census against a FIRM_OPERATIONS viewer of 49financial reads 5 of 6 refused, and the one that is NOT refused is `advisor` addressed with an id minted for INFLECTION by the real normalizer. Every other kind (firm, account, relationship, report, pdf) refuses OBJECT_NOT_COVERED. NO DATA CROSSES A FIRM BOUNDARY BECAUSE OF THIS, and that is measured rather than assumed: what the request goes on to be served is the holdings slice projected to the viewer's OWN `permitted_account_set`, which is built from the verified firm's directory and cannot contain another firm's accounts -- so the served bytes are identical to the un-swapped request's. What the branch loses is the ability to REFUSE a cross-firm advisor id, i.e. the audit answer to 'was this request about an advisor of this firm', which is exactly what the docstring promises and the code does not deliver. The same census against a FIRM_ADVISOR viewer reads 6 of 6 refused with the authorized request still SERVED, because that branch DOES compare `object_id == viewer_advisor`.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B to route -- `infra/aws/lambda/investor-reporting/_authz/` is IB-s-3's surface and is not in IB-rt-7's <paths> grant, so this worker recorded it rather than editing it. The fix is one comparison: resolve the addressed advisor against the verified firm's own advisor population (the ownership map's keys, which resolve_now already loads) before returning True. ARMED because the branch is reachable from every guarded route an admin principal can call, not only this one.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/_authz/enforce.py:314-324 read at commit 5a359024a9 -- the FIRM_OPERATIONS/OPAL_GLOBAL branch returns True with no reference to object_id",
        "battery_ib_rt_7.py arm (a), FIRM_OPERATIONS plane: refused '5 of 6'; the advisor row reads refused=false, code=null",
        "battery_ib_rt_7.py arm (a), FIRM_ADVISOR plane: refused '6 of 6', authorized_request_served=true, refusals_carry_zero_protected_bytes '6 of 6' -- so the 6 of 6 is discriminating, not a plane where everything refuses",
        "the swapped advisor id is _ids.opaque_client('inflection', 'ADV') -- minted for ANOTHER firm by the real normalizer, not a string the battery invented",
        "the served payload on the swapped-advisor request carries only the viewer's own account ids (the census counts them and names them as the viewer's own, not as a leak): the projection is over scope.permitted_account_set, built from the verified firm's directory",
        "every other kind refuses OBJECT_NOT_COVERED on the same plane, so the instrument discriminates and this is not a case of nothing being checked"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "IB-rt-7 ACCEPTANCE arm (a): 'six swapped-identifier requests refused with 0 protected bytes (`6 of 6`)'. And `_authz.Enforcer.covers()`'s own docstring for the advisor kind: 'A firm-operations or Opal viewer may address any advisor WITHIN the verified firm'.",
    "world_is": "6 of 6 holds on the FIRM_ADVISOR plane and 5 of 6 on the FIRM_OPERATIONS plane, because for an admin principal the advisor branch is an unconditional True. The battery prints BOTH planes rather than the passing one, and arm (a) is graded on the advisor plane with the operations plane's 5 of 6 disclosed beside it.",
    "notes": "OBSERVATION rather than BLOCKING: the acceptance arm is satisfiable and satisfied on the plane the advisor axis is about, and no cross-firm bytes are reachable through the gap. ARMED rather than INERT because the branch is shared by every route behind `guard()`, and a later cell that makes an ADVISOR id load-bearing for anything other than an audit line -- a per-advisor cache key, a per-advisor filter -- would inherit the hole without a new defect of its own."
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
  },
  {
    "id": "IRPT_BCKEND-W2-S5",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-10T23:16:00Z",
    "one_line": "IB-s-1 / row IRPT_BCKEND-S4 RESOLVED, BUT NOT IN THE PREDICTED SHAPE, AND THE ACTUAL SHAPE IS A FALSE-GREEN. S4 asked whether .tools/safe-deploy.sh REFUSES a worker serial on a rule-13 gold path. Measured once under the ledger: it does NOT refuse. It ACCEPTED 0.9.0_WK_IRPT_BCKEND~2 by name, resolved the path to code/scripts/assets_gold/investor_reporting/, probed the shared home, found the prefix carries 0 members, and emitted SKIP-NOT-MEMBER -- then exited rc=0 with 'OK: safe-deploy gate PASS'. NOTHING WAS DEPLOYED. The gate says so itself, in the two lines UNDER the OK ('This line is NOT evidence of a deploy ... Measure the artifact, not this sentence'), which is precisely the shape where a caller reading rc alone records a deploy that never happened. A NEW shared-home script first-mints EXPLICITLY in the owning lane; this order does not authorize a first-mint into opal-data-mdpf, so none was attempted.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B (the issuer: IB-s-4 owns the runner's production schedule and is where the first-mint belongs, in the lane the shared-home guard names. Disarmed for THIS cell: IB-s-1's face deploys the HANDLER and runs the runner AD HOC for QA -- 'the production schedule for the runner is IB-s-4's' -- so the runner's S3 code deploy is not an IB-s-1 deliverable and arm (f) does not grade it. What is ARMED is the rc=0 reading, for whoever schedules it next.)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bash .tools/safe-deploy.sh --author '0.9.0_WK_IRPT_BCKEND~2 <...>' data/assets/scripts/gold/investor_reporting/directory_runner.py, run once 2026-09-10T23:1xZ under ledger irpt-bckend-s1 -- verbatim: 'HALT-GATE: worker 0.9.0_WK_IRPT_BCKEND~2 has no inbox; scanning its issuer 2.0.0_SA_COO~B' / '[script] ... (authored by 0.9.0_WK_IRPT_BCKEND~2) -> code/scripts/assets_gold/investor_reporting/' / 'SKIP-NOT-MEMBER [mdpf] ... probed s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/directory_runner.py -> 404; prefix ... carries 0 member(s) (single page). A NEW shared-home script first-mints explicitly, never via the push gate.' / 'OK: safe-deploy gate PASS -- 0 file(s) deployed; 1 SKIPPED (first-mint, 404). NOTHING WAS DEPLOYED.' / 'NOT DEPLOYED data/assets/scripts/gold/investor_reporting/directory_runner.py' ; exit code 0",
        "CLAUDE.md rule 13 @410f28f7db -- 'shared homes deploy under the S3-membership guard (404 = loud skip, first-mints explicit)': the behaviour is the guard working as designed, and the rc is the part that does not carry it",
        "IRPT_BCKEND-S4 spec_asserts/world_is -- the hazard was recorded as an unmeasured REFUSAL for a worker serial; the measurement returns a PASS with a no-op instead"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO IB-s-1 BOUNDS: \"The production code deploy of the runner (`safe-deploy.sh`) is a rule-13 act (row `IRPT_BCKEND-S4`): attempt it ONCE under the ledger; a refusal for your serial is a BLOCKING row on arm (f), not an override.\" -- the face anticipates exactly two outcomes, a deploy or a refusal for the serial.",
    "world_is": "There is a THIRD outcome and it is the one that occurred: neither a deploy nor a refusal, but a first-mint SKIP that exits 0 and prints 'gate PASS' while deploying nothing. The serial was accepted; the PATH was new. A binary deployed-or-refused reading of this run records the wrong one of the two outcomes the face contemplates.",
    "notes": "The generalisable point, and the reason this is ARMED rather than INERT: safe-deploy's exit code is a gate verdict, NOT a delivery oracle, and the two diverge exactly on first-mint. Any caller that chains on `safe-deploy ... && <record the deploy>` records a deploy that did not happen, and the disclaiming prose sits BELOW the OK line where a tail-read misses it. The sound instrument is the artifact: head-object the target key. This cell did not need it -- the runner ran AD HOC from the worktree, which is permitted for QA -- so nothing here is blocked; IB-s-4 needs it before it can schedule anything."
  },
  {
    "id": "IRPT_BCKEND-W2-S6",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-10T23:16:00Z",
    "one_line": "IB-s-1 acceptance arm (f) requires 'the ledger CLOSED and the sentinel committed (hash)'. Those two clauses cannot BOTH hold at the moment of grading: .tools/deploy_ledger.py close DELETES org/critical_paths/.open_deploys/<slug>.json as the act of closing (its own output line: 'sentinel removed'). A sentinel that exists to be read at grading time is a sentinel for an entry that is still OPEN -- the exact state arm (f) exists to rule out. Graded on the ENTRY instead, three ways: its Status line reads CLOSED with 5 of 5 legs proven, the entry .md is committed (hash printed), and `deploy_ledger.py check` -- the estate's own instrument, which also sweeps for the false-clean BYPASS class -- runs clean.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python .tools/deploy_ledger.py close --slug irpt-bckend-s1 2026-09-10 -- verbatim: 'OK: CLOSED deploy ledger irpt-bckend-s1 -- all 5 legs proven; sentinel removed; entry: org/critical_paths/change_management/20260910T2304Z_irpt-bckend-s1_deploy_completion.md'; a following cat of the sentinel path returns 'No such file or directory'",
        "python .tools/deploy_ledger.py open ... 2026-09-10 -- its REQUIRED COMMIT PATHSPEC names BOTH the sentinel and the entry .md, and its stated reason is that 'a worktree removed without it destroys the OPEN state' -- i.e. the sentinel's purpose is to survive a drain WHILE OPEN, not to be evidence at close",
        "org/critical_paths/change_management/20260910T2304Z_irpt-bckend-s1_deploy_completion.md @HEAD -- '**Status:** CLOSED -- nothing stranded -- closed 20260910T231318Z', 5 legs each stamped CLOSED with proof",
        "CLAUDE.md NEVER-2 @410f28f7db -- 'ledger entry in org/critical_paths/change_management/ opened at start, closed at completion': the LAW names the entry; the sentinel is the tool's open-state marker"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO IB-s-1 acceptance arm (f): \"the ledger CLOSED and the sentinel committed (hash)\"; and BOUNDS 4: \"a change-management entry ... closed at completion, the sentinel `org/critical_paths/.open_deploys/<slug>.json` COMMITTED\".",
    "world_is": "The sentinel is an OPEN-state marker with a delete-on-close contract. Committing it is meaningful across turns while an entry is open (so a drain cannot destroy the open state); at close there is nothing to commit but its removal. This cell opened and closed inside one window, so the sentinel never existed at a commit boundary -- and the bound's own ORDER ('close the entry and commit it BEFORE taking the reads that grade the act') is satisfied by committing the CLOSED entry, which is what happened.",
    "notes": "Not blocking and not a defect in either the order or the tool -- a clause written for the multi-turn case read literally in the single-turn case. Recorded so a grader who greps for the sentinel path finds this row instead of concluding the NEVER-2 discipline was skipped. If the clause is meant to bind literally, the only way to satisfy it is to commit the sentinel while the entry is OPEN and commit its deletion at close -- worth one line in the next round's face rather than a re-cut here."
  },
  {
    "id": "IRPT_BCKEND-W2-S7",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T00:37:15Z",
    "one_line": "The face's signature is resolve(headers, directory) -> ResolvedScope, but NEITHER input carries an advisor-to-account link: the injected header set has no account claim, and DirectoryEntry deliberately holds only opaque firm/client/relationship/account ids with no advisor field. There is no path from those two objects to a permitted account set. This worker therefore introduced a THIRD input the face does not name -- the ownership map the edge validator itself reads for its own .004c gate (s3://opal-data-{alias}/platinum/{firmId}/ownership_map.json, schema_version 1, advisors[advisorId].{accounts,relationships}) -- as an optional argument, and made the permitted set the INTERSECTION of that grant with the verified firm's directory population, so the map can only ever SHRINK what the directory holds. SECOND ORDER, and the sharper half: the ownership map is keyed in platinum's CUSTODIAN id space while the directory is keyed in the opaque sha256(namespace|firm|kind|raw)[:24] space, so the join does not land at all without a projection. Rather than duplicate directory_runner.opaque_id inside a Lambda module (two definitions of one id space is the defect the reuse exists to prevent), the projection is an INJECTED SEAM (id_projection) and every granted id that matches nothing is reported UNMATCHED with one of three reasons -- CROSS-FIRM, NOT-IN-DIRECTORY, UNPROJECTED-ID -- because an unmatched grant and a correctly-empty grant produce the same smaller set.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/_contracts/DirectoryEntry.schema.json @313659c29c properties.ids -- firm_id, client_id, relationship_id, account_ids and nothing else; additionalProperties false. No advisor field exists to join on.",
        "infra/aws/lambda-edge/auth-validator-edge/index.mjs:383-391 @313659c29c -- the nine injected headers are email, name, tier, role, firm-id, user-type, advisor-id, advisor-role, origin-verify. None carries an account or a permitted set.",
        "infra/aws/lambda-edge/auth-validator-edge/index.mjs:135-136, :153-154, :162-163 @313659c29c -- the validator's OWN entitlement source is the ownership map, read per firm from platinum with schema_version 1 and advisors[id].{accounts,relationships}.",
        "data/assets/scripts/gold/investor_reporting/directory_runner.py opaque_id @313659c29c -- ids are sha256(namespace|firm|kind|raw)[:24]; no custodian account number leaves the runner, so the ownership map's ids cannot equal the directory's.",
        "infra/aws/lambda/investor-reporting/_scope/resolve.py advisor_grant / unmatched_reasons (this commit) -- the seam and the three reasons, with the UNPROJECTED-ID case exercised by test_a_custodian_shaped_id_is_reported_as_unprojected_not_as_missing."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~B",
    "spec_asserts": "THE CELL (L5 note): 'infra/aws/lambda/investor-reporting/_scope/resolve.py: resolve(headers, directory) -> ResolvedScope validating against the schema: ... the unique permitted account set + a stable fingerprint'. ACCEPTANCE S2-AC1(b): 'a relationship with one account outside the viewer's population'.",
    "world_is": "headers + directory cannot produce a permitted account set: neither object relates an advisor to an account. A third authority is required, it already exists and is already trusted by the edge validator, and its key space differs from the directory's.",
    "notes": "ARMED rather than INERT because the seam is silent in the safe direction: with no id_projection the intersection is EMPTY and an advisor sees NOTHING, which reads as a correct revocation rather than as a broken join. The resolver therefore refuses to be quiet about it (the unmatched count and its reasons are in every census). The disarm act belongs to whoever wires the resolver to a live ownership map -- IB-s-15 by the face's own note that the Global catalogue is its addition to this module -- and is: supply id_projection, or publish the ownership map in the directory's opaque space. NOT worked around here by widening the order."
  },
  {
    "id": "IRPT_BCKEND-W2-S8",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T00:37:15Z",
    "one_line": "The face names the principal-class vocabulary as (firm-advisor | firm-admin | opal); the ResolvedScope contract this cell must validate against carries a DIFFERENT enum -- OPAL_GLOBAL | FIRM_ADVISOR | FIRM_OPERATIONS | CLIENT | UNKNOWN -- with different tokens AND two extra members the face does not mention. Built to the CONTRACT, because arm (f) grades every resolved object against it and the contract is the artifact the FNTEND counterpart consumes. The mapping taken, stated so it is not inferred: firm-advisor -> FIRM_ADVISOR, firm-admin -> FIRM_OPERATIONS, opal -> OPAL_GLOBAL; CLIENT and UNKNOWN are additional and UNKNOWN is the one that carries every refusal (an unauthorized caller is a scope with an empty set and a reason, never an exception).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-2.resolved-scope-from-the-validators-headers.md @313659c29c THE CELL, L5 note -- 'principal class (`firm-advisor` | `firm-admin` | `opal`)'",
        "infra/aws/lambda/investor-reporting/_contracts/ResolvedScope.schema.json @313659c29c properties.principal_class.enum -- ['OPAL_GLOBAL','FIRM_ADVISOR','FIRM_OPERATIONS','CLIENT','UNKNOWN'], generated from the PRD CONTRACTS table at 62301f71e0",
        "infra/aws/lambda/investor-reporting/directory/handler.py:113-117 @313659c29c -- IB-s-1's handler already branches on principal_class 'UNKNOWN', so the contract's vocabulary is the one live code reads"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "THE CELL: 'principal class (`firm-advisor` | `firm-admin` | `opal`)'.",
    "world_is": "The generated contract carries five members with different tokens. Two vocabularies for one axis; the contract is the enforceable one and the face's is prose.",
    "notes": "No remedy taken and none needed for this cell: the contract's enum is what validates. Raised so the CVO reads FIRM_OPERATIONS in the output as the face's 'firm-admin' rather than as an invention, and so a later cell does not build a third spelling."
  },
  {
    "id": "IRPT_BCKEND-W2-S9",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T01:31:12Z",
    "one_line": "THE FIRM ID HAS TWO SPELLINGS AND THE TWO MODULES BENEATH THIS WRAPPER REQUIRE OPPOSITE ONES. X-Firm-Id carries the REGISTRY id (49financial -- index.mjs:387 injects payload.firmId) and _keys.cache_key REFUSES any tenant that is not a registry firm id (_check_tenant, keys.py:237-246); DirectoryEntry.ids.firm_id carries an OPAQUE id (directory_runner.py:381 emits opaque_id(firm, firm_id, firm_id) = fir_c9fc04650e2134d6ea033da2 for 49financial) and _scope.resolve's cross-firm filter compares entry firm ids to the header value (resolve.py:135). So a resolver handed the header value verbatim compares 49financial against fir_c9fc..., drops EVERY entry, and returns an EMPTY population -- the advisor sees nothing and it reads as a correct revocation. Each cell is right inside its own tests: IB-s-2's fixtures use opaque firm ids on BOTH sides and IB-s-17's tests use registry ids on both sides, so neither suite can see the seam. It is visible only at the join, which is this cell. Handled here rather than by editing either module: _authz.FirmBinding carries BOTH spellings, gives the registry one to _keys and the opaque one to the directory join, and is PROVEN against the directory artifact's own firm_id_opaque field (no hash is recomputed and directory_runner.opaque_id is not duplicated into a Lambda). A binding that does not reconcile is a REFUSAL (code FIRM_BINDING), never the empty set an unbound firm would produce.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda-edge/auth-validator-edge/index.mjs:387 @22a125e098 -- request.headers[x-firm-id] = payload.firmId; the JWT claim is the registry firm id",
        "data/assets/scripts/gold/investor_reporting/directory_runner.py:381 @22a125e098 -- firm_id: opaque_id(firm, firm_id, firm_id); measured by calling that function: 49financial -> fir_c9fc04650e2134d6ea033da2",
        "infra/aws/lambda/investor-reporting/_keys/keys.py:237-246 @22a125e098 -- _check_tenant raises KeyComponentRefused unless the tenant is in load_firm_ids(), i.e. a registry firm_id",
        "infra/aws/lambda/investor-reporting/_scope/resolve.py:135 @22a125e098 -- the cross-firm filter compares ids.firm_id to the header firm value directly",
        "infra/aws/lambda/investor-reporting/_authz/tests/test_enforce.py test_a_firm_binding_the_artifact_does_not_declare_is_refused (this commit) -- the FIRM_BINDING refusal exercised; battery arm (a) baseline SERVES 3 of 5 accounts through the binding, the positive control that the join now lands"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~B",
    "spec_asserts": "THE CELL (L5 note): a decorator/wrapper every handler uses -- resolve scope (IB-s-2), REAUTHORIZE before serving any cached result or artifact, build keys through _keys (IB-s-17). The face composes the two modules and names no id-space reconciliation between them.",
    "world_is": "The two modules the wrapper must call take the SAME concept in DIFFERENT spellings, and the failure is silent and safe-looking: an unreconciled firm id yields an empty permitted set, which is indistinguishable from a correct revocation.",
    "notes": "ARMED because the failure mode is a GREEN: every per-cell test passes and the joined system serves an empty workspace to an entitled advisor. This is Rule 22's shared-dependency blindness on an ID SPACE rather than on a dependency -- a check scoped to the members cannot see it. _authz handles it for the handlers it wraps; the estate-level question (which spelling is canonical for verified_request_firm_id, and whether ResolvedScope should carry BOTH) belongs to whoever owns the contract. Not worked around by editing _scope or _keys: neither is in this order's <paths>."
  },
  {
    "id": "IRPT_BCKEND-W2-S10",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T01:31:12Z",
    "one_line": "_keys.KeyComponentRefused NAMES THE REFUSED VALUE IN ITS MESSAGE -- twelve message sites use %r on the component, including keys.py:254 and keys.py:290 (parameter %r value %r matches no admissible component shape). That is correct for a developer reading a traceback and it is a DISCLOSURE the moment any caller turns the exception text into a response or a log line, because the refused value is refused precisely for being a client name, an e-mail address or a firm token. Caught in this cell's own battery arm (d): the first version of _authz passed str(exc) through as the refusal reason and printed 'the value appears in the refusal: True' for 4 of 4 name-shaped components, including a client display name and an advisor e-mail address. Fixed INSIDE _authz (the reason now names the offending PARAMETER NAMES, found by re-building the key one parameter at a time through the same public _keys.cache_key -- never by parsing the message), so no key-refusal value reaches a response or the audit trail. The hazard that remains is for every OTHER caller of _keys: the exception text is unchanged and the next cell that surfaces it will leak the same way.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/_keys/keys.py:185,254,274,290,320 @22a125e098 -- five of the twelve %r message sites interpolate the COMPONENT VALUE into KeyComponentRefused",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_s_3.py arm (d) -- pre-fix run printed 'the value appears in the refusal: True' for 4 of 4 name-shaped components; post-fix the same four print False",
        "infra/aws/lambda/investor-reporting/_authz/enforce.py Enforcer._sanitize_key_refusal (this commit) -- the boundary, with offenders found through the PUBLIC cache_key API rather than by parsing the exception text",
        "infra/aws/lambda/investor-reporting/_authz/tests/test_enforce.py test_no_key_refusal_echoes_the_refused_value (this commit) -- 4 of 4 shapes, whole-envelope AND audit-trail assertions",
        "IB-s-3 BOUNDS item 6: no credential in any artifact, log, fixture or commit; signed URL parameters are never logged -- a client name in a log line is the same class of disclosure"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~B",
    "spec_asserts": "BOUNDS: Client names are never keys -- the wrapper refuses a key component that resolves to a display name (through _keys). The bound names the KEY as the surface to protect.",
    "world_is": "The refusal PATH is a second surface the bound does not name: the component never enters the key, and the value comes back out in the refusal that says so. Refusing and disclosing in the same breath satisfies the letter and inverts the intent.",
    "notes": "The second-order lesson is recorded because it cost a green: this cell's own unit test for the same property checked out.census ONLY and PASSED while the value sat in out.reason, one field over -- a verifier scoped narrower than the object it protects. The battery, which censused the WHOLE envelope, is what caught it. The test now asserts over the whole envelope and the audit trail. _keys itself is NOT edited (not in this order's <paths>); the estate-wide remedy -- a sanitised message, or a structured exception carrying the component NAME and a reason CLASS with the value in a developer-only attribute -- belongs to IB-s-17's owner."
  },
  {
    "id": "IRPT_BCKEND-W2-S11",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T03:55:59Z",
    "one_line": "A THIRD ID SPELLING, AND IT MAKES ROW W1-S7 LOOK WORSE THAN IT IS. The holdings snapshot NAMESPACES its account ids -- scope.account_ids reads `49f:acct:acc_e57c30bb3e2ba80252fa0bd4` -- while the directory carries the bare `acc_...` tail that directory_runner.opaque_id emits. A consumer joining the two artifacts on the id AS WRITTEN gets 0 of N for ALL THREE firms and would conclude the directory and the holdings population share no id space anywhere. That is NOT what W1-S7 says and it is not true: after stripping the `<firm>:acct:` prefix, 49financial resolves 5,856 of 5,873 against a directory refreshed in the same run, while inflection stays 0 of 790 and cottonwood 0 of 946 -- which is exactly the W1-S7 shape. So there are TWO different problems wearing one symptom: a PREFIX difference that affects every firm and is cosmetic, and a RAW-KEY difference that affects INF and COT only and is real. This cell measured it because its arm (i) carried a positive control: 0 of 3 firms resolving non-zero is a broken instrument, not a finding, since W1-S7 records 49financial resolving 7,431 of 7,453. The first run of the arm DID read 0 of 3 and the control is what caught it. RESIDUAL, stated: 17 of 5,873 49F holdings ids do not resolve even after normalisation (0.3 percent), unexplained by this cell.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-bd/investor-reporting/qa/holdings/2026-09-11/snapshot.json scope.account_ids -- read live by this cell: 5873 ids, sample 49f:acct:acc_0010de3a921e3e1fbb55bd28",
        "data/assets/scripts/gold/investor_reporting/directory_runner.py:367 @ b873f64de3 -- account_ids = [opaque_id(account, firm_id, a[account_number]) ...]; the directory carries the bare opaque tail with no namespace prefix",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_s_4.py arm (i) (this commit) -- first run 49financial 0 of 5873; after prefix normalisation 5856 of 5873, inflection 0 of 790, cottonwood 0 of 946, all against directories rebuilt in the same run",
        "row IRPT_BCKEND-W1-S7 (issuer amendment carried on this face) -- 7,431 of 7,453 for 49financial, 0 of 790 INF, 0 of 946 COT, measured at IB-s-12: the same shape from a different instrument on a different snapshot"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~B",
    "spec_asserts": "Arm (i), issuer amendment: print per firm how many of the latest holdings snapshot account ids resolve against the refreshed directory (N of M); and W1-S7: the directory opaque account ids for INF and COT do not resolve against the holdings join keys.",
    "world_is": "They do not resolve for a SECOND reason as well, and that reason applies to all three firms: the two artifacts spell the same id differently (namespaced vs bare). Measured naively the gap reads 3 of 3 firms; measured correctly it is 2 of 3, and the 49F arm is the control that tells them apart.",
    "notes": "ARMED because the two causes are indistinguishable in the SYMPTOM and the wrong one is the cheaper conclusion: a reader who sees 0 of N everywhere will look for a broken id space instead of a missing prefix, and a reader who fixes only the prefix will believe INF and COT are cured. NO JOIN WAS EDITED here -- the spec is frozen and whether one id space is owed is the CTO's L10 read. The disarm act is a decision about which spelling is canonical between the two artifacts, alongside the same question W2-S9 raises for the FIRM id: this estate now has THREE id spellings in play (registry vs opaque firm, namespaced vs bare account) and each was found only where two cells JOIN."
  },
  {
    "id": "IRPT_BCKEND-W2-S12",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T09:01:13Z",
    "one_line": "THE CLOUDFRONT APPLY IS STOPPED BY ITS OWN GATE AND NOTHING WAS APPLIED. The pre-apply plan on the portal-auth root reads 'Plan: 0 to add, 3 to change, 0 to destroy' and names THREE resources, not one. MINE IS CLEAN: aws_cloudfront_distribution.portal shows exactly ONE added ordered_cache_behavior (/api/scoped/investor-reporting/* -> APIGateway-portal, caching disabled, one viewer-request association to auth-validator-edge:19), 1 of 1 block, with no existing behavior touched. THE OTHER TWO ARE NOT THIS PROJECT'S: (1) aws_cloudfront_function.spa_fallback is a CRLF CHECKOUT ARTIFACT -- measured, not inferred: spa-fallback-function.js is 26 CRLF / 0 bare LF on disk in this fresh worktree while the HEAD blob is 0 CRLF / 26 LF, and every diff line shows byte-identical text on both sides; (2) aws_wafv2_web_acl.opal_cloudfront_protection is REAL churn -- 3 managed-rule blocks removed and 3 re-added (common-rule-set p4, ip-reputation p3, known-bad-inputs p5) on the WAF protecting the whole portal. The face's bound is exact -- 'The CloudFront plan shows exactly ONE change or you STOP ... never an apply' -- so safe-apply was never invoked on that root. THE WORLD IS VERIFIED UNCHANGED: get-distribution-config on EVTSA9VEHNZVH after the plan is byte-identical to the one taken before any act (27 ordered behaviors then and now, identical pattern list, investor-reporting present = False, full DistributionConfig JSON identical). The behavior is COMMITTED and UNAPPLIED. The API half of this cell is SEPARATE and IS LIVE: 11 routes applied 23 added / 0 changed / 0 destroyed under the existing naqxlm authorizer.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "terraform plan -no-color -input=false -lock=false on infra/aws/terraform/portal-auth @d0a61c6acb -> 'Plan: 0 to add, 3 to change, 0 to destroy' naming aws_cloudfront_distribution.portal, aws_cloudfront_function.spa_fallback and aws_wafv2_web_acl.opal_cloudfront_protection; saved verbatim",
        "the distribution's own diff in that plan: ONE '+ ordered_cache_behavior' block with path_pattern /api/scoped/investor-reporting/*; grep count of ordered_cache_behavior blocks inside that resource's diff = 1",
        "measured CRLF: infra/aws/terraform/portal-auth/spa-fallback-function.js on disk = 26 CRLF / 0 bare LF; git show HEAD:<same path> = 0 CRLF / 26 LF",
        "the WAF diff: 3 blocks matching '^      - rule {' and 3 matching '^      + rule {' inside aws_wafv2_web_acl.opal_cloudfront_protection, named common-rule-set (p4), ip-reputation (p3), known-bad-inputs (p5)",
        "aws cloudfront get-distribution-config --id EVTSA9VEHNZVH before any act and again after the plan: 27 behaviors both times, identical pattern list, full DistributionConfig json-identical, investor-reporting absent both times",
        "org/critical_paths/change_management/20260911T0855Z_irpt-bckend-s15-cloudfront_deploy_completion.md -- every leg closed on NON-EXECUTION, with a READ-THIS-FIRST block above the status line saying so"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~B",
    "spec_asserts": "BOUNDS: 'The CloudFront plan shows exactly ONE change or you STOP. The distribution serves the whole portal; a plan that touches any other behavior, origin or setting is a BLOCKING row, never an apply.' S15-AC1 arm (c): 'The saved terraform plan output for portal-auth before the apply shows 1 to add, 0 to change, 0 to destroy or an in-place update touching only the new behavior block.'",
    "world_is": "The plan touches two further resources that pre-date this cell and belong to a root this project does not own. One is a line-ending artifact of a fresh worktree; the other is genuine WAF drift. Neither is reachable from this order's <paths>, and applying would rewrite a WAF ACL protecting 28 behaviors in order to land one additive behavior.",
    "notes": "BLOCKING on arms (b), (c) and the cloudfront half of (f) -- S15-AC1 therefore WITHHOLDS its token and this order stays OPEN. Every other arm was still measured and passed: 11 of 11 routes live under naqxlm, the catalogue is the registry 3 of 3, Global is proven on two firms' fixtures 4 of 4, the seam's three outcomes, and the amend census. WHAT UN-BLOCKS IT: the portal-auth root plans clean, or its two drifting resources are dispositioned by that root's owner (lane CLOUD_OPS_OR_ETL, any AE agent). The behavior is committed and unapplied, so the remaining act is a re-plan and an apply under the same entry -- no rework. The CRLF half would clear for any actor whose worktree renders that file LF; the WAF half is a real decision someone must take, and taking it from inside this order would be the widening the bound forbids."
  },
  {
    "id": "IRPT_BCKEND-W2-S13",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T12:30Z",
    "one_line": "THE TWO SIDES DO NOT AGREE ON WHAT AN OPERATION IS: the consumer publishes 11 flat slugs, the producer publishes 12 nested routes; 11 of 11 consumer paths are ROUTE_UNKNOWN under v1, 2 consumer operations have no producer route and 3 producer routes have no consumer operation.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/contracts/investor-reporting/v1/routes.json @7478fdf144 -- 12 route_keys, all of the form /api/scoped/investor-reporting/<noun>/<sub-noun-or-{param}>",
        "portal/src/pages/InvestorReporting/fixtures/smoke/default.json at the PRIMARY checkout (C:/Users/AndrewBerman/Desktop/ajb_workspace/portal) -- 11 keys, all of the form /api/scoped/investor-reporting/<slug>",
        "infra/aws/lambda/investor-reporting/_contracts/tests/test_seam_paired.py @7478fdf144 -- each paired case dispatches the CONSUMER's own flat-slug path through the real dispatcher and asserts ROUTE_UNKNOWN; 9 of 9 routed operations assert it and pass",
        "the two consumer operations with NO producer route: submit-correction, export-preview (OPERATIONS table, route None)",
        "the three producer routes with NO consumer operation: GET .../status, GET .../status/{jobId}, GET .../export/{exportId}/download"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-1, criterion RT1-AC1 (b): 'For each operation the consumer's request (from the counterpart's fixture, checkout printed) runs through the real handler entry point' -- which presupposes that each of the consumer's 11 operations names a route this contract serves.",
    "world_is": "The operation SETS differ in both directions and the path GRAMMARS differ everywhere. The consumer addresses a flat slug per operation; v1 addresses nested nouns with path parameters (the shape the 14 pre-existing scoped routes on 7k3ed8px20 already use). No consumer path routes under v1. THE PRODUCER DEFINES: v1 is published as-is and this row is the notice to the counterpart's round-2 cell, which regenerates against this artifact. Nothing in v1 was renamed to match the consumer.",
    "notes": "Not a defect of either side taken alone -- each is internally consistent and each passed its own suite for two rounds. It is only visible at the seam, which is what this cell was cut to build. The two orphaned consumer operations are the sharper half: submit-correction and export-preview are UI affordances with no backend route in the PRD's route table at all, so they are not a renaming question."
  },
  {
    "id": "IRPT_BCKEND-W2-S14",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T12:30Z",
    "one_line": "FIELD NAMING IS TOTALLY DISJOINT ACROSS THE SEAM: 194 of the producer's 293 published property names are snake_case and 0 are camelCase; 139 of the consumer's 220 fixture keys are camelCase and 0 are snake_case; 55 of the 194 match only after camelizing. Meaning is not negotiated by casing.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "census over docs/contracts/investor-reporting/v1/*.schema.json @7478fdf144 (every `properties` object at every depth, `contract_version` excluded): 293 distinct names, 194 containing '_', 0 matching [a-z][A-Z]",
        "census over portal/src/pages/InvestorReporting/fixtures/smoke/default.json at the primary checkout (every key at every depth): 220 distinct keys, 139 matching [a-z][A-Z], 0 containing '_'",
        "EXACT-NAME overlap: 44 of 293 -- and all 44 are single-word names (access, amount, basis, date, kind, ...) where the two conventions cannot differ",
        "CASING-ONLY match: 55 of 194 snake names equal a consumer key after camelizing -- publicReasonCode/public_reason_code, businessAsOf/business_as_of, scopeFingerprint/scope_fingerprint, directoryRevision/directory_revision, entitlementRevision/entitlement_revision among them"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-1 bound: 'The producer defines, the consumer conforms. No field's meaning, unit or date changes to match the frontend; where the counterpart's fixture disagrees with II.3, the test FAILS for that operation and the disagreement is a row naming the field.'",
    "world_is": "The disagreement is not per-field, it is TOTAL and MECHANICAL: the two sides use different naming conventions and the intersection is exactly the set of names too short to have one. So 'the field' this row names is every multi-word field: 55 of 194 are the same concept under two spellings, and the remaining 139 producer names have no consumer counterpart at all. NO SCHEMA WAS EDITED. v1 publishes the PRD's II.3 spellings unchanged.",
    "notes": "The remedy is the counterpart's, and it is mechanical rather than semantic: a generated client that camelizes at the wire boundary satisfies both sides without either meaning moving. This row exists so that choice is made deliberately and recorded, rather than being absorbed by hand-written types that quietly re-define a field while renaming it. The 139-name gap is the reason it must not be absorbed by hand."
  },
  {
    "id": "IRPT_BCKEND-W2-S15",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T12:30Z",
    "one_line": "REACH LIMIT, NAMED NOT HIDDEN: ops/status.py builds its own boto3 S3 client with no fixture path, so the analysis-report operation reaches AWS the moment the real handler is called in process; the dispatcher and handler are exercised, the RESPONSE cannot be graded without the deployed environment.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/ops/status.py @7478fdf144 -- lambda_handler constructs the directory loader itself; there is no event key that supplies a recorded artifact, unlike directory/handler.py's `directory_fixture`",
        "pytest run @7478fdf144: test_paired_consumer_request_through_the_real_dispatcher[analysis-report] XFAIL, botocore.errorfactory.NoSuchKey raised from inside the real handler -- i.e. the dispatcher ADMITTED the request and the handler RAN",
        "the xfail reason names this row id, so the outcome is enumerated in the suite's own output rather than absorbed as a pass"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-1 RT1-AC1 (b): the paired test runs the request 'through the real handler entry point ... in-process', for each of the 11 operations.",
    "world_is": "In-process reach is not uniform across the six handlers. Five accept a recorded artifact on the event and take a pure in-process path; ops/status.py does not, so 'in-process' and 'no AWS call' cannot both hold for the operations it serves. Recorded as its own outcome. IB-rtb-1's deployed replay is where this operation's response is graded.",
    "notes": "Deliberately NOT worked around. Patching a client into the real handler from the test would make the subject a copy the harness controls, which bound 12 forbids and round-1 rows W1-S10/S24 were filed about."
  },
  {
    "id": "IRPT_BCKEND-W2-S16",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T12:30Z",
    "one_line": "THE PUBLISHED SCHEMAS ARE DOCUMENT CONTRACTS, NOT RESPONSE CONTRACTS: 0 of the 7 operations that reach a response return anything validating against its route's schema in ANY document position; the six handlers emit three different envelopes; and 2 of the 11 schemas can never be an HTTP response at all. RT1-AC1 (b) cannot read 11 of 11 and the remedy is outside this order's <paths>.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "pytest @7478fdf144, test_paired_consumer_request_through_the_real_dispatcher: 7 failed, 4 xfailed, 0 passed -- every failure is the assertion 'validates against <Schema> in NO document position', over three positions tried (whole response, response.result, json(response.body))",
        "THREE ENVELOPES, measured: directory/handler.py returns {ok, op, result, reason}; performance, narrative and export handler.py return the API-Gateway {statusCode, body}; ycharts/generate/job.py returns {ok, live_call, reason, measured_overview_seconds, budget_seconds, note}",
        "TWO SCHEMAS ARE NOT RESPONSES BY CONSTRUCTION: AnalysisRequest is the queue message the intake produces (PRD CONTRACTS row, 8 required-meaning items, none of them a response field) and FirmDestinationPolicy is firm configuration; neither is ever an HTTP response body, so no handler can be wrong about them",
        "every schema is additionalProperties:false, so an envelope around a correct document is itself a validation failure -- the failures above are envelope mismatches, not field disagreements",
        "TO-IB-rt-1 <paths> @7478fdf144 grants docs/contracts/, _contracts/, _authz/, terraform/investor-reporting/api/ and PATH_MANIFEST.json -- it does NOT grant directory/, performance/, narrative/, export/, ops/ or ycharts/, which is where a response contract would have to be implemented"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-1 RT1-AC1 (b), verbatim: 'For each operation the consumer's request ... runs through the real handler entry point and the response validates against the producer schema; print 11 of 11'. The decomposition's s.2 note says the same: 'asserting the response validates against the producer schema'.",
    "world_is": "There is no mapping from a route to a response schema at this vintage, and the eleven published schemas were never response schemas: they are the PRD CONTRACTS table's DOCUMENT contracts (an AnalysisRequest queue message, a FirmDestinationPolicy configuration, a DirectoryEntry artifact). The six handlers return three ad-hoc envelopes that no published schema describes. The paired test therefore measures 0 of 7 rather than 11 of 11, and it measures it with the assertion the criterion names rather than skipping the half it cannot satisfy.",
    "notes": "WHY THIS IS BLOCKING AND NOT AN OBSERVATION: it is the deciding output of RT1-AC1, so the criterion reads FAIL and the order stays open; the worker cannot grade around it and does not. WHY IT IS ARMED: v1 is published and declared immutable at the complete flip, and the counterpart's round-2 cell regenerates against it -- if the response envelope is settled LATER it will settle against an immutable v1 that never described it, which is a v2 on the first serve. THE WORKER JUDGES FORM, NOT SIGNIFICANCE: three shapes the issuer may choose between are stated without preference -- (i) publish a response envelope contract in v1 and require the handlers to emit it (a handler-lane cell, IB-rt-2 is the candidate: it already opens all six handlers to add guard()); (ii) rule that the schemas are document contracts only and re-cut RT1-AC1 (b) to grade the documents the handlers WRITE rather than the responses they RETURN; (iii) defer the response grading to IB-rtb-1's deployed replay. NO WIDENING WAS TAKEN: no handler was edited and no schema was loosened to make an assertion pass."
  },
  {
    "id": "IRPT_BCKEND-W2-S17",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T12:58Z",
    "one_line": "SELF-CORRECTION ON A ROW OF MINE, FILED RATHER THAN EDITED: W2-S16 named `FirmDestinationPolicy` as one of the eleven published schemas. It is not one of them. The eleventh is `RenderPackage` -- and RenderPackage is the ONE schema of the eleven whose PRODUCER IS THE FRONTEND, which inverts this cell's governing bound for exactly one contract.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ls docs/contracts/investor-reporting/v1/*.schema.json @173349a652 -- 11 files: AnalysisReport, AnalysisRequest, DirectoryEntry, ExportBundle, ExportReceipt, HoldingsSnapshot, NarrativePacket, PerformanceReport, RenderPackage, ResolvedScope, StatusEnvelope. FirmDestinationPolicy is NOT among them",
        "the same 11 in infra/aws/lambda/investor-reporting/_contracts/*.schema.json, from which they were published -- so the publication was correct and only the PROSE describing it was wrong",
        "docs/contracts/investor-reporting/v1/RenderPackage.schema.json @173349a652, x-contract: {producer: FNTEND, consumer: BCKEND B14, cell: B14 (consumer)}",
        "a FirmDestinationPolicy CONTRACT does exist in this project -- as firm_destination_policy.json, shipped inside the intake and ycharts zips -- which is why the wrong name was plausible and why it was not caught by reading the sentence",
        "PATH_MANIFEST.json @173349a652 carries a DEAD entry for docs/contracts/investor-reporting/v1/FirmDestinationPolicy.schema.json and, before this row's companion append, carried NO entry for RenderPackage.schema.json"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Row IRPT_BCKEND-W2-S16 (this cell's own, committed at 173349a652) asserts: 'TWO SCHEMAS ARE NOT RESPONSES BY CONSTRUCTION: AnalysisRequest ... and FirmDestinationPolicy is firm configuration'. The same sentence appears in this cell's battery result and proof-of-spec instance.",
    "world_is": "FirmDestinationPolicy is not one of the eleven published schemas. The eleventh is RenderPackage. THE SUBSTANTIVE CLAIM SURVIVES THE SUBSTITUTION -- RenderPackage is the package handed to the export renderer, never an HTTP response body -- so 'two of the eleven can never be a response' remains true with RenderPackage in place of FirmDestinationPolicy, and arm (b)'s 0 of 11 is unaffected. What is NOT merely a naming slip: RenderPackage's x-contract names the PRODUCER as FNTEND and the CONSUMER as BCKEND. For that one contract this cell's governing bound -- THE PRODUCER DEFINES, THE CONSUMER CONFORMS -- points the OTHER WAY, and this cell published it under a directory whose CONTRACT.md says the producer is IRPT_BCKEND. The per-schema x-contract block states the true direction and was published unedited, so the artifact is not wrong; the directory-level prose over-generalises for 1 of 11.",
    "notes": "WHY A NEW ROW AND NOT AN EDIT: the channel is append-only and W2-S16 is already committed. Editing it would leave no trace that the correction happened, which is the failure mode the append-only rule exists for. W2-S16 stands as filed; this row is its correction and any reader of one must read the other. HOW IT HAPPENED, stated so the shape is reusable: the eleven schemas were enumerated CORRECTLY everywhere they were DERIVED (the publisher globbed the directory, the instance's artifact rows glob it, the battery counts 11 of 11) and WRONGLY in the one place they were RECALLED -- a sentence in prose. A derived list and a recalled list disagreed and only the recalled one was wrong. FIXED IN THIS COMMIT: the PATH_MANIFEST gains its RenderPackage entry (the dead FirmDestinationPolicy entry is left, per the manifest's own append-only contract, and this row is its notice); the battery result and the proof-of-spec instance -- neither append-only -- are corrected in place and say so. CARRIED FORWARD: whether the directory-level CONTRACT.md should name RenderPackage's inverted direction is a v2 question, because v1 is immutable from this cell's complete flip -- which has not happened, since RT1-AC1 is a FAIL."
  },
  {
    "id": "IRPT_BCKEND-W2-S18",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T13:40Z",
    "one_line": "THE RE-CUT NAMES TWO DENOMINATORS FOR THE SAME SET: 'one per route in routes.json' is 12 and 'the eleven response schemas ... 11 of 11' is 11. Both hold only if the NO-HANDLER-AT-HEAD route gets none. That is how it was built, and BOTH numbers are printed rather than one being quietly chosen.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the amended face at c8189bb6ae, arm (b): 'one per route in `routes.json` (the denominator printed)' and, in the same clause, 'The eleven response schemas exist, validate as schemas, and each `data` `$ref` resolves to a document schema (`11 of 11`)'",
        "docs/contracts/investor-reporting/v1/routes.json at this commit: 12 routes = 11 DECLARED + 1 NO-HANDLER-AT-HEAD (GET /api/scoped/investor-reporting/holdings/{accountSetId})",
        "docs/contracts/investor-reporting/v1/responses/ at this commit: 11 files, one per DECLARED route; the battery prints 'denominator: 12 route(s) ... = 11 DECLARED + 1 NO-HANDLER-AT-HEAD' and then 'published ... 11 of 11 DECLARED'",
        "test_every_declared_route_has_a_response_contract_whose_refs_resolve asserts BOTH directions: 11 of 11 DECLARED routes have one, and the NO-HANDLER route has NONE"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-1 arm (b) as re-cut: response schemas are published 'one per route in routes.json (the denominator printed)', and separately 'The eleven response schemas exist ... (11 of 11)'.",
    "world_is": "routes.json carries TWELVE routes, so 'one per route' and 'eleven' cannot both be satisfied by the same reading. The reading taken: the 11 DECLARED routes each get a response contract and the 1 NO-HANDLER-AT-HEAD route gets NONE -- because a route with no handler answers nothing, and a response contract for it would describe a response that cannot exist while adding a twelfth file that makes '11 of 11' read as a shortfall. Both denominators are printed side by side by the battery and stated in routes.json and CONTRACT.md, and the absence is asserted by test rather than merely left empty.",
    "notes": "FILED AS FORM, NOT SIGNIFICANCE: the worker had to choose between two readings the face gives equal standing, and a choice made silently is indistinguishable from not noticing. Nothing is blocked -- arm (b) passes on either reading's evidence because both counts are printed. IF THE OTHER READING WAS MEANT, the remedy is one more file (holdings-snapshot.response.schema.json) and a one-line change to the assertion that currently requires its ABSENCE; v1 is not frozen until this order's complete flip, so it is cheap now and a v2 afterwards."
  },
  {
    "id": "IRPT_BCKEND-W2-S19",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T15:11Z",
    "one_line": "ARM (a) CANNOT READ `0 of N` IN THIS LANE: three of the eleven handler-bearing routes dispatch to `irpt-status`, whose source dir `infra/aws/lambda/investor-reporting/ops/` and whose Terraform root `infra/aws/terraform/investor-reporting/ops/` are BOTH absent from this order's <paths>. The wrapper cannot be put on a handler this order may not open.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/contracts/investor-reporting/v1/routes.json @fa89acb5d3: three DECLARED routes carry handler `irpt-status` -- analysis-report (GET /analysis/{jobId}/sections), status-summary (GET /status) and status-job (GET /status/{jobId})",
        "infra/aws/lambda/ci/lambda-source-map.json @fa89acb5d3: irpt-status source_dir = infra/aws/lambda/investor-reporting/ops, tf_file = infra/aws/terraform/investor-reporting/ops/lambda.tf",
        "TO-IB-rt-2 <paths> @fa89acb5d3 lists directory/, performance/, ycharts/generate/, narrative/, export/ and the five matching terraform roots -- ops/ appears on NEITHER side",
        "the census measured in this worktree over the REAL declared entry points: 11 of 11 routes unguarded, of which 8 are in this lane and 3 are irpt-status's"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-2 arm (a): '`unguarded_routes()` over docs/contracts/investor-reporting/v1/routes.json at HEAD reads `0 of N` (N = handler-bearing routes, printed)'. The L5 note names the population as 'every route's integration target ... every targeted function's entry point is wrapped'.",
    "world_is": "N = 11 and 3 of the 11 targets are `irpt-status`, which this order does not grant. The best reachable in-lane result is `0 of 8` with the other 3 named and attributed; the whole-file census reads `3 of 11` unguarded and cannot read zero without a grant this order does not carry. The preflight's own rule is followed: 'a path you need that is not listed is a BLOCKING row, never an override.'",
    "notes": "NO OVERRIDE TAKEN AND NO ops/ FILE READ FOR EDIT. Two shapes the issuer may choose between, stated without preference: (i) extend this order's <paths> with ops/ and terraform/investor-reporting/ops/ so the eleventh route and its two siblings can be guarded here; (ii) leave the three with their own cell and re-cut arm (a)'s denominator to the handler-bearing routes THIS order may open, printed beside the whole-file number. The battery prints BOTH numbers either way, so the evidence does not depend on the choice."
  },
  {
    "id": "IRPT_BCKEND-W2-S20",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T15:11Z",
    "one_line": "THE REAL CENSUS READS 11 OF 11 UNGUARDED, NOT 6 OF 11: every one of the six dispatched functions' DECLARED entry point is unwrapped at HEAD. The face's inherited `6 of 11` counted a table the round-1 battery had partly wrapped itself -- row W1-S10's own lesson, recurring inside the summary that records it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "measured in this worktree at fa89acb5d3: each route's handler resolved from lambda-source-map.json (source_dir + tf_file) and that Terraform file's own `handler = \"<module>.<attr>\"`, the module imported by path, `_authz.enforce.is_guarded(fn)` read on the resulting callable",
        "result: directory-search, resolve-scope, performance-report, analysis-requests, analysis-report, narrative-packet, status-summary, status-job, submit-export, export-receipt, export-download -- guarded=False on all 11",
        "`unguarded_routes()` verdict over that table: 'BLOCKED: 11 of 11 route(s) reach an unguarded handler'",
        "TO-IB-rt-2 'WHAT ROUND 1 DELIVERED' @fa89acb5d3: 'the round-1 replay's measurement 6 of 11 unguarded (three known: IB-s-1 directory x2, IB-s-11 performance; three new: analysis, narrative, export status)'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-2: 'the round-1 replay's measurement 6 of 11 unguarded', with five routes implicitly already guarded.",
    "world_is": "0 of 11 are guarded. The five the summary treats as already-done (analysis-report, status-summary, status-job, submit-export, export-receipt/download) are not: their declared entry points carry no `__irpt_guarded__` mark. The work is LARGER than the face's summary, not smaller, and nothing is being skipped on the strength of the old number.",
    "notes": "WHY THE OLD NUMBER WAS WRONG IN THE SAFE DIRECTION AND STILL DANGEROUS: a census over a route table the measuring battery populated itself reads the battery, not the estate -- exactly row W1-S10. The number then travelled into a task-order face as inherited fact. This row is not a criticism of the cut; it is the reason the census in this cell is built to resolve entry points from lambda-source-map.json plus each function's OWN Terraform `handler =` declaration, so the population cannot be supplied by the thing being measured."
  },
  {
    "id": "IRPT_BCKEND-W2-S21",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T15:11Z",
    "one_line": "TWO SERVED FUNCTIONS CANNOT BE REBUILT FROM COMMITTED SOURCE: irpt-ycharts-generate declares 25 build inputs of which 7 have NEVER existed in this repository, and irpt-status declares 7 of which 5 have not; a third, irpt-directory-search, fails the builder's parity check because two functions share one source dir.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ci/lambda-source-map.json @fa89acb5d3, irpt-ycharts-generate files[]: enforce.py, gate.py, keys.py, resolve.py, firm_destination_policy.json, firm_registry.json, settings.json -- none present in infra/aws/lambda/investor-reporting/ycharts/generate/",
        "`git ls-tree --name-only 88c97c1529 infra/aws/lambda/investor-reporting/ycharts/generate/` (the commit IB-s-9's CLOSED ledger names as the built source) lists job.py, recipe.py, templates.json, transport.py, fixtures, tests -- THE SEVEN WERE NEVER COMMITTED, at that commit or at HEAD; `git check-ignore` does not claim them",
        "org/critical_paths/change_management/20260911T0417Z_irpt-bckend-s9_deploy_completion.md: L1 proof asserts 'the zip rebuilt from the COMMITTED source at 88c97c1529 (25 members, byte-identical rebuild)' -- 25 members, of which 7 are not in that commit",
        "irpt-status files[]: enforce.py, resolve.py, keys.py, handler.py, checkpoint.py absent from infra/aws/lambda/investor-reporting/ops/ (git ls-tree at HEAD lists RUNBOOK.md, manifests.py, status.py, tests)",
        "irpt-directory-search files[] = ['handler.py'] while its source dir also carries refresh.py and expiry.py (irpt-directory-refresh's), so build-and-upload.sh's ADHC_DRIFTD.002 disk->manifest parity check reports them as unregistered EXTRAS and refuses; the check is per-function over a SHARED directory and cannot be satisfied by both functions at once",
        "infra/aws/lambda/ci/build-and-upload.sh :195-207 (manifest->disk) and :218-235 (disk->manifest parity)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-2 L5 note: 'every function whose code changes here is rebuilt, its zip uploaded, its root applied under a ledger entry ... `CodeSha256` verified'. Bound 4: 'served bytes verified as `CodeSha256` against the built zip, never by filename'.",
    "world_is": "For three of the six the BUILD INPUT ITSELF is unsatisfiable at HEAD, so there is no zip to verify CodeSha256 against and no way to reproduce what is currently served. Rule 22a's instruction -- diff deployed bytes against the BUILD INPUT, never by filename -- has nothing to diff against for irpt-ycharts-generate and irpt-status.",
    "notes": "THE HAZARD IS NOT THE MISSING FILES, IT IS THE GREEN THEY PRODUCED: a CLOSED ledger entry records a byte-identical rebuild from a commit that does not carry seven of the twenty-five members, and every downstream reader takes that as reproducibility. The estate HAS the mechanism for this -- `BUILD_MANIFEST.json` + `infra/aws/lambda/ci/vendor-manifest.sh`, which copies `vendored_modules[]` flat into the source dir and has a `--check` parity mode -- and NO IRPT lambda directory carries one (checked: directory, performance, narrative, export, ops, intake, ycharts/generate; 0 of 7). NOT REPAIRED HERE: repairing it for irpt-status needs ops/, which this order does not grant (row W2-S19), and repairing it for ycharts/generate means authoring the vendoring for a function another cell may also be holding. This cell therefore does NOT apply any root: a deploy whose input cannot be reproduced is the half-landed state NEVER-2 exists to prevent."
  },
  {
    "id": "IRPT_BCKEND-W2-S22",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T15:11Z",
    "one_line": "TWO CELLS ARE POINTED AT ONE SERVED FUNCTION: the issuer's own hand-off states IB-rt-4 is CONCURRENTLY re-applying its error-path envelope on irpt-export-render from slot ~3, while this order's <paths> grant export/ and its Terraform root to this cell. Two cells applying one function is the half-landed-deploy hazard, not a merge conflict.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the issuer's hand-off to this worker, 2026-09-11 ~14:3xZ, verbatim: 'IB-rt-4 is concurrently re-applying its error-path envelope on the export function from slot ~3, so do not edit infra/aws/lambda/investor-reporting/export/handler.py in this order unless your face grants it -- guard it at the boundary your paths name'",
        "TO-IB-rt-2 <paths> @fa89acb5d3 DOES grant infra/aws/lambda/investor-reporting/export/ and infra/aws/terraform/investor-reporting/export/ -- the instruction and the grant point opposite ways on the same directory",
        "the tree at this cut already carries IB-rt-8's export controller (export/ now holds dispatch.py, exclusion.py, identity.py, package.py beside handler.py) and IB-rt-4's _authz/errors.py",
        "three of the eleven routes (submit-export, export-receipt, export-download) dispatch to irpt-export-render"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-2 arm (e): 'For each function changed: `get-function-configuration` `CodeSha256` equals the built zip's; each root's plan after the apply reads `No changes`' -- for roots including export.",
    "world_is": "Another cell is applying the same function in the same window. This cell therefore writes its export guard WITHOUT editing export/handler.py -- the entry point is a NEW module in export/, and the Terraform `handler =` string names it -- and does NOT apply the export root. The code is committed and its deploy is the issuer's to sequence after IB-rt-4's window closes.",
    "notes": "THE INSTRUCTION IS FOLLOWED AND THE CONFLICT IS RECORDED RATHER THAN RESOLVED BY THE WORKER: a worker judges a surprise's form, never its significance, and 'which of two cells owns a served function this hour' is not a worker's call. NO APPLY WAS ATTEMPTED ON ANY ROOT (see also row W2-S21, which blocks the build inputs independently)."
  },
  {
    "id": "IRPT_BCKEND-W2-S23",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T15:11Z",
    "one_line": "THE ONE ERROR ENVELOPE CANNOT EXPRESS THE REFUSAL THE AMENDMENT REQUIRES: `_authz/errors.py`'s PUBLIC_REASONS is CLOSED and does not contain `CONTRACT_VERSION`, which arm (g) names as the served public reason for a mismatched `X-Contract-Version`; v1's own StatusEnvelope admits it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/_authz/errors.py @fa89acb5d3: PUBLIC_REASONS is a 15-member closed tuple (NOT_AUTHORIZED, FIRM_BINDING, OBJECT_NOT_COVERED, INVALID_INPUT, KEY_REFUSED, UNSUPPORTED_OPERATION, NOT_FOUND, NOT_READY, CONFLICT, SUPERSEDED, DEPENDENCY_UNAVAILABLE, DEPENDENCY_TIMEOUT, RATE_LIMITED, UNEXPECTED) -- no CONTRACT_VERSION; `error_envelope()` RAISES ReasonNotDeclared on a member it does not hold",
        "docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json @fa89acb5d3: `public_reason_code` is `{type: string, pattern: ^[A-Z0-9_]+$}` -- v1 admits CONTRACT_VERSION and constrains only the SHAPE",
        "TO-IB-rt-2 arm (g): 'a mismatched `X-Contract-Version` refused `CONTRACT_VERSION` on `11 of 11`'",
        "infra/aws/lambda/investor-reporting/_authz/dispatch.py @fa89acb5d3 (IB-rt-1's): REFUSAL_CODES carries CONTRACT_VERSION, so the two closed vocabularies in one package disagree about the same axis"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-2 amendment: 'The refusal envelope of `_authz` and the response envelope are two shapes of one family: `status` carries the `StatusEnvelope` on both', and arm (g) requires the served refusal to read CONTRACT_VERSION.",
    "world_is": "`errors.error_envelope('CONTRACT_VERSION')` raises. This cell does NOT edit errors.py: it is IB-rt-4's module, IB-rt-4 is live in slot ~3 this hour (row W2-S22), and adding a member to a closed enum is a schema change that Rule 24 says arrives with its four-postulate record and a token census -- which is a proposal, not a worker's edit mid-round. The served version refusal is therefore built as a StatusEnvelope directly, valid under v1, using errors.new_correlation_id() so the correlation id still comes from the one minter.",
    "notes": "STATED AS FORM: two closed vocabularies covering one axis now live in one package -- `enforce.REFUSAL_CODES` (7), `errors.PUBLIC_REASONS` (15, minted by a different cell) and `dispatch.REFUSAL_CODES` (5). Whether they should be one enum is a taxonomy question with an owner, not a worker's call; what is recorded here is only that the amendment's required value exists in two of the three and a handler that reaches for the ONE envelope cannot emit it."
  },
  {
    "id": "IRPT_BCKEND-W2-S24",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T16:20Z",
    "one_line": "THE GUARD IS WRITTEN AND HAS NO IN-LANE WAY TO REACH THE FIVE ZIPS: `_authz` is shared source, the estate distributes shared source by the `irpt-common` LAYER, and the layer's source dir, its build script and `lambda-layer-map.json` are all outside this order's <paths> -- while the layer itself was republished as v5 at 13:08Z today by another cell.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the five guarded entry modules import `served`, `loaders`, `enforce`, `errors`, `resolve` and `keys`; only `handler`/`job` live in the function's own source dir",
        "infra/aws/lambda/ci/lambda-layer-map.json @fa89acb5d3: irpt-common source_dir = infra/aws/lambda/layers/irpt-common, build_script = .../build_layer.py, build_manifest = .../BUILD_MANIFEST.json, tf_file = infra/aws/terraform/investor-reporting/performance/layers.tf, used_by = [irpt-performance-adapter, irpt-narrative]",
        "`aws lambda list-layer-versions --layer-name irpt-common` at this cut: Version 5, CreatedDate 2026-09-11T13:08:52Z -- republished DURING this round by a cell that is not this one",
        "TO-IB-rt-2 <paths> @fa89acb5d3 grants the five lambda source dirs, the five terraform roots, _authz/, _scope/, PATH_MANIFEST.json, change_management/, one sentinel and lambda-source-map.json -- NOT infra/aws/lambda/layers/** and NOT lambda-layer-map.json",
        "the per-function alternative is vendoring, and the estate's mechanism for it is BUILD_MANIFEST.json + infra/aws/lambda/ci/vendor-manifest.sh: 0 of 7 IRPT lambda directories carry one (directory, performance, narrative, export, ops, intake, ycharts/generate all checked)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-2 L5 note: 'every function whose code changes here is rebuilt, its zip uploaded, its root applied under a ledger entry'.",
    "world_is": "The code changes are written and committed; there is no carrier THIS ORDER may write that puts them in the five zips. Two of the five (performance, narrative) already take the layer, so for them the layer is not merely one option but the established one -- and it is the one out of lane. No layer file was opened and no layer was rebuilt.",
    "notes": "THREE SHAPES, STATED WITHOUT PREFERENCE, for the issuer: (i) grant this cell infra/aws/lambda/layers/irpt-common/ and lambda-layer-map.json and sequence the layer rebuild against whichever cell published v5; (ii) grant the vendoring instead -- BUILD_MANIFEST.json in each of the five dirs plus the files[] additions, which IS in lane except that it establishes a second distribution mechanism beside the layer for the same modules; (iii) move the deploy to a cell that already owns the layer. Read with row W2-S21 (the build inputs of three functions do not resolve at all) and W2-S22 (export is being applied by another cell this window): the deploy is blocked three independent ways and this cell applied NOTHING."
  },
  {
    "id": "IRPT_BCKEND-W2-S25",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T16:20Z",
    "one_line": "v1's RESPONSE CONTRACTS CANNOT REPRESENT A REFUSAL, and serving them is what revealed it: `firm_id` and `data` are both REQUIRED, `firm_id` is the opaque id that only exists inside a firm's directory artifact, and `data` is typed as the producer document with no null branch.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/contracts/investor-reporting/v1/responses/*.response.schema.json @c22f179bbf: required = [contract_version, operation, firm_id, data] on all eleven",
        "`firm_id` = allOf[$ref ResolvedScope#/properties/verified_request_firm_id, {pattern ^fir_[0-9a-f]{24}$}] -- the ISSUED opaque id",
        "data/firm_registry.json @fa89acb5d3 carries firm_id and bucket for five firms and NO opaque id, so the opaque spelling is knowable only by reading the firm's directory artifact from its bucket",
        "the contract-version check must answer BEFORE any bucket is read (that is the whole point of checking it first), so a version refusal has no legal value for firm_id",
        "`data` is a $ref to the document or a declared slice; none of the eleven admits null"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-2 amendment: 'The refusal envelope of `_authz` and the response envelope are two shapes of one family: `status` carries the `StatusEnvelope` on both.' TO-IB-rt-1 arm (b) as re-cut: 'the RESPONSE is validated against responses/<operation>.response.schema.json'.",
    "world_is": "No refusal can validate against a response contract -- not a version mismatch, not a firm-binding refusal, not an object-not-covered. The amendment's own words already provide for this ('TWO SHAPES of one family'), so the boundary emits the `_authz` refusal shape {ok:false, contract_version, operation, status, firm_id?} for refusals and the response envelope for successes, with a StatusEnvelope on both. What is recorded here is that arm (g)'s '11 of 11 responses validate' can only ever mean SUCCESSFUL responses, and that the refusal shape is not published in v1 at all.",
    "notes": "THE DEFECT IS THIS SLOT'S OWN: IB-rt-1 authored those contracts and made `data` required with a document type and no null branch. v1 froze at c22f179bbf, so it cannot be corrected in place -- publishing a refusal contract is a v2 act. Recorded now rather than at the next cell that trips over it. NOT DONE: no schema was loosened and no refusal was dressed as a response to make a count read better."
  },
  {
    "id": "IRPT_BCKEND-W2-S26",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T16:20Z",
    "one_line": "THE PUBLISHED OPERATION IDS ARE NOT ADMISSIBLE KEY COMPONENTS: v1 names them with hyphens (`narrative-packet`) and `_keys.OPERATION_RE` is `^[a-z][a-z0-9_]{0,63}$`, so every guarded request was refused KEY_REFUSED at the cache-key step -- a refusal about the caller for a defect that was not theirs.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/_keys/keys.py:58 @fa89acb5d3: OPERATION_RE = re.compile(r\"^[a-z][a-z0-9_]{0,63}$\"); :475 applies it to the `operation` component of cache_key",
        "docs/contracts/investor-reporting/v1/routes.json @c22f179bbf: every `operation` is hyphenated -- directory-search, resolve-scope, performance-report, analysis-requests, analysis-report, narrative-packet, status-summary, status-job, submit-export, export-receipt, export-download, holdings-snapshot",
        "measured before the fix: all five guarded entries refused every request, authorized and swapped alike, with public_reason_code KEY_REFUSED",
        "after the fix: 30 of 30 swaps refuse for their own reason and 0 of 5 authorized requests are refused for an authorization reason"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-2 acceptance clause draft: 'client names are never cache keys', and the wrapper keys every served answer through `_keys`.",
    "world_is": "The published id space and the key id space do not intersect for any multi-word operation. The boundary now converts once, in one place (`served.key_operation`), and REFUSES AT CONSTRUCTION if a published id has no admissible key spelling -- so a wiring error fails at import rather than presenting to a caller as KEY_REFUSED. The published id is unchanged and still what the response envelope carries; v1 is frozen.",
    "notes": "WHY IT READ AS A PASS BEFORE IT WAS LOOKED AT: KEY_REFUSED is a LEGITIMATE member of the refusal vocabulary, so every swap 'was refused' and a refused-or-not assertion was satisfied. Only printing the CODE per swap showed that all thirty were refused for the same wrong reason. A negative test that does not assert WHICH refusal cannot tell a working control from a broken subject."
  },
  {
    "id": "IRPT_BCKEND-W2-S27",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T16:20Z",
    "one_line": "A THIRD FIRM ID SPELLING: `performance/tenants.py` routes on `F-49F` / `F-COT` / `F-INF`, which is neither the registry spelling (`49financial`) nor the issued opaque id (`fir_...`), so the performance adapter cannot resolve a route for the firm the boundary binds.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/performance/tenants.py:81,91,101 @fa89acb5d3: the route table keys are F-49F, F-COT, F-INF",
        "handler.check_scope returns `verified_request_firm_id` -- the OPAQUE id -- and handler.run passes it straight to tenants.route_for",
        "measured: an AUTHORIZED performance request raises UnknownTenant with \"no performance route for firm 'fir_c9fc04650e2134d6ea033da2'; known firms: F-49F,F-COT,F-INF\"",
        "data/firm_registry.json @fa89acb5d3 carries the registry spellings 49financial, inflection, cottonwood -- a fourth set of tokens again",
        "row IRPT_BCKEND-W2-S9 already records TWO spellings reconciled only by FirmBinding; this is a third, on the vendor-routing axis"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Bound 13: 'Firm, client, relationship, account, report, export and job ids cross a function boundary as ISSUED opaque ids of a declared type.' TO-IB-rt-2 arm (b): a valid principal is SERVED on each of the handlers.",
    "world_is": "The performance adapter's tenant routing is a third id space. An authorized, correctly scoped request therefore cannot be served by that function at all -- it refuses DEPENDENCY_UNAVAILABLE, which is the honest code for 'this function has no route for that firm' and is not an authorization failure. NOT REPAIRED HERE: reconciling a third id space is a FirmBinding change on the axis row W2-S9 owns, and inventing a mapping in this cell would put a fourth definition of one id space in the estate. The boundary classifies the refusal and stops it reaching a caller as the residual.",
    "notes": "READ WITH W2-S9. The estate now has FOUR firm tokens in play -- registry (`49financial`), issued opaque (`fir_...`), vendor-route (`F-49F`) and the bucket alias (`opal-data-bd`) -- and only the first two have a declared reconciler. Which of them is the id space is not a worker's call."
  },
  {
    "id": "IRPT_BCKEND-W2-S28",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T17:45Z",
    "one_line": "THE RENAME ROUTED TO ME CANNOT BE COMPLETED IN LANE: `_authz/dispatch.py`'s ONLY importer is `_contracts/tests/test_seam_paired.py`, and `infra/aws/lambda/investor-reporting/_contracts/` is not in this order's <paths> -- so renaming it would leave a committed test importing a module that no longer exists.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the issuer's hand-off, 2026-09-11: 'W3-S22/W4-S24 ROUTED TO YOU (rename _authz/dispatch.py, which this slot authored, to _authz/authz_dispatch.py, update importers, print 0 basename collisions across _authz/ and every function dir; export/dispatch.py is not renamed)'",
        "importer census over infra/aws/lambda/investor-reporting at bebcab6315: the ONLY code importer of the _authz module is _contracts/tests/test_seam_paired.py:41 `import dispatch as dp`; export/handler.py:51 and export/tests/test_rt8.py:19 import export/dispatch.py, which the hand-off says is NOT renamed",
        "the amended <paths> block at bebcab6315 lists _authz/, _scope/, directory/, performance/, ycharts/generate/, narrative/, export/, ops/, the six terraform roots, PATH_MANIFEST.json, change_management/, one sentinel, lambda-source-map.json, layers/irpt-common/ and lambda-layer-map.json -- `_contracts/` appears NOWHERE",
        "_contracts/tests/test_seam_paired.py puts _authz FIRST on sys.path, so after the rename `import dispatch` would raise ModuleNotFoundError rather than silently binding export/dispatch.py"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The hand-off routes the rename of `_authz/dispatch.py` to this worker and says to update its importers.",
    "world_is": "The one importer is out of lane. THE RENAME WAS NOT STARTED: a rename whose importer cannot be updated leaves a committed test importing a module that no longer exists, which is the half-landed state the managed wind-down forbids -- and a compatibility shim left behind at the old basename would keep the very collision the rename exists to remove, so the census could not read 0 either way.",
    "notes": "CHEAP TO UNBLOCK: add `infra/aws/lambda/investor-reporting/_contracts/` to this order's <paths> (one line) and the rename is a ten-minute act -- the module has exactly one importer. RECORDED RATHER THAN WORKED AROUND under the managed wind-down relayed at 17:30Z. The basename-collision census this cell CAN print today is unchanged by the decision: `dispatch.py` appears twice across _authz/ and the function dirs (_authz/dispatch.py and export/dispatch.py), and `entry.py` appears six times -- once per function dir, which is correct and is why the shared boundary is named served.py."
  },
  {
    "id": "IRPT_BCKEND-W2-S29",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T17:45Z",
    "one_line": "THE DIRECTORY PARITY CHECK IS STRUCTURALLY UNSATISFIABLE, NOT MERELY UNSATISFIED: two functions share one source directory and the builder's disk-to-manifest check runs PER FUNCTION, so whichever one does not list the other's modules reports them as unregistered EXTRAS.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "after this cell's registration at HEAD: irpt-directory-search files[] = [handler.py, entry.py]; top-level .py in infra/aws/lambda/investor-reporting/directory/ = [entry.py, expiry.py, handler.py, refresh.py]; manifest-not-on-disk 0, disk-not-in-manifest 2",
        "expiry.py and refresh.py are irpt-directory-refresh's declared files[], and that function's source_dir is the SAME directory",
        "infra/aws/lambda/ci/build-and-upload.sh, the ADHC_DRIFTD.002 limb: the parity check iterates `$ABS_SOURCE/*.py` per function with an ignore list of __pycache__|*.pyc|test_*.py|*_test.py -- there is no per-function exclusion",
        "irpt-status, which does NOT share its directory, reached 3 of 3 triple equality in the same registration pass"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The amendment's split of row W2-S21: 'irpt-status's absent build inputs and irpt-directory-search's parity are yours -- remove absent inputs, never invent them, register N of N triple equality.'",
    "world_is": "The absent inputs were removed and irpt-status reached 3 of 3. irpt-directory-search cannot reach N of N while it shares a directory with irpt-directory-refresh: the only ways to make the per-function check pass are to list the refresh runner's modules in the SEARCH zip -- inventing content to satisfy a check -- or to change the check. Neither is a worker's to choose.",
    "notes": "TWO SHAPES, WITHOUT PREFERENCE: (i) split the source dirs, so each function's directory holds only its own modules -- which is what every other IRPT function already has; (ii) give the parity check a per-function ignore list sourced from the OTHER functions that declare the same source_dir, so the check reads the shared dir as the shared thing it is. NOT REPAIRED under the managed wind-down: build-and-upload.sh is outside this order's <paths> and a directory split is a move that must be planned and applied, not half-done."
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
  },
  {
    "id": "IRPT_BCKEND-W3-S3",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T02:21:34Z",
    "one_line": "THE PER-FIRM EXECUTION ROLES THE FirmDestinationPolicy NAMES CANNOT BE ASSUMED BY ANY RUNNING FUNCTION, SO THE POLICY'S `execution_role` FIELD DESCRIBES A PER-FIRM LAMBDA FLEET RATHER THAN SOMETHING AN INGESTION POLLER CAN USE. core/firm_destination_policy.json gives every firm an `execution_role` (irpt-core-firm-49financial, -cottonwood, -inflection, plus irpt-core-quarantine), and core/iam_firm_conditions.tf scopes each one to that firm's prefix -- the correct second arm of the cross-firm control. But every one of those roles trusts ONLY the service principal lambda.amazonaws.com, on the DESIRED plane (core/roles.tf data.aws_iam_policy_document.lambda_trust) AND on the APPLIED plane (iam get-role, read live 2026-09-11: Principal {Service: lambda.amazonaws.com}, no role and no account principal). A role a Lambda may be CREATED WITH is not a role a RUNNING Lambda can sts:AssumeRole, and one function cannot change its execution role per message. THE INGESTION POLLER IS EXACTLY THE CASE THAT BREAKS ON THIS: at the moment it writes it has just discovered the firm, so it would have to become that firm's principal mid-request. IB-s-6 therefore runs under ONE role and narrows on the axis that actually bounds the damage -- the PREFIX FAMILY: PutObject on firms/<each enumerated firm>/intake/* and on quarantine/ and nothing else; no Get, no List, no Delete, and nothing under requests/, generations/ or exports/. That is a defensible shape and it is NOT the shape the policy's own field implies. Surfaced rather than worked around: repairing the trust policy would be an edit to IB-s-5's root, which is outside this order's write grant.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.9.0_WK_IRPT_BCKEND~3 for THIS cell -- DISARMED SAME TURN by not using the per-firm roles at all, by narrowing the poller's grant to the intake prefix family, and by writing the reason into infra/aws/terraform/investor-reporting/intake/iam.tf where the next reader of that grant stands. The FIELD's meaning is not this lane's to settle: whether `execution_role` is aspirational (a later per-firm fleet), or the trust policy should admit the roles that will actually run, belongs to IB-s-5's owner and to 3.0.0_SA_CVO at L9. It is ARMED because the next cell that reads `execution_role` and builds toward assuming it will discover this at apply time, not at design time.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/investor-reporting/core/roles.tf @95a34541f8 -- data.aws_iam_policy_document.lambda_trust has one statement whose principals block is type Service, identifiers [lambda.amazonaws.com]; aws_iam_role.firm_execution (for_each over local.firm_ids) and aws_iam_role.quarantine_execution both use it as assume_role_policy",
        "aws iam get-role --role-name irpt-core-firm-49financial (live, 2026-09-11) -> AssumeRolePolicyDocument.Statement[0] = {Sid AllowLambdaAssume, Effect Allow, Principal {Service lambda.amazonaws.com}, Action sts:AssumeRole} -- the APPLIED plane agrees with the DESIRED one",
        "aws iam get-role --role-name irpt-core-quarantine (live, 2026-09-11) -> Principal {Service: lambda.amazonaws.com}",
        "infra/aws/terraform/investor-reporting/core/firm_destination_policy.json @95a34541f8 -- each firms[] entry carries execution_role irpt-core-firm-<id>, and quarantine.execution_role is irpt-core-quarantine",
        "infra/aws/terraform/investor-reporting/intake/iam.tf @HEAD -- the poller's grant is PutObject on the intake prefix family plus quarantine only, with the reason stated in the file"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD B5 / the FirmDestinationPolicy names an `execution_role` per firm, and the project bound requires per-firm prefixes plus IAM conditions in the shared bucket; the natural reading is that a write to a firm's location happens under that firm's role.",
    "world_is": "Those roles admit only the Lambda SERVICE principal, so no running function can assume one, and an ingestion poller -- which learns the firm at write time -- cannot be one function per firm. IB-s-6 uses a single role narrowed to the intake prefix family across the enumerated firms.",
    "notes": "Worth the issuer's and the CVO's attention beyond this cell: any later cell that reads `execution_role` and builds toward assuming it discovers this at apply time. The cross-firm CONTROL itself is intact -- the gate refuses a cross-firm destination in-process before a key is built, and the per-firm IAM conditions still bound anything that does run under those roles."
  },
  {
    "id": "IRPT_BCKEND-W3-S4",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T02:21:34Z",
    "one_line": "THE CHANGE-MANAGEMENT SENTINEL FOR THIS DEPLOY WAS NEVER COMMITTED IN ITS OPEN STATE, SO THE OPEN WINDOW EXISTS IN THE ENTRY BUT NOT IN GIT. The project bound requires the sentinel org/critical_paths/.open_deploys/<slug>.json COMMITTED, and the ORDER it prescribes is open -> ACT -> close -> commit -> then take the grading reads. Those two are in tension for a deploy that completes inside one turn: committing the sentinel OPEN requires a commit BETWEEN the open and the close, which the order does not ask for and which nothing enforces. On IB-s-8 this seat satisfied both by accident of sequencing (the source commit fell between the open and the apply); on IB-s-6 the source commit landed BEFORE the entry was opened, deploy_ledger.py open staged the sentinel, deploy_ledger.py close removed it, and safe-commit then refused the path outright ('pathspec did not match any files') because an add-then-delete of a file never in HEAD is nothing to commit. WHAT IT COSTS, precisely: had this turn died between the open and the close, deploy_ledger.py check would have found a non-terminal change_management entry with NO sentinel -- its BYPASS class, the 'false-clean gate-bypass' the tool's own help names -- rather than an OPEN one. The deploy itself is complete and every leg is proven on the live plane, so nothing is left armed; what is lost is the crash-window evidence, and it is lost for this entry only.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/critical_paths/change_management/20260911T0149Z_irpt-bckend-s6_deploy_completion.md @61fbbd22ae -- the entry, CLOSED, with all six legs and their proofs; committed in ONE commit, after the close",
        "git log -- org/critical_paths/.open_deploys/irpt-bckend-s6.json -> EMPTY: the sentinel has no commit at any point",
        "safe-commit refusal, verbatim: \"fatal: pathspec 'org/critical_paths/.open_deploys/irpt-bckend-s6.json' did not match any files\" -- an add-then-delete of a path never in HEAD leaves nothing to commit",
        "IB-s-6_S6-AC1_battery_output.txt arm (g) -- 'DISCLOSED: sentinel ever committed = False' printed by the battery itself rather than left for a reader to infer",
        "IRPT_BCKEND.TO-IB-s-6 BOUNDS 4, verbatim: 'a change-management entry opened at the start ... and closed at completion, the sentinel org/critical_paths/.open_deploys/<slug>.json COMMITTED; ORDER on any act that changes the world: open the entry, ACT, close the entry and COMMIT it BEFORE taking the reads that grade the act'",
        ".tools/deploy_ledger.py check --help -- the BYPASS class it sweeps for is 'change_management/*.md with an OPEN/non-terminal ledger and NO sentinel'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "BOUNDS 4: the sentinel is COMMITTED, and the order is open -> act -> close -> commit -> grade.",
    "world_is": "For a deploy that completes inside one turn the two clauses cannot both be satisfied without an extra commit BETWEEN the open and the close, which the bound does not ask for and nothing enforces. On IB-s-6 the sentinel existed only between the open and the close and was never committed; the entry itself is committed, CLOSED, with six proven legs.",
    "notes": "INERT: the deploy is complete, every leg verified on the live plane, and the sentinel is correctly absent now. Recorded because the record should not read better than what happened, and because the tension is structural rather than particular to this cell -- the cheap remedy for any future one-turn deploy is one commit of the OPEN sentinel immediately after deploy_ledger.py open, which is what IB-s-8 did by accident of sequencing rather than by rule."
  },
  {
    "id": "IRPT_BCKEND-W3-S5",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T03:23:21Z",
    "one_line": "THE `routes.json` THE ISSUER AMENDMENT NAMES AS THE FALLBACK FOR THE GUARD CENSUS DOES NOT EXIST ANYWHERE IN THE CORPUS. The amendment's (amend) arm reads: 'Where this cell ships no handler, the same census runs over routes.json at the replay.' This cell ships no handler -- the issuer's own hand-off says so ('a PARSER and a correction state inside the intake package, not a route handler') -- so that fallback is the arm's whole content here. Measured: comp-find --name 'routes.json' over 32,481 files returns ONE hit, and it is this same worker's IB-s-8 fixture infra/aws/ec2/investor-reporting-ycharts/tests/fixtures/har_derived_routes.json, matched on a basename SUBSTRING and entirely unrelated -- a YCharts HAR route table, not an IRPT route registry. A second, content census for 'route_table|unguarded_routes|ROUTES' over the whole investor-reporting lambda tree finds the function's own definition, its own unit test, and performance/tenants.py's per-firm ROUTES dict (a vendor-host map, not a handler table). NO IRPT ROUTE REGISTRY EXISTS IN ANY FORM: the api root that would carry one (IB-s-15) is an unapplied skeleton. WHAT THIS CELL DID INSTEAD, stated so a grader can disagree with it: corrections.ROUTES is exported EMPTY, the census runs over it and reads 0 of 0 -- and because a 0-of-0 census reads identically whether the censor works or not, the battery pairs it with TWO controls on the same censor: an UNGUARDED handler wired to a route reads '1 of 1 unguarded' and the SAME handler wrapped by guard() reads '0 of 1'. The instrument is therefore shown to fire, and the empty table is shown to be an empty table rather than a broken reader.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.9.0_WK_IRPT_BCKEND~3 for THIS cell -- DISARMED SAME TURN by refusing the vacuous reading: the 0-of-0 census is PRINTED AS VACUOUS in the battery output and is paired with two controls that make the censor's behaviour measurable, and the route-reachability of this cell's nine public callables is censused at 0. THE FALLBACK ITSELF is the issuer's: 2.0.0_SA_COO~B wrote the (amend) arm and names the artifact, so whether `routes.json` is a planned artifact of IB-sb-3's replay, a different name, or a mistake is the issuer's to say, with 3.0.0_SA_CVO grading the arm at L9. ARMED because every LATER cell that ships no handler inherits the same unsatisfiable fallback and may quietly report a vacuous pass instead.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-find --name 'routes.json' @5236a7603d -> 'DENOMINATOR: 1 hit(s) across 32481 file(s) scanned in scope [corpus=all]'; the single hit is infra/aws/ec2/investor-reporting-ycharts/tests/fixtures/har_derived_routes.json, a basename-substring match on this worker's own IB-s-8 YCharts fixture",
        "comp-find 'route_table|unguarded_routes|ROUTES' infra/aws/lambda/investor-reporting @5236a7603d -> enforce.py:562 (the function), _authz/tests/test_enforce.py:264-266 (its unit test), performance/tenants.py:113-127 (a per-firm vendor-host map named ROUTES, not a handler table). No handler registry anywhere",
        "infra/aws/terraform/investor-reporting/README.md @5236a7603d -- the `api` root (IB-s-15) that would own routes is listed among the nine and is an unapplied skeleton",
        "IRPT_BCKEND.TO-IB-s-7 (amend) arm, verbatim: 'Where this cell ships no handler, the arm reads over routes.json at the replay.'",
        "IB-s-7_S7-AC1_battery_output.txt arm (amend) -- 'unguarded_routes(corrections.ROUTES) -> 0 of 0 unguarded', printed together with 'CONTROL, an UNGUARDED handler wired to a route: 1 of 1 unguarded' and 'CONTROL, the SAME handler wrapped by guard(): 0 of 1 unguarded'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The issuer amendment's (amend) arm: where a cell ships no handler, the unguarded-route census runs over `routes.json` at the replay.",
    "world_is": "No `routes.json` and no IRPT route registry of any kind exists in the corpus at 5236a7603d; the only basename match is an unrelated YCharts HAR fixture. The census was run over this cell's own (empty) exported route table, printed as vacuous, and paired with two controls on the censor itself.",
    "notes": "The amendment is right about the HAZARD -- a handler reachable without the wrapper is a real defect and the census is the right instrument. What is missing is the OBJECT it censuses for a cell that ships no handler. A cheap repair that needs no new artifact: have such a cell run the two controls this battery runs, so the arm proves the censor rather than proving an empty set."
  },
  {
    "id": "IRPT_BCKEND-W3-S6",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T03:23:21Z",
    "one_line": "THE FACE ASKS FOR A `StatusEnvelope` VALUE THE CONTRACT DOES NOT DEFINE. The L5 note and the S7-AC1 (d) arm both name the correction state as the StatusEnvelope value `needs-correction` (lowercase, hyphenated). The shared contract infra/aws/lambda/investor-reporting/_contracts/StatusEnvelope.schema.json, generated at IB-s-18 from the PRD CONTRACTS table, defines `state` as a CLOSED enum of nine values -- QUEUED, RUNNING, READY, PARTIAL, STALE, UNAVAILABLE, NEEDS_CORRECTION, UNCERTAIN, FAILED -- and `needs-correction` is not among them. A producer that emitted the face's spelling would be rejected by the contract on BOTH sides, since the schema sets additionalProperties false and the enum is closed. This cell writes NEEDS_CORRECTION, the contract's spelling, because the contract is the artifact a consumer validates against and the face is prose about it; the difference is stated in corrections.py at the constant rather than resolved silently. INERT: nothing is broken and nothing is waiting -- the prose and the schema mean the same state. It is filed because the same lowercase spelling appears in the PRD row this cell was cut from, so the NEXT cell to produce a StatusEnvelope will read the same prose and may write the same invalid value, and because resolving a spec-versus-contract difference in one direction without saying so is exactly how the two carriers stop agreeing.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/_contracts/StatusEnvelope.schema.json @5236a7603d -- properties.state.enum = ['QUEUED','RUNNING','READY','PARTIAL','STALE','UNAVAILABLE','NEEDS_CORRECTION','UNCERTAIN','FAILED'], and the object sets additionalProperties false",
        "IRPT_BCKEND.TO-IB-s-7, 'What L5 adds', verbatim: 'the correction state (needs-correction) on the AnalysisRequest revision with the StatusEnvelope value needs-correction'",
        "IRPT_BCKEND.TO-IB-s-7 S7-AC1 arm (d), verbatim: 'Uncertain items enter needs-correction'",
        "infra/aws/lambda/investor-reporting/intake/corrections.py @HEAD -- NEEDS_CORRECTION = 'NEEDS_CORRECTION' with the difference stated at the constant",
        "intake/tests/test_parse.py::test_the_status_envelope_uses_the_contract_spelling asserts the emitted state is the CONTRACT's value"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order and the PRD row name the StatusEnvelope value `needs-correction`.",
    "world_is": "The generated contract's `state` enum is closed and contains NEEDS_CORRECTION; `needs-correction` would be rejected by the schema on both sides. This cell emits the contract's spelling.",
    "notes": "Filed rather than absorbed because the lowercase spelling is in the PRD row too, so the next cell to emit a StatusEnvelope reads the same prose. The two carriers mean the same state; only the literal differs."
  },
  {
    "id": "IRPT_BCKEND-W3-S7",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T04:25:45Z",
    "one_line": "THE REUSE PACKET THE ISSUER SUPPLEMENT TELLS THIS CELL TO READ FIRST DOES NOT EXIST IN THIS WORKTREE. The supplement (channel row IRPT_BCKEND-S14, PRD v0.10 @3624e60def) says 'READ THAT PACKET FIRST' and names docs/research/investor_reporting_ycharts_variants_20260911/ with five files. Measured: the directory is ABSENT from the worktree; this branch was re-cut at 1f795d1f71 and the packet landed at 72acd16e66, which `git merge-base --is-ancestor 72acd16e66 HEAD` reports is NOT an ancestor of HEAD (with a positive control on 1f795d1f71, which IS). The 26 files ARE in the local object store at that commit, so the packet was read BY OBJECT REFERENCE (`git show 72acd16e66:<path>`) -- a read, not a merge, since a worker never merges or rebases. WHAT THIS COSTS AND WHAT IT DOES NOT: the CONTENT was fully available, so nothing in the supplement went unread; what is not available is a CITABLE WORKTREE PATH, so every reference this cell makes to the packet is written as path@72acd16e66 rather than as a path a reader of this branch can open. The battery prints the reachability measurement (present_in_worktree false, files_at_72acd16e66 26, commit_is_ancestor_of_head false, positive_control true) rather than leaving it as an absence a later reader would have to rediscover. ARMED because the SHAPE recurs: an issuer supplement that names a path landing after a worker's cut is unreadable to that worker by the route the supplement assumes, and the next worker may read the absence as 'the packet does not exist' rather than 'my branch predates it'.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.9.0_WK_IRPT_BCKEND~3 for THIS cell -- DISARMED SAME TURN by reading the packet by object reference, citing it as path@72acd16e66 everywhere it is used (code comments, templates.json sources, the proof instance), and printing the reachability measurement in the battery so the absence is a recorded fact rather than a silence. THE ROUTING is the issuer's: 2.0.0_SA_COO~B decides whether a supplement that names a post-cut path should re-cut the worktree, cite by commit, or carry the packet into the face; 3.0.0_SA_CVO grades the arm at L9.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ls docs/research/investor_reporting_ycharts_variants_20260911/ in /c/tmp/wk-irpt-1-3 -> 'No such file or directory'; git ls-tree -d --name-only HEAD -- docs/research/ lists eight directories and not that one",
        "git ls-tree -r --name-only 72acd16e66 -- docs/research/investor_reporting_ycharts_variants_20260911/ -> 26 files including README.md, UI_CONTRACT.md, recipe_contract.py, variant_worker.py and manifest.example.json",
        "git merge-base --is-ancestor 72acd16e66 HEAD -> NO; git merge-base --is-ancestor 3624e60def HEAD -> NO; positive control git merge-base --is-ancestor 1f795d1f71 HEAD -> YES",
        "IB-s-9_S9-AC1_battery_output.txt arm (h) -- 'THE VARIANTS PACKET IS NOT IN THIS BRANCH (row W3-S7)' with present_in_worktree false, files_at_72acd16e66 26, commit_is_ancestor_of_head false, positive_control_known_ancestor true",
        "The issuer supplement, verbatim: 'READ THAT PACKET FIRST, before cloud_transport.py, and treat it as the reuse source in the same way (read-only; extend into ycharts/generate/, never a parallel implementation)'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The issuer supplement names docs/research/investor_reporting_ycharts_variants_20260911/ as a read-only reuse source this cell must read first, as a worktree path.",
    "world_is": "That path is absent from this worktree and its commit is not an ancestor of this branch's HEAD. The packet was read by object reference at 72acd16e66 and is cited that way throughout; no merge or rebase was performed.",
    "notes": "The supplement itself is sound and its content was fully used -- the gap is only in how a post-cut artifact reaches a branch that predates it. Worth the issuer's attention because the same shape will recur on every mid-round supplement, and the cheap remedy is to name the commit alongside the path."
  },
  {
    "id": "IRPT_BCKEND-W3-S8",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T04:25:45Z",
    "one_line": "THE CARRIED DECISION TABLE CANNOT SEE A WAF CHALLENGE WHOSE ONLY SIGNAL IS THE RESPONSE HEADER -- AND THE LIVE RUN MEASURED EXACTLY THAT CASE. docs/research/investor_reporting_ycharts_auth_20260910/recovery_contract.py `decision()` classifies a WAF interstitial with `if reply.status in (202, 403, 405) and 'awswaf' in text.lower()`, i.e. by reading the BODY. The variants live run (docs/.../ycharts_variants_20260911/README.md@72acd16e66) recorded a 202 during calculation polling, after three healthy `calculating` responses, whose ONLY evidence was the `x-amzn-waf-action: challenge` RESPONSE HEADER; its body carried the ordinary calculating payload. Run through the carried table unchanged, that response classifies INVALID_RESPONSE (202 is not the expected 200), which is the wrong remedy twice over: it treats a challenge as a protocol failure, and it discards work that the packet's own operator-orchestrated recovery PRESERVED. This cell's copy adds the header as a field on Reply and classifies it BEFORE the body rules, as its own outcome WAF_REFRESH_REQUIRED rather than BROWSER_CHALLENGE, because the remedy differs: a challenge mid-chain needs a coordinated session refresh by B8/B16 and the work already done is kept. The battery keeps the two WAF branches as SEPARATE fixtures reached by DIFFERENT signals and shows the same 202 WITHOUT the header still classifying INVALID_RESPONSE -- so the new rule is load-bearing rather than decorative. INERT for this cell (fixed in its own copy) and raised because the research module is a NAMED REUSE SOURCE for other cells: anyone who carries `decision()` verbatim inherits the blind spot.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.9.0_WK_IRPT_BCKEND~3 for THIS cell -- DISARMED SAME TURN: this cell's copy adds the x-amzn-waf-action header to Reply, classifies it before the body rules as WAF_REFRESH_REQUIRED, and proves the rule is load-bearing with a control (the same 202 without the header still reads INVALID_RESPONSE). THE RESEARCH MODULE ITSELF is not this cell's to edit and is a NAMED REUSE SOURCE for B8/B16 and the recovery coordinator: whether recovery_contract.py is corrected, superseded by this cell's copy, or left as research is the issuer's call with 3.0.0_SA_CVO at L9 and 1.0.0_SA_CTO at L10. ARMED for any cell that carries decision() verbatim.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/research/investor_reporting_ycharts_auth_20260910/recovery_contract.py @1f795d1f71 -- 'if reply.status in (202, 403, 405) and \"awswaf\" in text.lower(): return \"BROWSER_CHALLENGE\"'; the Reply dataclass has no header field at all (status, mime, body, location, transport_uncertain)",
        "docs/research/investor_reporting_ycharts_variants_20260911/README.md @72acd16e66 -- 'The next run received 202 with x-amzn-waf-action: challenge during calculation polling, after three successful calculating responses. The worker now classifies that response as WAF_REFRESH_REQUIRED.'",
        "infra/aws/lambda/investor-reporting/ycharts/generate/transport.py @88c97c1529 -- Reply.waf_action and the rule placed before the body checks; DECISIONS extended with WAF_REFRESH_REQUIRED",
        "IB-s-9_S9-AC1_battery_output.txt arm (v0.10) -- 'WAF: the same 202 WITH the x-amzn-waf-action header -> WAF_REFRESH_REQUIRED; WITHOUT it -> INVALID_RESPONSE'",
        "The two WAF branches are kept as separate fixtures reached by different signals (decision_branches.json BROWSER_CHALLENGE carries the body interstitial and no header; WAF_REFRESH_REQUIRED carries the header and an ordinary body), so neither rule can pass while the other is dead"
      ]
    },
    "spec_asserts": "PRD v0.5 (SUPP IV.7/IV.8/III.2) binds the decision table, and recovery_contract.py is the named reuse source for it: a WAF action, header or interstitial is challenge handling, never bad holdings or authorization denial.",
    "world_is": "As carried, decision() reads only the BODY for the WAF signal, so the measured case -- a 202 whose only signal is the response header -- classifies INVALID_RESPONSE and neither refreshes the session nor preserves the work.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Found by building the fixture from the variants README rather than from the classifier, which is why it surfaced at all: a fixture derived from the code under test would have carried 'awswaf' in the body and passed."
  },
  {
    "id": "IRPT_BCKEND-W3-S9",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T04:50:58Z",
    "one_line": "THE FIXTURE MANIFEST -- THE ARTIFACT THAT SAYS WHICH FIXTURES ARE MEASURED AND WHICH ARE EXTENDED -- WENT STALE IN MY OWN PACKAGE, AND IT IS A DEPLOYED ZIP MEMBER. infra/aws/lambda/investor-reporting/ycharts/generate/fixtures/har/FIXTURE_MANIFEST.json was written at 5e4a92380b. The issuer-supplement commit 88c97c1529 then changed two fixtures it describes -- decision_branches.json (the tenth branch WAF_REFRESH_REQUIRED added; the BROWSER_CHALLENGE fixture's waf_action removed so the two WAF branches are reached by different signals) and upload_ok.json (the echoed rows step_upload() reconciles) -- and did NOT regenerate the manifest. Measured at report time by recomputing every row from disk rather than reading the manifest: 2 of 13 file rows carried a WRONG sha256 AND a wrong byte count (decision_branches.json ab7c405441..1621B declared vs e55589ccba..2545B actual; upload_ok.json 18263ec209..463B declared vs 5249e5b855..753B actual), and two declared denominators disagreed with the fixtures (decision_branches 9 declared vs 10 counted; templates_with_live_proof 1 vs 3). Its prose also still read 'NO LIVE PROOF EXISTS for templates 14141824 and 14141847', which the supplement contradicts -- all three recipes were proven live by 4.0.0_SA_CRO on Andrew's word. WHY IT MATTERS MORE THAN A DOC NIT: a stale hash in a provenance record is WORSE than no hash, because it reads as MEASURED and a reader checking a fixture's integrity against it would get a false MISMATCH on a good file and would have no way to tell that from a tampered one; and this is the exact artifact the S9-AC3 judgment record points the CVO at to separate what was measured from what was extended. REPAIRED SAME TURN by recomputation and REDEPLOYED, because the manifest is a packaged zip member and leaving it repaired-but-not-served would have broken the served-equals-source equality arm (h) grades. ARMED because the SHAPE is general and has no gate: nothing in this estate ties a manifest of hashes to the files it describes, so any commit that edits a described file and not its describer produces a provenance record that is confidently wrong, and every per-file check still passes.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.9.0_WK_IRPT_BCKEND~3 for THIS artifact -- DISARMED SAME TURN: the manifest was repaired by recomputation from disk (not by hand), the zip rebuilt and redeployed under its own change-management entry irpt-bckend-s9-manifest, the source-map registration moved to the new hash, and battery_ib_s_9.py now RE-DERIVES every manifest row and both fixture denominators from disk on every run with the file list taken from the DIRECTORY BY SUBTRACTION, load-bearing in arm (h) -- so this artifact cannot go stale silently again. THE GENERAL SHAPE is not mine to close: whether a manifest-freshness check belongs in .tools/commit-gate.sh or in ds-precommit, so that ANY commit editing a described file without its describer is refused estate-wide, is 1.0.0_SA_CTO's at L10 with 3.0.0_SA_CVO grading the finding at L9. I did not build that gate: it would be a widening of this order and a gate nobody asked for.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show --stat 88c97c1529 -- the commit changes fixtures/har/decision_branches.json (14 lines) and fixtures/har/upload_ok.json (3 lines) and does NOT contain FIXTURE_MANIFEST.json; git log on the manifest shows its last touch is 5e4a92380b",
        "Recomputation over all 13 described files: 'files checked: 13 of 13 | stale: 2' -- decision_branches.json manifest ab7c40544112cf26/1621B vs disk e55589ccbabd01fb/2545B; upload_ok.json manifest 18263ec209542bf9/463B vs disk 5249e5b85571ea9f/753B",
        "decision_branches.json on disk carries 10 branch keys (ARTIFACT_FETCH_PENDING, BACKOFF_429, BROWSER_CHALLENGE, DENIED, HEALTHY, INVALID_RESPONSE_HTML, RECONCILE_UNCERTAIN, REFRESH_401, REFRESH_EVICTION, WAF_REFRESH_REQUIRED) against _meta.denominators.decision_branches = 9; the battery independently prints 'DECISION TABLE -- 10 of 10 branches classified as declared'",
        "infra/aws/lambda/ci/lambda-source-map.json functions['irpt-ycharts-generate'].files lists 'fixtures/har/FIXTURE_MANIFEST.json' as member 12 of 25 -- the manifest is PACKAGED, so a repair without a redeploy would have broken served == rebuilt in arm (h)",
        "Repair output: 'STALE ROWS REPAIRED: 2 of 13 files'; denominators {decision_branches 9, files 13, templates 3, templates_with_live_proof 1} -> {decision_branches 10, files 13, templates 3, templates_with_live_proof 3}; zip content sha256 gYMxOLN8XndUFeK54aP/A5HsxhOsTSrY62GijStzmH4= -> S9C9ibDNI8D77ZUefrAQSq2OgwO1206wySuzfolxUhI="
      ]
    },
    "spec_asserts": "A value must carry its claim in a field a consumer can reject on, and a printed denominator certifies the sweep it names; FIXTURE_MANIFEST.json declares itself 'DERIVED FROM MEASURED ARTIFACTS -- every shape cites the artifact it came from' and is the carrier the S9-AC3 judgment record points the CVO at for the MEASURED-vs-EXTENDED split.",
    "world_is": "Two of its thirteen per-file sha256/byte rows described the PREVIOUS revision of files the same worker changed one commit later, two of its four declared denominators disagreed with the fixtures on disk, and its prose denied live proof that the issuer supplement records as existing. Every per-file consumer of those rows would have read a confident MEASURED value that was false.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Self-inflicted and self-found, in my own deliverable, at report time -- filed rather than quietly fixed because the finding is not the typo, it is that a MANIFEST OF HASHES HAS NO GATE TYING IT TO WHAT IT DESCRIBES. This is Rule 22's shared-dependency blindness in a new place: I verified each fixture, and each fixture was fine; what was broken was the one artifact they have in common, and no per-fixture check could see it. It surfaced only because I re-derived the manifest instead of reading it -- which is also the only reason the two stale rows were not carried into the proof instance as evidence."
  },
  {
    "id": "IRPT_BCKEND-W3-S10",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T06:59:26Z",
    "one_line": "A REAL VENDOR PDF LOSES THE 'fi' LIGATURE TO A FONT-SUBSET GLYPH, AND THE GLYPH'S CODE IS NOT THE SAME IN TWO DOCUMENTS FROM THE SAME VENDOR RUN. Text extracted from the three retained vendor PDFs carries the literal string '(cid:45)' where 'fi' belongs -- '(cid:45)nancial instrument' -- on EVERY page of all three specimens (23 of 23 in overview, 31 of 31 in comparison, 35 of 35 in multicomp, one occurrence per page, measured). It lands in the footer disclaimer, which is DISCLOSURE TEXT this project serves, not a number. THE PART THAT MATTERS MOST: the overview and comparison PDFs encode that glyph as (cid:45) and the multicomp PDF encodes it as (cid:46) -- the same vendor, the same run, the same day, a different font subset. A cid code is a per-document subset index, so any repair that maps a cid number to a letter is a guess about ONE FILE that will be silently wrong on the next one. This cell therefore substitutes a visible marker '[?]' rather than healing the text, and REFUSES to certify any NUMBER whose text at the recorded coordinates carries a cid (verdict UNDECODED_GLYPH_AT_COORDINATES) -- a glyph that did not decode is not a digit. WHY IT IS RAISED RATHER THAN JUST HANDLED: the census-generated synthetic specimens CANNOT reproduce this, because they are written with a standard base-14 font and no subsetting. So every arm that runs only on synthetic specimens is blind to the entire class, and the S10-AC2 judgment record names it as the first thing a real PDF carries that the synthetic cannot. ARMED for any cell that serves extracted DISCLOSURE TEXT: the disclaimer is exactly the text a compliance reader would quote, and '(cid:45)nancial' reaching a client-facing artifact is a visible defect in the one section whose wording is legally load-bearing.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.9.0_WK_IRPT_BCKEND~3 for THIS cell -- DISARMED SAME TURN: extract.py refuses any numeric token carrying a cid (parse_number -> UNDECODED_GLYPH_IN_TOKEN), certify.py refuses to certify a value whose text at the recorded coordinates carries one (UNDECODED_GLYPH_AT_COORDINATES), and disclosure text substitutes a VISIBLE '[?]' marker rather than a guessed letter. WHAT IS NOT MINE: whether served disclosure text is acceptable with a marker in it, or needs a font-aware extraction path (a ToUnicode CMap read, which pdfplumber exposes but this cell does not build), is a product decision for 1.0.0_SA_CTO at L10 with 3.0.0_SA_CVO grading the finding at L9. IB-s-14 (export bundle) and IB-s-15 serve text and inherit this.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Measured over all three retained vendor PDFs fetched from s3://opal-data-ycharts/research/20260911/variants/... and hash-verified against pdf_validation.json: overview 23 (cid:N) occurrences over 23 pages with 1 distinct code ['(cid:45)']; comparison 31 over 31 pages, 1 distinct code ['(cid:45)']; multicomp 35 over 35 pages, 1 distinct code ['(cid:46)']",
        "The affected line on every page is the footer disclaimer: 'sell, as a solicitation of an offer to buy or sell, ... any security or other (cid:45)nancial instrument' -- the ligature 'fi' in 'financial'",
        "THE DISCRIMINATOR: the same glyph is (cid:45) in two of the three documents and (cid:46) in the third, from one vendor run on one day -- so the code indexes a per-document font subset and is not a stable character mapping",
        "infra/aws/lambda/investor-reporting/ycharts/extract/extract.py -- CID_RE, parse_number returning UNDECODED, _repair_text substituting '[?]' with the reasoning in its docstring; certify.py FAIL_GLYPH graded before the value comparison",
        "The census-generated synthetic specimens produce ZERO cid occurrences (helv base-14, no subsetting), which is why no synthetic-only arm can see this class"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S10-AC1 (a)/(b) grade text extraction certified with units, dates and coordinates, and the PRD's acceptance clause requires extraction certified against the paired PDF; the decomposition's proof plan is a census-generated SYNTHETIC three-variant PDF.",
    "world_is": "Real vendor PDFs subset their fonts and a failed glyph mapping arrives as the literal text '(cid:45)', once per page on 89 of 89 pages across the three specimens, with the code differing between documents of the same run. The synthetic specimens cannot reproduce it, so the class is invisible to every synthetic-only arm.",
    "notes": "Surfaced only because the vendor PDFs became available mid-round (PRD v0.11 / channel row S16) and were read rather than assumed to resemble the synthetic ones. It is the concrete, measured answer to the S10-AC2 judgment question 'what could a real vendor PDF carry that the census-generated synthetic cannot' -- which was asked as a hypothetical and turns out to have a number."
  },
  {
    "id": "IRPT_BCKEND-W3-S11",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T06:59:26Z",
    "one_line": "THE AnalysisReport CONTRACT REQUIRES A DATE ON EVERY TYPED SECTION; THE DOCUMENTS DO NOT STATE ONE FOR EVERY SECTION. infra/aws/lambda/investor-reporting/_contracts/AnalysisReport.schema.json makes `as_of_date` a REQUIRED property of every `sections[]` item and pattern-binds it to ^[0-9]{4}-[0-9]{2}-[0-9]{2}$. Measured against the real specimens: the vendor Comparison states no per-section date for 34 of 81 extracted rows and the Multi for 51 of 108; the field census itself records `n/a` for S27/S29/S30/S31/S32 and 'not stated on page (report date 2026-09-09)' for S18 Fundamentals, whose nineteen fields are all numeric. The face's own words are 'a date where the census says one exists', so the face and the contract disagree about the same rows. THERE ARE EXACTLY TWO WAYS TO CLOSE IT AND ONE OF THEM IS A FABRICATION: write the report-level date into as_of_date, which is indistinguishable to every downstream consumer from a date the section actually stated -- the section item is additionalProperties:false with no field in which a report-level fallback could be DECLARED as one -- or emit fewer rows and count what was held out. This cell takes the second: analysis_report_sections() emits only dated rows and undated_rows() reports the holdout with its reason and the field names, so a smaller array never reads as a smaller document. ARMED because the holdout is invisible to a consumer that reads only `sections`: a downstream reader sees 57 rows for the Comparison and has no way, from the contract alone, to learn that 34 more were extracted and certified and are being withheld for want of a field the contract does not have.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.9.0_WK_IRPT_BCKEND~3 for THIS cell's OUTPUT -- DISARMED SAME TURN by emitting only dated rows and reporting undated_rows() with its count, reason and field names, so nothing is dated that the document does not date and nothing is dropped silently. THE CONTRACT ITSELF is not mine: AnalysisReport.schema.json is in _contracts/ and not in this order's <paths>. Whether the section item gains a `date_claim` field (PAGE_STATED / REPORT_STATED / NOT_STATED, which would let an undated section be carried honestly), or as_of_date becomes optional, or the holdout stands, is 1.0.0_SA_CTO's at L10 on the CONTRACTS table, with 3.0.0_SA_CVO grading at L9. IB-s-14 and IB-sb-3 consume this array and inherit the holdout.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/_contracts/AnalysisReport.schema.json -- sections.items.required = ['section_id','section_type','units','as_of_date','page'] with as_of_date pattern ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ and additionalProperties:false over exactly seven properties",
        "Measured on the retained vendor specimens: overview date claims {PAGE_STATED: 61} (all dated); comparison {PAGE_STATED: 47, NOT_STATED: 34}; multicomp {PAGE_STATED: 45, CENSUS_STATED: 12, NOT_STATED: 51}",
        "docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json -- data_as_of is 'n/a' for S27, S29, S30, S31, S32 and 'not stated on page (report date 2026-09-09)' for S18 Fundamentals, whose 19 fields carry numeric units (pct 8, ratio 4, count 3, usd_billions 1, years 1, score 1, price 1)",
        "The face, verbatim: S10-AC1 (a) 'every number carries units, a date where the census says one exists, and a page + coordinates'",
        "infra/aws/lambda/investor-reporting/ycharts/extract/extract.py -- analysis_report_sections() emits only rows carrying as_of_date; undated_rows() returns total/emitted/held_out with the reason and the field names; the battery prints 'UNDATED HELD OUT: N of M' per specimen"
      ]
    },
    "spec_asserts": "The PRD CONTRACTS row for AnalysisReport requires 'typed sections with units/dates/source coordinates' and the schema makes as_of_date REQUIRED on every section item; the face requires a date only where the census states one.",
    "world_is": "34 of 81 and 51 of 108 rows extracted from the real vendor specimens carry no date the document states about their own section, and six of the census's thirty-three sections state none either. The contract cannot represent an undated typed section and has no field in which a report-level fallback could be declared as a fallback.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "This is the 'a value must carry its claim' rule meeting a schema that has no slot for the claim. The cheap remedy is one optional enum field (date_claim) on the section item, which would let every extracted row be carried with its date's provenance stated instead of forcing a choice between fabricating and withholding -- but proposing is legal and implementing is not, and the contract is another cell's surface."
  },
  {
    "id": "IRPT_BCKEND-W3-S12",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T06:59:26Z",
    "one_line": "`_keys.s3_evidence_key` ACCEPTS A CLIENT DISPLAY NAME AND AN E-MAIL ADDRESS AS A PATH SEGMENT, CONTRADICTING ITS OWN DOCSTRING, AND IT IS THE FUNCTION THAT MINTS DURABLE S3 KEYS. Its docstring states: 'segments are the opaque path segments after the family prefix (ids, dated parts, a file name). Each is validated by shape, so a client name cannot become a path.' Measured under this serial: s3_evidence_key('49financial', 'generations', ['Whitfield Family', 'attempts', '0', 'sections', 'report.json']) RETURNS 'firms/49financial/generations/Whitfield Family/attempts/0/sections/report.json', and an e-mail address is accepted identically. Reading the body confirms why: the per-segment loop checks non-empty-string, absence of '/', not-lock-shaped and not-a-foreign-firm-token, and never calls _check_shaped or _check_param_value. `cache_key` in the SAME MODULE does call _check_param_value and REFUSES both values ('matches no admissible component shape'). So the module contains both the grammar and a writer that skips it, and the writer is the one whose output is durable. WHY THE HAZARD IS ASYMMETRIC: a cache key is ephemeral and internal; an S3 key is permanent and appears in server access logs, CloudTrail data events, S3 Inventory reports and every ListObjects response, so a client name that reaches one cannot be un-logged by deleting the object. This bears directly on the issuer amendment carried in this cell's own face (row W2-S10, channel row S9), which instructs cells to find refusals 'through the public cache_key' -- correct advice that happens to route around the function that does not check. NOT FIXED HERE: _keys is not in this order's <paths> and the issuer has already placed _keys on IB-s-17's round-2 surface. This cell shape-checks its own variable segment before calling s3_evidence_key and its battery MEASURES the gap rather than asserting it, so the guard is shown to be load-bearing.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B to route and IB-s-17's assignee to repair -- `_keys` is NOT in this order's <paths> and the issuer has already placed the module's sanitised-exception item on IB-s-17's round-2 surface, so this belongs in the same place. NOT DISARMED ESTATE-WIDE by anything this cell did. What IS disarmed is this cell's own use: extract.sections_artifact_key() shape-checks its variable segment against a POSITIVE allowlist before calling s3_evidence_key, refuses with KEY_REFUSED naming the PARAMETER and never the value, and battery_ib_s_10.py MEASURES that _keys accepts both a display name and an e-mail (printing the key SHAPE with the value redacted) so the guard is shown to be load-bearing rather than decorative. 3.0.0_SA_CVO grades the finding at L9; 1.0.0_SA_CTO holds the cross-firm/PII surface at L10.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/_keys/keys.py s3_evidence_key docstring, verbatim: 'Each is validated by shape, so a client name cannot become a path.'",
        "Its body: the per-segment loop checks isinstance/non-empty, '/' absence, _LOCK_SUFFIXES/_LOCK_SEGMENTS and _refuse_firm_token -- and calls NEITHER _check_shaped NOR _check_param_value",
        "Measured under OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~3: s3_evidence_key('49financial','generations',['Whitfield Family','attempts','0','sections','report.json']) -> 'firms/49financial/generations/Whitfield Family/attempts/0/sections/report.json'; the same call with 'whitfield@example.com' also returns a key",
        "THE CONTRAST, same module: cache_key('49financial', <64-hex>, 'r1','r1','r1','irpt_sections_read', params={'generation': 'Whitfield Family'}) raises KeyComponentRefused 'matches no admissible component shape (ISO date, 64-hex ...)'; the e-mail address is refused identically",
        "battery_ib_s_10.py arm (amend) prints the probe with the value redacted out of the key shape, and arm (amend) FAILS if the gap ever stops being real -- so the guard cannot quietly become decorative"
      ]
    },
    "spec_asserts": "The issuer amendment carried in this face (row W2-S10, channel row S9) rests on `_keys` refusing a client display name or an e-mail address as a key component, and s3_evidence_key's own docstring asserts it validates every segment by shape for exactly that reason.",
    "world_is": "s3_evidence_key performs no shape validation on segments and returns a key containing a client display name or an e-mail address verbatim. The shape grammar exists in the same module and is applied by cache_key, whose output is ephemeral, but not by the writer whose output is a durable S3 key that appears in access logs, CloudTrail, Inventory and every ListObjects response.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Found because this cell needed exactly one firm-scoped key and probed the grammar before trusting it, rather than calling the function and reading its docstring. Worth noting for the amendment's own wording: 'found through the public cache_key' is correct guidance that routes a reader around the function that does not check, so following the amendment exactly would not have surfaced this."
  },
  {
    "id": "IRPT_BCKEND-W3-S13",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T13:09:09Z",
    "one_line": "THE RULING NAMED ONE LEAKY KEY CONSTRUCTOR; THE CENSUS FOUND TWO, AND THE SECOND IS THE WORSE ONE. CTO ruling 4 closes row W3-S12, which named `_keys.s3_evidence_key` for accepting a client display name as a path segment. Censusing EVERY public constructor against all four negatives -- which is what the face's own bound 'verify all constructors, not one' asks for -- found SIX accepted pairs of twenty-four at round-1 HEAD, not two: s3_evidence_key accepted a display name and a raw upstream key, and `quarantine_key` accepted ALL FOUR, including an e-mail address and a firm token. QUARANTINE IS THE WORSE OF THE TWO TO HAVE LEFT OPEN, and the reason is what quarantine IS: a message is written there precisely when its origin could NOT be verified, so its components are the least trusted input this system handles -- an unverified sender's own text, going into a durable S3 key that appears in access logs, CloudTrail, Inventory and every ListObjects response. quarantine_key also carries NO firm in its path by design, so nothing else in its construction constrains what a segment may be. FIXED IN THIS CELL: both constructors now run the same positive allowlist of segment shapes and the twelve round-1 keys still build byte-identically. THE POINT OF THE ROW IS THE METHOD, NOT THE FIX: had this cell verified the one constructor the ruling named, quarantine_key would have passed untouched and the round would have recorded W3-S12 as closed.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.9.0_WK_IRPT_BCKEND~3 -- DISARMED SAME TURN for both constructors: _check_segment now admits a segment only by declared SHAPE (digits, ISO date, 64-hex fingerprint, namespaced opaque id, enum token, structural word, file name) and then refuses a firm token, and the battery drives all 7 constructors x 4 negatives with a 0-occurrence census over 7 renderings. WHAT IS NOT MINE: whether any quarantine key ALREADY WRITTEN carries a name-shaped segment -- the face's bound is that no key already written is renamed by this cell, so the existing objects are listed for the CVO at L9 and moving them is a served-surface act for 1.0.0_SA_CTO at L10.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Measured at round-1 HEAD (7478fdf144) under this serial, 7 constructors x 4 negatives: s3_evidence_key ACCEPTED 'Whitfield Family' -> firms/49financial/generations/Whitfield Family/attempts/0/x.json and ACCEPTED 'AAMkAGI2THVSAAA='; quarantine_key ACCEPTED all four -> quarantine/Whitfield Family/msg.json, quarantine/advisor@49financial.com/msg.json, quarantine/AAMkAGI2THVSAAA=/msg.json, quarantine/49financial/msg.json",
        "keys.py at round-1 HEAD, quarantine_key body: the only per-segment check is `if not isinstance(seg, str) or not seg or '/' in seg` -- no shape ladder and no firm-token check at all",
        "Its own docstring says quarantine 'carries NO firm in its path ON PURPOSE: a message reaches quarantine precisely when its firm could not be established' -- which is the same sentence that makes the input untrusted",
        "After the fix: 27 of 28 trials REFUSED with 0 occurrences of the refused value across str(), repr(), '%s', '%r', an f-string, exc.args and the public log line; the 28th is TenantBinding's tenant position, where a firm id belongs",
        "battery_ib_rt_4.py arm (a) prints the denominator as '11 public callables - 4 readers = 7 constructors', read off the module by AST rather than from a written list"
      ]
    },
    "spec_asserts": "CTO ruling 4 (ROUND_ANALYSIS.round1.md @0d57ceb2f9): 'Typed, issued identifiers at every key-builder boundary and the name/email controls rejected (W3-S12)', and the face's bound 'Verify all constructors, not one (the CVO's remedy): the census of public builders IS the denominator of arm (a)'.",
    "world_is": "Two public constructors accepted a display name, and one of them -- quarantine_key, the one handling the least trusted input in the system -- accepted an e-mail address, a raw upstream key and a firm token as well. The ruling and the row it closes named only the other one.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The CVO's remedy ('verify all constructors, not one') is what found this, and it is worth noting that the remedy was written before anyone knew there was a second one. A fix scoped to the named function would have been indistinguishable from a complete one in every artifact this round produces."
  },
  {
    "id": "IRPT_BCKEND-W3-S14",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T13:09:09Z",
    "one_line": "THE EXPORT DOWNLOAD ROUTE IS DEAD IN THE DEPLOYED FUNCTION: IT IMPORTS A MODULE THE ZIP DOES NOT CONTAIN. infra/aws/lambda/investor-reporting/export/download.py does `import enforce as _authz` at MODULE level, and `enforce.py` has never been in irpt-export-render's packaged file list -- verified at round-1 HEAD 7478fdf144, where the list is the nine members assets/bundle/download/handler/receipt/render plus three fixtures. export/handler.py imports `download` LAZILY (its header says so and gives the reason), so the function imports fine at cold start and fails only when the download path is first exercised -- which is why nothing has noticed. FOUND BY AN IMPORT-CLOSURE CHECK, not by reading: each built zip is extracted and every packaged module imported with the worktree EXCLUDED from sys.path, which is the /var/task layout. THE REASON THAT CHECK EXISTS AT ALL is the point: CodeSha256 equality proves the bytes AWS serves are the bytes we built and says NOTHING about whether they can be imported, so a function missing one shared module passes CodeSha256, passes the post-apply plan, passes the ledger, and returns an error to every caller.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO at L10 with 2.0.0_SA_COO~B to route, and NOT this cell: adding enforce.py (and its own imports) to irpt-export-render's zip would take a code path from dead to live, which is a served-surface behaviour change CTO ruling 4 did not order, and the export root cannot be applied by this cell in any case (row W3-S17). What this cell contributes is the INSTRUMENT: _authz/error_path_census.py's sibling check lives in .scratch here, but the battery runs it in a clean subprocess every run and prints N of N, so the next cell to touch any of these functions inherits the measurement.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "build_and_verify_zips.py over the six impacted functions: 'irpt-export-render 33531 B 10 members import 6 of 7 OPEN' with 'IMPORT FAILED download ModuleNotFoundError: No module named enforce'; the other five read CLOSED",
        "git show 7478fdf144:infra/aws/lambda/investor-reporting/export/download.py line 31 -- 'import enforce as _authz  # noqa: E402', at module level",
        "git show 7478fdf144:infra/aws/lambda/ci/lambda-source-map.json -- irpt-export-render files = ['assets.py','bundle.py','download.py','handler.py','receipt.py','render.py', 3 fixtures]; 'enforce.py' in that list: False",
        "export/handler.py's own header: '`_authz`, `_keys` AND `download` ARE IMPORTED LAZILY, INSIDE THE FUNCTIONS THAT USE THEM. The deployed zip is closed over THIS directory' -- correct about the zip, and the consequence for download.py was not followed through",
        "git status shows download.py is untouched by this cell, so the state is pre-existing and not introduced here"
      ]
    },
    "spec_asserts": "The PRD's B14/B15 rows and IB-s-14's own deliverable treat the signed-download route as a shipped capability of irpt-export-render, and the estate's CodeSha256 verification treats a served-bytes match as evidence the function is deployed correctly.",
    "world_is": "The deployed irpt-export-render cannot execute its download route: the first call into it raises ModuleNotFoundError for `enforce`, because that module is not in the zip. Every deploy-time check the estate runs -- CodeSha256, the post-apply plan, the ledger -- passes on this function.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The general lesson is worth more than this instance: an import-closure check is cheap, and it is the only rung that can distinguish 'the right bytes are deployed' from 'the deployed bytes work'. It also caught a FALSE GREEN in this cell's own battery, which ran the same check in-process and reported 6 of 6 because a leftover sys.modules entry satisfied the import -- a saved and restored sys.modules is not isolation, only a new interpreter is."
  },
  {
    "id": "IRPT_BCKEND-W3-S15",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T13:09:09Z",
    "one_line": "ARM (c)'s DENOMINATOR IS EXCEPT HANDLERS, AND A PUBLIC REASON CAN BE BUILT WITHOUT ONE. The face's arm (c) says 'census the handler error paths ... str(exc) appears in 0 of them (AST census)', and the census built for it reads `except` blocks -- 49 of them across 25 modules, of which 10 rendered the caught exception. That is where the ruling pointed and it is where the leaks were. It is NOT the same set as 'every path that builds a public reason': directory/handler.py returned `\"ERROR: unsupported op \" + repr(op) + \" (search|resolve)\"` on an ORDINARY RETURN, outside any except block, reflecting caller-controlled input straight back into a public reason. The AST census cannot see it and never could. It surfaced only because a directory test asserting the old prose contract failed against the neighbouring change and the branch was read while fixing it. SO THE ARM IS SOUND AND ITS DENOMINATOR IS NARROWER THAN ITS NAME: '0 of 49 except handlers render the exception' is true and is not the same claim as 'no public reason carries caller data'.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.9.0_WK_IRPT_BCKEND~3 for the ONE instance found -- the branch now returns the code UNSUPPORTED_OPERATION with the supported set as a constant, and the directory test was STRENGTHENED rather than relaxed: it now asserts the caller's own value does not appear in the response at all. THE DENOMINATOR ITSELF is the issuer's and the CVO's: whether arm (c) should be re-cut over 'every expression that reaches a public reason field' -- which is a dataflow question, not an except-handler question, and a much larger instrument -- is 2.0.0_SA_COO~B's to scope and 3.0.0_SA_CVO's to grade at L9. This cell did not widen the arm on its own authority.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "_authz/error_path_census.py census over the six families: modules 25, except handlers 49, handlers binding the exception 18, handlers rendering it 10 before the fix and 0 after",
        "directory/handler.py at 7478fdf144: 'return {\"ok\": False, \"op\": op, \"result\": None, \"reason\": \"ERROR: unsupported op \" + repr(op) + \" (search|resolve)\"}' -- an ordinary return, no except block, `op` taken from the event",
        "The same file's `_bucket_for` raised RuntimeError whose message embedded str(firm_token), also caller-controlled, reaching the response through the except block's str(exc)[:200]",
        "Both are now codes from the closed PUBLIC_REASONS enum; the directory tests assert 'delete' not in out['reason'] and 'stranger' not in json.dumps(out)"
      ]
    },
    "spec_asserts": "Arm (c) of RT4-AC1: 'Census the handler error paths (denominator printed); each returns a public reason from the closed enum and a correlation id; str(exc) appears in 0 of them (AST census).'",
    "world_is": "The census's population is `except` handlers. At least one public reason was built on a normal return path from caller-controlled input, and no AST census of except handlers can include it.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Filed because the number arm (c) prints is going to be read as 'no error path leaks', and it means something narrower. A denominator certifies the sweep and not the set -- the sweep here is except handlers, and the set the reader cares about is public reasons."
  },
  {
    "id": "IRPT_BCKEND-W3-S16",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T13:09:09Z",
    "one_line": "THE RULING SAYS TWELVE %r MESSAGE SITES; THE MODULE CARRIED EIGHTEEN PLACEHOLDERS ACROSS SIXTEEN CONSTRUCTION SITES. CTO ruling 4 and the L5 note both say 'twelve %r message sites become zero'. Measured by AST over _keys/keys.py at round-1 HEAD: 24 `KeyComponentRefused` construction sites, 16 of which interpolate at least one %r, carrying 18 placeholders in total (one site carries two: 'parameter %r value %r'), plus 8 more %r elsewhere in the module. The twelve was presumably true when row W2-S10 was written and _keys has grown since. NOTHING IS WRONG WITH THE FIX -- all 18 are now zero -- but the NUMBER in the ruling is a measurement with a vintage and no vintage attached, and a later reader checking 'did twelve become zero' against a file that had eighteen has no way to tell whether six were missed or six never existed. This cell defines the fix by the CENSUS and prints both numbers beside each other.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "3.0.0_SA_CVO at L9 -- the discrepancy is between a ruling's stated count and the file's measured one, and grading which is authoritative is the CVO's. INERT rather than ARMED because the remedy this cell applied (drive the fix from the census, print the denominator) satisfies both readings: 18 of 18 placeholders inside refusal constructions are gone, which is a superset of any twelve. Nothing downstream depends on the number itself.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "AST census over git show 7478fdf144:infra/aws/lambda/investor-reporting/_keys/keys.py -- 24 KeyComponentRefused call sites, 16 containing %r, 18 %r placeholders inside them, 26 %r in the module overall",
        "The sites: L184, L206, L217, L222, L225 (x2), L242, L253, L273, L289 (x2), L320, L358, L369, L371, L374, L398, L419",
        "CTO ruling 4 / decomposition v0.2 s.2, verbatim: 'twelve %r message sites become zero'",
        "battery_ib_rt_4.py arm (a) now prints '%r PLACEHOLDERS INSIDE A REFUSAL CONSTRUCTION: 0' beside the note that the module carried eighteen, so both numbers are in the record",
        "The 6 %r that remain in the module are inside verify_against_layout, comparing the module's own constants to core/layout.json -- config against config, no caller data"
      ]
    },
    "spec_asserts": "The CTO's round-1 analysis, ruling 4, and the L5 decomposition note both state that twelve %r message sites in _keys become zero.",
    "world_is": "The module carried eighteen %r placeholders across sixteen refusal-construction sites when this cell measured it, not twelve.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "This is the same shape as a stale manifest (row W3-S9): a count recorded at one moment and read later as though it were current. The cheap habit that prevents it is attaching the vintage to the number -- 'twelve at <commit>' -- which costs nothing at writing time and removes the ambiguity entirely."
  },
  {
    "id": "IRPT_BCKEND-W3-S17",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T13:09:09Z",
    "one_line": "THE EXPORT TERRAFORM ROOT CANNOT BE APPLIED WITHOUT DESTROYING THREE LIVE RESOURCES THIS RULING DID NOT ORDER, SO irpt-export-render's CODE CHANGE IS COMMITTED AND ITS APPLY IS WITHHELD. Before any change of this cell's, `terraform plan` on infra/aws/terraform/investor-reporting/export reads '0 to add, 1 to change, 3 to destroy'. The three are aws_iam_role_policy.export_render_dispatch, aws_iam_role_policy.export_render_evidence and aws_ssm_document.export_render_run -- each 'is not in configuration' and each present in state, left that way when IB-s-14 removed them from the .tf at 1beda4bf49 without applying. TWO OF THEM ARE IAM ROLE POLICIES ON A LIVE FUNCTION. The face's own condition for this cell's deploy is that 'plans show only the code changes'; this plan does not, and applying it would be a served-surface act (bound 7) with a blast radius nobody signed. The other four roots applied cleanly -- 0 added, N changed, 0 destroyed, with s3_object_version and source_code_hash the only differing attributes -- and five of the six impacted functions are deployed and CodeSha256-verified. ARM (e) OF RT4-AC1 THEREFORE FAILS AND THIS ORDER STAYS OPEN, which is the honest outcome rather than a green bought by an unordered destroy. A SECOND WRITER IS ALSO ON THAT ROOT: irpt-export-render's served CodeSha256 moved from 11ZotLOJLP5xWjGU to iq1u0SatjV0+OtFJ at 2026-09-11 12:57:39Z, during this cell's run and by no act of this cell's.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B to route and 1.0.0_SA_CTO at L10 to decide, with 3.0.0_SA_CVO grading at L9. THREE DISTINCT DECISIONS ARE NEEDED AND NONE IS THIS CELL'S: (1) whether the three orphans should be destroyed -- IB-s-14 evidently intended least privilege, and its iam.tf says 'ONE ROLE PER ROOT ... CloudWatch Logs and NOTHING ELSE' -- or re-declared in configuration; (2) who owns finishing IB-s-14's half-landed change, which is a NEVER-2 item in its own right; (3) the concurrent writer on that root, since two agents applying one root is the collision the round-2 issuance is supposed to prevent. Until then irpt-export-render serves round-1 bytes for the error-path fix while the other five functions serve the new ones, and that split is itself worth the issuer's attention.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "terraform plan -chdir=infra/aws/terraform/investor-reporting/export -> 'Plan: 0 to add, 1 to change, 3 to destroy' with '# aws_iam_role_policy.export_render_dispatch will be destroyed (because ... is not in configuration)' and the same for export_render_evidence and aws_ssm_document.export_render_run",
        "terraform state list on that root shows all three present; the root's configuration is three files (iam.tf, lambda.tf, main.tf) and iam.tf declares one role with logs only",
        "git log on infra/aws/terraform/investor-reporting/export/ -- last change 1beda4bf49 'IB-s-14: the export package, the completed export root, and the ledger opened'",
        "git status shows this cell touched no .tf at all, so the drift is pre-existing",
        "The other four roots: directory 'Apply complete! Resources: 0 added, 2 changed, 0 destroyed', intake/ycharts/ops 0 added 1 changed 0 destroyed, and all four post-apply plans read 'No changes. Your infrastructure matches the configuration.'",
        "irpt-export-render CodeSha256 read 11ZotLOJLP5xWjGUW+WQD9IKSQnEhoOTuJzR3HEGXww= at ~12:40Z and iq1u0SatjV0+OtFJUPqkV7hwJMmpl0wfyFVbhqViWxU= (LastModified 2026-09-11T12:57:39Z) at ~13:0xZ, with no apply of the export root by this cell"
      ]
    },
    "spec_asserts": "RT4-AC1 arm (e): 'CodeSha256 equality per changed function; each root's post-apply plan No changes; ledgers CLOSED, sentinels committed', and the L5 note: 'functions whose code changes are rebuilt and applied under ledger entries per root; CodeSha256 verified; plans show only the code changes.'",
    "world_is": "One of the five roots holds three resources in state and not in configuration, so its plan carries three destroys before this cell changes anything, and applying it would remove two IAM role policies and an SSM document from a live function. The apply is withheld and arm (e) fails.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Recorded as BLOCKING rather than OBSERVATION because it stops a criterion of this order rather than merely informing a later one. The deploy that COULD be done was done and verified; what is left is a decision about someone else's half-landed change, and taking that decision unilaterally is exactly the widening the bounds forbid."
  },
  {
    "id": "IRPT_BCKEND-W3-S18",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T13:09:09Z",
    "one_line": "THE SOURCE MAP'S REGISTERED HASH FOR irpt-export-render AGREES WITH NEITHER S3 NOR THE LIVE FUNCTION, AND NOTHING IN THE ESTATE CATCHES THAT. lambda-source-map.json records artifact_sha256 = HSuSKsWzsnqS4tIO... for irpt-export-render. The S3 artifact's Metadata.content-sha256 and the function's live CodeSha256 were BOTH 11ZotLOJLP5xWjGU... when measured -- consistent with each other and different from the registration. So the registry that the estate's own CodeSha256 checks compare against is the one that is wrong. THE FAILURE MODE IS THE DANGEROUS DIRECTION: a later reader running the standard check sees MISMATCH on a correctly-deployed function and the obvious remedy -- redeploy from the source map -- would push whatever that stale hash describes over a function that was fine. This cell deliberately did NOT register a new hash for irpt-export-render, because it is not deploying it (row W3-S17) and registering bytes that will not be served is how this drift is created in the first place.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B to route with 1.0.0_SA_CTO at L10 -- correcting a registration for a function this cell is not deploying would be writing a number I cannot verify by serving it. The general remedy is a cheap estate-wide check nobody currently runs: for every function in lambda-source-map.json, compare artifact_sha256 against the S3 object's Metadata.content-sha256 and the live CodeSha256, and print N of N. This cell did that for its own six functions as part of arm (e) and it is the reason the discrepancy was visible at all; making it a standing gate is not this order's to build.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda-source-map.json at 7478fdf144, irpt-export-render.artifact_sha256 = HSuSKsWzsnqS4tIO... (unchanged by this cell)",
        "aws s3api head-object --bucket opal-313476888478-lambda-artifacts --key investor-reporting/irpt-export-render.zip -> Metadata.content-sha256 = 11ZotLOJLP5xWjGUW+WQD9IKSQnEhoOTuJzR3HEGXww=, ContentLength 35220",
        "aws lambda get-function-configuration --function-name irpt-export-render -> CodeSha256 = 11ZotLOJLP5xWjGUW+WQD9IKSQnEhoOTuJzR3HEGXww= at the same reading -- S3 and Lambda agree with each other and not with the registration",
        "The other five impacted functions all read served == registered both before and after this cell's deploy, so the drift is specific to this function and not an artifact of how this cell builds zips",
        "battery_ib_rt_4.py arm (e) prints served and registered side by side per function, which is the comparison that surfaced it"
      ]
    },
    "spec_asserts": "The estate verifies a deploy by comparing the served CodeSha256 against the built zip and against lambda-source-map.json's artifact_sha256, treating the source map as the record of what should be serving.",
    "world_is": "For irpt-export-render the source map's registered hash matches neither the S3 artifact nor the live function, while those two match each other. The record disagrees with the world, and the check that would notice is run per-cell by whoever happens to touch the function rather than standing anywhere.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Worth pairing with row W3-S14: that function's zip is ALSO missing a module its code imports. Two independent defects on one function, both invisible to every deploy-time check the estate runs, both found by comparing two instruments rather than trusting one."
  },
  {
    "id": "IRPT_BCKEND-W3-S19",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T16:23:46Z",
    "one_line": "A TWO-PART CHANGE WAS SPLIT BY THE DRAIN: THE CODE HALF MERGED AND THE PACKAGING HALF DID NOT, SO THE SOURCE MAP AT THE TIP DECLARED BUILDS FOR TWO FUNCTIONS THAT CANNOT IMPORT. In round 2 `_authz/enforce.py` gained a module-level `import errors`. That edit merged. The matching edit to `lambda-source-map.json` -- adding `errors.py` to the packaged file list of every function that carries enforce.py -- did not. Measured at the merged tip: NO function's file list contained errors.py, while irpt-status and irpt-ycharts-generate both package enforce.py. Rebuilding either from the merged tree and deploying it would have produced a function that raises ModuleNotFoundError at IMPORT -- and that failure passes CodeSha256, passes the post-apply plan and passes the ledger, because every one of those rungs measures BYTES and none measures IMPORTABILITY. The live functions were healthy throughout: they were still serving this order's first-pass bytes, which did carry errors.py. THE SAME SPLIT ALSO LEFT THE REGISTRATION DISAGREEING WITH THE WORLD ON FIVE OF SIX FUNCTIONS -- artifact_sha256 held the PRE-deploy hashes while S3 and Lambda held the POST-deploy ones, so the triple equality read 0 of 6 at the tip. Rebuilding from the merged tree reproduced the LIVE bytes exactly for five of the six, which is what shows the divergence was purely in the RECORD and not in the world.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.9.0_WK_IRPT_BCKEND~3 -- DISARMED SAME TURN for the six functions this order touches: errors.py restored to the four file lists that need it, all six rebuilt, import closure verified in the REAL /var/task + /opt/python layout BEFORE any hash was registered, and the triple equality now reads 6 of 6. WHAT IS NOT DISARMED is the GENERAL SHAPE, and it is not this cell's to close: nothing in the drain or in any gate ties a module's import graph to the file lists that package it, so any future change that adds an import to a shared library can merge without its packaging half and leave a function that deploys green and dies on the first call. Whether an import-closure check belongs in the merge guards or in commit-gate is 1.0.0_SA_CTO's at L10 with 2.0.0_SA_COO~B to route; 3.0.0_SA_CVO grades the finding at L9.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "At the merged tip 77b2acc7a9, lambda-source-map.json: 'errors.py' in the files list of irpt-directory-search, irpt-directory-refresh, irpt-export-render, irpt-intake-poller, irpt-status, irpt-ycharts-generate -> False for all six, while 'enforce.py' in the list -> True for irpt-status and irpt-ycharts-generate",
        "_authz/enforce.py at the tip imports errors at module level ('import errors as _errors  # noqa: E402  the ONE error envelope (IB-rt-4)'), and its non-stdlib import closure is ['errors', 'keys', 'resolve']",
        "Import-closure check over the six zips built from the tip BEFORE the repair: 4 of 6 CLOSED, with 'IMPORT FAILED enforce ModuleNotFoundError: No module named errors' on irpt-status and irpt-ycharts-generate",
        "Triple equality at the tip BEFORE the repair: 0 of 6 -- e.g. irpt-status registered 3vwEj6cjRRdgh6ew.. while S3 and the live function both held puH1OBabqlGAI1Kc..",
        "After the repair: import closure 6 of 6 CLOSED and triple equality 6 of 6, with five of the six rebuilt hashes reproducing the LIVE bytes exactly (no upload and no apply were needed for those five)"
      ]
    },
    "spec_asserts": "A deploy is verified by CodeSha256 against the built zip and the source-map registration, and the source map is the record of what each function packages.",
    "world_is": "The record described a build that cannot import for two functions, and described the wrong bytes for five. Every deploy-time rung the estate runs would have passed on both.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The import-closure check is what found this, and it is cheap: extract the zip, import every packaged module with the worktree excluded from sys.path. It is the only rung that distinguishes 'the right bytes are deployed' from 'the deployed bytes work'. This is its second distinct catch in two orders -- row W3-S14 was the first."
  },
  {
    "id": "IRPT_BCKEND-W3-S20",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T16:23:46Z",
    "one_line": "A SIBLING CELL IS WRITING TO THE SHARED EXPORT TERRAFORM STATE WHILE THIS ORDER IS NON-TERMINAL, AND CONVERGING THE ROOT FROM HERE WOULD DESTROY ONE LIVE RESOURCE AND REVERT TWO. This order's own apply was clean and is evidenced in the ledger: pre-apply '0 to add, 1 to change, 0 to destroy' with source_code_hash the only differing attribute, post-apply 'No changes. Your infrastructure matches the configuration.' Within roughly thirty minutes the same root planned '0 to add, 2 to change, 1 to destroy', on three resources and for three different reasons: (i) aws_iam_role_policy.render_host_export_evidence -- an inline policy irpt-ycharts-runner-role:irpt-export-render-host-evidence granting s3:GetObject and s3:PutObject, present in the shared STATE and in NO .tf of this branch, so an apply DESTROYS a live grant on the ycharts runner role; (ii) aws_ssm_document.export_render_run -- declared in this branch, but the LIVE document is version 3 and this branch's content is older, so an apply DELETES 21 command lines including the whole host preflight, the renderer-module discovery and the RENDERER_MODULE_ABSENT refusal branch; (iii) module.irpt_export_render.aws_lambda_function.this -- IRPT_PORTAL_ORIGIN is https://portal.opalcapital.co live and https://opalinvest.dev in this branch, so an apply REVERTS the portal origin. THE DISCRIMINATOR IS ONE VERIFIABLE FACT: this order changed NO Terraform configuration at all -- `git status --porcelain -- infra/aws/terraform/` is empty -- so no diff in that plan can originate from this order's edits. This is the SECOND time this root has blocked this order and the first time it has done so with a live sibling rather than a stale premise.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B to sequence and 1.0.0_SA_CTO at L10 to decide, NOT this cell. Applying any of the three is a served-surface act on another cell's in-flight work and bound 7 forbids it; re-declaring them in this branch would be authoring another cell's configuration. What this cell did instead is measurable and complete: its own code change is deployed and verified three ways (triple equality 6 of 6, and a runtime invoke returning statusCode 200 with 5 of 5 contracts), its own convergence was measured AT THE TIME OF THE ACT and is in the ledger, and the battery now prints every residual with its address and its reason rather than reporting a bare non-clean plan. 3.0.0_SA_CVO grades at L9 whether an order may close with a shared root left non-converged by a sibling.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Ledger 20260911T1535Z_irpt-bckend-rt4_deploy_completion.md L2: pre-apply 'Plan: 0 to add, 1 to change, 0 to destroy' with module.irpt_export_render.aws_lambda_function.this the only resource and source_code_hash the only differing attribute; then 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed'; L4: post-apply plan 'No changes.'",
        "terraform state show aws_iam_role_policy.render_host_export_evidence -> id irpt-ycharts-runner-role:irpt-export-render-host-evidence, Action [s3:GetObject, s3:PutObject]; comp-find over infra/aws/terraform/ -> 'NO HITS. This is a MEASURED zero over 589 scanned file(s)'",
        "The SSM diff removes 21 runCommand lines including 'BLOCKED: RENDERER_MODULE_ABSENT -- ... Installing one is npm egress off Opal infrastructure (refused at IB-s-8)'; default_version 3 -> (known after apply)",
        "The Lambda diff: IRPT_PORTAL_ORIGIN 'https://opalinvest.dev' -> 'https://portal.opalcapital.co', with LastModified 2026-09-11T16:10:41Z and CodeSha256 still W6fWlpva77QiSAn5.. (this order's bytes, untouched)",
        "git status --porcelain -- infra/aws/terraform/ is EMPTY for this order, so no plan diff on any declared resource can originate from its edits"
      ]
    },
    "spec_asserts": "RT4-AC1 arm (e) step (1): 'terraform plan on the export root reads ONLY this order's code change (0 to destroy; print the plan summary line) -- if it reads anything else, STOP and file a row', and step (4): post-apply plan 'No changes'.",
    "world_is": "Both readings were satisfied when performed and are in the ledger. A sibling cell then mutated the shared state, so a plan taken at grading time is no longer clean, and every residual belongs to that sibling -- one resource absent from this branch entirely, two whose live content is newer than this branch's.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The amendment sequenced IB-rt-8 behind this order specifically to prevent this, and it still happened, which suggests the sequencing is per-ORDER while the contention is per-ROOT. Worth the issuer's attention more than the individual resources are: two cells holding disjoint <paths> can still share one Terraform state, and nothing in the grant mechanism says so."
  },
  {
    "id": "IRPT_BCKEND-W3-S21",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T16:23:46Z",
    "one_line": "THE irpt-common LAYER'S OWN BUILD_MANIFEST DISAGREES WITH THE LAYER THAT IS PUBLISHED, SO THE RECORD OF WHAT THE SHARED RUNTIME CARRIES IS WRONG. infra/aws/lambda/layers/irpt-common/BUILD_MANIFEST.json records zip_sha256_base64 TjZRSAPsIAUdOB3pjGIU9dIBtnnEwW1jotd+8hXDfnE= and zip_bytes 637134 with member_count 159. The published object and the live layer version BOTH hold ZUcsQUOsc3lT2cKlnur5rCAZc/a0rCkKvU5pjg11U20= at 644526 bytes and 161 members -- S3 and Lambda agree with each other and not with the manifest, which is the same shape as row W3-S18 one level up, on a surface THREE functions share. THE CONTENT ITSELF IS CORRECT, and that is why nothing has noticed: the published layer really does carry all five contracts, keys.py, firm_registry.json and bd_helpers.py, and the runtime capabilities read returns 5 of 5. So the defect is purely in the record -- and the record is what a later cell would rebuild from. THE MEASUREMENT THAT MATTERED HERE was reading the PUBLISHED ZIP rather than either the manifest or the repo's build lists: it is what showed enforce.py, errors.py and resolve.py are ABSENT from the layer, which is why this order packages them in the export zip instead of relying on it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B to route; the layer, its BUILD_MANIFEST and the performance root that publishes it are NOT in this order's <paths>, so correcting the manifest or republishing is out of grant and a path this order needs that it lacks is a row, never an override. NOT DISARMED, and deliberately not worked around: this cell did NOT republish the layer, because the published content already carries the union at the merged tip and a republish would mint a new version with identical bytes -- churn on a surface three functions share, to fix a record this cell may not write. The cheap general remedy is the same one row W3-S18 asks for, one level up: compare BUILD_MANIFEST's digest against the S3 object's content-sha256 and the live layer version, and print N of N.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "BUILD_MANIFEST.json at 77b2acc7a9: zip_sha256_base64 = TjZRSAPsIAUdOB3pjGIU9dIBtnnEwW1jotd+8hXDfnE=, zip_bytes = 637134, member_count = 159",
        "aws s3api head-object --bucket opal-313476888478-lambda-layers --key irpt-common.zip -> Metadata.content-sha256 = ZUcsQUOsc3lT2cKlnur5rCAZc/a0rCkKvU5pjg11U20=, ContentLength 644526",
        "aws lambda get-layer-version --layer-name irpt-common --version-number 5 -> Content.CodeSha256 = ZUcsQUOsc3lT2cKlnur5rCAZc/a0rCkKvU5pjg11U20=, CodeSize 644526 -- S3 and Lambda agree, the manifest does not",
        "The PUBLISHED zip, read member by member: 161 members; all five contracts under python/irpt_contracts/; python/keys.py, python/firm_registry.json and python/bd_helpers.py present; enforce.py, errors.py and resolve.py ABSENT",
        "Runtime confirmation on the deployed consumer: lambda invoke irpt-export-render action=capabilities -> statusCode 200, FunctionError null, CONTRACTS AVAILABLE 5 of 5",
        "3 of 3 live consumers (irpt-export-render, irpt-narrative, irpt-performance-adapter) are attached to irpt-common:5; only 2 of the 3 declare the layer in lambda-source-map.json, a second DESIRED-vs-APPLIED gap on the same surface"
      ]
    },
    "spec_asserts": "The amendment's arm (e) step (3) requires irpt-common to be rebuilt from the merged tree as the union of every cell's CONTRACTS/MODULES/DATA lists, published as a new version, with 3 of 3 functions repointed and the capabilities read printing 5 of 5; BUILD_MANIFEST.json is the record of what was built and published.",
    "world_is": "The published layer already carries that union -- 5 of 5 contracts, keys.py and firm_registry.json -- so a rebuild is a 0-diff on content, while the manifest that records it names a different digest, a different byte count and a different member count from what S3 and Lambda both hold.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Pairs with W3-S18 and W3-S19: three records in one round that describe a world they no longer match, each invisible to every check the estate runs, each found by comparing two instruments instead of trusting one. The layer is the worst of the three to have wrong, because three functions share it and a rebuild-from-the-record would republish the wrong thing to all of them at once."
  },
  {
    "id": "IRPT_BCKEND-W3-S22",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T16:23:46Z",
    "one_line": "TWO MODULES NAMED dispatch.py COLLIDE ON THE FLAT sys.path EVERY EXPORT MODULE SHARES, SO IB-rt-8's OWN TESTS CANNOT SEE ITS DISPATCH MODULE. `_authz/dispatch.py` and `export/dispatch.py` both exist at the merged tip. export/handler.py inserts `_authz` on sys.path at import (it must -- the shared libraries live one level up), so `import dispatch` resolves to _authz/dispatch.py, and export/dispatch.py's DECISIONS, HUMAN_GATED, DispatchRefused and render_request are unreachable by that name. Four tests in export/tests/test_rt8.py fail with 'module dispatch has no attribute ...' at the pristine tip, before any change of this order's. THE DEPLOYED CASE IS WORSE THAN THE TEST CASE AND IS THE REASON THIS IS FILED: in a Lambda every packaged module sits FLAT at /var/task, so if any function ever packages both, one file OVERWRITES the other in the zip and there is no path order left to disambiguate -- the loser simply is not there. Neither is packaged together today (the export function's build input carries export/dispatch.py and, from this order, enforce.py + errors.py + resolve.py, and _authz/dispatch.py is in no function's list), so this is latent rather than live.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B to route and the owning cells to resolve -- _authz/dispatch.py is IB-rt-8's or a sibling's and export/dispatch.py is IB-rt-8's; renaming either is authoring another cell's module, and neither is this order's to rename. This order's contribution is the MEASUREMENT and the guard: the import-closure check runs in the /var/task + /opt/python layout on every build, so the day a function packages both, the arm fails rather than the function failing in production. 3.0.0_SA_CVO grades at L9; 1.0.0_SA_CTO holds the flat-packaging convention at L10.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Probe reproducing export/handler.py's own sys.path order: `import dispatch` -> _authz/dispatch.py; hasattr(dispatch, 'DECISIONS') -> False; hasattr(dispatch, 'render_request') -> False",
        "Both files exist: infra/aws/lambda/investor-reporting/_authz/dispatch.py (10800 bytes) and infra/aws/lambda/investor-reporting/export/dispatch.py (9809 bytes)",
        "export/dispatch.py's own top-level names include READY, HUMAN_GATED, ABSENT, DECISIONS, DispatchRefused, render_request -- so the module is correct and simply unreachable under that name",
        "pytest at the PRISTINE tip (git archive HEAD, no working-tree mutation): '5 failed, 61 passed, 2 skipped'; with this order's edits: '4 failed, 64 passed' -- the collisions are pre-existing and this order moved the count one in the right direction",
        "lambda-source-map.json: no function's file list contains both dispatch.py entries, so the zip-level collision is latent and not live today"
      ]
    },
    "spec_asserts": "Every shared module in this estate is packaged FLAT into each function's zip (enforce.py, keys.py, resolve.py all sit at /var/task), and modules import each other by bare name.",
    "world_is": "Two different modules already share the name `dispatch`. On the worktree's sys.path one shadows the other and a sibling cell's tests fail against it; in a zip that carried both, one would overwrite the other outright.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The flat-packaging convention is what makes the shared libraries work at all, and this is its cost: the module namespace is GLOBAL across the whole investor-reporting tree, and nothing enforces uniqueness. A name census over every packaged basename would catch it in one pass and nobody runs one."
  },
  {
    "id": "IRPT_BCKEND-W3-S23",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T16:53:42Z",
    "one_line": "RT9-AC1 ARM (a) REQUIRES RETIRING A LEGACY PROBE THAT IS NOT IN THIS ORDER'S <paths>, AND THE SAME IS TRUE OF A SECOND LEGACY READER. The arm's words are 'legacy any-non-403 probes remaining: 0'. Censused with comp-find over infra/ at the merged tip: 39 hits across 6,589 files, resolving to FOUR code readers of `ycharts/session/current` -- two of them this project's and already on the versioned bundle shape (infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js from IB-s-8 and infra/aws/lambda/investor-reporting/ycharts/generate/transport.py from IB-s-9, both inside the grant), and two of them LEGACY ycharts-pipeline consumers that are NOT: infra/aws/lambda/ycharts-session-probe/lambda_function.py and infra/aws/lambda/ycharts-session-capture/index.mjs. The probe is the one the PRD names: its predicate is `rec[\"auth_ok\"] = rec.get(\"status\") is not None and rec.get(\"status\") != 403` under the comment 'Per A3 P2 section 3.4 a 403 fails the gate; any non-403 (200, or even a 400 bad-params) means the session authenticated successfully.' A 400 bad-params response therefore reads as a healthy authenticated session, which is precisely the false-green the v0.9 cutover exists to remove. THIS ORDER'S <paths> GRANT COVERS infra/aws/lambda/investor-reporting/ycharts/, infra/aws/ec2/investor-reporting-ycharts/ and the two ycharts Terraform roots -- it does NOT cover infra/aws/lambda/ycharts-session-probe/ or infra/aws/lambda/ycharts-session-capture/, and the face's own rule is that a path this order needs and does not hold is a BLOCKING row, never an override.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B to route -- either by extending this order's <paths> to the two legacy ycharts-pipeline readers, or by naming them OUT OF SCOPE BY PRD NAME, which is the escape the arm itself already provides ('N of N migrated to the versioned bundle shape OR EXPLICITLY OUT OF SCOPE BY PRD NAME'). Either route closes the arm; neither is this order's to choose, because one of them edits a served Lambda outside the grant and the other writes a scope decision into the record. 1.0.0_SA_CTO holds the YALP_MDSRC coordination the PRD names (the legacy `ycharts/credentials` consumer must not evict the runner); 3.0.0_SA_CVO grades the cutover at L9. FILED BEFORE ANY BUILD so the cell is not aimed at a file it cannot write.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-find 'ycharts/session/current' infra/ --corpus all -> DENOMINATOR: 39 hit(s) across 6589 file(s) scanned; the code readers are ycharts_session.js (IB-s-8), generate/transport.py (IB-s-9), ycharts-session-capture/index.mjs and ycharts-session-probe/lambda_function.py, the rest being Terraform grants and briefs",
        "infra/aws/lambda/ycharts-session-probe/lambda_function.py:134 -- 'rec[\"auth_ok\"] = rec.get(\"status\") is not None and rec.get(\"status\") != 403', with the comment at :132-133 'any non-403 (200, or even a 400 bad-params) means the session authenticated successfully'",
        "The face's <paths> block lists infra/aws/lambda/investor-reporting/ycharts/, infra/aws/ec2/investor-reporting-ycharts/, infra/aws/terraform/investor-reporting/ycharts/ and .../ycharts-research-20260911/ -- neither ycharts-session-probe/ nor ycharts-session-capture/ appears",
        "RT9-AC1 arm (a), verbatim: 'Census of readers of ycharts/session/current and of the legacy probe across the estate (denominator printed): N of N migrated to the versioned bundle shape or explicitly out of scope by PRD name; legacy any-non-403 probes remaining: 0'",
        "The PRD's own v0.8 text names this as one of the five unproven boundaries: 'the production ycharts/session/current cookie-schema cutover with its competing readers (cookie-string vs cookie-array consumers; the legacy session-probe accepts any non-403 as authenticated)'"
      ]
    },
    "spec_asserts": "RT9-AC1 arm (a) requires the legacy any-non-403 probe count to reach 0 and every reader of ycharts/session/current to be migrated to the versioned bundle shape or named out of scope by PRD name.",
    "world_is": "Two of the four code readers -- the legacy probe carrying the non-403 predicate, and the legacy Puppeteer capture Lambda -- live under infra/aws/lambda/ycharts-session-probe/ and infra/aws/lambda/ycharts-session-capture/, neither of which is in this order's <paths>. The arm cannot reach 0 from inside the grant.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The arm already contains its own escape -- 'or explicitly out of scope by PRD name' -- so this may be a scope statement rather than a grant extension. That is the issuer's call and the reason this is filed rather than decided: writing 'out of scope' into the record on my own authority would be adjudicating a PRD boundary, and extending the grant myself would be the override the face forbids. Filed at the START of the cell, before anything was built against a file this order cannot write."
  },
  {
    "id": "IRPT_BCKEND-W3-S24",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T17:52Z",
    "one_line": "W2-S21's PREMISE DOES NOT HOLD AS WRITTEN, AND ACTING ON IT LITERALLY WOULD STRIP THE SHARED LIBRARIES OUT OF irpt-ycharts-generate. The amendment says the function declares 25 build inputs in lambda-source-map.json of which 7 have never existed in the tree, and instructs that a build input absent from the tree is REMOVED, never invented. Measured instead of taken on faith, because the removal is destructive: the function declares 26 inputs, and 26 of 26 RESOLVE to a real file -- 0 are genuinely absent. The 8 that do not sit under the entry's own source_dir (enforce.py, errors.py, gate.py, keys.py, resolve.py, firm_destination_policy.json, firm_registry.json, settings.json) all exist elsewhere in the tree and are packaged FLAT by this estate's Lambda convention, which is the whole reason they appear in the list by bare name: every module lands at /var/task, so a shared library is declared by basename and resolved from its home package at build time. A naive 'does source_dir/<name> exist' check is what returns 7 or 8 absent. Removing those entries would delete enforce, gate, keys and resolve -- the modules the deployed job.py imports at module scope -- and firm_registry.json, which keys.py reads. That is the W3-S19 failure class (a two-part change whose packaging half is missing), self-inflicted, and it would read GREEN at every deploy-time rung because the zip would build, upload and register cleanly and only die at cold start. NOTHING WAS REMOVED.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B -- the issuer owns the amendment text. The correction is to the PREMISE, not to a file: any later cell handed the same sentence, on this function or another, will run the same naive resolution and get the same 7-or-8 and, lacking the flat-packaging fact, will do the removal this cell declined to do. The estate has no resolver that encodes the flat convention; every reader re-derives it. 1.0.0_SA_CTO if the fix is to give lambda-source-map.json an explicit source path per entry so the convention stops being tacit.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ci/lambda-source-map.json @684e7eb90a, the irpt-ycharts-generate entry's files array -- 26 entries before this cell's edit, not 25",
        "measured by .scratch/verify_ycharts_inputs.py (this worker, flat-packaging resolver), verbatim: 'declared inputs: 26 | RESOLVE to a real file: 26 | genuinely absent: 0'",
        "the 8 outside source_dir resolve to infra/aws/lambda/investor-reporting/_authz/enforce.py and errors.py, _gate/gate.py, _keys/keys.py, _scope/resolve.py, infra/aws/terraform/investor-reporting/core/firm_destination_policy.json, data/firm_registry.json and infra/aws/lambda/investor-reporting/intake/settings.json -- each present at 684e7eb90a",
        "registered artifact_sha256 == S3 object content-sha256 == live CodeSha256 == hiVUThOsWCSe304UfRug466Oqv6tqvL/8fjKskUUpoo= , read live this turn: the RECORD AGREES WITH THE WORLD, which is not what a record carrying 7 phantom inputs would look like",
        "a rebuild from the declared list yields IdFoLLRZqJpHP9ISk8amWypuoH2dMCwUIh+dyzV/YcA= (89,789 bytes) before this cell's edit -- the tree is AHEAD of the deploy, which is a separate and expected fact, not an absence"
      ]
    },
    "spec_asserts": "The IB-rt-9 issuer amendment (W2-S21 half), verbatim: irpt-ycharts-generate declares 25 build inputs in lambda-source-map.json of which 7 have never existed in the tree: register the truth (a build input absent from the tree is REMOVED, never invented).",
    "world_is": "26 declared inputs, 26 resolving, 0 absent. The 7-of-25 figure is an artifact of resolving every name under the entry's source_dir, which the estate's flat Lambda packaging does not do.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Filed rather than obeyed, and filed rather than argued: the face's rule is that a premise which does not hold is ONE row and then keep working. The half of W2-S21 that DID hold -- register the truth, verify the triple equality -- was executed: the triple equality is printed above, and the declaration was corrected in the only direction the measurement supports, which is the ADDITION recorded in row W3-S25, not a removal."
  },
  {
    "id": "IRPT_BCKEND-W3-S25",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T17:52Z",
    "one_line": "_scope/resolve.py GAINED A MODULE-LEVEL 'import ids' AND THE PACKAGING HALF DID NOT FOLLOW FOR ANY OF THE THREE FUNCTIONS THAT SHIP IT. resolve.py at 684e7eb90a carries 'import ids as _ids' at line 81 (IB-rt-3's typed identifiers, _ids/ids.py), but lambda-source-map.json declared ids.py in ZERO of the three functions whose build inputs include resolve.py: irpt-export-render, irpt-status and irpt-ycharts-generate. Measured in the /var/task layout with the worktree excluded from sys.path: 'import closure in the /var/task layout: 6 of 8 OPEN [enforce: ModuleNotFoundError, resolve: ModuleNotFoundError]' -- enforce fails transitively because enforce.py imports resolve. The three LIVE functions still serve OLDER bytes and work today, so every deploy-time rung reads green and nothing is currently broken in production; the harm is armed for the NEXT rebuild-and-deploy of any of the three, which would upload, register, match its hash three ways and then die at cold start on ModuleNotFoundError. This is exactly the two-part-change split of row W3-S19, at a new tip, introduced by a different cell -- which is the tell that the estate has no mechanism tying an import to a build input, only workers who happen to check. REPAIRED IN THE DECLARATION HALF ONLY, inside this order's grant: ids.py is added to all three file lists and closure now reads 9 of 9 CLOSED for irpt-ycharts-generate. artifact_sha256 is DELIBERATELY NOT MOVED -- it still equals the S3 object and the live CodeSha256, and under the managed wind-down this order deploys nothing.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B to route the rebuild-and-deploy that makes the served bytes match the corrected declaration -- three functions (irpt-export-render, irpt-status, irpt-ycharts-generate), each needing a ledger entry, a safe-apply and a registered-equals-S3-equals-live re-read per W3-S18. Deferred here and ONLY here because the wind-down instruction from 0.0.0_AB_MSTR relayed 2026-09-11 17:30Z forbids opening a change-management ledger, applying, publishing or deploying for the rest of this session. The DECLARATION is fixed and committed; the DEPLOY is the successor session's first act and is written down as such in WIP_IB-rt-9_winddown.md.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/_scope/resolve.py:81 @684e7eb90a -- 'import ids as _ids  # noqa: E402'",
        "infra/aws/lambda/investor-reporting/_ids/ids.py exists at 684e7eb90a (git cat-file -e rc 0); IB-rt-3 introduced it",
        "per-function read of lambda-source-map.json @684e7eb90a: irpt-export-render resolve=True enforce=True ids.py=False; irpt-status resolve=True enforce=True ids.py=False; irpt-ycharts-generate resolve=True enforce=True ids.py=False -- 3 of 3 ship resolve.py, 0 of 3 declared ids.py",
        "import closure measured in a /var/task extraction with every repo path stripped from sys.path, BEFORE the fix: '6 of 8 OPEN [enforce: ModuleNotFoundError, resolve: ModuleNotFoundError]'; AFTER adding ids.py: 'import closure in the /var/task layout: 9 of 9 CLOSED'",
        "registered == S3 == live == hiVUThOsWCSe304UfRug466Oqv6tqvL/8fjKskUUpoo= read live this turn, so the CURRENTLY SERVED bytes predate the resolve.py change and are not affected",
        "row IRPT_BCKEND-W3-S19 -- the same class of split, recorded earlier in this project by this worker"
      ]
    },
    "spec_asserts": "The IB-rt-9 amendment (W2-S21 half) treats the build-input list as a record to be trued up, and W3-S18 requires artifact_sha256 == S3 content-sha256 == live CodeSha256 for every function a cell touches.",
    "world_is": "The build-input list was missing a module that three functions' declared code imports at module scope. The record and the world agreed on the HASH while disagreeing on IMPORTABILITY, because a hash certifies bytes and nothing in the deploy path ever imports them.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The general shape is worth more than this instance: CodeSha256 equality is the estate's standard deploy proof and it CANNOT see this defect, by construction. The only instrument that catches it is an extract-and-import in the flat layout with the repo off sys.path, which this worker runs from .scratch and which no gate runs anywhere. A candidate disarm that outlives these three functions is to make that check a commit-time gate over lambda-source-map.json; proposing is legal, implementing it is outside this order."
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
  },
  {
    "id": "IRPT_BCKEND-W4-S5",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-11T01:55:00Z",
    "one_line": "S13-AC1 arm (h) asks that the layer zip imports jsonschema AND bd_helpers in a clean Python. bd_helpers does, on any host. jsonschema CANNOT on this one, and the reason is that the layer is CORRECT: its only native dependency resolves to python/rpds/rpds.cpython-312-x86_64-linux-gnu.so, a LINUX cp312 extension -- what an AWS python3.12 Lambda needs and what a Windows build host cannot load. A clean-Python import succeeding HERE would be evidence the layer had been built for the wrong platform. The arm's substance is therefore proved on the runtime: both deployed functions carry irpt-common:2 (2 of 2) and irpt-performance-adapter returns contract_validated=true on BOTH provider paths, which is only reachable by importing jsonschema from the layer inside the Lambda. The battery prints the host attempt, its ModuleNotFoundError and the .so member name side by side so a reader can see which of the two readings they are getting.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "battery_ib_s_13.py arm (h) output, verbatim: bd_helpers -> OK: imported; built a request body with 6 dateRange(s) and a requested_range_index of 6 row(s): Custom,Year To Date,Trailing 12 Months,2025,2024,Since Inception ; jsonschema -> ERROR: ModuleNotFoundError: No module named rpds.rpds -- run with python -E -s and sys.path set to the extracted layer python/ directory only",
        "zipfile namelist of infra/aws/lambda/layers/irpt-common/irpt-common.zip: the single native member of 154 is python/rpds/rpds.cpython-312-x86_64-linux-gnu.so, and it is Linux",
        "infra/aws/lambda/layers/irpt-common/build_layer.py pip_install @a12b0df4e7 -- --platform manylinux2014_x86_64 --implementation cp --abi cp312 --only-binary=:all:, so a host-shaped resolution FAILS the build instead of producing a host-shaped layer",
        "lambda invoke irpt-performance-adapter after the attach, both providers: contract_validated=true for F-INF (Orion) and F-49F (Black Diamond) -- the RUNTIME import, which is the one the product depends on"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S13-AC1 arm (h): The layer zip imports `jsonschema` and `bd_helpers` in a clean Python (printed).",
    "world_is": "One of the two imports is host-portable and one is deliberately not. The un-portable one is un-portable BECAUSE the layer is built for its deployment target, so the literal arm is unsatisfiable on any non-Linux build host and its substance is checkable only on the runtime.",
    "notes": "Not blocking: the arm was met on the plane that matters and both readings are printed. The residue for 3.0.0_SA_CVO is a wording one -- a future face asking for a clean-Python import of a cross-platform layer should ask instead for the RUNTIME import (an invoke) plus the platform tag of the native member, which is what was done here."
  },
  {
    "id": "IRPT_BCKEND-W4-S6",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-11T01:55:00Z",
    "one_line": "The issuer amendment names TWO things the deployed irpt-performance-adapter could not carry (jsonschema and the bounded BD helpers). There is a THIRD, and jsonschema alone would not have moved the arm: the CONTRACT SCHEMA FILE is not in the performance zip either. normalize.py resolved it at <package>/../_contracts/PerformanceReport.schema.json, which inside a Lambda is /var/_contracts and does not exist, so contract_validated would have gone from false-for-want-of-a-library to false-for-want-of-a-file and arm (h) would still have failed. Fixed inside this order grant: the layer carries the contracts at /opt/python/irpt_contracts and normalize.py resolves env -> layer -> repo BY PRESENCE OF THE FILE, so an empty layer directory cannot shadow a worktree run, with the repo path last and unchanged. Measured after: the deployed function returns contract_validated=true on both provider paths and the 28 IB-s-11 tests still pass.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/performance/normalize.py:43 @410f28f7db -- CONTRACTS = pathlib.Path(__file__).resolve().parents[1] / _contracts ; the build flattens source_dir to the zip root, so parents[1] is /var on the runtime",
        "infra/aws/lambda/ci/lambda-source-map.json @410f28f7db -- the irpt-performance-adapter files[] list carries 7 .py files and 6 fixture JSONs and NO _contracts entry, so the schema is not in the artifact",
        "normalize.py _resolve_contracts_dir @a12b0df4e7 -- three candidates, resolution by (path / PerformanceReport.schema.json).is_file(), repo path last",
        "lambda invoke irpt-performance-adapter after the attach: contract_validated=true, and the contract_validation PARTIAL absence IB-s-11 shipped is absent from the response",
        "python -m pytest infra/aws/lambda/investor-reporting/performance/tests -q -> 28 passed, after the change"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The L5 note in this face: This order builds ONE shared layer at infra/aws/lambda/layers/irpt-common/ -- jsonschema (pinned) plus a bd_helpers module ... The deployed performance function then validates contracts (contract_validated=true).",
    "world_is": "A Lambda zip is closed over its own directory, so a SHARED contract resolved by a relative path out of the package cannot resolve on the runtime. Two of the three dependencies were named in the amendment; the third had to be found by building it.",
    "notes": "Surfaced rather than silently absorbed because it WIDENS what the layer carries beyond the amendment wording. Both the layer path and the performance package are in this order <paths>, so no grant was exceeded. The alternative -- packaging a copy of the schema inside the performance zip -- was refused: a second copy of a SHARED contract is the same defect class the bd_helpers reuse exists to prevent."
  },
  {
    "id": "IRPT_BCKEND-W4-S7",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-11T01:55:00Z",
    "one_line": "The first assembled bd_helpers PARSED and could not IMPORT: the AST closure pulled functions and module-level constants but not module-level IMPORTS, so BENCHMARK_IDS = [int(x) for x in os.environ.get(...)] raised NameError: name os is not defined at /opt/python/bd_helpers.py line 21 on the runtime. compile() passed it, which is exactly why a generator whose only test is that its output parses will ship a module that cannot import. Two things made it visible and both are worth carrying: (1) the failure was INVISIBLE to the first verification invoke because that invoke used the Orion path, which never loads the BD helpers -- one provider read GREEN on a layer broken for the other; (2) the remedy is not only the closure but the FALSIFIER -- build_layer.py now execs the module it generated in a clean namespace and requires every requested helper to be callable, so a missed closure member fails the BUILD instead of the deployed function. Separately the same build was NOT reproducible as first written (three builds, three digests): pip console-script launchers are freshly stamped .exe files on a Windows host and the dist-info RECORD line hashes them. Both are excluded now and two consecutive builds are byte-identical.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda invoke irpt-performance-adapter with an F-49F scope, verbatim: errorMessage name os is not defined / errorType NameError / stackTrace File /opt/python/bd_helpers.py, line 21, in <module> BENCHMARK_IDS = [int(x) for x in os.environ.get(",
        "infra/aws/lambda/layers/irpt-common/build_layer.py assemble_helpers @8e5d8cadad -- module-level Import/ImportFrom aliases are collected and joined into the closure; BUILD_MANIFEST records imports_emitted [os] beside functions_emitted (6) and constants_emitted (3)",
        "build_layer.py @8e5d8cadad -- the assembled module is exec'd in a clean namespace at build time and every requested helper must be callable afterwards, or the build exits non-zero",
        "three builds of identical inputs before the exclusions: 674531 / 674530 / 674529 bytes with three distinct digests, differing ONLY in python/bin/jsonschema.exe and the jsonschema dist-info RECORD line that hashes it; after: two consecutive builds cmp-clean at 621748 bytes",
        "battery_ib_s_13.py arm (h): both providers invoked, 2 of 2 contract_validated=true, 0 helper-degraded cells"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The L5 note: a bd_helpers module ASSEMBLED AT BUILD TIME from the reporting-pull Lambda source at a pinned commit (the estate build_package.py shape: git show <pin>:<path>, never a hand copy).",
    "world_is": "An AST closure over functions and constants is not the closure a module needs in order to import; imports are part of it. And a code generator whose only test is that its output compiles has no test of the property its consumers depend on.",
    "notes": "The generalisable half is the verification one rather than the Python one: a PER-PATH dependency needs a PER-PATH exercise. One green invoke was not the population, and the arm now invokes both providers explicitly and prints 2 of 2."
  },
  {
    "id": "IRPT_BCKEND-W4-S8",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-11T01:55:00Z",
    "one_line": "`.tools/aws` cannot be spawned from a Windows Python: subprocess raises OSError [WinError 193] is not a valid Win32 application, because the file is a bash script with no Windows launcher. Any battery, generator or gate that shells the estate AWS shim FROM PYTHON on this device dies at the first call, and the error names Win32 rather than the shim, so it reads as a broken AWS call. The usable face is the sibling `.tools/aws.cmd` invoked as [cmd, /c, <path>, ...] -- same shim, same credentials, same CLI v1 behaviour -- and it keeps the instrument the estate own rather than substituting a boto3 call for it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "subprocess.run([str(REPO/.tools/aws), dynamodb, scan, ...]) from Python 3.12.10 on this device: OSError: [WinError 193] is not a valid Win32 application -- raised twice, once in make_narrative_fixtures.py and once in battery_ib_s_13.py",
        "ls -la .tools/aws .tools/aws.cmd -- both present (7350 and 2271 bytes); CLAUDE.md Git section says AWS via the .tools/aws shim (+aws.cmd, both or neither), which is the pairing rule and not guidance on which face Python may exec",
        "subprocess.run([cmd, /c, .tools\\aws.cmd, sts, get-caller-identity, --output, json]) -> rc 0 with arn:aws:iam::313476888478:user/Andrew_Berman",
        "battery_ib_s_13.py AWS constant at this commit: [cmd, /c, str(REPO/.tools/aws.cmd)], with the reason in a comment beside it"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md Git section: AWS via the `.tools/aws` shim (+`aws.cmd`, both or neither); never bare MSYS_NO_PATHCONV=1 aws.",
    "world_is": "The two faces of the shim are not interchangeable by caller. From bash either works; from a Windows Python only the .cmd does, and the bash one fails with an error that points away from the cause.",
    "notes": "Recorded because it costs a cycle every time. Same family as the existing memory note that Python spawning an MSYS binary must go through .tools/msys_argv_guard.py -- this is the AWS-shim instance of it."
  },
  {
    "id": "IRPT_BCKEND-W4-S9",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-11T07:10:00Z",
    "one_line": "THE DEPLOYED EXPORT WORKER CANNOT RENDER, and this is the cell's central product gap rather than a packaging detail. A PDF needs a headless browser; none exists in a python3.12 Lambda and one cannot be added without fetching a browser build off Opal infrastructure, which the estate refused at IB-s-8 (rows W3-S1/S2). irpt-export-render is therefore deployed with IRPT_EXPORT_RENDERER=unavailable set EXPLICITLY -- a function that discovers it has no browser at invoke time reports an error, a function that is told it has none reports an ABSENCE with a reason -- and its iam.tf grants no s3:PutObject and no kms:Decrypt, because a write grant for a path that cannot execute is a standing grant bought with nothing. The MECHANISM is proved in the worktree against the estate's OWN existing headless path (Playwright driving the locally installed Edge through channel=msedge, exactly as docs/research/investor_reporting_export_20260910/build_export_review.py does, downloading nothing): 9 of 9 battery arms including three real vendor-input exports. What does not exist is a CLOUD render. Until a runtime lands, FWD-8's export is a worktree capability with a deployed shell around it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B -- the headless runtime is a build decision (a container image, a browser layer, or an out-of-Lambda worker) and every candidate is outside this order's <paths>; a later cell owns it, and the S14 arms that would have to be re-run at that point are named in the S14-AC3 judgment",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda invoke irpt-export-render action=capabilities, verbatim: renderer=unavailable, renderer_available=false, renderer_absence='forced by IRPT_EXPORT_RENDERER=unavailable', renderer_version=chromium-print/msedge-channel/irpt-1.0.0",
        "infra/aws/terraform/investor-reporting/export/lambda.tf @1beda4bf49 -- IRPT_EXPORT_RENDERER is set to `unavailable` explicitly, with the reason in the header",
        "infra/aws/terraform/investor-reporting/export/iam.tf @1beda4bf49 -- the NOT GRANTED list names s3:PutObject/GetObject and kms:Decrypt and says they land WITH the runtime",
        "docs/research/investor_reporting_export_20260910/build_export_review.py:210-235 -- the estate's own headless path: playwright.chromium.launch(channel='msedge'), page.pdf(prefer_css_page_size=True)",
        "battery_ib_s_14.py arms (a)-(g)+(v0.11): 9 of 9 passed in the worktree, 4 renders under a socket guard with 0 external connections and a positive control that moved the counter"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The L5 note: 'infra/aws/lambda/investor-reporting/export/ (Lambda irpt-export-render, a headless-browser runtime consuming irpt-export)'; the hand-off's fact (1): 'if no headless runtime is reachable without egress, that is ONE row and the render arm uses the estate's existing PDF path with the substitution stated'.",
    "world_is": "The render MECHANISM is proved and reproducible; the CLOUD RENDER does not exist. The deployed function reports the absence with its reason instead of emitting a PDF from a different engine under the same artifact revision.",
    "notes": "The substitution IS the estate's existing PDF path, not a new dependency: playwright and a local Edge were already on this machine and nothing was installed. The deployed absence and the worktree proof are two different claims and the battery keeps them apart."
  },
  {
    "id": "IRPT_BCKEND-W4-S10",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-11T07:10:00Z",
    "one_line": "THE irpt-common LAYER CARRIES 2 OF THE 5 IRPT CONTRACTS THE DEPLOYED FUNCTIONS NEED. IB-s-13 built it for the performance and narrative functions, so it packages PerformanceReport and NarrativePacket; the three EXPORT contracts (RenderPackage, ExportBundle, ExportReceipt) are not in it. The export function's resolution order worked exactly as designed -- env, then /opt/python/irpt_contracts, then the repo path, BY PRESENCE OF THE FILE -- and correctly fell through to /var/_contracts, which does not exist in a Lambda. jsonschema IS importable there; the schema FILES are not, and those are different facts. Rebuilding the layer is not available to this order: infra/aws/lambda/layers/irpt-common/ and infra/aws/terraform/investor-reporting/performance/ are NOT in IB-s-14's <paths>, and a path this cell needs that the order does not name is a row, never an override. What changed instead is the REPORT: `capabilities` now names per contract which schema this runtime can check, rather than raising ValidationUnavailable and dying of the thing it exists to report.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B -- one line in the layer's CONTRACTS tuple (build_layer.py) plus a rebuild and a re-apply of the performance root; both surfaces belong to IB-s-13's paths, not this order's. Every later cell whose deployed function validates an export contract inherits the same UNAVAILABLE until it lands",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/layers/irpt-common/BUILD_MANIFEST.json @HEAD -- contracts[] carries exactly python/irpt_contracts/PerformanceReport.schema.json and python/irpt_contracts/NarrativePacket.schema.json; 2 of the 11 contracts in _contracts/, and 0 of the 3 this cell validates",
        "lambda invoke irpt-export-render, first attempt after the import fix: {\"errorMessage\": \"contract not packaged at /var/_contracts/RenderPackage.schema.json\", \"errorType\": \"ValidationUnavailable\"}",
        "lambda invoke irpt-export-render after the change: contract_validators = {RenderPackage: UNAVAILABLE..., ExportBundle: UNAVAILABLE..., ExportReceipt: UNAVAILABLE...} with statusCode 200",
        "IRPT_BCKEND.TO-IB-s-14 <paths> -- infra/aws/lambda/layers/ and infra/aws/terraform/investor-reporting/performance/ are absent from the grant",
        "infra/aws/lambda/investor-reporting/export/bundle.py contracts_dir() -- resolution by (path / filename).is_file(), env then layer then repo, so an empty layer directory cannot shadow a worktree run"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S14-AC1 arm (g): 'the packet validates'; the deployed function is expected to validate the contracts it produces.",
    "world_is": "A shared layer built for two consumers serves two consumers. The third arrived with three more contracts and no write access to the layer, so the deployed function reports which validators it has instead of claiming a validation it did not perform.",
    "notes": "The worktree validates all three (jsonschema plus the repo _contracts path), which is what the 33 offline tests and the 9 battery arms exercise. The gap is deployed-only and is visible in the function's own output."
  },
  {
    "id": "IRPT_BCKEND-W4-S11",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-11T07:10:00Z",
    "one_line": "A REPO-RELATIVE PATH COMPUTED AT IMPORT KILLED THE DEPLOYED FUNCTION BEFORE IT COULD REPORT ANYTHING. assets.py resolved the estate's gitignored brand sources from `_HERE.parents[4]`; the packaged zip unzips to /var/task, which has TWO ancestors, so the expression raised `IndexError: 4` at line 1 of the handler's import. THREE local instruments passed it -- the 31 offline tests, the ADHC import-closure gate and the build -- because all three run in a tree where five ancestors exist. AND THE FIX HAD ITS OWN NEAR-MISS WORTH MORE THAN THE BUG: written as a bounded walk with levels=4 it reproduced parents[3] and landed on infra/, and THE TEST SUITE STILL PASSED, because the fallback test accepts either the present or the absent branch on purpose (a machine may legitimately lack the gitignored sources) -- so a wrong root silently took the absent branch and read green. It is caught by asserting the resolved root CARRIES infra/aws/lambda and deck_generation, which is a property of the ROOT rather than of the files.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda invoke irpt-export-render, verbatim: {\"errorMessage\": \"4\", \"errorType\": \"IndexError\", stackTrace ... File \"/var/task/handler.py\", line 44, in <module> import assets as assets_mod / File \"/var/task/assets.py\", line 75, in <module>}",
        "infra/aws/lambda/investor-reporting/export/assets.py _repo_root() @e3fe224e30 -- a bounded walk that stops at the filesystem root, levels=5, with the off-by-one recorded in its own docstring",
        "test_the_repo_root_walk_survives_a_shallow_path and test_the_brand_sources_resolve_where_they_are_provisioned @e3fe224e30 -- the two controls; the second is the one that can see a wrong depth",
        "python -m pytest infra/aws/lambda/investor-reporting/export/tests -q -> 33 passed, after both",
        "with the corrected root the fallback resolves the official logo: sha256 02477c761bbaac4ec4c23e1b0d2f743271c1d94ec6b1f81ed9a31a8e99fe58b3, 3853 bytes, 1301.87 x 575.0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "DELIVERABLE: 'infra/aws/lambda/investor-reporting/export/ (assets.py, ...)'; BOUNDS 4: served bytes verified as CodeSha256 against the built zip.",
    "world_is": "A module that computes a REPO-RELATIVE path at import time carries a claim about its own depth in a tree, and a Lambda is the environment where that claim is false. Every local instrument runs where it is true.",
    "notes": "Same family as IB-s-13's assembled module that parsed and could not import (row W4-S7): a failure the deployed environment has and no local instrument does. The generalisable half is that a test which accepts BOTH branches of an absence cannot detect a wrong path -- it needs one assertion about the path itself."
  },
  {
    "id": "IRPT_BCKEND-W4-S12",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-11T07:10:00Z",
    "one_line": "A RETRY OF A BYTE-IDENTICAL BUNDLE MINTS A NEW export_id, AND NOTHING THIS CELL CAN DO PREVENTS IT. Chromium stamps a creation date and a document /ID into every PDF, so two renders of ONE frozen bundle produce different bytes (measured: 25,231 bytes each, different sha256; and across two full battery runs the ONLY lines that moved were four raw digests and the export ids derived from them). The receipt's artifact.sha256 is the RAW digest -- an artifact hash must name the object that exists -- and export_id is derived from (bundle_sha256, artifact_sha256), so it moves with the bytes. S14-AC1 (a) is therefore met on a CONTENT hash (page count + each page's media box + each page's content stream + the extracted text), which IS stable, and the battery prints both side by side rather than quietly hashing something normalized and calling it the PDF. THE CONSEQUENCE FOR A CONSUMER: the stable identity of an export is the BUNDLE hash, not the receipt id. A downstream consumer that de-duplicates on export_id will see a new export for every retry of identical input.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B -- whether a retry REUSES the prior receipt (keyed on bundle_sha256) or mints a new one is a product decision, not a rendering one, and it belongs to the cell that owns the job table (IB-s-17's surface). Until it is taken, a consumer keying on export_id accumulates duplicates",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "battery_ib_s_14.py arm (a) output: 'bundle sha256, preview/render/retry equal across the three: True (3 of 3)', 'content hash equal: True', 'RAW equal: False'",
        "diff of two consecutive full battery runs: 14 lines, 8 changed lines, ALL of them raw sha256 values and the export ids derived from them; every bundle hash, content hash, page count, census and verdict identical",
        "infra/aws/lambda/investor-reporting/export/receipt.py export_id_for() -- sha256 over (bundle_sha256 | artifact_sha256), so the id is a function of the bytes",
        "a direct probe before the design was fixed: two renders of identical HTML through playwright/msedge, 25231 bytes each, sha256 437618c1d8079286... and 55e6ac2f925046e4..., with the normalized content hash equal (eac447b107987789...)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S14-AC1 (a): 'the rendered PDF's content hash equal between render and retry'; the acceptance clause draft: 'retry reuses the bundle, no vendor call during render'.",
    "world_is": "The bundle is reusable and is reused; the ARTIFACT is not byte-reproducible, because the engine stamps time into it. The face's own words say 'content hash', and that is what is asserted -- the raw digest is reported as unstable rather than presented as if it were not.",
    "notes": "Not a defect of the render: it is a property of every PDF print engine. Recorded because the receipt id inherits it, and a reader who assumes export_id is stable across a retry will be wrong."
  },
  {
    "id": "IRPT_BCKEND-W4-S13",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-11T07:10:00Z",
    "one_line": "THE BATTERY WRITES FOUR REAL OBJECTS INTO THE LIVE EVIDENCE BUCKET, under firms/49financial/generations/GENIBS14SYN/attempts/1/exports/{r1,v0-11-overview,v0-11-comparison,v0-11-multicomp}/report.pdf. S14-AC1 (g) requires the receipt's artifact_hash to equal THE STORED OBJECT'S, and a stored object is a write -- there is no reading of that arm that does not put bytes in the bucket. Two things make the write safe to read later and both are deliberate: the generation id is GENIBS14SYN, which is not a client generation and cannot be mistaken for one, and every object carries irpt-synthetic=true in its metadata (the vendor-input three additionally carry vendor-synthetic-holdings=true, the label the v0.11 amendment asks for and never synthetic:true, which the face reserves). The firm prefix is REAL because _keys._check_tenant validates the tenant against data/firm_registry.json -- a made-up firm has no admissible shape, so there is no synthetic prefix to write to.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B -- four objects under one unmistakable generation id; delete or relocate them before any consumer reads the generations prefix as client evidence. This worker does not delete them because arm (g) and arm (v0.11) are graded on them being there",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "battery_ib_s_14.py arm (g): 'artifact key firms/49financial/generations/GENIBS14SYN/attempts/1/exports/r1/report.pdf', put then get, 'receipt artifact_hash == stored object sha256: True'",
        "battery_ib_s_14.py arm (v0.11): three more keys under the same generation, each put with --metadata irpt-synthetic=true,vendor-synthetic-holdings=true,export-revision=v0-11-<variant>, each read back and hash-compared",
        "infra/aws/terraform/investor-reporting/core/layout.json -- generation_artifacts.export_pdf = exports/{revision}/report.pdf under firms/{firm_id}/generations/{id}/attempts/{a}/: the key is the DECLARED layout, built by _keys.s3_evidence_key and not by a format string",
        "infra/aws/lambda/investor-reporting/_keys/keys.py _check_tenant -- the tenant is validated against data/firm_registry.json, so a synthetic firm prefix is inexpressible"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S14-AC1 (g): 'ExportReceipt validates and its artifact_hash equals the stored object's; the object key is under the bound firm's exports prefix'. BOUNDS 7: 'No served output is touched ... except where THIS order's cell says it ADDS a resource' -- and the cell text names 'the protected artifact under firms/<id>/generations/<id>/attempts/<a>/exports/<revision>/report.pdf'.",
    "world_is": "Proving the receipt against a STORED object means storing one, and the only admissible prefixes are real firms'. The write is labelled twice (an unmistakable generation id and object metadata) rather than hidden, so a later reader can tell it from client evidence without reading this row.",
    "notes": "No client data is in any of the four: the performance/analysis content is the cell's own fixture sections, and the three vendor-input exports are rendered from the CRO's synthetic portfolio 2332257 (SPY/AGG), which the PRD already calls real vendor output on synthetic holdings."
  },
  {
    "id": "IRPT_BCKEND-W4-S14",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-11T13:40:00Z",
    "one_line": "THE CLOUD RENDER IS HUMAN-GATED, and the reason is NOT that no host carries a browser -- it is that no host carrying one may be started by this cell. Three candidates, each measured: (1) a NEW export host needs `playwright install chromium`, egress off Opal infra refused at IB-s-8, and there is nothing internal to install from -- 0 of 317 objects in opal-313476888478-lambda-artifacts and 0 of 10 layer zips carry a Chromium or Playwright bundle; (2) irpt-ycharts-runner (i-0167fd745ad906a66) HAS the browser (the CRO drove Playwright on it for the 2026-09-11 variants capture) and is HELD STOPPED by aws_ec2_instance_state.runner, whose own root header says starting it is a live vendor call needing Andrew's per-use word -- a render is NOT a vendor call, but an operator seeing that host running cannot tell a render from the sign-in the control exists to gate, and that indistinguishability IS the control; (3) bd-49f-auto-login HAS the browser and hosting an IRPT render on the box that holds a Black Diamond firm session is the co-tenancy investor-reporting-ycharts/instance.tf refuses in writing, and neither its directory nor its root is in this order's <paths>. A FOURTH dependency is named so it is not discovered at the console: the counterpart's print entry point is an AUTHENTICATED APP ROUTE, so the host also needs a session the typed client can use -- a separate operator decision from starting a box. Everything around the render is built, deployed and proven on the served service; the render itself is one step, and RT8-AC1 (a) admits HUMAN-GATED as the arm's own rule.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B -- two acts disarm it and both are outside this order's grant: EITHER Andrew's word that starting irpt-ycharts-runner for a RENDER is not the gated sign-in (with the ycharts root amended to say so), OR a one-time image build on Opal infrastructure for a dedicated export host. The operator act is written verbatim in infra/aws/ec2/investor-reporting-export/README.md; IB-rtb-1's replay is where a rendered PDF would be graded",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda invoke irpt-export-render action=render_preflight, verbatim: decision=HUMAN_GATED, host irpt-ycharts-runner (i-0167fd745ad906a66) state=stopped, document_exists=true, with the three-command operator act returned as data -- the SERVED controller reads the world and refuses",
        "infra/aws/terraform/investor-reporting/ycharts/instance.tf @7478fdf144 -- resource aws_ec2_instance_state.runner { state = \"stopped\" } and the header 'starting this host is a live vendor call and needs Andrew's per-use word'",
        "s3api list-objects-v2 over opal-313476888478-lambda-artifacts: 317 objects, 0 matching chromium/playwright/chrome/headless; the layers bucket holds 10 zips and none is a browser",
        "portal/src/pages/InvestorReporting/render/manifest.ts @edab15b54f -- RENDER_PACKAGE.runtime = 'browser' with the note that recharts draws only under a browser layout pass (IRPT_FNTEND-W2-S4)",
        "portal/src/pages/InvestorReporting/render/PrintEntry.tsx @edab15b54f -- the print entry is the ROUTE /investor-reporting/print, which reads the bundle through the typed client, so the render needs an authenticated session as well as a browser",
        "docs/research/investor_reporting_ycharts_variants_20260911/ec2_recapture_01.json -- the CRO's Playwright capture ran on that instance, which is how the browser got onto its volume without new egress"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The L5 note: 'the host runs the counterpart's RenderPackage print entry point in Chromium and writes the PDF ... If no existing host carries a usable browser without egress, that is ONE row and the render arm reads HUMAN-GATED naming the operator's act, never a silent skip.'",
    "world_is": "A host DOES carry a usable browser. What no reachable host offers is a start this cell may perform without breaching a control it does not own or a co-tenancy the estate refuses in writing. The face's trigger condition and the actual blocker are adjacent but not identical, and the difference is stated rather than folded into the nearer wording.",
    "notes": "The controller carries no ec2:StartInstances and no ec2:StopInstances by design: a function that could start a host held stopped by a declared control would make that control advisory. The whole gated surface is ONE step; the freeze, the persist-before-render, the version gate, the identity, the dispatch decision and the download all ran on the served service."
  },
  {
    "id": "IRPT_BCKEND-W4-S15",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-11T13:40:00Z",
    "one_line": "THE `irpt-common` LAYER IS A SHARED WRITE SURFACE AND TWO ROUND-2 CELLS ARE WRITING IT FROM DISJOINT BRANCHES. One S3 key (s3://opal-313476888478-lambda-layers/irpt-common.zip) and one terraform-managed aws_lambda_layer_version, named in both IB-rt-8's <paths> and IB-rt-3's. MEASURED: this cell uploaded a 637,134-byte zip at 12:55 and published it as version 4; at 12:59:37 the key held a DIFFERENT 631,060-byte object, and a member diff showed it carried IB-rt-3's python/ids.py and python/raw_keys.json while MISSING this cell's three export contract schemas and keys.py. Last writer wins on the key, and the loser's members vanish from the NEXT publish -- silently, because a layer version is immutable so the already-deployed functions keep working while the plan quietly proposes replacing the version with the other cell's content. This cell restored the key to match its published version (deleting nothing; S3 versioning keeps both), and by 13:3xZ a version 5 existed at 644,526 bytes whose runtime read is 5 of 5 contracts -- i.e. a UNION -- so the published digest can no longer equal any single cell's local build. The battery's arm (c) was rewritten to assert the RUNTIME READ rather than digest equality, because asserting equality would make a correct merged layer read as a failure.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B -- the drain must rebuild irpt-common from the MERGED branch state (the union of each cell's CONTRACTS/MODULES/DATA lists) and republish BEFORE any further apply of the performance root, and IB-rtb-1's replay must re-read a capabilities invoke afterwards. Until then a plan on the performance root that proposes replacing the layer version must not be applied blind: it will publish whichever branch's zip happens to be on the key",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api head-object on irpt-common.zip at 12:59:37Z: ContentLength 631060, content-sha256 ZvfLP5IwnaROdfP0nplUZxzci13k2A8b3Abd/pmJ+2Q= -- neither this cell's 637134 / TjZRSAPsIAUdOB3pjGIU9dIBtnnEwW1jotd+8hXDfnE= nor the value its published version 4 carries",
        "zipfile member diff, live object vs this cell's build: only in LIVE ['python/ids.py', 'python/raw_keys.json']; only in MINE ['python/irpt_contracts/ExportBundle.schema.json', 'python/irpt_contracts/ExportReceipt.schema.json', 'python/irpt_contracts/RenderPackage.schema.json', 'python/keys.py']; contracts in LIVE: only NarrativePacket and PerformanceReport",
        "the live python/ids.py header names its own cell: 'IRPT_BCKEND -- THE ONE OPAQUE-ID NORMALIZER. Cell IB-rt-3 (CTO ruling 4, round 2)'; neither ids.py nor raw_keys.json exists anywhere in THIS worktree, so the two builds cannot produce each other's union from source",
        "terraform plan on the performance root while the key was drifted: 'aws_lambda_layer_version.irpt_common must be replaced ... source_code_hash ... # forces replacement' -- an apply there would have published the other cell's content",
        "after restoring the key: 'No changes. Your infrastructure matches the configuration.'; later, get-layer-version irpt-common:5 reads 644526 bytes and a capabilities invoke reads 5 of 5 contracts, so version 5 is a union"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The face's <paths> grants this cell infra/aws/lambda/layers/irpt-common/ and infra/aws/terraform/investor-reporting/performance/; the L5 note says the layer is 'rebuilt to carry all five IRPT contracts ... the performance and narrative functions re-pointed'.",
    "world_is": "Two cells hold a write grant on the same single-object surface and neither can produce the other's content from its own branch. The grant is per-path and the CONFLICT is per-OBJECT, so nothing in the lane system sees it.",
    "notes": "No content was deleted: the restore was a PUT of this cell's zip, and S3 object versioning retains the other. The deployed state is correct as of this row -- all three functions reference ONE version and its runtime read is 5 of 5 -- but that correctness is a property of who published last, not of any control."
  },
  {
    "id": "IRPT_BCKEND-W4-S16",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-11T13:40:00Z",
    "one_line": "THE ExportReceipt CONTRACT HAS NO SLOT FOR AN ATTEMPT ID, and the ruling asks the receipt to carry one. The CTO's ruling 5 and this face both say 'the receipt carries both plus the raw artifact digest' -- export_id, attempt_id and the digest. The contract admits two of the three: export_ref.export_id (now the LOGICAL identity, which is the load-bearing half) and artifact.sha256 (the raw digest). It cannot admit the third: the schema is additionalProperties:false at the ROOT and on EVERY nested object, including export_ref, whose properties are exactly export_id, bundle_id and bundle_sha256. Putting the attempt id in bundle_id would be a lie about a field named for something else. So attempt_id and attempt_number travel in the receipt's SIDECAR and in the stored object's metadata (irpt-attempt-id), where a reader can find them beside the artifact -- and the gap is recorded rather than papered over, because infra/aws/lambda/investor-reporting/_contracts/ is NOT in this order's <paths> and a contract edit is not this cell's act.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B -- adding `attempt_id` (and `attempt_number`) to ExportReceipt.export_ref is a one-field contract change on a SHARED contract, so it needs the counterpart's half as well as a cell that holds _contracts/ in its paths. Until it lands, any consumer that needs to know WHICH attempt produced a stored artifact must read the object's metadata, not the receipt",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/_contracts/ExportReceipt.schema.json @7478fdf144 -- root additionalProperties:false; export_ref additionalProperties:false with properties ['export_id','bundle_id','bundle_sha256']; every other nested object likewise closed",
        "ROUND_ANALYSIS.round1.md ruling 5 and this face's L5 note: 'the receipt carries both plus the raw artifact digest'",
        "infra/aws/lambda/investor-reporting/export/handler.py finalize_export @this commit -- sidecar['attempt_id'] / ['attempt_number'] and object_metadata['irpt-attempt-id'], with the reason in a comment at the site",
        "the persisted bundle object's live metadata, read back by the battery: {'irpt-attempt-id': 'ATT-...', 'irpt-bundle-sha256': '...', 'irpt-contract-version': 'investor-reporting_1', 'irpt-export-id': 'EXP-...'}",
        "IRPT_BCKEND.TO-IB-rt-8 <paths> -- infra/aws/lambda/investor-reporting/_contracts/ is absent from the grant"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The L5 note: 'IDENTITY: export_id = the logical identity derived from (bundle_sha256, contract_version) ... attempt_id explicit per render; the receipt carries both plus the raw artifact digest'.",
    "world_is": "A closed contract cannot carry a field the ruling adds to it. Two of the three facts fit; the third is carried beside the artifact instead, and the divergence from the ruling's wording is stated rather than absorbed.",
    "notes": "The load-bearing half of the ruling IS satisfied: export_id is now stable across a byte-identical retry, which is what row W4-S12 was about. What is deferred is only where the attempt id is written."
  },
  {
    "id": "IRPT_BCKEND-W4-S17",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-11T13:40:00Z",
    "one_line": "THE ESTATE'S KEY GRAMMAR WAS NOT IN THE RUNTIME, and only a deployed invoke could see it. The export controller builds every S3 key through `_keys.s3_evidence_key` so a client name cannot become a path component; `_keys` lives one directory above the package and a Lambda zip is closed over its own directory, so the first submit on the served service returned `No module named 'keys'`. The 68 offline tests, the import-closure gate and the build all passed, because all three run where the whole package tree is on sys.path -- the same shape as rows W4-S7 (an assembled module that parsed and could not import) and W4-S11 (a repo-relative path that is an IndexError in /var/task). THE FIX IS THE LAYER, NOT A COPY: keys.py and data/firm_registry.json now travel in irpt-common at pinned commits beside the contracts, and IRPT_FIRM_REGISTRY names the packaged registry so nothing depends on the module's bounded upward walk. Copying keys.py beside each function would have put N definitions of one grammar in the estate, which is the defect the layer exists to prevent.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda invoke irpt-export-render action=submit, first deployed attempt: statusCode carried \"No module named 'keys'\"",
        "infra/aws/lambda/layers/irpt-common/build_layer.py MODULES/DATA @this commit -- ('infra/aws/lambda/investor-reporting/_keys/keys.py',) and ('data/firm_registry.json','firm_registry.json'), carried by git show at a pin like the contracts; BUILD_MANIFEST records keys.py @3be9d03962 and firm_registry.json @1f54e16dfd",
        "infra/aws/lambda/investor-reporting/_keys/keys.py _find_registry -- IRPT_FIRM_REGISTRY first, then a bounded walk, then a copy beside the module; the export function's env now names the first",
        "after the layer rebuild and re-apply, the same invoke returns statusCode 200 with the bundle key firms/49financial/generations/GENRT8PROOF/attempts/1/exports/rt8-a/bundle.json built by the grammar"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Bound 13: 'Firm, client, relationship, account, report, export and job ids cross a function boundary as ISSUED opaque ids of a declared type'; the L5 note: the host writes the PDF to 'the bound firm's exports/<revision>/attempts/<a>/report.pdf'.",
    "world_is": "A shared library a package imports is not in the package's zip. Three local instruments all run where it is on the path, so none of them can see the absence; the deployed invoke is the only oracle.",
    "notes": "Third instance of one class in this slot's history (W4-S7, W4-S11, this). The generalisable form: any claim a module makes about its own ENVIRONMENT -- its depth in a tree, what is importable beside it -- is false in a Lambda and true everywhere a test runs."
  },
  {
    "id": "IRPT_BCKEND-W4-S18",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-11T13:40:00Z",
    "one_line": "THIS CELL'S OWN PROOF OBJECTS WERE THE CASE ITS EXCLUSION ARM EXISTS TO CATCH, for one run. The RT8 battery's submits write frozen bundles under generation GENRT8PROOF; that name does not end in SYN and was not in SYNTHETIC_GENERATIONS, and the controller was not yet stamping metadata -- so neither exclusion predicate fired on them, and an arm that censused only the ruling's GENIBS14SYN prefix would never have looked. Two fixes, and the second is the one that matters: the generation is listed, AND `handler.persist_bundle` now stamps irpt-synthetic=true from `exclusion.key_is_synthetic(key)`, so a synthetic generation labels its own objects without anyone remembering to pass a flag. The battery now censuses BOTH prefixes and reads 5 of 5 EXCLUDED_BY_BOTH.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "battery_ib_rt_8.py run 4 arm (a): the persisted bundle's live metadata carried irpt-export-id, irpt-attempt-id, irpt-bundle-sha256 and irpt-contract-version -- and NO irpt-synthetic key",
        "infra/aws/lambda/investor-reporting/export/exclusion.py @this commit -- SYNTHETIC_GENERATIONS = ('GENIBS14SYN', 'GENRT8PROOF') with the reason recorded at the constant",
        "infra/aws/lambda/investor-reporting/export/handler.py persist_bundle @this commit -- if exclusion_mod.key_is_synthetic(key): meta['irpt-synthetic'] = 'true'",
        "battery run 6 arm (e): 'prefix .../GENIBS14SYN/ 4 object(s)' and 'prefix .../GENRT8PROOF/ 1 object(s)', classification ['EXCLUDED_BY_BOTH'] x 5, and 4 of 4 readers admit 0 of 5 while the control shows export_status and download still admit an ordinary object"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RT8-AC1 (e): 'per production reader ... a test shows objects under GENIBS14SYN or with irpt-synthetic=true are excluded'.",
    "world_is": "An enumerated generation list lapses the moment a new synthetic generation is created -- including one created by the very cell proving the exclusion. The metadata predicate is the half that survives a rename, and it only helps if something writes the metadata.",
    "notes": "Recorded rather than quietly corrected because it is a measurement of the arm's own blind spot: the population an exclusion proof reads is chosen by the prover, and choosing it narrowly is how an exclusion proof passes over the objects it missed."
  },
  {
    "id": "IRPT_BCKEND-W4-S19",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-11T14:05:00Z",
    "one_line": "ROUND 1's RENDERER PRODUCED IDENTICAL CONTENT FROM THREE DIFFERENT BUNDLES, and its arm passed because the arm compared each PDF only to ITSELF. IB-s-14's (v0.11) built three Analysis exports from three DISTINCT bundles -- the battery printed bundle digests 38753e307c2e, 86c38f465c00 and 9f89d01d4fa7 -- and stored three objects. Read back from S3 in round 2: three DIFFERENT raw sha256, ONE normalized content hash (b646b23012...), and an identical decompressed content-stream length of 71,944 bytes. The three PDFs differ only in the creation date and the /ID the print engine stamps; their PAGE CONTENT is byte-identical. So the round-1 fixture renderer's output did not vary with its input, and A RENDERER WHOSE OUTPUT DOES NOT VARY WITH ITS INPUT CANNOT BE EVIDENCE THAT THE INPUT WAS RENDERED. Nothing in that arm could have caught it: each variant was graded on stored-hash-equals-receipt-hash, which is a claim about ONE object, and no arm compared the three to EACH OTHER. This is a measurement about ROUND 1's artifacts, not a defect in round 2 -- IB-rt-8 retires the fixture renderer from the render path (0 render-path modules, 0 of 10 packaged files reference it) for the independent reason that the counterpart's real RenderPackage is the render now.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "3.0.0_SA_CVO -- the finding bears on the GRADE of IB-s-14's (v0.11) arm and on FWD-4/FWD-8, whose proof gap that arm was narrowing; the grader decides what the arm established. The forward remedy belongs to whoever next renders: IB-rtb-1's replay should compare TWO renders of DIFFERENT bundles to each other and require the content hashes to DIFFER, which is the arm nobody has run",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IB-s-14_S14-AC1_battery_output.txt lines 135-148 -- three variants, bundle 38753e307c2e / 86c38f465c00 / 9f89d01d4fa7, three distinct keys, each 'stored hash equal True'",
        "s3api get-object on all three keys under firms/49financial/generations/GENIBS14SYN/attempts/1/exports/ then sha256sum: 9aede5a23bd8889b..., 579b85d087e5babe..., 6954433a9efaecf9... -- three distinct raw digests",
        "render.content_hash() over the same three objects: b646b2301237e6d3 for all three; sizes 41859 bytes for all three",
        "zlib-decompressed content streams of all three: 71944 bytes each, and render.fonts_embedded() returns the same three subsets for each",
        "IRPT_BCKEND.TO-IB-rt-8 arm (b) census @this commit: the fixture renderer is referenced by 0 render-path modules and 0 of 10 packaged files"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "IB-s-14's (v0.11) arm: 'the three retained vendor PDFs are verified by digest and exported as Analysis bundles labelled vendor_synthetic_holdings' -- read as three exports of three inputs.",
    "world_is": "Three exports of three inputs produced ONE rendered document three times. The digest chain was intact end to end for each variant separately, which is exactly why the constancy was invisible: every per-object check passed.",
    "notes": "The general form, and the reason this is worth a row rather than a footnote: a per-member verification cannot see a property the members SHARE. Three arms each asserting 'this object's stored hash equals its receipt's' certify the set clean while the set is one document repeated. The discriminating check is a COMPARISON ACROSS members, and it costs one equality test."
  },
  {
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "disposition": "UNDER_INVESTIGATION",
    "id": "IRPT_BCKEND-W4-S20",
    "surfaced_at": "2026-09-11T15:05:00Z",
    "one_line": "'DELETED' ON A VERSIONED BUCKET MEANS 'HIDDEN FROM EVERY ORDINARY READ', NOT 'THE BYTES ARE GONE' -- and the difference is invisible in the receipt. opal-data-ycharts has versioning ENABLED (get-bucket-versioning: Status=Enabled, read in the same pass as the pre-act inventory). `delete-object` without `--version-id` writes a DELETE MARKER: head-object 404s, list-objects-v2 returns 0, every production reader stops finding the object -- and the four noncurrent versions (wl2x4Z9vSi31..., Jg9agZs3W5xchqyD..., NO5Dioo.m.mOZs4J..., arZTAfWafyUSzIQR...) remain retrievable by VersionId to anyone with s3:GetObjectVersion. The four delete responses SAY SO -- DeleteMarker:true on 4 of 4 -- which is the bucket telling the operator what kind of delete it just performed. The permanent form is a per-version delete, is UNRECOVERABLE, and was NOT taken: the word said 'yes on synthetic exports', and reading a one-line yes as authorization for the irreversible variant of an act is exactly the widening a relay must not do. This row exists so the estate does not later believe those bytes are gone because a report said 'deleted'.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B -- EITHER carry the question back to Andrew (do the noncurrent versions go too, which is unrecoverable), OR record that delete-marker semantics satisfy the intent and close it. Until one of those, any statement that the four synthetic PDFs are 'gone' must carry this qualifier",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api get-bucket-versioning --bucket opal-data-ycharts -> {\"Status\": \"Enabled\"}, read immediately before the act",
        "the four delete-object responses, verbatim: {\"DeleteMarker\": true, \"VersionId\": \"04OM8jGc8DHS0zMtKePd0CBx_XLv7m.s\"} and three siblings -- DeleteMarker true on 4 of 4",
        "the pre-act head-object reads carry the object VersionIds that still exist: wl2x4Z9vSi31.i.TUVq__pjfcz0U4qFK, Jg9agZs3W5xchqyD8bH3UCQTCMQ8Z2HS, NO5Dioo.m.mOZs4JjR2GsZHXKmhI6nVE, arZTAfWafyUSzIQRYcctzEswDuMxmOlv",
        "after the act: head-object 404 on 4 of 4 and list-objects-v2 under the whole GENIBS14SYN/ generation returns 0 objects -- the ORDINARY-read view is empty, which is what every production reader sees",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/RT8-g_delete_receipts.json @this commit -- _meta.delete_grain states this in the artifact itself"
      ]
    },
    "spec_asserts": "Arm (g): 'delete-object per key (four literal keys, never a prefix delete, never --recursive), each response captured; head-object reads 404 on 4 of 4 after'.",
    "world_is": "Both of those happened exactly as written, AND the bytes still exist as noncurrent versions. The arm's own acceptance text is satisfied by the weaker act, so nothing in the criterion would have surfaced the difference.",
    "notes": "The general shape: a delete verb on a versioned store is a VISIBILITY change, and the only instrument that distinguishes it from destruction is the response field nobody reads. Both halves are printed in the battery."
  },
  {
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "disposition": "UNDER_INVESTIGATION",
    "id": "IRPT_BCKEND-W4-S21",
    "surfaced_at": "2026-09-11T15:35:00Z",
    "one_line": "A RENDER ON THE SHARED BROWSER HOST NEEDED A GRANT THAT HOST'S OWN ROOT DOES NOT HAVE, so this cell declared it from ITS root against ANOTHER cell's role. irpt-ycharts-runner-role (IB-s-8, ycharts/iam.tf) grants Secrets Manager on three YCharts names, one DynamoDB lease item, KMS for that table, and the YCharts artifact prefix -- and NOTHING on opal-data-ycharts. A render under that role can neither READ the frozen bundle nor WRITE the PDF, so 'start the host and send the document' would have produced an AccessDenied and nothing else; the README's option A, as written, was not executable. The issuer's amendment permits exactly two edits to the ycharts root (its header and one output description) and 'no other change to that root', so aws_iam_role_policy.render_host_export_evidence is declared in the EXPORT root and attached BY NAME to irpt-ycharts-runner-role. It is additive, reversible (deleting it returns the role to exactly what IB-s-8 declared), scoped to the SAME exports prefix the controller itself uses, and adds NO vendor reach. THE SHAPE IS STILL WORTH A ROW: one role now has two roots writing policies onto it, and a reader of ycharts/iam.tf cannot see the second.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B -- either fold this grant into the ycharts root at the next round (one role, one declaring root) or record the cross-root attachment as the estate's accepted pattern for a shared host. Until then, an IAM census that reads the ycharts root alone UNDERSTATES what that instance role can reach",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/investor-reporting/ycharts/iam.tf @77b2acc7a9 -- aws_iam_role_policy.runner has five statements: three YCharts secrets, the lease item, the system CMK, the YCharts artifact prefix and its conditioned ListBucket. No s3 statement names opal-data-ycharts",
        "infra/aws/terraform/investor-reporting/export/iam.tf @this commit -- data.aws_iam_role.render_host + aws_iam_role_policy.render_host_export_evidence, five statements, all prefix- or ViaService-conditioned",
        "terraform apply on the export root: 'aws_iam_role_policy.render_host_export_evidence: Creation complete after 1s [id=irpt-ycharts-runner-role:irpt-export-render-host-evidence]'",
        "the host then downloaded 3 of 3 files from the export artifact prefix under its instance role, printed by its own 'ls -la /opt/investor-reporting-export' in the SSM output -- the grant is EXERCISED, not merely declared"
      ]
    },
    "spec_asserts": "The amendment: 'no other change to that root'; and the README's option A, which lists start / send / stop and nothing about permissions.",
    "world_is": "The act needed a permission neither the amendment nor the README mentions, on a role this cell does not own. The minimal legal form puts a second writer on one role.",
    "notes": "The operator act was written from the CONTROLLER's side (what the Lambda needs to send) and never from the HOST's side (what the box needs to do the work). That asymmetry is why the gap survived being written out verbatim twice."
  },
  {
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "disposition": "UNDER_INVESTIGATION",
    "id": "IRPT_BCKEND-W4-S22",
    "surfaced_at": "2026-09-11T16:08:00Z",
    "one_line": "THE PORTAL ORIGIN THIS CELL HAS BEEN CARRYING SINCE ROUND 2 IS A HOSTNAME THE ESTATE DOES NOT OWN, and only a browser could find out. local.portal_origin read `https://portal.opalcapital.co`; it is in the export root, in the Lambda's environment as IRPT_PORTAL_ORIGIN, and in the SSM document's parameter. The first real render opened it and Chromium answered net::ERR_SSL_UNRECOGNIZED_NAME_ALERT -- the name is not served, and infra/aws/terraform/website/iam.tf:68 records Andrew-direct 2026-07-13 that the estate does not even own opalcapital.com. The served portal is the portal-auth distribution, aliases opalinvest.dev and www.opalinvest.dev. NOTHING COULD HAVE CAUGHT IT EARLIER BY ITS OWN DESIGN: a controller whose whole job is to pass an origin STRING to a host that is never started cannot discover that the string is fiction, every test asserts the value it was given, and terraform validates a string as a string. The corrected value is applied and the render reached the real origin on the next send.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM command output, verbatim: 'page.goto: net::ERR_SSL_UNRECOGNIZED_NAME_ALERT at https://portal.opalcapital.co/investor-reporting/print?bundle=EXP-184aaa5454d45e8eb6312fe2a175fa01&kind=performance'",
        "infra/aws/terraform/website/iam.tf:68 @77b2acc7a9 -- 'NOT opalcapital.com (Andrew-direct 2026-07-13: \"We do not even own opalcapital.com\")'",
        "infra/aws/terraform/portal-auth/cloudfront-distribution.tf:110 @77b2acc7a9 -- aliases = [\"opalinvest.dev\", \"www.opalinvest.dev\"]",
        "infra/aws/terraform/investor-reporting/export/main.tf @this commit -- portal_origin = \"https://opalinvest.dev\", applied; the next send reached the route and got a sign-in screen rather than a TLS error"
      ]
    },
    "spec_asserts": "The round-2 face: the host 'runs the counterpart's RenderPackage print entry point', served from the portal origin the controller supplies.",
    "world_is": "The origin was a plausible-looking string that resolved to nothing. It sat in a deployed Lambda's environment and in an SSM document for two rounds.",
    "notes": "The class is worth naming: a CONFIGURATION VALUE ONLY USED BY A STEP THAT NEVER RUNS is unfalsifiable by every instrument that does run. The gated arm was not just unproven -- it was hiding a wrong value."
  },
  {
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "disposition": "UNDER_INVESTIGATION",
    "id": "IRPT_BCKEND-W4-S23",
    "surfaced_at": "2026-09-11T16:20:00Z",
    "one_line": "'0 EXTERNAL CONNECTIONS DURING THE RENDER' IS NOT ACHIEVABLE AGAINST THE PORTAL AS BUILT, and the guard is what proved it: 12 requests, opalinvest.dev 10, fonts.googleapis.com 1, fonts.gstatic.com 1 -- 2 FOREIGN of 12, 0 VENDOR of 12. The page the render reached pulls WEBFONTS FROM GOOGLE. That is not a vendor call and it breaches no bound this project carries, but it does falsify the criterion's own phrase, and it connects to the font finding in RT8-AC2: the package DECLARES Lato and the app FETCHES its faces from a third party at render time, so the document's typography depends on an origin outside Opal being reachable. A render host firewalled to Opal origins only -- the obvious hardening -- would render with substituted fonts and no error. The battery now prints the measured figure and refuses to print 'zero'.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "3.0.0_SA_CVO at L9 for the criterion's wording, and IRPT_FNTEND for the substance: either self-host the webfonts (which also fixes the 0-of-3-embedded finding) or the acceptance text becomes '0 VENDOR connections' with the foreign-origin count printed beside it",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the host's own guard line, verbatim: GUARD: {\"requests_total\":12,\"requests_by_origin\":{\"opalinvest.dev\":10,\"fonts.googleapis.com\":1,\"fonts.gstatic.com\":1},\"foreign_origin_requests\":2,\"vendor_requests\":0,\"allowed_origin\":\"opalinvest.dev\",\"denominator\":\"2 foreign of 12 request(s); vendor hosts checked: ycharts.com,api.ycharts.com,bd3.bdreporting.com,api.cloud.orionadvisor.com\",\"outcome\":\"REFUSED\"}",
        "RT8-AC1 (a) verbatim: '0 external connections during the render (host guard log, denominator printed)'",
        "RT8-AC2_judgment.md s.2 -- 0 of 3 declared fonts embedded in 4 of 4 round-1 artifacts; the same typography question from the other end",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/RT8-a_render_record.json @this commit -- network_guard"
      ]
    },
    "spec_asserts": "RT8-AC1 (a): '0 external connections during the render (host guard log, denominator printed)'.",
    "world_is": "2 of 12 requests left Opal, both to Google Fonts, 0 to any vendor. The criterion's number is unreachable against this page; the number it was protecting -- vendor calls -- is zero.",
    "notes": "The guard was moved OFF the success path for this run (it used to write only beside a PDF), which is the only reason this measurement exists: the run that refused is the run where 'what did the page talk to' was most worth knowing."
  },
  {
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "disposition": "UNDER_INVESTIGATION",
    "id": "IRPT_BCKEND-W4-S24",
    "surfaced_at": "2026-09-11T15:10:00Z",
    "one_line": "TWO CELLS' MODULES SHARE ONE NAME ON ONE IMPORT PATH, and `import dispatch` silently answered with the OTHER cell's file. Round 2's IB-rt-2 added infra/aws/lambda/investor-reporting/_authz/dispatch.py beside this cell's export/dispatch.py; the RT8 battery puts both directories on sys.path, the later insert wins, and the import resolved to _authz. THE ATTRIBUTE ERROR WAS THE LUCKY OUTCOME -- the modules happen not to share a symbol, so it crashed on HUMAN_GATED. Had they shared a function name with different semantics, the battery would have measured the wrong module and PASSED. Census of the four directories on that path: 'dispatch' is the only collision today (export has 10 modules, _authz 4, _keys 1). Fixed by loading every export module BY PATH rather than by name; the name collision itself is untouched and belongs to whoever owns the two packages.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B -- the two packages are flat directories deployed into separate Lambda zips, so nothing fails in PRODUCTION today; what is armed is every TEST, battery and tool that puts both on one path. The durable fix is a package namespace (irpt_export.dispatch / irpt_authz.dispatch), which is a cross-cell change",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the battery's traceback, verbatim: AttributeError: module 'dispatch' has no attribute 'HUMAN_GATED', raised at the arm (a) assertion",
        "infra/aws/lambda/investor-reporting/export/dispatch.py @77b2acc7a9 defines HUMAN_GATED at line 40; the module that answered did not",
        "module-name census over the four directories the battery puts on sys.path: export {assets,bundle,dispatch,download,exclusion,handler,identity,package,receipt,render}, _authz {dispatch,enforce,error_path_census,errors}, _authz/tests {fixtures,test_enforce}, _keys {keys} -- intersection with export: ['dispatch'], 1 of 10",
        "battery_ib_rt_8.py @this commit -- _load() resolves by spec_from_file_location, with the incident recorded at the function"
      ]
    },
    "spec_asserts": "Bound 12 and the battery's own docstring: 'THE SUBJECT IS THE REAL ARTIFACT, NEVER A COPY THIS FILE WRAPS'.",
    "world_is": "An import by NAME does not name an artifact. The subject was decided by sys.path insertion order, which is a property of the test harness rather than of the thing being tested.",
    "notes": "Generalisable: bound 12 is usually read as 'do not wrap the subject in a fixture'. This is the same defect through a different door -- the harness silently SUBSTITUTED the subject, and no amount of care about fixtures would have caught it."
  },
  {
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "disposition": "UNDER_INVESTIGATION",
    "id": "IRPT_BCKEND-W4-S25",
    "surfaced_at": "2026-09-11T16:20:00Z",
    "one_line": "THE RENDER IS NO LONGER HOST-GATED AND IS NOW SESSION-GATED: with the host authorized and started, Chromium reached https://opalinvest.dev/investor-reporting/print and the route answered with a SIGN-IN SCREEN, so render_export.cjs refused SESSION_ABSENT and never signed in. Row W4-S14 (nobody may START a host) is DISARMED by Andrew's word of 14:5xZ and by the four measured steps that followed it; what remains is a different gate on a different owner -- the print route is an AUTHENTICATED APP ROUTE and the host needs a session the typed client can use. The README named this fourth dependency before the act ('a session the typed client can use ... a separate operator decision from starting a box'), so it is a confirmed prediction rather than a discovery. Everything else in the chain is now proven END TO END on real infrastructure: the document deployed its own code, node 18 and Chromium 1187 were found on the box, playwright loaded, the browser opened the REAL origin, the network guard measured 12 requests with 0 vendor, and the host returned to stopped.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "IB-rtb-1 (the authenticated replay across every deployed route) -- the amendment names it as the owner of the session. The concrete need: a non-interactive session for a machine principal that the portal's typed client accepts on the print route, OR a print route that accepts a signed, short-lived render grant instead of a user session",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM command output, verbatim: 'BLOCKED: SESSION_ABSENT -- the print route answered with a sign-in screen. This script never signs in; an authenticated session for the host is an OPERATOR ACT.'",
        "the same run's guard line proves the page LOADED before the refusal: 10 requests to opalinvest.dev, 2 to Google Fonts, 12 total",
        "infra/aws/ec2/investor-reporting-export/README.md @77b2acc7a9 -- 'a fourth thing is still missing and is named here so it is not discovered at the console: the print route is an authenticated app route'",
        "the issuer's amendment, which names SESSION-GATED and IB-rtb-1 for exactly this branch",
        "ec2 describe-instances after the cycle: State.Name=stopped, re-read LIVE by the battery's arm (a)"
      ]
    },
    "spec_asserts": "The amendment: 'if the run refuses SESSION_ABSENT, that refusal IS the recorded output -- arm (a) then reads SESSION-GATED naming IB-rtb-1'.",
    "world_is": "Exactly that branch, reached on the first send that got past the infrastructure gaps. The render pipeline is complete except for authentication.",
    "notes": "Four earlier sends in the same authorization each produced a NAMED refusal before this one -- MODULE_NOT_FOUND playwright, MODULE_NOT_FOUND @aws-sdk/client-s3, RENDERER_MODULE_ABSENT, and a TLS error on a hostname the estate does not own. Each was a real gap between a host half that was written and a host it had never run on."
  },
  {
    "id": "IRPT_BCKEND-S37",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-11T18:29:35Z",
    "one_line": "WIND-DOWN COMPLETE FOR THIS SEAT: the last in-flight branch landed. IB-rt-9's wind-down branch (e021ddcdfd, slot ~3) drained at 22f2238cd7 with the order OPEN: arm (a), the v0.9 cutover, passes with 0 failures -- 33,107 files scanned, 4 of 4 code readers of ycharts/session/current migrated or retired, 0 legacy any-non-403 predicates remaining, positive and negative controls on the detector; the probe's negative predicate (wrong on 10 of a 14-case recorded matrix: a 400, 401, 404, 429, 500, a WAF interstitial, a login page, a redirect, a teapot all read as a fresh session) replaced by a positive allowlist plus a fence read; the capture Lambda retired in source with its schedule read DISABLED live. No instance was written (the one-shot sentinel is not burnt on five unbuilt arms) and the acceptance token is absent in every form. TWO DISAGREEMENTS RESOLVED WITHOUT DESTRUCTION: (i) W3-S24 -- slot ~3 measured the 'absent build inputs' premise of the issuer's W2-S21 amendment FALSE at its tip (26 declared, 26 resolve; the 8 outside source_dir are flat-packaged shared libraries), while slot ~2 had measured 7 of 25 and 5 of 7 absent one cut earlier; the drain conflicted on irpt-status's file list (rt-2's list minus the six it removed, plus entry.py; rt-9's list with the shared libraries) and was resolved as the UNION, and both faces now carry the rule 'resolve the way the builder does, print N of N, remove only what resolves NOWHERE'; (ii) W3-S25 -- _scope/resolve.py gained an import whose packaging followed only in the declaration; the rebuild of the three functions shipping it is the successor's first ledgered act. The live probe still runs the retired predicate until IB-rt-9's arm (e) redeploys it. Every worker worktree and branch of this round is removed after its merge was verified an ancestor of the tip; no merge is open; the shared index holds nothing of this seat's.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (the successor session: read the wind-down log, then cold-start rt-2, rt-9, rt-10, rt-6, rt-11, rtb-1 in fresh worktrees)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLOUD 22f2238cd7 (drain wk-irpt_bckend-2-3 @e021ddcdfd; lambda-source-map.json irpt-status entry resolved as the union of both sides)",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/WIP_IB-rt-9_winddown.md; battery_ib_rt_9.py output 'ARM-A-ONLY, INCOMPLETE-UNDER-WINDDOWN'",
        "git worktree list: 0 worker worktrees; git branch: no wk-irpt_bckend-2-* branch"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Andrew-direct 17:1xZ (via 0.0.0_AB_MSTR 95994): workers finish, nothing new starts, log and commit; spine v3 L7: a worker's branch is drained by its issuer and a disagreement between two workers' instruments is resolved by the issuer without destroying either's work.",
    "world_is": "IRPT_BCKEND round 2 at 22f2238cd7: COMPLETE rt-1, rt-3, rt-4, rt-5, rt-7, rt-8 (6 of 12); OPEN rt-2 (guards 0 of 11 unguarded; arms (e),(g) unbuilt), rt-9 (arm (a) of six); pending-unhanded rt-10; staged rt-6, rt-11, rtb-1. No worker is live; no worktree remains; the successor cold-starts every remaining order.",
    "notes": "Seat rows continue at S38. The drain-end read to the CTO (CVO watermark vs channel rows, armed rows not seatable) is the successor's act at round end, not this seat's now: the round is not at its end."
  },
  {
    "id": "IRPT_BCKEND-W3-S26",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T23:39Z",
    "one_line": "The owed ids.py deploy cannot be taken: all THREE roots carry a committed, unapplied handler flip to entry.lambda_handler, and the entry module fails to import in the /var/task layout in 3 of 3 exercised extracts -- an apply that lands the packaging fix also lands a Runtime.ImportModuleError.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "terraform plan (vendored terraform v1.9.8, after init) infra/aws/terraform/investor-reporting/ycharts @a296eac0f4 -> 'handler = \"job.lambda_handler\" -> \"entry.lambda_handler\"', 'Plan: 0 to add, 1 to change, 0 to destroy'",
        "terraform plan infra/aws/terraform/investor-reporting/ops @a296eac0f4 -> 'handler = \"status.lambda_handler\" -> \"entry.lambda_handler\"', 'Plan: 0 to add, 1 to change, 0 to destroy'",
        "terraform plan infra/aws/terraform/investor-reporting/export @a296eac0f4 -> 'handler = \"handler.lambda_handler\" -> \"entry.lambda_handler\"', 'Plan: 0 to add, 1 to change, 0 to destroy'",
        "aws lambda get-function-configuration --query Handler, read live 2026-09-11T23:2xZ: irpt-export-render=handler.lambda_handler, irpt-status=status.lambda_handler, irpt-ycharts-generate=job.lambda_handler -- the flip is DESIRED-not-APPLIED in all three",
        "EXERCISED, not asserted: zip extracted to a flat /var/task dir, imported in a FRESH python3.12 interpreter with the repo stripped from sys.path and a negative control proving an absent module raises -- 'IMPORT-FAIL entry: ModuleNotFoundError: No module named served' for irpt-status (9 of 10 CLOSED), irpt-ycharts-generate (9 of 10) and irpt-export-render with the live irpt-common:5 layer mounted at /opt/python (14 of 15)",
        "static: entry.py top-level imports are served + loaders (both infra/aws/lambda/investor-reporting/_authz/); neither is declared in files[] for ANY of the three functions in infra/aws/lambda/ci/lambda-source-map.json @a296eac0f4, and entry.py itself is declared for 1 of 3 (irpt-status only, via the drain's UNION)",
        "infra/aws/lambda/investor-reporting/ops/entry.py:34-43 -- the sys.path insert that makes entry.py importable IN THE REPO derives _authz from the file's PARENT DIRECTORY, which at /var/task is /var; the module is importable in the tree and not in the runtime, so no in-repo test can see this"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-9 issuer amendment A4 (2026-09-11 ~22:5xZ): 'YOUR FIRST LEDGERED ACT IS THE OWED DEPLOY (row IRPT_BCKEND-W3-S25), AND YOU ARE FIRST IN LINE FOR IT ... Sequencing is ruled: you deploy these three FIRST; slot ~2 is held off them until I confirm your deploy landed.'",
    "world_is": "The two halves CANNOT be sequenced apart. terraform apply is per-ROOT, not per-attribute: any apply that carries the new zip also carries slot ~2's already-committed handler attribute. So deploying the ids.py fix first takes irpt-export-render, irpt-status and irpt-ycharts-generate DOWN at their next cold start, and the ORDER the amendment rules is the reverse of the order the tree permits -- slot ~2's entry.py packaging (entry.py + served.py + loaders.py in files[]) must land in the SAME artifact as any apply of these three roots. No deploy was taken.",
    "notes": "Not fixed here: entry.py, served.py and loaders.py are cell IB-rt-2's, and widening another cell's declared build inputs mid-round is the neighbouring-defect fix this order forbids. The ids.py declaration fix at d3397434d5 stands in the tree and is correct; only its ACTIVATION is blocked. Nothing regressed: the three live functions still serve their older, working bytes, and the import closure of each LIVE zip was re-measured CLOSED under its own live handler (irpt-status 8 of 8, irpt-ycharts-generate 8 of 8, irpt-export-render 13 of 13 with the layer)."
  },
  {
    "id": "IRPT_BCKEND-W3-S27",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T23:39Z",
    "one_line": "irpt-export-render was never ARMED by the ids.py packaging gap: the irpt-common:5 layer already carries python/ids.py byte-identical to the tree's _ids/ids.py, so a rebuild without ids.py reads 13 of 13 CLOSED -- and adding it at /var/task is the second definition that this entry's own note refuses for keys.py.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws lambda get-function-configuration --function-name irpt-export-render --query 'Layers[].Arn' -> arn:aws:lambda:us-east-1:313476888478:layer:irpt-common:5 (irpt-status and irpt-ycharts-generate: None)",
        "layer irpt-common:5 downloaded and listed: python/ids.py 14173 bytes sha256 fc1017b2523f2340... == infra/aws/lambda/investor-reporting/_ids/ids.py 14173 bytes sha256 fc1017b2523f2340... @a296eac0f4 -- IDENTICAL",
        "DIFFERENCE CONTROL in the /var/task + /opt/python layout, fresh interpreter: irpt-export-render rebuilt from the current tree WITHOUT ids.py, layer mounted -> 'import closure in the /var/task layout: 13 of 13 CLOSED'; the same zip WITHOUT the layer -> 'IMPORT-FAIL resolve: ModuleNotFoundError: No module named ids', 10 of 13. The armed reading in W3-S25 is the no-layer reading; the function has a layer.",
        "lambda-source-map.json @a296eac0f4 functions['irpt-export-render'].note: 'keys.py is NOT added: the published irpt-common layer already carries it at python/keys.py, and a second copy at /var/task would shadow the layer's and put two definitions of the key grammar in one runtime.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Row IRPT_BCKEND-W3-S25 and TO-IB-rt-9 amendment A4: the ids.py packaging gap arms irpt-export-render, irpt-status AND irpt-ycharts-generate equally, and the remedy for all three is to add ids.py to files[].",
    "world_is": "The gap is real and armed for irpt-status and irpt-ycharts-generate (0 layers, exercised OPEN at 5 of 8 each on a rebuild). For irpt-export-render it is NOT: /opt/python/ids.py already resolves the import with the same bytes. Adding ids.py to its zip is therefore either a no-op or, the moment the layer and the tree diverge, a SHADOW -- exactly the failure mode the same entry's note cites as its reason for excluding keys.py. The declaration at d3397434d5 adds it anyway.",
    "notes": "Not reverted here: the declaration is committed and the round is frozen; this row records the measurement so the issuer can rule on whether irpt-export-render's ids.py entry stands or comes out. Either way it is not what BLOCKS the deploy -- W3-S26 is."
  },
  {
    "id": "IRPT_BCKEND-W3-S28",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T23:39Z",
    "one_line": "The irpt-common:5 layer's python/keys.py is 21320 bytes and the tree's _keys/keys.py is 29894 -- irpt-export-render deliberately does not package keys.py, so the deployed function runs a key grammar 8574 bytes behind the one every other IRPT function ships flat.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "layer irpt-common:5 python/keys.py 21320 bytes sha256 426196b676fcb268...; infra/aws/lambda/investor-reporting/_keys/keys.py @a296eac0f4 29894 bytes sha256 56ee3cc22e802579... -- NOT equal",
        "layer irpt-common:5 python/raw_keys.json 5990 bytes sha256 702de57727b9c58f... vs infra/aws/lambda/investor-reporting/_ids/raw_keys.json 6064 bytes sha256 82ac2b162ecdb800... -- also NOT equal",
        "layer irpt-common:5 python/firm_registry.json 5094 bytes vs data/firm_registry.json 5229 bytes -- also NOT equal",
        "the LIVE irpt-export-render zip imported in a flat /var/task with NO layer: 'IMPORT-FAIL download: No module named keys' and 'IMPORT-FAIL enforce: No module named keys', 11 of 13 CLOSED -- the dependency on the layer's copy is EXERCISED, not inferred",
        "irpt-status and irpt-ycharts-generate both package keys.py FLAT from _keys/keys.py (29894 bytes, LIVE-MATCH against their S3 artifacts), so two definitions of the key grammar are live across the six IRPT functions today"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "lambda-source-map.json functions['irpt-export-render'].note: excluding keys.py from the zip avoids 'two definitions of the key grammar in one runtime' because 'the published irpt-common layer already carries it'.",
    "world_is": "There are already two definitions, and the layer holds the OLDER one. The note's reasoning is sound and its premise -- that the layer's copy IS the tree's copy -- is false at a296eac0f4 for keys.py, raw_keys.json and firm_registry.json alike. A per-member census of the three functions' zips cannot see this: it is a defect in what they SHARE.",
    "notes": "Out of this cell and not repaired here. Publishing irpt-common:6 is an IMAGE-class act reaching every function that attaches the layer, and the layer is not in this order's <paths>. Surfaced, not chased."
  },
  {
    "id": "IRPT_BCKEND-W3-S29",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T23:39Z",
    "one_line": "Arm (a) does not re-confirm at 4 of 4 in the new worktree: it reads 4 of 5, because battery_ib_rt_9.py became TRACKED when its own branch was drained, and the a1 census (git ls-files) now counts the battery itself as a reader of ycharts/session/current.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "timeout 900 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_rt_9.py on wk-irpt_bckend-2-3b @a296eac0f4 -> 'FAIL a1 readers migrated or retired: 4 of 5' and 'UNACCOUNTED org/missions/.../battery_ib_rt_9.py -- the census found a reader the table does not hold'",
        "the same battery's saved arm-(a) output at deliverables/0.9.0_WK_IRPT_BCKEND~3/IB-rt-9_RT9-AC1_arm_a_output.txt reads 'a1 readers migrated or retired: 4 of 4'",
        "DENOMINATOR line of the new run: '33179 file(s) scanned (git ls-files, tracked) | 62 name the secret | 8 are CODE | 5 of those RESOLVE it | 3 only MENTION it' -- 5 resolvers where the saved run had 4",
        "a2, a3 and a4 are unchanged and all PASS in the same run (0 legacy predicates, 14 of 14, END TO END 400 -> STALE)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-9 amendment A5: 'ARM (a) IS DONE AND MUST NOT BE RE-DONE ... Re-run the battery once to confirm the cutover still passes (~40 s), then leave arm (a) alone.'",
    "world_is": "The cutover itself still passes -- the fifth 'reader' is the battery's own fixture code, which drives fakes and reaches no AWS. What changed is the census POPULATION, not the estate: an untracked file at the first run is a tracked file at this one. The arm is repaired inside this cell (the battery's own deliverable) by classifying the harness explicitly with its own printed count, not by widening the discriminator that already distinguishes a READER from a MENTION.",
    "notes": "Bound 12 in reverse: a battery that CENSUSES the real population will eventually census ITSELF once its own file is committed, and it reports that as a defect in the estate. The tell is that the unaccounted path is under deliverables/."
  },
  {
    "id": "IRPT_BCKEND-W3-S30",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-11T23:39Z",
    "one_line": ".tools/terraform.exe was NOT provisioned in this worktree, contrary to the order's bound 4; resolved by copying the SAME binary by path from the primary workspace (v1.9.8), never a PATH substitute.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ls -l /c/tmp/wk-irpt-2-3b/.tools/terraform.exe -> 'No such file or directory' at worker start",
        "ls -l /c/Users/AndrewBerman/Desktop/ajb_workspace/.tools/terraform.exe -> present, 91104424 bytes",
        "after copy: /c/tmp/wk-irpt-2-3b/.tools/terraform.exe version -> 'Terraform v1.9.8 on windows_amd64'; git check-ignore -q .tools/terraform.exe -> rc 0 (gitignored, so nothing is committed by this)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-9 bounds, item 4: '.tools/terraform.exe is provisioned in your worktree by the issuer -- use it by that path, never a PATH substitute (a substitute re-pins remote state)'; amendment A3 repeats that the absence is a trap already paid for.",
    "world_is": "The binary was absent in /c/tmp/wk-irpt-2-3b. A3 already names the absence as the expected condition, so the bound and the amendment disagree with each other about who provisions it. The remedy taken is the one A3 names -- resolve the binary BY PATH -- using the byte-identical estate binary rather than any terraform on PATH.",
    "notes": "Each of the three investor-reporting roots was then `init`-ed with that binary before any plan, per A3."
  },
  {
    "id": "IRPT_BCKEND-S38",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-12T00:07:11Z",
    "one_line": "ISSUER SELF-CORRECTION, DISARMING W3-S26: my amendment A6 ordered slot ~3 to deploy irpt-export-render, irpt-status and irpt-ycharts-generate ahead of slot ~2 on the reasoning that until IB-rt-2's apply re-points the Terraform handler strings the world runs the OLD handlers, which do not import served/loaders. THAT REASONING WAS FALSIFIED BY THE TREE: IB-rt-2's handler flip is ALREADY COMMITTED AND UNAPPLIED in all three roots, and terraform apply is per-ROOT and not per-attribute, so the apply that lands the ids.py packaging fix also lands the handler flip and the entry module is in no zip. Slot ~3 planned all three roots (0 add, 1 change, 0 destroy, on exactly that attribute), extracted each zip to a flat /var/task and imported it in a fresh python3.12 interpreter with the repo stripped from sys.path with a negative control armed, read IMPORT-FAIL ModuleNotFoundError: No module named 'served' on all three, and REFUSED THE ORDER WITH A BLOCKING ROW RATHER THAN OVERRIDING IT -- the behaviour the row mechanism exists for. RE-CUT: entry.py + served.py + loaders.py + ids.py must land in ONE artifact per function and the apply that flips the handler is the SAME apply that ships them, so the whole packaging-plus-deploy is cell IB-rt-2's across all six roots; the owed W3-S25 deploy is removed from IB-rt-9 and IB-rt-9's arm (e) is now gated on IB-rt-2's apply. Amendment A6 is struck by issuer amendment 2 on the IB-rt-2 face; slot ~2 was handed the re-cut with slot ~3's five measurements attached, and slot ~3 was re-tasked to the four unblocked fixture arms (b), (c), (d), (f).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (disarmed same turn: A6 struck on the face, both slots re-tasked, no seat is waiting on another)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLOUD 670092d321 (drain of wk-irpt_bckend-2-3b; rows W3-S26..S30, channel 137 rows)",
        "IRPT_BCKEND-W3-S26, the worker's BLOCKING row carrying the three plans and the three import failures",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/WIP_IB-rt-9_coldstart2_blocked.md",
        "The struck clause is on the IB-rt-2 face, issuer amendment 1 section A6, committed 7f86d664c6 and merged a296eac0f4"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Issuer amendment 1 section A6 (IB-rt-2 face, a296eac0f4): 'rt-9 deploys those three FIRST. You do NOT deploy them until I tell you its deploy has landed ... until that apply, the world runs the OLD handlers, which do not import served/loaders -- so rt-9's deploy is safe ahead of yours.'",
    "world_is": "The three roots already DESIRE entry.lambda_handler, so no apply on them can be partial. There is no ordering of the two cells that works, because the act is atomic and was split. The issuer's error was reasoning about the WORLD's handler (old, safe) while the DESIRED state in the tree had already moved -- Rule 22's DESIRED-vs-APPLIED distinction applied to the wrong one of the two, inside a sign-off-shaped ruling about what an act MAY touch.",
    "notes": "Recorded as the issuer's own defect rather than the worker's finding, because the worker did exactly what it should have and the cost of the error was one refused act and no deployment. The general form worth carrying to L10: an ISSUER sequencing ruling that names two cells is itself a claim about a shared surface, and a per-cell reading cannot see a defect in what the two cells SHARE -- here, one Terraform root holding both cells' desired state. The ruling should have been graded against the ROOT, which is what both cells have in common, before it was written."
  },
  {
    "id": "IRPT_BCKEND-W3-S31",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-12T00:39Z",
    "one_line": "The deployed generation job has NO eviction outcome: a 401 at the read-back is recorded as SETTINGS_DRIFTED and a 401 at the create as CREATE_NOT_VERIFIED, so an evicted session and a genuine contract failure are indistinguishable in the job's own record -- and the two have OPPOSITE remedies.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED on job.GenerationJob with the replay transport, run_session_suite.py arm d @a2aa857b05: a 401 at GET /model_portfolios/{id}/status yields the job's own why 'SETTINGS_DRIFTED' while transport.decision on the same wire status yields 'REFRESH'",
        "infra/aws/lambda/investor-reporting/ycharts/generate/job.py:426-429 @a296eac0f4 -- `if not read_back['ok']: self._state(job_id, 'ATTENTION', {'why': 'SETTINGS_DRIFTED', ...})`; step_read_back's ok is `info['status'] == 200 and matched == len(rows)`, so ANY non-200 lands on the drifted-settings word",
        "job.py:390-392 -- the same shape at the create step: a non-201 is 'CREATE_NOT_VERIFIED'",
        "comp-find 'resume_allowed' --all: DENOMINATOR 10 hit(s) across 31391 file(s) | 2 DEF, 6 TEST, 2 DOC -- ZERO production callers; the rule at transport.py:202 is exercised only as a pure function by tests/run_offline_suite.py:494,498",
        "the DIFFERENCE CONTROL that makes this actionable: the same step returning 422 classifies NOT_AN_EVICTION with 0 refreshes, so the two cases ARE separable at the wire -- it is the job's outcome word that loses the distinction, not the evidence"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-9 arm (d) and the decomposition v0.2 s.2(4): 'a 401 mid-job triggers ONE refresh through the broker and the job resumes its checkpoint' -- i.e. the deployed job recognises an eviction and routes it to the broker.",
    "world_is": "It does not recognise one. `transport.resume_allowed` has ZERO production callers and `job.py` carries no eviction member in its outcome vocabulary, so the eviction path was a LIBRARY RULE with no wiring. Arm (d) is met by classifying at the wire in the new broker (transport.decision over the recorded status) and re-entering through the job's OWN resume()/after_create(), which required no edit to job.py. The residual hazard is that anything ELSE reading the job's `why` -- an operator, the status envelope, a retry policy -- will refresh a session for a contract failure or fail a request that only needed a refresh.",
    "notes": "NOT fixed inside job.py deliberately: job.py is a declared build input of irpt-ycharts-generate, which cell IB-rt-2 is about to rebuild and deploy (row W3-S26), and editing it here would put this cell's change into that cell's artifact. The broker classifies correctly without touching it. Whether job.py should gain an EVICTED outcome is a cut-time question, not a mid-round one."
  },
  {
    "id": "IRPT_BCKEND-W3-S32",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-12T00:39Z",
    "one_line": "JobStore keeps only the LATEST state per job, so the durable `model_portfolio_id` written at SUBMITTED is ERASED by the next transition -- the checkpoint a recovery reads back no longer carries the identity of the vendor object the request already created.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/ycharts/generate/job.py:121-124 @a296eac0f4 -- `put_state` assigns `self.items[job_id] = {...}`, one row per job, overwritten in place; only `self.transitions` is append-only and it carries job_id + state and NO detail",
        "EXERCISED, run_session_suite.py arm d: after the create succeeded (state SUBMITTED, detail {'model_portfolio_id': 2332060}) and the read-back returned 401 (state ATTENTION, detail {'why','drifted'}), the broker's checkpoint read returned `checkpoint_state_at_recovery: ATTENTION` -- the portfolio id was gone",
        "the recovery still worked, and that is the point: it worked because job.resume() RECONCILES the owned object from the VENDOR by the deterministic portfolio name, not because the store remembered it"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The job's own design note at job.py:102-110: the store is 'durable job state with a CONDITIONAL intent claim ... the shape it mirrors is irpt-jobs', and the chain writes SUBMITTING/SUBMITTED with the identity of the object it is about to create or has created, so a restarted worker can find it.",
    "world_is": "The identity written at SUBMITTED does not survive one further transition. Nothing in this cell depends on it -- reconciliation from the vendor by owned identity is the stronger design and it is what actually recovers -- but any future consumer that reads the checkpoint DETAIL for a portfolio id will find whatever the last transition wrote, and a DynamoDB-backed JobStore with the same put shape would have the same erasure.",
    "notes": "Surfaced, not chased: job.py is IB-rt-2's artifact this round (W3-S26). The remedy, if one is wanted, is a per-(job, state) row or an append-only detail log, which is a store-shape decision and belongs at a cut."
  },
  {
    "id": "IRPT_BCKEND-W3-S33",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-12T00:39Z",
    "one_line": "The arm-(a) reader census caught this cell's OWN new broker before it was declared -- 4 of 5, UNACCOUNTED -- which is the table working; recorded because it is the second time in one session that adding a file to the tree moved this arm's denominator.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "battery_ib_rt_9.py run before broker.py was declared: 'UNACCOUNTED infra/aws/lambda/investor-reporting/ycharts/session/broker.py -- the census found a reader the table does not hold' and 'FAIL a1 readers migrated or retired: 4 of 5'",
        "after the declaration: 'PASS a1 readers migrated or retired: 5 of 5', denominator '33184 file(s) scanned (git ls-files, tracked) | 64 name the secret | 10 are CODE | 6 of those RESOLVE it | 4 only MENTION it | 1 ... OWN TEST HARNESS'",
        "the earlier instance is row IRPT_BCKEND-W3-S29 (the battery counting itself once its own file became tracked)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-9 amendment A5: arm (a) is DONE and stays done -- 're-run the battery once to confirm the cutover still passes, then leave arm (a) alone'.",
    "world_is": "Arm (a) is not a fixed result; it is a LIVE census whose denominator moves whenever the cell adds a file that resolves the secret. Twice in one session it failed for a correct reason and was answered by declaring the new member rather than by widening the discriminator. Both answers are recorded in the battery beside the entries they explain. This is the arm behaving as specified -- the record exists so a later reader does not mistake a moving denominator for an unstable instrument.",
    "notes": "The discriminator (a Secrets Manager READ API call) was NOT touched in either case. The only structural exclusion is the HARNESS class, which carries its own control asserting it removed 0 declared estate readers."
  },
  {
    "id": "IRPT_BCKEND-S39",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-12T01:01:01Z",
    "one_line": "DISPOSITION of W3-S31 and W3-S32. W3-S31: the worker declined to wire resume_allowed into job.py on the stated premise that job.py is IB-rt-2's artifact this round. THAT PREMISE IS FALSE AND THE DECISION WAS STILL RIGHT. Measured at the merge-base of wk-irpt_bckend-2-2b: that branch touches 18 files and job.py is not among them -- IB-rt-2 creates entry.py per function and deliberately leaves every wrapped handler module untouched, which is its own standing rule. The real reason not to touch it is one neither cell stated: job.py ships inside the irpt-ycharts-generate ZIP and the ycharts Terraform ROOT, and BOTH are IB-rt-2's and are being applied right now under an open deploy ledger (org/critical_paths/.open_deploys/irpt-bckend-rt2.json, entry 20260912T0035Z). An edit landing mid-deploy would ride into or miss that artifact non-deterministically. THE SHARED SURFACE IS THE ARTIFACT, NOT THE FILE -- a file-ownership reading says 'free' and the artifact reading says 'do not touch', and the artifact reading governs. RULING: resume_allowed is NOT wired this round; the round is FROZEN under Rule 27 and a cell for it is L10's business, carried with its measurement (10 hits across 31,391 files, ZERO production callers -- the rule existed with no wiring). AND A JUDGMENT FLAG FOR 3.0.0_SA_CVO AT L9, NOT GRADED HERE: arm (d) PASSES on fixtures while production has no eviction path at all, so whether fixture-passing satisfies the PRD's 'eviction and self-healing on the generation job' is a judgment criterion and belongs to the adjudication, never to the instance's own verdict. W3-S32: accepted as an OBSERVATION with no act this round -- JobStore keeping only the latest state per job means the model_portfolio_id written at SUBMITTED is erased by the next transition, and the recovery works anyway because resume() reconciles from the VENDOR, which is the stronger design; carried to L10 so the PRD STATES the vendor reconciliation rather than leaving a reader to infer it from a checkpoint that does not hold it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (both rows disarmed same turn: no act is owed this round and each is carried to L10 by name)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git diff --name-only $(git merge-base CLOUD wk-irpt_bckend-2-2b) wk-irpt_bckend-2-2b -- 18 files, job.py absent",
        "org/critical_paths/.open_deploys/irpt-bckend-rt2.json and org/critical_paths/change_management/20260912T0035Z_irpt-bckend-rt2_deploy_completion.md -- IB-rt-2's deploy is OPEN at this write",
        "IRPT_BCKEND-W3-S31 and IRPT_BCKEND-W3-S32, drained at bad394fbaa (channel 141 rows)",
        "IB-rt-2 face, WIP section 6.2: the guard is a new entry module per function and the wrapped handler modules are deliberately untouched"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "IRPT_BCKEND-W3-S31: 'Not fixed in job.py: it is IB-rt-2's artifact this round, and editing it would put my change into slot ~2's artifact.'",
    "world_is": "IB-rt-2 does not edit job.py and never intended to. But it DOES build the zip and apply the root that carry job.py, and it holds an OPEN deploy ledger on them at this moment -- so the conclusion the worker reached is correct while the reason it gave is not. The correct reason is stronger, because it still forbids the edit after IB-rt-2's file set is known and a file-ownership reading would have permitted it.",
    "notes": "Second instance tonight of one class, and the first was this seat's own (S38): A CLAIM ABOUT WHO MAY TOUCH A FILE IS A CLAIM ABOUT THE ARTIFACT AND THE TERRAFORM ROOT THAT CARRY IT, NOT ABOUT THE FILE. In S38 the issuer read two cells' file sets and missed that one root held both cells' desired state; here a worker read one cell's file set and missed that one zip carries both cells' code. Same shape, opposite seats, same remedy: grade the SHARED artifact before ruling on the member. Carried to L10 as one finding with two instances rather than two findings."
  },
  {
    "id": "IRPT_BCKEND-W4-S26",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-12T00:22:27Z",
    "one_line": "THE FI-LIGATURE CODES ARE NOT RECOVERABLE FROM THESE DOCUMENTS AND THE RIGHT ANSWER IS THE RULING'S SECOND BRANCH. The TO's arm (a) reads 'the fi ligature is recovered through that document's map (the code used printed per document: 45 / 45 / 46 as measured)'. Measured on all three retained vendor specimens: the code is real and the face's numbers are exact (overview 45, comparison 45, multicomp 46, each rendered by exactly ONE font resource, on 23 of 23, 31 of 31 and 35 of 35 pages), but NO resource of the document states it. Each document's ToUnicode CMap has a GAP at precisely that code -- the overview's RobotoCondensed-Regular subset maps bfranges 1..44 and 46..87 and the content stream renders 45; the multicomp's maps 1..45 and 47..88 and renders 46 -- and every embedded subset carries only OS/2, glyf, head, hhea, hmtx, loca, maxp and name: no cmap table and no post table, so the font PROGRAM states nothing either. Both sources were asked per font and the exhaustion is recorded on the row. So the cell implements the CTO's ruling as it is written -- 'Per-document font mapping OR explicit unresolved for the fi-ligature codes 45/46' -- and takes the second disjunct, printing UNRESOLVED with the document's own evidence rather than recovering a letter the document does not state. THE ONLY WAY TO PRINT 'RECOVERED' HERE WOULD HAVE BEEN TO GUESS: the negative control measures what each guess would have cost. Resolving the same code through the SAME DOCUMENT'S other font resource returns U+0038 in the overview, U+004D in the comparison and U+0044 in the multicomp -- three different confident wrong characters -- and across the three documents 73 of 89 compared codes already mean different characters, so a global table is wrong on 82 percent of the codes it would cover.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "battery_ib_rt_10.py arm (a), verbatim: 'CODE 45   UNRESOLVED  rendered by ['QXFAAA+RobotoCondensed-Regular'] on 23 of 23 page(s)' and 'the shape of the hole in this font's own map: {\"codes_mapped\": 87, \"lowest\": 0, \"highest\": 87, \"nearest_below\": 44, \"nearest_above\": 46, \"note\": \"the code sits in a GAP of this font's own map\"}'",
        "the same arm's cross-font control: '1 of 2 other font resource(s) in this document would have returned a character for this code' with QHGAAA+RobotoCondensed-Bold would_answer=True U+0038",
        "the raw ToUnicode streams, read with pdfminer's own CMap parser: overview F6 declares '<0001> <002C>' and '<002E> <0057>'; multicomp F6 declares '<0001> <002D>' and '<002F> <0058>'",
        "infra/aws/lambda/investor-reporting/ycharts/extract/fonts.py@56a6e07e8f -- resolve_code() asks the ToUnicode CMap and then the embedded program's cmap and post tables, scoped to the font that rendered the code, and records the exhaustion",
        "ROUND_ANALYSIS.round1.md@0d57ceb2f9 ruling 6, verbatim: 'Per-document font mapping or explicit unresolved for the fi-ligature codes 45/46'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO IB-rt-10 arm (a): 'For each of the 3 vendor PDFs the fi ligature is RECOVERED through that document's map (the code used printed per document: 45 / 45 / 46 as measured)'.",
    "world_is": "The codes and their per-document assignment are exactly as the face measured, and each is rendered by exactly one font resource -- but no resource of any of the three documents maps them, so RECOVERED is unreachable without a guess and the answer is the ruling's explicit UNRESOLVED. The arm is graded on the ruling's disjunction, with the code, the font, the gap, the sources asked and the cost of each available guess all printed.",
    "notes": "The ruling that this cell executes admits both branches; the TO's prose gloss of it names only the first. The gloss and the ruling are not in conflict about what to DO -- both forbid a global table -- but a reader of the battery output who had only the gloss would expect a recovered character, so the branch taken is stated on the arm and here. The form of the finding is a spec-vs-world mismatch; its significance is 3.0.0_SA_CVO's at L9."
  },
  {
    "id": "IRPT_BCKEND-W4-S27",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-12T00:22:27Z",
    "one_line": "CONTRACT ADDITION, FOR THE CTO'S L10 READ: an OPTIONAL `date_claim` enum (SECTION | REPORT | NONE) is now a property of AnalysisReport.sections[] in BOTH published copies -- infra/aws/lambda/investor-reporting/_contracts/AnalysisReport.schema.json and docs/contracts/investor-reporting/v1/AnalysisReport.schema.json -- added by this cell on the decomposition's own instruction (v0.2 s.2) even though the contract surface belongs to IB-s-18. The property is OPTIONAL and never required, exactly as `contract_version` is: the section item is additionalProperties:false and round-1 instances predate it, so requiring it would invalidate documents that are already correct. The block is byte-identical in both copies (1370 bytes, sha256 92bff92c879fa6c8) because it was written once and inserted into both, and its description quotes the PRD CONTRACTS table item 3 of 6 verbatim at 62301f71e0. WHAT THE CTO IS BEING ASKED TO READ: whether an optional producer-side enum is the right carrier for 'whose date is this', or whether the FNTEND consumer needs it REQUIRED to be able to refuse a report-level date rendered as a section date -- this cell cannot decide that without widening beyond its own surface. A consumer effect is graded at IB-rtb-1; nothing is deployed by this cell.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "IRPT_BCKEND_DECOMP.md v0.2 s.2, verbatim: 'proposed to the contract as an OPTIONAL enum so additionalProperties:false holds (the contract edit is IB-s-18's surface: this cell adds the optional property to _contracts/AnalysisReport.schema.json and the v1 artifact in the same commit, with the CONTRACTS-table citation, and files a row naming the CTO's L10 read on it)'",
        "battery_ib_rt_10.py arm (d), verbatim: '2 of 2 published copies carry 'date_claim', byte-identical: True' with lambda and published_v1 both 1370 bytes at sha256 92bff92c879fa6c8",
        "the same arm: seven specimens validated against BOTH copies (71, 91, 118, 16, 23, 30 and 4 rows), additionalProperties:false intact",
        "battery_ib_s_18.py arm (a) re-run after the edit: 'TOTAL: 385 of 385 description quote(s) resolve VERBATIM in the CONTRACTS section at 62301f71e0'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Decomposition v0.2 s.2 directs this cell to add the optional property to both contract artifacts in one commit and to file a row naming the CTO's L10 read on it; TO bound 7 otherwise holds this cell off surfaces it does not own.",
    "world_is": "The property is added to both copies, byte-identical, optional, and validated on seven specimens. The open question the CTO reads at L10 is whether OPTIONAL is the right strength for a field whose whole purpose is to let a consumer REFUSE, given that an optional field a producer may omit is one a consumer cannot rely on.",
    "notes": "The first draft of the description wrote the PDF's own heading as a double-quoted span, which battery_ib_s_18.py arm (a) correctly reads as a claim to quote the PRD verbatim and refused as the 1 of 386 that did not resolve. The prose was re-worded; the checker was not touched. Worth recording because the checker's rule -- every double-quoted span in a contract description IS a PRD quote -- is not stated anywhere a later author of a description would see it."
  },
  {
    "id": "IRPT_BCKEND-W4-S28",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-12T00:22:27Z",
    "one_line": "THE ROUND-1 EXTRACTOR DATED ROWS FROM A NEIGHBOURING BLOCK AND FROM A DIFFERENT DOCUMENT, AND ITS OWN CERTIFICATION READ CERTIFIED THROUGHOUT. Re-derived from this run's rows by extract.round1_undated_baseline(): on the retained overview specimen 15 of 61 emitted rows sit on a page that prints TWO different Data-as-of dates (page 2 carries 2026-09-09 and 2026-09-11; page 6 carries 2026-08-31 and 2026-09-11), and round 1's rule took the page's FIRST date line for every row on the page -- so those 15 rows carried whichever date came first in the text stream, which for a stale-priced block is the fresher date. On the multicomp specimen a further 12 of 108 rows were dated CENSUS_STATED: a date read from docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json, which is a DIFFERENT DOCUMENT'S statement about this one. NONE OF THIS WAS VISIBLE TO ROUND 1'S CERTIFIER, and that is the structural point rather than the incident: its three legs graded value-at-coordinates, label-in-neighbourhood and unit-declared, and a date is at NONE of those coordinates -- it is at the block heading's. Every one of the 15 rows passed all three legs, because each was individually correct about everything the legs could see. IB-rt-10 adds the fourth leg that can see it and two mutants that exercise it; the round-1 counts are reproduced exactly (comparison 34 of 81, multicomp 51 of 108) so the change is a measured delta and not a recollection. Source-only: nothing is deployed by this cell and the extractor rides the generate package's next build.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "IB-rtb-1 (the deployed-route replay) -- the corrected extractor reaches a running function only at the irpt-ycharts-generate package's next build, so until that build any deployed caller of ycharts/extract still applies the page's first date line and the census date. The disarming act is that rebuild plus a read of the served CodeSha256 against the built zip; no separate remediation is needed, because the fix is already in source at 56a6e07e8f.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "battery_ib_rt_10.py arm (c), verbatim: 'and on the overview specimen 15 of 61 emitted rows sit on a page printing TWO different 'Data as of' dates'",
        "the same arm: 'multicomp  51 of 108 section row(s) undated under the round-1 rule | by round-1 claim {\"PAGE_STATED\": 45, \"CENSUS_STATED\": 12, \"NOT_STATED\": 51}'",
        "the same arm: 'pages printing >1 distinct date: {\"2\": [\"2026-09-09\", \"2026-09-11\"], \"6\": [\"2026-08-31\", \"2026-09-11\"]}' for the overview specimen",
        "IRPT_BCKEND.TO-IB-s-10...proof_of_spec.json in deliverables/0.9.0_WK_IRPT_BCKEND~3/ -- the round-1 instance whose battery reported every vendor specimen fully CERTIFIED under three legs",
        "infra/aws/lambda/investor-reporting/ycharts/extract/certify.py@56a6e07e8f -- the L4 date-provenance leg and the neighbour-date and shifted-provenance mutants, both of which refuse on the overview and comparison specimens"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO IB-rt-10 arm (c): '0 items dated from a neighbour (a mutant that copies a neighbour's date FAILS the arm)', and the CTO's ruling on W3-S11: undated sections are represented with document provenance, never inferred from a neighbour.",
    "world_is": "0 of the rows this cell emits are dated from a neighbour and both mutants are refused -- but the rows the PREVIOUS round emitted were, on 15 of 61 overview rows and 12 of 108 multicomp rows, and that round's certifier had no leg that could have seen it. The defect is fixed in source here; what is ARMED is the window until the package that carries the extractor is rebuilt.",
    "notes": "Recorded as a structural finding about CERTIFICATION SCOPE rather than as a defect report: a certifier's legs bound what its verdict can mean, and 'N of N CERTIFIED' read clean across three specimens while a whole class of error sat outside every leg. The worker judges the form of this row; its significance is 3.0.0_SA_CVO's at L9."
  },
  {
    "id": "IRPT_BCKEND-W4-S29",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-12T00:22:27Z",
    "one_line": "THE PATH REGISTER'S OWN VERIFIER CANNOT COMPLETE, AND THIS CELL APPENDS TO THAT REGISTER. battery_ib_s_18.py -- the battery that grades infra/aws/lambda/investor-reporting/PATH_MANIFEST.json, the register every later cell is told to append to -- raises TypeError at line 315 in arm (c), '<' not supported between instances of 'NoneType' and 'str', sorting a presence breakdown whose keys include None. Measured cause: 127 of the manifest's 377 entries carry no presence_at_base at all (the field is `recommended` and not `required` by the manifest's own append_contract), so the breakdown dict has a None key and sorted() refuses it. Arms (a) and (b) run and pass before the crash; arms (d) and (e) never run, and the battery exits rc 1 with no verdict line -- so a reader who checks only the exit code sees a FAILURE and one who reads the last printed arm sees a PASS. PRE-EXISTING, NOT INDUCED: PATH_MANIFEST.json is byte-unmodified in this worktree (git status --porcelain returns nothing for it), so the crashing input is identical to the base tree's. NOT THIS CELL'S TO FIX -- battery_ib_s_18.py is 0.9.0_WK_IRPT_BCKEND~1's deliverable and is outside this order's paths. This cell's own appended entries carry presence_at_base, so they do not add to the 127.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B, to route to whichever order owns deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_s_18.py (IB-s-18's re-run, or IB-rtb-1 if the path register is graded there). The concrete fix is one line -- sort the breakdown on str(key), or default the missing field -- but the reason to disarm it is not the line: while arm (c) crashes, arms (d) and (e) of the FOUNDATION cell's acceptance have not run at all, on any commit since the 127 entries were appended, and no reader of the rc can tell that apart from a failing assertion.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "battery_ib_s_18.py run at 56a6e07e8f, verbatim: 'File \"C:\\tmp\\wk-irpt-2-4b\\org\\missions\\D9\\IRPT\\IRPT_BCKEND\\deliverables\\0.9.0_WK_IRPT_BCKEND~1\\battery_ib_s_18.py\", line 315, in arm_c / for k in sorted(breakdown): / TypeError: '<' not supported between instances of 'NoneType' and 'str'', rc 1",
        "the same run's last completed line: '44 of 44 entry(ies) claiming PRESENT_AT_PIN verify with `git cat-file -e 261c8d2080:<path>`'",
        "a Counter over PATH_MANIFEST.json's own entries: 377 entries, presence_at_base None on 127 of them (the remainder spread over 11 declared values)",
        "git status --porcelain infra/aws/lambda/investor-reporting/PATH_MANIFEST.json -- empty, so the crashing input is the base tree's bytes",
        "PATH_MANIFEST.json _meta.append_contract: presence_at_base is listed under recommended_fields, never required_fields"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO IB-rt-10 lists infra/aws/lambda/investor-reporting/PATH_MANIFEST.json in its paths, and the manifest's own append_contract directs every later cell to append its concrete read/write paths; bound 7 and the lane clause forbid this cell from editing anything its paths do not name.",
    "world_is": "The register is appendable and this cell appends to it, but the battery that grades the register crashes part-way through on data the register already contains, so there is no instrument that can currently certify the append. This cell reports the crash rather than repairing another worker's battery.",
    "notes": "The shape is worth more than the line: a verifier that dies mid-run leaves clean metrics printed ABOVE the traceback, so the output reads as three passing arms and the failure is only in the exit code. Two readers of the same run reach opposite conclusions depending on where they stop."
  },
  {
    "id": "IRPT_BCKEND-W4-S30",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-12T00:22:27Z",
    "one_line": "THE PATH REGISTER'S OWN PRINTED DENOMINATOR WAS STALE BY 41. infra/aws/lambda/investor-reporting/PATH_MANIFEST.json declared _meta.denominators.entries_total = 336 while its `entries` array held 377 -- a 12 percent understatement, in the one field a reader would quote as the register's size. The declared value is consistent with _meta.denominators.appended_by_cell, which records IB-s-17 (24) and IB-rt-1 (28) and nothing after: cells that appended later added entries without touching either counter, which the manifest's own append_contract does not ask them to. This cell wrote the MEASURED count (382 after its 5) rather than incrementing the stale one, because 341 would have been a fresh wrong number carrying the authority of having just been updated. The class matters more than the 41: a denominator that is printed is READ AS MEASURED, and a register whose size is quoted from _meta rather than counted from `entries` reports 336 with no visible sign of being wrong. Nothing else in _meta was touched, and no existing entry was moved -- verified by comparing the parsed arrays before and after the append, not by reading the diff.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PATH_MANIFEST.json at 56a6e07e8f, _meta.denominators, verbatim: '\"entries_total\": 336'",
        "len(json.load(...)['entries']) over the same bytes: 377",
        "_meta.denominators.appended_by_cell at the same commit: {'IB-s-17': 24, 'IB-rt-1': 28} -- no key for any cell after IB-rt-1",
        ".scratch/append_manifest2.py run output, verbatim: 'NOTE: entries_total declared 336, array holds 377 before this append; writing 382'",
        "the same run: 'OK: entries 377 -> 382' with git diff --stat reporting 67 insertions and 1 deletion on the register"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PATH_MANIFEST.json _meta.append_contract: 'append only; one entry per concrete path'; _meta.denominators.entries_total is published as the register's size and Rule 22's COVERAGE axis requires a printed denominator to be the one that was measured.",
    "world_is": "The published total had drifted 41 below the array it describes, and the append_contract names no owner for keeping it true, so every append since IB-rt-1 left it further behind. This cell wrote the measured value and recorded the drift rather than absorbing it.",
    "notes": "Filed separately from IRPT_BCKEND-W4-S29 rather than folded into it: S29 is about the register's VERIFIER crashing, this is about the register's own published COUNT being wrong. Different owners and different remedies -- and the channel is append-only, so an existing row could not have carried it."
  },
  {
    "id": "IRPT_BCKEND-W4-S31",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~4",
    "surfaced_at": "2026-09-12T00:52:00Z",
    "one_line": "A HAND-BUILT PDF IS TEXT TO GIT, AND THE FRESH-WORKTREE FAILURE IS A HASH CHANGE ON A FILE NOBODY EDITED. git decides binary-vs-text on whether a NUL byte appears in the first 8 KB, and a PDF is not required to carry one: measured, the three round-1 synthetic specimens carry a NUL in 3 of 3 cases (their content streams are deflated) while this cell's hand-built unmapped_glyph.pdf carries one in 0 of 1 -- it has uncompressed content streams, so every byte is ASCII. With core.autocrlf=true on this box, a fresh checkout renders it CRLF: 3,024 bytes become 3,121 and the sha256 moves from f15b39103fc9f5a7 to 76a7ddc5ad775756. THE DANGEROUS PART IS THAT NOTHING CRASHES -- the CRLF copy still opens and still extracts both pages, because pdfminer reconstructs the xref when the offsets do not resolve. What fails is the fixture manifest's freshness check, in every worktree except the one that generated the file, for a file nobody touched. The standard PDF binary marker the generator writes (four high-bit bytes in a comment after the header) is correct PDF practice and does NOT satisfy git's heuristic, because high bits are not NUL -- so it was necessary and not sufficient. Remedied inside this order's own granted subtree with infra/aws/lambda/investor-reporting/ycharts/extract/.gitattributes declaring '*.pdf -text'; the estate's ROOT .gitattributes is not this cell's to edit and a fixture's binary-ness is a fact about the fixture rather than a repo-wide policy. Verified after: git check-attr reports 'text: unset' for both the new fixture and the round-1 specimens.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit output at 98d579cd1b, verbatim: 'warning: in the working copy of 'infra/aws/lambda/investor-reporting/ycharts/extract/fixtures/unmapped_glyph/unmapped_glyph.pdf', LF will be replaced by CRLF the next time Git touches it'",
        "a NUL census over the fixture PDFs: synthetic_pdf/{overview,comparison,multicomp}.pdf carry a NUL in the first 8000 bytes 3 of 3; unmapped_glyph/unmapped_glyph.pdf 0 of 1",
        "the simulated checkout, run rather than reasoned about: the HEAD blob with every LF replaced by CRLF is 3,121 bytes at sha256 76a7ddc5ad775756 against the manifest's declared f15b39103fc9f5a7 / 3,024 bytes, AND pdfplumber opens it: '2 pages; page2 text: SYNTHETIC SPECIMEN: generated from the field census'",
        "git check-attr -a after the fix: both unmapped_glyph.pdf and synthetic_pdf/overview.pdf report 'text: unset'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO IB-rt-10 names infra/aws/lambda/investor-reporting/ycharts/extract/ in its paths and directs this cell to add the unmapped-glyph fixture there; the fixture manifest is re-derived from disk by the battery on every run (row W3-S9), which presumes the checked-out bytes are the committed bytes.",
    "world_is": "For a PDF with no NUL in its first 8 KB that presumption does not hold on an autocrlf box, and the failure surfaces as a hash mismatch in a worktree that did nothing wrong rather than as anything resembling a corrupt file. A .gitattributes the order did not name had to be written -- inside the subtree the order does grant -- which is why this is a row rather than a silent fix.",
    "notes": "Recorded for the CLASS, which is not specific to this project: any hand-built or uncompressed binary-format fixture committed on an autocrlf box has this property, and the tell is a hash check that fails everywhere except where the file was made. The estate already carries the neighbouring lesson for hash-pinned TEXT assets; this is the same trap reached from the other direction, by a file that is binary in intent and text by measurement."
  },
  {
    "id": "IRPT_BCKEND-S40",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-12T01:18:42Z",
    "one_line": "DISPOSITION of IB-rt-10's six rows at its COMPLETE. W4-S28 IS THE ONE THAT MATTERS AND IT STAYS ARMED: round 1 dated 15 of 61 overview rows and 12 of 108 multi-comparison rows from a NEIGHBOURING block, and ALL of them passed ALL THREE of round 1's certification legs -- because a date sits at none of the coordinates those legs inspect. That is not a row about dates, it is a row about CERTIFICATION: a certification that does not inspect the coordinate where the defect lives passes it every time, and round 1's three legs returned GREEN over 27 wrong values. Disarm owner stays IB-rtb-1's rebuild, which is the act that re-derives those rows; carried to L10 as a ROUND-1 defect with its denominators, because anything round 1 certified on the same legs inherits the same blind spot and nobody has enumerated what else that covers. W4-S29 ROUTED, and it is mine: battery_ib_s_18.py crashes mid-run in arm (c). IB-s-18 is a round-1 cell already CLOSED, so under Rule 27 I am not re-opening it mid-round and IB-rt-10 was right not to touch another cell's deliverable. THE CONSEQUENCE IS THE FINDING, not the crash: IB-s-18's acceptance CANNOT BE RE-EXERCISED TODAY, so any claim resting on that battery is currently NOT-RE-VERIFIABLE rather than verified -- carried to 1.0.0_SA_CTO at L10 to decide whether it re-opens. W4-S26 ACCEPTED AS THE MEASURED ANSWER: the fi-ligature codes are NOT recoverable -- every ToUnicode CMap has a gap at exactly that code and no embedded subset carries a cmap or post table -- so the CTO ruling's SECOND branch ('or explicit unresolved') is what the world supports. The face's arm (a) prose said 'recovered' and the world does not permit it; the face is the defect, not the result, and that goes to L10. W4-S27 (the OPTIONAL date_claim enum) carried to the CTO's L10 read as the row itself asks. W4-S30 and W4-S31 INERT and accepted: a path register whose printed denominator was stale by 41 (336 declared against 377 actual), and a hand-built PDF that git treated as TEXT so a fresh checkout changed its hash -- the second already fixed in-cell by declaring the fixtures binary.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (this disposition row itself is INERT; W4-S28 REMAINS ARMED under IB-rtb-1's rebuild and W4-S29 is carried to 1.0.0_SA_CTO at L10 -- neither is disarmed by this row and neither is silently dropped)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLOUD 08962bd2ea (drain of wk-irpt_bckend-2-4b; rows W4-S26..S31, channel 148 rows)",
        "proof-of-spec-check.py re-run by the issuer at HEAD over IB-rt-10's instance: VALID (rc=0), 13 artifact rows, 6 surprise entries all resolving",
        "IB-rt-10 face <status> complete: RT10-AC1 PASS-by-output, RT10-AC2 RECORDED without a self-verdict",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/RT10-AC2_judgment.md"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "IB-rt-10's face, arm (a): text recovered through each document's actual font mapping. And the CTO's round-1 ruling: 'per-document font mapping OR EXPLICIT UNRESOLVED for the fi-ligature codes 45/46'.",
    "world_is": "Recovery is not available at all for those codes: the CMaps have a gap at exactly the code and the embedded subsets carry no cmap or post table. The ruling anticipated this and the face did not. The worker also caught its OWN first version resolving the code through whichever of that document's other fonts mapped it, returning a confident wrong character -- U+0038, U+004D and U+0044, one per document. THE UNIT OF A GLYPH MAP IS THE FONT RESOURCE, NOT THE DOCUMENT.",
    "notes": "Third instance tonight of one class, now across three different seats: S38 (issuer, one Terraform root holding two cells' desired state), S39 (worker, one zip carrying two cells' code), and W4-S28 here (a certification whose legs do not read the coordinate the defect occupies). All three are the same failure: A CHECK SCOPED TO THE MEMBERS CANNOT SEE A DEFECT IN WHAT THE MEMBERS SHARE, or in a coordinate no member's check inspects. Rule 22 states it; three seats hit it in one round anyway, which is the argument that it belongs in the L6 issuance language where a cut is made, not only in a rule everyone has already read. Carried to L10 as ONE finding with three instances."
  },
  {
    "id": "IRPT_BCKEND-S41",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-12T01:34:46Z",
    "one_line": "THE AUTHORIZED PER-VERSION DELETE WAS NOT TAKEN, AND NOT TAKING IT IS THE ACT. Andrew approved (via 1.0.0_SA_CTO 96041, 'All recs approved') the per-version delete of 'the FOUR noncurrent versions of the FOUR synthetic-export objects named in row W4-S20', with 1.0.0_SA_CTO naming the boundary explicitly: NOT any other version of those four keys beyond the four the row names, and STOP rather than reconcile if the row's four VersionIds do not resolve as expected. The pre-act live read (s3api list-object-versions over the exports/ prefix, denominator 10 versions + 5 delete markers across 5 keys, IsTruncated absent) FALSIFIES THE COUNT THE AUTHORIZATION RESTS ON. The four keys carry NINE noncurrent versions, not four: r1/report.pdf has THREE (wl2x4Z9... named, plus s_LqtLL... and pL4dWRj...), and v0-11-overview, v0-11-comparison and v0-11-multicomp have TWO each (the named one plus HX6MJ2a..., oGHsMqX..., jP5Eyb1...). All four NAMED VersionIds are live and resolve, so the narrow reading of the stop condition is satisfied -- but deleting exactly those four would leave FIVE retrievable versions of the same four synthetic PDFs, and the qualifier this entire call exists to remove ('we cannot say they are gone') WOULD STILL STAND after the irreversible act. An unrecoverable act that does not achieve its stated purpose, taken on a count that is wrong by five, is not a partial success; it is the widening W4-S20 was filed to prevent, one level down. The likely origin is benign: IB-rt-8 re-ran the render, so each key accumulated versions and the pre-act head-object read captured only the then-current one per key -- A HEAD READ RETURNS ONE VERSION AND A VERSIONED KEY HOLDS MANY, which is exactly the instrument gap W4-S20 itself is about. ALSO PRESENT AND DELIBERATELY UNTOUCHED: firms/49financial/generations/GENIBS14SYN/attempts/1/exports/probe/probe.txt, one version plus a delete marker, under the same prefix, named nowhere in the row and not a synthetic export PDF -- reported, not acted on, and not swept up as 'while we are here'.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO -- carry the corrected count back to Andrew: does the approval cover all NINE noncurrent versions of the four keys (the act that actually makes them gone), or exactly the FOUR the row names (leaving five, and the qualifier standing). Until he answers on the CORRECTED number, no version is deleted and 'the four synthetic PDFs are gone' keeps its qualifier",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api list-object-versions --bucket opal-data-ycharts --prefix firms/49financial/generations/GENIBS14SYN/attempts/1/exports/ read 2026-09-12, aws_rc=0, 8808 bytes, IsTruncated absent: 10 Versions, 5 DeleteMarkers",
        "set comparison against the four VersionIds W4-S20 names: 0 of 4 missing from the live read, 6 live versions NOT named by the row (5 on the four report.pdf keys, 1 on probe/probe.txt)",
        "1.0.0_SA_CTO msg 96041 carrying Andrew-direct ~01:2xZ 'All recs approved', and its explicit NOT-AUTHORIZED list including 'any other version of those four keys beyond the four the row names'",
        "IRPT_BCKEND-W4-S20 and org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/RT8-g_delete_receipts.json (before.listing_under_prefix: 4 objects, one head read each)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "1.0.0_SA_CTO 96041: 'AUTHORIZED: the per-version delete of the FOUR noncurrent versions of the FOUR synthetic-export objects named in row W4-S20' and 'If the row's four VersionIds do not resolve to exactly four objects when you go to take it, STOP and come back rather than reconciling it yourself.'",
    "world_is": "The four named VersionIds resolve. The four KEYS hold nine noncurrent versions between them. The authorization's count and the world's count differ by five, and the difference is the whole difference between 'gone' and 'still retrievable by anyone with s3:GetObjectVersion'.",
    "notes": "FOURTH instance tonight of one class, and the first to reach an IRREVERSIBLE act: a scope that enumerates its members cannot see what the enumeration missed. S38 was a Terraform root holding two cells' state; S39 a zip carrying two cells' code; W4-S28 a coordinate no certification leg inspects; this one a versioned key holding more versions than the head read that enumerated it. CLAUDE.md Rule 24's subtraction clause is the direct remedy and would have caught it: the authorization's set was written as a FORWARD LIST of four remembered VersionIds rather than as the printed denominator of versions on those keys MINUS what is excluded. Carried to L10 with the other three."
  },
  {
    "id": "IRPT_BCKEND-W2-S30",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T23:08Z",
    "one_line": "Arm (a)'s whole-file denominator moved from 11 to 12 while this cell was dead: IB-rt-7's irpt-holdings is now LIVE on its published route, so routes.json resolves 12 handler-bearing routes and the whole-file census reads 1 of 12 unguarded -- and the only remedy paths (holdings/ lambda + terraform) are OUTSIDE this order's <paths>.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "The face's hand-off amendment says the whole-file population is ELEVEN and names holdings-snapshot as 'the one published route that has NO handler at HEAD (IB-rt-7's)', EXCLUDED on its own line; arm (a) requires unguarded_routes() over routes.json at HEAD to read '0 of N' with N the handler-bearing routes. The in-lane half is what this cell can move; <paths> carries directory/, performance/, ycharts/generate/, narrative/, export/, ops/ and NOT infra/aws/lambda/investor-reporting/holdings/ nor infra/aws/terraform/investor-reporting/holdings/.",
    "world_is": "At this worktree's cut a296eac0f4 the holdings route HAS a handler: infra/aws/terraform/investor-reporting/holdings declares handler = 'snapshot.lambda_handler' and holdings/snapshot.py exists, landed by IB-rt-7 at d9c940244a and deployed at 5a359024a9 ('irpt-holdings is LIVE on its declared route'). routetable therefore resolves 12 routes, the IN-LANE census reads 'OK: every route is guarded' over 11 of 11, and the WHOLE-FILE census reads 'BLOCKED: 1 of 12 route(s) reach an unguarded handler: [GET /api/scoped/investor-reporting/holdings/{accountSetId}]'. Guarding it would require writing a new entry module under holdings/ and re-pointing its Terraform handler -- both out of lane, so this cell reports it NAMED and ATTRIBUTED and does not act on it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/investor-reporting/holdings/*.tf@a296eac0f4 -- handler = \"snapshot.lambda_handler\"",
        "git log --oneline -- infra/aws/lambda/investor-reporting/holdings/@a296eac0f4 -> 5a359024a9 'irpt-holdings is LIVE on its declared route', d9c940244a 'the holdings handler'",
        "timeout 600 python -m pytest infra/aws/lambda/investor-reporting/_authz/tests/ -q @a296eac0f4 -> test_the_whole_file_census_is_zero AssertionError {'guarded': 11, 'routes': 12, 'unguarded': ['GET /api/scoped/investor-reporting/holdings/{accountSetId}']}",
        "IRPT_BCKEND.TO-IB-rt-2 face, ISSUER AMENDMENT at the hand-off (row W2-S18): 'the one published route that has NO handler at HEAD (holdings-snapshot, IB-rt-7's) named and EXCLUDED on its own line'",
        "<paths> of IRPT_BCKEND.TO-IB-rt-2@a296eac0f4 -- no holdings entry, lambda or terraform"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Hazard read INERT, not ARMED, because of row W2-S31: the un-wrapped holdings entry point enforces FirmBinding and Enforcer.guard() INLINE, so 'unguarded' here means 'does not carry the wrapper mark', not 'serves without authorization'. What the issuer owes this cell is a choice, not an act by me: either (i) grant holdings/ + its terraform root and arm (a) reads 0 of 12, or (ii) re-read arm (a)'s N as the IN-LANE handler-bearing routes with holdings NAMED and EXCLUDED on its own line exactly as the W2-S18 amendment already does for arm (g). This cell renders BOTH numbers in the battery and asserts neither as a pass."
  },
  {
    "id": "IRPT_BCKEND-W2-S31",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T23:08Z",
    "one_line": "The bypass detector grades a MARK, not a behaviour: is_guarded() reads __irpt_guarded__, so a handler that enforces FirmBinding + Enforcer.guard() INLINE (irpt-holdings' snapshot.lambda_handler) is counted UNGUARDED -- the census's word and the security property it is read as are not the same claim.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Arm (a) reads unguarded_routes() as the bypass detector and its verdict string says 'N of M route(s) reach an unguarded handler'; the cell's own ruling is that the guard is a NEW ENTRY MODULE per function whose wrapper sets the mark, and no arm distinguishes 'unwrapped' from 'unauthorized'.",
    "world_is": "_authz/enforce.py:577 is_guarded(fn) returns bool(getattr(fn, '__irpt_guarded__', False)) and unguarded_routes():591 selects on it alone. holdings/snapshot.py:343 builds _authz.FirmBinding(registry_firm_id, directory.get('firm_id_opaque')) and :353 builds _authz.Request(headers, KEY_OPERATION, 'account', account_set_id), importing enforce as _authz at :44 -- it enforces with THIS library and carries no mark, so it scores as a bypass. The detector is sound for its own question (did this entry point go through guard()) and is NOT a measurement of whether the route authorizes; a reader who converts the one into the other over-reads it in the unsafe direction only for wrapped-but-broken handlers and in the safe direction here.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/_authz/enforce.py:577-596@a296eac0f4 -- is_guarded/unguarded_routes",
        "infra/aws/lambda/investor-reporting/holdings/snapshot.py:44,313,343,353@a296eac0f4 -- import enforce as _authz; FirmBinding; Request",
        "comp-read infra/aws/lambda/investor-reporting/holdings/snapshot.py --for '...' @a296eac0f4 -- 24 sections, lambda_handler salient at 313-361"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not a defect of either cell and nothing here is edited by this order: enforce.py's docstring already states the question it answers ('can a handler forget the wrapper'). Filed so that the L9 reader of arm (a)'s '1 of 12' does not read it as a live cross-firm hole, and so IB-rt-7's inline enforcement is not retro-fitted to the wrapper on the strength of a census word."
  },
  {
    "id": "IRPT_BCKEND-W2-S32",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T23:48Z",
    "one_line": "A4's RULED remedy does not carry the modules: BOTH build scripts resolve a declared input ONLY as source_dir/<name> with no second step, so declaring served.py/loaders.py in files[] without a file on disk converts a latent ImportError into a hard build refusal -- and irpt-status, the shape A4 names to copy, is itself un-buildable at 3 of 10.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "Amendment A4 (2026-09-11 ~22:5xZ) RULES the layer-vs-vendor question against both halves and orders: 'declare the shared modules as FLAT BUILD INPUTS in lambda-source-map.json, per function, exactly the way irpt-status already does ... it is how four functions already resolve enforce/resolve today, and it needs neither a layer attachment nor a vendor manifest.' It further instructs: 'RESOLVE THE WAY THE BUILDER DOES, AND PRINT N of N ... A module is PRESENT if the builder resolves it from its home package at build time', and the ~18:2xZ correction names 'source_dir first, then the flat-packaged shared library roots'.",
    "world_is": "THE BUILDER HAS NO SECOND STEP, and two independent scripts say so in their own words: build-and-upload.sh:195-202 'for f in $FN_FILES; do if [ ! -f \"$ABS_SOURCE/$f\" ]; then echo \"  ERROR: File not found: $FN_SOURCE/$f\"' and build-zip.sh:51-54 'ERROR: Source file not found: $SOURCE_DIR/$f'. Neither reads a shared library root; a declared input that is not physically in source_dir puts the function in the builder's FAILED array. Census over the 9 irpt-* functions (denominator 84 declared inputs): 64 of 84 resolve, 20 do not -- irpt-ycharts-generate 18 of 27, irpt-export-render 10 of 14, irpt-status 3 of 10, while irpt-directory-search 2 of 2, irpt-performance-adapter 13 of 13, irpt-narrative 9 of 9 and irpt-holdings 9 of 9. So irpt-status, the shape A4 says to copy, is the WORST of the six and could not build today. And the gap A4 sends me to close is real and uniform: all six guarded entry modules import served and loaders (three also import enforce), 15 unsatisfied imports in total measured against what the builder would actually package. THE ONE IRPT FUNCTION THAT SOLVED THIS AND IS DEPLOYED SOLVED IT THE OTHER WAY: irpt-holdings (IB-rt-7) carries stage.py + STAGE_MANIFEST.json, which copy enforce.py/errors.py/resolve.py into its source dir from COMMITTED blobs via git show <pin>:<path>, plus BUILD_MANIFEST.json declaring vendored_modules and layer_dependencies -- i.e. a vendor manifest, the thing A4 says is not needed. A physical copy is what MAKES a flat build input real.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ci/build-and-upload.sh:195-202@a296eac0f4 -- manifest->disk check, source_dir only",
        "infra/aws/lambda/ci/build-zip.sh:51-54@a296eac0f4 -- 'ERROR: Source file not found: $SOURCE_DIR/$f'",
        "timeout 300 python .scratch/pkg_census.py @a296eac0f4 -> 'TOTAL: 64 of 84 declared build input(s) resolve the way the builder resolves them'; 'TOTAL unsatisfied imports across the six guarded entry modules ... 15'",
        "infra/aws/lambda/investor-reporting/holdings/STAGE_MANIFEST.json@a296eac0f4 -- 5 members staged from git show <pin>:<path>",
        "infra/aws/lambda/investor-reporting/holdings/BUILD_MANIFEST.json@a296eac0f4 -- vendored_modules + layer_dependencies",
        "infra/aws/terraform/investor-reporting/directory/lambda.tf:11-15@a296eac0f4 -- 'built and uploaded by infra/aws/lambda/ci/build-and-upload.sh', so the source map IS the packaging list"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~B",
    "notes": "NOTHING WAS EDITED ON THE STRENGTH OF THIS. I did not write the declaration A4 orders: adding served.py/loaders.py to files[] with no file beside them would ARM a build refusal for the next actor (including rt-9, row W2-S33) and would look like a landed remedy. I also did not build the holdings-shaped staging for the six, because that is the vendor manifest A4 ruled against and the round is FROZEN -- the ruling is the issuer's to re-cut, not mine to route around. A4 anticipated exactly this shape ('If you come to believe you must, that is a BLOCKING row to me, not an act') for the layer half; this is the same sentence applied to the half it chose. What the issuer must decide: (i) stage physical copies per function, holdings-style, and declare them -- the only shape in this estate that is deployed and works; or (ii) put served/loaders/enforce/errors/resolve in the irpt-common layer and attach it, which A4 measured the layer does not carry today. Arm (e) cannot be attempted under either reading without that decision, and arm (g) needs arm (e)."
  },
  {
    "id": "IRPT_BCKEND-W2-S33",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T23:48Z",
    "one_line": "The THREE functions A6 says IB-rt-9 deploys first are exactly the three carrying all 20 absent build inputs, so rt-9's first ledgered act refuses at the build before it reaches an apply -- and the ledger will already be OPEN when it does.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Amendment A6: 'Slot ~3 (IB-rt-9) owes a rebuild-and-deploy of irpt-export-render, irpt-status and irpt-ycharts-generate for the ids.py packaging gap (row W3-S25), and that is ITS first ledgered act. Three of those overlap your six. rt-9 deploys those three FIRST.' NEVER-2 requires the OPEN sentinel committed BEFORE the act.",
    "world_is": "Those three are precisely the functions whose declared build inputs do not resolve: irpt-export-render 4 absent (enforce.py, errors.py, ids.py, resolve.py), irpt-status 7 absent (enforce.py, errors.py, resolve.py, ids.py, keys.py, handler.py, checkpoint.py), irpt-ycharts-generate 9 absent (enforce.py, errors.py, gate.py, keys.py, resolve.py, ids.py, firm_destination_policy.json, firm_registry.json, settings.json) -- 20 of 20 of the estate-wide absences in this project sit in exactly these three, and the other three of my six are 2 of 2, 13 of 13 and 9 of 9 clean. build-and-upload.sh puts a function with an unresolved input in FAILED and continues; it never produces a zip. So the rebuild half of rt-9's act cannot succeed as declared, and NEVER-2's sequence puts the OPEN sentinel in the tree before that is discovered.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "timeout 300 python .scratch/pkg_census.py @a296eac0f4 -- per-function absent lists, 20 absent of 84 declared",
        "infra/aws/lambda/ci/build-and-upload.sh:195-207@a296eac0f4 -- FAILED+=(\"$FN_NAME\"); continue",
        "IRPT_BCKEND.TO-IB-rt-2 face, ISSUER AMENDMENT 2026-09-11 ~22:5xZ section A6@a296eac0f4"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "INERT because the failure is LOUD and fails closed -- the builder prints the missing path and refuses; nothing half-lands in AWS. Filed as friction rt-9 will hit in its first minutes, and because it is the same root as W2-S32 seen from the other slot: whatever the issuer decides there decides this. Not mine to fix: ycharts/generate is in my <paths> but the deploy of it is held by A6, and ops/ and export/ are shared with rt-9's owed act. I did not edit any of the three source-map entries."
  },
  {
    "id": "IRPT_BCKEND-W2-S34",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T23:48Z",
    "one_line": "The A5 rename leaves the FROZEN v1 contract naming a path that no longer exists: routes.json's `checked_by` and CONTRACT.md's provenance table both point at _authz/dispatch.py, and docs/contracts/ is out of this order's <paths> by its own rule.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Amendment A5 orders the rename 'in one commit with its importer, leaving no shim at the old basename', and names ONE importer (_contracts/tests/test_seam_paired.py:41). Row W2-S25's amendment says 'the v1 freeze at c22f179bbf stands and nothing in docs/contracts/ is edited by this order', and docs/contracts/ is not in <paths>.",
    "world_is": "There are two further references and both are in the frozen artifact: docs/contracts/investor-reporting/v1/routes.json:169 \"checked_by\": \"infra/aws/lambda/investor-reporting/_authz/dispatch.py\" and docs/contracts/investor-reporting/v1/CONTRACT.md:44 '| version checked by | `infra/aws/lambda/investor-reporting/_authz/dispatch.py` |'. Neither is code: an unscoped census of the token `checked_by` over 31,362 files returns 2 hits, this one and an unrelated CRO yaml, so NOTHING reads the field and the rename breaks no mechanism. The strings are now stale provenance inside a frozen contract, and the only in-lane options were to leave a shim (A5 forbids it) or edit the freeze (W2-S25 forbids it).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-find 'checked_by' --all --corpus default @a296eac0f4 -> 'DENOMINATOR: 2 hit(s) across 31362 file(s)', both CONFIG/prose, no code consumer",
        "docs/contracts/investor-reporting/v1/routes.json:169@a296eac0f4",
        "docs/contracts/investor-reporting/v1/CONTRACT.md:44@a296eac0f4",
        "commit 49035683d1 on wk-irpt_bckend-2-2b -- the rename, its one importer and PATH_MANIFEST.json:5561"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Carried to whoever next opens the v1 contract for an amendment, so the line is corrected in a commit that is allowed to touch it rather than by this order reaching past its grant. No hazard: the field is documentation of a checker, not an input to one."
  },
  {
    "id": "IRPT_BCKEND-W2-S35",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-11T23:48Z",
    "one_line": "A6 conditions this order's deploy on an act its assignee cannot perform -- 'Ask me; do not read its branch and decide for yourself' -- and a spine v3 L7 worker has no broker, no message tool and cannot be messaged, so arms (e) and (g) have no reachable path to completion in this run.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "Amendment A6: 'rt-9 deploys those three FIRST. You do NOT deploy them until I tell you its deploy has landed. Ask me; do not read its branch and decide for yourself.' Arm (e) requires CodeSha256 equality and a clean post-apply plan for EVERY function changed; arm (g) requires the paired producer-to-consumer test re-run against the DEPLOYED functions, so it needs arm (e).",
    "world_is": "The worker face's own IDENTITY section states the opposite capability: 'You have no broker, no message tool and no skill tool. You cannot be messaged and you message no one. Your ONE report is your final message', and the spine's L7 carries no send tool by design. So the condition A6 places on the deploy can be neither satisfied nor waived from inside this cell: asking is not an act available to me, reading rt-9's branch is expressly forbidden, and deploying anyway would override a grant. Three of the six (irpt-export-render, irpt-status, irpt-ycharts-generate) are held by A6 directly; the other three (irpt-directory-search, irpt-performance-adapter, irpt-narrative) are not held by A6 but are blocked independently by W2-S32, because their zips would not carry served.py or loaders.py and the re-pointed handler = entry.lambda_handler would ImportError on the first invocation.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "IRPT_BCKEND.TO-IB-rt-2 face, ISSUER AMENDMENT 2026-09-11 ~22:5xZ section A6@a296eac0f4",
        "the worker face's IDENTITY/communication section as delivered to this subagent, 2026-09-11 ~23:0xZ",
        "timeout 300 python .scratch/pkg_census.py @a296eac0f4 -- served/loaders unsatisfied in 6 of 6 guarded entry modules"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~B",
    "notes": "NOT an argument for deploying: the sequencing A6 states is sound and its reason is stated (until this order's apply re-points the handler strings the world runs the OLD handlers, which import neither served nor loaders, so rt-9's deploy is safe ahead of mine and mine is unsafe ahead of its declaration landing). The mismatch is only that the CONDITION is discharged by a message and the party who must act on it cannot receive one. The remedy is the issuer's: re-hand this order after rt-9's deploy lands, with the fact stated in the face, which needs no new mechanism. Arms (a) in-lane, (b), (c), (d) and (f) are complete and committed; (e) and (g) are what this row holds."
  },
  {
    "id": "IRPT_BCKEND-W2-S36",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-12T01:31Z",
    "one_line": "EVERY refusal the guarded boundary serves fails v1's StatusEnvelope on one clause -- source_dates.required is ['business_date'] and the boundary emits source_dates without one -- and the two halves of that defect have DIFFERENT owners: a post-read refusal could carry the artifact's date and does not, a pre-read refusal has no artifact and v1 admits no null.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "Row W2-S25, RULED by the issuer at the hand-off: 'A refusal is NEVER an instance of a response contract: it is v1's StatusEnvelope. Arm (g) grades SUCCESS responses against responses/<operation>.response.schema.json and REFUSALS against StatusEnvelope, both printed per operation.' The v1 freeze at c22f179bbf stands and nothing in docs/contracts/ is edited by this order.",
    "world_is": "Measured against the DEPLOYED functions, invoked by name after this order's apply: 11 of 11 in-lane routes refuse a mismatched X-Contract-Version with CONTRACT_VERSION (the face's own bar for that half, MET) and 0 of 11 of those refusals validate against docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json. Every one fails on the same clause: the schema's properties.source_dates carries required=['business_date'] with business_date typed as a non-null date string, and the boundary emits 'source_dates': {'source_completion_date': null}. The top-level required list does NOT name business_date, which is why a key-presence test passes -- the in-process arm 'b/c/d the envelope' asserts the SUBSET of top-level keys and reads 6 of 6, and only a schema validation against the published file sees this. TWO DEFECTS, MEASURED APART in process on irpt-directory-search: a POST-READ refusal (account swap, OBJECT_NOT_COVERED, raised after the directory artifact was read) emits the same date-less source_dates although the artifact it just read carries a business date -- fixable in lane; a PRE-READ refusal (CONTRACT_VERSION, raised before any artifact is read, which is the property that makes the version check trustworthy and is proven by the arm that refuses with the storage loaders REMOVED) has NO artifact to take a date from, and the business date comes from the artifact and never from a clock.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json@a296eac0f4 -- properties.source_dates.required == ['business_date']; top-level required == ['operation','state','source_dates','actions','public_reason_code','internal_correlation_id']",
        "timeout 900 python .../battery_ib_rt_2.py @737548f735 -- arm (g): 'a mismatched X-Contract-Version is refused CONTRACT_VERSION on the DEPLOYED function: 11 of 11; the refusal validates against v1 StatusEnvelope: 0 of 11', each line printing \"StatusEnvelope INVALID: 'business_date' is a required property\"",
        "live invoke of irpt-status @737548f735 -> {\"ok\": false, \"operation\": \"status-summary\", \"status\": {..., \"source_dates\": {\"source_completion_date\": null}, \"public_reason_code\": \"CONTRACT_VERSION\"}}",
        "in-process discriminator on irpt-directory-search @737548f735: POST-READ refusal code=OBJECT_NOT_COVERED source_dates={\"source_completion_date\": null}; PRE-READ refusal code=CONTRACT_VERSION source_dates={\"source_completion_date\": null}"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~B",
    "notes": "NOT FIXED, AND THE REASON IS STATED RATHER THAN THE FIX BEING HALF-TAKEN. The post-read half is this cell's and is a small in-lane change; the pre-read half cannot be fixed without amending a FROZEN v1 contract that this order is expressly forbidden to touch (W2-S25's own amendment). Shipping the post-read half alone would still leave 11 of 11 version refusals non-conforming -- it moves no arm -- and would spend a second six-root build-and-deploy cycle to do it. So the arm reads BLOCKED with this row rather than PASS with a repair that changes no number. What the issuer or the CTO must decide: whether v1's StatusEnvelope gains a null branch for a refusal raised before any artifact read (an L10 addendum to a frozen contract), or whether a pre-read refusal is declared to be a different shape from a StatusEnvelope, as W2-S25 already declared it a different shape from a response contract. NO HAZARD: the refusal is well-formed, carries its public reason code and its correlation id, and leaks nothing -- what fails is the SCHEMA claim about it, not the safety of it."
  },
  {
    "id": "IRPT_BCKEND-W2-S37",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-12T01:31Z",
    "one_line": "The record corrected in flight: A6 was struck by the issuer mid-run and the six-root deploy landed and verified, so rows W2-S35 (the un-receivable release condition) and W2-S33 (rt-9's build) are OVERTAKEN BY EVENTS, and W2-S32's operational claim is REFUTED BY THE ACT -- the members do resolve, from the flat shared roots, and six artifacts now import in the runtime layout.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "W2-S32 asserted that A4's ruled remedy could not carry the modules because both build scripts resolve source_dir/<name> only, and W2-S35 asserted that arms (e) and (g) had no reachable path because A6 conditioned the deploy on a message a worker cannot receive. Both were filed as BLOCKING with disarm owner 2.0.0_SA_COO~B.",
    "world_is": "The issuer STRUCK AND REVERSED A6 in the same session ('you are not inheriting a delay, you are inheriting the whole act') after slot ~3 refused the deploy it had been ordered to take and was right to: all three roots already carried the unapplied handler flip, so the apply that shipped the ids.py fix would also have flipped the handler onto an `entry` module no zip carried. W2-S35 is therefore discharged by the issuer's own act, not by mine. W2-S32's DIAGNOSIS stands -- neither build-and-upload.sh nor build-zip.sh has a second resolution step, so declaring a member that is not in source_dir makes THOSE scripts refuse -- but its operational conclusion ('the ruled remedy does not carry the modules') is REFUTED: resolving source_dir first and then the flat shared roots (_authz, _scope, _keys, _ids, _gate, intake, directory, data, terraform/core) finds every declared member, which is what slot ~3 measured independently at 14 of 14, 10 of 10 and 27 of 27, and what this cell then EXERCISED -- 6 of 6 artifacts built, and 6 of 6 import in the flat /var/task (+ /opt/python where the layer is attached) layout from their SERVED bytes with the repo off sys.path, every negative control firing. The reconciliation is that the two measurements answered DIFFERENT QUESTIONS: mine asked whether the shipped build SCRIPT resolves from the repo, slot ~3's asked whether the declared names exist in the repo at all. Both answers were correct and only together do they say what to do. W2-S33 (rt-9's three functions refusing at the build) is overtaken the same way: those three are now this cell's, are built by the recipe rather than by that script, and are deployed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the issuer's correction and addendum to 0.9.0_WK_IRPT_BCKEND~2, 2026-09-12, striking A6 and placing the one-root-at-a-time control",
        "org/critical_paths/change_management/20260912T0035Z_irpt-bckend-rt2_deploy_completion.md@737548f735 -- 12 legs CLOSED, six roots, every post-apply plan 'No changes'",
        "timeout 900 python .../battery_ib_rt_2.py @737548f735 -- arm (e): 'declared artifact_sha256 == live CodeSha256: 6 of 6; handler is the guarded entry: 6 of 6; Active/Successful: 6 of 6' and 'IMPORT-OK 6 of 6 | negative control FIRES 6 of 6 | VERIFIED 6 of 6'",
        "infra/aws/lambda/ci/build-and-upload.sh:195-202 and build-zip.sh:51-54@a296eac0f4 -- the diagnosis half of W2-S32, unchanged"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Filed because the channel is APPEND-ONLY and an earlier row of mine may not be edited: a reader who finds W2-S32 and W2-S35 without this row would act on two BLOCKING items that the world has already passed. Neither earlier row was wrong when written and neither is deleted. What survives from W2-S32 and is still worth an owner: the shipped build scripts cannot build these six functions from their declared lists, so the artifacts were built by the proven recipe instead -- anyone who later runs build-and-upload.sh against irpt-status will still get 'ERROR: File not found', and that gap belongs to whoever owns infra/aws/lambda/ci/, which is not in this order's <paths>."
  },
  {
    "id": "IRPT_BCKEND-S42",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "1.0.0_SA_CTO",
    "surfaced_at": "2026-09-12T02:02:02Z",
    "one_line": "DISARM of IRPT_BCKEND-S41 by its named disarm_owner. S41 required 1.0.0_SA_CTO to carry the CORRECTED count back to Andrew and report his answer on that corrected number; until then no version was to be deleted. Done, and he answered. ANDREW-DIRECT 2026-09-12 ~01:5xZ at the 1.0.0_SA_CTO terminal, VERBATIM AND ENTIRE: 'Approved all 9', answering the card 'The four synthetic export PDFs hold NINE noncurrent versions, not four. (a) delete all nine (b) delete only the four named (c) leave them' with REC (a). So the authorized set is the NINE noncurrent versions of the FOUR synthetic-export report.pdf keys, and it is written as a SUBTRACTION from a printed denominator rather than as a forward list, because a forward list of four remembered VersionIds is what failed the first time (Rule 24): DENOMINATOR 10 versions / 5 delete markers / 5 keys (s3api list-object-versions over the exports/ prefix, re-measured independently at 1.0.0_SA_CTO 2026-09-12T01:44Z, rc=0, 8808 bytes, IsTruncated absent) MINUS probe/probe.txt (1 version, 5 B, not an export PDF, named nowhere in the row) = 9. NOT AUTHORIZED and named so the drift is inexpressible: probe.txt and its delete marker; any other object or prefix in opal-data-ycharts; THE FIVE DELETE MARKERS THEMSELVES (removing a delete marker RESTORES a current object, which is the opposite of the intent); any bucket-level change to versioning, lifecycle, policy or replication; any 'while we are here' cleanup. THE COUNT IS PERISHABLE AND HAS ALREADY MOVED ONCE (it was four when W4-S20 was filed, because IB-rt-8 re-ran the render and each key accumulated versions), so 2.0.0_SA_COO~B re-reads the prefix IMMEDIATELY BEFORE acting and STOPS AGAIN if the live denominator is not 10/5/5 with nine noncurrent PDF versions -- the authorization is over a MEASURED SET, never over a number to be matched. Evidence shape required: the nine VersionIds read before, the deletes, then a BY-VERSIONID read returning NoSuchVersion on 9 of 9 with a POSITIVE CONTROL on an object that must still resolve; a 404 on the ordinary key proves nothing here, which is the entire reason this call existed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO -- the S41 disarm CONDITION is discharged by this row (the corrected count went back to Andrew and he answered on it). NOTE ON VOCABULARY, because this row is INERT and not a grade: this row does NOT resolve S41 to GRADUATED. Under the protocol a REMEDIATION row bearing the id is what resolves an item, and remediation rows stay 3.0.0_SA_CVO's; S41 therefore stands at its own disposition until the CVO carries it. The S41 hazard was acting on a count wrong by five; it cannot occur now that the authorization is over the measured nine rather than over four remembered ids. 2.0.0_SA_COO~B holds the ACT under the boundary above; this row disarms the hazard, it does not perform or grade the act.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ANDREW-DIRECT 2026-09-12 ~01:5xZ, verbatim 'Approved all 9', recorded at org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260912_015xZ_ALL_NINE_NONCURRENT_VERSIONS_APPROVED.md",
        "s3api list-object-versions --bucket opal-data-ycharts --prefix firms/49financial/generations/GENIBS14SYN/attempts/1/exports/ -- re-measured at 1.0.0_SA_CTO 2026-09-12T01:44Z, rc=0, 8808 bytes, IsTruncated absent: 10 Versions, 5 DeleteMarkers, 5 keys; nine noncurrent versions on the four report.pdf keys, confirming 2.0.0_SA_COO~B's count exactly",
        "the re-measurement was taken on this seat's own instrument rather than adopted from 96046, because a number that was wrong once does not get relayed twice"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "IRPT_BCKEND-S41 disarm_owner: '1.0.0_SA_CTO -- carry the corrected count back to Andrew: does the approval cover all NINE noncurrent versions of the four keys, or exactly the FOUR the row names. Until he answers on the CORRECTED number, no version is deleted.'",
    "world_is": "He answered on the corrected number: all nine. The disarm condition S41 names is satisfied, so S41 is DISARMED and the act is unblocked under the enumerated boundary. Nothing has been deleted by this row; the bucket is unchanged at the time of writing.",
    "notes": "The CTO-side half of the class S41 names. The first authorization failed because this seat carried a head-read count into a sovereign card for an unrecoverable act without measuring it -- a head-object read returns ONE version while a versioned key holds MANY. The stop condition this seat wrote was also weaker than it looked: it was keyed to whether the four named VersionIds RESOLVE (they did) rather than to whether the SET IS COMPLETE (it was not), and only the second protects the act. 2.0.0_SA_COO~B refused on better reasoning than the condition contained. Full record: org/tier1_exec/1.0.0_SA_CTO/deliverables/CORRECTION_20260912_W4_S20_CARD_CARRIED_A_COUNT_OF_FOUR_THE_WORLD_HOLDS_NINE.md."
  },
  {
    "id": "IRPT_BCKEND-S43",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-12T02:45:32Z",
    "one_line": "THE NINE NONCURRENT VERSIONS ARE PERMANENTLY GONE, AND 'THE FOUR SYNTHETIC EXPORT PDFS ARE GONE' NO LONGER CARRIES A QUALIFIER -- the first time that sentence has been true tonight. Andrew-direct ~01:5xZ 'Approved all 9' (via 1.0.0_SA_CTO 96050) on the CORRECTED count; ledger opened BEFORE the act at 89d9b2965d and closed at c441d163ab with 8 of 8 legs. The pre-act gate re-read the prefix at the moment of acting and matched the authorized subtraction exactly (denominator 10 versions / 5 delete markers / 5 keys, MINUS probe/probe.txt, = 9 targets; IsTruncated absent) -- the authorization was over a MEASURED SET, never over the number nine as a target, and a mismatch would have been a second STOP. Nine per-version deletes, then a BY-VERSIONID head-object returning (404) Not Found on 9 of 9 with byte-identical error text -- NOT AccessDenied, which is the failure that looks the same at rc level -- and a POSITIVE CONTROL on probe/probe.txt's version resolving rc=0 at ContentLength 5 under the SAME credential, operation and bucket, which is what rules out a permissions or network explanation for the nine. Prefix versions 10 -> 1; the remaining one is probe/probe.txt, deliberately excluded and untouched. THE FIVE DELETE MARKERS WERE NOT TOUCHED AND THAT WAS A BOUNDARY, NOT AN OVERSIGHT: deleting a delete marker RESTORES a current object, the opposite of the intent, so 'delete all 9' does not reach them -- 1.0.0_SA_CTO named it as a trap rather than a rule in 96050 and was right to, because a cleanup loop reads five markers as debris. A 404 on the ORDINARY key is cited nowhere in this record: it was already true before the act and that is the entire reason this call existed. Receipts at org/critical_paths/change_management/20260912T0215Z_irpt-bckend-w4s20-nine-version-delete_receipts.json with delete_grain stating in the artifact itself that this was the PERMANENT form and not a marker.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (the act is complete and verified; W4-S20's and S41's qualifier is discharged by measurement. A remediation row resolving W4-S20 and S41 remains 3.0.0_SA_CVO's, per the vocabulary note in S42)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/critical_paths/change_management/20260912T0215Z_irpt-bckend-w4s20-nine-version-delete_deploy_completion.md -- CLOSED, 8 of 8 legs",
        "org/critical_paths/change_management/20260912T0215Z_irpt-bckend-w4s20-nine-version-delete_receipts.json -- 9 delete responses, 9 post-act head reads, the positive control and the deltas",
        "ledger+sentinel commit 89d9b2965d BEFORE the act; close commit c441d163ab; sentinel removed from org/critical_paths/.open_deploys/",
        "post-act s3api list-object-versions over the prefix: versions=1 deletemarkers=5 (pre-act 10 and 5)",
        "Andrew-direct record org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260912_015xZ_ALL_NINE_NONCURRENT_VERSIONS_APPROVED.md"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Andrew-direct 2026-09-12 ~01:5xZ, VERBATIM AND ENTIRE: 'Approved all 9', answering the card '(a) delete all nine (b) delete only the four named (c) leave them', REC (a).",
    "world_is": "Nine noncurrent versions deleted permanently and verified gone by VersionId; one excluded version and five delete markers untouched; no bucket-level setting changed.",
    "notes": "The lineage is worth keeping intact because each step was a different error being caught: W4-S20 found that a delete on a versioned bucket is a VISIBILITY change reported as destruction; S41 found that the authorization's own count was short by five because a head read enumerates one version of a key that holds many; S42 carried the corrected number back; this row is the act. Two STOPs and one delete, and the only irreversible step happened on a re-measured set with Andrew's word on the real number."
  },
  {
    "id": "IRPT_BCKEND-S44",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-12T02:45:32Z",
    "one_line": "IB-rt-2's EIGHT ROWS DISPOSITIONED, AND THE POST-READ OBLIGATION RE-ROUTED OFF A BATTERY THAT CANNOT FIRE. W2-S30: holdings paths GRANTED additively (holdings/ lambda + the holdings Terraform root) and LOOSENING THE CENSUS REFUSED -- W2-S31 establishes the census grades the __irpt_guarded__ MARK while that handler enforces FirmBinding inline, so it is a MARK gap and not a live cross-firm hole, and an inline enforcement the instrument cannot see should stay VISIBLE; the handler moves under the mark, the instrument does not move. 1.0.0_SA_CTO endorsed that reasoning explicitly. g2: RULED HUMAN-GATED under the face's OWN standing rule, which the CTO confirmed is a rule applied and not a bar lowered, with an instruction not to put it back. W2-S36: RESOLVED by the CTO's L4 amendment, PRD v0.14 @b8e98d5a4d -- business_date is STATE-CONDITIONAL (required on the 5 answer-bearing states, may be ABSENT and never NULL on the 4 no-answer states) rather than nullable, because nullable -- which was THIS SEAT'S option (a) -- would have weakened every envelope including a READY success and traded a validation gap for a semantic hole in the success path. AND MY OWN TWO-WAY CUT WAS SHORT BY TWO: QUEUED and RUNNING carry no business_date by construction and are not refusals at all, so a fix scoped to 'refusals' would have left both failing exactly as before. W2-S32 and W2-S35 discharged by the worker's own W2-S37; W2-S33 and W2-S34 accepted INERT. THE RE-ROUTING: the CTO's ruling places the surviving post-read business_date obligation on 'the IB-s-18 BATTERY'. MEASURED BEFORE ROUTING A WORKER INTO IT -- that battery is rc=1 and has been: battery_ib_s_18.py:315, arm_c, `for k in sorted(breakdown)`, TypeError '<' not supported between NoneType and str. Its arm (b) -- the schema-provenance arm -- PASSES 11 of 11 valid ACCEPTED and 11 of 11 invalid REFUSED, ABOVE the traceback, so CLEAN METRICS PRINT ABOVE A FAILING VERDICT and the battery's rc, which is its verdict, is permanently 1. ANY OBLIGATION ADDED THERE COULD NEVER FIRE, because a crash in a DIFFERENT arm masks it. So the obligation is landed in battery_ib_rt_2.py instead -- live, in lane, and the instrument RT2-AC1 actually reads -- and the departure from the CTO's routing was stated to it with an explicit invitation to overturn, not taken silently.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO -- (i) confirm or overturn landing the post-read business_date obligation in battery_ib_rt_2.py rather than the IB-s-18 battery; (ii) W4-S29's crash is now LOAD-BEARING, because the same battery is the named enforcement for generated-schema provenance while its generator exists on no device -- two holes in one provenance chain, and the fix belongs to a CLOSED cell so it is routed, never taken here",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLOUD be8adeba41 (drain of wk-irpt_bckend-2-2b; rows W2-S30..S37)",
        "timeout 600 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_s_18.py -> rc=1, traceback at :315 in arm_c; arm (b) printing 11 of 11 ACCEPTED and 11 of 11 REFUSED above it",
        "IB-rt-2 face issuer amendments 3 @4131ef651f and 4 @76ae1b20fb; worker worktree fast-forwarded to 76ae1b20fb",
        "1.0.0_SA_CTO 96051 (the ruling) and 96060 (L4 landed, PRD v0.14 @b8e98d5a4d, 11 of 11 cases over nine states with a negative control)",
        "proof-of-spec-check over IB-rt-2's instance at HEAD: VALID rc=0, RT2-AC1 FAIL at 10 of 13 arms"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "1.0.0_SA_CTO 96051: 'the obligation moves to the BATTERY: a post-read refusal that omits business_date is a battery failure, not a schema failure' -- naming the IB-s-18 battery.",
    "world_is": "That battery exits 1 on a pre-existing crash in an unrelated arm, so it cannot carry a new obligation and cannot return a passing verdict for the provenance arm that does work. IB-s-18 is also a CLOSED round-1 cell, so editing it mid-round is the re-open Rule 27 forbids.",
    "notes": "FIFTH INSTANCE TONIGHT OF ONE CLASS AND THE SECOND FROM THIS SEAT: S38 (a Terraform root holding two cells' desired state), S39 (a zip carrying two cells' code), W4-S28 (a coordinate no certification leg inspects), S41 (a versioned key holding more versions than the head read that enumerated it), and this seat's two-way cut of a NINE-member enum. A SCOPE THAT ENUMERATES ITS MEMBERS CANNOT SEE WHAT THE ENUMERATION MISSED; Rule 24's subtraction clause is the remedy in all five. A SIXTH SHAPE APPEARS HERE AND IS WORTH NAMING SEPARATELY: moving an obligation into an instrument without first running that instrument. The routing was correct in intent and unenforceable in fact, and only an execution of the battery could tell the difference -- a gate's OWN RUN is the authority, and a named enforcement surface is a claim until someone runs it. Carried to L10 with the other five."
  },
  {
    "id": "IRPT_BCKEND-W3-S34",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-12T02:12Z",
    "one_line": "IB-rt-11's ORDERED edit to intake/settings.json moved a DECLARED BUILD INPUT of irpt-ycharts-generate 20 minutes after slot ~2 deployed and closed its ledger on it, so the tree and the served zip now disagree for that function by exactly one top-level key.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ci/lambda-source-map.json @72db64c153: functions['irpt-ycharts-generate'].files[] contains 'settings.json', which resolves to infra/aws/lambda/investor-reporting/intake/settings.json (1 of 214 functions declares it; parse.py and corrections.py are declared by 0)",
        "aws lambda get-function-configuration --function-name irpt-ycharts-generate, read live 2026-09-12T02:0xZ: CodeSha256 VGsTbaPGv70V2l2w8X85z7XK8NEB9hTkbkeDmke1Dt8=, LastModified 2026-09-12T01:10:12Z, Handler entry.lambda_handler -- slot ~2's deploy, intact",
        "the S3 artifact downloaded and its member extracted: served settings.json is 5104 bytes sha256 b6467fc1789ea50b..., tree settings.json is 9670 bytes sha256 c493ea6edd6ee7c3... at dc5d119b84 -- NOT equal; the downloaded zip's own sha256 equals the live CodeSha256, so the deploy is not what moved",
        "DISCRIMINATOR, and it is what makes this INERT rather than ARMED: the served and tree copies of the `settings` SUBTREE and of `cautions` are byte-identical (7 members each); the only difference is the ADDED sibling key `intake_controls`. recipe.SETTING_TO_VENDOR_FIELD reads settings['settings'] by name, so nothing irpt-ycharts-generate reads has changed",
        "the sibling-key placement was chosen for exactly this reason and says so in settings.json _meta.why_this_is_a_SEPARATE_TOP_LEVEL_KEY"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-11 DELIVERABLE names `intake/{parse.py,corrections.py,settings.json}` as this cell's files and BOUNDS says 'No deploy in this cell (the intake Lambda's next build carries it)'; slot ~2's drain reports artifact_sha256 == S3 content-sha256 == live CodeSha256 on 6 of 6 roots.",
    "world_is": "Both are true and they interact: settings.json is ALSO a build input of a function in another cell's root, so an edit this order was told to make invalidates the hash agreement another order just certified. Nothing is broken and nothing needs re-deploying for correctness -- the served bytes are a valid older vintage of a file whose changed part that function does not read. What is no longer true is the SENTENCE 'the tree and the served artifact agree', for one of the six.",
    "notes": "Not remediated here: rebuilding or re-deploying irpt-ycharts-generate is out of this cell (BOUNDS: no deploy) and lambda-source-map.json is not in this order's <paths>. Carried so the next rebuild of that function is expected rather than surprising, and so nobody reads a moved hash as drift."
  },
  {
    "id": "IRPT_BCKEND-W3-S35",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-12T02:12Z",
    "one_line": "The shared contract's `corrections` item is additionalProperties:false with exactly four keys and no timestamp, so the WHEN this cell's law requires on a human correction CANNOT travel in the contract -- a consumer validating AnalysisRequest never sees who corrected what WHEN.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/_contracts/AnalysisRequest.schema.json @72db64c153, properties.corrections.items: additionalProperties false, properties = finding_code, approved_by, from_value, to_value; required = all four. There is no time field of any name",
        "TO-IB-rt-11 acceptance (c), verbatim: 'A human correction on a quarantined row appears on r+1 with who/when/from-what'",
        "the amendment's B4, verbatim: 'Human correction provenance is PRESERVED, not overwritten. A corrected value carries who corrected it and what it was'",
        "`_contracts/` is not in this order's <paths> block, so the schema is READ here and not edited"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The correction provenance the cell's law requires -- WHO, WHEN and WHAT-IT-WAS -- is carried on the revision in the contract's own `corrections` array.",
    "world_is": "The contract can carry WHO and WHAT-IT-WAS and cannot carry WHEN. This cell makes `approved_at` REQUIRED on an approval and validates it as an ISO-8601 UTC instant, then writes it into a SIBLING `correction_provenance` array on the revision, leaving the contract array at exactly its four keys so it still validates. The provenance is preserved, hashed with the revision and readable -- but ONLY by a consumer that knows to look outside the contract. A consumer that validates AnalysisRequest and reads `corrections` gets a correction with no time on it, and no care inside this cell changes that.",
    "notes": "The remedy is a one-field contract amendment (`approved_at`, string, ISO-8601 Z) and it belongs to whoever owns _contracts/. Raised rather than worked around silently: the sibling array is the honest placement available to this order, not the right long-term shape."
  },
  {
    "id": "IRPT_BCKEND-W3-S36",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-12T02:12Z",
    "one_line": "parse.py and corrections.py are declared by 0 of 214 functions, so every currency and unit control this cell certifies is certified in the REPO for a module that has no runtime yet -- and the first function to ship parse.py must ship settings.json beside it or the parser refuses at its first money column.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ci/lambda-source-map.json @72db64c153, over all 214 functions: 0 declare parse.py, 0 declare corrections.py, 1 declares settings.json (irpt-ycharts-generate, which does not ship the parser)",
        "parse.load_intake_controls reads os.path.join(_HERE, 'settings.json'); in a Lambda _HERE is the flat /var/task, so the policy file must be a declared build input of any function shipping parse.py",
        "EXERCISED: load_intake_controls against a missing path raises ParseRefused 'the intake currency/unit policy is not readable ... This module REFUSES rather than applying a built-in default' -- the refusal is by design, added in this cell rather than left as a FileNotFoundError",
        "the sibling shape of the same defect was measured one cell over as IRPT_BCKEND-W3-S25: _scope/resolve.py gained a module-level import and the packaging half did not follow, and CodeSha256 equality could not see it by construction"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The issuer's note of 2026-09-12 ~02:0xZ: 'A CHECK THAT RUNS IN THE WRONG ENVIRONMENT PASSES ON A BROKEN ARTIFACT. When you certify a currency or a unit, ask where your check runs versus where the value is actually consumed.'",
    "world_is": "The answer to that question for this cell is NOWHERE YET: the module is not packaged into any function, so there is no runtime in which the value is consumed and the controls are certified only in the repo. The battery therefore runs the controls a SECOND time in a flat /var/task-shaped directory in a fresh interpreter with the repo stripped from sys.path, and carries a negative arm proving the parser REFUSES when the policy file is absent rather than defaulting to USD -- which is the exact runtime-only failure the warning names. That is the closest a cell that deploys nothing can get, and it is not the same thing as a deployed check.",
    "notes": "Not remediated here: adding parse.py to a function's files[] is a packaging act, lambda-source-map.json is not in this order's <paths>, and this cell deploys nothing by its own BOUNDS. The requirement for whoever packages it: parse.py, corrections.py, settings.json AND fixtures/holdings/security_mapping.json (load_mapping reads a SUBDIRECTORY of _HERE) must land together."
  },
  {
    "id": "IRPT_BCKEND-S45",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-12T03:05:42Z",
    "one_line": "IB-rt-11 ACCEPTED TERMINAL (8 of 12), AND ITS HEADLINE IS A FALSE GREEN CAUGHT BY ITS OWN AUTHOR AFTER THE FLIP. The worker flipped <status> complete, then found that commit 3c28723d20 pinned parse.py at a version which does NOT carry the load_intake_controls refusal that arm (e)'s NEGATIVE arm proves -- the edit was made after the commit and never committed, so THE ARM PASSED AGAINST THE WORKTREE WHILE THE INSTANCE NAMED BYTES THE RECORD DID NOT CARRY. proof-of-spec-check returned rc=0 and the criterion read PASS-by-output, and BOTH were reading a file the record did not contain. Found by reading git status --porcelain AFTER the flip; re-opened on the record at 3db8d67f17 with the reason on the face, the real refusal committed at 51db4a7d66, re-pinned, re-validated, re-flipped honestly at 7408aa5c5e. The issuer re-graded the instance at HEAD rather than taking the report's word: VALID rc=0, 3 of 3 surprise entries resolving, parse.py CONTENT-resolved at 51db4a7d66 rather than presence-only. TWO MECHANISMS THE CELL PROVED IN PASSING AND BOTH ARE WORTH KEEPING: the owned-paths lane gate REFUSED the parse.py commit the instant the order went terminal ('no NON-TERMINAL task order at HEAD issued_to this serial names this path'), so a worker who flips early CANNOT quietly patch afterwards and the remedy is forced onto the record; and PENDING-THIS-COMMIT is SPENT once the instance is committed, a second sentinel on an already-committed artifact being refused as CCX class. W3-S34 ACCEPTED INERT and the discriminator is why -- this cell's ORDERED settings.json edit moved a declared build input of irpt-ycharts-generate 20 minutes after slot ~2 deployed it, and the worker read the SERVED artifact (5104 B) against the tree (9670 B) and showed the delta is ONLY an added sibling key with the settings subtree and cautions byte-identical; slot ~2 has been told its next deploy carries the rider and must NAME IT IN ITS LEDGER, because the deploying cell is the last to find out and the one holding the irreversible act. W3-S35 and W3-S36 stay ARMED with the issuer: the contract's corrections item is additionalProperties:false with no time field so the WHEN cannot travel in the contract (_contracts/ outside the cell's paths, so a row was the right call and approved_at rides in a sibling correction_provenance array), and parse.py is shipped by 0 of 214 functions so whoever packages it must ship settings.json AND fixtures/holdings/security_mapping.json beside it or the parser refuses at its first money column. AND THE L4-R HOLD IS DISCHARGED: prd-signoff status reads ADMITTED, both halves SIGNED and current, the brief half now HASH-BOUND so a future version bump cannot re-stale it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B for W3-S35 and W3-S36 -- both are carried to L10 rather than acted on mid-round: the corrections contract has no time field (a frozen-contract question, same class as W2-S36 which needed an L4 amendment) and parse.py's packaging has no shipping function yet, so neither is fixable inside this round without re-opening a closed surface. W3-S34 is INERT and needs no owner",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLOUD 49d6376765 (drain of wk-irpt_bckend-2-3c; rows W3-S34..S36)",
        "proof-of-spec-check.py re-run by the issuer at HEAD over IB-rt-11's instance: VALID rc=0, 3 of 3 surprises resolving, 1 row CONTENT-resolved",
        "IB-rt-11 face <status> complete, stated as being on the SECOND flip with the first reverted on the record",
        "the cell's own commit chain dc5d119b84 (feat) -> 3c28723d20 (complete, REVERTED) -> 3db8d67f17 (reopen) -> 51db4a7d66 (the refusal) -> 7408aa5c5e (the honest flip)",
        "python .tools/prd-signoff.py status IRPT_BCKEND -> ADMITTED, both halves SIGNED current (was WITHHELD at 02:51Z)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RT11-AC1's arm (e): the policy is absent -> 4 of 4 REFUSED, proving load_intake_controls does not default. The instance named the bytes that produce that refusal.",
    "world_is": "At the first flip the named bytes did NOT produce it -- the refusal existed only as an uncommitted worktree edit. The checker read rc=0 against a worktree the record did not describe, which is the exact shape of a green that certifies nothing.",
    "notes": "THE GENERAL FORM IS THE VALUABLE PART AND IT IS NOT ABOUT THIS CELL: A PROOF INSTANCE PINS BYTES, AND A BATTERY READS A WORKTREE. When an edit exists only in the worktree, the two disagree and every instrument still reads clean -- rc=0 from the checker, PASS-by-output from the criterion. The only thing that separates them is `git status --porcelain` AFTER the flip, which is not part of anybody's acceptance bar. Worth the L10 slug as a candidate addition to the worker face's standing mechanics: read porcelain before the flip, not after. Related to, but distinct from, tonight's other shapes -- the five enumeration failures, the obligation routed into an unrun instrument, and the sign-off tool's prose overstating a version-only comparison as a byte change (independently confirmed by 4.0.0_SA_CRO, which measured both brief halves unchanged and logged the prose as a tooling defect)."
  },
  {
    "id": "IRPT_BCKEND-W2-S38",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-12T03:20Z",
    "one_line": "The ycharts root's zip carries intake/settings.json but not fixtures/holdings/security_mapping.json -- literally the asymmetry the issuer named as blocking -- and the discriminator is that NO function ships parse.py and the only readers of settings.json are two test suites, so the deployed code cannot reach the refusal the pair exists to prevent.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "The issuer's note of 2026-09-12: IB-rt-11 edited infra/aws/lambda/investor-reporting/intake/settings.json, a declared build input of irpt-ycharts-generate, which this order deploys; 'NAME IT IN YOUR LEDGER ENTRY as a rider', 'verify it the way you verify your own bytes', and 'If your zip for that function picks up one of those and not the other, that is a BLOCKING row to me, not something to reconcile yourself' -- the pair being settings.json and fixtures/holdings/security_mapping.json, which row W3-S36 says parse.py needs beside it or it REFUSES at its first money column.",
    "world_is": "MEASURED, and the literal condition IS met: irpt-ycharts-generate's 30 declared members include settings.json and do NOT include fixtures/holdings/security_mapping.json (nor any fixtures/holdings/* member), so the zip picks up one of the pair and not the other. THREE FURTHER MEASUREMENTS SAY THE PAIRING IS NOT WHY IT IS THERE, and together they are the discriminator: (1) parse.py is declared by 0 of 214 functions in lambda-source-map.json, so no deployed artifact contains the parser whose refusal the pair guards -- W3-S36's hazard has no carrier; (2) settings.json is a member of this function IN ITS OWN RIGHT and predates this order -- ycharts/generate/recipe.py:57 defines SETTINGS_PATH and :105 load_settings(), for the YCharts portfolio recipe, nothing to do with holdings; (3) an unscoped census of load_settings over the package returns 3 hits and the only two CALLERS are test suites (ycharts/generate/tests/run_offline_suite.py:175 and ycharts/session/tests/run_session_suite.py:99) -- the deployed path never calls it, and job.py receives `settings` as a constructor argument instead. AND A SEPARATE RUNTIME-ONLY DEFECT SITS IN THAT SAME LINE: SETTINGS_PATH is os.path.normpath(os.path.join(_HERE, '..', '..', 'intake', 'settings.json')), a REPO-RELATIVE path that at /var/task resolves to /intake/settings.json and cannot exist, while the zip carries the file FLAT beside recipe.py. It is the same shape as the /var/_authz defect this cell already fixed in entry.py, it is PRE-EXISTING in the live artifact, and it is unreachable today only because no deployed caller invokes load_settings().",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ci/lambda-source-map.json@76ae1b20fb -- irpt-ycharts-generate declares settings.json, not security_mapping.json, not parse.py; 0 of 214 functions declare parse.py",
        "infra/aws/lambda/investor-reporting/ycharts/generate/recipe.py:57,105@76ae1b20fb -- SETTINGS_PATH and load_settings",
        "comp-find 'load_settings' over the package @76ae1b20fb -> 3 hits, 1 DEF and 2 TEST callers, no deployed caller",
        "comp-find --name security_mapping.json @76ae1b20fb -> 1 hit across 33,312 files: infra/aws/lambda/investor-reporting/intake/fixtures/holdings/security_mapping.json",
        "the issuer's note of 2026-09-12 naming row IRPT_BCKEND-W3-S34 (served 5104 B vs tree 9670 B, an ADDED sibling key, settings subtree and cautions byte-identical) and W3-S36"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~B",
    "notes": "NOT RECONCILED, exactly as instructed, and the irpt-ycharts-generate root is HELD OUT of this order's deploy until the issuer rules. The other roots proceed. What the issuer asked for IS done: the rider is named in the ledger entry on that function's leg, so the entry states what the apply carries rather than only what this cell authored. My reading, offered and not acted on: the asymmetry is INERT because the pair's hazard needs parse.py and nothing ships it, and settings.json is this function's own member for its own reason -- but the instruction was that the condition is the issuer's call, so it is the issuer's. The SETTINGS_PATH defect is a separate finding in a path this order holds; it is pre-existing in the live bytes, no deployed caller reaches it, and it is not fixed here because C4 says one deploy and this root is held."
  },
  {
    "id": "IRPT_BCKEND-W2-S39",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-12T03:20Z",
    "one_line": "A defect this cell INTRODUCED and has now removed: served.Entry held one cache dict for the MODULE'S lifetime, so a warm container served a payload computed from an artifact that had since changed -- authorization was never at risk, freshness was, and no better cache key could have fixed it because the boundary cannot see the artifacts its computes read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The PRD cell B3 is 'authorization enforcement on every route, warm-cache revocation' and its acceptance clause says 'a cached result or artifact is reauthorized before serving'. Enforcer.serve() implements exactly that and its docstring says so: both branches run resolve_now + covers before anything is returned, so there is no ordering in which cached bytes escape without a current decision.",
    "world_is": "The reauthorization claim is TRUE and was never the gap. What this cell added was the CACHE'S LIFETIME: served.Entry.__init__ did `self.cache = cache if cache is not None else {}` and handed that one dict to every Enforcer it built, so in a warm Lambda container every invocation shared it. The six functions had no such cache before this order (their handlers did not use Entry at all) and holdings' own make_holdings_enforcer passes cache=None, which gives the Enforcer a FRESH dict per request -- so this was a regression shipped tonight to six live functions. MEASURED, and found by accident by a holdings test: a snapshot whose node clocks collapse is refused NOT_READY when its case runs ALONE, and is SERVED when a valid request for the same (tenant, scope fingerprint, operation, params) ran first in the same process; clearing the cache made it refuse again. The cache key is _keys.cache_key(tenant, permitted_account_set_fingerprint, source_revision, schema_revision, config_revision, operation, params) -- it carries the tenant and the scope fingerprint, so NOTHING CROSS-FIRM was reachable, and it carries no artifact vintage, so a changed artifact was invisible. A BETTER KEY CANNOT CLOSE IT: source_revision was sitting at the module default 'src-1', a constant, and populating it from the directory artifact's as_of_business_date (done, and it also removed a second directory read) does not help when the artifact that moved is the SNAPSHOT, which the boundary never sees. An invalidation rule can only be as good as the inputs the invalidator can see.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/_authz/enforce.py:459-495@76ae1b20fb -- cache_key_for and serve, both branches reauthorizing",
        "infra/aws/lambda/investor-reporting/_keys/keys.py:459-472@76ae1b20fb -- the cache_key components; REVISION_RE at :57 admits an ISO date",
        "measured in process @76ae1b20fb: run 1 good snapshot served and cache size 1; run 2 node-clocks-stripped snapshot SERVED with no cache clear; run 3 same snapshot after cache.clear() refused NOT_READY",
        "infra/aws/lambda/investor-reporting/holdings/snapshot.py:266-279@76ae1b20fb -- make_holdings_enforcer(cache=None), the pre-existing per-request behaviour",
        "the fix, committed at e42495e8f1: Entry.shared_cache is None unless supplied and enforcer_for passes a fresh dict per request; the artifact vintage feeds source_revision"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "FIXED IN THE TREE at e42495e8f1 and INERT there; it is ARMED IN THE WORLD until C4's deploy ships it, because the six live functions carry the module-lifetime cache now. Bounded: within one warm container, an identical authorized request can be answered from a payload computed earlier in that container's life. No cross-firm or cross-scope reach, and every answer is still authorized against current inputs. Hazard read INERT rather than ARMED because the deploy that removes it is already ordered and scheduled as C4's single act, so nothing further is needed to disarm it than the act already owed. What is GIVEN UP by the fix is re-use across invocations, which nothing in this cell's spec asks for; what is KEPT is the warm-cache arm, exercised by supplying a shared cache explicitly as test_enforce and test_export already do."
  },
  {
    "id": "IRPT_BCKEND-W2-S40",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-12T03:20Z",
    "one_line": "The investor-reporting package's test suite cannot be run as a whole: a single pytest over the package reads 48 failed and 39 errors from cross-directory bare-name collisions, while every directory run on its own is green -- so any reader who runs the obvious command gets a false picture of the package.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Bound 12 and this cell's own practice take the REAL module as the subject, and routetable._import_entry documents the collision class in detail: five functions ship a top-level module under the same bare name because a deployed zip flattens one function's files into one directory, so in one interpreter the first to import wins and every later one silently gets the WRONG module.",
    "world_is": "The mechanism is known and handled INSIDE the census, and not outside it. Measured at this cut: `python -m pytest infra/aws/lambda/investor-reporting/ -q` reads '48 failed, 460 passed, 39 errors' WITH this worker's new test file deselected, so it is not caused by this order. Per-directory it is clean: _authz 131, _scope 50, _keys 45, _ids 29, directory 37, performance 28, narrative 37, export 68, ops 34, holdings 29, intake 15 -- all pass; _contracts reads 14 failed / 39 passed, and those are IB-rt-1's paired-consumer arms failing at test_seam_paired.py:374 on the consumer fixture's key shape, before any dispatcher call. This worker's own new file caused one instance of the same class in both directions and now cleans up after itself (it resolves its subject through routetable.entry_points(), by path, lazily), which is evidence that the trap is live rather than historical.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "timeout 900 python -m pytest infra/aws/lambda/investor-reporting/ -q --ignore=infra/aws/lambda/investor-reporting/holdings/tests @76ae1b20fb -> '48 failed, 460 passed, 39 errors'",
        "per-directory runs at the same commit, each printed green except _contracts (14 failed, IB-rt-1's, at test_seam_paired.py:374)",
        "infra/aws/lambda/investor-reporting/_authz/routetable.py:111-169@76ae1b20fb -- the purge that handles this inside the census, and its measured example (performance/entry.py got the DIRECTORY handler and raised AttributeError classified UNEXPECTED)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not this order's to fix and not fixed: the remedy is either a conftest per function directory that isolates sys.path and sys.modules, or a pytest invocation contract that says the package is tested per directory -- both are decisions about the whole package, spanning cells this order does not hold. Filed because the failing command is the OBVIOUS one: a seat that runs pytest over the package to check this project's health will read 48 failures that do not exist, and a seat that trusts a whole-tree green would be trusting an ordering."
  },
  {
    "id": "IRPT_BCKEND-W2-S41",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-12T03:20Z",
    "one_line": "Amendment 3 C1 grants the holdings paths in PROSE and the <paths> block does not carry them, so the lane gate refuses the commit -- C1's work is written, tested and PASSING in the worktree and cannot be committed until one line of <paths> changes.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "spec_asserts": "Amendment 3, C1: 'GRANTED, additive, for this cell only: infra/aws/lambda/investor-reporting/holdings/ and the holdings Terraform root.' The order's own lane clause says 'the <paths> block above IS the grant (RULING 1 @9ef9a40aae)', and ADHC_OWNPTH.005 says the order is the grant and a missing path is a cut defect, never an override.",
    "world_is": "The <paths> block at HEAD (76ae1b20fb, and unchanged at e42495e8f1) carries 23 entries and NEITHER infra/aws/lambda/investor-reporting/holdings/ NOR infra/aws/terraform/investor-reporting/holdings/ is among them. safe-commit refuses both files with 'agent=0.9.0_WK_IRPT_BCKEND~2 not in permitted_agents -- WORKER: no NON-TERMINAL task order at HEAD issued_to this serial names this path in its <paths> block'. The gate is CORRECT: it reads the machine-readable grant, and the amendment changed the prose. The work itself is complete and green: holdings/entry.py puts the shared boundary in front of snapshot.py without widening what any caller reaches, the Terraform root names entry.lambda_handler, holdings/tests/test_entry_guarded.py is 29 of 29 passing including a difference control and a refused-never-narrowed arm, and the census re-cut reads 'OK: every route is guarded' over 12 of 12 with the mark NOT loosened.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-2...md@76ae1b20fb -- the <paths> block, 23 entries, no holdings",
        "bash .tools/safe-commit.sh ... @76ae1b20fb -> 'ERROR: owned-paths lane violation(s) detected (block mode)' naming holdings/entry.py and holdings/lambda.tf",
        "timeout 300 python -m pytest infra/aws/lambda/investor-reporting/holdings/tests/ -q @worktree -> '29 passed'",
        "in-process census over the real table @worktree -> 'WHOLE FILE: OK: every route is guarded | routes: 12'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~B",
    "notes": "ARMED because the work sits UNCOMMITTED in a worktree: four files (holdings/entry.py, holdings/tests/test_entry_guarded.py, the _authz census re-cut, and the holdings lambda.tf re-point) exist only on this device's filesystem, and a worktree removal or a forced clean loses them. That is the hazard, and it disarms the moment the <paths> line lands and the commit is taken. NOT OVERRIDDEN: GIT_COMMIT_AUTHOR_OVERRIDE would have committed it and is exactly the escape the rule forbids. The _authz half of the same work WAS committed separately at e42495e8f1 because _authz/ IS in <paths>; the census re-cut is held with the holdings files deliberately, because committing a test that asserts 0 of 12 guarded without the entry module that makes it true would leave a failing test in the tree for everyone else."
  },
  {
    "id": "IRPT_BCKEND-S46",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-12T04:03:19Z",
    "one_line": "IB-rt-2 REACHED 15 of 15 ARMS WITH THE TOKEN PRINTING AND DID NOT FLIP, AND BOTH HALVES OF THAT ARE CORRECT. W2-S41 IS THE ISSUER'S DEFECT AND IS FIXED: amendment 3's C1 granted infra/aws/lambda/investor-reporting/holdings/ in a PROSE SENTENCE and never added it to the <paths> BLOCK, which is the surface the owned-paths lane gate actually reads, so the gate refused four files of finished work and THE GATE WAS RIGHT. Two lines added to <paths> at a3e84db9ef, verified present at the worker's own HEAD after its worktree was fast-forwarded to f27b6f4cc3 with its four uncommitted files confirmed intact before and after. A GRANT IS ONLY REAL IN THE SURFACE THE ENFORCER READS -- and this is the INVERSE of the failure /canonical-flow already warns about, where a DOCTRINE line routed an act through a seat the gate did not require and the cost was an invisible WAIT; here a doctrine line GRANTED what the gate does not read and the cost was an invisible REFUSAL. Same root, opposite direction: prose is not a grant and prose is not a gate. AND THE WORKER'S REFUSAL TO FLIP ON A PASSING TOKEN IS A FINDING IN ITS OWN RIGHT: the <paths> grant is LIVE ONLY WHILE THE ORDER IS NON-TERMINAL, so flipping would have RETIRED the grant and permanently orphaned C1's work -- A TERMINAL FLIP REVOKES THE GRANTS THE ORDER CARRIES, so the flip is the LAST act and never the act that frees you to finish. No face states that. Its second call is equally right: it did NOT hand holdings' Entry the shared loaders the other six use, because make_holdings_enforcer defaults ownership to _no_grant and wiring them would have turned a route that serves NOTHING into one that serves real holdings -- IB-rt-7's decision, not this cell's. A MARK MUST NOT WIDEN WHAT IT MARKS. W2-S38 RULED IN: IB-rt-11's intake/settings.json rider ships with the deploy and is NAMED IN THE LEDGER on the irpt-ycharts-generate leg, because an entry listing only the author's own changes understates what the apply carries. W2-S40 accepted INERT. W2-S39 IS THE ONE THAT CHANGES URGENCY: the cell introduced a stale-payload defect tonight and removed it IN THE TREE -- served.Entry held one cache dict for the module's lifetime, so a snapshot that must be REFUSED was SERVED from a prior request's payload -- and the fix is STILL ARMED ON THE SIX LIVE FUNCTIONS until a deploy ships it. Authorization was never at risk and the worker disclosed that plainly rather than minimising it. A known armed serving defect sitting in production while we sequence is a worse trade than any sequencing benefit, so the ONE deploy is now urgent rather than merely ready.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.9.0_WK_IRPT_BCKEND~2 under issuer amendment 5 -- the single deploy disarms W2-S39 on the six live functions and lands C1, the v0.14 envelope work, the post-read business_date emission and the named rider. Until that apply verifies, W2-S39 stays ARMED in the world and this row stays ARMED with it",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLOUD f27b6f4cc3 (drain of wk-irpt_bckend-2-2b; rows W2-S38..S41 and the 15-of-15 instance)",
        "the <paths> block at f27b6f4cc3 read in the worker's own worktree: both holdings paths present (absent at a3e84db9ef~1)",
        "proof-of-spec-check over IB-rt-2's instance: VALID rc=0, 21 of 21 rows resolving; RT2-AC1 PASS-by-output, token IBRT2-SIX-GUARDED, 15 of 15 arms",
        "the worker's own disclosure that arm (a)'s 0 of 12 reads uncommitted bytes from the filesystem and a clean checkout reads 1 of 12 -- printed ABOVE its own token",
        "issuer amendment 5 at a3e84db9ef (the <paths> fix, the W2-S38 ruling, the one-deploy instruction)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Issuer amendment 3, C1: 'GRANTED, additive, for this cell only: infra/aws/lambda/investor-reporting/holdings/ and the holdings Terraform root.'",
    "world_is": "That sentence existed only in prose. The <paths> block -- the surface .tools/git-hooks/install-owned-paths and the lane gate read -- did not name either path, so the grant had no effect on the only reader that matters and four files of completed work could not be committed.",
    "notes": "⭐ THE WORKER ALSO DID SOMETHING THIS ROUND HAS BEEN SHORT OF: its battery DISCLOSES ITS OWN WEAKNESS ABOVE ITS OWN TOKEN -- arm (a)'s '0 of 12' is read from filesystem bytes that are at no commit, and it prints that a clean checkout reads '1 of 12'. A passing token that names the condition under which it would fail is worth more than a passing token. Compare tonight's opposite cases: an arm that passed while printing '0 of 11' beside itself, and an instance that pinned bytes the record did not carry. Both of those were also caught by their own authors, which is the round's real pattern. To the L10 slug as a positive finding alongside the grant-revocation-on-flip property."
  },
  {
    "id": "IRPT_BCKEND-W3-S37",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-12T03:36Z",
    "one_line": "After a Terraform root is DELETED from the tree, `terraform state list` in its directory refuses with 'Backend initialization required -- Unsetting the previously set backend s3', writes NOTHING to stdout and exits 1 -- so an emptiness check that reads stdout alone PASSES on a command that never looked at the state.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED in infra/aws/terraform/investor-reporting/ycharts-research-20260911 after main.tf was deleted at cbc1e4e2fd: `.tools/terraform.exe state list` -> rc=1, 0 stdout lines, stderr 'Error: Backend initialization required, please run \"terraform init\"  Reason: Unsetting the previously set backend \"s3\"'",
        "the first version of battery_ib_rt_9.py arm (e) read `stdout.splitlines()` and printed 'research state key still reachable from this worktree: 0 resource(s)' -- the refusal rendered as a clean zero, and the check FAILED only because it also required rc==0",
        "the corrected instrument reads the STATE OBJECT itself: aws s3api get-object on s3://opal-313476888478-terraform-state/investor-reporting/ycharts-research-20260911/tfstate -> serial=13, resources=[] (0), which needs neither the deleted backend declaration nor terraform",
        "the battery now carries the refusal as its OWN check: 'e the retired instrument's refusal is DISTINGUISHED from an empty state: rc=1 with 0 stdout lines'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Decomposition v0.2 s.2 and TO-IB-rt-9 acceptance (e): the research root is absorbed and then 'deleted from the tree', with its resources under the ycharts root and `state list` printed -- i.e. a state listing remains the way to show which root owns what.",
    "world_is": "It does for the DESTINATION root and it does not for the deleted SOURCE root, and the failure is silent in the dangerous direction. Deleting the root removes the `backend \"s3\"` block that addressed the state, so terraform cannot reach the state it just emptied. This is PERMANENT and by design -- not a transient failure an `init` would fix -- so the instrument is retired rather than retried, and the emptiness of the source state is read from the tfstate OBJECT. The general form: any verification of a SOURCE state's emptiness that runs AFTER the source root is deleted must not use `terraform state list`, and any check that treats empty stdout as zero rows inherits this.",
    "notes": "INERT because the reading was correct here (0 resources, confirmed from the object) and because the check that would have been fooled never shipped green -- it failed on the rc leg. Recorded because the NEXT root retirement in this estate will meet the same refusal, and because the pattern is the same class this round keeps measuring: an error and a clean zero are indistinguishable on stdout, so a 0 must come with the exit code beside it."
  },
  {
    "id": "IRPT_BCKEND-W3-S38",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~3",
    "surfaced_at": "2026-09-12T03:36Z",
    "one_line": "The research root's S3 STATE OBJECT survives its root: the tree no longer declares ycharts-research-20260911 and nothing owns that state key, but the object is still there, empty, addressed by nothing.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws s3api get-object on s3://opal-313476888478-terraform-state/investor-reporting/ycharts-research-20260911/tfstate succeeds and returns a state document with serial=13 and resources=[]",
        "git ls-tree -r HEAD -- infra/aws/terraform/investor-reporting/ycharts-research-20260911 -> 0 files (2 at HEAD~2), so no root in the tree declares that backend key",
        "the change-management entry 20260912T0314Z_irpt-bckend-rt9_deploy_completion.md records the object as deliberately left in place"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-IB-rt-9 acceptance (e): 'the research root gone from the tree, its resources under the ycharts root' -- retirement of the root.",
    "world_is": "The root is gone and the state key is not. Deleting an S3 object is a destructive delete needing a human's word (CLAUDE.md Agent Autonomy), so this order left it rather than reaching for one, and it is inert on its own -- an empty state document nothing reads. What it IS: an orphan that no `terraform state list` can reach and no root will ever reconcile, and the kind of object a later census of 'state keys with no declaring root' would surface as a finding. Naming it here means that census finds an explanation rather than a mystery.",
    "notes": "The remedy, if one is wanted, is a one-line `aws s3 rm` on Andrew's word, or a documented convention that retired roots' state keys are left in place. Not this order's to choose. The same entry also records the 686 MB gitignored .terraform/ provider cache left in that directory in THIS WORKTREE ONLY -- no fresh checkout has it."
  },
  {
    "id": "IRPT_BCKEND-S47",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-12T04:10:15Z",
    "one_line": "IB-rt-9 ACCEPTED TERMINAL AT 6 OF 6 ARMS -- round 2 is 9 of 12, IB-rt-2 the only order still open. Issuer verification at HEAD rather than on the report: proof-of-spec-check VALID rc=0, 8 of 8 artifact rows resolved at pin with 4 CONTENT-resolved, 10 of 10 surprise rows resolving; and the arm (e) ledger's sentinel read ABSENT from org/critical_paths/.open_deploys/ so NEVER-2's half-landed state does not exist. ARM (e) IS THE STRONGEST WORK IN THE ROUND ON METHOD. It used `import` + `state rm` INSTEAD of `state mv`, because across two S3-backed states a `state mv` means hand-editing two pulled state files and a hand-edited state has no undo -- choosing the recoverable instrument over the convenient one. And it read non-destruction WITH A DIFFERENT INSTRUMENT THAN THE ONE THAT DID THE WORK: `describe-secret` and `describe-log-groups` both still return the objects, because `state rm` reporting 'Removed' is TERRAFORM DESCRIBING ITSELF and not the world. The only world change in the whole arm is tags_all gaining Project = OpalPortal on two resources, with Owner and Purpose carried verbatim. AND IT RE-OPENED AFTER ITS OWN FIRST FLIP, FOR THE MIRROR-IMAGE REASON TO IB-rt-11's: arm (e) took its baseline from HEAD~2, a RELATIVE ref that meant the pre-deletion commit when it was written and something else two commits later, so a fresh run read 'down from 0' and FAILED while the world was correct throughout -- THE INSTRUMENT MOVED, NOT THE WORLD. Re-opened on the record at 1f7edd7ef6, baseline made SELF-LOCATING (git log --diff-filter=D finds the deleting commit and the baseline is its parent), re-flipped at 6d5a801053 on a run verified to reproduce. A RELATIVE REF AS A BASELINE IS A MOVING TARGET and stops meaning what it said the moment anything lands after it -- including the arm's own commit and its own proof. W3-S37 accepted INERT and it is a false-green finding worth keeping: after a root is deleted, `terraform state list` in its directory REFUSES, writes NOTHING to stdout and exits 1, so an emptiness check reading stdout alone PASSES ON A COMMAND THAT NEVER LOOKED; the instrument is retired, emptiness is now read from the tfstate OBJECT, and the refusal is its own printed check. W3-S38 stays ARMED with this seat: the research root's S3 STATE OBJECT SURVIVES ITS ROOT -- empty, addressed by nothing, and LEFT IN PLACE because deleting an S3 object needs a human's word. RULED: it stays. It is named here so a later 'state keys with no declaring root' census finds an explanation rather than a mystery, and it is carried to L10 rather than turned into a second S3 delete request tonight.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO at L10 for the two items outside this lane: (i) W3-S38's orphaned S3 state object, which needs Andrew's word if it is ever to be deleted and is deliberately NOT being asked for tonight; (ii) the live ycharts-session-probe still running the RETIRED non-403 predicate on an ENABLED 6-hourly rule, because redeploying it needs infra/aws/terraform/ycharts-pipeline/ which NO order granted -- so SessionFresh=1 remains not evidence of anything and is cited nowhere in the cell",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLOUD 12d1cf85c0 (drain of wk-irpt_bckend-2-3b; rows W3-S37, W3-S38)",
        "proof-of-spec-check.py re-run by the issuer at HEAD: VALID rc=0, 8 of 8 artifact rows, 4 CONTENT-resolved, 10 of 10 surprises resolving",
        "org/critical_paths/.open_deploys/ listed at HEAD: 6 sentinels, NONE matching rt9 -- the arm (e) ledger is closed",
        "org/critical_paths/change_management/20260912T0314Z_irpt-bckend-rt9_deploy_completion.md -- 6 legs, OPEN sentinel at 244d3a968d before the act, CLOSE at cbc1e4e2fd before the grading reads",
        "the cell's commit chain including the reverted first flip 076bdb0973 and the reopen 1f7edd7ef6, left on the record"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Arm (e): the research root's resources move under the ycharts root's state, the research root is deleted from the tree, the host reads stopped, and the ycharts root's post-apply plan reads No changes.",
    "world_is": "All of that, proven leg by leg: pre-move plan 2 to add, two imports taking the ycharts state 17 -> 19, the research state object reading resources [], apply 0 added / 2 changed / 0 destroyed, post-apply No changes, host i-0167fd745ad906a66 stopped. The one residue is the empty S3 state object, named in W3-S38 rather than silently deleted.",
    "notes": "RECORD CORRECTION BY THIS SEAT, stated here because a commit message is part of the record and a wrong one is rot: commit 187ff36582 carries the CHANNEL ROW IRPT_BCKEND-S46 but reuses the message file written for issuer amendment 5, so its subject reads 'amend(IRPT_BCKEND IB-rt-2): my C1 grant was PROSE-ONLY...' while its diff is one insertion into INVESTIGATION_v1.md. The FACE amendment is the EARLIER commit a3e84db9ef; a reader looking for the <paths> fix at 187ff36582 will find the row instead. Not amended -- CLOUD is shared and rewriting it is worse than correcting it forward. THE TWO RE-OPENS TONIGHT ARE ONE FINDING FROM OPPOSITE ENDS: IB-rt-11 named BYTES the record did not carry, IB-rt-9 named a COMMIT that had moved. Both read rc=0 and PASS, both times the thing read was not the thing claimed, and both were caught by their own author after the flip. The habit that catches both is cheap and belongs in the worker face's standing mechanics next round: AFTER THE FLIP, RE-RUN THE INVOCATION AND READ `git status --porcelain`. Neither is in anybody's acceptance bar today."
  },
  {
    "id": "IRPT_BCKEND-W2-S42",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-12T04:51Z",
    "one_line": "The ycharts Terraform root now plans 0 to add, 0 to change, 2 to DESTROY -- a LIVE secret and a log group that IB-rt-9 removed from the configuration without applying -- so ANY apply of that root by any cell destroys another cell's resources, and that is a second and stronger reason the root was held than the E3 guard it was held on.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "spec_asserts": "Amendment 5: 'Any root whose plan shows more than your changes plus the named rider is a BLOCKING row and a stop', and the arm (e) bar is that each root's plan after the apply reads `No changes`. The first deploy of this cell recorded exactly that for the ycharts root on 2026-09-12T01:0xZ.",
    "world_is": "Read at 2026-09-12T04:4xZ, ycharts root, `terraform plan -lock=false`: 'Plan: 0 to add, 0 to change, 2 to destroy' with 'aws_cloudwatch_log_group.research_probe will be destroyed (because ... is not in configuration)' and 'aws_secretsmanager_secret.research_session will be destroyed (because ... is not in configuration)', plus 'Changes to Outputs: - absorbed_research_session_secret = \"ycharts/session/research-20260911\" -> null'. THE SECRET IS LIVE, not already deleted: describe-secret returns Name ycharts/session/research-20260911, ARN ...-FQCIve, DeletedDate null, with staged versions. PROVENANCE: `git log -- infra/aws/terraform/investor-reporting/ycharts/` names f83f73ce6c, 'L7(IRPT_BCKEND IB-rt-9) arm (a): the v0.9 cutover on every reader of ycharts/session/current' -- IB-rt-9 removed both resources from the root's CONFIGURATION and did not apply the root, so the STATE still holds them and the next apply reconciles by destroying them. This cell's own first deploy of that root read `No changes` AFTER its apply, so the divergence was introduced between that apply and now, by a commit that is not this cell's.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "terraform plan @36e4c5f70b in infra/aws/terraform/investor-reporting/ycharts -> 'Plan: 0 to add, 0 to change, 2 to destroy' naming aws_cloudwatch_log_group.research_probe and aws_secretsmanager_secret.research_session",
        "aws secretsmanager describe-secret --secret-id ycharts/session/research-20260911 -> DeletedDate null, ARN arn:aws:secretsmanager:us-east-1:313476888478:secret:ycharts/session/research-20260911-FQCIve",
        "git log --oneline -- infra/aws/terraform/investor-reporting/ycharts/ -> f83f73ce6c 'L7(IRPT_BCKEND IB-rt-9) arm (a): the v0.9 cutover on every reader of ycharts/session/current'",
        "org/critical_paths/change_management/20260912T0035Z_irpt-bckend-rt2_deploy_completion.md -- this cell's FIRST ycharts apply recorded a post-apply plan of 'No changes'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~B",
    "notes": "ARMED and the hazard is not this cell's to take: the next apply of that root for ANY reason destroys a live secret and a log group belonging to IB-rt-9's work, and a secret deletion is a human-confirmation act under this estate's own rules. NOT APPLIED BY THIS ORDER and nothing was rolled back -- the root was already held on the amendment 5 E3 guard (row W2-S38) and this is an INDEPENDENT second reason, found only because arm (e) re-read the plan rather than trusting the first deploy's recorded 'No changes'. A post-apply plan is a PERISHABLE claim: it was true when written and another cell's commit falsified it four hours later. WHAT IT COSTS THIS CELL, stated: irpt-ycharts-generate keeps the PREVIOUS served.py, so it alone lacks the v0.14 state-conditional envelope and the post-read business_date, and row W2-S39's cache-lifetime defect stays ARMED on that one function until this root can be applied. Two parties must move before it can: 2.0.0_SA_COO~B on the E3 guard, and whoever owns IB-rt-9's cutover on whether those two resources are meant to be destroyed."
  },
  {
    "id": "IRPT_BCKEND-W2-S43",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-12T05:22Z",
    "one_line": "MY OWN ROW W2-S42 MIS-ATTRIBUTED ITS CAUSE: the ycharts root's two pending destroys were not IB-rt-9 removing declarations, they were MY WORKTREE predating the commit that ADDS them -- `git log -- <path>` answers 'what last touched this path', never 'what changed this thing', and I read the top commit as the cause.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Row W2-S42, written by me at 2026-09-12T04:51Z, asserts: 'aws_cloudwatch_log_group.research_probe and aws_secretsmanager_secret.research_session ... IB-rt-9 removed both resources from the root's CONFIGURATION and did not apply the root, so the STATE still holds them', citing f83f73ce6c 'L7(IRPT_BCKEND IB-rt-9) arm (a)' as the provenance.",
    "world_is": "f83f73ce6c REMOVED NOTHING from that root: `git show --stat f83f73ce6c -- infra/aws/terraform/investor-reporting/ycharts/` prints one file, `iam.tf | 28 ++++++++`, additions only. The two resources were ADDED, not removed, at 244d3a968d in a NEW file `research_absorbed.tf` -- IB-rt-9's arm (e) absorbing them from the ycharts-research-20260911 root by import-then-state-rm, with every non-tag attribute read from `terraform state show` so the move plans as bookkeeping. `git log -S'research_probe' -- infra/aws/terraform/investor-reporting/` returns exactly ONE commit and it is that one. WHY MY PLAN SAW TWO DESTROYS: the shared S3-backed STATE already held both resources because slot ~3 had imported them, and `research_absorbed.tf` was NOT YET IN MY WORKTREE -- it arrived with the fast-forward to ad85e34384. Terraform compared a state that had them against a configuration that did not and correctly planned to destroy them. The gap was on MY side of the comparison. At the current HEAD the same root plans `No changes. Your infrastructure matches the configuration.`, and amendment 6 F2's instruction to RESTORE the declarations was a no-op because they were never gone.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show --stat f83f73ce6c -- infra/aws/terraform/investor-reporting/ycharts/ -> 'ycharts/iam.tf | 28 ++++++++++++++++++++++ | 1 file changed, 28 insertions(+)'",
        "git log --oneline --all -S'research_probe' -- infra/aws/terraform/investor-reporting/ -> 244d3a968d only, 'the research root's two live resources declared in the ycharts root'",
        "git cat-file -e HEAD:infra/aws/terraform/investor-reporting/ycharts/research_absorbed.tf @ad85e34384 -> PRESENT",
        "terraform plan in infra/aws/terraform/investor-reporting/ycharts @ad85e34384 -> 'No changes. Your infrastructure matches the configuration.'",
        "the same plan @36e4c5f70b -> 'Plan: 0 to add, 0 to change, 2 to destroy' (row W2-S42)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "THE CHANNEL IS APPEND-ONLY SO W2-S42 STAYS AS WRITTEN, and a reader must reach this row to know its provenance clause is wrong. WHAT SURVIVES OF IT AND IS STILL WORTH THE OWNER'S TIME: (1) the OBSERVED FACT was real -- that root genuinely planned to destroy a live secret holding two versions, and applying it at that moment would have destroyed it; (2) the issuer independently verified the secret is live before ruling, which was the right check on a destructive-class claim; (3) the LESSON the issuer drew -- re-read a plan immediately before any later apply to the same root and never carry a clean plan across another cell's commits -- is STRENGTHENED rather than weakened, because the thing that moved was not the world but MY VIEW of it: a stale worktree plus a shared state is a second, quieter way for a plan to be wrong, and it reads identically to the first. THE METHOD DEFECT, stated so it is not repeated: `git log -- <path>` answers 'what last touched this path'. It cannot answer 'what changed this thing', and its top entry is a NEIGHBOUR, not a cause. `git log -S<token> -- <path>` answers the actual question and named exactly one commit. I cited a neighbour and called it a cause, in a row that accused another cell of leaving a root un-appliable. No act was taken on the wrong attribution -- the root was held, which was correct for the other reason (W2-S38) and correct by luck for this one."
  },
  {
    "id": "IRPT_BCKEND-S48",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-12T05:45:08Z",
    "one_line": "IB-rt-2 ACCEPTED TERMINAL -- round 2 is 10 of 12, IB-rt-6 RELEASED and IB-rtb-1 gated only on it. All seven functions live on entry.lambda_handler, proof-of-spec VALID rc=0 over 23 of 23 rows, status flipped LAST after the verify, 6 open sentinels at HEAD and none this seat's. The third apply disarmed W2-S39, so the cache defect the cell introduced is no longer served anywhere. AND THE ISSUER MUST CORRECT ITSELF ON W2-S42. I relayed and AMPLIFIED a false causal claim: that the ycharts root planned two destroys 'because IB-rt-9 removed both from config at f83f73ce6c and never applied'. MEASURED NOW WITH MY OWN INSTRUMENTS: git show --stat f83f73ce6c shows iam.tf +28 lines and REMOVES NOTHING, and git log --diff-filter=A shows research_absorbed.tf was ADDED at 244d3a968d -- IB-rt-9's own arm (e) OPEN commit, declaring the research root's two live resources in the ycharts root BEFORE it touched state, exactly as NEVER-2 requires. IB-rt-9 DID THE RIGHT THING AND MY ROW ACCUSED IT OF THE OPPOSITE. The two destroys were real in IB-rt-2's plan and the cause was on ITS side: research_absorbed.tf was ABSENT FROM ITS WORKTREE while the shared state already held the imports. W2-S43 (the worker's own correction) and this row carry it; W2-S42 stands uncorrected in place as the append-only rule requires. MY FAILURE IS PRECISELY RULE 22's ORDERING AND I NAME IT AS THAT: the claim had TWO parts -- (i) the secret is live, (ii) the root's config omits it because IB-rt-9 removed it -- and I verified (i), which was cheap, true and DISPUTED BY NOBODY, then acted as though that verified (ii), which carried the whole accusation. describe-secret CANNOT DISTINGUISH THE TWO WORLDS: the secret reads live whether the config declares it or not. So DISCRIMINATION PASSED INSIDE A WRONG GRAIN -- my instrument agreed precisely about the half that was never in question. One git show would have cost three seconds and I did not run it because the row already read convincing. THE RULING ITSELF WAS STILL RIGHT AND NOT BY LUCK: refuse any plan carrying a destroy, restore rather than state rm, stop rather than improvise -- correct whatever the cause, because it keyed on the ACT's reachable state and not on whose fault it was. The restore turned out to be a no-op, nothing was destroyed, and the secret reads DeletedDate None. A ruling that does not depend on the cause survives getting the cause wrong; an ACCUSATION does not.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B (corrected same turn: the false cause is retracted here, 1.0.0_SA_CTO is told in its own message because it holds L10 and the claim named a completed cell, and nothing was done to IB-rt-9's work on the strength of it)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLOUD 781882e9d3 (final drain of wk-irpt_bckend-2-2b; rows W2-S43 and the terminal flip at c6bcccd551)",
        "git show --stat f83f73ce6c -> infra/aws/terraform/investor-reporting/ycharts/iam.tf | 28 ++ ; 5 files changed, 964 insertions, 115 deletions -- the declarations are NOT among the deletions",
        "git log --oneline --diff-filter=A -- .../ycharts/research_absorbed.tf -> 244d3a968d 'open(IRPT_BCKEND IB-rt-9 arm e): ... the research root's two live resources declared in the ycharts root'",
        "aws secretsmanager describe-secret --secret-id ycharts/session/research-20260911 -> DeletedDate ABSENT, 2 versions (true BEFORE and AFTER; it never discriminated)",
        "proof-of-spec-check over IB-rt-2's instance at HEAD: VALID rc=0, 23 of 23 rows resolving"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Issuer amendment 6 F2, committed at f4b229db52: 'the root really does plan to destroy a live secret plus a log group, because IB-rt-9 removed both from config at f83f73ce6c and never applied.'",
    "world_is": "IB-rt-9 ADDED those declarations in its pre-act OPEN commit. f83f73ce6c removed nothing. The plan's two destroys came from a stale worktree on the reading side, and the same plan output is produced by both causes -- which is why the output could not adjudicate between them and a git read could.",
    "notes": "⭐ THE WORKER'S METHOD CORRECTION IS THE REUSABLE PART AND IT IS SHARPER THAN MY APOLOGY: `git log -- <path>` ANSWERS 'WHAT LAST TOUCHED THIS PATH', NEVER 'WHAT CHANGED THIS THING' -- its top entry is a NEIGHBOUR, not a cause, and `git log -S<token>` named exactly one commit. A neighbour cited as a cause is how a row comes to accuse another cell. ⭐ AND ITS OTHER TWO FINDINGS EXTEND EARLIER ONES: a clean plan PERISHES IN TWO DIRECTIONS -- somebody else's commit, or your own stale worktree over a shared state -- and THE PLAN OUTPUT IS IDENTICAL, which is the fifth duplicated-fact divergence in that cell and the first that was a duplicated VIEW rather than duplicated data; and a PASSING ARM WAS PRINTING A SENTENCE THAT HAD BECOME FALSE (arm (e)'s hardcoded 'HELD ROOT ... not applicable by anyone' paragraph, after both halves were untrue), now a measurement instead of a paragraph -- A GREEN ARM IS NOT LICENCE FOR THE PROSE BESIDE IT. All three go to the L10 slug. Also for the slug: this cell withheld its flip at 15 of 15 THREE times -- once with four deliverables at no commit under my prose-only grant, once with one function still serving its own defect, once on my backwards guard -- because a terminal flip retires the <paths> grants the order carries. Two arms remain HUMAN-GATED rather than measured and the status line says so itself: 0 of 12 success responses measured, none claimed."
  },
  {
    "id": "IRPT_BCKEND-W2-S44",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-12T06:10Z",
    "one_line": "ARM (d) IS BLOCKED ON ONE NAMED DEPENDENCY, measured on the host: `import directory_runner` fails with ModuleNotFoundError: No module named 'ids', the bundle carries only the two runner files, no ids.py exists anywhere on the host, and all three remedies are out of this order's reach -- two by lane and the third by the estate's own one-normalizer law.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "The face's arm (d): 'THE HOST CAN RUN IT. The SSM run's stdout shows the runner's import check passing on the host (module names printed) -- or a BLOCKING row naming the missing dependency and this arm reads BLOCKED.' The L5 note adds that the runners reach first-party code by repo shape and that 'a missing dependency on the host is a BLOCKING row and arm (d) reads BLOCKED'.",
    "world_is": "MEASURED ON THE HOST, not inferred. mdpf-daily-runner i-02448edb624a7a7cf was started (it was `stopped`), reported SSM PingStatus Online, and ran one read-only AWS-RunShellScript (command id 15783da8-aea7-41b6-a000-b1557ad6f8f5, Status Success rc=0, writes confined to /tmp). Its stdout: python3 is 3.9.25; boto3 1.42.97, pandas 2.3.3 and jsonschema 3.2.0 ALL RESOLVE; a repo-shaped tree assembled from what is actually pullable (the minted tarball into data/assets/scripts/gold/investor_reporting/, the distributed trading_calendar.py into lib/) gives trading_calendar; and then `import directory_runner` prints IMPORT-FAIL: ModuleNotFoundError: No module named 'ids'. A bounded find over /opt /srv /home /usr/local/lib /var/lib returned NO ids.py anywhere on the host (it did find /opt/mdpf/scripts/gold/trading_calendar.py, so the calendar is genuinely distributed and the search works). WHY: directory_runner.py imports BOTH trading_calendar (line 108) and ids (line 115) at MODULE LEVEL, col 0, so the module cannot be imported at all without them, and it uses _ids.opaque at line 146 for the opaque-id normalization. The minted bundle carries EXACTLY TWO members, flat: directory_runner.py (45,676 B) and holdings_snapshot.py (74,684 B) -- verified by downloading it and listing the tar. THE THREE REMEDIES, EACH MEASURED OUT OF REACH: (1) add ids.py as a third bundle member -- the member list is a hardcoded dict in .tools/safe_deploy_core.py:233-246 and .tools/ is NOT in this order's <paths>; (2) distribute infra/aws/lambda/investor-reporting/_ids/ids.py to a host-readable code prefix -- that path is NOT in <paths>, and the assets_gold layer mapping only covers data/assets/scripts/gold; (3) copy ids.py into data/assets/scripts/gold/investor_reporting/, which IS in <paths> -- FORBIDDEN BY LAW, not by lane: ids is THE ONE opaque-id normalizer (IB-rt-3, CTO ruling 4) and irpt-holdings' own BUILD_MANIFEST.json states it is 'never vendored beside the function, because a second copy of either is the defect the layer exists to prevent'. Editing the runner to accept an injected normalizer is also refused by the face ('No runner is edited to change its import shape here').",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ssm get-command-invocation 15783da8-aea7-41b6-a000-b1557ad6f8f5 on i-02448edb624a7a7cf -> Status Success rc=0, stdout 'IMPORT-FAIL: ModuleNotFoundError: No module named ids' and 'OK: boto3 1.42.97 / pandas 2.3.3 / jsonschema 3.2.0'",
        "tarfile listing of s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz (ETag 964b4eef4f50792d4599e7df0d419486, 34476 B) -> 2 members, flat",
        "data/assets/scripts/gold/investor_reporting/directory_runner.py lines 108 and 115 (module-level, col 0) and line 146 (_ids.opaque)",
        ".tools/safe_deploy_core.py:233-246 -- the investor_reporting bundle's members dict, two entries",
        "comp-find --name ids.py --corpus default -> 2 hits, both under infra/aws/lambda/investor-reporting/_ids/",
        "infra/aws/lambda/investor-reporting/holdings/BUILD_MANIFEST.json -- 'never vendored beside the function, because a second copy of either is the defect the layer exists to prevent'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~B",
    "notes": "WHAT THIS BLOCKS AND WHAT IT DOES NOT. Arm (d) reads BLOCKED with the dependency named, which is the face's own provision rather than a failure of it. Downstream: arm (b) (three firms built for real, before/after revisions) CANNOT happen, because a runner that cannot be imported cannot build; arm (c)'s source-completion and new-revision arms depend on a successful build, while its missed-trigger and expiry arms do not. Arm (a) is NOT blocked by this -- the SSM dispatch can be written and PROVEN to dispatch, with a real command id on a real manifest, and the build's outcome is then an honest REFRESH_FAILED naming this dependency. The fix is one line of a member list or one distribution of one file, by a lane that holds .tools/ or _ids/; it is ten minutes of work for someone who may do it, and it is not ten minutes this order may take. NOT a defect of IB-rt-5's mint: the mint did exactly what it declared, both per-member shas verify against the repo bytes (directory-runner-sha256 1e8eb8a5... equals the repo file), and the bundle's two-member scope was the declared scope."
  },
  {
    "id": "IRPT_BCKEND-W2-S45",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-12T06:25Z",
    "one_line": "The completion manifest that refresh.py's own docstring calls 'the ONLY memory this cell has between fires' is NEVER PERSISTED and never read back: refresh.py contains zero references to boto3/s3/put_object, lambda_handler passes no last_manifest_as_of, so the MISSED-trigger detector is dead code in production and there is no manifest OBJECT for arm (a) to read.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "refresh.py:85 -- 'The completion manifest -- the ONLY memory this cell has between fires.' The face's arm (a): 'the deployed function's manifest after one driven fire reads build_dispatch: SSM with the command id'. The L5 note: 'read the runner's completion manifest, and record COMPLETED / FAILED / MISSED as the round-1 envelope already does'. The function's IAM grants s3:PutObject on <firm bucket>/investor-reporting/directory/_refresh/* with the comment 'writes ONLY the refresh manifests beneath them'.",
    "world_is": "THREE MEASUREMENTS, each a zero with its denominator printed. (1) comp-find 'put_object|boto3|s3' over infra/aws/lambda/investor-reporting/directory/refresh.py -> 0 hits across 1 file scanned. Over the whole directory package -> 5 hits across 7 files, ALL FIVE in handler.py (the directory SEARCH handler, lines 5, 84, 85, 382, 383); refresh.py and expiry.py carry none. So nothing in the refresh path can write an object. (2) comp-find 'last_manifest_as_of' over the package -> 7 hits: the def at refresh.py:144, its use at :155, the parameter at :165, the guard at :177 and the call at :178 -- and exactly ONE caller supplies it, tests/test_refresh_expiry.py:218. lambda_handler (:290-304) calls refresh_firm(firm_id, now, build_fn=None, correlation_id=...) and passes NO last_manifest_as_of, so the guard `if last_manifest_as_of is not None` is ALWAYS FALSE in production and the missed-fire branch is unreachable there. (3) The world agrees: `s3 ls --recursive` on investor-reporting/directory/_refresh/ in all three firm buckets returns NOTHING, while the function HAS been invoked (its log group carries a stream from 2026/09/11). So the IAM grants a write that no code performs, and the cell's memory does not exist.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-find 'put_object|boto3|s3' infra/aws/lambda/investor-reporting/directory/refresh.py -> 'DENOMINATOR: 0 hit(s) across 1 file(s) scanned'",
        "comp-find 'put_object|boto3' infra/aws/lambda/investor-reporting/directory -> 5 hits across 7 files, all in handler.py",
        "comp-find 'last_manifest_as_of' infra/aws/lambda/investor-reporting -> 7 hits; only caller supplying it is directory/tests/test_refresh_expiry.py:218",
        "infra/aws/lambda/investor-reporting/directory/refresh.py:290-304 -- lambda_handler, no last_manifest_as_of argument",
        "aws s3 ls s3://opal-data-{bd,cot,inf}/investor-reporting/directory/_refresh/ --recursive -> empty for all three",
        "aws logs describe-log-streams /aws/lambda/irpt-directory-refresh -> one stream 2026/09/11",
        "infra/aws/terraform/investor-reporting/directory/schedule.tf:157,178-185 -- the PutObject grant on _refresh/*"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "IN THIS ORDER'S LANE AND THIS ORDER FIXES IT: directory/refresh.py is in <paths>, the IAM already grants the write, and the missed-trigger arm cannot be real until the memory is. The fix is a persisted manifest write plus a read-back of the previous manifest into last_manifest_as_of. Filed rather than silently repaired because it changes what the face's arm (a) and arm (c) are measuring: before this, 'the deployed function's manifest' named an object that has never existed, and the MISSED arm was provable only in a test harness. NOT a defect of IB-s-4's design -- the envelope, the precedence rule and the subtraction-based detector are all correct and are what makes the fix small; what was missing is the durable half, and round 1 honestly recorded the build as NOT_WIRED so nothing downstream was relying on the manifest either."
  },
  {
    "id": "IRPT_BCKEND-W2-S46",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-12T06:25Z",
    "one_line": "The L5 note's 'dispatch via SSM, WAIT BOUNDED for completion, read the completion manifest' cannot fit the function it is for: irpt-directory-refresh has a 60-SECOND timeout and the measured cost of reaching an SSM-ready host from STOPPED is ~45s of polling before the runner does any work at all -- and the runner's own work is minutes of pandas and per-firm S3 loads.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "Decomposition v0.2 s.2, quoted by the face: build_fn becomes 'dispatch the minted directory_runner.py for one firm on one business date via SSM, wait bounded for completion, read the runner's completion manifest, and record COMPLETED / FAILED / MISSED'. The estate's named pattern is mdpf-accrual-trigger, which this cell is told to follow.",
    "world_is": "MEASURED. `aws lambda get-function-configuration --function-name irpt-directory-refresh` -> Timeout 60, MemorySize 512, declared at terraform/investor-reporting/directory/schedule.tf:133. The host mdpf-daily-runner i-02448edb624a7a7cf was STOPPED; in this worker's own probe the sequence start-instances -> state running took one 15s poll, running -> SSM PingStatus Online was satisfied on the first check, and send-command -> Status Success took one further 15s poll: roughly 45 SECONDS of polling for a command that did nothing but print, with the Lambda's entire budget being 60. The runner's real work is strictly larger: three distinct per-firm `load` implementations reading S3 sources (directory_runner.py:196, :257, :311, :335) plus pandas imports at :243, :258, :453 and jsonschema at :744. AND THE ESTATE'S OWN PATTERN DOES NOT WAIT: mdpf-accrual-trigger sends the command and RETURNS (lambda_function.py:118-136, 'synchronous on purpose: the SSM command status carries the script rc' refers to the SHELL being synchronous on the host, not to the Lambda waiting) -- so 'wait bounded' is not what the pattern this cell is told to copy actually does.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws lambda get-function-configuration --function-name irpt-directory-refresh -> '60 512 refresh.lambda_handler ... python3.12'",
        "infra/aws/terraform/investor-reporting/directory/schedule.tf:133 -- timeout = 60",
        "this worker's probe transcript: stopped -> running (one 15s poll) -> PingStatus Online -> send-command -> Status Success (one 15s poll)",
        "infra/aws/lambda/mdpf-pipeline/mdpf-accrual-trigger/lambda_function.py:118-136 -- send_command then return, no wait on the command",
        "data/assets/scripts/gold/investor_reporting/directory_runner.py:196,257,311,335 (per-firm loads), 243,258,453 (pandas), 744 (jsonschema)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~B",
    "notes": "THE DESIGN CHOICE IS NAMED RATHER THAN TAKEN SILENTLY, which is what G4 asks for. Three options and none is free: (1) raise the timeout toward 900s -- in this order's lane (the root is granted) but it makes a scheduled Lambda sit for minutes waiting on an EC2 boot, and it bills for the wait; (2) make the dispatch ASYNCHRONOUS like the pattern it is told to copy -- fits 60s, records build_dispatch: SSM and the command id immediately, and moves 'read the completion manifest' to the NEXT fire, which changes the cell's contract from one-fire-one-answer to two-phase; (3) a bounded wait INSIDE the 60s budget that records DISPATCHED-PENDING with the command id when the command has not finished, and reconciles on the next fire -- which is (2) with a best-effort fast path. I have implemented (3) because it is the only one that both fits the measured budget and still satisfies the face's own words for the fast case, but the CHOICE is the issuer's to confirm. AND THE G4 WINDOW, STATED: while row W2-S44 stands, a deployed dispatch cannot succeed, so every weekday 09:00 ET fire would start a shared EC2 host and record an honest REFRESH_FAILED. That is not a WRONG artifact -- the build genuinely failed and the manifest would say so with the dependency named -- and the start is safe (the mdpf chain's own 15:00Z run self-stops the host, and the trigger pattern starts it too). It is nonetheless a daily side effect on shared infrastructure for no product value, which is why nothing is deployed by this order until the issuer rules."
  },
  {
    "id": "IRPT_BCKEND-W2-S47",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-12T06:25Z",
    "one_line": "Arm (b) asks for a revision 'before and after (r -> r+1)' and for 'the previous revision object still present', but NO production directory artifact has ever existed for any firm: all three latest.json read 404 and investor-reporting/ holds only qa/ -- so the act is a FIRST MINT and the retained-previous-revision clause is vacuous by construction.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The face's arm (b): 'THREE OF THREE, BEFORE/AFTER. Per firm: the latest.json revision before and after (r -> r+1), the artifact hash differs, the previous revision object still present (head-object), the entry count with its denominator, 0 ids carrying `:acct:`.' The L5 note: 'the latest.json revision advances ... and the previous revision is retained (immutable revisions)'.",
    "world_is": "MEASURED WITH A POSITIVE CONTROL, because a 404 can be a permissions artifact rather than an absence. get-object on investor-reporting/directory/latest.json returns 404 for opal-data-bd, opal-data-cot AND opal-data-inf. `s3 ls s3://<bucket>/investor-reporting/` returns exactly one child for each -- `PRE qa/` -- so there is no `directory/` prefix under production at all. The control: `s3 ls s3://opal-data-bd/` lists many prefixes, so the credential reads these buckets fine. WHAT DOES EXIST IS QA, and it shows the runner works: investor-reporting/qa/directory/ carries two dated builds per firm (bd 2026-09-09 6,371,481 B and 2026-09-10 6,392,329 B; cot 2026-09-09 417,709 B and 2026-09-10 420,584 B; inf 2026-09-10 and 2026-09-11 450,726 B each) plus a latest.json pointer of 273-275 bytes for each. So `r -> r+1` has no r: the first production build mints latest.json and one dated object, and 'the previous revision object still present' cannot be shown because there is no previous revision. NOTE ALSO that the revision is not an integer: directory_runner.py:822 builds it as `irpt-dir/<firm>/<business_date>/1.0`, so an advancing revision is a CHANGED STRING carrying a new business date, never r+1 arithmetic.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws s3api get-object investor-reporting/directory/latest.json -> 404 on opal-data-bd, opal-data-cot, opal-data-inf",
        "aws s3 ls s3://opal-data-{bd,cot,inf}/investor-reporting/ -> 'PRE qa/' only, for all three",
        "POSITIVE CONTROL: aws s3 ls s3://opal-data-bd/ -> many prefixes listed, so the read works",
        "aws s3 ls s3://opal-data-{bd,cot,inf}/investor-reporting/qa/ --recursive -> two dated directory builds plus latest.json per firm",
        "data/assets/scripts/gold/investor_reporting/directory_runner.py:822 and :770-780 -- the revision string shape and the dated/latest key pair"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not a blocker on its own and not a defect of anyone: round 1 built to QA deliberately and the production prefix was always this cell's to first-mint. Filed because arm (b) is worded for an ADVANCE and the world offers a FIRST MINT, and those are different evidence: the before half is an ABSENCE (recorded here with its control), the after half is one dated object plus one pointer, and the immutability clause becomes provable only on the SECOND production build. A reader who takes arm (b)'s '(r -> r+1)' literally would look for an integer that does not exist in the revision grammar either."
  },
  {
    "id": "IRPT_BCKEND-W2-S48",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
    "surfaced_at": "2026-09-12T07:08Z",
    "one_line": "THE DEPLOYED REFRESH FUNCTION CANNOT RESOLVE A TRADING CALENDAR AT ALL -- its served zip carries four members and trading_calendar.py is not one of them -- so resolve_calendar() returns None, missed_business_dates() returns None, and every fire that HAS a prior manifest can only answer CALENDAR_UNAVAILABLE. Fixing the missing manifest write (W2-S45) does not reach this: it is the second half of the same dead detector.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "expiry.resolve_calendar's docstring: 'The trading calendar, or None. NEVER an approximation ... imported lazily and by NAME so this module can be read, imported and unit-tested in an environment that has no pandas_market_calendars -- which includes the Lambda runtime.' CLAUDE.md: 'One frontier: lib/trading_calendar.py'. The face's arm (c) requires a MISSED-trigger verdict on the real path, and refresh_firm reaches it only through missed_business_dates.",
    "world_is": "MEASURED ON THE SERVED ARTIFACT, not on the declaration, because those are different claims. `aws lambda get-function --function-name irpt-directory-refresh` -> Code.Location downloaded and listed: FOUR members, errors.py / expiry.py / handler.py / refresh.py, and NO trading_calendar.py. lambda-source-map.json declares the same four. So `import trading_calendar` inside resolve_calendar (expiry.py:116-128) raises and the except returns None -- deliberately, and honestly, but the consequence is that the deployed function has no calendar. THE CHAIN: resolve_calendar(None) -> None; missed_business_dates(...) -> None; refresh_firm's first branch then returns CALENDAR_UNAVAILABLE for any fire that has a last_manifest_as_of. Today that branch is unreachable for a second reason (W2-S45: nothing is ever persisted, so last_manifest_as_of is always None and the branch is skipped entirely) -- which is why the estate has never seen CALENDAR_UNAVAILABLE either. MEASURED AGAIN AFTER FIXING W2-S45 IN THE TREE: an offline probe with a fake S3 and a controlled clock ran three fires; fire 2 still read `previous: None` after fire 1 had written its manifest, because last_manifest() resolves the calendar FIRST and returns before touching S3. The two gaps mask each other and neither is visible from the other's side.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "zipfile listing of the SERVED irpt-directory-refresh artifact (downloaded from its own Code.Location) -> 4 members, trading_calendar absent",
        "infra/aws/lambda/ci/lambda-source-map.json, irpt-directory-refresh.files -> ['refresh.py','expiry.py','handler.py','errors.py']",
        "infra/aws/lambda/investor-reporting/directory/expiry.py:116-128 -- resolve_calendar returns None when the import fails",
        "infra/aws/lambda/investor-reporting/directory/refresh.py:144-160 -- missed_business_dates returns None when the calendar is unresolved; refresh_firm:177-190 turns that into CALENDAR_UNAVAILABLE",
        "offline probe with a fake S3 at this worktree: fire 1 wrote _refresh/2026-09-10/manifest.json, fire 2 still read previous=None"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "IN LANE AND THIS ORDER FIXES IT, by the same distinction amendment H3 drew for ids.py: declaring trading_calendar.py as a packaged member of this function RESOLVED FROM lib/trading_calendar.py is a DISTRIBUTION, not a second definition, and lambda-source-map.json is in this order's <paths>. A FILE COPY into directory/ would be a second copy of the estate's ONE frontier and is refused. NOT a defect of IB-s-4: expiry.py's lazy-by-name import with an honest None is the right shape for a module that must be unit-testable without pandas_market_calendars, and round 1 could not have seen this because the branch it feeds was unreachable for the OTHER reason. THE PAIR IS THE POINT: W2-S45 (no memory) and this row (no calendar) each make the missed-trigger detector dead, and fixing either alone leaves it dead -- which is exactly why a green arm on one of them would have been a false green."
  },
 {
  "id": "IRPT_BCKEND-W2-S49",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_BCKEND~2",
  "surfaced_at": "2026-09-12T09:41Z",
  "one_line": "THE SCHEDULED-GOLD HOST CANNOT BUILD ANY OF THE THREE DIRECTORIES AND CANNOT WRITE ANY OF THE THREE DESTINATIONS. Measured from the host's own identity, not from a policy read: 5 of 9 source prefixes the directory runner needs are AccessDenied to mdpf-daily-runner-ec2-role, and 3 of 3 destination prefixes are AccessDenied. The dispatch this cell builds is therefore correct and the BUILD behind it cannot land an artifact. The remedy is an IAM change on a role owned by another root and OUTSIDE this order's <paths>, so it is a BLOCKING row and not something this worker widens into.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "TO IB-rt-6 acceptance RT6-AC1 (b): 'THREE OF THREE, BEFORE/AFTER. Per firm: the latest.json revision before and after (r -> r+1), the artifact hash differs, the previous revision object still present.' The L5 note the order carries: 'The mechanism is the ESTATE's, not invented ... a trigger Lambda issues an SSM command to the mdpf daily-runner host ... that pulls the minted script ... and runs it with the host's own python and dependencies.' That note establishes the DISPATCH mechanism, and it is correct; it assumes without measuring that the host's own identity may read the three firms' identity sources and write the three firms' directory prefixes. The order's <paths> grants infra/aws/terraform/investor-reporting/directory/ and does not name any root that declares mdpf-daily-runner-ec2-role.",
  "world_is": "MEASURED ON THE HOST, BY THE HOST, at 2026-09-12 via SSM command fb070815-519e-4699-9a6b-193267476d25 (AWS-RunShellScript, read-only, /tmp only, Status Success rc=0). Caller printed by the run itself: arn:aws:sts::313476888478:assumed-role/mdpf-daily-runner-ec2-role/i-02448edb624a7a7cf. A POSITIVE CONTROL ran in the same sweep so a blanket failure could be told from a scoped one: s3://opal-data-mdpf/code/scripts/ READ-OK. READS THE RUNNER NEEDS (denominator 6 source prefixes + 3 destinations): READ-OK opal-data-inf/silver/api_dims/accounts_v2/; READ-OK opal-data-assets/blackdiamond/cottonwood/silver/fact_allocations/; READ-DENY opal-data-49financial/gold/advi/dimensions/dim_relationship/ (AccessDenied); READ-DENY opal-data-assets/blackdiamond/49f/silver/dim_account_xref/ (AccessDenied); READ-DENY opal-data-inf/silver/api_dims/representatives/ (AccessDenied); READ-DENY opal-data-inf/silver/api_dims/household_rep_mapping/ (AccessDenied). DESTINATIONS, 0 of 3 reachable: opal-data-bd/investor-reporting/, opal-data-inf/investor-reporting/ and opal-data-cot/investor-reporting/ are all AccessDenied -- opal-data-cot appears in the role's policy document not at all. THE POLICY READ AGREES WITH THE HOST'S OWN ATTEMPT, which is the second instrument: mdpf-daily-runner-ec2-role carries one inline policy (mdpf-runner-scoped) and one attached policy (AmazonSSMManagedInstanceCore); the inline document names opal-data-49financial in no statement, grants opal-data-inf only silver/api_dims/accounts_v2/*, gold/eclipse/*, silver/eclipse/*, orion/jwt/* and one gold timeseries object, and grants s3:PutObject on no firm bucket at all. ALSO MEASURED IN THE SAME RUN, and separately blocking the same build: the host has NO copy of any firm's runner_common.py (bounded find over /opt /home /srv -> 0 hits), and directory_runner.py instantiates one per firm BY REPO PATH in SourceSet.__init__ (data/assets/scripts/gold/runners_49f, data/inf/scripts/gold/runners_inf, data/cot/scripts/gold/runners_cot); the minted bundle investor-reporting.tar.gz carries exactly three members (directory_runner.py, holdings_snapshot.py, ids.py -- tar -tzf printed on the host) and none of them is a runner_common. THE THREE FIRM SOURCE TREES ARE ALSO OUTSIDE THIS ORDER'S <paths>. WHAT IS NOT BLOCKED, measured in the same sweep so the two are not confused: the host runs python 3.9.25 with boto3 1.42.97, pandas 2.3.3, jsonschema 3.2.0, pyarrow 21.0.0 and numpy 2.0.2; it is running and its SSM agent is Online; ssm:SendCommand from this seat reached it and returned Success. The DISPATCH half of this cell is buildable and is being built; the BUILD half is not.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "SSM command fb070815-519e-4699-9a6b-193267476d25 on i-02448edb624a7a7cf, Status Success rc=0 -- the READ-OK/READ-DENY table above is its verbatim stdout",
    "aws iam get-role-policy --role-name mdpf-daily-runner-ec2-role --policy-name mdpf-runner-scoped -- 26 statements, none naming opal-data-49financial, none granting s3:PutObject on any firm bucket",
    "aws iam list-attached-role-policies --role-name mdpf-daily-runner-ec2-role -> AmazonSSMManagedInstanceCore only",
    "data/assets/scripts/gold/runners_49f/runner_common.py: GOLD_BUCKET = 'opal-data-49financial', SILVER_BUCKET = 'opal-data-assets'",
    "data/assets/scripts/gold/investor_reporting/directory_runner.py:217-231, 300-310, 322-331 -- Firm49F/FirmINF/FirmCOT each _import_runner(<repo path>, 'runner_common') in __init__",
    "aws s3api head-object opal-data-mdpf code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz -> ETag a35420ac32cd714856db41fbcab5a073, source-repo-paths naming three files",
    "aws s3api list-objects-v2 on investor-reporting/directory/ in opal-data-bd, opal-data-inf and opal-data-cot -> None in all three (no production directory artifact exists yet in any firm bucket, so every build here is a FIRST MINT)"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "WHAT THIS WORKER DOES INSTEAD OF WIDENING. The order's own arm (d) already carries the branch this lands in: 'or a BLOCKING row naming the missing dependency and this arm reads BLOCKED'. So: the SSM dispatch, its least-privilege Lambda IAM, the dispatch/reconcile accounting and the arms that do not need a landed artifact are built and deployed; arm (b) and the two build-dependent halves of arm (c) read BLOCKED against this row and RT6-AC1 is reported FAIL rather than flipped. NO WRONG ARTIFACT IS REACHABLE BY THE WINDOW THIS LEAVES (the order's G4 question, answered rather than implied): after the deploy, a scheduled fire dispatches a command that fails on the host, and the runner's own _assert_destination plus the AccessDenied above mean nothing is written anywhere -- the fire records the dispatch, the NEXT fire reads the command's invocation status back and records REFRESH_FAILED with the command id. A RUNNING state is therefore perishable and cannot sit forever. THE REMEDY IS NOT MINE TO CHOOSE EITHER: extending a SHARED scheduled-gold host role to read three firms' identity dimensions and write three firms' investor-reporting prefixes is a cross-firm widening on a role other pipelines assume, and the standing bound puts that behind a named sign-off, not behind a worker's convenience. NOT A DEFECT OF IB-rt-5: the bundle it minted is correct for what it declared, and the ids.py member this worker added under amendment H3 resolved the import blocker it did have."
 }
]
```

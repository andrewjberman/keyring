# IRPT_BCKEND -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Opened by:** `2.0.0_SA_COO~B` at the L6 issuance (seat rows; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`,
identity, folder == project, the allocator coordinate). Lane `ANY`.
**Id grammar:** a worker's row is `IRPT_BCKEND-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that
coordinate); a seat's row is `IRPT_BCKEND-S<k>`; the CVO's adjudication rows live in `../adjudications/` as
`IRPT_BCKEND-C-S<k>`. **Append-only during the round.** Never edit an existing row. **Denominator at this write:** 39 rows, COUNTED not carried forward -- the MERGE of <branch> and CLOUD resolved as a strict UNION of both sides (37 ours + 27 theirs, 25 shared); no row dropped, no id duplicated.
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
  }
]
```

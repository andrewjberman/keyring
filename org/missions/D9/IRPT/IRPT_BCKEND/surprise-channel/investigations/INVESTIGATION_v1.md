# IRPT_BCKEND -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Opened by:** `2.0.0_SA_COO~B` at the L6 issuance (seat rows; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`,
identity, folder == project, the allocator coordinate). Lane `ANY`.
**Id grammar:** a worker's row is `IRPT_BCKEND-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that
coordinate); a seat's row is `IRPT_BCKEND-S<k>`; the CVO's adjudication rows live in `../adjudications/` as
`IRPT_BCKEND-C-S<k>`. **Append-only during the round.** Never edit an existing row. **Denominator at this write:** 65 rows, COUNTED not carried forward -- the MERGE of <branch> and CLOUD resolved as a strict UNION of both sides (64 ours + 54 theirs, 53 shared); no row dropped, no id duplicated.
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
  }
]
```

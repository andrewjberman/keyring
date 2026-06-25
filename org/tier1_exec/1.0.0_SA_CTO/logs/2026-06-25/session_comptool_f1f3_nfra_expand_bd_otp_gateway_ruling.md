# 1.0.0_SA_CTO -- comp-tool F1-F3 + NFRA_EXPAND PRD + SVG board + BD OTP gateway ruling

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, EXPLORE, COORDINATE, DIAGNOSE
**Window:** 2026-06-25 14:21Z -> 20:55Z (since last log @ commit 1c1eb9f54)
**Serial:** 1.0.0_SA_CTO | **Branch:** CLOUD

---

## Summary

Big multi-thread CTO window. Four arcs: (1) built the comp-tool use-path fills F1-F3
(Andrew-direct, from the day's 5-gap cluster); (2) consolidated F4+HEATMAP+MS-Cloud into
the NFRA_EXPAND macro and drafted its PRD with the hard privacy boundary + Andrew's 2
rulings; (3) rendered the HOT project board as an Opal-branded SVG and saved the renderer
into the /registry-check skill; (4) resolved the BD-49F durable-auto-login OTP-read
mechanism -- RULED app-reg OFF (Andrew-direct), the read goes through the existing OPLMCP
delegated gateway, grounded live via the m365 MCP tools.

---

## Work done (by arc)

### Arc 1 -- comp-tool use-paths F1-F3 (the gap cluster)
- **Design:** `docs/architecture/NFRA_COMPTOOL_USEPATHS.md` -- 4-layer model (L1 Discovery /
  L2 Coverage / L3 Composition / L4 Substrate); F1-F4 build order. (8447f028f)
- **F1 (732399014):** `org/modules/graph/comp_api.py` -- in-process python facade over the
  comp-tool CLIs (the L3 composition keystone). `run(tool,argv)` universal invocation
  (inspect-based main()/main(argv) dispatch, stdout capture) + structured accessors
  (routes/pipescript_threads/iam_analysis/pipeline_dag) + io/deployed convenience. Marked
  DONE in the use-paths doc (8b6d0d88f).
- **F2 (9f04f0ed5):** `org/modules/graph/pipeline_cli.py` -- `_autowalk_pipeline_for_script`
  added; a bare non-bd gold id now auto-resolves to its owning pipeline (MDPF/cot gap). The
  builder-dispatch was already present; the real gap was the id-resolver.
- **F3 (258d968bb):** `.tools/comp-freshness` -- `--raw` + `--max-age` on the artifact
  subparser for unregistered S3 prefixes (the aws_freshness gap). Verified on
  s3://opal-data-bd/forwardfill_v2/allocations/ (--raw -> RAW, --max-age 720 -> PASS).
- **Adjacent (ae63b4d24):** `comp-surface-check` egress-check limb (SNS subscriber
  deliverability, fail-closed, observe-only) -- commit-through for 0.7.0.

### Arc 2 -- NFRA_EXPAND (graph = SSOT for all Opal properties)
- **Consolidation (6d9aacaaa):** wrapped F4(auth-edge) + NFRA_HEATMAP + MS-Cloud/GraphAPI
  ingestion into ONE macro. Strands: A=EXPAND_MSCLOUD (SP+OneDrive ingest), B=EXPAND_AUTHEDGE
  (F4b auth-edge; F4a prefix-grain DROPPED), C=HEATMAP_OBJECT + HEATMAP_PROCESS.
- **PRD (294ab770a, 859200c7c):** `docs/architecture/NFRA_EXPAND_PRD.md` -- the HARD scope
  boundary (SharePoint+OneDrive document clouds ONLY; Outlook + ALL personal/P2P comms
  strictly off-graph, enforced in code; structure/metadata/access-topology not content) +
  3-phase sequencing + Entra-ID access-provisioning as a dedicated later phase. Folded
  Andrew's 2 rulings: (Q2) access-topology RETAINED = security-valid not privacy; (Q4) a
  SINGLE AWS Nessie graph, Andrew-only access now.
- Lanes: B->0.7.0_AE_CloudOps (Ph1); C-local->0.4.0_DE+DS+0.5.0_AE (Ph1); A->AE-cloud+m365
  owner (Ph2); C-global gated on A (Ph3).
- **OPEN (surfaced, unresolved):** HEATMAP_PROCESS duplicates NFRA_WRKFLW (both OPLMCP-traffic
  workflow-mining) -- offered Andrew the fold (supersede HEATMAP_PROCESS, NFRA_WRKFLW = the
  process arm); not yet answered.

### Arc 3 -- branded SVG project board
- Rejected the raw /registry-check output ("looks like shit") -> rendered the 22-HOT board
  /draw-style, then as an Opal-branded SVG on Andrew's desktop
  (`C:\Users\AndrewBerman\Desktop\opal_project_board.svg`, 1740x2247, valid XML).
- Styling pulled from `deck_generation/brand_spec/brand.json` (navy #163372, purple #5F3BE3,
  cool-grey, charcoal; Lato) + the KO-white interlock logo (paths inlined).
- **Saved the generator (77552687e):** `.claude/skills/registry-check/render_board_svg.py`
  (output-path now a CLI arg; docstring marks it a curated SNAPSHOT) + a "Branded SVG board"
  section in the skill's SKILL.md.

### Arc 4 -- BD-49F durable-auto-login OTP read (RULING + grounding)
- CVO reported both auto-login gates resolved (egress on native AWS IP, BrightData dropped;
  OTP mailbox = Andrew@opalinvest.com in-tenant) and pushed to provision an app-only
  Mail.Read app-reg + ApplicationAccessPolicy.
- I started down the app-reg path (verified M365-MCP-Graph app-only token: roles=None,
  mailbox AccessDenied -- app-only was NOT the configured mechanism). **Andrew corrected me
  twice:** "you shouldn't need to reprovision anything" / "use the GraphAPI by way of our mcp
  server to check my email."
- **Grounded live:** `mcp__m365__whoami` -> Andrew@opalinvest.com; `list_recent_email`
  returned the BD OTP directly (From "Black Diamond" noreply@bdreporting.com, subj
  "Authentication Code You Requested", body "Authorization code: <6digit>", 20:46:54Z).
- **CTO RULING (Andrew-direct, supersedes the app-reg plan):** the OTP read uses the EXISTING
  OPLMCP gateway (delegated-as-Andrew, server-side auto-refreshing token, Fernet
  opal/mcp/m365-fernet) -- NO app-reg, NO admin-consent, NO ApplicationAccessPolicy, NO new
  SM secret. Delegated-token-IS-Andrew's-mailbox = intrinsically single-mailbox (stronger
  scope than an app-policy clamp). CVO accepted + withdrew the app-only push.
- **Grounded config banked:** mailbox=Andrew@opalinvest.com, sender=noreply@bdreporting.com,
  subject="Authentication Code You Requested", regex `Authorization code: (\d{6})`.
- Routed the box<->gateway integration to COO (NFRA_OPLMCP lane) + the one real tradeoff:
  delegated=refresh-coupled -> a gateway-token liveness probe (COO accepted; 0.6.0 wires the
  box read; 0.5.0 confirms box-auth). Memory banked.

---

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| comp_api.py (F1, built) | L3 in-process facade over comp CLIs | BUILT -- self-routing accessors verified |
| comp-pipescript io/deployed | F2 auto-walk target (MDPF/cot id-resolve) | PASS -- bare id now resolves |
| comp-freshness (F3, extended) | --raw/--max-age on opal-data-bd/forwardfill_v2 | PASS -- RAW + max-age 720 PASS |
| comp-surface-check | egress-check limb + safe-commit gate (SVG commit) | PASS -- "no critical surface" on 77552687e |
| mcp__m365__whoami / list_recent_email | ground BD OTP read via the gateway (delegated) | PASS -- read Andrew mailbox, OTP present |

- **What worked:** the m365 MCP gateway grounded the entire BD OTP mechanism live in two
  calls -- decisive over the app-reg hypothesis. comp-surface-check rode the SVG commit clean.
- **What failed:** my app-only client-credentials test on M365-MCP-Graph (roles=None,
  AccessDenied) -- correctly a NEGATIVE result that disproved the app-reg framing.
- **Gap found:** none new in the comp toolchain this window; F1-F3 closed the standing gaps.
  Rail note: used raw `aws secretsmanager list-secrets` (discovery of IT-provisioned secrets
  Andrew said exist) + a one-shot token curl (external Graph verify) -- neither has a comp-tool
  surface (SM secret inventory + MS token endpoint are off-graph), operational-discovery.

---

## Blockers

None. The BD app-reg "gate" CVO flagged dissolved (gateway is the mechanism, no provisioning).

---

## Current State (handoff)

- **comp-tools:** F1 `comp_api.py`, F2 `pipeline_cli._autowalk_pipeline_for_script`, F3
  `comp-freshness --raw/--max-age` all committed + DONE in NFRA_COMPTOOL_USEPATHS.md. F4 is
  re-homed into NFRA_EXPAND Strand B (EXPAND_AUTHEDGE), not a standalone.
- **NFRA_EXPAND:** PRD complete at `docs/architecture/NFRA_EXPAND_PRD.md` (+ _SCOPING.md). All
  5 project JSONs registered (NFRA_EXPAND, EXPAND_MSCLOUD, EXPAND_AUTHEDGE, HEATMAP_OBJECT,
  HEATMAP_PROCESS; NFRA_HEATMAP superseded). Ready for COO decomposition. UNRESOLVED:
  HEATMAP_PROCESS<->NFRA_WRKFLW dedup (Andrew not yet answered).
- **SVG board:** renderer at `.claude/skills/registry-check/render_board_svg.py` (snapshot,
  data hand-curated 2026-06-25); regenerate via `python ...render_board_svg.py [out.svg]`.
- **BD OTP:** mechanism = OPLMCP gateway delegated. Config grounded (above). Owners: 0.6.0
  (box->gateway wire), COO (gateway endpoint + token-liveness probe), 0.5.0 (box-auth). NOTE:
  .bd.identity cookie DEAD since 19:33Z (SNS alarms ~5-15min) -- reseed time-sensitive; manual
  paste stays the 22:30Z GO floor, gateway auto-auth is the parallel bonus. Secret VALUES for
  M365-MCP-Login/Graph were pasted cleartext this session -> flagged to CVO for rotation call.

---

## Next Steps

- [Andrew] resolve HEATMAP_PROCESS<->NFRA_WRKFLW dedup (CTO offered the fold).
- [2.0.0_SA_COO] decompose NFRA_EXPAND (Strand B->0.7.0 first); own the gateway-token
  liveness probe + box<->gateway OTP contract.
- [0.6.0_AE] re-point getOtpCode to the OPLMCP gateway delegated call (drop app-reg path).
- [3.0.0_SA_CVO] cert "delegated via gateway, Andrew's mailbox, structurally single"; rotation
  call on the cleartext M365-MCP-* secrets.

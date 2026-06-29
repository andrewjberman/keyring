# 0.7.0_AE_CloudOps~B (B lane) -- R8-PRIV close, G2 cut-1 oracle + derive-gap finding, close-time-flip spec, MCP-auth grounding for Andrew

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, COORDINATE

## Window
Since the last log (10eb7b089). 3 commits + 1 grounded-investigation (no-commit) + a live G2 PASS-2 interim. Driven via COO/CVO/base broker; tail of the window = direct Andrew Q&A on the MCP gateway auth state.

## Work done

1. **NFRA_OPLMCP.R8-PRIV -- CLOSED, all 4 ACs (8d381884e).** My own privacy catch driven end-to-end: surfaced the P2 (gateway audit-lake args unredacted = scope-dependent privacy) -> CTO ruled the policy (fail-closed per-tool args-field allowlist) -> I built it (838d8790b, audit.py _safe_args) -> base-AE deployed it (on-box md5-confirmed) -> CVO independently served-verified (NEVER#7): called list_recent_email (undeclared, content-bearing) on the LIVE gateway returning a REAL sensitive email (subject/account/allocation); the Athena audit row showed args={"_omitted":"args fail-closed..."} -- ZERO leak, metadata-only; declared tools still log normally. Structurally closes the gap; the 3-tool scope-hold LIFTS (any tool now safe-by-fail-closed). COO RAVC2-ACCEPT.

2. **NFRA_COMPAWS.PHASE-0 G2 cut-1 edge-census ORACLE increment-1 (8b915f081) + a live derive-gap finding.** Built an INDEPENDENT live boto3 enumerator (g2_edge_oracle.py -- deliberately NOT comp_aws_cli, so PASS-2 diff is non-circular) + the generated census (g2-edge-census-cut1.yaml): 212 ASSUMES + 31 IN_SG + 21 SG nodes. The SG census makes the "0 world-open non-web SG" assertion CERTIFIABLE (exactly 1 world-open SG = m365-mcp-gateway-alb-sg 80/443 = WEB/ALB -> 0 non-web). CVO PASS-2 interim surfaced the cert is gated on a fresh derive (live graph built 14:05Z predates the 15:28Z increment); inline derive_edges() timed out >180s. CORRECTED CVO's framing: 8b915f081 added the ORACLE only (NOT a derive change), so the 196-vs-212 + IN_SG gaps are candidate REAL derive gaps, not pre-increment artifacts. Concrete finding flagged: the derive emits LAMBDA-[IN_VPC]->SG (Lambda-only, edge_type IN_VPC) and does NOT emit EC2->SG at all -> ~30 EC2->SG edges are a genuine derive blast-radius gap (+ an IN_VPC-vs-IN_SG naming reconciliation). To unblock PASS-2: I'll provide a fast scoped ASSUMES+IN_SG derive run (avoid the full-estate timeout) or trigger the globgrph re-derive.

3. **Close-time-flip durable-fix SPEC (b694340a0, COO BANK 191217Z).** docs/briefs/close-time-to-status-flip-durable-fix-proposal-20260629.md -- two mechanisms for the registry-open-but-landed gap (the SFN-FIX + R8 class): (a) close-commit-flips-TO gate in safe-commit (event-driven, WARN-degrade for owned-paths), (b) /drive periodic to-check-vs-LIVE pass (catches the no-marker class). Recommend both-layered (mirrors LAMBDAMAP prevent+detect). Decide-before-build; routed COO+MSTR.

4. **MCP gateway auth -- grounded state for Andrew (no commit; investigation).** Andrew asked where "MCP auth at the edge" stands. Grounded from NFRA_OPLMCP project records + the CVO 06-23 delivery-structure/auth assessment: the original ALB-cookie-OIDC edge auth did NOT fit native MCP clients (need OAuth 2.1 Bearer, not cookies); the fix SHIPPED as OPLMCP .06 Model-B (gateway-as-OAuth-AS facade, Bearer-on-/mcp + ALB path-rule bypass), LIVE at gateway v1.3.0. OPLMCP is build-complete but Andrew-gated/de-prioritized; the only open items are 3 Andrew-actions (synthetic test mailboxes for per-user isolation cert, AC5 Claude-for-Work data-terms sign-off, Andrew's own connect e2e). Advised dropping the "portal-wrap (Structure C)" framing (Andrew's correct push-back: serverless portal is a poor host for the stateful EC2 broker; C is a different product, not a better auth path). OFFERED a live smoke-test of the gateway /mcp bearer challenge (pending Andrew's go).

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| boto3 enumerator (g2_edge_oracle.py) | live ASSUMES+IN_SG+SG census | PASS | 212/31/21; independent of comp_aws_cli by design (non-circular oracle) |
| ds-commit-gate.sh | g2_edge_oracle.py | PASS | py_compile+ruff clean |
| comp-kuzu (via CVO) | STATE_MACHINE/edge counts | PARTIAL | graph 14:05Z is pre-increment (ASSUMES=196/IN_SG=0); cert gated on fresh derive |
| aws (athena/glue/ec2/lambda/iam/sfn/ecs) | R8-PRIV AC4 + G2 enumeration | PASS | rail-checked markers (oracle MUST be raw-aws-independent; gateway-internal/Glue/cert-brief have no comp-tool) |

**What worked:** the independent oracle is doing its job -- caught a real derive gap (EC2->SG missing) on its first PASS-2. **What failed:** the full derive_edges() inline run (>180s full-estate) -- need a scoped path for the cert. **Gap found:** derive emits IN_VPC (Lambda-only) not EC2->SG -- a blast-radius coverage gap routed to CVO/CTO.

## Files Modified
see commit messages: b694340a0 (close-time-flip spec), 8d381884e (R8-PRIV TO close), 8b915f081 (g2_edge_oracle.py + g2-edge-census-cut1.yaml).

## MCP traffic
~10 broker messages. Significant: CVO AC4 served-verify SIGN (R8-PRIV close); COO RAVC2-ACCEPT R8-PRIV + close-time-flip BANK + G2->COMPDRIFT-TO-2 queue; CVO G2 PASS-2 interim (re-derive gate) -> my correction (real-gap-not-artifact); peer 0.8.0_AE_CloudComp~B no-double check on G2-inc-2 (confirmed mine). RAVC open: G2 PASS-2 (gated on fresh derive).

## Current State (handoff)
- **R8-PRIV:** CLOSED (all ACs, CVO-signed). Gateway audit fail-closed args-allowlist LIVE; scope-hold lifted.
- **G2 cut-1 increment-1:** LANDED (8b915f081). PASS-2 GATED on a fresh derive (graph 14:05Z < increment 15:28Z). Real derive gap flagged: comp_aws_cli derive_edges emits LAMBDA-[IN_VPC]->SG only, MISSES EC2->SG (~30 edges) -- a blast-radius gap for CVO/CTO. NEXT: provide a fast scoped ASSUMES+IN_SG derive (or trigger globgrph re-derive) so CVO diffs oracle-vs-derive.
- **G2 increment-2** (role->bucket GRANTS policy-parse): MINE (confirmed vs 0.8.0_AE_CloudComp~B); PACED on increment-1 PASS-2 (the derive-gap picture may reshape it).
- **OPLMCP MCP auth:** build-complete + LIVE (v1.3.0, Model-B); only Andrew-gated items remain. Live smoke-test OFFERED to Andrew, pending his go.
- **COMPDRIFT TO-2** (comp-drift orchestrator): COO authors the stub when I'm ~clear of G2.
- **Close-time-flip spec:** routed COO+MSTR, decide-before-build.

## Next Steps
- [0.7.0_AE_CloudOps~B] provide the fast scoped derive (or trigger globgrph re-derive) -> unblock CVO G2 PASS-2.
- [3.0.0_SA_CVO] run G2 PASS-2 (oracle-vs-derive diff + SG-assertion) once the derive reflects the increment; adjudicate the EC2->SG derive gap.
- [Andrew] OPLMCP 3 gated items (test mailboxes, data-terms sign-off, connect e2e); + go/no-go on the gateway live smoke-test.
- [2.0.0_SA_COO + MSTR] decide the close-time-flip mechanism.

## Blockers
None hard. G2 PASS-2 is gated on a fresh derive -- actionable by me (scoped derive / re-derive trigger), not a blocker.

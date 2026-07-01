# NFRA_INTEGRATIONS — canonical project proposal (Andrew-direct → CTO to create)

**Author:** 0.5.0_AE_OpalETL | **Sovereign:** Andrew (directed 2026-07-01) | **Create-as-project:** 1.0.0_SA_CTO (PRD + JSON, arch-lane) | **CC:** 2.0.0_SA_COO (registry), 0.7.0_AE_CloudOps (gateway owner-of-record + INTEGRATION_FRAMEWORK.md author)
**Type:** project-creation proposal (mirrors the SCTY flow — I author the scope; CTO creates the formal project + PRD).

## 0. Andrew directive (verbatim intent)
> "promote integration framework to CTO and let's have them make a canonical NFRA_INTEGRATIONS project and we get a process in place for **implementation, governance, and storage**."

Create **NFRA_INTEGRATIONS** as the canonical project-of-record for external-source MCP integrations, spanning the three pillars. Promote the gateway-local `INTEGRATION_FRAMEWORK.md` to a formal `docs/architecture/` standard and fill the storage-schema gap.

## 1. Why now
The MCP gateway generalized from M365-Graph-only to a registrable multi-source model (YCharts landed 2026-07-01, dormant; kuzu/nessie/iceberg charted next). The implementation framework EXISTS but is gateway-local + informal; governance is per-integration-ad-hoc; storage/bucket/dependency schema is CONVENTION, not canonical. As the integration set grows, formalize the spine now (before N integrations calcify N conventions).

## 2. Current state (grounded)
- **Implementation: EXISTS, informal.** `infra/aws/ec2/m365-mcp-gateway/INTEGRATION_FRAMEWORK.md` (v1, 0.7.0): the `IntegrationSpec` schema (id / auth_kind / tool_prefix / secret_id / read_only / min_tier / hosts), the `app/integrations/<id>/` package layout + `registry.py`, the 5-step add process, fail-closed enablement (`ENABLED_INTEGRATIONS` default empty), the 3 AuthKinds (DELEGATED_USER / SHARED_SECRET / NONE). GAP: lives with gateway code, NOT a `docs/architecture/` standard (0.7.0 flagged this as a CTO-lane promotion).
- **Governance: PARTIAL/ad-hoc.** CTO arch-gates each integration (new egress + tool surface on the SEV1 box) — real but not codified as a repeatable gate. SCTY tier alignment exists as a HOOK (`min_tier` in the spec; enforcement wired now that the SCTY guard is live). Credentials follow the Third-Party Data Standard §3 (SM-only, HAR→C6). GAP: no single governance doc binding these.
- **Storage: CONVENTION, not canonical.** Per-firm buckets (`opal-data-{bd,cot,inf,mdpf,schwab}`) + medallion (`01_raw`/`silver`/`gold`/`platinum`) + shared artifact buckets — firm-separation is hard-gate+IAM-enforced, but there is NO single canonical bucket/dependency-schema doc. Integration DEPS are in-package on the gateway EC2 venv (NOT Lambda layers); integration CREDENTIALS are per-integration SM secrets. GAP: where integration-pulled DATA lands (if persisted), the namespace/bucket rules, and the dependency-org rule are undocumented.

## 3. Proposed NFRA_INTEGRATIONS scope — the 3 pillars

### Pillar 1 — IMPLEMENTATION (the framework, formalized)
- Promote `INTEGRATION_FRAMEWORK.md` → `docs/architecture/NFRA_INTEGRATIONS_PRD.md` as the standard (keep a pointer in the gateway tree). The `IntegrationSpec` schema + `app/integrations/<id>/` layout + `register()`/`registry.py` + `run_integration_tool()` audited path = the canonical implementation contract.
- The 5-step add-an-integration process becomes the mandated checklist (author → register → provision secret → grant IAM → enable+deploy).

### Pillar 2 — GOVERNANCE (repeatable gate + ownership)
- **Per-integration CTO arch-gate** codified: new egress (hosts allowlist) + new tool surface on a SEV1 box + the secret/IAM grant = the gated change; read-only-by-default (no destructive guard needed); a mutating capability is an explicit escalation.
- **SCTY_MCPGUARD alignment** (now live): every integration call resolves caller identity → tier → enforce `spec.min_tier` in `run_integration_tool()` (the hook is in place; wire it to the deployed guard). Read-only integrations carry no destructive capability by construction.
- **Fail-closed enablement** as the standing safety: code ships dormant; enabling is a deliberate arch-gated deploy (env + IAM), never a config flip.
- **Ownership model:** gateway owner-of-record (0.7.0/CloudOps AE) owns the box + deploy; the integration author builds under the framework; CTO arch-gates; CVO live-certs a new integration's read-only + audit + tier behavior.
- **Third-Party Data Standard §3** for all credentials (SM-only, never git/logs/messages; HAR→C6 for browser sessions).

### Pillar 3 — STORAGE (the canonical schema — the net-new to author)
The gap to fill. Define, canonically:
- **Code:** `app/integrations/<id>/` (spec + integration + client), namespaced `tool_prefix` per integration.
- **Dependencies:** gateway-EC2 = in-package + the gateway venv (NOT Lambda layers — different from the pipeline Lambdas' layer/layer-map model; document BOTH models + when each applies). A new heavy dep is a gateway-venv + deploy concern, arch-noted.
- **Credentials:** one SM secret per integration (`<source>/credentials`), IAM `GetSecretValue` scoped to that ARN on the gateway role.
- **Data (if persisted):** the canonical bucket rule for integration-pulled data — per-firm/medallion convention + firm-separation (an integration must NOT cross firm buckets); where a persisting integration's artifacts land + the naming. (YCharts is read-only-passthrough today; kuzu/nessie/iceberg are read-only in-estate; a future persisting integration needs this rule.)
- **Egress:** the `hosts` allowlist per integration = the network-egress governance basis.

## 4. Ask to CTO
1. Create **NFRA_INTEGRATIONS** (project JSON `org/projects/NFRA_INTEGRATIONS.json` + REGISTRY row — COO) as an NFRA-macro platform project.
2. Author/promote **`docs/architecture/NFRA_INTEGRATIONS_PRD.md`** = the promoted INTEGRATION_FRAMEWORK.md (Pillar 1) + the codified governance (Pillar 2) + the canonical storage/dependency/bucket schema (Pillar 3, the net-new).
3. Relationships: references NFRA_OPLMCP (the gateway), NFRA_MSGRAPH (the delegated-user native source), SCTY_MCPGUARD (the tier gate — now live), the Third-Party Data Standard, and DATA_PLATFORM (the bucket/firm-separation convention it makes canonical for integrations).
4. Lanes: CloudOps/AE (gateway + framework), CTO (arch-gate + the PRD), CVO (per-integration live-cert), COO (registry + decomposition).

**Offer:** I (0.5.0) can draft the Pillar-3 storage/dependency/bucket schema section (the net-new) since I just mapped the bucket/dependency reality this session — hand it to CTO for the PRD. Andrew directed this to me; issuing to CTO for the formal project creation.

*Grounded 2026-07-01 against INTEGRATION_FRAMEWORK.md, app/integrations/, the bucket/firm-sep convention, LAMBDA_DEPLOYMENT_PROTOCOL layer model, Third-Party Data Standard. Author: 0.5.0_AE_OpalETL.*

# ADHOC.unmanaged-lambdas-adoption — seven unmanaged Lambdas: 4 adopted (zero-diff), 3 dossiers routed

**archetype:** MIXED (TRACE/VALIDATE/DEPLOY)
**Agent:** 0.7.0_AE_CloudOps~E · **Session:** 2026-08-04 ~2215Z–0020Z · **TO:** ADHOC.unmanaged-lambdas-adoption (COO; CTO framework 170852Z + rider 170951Z; re-spawn on COO GO 220025Z)

## What happened

Startup per org/XXX.md (re-registered PID 25312, Monitor bmtmdy1gw, PATH 94/95 + forwarder exercised,
inbox both-probes empty, TO scan via to-check --all). CRO consult fired FIRST (blocking only the
research pair) and answered in 6 minutes (222913Z). All seven functions grounded on live primitives;
coldness discriminator separated them 4 HOT / 3 cold with zero ambiguity:

**ADOPTED (import + TF-adopts-live, import-then-plan-ZERO-DIFF proven, per NFRA_TERRAFORM-P2):**
- access-anomaly-scanner, cost-anomaly-scanner, security-sweep-comprehensive -> NEW module
  `infra/aws/terraform/security-ops/` (24 resources imported; plan "No changes";
  tag security-ops-v0.1.0). Tagless provider deliberately — default_tags would have broken the
  zero-diff gate. Role tags on security-sweep-dedicated-role transcribed verbatim after the first
  plan caught my omission (the instrument found my own error — that is the gate working).
- finbert-batch-processor -> `news-pipeline/finbert-batch.tf` via untagged provider alias
  (8 resources; targeted plan "No changes"; tag news-pipeline-finbert-adopt-v1). CRO: KEEP.
  Name-stem guard carried verbatim in the TF file, the verdict table, and the source map.
- NO APPLY OCCURRED and none was pending: imports mutate state only; both plans read "No changes",
  so DELTA=0 by construction. Deploy-completion ledger not opened — no deploy began.

**DECOMMISSION-CANDIDATES (dossier-only, routed to CTO; nothing deleted):**
- opal-bd-transaction-consolidator — dangling S3 permission (bucket notification does not reference
  it), 0 inv/30d, last log 2026-02-09. Shared-role caveat recorded (bd-processor-lambda-role heat
  is OTHER fns; role must never be part of any decommission).
- schwab-anonymizer — zero triggers, zero retained log events, role unused since 2025-12-11.
  Guard-vs-stillborn undecidable from metrics (PII anonymizer = plausible rare-event instrument);
  49F/Schwab owner consult recommended before ruling.
- sentiment_query_api — sole trigger points at DELETED API Gateway cxm5b58nme (NotFoundException);
  CRO: no research consumer. Strongest candidate.

**Routed finding AAS-ERR:** access-anomaly-scanner errors 353/983 inv/30d — the scan runs, the
ALERT DISPATCH leg fails hourly (SSM SendCommand -> moltbot i-0b784d4908e320fc4 InvalidInstanceId;
instance stopped/SSM-dark). Access-anomaly alerts silently dropped. Same dispatch dependency in
cost-anomaly-scanner is untested-cold, not proven-good. Surfaced as owned finding, NOT fixed in-TO,
NOT an alarm-build (moratorium respected).

## Compiler Tools

| Tool | Invocation | Result | Notes |
|---|---|---|---|
| comp-which | "how do I grep the repo" (A.3 exercise) | forwarder RAN | PATH probe: 94/95 resolve bare |
| comp-debris | --days 30 --types lambda (+ --json) | 196 lambdas banded: my 4 HOT / my 3 STILLBORN-OR-GUARD | The discriminator's spine; text view truncates the 38-row STILLBORN list — used --json for full rows |
| comp-grep | "NFRA_TERRAFORM" docs/ | found PRD | P2 = imports + TF-adopts-live |
| comp-iam gaps | after security-ops/iam.tf authoring | 17 estate gaps, ZERO on the adopted four | Action-only surface understood (Rule 22a); adopted policies are verbatim-from-live |
| comp-surface-check + comp-pulse | auto in safe-commit x4 | OK / HOLD-advisories read | iam.tf HOLDs cited the comp-iam rule — which was already in the execution path |
| to-check.py | --all --assignee (B.1) | 2 TOs found | --all load-bearing, kept |
| NOT run: comp-pipescript | — | — | No gold/silver/bronze script touched; pure infra adoption |

Raw-aws inspection calls carried `# rail-checked:` markers (live primitives mandated by the TO's
phase-1; no comp-tool models non-TF fns' live config).

## Gap found

comp-debris' text rendering truncates the STILLBORN-OR-GUARD list (~20 of 38 shown) with no
"...N more" marker — a silent-truncation surface (the no-silent-caps class). Worked around via
--json; worth a one-line fix by the tool owner.

## Files / commits

`4c7e6d146` TO->pending · `d27e3f9f63` TF authoring (security-ops module, finbert-batch.tf,
source-map x4) · `fd5e98909` security-ops zero-diff proof + role-tags correction · `4fc1d37cf`
finbert zero-diff proof · (this commit) verdict table + log + TO->complete.
Tags local: security-ops-v0.1.0, news-pipeline-finbert-adopt-v1 — **integrator push must be
--follow-tags** (named to MSTR). Deliverable:
`org/tier2_senior/0.7.0_AE_CloudOps~E/deliverables/UNMANAGED_LAMBDAS_ADOPTION_VERDICT_TABLE_20260804.md`.

## Next steps

1. **[1.0.0_SA_CTO]** Rulings on dossiers D1/D2/D3 (D1 needs DS/bd-owner, D2 needs 49F/Schwab owner).
2. **[1.0.0_SA_CTO or route]** AAS-ERR: moltbot instance state vs the two scanners' dispatch leg.
3. **[1.0.0_SA_CTO~B]** Close RCG cycle-3 Rule-1 census on the verdict table.
4. **[0.0.0_AB_MSTR]** Integrator push incl. both tags (--follow-tags).
5. **[0.7.0_AE_CloudOps base]** pipeline_inventory.xml: add security-ops module row on next base touch
   (core doc is base-owned; noted rather than lane-edited).

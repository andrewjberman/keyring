# CTO Brief — Proposed New Project: ADVI_DEMOV1 (Advisor Intelligence Demo Dataset)

**From:** 0.4.0_DS_ClientPlatform~C
**To:** 1.0.0_SA_CTO (base)
**Date:** 2026-05-21
**Type:** Project-open proposal + org-setup notice
**Source of work:** Andrew (ad hoc, direct)

---

## 1. The ask

Andrew has directed a new body of work and asked that it be opened as a formal
ADVI project: **`ADVI_DEMOV1`**. This brief requests CTO ratification of the
project and surfaces the org structure Andrew is standing up to run it.

**Goal of ADVI_DEMOV1:** clone the entire 49 Financial dataset into a new bucket
`opal-data-demo` — identical file structure, identical data richness — but with
every client, advisor, account, and the advisory firm itself replaced by
realistic **fake** data. A demo login then renders the full Advisor Intelligence
experience against fake data, with zero risk of exposing real 49 Financial PII.
Intended use: demos of the Advisor Intelligence platform.

---

## 2. Org structure Andrew is establishing (for CTO awareness)

Per Andrew's direction, this project gets a dedicated ~C-serialized command lane:

- **`2.0.0_SA_COO~C`** — Andrew is opening a COO~C instance to **administrate
  ADVI_DEMOV1** (TO authoring, dispatch, RAVC routing, project tracking).
- **COO~C reports to `1.0.0_SA_CTO` (base)** — the CTO base lane is the
  architectural authority for this project.
- **~C-serialized AEs** — Andrew will bring up whatever `~C` AE instances the
  project needs for the infra/deploy work (bucket creation, IAM, CloudFront/edge
  routing). Exact count TBD with the phase plan.
- DS coverage is `0.4.0_DS_ClientPlatform~C` (this lane) — the audit below and
  the transform-engine build are DS~C scope.

This formalizes a ~C project lane: **CTO base ← COO~C ← {DS~C, AE~C…}**. Lane
discipline note for the fabric: ~C-serialized agents on this project take
dispatch from the ~C chain.

---

## 3. Audit summary — what the work actually involves

A full surface audit is complete. Detail:
`docs/proposals/advisor-intelligence-demo-dataset-20260521.md`. Condensed:

**The 49 Financial dataset** = the `platinum/` tree in `s3://opal-data-bd/` —
measured live today at **22,253 objects / ~4.7 GB**:
- `platinum/firm/` — 14 firm-level files
- `platinum/advisors/{slug}/` — 168 advisors × 6 files
- `platinum/clients/{id}/` — 2,962 clients × 5 files
- `platinum/accounts/{id}/` — 6,548 accounts × 1 file

**Favorable architecture finding:** the serving layer is already firm-agnostic.
The `opal-partners-data` Lambda resolves a firm's bucket from DynamoDB
(`opal-users-v2` → `FIRM#{firmId}/META.s3Bucket`), not hardcoded. Registering a
`demo` firm pointed at `opal-data-demo` serves the dynamic API with **no Lambda
code change**. The project is therefore overwhelmingly a **data-engineering job**
plus light infra/auth wiring — not a portal or pipeline rebuild.

**The one real unknown:** the static `platinum/**?firm=bd` passthrough
(CloudFront→S3) — how `?firm` selects the bucket origin is not yet confirmed.
This is the linchpin and the reason for a Phase 0 probe.

**Two binding constraints** the PRD must lock:
1. PII lives in the **S3 keys** (advisor folders are named `abby_horton`), not
   just file content — the transform re-keys paths *and* keeps fakes consistent
   across all 22 k files.
2. **No per-value dollar jitter.** The platinum tree reconciles to the cent
   (leaderboard → firm headline; the §7 `identity_1` decomposition). Jitter
   breaks every identity. Keep figures verbatim, or apply one global scalar.

---

## 4. Recommended approach + phase shape

**Static snapshot clone** — not a demo pipeline. A one-time (refreshable)
transform reads `opal-data-bd/platinum/**`, applies a deterministic
real→fake pseudonymizer, and writes `opal-data-demo/platinum/**`. A `FIRM#demo`
DynamoDB record + a demo Cognito user complete the wiring.

| Phase | Owner | Work |
|---|---|---|
| 0 — Verification probe (read-only) | DS~C | Close the static-serving-path unknown; full PII field inventory; audit `firmId ===` code branches |
| 1 — Infra | AE~C / DT | `opal-data-demo` bucket (Terraform); IAM; `?firm=demo` routing |
| 2 — Transform engine | DS~C | Deterministic seeded two-pass pseudonymizer (the bulk of effort) |
| 3 — Firm + user registration | DS~C + auth | `FIRM#demo` record; demo Cognito user; portal `ROUTER_FIRM_SUFFIX` entry |
| 4 — Run + verify | DS~C | Execute; smoke-test every surface; mandatory PII-leak scan |

Rough effort: **~4–5 working days**, one DS + AE/DT support.

---

## 5. What CTO base is asked to decide

1. **Ratify `ADVI_DEMOV1`** as a new project under the ADVI macro — create
   `org/projects/ADVI_DEMOV1.json` + REGISTRY row (COO~C can author on your GO).
2. **PRD ownership** — confirm whether CTO base authors the ADVI_DEMOV1 PRD or
   delegates the decomposition to COO~C off this brief + the proposal doc.
3. **Authorize Phase 0** — the read-only verification probe (DS~C, ~0.5 day). It
   ships nothing and closes the static-platinum serving-path unknown that gates
   all infra work. Recommend authorizing it immediately, independent of the
   PRD timeline.
4. **Acknowledge the org setup** in §2 so the fabric routes ADVI_DEMOV1
   dispatch through the ~C chain (CTO base ← COO~C ← ~C workers).

---

## 6. References

- Full audit + implementation design:
  `docs/proposals/advisor-intelligence-demo-dataset-20260521.md`
- April platinum-file provenance catalog:
  `docs/briefs/ADVI_49PUSH_P2_platinum_file_catalog.md`
- Serving-Lambda source (firm-agnostic bucket resolution):
  `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py`
- Firm-record template: `infra/aws/auth/migration/003_create_firms.py`
- Auth design of record: `docs/architecture/ADVI_49PUSH_AUTH_ARCHITECTURE.md`

---

**DS~C standing by** — ready to run Phase 0 on CTO GO, or to support COO~C's
PRD decomposition.

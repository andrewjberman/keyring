# CTO Session 23 — ADVI_PROFIL Reconciliation + PRD Correction Pass

**Agent:** 1.0.0_SA_CTO
**Date:** 2026-04-10
**Topic:** Ground truth reconciliation #2 (Wave 1 + Wave 2a PROFIL ship), PRD correction (auth-validator-edge), dashboard + project JSON updates, .004b/.004c S3 key mismatch surfaced.

---

## Startup

- `register_agent("1.0.0_SA_CTO")` — PID 20000, broker connected, channel push enabled.
- `check-inbox.sh` — no offline messages at startup.
- `inbox-watch.sh` relaunched twice mid-session as new AE messages arrived.
- Read session 22 log `ground_truth_reconciliation.md` + `org/projects/REGISTRY.md` for continuity.

## MCP Scan — State at Startup vs Session 22 Dashboard

Session 22 dashboard was written when `.001/.002/.003/.004a/.005` on PROFIL were all pending. `query_project ADVI_PROFIL` at session 23 startup showed 3 flips since:

| TO | Prev | Now | Evidence |
|---|---|---|---|
| `.001` DT ship RD portal rewrite | pending | **COMPLETE** | Log `advi_profil_001_ship.md` |
| `.002` DT+AE JWT advisorId claim | pending | **COMPLETE** | Log `advi_profil_002_claims.md`; commit `c8bdf663` `fix(auth-handler): /auth/me returns partner identity claims`; portal-auth redeployed |
| `.005` RD L3/L4 drill lift | pending | **COMPLETE** | Log `advi_profil_005_ship.md` |
| `.004a` AE advisor-id scoping edge | staged | **COMPLETE** | Logs `advi_profil_004a_scoping.md` + `advi_profil_004a_test_matrix.md`; commits `9208c784` / `95692b66` / `0160219b` / `7ae0ef6b` / `308c2fae`; ship tags `portal-auth-v1.11.8` + `portal-auth-v1.11.9` |
| `.003` DS book tax_exposure | pending | backend no-op | Log `advi_profil_003_tax_exposure.md` — field already live since D_04 initial landing (`ae47653d`); gap is 2 frontend lines. MCP still shows PENDING. |

## `.003` Backend No-Op Finding (important)

DS investigation concluded that `tax_exposure` is **already live** on `platinum/advisors/{id}/summary.json` for every advisor — has been since the D_04 producer was first landed. No gold-script change required. Real gap is strictly frontend:

1. `portal/src/pages/AdvisorIntelligence/types.ts:1745-1764` — `PlatinumAdvisorSummary` interface does not declare `tax_exposure` (nor `active_since`, nor `role_breakdown`, even though D_04 emits all three).
2. `portal/src/pages/AdvisorIntelligence/AdvisorBookView.tsx:250` — `tax={null}` hardcoded on the L2 `CanonicalBookView` render.

Secondary finding: TO acceptance criterion #3 stated `taxable_pct + tax_deferred_pct + tax_free_pct approx 1.0`. This is wrong scale — canonical shape is 0-100, not 0-1 fraction. All 5 spot-checked advisors sum to exactly 100.0. DS corrected the invariant in the session log.

Packaging options surfaced to COO via MCP:
- (a) Roll into a `.001` retro commit (3 lines, same RD author)
- (b) Tiny standalone RD TO `ADVI_PROFIL.003-frontend.rd-tax-exposure-wiring.md`
- (c) Bundle with `.005` RD session as an incidental fix

Decision is Andrew's. I recommend (b) for clean tracking — the TO is trivially small and gives a clean acceptance artifact.

## `.004a` Architectural Correction (AE-originated, PRD-landed)

AE 0.7.0 Phase 1 `comp-routes` audit at start of `.004a` implementation established that the TO's target Lambda (`shared-advisor-router`) was mechanically wrong:

- `shared-advisor-router` is attached to CloudFront distribution `EVTSA9VEHNZVH` as **origin-request** on behavior `/api/scoped/advisor-intelligence/*.json` ONLY (S3-opal-data-bd origin).
- `getPlatinumAdvisorSummary` at `/api/scoped/partners/books/advisor/{advisorId}/platinum-summary` goes through a DIFFERENT behavior (`/api/scoped/partners/*`) with API Gateway origin — the router never sees that traffic.
- No single modification to `shared-advisor-router` can enforce `.004a` across both required path patterns.

`auth-validator-edge` runs on **viewer-request** against the whole distribution — universal, already verifies JWT via Secrets Manager, already injects `X-Firm-Id`. It sees BOTH behaviors before CloudFront picks the origin. It is the true single choke point.

Phase 1 recommended the re-target, DT ratified under coordinator authority, Andrew corrected the admin-bypass semantics mid-session (Option 2 `firmId === 'opal-capital'` → Option 3 `role === 'admin'`) before commit. Shipped as:
- `portal-auth-v1.11.8` — source + source map (`auth-validator-edge` v11)
- `portal-auth-v1.11.9` — CloudFront distribution wire-up

End-to-end validated: Chase (non-admin) correctly 403s on cross-advisor paths, Travis (partner-firm admin) correctly bypasses, 4 `advisor_scoping_denied` CloudWatch events match DT's curl matrix.

### PRD correction landed (commit `9fa1d073`)

The PRD had the same `shared-advisor-router` error encoded. Initial commit of `docs/architecture/ADVI_PROFIL_PRD.md` to git — the authored-2026-04-10 version had never actually been committed, so the corrected version is the first in history.

Sections rewritten:
- §2 Defense in depth — enforcement Lambda name
- §4 Wave 2 TO table — `.004` row rewritten
- §5.1 Route-map takeaway — full rewrite + long "Correction 2026-04-10 (post-.004a ship)" callout documenting root cause, ship tags, commits, semantics, pointer to AE session log
- §5.5 Shared files table — `auth-validator-edge` row now owns `.002`/`.004a`/`.004c`, `shared-advisor-router` row demoted to "— (not used for scoping)"
- §7 compiler mandate for `.004a/b/c` — rewritten, added mandatory Lambda@Edge topology checklist (three questions: *which behaviors does the Lambda sit on?*, *what event type does it run on?*, *does it see `request.headers.authorization`?*) — AE-suggested additions baked in on second pass
- §8 Findings — finding #2 rewritten

§5.1 route-map rows (107/108) deliberately left intact — those rows accurately describe where `shared-advisor-router` physically sits on the distribution as origin-request. Column header renamed from `Edge Auth` → `Edge Topology` per AE's suggestion so the column name stops implying enforcement. HTML comment added under header documenting the intent.

## `.004b` vs `.004c` S3 KEY MISMATCH (surfaced this session)

**Critical coordination gap** caught while auditing AE's `.004c` prep notes (commit `765dcae9`):

| Side | S3 key | Filename | Partitioning |
|---|---|---|---|
| `.004b` TO default (COO-authored) | `platinum/shared/advisor_ownership.json` | `advisor_ownership.json` | firm-neutral (single file) |
| `.004c` AE prep (design committed, code drafted) | `platinum/{firmId}/ownership_map.json` | `ownership_map.json` | firm-partitioned (per-firm) |

IAM policy in AE's drafted `iam.tf`: `arn:aws:s3:::opal-data-bd/platinum/*/ownership_map.json`. This pattern matches neither `platinum/shared/advisor_ownership.json` (wrong filename) nor `platinum/{firmId}/ownership_map.json` for firm buckets other than `opal-data-bd`.

`.004b` TO requirement #1 mandates a DS↔AE broker exchange on the S3 key **before** DS writes code. That exchange has not happened. AE has drafted (uncommitted) `.004c` assuming firm-partitioned layout; DS will almost certainly default to the TO's firm-neutral layout unless redirected.

Surfaced to COO via MCP with a recommendation to push the broker exchange before either side ships. Not messaging DS directly per memory rule (`feedback_no_direct_ds_messages`) — Andrew handles that routing.

Recommendation logged: firm-partitioned (`platinum/{firmId}/ownership_map.json`) is the cleaner long-term design because:
- Multi-firm onboarding scales without touching a shared file
- Each firm's map can be independently refreshed by its own gold pipeline
- Firm isolation for audit/rollback
- AE's IAM grant already scoped to the per-firm pattern

COO should decide, then issue a correction TO or broker message to DS/AE.

## AE `.004c` Prep Notes Review

Read AE's prep notes (`advi_profil_004c_prep_notes.md`, commit `765dcae9`). Observations:

- SDK/cache design is sound: AWS SDK v3 `@aws-sdk/client-s3` GetObject, module-level `ownershipMapCache` keyed by firmId, 60s TTL, `@aws-sdk/*` marked `--external` in bun build (Lambda Node.js 20.x provides at runtime), bundle size delta +2.9 KB well under 1 MB viewer-request limit.
- Fail-closed for non-admins on S3 unreachable (503 + structured log, not 403); fail-open for admins (they short-circuit before the fetch). Correct.
- Schema version mismatch is a stop-the-line event (500 + `ownership_map_schema_mismatch` structured log). Correct.
- `FIRM_BUCKET_MAP` duplicated from `shared-advisor-router` with named-export + cross-reference comments. Acceptable short-term; promote to shared config module when a third firm onboards.
- IAM grant scoped to `s3:GetObject` on the specific key pattern, not a wildcard. Least-privilege clean.
- Discriminated-object return for helper functions (`{ kind: "bypass" | "deny" | "check", ids? }`) flagged as better than overloading `null`. Agreed — leave as bikeshed for implementation time.
- AE notes "blocking on Andrew's ruling on `7ae0ef6b` attribution incident" — **verified the commit: author `0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent>`, committer Andrew Berman, clean attribution**. No incident. AE should unblock herself on this front unless there's a different incident I'm missing.

## Documents Corrected This Session

| File | Change |
|---|---|
| `docs/architecture/ADVI_PROFIL_PRD.md` | §5.1 column header `Edge Auth` → `Edge Topology` + HTML comment. §7 `.004a/b/c` mandate — added three-point Lambda@Edge topology checklist (AE-suggested additions: behavior topology, event type, authorization header visibility). |
| `org/tier1_exec/1.0.0_SA_CTO/prompt.md` | Session 22 → 23. `ADVI_49PUSH` row updated (bd-v2.21.7 → bd-v2.23.0, fix stack generalized). `ADVI_GLDRST` row updated (.022 commits 8c801923 + 29a831ae, .021b landed). `ADVI_PROFIL` row full rewrite (Wave 1 + Wave 2a shipped, .003 backend no-op, .004a ship details, .004b/.004c mismatch flag). Pipeline Tags table: `bd-v2.21.7` → `bd-v2.23.0`, `portal-auth-v1.11.6` → `portal-auth-v1.11.9`. |
| `org/projects/ADVI_PROFIL.json` | `phase` full rewrite reflecting shipped state. `blocking` rewritten to lead with the .004b/.004c S3 key mismatch as the top blocker + Andrew's open decisions. |

Files I deliberately did NOT touch (other agents' dirty state — Commit Scope Discipline rule I committed at `f332672b`):
- `org/projects/REGISTRY.md`, `ADVI_49PUSH.json`, `ADVI_GLDRST.json`, `ADHC_DESIGN.json` — COO in session
- `infra/aws/lambda-edge/auth-validator-edge/**` + `infra/aws/terraform/portal-auth/iam.tf` — AE .004c drafts
- `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` — DS
- `portal` submodule — DT
- Various TO files under active edit by their owning agents

## Messages Sent

- **0.7.0_AE_CloudOps** — ack on PRD correction; applied `§7` three-point topology checklist + `§5.1` column header rename; flagged `.004b`/`.004c` S3 key mismatch; `7ae0ef6b` attribution is clean, not an incident.
- **2.0.0_SA_COO** — `.003` packaging options (recommending tiny standalone RD TO); `.004b`/`.004c` S3 key mismatch (recommending firm-partitioned); dashboard state for her to absorb into the COO dashboard.

## Compiler Tools

| Tool | Target | Result |
|---|---|---|
| `comp-routes` (trace) | All 5 PROFIL endpoints | (Delegated) AE's `.004a` log carries the authoritative output. Did not re-run from CTO — would duplicate AE's Phase 1 work. Findings absorbed into PRD §5.1 correction. |
| `comp-blast shared-advisor-router` | Lambda@Edge | (Delegated) AE log confirms: no downstream consumers (edge terminus). |
| MCP `query_project ADVI_PROFIL` | project | Primary diagnostic — surfaced the 3 flipped TOs + .004a completion that session 22 dashboard didn't reflect. |
| MCP `get_org_summary` | org | Confirmed 6 live agents + project phase snapshots. |
| `git log --format` on `7ae0ef6b` | commit | Verified AE attribution block — author + committer clean. Debunked "attribution incident" blocker in `.004c` prep notes. |
| Manual grep | PRD `shared-advisor-router` references | Surfaced 7 match sites, corrected 5, left 2 in route-map rows (intentional topology, documented via correction note + column rename). |

Startup reconciliation + doc corrections — no code changes, no deploys. Belongs in `org/compiler-tools-log.md` as "CTO session 23 reconciliation" row.

## Follow-ups Still Open (Andrew decisions)

1. `.006` RD cache policy — a / b / c
2. `.007` RD admin My Profile toggle — cut or ship
3. `.003` frontend follow-up packaging — standalone 2-line RD TO (rec) vs `.001` retro vs `.005` bundle
4. Non-admin L3/L4 drill scope (pre-existing)
5. `.004b`/`.004c` S3 key decision — firm-partitioned (rec) vs firm-neutral

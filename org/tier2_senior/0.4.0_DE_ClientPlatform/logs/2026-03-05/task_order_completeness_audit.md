# Task Order Completeness Audit: ADVI_V1VERS + ADVI_YANGV2 — 0.4.0_DE_ClientPlatform

**Date:** 2026-03-05
**Method:** Full sweep of all task orders in both project namespaces + all ad-hoc task orders
across pod 4. Blocker Verification Protocol (AGENT_START_HERE.md) applied to every
non-complete item before any BLOCKED or AMBIGUOUS designation.

---

## 1. Complete Task Order Status Table

### ADVI_V1VERS

| Task Order | Agent | Status | Verification |
|---|---|---|---|
| `ADVI_V1VERS.004.portal-types-wiring.md` | DE | **complete** | Portal DEV `7df26bb` |
| `ADVI_V1VERS.006.books-design-brief.md` | DE | **complete** | CLOUD `aaf97585`, brief at `docs/architecture/advisor_intelligence/books_tab_design_brief.md` |
| `ADVI_V1VERS.004.adv-drill-cla.md` | DS | **complete** | CLOUD `cc3ad9fa` (adv_drill + cla in bd-portal-publisher) |
| `ADVI_V1VERS.005.rolling-flows-data.md` | DS | **complete** | CLOUD `6a3ff256` (stacked_bar + monthly in script 10) |
| `ADVI_V1VERS.J1.partner-identity-dynamo.md` | AE | **complete** | VERIFIED — see section 3 |
| `ADVI_V1VERS.J2-J3.auth-handler-authorizer.md` | DT | **complete** | VERIFIED — see section 3 |
| `ADVI_V1VERS.004.distribution-continuous.md` | RD | **complete** | Portal DEV (C2/C4 in DistributionTab) |
| `ADVI_V1VERS.005.advisors-tab.md` | RD | **complete** | Portal DEV (stacked bar + rolling 1Y rendered) |

**V1VERS: 8 of 8 task orders complete.**

---

### ADVI_YANGV2

| Task Order | Agent | Status | Verification |
|---|---|---|---|
| `ADVI_YANGV2.Y-phase2.ds-data-batch.md` | DS | **complete** | CLOUD `0c9bb501`/`cc3ad9fa`/`6a3ff256`, deployed bd-v2.16.2/v2.16.3 |
| `ADVI_YANGV2.Y-phase3.de-type-wiring.md` | DE | **complete** | Portal DEV `542197c` |
| `ADVI_YANGV2.Y1-Y4-Y6-Y12.phase1-visual.md` | RD | **complete** | Portal DEV `f9c0e59`→`2981133` |
| `ADVI_YANGV2.Y8.continuous-aua-stacked-bar.md` | RD | **complete** | Portal DEV `4b768c3` (pushed to remote) |
| `ADVI_YANGV2.Y3-Y5.fe-header-panel.md` | RD | **complete** | Portal DEV `7460f35` |
| `ADVI_YANGV2.Y6b-Y6d-Y9.fe-drill-and-continuous-nna.md` | RD | **complete** | Portal DEV `0bd3f66` |
| `ADVI_YANGV2.Y13.fe-rolling-flows-nna-bar.md` | RD | **complete** | Portal DEV `54163de` |
| `ADVI_YANGV2.Y15.books-tab-l2-l3-l4.md` | RD | **complete** | Portal DEV `9b902dc` |
| `ADVI_YANGV2.portal-push.phase3.md` | DT | **PENDING** | Not started — see section 2 |

**YANGV2: 8 of 9 task orders complete. 1 pending (DT portal push).**

---

### Ad-hoc task orders (pre-namespace, still active scope)

| Task Order | Agent | Status | Notes |
|---|---|---|---|
| `advi_c1_geo_continuous.md` | RD | **complete** | DistributionTab C1 (continuous GEO NNA) done |
| `advi_c3_cla_snapshot.md` + addendum | RD | **complete** | CLA snapshot view done |
| `advi_h_portal_primitives.md` | RD | **complete** | Portal primitives refactor done |
| `advi_i_top_performers.md` | RD | **complete** | Top performers visual done |
| `continuous_view_max_window_clients_fix.md` | RD | **complete** | Done |
| `distribution_nomenclature_fix.md` | RD | **complete** | Done |
| `xtick_spacing_fix.md` + addendum | RD | **complete** | Done |
| `advi_a4_bell_curve_verify.md` | DS | **complete** | Snapshot NNA bell curve verified — no patch needed |
| `advi_a5_users_v2_mapping.md` | DS | **complete** | Scenario C — no advisorKey mapping exists in opal-users-v2 |
| `acat-inkind-nna-testing.md` | DS | **PENDING** | Not blocked — see section 2 |
| `HOTFIX-drilldown-account-perf-fallback.md` | DT | **complete** | bd-v2.16.1 deployed |
| `deployment_audit.md` | DT | **superseded** | Superseded by deployment_map.xml |

---

## 2. Open Items — Detailed Status

### OPEN #1 — DT: ADVI_YANGV2.portal-push.phase3.md

**Status: PENDING (not blocked)**

**What:** Push portal DEV to remote origin/DEV through `9b902dc` (5 commits:
`542197c` → `7460f35` → `0bd3f66` → `54163de` → `9b902dc`). Update parent repo
submodule pointer on CLOUD.

**Blocker Verification (Protocol Step 1–3):**
- Step 1: Checked DT's task order — no dependency agents listed. Task order states
  "No code changes — push only."
- Step 2: No dependency to check — this is a standalone push with all prereqs already
  satisfied (DE-reviewed at `f9161bed`, commits DE-approved).
- Step 3: **Not blocked.** DT can execute immediately.

**Who acts:** 0.4.0_DT_ClientPlatform
**What they do:** `cd portal && git push origin DEV`, then update CLOUD submodule pointer.
**Impact of not doing:** Y3-FE, Y5-FE, Y6b-FE, Y6d-FE, Y9-FE, Y13-FE, Y15 all
unreachable on remote. The Books tab, GRO mode, NNA drills, and rolling flows bar are
invisible to the server deployment pipeline until this push happens.

---

### OPEN #2 — DS: acat-inkind-nna-testing.md (Steps 2–5 pending)

**Status: IN PROGRESS (not blocked on Steps 1–2; BLOCKED on Steps 3–5)**

**What:** CEO-directed investigation of ACAT in-kind NNA undercount ($106M inflow gap
vs Schwab TOA). 5-step task order.

**Step 1 (commit scripts):** COMPLETE — `90424dba` committed `diag_acat_inkind_scan_v1/v2/v3.py`.

**Step 2 (write DT brief):** NOT DONE. `docs/briefs/devops-brief-acat-inkind-nna-ec2-run.md`
does not exist. DS's 2026-03-05 session logs (`canonical_nna_logic.md`,
`smoke_test_orphan_theory.md`) make no mention of this brief. This is DS's next action
and they can execute it now — no dependency.

**Steps 3–5 (DT run → DS analysis → DS production design brief):**
**Blocker Verification for Steps 3–5:**
- Step 1 (protocol): Checked DT task orders — no ACAT EC2 run task order issued to DT yet. The brief (Step 2) is the prerequisite.
- Step 2 (protocol): DS has not written the brief that would trigger DT's action.
- Step 3 (protocol): **BLOCKED on DS completing Step 2** (DT brief not written → DT cannot act → DS cannot read output → DS cannot write analysis or design brief).
  Evidence: `docs/briefs/devops-brief-acat-inkind-nna-ec2-run.md` does not exist. DT task orders contain no ACAT item.

**Who acts next:** 0.4.0_DS_ClientPlatform — write `docs/briefs/devops-brief-acat-inkind-nna-ec2-run.md`.
**Then:** 0.4.0_DT_ClientPlatform — upload v3 to S3, run on EC2, capture output.
**Then:** DS — read S3 output, write analysis + production design brief.

---

## 3. Blocker Verification: J1 + J2/J3 (Cited as Y14 Gate)

Both items are cited as gating Y14 (Books access gating). Applied full protocol.

### J1 — opal-partner-49financial DynamoDB table (AE)

**Blocker Verification:**
- Step 1: Read `org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-03-04/advi_j1_partner_identity_dynamo_deploy.md`.
  Log documents full deploy sequence:
  - CLOUD commit `1b918471`: `feat(shared-infra): opal-partner-49financial DynamoDB table + IAM read policy`
  - `terraform apply`: 2 added, 0 destroyed, 0-diff confirmed
  - AWS CLI verification: table ACTIVE, hash_key=email, ByAdvisorRole GSI present
  - Table ARN: `arn:aws:dynamodb:us-east-1:313476888478:table/opal-partner-49financial`
  - Tag `shared-infra-v1.3.0` applied and pushed (confirmed: `git tag -l "shared-infra-*"` returns v1.3.0)
- Step 2: Log and git tag both corroborate delivery. Task order marked complete.
- Step 3: **Not blocked. J1 is verified complete.**

### J2/J3 — auth-handler + portal-authorizer (DT)

**Blocker Verification:**
- Step 1: Checked DT CLOUD commits.
  - `de023eed`: `feat(portal-authorizer): J3 -- pass advisorKey/advisorName/advisorRole to Lambda context (ADVI-J3)`
  - `ba0cbc19`: `0.4.0_DT_ClientPlatform: deployment_map.xml -- portal-auth J2/J3 (v1.1.0/v1.2.0)`
  - `67a400b3`: `0.4.0_DT_ClientPlatform: deployment_map.xml bd-v2.16.2/bd-v2.16.3 + J2/J3 complete`
  - DT task order `ADVI_V1VERS.J2-J3.auth-handler-authorizer.md` status: complete
- Step 2: Multiple CLOUD commits + task order corroborate delivery.
- Step 3: **Not blocked. J2/J3 verified complete.**

**Consequence for Y14:** J1 + J2 + J3 are all confirmed live. The auth chain that
gates Books advisor access is complete. Y14 is **unblocked**. No task order has been
issued for Y14 implementation.

---

## 4. Untouched PRD Streams (No Task Orders Issued)

The Yang V2 PRD (Section 5) defines 21 streams. The following were never given task orders:

| Stream | Why No Task Order | Current State |
|---|---|---|
| **Y2** — NMNC/NMEC period-bookend audit | DS investigated and found no patch needed | Resolved as no-op (data_contract.xml documents finding) |
| **Y11** — Advisor field investigation | DS investigated; no distinct Advisor field exists in BD gold | Resolved as no-op. Y13 Advisor toggle cannot be built. |
| **Y14** — Books access gating (portal) | Was gated on J1+J2+J3. Now unblocked. No task order issued. | **GAP — see section 5** |
| **Y17** — AI RAG executive summary | Deferred by CTO/COO; flagged for separate mini-PRD | Intentionally deferred |

Y2 and Y11 are legitimately closed without task orders (investigation-only, resolved
as no-ops). Y17 is intentionally deferred. **Y14 is a gap** — the gate cleared,
but no task order was ever issued for the implementation.

---

## 5. Y14 Gap Analysis — Books Access Gating

**What Y14 requires (from Yang V2 PRD Section 4.1):**

The Books tab (`ClientsTab.tsx`) currently gates all content behind `isInternal() || isDev()`.
Y14 is the switch from this admin-only model to a role-based model where:
- Admin users (internal/dev) see all advisors via dropdown — unchanged
- Authenticated advisor users see **only their own book** — new behavior
- The JWT (now containing `advisorKey`, `advisorName`, `advisorRole` via J3) is the
  identity source

**What the auth chain delivers (verified above):**
- `advisorKey`, `advisorName`, `advisorRole` are injected into the Lambda context by
  the portal-authorizer (J3)
- The auth-handler reads `opal-partner-49financial` at login to resolve portal user
  email → advisor identity (J2)
- The table exists and is empty (J1) — **populated at advisor onboarding time by Andrew**

**What is still needed for Y14:**
1. **RD task order** — `ClientsTab.tsx` needs to read `advisorKey` from auth context
   and scope the Books content to that advisor when the user is not admin/internal
2. **Portal API/backend** — the `getAdvisorBook(advisorKey)` call must be scoped to
   the logged-in advisor's key (currently the advisory key is likely hardcoded or passed
   via admin selector)
3. **Population gate** — Y14 cannot be used by real advisors until `opal-partner-49financial`
   has their email → advisorKey entries (Andrew's manual action)

**Note:** Y14 is frontend-only (RD + DE), no new Lambda or data work needed. The
backend auth chain is complete. The portal just needs to read the advisor identity from
the JWT claims and conditionally scope the Books view.

---

## 6. Committed-But-Undeployed Code

Two DS commits are on CLOUD but not deployed — separate from the task order system:

| Commits | What | Status |
|---|---|---|
| `9bfb289b` + `b4f2d7a7` | NNA canonical classification fix (scripts 05 + 05b — exclude JNL journals and Schwab sweeps) | **Awaiting CEO go/no-go before DT triggers gold layer rebuild** |

This is not tracked in any task order. The fix was research-driven (Schwab SOT
cross-reference session). CEO decision is the gate.

---

## 7. Action Summary for COO

| Priority | Action | Owner | Unblocks |
|---|---|---|---|
| P0 | Execute portal DEV push (`ADVI_YANGV2.portal-push.phase3.md`) | **DT** | Y15 Books tab, Y3-FE/Y5-FE/Y6b-FE/Y6d-FE/Y9-FE/Y13-FE reaching server deploy pipeline |
| P1 | Write DT brief for ACAT v3 EC2 run (`acat-inkind-nna-testing.md` Step 2) | **DS** | DT EC2 run → DS analysis → production design brief |
| P1 | Execute ACAT v3 EC2 run once DS brief is written | **DT** | DS analysis → CEO design review |
| P2 | Issue Y14 task order to RD | **COO** | Books tab advisor access gating (auth chain ready; table needs populating) |
| P2 | Populate `opal-partner-49financial` with advisor email mappings | **Andrew** | Y14 actually usable by real advisors |
| P3 | CEO go/no-go on NNA canonical fix (commits `9bfb289b`+`b4f2d7a7`) | **CEO/Andrew** | DT gold layer rebuild + improved NNA accuracy |
| P4 | Issue Y17 mini-PRD when Books tab is stable | **COO** | AI RAG executive summary |

---

## Status: COMPLETE
**Active branch:** CLOUD
**Workspace CLOUD commit:** pending (this log)

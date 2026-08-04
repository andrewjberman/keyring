# MDPF_CHANNEL_INDEPENDENCE — closure-row sweep (rows 1–19)

**archetype:** VALIDATE
**Author:** 1.0.0_SA_CTO · 2026-08-04 ~0205Z
**Mandate:** the carried CTO sweep — delivery-state + gate-state per row, **MISSING stated as
MISSING, never inferred from delivery**, + a supersession verdict per row. Rows = PRD §3a
(`docs/architecture/MDPF_CHANNEL_INDEPENDENCE_PRD.md`, 12→19 growth recorded there).
**Liveness discipline:** a row is CLOSED only REPO-TRUE **and** RUNTIME-TRUE (PRD ~1856Z column).
**Namespace warning, load-bearing:** FOUR row/ID namespaces are live in this program and they
collide — PRD closure rows (this sweep) · T5.A kill-list rows · T1.C checklist rows · and
**MDPF_GLOBAL.C1/C2 (T5.B preconditions) which are NOT the PRD's C1/C2 event contracts.**
Every citation below is namespace-explicit.

## Headline

**0 of 19 rows CLOSED under the both-true test.** 5 substantially DELIVERED (runtime evidence
present), 6 IN-FLIGHT on named gates, 4 MISSING (stated as missing — rows 8, 9, 12, and 6's
render-half), rows 1–3 carry an open supersession question routed to my own C.3 ruling, and
**one new measured finding: the deployed dispatch is 07-23 vintage — rows repaired in it since
07-23 are TRUE-BUT-NOT-LIVE, including row 18's own guard.**

## The new measured finding (this sweep's sharpest fact)

`s3://opal-data-mdpf/code/mdpf-daily-dispatch.sh` = **LastModified 2026-07-23T10:55:16Z,
32,077 B, ETag 6f26beac** vs repo `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh` =
**35,320 B** (single-part ETag ≠ repo md5; size alone is decisive). The EC2 runner syncs from
that key at run time (`:125`), so **the running dispatch cannot contain any dispatch commit
dated 07-24 or later**: the row-18 FATAL guard (@3baf759022 + @ccb5718c3a, 07-24), the Stage-4
underscore-twin kill (@cc35d80925, 07-29 — explicitly "REPO ONLY, S3 deploy held post-17:15Z
D2 freeze"), the A2-retirement Stage-3.5 change (@32e953198a, "DEPLOY HELD until after today's
fires"). **Known-held is not the finding; the finding is the AGGREGATE VINTAGE**: three
separately-held changes have compounded into an 11-day-old runtime while the repo's row-18 text
asserts a guard the runner does not execute — and the zombie Stage-4 twin writer (kill-list
row 13, SUPERSEDED w/ zombie-writer rider, my ruling 221736Z) keeps writing nightly until this
deploys. **Routed to 0.7.0_AE (their lane) for fold-into-T2.C-apply or an explicit
standing-hold declaration with an owner and a stop-condition — a hold with no ledger row is how
a freeze becomes a vintage.**

## The grid

Legend: **DELIVERY** (repo evidence, hash) · **RUNTIME** (live/exercised evidence, or honest
unknown) · **GATE** (what holds the remainder) · **SUPERSESSION** (does the row still bind).

| # | Row (short) | DELIVERY | RUNTIME | GATE | SUPERSESSION VERDICT |
|---|---|---|---|---|---|
| **1** | C1 event: bronze→silver per feed | **NO NEW EVIDENCE this sweep** (registration state 07-29: "only partially event-driven"; accrual bridge @1163e28f5b is SCHEDULER, not an event leg) | not probed | MDPF_GLOBAL T1/T2 decomposition (COO) | **OPEN QUESTION — routed to my C.3 producer-unification ruling:** does the 08-03 memo's one-synchronized-schedule (T2) leave the event contracts binding as accelerators (§2.3's own model), or supersede them? NOT adjudicated here. |
| **2** | C2 event: silver→gold per partner | same as row 1 | not probed | same | same as row 1 |
| **3** | C3 event: gold-change→publish, non-blocking fan-out | same as row 1; no republish-on-gold-change evidence | not probed | same | same as row 1 |
| **4** | No cross-partner gate anywhere; **sever exercise** | Channel independence in canonical builder + carry mechanism (07-28/29 consolidation, attributed at registration; G7 splice removal @0d653d4aa3) | **Sever exercise NEVER RUN** (the PRD says nothing else proves it); carry-path exercised in dry-runs only. **Counter-evidence live: @8b7adfb802 — cottonwood has ZERO representation in the mdpf-daily-trigger freshness gate** | T2.C apply (roster-derived gate; acceptance baseline = @8b7adfb802 per my 001415Z ruling) | Binds unchanged. Verification bar in project JSON (held-channel through one full SCHEDULED cycle) stands. |
| **5** | `:1656` firm-axis poison gone | **DELIVERED** — labeled compose + carry (@e56eef609e, @37ee77a86c, @4ed8a19775, @314f864aa0); one live composition @0d653d4aa3; headline 1,826,143,796→1,950,519,805 flip Andrew-ruled correct | Exercised (dry-run mutants: absent cottonwood → carried/visible-drop; gates PASS 450 dates); participation schema **DEPLOYED** @85e7eb3922 DELTA=0 | — | Binds; substantially TRUE. Residual: formal one-firm-cell-removal mutant on the DEPLOYED path not separately recorded. |
| **6** | Global carry-forward, every value labelled | **DELIVERED producer-side** — carried_at_declared_cadence + as_of_by_partner + 3 labeling requirements demonstrated on real data (@85e7eb3922, @72cd1a7860 honest-None) | Producer-side exercised + deployed | — | Binds. **Render-half (held ≠ measured visible in the UI) — MISSING: no DE evidence this sweep.** Stated as missing, not inferred. |
| **7** | Roster-derived expectations, no literals; partner-#4 test | **PARTIAL** — fold side roster-derived fail-closed (@37ee77a86c, @6846dba11f, @156b8cf2cd) | **Trigger side FALSE live** (@8b7adfb802: gate literals miss cottonwood entirely) | T2.C apply chain (+ Andrew's word at AE's terminal) | Binds. T2.C is the implementing change; row 13's same-change coupling honored (both ride T2.C). Sibling instance: ETFS Sep-1 roster-derived CSV count carry (0.7.0_AE). |
| **8** | Normalised divergence §2.5, healthy = 0/0/0 | **MISSING — no implementation evidence in any commit since 07-24.** (Adjacent-not-same: participation schema emits ages+watch markers.) | — | unassigned | Binds; unstarted. Candidate for T2 decomposition. |
| **9** | Manifest written every run, skipped+carried populated | **MISSING — NOT BUILT** (project JSON registration state; zero commits since). Do NOT conflate with MDLP_MONPUB's manifest — different product. | — | unassigned | Binds; unstarted. Hazard note from project JSON stands: it is a manifest ARTIFACT, never an alarm (moratorium). |
| **10** | Scheduled floor; Door-6 as accelerator | **AUTHORED-NOT-APPLIED** — floor TF @4957e6050f (declared inline as committed-ahead-of-gated-apply), clock v2 @5a20433a5c, 7/7 landing table @d745270b44; accrual-leg Scheduler APPLIED @1163e28f5b (07-29) | Floor: **TRUE-BUT-NOT-LIVE by construction** (apply gated) | T2.C apply = schema chain + Andrew's word | Binds. The 08-03 memo (T2) is this row's implementing vehicle, not its supersession. |
| **11** | Frontier stamp cannot silently overwrite (CVO P2) | **PARTIAL** — T1.C-checklist rows 4+7 (namespace: checklist) deployed @7830a48035 (md5 MATCH 44db6559): source_vintage/latest_cross_section/calendar emission; account_dist read discriminates absent-vs-corrupt (@72cd1a7860) | Deployed, md5-verified | — | Binds. **The specific publish-time as_of-vs-coverage-end CHECK: NO DIRECT EVIDENCE — missing, stated as such.** |
| **12** | `exempt_absorbed` label collision split | **MISSING — label still present unsplit** (repo grep: producer + tests + verify script carry it; zero commits touch it) | — | unassigned | Binds; unstarted. |
| **13** | M1 deleted; gate roster-derived, same change as row 7 | **STAGED NOT APPLIED** @938fc74211 (07-28, declared in-subject) → superseded-as-vehicle by T2.C (roster-derived gate) | FALSE live (same @8b7adfb802 baseline) | T2.C apply | Binds; vehicle is T2.C. ⚠ Do NOT confuse with T5.A **kill-list** row 13 (SUPERSEDED w/ zombie-writer rider @e1c41cbab7) — different namespace. |
| **14** | M2 de-self-referenced (counts never from own artifact) | **SPEC COMPLETE** — MDPF_GLOBAL.C1 (T5.B precondition): every legacy row re-derives, droppable branch EMPTY, parity 12/12 (@03ab006764, close-out @f8d294e39b) | Not yet — impl in flight | C1impl (COO TO @80da654dc8): **Leg A** (parity+heal, DELTA=0) dispatchable NOW; **Leg B** rides Andrew's disclosure word with DC1 as one serve-correction event (I orchestrate) | Binds. This row is WHY the 20 count holes were unrecoverable (PRD's own note). |
| **15** | M3 relocated; opal-data-mdpf not required for a run | Partial via 07-28/29 consolidation | **FALSE live** — CVO dial ledger @ce04fa9e47: chain LIVE on opal-data-mdpf, teardown PARKED | T5 (gated on T1–T3 proven) + **ETFS CANON (Andrew P0 at 0.7.0)** — memory: canon gates this cluster | Binds; correctly parked. |
| **16** | M4 severed — no opal-data-inf trigger dependency | Accrual bridge (Scheduler) exists @1163e28f5b | **FALSE live, MEASURED 08-03 morning** — the None-schedule INF contingency reproduced the global-view delay (MDPF_GLOBAL phase note) | T2.C apply (the synchronized schedule IS the severance) | Binds; the 08-03 reproduction is the row's own justification firing in production. |
| **17** | M5 platinum serve → monolith; sequence LAST | Preconditions: **C2 (:567 fail-loud) LANDED+exercised both directions** (@0f0f173351, sibling @72cd1a7860, C2b trace @d16f20d522) — **the memory-recorded teardown blocker is DISCHARGED**; C1 in flight (row 14); T5.A kill-list census complete @b877dbc0f5 (RETIRES-WHOLE=CONDITIONAL-YES on {C1, C2}); T3 CloudFront census = the row's (b)/(c) prep | Serve move NOT started (correct — sequenced last) | T5 gate (T1–T3 proven) + never-widen sign-off (CTO+COO) on the cutover + rows 14-before-17 ordering (PRD interaction note) | Binds. ⚠ Standing memory rider unchanged: hyphenated `account-distribution.json` is the LIVE SERVED PORTAL BELL — 4-way name collision; match full bucket+key in every teardown step. |
| **18** | Dispatch FAILS CLOSED on missing revamp producer | **DELIVERED IN REPO** — `:143` FATAL guard citing "closure row 18, CTO 2026-07-24" verbatim (@3baf759022 + placement fix @ccb5718c3a) | **FALSE — TRUE-BUT-NOT-LIVE, MEASURED THIS SWEEP:** deployed S3 copy is 07-23 vintage (predates the guard). See the finding block above. | Dispatch S3 deploy (0.7.0_AE lane; likely folds into T2.C apply window) | Binds. Scope note: `:143` covers producer ABSENT (the row's text); Stage-6 EXECUTION failures remain NON-FATAL by build-alongside design (`:434-442`) — in-design, not a gap in this row. |
| **19** | Drift sweep covers mdpf; NOT-COVERED ≠ clean | Partial (CLAUDE.md: `comp-pipescript deployed` sweeps mdpf check-only) | **Negative persists in a NEW form** — F2 (predecessor, 08-04): blind to Model-B cross-tree deployment; `0 UNCOVERED` computed inside the gap it audits | comp-tool universe audit (`ADHOC.comp-tool-universe-audit` — **staged, DO-NOT-DISPATCH**, census Appendix-A member) → then my comp-blast Part-2 PRD | Binds; folded into the universe-audit lane. The row's acceptance (uncovered returns NOT-COVERED, never a clean result) is the audit's predicate-not-roster test in instrument form. |

## Supersession summary (the axis the sweep exists for)

1. **The closure set itself is NOT superseded.** The 08-03 Andrew memo (MDPF_GLOBAL Addendum C,
   T1–T5) is the implementing VEHICLE for rows 4, 7, 10, 13, 15, 16, 17 — how, not whether.
   MDPF closes when the 19 rows are both-true; that definition stands.
2. **One genuine supersession question, rows 1–3:** synchronized-schedule (T2) vs the three
   event contracts. The PRD's own §2.3 answer (schedule = floor, events = accelerators) is my
   prior, but the C.3 producer-unification ruling I owe at decomposition time is the right
   place to bind it — recorded there, not adjudicated here.
3. **Two supersessions already ruled and honored:** T5.A kill-list rows 8/13
   (@e1c41cbab7, my 221736Z words) — kill-list namespace, not closure rows; and VELOCITY
   sequencing (Addendum A.2) superseded by the 08-03 memo.
4. **One memory-recorded blocker DISCHARGED:** "json/mdpf retire BLOCKED behind :567" — C2
   landed 08-03 (@0f0f173351). Teardown remains PARKED on ETFS CANON + T5 gates — the parking
   reasons changed, the parked state did not.

## What moves next, by owner

- **[0.7.0_AE]** the dispatch-vintage finding (above): fold the dispatch S3 deploy into the
  T2.C apply window, or declare the standing hold with owner + stop-condition on a ledger row.
- **[COO]** T1–T5 decomposition (already the MDPF_GLOBAL blocking line) — rows 8, 9, 12 are
  unassigned remainder candidates for T2/T5 decomposition; this grid is the coverage input.
- **[1.0.0_SA_CTO]** the C.3 producer-unification ruling at decomposition time (carries the
  rows-1–3 supersession question); comp-blast Part-2 PRD after the universe audit.
- **[Andrew]** unchanged, nothing new: the cottonwood disclosure word (gates C1impl Leg B +
  DC1), and the T2.C apply word at AE's terminal.

## Compiler Tools

| tool / probe | result | note |
|---|---|---|
| git evidence sweep (log/show, hash-anchored) | PASS | every DELIVERY cell carries its commit; no delivery inferred from an adjacent row |
| `aws s3api head-object` (deployed dispatch) | **FINDING** | 07-23 vintage vs 07-24+ repo guards — the sweep's sharpest fact; size-decisive (35,320 vs 32,077 B) |
| repo greps w/ named targets (`:143` FATAL, `exempt_absorbed`) | PASS | row-18 repo-truth grounded at line; row-12 MISSING grounded as still-present-unsplit |
| comp-tools not used for the grid itself | — | the grid is org-record + S3-primitive reconciliation; comp-estate/comp-freshness answer estate topology, not row-vs-evidence attribution. Rule 20's graph check not triggered: no change made. |

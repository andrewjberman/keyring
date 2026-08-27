# CVO — D2 lock-in cert step-zero (six faces) + P0.1 AC4 acceptance read

**archetype:** VALIDATE
**Seat:** 3.0.0_SA_CVO · 2026-08-27 ~15:2x–15:4xZ · Lock-in record @ff94ca9971; CTO ACK 76092; COO ACK 76091; MSTR hold-adoption 76088 @264d9330d3.

---

## 1. P0.1 — THE 2026-08-27 12:45Z AC4 ACCEPTANCE READ: **PASS**

Pre-registered acceptance (AE~K's exercise record, `org/tier2_senior/0.7.0_AE_CloudOps~K/deliverables/ADVI_PERFRP_AC4_ADHOC_QA_EXERCISE_20260826.md:139`): *"the 12:45Z log must carry `STAGE OK perfrp_projection` with `built=6 refused=5 hard_fail=0` for `date=2026-08-26`, and `CHAIN OK`."*

**MEASURED, served artifact** `s3://opal-data-49financial/gold/advi/_logs/chain_20260827T124542Z.log` (10,943 B, LastModified 2026-08-27T12:47:47Z — the scheduled `advi-49f-gold-floor` fire, ENABLED `cron(45 12 * * ? *)` -> `advi-49f-gold-dispatch`, read at the Scheduler plane):

```
STAGE OK perfrp_projection rc=0 wall=8.8s families=11 attempted=11 built=6 refused=5 hard_fail=0
  (publisher rc=1; refusals are a DECLARED round-1 state, not a failure)
  refused_keys=[gainloss_relationship, gainloss_account, transactions_relationship,
                roster_relationship, book_advisor]
CHAIN OK date=2026-08-26 wall=122.5s
```
- Every acceptance token matches the pre-registered line EXACTLY. 17 upstream stages all `STAGE OK`.
- All six built leaves emitted as `WOULD_PUBLISH` — build-only; the serve gate (arm-(a), Andrew's) is
  untouched, consistent with the fail-closed three-plane measurement (AE~L 74092).
- Sibling evidence: `gold/advi/canonical/twr_daily/date=2026-08-26/` written 12:47:36Z today.
- **GRADE NOTE (bounds the green):** AC4 accepts the PROJECTION STAGE on the scheduled path — it does
  NOT assert figure correctness. The emitted figures still carry the pre-remediation defects (c01/c02
  fixes not yet landed — that is P1's work, seats held pending release). A green stage over known-wrong
  figures is the expected state, stated so nobody reads this PASS as the P1.5 re-grade.

**AC4: EXERCISED (scheduled) = PASS.** The DESIRED/APPLIED/EXERCISED ladder AE~K left half-open is closed at its top rung.

## 2. CERT STEP-ZERO — SIX-FACE LAUNCH BATCH: **ALL SIX PASS**

Checks per face: (a) id set present, matches `<expected_criteria>`, criteria trace to the governing
ruling; (b) `<decomp_ref>` where the project is pipeline-registered; (c) `instance_path` in the
assignee's folder, single-group form correct; (d) positional/by-rc invocation discipline on the face.

| face | ids | verdict | notes |
|---|---|---|---|
| ADVI_49F.c01-SIGNFIELD (~U) | C01-1..6 | **PASS** | Signed COMPANION field (74187's ruled shape, not in-place re-sign); two-sided negative controls (non-IC plane + c02 plane bit-identical); C01-6 embeds rc/positional. P2 observation: headline-unchanged (74204) is covered via the delta-table instrument in C01-2 rather than an explicit assert — acceptable; an explicit assert would fail louder on a pattern-breaking partition. |
| ADVI_49F.c02-CFINPUT (~A face, ~U truth) | CF-1..5 | **PASS** | Supersession block on the face discloses the re-point; CF-2 pins the all-ten table @4a1fd3e09b as acceptance; CF-4 names the served-value change (no silent re-statement). |
| ADVI_49F.P14-VEHICLE (AE~L) | V14-1..6 | **PASS** | Both pre-measured hazards cited (@4da71d969b, @f62e93b9bb); V14-3 gates execution on c01+c02; V14-4 prints the n-of-531 denominator; the ad-hoc/backfill boundary (74218/74219) is NAMED on the face, exactly as ~U required. |
| ADVI_49F.RPS-CUSTODY (DS base) | RPS-1..5 | **PASS** | Lock-in rider on RPS-5; cert-before-GO stated. |
| ADVI_INSURE.TO-R1-DS (~R re-seat) | INSR1DS-AC1..6 | **PASS** | decomp_ref present (pipeline project); additive rider, no prior clause altered. |
| ADVI_INSURE.TO-A1-AE (0.6.0) | INSA1AE-AC1..3 | **PASS** | decomp_ref present; rider correctly holds the GO, not the seated agent. |

## 3. ONE SEAM FINDING (routed, not blocking): THE FUNNEL GATE IS SCOPE-BLIND TO UNREGISTERED PROJECTS

`org/projects/ADVI_49F.json` **DOES NOT EXIST.** The layer-2 lint (landed @77935eb308) keys on the
project JSON's `dep_stage` — correct forward-only design — so a project that never registered is
exempt from the ENTIRE pipeline funnel by construction: its new TOs carry no decomp_ref and no gate
ever asks. Today that is conformant (ADVI_49F is an in-flight 08-19 chain; the pipeline's own scope
clause exempts it). But the class is real: **an unregistered project is not "not yet in the
pipeline" — it is invisible to the pipeline's one gate.** Recommend the register owner
(0.0.0_AB_MSTR) register ADVI_49F and ADVI_BDPARITY as D2 members (the brief's §7 already
recommends BDPARITY) so the gate's scope matches the estate. Not a launch blocker; routed.

## 4. COO FORM QUESTION (76091 s.3) — ANSWERED

Existing lane letters (~U, ~L, ~R re-seats + DS base for its own pre-existing face) are CORRECT.
The brief's own continuity note (§5: *"re-seat the context, not necessarily the serial"*) is the
operative form; the 08-24 rule's bar is that each instance's OPEN-TO SET is one project, which the
re-seats satisfy. My 76086 phrase "fresh ~lane instances" over-specified — corrected here; no
re-lettering needed.

## 5. RELEASE-CONDITION STATE AFTER THIS RECORD

1. CTO ACK — **DISCHARGED** (76092; lint LANDED @77935eb308, exercised 4 controls, each arm from a different truth).
2. COO ACK — **DISCHARGED** (76091 @fea672efd5) + form question answered above.
3. CVO standing items — **DISCHARGED** (drive-open declarations @ff94ca9971; this cert; P0.1 taken).
4. **Lock-in report to Andrew -> his release of 0.0.0_AB_MSTR on launching. That word is the only remaining gate.**

Open, non-gating: the P1.1 threshold convergence (COO/CTO — @3b2982e290 vs Andrew's ~23:4xZ no-filter
word; enters a TO only on a converged cited word). Per the drive-open durability rule, CVO lands the
converged outcome in `org/surprise_channel/ADVI_PERFRP/INVESTIGATION_v1.md` when it exists.

— 3.0.0_SA_CVO

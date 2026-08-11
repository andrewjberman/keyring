# RULE-14e CERTIFICATION -- CRO~A INF STOP MECHANISM + REPAIR (chapter 01)

**Certifier:** 3.0.0_SA_CVO · **2026-08-11, pass run 0632-0638Z** · **archetype:** VALIDATE
**Subject:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/INF_ATOMDECOMP_RUN_20260811/01_STOP_MECHANISM.md`
(authored ~0445-0515Z). **Request:** 1.0.0_SA_CTO 062446Z. Live reads 2026-08-11T06:32-06:36Z.
**Operative post-cert frame:** COO ruling 063239Z (direct-SSM collision mechanism; 13:47Z-only
trigger; steps-satisfy-deploy-obligation) -- cited where it touches a cell.

---

## VERDICT: **CERTIFIED** -- diagnosis and repair mechanics all verified. The repair-EFFECTIVENESS
## cell is explicitly PENDING-EXERCISE (C_01's guard verdict on the restored snapshot was not yet
## observable at 06:36Z; the production proof is the 13:47Z scheduled cycle, exactly as the chapter
## itself framed and COO has since ruled). Zero cells refused.

## GROUNDING TABLE

| Cell | Chapter claim | My re-derivation | Verdict |
|---|---|---|---|
| The freeze anchor | last `pipeline-complete.json` 2026-07-31T14:56Z | head-object: **14:56:49Z exact** (third independent confirmation tonight) | CONFIRMED |
| The guard | `nna_coverage_guard.py:320` raises on partition account-loss; BLOCKS, not WARNs | `:320` `raise NNACoverageRegression(...SERVED NNA...DROPPED...)` verbatim; C_01 `:884-885` "These BLOCK. They are not WARNs" | CONFIRMED |
| Universe mechanism | accounts_v2 rep-allowlist; `INFLECTION_REP_IDS = {3, 6, 10, 11, 12}` at `convert_orion_api_to_silver.py:632` | `:632` exact, carrying the Andrew-direct rep-10 ruling comment (@93c898445) the event-A narrative depends on | CONFIRMED |
| The restore (F2) | 26,371 rows restored; upload 05:13:28Z VersionId `Ls9G...wCa`, prior `n3ep...GpAm` retained; union = 1,434,111 lines / 850 accounts | `list-object-versions`: both VersionIds EXACT, current IsLatest 05:13:28Z (39,948,483B), prior retained (39,257,615B) -- one-call rollback structurally real. **Content recount from the live object: 1,434,111 lines, 850 distinct accounts -- both EXACT** | **CONFIRMED** |
| Vendor-side cause, not deploy | pull bytes unchanged since 07-02 at claim time | TRUE AT VINTAGE; the deployed object NOW reads 05:47:12Z because DS discharged F1 after the chapter (below) -- movement, not error | CONFIRMED at vintage |
| Repair effectiveness | QA run dispatched 05:14:35Z; "the 13:47Z scheduled cycle remains the production proof (ad-hoc is QA, never production evidence)" | QA chain observed MID-FLIGHT: `canonical_performance` through 2026-08-11 written 06:18:33Z (C_00 passed); `canonical_nna` still ends 2026-07-31 (1,426 partitions) -- **C_01's guard verdict on the restored snapshot not yet observable.** | **PENDING-EXERCISE, as the chapter itself honestly graded.** Fold owed after 13:47Z |
| Findings-beside-the-path | pull script deployed-with-no-repo-home (MISSING_IN_REPO) | TRUE AT VINTAGE and **discharged post-authoring by DS**: baseline byte-exact repo-homing @9b29609e42 (05:33Z), CPR-1 union-preserve @9196959b53 (05:39Z -- F1's durable remedy), twin sync @76386cd21c, redeploy 05:47:12Z. *(The union-preserve fix's own verification = DS lane + the Sunday 08-16 exercise; not certified here.)* | CONFIRMED at vintage; remains-list partially discharged |

## THE ESTATE MOVED UNDER THIS CERT, AGAIN -- stated as a pattern, not a complaint

Every certification tonight has found part of the subject's "what remains" list already executed
by the time the cert ran (CPR-4's D_04 fix mid-pass; F1's union-preserve + repo-homing here; the
cottonwood addendum chain). This is the fabric working fast, and the records have kept up honestly
-- but it means EVERY cert I issue is a vintage-stamped snapshot, and consumers of the SSOT matrix
should read the cert timestamps as load-bearing, not decorative.

## POST-CHAPTER MECHANISM, folded for completeness (COO 063239Z, not a chapter cell)

The 0558Z direct-SSM republish attempt ran mid-chain on the same runner and **C_01's guard refused
the mode-incoherent input** -- launch succeeded, republish never executed, no data harm. Direct SSM
is a FIFTH armed dispatch path carrying neither the trigger's env export nor the dispatch lock.
COO has ruled step-4-class refires to the scheduled cycle only. For the matrix: the guard that
stopped the pipeline for nine days and the guard that refused the bad republish are THE SAME
CONTROL BEHAVING CORRECTLY BOTH TIMES -- the chapter's core reading (the guard is right, the
architecture re-derives history it should not) survives its second live exercise of the night.

## What you should have asked but did not (Doctrine §7)

How many OTHER armed dispatch paths the INF runner has. The chapter found the aggregator's direct
invoke had silently replaced the documented rule as the live dispatch (finding 3); COO's collision
measurement now adds direct SSM as a fifth path. Nobody has enumerated the full set: EventBridge
rule, aggregator direct-invoke, inf-gold-trigger lambda, direct SSM, and whatever the 08-06 UNTRACED
manual fire was. A pipeline with N undocumented ways to start is N-1 collision classes waiting for
the next repair window -- the W-C/W-D refactor should carry a DISPATCH-PATH CENSUS cell (enumerate,
then close all but the sanctioned one) before the mutex remedy is designed, or the mutex will be
sized against an unmeasured N.

-- 3.0.0_SA_CVO

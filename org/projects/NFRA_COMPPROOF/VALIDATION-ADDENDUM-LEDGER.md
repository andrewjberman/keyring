# Graph + Tooling e2e Validation -- ADDENDUM LEDGER (fix -> retest -> revalidate)

**Owner:** 2.0.0_SA_COO~B (NFRA_COMP* program coordination)
**Source:** ~B's Andrew-direct 52-agent e2e validation, `org/tier2_senior/0.8.0_AE_CloudComp/GRAPH_TOOLING_VALIDATION_REPORT_20260701.md` (commit 4e9f0258d), Nessie HEAD 5cca1bdd.
**Verdict:** VALIDATED_WITH_GAPS -- graph categorically complete + current (52 node/52 edge cats, 19844n/34834e, provenance CURRENT); 27/32 tools PASS with spot-checks matched to LIVE AWS/TF/source; 0 hard failures; 3/5 cross-layer walks connect. Trustworthy for load-bearing cases.
**This is the COMPPROOF-B SEED** (the first honest, source-grounded e2e proof-of-tooling) -- routed to CTO 132020Z-adjacent for the COMPPROOF PRD baseline + gap-list.
**Andrew-direct addendum:** Step 1 re-verify -> Step 2 fix (per error, to owner) -> Step 3 revalidate (re-run affected checks / full workflow -> 0 open gaps).

## DISCIPLINE GATE (Rule-22 / NEVER#5)
E3 + M1-M4 are self-disclosed with file:line but NOT adversarially re-verified; comp-grep/comp-glob/comp-validate were UNTESTED (transient rate-limit hit 8 agents). A self-disclosed error is a HYPOTHESIS until adversarially confirmed -- **no fix dispatches for the unverified set until ~B's Step-1 re-verify greens them.** E1 + E2 are grounded structural HIGHs (root-caused file:line) -> proceed now.

## ERROR REGISTER

| ID | Sev | Class | Finding (file:line) | Owner | Status |
|---|---|---|---|---|---|
| E1 | HIGH | naturalness | comp-which routes read Qs ("what lambdas read bucket X") to comp-aws DERIVE (8-min rebuild); comp_route.py ignores the manifest mode:query\|rebuild tag | ~E (comp_route) + ~B assist + CTO | **FOLDED INTO COMPROUTE default-router re-scope** (Andrew-direct). E1 = the mode-GATE hard prior. Design converging CTO/~E/~C; dispatch on CTO ruling. |
| E2 | HIGH | connectivity | portal serving->prod provenance dead-ends: SERVED_FROM lands on coarse opal-data-portal-v2 BUCKET not key-level S3Keys (derive_runner.py:1300); Endpoint->Lambda = 0 edges | ~D/DE (globgrph/TSGRAPH derive) | BANKED into the (a) GRAPHUNI derive-fidelity follow-on (~D ACK 131948Z) -- one derive pass, dispatched with (a). |
| E3 | HIGH | tool | comp-drift reports a CLEAN lambda as a deploy break: drift_cli.py:217 passes target positionally to `comp-lambdamap parity` (no positional -> rc=2) | ~B author / COO~B exec-land | **EXEC-LANDED 17eaca870** (parity --json + target-verdict filter; IAM scoped to target's role via graph ASSUMES edge; estate drift -> informational. Two-dir self-test PASS: clean=EXIT0, real-drift=EXIT1. CVO~B Step-3 re-run) |
| M1 | MED | tool | comp-trace S3 direction inverted | TBD on re-verify | RE-VERIFY (~B Step-1) |
| M2 | MED | tool (SEV1-adjacent) | comp-types fabricates + PERSISTS a consumer graph for 0-importer nested types (MP/benchmark surface) | TBD on re-verify | RE-VERIFY (~B Step-1) -- MP/benchmark = critical-surface, verify carefully |
| M3 | MED | tool | comp-parity headline is a hardcoded frozen string (Rule-22 reserved-word: "PROVEN" as a live verdict, comparators never run) | ~A | **LANDED 0f3006763** (AE-authorable, ~A author-line; self-test both-dir PASS -- reserved-word removed + honest RECORDED relabel, function intact rc=0; CVO~B Step-3 re-run) |
| M4 | MED | tool | comp-heat federated mode crashes on its own default query | ~A | **LANDED b36791252** (AE-authorable; bash-escape single-quote in _trino_fed.py; self-test both-dir PASS -- shlex POSIX round-trips all 3 canonical queries exact; live-Fargate run deferred to CVO~B Step-3 if warranted) |

## UNTESTED (rate-limited) -- Step-1 must exercise
comp-grep, comp-glob, comp-validate -> PASS-or-error. (comp-grep/glob are the router's own fallback surface -> important they PASS.)

## SEQUENCE
1. **Step 1 (~B, GO'd 131831Z):** re-verify the 3 untested + adversarially confirm E3 + M1-M4 (live repro + file:line). RAVC COO~B -> the CONFIRMED set.
2. **Step 2 (on confirm):** dispatch fixes to owners. E1 rides the COMPROUTE increment; E2 rides (a); E3 = ~B; M1-M4 = owners TBD (M2 critical-surface care).
3. **Step 3:** revalidate -- re-run the affected checks / the workflow -> 0 open gaps. CVO~B verify-gate (COMPPROOF-adjacent honesty).

## STATUS UPDATE 2026-07-01T1326Z
- **Step-1 re-verify COMPLETE (~B, RAVC'd):** all 5 errors CONFIRMED with live repro + file:line, 0 retractions; the 3 rate-limited tools (comp-grep/comp-glob/comp-validate) all PASS. Caveat CLOSED. Rule-22 satisfied -> the confirmed set is actionable.
- **DISPATCHED:**
  - E1 -> **DECOMPOSED into the COMPROUTE default-router increment** (CTO BLESSED 132556Z): DR3 (~B) = manifest mode:query|rebuild tagging; the hard mode-gate is DR1 (~E) Stage-A. E1 closes when a read routes to a query surface (0 mode:rebuild).
  - E2 -> **~D (a)-derive-fidelity queue** (banked; one derive pass with the (a) cross-script bridges; CVO~B pins the coverage-proof).
  - E3 -> **~B authoring** (whole-estate parity --json + filter; scope --deep IAM to target) + two-direction self-test (clean passes + real break caught) -> **COO~B exec-lands** (org/modules/graph/ = exec-lane).
  - M1-M4 -> **~A comp-tool correctness sweep** (dispatched 132612Z; ~A ACK). M2 (comp-types, MP/benchmark SEV1) = comp-surface-check + CVO~B verify.
- **Step-3 revalidate:** CVO~B-gated, after the fixes land -> re-run the affected checks / the workflow -> 0 open gaps.

## REVALIDATE PROGRESS 2026-07-01T1511Z
- **E3 (17eaca870) REVALIDATE GREEN** (~B, served-behavior): clean lambda EXIT 0, false break dead.
- **M4 (b36791252) REVALIDATE GREEN** (~B): comp-heat federated rc=0, real rows, no crash.
- **E1 REOPENED (grounded, NOT closed -- COO~B under-verified, ~B was right):** my earlier "E1 CLOSED (stale checkout)" was WRONG. ~B pulled the flip (94b64a5af confirmed ancestor) + STILL got comp-aws-derive TOP; I reproduced it on MY flipped checkout. It's PHRASING-brittle, not env-state: "what lambdas read from opal-data-bd" (no "bucket") -> comp-parity (derive excluded, correct); "what lambdas read from THE opal-data-bd BUCKET" -> comp-aws derive (cloud.derive.refresh, write_path:true) TOP in the near-tie. The word "bucket" lexically matches derive's "cloud-graph estate topology" desc hard enough that the write_path HARD-gate does NOT fire. So the shipped E1 fix does NOT hold for common phrasings -- a success-shaped-but-wrong (commit landed + fixture-cert GREEN [comp-build cases] + my spot-check passed, but the live agent-facing behavior is broken). ROUTED to ~E (DR1 exclusion) + ~C (provider/surface) + CTO (hard-gate ruling). **ROOT-CAUSE FIX (Andrew-direct): a POTION (Model2Vec static-embedding) SEMANTIC MATCHER** replaces the lexical token-overlap that causes this -- "read from the bucket" would semantically land near consumer/reader caps (comp-blast/comp-kuzu READS_S3), not near "derive/rebuild," regardless of the "bucket" token. Immediate: ~E closes the write_path hard-gate gap (fires any phrasing). Root: the Potion precision-matcher = a COMPROUTE follow-on increment (CTO+~E shape; shadow-first vs the lexical baseline on the fixture + these E1 phrasings; COMPLEARN-fed).
- **M3 (0f3006763):** landed; formal revalidate rides the CVO~B Step-3 sweep.
- **M1 LANDED** (e72679f5c, ~A): comp-trace inverted S3 direction -- fixed via a TIER-INVARIANT (gold script writes gold/platinum never silver/bronze; dropped exactly the 2 false silver/allocations writes, 0 real edges lost -- chose it over 3 var-tracker hacks that dropped 17 REAL reads). Two-direction verified (extractor-unit; e2e needs a graph rebuild -> CVO~B Step-3/nightly).
- **M2 LANDED** (db5214e6c, ~A, SEV1): comp-types fabrication -- cmd_index ran TenantLayout-specific searches for ANY type -> 38 fabricated sites + a bogus persisted PASS manifest on 0-importer types. Fix gates those searches to type_name=='TenantLayoutConfig'. Verified: 0-importer types index 0 == blast=0; TenantLayoutConfig 65 intact; comp-surface-check clean. CVO~B SEV1-verify rides Step-3. (Commit MSG cosmetically corrupted -- backtick-in-double-quote cmd-subst; CODE DIFF correct+verified; transparent, lesson banked.)
- **ALL 4 M's DONE** (M1/M2/M3/M4, each two-direction-self-tested). Addendum tally: E3 GREEN + 4 M's landed = 5 of 7. E1 REOPENED (hard-pre-filter + Potion). E2 (~D/DE) rides (a).
- REMAINING for full revalidate: E1 (~E hard-pre-filter fix -> ~B revalidates both phrasings) + E2 (~D/DE, rides (a)). CVO~B Step-3 is the authoritative independent close.

## NOTES
- E1's convergence with the Andrew-direct COMPROUTE default-router re-scope is the headline: ~B's independent validation root-caused the exact problem Andrew directed (read intent -> rebuild tool). The fix is ONE increment, not two.
- ~B stays OFF COMPPROOF tasking (Andrew hard constraint) -- but the validation + this fix->retest->revalidate addendum IS ~B's Andrew-direct lane (not COMPPROOF), so ~B on E3 + E1-assist is in-scope.

# ADHC_GLDINC — A_01 nondeterminism class adjudication (CTO ruling)
**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

**Session:** 2026-06-11 ~22:58–23:04Z (ws CTO 1.0.0_SA_CTO, event-driven via inbox Monitor)

## Trigger
DS 225838Z proactive finding + AE 230039Z census escalation: the A_01 full-path
nondeterminism (thread-completion-order concat -> keep='last' dedup, no total-order)
claimed as a copy-pasted defect CLASS across bd gold (A_03/B_01/A_04/
build_canonical_prices_v2/7x E_*/A_00-maybe). Both asked for class-extension of the
A_01 fix-oracle-first ruling. DS 230216Z added the deploy-discipline view + held A_03
(evidence phase needs a deterministic oracle). prices_v2 flagged as critical node
(canonical_prices feeds A_03/B_01/B_02/C_*/D_*).

## Independent verification (before ruling — empirical, line-cited)
Direct Read of every cited site. The dedup-signature grep is too coarse; the true
discriminator is the parallel-load CONCAT ASSEMBLY SHAPE:

| Script / site | Assembly | Class |
|---|---|---|
| A_04.client_dimension L114-120 | `dfs.append(fut.result())` in `as_completed` | **CLASS-N (nondeterministic — the real A_01 defect)** |
| A_03.positions_cube L885-916 | `dfs[futures[future]] = result` (index-slot) | CLASS-I (deterministic) |
| B_01.holdings_lots L247-264 | index-slot | CLASS-I |
| build_canonical_prices_v2 L97-130 + L580 | index-slot both sites, sorted keys | CLASS-I — **prices_v2 CLEAN** |
| A_03 L333 _latest_cum_units | upstream-sort dependent | AE to confirm (expected PASS; input CLASS-I-rooted) |

AE's 230228Z self-corrected census (independent, crossed in flight) converged EXACTLY
— index-slot deterministic: A_00, A_03, B_01, prices_v2, E_02/03/04/09/10; completion-order:
A_04 only (+E_13 unverified). A_03 production etag byte-identical rerun pairs corroborate.
Two independent derivations, same result.

## Ruling (DS 230255Z, AE 230339Z, COO CC 230400Z)
1. **Fix-oracle-first class-extension GRANTED, scoped to CLASS-N**: A_04 now, E_13 if
   confirmed. A_01 remedy verbatim (provenance _file_date+_intra_pos + total-order sort;
   ref A_01 L188-189/L239-245/L496-534), materiality probe first (targeted x2 loads, NOT
   full builds), changed-keys delta where served output moves. A_04 serves household dim
   (primary_architect/implementor) -> per-script never-widen sign-off (CTO+COO) +
   in-commit verified-drift acceptance record (A_01 73ec87a84 model). E_13 batch-eligible.
2. **CLASS-I = NOT broken oracles**: no standalone pre-fixes, no materiality burn.
   Explicit-determinism hardening (0-diff verified vs unmodified oracle) folds into each
   script's GLDINC incremental engineering. **A_03 un-hold RATIFIED** — GLDINC proceeds
   B_01 next, A_04 last with its fix.
3. **Standing convention RATIFIED**: new gold parallel loads use index-slot assembly or
   A_01-style provenance; completion-order append into order-sensitive dedup = defect.
4. **Routed to COO** (low-pri decomposition): (a) code-read census of inf+cot gold trees +
   bd C_*/D_* completeness (zero runs); (b) ds-precommit-check AST rule candidate
   (append-under-as_completed feeding keep='last'/'first' dedup).
5. **Cost discipline held**: no ad-hoc gold runs; shadow harness remains the detector.

## Compiler Tools
No comp-* runs: the adjudication required line-level loader-shape classification (direct
Grep/Read of 5 gold scripts), which the graph does not encode; no code/infra change was
made this session (ruling only), so no Rule-20 pre-change graph check applied. Blast
radius of the prices_v2 question was already enumerated in AE's census (consumer list)
and dissolved by the CLEAN finding.

## Net
GLDINC unblocked (A_03 hold released); defect class narrowed from claimed ~10 scripts to
1 confirmed (A_04) + 1 TBV (E_13); prices_v2 clean by two independent reads. The
escalate-early + verify-before-fix discipline worked end-to-end.

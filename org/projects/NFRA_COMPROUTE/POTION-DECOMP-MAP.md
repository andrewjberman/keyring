# NFRA_COMPROUTE -- POTION precision-matcher increment (DECOMP MAP)

**Andrew-direct** ("throw potion nlp on that ... quick on the uptake") -> the semantic-matcher fix for the router's lexical brittleness (the E1 "bucket"->comp-aws-derive class + the adversarial-vocab residual).
**Arch:** 1.0.0_SA_CTO -- `docs/architecture/NFRA_COMPROUTE_POTION_DESIGN.md` (48115686e) is the authority; this map decomposes it.
**Coordinator:** 2.0.0_SA_COO~B | **Staffing:** ~E engine, ~C surface, CVO~B shadow-eval, CTO arch-lead + leg-GO RAVCs.
**Root cause:** the stage-2 relevance signal is LEXICAL token-overlap -> "bucket" lexically matches derive's estate-desc + outranks a soft write_path signal. Two tracks: fix the safety gate (T1) + swap the relevance signal to semantic (T2).

## LEG T1 -- write_path HARD PRE-FILTER (~E, immediate safety; DISPATCHED 152601Z)
CTO owns the gate-hole: the write_path ruling was phrasing-scoped + top-1-only, so "bucket"-phrasings + the near-tie surface bypassed it. FIX: cap.write_path==True is a HARD PRE-FILTER DROP -- removed from the candidate set BEFORE lexical/posterior ranking AND across the near-tie surface, for read/navigate intents. AC: read intent surfaces 0 write_path caps for ALL phrasings (~B revalidates "...opal-data-bd" + "...bucket" + state-machine/invokes). This gate STAYS after POTION (structural safety net) + is the pre-POTION baseline gate. Independent of Potion -- ship first.

## LEG T2-ENGINE -- the Model2Vec relevance-swap (~E)
Model2Vec (POTION) static embeddings: offline-cache the ~57 cap-description vectors; at route-time embed the intent (token-avg, sub-ms, no GPU/serving) -> cosine -> the stage-2 RELEVANCE input (lexical -> semantic). route() stays 3-stage; ONLY the stage-2 relevance signal swaps. Structural gates (write_path/surface-priors) UNCHANGED + hard backstop; COMPLEARN unchanged. Recommend semantic-PRIMARY + lexical-exact-NAME secondary boost. ANTI-DRIFT: pin the Model2Vec version (a bump re-runs the shadow-gate); cap-vector STALENESS gate (cached-vector-hash == cap-description-hash; a desc edit without re-embed = STOP); ONE home/owner for model+vectors+embed-fn. AC: the swap is a pure relevance-input change (gates untouched); version-pinned + staleness-gated; runs inline sub-ms.

## LEG T2-SURFACE -- thinking-window richer-vector arm (~C)
The 3rd shadow arm: embed the agent's THINKING-window (recent reasoning pre-tool-call), not just the bare query, into the intent vector (Andrew's richer-signal idea). Surface integration of the semantic ranking into comp-which. AC: a thinking-window intent vector is available where the reasoning exists (augments, not replaces, the query vector); comp-which surface consumes the semantic ranking; comp-surface-check clean.

## LEG T2-EVAL -- the shadow-eval + FLIP-GATE (CVO~B, load-bearing)
SHADOW-FIRST: run POTION in parallel with the live lexical router, log both. 3 ARMS measured: pure-semantic vs blend (semantic+name-boost) vs ~C's thinking-window -- pick the winner. EVAL CORPUS: the fixture + the E1 "bucket" phrasings + the adversarial-vocab set + the **COMPPROOF-B 20-run labeled intent->cap pairs** (B<->C synergy: B's blind-run labels ARE C's ground-truth -- wire C1 to consume them). THE FLIP-GATE (all 3 REQUIRED, MEASURED not assumed): (1) net precision GAIN over the lexical baseline; (2) ZERO structural-gate regression -- read-never-surfaces-write_path 100% (E1 class, NON-NEGOTIABLE; ONE regression blocks the flip regardless of net gain); (3) ALL E1 "bucket" phrasings FIXED. Static embeddings trade nuance for speed -> PROVE the win, don't assume it. Flip only on all 3 GREEN (same discipline as the DRV shadow-flip). AC: the 3-arm shadow-eval + the winner + the 3-criterion flip-gate verdict; CVO honesty-gate (held-out data).

## SEQUENCING
T1 ships first (safety, ~B revalidates) -> T2-ENGINE + T2-SURFACE build in shadow (interface-locked ~E<->~C) -> T2-EVAL runs the 3-arm shadow -> flip ONLY on the 3-criterion gate GREEN. This IS NFRA_COMPPROOF-C1 (the COMPROUTE efficacy eval) operationalized -- C1's eval consumes the 20-run labels. CTO arch-leads + RAVCs each leg GO.

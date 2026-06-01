# /spot-check cycle 13 — 1713Z 2026-06-01 — CLEAN-no-fix

10 commits triaged (11 delta − 1 own). MDPF cohort-1c reconcile + Schwab-re-derive scope + FIND_INSURE PMA-segregation. No alignment-metadata drift requiring CVO fix, no Tier-0 ledger. 13th consecutive clean.

KEY UPDATES (breadcrumbs):
1. MDPF cohort-1c reconcile CLOSED (DE 081be4a0e): -$172M = -$25M SMA-breakout + -$147M v0.9 BD->Schwab residual re-level. **FE fix = Andrew-direct FOLD (DE-validated: sma additive-separate, keeps SMA in non_model both sides => no SMA-step; DS~B withdrew fold-of-residual rec). SUPERSEDES my cycle-12 breadcrumb (RD~B F5).** Source-partition methodology_version flip (v0_8_ruling2<=5/17 -> v0_9_1>=5/18) corroborates the data-model at producer.
2. Schwab re-derive SCOPE-CERT (DS~B ab923898b): 1/16-5/17 EXACT-feasible (4/15 anchor $1,556M Schwab vs $1,699M full-book, 17 unmatched ~$5.9M); 1c=bandaid-estimate; pre-1/16 NOT re-derivable; 49F-scope. MATCHES my primed 5-point verify (164639Z ACK). Re-emit itself PENDING — I fire on DS~B re-emit-done ping. DE built serving continuity-verify harness in parallel (c7ab91381, FAILs on current seam / PASSes post-re-derive).
3. LD-0012-class naming fixes self-caught+fixed: 22bb6f9bf (backwards headline comment 1b=sma/1c=non-model -> explicit 1a=model/1b=non-model-PLUG/1c=SMA, doc-only values unchanged) + 3af2911c7 (stale '1c non-additive sub-slice of 1b' -> Andrew-canonical 1c ADDITIVE+DISJOINT total=1a+1b+1c). Both DS~B, per Andrew/CTO.
4. FIND_INSURE PMA segregation (DS~C 62fd126c4): PMA off #1 IMO slot -> adjacent_wm_targets (data+score preserved, relabeled true_identity, NOT deleted); CTO ruling 162518Z + COO off-slot GO; 24->23 IMOs, lincoln-investment #1; #79 WRONG_DOMAIN flagged; tests 3 pass. + source-list-corrections defensive layer (4fe0a7cb2: #79 PMA + #31 eagle-strategies flagged, no name/url mutation). NOTE: deeper relabel/drop A/B may still be PENDING_ANDREW_AB; the off-slot SEGREGATION (reversible, data-preserved) is the GO'd scope.

Substance-meta: -$172M decomposition both-explained; 24->23 plausible; backwards-comment = the LD-0012 catch (fixed). Checkpoint -> 62fd126c4.

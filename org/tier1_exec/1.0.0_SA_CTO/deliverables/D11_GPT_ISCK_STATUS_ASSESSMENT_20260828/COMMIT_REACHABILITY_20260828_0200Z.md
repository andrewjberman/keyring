# ISCK / D11 — COMMIT REACHABILITY TABLE (machine-derived, 2026-08-28T02:00:11Z)

**Why this exists:** the GPT memorandum (§4.7, same folder) found the status report's push-state prose
ambiguous ("origin carries X" beside "X is LOCAL at writing"). It asked for a generated table stating,
per cited commit, whether it is an ancestor of local HEAD, of `origin/CLOUD`, and of the declared
round-2 boundary pin. This is that table. **Method:** `git fetch origin CLOUD` then
`git merge-base --is-ancestor <c> <ref>` per cell, at `1.0.0_SA_CTO~X`, laptop. **Negative control:**
`deadbeef00` -> NOT-AN-OBJECT (the instrument can return NO). **Denominator:** 36 cited commits,
36 resolved as objects.

**Refs at read:** local HEAD `5a58e6cc5d` · `origin/CLOUD` `3fbb493cda` · boundary pin `9760630ae7`
· `git rev-list --left-right --count HEAD...origin/CLOUD` = **34 ahead / 0 behind** (fast-forward).

**Push is INTEGRATOR-ONLY** (LD-0367 rule 2 / LD-0368 gate refused `git push origin CLOUD` from this
seat at 01:57Z; not overridden). The 34-commit tail rides `0.0.0_AB_MSTR`'s integration window. So the
memo's step 1 ("push the intended amendments") is executed here as THIS TABLE, not as a push.

| commit | subject | ancestor of HEAD 5a58e6cc5d | ancestor of origin/CLOUD 3fbb493cda | ancestor of boundary pin 9760630ae7 |
|---|---|---|---|---|
| d869c9ffe0 | ruling(ISCK): Andrew adopts Issue 3 as the Identity-State Co | YES | YES | YES |
| b56bd2b7f0 | evidence(WP-0): the C2/C3 evidence estate is PINNED -- and t | YES | YES | YES |
| 208308bd47 | amend(WP-1 + v0 fix): the PRD amendment set is COMPLETE -- a | YES | YES | YES |
| 2cdda17b51 | contract(WP-2 draft): ISCK Identity-State Contract v0 -- 10  | YES | YES | YES |
| 21d6fc7325 | contract(v0.1 boundary): 21 findings from 3 seats, ALL fixed | YES | YES | YES |
| 14e6bcc50d | charter(round 2): the two external reviews synthesized -- te | YES | YES | YES |
| 9fa5a91af5 | feat(R2-1 fabric split): location becomes TWO FAMILIES -- ex | YES | YES | YES |
| 1b08f0e37e | fix(round-2 batch 1: R2-3 warrants + R2-6 uniqueness): the s | YES | YES | YES |
| 5ffb98936c | fix(round-2 batch 2): the forbid half becomes the idiom, the | YES | YES | YES |
| e07b9efec0 | feat(R2-5 absence cell): observed_absent lands -- the nerves | YES | YES | YES |
| 7b6629d3b7 | feat(R2-7 mint receipt): LAW 1's compensating control is DEF | YES | YES | YES |
| 547730fd8a | feat(R2-8 BRIDGE_ASSERTION): the first load-bearing consumer | YES | YES | YES |
| 7a1192b0c3 | fix(bridge arm isolation): five isolating mutants -- ablatio | YES | YES | YES |
| 4f66d2edf2 | record(3.17 declared_cardinality): the CV-1 certification's  | YES | YES | YES |
| d2fc841873 | gate(run_gates.sh + mint coverage): gates run against ATOMIC | YES | YES | YES |
| 3c37267b91 | fix(battery-integrity batch): path-grained assertions close  | YES | YES | YES |
| f18f4cf8d4 | gates(COO-R2-1): the RUN_GATES summary line prints the candi | YES | YES | YES |
| 1061546c63 | design(R2-2): events are the truth, status is a projection - | YES | YES | YES |
| bfcebc58c5 | design(R2-2 landing checklist): eight lines the implementing | YES | YES | YES |
| 8f8fe7db5f | schema(ARM-4 adjudicated): 25 of 25 candidates ruled -- 4 fo | YES | YES | YES |
| 05086d045c | doctrine+schema(ARM-4 CUT 4, option B): FREE meant free of R | YES | YES | YES |
| 2795145b63 | contract+schema(DT-R2-6): contradicted -> adjudicated_by RET | YES | YES | YES |
| d144e7937c | contract(sec 3.2 carrier): contradicted is LEFT by SUPERSESS | YES | YES | YES |
| 7c093caff5 | design(R2-2 fold binding): the two verification_standing row | YES | YES | YES |
| db4062c3a7 | probe(ARM-3 repairs): census 94 of 95, ZERO open -- and the  | YES | YES | YES |
| 9fb81b743a | probe(ARM-4 consume gate): the gate consumes the ruling -- a | YES | YES | YES |
| 6245dc0a3d | probe(loader guard): the duplicate-key defect I shipped in t | YES | YES | YES |
| bb7444a08e | probe(entry guard): CRO~X's superset attack landed -- my loa | YES | NO | NO |
| 9760630ae7 | gates(runner): the summary subtracts the consume gate's adju | YES | YES | YES |
| ece1ac0f41 | boundary(ISCK round 2): CUT on both attackers' dry -- ~40 fi | YES | YES | NO |
| 7c776ccc5d | boundary(round 2, amended): exit condition 2 MET -- package  | YES | NO | NO |
| 8bce3fa495 | boundary(round 2, amended 2): CRO~X's re-verify found three  | YES | NO | NO |
| f6269a9a82 | boundary(round 2, amended 3): condition 2 EXERCISED not argu | YES | NO | NO |
| 1a5624ae2a | govern(D11 L0): name CRO family as v1 emission authorizer an | YES | YES | YES |
| 5cd7726d8e | ledger(D11 tick-2 call CLOSED-CERTIFIED): the authorizer cha | YES | YES | YES |
| f6b4fb0c56 | carrier(self-drive D11): the XXX.md Step 1b-F clause lands B | YES | YES | YES |

**Reading:** the boundary pin and the boundary record itself are on origin; the three boundary
AMENDMENTS (`7c776ccc5d`, `8bce3fa495`, `f6269a9a82`) and DT~X's post-boundary entry guard
(`bb7444a08e`) are LOCAL to this device until the next integration window. That resolves the memo's
§4.7 ambiguity: the status report was right on both counts — the pin was on origin, the amendments
were not — and the prose failed to keep the two sets apart.

**Gate state at local HEAD 5a58e6cc5d (atomic extract, `run_gates.sh`, 01:59Z):** six of six exit 0 |
11 open candidates (ARM1 9, ARM3 0, ARM4 2 of 20 undisposed) — identical to the pin.

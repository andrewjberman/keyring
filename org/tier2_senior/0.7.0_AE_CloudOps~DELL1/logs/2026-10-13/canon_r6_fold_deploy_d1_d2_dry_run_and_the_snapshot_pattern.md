# MDPF_CANON round 6: four scripts, the package with its commit stamp, one dry run, and a premise about tax snapshots that did not hold -- 0.7.0_AE_CloudOps~DELL1

**Date:** 2026-10-13 (UTC; ~13:34Z - 14:10Z, after a day-long wait for the GO)
**Task Order:** ADHOC.canon-r6-fold-deploy (risk WORLD)
**Status:** COMPLETE
**archetype:** DEPLOY
**Branch:** box/dell1

## Objective

Deploy CN-f-1's four gold scripts to `code/scripts/gold/`, the gold lambda package at pin `51cfc93ea8` with
`MDPF_GOLD_COMMIT` set to the full built SHA in the same apply, and run one `qa_local` dry run; leave the emitter lambda
untouched.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| r6_cn_f_1.py | contract / seams (C1) | PASS | 13 of 13 and 6 of 6 arms |
| mdpf-code-equality.py | whole tree before and after; --files | PASS | 40/37 -> 44/33; four names NAMED EQUAL; no other change |
| safe-deploy.sh | four named files | PASS | gate PASS, VERIFY OK x4 |
| build_package.py / safe-apply.sh | --pin 51cfc93ea8; planfile apply | PASS | plan 0/1/0, only code + MDPF_GOLD_COMMIT |
| lib/opal_naming address() | tax store addresses | PASS | store keys computed from the builder, not typed |
| comp-rail | three denials (an AWS listing read as freshness, a census piped to a receiver, a trailing comment swallowing a call) | WARN | each ran nothing; answered with the named tool or an audited rail-checked line |

**What worked:** the before print read the day's own manifest for the state keys and the builder for the tax store
addresses, so the after print was a diff, not a re-derivation.
**What failed:** none of the acts; the order's premise (tax stores are no-op creates on a same-day re-run) was wrong.
**Gap found:** `taxsma` snapshot keys carry the response sha256, so every gateway acquisition is a new object.

## Work Completed

1. **GO and preconditions.** GO msg 4846 at 13:34Z (W8-S4 read @0c2611c918); 2b pin ancestor of origin, four files pin==HEAD;
   2c CTO half SIGNED @08d546b134; 2d dispatch complete, manifest after 13:30Z at 13:31:51Z; 2e/2f no act in flight.
2. **L1 before print:** whole-tree equality, prior VersionIds of the four keys, function + env + deployed manifest commit,
   the Scheduler input verbatim, 16 served objects, state keys and tax stores by VersionId, emitter CodeSha256.
3. **D1 (L2-L5)** at 13:48Z, after the 13:40Z accrual run's sync had finished: NAMED EQUAL x4.
4. **D2 (L6):** built from the pin, uploaded, the one `.tf` value and comment committed (`1c1ac084c8`), targeted plan graded
   per attribute (only code + `MDPF_GOLD_COMMIT`), applied 13:55:34Z, CodeSha256 equals the base64 of the built digest, env
   equals the in-zip `source_vintage.commit`, re-plan clean.
5. **D4 (L7):** 13:57:03Z-13:58:18Z, 200, green, errors [], 16 of 16; 16 served objects, control key, existing store
   objects and the emitter unchanged; two NEW workbook snapshot objects at 13:58:14Z. Stopped, filed row D1-S20, no rollback.
6. **L8:** after print 44/33; the four D1 names EQUAL; no other change; emitter control unchanged.
7. **After the issuer's answer (msg 4871):** no rollback, C4 amended, proof instance filed and the order flipped.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Started D1 at 13:48Z, not 13:36Z | the accrual bridge's 13:40Z code sync reads this prefix; the order's 2d names the dispatch and the lambda, and a mid-sync copy is avoidable |
| Stopped at the two new objects instead of rolling back | the order says STOP and report; a code rollback removes nothing write-once and would put pre-fold code on tomorrow's first folded fire |
| Stated the deviation in L7's proof before closing | the ledger records what was measured, not what was expected |

## Open Items

- The first-fold acceptance is the issuer's read on 2026-10-14 13:30Z.
- Detached worktrees `/c/dev/wk-aw1-pin` and `/c/dev/wk-firmbkts-31` remain on disk.

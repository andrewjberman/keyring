# 1.0.0_SA_CTO~Y -- session close: the K-sweep positive arm, the 604 split, the permuted-arm card, and fourteen window holds

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE, COORDINATE
**Window:** 2026-08-29 06:25Z (last log `session_0333-0625Z_d11_segment_a_b_c.md` @b45042c8f6) -> 20:55Z. Paired with `1.0.0_SA_CTO~X` on D11 per Andrew's 03:45Z word.

## What happened

1. **The K-sweep positive arm (issuer's pre-cut question 81251).** The issuer measured a plane mismatch: `pipesym_to_firm`'s left endpoint is `symbol`, the fusion carrier is "CLOUD_NODE", so the firm-carrying arm would need a declared cloud-node -> symbol chain. Measured at the content-addressed inputs instead of the labels: the 19,482 fusion population is the L2 STRUCTURE id set across four layers (portal 10,365 / ms 6,047 / aws 1,733 / pipeline 1,337; only 1,388 arn-shaped), **all 1,337 pipeline symbols are inside it by exact string equality**, they are 1,337 of the 1,941 cohort, and the shard's ':'-segment-2 firm parse agrees with the cohort parse 1,337/1,337. "CLOUD_NODE" is the Kuzu table the set was read from, not an id space. No chain needed; the arm is view P = same-firm over the 1,337, MEASURED there / ABSENT on 18,145 / metric domain 893,116 pairs, typed CONTROL_ONLY because its label IS the 6.3 label (circular for 6.3). Design lane ruled reading (a') on it (81287 sec 10b); issuer withdrew the premise (81275); COX withdrew its inferred disjointness (81309). Probe committed as the cell input @fb0a013b04 (members + labels listed, inputs at digests); base rate corroborated by arithmetic on the partition sizes (438,018 / 893,116 = 49.04%, matching CCX's pair count).
2. **The 604 split -- my defect, referred and closed.** My 81265 wrote the cohort's 604 non-pipeline entities as "368 ARNs + 235 other" = 603. The issuer referred it as an open_discrepancy rather than guessing (81521). Re-measured: 368 arn + 235 other + 1 colon-shaped non-pipeline id = 604; the one is `event-source::CUSTOM::bd-pipeline.gold-chain` (EVENT_SOURCE, aws, bd) -- present in my raw census as "colon-id 1,338" and dropped when I summarised. Amendment @0a182e00a0; both certifiers bound it to the wave-3 successor; the mechanism recorded as HISTORICAL in the cell.
3. **The permuted-arm control was substrate-carded** (`~X`, @4e7016f471): sound as the diagnostic (firm-blindness as mechanism), UNSOUND as a gate on three grounds -- one draw with no scale, one RNG stream shared with the battery, an untracked local input. Accepted as written. Owner disposition for the rebuild at the post-wave-3 cut stated and recorded @77cfaac66e: primary input = the served artifact at its immutable S3 URI + sha (local copy is a cache), one independently seeded RNG per arm with seeds on the oracle, (K,T) declared, failure signal = outside the typed battery's band.
4. **Wave 3 state at close:** sealed 16 times today (18 seal files / 18 run dirs), 0 certified; each blind nomination found a real record defect (ddof plant, stale ruling carriers, run_id identity, a stale attempt token). No faces cut. The carding remainder (18 cells / 35 subjects) cut @735029ea47 and rebuilt, awaiting its own blind lock. Wave 2 closed at all three faces; sec 6.3 EVALUATED FALSE on both frames with the cause measured by my (a) controls and carried on COX's successor as CITED, not re-derived.
5. **/exec-sum SESSION** rendered for Andrew at 20:10Z (D11 segment, card form, grounded on telemetry 378,306 rows / 142 files, comp-state self-test 4/4, both project JSONs, to-check 0 + 0 open, the run dirs). Realistic read: ~2 working days to a K-sweep answer and a carded remainder; program completion >= 4 weeks out and hinging on an unscheduled L4 cut (Addendum 1f: persistence reads at N >= 20 nights).
6. **Fourteen window frames (39-54) acked; hold honoured on every OPEN; commits verified at each CLOSE** that carried mine (37: probe; 38: amendment) by is-ancestor + ls-tree/content + positive control. MSTR's ack-block census (83806): my 83744 row carries only my own ack; a foreign attempt bounced on the race, not on a guard -- broker mechanism routed to its owner, not this seat.

## Own errors, on the record
- The 604 split (item 2): a raw census with the right number, summarised without adding it up. Same class the issuer named against itself the same hour.

## MCP traffic
~45 in / 6 out. Significant out: 81265 (population measurement), 81282 (reconcile with COX), 81315 (probe committed), 81339 (base-rate corroboration), 81532 (604 closure), 82680 (owner disposition). Zero QUEUED/REFUSED. Every frame READ-acked; one ack reported broker failure and was found already carried on retry.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| python (json, sets) | population x pipeline-symbol x cohort intersections at the pinned inputs | measured | 1,337/1,337; 1,337/1,941; agreement 1,337/1,337 |
| python (json) | cohort-rest by id shape + node_type | measured | 368 + 235 + 1 = 604; the one named |
| git show / is-ancestor / ls-tree | pins at windows 37, 38 | on origin, controls firing | probe + amendment |
| .tools/safe-commit.sh (x2) | fb0a013b04, 0a182e00a0 | msg-verify MATCH | behind a mechanical window gate each time |
| comp-state --self-test / comp-state | for /exec-sum | PASS 4/4; D11 rows lexical | no real drift |
| .tools/directives-check.py --json, .tools/to-check.py --all --project | for /exec-sum | measured | 0 + 0 open TOs |

What worked: reading the population instead of the labels -- one intersection overturned a premise three seats had reasoned from. What failed: my own summary of a census I had already run correctly. Gap found: none new; the "carrier_table vs entity_domain" naming trap is now two typed fields on wave-3 artifacts.

## Blockers
None at this seat. Wave 3's certification and the carding lock are the certifiers' and the issuer's; the permuted-arm rebuild is a cut-time act at the post-wave-3 cut.

## Current State (handoff-grade)
- Deliverables, all ON origin @b9854c9122 (window 54 CLOSE): Andrew-direct record 52f435a021; census 9b2c687dc8; (a) c11d1ff734 + carrier repair 2dc3076501; to-check third population fb30afe388; session log b45042c8f6; K-sweep probe fb0a013b04 + amendment 0a182e00a0. Folder: `org/tier1_exec/1.0.0_SA_CTO~Y/deliverables/{D11_SUBSTRATECARDING_COVERAGE_CENSUS_20260829.md, D11_L3W2_INDEPENDENT_REDERIVATION/*}`.
- Owned forward: methodology / persistence / location / key rows of the permuted-arm rebuild at the post-wave-3 cut (disposition @77cfaac66e). Nothing else owed.
- Watcher bnxfue2y1 live; inbox drained; zero crons; tree clean at this seat's paths.

## Next Steps
1. **[2.0.0_SA_COO~X]** wave-3 seal discharge + joint certification -> seat COX/CCY/CCX -> K sweep runs; the carding remainder's blind lock -> seat the 35 subjects.
2. **[1.0.0_SA_CTO~Y]** the permuted-arm instrument rebuild when the post-wave-3 cut names it; otherwise event-driven on the segment.
3. **[1.0.0_SA_CTO~X]** registry v1.1; the L1-table amendment carrying carrier_table vs entity_domain.

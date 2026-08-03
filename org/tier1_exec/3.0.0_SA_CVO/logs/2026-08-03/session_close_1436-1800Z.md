# Session close 1436-1800Z -- MDLP_MONPUB validation/witness arc end-to-end + Andrew-direct rollback/CloudFront audit

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE

**Serial:** `3.0.0_SA_CVO`. Fresh session, launched on MSTR-TO (validate ~F's ST Model Portfolio
manifest-regression spec BEFORE CTO orders the fix). Window = whole session; 8 commits, all mine.

## What happened (chronological, each with its own committed log in this folder)

1. **Spec validation RAVC** @f4ab1ae778 -- CONDITIONAL GO on CTO's MDLP_MONPUB spec @d59fc15920.
   Independent grounding surfaced 3 findings absent from BOTH ~F's log and the spec: (F1,
   required) FAILED executions publish before crashing -- the 12:09-12:58Z versions carry
   data_as_of=2026-07-31 from the defective pkl, so W2 gained the build-before-publish reorder;
   (F2) the regression was ESTATE-WIDE (~40 keys), guard covers 3 -- recorded residual R1;
   (F3) backward writes recurrent + a raw-S3-copy mechanism bypasses any Lambda guard -- R2.
   CTO folded all four conditions @2733bfceff; sign-off UNCONDITIONAL after re-read.
2. **W1 premise refuted post-sign-off** @d077c9a4db -- MSTR~Z content-verified the "known-good"
   07-30 object: ST row garbage (1Y -13.64 vs bmk +4.74, vol ~23-26). I re-confirmed from my own
   fetched copies both directions. MY MISS on the record: my version walk verified
   existence+vintage, never VALUES. Banked to memory:
   `feedback_known_good_is_a_content_claim_read_values_before_republish.md`. W1 blocked; W4
   (corrected 07-31) became the heal path.
3. **Andrew-direct audit** (rollback UX + CloudFront) @30a13b89b1 -- root-caused the 07-31
   rollback-picker failure (history sorted on exec-{random uuid} DESC = hex-alphabet order, not
   time; the 07-27 target exec-5a4149176fb6 structurally invisible) and mapped all cache layers
   (edge invalidation fixed 08-01; browser 5-min; React Query staleTime/gcTime Infinity + 12h
   localStorage persistence with ZERO invalidateQueries in the DataRefresh UI = the real 07-31
   culprit). Produced FOUR ordered work items: W5 (time sort), W6 (client-cache invalidation),
   W8 context, W9 (DefaultTTL-86400 amplifier; injector load-bearing for the TTL).
4. **W4 recovery witness PASS** @b16913d35e -- estate healed at 07-31; served ST row read
   value-by-value vs sitez's authoritative pin, 10/10 periods to 2dp; no serve mutation in the
   blocked window (version-gap).
5. **W2 failing-direction battery witnessed COMPLETE** @ff496d7621 + @9ba99fcb5c -- method
   ruling (direct-invoke live legs only -- trigger-path mutants DENIED as estate-wide via R1;
   scratch-first; leg-3/force_publish scratch-only, reversing my own earlier live-with-restore
   idea), CTO-ratified; legs A/B grounded on CloudWatch at deployed vintage with zero-write
   proven by S3 version-gap; ETag-pin discrepancy resolved as a benign real-user rebuild
   (yang@opalinvest.com, 16:21:45Z -- itself a production passing-direction exercise); leg C
   both halves on seeded scratch.
6. **W8 ruling + witness COMPLETE** @624a24c4a3 -- grounded the middle segment at every hop
   incl. the LIVE state machine definition; surfaced the load-bearing architectural fact (SFN
   Parameters block is a TOP-LEVEL WHITELIST -- force_publish survives ONLY inside the manifest
   body; a top-level flag passes direct-invoke and silently breaks orchestrated), now in the
   spec; witnessed all 3 legs (stamped manifest landed LAST with both fields in-body; manifest-
   arm (:146) bypass with rollback id in the log, no top-level flag in the event; negative
   control refused at post-W8 line numbers); fixture cleanup independently verified (get-item
   empty x2).
7. **W5 exercised on the LIVE Lambda** (same log) -- direct invoke: 25 items strictly
   time-ordered, exec-5a4149176fb6 PRESENT. Differential acceptance satisfied on the deployed
   artifact against the production table, answering Andrew's direct "is it fixed" with an
   exercise, not a deploy citation.
8. **Instrument register** @aeca48e395 -- two CF comp-tool coverage gaps (COO-routed), Gap 1
   independently hit by me same-day.

## MCP traffic

~35 messages handled across MSTR / CTO / COO / DS / DT. Significant: MSTR-TO discharged; CTO
RAVC opened+closed (CONDITIONAL GO -> fold -> UNCONDITIONAL); 2 method rulings issued (W2
battery, W8 exercise design) both CTO-ratified; 5 witness verdicts delivered; Andrew-direct
relay to CTO (cache-invalidation findings, verbatim + scope) -> W9 ordered; COO priority-chase
resolved (crossed my ruling in flight); 1 malformed send (nonexistent serial, broker-rejected,
nothing delivered -- on the record).

## Compiler Tools

| Tool | Context | Result |
|---|---|---|
| comp-routes behaviors | CF behavior/origin/edge-lambda map for the audit | PASS (DESIRED-plane; TTL gap -> register entry) |
| comp-cache key | portal query-key trace for benchmarks artifact | PARTIAL (0/103 hits -- artifact fetched via wrapper fn; raw two-stage drill followed) |
| comp-grep | outputs-manifest writer census; create_invalidation 7-creator census | PASS (denominators printed) |
| comp-which HUD | advisories honored throughout; ~8 raw calls carried `# rail-checked:` markers (object-version walks, CloudWatch forensics, live ASL -- no comp-tool models these) | PASS |

What worked: comp-routes as the map + live primitives for values (the interim pattern, now in
the register entry). Gap found: comp-routes carries no cache-policy identity/TTLs; comp-blast
has no CF path-pattern nodes (both registered @aeca48e395, register-only).

## Blockers

None at me.

## Current State (zero-context handoff)

- **Serve:** `s3://opal-data-portal-v2/json/benchmarks/*` healthy at data_as_of=2026-07-31
  (true T-1), last rebuilt 16:23:49Z by a real user pull through the live W2 guard.
- **MDLP_MONPUB:** W1 superseded (premise refuted); W2 WITNESSED-COMPLETE; W4 witnessed closed;
  W5 deployed+exercised; W8 witnessed closed (fixtures cleaned, verified); W9 closed
  (live-primitive grounding, per COO); W3 written in-repo, deploy pending; W6 PROD promote
  in-flight at 0.2.0_DT_PortfolioAnalytics; W9b at ~F.
- **Andrew closeout gates (spec 5c):** gate 2 (W8) CLEARED; gate 1 (W6 promote) + gate 3
  (auth-header capture, behind the promote) remain, then tier2 /logs -> Andrew closeout -> RCG.
- **Traversal residual:** stamped-rollback full trigger-path traversal is SOURCE-GROUNDED-NOT-
  EXERCISED (live ASL verified); upgrades at the first genuine rollback (designated shared
  live-exercise event for W6+W8).
- **Scratch:** `opal-313476888478-yang-qa-scratch` rides 7-day self-expiry; DDB fixture records
  deleted (verified).
- **Memory banked:** known-good-is-a-content-claim (MEMORY.md updated, 12,984B, under cap).

## Next Steps

1. **[0.2.0_DT_PortfolioAnalytics]** Land the W6 PROD promote; deliver W3 deploy.
2. **[3.0.0_SA_CVO]** Witness W6 promote + W3 deploy when they arrive (client-cache
   invalidation both-directions exercise per the TO; blanket clear() is the named forbidden
   easy-pass). Witness the traversal upgrade at the first genuine rollback.
3. **[Andrew]** Closeout per spec 5c once gates 1+3 land.

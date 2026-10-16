# IRPT_DASHBD: CVO adjudication, round 147 (workstreams B-49F and CONTRACT, ~D2): publisher 0.2.0, the Cottonwood publish handler and root, source contract 0.4.3

<sweep_watermark>2026-10-16T04:39Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T04:39Z, on msg 9044 (shared packet @52f18dfe5c, blob d9fc5582ee). Four orders: DB-b-279, 280, 281 (workstream B-49F, drain 220c9c63f3) and DB-b-282 (workstream CONTRACT, drain d12e8f62d2), all in HEAD. No judgment criterion. Re-run on the landed tree (HEAD 2013283a5d): DB147-1-AC1..AC3, DB147-2-AC1..AC3, DB147-3-AC1, AC2, DB150-1-AC1..AC3 PASS (11 of 12). DB147-3-AC3 FAILS on trunk; this seat confirmed why: the merge 220c9c63f3 adds exactly one source-map entry (irpt-cot-reporting-publish-lambda) and changes no other entry against its first parent, and no commit has touched the source map since. The checker compares against the order's older base, where another seat has since changed irpt-ycharts-generate. round-close --round 147: B-49F MAY-CLOSE, CONTRACT MAY-CLOSE. DB-b-283 (the WORLD apply) HAS NOT RUN: Lambda irpt-cot-reporting-publish-lambda returns ResourceNotFoundException (read-only, 04:3xZ). Struck DB118-3-AC3 still FAILS. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S64",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T04:39:00Z",
  "one_line": "Round 147 (~D2): the 49F series is byte-identical to its base under publisher 0.2.0; the Cottonwood publish handler is dry-run by default and writes only on upload exactly True, at builder addresses; the Terraform root has no schedule and the naming gate grades it CONFORMANT; SOURCE contract 0.4.3 lets income_received be null for the Black Diamond-computed source, both schema hashes unchanged, with its rule-24 record key. ONE-DRAIN RULE: 0.4.3 changes no writer; it relaxes the contract to match what the Cottonwood gold already writes (S104: null on 52,468 of 52,468 floor-era rows), so no red window opened. WHAT THE ISSUER'S SECTION 2 MISSED: (1) A VALUE MUST CARRY ITS CLAIM: for the BD-computed source, 0.4.3 allows null with NO claim pairing, unlike Orion's (null only with flow_claim absent), so a reader cannot tell 'income not computed' from 'no income'. And because every Cottonwood row is null, Cottonwood's reports will carry no income at all. S104 records the fact but reads INERT, with no remediation, owner plan or disclosure line. (2) The Lambda's calendar source is called unmeasured: the bundle ships lib/trading_calendar.py, which imports pandas_market_calendars and, absent that, answers from a hardcoded NYSE table covering 2010-2027 only (W226-S1). The layer's contents decide which one runs, and nothing records it. Dismissed (4): D2-W226-S1 (calendar fallback: carried here as a gap to measure at the apply), D2-W226-S2 (base defect, cured by merging 225 into 226), D2-W226-S3 (checker grant clause, fixed), D2-W226-S4 (the naming gate reads committed files only). D2-S104 held.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W226-S1",
   "IRPT_DASHBD-D2-W226-S2",
   "IRPT_DASHBD-D2-W226-S3",
   "IRPT_DASHBD-D2-W226-S4"
  ],
  "spec_asserts": "Spine L9/L10; CTO msg 8735 one-drain rule; A VALUE MUST CARRY ITS CLAIM (CLAUDE.md section 4): a null must be distinguishable from a measured value by a field a consumer can reject on.",
  "world_is": "Code and contract only; nothing planned, applied, invoked or served; the Cottonwood series does not exist in S3. Cottonwood income is null everywhere and the source contract now allows that for the BD-computed source without a claim field.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T04:3xZ at HEAD 2013283a5d: 11 of 12 PASS; DB147-3-AC3 FAIL ('another entry changed: irpt-ycharts-generate')",
    "lambda-source-map.json: 220c9c63f3 vs its first parent adds exactly irpt-cot-reporting-publish-lambda and changes no other entry; no commit touches the file after 220c9c63f3",
    "org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json 0.4.3: income_received nullable_when {source orion, flow_claim absent}; also_nullable_when [{source 'computed from Black Diamond values and flows'}] with no claim field",
    "aws lambda get-function-configuration irpt-cot-reporting-publish-lambda: ResourceNotFoundException (DB-b-283 not run)",
    "lib/trading_calendar.py line 41 imports pandas_market_calendars; the fallback warning names a hardcoded 2010-2027 table",
    "round-close-check --round 147: B-49F MAY-CLOSE (3 orders), CONTRACT MAY-CLOSE (1 order)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Four INERT worker rows (a tooling fact carried forward, a base defect cured, a checker fixed, a gate property). D2-S104 is held, not dismissed: Cottonwood's missing income needs an owner and a disclosure, which the slug asks the CTO for."
 }
]
```

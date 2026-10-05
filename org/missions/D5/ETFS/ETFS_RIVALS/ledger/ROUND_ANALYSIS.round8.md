# ETFS_RIVALS -- ROUND 8 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-05 ~16:5xZ

**Input:** CVO~RV slug msg 29705, `surprise-channel/remediations/REMEDIATION_v8.Z.md` @5867175a58. The review is
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R8_REVIEW_20261005.md` (66 lines, read to EOF). Earlier grades: @0fe137ee28
(C-S27 sa-1 PASS; C-S28 ui-5 NOT MET).

## 1. WHAT THE ROUND DELIVERED

Round 8 is applied 5 of 5 at `b166e04416` (CTO half @74e2071bec plus ADDENDUM 1 @3484081815). The entry `etfs-rivalfunds-round8` was
CLOSED 6 of 6 @776a95c2da. The served page is batch `rv-publish-1005r8b` (verified here). The round covered:
- workstreams A-D (an-1, rw-1, rn-1, fc-1, lg-1, gc-1, hc-1, bt-1, rp-1);
- su-1, whose publish hookup was removed by the forward fix;
- G0 `map-2`, under which SCHY is a rival, not a benchmark.

**Round 8 is CLOSED.**

## 2. GRADES (CVO~RV L9: rendered text, real clicks, 13 fund views)

| order | J1 |
|---|---|
| RIV-an-1: one name per security in the AI accounts | **PASS** (441 keys, 0 under two names), with one P3 residue |
| RIV-rw-1: trend caption, audit trail and AI leads | **PASS** on U07 and U12; U18 not exercised |
| RIV-rn-1: opens on the last 30 trading days | **PASS**, with one P3 residue |
| RIV-fc-1: any security name opens its modal | **NOT MET on the AI text** (C-S35): 395 plain mentions of 43 modal-bearing names, against 253 linked. 1,837,070 B of the 2,097,152 B gateway cap |
| ui-5 (10-05 organic) | **NOT MET** (C-S36): 22 of 22 ticker-form names unchanged; no round-8 cell carried them |

**The CVO's process finding is accepted.** Round 8 was cut before the 10-05 grades it was meant to follow, so ui-5's residue had no
cell. From now on, an enrichment item that reads "whatever grade X leaves open" is recut after X, or the analysis states that it is
deferred to round N+1. This analysis carries C-S36 explicitly.

## 3. RULINGS

| # | item | ruling |
|---|---|---|
| 1 | **S24 (ARMED): the daily capacity, with tomorrow's reset unmeasured** | **No backfill pull until a measured capacity budget exists.** That budget is a round-9 cell: production's daily Bloomberg use per leg, read from the vehicle and enrichment logs, against the measured trip point (about 170k rows on 10-05), with headroom. **For tomorrow's 07:00 ET vehicle:** COO~RV's hourly one-query probe keeps running. If it has not read data by 10:30Z, MSTR~Z runs the runbook's P0 probe at 10:45Z (one query) and posts the result before the vehicle fires. |
| 2 | **S29: Step B's G5 replay** | Ruled (B) at 16:2xZ: a round-9 named-fund G5 rebuild with every other fund byte-equal, then Step B under its own pair. |
| 3 | **C-S35: fc-1's AI text** | A round-9 cell: every modal-bearing name in the AI faces and dialogs opens its modal. **The gateway cap is the constraint:** the page sits at 1.84 of 2.10 MB, so the cell measures the page size after linking. If linking all 395 would cross the cap, the cell links a name once per face and states that rule. |
| 4 | **C-S36: the 22 ticker-form names** | A round-9 cell: each security shows its company name from the served crosswalk or security universe, or a reason when none is served. |
| 5 | **The live G5 history differs from current code on 176 of 189 dates** (found by Step B's dry run) | **Measure first; no replay now.** A round-9 read classifies the differences by cause (the code change behind each). A replay is cut later, under its own pair, only for a cause the classification shows to be a defect in the old values. History is never rewritten in place: a replay writes new revisions. |
| 6 | **8 OPEN remediation rows unmoved for 2+ rounds** (S7, S13, S14, W3-S11, W3-S12, W5-S3, W5-S7, W5-S14) | A round-9 triage. Each row is cut as a cell, closed with a citing row, or names what blocks it. None is carried silently into round 10. |
| 7 | **The P3s** (the ledger header pin, IDVZ's R30 day count of 29 against 30, Nebius under two keys) | COO~RV's own, in its issuance. |

## 4. ENRICHMENT LIST (round 9, ONE issuance by `2.0.0_SA_COO~RV`)

1. **The G5 named-fund rebuild** (ruling 2), then Step B under its pair (Andrew's "Backfill is approved for IDVZ/PFOE", @4bd948e824).
2. **The IDVZ/PFOE daily join** through a rivalfunds-owned gate file. No Positioning file is written or read differently (Andrew-direct
   @33ff3bdac0).
3. **security_universe, built incrementally** (the prior universe plus that day's G1), as its own invocation. Its first served key is
   relayed to the laptop CTO.
4. **C-S35:** the AI-text name links, within the gateway cap.
5. **C-S36:** the 22 ticker-form names.
6. **S24:** the measured Bloomberg capacity budget.
7. **The G5 history-drift classification** (a read, no replay).
8. **The triage of the 8 stale OPEN remediation rows.**

## 5. ACTS FOR ANDREW (cited)

None in this round. The backfill is approved (@4bd948e824), and the Positioning boundary is his word (@33ff3bdac0).

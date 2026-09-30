# Never-widen sign-off packet, RE-CUT -- the Performance adapter reads 49F from the holdings gold (PRD v0.20)

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-29 ~07:5xZ.

**Why re-cut:** 4.0.0_SA_CRO REFUSED the first cut on blob 189aaef2
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/NEVER_WIDEN_SIGNOFF_CRO_HALF_ADAPTER_HOLDINGS_GOLD_49F_20260929.md`
@eca8083ad2, row S195). The refusal was about the gold, not the design, code, plans or prefixes. 1.0.0_SA_CTO ruled the
open points as PRD ADDENDUM v0.20 @613bfc6ecf, rulings 13-17 (102611).

**Ledger:** `irpt-adapter-holdings-gold-49f-r2-20260929` (U1 and P1 closed). The first cut's ledger was closed
SUPERSEDED with nothing applied.

**Carried unchanged** from the first packet (`NEVER_WIDEN_SIGNOFF_PACKET_ADAPTER_HOLDINGS_GOLD_49F_20260929.md`,
blob 189aaef2, which the CRO half read as consistent):
- section 1's three surfaces: the role policy and the bucket fence (ae20e904e6), and every artifact member except the
  two named below;
- section 2's table rows B-F and the reader count;
- the rollback per key;
- the CTO's condition 1 as recorded in the old ledger @caa7bdb08f: under rollback, live qfxZ0DzB reopens the
  pre-switch engine pointer (a separate key namespace), and a by-id open of an OPAL_HOLDINGS record refuses as
  UNEXPECTED.

## 1. What changed since the refusal -- each item of the CRO half's section 6

| CRO section 6 | done | evidence |
|---|---|---|
| 1. producer: a cusip-less position never priced by key; re-emit 557 of 557 complete; the census before/after | v0.20 rulings 13-14 in the producer; 49F gold re-emitted 06:43-07:08Z | TO-IB-er-301 amendment 1, DS~E @eee6a7a721. E3-AC4 PASS on the issuer's re-run: 0 OK rows at \|r\| >= 1 (was 2,846), 4 at \|r\| > 0.5 (was 4,061), `leveraged` on all 557 days, manifests 557 of 557 |
| 2. the near-zero base | ruling 15: the basket is the LONG holdings; a margin debit sits outside it, flagged `leveraged` | same re-emit |
| 3. adapter: the fresh path refuses what the reopen path refuses | ruling 16, IB-pr-214 @31d86a99ea: the 49F fresh path raises EngineReturnImplausible on any series point <= -1 | P21-4-AC1 PASS (issuer re-run on CLOUD): an OK day of -1.2 refuses; a NOT_COMPUTABLE day is skipped as PARTIAL |
| 4. the after-read discriminates | the two S195 accounts are added to the reads below | section 3 |

Also in this artifact: IB-pr-211 @78f7ffb758, where `_authorize_release` passes the request, so a render names its
grant. That was window 21's K8 refusal, read at adapter corr-d490a5849a80.

## 2. The artifact -- `qfxZ0DzB..` (live) -> `hD7G6YT1..` (S3 version 3donK_gT)

- Census vs live: 69 -> 70; `holdings_gold.py` added; `PerformanceReport.schema.json`, `entry.py`, `installed.py`,
  `retained.py` differ; nothing else moves.
- Vs the refused `qosuSxAf`: `entry.py` and `retained.py` only.
- Flat census pin skew 0. ~Y's zip_module_census flags nothing new (its FAIL set is a strict subset of live's).
- Cold start with /var/task mapped: import OK, the same named envelope as live.
- Plans re-run fresh: performance 0/2/0, shared-infra 0/1/0, identical to the first cut's.

## 3. What the act would serve -- the CRO's own census, re-run on the re-emitted gold

The chain `prod(1 + r)` over each account's OK rows, windows ending 2026-09-25 (the adapter's rule,
`holdings_gold.py`), before -> after:

| window | accounts | chain >= +100% | chain <= -100% | chain in (-100%, -50%] | non-finite | max / min after |
|---|---|---|---|---|---|---|
| YTD | 7,127 | 22 -> **2** | 2 -> **0** | 10 -> 2 | 0 | +197.9% / -61.2% |
| 1Y | 7,300 | 36 -> **4** | 2 -> **0** | 7 -> 4 | 0 | +197.9% / -91.5% |
| SI | 7,814 | 42 -> **7** | 5 -> **0** | 11 -> 5 | 1 -> **0** | +230.5% / -91.4% |

Named rather than refused: 2 YTD accounts (7 since inception) chain at or above +100%, with a maximum of +197.9%
YTD. No day in any of them is at or beyond +/-100%, because ruling 16 makes such a day NOT COMPUTABLE. Whether a
concentrated account tripling is real is a reading the after-read can take on one of them.

**The CRO's named accounts, after:**
- ..0273 (cusip-less, r = 439.43 on 2025-09-09): YTD 0.00%, since inception 0.00%, 281 days named NOT COMPUTABLE, so
  PARTIAL.
- ..0695 (near-zero base, 2026-03-18): YTD +4.38%, 2 non-OK days.
- ..4581 (near-zero base, 2024-08-01; three raw keys end in 4581): YTD 0.00% / 0.00% / +4.90%.

## 4. Apply protocol (the first packet's section 3, amended)

1. Both halves at HEAD naming this file's blob.
2. CRO BEFORE-read on qfxZ0DzB. The first half's before-read stands (CRO 102607); it adds ..0273 and ..0695 YTD and
   one of the 2 YTD accounts at or above +100%.
3. Fresh plans equal P1's; safe-apply performance, then shared-infra (halt gate; HALT_ACK=1 only on 0 STOP items).
4. Read back: CodeSha256 == hD7G6YT1; the role and bucket policies as planned; a real cold-start invoke; one real 49F
   since-inception answer with its wall time printed. **At or over 48 s -> rollback** (CTO condition 2).
5. CRO AFTER-read: the same accounts. NEW-01 and the control read OPAL_HOLDINGS figures; ..0273 reads PARTIAL; no
   figure at or below -100% on either reader; COT and INF unchanged. Any unnamed difference -> same-turn rollback.

**Rollback per key:** Lambda -> S3 version 5bmwADQs (qfxZ0DzB) as the artifact, re-apply; role policy and bucket fence
-> revert ae20e904e6's two .tf files, re-apply both roots.

## What the halves sign against

This file's committed blob; the first packet's carried sections (blob 189aaef2); artifact hD7G6YT1 (S3 version
3donK_gT); ae20e904e6; the gold as re-emitted at 07:08Z (E3-AC4 PASS); and the apply protocol in section 4.

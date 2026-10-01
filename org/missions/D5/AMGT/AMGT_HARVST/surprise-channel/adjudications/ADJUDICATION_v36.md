# AMGT_HARVST ROUND 27 -- L8 COMPILE (no judgment criterion; one WORLD act, no served gold moved)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~09:5xZ
**Input:** `2.0.0_SA_COO~H`'s `round27/ROUND27_DRAIN_END_PACKET.md` @`699fb78c93`, msg 27065. The packet was read to EOF (5,486 B).
**L7 re-measured:** q-2..q-6 read `complete`, and q-1 and q-7 read `withdrawn`, on their LAST `<status>` tag. There are 0 judgment
criteria.

---

## 1. RE-READ BY THIS SEAT

- **`q-1`'s act wrote exactly one object.**
  - S3 `opal-data-harvest` `amgt/harvest/` was scanned: 3,058 objects.
  - Objects modified 08:00-09:35Z: **1**, `bronze/run_record/date=2026-09-30/20260930T084110Z-run-4ee47491.json`, at 08:42:31Z.
  - The pair held.
- **No served gold moved.** The latest `chatter_daily` part is still `part-20260930T072527Z` (07:25:36Z), and the latest
  `article_security_mention` part is still `part-20260930T062354Z` (06:24:24Z).
- **The FWD-7 census (q-3), re-derived** over the served `chatter_daily` for the window 09-01..09-30, 191 securities x 30 days:
  - **ELIGIBLE 0**, which agrees with the packet.
  - This seat's first pass counted any covered publisher and read 188 NOT_SEARCHED / 3 PARTIAL. The two extra PARTIAL are
    ASML_NA and ASML_US, covered by **sa** only (26 days PARTIAL, 4 DENIED).
  - sa is outside the declared set `{bbg, wsj}`. Against the declared set they are NOT_SEARCHED, so the packet's 190 / 1 is right.
    The first pass used the wrong domain.
- **One contract-fidelity point for the CTO.**
  - `C-HV-RANK-DECLARED-SET` drops from the declared set only "a publisher that refused for the whole universe in the window".
  - sa did not refuse for the whole universe: it covered ASML on 26 days.
  - Either the declared set should be `{bbg, sa, wsj}`, or the contract's exit rule needs a second clause. The eligibility result
    is 0 either way, since adding a publisher only tightens eligibility.

## 2. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W71-S1` (ARMED: after the parse fix, a silver append adds 11 bbg rows beside the 11 empty hash-keyed rows) | **GRADUATED** (disarmed) | It fires only on the round-28 served silver rebuild. That rebuild is a WORLD act that needs a pair, and the CTO's ruling binds the pair to name the 11 rows' fate. It re-arms if that pair omits them, and this seat reads the round-28 pair for it. |
| `Z-W70-S1` (BLOCKING on q-1 AC1: cached listings record no reach) | **CARRIED**, block released | q-1 is withdrawn, so no order is blocked. The defect is round 28, item 1. |
| `Z-S45` (the cause of bbg's refusal) | **CARRIED**, INERT | It answers the CTO's question: the job re-fetched the known-rejected key with no listing request. Holding a rejected key within a day is round 28, item 1. |
| `Z-S44` (bbg silver empty) | **CARRIED** | fixed in code (q-2, `silver_from_bronze.py:115`); the served rebuild is round 28 |
| INERT worker rows | **CARRIED** | as the packet |

## 3. FOR THE ROUND-27 ANALYSIS

1. FWD-7 is bound by collection reach. At 0 of 191 eligible, the HOLD is honest, and q-7's withdrawal was correct: a flip could
   only freeze the legacy rank.
2. The declared-set exit rule versus sa (section 1).
3. Round-28 items 1-3 as the packet lists them. `publishers_found_codes` then reaches the page, which is also what DSGN n-3's
   992 HK wording needs (DSGN_AMGTV1 ADJUDICATION_v13).
4. The issuer's authoring defects are named, and the remedy is plain tokens in `<expect>`.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 7 of 7 (5 complete, 2 withdrawn). **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W71-S1` GRADUATED; `Z-W70-S1` CARRIED with its block released. **MET**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S46",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T09:50:00Z",
    "one_line": "L8 round 27: q-1 wrote exactly 1 object (run record, of 3,058 scanned) and no served gold moved; FWD-7 census re-derived 0 of 191 eligible (190/1 holds against the declared set; sa covers ASML 26 days yet sits outside it -- a contract exit-rule question); Z-W71-S1 graduates on the pair that must name the 11 rows.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-HVST-q-2..q-6 'complete', q-1 and q-7 'withdrawn' on their LAST <status> tag.",
        "S3 opal-data-harvest amgt/harvest/: 3058 objects scanned; modified 08:00-09:35Z = 1 (bronze/run_record/date=2026-09-30/20260930T084110Z-run-4ee47491.json 08:42:31Z); gold chatter_daily latest part-20260930T072527Z, article_security_mention latest part-20260930T062354Z.",
        "chatter_daily part-20260930T072527Z, window 2026-09-01..30, 191 securities x 30 days: 0 with {bbg,wsj} covered every day; ASML_NA and ASML_US covered ('sa',) 26 days PARTIAL, () 4 days DENIED."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W71-S1"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @699fb78c93 asserts 7/7 terminal, q-1's one put, no served gold moved, and ELIGIBLE 0 of 191 (NOT_SEARCHED 190, PARTIAL 1).",
    "world_is": "True as read. The 190/1 split holds against the declared set {bbg, wsj}, although sa, which covers two names, is outside that set without having refused for the whole universe.",
    "notes": "FOR THE ROUND-27 ANALYSIS: the declared-set exit rule vs sa; the round-28 silver pair must name the 11 hash-keyed rows (Z-W71-S1 re-arms otherwise)."
  }
]
```

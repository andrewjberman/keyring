# AMGT_HARVST ROUND 31 -- L8 COMPILE (no judgment criterion; two WORLD acts, one LOCAL)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~05:0xZ
**Input:** `2.0.0_SA_COO~H`'s `round31/ROUND31_DRAIN_END_PACKET.md` @`17829298e0`, msg 27521. The packet was read to EOF.
**L7 re-measured:** `ad-1`, `ad-2` and `ad-3` read `complete` on their LAST `<status>` tag. There are 0 judgment criteria.

---

## 1. RE-READ BY THIS SEAT

- **`ad-1`, the token store:** `dowjones/wsj/session` and `dowjones/barrons/session` exist in Secrets Manager
  (`describe-secret`, created 2026-09-30T22:24:26Z and 22:25:08Z). The values were not read; the SHA-256 match is the
  packet's AC1 readback. The packet's own caveat stands: nothing reads either secret yet.
- **`ad-2`, sa batch 1:** the two A2 run records on S3 (`opal-data-harvest`, `bronze/run_record/date=2026-10-01/`):
  - `20261001T003038Z-run-9baf63af`: backfill, 8 fetched, 8 stored-join, 1 fetched-not-stored, job status `error`;
  - `20261001T004923Z-run-451099a2`: backfill, 20 fetched, 20 stored-join, **4 rejected**, 1 fetched-not-stored, job status
    `upstream_unavailable` (a listed STOP).
  - The total is 28 fetched and stored, sa only, which matches the packet. The packet does not report the 4 rejected
    articles in run 2. That is the run's own reject path, not a fault, but the round-32 per-name ceiling should know it.
- **`Z-S50`, the date-bound test:** `lib/opal_data_harvest/test_o1_run_record_reach.py -k never_overwritten` re-run by
  this seat on 2026-10-01: **1 passed**. The repair holds on the date that broke it.

## 2. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S50` (date-bound test) | **GRADUATED** | repaired at the close; re-run 1 passed on 10-01 (section 1) |
| `Z-W85-S2` (sa `check()` hard-coded account id) | **GRADUATED** | closed in code by `ad-1` A0 `9e68057327` (reads the stored session's `user_id`, raises when absent) |
| `Z-W87-S1..S3`, `Z-W88-S1..S4`, `Z-S48`, `Z-S49` | **CARRIED**, INERT | as the packet; `Z-W88-S3` (whether `error` joins the STOP list) is the CTO's round-32 call |

All 10 rows of the round read INERT. None is BLOCKING or ARMED.

## 3. FOR THE ROUND-31 ANALYSIS

1. **sa's transport is the bottleneck, not the challenge or the account.** Both A2 jobs ended on late-article transport
   or 5xx, never a challenge. That is the FWD-11 v0.13 question in miniature: the sa path passes no challenge because it
   meets none, so it proves nothing about "beat captchas" (L4-R v0.13 condition 1).
2. **The 4 rejected articles in run 2** belong beside the measured 1.33 listing pages per name before the 105-page
   ceiling is cut.
3. **The Friday round:** the v0.13 ratified-text half was SIGNED at 04:4xZ (`prd-signoff.py status AMGT_HARVST` reads
   ADMITTED). The packet's "owed" line was read before that stamp.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 3 of 3. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** 0 such rows this round. **MET (vacuous)**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S51",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T05:00:00Z",
    "one_line": "L8 round 31: the wsj/barrons session secrets exist; the two A2 sa run records read 8+20=28 fetched and stored (sa only), plus 4 rejected in run 2 that the packet omits; Z-S50's repaired test passes on 10-01; Z-S50 and Z-W85-S2 graduate; all 10 round rows INERT.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-HVST-ad-1, ad-2, ad-3 read 'complete' on their LAST <status> tag.",
        "aws secretsmanager describe-secret dowjones/wsj/session created 2026-09-30T18:24:26-04:00; dowjones/barrons/session created 2026-09-30T18:25:08-04:00 (values not read).",
        "s3://opal-data-harvest/amgt/harvest/bronze/run_record/date=2026-10-01/20261001T003038Z-run-9baf63af.json: fetched 8, stored_join 8, fetched_not_stored 1, job sa status error.",
        "s3://opal-data-harvest/amgt/harvest/bronze/run_record/date=2026-10-01/20261001T004923Z-run-451099a2.json: fetched 20, stored_join 20, rejected 4, fetched_not_stored 1, job sa status upstream_unavailable.",
        "pytest lib/opal_data_harvest/test_o1_run_record_reach.py -k never_overwritten on 2026-10-01: 1 passed."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-S50",
      "AMGT_HARVST-Z-W85-S2"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @17829298e0 asserts 3/3 complete, the token store in Secrets, 28 sa articles fetched with every job ending on transport/5xx, and Z-S50 repaired.",
    "world_is": "True as read on Secrets Manager, the S3 run records and a re-run of the repaired test; run 2 also rejected 4 articles, which the packet does not state.",
    "notes": "FOR THE ROUND-31 ANALYSIS: the sa path meets no challenge, so it says nothing about FWD-11's 'beat captchas'; carry the 4 rejected articles into the 105-page ceiling cut."
  }
]
```

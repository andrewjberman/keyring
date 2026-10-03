# AMGT_HARVST ROUND 39 -- L8 COMPILE + L9 -- a LOCAL round, suites green on this seat's own run; the last three ARMED items disarmed; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-03 ~01:1xZ
**Input:** `2.0.0_SA_COO~H`'s `round39/ROUND39_DRAIN_END_PACKET.md` @`c51ed497c2` (3,176 B, read to EOF), msg 28850. **2 of 2 orders
are terminal** (al-1, al-2). Nothing was served. No cell processed publisher text. FWD-16, FWD-17 and the event rebuild stay HELD on
Andrew's publisher-terms card.

## 1. What this seat re-read

- **The commits.** `8d242a4bb7` (al-1), `a12f8edbd8` (al-2), `e3b1a9bb49`, `b52ce0f591`, `5b33a747e3` (the worker.py amendment
  carrier), `949b24cadb` (Z-S68's repair) and `9edfeae04d` (the CTO's proof-of-spec-check fix for Z-S11) are all ancestors of HEAD.
- **The suites, run by this seat** (`round39/checks/suites_green.py`, 01:03-01:05Z, rc 0): `lib/research/harvest` 344 passed;
  `lib/opal_data_harvest` 612 passed, 3 skipped, **0 failed in either**. This matches the issuer's run.
- **al-1 in code.** `publishers.py:1095` defines `LISTING_EMPTY_200`. `:1178` sets it when a listing answers 200 with no URLs, and
  `:1011` reads it on page 1, so a zero-hit 200 is no longer a silent "no articles".

## 2. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W91-S20` (ARMED: `listing_empty_200` did not reach the job row) | DISMISSED_WITH_REASON | disarmed by Z-W91-S22. AMENDMENT 1 @`2ecab274f4` granted `worker.py`, and the carrier @`5b33a747e3` is on HEAD |
| `Z-W91-S22`, `Z-S81` | DISMISSED_WITH_REASON | disarm and resolution records: Z-W91-S20 above; Z-S68's stale tests repaired @`949b24cadb` |
| `Z-W91-S21` | DISMISSED_WITH_REASON | a sparse-cone artefact (the cone lacks `integrations/bloomberg`). The full tree reads 0 failed (section 1) |
| `Z-W90-S23` | **GRADUATED** (Z-C-S69) | its first half is the same sparse-cone artefact. Its residual is real: an ft or no-text article has no content key, so `score_missing` re-appends its null-label marker row in `article_sentiment` on every score run. That is 0 calls, but the append-only store grows by one row per such article per run. This is an enrichment item, live only once FWD-16 is un-held |

## 3. The last three ARMED items (remediation rows advanced IN PLACE, clocks only)

| item | file | evidence |
|---|---|---|
| `Z-S11` (proof-of-spec-check compared invocation strings) | REMEDIATION_v1 | the checker's owner fixed it: `9edfeae04d` "invocation alignment compares the RUNNABLE forms -- both sides decoded" (CTO msg 28800), on HEAD |
| `Z-W91-S10` (barrons' zero-hit 200 read as "no articles") | REMEDIATION_v5 | al-1 complete @`e3b1a9bb49`, proof VALID @`b52ce0f591`. The status is in code (section 1), and the planted page fails 2 of 2 on the old worker and passes 2 of 2 on the new. The live barrons proof waits on the terms card; the silent-zero hazard is closed in code |
| `Z-W91-S20` | -- | not graduated; DISMISSED in section 2 |

After this commit `comp-surprise` should read ARMED 0 for HARVST.

## 4. Outcome state (unchanged by this round)

| FWD | state |
|---|---|
| FWD-16 | code complete and keyed to the content hash (v0.17); HELD (card) |
| FWD-17 | code complete; HELD (card) |
| FWD-6 | the event rebuild (438) is HELD (card) |
| FWD-11 ft limb | licence-only; STOP_FT HARD |

Nothing is cuttable for round 40 without Andrew's word on the publisher-terms card or the FT licence (packet section 5). That is the
CTO's to carry to him.

## 5. L10 PRECONDITION

2 of 2 orders are terminal; every BLOCKING or ARMED row is dispositioned; 0 judgment criteria were cut. **MET.**

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S68",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-03T01:10:00Z",
    "one_line": "Round 39 L8 (LOCAL, nothing served): this seat's own suite run reads lib/research/harvest 344 passed and lib/opal_data_harvest 612 passed, 3 skipped, 0 failed; al-1's listing_empty_200 is in code (publishers.py:1095/1178/1011); Z-W91-S20 disarmed by the worker.py amendment carrier 5b33a747e3; Z-S11 disarmed by the CTO's checker fix 9edfeae04d and Z-W91-S10 by al-1 (remediation rows advanced in place) -- HARVST ARMED goes to 0.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round39/checks/suites_green.py (01:03-01:05Z): SUITES RESULT: PASS (0 failure(s)).",
        "git merge-base --is-ancestor 8d242a4bb7 a12f8edbd8 e3b1a9bb49 b52ce0f591 949b24cadb 9edfeae04d 5b33a747e3 HEAD -> all true.",
        "lib/opal_data_harvest/publishers.py:1095 LISTING_EMPTY_200; :1178 set on 200 with no URLs; :1011 read on page 1."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W91-S20",
      "AMGT_HARVST-Z-W91-S22",
      "AMGT_HARVST-Z-S81",
      "AMGT_HARVST-Z-W91-S21"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-W91-S20 is disarmed by the amendment carrier on HEAD (its record Z-W91-S22); Z-S81 records Z-S68's repair (949b24cadb); Z-W91-S21 is a sparse-cone artefact (the full tree reads 0 failed).",
    "spec_asserts": "Round 39's code lands green and closes its rows.",
    "world_is": "True at HEAD on this seat's own run.",
    "notes": "L10 precondition MET."
  },
  {
    "id": "AMGT_HARVST-Z-C-S69",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-03T01:10:00Z",
    "one_line": "Graduated (enrichment, live only once FWD-16 is un-held): a quarantined (ft) or no-text article carries no content key, so score_missing re-appends its null-label marker row in the append-only article_sentiment store on every score run -- 0 FinBERT calls, but one row per such article per run, unbounded.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W90-S23 (world_is: 'its null-label marker row in article_sentiment is no longer deduped by latest_scores and score_missing re-appends it on every score run')."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W90-S23"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "An append-only store grows by what happened, not by how often a job ran.",
    "world_is": "Key-less marker rows re-append per run.",
    "notes": "The row's own remedy: dedupe key-less marker rows (e.g. by record_hash) in a later cell."
  }
]
```

-- 3.0.0_SA_CVO~Z

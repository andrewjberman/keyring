# AMGT_HARVST ROUND 45 -- L8 COMPILE + L9 -- FWD-2 PASS (every field the publisher sent serves typed; the literal AC3 census is the defect, not the data); FWD-12 PASS on (a)-(d); FWD-9 clip read PASS; 2 ARMED rows DISARMED; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-05 ~00:4xZ
**Input:** `2.0.0_SA_COO~H`'s `round45/ROUND45_DRAIN_END_PACKET.md` @`136d4107b9` (40 lines, read to EOF).
- Three cells: ar-1 (worker `~93`) plus its served silver write, and the issuer acts ar-2 and ar-3.
- The write's pair is COO @`b5d31484b7` / CTO @`16eb97eae5`; its NEVER-2 entry closed @`4e84fd3f2e`.

## FWD-2 -- "every field present in the received article ... appears typed in the queryable table"

**The instrument first (row Z-S85).** The AC3 invocation (`round45/checks/ar-1.AC3.py`) runs
`deliverables/0.9.0_WK_AMGT_HARVST~93/ar-1.field_census.py`, which picks a `bronze_key`'s silver row by `run_stamp` and keeps the
first-read row on a tie. This seat diffed it against the issuer's copy (`round45/ar-1.field_census.reader_rule.py`). The only change
is that selection, now `store.supersedes(...)`. This seat confirmed that rule is the serving reader's own:
`lib/research/harvest/store.py:393` (`silver_latest`) and `lib/research/harvest/publication_gold.py:1088`. So the copy grades what
serves, and the literal census grades superseded rows. **The literal AC3 FAIL is an instrument defect, and the PASS stands on the
copy.** The census file the order names still carries the old rule. Fix it at its source, or the next run repeats the false FAIL.

**This seat's own read of served silver, through `store.silver_latest(<pub>, 'article', ('bronze_key',))`:**
- **barrons, 164 rows.** The fields round 44 found lost now serve:
  - `tickers` 142;
  - `isBICPaywall` / `isFreeArticle` / `paywallIndex` 149;
  - `flattenedSummary` 149;
  - `languageCode` 149;
  - `djmlKeyword` 64.
- **wsj, 444 rows.** `html_lang` 429. `isAccessibleForFree`, `keywords`, `description` and `inLanguage` serve inside the typed
  `json_ld` / `html_meta` / `articleData` columns on 429. That is the same verbatim-container shape earlier rounds accepted for nested
  publisher blocks (Z-W10-S8).
- **The 15 wsj rows without JSON-LD** match the round's 15 first rows. This seat read their 15 originals: **0 of 15 carry any of those
  fields.** Nothing they were sent is lost.

**Grade: FWD-2 PASS. A REALIZED candidate.** "A query by company and date returns it" rests on the issuer's census (all five publishers).
This seat did not re-run the query.

## FWD-12 -- (a) to (d)

- (c) `lib/opal_data_harvest/config.json:26` reads `"sa": 200` at HEAD (it was 25 at round 44).
- (a), (b) and (d) read as before on the aq-4 instrument: 33 = 33 quarantined, 0 article requests, 0 mismatches over 11,210 rows.
- Ruling 3 of the analysis puts depth past page 25 on a new backfill outside (c).

**Grade: FWD-12 PASS. A REALIZED candidate.**

## FWD-9 -- the served clip (ar-3, row Z-S82)

The issuer reads 212 names with 0 leaks, and 1,355 pre-2026 day probes serve no data. This is consistent with this seat's round-44
reading of Z-S82 as a context question rather than a served leak. Row Z-S84 corrects Z-S82.

**Read PASS, accepted on the issuer's evidence.** It was not re-read here.

## Rows

| row | disposition | grounds |
|---|---|---|
| `Z-W93-S1` (BLOCKING, ARMED) | **DISARMED** (REMEDIATION_v6) | @`ccb21d1a4e`; the two golden-pin files 17 passed (this seat's run) |
| `Z-W93-S2` (ARMED) | **DISARMED** (REMEDIATION_v6) | the write's VERIFY holds (wsj 429/429, bbg 1247/1247, ft 170/170); the 15 no-JSON-LD rows lose nothing |
| `Z-S85` | for the analysis | the census tie defect: fix the named census at source |
| `Z-S83`, `Z-S84`, `Z-W93-S3` to `S5` | INERT; left with their owners | record, correction and observation rows |

## L10 PRECONDITION

- The cells are terminal, and the served write's ledger is closed.
- The round's two ARMED rows are DISARMED with rows the instrument reads.
- `comp-surprise --armed AMGT_HARVST` read 2 before REMEDIATION_v6 (exactly those two).

**MET.**

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S77",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-05T00:40:00Z",
    "one_line": "Round 45 L8/L9: FWD-2 PASS -- served barrons now carries tickers 142, paywall flags 149, summary 149, language 149 of 164; wsj's four fields serve in typed json_ld/html_meta on 429 of 444, the other 15 originals carry none (0 of 15); the literal AC3 census FAIL is its run_stamp tie rule (the serving reader uses store.supersedes, store.py:393); FWD-12 PASS (sa cap 200 at HEAD); Z-W93-S1/S2 DISARMED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "store.silver_latest('barrons'|'wsj','article',('bronze_key',)) read by 3.0.0_SA_CVO~Z, 2026-10-05",
        "diff 0.9.0_WK_AMGT_HARVST~93/ar-1.field_census.py vs round45/ar-1.field_census.reader_rule.py: selection rule only",
        "lib/opal_data_harvest/config.json:26 \"sa\": 200"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A compile record: FWD-2 and FWD-12 graded on served silver and HEAD; the two ARMED rows carry DISARMED rows in REMEDIATION_v6.",
    "spec_asserts": "FWD-2: every field the publisher sent serves typed, with nothing lost.",
    "world_is": "Every sampled field serves typed; the 15 rows without JSON-LD come from originals that never carried it.",
    "notes": "Fix the AC3 census at its source (Z-S85) before the next field census runs."
  }
]
```

-- 3.0.0_SA_CVO~Z

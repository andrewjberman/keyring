# NEVER-WIDEN -- CTO HALF -- ETFS_RIVALS round 2, `RIV-d-3` (the live join) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~22:3xZ

**Against:** `deliverables/2.0.0_SA_COO~RV/round2/NEVER_WIDEN_HALF_COO_D3.md` @`66820a65e8` (msg 27396, READ-acked; read to EOF,
7,439 B).

## VERDICT: REFUSE -- ONE ITEM (key 4's served delta is unnamed); everything else is ACCEPTED as measured below

## 1. RE-MEASURED BY THIS SEAT

- **Before-counts** (paged `list_objects_v2` over `opal-data-etfs`, counted client-side):
  - `bloomberg/etfs/bronze/holdings/` 0 and `.../silver/holdings/` 0;
  - gold `peer_group_map`, `holdings_coverage`, `corporate_actions` and `flow_reconciliation` 0 each;
  - `canonical_shape` 325, `trade_schedule` 324, `platinum/page` 6.
  - All equal the COO half. (`rivalfunds/etfs/state/` holds 15 objects in total, from round-1 stages. The half's six named
    subdirectories are new.)
- **The vehicle** (`scheduled_daily_pull.cmd`):
  - the base is 394 lines at `2e38c030f4`;
  - RIV-b-1 added the 122-line leg at `695e59f854` / `1faa6d4f8d` (516 lines), gated OFF by `RIVALFUNDS_BBG_LEG` (`:422`);
  - the exit codes 90-97 are disjoint from every other leg.
  - Key 9's one enabling line is additive. That is Andrew's "Anything we do for this would have to be additive", in COO~RV's
    verbatim record.
- **IDVZ and PFOE:** gate 0 plus silver = 0 match Andrew's "1b" (PRD v0.5, CVO-signed @`2aa3a7d402`) and this seat's ruling (b)
  (msg 27404).

## 2. THE REFUSED ITEM: key 4 moves SERVED output by code the half does not enumerate

- **The predecessor-code diff** (standing CORPUS discipline, y-4 AMENDMENT 1): `git diff --stat 3eaa380467 HEAD --
  data/etfs/scripts/rivalfunds` (3eaa380467 is the round-1 stamp the half names).
  - **The producers of what is ALREADY served are rewritten:** `gold_canonical_shape.py` +285/-, `gold_trade_schedule.py` +522/-
    and `publish_page.py` +46/-. The shape is now multi-source (RIV-g-3), and the schedule is now v2 (income-clean and
    corporate actions).
- **Key 4** writes new revisions of `canonical_shape`, `trade_schedule` and `platinum/page`. **The newest page revision is what
  `/rivalfunds` serves.**
- "Never overwrite" is true, but it is not the question. **The question is what a reader sees change for the funds already on the
  page** (the BASG issuer funds), and the half names no expected delta for them.
- Income-clean (C-INCOME-CLEAN) and corporate actions will, by design, change some existing trade rows: removed as income, split
  or relabelled. That change has to be READ FROM THE PRODUCERS' RULES, not assumed zero.

## 3. REMEDY (the COO half re-signs; this seat then signs)

1. **The serializing dry run:**
   - Run the round-2 G1, G5 and page stages, as built, over the CURRENT inputs for the funds already on the page, through a
     write-capturing client.
   - Diff the captured revisions against the current served ones, per fund. Print the change classes with counts: rows removed as
     income; rows changed by a corporate action; source selection changed; figures changed for other reasons.
   - "Other reasons" must be 0, or each instance must be named.
2. **The positive arm before the cut:** the d-3 ACs pass against the CAPTURED revisions.
3. **The served negative arm after the act:** a fund with no corporate action and no income in the window reads byte-equal on the
   page, except for its new group label.

## 4. ACCEPTED (unchanged by the refusal)

- keys 1-3 and 5-10;
- the act-start gates 0-6;
- the Terminal branch B;
- the unmoved list;
- the rollback table.

## AMENDMENT 1 (~23:3xZ) -- RE-SIGNED: key 4 remedied (answers `2.0.0_SA_COO~RV` msg 27430; COO half @`d6f7c6956d`)

**VERDICT: SIGNED**, with one condition.

**Read here** (`round2/key4_served_delta.json`; the COO half's key-4 section):
- 650 served BASG inputs were replayed through the merged round-2 code into a local sink.
- **G1:** 11,272 = 11,272 rows over 325 dates, and 0 fund-dates differ. The only differing cell is `gold_version` (11,272, a version
  stamp). 3 columns are added and 0 removed.
- **G5:** 837 = 837 trades. Every class is 0, including other. The only differing cells are `inference_version`,
  `corporate_actions_applied` and `dividends_applied` (837 each), which are labels.
- **The page:** layout only.

**The gap it leaves, which the condition closes:**
- The dry run replayed with G3 "none-available", but the act imports G3 (`dividends.json`, 4,780 records) BEFORE G5 (G5 waits for G3).
- "BASG's securities are not in the `DVD_HIST_ALL` pull" is the reason the labels read none-available. That is a claim about the
  imported data, and this dry run did not measure it with that data in place.
- If any BASG security were in the import, C-INCOME-CLEAN would move BASG trades at the act.

**Condition:**
- After G3's import lands and BEFORE G5's first write, re-run `key4_served_delta.py` with the imported G3 as its G3 input.
- It must read the same as above: 0 value changes, every class 0, and only the four label cells.
- Anything else STOPs the act before G5 writes and before the page publishes.
- This is the positive arm on the act's own inputs.

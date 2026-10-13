# For dell1 (MDPF_DEMQUE): the active Cottonwood set and the reverse match (2026-10-13 ~21:0xZ)

**From:** `1.0.0_SA_CTO~DELL2`. **To:** `1.0.0_SA_CTO~DELL1`, for `2.0.0_SA_COO~Q1` (MDPF_DEMQUE). **Under:** pivot direction `XB-20261013T180328Z-d4a5`,
section 5 join "Active Cottonwood set" (dell2 -> dell1).

**The files** (commit `ec617572b8` on box/dell2; reaches CLOUD at the integrator's pass), in
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/`:
- `ACTIVE_COTTONWOOD_SET.csv`: 42,319 rows, sha256 `eb9dd0c3f6def67eab31c1b931e7fe66ad07ef37e2600908733da0a154afebfc`. 769 active
  accounts, 3,357 securities, each with its per-security held window.
- `REVERSE_MATCH.csv`: 769 rows, sha256 `20fb38333542b23beab5a61316cf9acdc0119dbf0be85b55fe150ec191c09a64`. Every current Black Diamond
  Cottonwood account against its Commonwealth predecessor: 457 matched, 12 near, 300 none.

**Definitions:**
- **Active** means a non-cash position in the 2026-10-12 snapshot.
- **Former clients:** 986 accounts, and 1,699 securities held only by them. These are EXCLUDED from every vendor draw, not ranked last
  (Andrew's ADVI memo; cluster ruling).
- **Windows** run from each account's earliest record, never before 2012-01-01 (Andrew's backfill law, @82c7c92449).

**The files carry RAW account numbers.** They are kept in the private git on Andrew's 2026-10-09 word, and the project's account-id test
exempts exactly these two files by sha256 (`92ab57aedf`). Never print an account number in a message or a log.

**Ask of dell1:** `rank.py` windows P1 to these held dates and EXCLUDES P3 (former clients); dell1 owns the filter (direction section 5).

-- 1.0.0_SA_CTO~DELL2

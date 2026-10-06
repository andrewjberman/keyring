# NFRA_OPLGTW -- ROUND 22 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-10-06 ~19:4xZ -- R29: a blank cusip never qualifies

**L10 on `3.0.0_SA_CVO~O`'s round-22 slug** (msg 30248, `surprise-channel/remediations/REMEDIATION_v9.md`
@29abce24c0; graduated by `adjudications/ADJUDICATION_v14.Z.md` C-S38):
- 1 OPEN for this seat: Z-W28-S1.
- 1 OPEN for the issuer: Z-W28-S2.
- Z-W15-S41 is REMEDIATED in place (C-S40).

**The issuer's close:** @007bf22b57. OG-ga-1 FAILED on AC2; AC1 and AC3 PASS. The S41 grant is live at grant_revision
3, which adds `download_filtered` only (Andrew-direct "Yes go ahead", record @ca460bf9fe).

## 1. What round 22 did

- **OG-ga-1** wrote `download_filtered` onto the one live `dim_asset` grant, then ran one real on-host download as the
  holder (`deliverables/0.9.0_WK_NFRA_OPLGTW~28/GA1_DOWNLOAD.json`).
- **Result:**
  - 2173 rows returned: every one of the 2150 held CUSIPs, plus 23 rows whose cusip is blank.
  - 0 non-blank unheld rows.
  - The 22 duplicate rows are those blank rows sharing one key (2151 distinct = 2150 + 1 blank).
- **Mechanism:** read at CLOUD this turn.
  - `app/integrations/schwab/integration.py:341` builds `position_cusips = frozenset(row[0] for row in pos_rows)`
    with no blank or null filter.
  - All three callers of `sem.qualify_asset_plan` take that set: the query path `:656-661`, the stub `:843`, and the
    download path `:939-946`.
  - So the query path has served the same 23 rows to this holder since OG-q-7, and the download now matches it.

## 2. Outcome grades

**0 REALIZED, 1 NOT_REALIZED, 7 HELD, 0 DEFERRED** (round 21: 0 / 0 / 8 / 0).

| FWD | grade | basis |
|---|---|---|
| FWD-3 (each person sees only the information granted to them) | **NOT_REALIZED** (was HELD) | A real grant is served 23 `dim_asset` rows that no held CUSIP qualifies (Z-W28-S1). This is a measured violation, not a pending walkthrough. It re-grades after the R29 release. |
| FWD-4 (Menachem downloads the same approved information he can query) | HELD | Download equals query is now EXERCISED for the real holder: one helper, 2173 = 2173. Two things are still missing: "approved information" needs R29, and Menachem needs G-E. |
| FWD-1, 2, 5, 6, 7, 8 | HELD | Unchanged: OG-v-7, G-E, and R7's host-side flag. |

## 3. Rulings

**R29 -- a blank or null cusip never qualifies a `dim_asset` row.**
- C3 (`prd/NFRA_OPLGTW_PRD.md:163`) restricts the asset reference dataset's CUSIPs "to holdings of the authorized
  accounts", and says "absent qualification denies the asset read".
- A blank is not a CUSIP, and it identifies no holding. Admitting it turns the held filter into a wildcard over every
  blank-cusip asset row.
- The ratified text already decides this, so C3 is NOT amended. The ENDPOINT and CONTRACTS halves do not re-open,
  and AC2 stays as written.
- The 23 rows are a gateway defect under C3. They are not a held-test artifact.
- A held position whose cusip is blank does NOT make its asset reachable through `dim_asset` in v1. Keying asset
  policy on another identifier would be a new contract, and nothing here cuts it.

**R30 -- the fix is a release.** The project un-parks on R28 event 5 (a slug row), and round 23 is ONE issuance:
1. **The fix cell.** In `integration.py:341`, `position_cusips` drops None and every value that is empty after
   `str.strip()`.
   - The cell adds a regression test: a held position with a blank cusip, plus a whitespace-only one, against
     `dim_asset` rows with a blank cusip. The expected result is 0 blank rows on both the query and the download path.
   - The existing qualify tests stay green.
   - At most three mechanical criteria.
2. **The release cell** ships it on the live ref under the usual never-widen halves.
   - It narrows served output, so the halves name the 23 rows that leave, per key and for the one live grant.
   - The rollback is the prior release.
   - The CTO half follows the ask.
3. **The post-release read** is ga1.AC2, run UNAMENDED as the real holder. The bar is `unheld_returned 0`, with 2150
   returned and no duplicates, plus the same read on the query path.
   - Its pass flips FWD-3's measured violation off, so FWD-3 returns to HELD on OG-v-7.
   - FWD-4's approved-information half then stands for this holder.

**R31 -- no grant revert meanwhile.** The 23 rows are asset reference fields only, with no account data. The query
path has served them to this one internal holder since OG-q-7. Reverting would undo Andrew's word on S41 to remove a
pre-existing exposure that the R30 release removes on both paths. The issuer's disarm for the act (Z-S59, 19:11Z)
stands.

**Z-W28-S2 (the issuer's):** carried as an order-form rule, not a cell. The next operator-command order redirects
`prepare()`/`activate` output to the off-repo directory, prints only the operations line, and names how it resolves
the holder's pk.

## 4. Enrichment list for round 23

1. R30 cell 1 (the :341 fix and its test).
2. R30 cell 2 (the release) with the post-release read 3.

Still un-park events after round 23: OG-v-7, G-E, and R7's flag.

## 5. What this analysis does not do

It deploys, applies and grants nothing. It amends no PRD text. It re-measures nothing beyond the slug, the close
commit, and the CLOUD bytes of `integration.py`.

-- 1.0.0_SA_CTO~O

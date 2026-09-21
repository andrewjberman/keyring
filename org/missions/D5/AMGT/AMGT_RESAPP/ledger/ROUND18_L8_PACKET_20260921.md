# AMGT_RESAPP round 18 -- the COO's drain-end packet to `3.0.0_SA_CVO~Z`

**From:** `2.0.0_SA_COO~Z`. **Vintage:** HEAD `7b5d497e59` on SITEZ, LOCAL (LD-0522 puts the push with
`0.0.0_AB_MSTR~Z`). **Written:** 2026-09-21 ~17:5xZ.
- **DRAIN-END, complete:** 2 of 2 terminal, 0 open.
- **Issued** as one slug @`c13e1b93df` (decomposition s.26 + both orders + both COO halves), per Andrew-direct ~15:12Z.
- **Scope:** re-ruled before issuance to the two manager-visible cells, per Andrew-direct ~16:5xZ (@c5532df80a).
- **Pairs:** both completed by the CTO halves @`154cb8e5c4`.
- **Spawn:** both workers from worktrees pinned to that commit.

## 1. Round state, final

**`AMGT-rk-74` (slot ~74), served `crosswalk_source`.**
- **Drained:** `1dc7089050`.
- **Second instrument, this seat's own:**
  - Live `get-function-configuration`: CodeSha256 `P4n1bVaa...Pom0=`, State Active / Successful. The artifact's latest VersionId is `o5x2gdqq...b3a`. Both equal the worker's post-act values.
  - A DIFFERENT SAMPLE from the worker's BA census: I invoked `/api/scoped/amgt/security/<key>/overlay` for CAT, CSL and 6861, plus NVDA as an uncovered control. All 4 returned 200. Each carries `crosswalk_source` = `s3://opal-data-harvest/crosswalk/v1/2026-09-19.json` at index 3, beside vintage `2026-09-19`.

**`AMGT-rk-72` (slot ~72), CSL second seed.**
- **Drained:** `c1fdd952e1`.
- **Second instrument, this seat's own:** `list_object_versions` over `filings/v1/CSL_AU_Equity/`.
  - Exactly ONE key, `UNRESOLVED-SOURCE.source.json`, and 4 versions with 0 delete markers. The new latest is `GzAiBH5L...Z4_9` (17:22:08Z, 4488 bytes, sha256 `c9224976...91f4`, equal to the AC5 receipt), on top of the pre-act `OGe4GT77...HvDJ`.
  - The stored step-4 attempt names both seeds with their source labels. `verified_site` is null.
  - This is inside the pair's UNRESOLVED branch.

The worker's report gave every criterion as PASS-by-output. Proof instances are VALID, rc 0, from each worktree's own checker.

## 2. Outcomes for the grade

1. **R18-C ended UNRESOLVED-SOURCE BY DESIGN**, which is one of the ruling's two sanctioned outcomes.
   - Seed 1, `www.csl.com.au`, reset the connection again (the W40-S1 symptom).
   - Seed 2, `https://www.asx.com.au/markets/company/CSL`, answered 200. But the bounded crawl spent all 40 pages on ASX's own generic pages (`candidates_tried=0`, `queue_remaining=292`) before it reached any CSL document.
   - **A product note for the CTO's analysis, not a defect of the cell:** `_host_allowed` admits the whole exchange host, so an exchange seed spends the crawl budget on the exchange's own site. Whether a scoped announcements path is a sanctioned next seed is a ruling, not something this seat can decide.
   - CSL is still unresolved for the managers.
2. **R18-A is live and visible on every security page's identity block.** Rollback did not fire. The ledger entry was opened before the upload and closed on the served read. The first apply attempt hit the tool's 120-second bound with nothing written: the worker verified CodeSha256 unmoved and no state lock, then re-ran once. It was never half-landed.

## 3. Issuer defect, found and disarmed at the drain -- row `Z-S193`

- rk-72's order specified its discriminating arm as "HEAD's `battery.py` (merge-base with SITEZ if HEAD has moved)". That read predates the rule only until the rule merges.
- On SITEZ after the drain, `lib/research/filings/tests` read **1 failed / 78 passed**.
- This seat pinned `PRE_EXCHANGE_SEED_COMMIT = 154cb8e5c4`, the parent of `a486c3854b`, and filed and disarmed the row in one commit @`7b5d497e59`. Result: **79 passed**, and the arm still discriminates.
- The worker graded correctly on its own branch. The defect is the order text, and the lesson is named in the row.
- AC1 and AC2 were read pre-merge and stand as graded.

## 4. Rows

- **Filed by the workers:** `Z-W72-S1`. AC3's derivation carries no `domicile`, so step 5 prints "jurisdiction UNKNOWN" where the rk-38 record printed AU. It is confined to free text, and the disposition is yours. rk-74 filed none.
- **Filed by this seat this round:**
  - `Z-S192`, the rk-48 out-of-radius writes. RETAIN is ruled by the pair `NEVER_WIDEN_RK48_AS_LANDED_HALVES.md`, complete @`0b71e7f5ab`.
  - `Z-S193`, above.
- **Rows these cells close, whose disarms are owed by their owners** (a pure disarm sets `DISMISSED_WITH_REASON`):
  - `W54-S2`'s second half, by rk-74.
  - `W40-S1`, by rk-72: resolved by design into UNRESOLVED carrying both seeds.

## 5. What this seat asks of L9/L10

- Grade the 2 terminal cells on their branch-HEAD criteria. There is no judgment criterion in either.
- Round 19 carries the rk-48 reason-text fix the CTO ruled. It cannot be cut until PRD v0.15's two halves are re-signed (LIMB 6 refuses any newly-added order). You owe the ratified-text half, and `4.0.0_SA_CRO~Z` owes the brief half.
- Ingestion, migration and backfill stay held on those signatures and on the laptop tenancy act.

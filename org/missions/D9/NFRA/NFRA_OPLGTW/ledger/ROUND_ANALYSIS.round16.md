# NFRA_OPLGTW -- ROUND 16 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-10-05 ~00:0xZ

**L10 on `3.0.0_SA_CVO~O`'s round-16 slug** (msg 29331, `surprise-channel/remediations/REMEDIATION_v4.md` @4a5adbf2d6):
- 7 rows: 4 dismissed and 3 graduated (1 REMEDIATED, 2 OPEN).
- No L9 grade: the round was all-mechanical.
- The gate reads 0 of 87 orders open and 0 of 319 rows undispositioned.

**The issuer's terminal message** is msg 29315: round 16 is terminal at 5 of 5. Release r16 `4b6b823fae` went LIVE at
23:12:32Z.

**Issuer: `2.0.0_SA_COO~O`.** ONE issuance, section 4.

## 1. What round 16 did

- **OG-gr-3: R9 grain and R9a single-page fallback.**
  - The drain `04690bcc28` dropped 14 of the branch's 15 files.
  - The issuer's repair restored them byte-identical to `63203de59f` (drained @ef092da049).
- **OG-rl-5: the r16 release, widened at A3 on R12.**
  - It carries the two `dim_transaction` data prefixes the ratified C3 v1.7 names. Their absence had made live
    `af2d762970` serve 0 Schwab snapshots.
  - It deletes the query path's placeholder `dim_asset` guard.
  - Verify passed 15 of 15 and the ledger is CLOSED. AC1 was re-graded by the issuer after A6 (a stale expect, row
    Z-W15-S38).
  - All three never-widen halves are signed. The CTO's half carried C1, which was met:
    - before the act, 1 live grant, naming all four datasets;
    - after the act, `dim_balance` and `dim_transaction` at 14 servable per master, and reads without a grant
      REFUSED `ENTITLEMENT_DENIED`.
- **OG-o-5:** runbook section 7. OGO2-J1 PASSes on A1 (CVO re-grade @3b572c8c37).
- **OG-ts-1:** the grant-writer tests run against the pinned staged closure, 24 of 24.
- **OG-ar-1:** aged-row triage, 41 of 41.

**Served state on `4b6b823fae`** (`rl5_phaseB_verify_after.out`, synthetic principal, 0 grants written):
- 14 qualified days per master are servable for every contract dataset.
- `dim_position` and `dim_asset` rows pages are OK.
- `dim_asset` returns held CUSIPs only: 49 of a 2,160-CUSIP universe, 0 unheld.
- `dim_asset` `prepare_download` stays REFUSED.

## 2. Outcome grades

| FWD | grade | why |
|---|---|---|
| FWD-1 (Menachem, Schwab, work Claude) | HELD | Unchanged. The walkthrough waits on Andrew's own tests, then Alyssa (OG-v-7). Menachem's grant waits on his tid/oid (G-E). |
| FWD-2 (accurate answers, masters separate) | NOT_REALIZED, *narrowed* | Holdings are now pageable on served `4b6b823fae`: the `dim_position` page is OK, and the census is 56 of 56 with R9 columns and 0 blank. **Balance answers are unproven.** `dim_balance` pages on grain `(account,)` (`query.py:160`), which has never been measured for uniqueness on a served snapshot. FWD-2 moves to HELD when OG-gr-4 measures that grain unique and a balance page is served. |
| FWD-3 (each sees only their grant) | HELD | Unchanged. The served refusal of reads without a grant (C1) supports it, but on a synthetic principal. The denial arms grade on Alyssa's session at the walkthrough. |
| FWD-4 (download equals query) | **NOT_REALIZED** (was HELD) | Served `4b6b823fae` answers a `dim_asset` QUERY but REFUSES the same `dim_asset` DOWNLOAD (`asset_policy_selection_unavailable`). So "downloads the same approved information he can query" fails for one dataset. The remedy is OG-q-6 then OG-rl-6 (section 4). |
| FWD-5 (scope, date, limits) | HELD | Unchanged. |
| FWD-6 (change or revoke) | HELD | Unchanged. |
| FWD-7 (existing users keep working) | HELD | Unchanged. The release kept 65 of 65 tools and 50 of 50 `.env` key names. |
| FWD-8 (support and withdraw the pilot) | **HELD** (was NOT_REALIZED) | OGO2-J1 PASSes on OG-o-5 A1 (@3b572c8c37). The operator walkthrough remains (OG-v-7). |

**Tally: 0 REALIZED, 2 NOT_REALIZED, 6 HELD, 0 DEFERRED** (round 15: 0 / 2 / 6 / 0). The total is the same but the
members changed: FWD-8 left NOT_REALIZED and FWD-4 entered it. FWD-4's entry is a gap that the round's own capability
change exposed. It is not a regression of anything that was served before.

## 3. Rulings

**R13 -- the rows routed to this seat.**

- **Z-W15-S36 (a release order cannot commit its release branch without the override its Bounds forbid): (a).**
  - The release-order form names `GIT_COMMIT_AUTHOR_OVERRIDE` as a sanctioned step for the release-branch commit only.
    The commit is bounded to the order's `<paths>`, and those list the `org/standards` contract twin whenever the
    contract ships.
  - The issuer's post-read proves the release commit's file list is within `<paths>` and cites the audit-log line.
  - **Why not (b).** A gate that reads the order from another tree would widen what owned-paths admits on every
    branch, to save one audited line per release. The override log is already the instrument.
  - The issuer writes the form. The CVO closes the row ACCEPTED_BY_RULING R13.
- **S36 (v1):** CLOSED_UNREMEDIATED, CARRIED_BY `NFRA_OPLGTW-W2-S6`. Its own remedy text says the probe-fixture removal
  is open under W2-S6.
- **Z-W17-S4 (v3):** CLOSED_UNREMEDIATED, ACCEPTED_BY_RULING R10 (round-15 analysis section 3: KEPT, closed as design).
  The CVO writes the clock on that word (ruling @cc05804f8f).
- **Z-W13-S2 (v2):** PLACED with its owners as `ADVI_49F-Z-S1`, in the commit that lands this analysis
  (`org/surprise_channel/ADVI_49F/INVESTIGATION_v1.md`). It is CLOSED_UNREMEDIATED, CARRIED_BY `ADVI_49F-Z-S1`. The 49F
  ADVI chain is not this project's surface.
- **Z-S43 (v2) stays OPEN**, owned by this seat.
  - Moving condition: the delegated identity is invited to the Research Team Meeting series (a person's act, through
    IT, G-TEAMS-TX), and then OG-tx-2's REACH arm re-runs.
  - It grades NFRA_TRNSPT's outcome, not this project's.
- **Z-S50:** REMEDIATED (@f2c150d420). Noted.

## 4. THE ENRICHMENT LIST ROUND 17 CUTS (one issuance, `2.0.0_SA_COO~O`)

1. **OG-q-6 (build, LOCAL): the C3 holdings restriction on the `dim_asset` download paths.**
   - `prepare_download` (`integration.py:816`) and `export_query` (`:893`) apply the same `sem.qualify_asset_plan`
     mechanism the query path runs at `:621-654`: a qualified position snapshot for the same master and date, filtered
     to the grant's accounts. Their two guards are then retired.
   - Acceptance, through the served construction with no seam:
     - a `dim_asset` download holds only held CUSIPs, and a planted unheld CUSIP is absent;
     - a grant whose accounts hold nothing refuses `asset_read_denied_unqualified`;
     - the `dim_asset` query is unchanged.
2. **OG-rl-6 (release): carries OG-q-6 on live `4b6b823fae`, under three halves.** Served output moves: `dim_asset`
   downloads open under C3. Chain: q-6, then rl-6. The release-branch commit follows R13 (a).
3. **OG-gr-4 (read-only): `dim_balance`'s grain `(account,)`.**
   - Measure its uniqueness on the 28 served snapshots (14 days by 2 masters).
   - Serve one `dim_balance` rows page through the served construction: synthetic principal, 0 grants written.
   - If the grain is not unique, paging refuses as designed and this seat rules a grain, as R9 did.
   - This cell can run beside q-6.
4. **Z-W15-S37:** give each acceptance-fixture module its own session manager or app instance, so that the whole
   schwab test set passes in ONE pytest process with 0 setup errors. A "full set" criterion then grades one run.
5. **Z-W16-S5:** re-measure p95 over the first full trading day on `4b6b823fae` (Monday 2026-10-05), against the same
   reference and cap, and grade it.
6. **The issuer's seven remaining OPEN rows:** W6-S2, W1-S9, W2-S6, Z-W13-S5, Z-W12-S7, S63 and Z-W15-S31.
   - Each is listed with its owner and the condition that moves it, or closed with one of the four reasons.
   - Z-W12-S7 is a dated act: the operator re-authorizes before ~2026-10-18.
   - A row that needs this seat's L4 is routed here.

**Stated dependencies, not cells:**
- OG-v-7 waits on Andrew's own tests, then Alyssa. It is also where FWD-1, 3, 5, 6, 7 and 8 are exercised.
- The pilot waits on G-E (Menachem's tid/oid) and on R7's host-side flag.
- Z-S43 waits on the meeting invitation.
- The D9 -> D6 move waits on the joint boundary with NFRA_MCPINDEX.

## 5. What this analysis does not do

It deploys, applies and flips nothing, and it writes no grant. It re-measured only from git and the repository:
- the release census, contract blobs and guard count (the CTO half @75d651b7f4);
- `catalog.py:598-607`, `semantics.py:330-360` and `query.py:155-165`;
- the Phase B after-read and ledger entry, against C1;
- `comp-surprise --project NFRA_OPLGTW`: 69 remediation rows (54 REMEDIATED, 14 OPEN, 1 CLOSED_UNREMEDIATED), 319
  items, 0 undispositioned, 1 ARMED.

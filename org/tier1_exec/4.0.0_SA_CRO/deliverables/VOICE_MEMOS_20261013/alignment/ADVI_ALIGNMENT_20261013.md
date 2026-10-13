# ADVI (Advisor Intelligence) alignment report -- Andrew's voice memo of 2026-10-13 vs the projects as they stand

- Readers: Andrew Berman; the laptop CTO (1.0.0_SA_CTO).
- Source memo: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/ADVI_REVIEW_TRANSCRIPT.md` (auto-transcript, quoted verbatim).
- Measured 2026-10-13 between about 15:30Z and 16:30Z on `box/laptop` @3cf0e276a1. Read-only. No AWS calls.
- Black Diamond = BD. "BV price / BVPRCE" in the memo is project **ADVI_BDPRCE**. "DEM QUE" is **MDPF_DEMQUE**.

**Conclusion.** Firm buckets (ADVI_FIRMBKTS) is staffed in line with its peak rank. However, its written plan stops at mechanics: there is no written per-firm plan for Inflection and Cottonwood, and no project owns retiring legacy operations. The Cottonwood backfill (ADVI_COTBKF) has the most activity of the four projects and the lowest rank in the memo. It sizes its price need over every account in the delivery, which contradicts the memo's active-accounts-only instruction. MDPF_DEMQUE already ranks living clients first, but it puts former clients last rather than excluding them. Billing (ADVI_BILLING) has built a second fee panel on portal DEV next to the existing QTD/YTD/Max Fee Summary on PROD, and its PRD never mentions the existing panel. Black Diamond pricing (ADVI_BDPRCE) is a real defect-fix project, explained in section 2a.

---

## 1. What Andrew asked for (ranked)

The memo makes only rank 1 and the last rank explicit. Ranks 2-4 are inferred from its emphasis.

1. **ADVI_FIRMBKTS: lock in the migration, with a plan that covers every operating function and a decommissioning plan.** "firm buckets, that is obviously if peak importance, we want to make sure that we have locked that in", with "a clear plan for the migration to these buckets, including all current operating functions that run for Advisor Intelligence, as well as a decommissioning plan for legacy buckets and legacy operations".
2. **ADVI_BILLING: do not duplicate the billing figures already on the page; the purpose is billing from custodian data.** "on the advisor intelligence page, we do track quarter-to-date year-to-date and max billing ... We've already built out functions for that. So we don't want to duplicate work here." And: "the purpose of the billing project is that we want to be able to figure out how we handle this from the custodian level data, not so we relying on black diamonds."
3. **ADVI_COTBKF with MDPF_DEMQUE: a clear way to match the backfill accounts to Black Diamond, and an efficient data quota.** "some clear matching mechanism ... that the Commonwealth backfill data ... we're able to match those through to the black diamond repository", and "if we are not able to adequately match these ... then we don't know what is an arc of all accounts."
4. **ADVI_BDPRCE: explain where it stands and what it is for.** "the Black Diamond pricing, I don't really understand where we're at or the purpose of that. That's a new project that needs to be explored."
5. **Last: backfill for closed accounts.** Backfill only ACTIVE accounts' securities over the periods they were held, priced daily per account: "any active account has backfill for its various securities ... for the period that they were held." Closed accounts wait: "we're throwing back the DEM QUE for securities that were held by a client accounts that no longer are even active. This we don't need to waste quota on this stuff. This is a deep, deep, deep, pistorical [historical] priority."

## 2. Coverage table

The fwd column counts endpoint outcomes graded REALIZED; FWD = endpoint outcome. The box CRO recommendations come from the four box status reports and the aggregate in `C:\Users\AndrewBerman\Desktop\today_report\`. The four box report copies there are byte-identical to the repo copies under `org/tier1_exec/4.0.0_SA_CRO/deliverables/` (cmp).

| project | Andrew's intent | chartered outcomes (PRD) | actually delivered / live (evidence) | coverage verdict | recommended move |
|---|---|---|---|---|---|
| **ADVI_FIRMBKTS** (dell1, round 7, fwd 0/8; box CRO: KEEP) | Locked-in migration to the full-name firm buckets; a plan that covers every Advisor Intelligence operating function; a decommissioning plan for legacy buckets AND legacy operations. | PRD v1.4 (`prd/ADVI_FIRMBKTS_PRD.md`), FWD-1..8: readable keys, a one-rule mapping table, a registry lookup, an invisible cutover per firm, triggers repointed (FWD-5), a 45-day quiet-window proof before any delete (FWD-6), and Andrew's decisions on the prohibited key and the B2 credential (FWD-7/8). The method is in DEC-4..DEC-16 (per-firm 7-step cutover, triggers, policies, bronze and silver to `opal-data-assets`, holds re-pointed). | 49 Financial platinum moved to `opal-data-49financial`: 49,231 keys; 8 of 8 IRPT Lambdas and 3 edge functions on the flipped build (dell1 box report lines 111-113). 0/8 REALIZED. FWD-1 and FWD-4 PARTIAL (`ledger/ROUND_ANALYSIS.round6.md` @1c1189d82b). Round 7 is a second blind reader for FWD-1 plus the exec-summary trigger fix (158 client summaries about five months stale). Inflection and Cottonwood not started. Every act on `opal-data-inf` is held on Andrew's FWD-7/FWD-8 rulings (PRD DEC-13, lines 254-263), yet the dell1 block lists `andrew_acts: []` (line 98). | **PARTLY.** The mechanics and the decommission standard are chartered. Missing: a written per-firm plan for Inflection and Cottonwood, and an inventory of operating functions. Retiring legacy operations is explicitly disowned: "its fate is not this project's to rule" (DEC-7, line 229). | **KEEP + REPOINT.** Close round 7 on 49 Financial (agrees with the box CRO). Make the next enrichment list the written Inflection and Cottonwood migration and decommission plan: every Advisor Intelligence operating function, each legacy operation to retire, and Andrew's DEC-12/13/14 calls as cards. Writing the plan does not start the moves, so the box CRO's "not starting -inf or -cot" still holds. |
| **ADVI_BDPRCE** (dell1, round 1 closed, fwd 0/9; box CRO: KEEP) | Understand where it stands and what it is for; explore it. | PRD v1.0, FWD-1..9: one written price rule in one place (FWD-2), every price traceable (FWD-3), median of DISTINCT trades (FWD-4), stable across runs (FWD-5), past dates read that date's trades (FWD-6), no price moves before Andrew sees the before/after diff (FWD-7), consistent gain basis per lot (FWD-8), exact per-lot units and cost (FWD-9). | Registered today, after Andrew's "Yes as written" (~12:1xZ). Round 1: 4 of 4 read-only orders complete, nothing served moved (`deliverables/2.0.0_SA_COO~K1/round1/R1_CLOSE.md`, roundclose @c5c796789b). The CTO ruled THE price rule at ~15:2xZ (@cd65a96bb6). Measured: the written rule reproduces 1,148 of 1,657 served rows; 61 of 586 sampled lots carry a price that matches no canonical row. The dell1 box block (13:01Z) is stale here: it reads "round: none, PRD". | **COVERED** as exploration, which is under way. **NOT COVERED:** Andrew's understanding. See 2a. | **KEEP** (agrees with the box CRO). Send Andrew the 2a paragraph. His only act is the per-fix before/after review (FWD-7). |
| **ADVI_COTBKF** (dell2, round 80, fwd 5/9; box CRO: PARK) | Backfill ONLY active accounts' securities, over each account's holding periods, priced daily. Closed accounts are the last priority. A clear match from the Commonwealth accounts to the Black Diamond accounts. | PRD v0.10 header (`project.json` still says v0.3, last_updated 2026-10-09: registry drift). FWD-1..9 cover the WHOLE delivery: every account's history, daily after-fee returns back to 2013 (FWD-3), the relationship records, documents, sensitive fields, the crosswalk (FWD-8) and history across account changes (FWD-9). The price need in ADDENDUM v0.4 (PRD lines 214-222): 4,634 securities and 3,421,735 security-days over ALL transactions. Each security's window runs from its first to its last trade date across every account, not per account (`deliverables/0.9.0_WK_ADVI_COTBKF~8/PRICE_NEED_20261007.json`). | The crosswalk exists and FWD-8 graded REALIZED: 1,533 Commonwealth accounts, 471 MATCHED, 1,062 NOT_MATCHED with reasons, 21 near matches waiting on a person (`deliverables/0.9.0_WK_ADVI_COTBKF~49/ENDPOINT_READ_20261009.md` line 14). It matches against `s3://opal-data-cot/gold/dimensions/accounts_dimension_latest.parquet` and `.../gold/canonical/holdings/` (`task-orders/ADVI_COTBKF.TO-CB-c-3.crosswalk.md` lines 35-37). That source is the BD-fed Cottonwood serving stack (inferred). 622 commits in 7 days; 0 readers on the served tables; the return history is called defective (dell2 report lines 358-363). Round-80 L8 packet @c47cd08791 (13:35Z). | **CONTRADICTED** on scope: the need covers the whole delivery, not active accounts only. **PARTLY** on matching: a rule-based match to the BD-side account set exists, but only in one direction, and the share of the 1,062 unmatched that are closed accounts was not read. | **REPOINT, then PARK.** (1) Drain round 80. (2) One cell: an "active set" file (crosswalk MATCHED accounts + current BD Cottonwood accounts, each with its holding windows), plus a reverse read showing every current BD Cottonwood account mapped to a Commonwealth predecessor or "none". (3) Restate the FWD-3 price population as active accounts over their held windows. (4) PARK the rest. This partly disagrees with the box CRO: park the round loop, but not the matching cell. |
| **ADVI_BILLING** (dell2, round 3, fwd 1/6; box CRO: PARK) | Do not duplicate the existing QTD/YTD/Max billing on the Advisor Intelligence page. The goal is billing from custodian data, not BD. | PRD v0.1, FWD-1..6: one household's past-quarter fee recomputed from Opal's data and matched to the Schwab debit; who bills today; the advisor-facing fee with its working; a trace to the agreement; the Schwab fee file without BD; the buy-or-build call. C-SHAPE: "Black Diamond's fee data is a reference, not the model" (PRD line 82). | A NEW panel `AdvisorBookFeePanel.tsx` and a new `advi-billing` endpoint and Lambda, on portal origin/DEV only (@6d383958, 2026-10-09). The panel is not on origin/PROD (ls-tree). FWD-3 REALIZED on DEV. 0 seats since 2026-10-09. The EXISTING fee surfaces on PROD: `tabs/FeeSummaryPanel.tsx` and `FeeEfficiencyPanel.tsx`, fed by `fee_summary` with `window_revenue {qtd,ytd,max}` (`types.ts` lines 1879-1887). The producer is `data/black_diamond/scripts/gold/D_02.advisor_client_detail.py` (BD fee-rate history and C_08 fee detail; per-firm twins under `data/cot/` and `data/inf/`). Inflection also has `ClientBillingSummary` (ADVI_INFSHIP). The PRD names none of them: grep for fee_summary / ROLLUP / window_revenue / D_02 / C_08 / fee_rate_history over the PRD = 0 hits. | **PARTLY.** The custodian purpose matches the memo. The duplication risk is real at the UI layer: two fee panels on one page, on different bases (implied revenue from BD fee rates vs fees recomputed from custodian data). | **REPOINT.** Route the custodian-computed fee INTO the existing `fee_summary` contract and Fee Summary panel as its new source (QTD/YTD/Max), replacing BD fee rates. Do not ship a second panel; hold `AdvisorBookFeePanel` out of the PROD promote until that is decided. Otherwise agrees with the box CRO's PARK: no seat until Andrew answers. |
| MDPF_DEMQUE (D8/MDPF, dell1 with site Z draws; fwd 1/9; box CROs: KEEP) | The vehicle for Cottonwood prices: spend quota only on active securities; keep daily pricing per account. | PRD v0.3 FWD-1: "a named security a living Cottonwood client holds ..." reaches the client's page. FWD-3: a backfill never stops a production pull. C-IDENTITY locks a mapping against the client's own trade prices. | `rank.py` (DQ-t-13): "P1 living client > P2 match open > P3 gone (crosswalk)". Former clients are ranked LAST, not excluded. CARD-A (1,319 names) yields a P1 slice of 609 names, re-windowed to 471,522 cells. Today's Andrew-direct adds a 2012 floor, a need-class declaration and a hold on new Bloomberg draws until his form is complete; the CTO holds P1 until coverage counts are read (decomp amendments 8-11, @48445922d6). FWD-1's last hop has no reader page (sitez report line 514). | **PARTLY.** Active-first ordering exists. Former-client exclusion and per-account windows do not. | **KEEP + REPOINT:** make P3 (former clients) EXCLUDED, not merely last, until Andrew lifts it; window P1 per account's held dates. |
| ADVI_FIRMSEP (inactive) | -- | Multi-firm separation and Cottonwood onboarding readiness (registry name). | Inactive in `org/projects/ADVI_FIRMSEP.json`. Its scope is carried by ADVI_FIRMBKTS (FIRMBKTS PRD line 49: "cot dropped from FIRMSEP"). | n/a | **CLOSE** (superseded). Content not read beyond the registry name. |
| ADVI_VALFIN, ADVI_BFIX4 (inactive) | -- | Registry names only. | Inactive, no seat. | n/a | **CLOSE** after an owner read (not read here). |
| ADVI_PERFRP, ADVI_ROSTERCOLS (laptop, D2/ADVI, "active") | -- | Not in `org/projects/ADVI_*.json`; register location not read. | 0 seats. Andrew ordered both closed under his unseated rule (`today_report/ANDREW_DIRECT_20261013_134xZ_LAPTOP_PARE_DOWN_UNSEATED_CLOSES_EXCEPT_SPMOVE.md`). | n/a | **CLOSE** (Andrew's order). This disagrees with the laptop box CRO's PARK, which predates his order. |
| OPAL_ADVIPOINTERS (laptop, active) | -- | One canonical path per firm. | 0 seats, 10 orphan orders (laptop report lines 336-366). | n/a | **CLOSE** (superseded by ADVI_FIRMBKTS + MDPF_CANON), as the box CRO and Andrew's 13:4xZ record say. |

Registry census: 105 `org/projects/ADVI_*.json` files. 75 complete, 18 closed, 4 merged, 1 cancelled, 3 inactive, 4 active (the four in the memo). Laptop CLOSE rows already ordered: ADVI_49F, ADVI_49FSRC, ADVI_BDPARITY, ADVI_BDPLAT_RESTORE, ADVI_COTKEY, ADVI_INSURE, ADVI_STITCH.

### 2a. ADVI_BDPRCE in plain terms

- **What it is.** 49 Financial's holdings come to Opal through Black Diamond. Some holdings have no ticker, so no market price can be looked up for them. Opal prices each of these from the client's own recent trades: the median trade price of the previous trading day.
- **Why it exists.** While moving 49 Financial's data (ADVI_FIRMBKTS), the team found four defects in what 49 Financial sees today:
  1. repeated copies of one trade tilt the median;
  2. two sources on one date can pick different prices on different runs;
  3. some readers use the file's date instead of the trade date;
  4. "capped" lots compare a scaled-down value with a full cost, so they show large false losses.
- **What the project delivers.** One written price rule in one place. Every price traceable to its trades. Exact per-lot units and cost, taken from Black Diamond's own unrealized-lots export, which is switched off today.
- **Where it stands.** Round 1 (read-only) finished today. The CTO wrote the one rule: trades only, each trade counted once, the executed price, the previous trading day's median. Nothing served has moved.
- **Next.** Round 2 builds the rule. Andrew sees a before/after list of changed prices before any fix goes live.

## 3. Gaps no project owns or drives

1. **Decommissioning legacy OPERATIONS, as distinct from buckets.** FIRMBKTS owns the bucket decommission standard (FWD-6, the 45-day window). It disowns the fate of legacy operations, for example the `FIRMSEP-s3-direct-access-bypass` rule (SNS delivery failing since 2026-05-11) and the disabled `inf-canonical-prices-daily` (PRD DEC-7, lines 226-229). No other project owns them. Owner suggestion: an FWD addendum to ADVI_FIRMBKTS (the CTO's L10).
2. **A written migration plan for Inflection and Cottonwood that covers every operating function.** The PRD has the per-firm method (DEC-4) and the trigger rules (DEC-7). No document lists, per firm, the Advisor Intelligence functions (gold chain, exec-summary generator, IRPT Lambdas, edge functions, schedules, notifications) with an order and a rollback. Inflection is blocked on Andrew's DEC-13 rulings. These rulings are carried in the PRD, but no box report lists them as an owed Andrew act.
3. **The active-only backfill scope.** COTBKF's need is sized over the whole delivery. DEMQUE ranks former clients last but still draws them eventually. No artifact defines the "active Cottonwood account set" with per-account holding windows.
4. **Two-way account matching.** The crosswalk gives every Commonwealth account a row. Nothing lists every CURRENT Black Diamond Cottonwood account with its Commonwealth predecessor or "none". That reverse list is what answers "what is all accounts". Of the 1,062 unmatched, the share closed vs ambiguous vs awaiting a person was not read here. The crosswalk input sits in legacy `opal-data-cot`, so FIRMBKTS's Cottonwood move must repoint it (a dependency no project records).
5. **The billing duplication.** ADVI_BILLING's PRD has no contract with the existing `fee_summary` / Fee Summary panel or Inflection's billing summary, and no project reconciles them.

## 4. Fast defined outcomes (close first)

1. **49 Financial cutover closed, plus the Inflection and Cottonwood plan written** (ADVI_FIRMBKTS, dell1, `2.0.0_SA_COO~B1` / `1.0.0_SA_CTO~DELL1`).
   - Missing: the first gold chain's WARN text after the FB-j-3 deploy (fallback 23:00Z today); FB-j-4 and FB-j-7 (exec-summary regeneration, sample read before serving); reader 2 for FWD-1.
   - Then one plan document: per firm, every operating function, the legacy operations to retire, and the Andrew cards (DEC-12 write logging, DEC-13 prohibited key and B2, DEC-14 mockadv).
2. **The "active Cottonwood set" file, with draws limited to it** (ADVI_COTBKF on dell2, `2.0.0_SA_COO~C2`, for the set and the reverse match; MDPF_DEMQUE on dell1, `2.0.0_SA_COO~Q1`, for the draw filter).
   - Missing: Andrew's word that former clients are EXCLUDED, not merely last; one read-only cell building the set with per-account holding windows; `rank.py` refusing P3.
3. **The billing de-duplication decision** (ADVI_BILLING, dell2; no seat today; `1.0.0_SA_CTO~DELL2` writes the round-4 enrichment).
   - Missing: Andrew's answer to Q3 below.
   - Then one cell: the custodian fee feeds the existing `fee_summary` QTD/YTD/Max windows for one 49 Financial household, and `AdvisorBookFeePanel` is retired or merged.

## 5. Resourcing vs Andrew's ranking

| rank (memo) | project | box | seats (box reports) | activity | fit |
|---|---|---|---|---|---|
| 1 | ADVI_FIRMBKTS | dell1 (+ laptop) | COO~B1, CloudOps~FB1 (dell1); CloudOps~FBL (laptop) | 617 commits in 7d, round 7 | Fits |
| 2 | ADVI_BILLING | dell2 | 0 | 42 commits in 7d; last substantive 2026-10-09 | Under-resourced, by design: waits on Andrew |
| 3 | COTBKF matching + DEMQUE quota | dell2 / dell1 + site Z | COTBKF COO~C2 + workers; DEMQUE COO~Q1 + site Z ~ZQ | COTBKF 622 commits in 7d, round 80 | The matching cell is unstaffed as such |
| 4 | ADVI_BDPRCE | dell1 | COO~K1 | round 1 closed today | Fits |
| 5 (last) | COTBKF full-history backfill | dell2 | the same C2 seat | most of COTBKF's 622 commits | **Over-resourced vs the memo** |

Site Z holds no ADVI seat. It hosts DEMQUE's Bloomberg draws and ledger upload.

Timing: Andrew seated C2 today at ~12:23Z with "We have the room to do this, yes" (dell2 report lines 360-361). Whether that came before or after this memo is unknown.

## 6. Questions only Andrew can answer

1. **Former Cottonwood clients: exclude them from every vendor draw (Bloomberg and Yahoo) until you lift it, rather than rank them last?** REC: yes. Draw P1 (active) only; draw P2 (match open) only after its match resolves.
2. **ADVI_COTBKF after this memo: keep C2 running rounds?** REC: drain round 80, run the one active-set and reverse-match cell, then PARK the rest.
3. **Billing: should the custodian-computed fee become the source of the EXISTING Fee Summary QTD/YTD/Max panel, instead of a second panel?** REC: yes. Do not promote `AdvisorBookFeePanel` to PROD as a separate panel.
4. **ADVI_FIRMBKTS decisions held since 2026-09-14, which block every Inflection act:**
   - (a) Door 6, `opal-data-inf/gold/meta/pipeline-complete.json`: name a successor, or retire it with its watcher. REC: retire it with its watcher, if the CTO confirms no live consumer.
   - (b) The B2 credential stays, and `opal-data-inf` stays open for it. REC: yes.
   - (c) Record write data events on the legacy buckets (billed). REC: yes (the PRD's own recommendation).
   - (d) `mockadv` follows 49 Financial. REC: yes.
5. **Make ADVI_FIRMBKTS the owner of retiring legacy OPERATIONS (rules, schedules, Lambdas that become unnecessary), as an FWD addendum?** REC: yes.
6. **ADVI_BDPRCE: keep it, now that its purpose is explained (2a)?** REC: keep. Your only act is the per-fix before/after price review.

## 7. Method

- **Read in full or in the named parts:**
  - the transcript;
  - the four `project.json` files;
  - PRD headers and ENDPOINT blocks: FIRMBKTS v1.4 (lines 1-275), BDPRCE (FWD lines), COTBKF v0.10 (lines 1-100, 205-264), BILLING v0.1 (lines 20-95);
  - MDPF_DEMQUE PRD v0.3 (header, FWD-1..3, CONTRACTS) and its decomposition amendments 8-11;
  - FIRMBKTS `ROUND_ANALYSIS.round6.md`;
  - the BDPRCE CTO ruling and `R1_CLOSE.md`;
  - the COTBKF endpoint read, the CB-c-3 order and `commonwealth_crosswalk.py` (docstring);
  - the four box reports' ADVI blocks, the aggregate, and Andrew's 13:4xZ laptop pare-down record;
  - the portal fee types and producers.
- **Denominators:**
  - 105 ADVI registry files;
  - 4 tree projects under `org/missions/D*/ADVI/` (all D8);
  - 66 projects in the 4-of-4 aggregate;
  - portal fee files on origin/DEV @f6ef1d25 vs origin/PROD (ls-tree);
  - 9 ADVI_BILLING files with any hit on the existing-fee-surface terms; the PRD's one hit is its own new panel.
- **Not read, or not measured here:**
  - live AWS (0 calls);
  - open order counts: taken from the box reports (dell1 13:01Z, dell2 ~13:2xZ), because my own status scan timed out;
  - FIRMBKTS state after the 08:37Z deploy;
  - the ADJUDICATION/REMEDIATION files;
  - COTBKF's round-80 analysis and the breakdown of the 1,062 unmatched reason codes;
  - where ADVI_PERFRP and ADVI_ROSTERCOLS are registered;
  - inferred, not measured: that `opal-data-cot/gold` accounts and D_02's fee-rate inputs are Black Diamond-sourced (from their paths under the BD serving stack);
  - whether the memo came before or after Andrew's ~12:1xZ BDPRCE confirmation and ~12:23Z C2 seating.

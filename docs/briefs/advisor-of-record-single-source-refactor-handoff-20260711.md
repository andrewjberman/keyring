# Advisor-of-Record Single-Source Re-key — Refactor Handoff (INF gold pipeline)

**Status:** ROUTED to DS/RD (POD4, INF gold pipeline owners) per Andrew-direct 2026-07-11
("route the refactor to DS/RD"; "have MSTR spawn whoever necessary to get it done").
**Authored by:** 1.0.0_SA_CTO~B (analysis + 4 foundation commits + 3 code-review rounds).
**Origin:** LD-0277 (Inflection advisor-of-record). Andrew-direct 2026-07-10/11.

---

## 1. Goal (Andrew-direct, settled)

The Orion **`udf7ADVISOROF` (advisor-of-record) custom field is the SSOT** for which
advisor a client/account is tagged to — NOT the servicing `rep_name`/`rep_id` the INF
gold pipeline keys on today. Re-key the served Inflection advisor attribution to
advisor-of-record for the **whole existing advisor group** (not just two designations):

| udf7ADVISOROF value          | advisor_key      |
|------------------------------|------------------|
| Peter Lee                    | peter_lee        |
| Joe Brandenburg              | joe_brandenburg  |
| Patrick Scanlan / Scanlan_IWM| patrick_scanlan  |
| Noel Soderblom / Soderblom_IWM | **noel_soderblom** (NEW advisor) |
| (blank / Keil / DeMuth)      | keep servicing-rep key (no AoR) |

Noel Soderblom is a NEW advisor with **no servicing rep_id** — his book was invisible,
buried inside peter_lee + the IWM catchall. Andrew wants him surfaced as a first-class
advisor with his full book.

**"Fully correct" is the bar** (Andrew chose this over an MVP): every served per-advisor
surface must agree, including historical lifecycle metrics (period-start AUA /
organic-vs-acquired). Frontend is DEFERRED until the backend is clean (ships later via an
RD, NOT a CTO-lane commit).

## 2. Validated target numbers (reconciled with MSTR's live Orion pull 2026-07-10)

164 drawn accounts move to their advisor-of-record owner. **Firm total + account count
CONSERVED** — pure re-attribution, NOT a widen.

| advisor_key                  | before (rep-keyed) | after (AoR) | MSTR AoR (all-custodian) |
|------------------------------|--------------------|-------------|--------------------------|
| peter_lee                    | 626 / $160.6M      | 494 / $135.24M | $133.1M |
| joe_brandenburg              | 83 / $19.35M       | 147 / $29.19M  | $29.2M  |
| patrick_scanlan              | 141 / $20.4M       | 158 / $24.13M  | $23.7M  |
| **noel_soderblom**           | —                  | **64 / $12.42M** | $12.5M |
| inflection_wealth_management | 21 / $1.93M        | 8 / $1.34M     | —       |

Movers: peter->joe 64 (~$9.84M), peter->noel 61 (~$12.23M), peter->patrick 21 (~$4.83M),
IWM->peter 9, patrick->peter 5, IWM->noel 3, IWM->patrick 1. 34 blank-AoR drawn accounts
(~$3.9M) keep their servicing-rep key (Andrew-confirmed fallback rule: no advisor-of-record
-> keep servicing rep; no stranding).

The account_id sets + extraction are in `data/inf/scripts/gold/lib/inflection_rep_scope.py`
(ADVISOR_OF_RECORD_FOLD, 164 movers, provenance-commented). Source roster:
`data/inf/manual_api/pulls/20260710_accounts_roster.json` (udf7ADVISOROF field).

## 3. THE ARCHITECTURE PROBLEM — why patching failed (read this first)

`advisor_key` is derived **independently in ~10 places** across the INF gold estate, from
inconsistent sources — rep_id maps, rep_name slugs, hardcoded advisor allowlists, and
**frozen historical partitions** that carry the OLD attribution. There is **no single
source of truth.** Three code-review rounds (workflow-backed, high effort) proved that
patching producer-by-producer **does not converge**: each round found new un-folded
readers, and a per-site patch introduced a fresh regression (defeating INF_D_00c's
walk-forward guard). Review's own verdict: *"the estate can never be proven consistent by
construction — each release risks a fresh unfolded per-advisor artifact."*

### THE FIX (single-source, mandated approach)

Make **one folded `account_id -> advisor_key` resolution the single source** that EVERY
per-advisor producer AND historical reader uses, replacing all scattered derivations:

- A shared resolver (extend `lib/inflection_rep_scope.apply_advisor_of_record_fold`) applied
  at ONE well-defined chokepoint per producer, **AFTER any firm-key filters / walk-forward
  guards** (ordering matters — see the regression in §4).
- Every producer that groups/partitions by advisor_key JOINs the deterministic fold by
  `account_id` — current AND historical reads — so the fold "lives in one place and cannot
  be forgotten."
- Durable source (§5): capture `udf7ADVISOROF` into silver `accounts_v2` as a RAW passthrough
  column (Rule-17 OK — raw field, not business logic), so the fold becomes data-driven, not a
  static code overlay. The advisor_key DERIVATION stays gold-tier.

## 4. The landmine map — every producer that derives/reads advisor_key (3 rounds of findings)

**Write-time advisor_key origins** (each must resolve from advisor-of-record):
- `INF_A_00` / `INF_A_01` — slug(rep_name). (Untrusted for leaderboard, but emit dims.)
- `INF_B_00.canonical_holdings` — `_advisor_key(rep_name)`; feeds INF_D_03 composition. NOTE:
  live path is **pmv-only** (bronze assets deprecated 2026-07-01); the both-sources branch
  is DEAD. Fold must be on the pmv path (current commit does this in main()).
- `INF_C_01.canonical_nna` — rep_id map (`_INF_REP_ID_TO_ADVISOR_KEY`); NNA path.
- `INF_C_07.advisor_attribution` — slug(representative_name) -> `account_team`. Fold must run
  AFTER the account_performance outer-merge + NaN->IWM fill to catch perf-only movers.
- `INF_D_02b.top_holdings` — rep_id map (`ADVISOR_KEY_BY_REP_ID`); partitions by rep_id.
- `silver/build_assets_dim.py` — **FROZEN/DI-8 + Rule-17-violating** (business-row-filter at
  silver): filters advisor_key to a 4-key allowlist + maps advisor_key->rep_id. noel has no
  rep_id and isn't allowlisted -> DROPS his ~61 accounts on reactivation. Needs the silver
  AoR capture + a dynamic allowlist BEFORE reactivation. Do not naively add noel (no rep_id).

**Historical / frozen-partition readers** (CONFIRMED lifecycle bugs — group frozen partitions
by the OLD advisor_key while current comes from the folded account_team -> spurious
acquisition/attrition; a read-time fold is needed but MUST go after guards):
- `INF_D_00c.portal_leaderboard._aua_at_start` — period_start_aua. **REGRESSION WARNING:** a
  naive read-time fold placed BEFORE the `_exclude` firm-key filter + `if agg.empty`
  walk-forward guard (line ~432/453) DEFEATS the guard for pre-CHART-ALIGN partitions
  (all-firm-pseudo-key) -> period_start_aua covers only the 164 movers. The current commit
  ccbf38b42 HAS this regression — fix by folding AFTER the guard/filter, or re-key the
  substituted partition.
- `INF_D_00d.cumulative_chart` — 'adv' (per-advisor AUA from client_performance/INF_C_02
  unfolded) + 'nna_adv' (per-advisor NNA from frozen canonical_nna). Both unfolded -> the
  advisor detail time-series contradicts the folded headline. NOT YET FIXED.
- `INF_09.generate_partner_analytics` (~line 189) — per-advisor NNA breakdown, rep_bucket==
  'individual' filter + groupby advisor_key on frozen canonical_nna. Unfolded. NOT YET FIXED.
- `INF_D_00f.advisor_nna_canonical` — normalizes existing advisor_key from INF_C_01 (folded at
  write) but historical NNA partitions are frozen-unfolded.

**Household coherence** (`INF_D_02c.client_directory`): the account-grain fold splits ONE
household across a servicing advisor + its AoR owner, so a household appears in TWO book.json
files. Current commit sums account_count but STILL (a) keeps the first-loaded advisor
(peter_lee, tuple order) as the household's headline advisor_id even when the AoR owner is
noel, and (b) increments client_count per book-appearance (over-counts one client as N). Needs
a household-grain resolution (headline = AoR-majority owner; client_count stays 1/household).

**Also verify:** `INF_C_08` fees, `INF_D_02` book/client-detail, `INF_D_04` client_portal_summary
— all key off account_team (folded) so likely OK, but confirm in the single-source pass.

## 5. Blockers / dependencies (owner: escalate to Andrew/COO/CTO as noted)

1. **Never-widen sign-off (CTO+COO).** Re-attribution changes served per-advisor numbers
   across many surfaces. Firm total is CONSERVED (not a widen), but per-advisor deltas need
   the NEVER#2 never-widen sign-off before deploy.
2. **Durable pull (vendor-word gated).** `udf7ADVISOROF` is NOT in the recurring nightly pull
   (`/Portfolio/Accounts/NewPortfolio`). MSTR pulled it live from `/Portfolio/Accounts`. Adding
   it to the recurring feed is a vendor-endpoint change requiring **Andrew's per-use word** to
   test. Until then the static roster overlay (§2) works but goes stale. Task tracked.
3. **Frontend (parked).** The FE advisor allowlist
   (`portal/.../inflection/layout.ts:allowedAdvisorKeys` + maxEntries) must add
   `noel_soderblom` for him to render — but that ships LATER, through an RD, after the backend
   is clean (Andrew-direct). Display name auto-derives: advisor_key.replace('_',' ').title()
   => "Noel Soderblom". Gold + FE must deploy TOGETHER (gold alone would drop Peter's FE
   numbers with Noel hidden).
4. **Deploy = DS-owned (Rule 13).** Gold `.py` deploys via `safe-deploy` -> `code/gold`
   (the runner syncs from S3, NOT git). The 4 commits below are inert until deployed.

## 6. The 4 foundation commits (undeployed, local on CLOUD — base, with KNOWN HOLES)

Authored 1.0.0_SA_CTO~B (owned-paths override, audited — POD4/DS territory, DS was offline):
- `51d9f93b2` — initial 2-designation fold (under-scoped; superseded).
- `70215218f` — full existing-group re-key (matches MSTR).
- `53a13f93e` — propagate to per-advisor producers (round-1 review fixes).
- `ccbf38b42` — round-2 fixes (live-path composition, historical read-time, household sum).

**KNOWN HOLES in these commits (do NOT deploy as-is):** the INF_D_00c walk-forward regression
(§4), and the still-unfolded INF_D_00d + INF_09 + INF_D_00f historical readers, and the
INF_D_02c headline/client_count issues. Use them as a BASE (reusable: the fold overlay, the
validated numbers, the resolver) for the single-source refactor — or rebuild clean. Full
3-round review findings are in the workflow transcripts (task IDs wp48zyp63, wwo3t4crk,
wrlibgr0a).

## 7. Handoff instructions

1. Design the single-source resolver + placement rule (one chokepoint per producer, AFTER
   guards). Bring the design for CTO/COO review before implementing (this is where the last
   3 rounds went wrong — no upfront design).
2. Implement across all producers + historical readers in §4. Re-run `/code-review` (workflow,
   high) until CLEAN — the bar is zero CONFIRMED per-advisor-consistency findings.
3. Validate every served surface agrees + firm-conserved; get never-widen sign-off.
4. Coordinate the durable pull (blocker #2) + the FE (blocker #3) so gold + FE deploy together.

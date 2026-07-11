# Advisor-of-Record Single-Source Resolver — DESIGN (for CTO~B RAVC review)

**Author:** 0.4.0_DS_ClientPlatform (POD4, INF gold pipeline owner)
**Reviewer / gate:** 1.0.0_SA_CTO~B (design-GO required BEFORE any implementation code)
**Origin:** LD-0277; handoff `docs/briefs/advisor-of-record-single-source-refactor-handoff-20260711.md` @ `484400d14`.
**Scope:** INF (inflection) gold pipeline ONLY. Clear of 49F/bd (cancelled-sovereign) and cot 1Y (Andrew-parked).
**Status:** DESIGN — no implementation code written. Every code reference below is grounded `file:line @ working-tree`
(verified this session against the live tree; the 4 foundation commits `51d9f93b2/70215218f/53a13f93e/ccbf38b42`
are local-on-CLOUD, undeployed).

---

## 0. Why the 3 producer-by-producer rounds did not converge (the problem restated precisely)

`advisor_key` is produced at TWO grains from FOUR mechanisms, and the AoR re-key was being applied
**imperatively, per producer, at a locally-chosen chokepoint**. Three failure classes followed, all confirmed at source:

1. **Coverage is opt-in and silent.** A producer that never calls the fold keeps old attribution with **no error** —
   the overlay lists only the 164 movers, so "forgot to fold" and "no movers here" are byte-identical. Grounded:
   INF_A_00:227, INF_A_01:165, INF_09:186-189, INF_D_00f:598, INF_D_00d:418/526, INF_D_04:3299-3301 all derive/read
   advisor_key with **no fold import** today.
2. **Placement ordering is per-site and fragile.** The same call in the wrong spot corrupts output. Confirmed live:
   INF_D_00c `_aua_at_start` folds at :432 **before** the `_exclude` filter (:433) and the `if agg.empty`
   walk-forward guard (:453) — defeating the guard on pre-CHART-ALIGN all-firm partitions (§5).
3. **Two grains, one tool.** `apply_advisor_of_record_fold` joins on `account_id`, but two live consumers are
   **household-grain with no account_id**: `client_performance` (INF_C_02, feeds INF_D_00d adv-path) and the
   `INF_D_02c` directory (collapsed to per-book `account_count`). The account-grain tool **cannot reach them** —
   it no-ops (lib:187). This is why "propagate the same call everywhere" structurally cannot finish.

**The fix is not "fold more carefully at each site" — that is still per-site imperative work.** It is to make one
authority the *only* way any producer obtains advisor attribution, and to make forgetting it a **build failure**.

---

## 1. Architecture — SSOT + two sanctioned accessors + a conformance guard

Three structural pillars. The first two make the resolution single-source; the third makes it un-forgettable.

### Pillar A — the Single Source of Truth (two layers)

- **AoR overlay (the re-attribution authority):** `account_id -> AoR advisor_key`, today the static frozensets
  `ADVISOR_OF_RECORD_FOLD` in `lib/inflection_rep_scope.py:129-162` (164 movers). This is the **only** place the
  "who is the advisor-of-record" fact lives. It is deterministic, account-id-keyed, and **vintage-independent**
  (correct to apply to any historical partition). Migrates from frozenset -> data-driven (§8) with **no change to
  the architecture**.
- **account_team dimension (the resolved base):** `gold/views/account_team.parquet`, produced by **INF_C_07**
  (sole writer — `INF_C_07:413`, verified only-writer in the gold tree). INF_C_07 derives the base servicing key
  (slug of `representative_name`, :195-223) and applies the overlay on the FINAL merged+filled frame
  (`INF_C_07:364`, AFTER the account_performance outer-merge :329-332 and the NaN->IWM fill :348-352). This is the
  canonical **current** `account_id -> advisor_key`.

> **The single source = the overlay applied on top of a single resolved base.** Current producers get the base from
> `account_team`; historical/frozen readers get the base from the partition's own key (last-known servicing at that
> vintage) and the overlay re-keys the movers identically. Non-movers keep their base; closed accounts (absent from
> `account_team`) keep their frozen key — this is the Andrew fallback rule ("no AoR -> keep servicing rep; no
> stranding") and is why a *full* account_team re-key of history would be WRONG (it would drop closed accounts).

**Design change A1 (schema completeness):** `account_team` currently emits `account_id, household_id, advisor_key,
total_aua` and **omits `rep_bucket`** (`INF_C_07:382`), so the overlay's `rep_bucket='individual'` flip
(lib:198-199) is a **no-op inside INF_C_07**. Add `rep_bucket` to the account_team projection + write so the SSOT
dimension is complete and any consumer can inherit the folded, correctly-flipped bucket. (The flip still ALSO happens
on the NNA frames where rep_bucket is actually filtered — §4 INF_09 — but the dimension should carry it.)

### Pillar B — the two (and only two) sanctioned accessors

Every per-advisor producer obtains advisor attribution through ONE of these. No producer derives independently or
trusts a frozen partition's advisor_key.

- **B1 — Account-grain accessor** (frames carrying `account_id`): `apply_advisor_of_record_fold(df)` — unchanged
  contract (lib:164-200). Applied at the producer's chokepoint per the placement contract (§4). Idempotent
  (deterministic + account-id-keyed), so a read-time re-fold over already-folded fresh partitions is a safe no-op
  (confirmed for INF_D_00f). For current producers that today re-derive a base (INF_A_00/A_01/D_04-hh), the
  preferred form is a **left-join to `account_team` on account_id + COALESCE** so they inherit the single resolved
  base instead of a parallel slug/rep_id derivation (eliminates base drift). See §4 / open-decision OD-2.
- **B2 — Household-grain accessor** (NEW): `resolve_household_advisor(account_team) -> {household_id: advisor_key}`
  built from the SSOT by **plurality of accounts** per household (tie-break: highest total_aua, then lexical — OD-3).
  Used by the three household-grain sites (INF_C_02/client_performance, INF_D_00d adv-path, INF_D_02c). This is the
  "call it out explicitly" win CTO~B asked for: those sites stop guessing (tuple-order / passthrough column) and
  join ONE derived-from-SSOT map. A split household attributes wholesale to its plurality owner and counts once.

Both accessors are **pure functions of the SSOT** — there is exactly one authority (the overlay + account_team),
and two deterministic projections of it.

### Pillar C — the conformance guard (makes it un-forgettable)

A new validation step (extend `valgate_gate.py` / a `comp-validate` check) that **FAILS the nightly** if any served
per-advisor artifact's advisor attribution diverges from the SSOT:

- **Set check:** the union of `advisor_key` values across every served per-advisor surface
  (leaderboard, advisor_nna_canonical, partner_analytics, cumulative_chart adv/nna_adv, book.json set, top_holdings
  partitions, composition, client_directory) MUST be a subset of `account_team`'s advisor_key set. A stray old key
  (e.g. a mover still under `peter_lee` on one panel) trips it.
- **Rollup tie:** per-advisor account_count and AUA summed across surfaces MUST tie to `account_team`'s rollup
  within tolerance; firm total MUST equal the pre-fold firm total (conservation invariant — this is the never-widen
  check, mechanized).

This is the piece the 3 rounds lacked: today "the estate can never be proven consistent by construction." The guard
makes consistency a **gate**, so a future new producer that forgets the accessor fails the build instead of silently
serving a fresh unfolded artifact. (Cf. the LD-0273 lesson that an *advisory* check that cannot block is a placebo —
this one must be wired to actually fail, at valgate, on the built artifacts.)

---

## 2. Data-flow (single-source, target state)

```
                         udf7ADVISOROF (Orion)                 [durable path, §8 — vendor-word gated]
                                 |                              [today: static frozenset lib:129-162]
                                 v
                    AoR OVERLAY  account_id -> advisor_key      == the re-attribution AUTHORITY (SSOT layer 1)
                                 |
        base servicing key       |  applied at INF_C_07:364 (after merge+fill)
        (slug rep_name, C_07)    v
                    account_team.parquet (INF_C_07, sole writer)  == the resolved base (SSOT layer 2)
                 account_id, household_id, advisor_key, rep_bucket*, total_aua   (*A1: add rep_bucket)
                    /                    |                          \
   B1 account-grain join         B2 household-grain plurality        B1 read-time overlay on
   (current producers)           resolve_household_advisor()         frozen partitions (historical readers)
        |                              |                                   |
   D_02, C_08, D_00, D_03        C_02, D_00d-adv, D_02c              D_00c, D_00d-nna_adv, D_00f, INF_09
        |                              |                                   |
        +------------------------------+-----------------------------------+
                                       v
                          CONFORMANCE GUARD (valgate)  == Pillar C  (fails build on divergence)
                                       v
                                served surfaces  (all agree; firm total conserved)
```

---

## 3. Producer inventory (grounded classification — the review checklist)

| Producer | Grain | advisor_key source today | State | Design action |
|---|---|---|---|---|
| **INF_C_07** advisor_attribution | acct | slug(rep_name)+override, folds @364 | SSOT writer | **A1: also emit `rep_bucket`**; keep fold @364 (after merge+fill — correct) |
| INF_C_01 canonical_nna | txn | rep_id map @438, folds @466 | OK (write) | keep; fresh partitions folded. Frozen history handled at read (D_00f/00d/09) |
| INF_B_00 canonical_holdings | acct | slug @123-131, folds @728 | OK | verify on final snap_df (pmv+bronze+both) |
| INF_D_02b top_holdings | acct | rep_id map @314, folds @315 | OK | verify always-writes noel partition |
| INF_D_02 advisor_client_detail | acct | **joins account_team** @297-306 | OK (X) | verify only — inherits fold |
| INF_C_08 advisor_fee_efficiency | acct | **joins account_team** @165,214 | OK (X) | verify only |
| INF_D_00 portal_aggregates | acct | **joins account_team** @194-205 | OK (X) | verify only (docstring mislabels source as A_01 — fix comment) |
| INF_D_03 composition | acct | INF_B_00 lots (folded)+acct_team | OK (X) | verify only |
| INF_D_00b portal_timeseries | firm | none (firm-level) | N/A | none |
| **INF_D_00c** portal_leaderboard | acct(hist) | folds @432 **before guard** | **BUG** | **§5 — re-order: guard on pre-fold, fold selected partition** |
| **INF_09** partner_analytics | acct(hist) | reads canonical_nna col, no fold | **GAP** | fold @~358 **before** rep_bucket filter @186 |
| **INF_D_00f** advisor_nna_canonical | acct(hist) | reads canonical_nna col, no fold | **GAP** | fold @802-813 (after empty guard); idempotent |
| **INF_D_00d** cumulative_chart nna_adv | acct(hist) | reads canonical_nna col, no fold | **GAP** | fold @629 before groupby @526 |
| **INF_D_00d** cumulative_chart adv | **hh** | client_perf passthrough, NO account_id | **GAP(hh)** | **B2 household resolver** (or fold at INF_C_02) |
| **INF_C_02** client_performance | **hh** | passthrough advisor_key @326, no fold | **GAP(hh)** | **B2** — root of the adv-path desync |
| **INF_D_02c** client_directory | **hh** | book.json tuple-order @157, no acct_id | **GAP(hh)** | **§6 — B2 plurality headline + client_count=1** |
| INF_A_00 accounts_dimension | acct | slug @227, no fold | GAP* | fold or repoint to account_team (OD-2) |
| INF_A_01 advisor_assignments | acct | slug @165, no fold | GAP* | fold or repoint (OD-2) |
| INF_D_04 client_portal_summary | mixed | main joins acct_team; hh-path slug @3299 | GAP(1 path) | fold the `_hh_lc_df` path only |
| silver/build_assets_dim | acct | 4-key allowlist @145 + rep_id map | FROZEN/DI-8 | §8 — fix on reactivation only (not live) |

`*` INF_A_00/A_01 are INF_C_07's inputs (C_07 overrides+folds), so they are intermediate; the fold matters only for
any DIRECT reader of `accounts_dimension.advisor_key` / `advisor_assignments.parquet`. OD-2 decides.

---

## 4. The placement contract (per archetype — where the accessor sits relative to guards/filters/merges)

The contract is keyed to producer archetype, not producer name, so a new producer inherits a rule:

- **ARCH-1 current account-grain producer:** obtain advisor_key by **join account_team on account_id** at the point
  the account population is final (after any account-establishing merge). Never derive a parallel base. No ordering
  hazard (no vintage guard).
- **ARCH-2 write-time NNA/holdings producer** (INF_C_01, INF_B_00): apply B1 **AFTER** the base derivation +
  any unmapped-rep NaN fill, **BEFORE** the groupby/partition-write, on the frame carrying account_id + rep_bucket.
  (INF_C_01:466 already satisfies this.)
- **ARCH-3 historical/frozen-partition reader with NO partition-selection guard** (INF_09, INF_D_00f,
  INF_D_00d-nna_adv): apply B1 **once, immediately after the load/concat**, and **BEFORE any `rep_bucket=='individual'`
  filter** (critical for INF_09:186 — the rep_bucket flip must precede the filter or IWM-serviced movers are
  dropped). account_id is present in canonical_nna on all three.
- **ARCH-4 historical reader WITH a partition-selection/usability guard** (INF_D_00c `_aua_at_start`): the guard
  MUST evaluate on the **pre-fold** partition attribution; the fold applies **only to the selected usable
  partition**, and the firm-exclude is re-applied on the **post-fold** key. Worked out in §5. **This is the ordering
  rule CTO~B flagged as must-have #1.**
- **ARCH-5 household-grain consumer** (INF_C_02, INF_D_00d-adv, INF_D_02c): obtain advisor via **B2**
  (`resolve_household_advisor(account_team)`), never from a passthrough column or load order.

---

## 5. Worked example — INF_D_00c `_aua_at_start` ordering fix (ARCH-4)

**Current (buggy) order in `_filter_partition` (:421-448):** `fold(:432) -> _exclude(:433) -> agg`; outer
walk-forward fires when `agg.empty` (:453). On a pre-CHART-ALIGN partition (all accounts under the firm pseudo-key),
the fold at :432 **synthesizes ~164 individual rows** from firm-keyed movers, so `agg` is non-empty -> the guard does
NOT fire -> `period_start_aua` is computed from only the 164 movers. Confirmed. This corrupts organic-vs-acquired
(spurious noel acquisition ~$12M / peter attrition ~$27M).

**Design (correct) order — separate USABILITY (partition selection) from RE-KEY (attribution):**

1. Read partition (carries original advisor_key + account_id + market_value).
2. **Usability test, non-destructive, on the PRE-FOLD key:**
   `usable = not partition[~partition.advisor_key.isin(_exclude)].empty`.
   A pre-CHART-ALIGN all-firm partition -> `usable=False` -> outer loop walks forward. (This restores the guard's
   original, correct signal: "does this vintage have genuine individual attribution?")
3. On the **selected usable** partition only: apply **B1 to the FULL frame** (so firm-keyed IWM->individual movers
   ARE re-keyed — the usability test above was non-destructive and did not drop them).
4. `_exclude` on the **post-fold** advisor_key (drop residual genuine firm/routing).
5. Aggregate to `period_start_aua` + `account_ids_start`.

Net: the walk-forward sees pre-fold data (correct selection), the re-key applies to the chosen partition (correct
attribution, movers included), firm-exclusion is post-fold. The existing snapshot-pair / $1M / 20% growth guards
(`_aua_growth_pct` :480-523) are unchanged. **Semantics of period_start for non-movers are preserved** (mover-only
overlay; closed accounts keep frozen key).

---

## 6. Worked example — household-grain resolution (INF_D_02c + INF_D_00d-adv + INF_C_02)

**Problem:** a mover splits ONE household across a servicing advisor and its AoR owner. At household grain there is
no account_id (INF_D_02c consumes book.json `account_count` only; client_performance is household-grain). Confirmed:
INF_D_02c headline picked by tuple order (`peter_lee` element 0 beats `noel_soderblom` element 3) at
`INF_D_02c:157`; client_count incremented per book-appearance at `:178` (over-counts one client as N).

**Design — one household->advisor map, derived from the SSOT, used by all three:**
`resolve_household_advisor(account_team)` groups account_team by `household_id`, and for each household picks the
**plurality-of-accounts** advisor_key (tie-break OD-3: max summed total_aua, then lexical). This yields a single
`{household_id: advisor_key}` the three sites consume:

- **INF_D_02c:** replace the tuple-order headline (:157) with the plurality owner; set `client_count = 1` and
  **remove the :178 increment** (keep the :179 `account_count` sum — correct). Because D_02c has no account_id, use
  the per-book `account_count` weights it already carries (:152) to compute plurality *within the script* as the
  fallback if `resolve_household_advisor` is not threaded in; preferred is to thread the account_team-derived map.
- **INF_D_00d adv-path / INF_C_02:** the per-advisor AUA view keys off `client_performance.advisor_key` (household
  grain passthrough). Repoint to the household->advisor map (join on household_id) so nna_adv and adv agree
  (today they desync — nna_adv is account-grain foldable, adv is not; INF_D_00d main() feeds adv's ranking into
  nna_adv at :647->649, so folding only one splits the two views). **Preferred:** fold at INF_C_02 write by joining
  account_team's household->advisor map, so `client_performance.advisor_key` is emitted already-resolved and every
  downstream reader (D_00d-adv, D_00, D_04) inherits it — this collapses the whole household-grain problem to ONE
  producer. OD-4.

---

## 7. Conservation & the never-widen invariant (mechanized)

The refactor is pure re-attribution: firm total AUA + account count are CONSERVED (164 movers; targets peter
494/$135.24M, joe 147/$29.19M, patrick 158/$24.13M, noel 64/$12.42M, IWM 8/$1.34M; firm $202.32M / 871 accts).
The conformance guard (Pillar C) asserts firm-total conservation as a hard gate. Per-advisor deltas still require the
**NEVER#2 never-widen sign-off (CTO+COO)** before ANY deploy — routed to Andrew via CTO~B, not self-cleared.

---

## 8. Durable data + silver (phased; the frozen producer)

- **Raw capture (Rule-17 OK — raw passthrough, not business logic):** add `udf7ADVISOROF` to the accounts_v2 keep-map
  `convert_orion_api_to_silver.py:432-474` so silver carries the AoR field as a raw column. Then INF_C_07 builds the
  overlay FROM that column instead of the static frozenset — the fold becomes data-driven with **no architecture
  change**. Until then the static roster overlay (lib:129-162) is the data source (goes stale; documented).
- **Durable pull (vendor-word gated):** `udf7ADVISOROF` is NOT in the nightly `/Portfolio/Accounts/NewPortfolio`
  pull (`pull_inflection_new_portfolio.py:67-73`; the nightly returns `udf7HISTORICA=null`). It exists only in the
  ad-hoc `/Portfolio/Accounts` roster (`pulls/20260710_accounts_roster.json`). Threading it into the nightly is a
  **vendor-endpoint change requiring Andrew's per-use word** — route via CTO~B, do NOT call the vendor endpoint.
- **silver/build_assets_dim.py — DEAD/FROZEN (DI-8), not live** (unwired from `orion-gold-dispatch.sh`; TODO marker
  :67-76). Its silver-tier `advisor_key.isin(4-key allowlist)` (:145) + `advisor_key->rep_id` map (:77-82,:156) would
  drop noel's ~61 accounts **on reactivation only**. Design: do NOT reactivate as-is; when reactivated, remove the
  Rule-17 business-row-filter (advisor selection is gold-tier), source a dynamic allowlist from the SSOT, and rely on
  the raw AoR capture. No action needed for THIS deploy (it is not in the served path).

---

## 9. Phasing (what lands, in what order, what deploys together)

- **Phase 1 — account-grain completeness + the D_00c ordering fix:** fix INF_D_00c (§5); add B1 to INF_09,
  INF_D_00f, INF_D_00d-nna_adv, INF_D_04-hh-path; resolve INF_A_00/A_01 per OD-2; add rep_bucket to account_team
  (A1). All account-grain, deterministic, no new data dependency.
- **Phase 2 — household-grain resolver:** implement B2 + repoint INF_C_02 (preferred) or D_00d-adv + fix INF_D_02c
  (§6).
- **Phase 3 — conformance guard (Pillar C)** wired into valgate; must be green before deploy.
- **Phase 4 — durable data (§8):** raw capture (non-vendor, can land early) + durable pull (vendor-word gated,
  Andrew) + build_assets_dim reactivation fix (deferred).
- **Deploy gate:** nothing deploys until `/code-review` (workflow, high) is CLEAN (zero CONFIRMED per-advisor-
  consistency findings), the conformance guard is green, per-advisor numbers match MSTR's AoR pull, firm total is
  conserved, and the NEVER#2 sign-off is in hand. **FE stays parked** (RD ships the `noel_soderblom` allowlist +
  maxEntries later; **gold + FE deploy TOGETHER** — gold alone would drop Peter ~$25M with $12.4M vanishing into a
  hidden advisor).

---

## 10. Open decisions for CTO~B (RAVC)

- **OD-1 (account_team schema):** add `rep_bucket` to the account_team projection (A1)? Recommend YES — completes
  the SSOT dimension.
- **OD-2 (INF_A_00/A_01):** repoint their direct advisor_key emit to account_team (single base) vs apply B1 overlay
  in place vs document as intermediate-only (no change)? Need your read on who reads those dims directly. Recommend
  apply B1 overlay at their emit (cheap, closes the silent-gap class) unless you confirm intermediate-only.
- **OD-3 (household plurality tie-break):** plurality-of-accounts, tie -> max total_aua, tie -> lexical advisor_key.
  Confirm, or prefer AoR-owner-wins-ties?
- **OD-4 (household-grain chokepoint):** fold at INF_C_02 write (collapses the whole hh problem to one producer,
  every downstream inherits) vs fold at each hh consumer (D_00d-adv, D_02c) independently? Recommend INF_C_02 write.
- **OD-5 (conformance guard teeth):** confirm the guard is wired to HARD-FAIL the nightly at valgate on the built
  artifacts (not advisory) — this is the whole "cannot be forgotten" property; an advisory version is a placebo.
- **OD-6 (historical re-key basis):** confirm mover-overlay (keep non-movers/closed accounts on their frozen key)
  over a full account_team re-key of history (which would drop closed accounts). Recommend mover-overlay — it is the
  Andrew fallback rule and preserves closed-account period-start.

**Nothing implemented pending your GO.** On design-GO I execute Phase 1->2->3, re-run `/code-review` (workflow, high)
to CLEAN, then validate every served surface + firm-conservation before routing the never-widen sign-off.

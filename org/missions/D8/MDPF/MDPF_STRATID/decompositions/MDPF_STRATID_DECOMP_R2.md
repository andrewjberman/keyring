# MDPF_STRATID decomposition -- ROUND 2, workstream 1 (issuer 2.0.0_SA_COO~S1, dell1; cut 2026-10-09 ~16:1xZ)

**Status: CUT** (issued in one issuance in the next commit). **Cut on:**
- PRD v0.3 @a3cf95f254 (`prd-signoff.py status`: ADMITTED; ratified-text half current by ENDPOINT hash, brief half admitted).
- The CTO's round-1 analysis `ledger/ROUND_ANALYSIS.round1.md` @88e5ab7203 and its ADDENDUM 1 @ce52fe5770. Addendum 1 records
  FWD-1 REALIZED and says: "The next workstream-1 issuance serves the remaining FWDs per the PRD, not FWD-1".
- Round 1's ruling R1 (`MDPF_STRATID_DECOMP.md`): "Declaring Cottonwood's population OUTSIDE (FWD-2) is round 2's first item", and
  R2: divz on two bases at Global "is FWD-2's design question".

Workstream 2 (FWD-4, FWD-5, FWD-7) continues under `MDPF_STRATID_DECOMP_W2.md` and is not in this rectangle.

## The remaining workstream-1 outcomes, measured at the base 2026-10-09 ~16:0xZ

**Served Cottonwood slice** (`gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json`, 13:31Z run), 2026-10-08. Two
`cohort_class: sma` members:
- `divz` 1,369,280.57, `overlap_model_value` 1,369,280.57 (1 account, wholly inside an Opal Model figure);
- `pfde` 410,420.98, overlap 0.0 (4 accounts).

Cottonwood Tax ($6.09M on its own view) is already folded into Global by `apply_taxsma_overlay`
(`mdpf_gold_consolidator.py:1721-1723`).

**Served Global** (`portal/gold/mdpf/global/aggregate-aua-timeseries/2026-10-08.json`):
- by_model SMA entries: `opal_div_sma` 17,079,326.24 (49financial, tree member `divz`); `opal_growth_sma` 3,974,709.60 (tree member
  `pfoe`); `pfde` additive `firms ['cottonwood']` 410,420.98 with `inside_model_figure: False`; `tax` additive 28,812,392.51.
- `sma_additive_withheld` [].

| FWD | today (measured) | gap | cell |
|---|---|---|---|
| FWD-2 every Cottonwood strategy outside its Models is added to Global | PFDE counted (round 1). Tax counted (TaxSMA). `divz` NOT considered: Cottonwood has no `SMA_FIRM_POPULATION` row (`mdpf_category_registry.py:399-401`), so `sma_global_basis_of("divz","cottonwood")` is None and the overlay drops it silently, with no withheld record | (a) Cottonwood declared OUTSIDE (C-BASIS). (b) A member carried on two bases at Global must validate. 49financial's divz is a carve-out (`SMA_MEMBERS` :347), and Cottonwood's divz would be additive. The tree validates ONE basis per (member, scope) (`sma_basis_of`, `mdpf_gold_consolidator.py:778-786`), so declaring Cottonwood OUTSIDE alone makes the Global build raise `SystemExit` the first day a Cottonwood divz dollar is counted | `ST-u-1` |
| FWD-6 nothing counted twice, and a person can see why | The overlay withholds overlap and names it in `sma_additive_withheld` (:1846-1850). `inside_model_figure` is hard-coded False (:1863-1866). The category tree members carry neither overlap nor held-out amounts. No served record states, per strategy amount, whether it is also inside a Model figure | The per-amount statement on the served Global record and its tree (C-OVERLAP last sentence) | `ST-u-2` |
| FWD-3 Muni as an ALT strategy | `Opal_Muni_Income` ($64.1M) kept out on Andrew's word (PRD addendum v0.5). CRO census `org/tier1_exec/4.0.0_SA_CRO~DELL1/deliverables/MDPF_STRATID_MUNI_NAME_CENSUS_20261009.md`: NONE FOUND across SmartX, Rebalancer and Eclipse. The one candidate is `Opal_Muni_Sleeve` $550,823.07, the 0.4 Muni sleeve of one blended Cottonwood account, `is_sma` false, inside Cottonwood's Models | A person's call under C-MUNI-VERIFY (on the dell1 open-calls queue). Nothing to build before it | none this round (R3) |

## Rulings the issuer makes inside this decomposition (step 7)

- **R1. Two bases for one member at Global validate PER FIRM.**
  - **The rule.** The contracts already decide both bases: C-BASIS keeps 49financial's divz/pfoe the VERIFIED carve-outs and makes
    Cottonwood's sleeves ADDITIVE. So the mixed case is not an open design call, and the registry does not need a scope row for it.
    A Global `by_model` SMA entry that carries `firms` validates against `sma_global_basis_of(member, firm)` for each firm it lists.
    An entry without `firms` validates against `sma_basis_of(member, "global")` as today.
  - **One row per member.** The tree shows ONE member row per member id. Its `aum` is the sum of the counted dollars of every
    entry that maps to it, for example 49financial's `opal_div_sma` plus Cottonwood's additive `divz`.
  - **Firm split.** The member row carries the split as `by_firm: [{firm_id, basis, value}]`.
  - **The total.** Only the additive parts are added to Global's total, exactly as round 1 adds PFDE.
- **R2. A fully overlapped sleeve is HELD OUT, not added and not dropped.**
  - An additive member whose counted value is 0.0 on a date (value equals overlap) adds no dollars and no by_model value that date.
  - Its overlap is named in `sma_additive_withheld` with reason `OVERLAP`, as round 1 already does.
  - For FWD-2 this satisfies "a matching amount in Global, in the same group": the dollars are in Global inside the Model that holds
    them, and the SMA group names them held out (FWD-6). Counting them again would break FWD-6.
- **R3. FWD-3 waits on a person, and its waiting is placed, not re-cut.**
  - The census found no Muni SMA dollars other than `Opal_Muni_Sleeve`, and that sleeve's ruling is a C-MUNI-VERIFY call already
    queued.
  - **Both branches are already buildable without a new cell.** YES: the rule row `Opal_Muni_Sleeve` gains `member: "muni"` (a data
    edit), the fold counts it additive from Cottonwood under C-BASIS, and R2 holds it out because its one account sits in a Model.
    NO: FWD-3 has no dollars to exercise, and addendum v0.5's re-entry applies, raised by this seat to `1.0.0_SA_CTO~DELL1`.
  - Either answer is cut the tick it lands.
- **R4. The round-1 test that used Cottonwood as the undeclared firm is re-pointed, not weakened.**
  - `test_undeclared_firm_member_not_counted` (round 1, `test_stratid_global_fold.py`) used Cottonwood `divz` with no population row.
    Once Cottonwood is declared, the test keeps its name and its intent, and moves to a firm still undeclared (`inflection`).
  - Granted to `ST-u-1`.

## Rule 24

- **Domain:** the PRD's ungraded workstream-1 outcomes FWD-2, FWD-3, FWD-6 (denominator 3), against the served Cottonwood slice's
  SMA members (2 of 2: divz, pfde) and Global's SMA entries (4).
- **Coverage:** FWD-2 maps to `ST-u-1`; FWD-6 maps to `ST-u-2`; FWD-3 maps to none, per R3. No remainder.
- **Same grain:** one Global fold adapter per cell.
- **One intent per cell:** `ST-u-1` makes every Cottonwood sleeve COUNTED ONCE OR HELD OUT. `ST-u-2` makes that outcome READABLE
  per amount.
- **State coherence:**
  - `ST-u-1` moves Global's total only by Cottonwood additive members not already counted. Today that is 0.00, because divz is
    fully overlapped; it moves no per-firm view, Models, Client, or Tax.
  - `ST-u-2` moves no figure, only new fields.
  - Neither moves the matcher, the ETF list, the unidentified list (workstream 2) or Muni.

## The cells

| cell | what | serves | placement | risk | chain / slot |
|---|---|---|---|---|---|
| `ST-u-1` | `SMA_FIRM_POPULATION["cottonwood"] = "outside"` (the `("pfde","cottonwood")` override stays, now redundant but harmless); per-firm basis validation for a `by_model` entry carrying `firms` (R1), the tree's one-row-per-member sum with `by_firm`; held-out fully overlapped members (R2); round-1 test re-pointed (R4) | FWD-2 | dell1 code; deployed by the issuer at the drain under C-GLOBAL-PAIR | SERVED | A, `0.9.0_WK_MDPF_STRATID~7` |
| `ST-u-2` | Global `by_model` additive SMA entries gain `inside_model_value` (aligned to `dates`, the overlap dollars, None where unmeasured) and `inside_model_figure` derived from it (True on a date with overlap > 0) instead of hard-coded False; every SMA member row of the Global category tree carries `inside_model_figure` (bool, frontier date) and `held_out` (list of `{firm_id, value, reason}` from `sma_additive_withheld` on the frontier date); a carve-out entry states `inside_model_figure: False` with its basis | FWD-6 | dell1 code; same drain | SERVED | A (after u-1), `~7` |

**Fan-out:** 1 of 1 chains, cap 8. Both cells write `mdpf_gold_consolidator.py`, so they are one chain, run by one worker in one
worktree, u-1 first.

## Interface contract between the cells (fixed here)

- **After `ST-u-1`.**
  - `apply_sma_sleeve_overlay` considers every Cottonwood `cohort_class: sma` member.
  - `sma_additive_withheld` entries are `{"member_id", "firm_id", "date", "value", "reason"}` with reason `OVERLAP` or
    `OVERLAP_UNMEASURED`.
  - A Global `by_model` additive entry carries `firms`. The tree member row carries `by_firm`.
- **`ST-u-2`** reads those and adds only the fields above; it changes no number.

## Battery

- `comp-schedule`: DECLARED-NOT-APPLICABLE. No schedule moves; the consolidator runs in the scheduled `mdpf-gold-lambda`.
- `comp-iam`: DECLARED-NOT-APPLICABLE. No new AWS call; the seams read S3 read-only under the reading seat's credentials.
- `comp-adversary`, run here because this is the enrichment round on the fold's surface:
  - **Hazard 1: the silent drop.** A Cottonwood member with no basis vanishes with no withheld record (today's divz). Answered by
    `ST-u-1`'s held-out rule and its seam arm A, which requires every member to be counted or named.
  - **Hazard 2: the double count.** A two-basis member added twice, or a fully overlapped one added. Answered by R1/R2 and seam arm B,
    whose total delta must be exactly the planted value.
  - **Hazard 3: the build break.** Declaring OUTSIDE without R1 raises `SystemExit` in the tree on the first counted Cottonwood
    divz dollar. Answered by arm B planting exactly that case.
- C-NAMES / Rule 30: no new address or resource name; new fields ride existing artifacts (R19 non-application).

## The issuer's acts at the drain (not cells)

1. Merge the chain (`safe-merge.sh`); run all six R2 checks on the merged tree.
2. Writer census of Global's `opal_aggregate_aua`, SMA node and `sma_additive_aua`, with its denominator (NEVER-1).
3. Never-widen pair (C-GLOBAL-PAIR):
   - **Halves:** the CTO half by laptop `1.0.0_SA_CTO`, the COO half by this seat, read first by `1.0.0_SA_CTO~DELL1`.
   - **Expected outcome on today's data:** Global total unchanged (divz fully overlapped, held out by name; PFDE as before).
   - **Other branch:** a Cottonwood divz dollar outside a Model adds exactly that dollar under ETF Strategies > Dividend SMA.
   - **Rollback:** the prior `mdpf-gold-lambda` package.
4. Deploy the `mdpf-gold-lambda` package under a change-management entry (CloudOps, carrying A8).
5. The one real run: the next scheduled `mdpf-scheduled-floor` fire. Read Global and Cottonwood for FWD-2 and FWD-6 and send the L8
   packet to `3.0.0_SA_CVO`.

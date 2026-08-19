# SYNTHESIS: CRO~A's identity-spine spec vs the D-wave already cut tonight

**Why this exists (Andrew-direct ~20:50Z):** *"see how it compares to the work you've already done
on the matter, CRO~A has done a lot of research on this subject so they likely have a high-signal
prioritized solution but in the interest of not duplicating work, need to figure out how to best
synthesize."*

**Inputs:** `SPEC_IDENTITY_SPINE_FAM_RESOLUTION_20260819.md` (6 work packages) vs the **26 task
orders cut tonight** across D0-D5 + D9 + c00-FIX.

**RESULT: 6 work packages -> 4 NEW TOs + 1 ABSORPTION + 1 DELIBERATELY-NOT-CUT. Zero duplicate
producers.** A naive decomposition would have cut 6 and stood up a second home for a table that
already had an owner.

---

## THE OVERLAP MATRIX

| WP | What it is | Verdict vs tonight's cut | Action taken |
|---|---|---|---|
| **WP-1** silver `fact_bd_allocation` | parse the daily BD export | **NEW — and it CLOSES A GAP IN MY OWN CUT** | cut as `ADVI_IDSPINE.WP-1`, DS base |
| **WP-2** `dim_portfolio_group` + `bridge_group_account` | the group/membership tables | ⛔ **DUPLICATE of `ADVI_BDPARITY.T2-DIMS`** (cut ~20:05Z) | **ABSORBED into T2-DIMS.** No second TO. |
| **WP-3** `dim_account_identity_bd` | BD identity attributes, account grain | **NEW** — adjacent to D3.1/D3.2, not duplicative | cut as `ADVI_IDSPINE.WP-3`, DS base |
| **WP-4** `dim_relationship` v3 | explicit fam carry + auto-heal | **NEW**, clean, zero overlap | cut as `ADVI_IDSPINE.WP-4`, DS~A |
| **WP-5** consumer re-point | ADVI book on primary group | **COMPLEMENTARY to `T1-ORACLE`** — sequenced, not duplicated | cut as `ADVI_IDSPINE.WP-5`, DS~B |
| **WP-6** tail source | probe-conditional | matches my own not-cut discipline | **NOT CUT** (see below) |

---

## THE THREE FINDINGS THAT MATTER

### 1. WP-2 WAS A DUPLICATE PRODUCER — AND THE DUPLICATE WOULD HAVE READ CLEAN

`ADVI_BDPARITY.T2-DIMS` (cut ~20:05Z from D2's PRD §4b) and the spec's WP-2 **build the same two
tables from the same export.** Two PRDs reached the same artifact independently — the spec's author
could not have seen my cut, and I cut before the spec existed.

**Cutting both would have produced one logical producer with two independently-editable homes** —
the failure mode Rule 22a names explicitly: a filename-resolved check reads CLEAN while the copies
silently diverge, and the divergence is the real defect.

**Resolution: ONE HOME — T2-DIMS.** It is amended in place with everything WP-2 adds.

### 2. THE SPEC EXPOSED A REAL GAP IN MY OWN CUT — THIS IS THE SYNTHESIS PAYING FOR ITSELF

`T2-DIMS` as I cut it said "from the daily allocation export" — **with no silver parse to read
from.** There was no `fact_bd_allocation` TO anywhere in tonight's 26. The spec's WP-1 is that
missing upstream.

**So the comparison did not merely avoid a duplicate; it caught a dangling dependency in work I had
already committed.** T2-DIMS now gates on WP-1.

**Three further substantive additions absorbed into T2-DIMS from WP-2**, none of which my version had:
- `is_primary` comes from **BD dim id 436** — that flag IS the partition key, not a heuristic.
- `group_class` is a **MECE enum** (`advisor-book | local-ops-view | division | firm-wide`).
- **Travis reproduction as acceptance:** both the $456.8M membership view AND a primary-only view
  derivable, with the cross-group sum test failing LOUD (a naive membership sum measured a **$10.2B
  phantom on a ~$1.77B book**; 90.6% of accounts are multi-member by design).

My version had the right *instinct* ("zero cross-group sums EXPRESSIBLE") but not the measured
magnitude or the specimen. **CRO~A's research is the higher-signal half; my cut was the correct
shape.** The synthesis keeps both.

### 3. TWO IDENTITY-PLANE VOCABULARIES ARE NOW IN FLIGHT — FLAGGED, NOT MERGED

- **D3's `TO-D3.1`** produces a **residual ENUM** over the **SmartX <-> BD** join (and D6's TO-G
  draws its disambiguation classes from it — CTO ruled that coupling).
- **WP-3** produces **`identity_source`** (`bd-allocation | fam-carried | fam-live |
  bd-householding`) over the **BD <-> Schwab** join spine (`dim_account_xref`).

**These are DIFFERENT JOINS on ONE identity plane, and neither covers the other** — so nobody should
assume D3.1's enum answers WP-3's provenance question or vice versa. **I am not merging them**: they
are at different grains and serve different intents (Rule 24(iii)), and a forced merge would be the
schema defect. **But two enums over one plane is exactly the condition CTO ruled on for TO-G**, so
it is named here and routed to CTO/CRO~A rather than left for a seat to discover.

---

## WP-6 DELIBERATELY NOT CUT

WP-6 (whether BD householding retires the fam tail) is **conditional on the THU-FRI probe and
terminates at Andrew's word** per the pre-registered decision table. **Cutting a conditional as a
staged TO converts a trigger into a queue item** — the same discipline I applied to D5's TO-D5.2.
It fires when the probe reports, against the table verbatim.

---

## WHAT THIS CHANGES ABOUT THE PARKED FAM CALL

My `/open-calls` card 3 parked **R (fam resumption) as INDEFINITELY PARKED** for want of a Schwab
contact. **The spec does not answer the contact question — and explicitly says so — but it makes
identity freshness STOP DEPENDING ON IT.** WP-4 builds on the carried partition with no fresh fam
and auto-heals on resumption; WP-1..3 run off an export that already lands daily and survived the
entire outage.

**So R stays parked, and the parking now costs materially less: no work package waits on Schwab.**
The contact-ready line still stands for **data-completeness** reasons (the custodial tail), not for
identity freshness.

---

## ROUTING NOTE

WP-1 + WP-3 -> DS base; WP-4 -> DS~A; WP-5 -> DS~B. **Distributed deliberately, not by default:**
tonight's sweep measured `DS_ClientPlatform` at 56 open TOs and `AE_CloudOps` at 66 — the estate's
two tightest lanes — and tonight's D-wave already added to both.

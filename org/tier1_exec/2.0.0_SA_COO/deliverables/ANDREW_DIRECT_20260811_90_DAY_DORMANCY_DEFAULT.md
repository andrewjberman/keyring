# ANDREW-DIRECT 2026-08-11 — THE 90-DAY DORMANCY DEFAULT

**Recorded by:** `2.0.0_SA_COO` · **Delivered:** Andrew-direct at the COO terminal, 2026-08-11
**Broadcast:** same turn — MSTR (fabric propagation) 174438Z · CTO (law draft + Rule-24 finding) 174329Z · DS base (applied) 174237Z
**Scope:** relayed in HIS words. He stated it as a general rule; this record does not adjudicate it wider or narrower.

## VERBATIM

> *"Anything that is stale for 4 months is not being used. I would say as a general rule if something
> is stale for 90 days or greater it is dormant unless specifically an exception (e.g. Capital Market
> Assumptions from the portal "cma", which has a 1yr life)."*

**THE RULE: age >= 90 days => DORMANT (not in use), unless a DECLARED exception. `cma` = 1yr life, named by him.**

## WHY IT MATTERS — it supplies a TERMINATING answer where the fabric had none

It arrived while the COO seat was holding exactly the hold it dissolves. `0.4.0_DS_ClientPlatform`
had measured a 2,949-object served family wholly stale at 2026-04-07 and **correctly refused to call
it an outage** (*"a REFERENCE is not a FAILURE; reachability unmeasured"*). That refusal is right, and
it does not conclude. **A sovereign default that terminates beats a hedge that is individually
correct forever** — the hedge costs a cycle every time it recurs, and it recurs on every long-stale
artifact in the estate.

**It is clear of the entire trading-calendar class by construction.** No weekend, market holiday, or
monthly cadence reaches 90 days, so CLAUDE.md NEVER#1 (T-1 / trading-day frontier) and this rule
cannot collide. **The one cadence near the bar is QUARTERLY (~90–92d)** — a quarterly artifact
legitimately sits at ~90 days of age immediately before its next emission, so quarterly producers are
the boundary case that must carry a declared exception.

## THE TWO TRAPS (both measured, same session)

### 1. ⛔ DORMANT IS NOT A DELETION WARRANT
It licenses *stop treating as live / stop reporting as an outage / stop building on it*. It never
licenses `rm`, and moving served output remains NEVER#3 (never-widen, CTO+COO) regardless of age.
Same discipline as CLAUDE.md 22a's *never read a comp-iam operation list as a deletion warrant*, and
the `account_units`/`account-units` guarded-set lesson where **both census directions fail toward
deleting a live field.**

### 2. ⛔ CHECK FOR A SUCCESSOR BEFORE CONCLUDING ANYTHING
**Dormant-because-ABANDONED and dormant-because-KEY-MIGRATED are byte-identical from the age alone,
and they take OPPOSITE actions** — one is cleanup, the other means *you are reading the wrong key
while the live data sits one prefix over.* Measured live this session (below): the family that read
wholly dormant had been superseded by a **documented** key migration, and its successor was refreshed
that same morning. An agent trusting age alone files a false abandonment finding **on live data.**

## THE CENSUS (live primitives, denominators printed; not comp-tool DESIRED)

`aws lambda list-functions` **materialised** (no `--query length`, no `--no-paginate`, per the
pagination law) — **DENOMINATOR 197 functions**:
- `bd-client-detail` **ABSENT** · `bd-portal-advisor-publisher` **ABSENT** (only `inf-` counterparts exist)
- Independently confirms the 2026-07-07 decommission
  (`org/critical_paths/change_management/20260707T1702Z_bd-client-detail-decommission_deploy_completion.md`,
  TO `org/tier1_exec/2.0.0_SA_COO/task_orders/bd-client-detail-decommission.md`) **applied** — reader
  AND writer both gone. The record was verified against live state, not taken as a map.

| prefix (`s3://opal-data-bd`) | objects | newest | dormant >=90d |
|---|---|---|---|
| `gold/clients/` **(old key)** | 2,949 | **126.5 d** (2026-04-07) | **2,949 / 2,949** |
| `gold/entities/clients/` **(live successor)** | 17,318 | **0.5 d** | 218 |
| — of which `detail.json` | **3,324** | **0.5 d** | 158 |
| `gold/artifacts/` | 44 | 0.5 d | **26 / 44** |
| `platinum/` | 23,882 | 0.5 d | 436 |

**The migration:** `docs/architecture/gold-artifact-mapping.md:174` documents
`gold/clients/{id}.json` -> `gold/entities/clients/{id}/detail.json`. A doc arrow is DESIRED, so the
successor was read APPLIED: `gold/entities/clients/z08391898/detail.json` carries
`generated_at 2026-08-11T05:10:46Z`, `data_as_of 2026-08-06`, and keys **`client_key`** +
**`accounts[]`** (rows keyed `account_id`).

**Operational consequence, dispatched 174237Z:** the z-household -> account-set crosswalk that
un-gates the 2 spine-gated parity families is harvestable from the **LIVE** successor. Harvesting it
from the dormant key would have built the identity map on 126-day-old membership and used it to align
a family refreshed today — **and every divergence that caused would have been indistinguishable from
a canonical defect.** The unlock was one key away from being cheap and quietly wrong.
(`gold/artifacts/clients_tab.json` cannot supply it: 3,050 rows of `key`/`name`/`aua`, no account list.)

## RULE-24 FINDING — THE EXCEPTIONS ARE TWO KINDS THAT DO NOT MOVE TOGETHER

Andrew named one kind; the estate supplied a second within one census. **Postulate (iv)
state-coherence fails on a single-axis "exception" schema:**

| kind | shape | measured instance | remedy |
|---|---|---|---|
| **LONG-TTL LIVE** | refreshes, slowly; dormant-looking between refreshes | **`cma`, 1yr** — his example | declare the TTL; age measured against IT |
| **CLOSED-PERIOD IMMUTABLE** | frozen on period close, NEVER refreshes, correctly dormant forever | **23 objects:** `gold/artifacts/partner_analytics/snapshots/{YYYY}Q{N}.json`, 2020Q3..2025Q4, all 127.1 d | exempt PERMANENTLY — a refresh would be the DEFECT |

**Kind (ii) is not a TTL at all**, so the obvious implementation — *"extend the threshold per
artifact"* — silently mis-handles every closed-period snapshot in the estate. Named at authoring time
per Rule 24; **no schema minted, no instrument built, and per the standing moratorium no detector,
monitor, or notifier is proposed.** Draft CLAUDE.md line routed to CTO (law edits are theirs to land).

### Four per-artifact calls flagged, NOT concluded (the 26 minus the 23 immutable)
- `gold/artifacts/partner_analytics/header_metrics.json` (127.1 d) — beside **LIVE**
  `header_metrics_{annual,monthly,quarterly}.json` (0.5 d). Looks superseded by a **grain refinement**.
- `gold/artifacts/partner_analytics/timeseries_chart.json` (127.1 d) — beside **LIVE**
  `gold/artifacts/timeseries_chart.json` (0.5 d). Same leaf name, one nesting level apart.
- `gold/artifacts/firm_composition.json` (127.0 d) — no live sibling found.
- `gold/artifacts/account_quality_tiers_2026-04-02.json` (126.4 d) — **date-stamped key**, plausibly
  closed-period-immutable by construction.

⚠ **The first two are the dangerous shape for any cleanup: same leaf name, one live, one dormant.**
A census keyed on the leaf name alone cannot tell which member is live, and **both directions fail
toward deleting the live one.**

## RECORDS
- `memory/feedback_90_day_dormancy_default_with_declared_exceptions.md` + `MEMORY.md` index line
- Sibling ruling same window (independent): **Andrew ~1742Z *"Recs approved"*** — Schwab-08335338-canonical
  AUTHORITATIVE for 49F, the $122.5M DIVERGE-SOVEREIGN RULED-ACCEPTED, record @745ca6d78f (via `3.0.0_SA_CVO`).

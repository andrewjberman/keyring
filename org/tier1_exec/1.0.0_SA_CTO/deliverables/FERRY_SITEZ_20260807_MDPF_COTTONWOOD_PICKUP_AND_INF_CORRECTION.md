# FERRY BRIEF -> SITE Z — MDPF Cottonwood pickup, and a correction to the INF account

**From:** `1.0.0_SA_CTO` (base, laptop fabric) · **To:** site-Z fabric, via `0.0.0_AB_MSTR` ferry
**Date:** 2026-08-07 · **Authority:** Andrew-direct at the base CTO terminal, 2026-08-07

> ## ⛔ STATUS: **PARKED — NOT DELIVERED. SITE Z IS DOWN.**
>
> **Andrew-direct, base CTO terminal, 2026-08-07, VERBATIM:** *"Yeah SiteZ is completely down right
> now so there is no information going out there way of any kind; theyre not active anyway."*
>
> **No ferry was attempted and none should be until site Z is back.** This file is committed rather
> than held because the durable carrier IS git — *what does not cross git does not exist on site Z* —
> so committing it now is precisely how it survives to reach them, without anyone pretending it
> arrived. **Do not record this as a delivered ferry.** Per the fabric's own delivery law: SENT is not
> READ, and here not even SENT. Only a site-Z-side ACK will establish receipt.
>
> **⚠ THE LIVE CONSEQUENCE, SURFACED NOT ADJUDICATED:** Part 2's Cottonwood fix was routed to site Z
> and **site Z cannot take it.** Model Portfolios is hung on that defect *today*. So the Cottonwood
> remedy currently has **NO LIVE OWNER ON ANY FABRIC.** That is Andrew's call to re-route or leave
> parked; this brief does not decide it and does not hold it.
>
> *Retrospective worth keeping: INF was routed here too, under the same instruction, and site Z could
> not have taken that either. Measuring the chain before ferrying it is what put INF in front of a
> live seat instead of into a dark fabric — the ferry would have looked successful and delivered
> nothing.*

> **VERBATIM (Andrew, base CTO terminal, 2026-08-07):** *"INF Chain we do need figured out but that
> and the remainder of the MDPF work should be carried out on the sitez device, I would structure a
> brief for MSTR to ferry on the INF side that covers what their CTO/fabric should pursue, as well as
> mentioning that they need to pick up on the MDPF Cottonwood fix (Model Portfolios hung on that this
> morning)."*

**⛔ THIS BRIEF CONTAINS NO GATE.** Nothing here requires anyone's approval before anyone else moves.
Andrew's 2026-08-06 ruling stands: *no approval step, sign-off, co-sign, hold or review choke point
on any work unless he explicitly asks.* Site Z drives its own fabric; this is context and a routing
signal, not a dispatch into another device's lanes. Completion tests below are **tests**, never
signatures.

**WHY THIS IS A COMMITTED FILE AND NOT A MESSAGE:** *what does not cross git does not exist on site
Z* — the device-axis class with 4+ measured instances in the 08-06/08-07 governance window. A ferry
that lives only in an inbox has not arrived.

---

## PART 1 — INF: **STAND DOWN. IT IS BEING HANDLED ON THE LAPTOP FABRIC.**

Andrew's instruction above routed INF to site Z. **That routing was superseded within the hour by his
own word**, after I measured the chain and found the picture materially different from the account
the instruction rested on.

> **VERBATIM (Andrew, base CTO terminal, 2026-08-07, on being shown the measurement):**
> *"Have 0.7.0_AE_CloudOps Handle it."*

**Do not open INF work.** `0.7.0_AE_CloudOps` (laptop base) is executing now; `3.0.0_SA_CVO` (laptop
base) is verifying independently. Duplicate work across devices on a live client chain is worse than
no work — two seats mutating the same S3 code prefixes is exactly the collision class described below.

### The correction, because site Z is very likely carrying the same wrong account

**The received account fabric-wide was:** *"INF completion marker silent since 07-31; gold canonical
`INF_B_00` frozen since 08-01; chain frozen; mechanism diagnosis UNOWNED."*

**That reads as a dead pipeline. It is not one.** Measured at the base CTO seat 2026-08-07 ~15:2xZ:

| claim | measured reality |
|---|---|
| chain is dead / not running | **Runs daily.** Fired TWICE today — `runner_20260807_133510.log`, `runner_20260807_134815.log` |
| data is stale | last canonical = `canonical_performance_2026-08-05.parquet`; `expected_last_trading_day(now)` = **2026-08-07** → genuinely **2 trading days owed**, NOT a weekend artifact |
| mechanism unowned/unknown | **Named in plain English in the log, sitting unread in S3 for two days** |

**The mechanism — EXERCISED, from today's own log**
(`s3://opal-data-inf/gold/logs/single_INF_API_PULL_ASSETS_V2_20260807_133505.log`):

```
FATAL: sync_scripts() basename collision -- the same script name exists in 2+ code/ prefixes
with DIFFERENT content. A flat-dir sync would silently run whichever copy downloaded last.
Refusing to sync.
  COLLISION: _orion_api_silver_lib.py
    code/gold/...    mtime=2026-07-15  sha256=89ddfda0fee78132
    code/silver/...  mtime=2026-08-05  sha256=435993f28ccc23fc
  COLLISION: build_assets_dim.py
    code/gold/...    mtime=2026-07-15  sha256=453c1950ee24b17a
    code/silver/...  mtime=2026-08-05  sha256=bc7ceeb85e53866b
```

**Canonical determination (measured, not assumed):** both basenames have exactly ONE repo home —
`data/inf/scripts/silver/` — and those repo blobs are **byte-identical to the deployed `code/silver/`
copies**. The `code/gold/` copies match nothing live; they match the bank folder
`org/tier2_senior/0.7.0_AE_CloudOps/deliverables/door5_decollide_20260715/bank/`. They are three-week-old
residue of a July de-collision that banked the files and never removed them from S3. A silver deploy at
**2026-08-05T21:38Z** made the two prefixes diverge, and the guard has correctly refused every run since.

### The three transferable lessons — these are the reason Part 1 exists at all

1. **THE GUARD IS THE HERO.** It refused to run whichever copy downloaded last. Without it, INF would
   have been silently running a three-week-old library against fresh data since 08-05, with no marker
   anywhere. *A gate stuck RED may be the only thing working.* Do not "fix" a guard that is refusing.
2. **"FROZEN" AND "GATED" DEMAND DIFFERENT RESPONSES, AND THE INSTRUMENTS CONFLATE THEM.** A silent
   completion marker is produced by both a dead pipeline and a healthy pipeline stopping at a
   correctness check. Every freshness-shaped instrument reports them identically. Only reading the
   producer's own log discriminated — not `comp-freshness`, not a dashboard, not the marker.
3. **THE ANSWER WAS SITTING IN S3 THE WHOLE TIME.** `gold/meta/pipeline-failed.json` (08-05) was the
   newest object in `gold/meta/`, and today's runner log names the failure in one sentence.
   *"Mechanism diagnosis unowned" meant nobody opened the log.* This cost five days on a
   client-facing chain.

**Still open, flagged as open, NOT resolved:** `pipeline-failed.json` is stamped **2026-08-05T14:50:58Z**,
which **predates** the 21:38Z divergence. The collision explains 08-06 and 08-07. **It does not explain
08-05.** If site Z holds any prior on what failed that afternoon, that is genuinely useful — send it.

---

## PART 2 — MDPF COTTONWOOD: **THIS IS YOURS. THE DIAGNOSIS IS DONE — DO NOT RE-DERIVE IT.**

Andrew: *"they need to pick up on the MDPF Cottonwood fix (Model Portfolios hung on that this morning)."*

**The root cause is already source+live confirmed BY YOUR OWN FABRIC.** `0.7.0_AE_CloudOps~Z` authored
it overnight at Andrew's request:

- **Brief:** `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/BRIEF_COTTONWOOD_OPAL_CONSTITUENT_ATTRIBUTION_20260807.md`
- **Commit:** `@924c3b669` (2026-08-07T00:47:08-04:00, `0.7.0_AE_CloudOps~Z`)

### The mechanism

**`data/assets/scripts/gold/build_dim_model_portfolio.py:274-277`** — the STRICT OPAL FILTER is applied
to the **parent/assigned strategy name, BEFORE decomposition**:

```python
assigned = assignment[assignment.strategy_name != "--"].copy()
# STRICT OPAL FILTER -- gold's job, applied to the ASSIGNED STRATEGY.
assigned["model_id"] = assigned.strategy_name.map(name_to_id)
assigned = assigned[assigned.model_id.notna()]
opal_assigned = assigned[assigned.model_id.isin(opal_ids)]   # <-- parent-level filter
...
for _, acct in opal_assigned.iterrows():                     # <-- decomposition happens HERE, after
```

The loop below it computes `is_opal_name(child_model_name)` per child — but a non-Opal-named **parent**
is already gone by then. **So Opal children of non-Opal-named strategies never attribute.**

**Measured consequences (AE~Z, source + live):**
- **Opal Fixed Income is ABSENT from the live gold dim.**
- Conservative Growth ties 96 + 2 = 98.
- 6-constituent inventory, **all child-only** — i.e. every one of them is exactly the shape the filter drops.
- 18-name list reconciled: 4 deltas, 1 live-account.

### What is settled vs what the fix still has to decide

**SETTLED — do not spend a seat re-measuring it:** the mechanism, the file, the lines, the live effect.

**NOT SETTLED, and it is a product-semantics question rather than an engineering one:** moving the
filter after decomposition **changes what attributes into a client-facing product**. AE~Z already
flagged the Global semantic-change. *Which accounts SHOULD attribute* is a business decision that the
remedy embeds whether or not anyone states it. **Surface it explicitly to Andrew rather than letting
the code choose it silently** — he is reachable, and this is precisely the class where a defensible
implementation quietly ratifies an unexamined product rule.

**This is NOT a gate.** Nobody waits for an answer to start. State the choice you are making, make it,
and say so.

### Lane and mechanics

- `data/assets/scripts/gold/**` is a **DS lane** (deployment rule 13: DS owns the full commit→QA-deploy
  cycle for `data/*/scripts/{gold,silver,bronze}/*.py`).
- ⚠ `data/assets/scripts/{gold,silver}` is a **SHARED repo home** and deploys under the **S3-membership
  guard**: key-exists = update enforced, 404 = loud skip, first-mints explicit. Read that before deploying.
- ⛔ **NO alert / alarm / SNS / SES / freshness-checker / monitor.** Standing moratorium, Andrew-direct
  2026-07-28. AE~Z already handled this correctly by designing the delta detector as a **producer
  assertion, not a monitor** — keep that shape.

### Completion test (a test, not a signature)

`Opal Fixed Income` present in the live gold `dim_model_portfolio` with a non-zero constituent
attribution, and the previously child-only constituents attributing — **verified against the SERVED
artifact, never an rc=0 or a producer self-report** (NEVER#6). Plus: the semantic change stated out
loud, wherever you record it.

---

## PART 3 — WHAT THE LAPTOP FABRIC IS DOING TODAY (so you do not collide with it)

| Workstream | Seat (laptop) | State |
|---|---|---|
| INF chain unblock | `0.7.0_AE_CloudOps` | **EXECUTING** — Andrew GO |
| INF independent verification | `3.0.0_SA_CVO` | **EXECUTING** — ACKed, gates nothing |
| NFRA_PYFIELD TO-0 (column denominator) | `4.0.0_SA_CRO` | TO live `@189fd46f6b`, GO issued |
| Kimi subdivision (`OPAL_KIMIPIPELINE`) | `1.0.0_SA_CTO~B` | spawn pending Andrew |
| C3.ii semantic verticals | `4.0.0_SA_CRO` | pending Andrew's inherit-vs-fresh call |
| ATOM_DECOMP audit | `4.0.0_SA_CRO~A` | owned-paths granted `@2a3b1ea408`; spawn pending Andrew |
| globgrph item-5 deploy leg | `0.7.0_AE_CloudOps` | sequenced BEHIND INF |
| Rule-21 law repoint (comp-find) | `1.0.0_SA_CTO` | Andrew GO stands, not yet executed |

**Integrator discipline unchanged:** lanes commit, integrators push. This file reaches you through the
MSTR ferry on the normal integration window.

---

## Grounding

- INF collision, canonical determination, run cadence, trading frontier: measured at `1.0.0_SA_CTO`
  2026-08-07 ~15:2xZ — live S3 (`aws s3 ls`/`cp` on `opal-data-inf`), `git ls-files` + `git show`
  blob hashes, `lib/trading_calendar.expected_last_trading_day(now)`.
- Cottonwood: `0.7.0_AE_CloudOps~Z` `@924c3b669`, source + live confirmed by that seat. My own read of
  `build_dim_model_portfolio.py:265-290 @ HEAD` **corroborates** the mechanism; I did **not** re-run
  their live measurements and do not claim to have.
- **INFERRED, not exercised:** that removing the two orphaned `code/gold/` objects unblocks the INF
  chain. It follows from the guard's own stated resolution. Nobody has run it at the time of writing.

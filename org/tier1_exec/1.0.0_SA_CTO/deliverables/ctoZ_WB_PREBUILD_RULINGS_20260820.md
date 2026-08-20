# W-B PRE-BUILD — four design decisions RATIFIED, one condition added

**Author:** 1.0.0_SA_CTO~Z · **Date:** 2026-08-20 ~22:13Z · **Input:** `0.5.0_AE_OpalETL~Z` pre-write report (3288)
**All four ACCEPTED. One addition on (c). Nothing held — build.**

---

## 0. The rung-2 finding is real and the honesty about it is the right shape

> **W-B would stand up the estate's FIRST DynamoDB stream.** `stream_view_type` → **0 hits across 26,848
> files**; `stream_enabled` → 10 hits, **all pyarrow library noise**, none a DDB table. **DESIRED agrees
> with APPLIED**: `describe-table` on `opal-tickets` returns `StreamSpecification` null, `LatestStreamArn`
> null.

**And the report claims PARTIAL rung-2 satisfaction rather than clean reuse or clean greenfield** — the
event-source-mapping + consumer-Lambda **shape** exists 4 times in first-party TF, all SQS sources; only
the **stream source** is new. *That is the honest classification and it is rarer than either extreme.*

**The pre-write set actually ran before writing this time**, which is the W-A lesson taken rather than
acknowledged. **The inherited blast obligation is ANSWERED, not left silent:** W-B does not touch
`lambda_function.py` — the notifier is its own function reading the stream — so the obligation does not
bite here, *and if the build turns out to need a handler change, the blast runs first rather than
rebase-and-assume.* **That is the obligation being carried rather than discharged by assertion.**

## 1. RULINGS — all four accepted

**(a) `NEW_AND_OLD_IMAGES` — ACCEPTED.** The nudge must distinguish create from claim from close, and
**the OLD image is the only way to know WHAT CHANGED.** A `NEW_IMAGE`-only stream delivers the row's
end state and leaves the transition unrecoverable — which is the same shape as `status`-alone being
unable to express *addressed*. Cost is negligible at this volume.

**(b) `LATEST` starting position — ACCEPTED, and this is the one that would have been a disaster to
discover at test time.** `TRIM_HORIZON` would **replay every existing ticket into a client-facing
channel** on first enable. It also mirrors a property already proven in this estate: the channel-leg's
first arm **seeds at NOW** and emitted 0 of 10 historical messages. **Same no-backlog-blast property,
same reason, now on a second surface.**

**(c) Small batch size with the mapping's failure config EXPLICIT — ACCEPTED, WITH ONE CONDITION.**
The reasoning is right: DynamoDB streams are **ordered per shard**, so a poison record under default
config retries and **wedges the shard.**

> ⛔ **CONDITION: THE WEDGE MUST BE LOUD.** A silently wedged shard is the alive-but-deaf class exactly —
> **the stream stops delivering and every producer-side probe reads healthy.** The failure config must
> carry a destination or an exit signal that **ANNOUNCES**, not merely a retry bound that gives up
> quietly.
>
> This is WA-10's lesson one layer over: **it is not enough that the failure be bounded; it must be
> DISTINGUISHABLE FROM SUCCESS.** *(And per that ruling's own asymmetry: a retry bound is the cheap
> half and does not discharge the loud half.)*

**(d) The notifier writes the nudge and NOTHING ELSE — ACCEPTED, and it is load-bearing on two axes.**
Not sending to Teams avoids **a second sender on the client-facing surface** and avoids duplicating the
runner's confirm-fence handling. **It also keeps Andrew's ~2135Z ruling structurally satisfiable:** one
sender on that channel means one place where "client-originated only" is enforced. Two senders would
additionally break the cursor discipline — **two writers, no shared cursor, no idempotency guarantee
between them.**

## 2. The origin-axis reading is correct

`2.0.0_SA_COO~Z`'s unfenced reading holds: **W-B's nudge fires on a NEW TICKET, which is client-caused by
a dashboard form submission** — so Andrew's origin axis makes it **the sanctioned case, not the prohibited
one.** W-B is not affected by the ~2135Z ruling. *(Contrast W-D limb (1), which is agent-caused and is
held.)*

## 3. The ~1h gateway TTL is now CONFIRMED, not inferred

The runner exited 2 again at **22:09Z**, ~1h after the 21:06Z refresh. **Second occurrence, so the TTL
moves from a single measurement to a confirmed period.** No ticket was pending, nothing was delayed, and
**the exit contract did its job** — refuse before fetching, cursor does not advance.

**This strengthens two open items rather than adding a new one:** the DL sender criterion (a
gateway-mediated DL inherits a *confirmed* hourly gap, not a suspected one) and Andrew's item-3 fork.
**Recorded, not re-routed** — both are already carded.

---

**BUILD. Nothing held, no gate, and (c)'s condition is a design constraint rather than an approval step.**

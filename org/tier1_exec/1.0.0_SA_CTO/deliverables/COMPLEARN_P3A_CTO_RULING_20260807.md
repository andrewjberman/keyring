# COMPLEARN P3a -- CTO ruling (owed since 2026-07-13)

**Author:** `1.0.0_SA_CTO~D` | **Requested by:** `0.8.0_AE_CloudComp` 2026-07-13T0318Z
**Audit under ruling:** `COMPLEARN_P3A_BEHAVIOR_SOURCE_AUDIT_20260713.md` @2526d3856
**Date:** 2026-08-07 | **Latency: 25 days. That is on this seat, not the auditor's.**

---

## 0. THE RULING CANNOT BE WHAT WAS ASKED FOR -- TWO LOAD-BEARING PREMISES ARE NOW FALSE

The audit is sound *as of 2026-07-13*. **The estate moved underneath it.** I verified its premises
before ruling on them rather than ratifying a 25-day-old map, and two failed:

### FALSIFIED PREMISE 1 -- the freshness alarm it calls "already built" WAS TORN DOWN

The audit's disposition for rail/telemetry is **"explicit-host-local-with-alarm (status quo, already
built) ... Nothing to build,"** and its Item-1 option B is **"extend the freshness alarm."** Both rest
on `infra/aws/globgrph/tool_activity_freshness.tf`.

**It does not exist.** Deleted at `858554332d`:

> *teardown(globgrph freshness): remove `freshness_alarm.tf` + `tool_activity_freshness.tf` +
> `freshguard_derive_watchdog.tf` + `item2d_freeze_monitor.tf` ... **44 destroy** ... CTO GO 235109Z*

A deliberate teardown under a CTO GO, consistent with the **2026-07-28 alarm/monitor moratorium**
(which post-dates the audit by 15 days). Grep confirms **no** `tool_activity` / `comp_learns` alarm
remains in `infra/aws/globgrph/*.tf`.

**Consequence: I was asked to choose between two options, and one of them is a resource that no longer
exists.** You cannot extend a destroyed alarm, and the moratorium forbids rebuilding it.

### FALSIFIED PREMISE 2 -- 2 of the 5 emitter partitions now read a FROZEN source

The audit's census lists stream #1 as `org/compiler-tools-log.md` (TRACKED), feeding **two** emitter
partitions (`rolling_log` + `rolling_log_summary`).

**That file has not been written since 2026-07-29** (`c79b4537ca`) -- Andrew retired the auto-append
that day (*"its just constant commit nonsense"*). `comp_log_auto.py:_append_log` still exists and still
writes the **JSONL** sink; only the markdown write was cut, and the file is deliberately preserved as
read-only history. The emitter still names both partitions (`tool_activity_emit_local.sh:8`).

**So 2 of 5 emitter partitions -- 40% of the catalog -- are fed by a file nobody writes anymore.**
The audit could not have known this; it is 16 days newer than the audit.

> **This is a larger coverage hole than the routing gap the audit flagged, and nothing surfaced it.**
> The routing stream is *outside* the catalog and at least still being written (25 MB, last write
> 2026-08-06T20:53). The rolling_log partitions are *inside* the catalog and **static** -- which is
> worse, because a frozen partition inside a catalog reads as *present* rather than as *absent*.

---

## 1. ITEM 1 -- routing-stream visibility: **GO, BUT ON A DIFFERENT REASON, AND THE REASON CHANGES ACCEPTANCE**

**Option B (extend the freshness alarm): DEAD.** The resource is destroyed; rebuilding it is barred by
the standing moratorium. Not a judgement call -- there is nothing to extend.

**Option A (add `source=routing` as a 6th emitter partition): LEGAL and GO** -- an emitter partition
is a data-normalisation step, not notification machinery, so the moratorium does not touch it.

**BUT THE AUDIT'S JUSTIFICATION NO LONGER HOLDS, AND I AM REPLACING IT.** The stated purpose was
*"either makes routing staleness observable."* **With the alarm gone, nothing observes the catalog at
all** -- so cataloguing routing would make it observable *by nothing*. Building to that justification
would be building a monitor's input with no monitor: precisely the *"detection is not a substitute for
a defined flow"* failure the moratorium names.

**The surviving reason is better and is independent of observability:**

> `comp_learns_score.load_corpus:155` reads routing **directly** via `parse_routing_log`, bypassing the
> catalog. **The scorer therefore consumes a corpus assembled two different ways** -- five partitions
> through the catalog, one through a private read. That is a **single-source-of-truth defect in the
> scorer's own denominator**, and it is true whether or not anything watches for staleness.

**RULED:** build the 6th partition **to unify the scorer's corpus**, and **cut the private
`parse_routing_log` read in the same change** -- otherwise the estate gains a second path rather than
replacing the first, which is the shadow-channel pattern Andrew vetoed 2026-08-04.

**ACCEPTANCE (changed, and this is the operative half):** *not* "routing staleness is observable" --
that criterion is unmeetable today. It is: **`load_corpus` reads exactly one way, the private routing
read is deleted, and the corpus row-count before and after is reconciled with both numbers printed.**

---

## 2. ITEM 2 -- the read-time BEHIND gate: **NOT MINE TO RULE. OPEN CALL TO ANDREW.**

**I am not ruling this, and the reason is not caution -- it is that ruling it either way would
adjudicate the scope of a standing sovereign word.**

The proposal is: `comp-learns-status` checks the served `computed_at` at read time; BEHIND = loud
banner, optional `--strict` nonzero exit. Zero new crons.

**It sits exactly on the moratorium's boundary, and both readings are defensible:**

| reads as PERMITTED | reads as BARRED |
|---|---|
| The moratorium's own carve-out: *"a finding still lands as a GATE or an OWNED BLOCKING ITEM -- that is unchanged."* `--strict` nonzero-exit **is** a gate. | Andrew's verbatim, same ruling: **"We don't need freshness checkers at this point."** This is a freshness checker by name and by function. |
| No cron, no SNS, no SES, no alarm, no notification machinery -- none of the moratorium's enumerated artifacts. | The moratorium is explicitly a **widening** rule; its own text says *"the narrow scoping is why it recurred."* Reading "no new resources" as permission is the narrowing it warns against. |

**And the fact that decides it is not in the moratorium at all: the estate DELIBERATELY TORE DOWN its
freshness machinery three weeks ago** (`858554332d`, 44 destroy, CTO GO). **Building a read-time
freshness check now would partially re-instate a capability that was intentionally removed.** Whether
that is a correct re-instatement or a quiet reversal of his direction is **his call, not mine.**

**Nothing is held behind this.** Item 1 and Item 3 proceed regardless; Item 2 is simply not built until
he rules. `0.8.0_AE_CloudComp` should **not** build it on this ruling.

**RECOMMENDATION IF HE ASKS FOR ONE:** the ordering in his own moratorium is *canonical routes and
schedules first, monitoring only once the thing being monitored is settled.* The COMPLEARN catalog is
**not settled** -- 40% of its partitions read a frozen file (§0). **A read-time freshness check built
today would report BEHIND on partitions that are frozen by design, which is the moratorium's exact
"measures the wrong thing precisely" failure.** Fix the frozen partitions first; then the question is
worth re-asking.

---

## 3. ITEM 3 -- the PRD text amend: **GO. RULED. Mine to land.**

The text is still live. `NFRA_COMPLEARN_PRD.md` §7 reads *"Each tick: refresh `tool_activity` from the
day's logs."* A cloud Fargate **cannot** refresh `tool_activity` -- three of its streams are
host-only, gitignored, and unreadable from a cloud runner.

**Amend to: "Each tick: READS the day's `tool_activity` catalog."** The landed architecture is the
correct resolution and the PRD text is simply wrong about it.

*Note for the record: the audit cites `:65`; the text now sits in §7 -- the file moved in 25 days.
The amend is still correct; the line citation is not. A line number without a vintage is not a
citation, and this is a live instance of it.*

---

## 4. WHAT I AM HANDING BACK, AND WHAT I AM NOT

| item | verdict | owner |
|---|---|---|
| 1. routing 6th partition | **GO** -- on corpus-coherence, new acceptance criterion, private read deleted in the same change | `0.8.0_AE_CloudComp` |
| 1b. extend the alarm | **DEAD** -- resource destroyed, rebuild barred | -- |
| 2. read-time BEHIND gate | **NOT RULED -- open call to Andrew.** Do not build. | Andrew |
| 3. PRD §7 amend | **GO** | `1.0.0_SA_CTO` (mine) |
| **NEW: frozen rolling_log partitions** | **surfaced, unowned** -- 2 of 5 partitions read a file frozen since 07-29 | routes to Andrew/COO |

**The new finding is not routed as a build and not gated.** It is surfaced because it is bigger than
the gap the audit was commissioned to find, and because **§2's recommendation depends on it** -- the
catalog is not settled, so it is not yet a thing worth monitoring even if Andrew permits monitoring.

**On the 25-day latency:** the audit was complete, correct, and actionable on 2026-07-13. It sat
because no seat carried the ruling. **Two of its three items decayed in that window** -- one option
became a destroyed resource, one premise became false. *A ruling owed is not inert; the substrate
moves under it, and the cost is paid by whoever finally reads it.*

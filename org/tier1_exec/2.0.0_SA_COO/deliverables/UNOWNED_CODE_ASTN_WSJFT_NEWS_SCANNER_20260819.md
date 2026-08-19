# COO carry: `tools/news_scanner` / `ASTN_WSJFT` is UNOWNED — the condition that generates drift rows

**Opened:** 2026-08-19 ~22:40Z by `2.0.0_SA_COO`, out of `0.8.0_AE_CloudComp`'s T4 declarations
census (@b1cd375c32), rows **L1** and **L2**.
**Recorded durably because a finding that lives only in a message is not carried.** I told two seats
I would carry this; this file is that carry.

## What the census found
| Row | Lambda | Divergence | Census owner |
|---|---|---|---|
| L1 | `news-ingestion-scheduler` | bundled copy of `tools/news_scanner/scripts/utilities/text_cleaner.py` diverged | `2.0.0_SA_COO` (routing — *lane ANY claims no owner*) |
| L2 | `news-trending-analysis` | bundled copies diverged, 2 members (`stopwords.py` sim **0.554**) | `2.0.0_SA_COO` (routing) |

`0.8.0`'s "lane ANY claims no owner" was **accurate**, and it was worth asking why rather than just
assigning a seat.

## THE CAUSE IS UPSTREAM OF THE DRIFT — the code itself is unowned
- **`tools/news_scanner`'s last 12 commits span SIX authors:** Andrew, `4.0.0_SA_CRO~SWEEP`,
  **`2.1.0_SA_COO` (a RETIRED serial)**, `2.0.0_SA_COO`, `1.0.0_SA_CTO`, `0.4.0_DT_ClientPlatform`.
- **`ASTN_WSJFT`** — the consumer project, `status: active` — carries **NO DECLARED OWNER** in its
  registry entry.

**So these rows had no claimant because there is nobody to claim them, not because the routing rule
was ambiguous.**

## Why I did not simply assign a seat and close it
**ASSIGNING A DRIFT-FIX OWNER WITHOUT AN OWNING PROJECT RELOCATES THE ORPHAN.** The bundled copies
would diverge again under the next six-author month, and the next census would route the same two
rows back to this desk — a loop that looks like work being done and is work being re-done.

**A retired serial appearing in the recent-author list is the tell:** contributions are arriving from
lanes that no longer exist to be held responsible for them.

## Disposition
- **REMEDIATION (the divergence itself) -> `0.7.0_AE_CloudOps`**, assigned on MECHANISM: they own the
  lambda deploy plane and the bundling that produced it. Queued explicitly BEHIND the mdpf feeder
  regression. Sent 223821Z.
- **THE OWNERSHIP GAP -> carried here, and routed to MSTR** as a registry act. **Deliberately NOT
  folded into a DRIFT row** — a row's remedy is "reconcile the copies"; this one's remedy is "name an
  owner", and collapsing them would file a structural gap under a cleanup label.

## The generalisation worth keeping
**A REGISTRY ENTRY WITH NO OWNER IS NOT A METADATA GAP — IT IS A GENERATOR.** Unowned code accretes
contributions from whichever lane happens to touch it, diverges from its bundles, and emits census
rows forever, each of which routes to a coordinator who can only re-assign it. **The census row is
the symptom; the empty owner field is the mechanism.**

Same shape as tonight's dead-seat TO class (`#42` at `0.5.0_AE_OpalETL~A`, 36 days): **work addressed
to nobody does not fail loudly — it accumulates quietly and reads as backlog.**

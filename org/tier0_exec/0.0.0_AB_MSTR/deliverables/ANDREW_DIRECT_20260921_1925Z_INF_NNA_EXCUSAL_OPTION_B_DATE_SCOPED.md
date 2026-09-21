# ANDREW-DIRECT 2026-09-21 ~19:2xZ at the 0.0.0_AB_MSTR terminal -- INF NNA stall: option (b), the date-scoped excusal

**Channel:** the 0.0.0_AB_MSTR terminal (laptop), a typed message.
**Recorded by:** 0.0.0_AB_MSTR, the same turn.

## VERBATIM

> **"(B) is good"**

## What it answered

MSTR relayed `0.7.0_AE_CloudOps~X`'s root cause and options (msg 99176; write-up
`org/tier2_senior/0.7.0_AE_CloudOps~X/deliverables/INF_NNA_351_1206_ROOT_CAUSE_20260921.md` @79cc430cba).

**The fact.** Orion reclassified one transfer between two accounts of the same client (household 18):
- txn 5835499, account 351, +120,000.00;
- txn 5833840, account 1206, -120,000.00.

It went from "Merge In/Out ... Other Account" to "Internal Account Journal In/Out", with editedDate
2026-09-05 20:28, after the 09-05 pull. This is the only type change among 1,473,605 txn ids.

**The two options put to him:**
- **(a)** Account-wide excusal of both accounts. This permanently strips the guard from 351, a live account.
- **(b)** Date-scoped excusal. Excusal entries gain an optional `partitions` list matched on
  (account, partition), and existing entries keep their account-wide meaning. This needs a small guard
  change plus tests. It excuses (351, 2026-09-04) and (1206, 2026-09-04), quoting the reclassification as
  the vendor raw fact (his 2026-07-23 standard).

## Ruling as stated

**Option (b).** Excuse exactly (351, 2026-09-04) and (1206, 2026-09-04) through a date-scoped excusal. The
account-wide excusal (a) is not taken.

This is Andrew's own ruling, so the excusal no longer waits on a CTO ruling. The excusal decider named in
the brief was the CTO.

## Surfaced, NOT adjudicated

- **Who builds and deploys the guard change.** `data/inf/scripts/gold/**` is the DS lane (POD4); Rule 13
  applies (commit, then QA-deploy via `safe-deploy`). `0.7.0_AE_CloudOps~X` committed the earlier message
  patch under a POD4 override on his in-session word. Routing is `1.0.0_SA_CTO`'s to make.
- **Proof.** The next scheduled ~11:32Z run is the acceptance. An ad-hoc QA run can come first, after
  which `pipeline-complete.json` is newly written, `header_metrics.json` shows a current `data_as_of`, and
  the alarm stays OK.

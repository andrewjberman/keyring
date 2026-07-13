# CVO — **THE 0-ROW ROSTER ROOT HOLE IS LIVE**, and the fix is **SIX COPIES, FOUR VERSIONS, ZERO GUARDS**

**agent:** 3.0.0_SA_CVO · **date:** 2026-07-13 · **severity:** **LIVE — can fire tonight**
**origin:** `0.4.0_DS_ClientPlatform~A` retracted his own "layer-1 is already closed" correction to me. I verified it.
**status:** root hole **OPEN**. Fix scope **quadrupled**. Verification target is the **deployed Lambda package**.

---

## The daily producer bypasses the guard everyone cited

`infra/aws/lambda/inf-pipeline/inf-accounts-v2-daily/lambda_function.py`:

```python
from convert_orion_api_to_silver import build_accounts_v2   # <-- NOT main(). The guard is never reached.
accounts_df = build_accounts_v2(snap)
_log(f"STEP3: accounts_v2 {len(accounts_df)} rows")          # <-- A WARN IN A LOG IS NOT A GATE
write_silver_api_dim_parquet(accounts_df, "accounts_v2", snap, upload_s3=True)   # <-- guards NOTHING
# then stamps:  {"status": "ok", "rows": 0}                  # <-- "ok" ON ZERO ROWS
```

The `main()` 0-row guard (`6010ea93a`, 2026-05-13) **protects the backfill path — the one path that is not the
daily producer.** `main()` was fixed; **the Lambda walked straight past it.**

**The roster feed is still advancing (partitions through 07-12). A 0-row roster can land tonight.**

## The fork — measured, all copies, explicit counts (no empty-output ambiguity)

| copy | sha | lines | raises | 0-row guard |
|---|---|---|---|---|
| `data/inf/scripts/silver/` | `5d90cae6` | 489 | 0 | **NONE** ← the REPO |
| `lambda/inf-accounts-v2-daily/` | `c3f08209` | 397 | 0 | **NONE** ← **THE DAILY PRODUCER** |
| `lambda/inf-silver-chain/` | `c3f08209` | 397 | 0 | **NONE** |
| `lambda/inf-api-positions/` | `ac92be04` | 257 | 0 | **NONE** |
| `lambda/inf-api-reps/` | `ac92be04` | 257 | 0 | **NONE** |
| `lambda/inf-api-txn/` | `16448610` | 257 | 0 | **NONE** |

> **FOUR distinct versions of one library across SIX copies. ZERO raises in any of them.**
>
> **A FIX IN `data/` TOUCHES NONE OF THE FIVE RUNTIME COPIES.** It would pass review, pass tests, land clean —
> **and protect nothing.** It would look *exactly* like a closure.

**This is the F7 shape: a guard the runtime never imports.** DS~A predicted it against his own work before I
measured it.

## Consequences for the fix

1. **The chokepoint is not one chokepoint — it is four, or it is none.** *A guard that must be pasted into N
   places is a guard with N failure modes*, and the next vendored copy inherits the hole silently. **Collapse
   the fork, or make the guard un-bypassable at the write boundary.**
2. **Verification is against the DEPLOYED LAMBDA PACKAGE.** Not a repo diff, not a commit hash, not a green
   suite. *Landing is not the property that matters; reachability from the runner is* — the same rule that
   just saved the hold-lift criterion, applied one layer down.
3. **The re-armed trio.** `INF_D_00c / INF_D_00d / INF_D_04` read **LATEST** with **no row guard**. DS~A's
   *"LATENT, not live"* rested on the root guard keeping `latest` non-empty. **That premise is dead → they are
   LIVE.** *His two "safe" conclusions were each load-bearing for the other* — the composition failure again.

## What still holds

My SEV, DS~A's `INF_B_00` walk-back, and my verification of it. **The walk-back now protects the served
holdings number even if a 0-row roster lands tonight** — so the fix I signed is doing more work than either of
us knew when I signed it. **That is luck, not design, and it is recorded as luck.**

## ⛔ I AM NOT TAKING VINDICATION ON LAYER-1

DS~A says I was right. **I was right about the REMEDY and wrong about my METHOD, and those do not cancel.**

I prescribed *"silver must NEVER write a 0-row roster"* **without ever opening silver.** His correction of my
method was **TRUE**, and **it stays on my record.**

> **A CORRECT CONCLUSION REACHED WITHOUT GROUNDING IS A GUESS THAT LANDED.**
> *A right answer held for a wrong reason is not knowledge* (COO, this morning).

Had he been right that the producer was closed, my prescription would have been exactly the **"blanket fix
across an ungrounded blast"** this fabric has spent the day punishing — the `INF_B_00` trap, where a blanket
fix *introduces* a defect into a correct script. **The gamble paying is not evidence that the gamble was
sound**, and a verifier who books a lucky call as a win has stopped being a verifier.

---

— `3.0.0_SA_CVO`

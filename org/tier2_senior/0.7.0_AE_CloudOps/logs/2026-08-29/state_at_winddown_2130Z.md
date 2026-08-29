# 0.7.0_AE_CloudOps -- STATE AT CONTROLLED WIND-DOWN (2026-08-29T21:30Z)

**archetype:** COORDINATE
**secondary_archetypes:** TRACE

Written on the Andrew-direct controlled wind-down (`0.0.0_AB_MSTR` 83940, sovereign, device
reboot). This seat is NOT one of the named leaders, so this is not a `/handoff save` block --
it is the narrower thing the instruction asks of every seat: the state a cold successor cannot
reconstruct. Committed, NOT pushed (publication is MSTR's final window).

---

## 1. WHERE I STOPPED, EXACTLY

**P2F-3b (composite-marker accelerator, TF) -- RULED BUILDABLE, NOT STARTED.**
`2.0.0_SA_COO` 83898 ruled the gate at 21:15Z and split it:

```
  BUILD the TF rows   -> UNBLOCKED, on the STATED contract. Start now.
  CLOSE P2F-3b        -> requires the accelerator EXERCISED against a REAL emitted marker.
```

The wind-down (21:29Z) arrived 14 minutes after that ruling. **I had completed the route
analysis below and had written no Terraform.** No `.tf` file is dirty; nothing is half-landed.

## 2. THE ROUTE IS DETERMINED BY MEASUREMENT, NOT BY PREFERENCE -- DO NOT RE-DERIVE THIS

A successor's obvious first instinct is an EventBridge rule on S3 ObjectCreated. **That route
is closed, and the reason is not discoverable from the TO.** Measured 21:2xZ:

```
  aws s3api get-bucket-notification-configuration --bucket opal-data-assets
      --query EventBridgeConfiguration            ->  null      (EventBridge NOT enabled)
```

Enabling that flag is **bucket-wide** -- S3 offers no prefix scoping on the EventBridge
enablement itself. `opal-data-assets` is the **THREE-FIRM** bucket (`blackdiamond/` alone holds
`49f/`, `49financial/` and `cottonwood/`). `1.0.0_SA_CTO` **refused that exact bucket-wide flag
at 83375**, and restated the constraint at 83907: anything that fires on the marker must be
scoped to `schwab/08335338/`, **never bucket-wide**.

>> **THEREFORE the sanctioned route is an S3 BUCKET NOTIFICATION, prefix-scoped** -- which costs
nothing new, because it is already the shape used 8 times in this bucket. Measured, all 8
prefix-scoped, none bucket-wide:

```
  silver-schwab-08335338   s3:ObjectCreated:*   Prefix=schwab/08335338/bronze/
  silver-schwab-08242234   s3:ObjectCreated:*   Prefix=schwab/08242234/bronze/
  silver-blackdiamond      s3:ObjectCreated:*   Prefix=blackdiamond/cottonwood/bronze/
  silver-eclipse / silver-orion / silver-etf-{divz,idvz,filepoint}   ... all */bronze/
```

⛔ **CTO 83907's warning names the shape the mistake will arrive in:** not "enable EventBridge"
but "add a trigger for the marker." A successor that reaches for EventBridge will be reaching
for the refused act without knowing it.

## 3. THE MARKER KEY -- CORRECTED, AND THE CORRECTION MATTERS

M-4 originally published a key with **no bucket**, and the obvious completion was wrong. On the
face @`8de15b7bb3` (`0.4.0_DS_ClientPlatform~V` corrected it at source after my 83895):

```
  BUCKET  opal-data-assets        silver_registry.py:46 ASSETS_BUCKET
                                  schwab_runtime.py:34  MONOLITH = env MONOLITH_BUCKET
  FULL    s3://opal-data-assets/schwab/08335338/meta/complete/date=YYYY-MM-DD.json
```

⛔ **The bucket is ENV-OVERRIDABLE (`MONOLITH_BUCKET`), so the consumer must NOT hardcode it
either** -- `~V`'s own note, and it applies to the TF as much as to the converter.

**Why this is worth a paragraph rather than a line:** I probed `opal-data-49financial` first
(the reading "for 49F" invites) and got a clean zero. That bucket holds exactly two top-level
prefixes, `_code/` and `gold/` -- **no `schwab/` tree at all.** An out-of-corpus zero and a
genuine absence are byte-identical, and this one would have been **permanent**: a consumer
polling that key waits forever and reports the producer late, daily, with no error anywhere.
Caught only by a positive control asking whether the prefix existed at all.

## 4. THE CLOSE CONDITION IS NOT YET SATISFIABLE

Measured 21:0xZ in the CORRECT bucket, with a working positive control:

```
  schwab/08335338/meta/  subprefixes : conversions/ , pulls/      <- no complete/
  meta/complete/         objects     : 0
  POSITIVE CONTROL meta/conversions/ : 480 objects                <- instrument works
```

`~V` 83923: **M-2 is BUILT but NOT DEPLOYED** -- "the emit changes a LIVE production converter's
WRITE SET", publication is the integrator's gated act. **The first real marker appears only
after that deploy.** So P2F-3b cannot CLOSE until that lands, regardless of when the TF is
written. ⛔ **Do not close on a hand-crafted marker written by this seat** (COO 83898, explicit):
the arm must consume one the producer emitted.

⚠ **`fact_rlw` will sit in `declared_not_written` on EVERY date** until that spec is resolved.
**Do not "fix" the permanently non-empty disagreement by dropping it from the declaration** --
which member is wrong belongs to the RLW feed's owner. A consumer that red-lights on a non-empty
disagreement will red-light daily; one that ignores it inherits the blindness the marker retires.

## 5. THE FLOOR HALF IS ALREADY LIVE -- DO NOT RE-APPLY

```
  advi-49f-gold-floor   ENABLED since 2026-08-19T17:32:28Z   cron(45 12 * * ? *) UTC
  target advi-49f-gold-dispatch ; flexible_time_window OFF ; never modified since
  TF: infra/aws/terraform/opal-assets/advi_49f_floor.tf:280
```

It sits on the **EventBridge SCHEDULER** plane, not the Rules plane -- which is why the TO read
`pending` for 11 days while the apply was already done. **A trigger census must sweep both
planes.** NEVER#4 holds: the accelerator is an accelerator only, never the sole trigger.

## 6. OTHER ITEMS THIS SEAT HOLDS, ALL BLOCKED ON NAMED OWNERS

| item | state | who holds it |
|---|---|---|
| BD calendar guard (`gold_dispatch.sh`) | committed, sentinelled BUILD-ONLY, **INERT by design** | needs a POD4 seat to land `lib/trading_calendar.py` into `data/black_diamond/scripts/gold/lib/` (sha256 41b1c0c12651c62e, 6,979 B), then observe the SKIP arm in a real gold-layer log, then CM entry + SERVE-RELEASE-ACK |
| freshguard-leg4 `Deploy`-field correction | **HELD** | Andrew -- the sovereign card quotes the entry's current text, so correcting it first would invalidate the card |
| P4-EDGEREAD-49F | **COMPLETE**, proof VALID rc=0 violations=0 | closed; bound stated -- CURRENT as of 2026-08-29T15:2xZ, expires if the edge changes before the flip |
| next 12:45Z fire | **WATCH** | 08-29 wrote 2 manifests vs the usual 4-6. "fewer changed dims" and "incomplete run" are DIFFERENT STATES and nothing yet distinguishes them |

## 7. FIRST ACT FOR A SUCCESSOR

1. Read this file's §2 before touching any trigger design -- it is the only record of why
   EventBridge is closed on this bucket.
2. Write the P2F-3b TF as a **prefix-scoped S3 notification** on
   `schwab/08335338/meta/complete/`, bucket read from config not hardcoded.
3. Do NOT apply until `~V`'s M-2 converter change is deployed and a real marker exists.
4. `.tools/safe-apply.sh`, never bare `terraform apply`.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | `'schwab_runtime' --files --all` | PASS | 140 hits / 130,427 files; located the converter surface |
| `comp-find` | `'advi-49f-gold-floor' --all` | PASS | 175 hits / 130,522 files; located `advi_49f_floor.tf:280` |

**What worked:** `comp-find`'s printed denominator + band split put the TF file in the HEAD band
immediately. **What failed:** nothing this window. **Gap found (unchanged from my 17:40Z log):**
no comp-tool sweeps the **EventBridge Scheduler** plane, which is how an 11-day-old floor stayed
invisible to a Rules-plane census. Same gap now has a second face -- no comp-tool reports a
bucket's `EventBridgeConfiguration` either, which is the fact that closed the accelerator route.

## Current State

Nothing deployed by this seat today. No TF written. No apply. Working tree clean of my work
after this commit. Push state: **LOCAL -- not pushed by me**, per 83940 (publication is MSTR's
final integration window).

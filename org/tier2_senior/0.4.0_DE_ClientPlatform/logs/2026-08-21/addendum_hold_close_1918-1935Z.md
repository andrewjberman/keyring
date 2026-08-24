# Addendum 1918-1935Z -- Andrew's two-condition hold fully expressed; and a positive control that validated nothing

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE
**serial:** 0.4.0_DE_ClientPlatform (base)
**window:** 2026-08-21 ~1918Z -> ~1935Z (close-out; delta since `addendum_s3_disarm_1730-1745Z.md`)

## The sovereign hold

**Andrew-direct 2026-08-21 19:18Z, VERBATIM** (relayed by COO): *"the position on flipping this should be held until source gaps and schedule are addressed, that needs to be documented, including relevant publisher resources, paths, and etc for the switch covering what is the current route and what is the contemplated route."*

Two conditions, **both required, neither sufficient**. The second — schedule — is one nobody had surfaced through an entire afternoon of nine seats verifying this chain at five planes. It surfaced because Andrew asked what we display on the daily schedule.

`clients-tab-slim` was my last `flip` row: it **clears** the source-gap condition (the one clean key of ten) and **fails** the schedule one. CTO ruled it HELD — his earlier stays-flipped ruling was made on the source-gap plane alone and before Andrew's word. Registry is now **FLIP 0 / HELD 14 / STRUCTURAL 1**; nothing prefers its twin.

## The near-miss: a positive control that validated nothing

I verified COO's schedule finding rather than taking it on report. My first two probes said COO was **wrong**:

```
aws events describe-rule --name advi-49f-publisher  ->  ResourceNotFoundException
aws events list-rules --name-prefix advi            ->  0 rules, on the only bus
```

Then the other API: `aws scheduler list-schedules` -> **`advi-49f-publisher  State=DISABLED`**. It is an EventBridge **Scheduler** entry, not an Events rule. COO was right throughout.

**The instructive part is the control.** To check that "0 rules" wasn't a broken probe, I ran `list-rules --name-prefix mdpf` and got `mdpf-feeder-accelerator`, ENABLED. **The control fired.** It proved the `events` API worked and that I could read rules from it — and proved nothing whatever about the question, because the question was never about that API.

**A control inside the wrong plane cannot detect a wrong-plane error.** It validates the instrument while the instrument answers a different question, and it makes the wrong answer look rigorous. **CTO and CVO hit the identical trap within the same minute.** Three seats, one API confusion, each holding a guard that could not fire.

Easy to miss for a second reason: the neighbouring `advi-49f-gold-floor` is ENABLED, so the 49F gold family looks scheduled at a glance.

## Sixth iteration on one comment

Reading the census *after* the commit (CTO's instruction, not the one I intended) exposed one more: state census said 15 rows, a row count said **16**. The 16th was the recipe's own first line, carrying the row pattern literally — exactly as two earlier versions carried a state literal. Fixed with a bracket expression so the line matches a row without being one.

Every census a seat might run now returns the truth or the one documented irreducible artifact (the type declaration, which *is* the type).

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `aws events` / `aws scheduler` | rule state, both APIs, plus a positive control | the near-miss above; correct answer only from the second API |
| `comp-keys prefix` | twin freshness | frozen 15:03-15:04Z, ~4h15m, measured not inferred from rule state |
| `comp-find` | `advi-49f-publisher` in `infra` | TF-declared at `advi_49f_publisher.tf:31` (desired plane) |
| `bunx tsc -b` | after each edit, **mutant control first** | rc=0 every time; mutant rc=2 every time |

## Blockers

None. Nothing pends at this seat.

## Current state

Portal DEV `3ade1aba`. **FLIP 0 / HELD 14 / STRUCTURAL 1**, row count 15 = the ruled P4E-1 denominator, census READ at HEAD after the act. Consumer-visible flips **zero**. `origin/PROD` untouched at `8a96c916`. Andrew's two-condition hold is fully expressed in the artifact — no row contradicts the sovereign position.

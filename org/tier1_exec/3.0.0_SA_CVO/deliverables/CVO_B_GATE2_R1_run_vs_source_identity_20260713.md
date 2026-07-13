# GATE-2 (CVO~B) — R1 is NECESSARY, NOT SUFFICIENT: the freshness assertion keys on the SOURCE, not the RUN

**Author:** `3.0.0_SA_CVO~B` (LD-0277 dedicated validation lane; gate-2)
**Date:** 2026-07-13
**Status:** CONFIRMED-BY-EXERCISE. Gate-2 determination on the round-8.2 F1 fix shape.
**Vintage:** all citations `@ HEAD 127e7dc0f`, `data/inf/scripts/gold/lib/aor_resolution.py` **UNCOMMITTED working-tree** (DS is authoring R1 as this was written — read it at that vintage, not at a later one).
**Fixture:** `aor_r1_run_vs_source.py` (this dir). Hermetic — stubbed S3, real lib, no prod touch, no gold run.

---

## 0. Credit, and what is new here

The **F1 inversion** (the rollback fails OPEN, not closed) is **base CVO's finding**, committed first at `b40d5cebe`. I derived it independently from a dispatch-level exercise before reading his message; convergent derivation, his priority. **This document is not that finding.** It is the next question: *does the fix now being written actually close it?*

**It does not close it. It narrows it.** R1 is real progress and must ship. It is not sufficient, and the residue is the same defect class in the same place.

## 1. What R1 does

DS's in-progress guard (`load_resolution`, R1 block): `expected = run_as_of()`; RAISE unless the resolution's stamped `as_of` set `== [expected]`. Deliberately an exact match — not wall-clock, not a tolerance window. **That reasoning is correct and I endorse it**: a wall-clock check false-raises on weekends and gets deleted by the third Saturday; a tolerance window is where fail-open hides.

## 2. What it does not do

**The guard asserts the resolution was built for THIS RUN'S SOURCE PARTITION. Its docstring claims it asks "was this resolution built FOR THE RUN I AM IN?" Those are the same question only if a source partition is used by at most one run.**

The pin is the latest accounts_v2 **partition** (`orion-gold-dispatch.sh:1296` — `aws s3 ls .../accounts_v2/ | tail -1`). It identifies the **source**, never the **run**. Every run sharing a partition shares a pin:

- a **same-day recovery run** (nightly full 02:05Z, then `--chain incremental` at 09:00Z);
- a **weekend/holiday** when the feed does not advance — **DS's own justifying comment concedes the pin repeats** ("the data legitimately does not advance");
- **any re-run before the next partition lands.** **LIVE RIGHT NOW:** latest partition = `2026-07-12`, today = `2026-07-13`. Every run today pins to the same `2026-07-12`.

On those runs the guard's two sides **agree with each other while the resolver never ran in this chain.** DS cites that self-agreement as the property that avoids false raises. It is also exactly what makes it blind. *A guard keyed on a value that repeats cannot distinguish "the resolver ran" from "a previous run's artifact is still sitting at the overwrite-latest key."*

## 3. Exercised (the arms, real lib, `INF_AOR_ASOF=2026-07-12`)

| arm | state | R1 | |
|---|---|---|---|
| A1 | artifact ABSENT | RAISED | ok |
| A2 | STALE, source **ADVANCED** (artifact 07-11, run pinned 07-12) | RAISED | **ok — R1 closes the partition-boundary rollback** |
| **A3** | **STALE, SAME partition** (earlier run today / frozen feed) | **RETURNED**, served `advisor_key=noel_soderblom` (**FOLDED**) on a switch-**OFF** run | ***FAIL-OPEN SURVIVES*** |
| A4 | FRESH, written by this run (control) | RETURNED | non-placebo — not a stuck RAISE |

**A2 and A3 diverge ⇒ the instrument discriminates. A4 ⇒ it can still pass.** This is the arm MSTR's acceptance bar demands: *a deliberately-constructed state on which gate-2 goes RED.*

**A3 is not a corner case — it is the shipping behavior of two chains.** Measured off the real dispatch (switch ON):

| chain | resolver `INF_A_0` | unconditional `load_resolution()` consumers |
|---|---|---|
| `CHAIN_COMPUTE` / `CHAIN_FULL` | present | 10 |
| **`CHAIN_INCREMENTAL`** | **ABSENT** | **5** — `INF_09`, `INF_D_00c`, `INF_D_00d`, `INF_D_00f`, `INF_D_02b` |
| **`CHAIN_GOLD_A`** | **ABSENT** | **2** — `INF_A_00`, `INF_A_01` |

`CHAIN_INCREMENTAL` **refreshes the resolver's own source** (`INF_API_SILVER_ACCOUNTS_V2`, step 7) and then runs five AoR consumers with no resolver. It moves the source and leaves the SSOT behind. The `:354` prepend touches `CHAIN_COMPUTE` **only** — these are separate literals it never reaches. (The scheduled nightly is safe: bronze-complete fires `{mode: full}` — `inf-pipeline/eventbridge.tf:237`, verified independently, not taken from self-report. The exposure is **recovery runs**, which happen exactly when things are already broken.)

## 4. Root cause

**`as_of` stamps the SOURCE PARTITION; the assertion needs a RUN identity.**

The design already knows this distinction and already got it right **once**: the event LEDGER is keyed by run timestamp — *"a NEW timestamped key EVERY run, NO fixed path → uncollapsible by construction."* The RESOLUTION is a **fixed key stamped with a value that repeats.** The guard inherited the weaker identity from the artifact it was bolted onto.

This is the **round-7 frozen-as-of collapse**, rebuilt at the new chokepoint — the exact class the SSOT refactor existed to kill, and the same axis as my own round-7 self-gap (I enumerated the date axis only over *advancing* values; the *frozen-repeat* value was where the defect lived). **It recurred because `as_of` was the only identity the artifact carried, so it was the only one the guard could ask about.**

## 5. Gate-2 determination — the remedy

R1 **ships** (it closes A2). It is **not sufficient**. Three items, all cheap:

1. **Stamp the resolution with a RUN identity and assert THAT.** The resolver already mints a per-run timestamp for the ledger event key — reuse it. Dispatch exports it at chain start (same mechanism as `INF_AOR_ASOF`); the resolver stamps it into the resolution; `load_resolution` asserts `stamped_run_id == this run's id`. This makes **every** resolver-skipped path loud — switch-OFF rollback, incremental/gold-* recovery, a resolver that no-ops or fails to land — including on a repeated partition. **A3 goes RED.** Keep R1's `as_of` check alongside it (they catch different things: R1 catches *wrong source*, run-id catches *wrong run*).
2. **F1 proper: make `INF_A_0`'s entry UNCONDITIONAL** — and note this is *not* redundant with (1): (1) makes a skip **loud**, (2) makes the skip **not happen**. Without (2), a run-id assertion turns every `--chain incremental` recovery run into a hard abort. **So `INF_A_0` must be added to every chain that carries AoR consumers** (`CHAIN_INCREMENTAL`, `CHAIN_GOLD_A`, and the `gold-*` variants), not just `CHAIN_COMPUTE`.
3. **Lift `INF_D_11` off the same conditional separately** (`dispatch:354`). A rollback currently drops the resolver **and the detector that would have caught the drop** in one flip. Do not let one conditional govern both. (Base CVO's (a).)

**Deploy-ordering trap in the F1 remedy itself** — `comp-pipescript deployed` (working-tree): `INF_A_0` = **`MISSING_ON_S3`**, `INF_D_11` = **`MISSING_ON_S3`**, all 10 consumers = `STALE`. The dispatch comment `:344-346` says the entry is gated *because the scripts are not deployed* — "an unconditional entry would fail the chain on a missing script." **So making the entry unconditional before the resolver is uploaded converts a silent fail-open into a hard nightly abort.** The unconditional entry MUST land atomically with (or strictly after) the resolver+detector upload. This is a release-mechanics precondition, not a code fix.

## 6. What gate-2 asserts, and what it does not

- **ASSERTED (exercised):** R1 closes A2; R1 does **not** close A3; the served key under A3 on a switch-OFF run is the **folded** one.
- **ASSERTED (measured off the real dispatch):** chain membership above; `CHAIN_INCREMENTAL` refreshes accounts_v2 and carries 5 consumers, no resolver.
- **NOT ASSERTED:** I have **not** exercised the full chain end-to-end through a real gold run (CLAUDE.md forbids ad-hoc gold runs to validate work; validation rides the scheduled nightly). The dispatch-level exercise drives the **real chain-assembly code path** and the **real consumer read path**; it does not execute the gold scripts. **Stated as an explicit gap, not blurred into a pass.**
- **NOT ASSERTED:** severity of the recovery-run exposure in production — the nightly is `mode: full` and therefore safe today. **Harm is NOT demonstrated. The gate's absence is the finding.**

**Gate-2 remains OPEN. Go-live WITHHELD.** Not because R1 is wrong — it is right — but because the assertion does not yet ask the question its own docstring claims it asks.

# CVO FINDING — R8-F1 INVERSION: the documented rollback fails **OPEN**, not closed

**agent:** 3.0.0_SA_CVO (base) · **date:** 2026-07-13 · **archetype:** VALIDATE
**Object:** gate-1 finding **F1** in `docs/briefs/advisor-of-record-go-live-gate-findings-20260713.md:53 @ 66f8f1e06`
**Priority: P0** — blocks the round-8.2 scope and the go-live release checklist. Route before DS builds round-8.2.

---

## Verdict

**F1's conclusion is right — the switch-only rollback is broken. F1's *mechanism* is wrong, in the
dangerous direction.** F1 predicts a **loud abort** (fail-closed, serve-stale). The exercised behavior
is a **silent freeze** (fail-open, serve stale attribution *as if current*), with the detector that
would have noticed removed by the very same switch.

A release checklist built on F1-as-written will assume a bad rollback announces itself. **It will not.**

---

## What F1 says vs. what is true

F1 (`:53`): under OFF, "the resolver drops from the chain → **the artifact isn't produced → consumers
RAISE → the nightly aborts**."

The middle step does not follow. `RESOLUTION_KEY` is **overwrite-latest** — a single fixed key, not
date-partitioned — and the documented rollback is **"flip only"** (brief `:29`). Nothing deletes the
artifact. So:

| State | Artifact | `load_resolution()` | Result |
|---|---|---|---|
| **A — pre-GO** (resolver never ran) | ABSENT | RAISES | abort. *This is the state F1 describes.* |
| **B — post-GO rollback** (resolver ran under ON, then switch OFF) | **PRESENT, STALE** | **RETURNS** | **silent freeze. This is the state the rollback actually occurs in.** |

F1 reasons about the rollback using **State A's** condition. The rollback happens in **State B**.

---

## Grounding

**SOURCE-CONFIRMED** (all `@ ee2780818`, both files clean at HEAD):
- `orion-gold-dispatch.sh:353-354` — `INF_A_0` (resolver) **and** `INF_D_11` (drift detector) enter
  `CHAIN_COMPUTE` only under `INF_AOR_FOLD_ACTIVE=1`.
- `lib/aor_resolution.py:52` — `RESOLUTION_KEY = 'gold/dimensions/aor_resolution.parquet'` (fixed key);
  `:10` — *"overwrite-latest like every dim"*; `:432` — the resolver writes that key.
- `lib/aor_resolution.py:232-251` — `load_resolution()` validates **only** readability, non-emptiness,
  and the presence of `account_id` + `advisor_key`. **It never inspects the `as_of` column it returns**
  (`as_of` is in `RESOLUTION_COLS`, `:59` — the field is right there, unread).
- 10 consumers call it unconditionally (`INF_A_00:235`, `INF_A_01:177`, `INF_B_00:734`, `INF_C_01:474`,
  `INF_C_07:406`, `INF_D_00c:451`, `INF_D_00d:660`, `INF_D_00f:815`, `INF_D_02b:319`, `INF_09:406`).

**APPLIED** (live, with a working positive control): `gold/dimensions/aor_resolution.parquet` does **not**
exist in S3 today — prefix listing of `s3://opal-data-inf/gold/dimensions/` returns 5 objects + an
`_aor_exercise/` prefix; control `accounts_dimension_latest.parquet` (48,428 B, 2026-07-10) reads fine.
*(My first probe used a non-existent control key and 404'd on both — uninformative; re-run with a real
control. Recording that because a 404-on-both would have read as confirmation.)*
⇒ We are in State A today, consumers SERVE-HELD. **F1's "NOT a current-state bug" is correct.**

**EXERCISED** — `org/tier1_exec/3.0.0_SA_CVO/deliverables/aor_f1_rollback_falsifier.py`, stubbed s3, no prod touch, three arms:

```
ARM 1  artifact ABSENT   (F1's assumed state)      -> RAISED   (RuntimeError)      [as-predicted]
ARM 2  artifact STALE    (post-GO rollback state)  -> RETURNED (as_of=2026-07-03)  [*** UNEXPECTED ***]
ARM 3  artifact FRESH    (control)                 -> RETURNED (as_of=2026-07-13)  [as-predicted]
```

Arms 1 and 2 **diverge**, so the instrument discriminates. A 10-day-stale resolution is accepted by the
SSOT chokepoint as indistinguishable from today's.

---

## Why it is worse than F1 states

Under a post-GO switch-OFF, **all three** of these happen together:
1. Consumers attribute every AoR view off a **frozen** resolution whose `as_of` never advances — and
   nothing checks `as_of`.
2. `INF_D_11`, the drift detector that would flag it, is dropped by **the same conditional** (`:354`).
3. `INF_D_10.aor_conformance.py` runs `--mode advisory` (`orion-gold-dispatch.sh:273`) — it cannot block.

The rollback removes the data guarantee **and** its detector in one flip, and serves.

---

## What the F1 fix does and does not close

Making `INF_A_0`'s entry unconditional (F1's remedy, already documented in-code at `:350-352`) is
**correct and necessary** — it fixes the **full chain**. It does **not** close:

- **`INF_D_11` is on the same line** (`:354`). If only the resolver is lifted out of the conditional,
  a switch-OFF still silently drops drift detection. Lift both, or rule explicitly on why not.
- **`CHAIN_INCREMENTAL` (`:361`) and `CHAIN_GOLD_A/B/C/D/CD` (`:365-369`) are separate literals** — the
  prepend at `:354` never touches them. They contain AoR consumers (`INF_A_00`, `INF_B_00`, `INF_C_01`,
  `INF_C_07`, `INF_D_00c/00d/00f/02b`, `INF_09`). **Any `--chain incremental` or `--chain gold-*`
  recovery run — even with the switch ON — executes consumers with no resolver in the chain, reading
  the stale fixed key. Silently.** Recovery re-runs are exactly what gets reached for after a bad
  night, so this is not a hypothetical path.
  *(Not a scheduled-nightly hazard: the INF cron and the bronze-complete rule both fire
  `mode = "full"` — `infra/aws/terraform/inf-pipeline/eventbridge.tf:174,271`.)*
- **The structural root: the SSOT read has no freshness assertion.** Every path that skips the resolver
  reads stale-but-valid and passes.

---

## Recommendations

**For CTO (P0, architecture ruling).** Put the freshness assertion **inside `load_resolution()`**
(`aor_resolution.py:232`) — the one function the design already elected as the chokepoint every consumer
inherits through (*"zero AoR logic lives at any call-site"*, `:233-237`). Assert the resolution's `as_of`
against the run's expected as-of (the resolver already pins `INF_AOR_ASOF`, `:382`), and RAISE with the
existing *"serve stale, not garbage"* semantics otherwise. One function, zero call-site churn — and it
converts **every** resolver-skipped path (rollback, incremental, group-stage recovery, a resolver that
silently no-ops) from silent-fail-open to loud-fail-closed. Without it, the release is one forgotten
`--chain` flag away from serving frozen attribution. **Ruling needed on the tolerance** (exact-match vs
N-day) — I am not specifying the policy, only that the assertion belongs at this chokepoint.

**For DS (P0, round-8.2 scope).** F1's fix as currently scoped (unconditional `INF_A_0`) leaves the
chokepoint fail-open. Recommend round-8.2 carry (a) the `INF_D_11` lift, (b) the vintage assertion per
the CTO ruling. Do not treat "resolver entry unconditional" as closing F1.

**For COO (P1, release checklist).** The checklist's rollback step currently inherits F1's assumption
that a bad rollback aborts loudly. It does not. The rollback leg needs a **positive** post-rollback
assertion (the resolution's `as_of` advanced), not merely "the nightly did not fail."

**For CTO~B / whoever holds gate-1 re-review.** The brief's claim at `:53` that *"DELTA-0-under-OFF is
thus unreachable via the dispatch"* is **false post-GO** — under OFF the dispatch runs fine and reaches
DELTA-0; it just measures against a frozen resolution. That sentence is precisely what makes the
fail-open invisible. Recommend it be corrected in the record.

---

## Consequence for gate-2 — my own instrument gap

F1 correctly notes my `~B` lane's DELTA-0 (0/871) was measured **resolver-direct**. That is right, and it
is worse than it reads: a resolver-direct harness always holds a freshly-written resolution, so it cannot
express the **"artifact exists + resolver skipped"** state at all. My PASS was structurally incapable of
seeing this. **The gate-2 re-verify must add an arm no existing instrument has:** run the resolver ON once
(artifact lands) → flip OFF → drive the chain **through the dispatch** → assert consumers RAISE. Today
they silently succeed. That arm is the F1 falsifier and it is the arm a resolver-direct instrument cannot
write. Falsifier driver: `org/tier1_exec/3.0.0_SA_CVO/deliverables/aor_f1_rollback_falsifier.py` (hermetic; promote into the gate-2
battery).

---

## What you should have asked but did not

**Is `as_of` load-bearing anywhere else it is carried but never read?** The resolution frame ships `as_of`
through `RESOLUTION_COLS` (`:59`), `STATE_COLS` (`:62`), and the event ledger (`:160`) — and the consumer
read discards it. The same class of defect (a vintage field present, plumbed, and never asserted on) is
what let the mdpf `ROLL_SOURCE_ABSENT` mislabel land, and what the round-8 date-axis re-open was about.
Before go-live, someone should sweep **every** AoR artifact for a carried-but-unasserted `as_of` — the
fix I recommend above closes the one at the chokepoint; I have not verified it is the only one, and I am
explicitly not claiming it is.

— 3.0.0_SA_CVO

# /self-drive AMGT_RESAPP -- tick 63 (2026-09-22 ~19:5x-20:1xZ), `1.0.0_SA_CTO~Z`

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260922_SELF_DRIVE_AMGT_RESAPP.md`,
cadence appended @`59491dd5f9` (30m -> every 3h on Andrew's ~18:4xZ word; job `26a36ae7`). **state: ARMED.**
Covers ticks 61-63 (61 and 62 were quiet by the delta rule; this one is not).

---

## STEP 0 -- SCOPE, SEQUENCE, INBOX

```
SELF-DRIVE SCOPE: AMGT_RESAPP -> 1 directive [D5] -> 1 project driven; 2 siblings in the same macro
  device: SITEZ (branch SITEZ)   register: D5 members [AMGT_RESAPP, AMGT_HARVST, +AMGT_CORPUS this tick]
```

**0.7 SEQUENCE** -- `sequence-check --project AMGT_RESAPP` at `55903c6259`: `UNPLACED -- a register project the
sequence does not list`, enforcement TRACK, 0 flags over a 0-project denominator. Unplaced means the directive's own
rules govern; nothing is waiting on a gate and nothing is held. **CAPACITY: 2 live COO lanes (`~Y`, `~Z`), no cap
ruled for this box**, against Andrew's 3-COO word of 2026-09-14 -- so a third lane is available and is what
`AMGT_CORPUS` will need.

**0.8 INBOX** -- 73 queued, **0 new since tick 62's last act** at the time of the read (the newest was the CVO's R5,
already executed). Three arrived DURING the tick and are handled below. Beside it, the order census:
**7 of 7 round-30 orders read `pending`** over a denominator of **184** orders in `task-orders/`.

⛔ **A WRONG-DOMAIN ZERO, caught inside this tick and worth the line.** My first census pointed at
`.../task_orders/` (underscore) and printed **`DENOM orders: 0`** -- a clean, confident, denominator-bearing zero
over a directory that does not exist. The real directory is `task-orders/` (hyphen) and holds 184. **It did not
look careless; it looked measured.** Rule 24's tell fired exactly as written: the denominator's scope was narrower
than the sentence beside it, and had I not re-located the path by `Glob` I would have concluded round 30 had no
orders at all.

---

## STEP 1-2 -- CALLS

**No open calls in scope pitched this tick.** The one governance fork of round 30 was closed at tick 62 (CVO R5
@`af2c1a673e`, this seat's REC of NO adopted). One card stands at Andrew, below; it blocks nothing.

---

## STEP 3 -- ACTS TAKEN (the driver's own lane)

### A. The AE seat that R5's route ends at DID NOT EXIST -- seated, and this is the tick's real finding

`get_agent_status("0.7.0_AE_CloudOps")`: **NOT REGISTERED**, latest logs 2026-09-14. `org/mcp/liveness.json`:
**6** registrations, all site-Z lanes, **no AE seat**. So the CVO's R5 routed `rk-122`'s commit and `safe-apply`
to a seat that was dark when the ruling was written -- **on the one act in round 30 with Andrew waiting**, and
nothing in the round would have said so: the worker stops at a row either way, and the routing hop would have
arrived at a dark inbox and read as delivered ("queued if not live" is a wish, not a delivery).

Spawned same-tick per the 2026-09-17 call-routing word: `.tools/spawn-agent.ps1 -Model claude-opus-5 -Effort high
0.7.0_AE_CloudOps` -> launched, audited in `org/mcp/agent-spawn-audit.log`.

**Seated the BASE serial, not a `~Z` lane, deliberately:** `2.0.0_SA_COO~Z`'s gate exercise (positive control,
quoted in my CTO half at `:55-56`) proved PERMIT for exactly `0.7.0_AE_CloudOps` and REFUSE for the COO lane, the
DT and the worker. A lane suffix I have not exercised against `owned-paths-validate.py` is an unmeasured grant --
and R5 exists precisely because nobody crosses that lane on an unmeasured basis.

**Confirmed live within the tick.** `0.0.0_AB_MSTR~Z` (msg, 19:53:34Z) had independently spawned
`0.7.0_AE_CloudOps~A` off my CTO half's text without exercising the grant, read my measurement as the better
evidence, and **killed its own duplicate** (PID 44356, no work done); base PID 6632 stands. The seat then reported
(msg 24361, 19:59Z): registered, watcher armed, **both never-widen halves and the order read**, its plan bound
stated back BEFORE the patch (one `+ ordered_cache_behavior`, zero removed, `spa_fallback` absent; a 2-resource
plan admitted only with a printed field-by-field WAF diff; a missing `viewer-request -> auth-validator-edge`
association is a REFUSAL, not a warning), and `.open_deploys/` censused across **33 live worktrees** with
`amgt-rk122-edge-behavior` ABSENT from all 33. It is standing by and has committed nothing.

⭐ **Its WAF limb is stronger than my signed half's and I adopt it:** my half made "any WAF rule content moved" a
rollback trigger; it will PRINT the field-by-field diff rather than assert the no-op.

### B. `AMGT_CORPUS` registered (L3) and given its endpoint and PRD (L2+L4)

On Andrew's ~18:2xZ word. Three carriers, all in this seat's own commits (Rule 27):

| act | commit | evidence |
|---|---|---|
| L3 registration | `7cedd1fd9d` | tree row + generated index entry + D5 members line; `missions-tree-index check`: tree=25 under 9 directive folders, 25 valid, flat index 374 rows (25 generated, 349 hand-written, 0 parse errors), **0 violations**. MACROS.yaml needed NO edit -- `AMGT` already charters the corpus |
| L2 endpoint + L4 PRD v0.1 | `03918b5b3e` | 9 outcomes, 12 contracts, 12-row manifest, 5 substrate cards; `[prd-manifest] OK` |
| L4-R routed | msgs 24367 / 24368 | `prd-signoff status AMGT_CORPUS` -> **WITHHELD**, both halves MISSING, owed by `3.0.0_SA_CVO~Z` and `4.0.0_SA_CRO~G` |

**The endpoint's derivation is a printed SUBTRACTION, not a forward list** (Rule 24): over the brief's 13
outcomes -- 7 wholly the AMGT_RESAPP addendum's, 4 split across the seam, 2 wholly here, 1 minted (FWD-9,
read-only, because a constraint nobody exercises is a belief). **13 -> 9 FWD.** I asked the CVO to run the
subtraction the OTHER way, from the brief's list against both endpoints, because the failure mode here is a
green: an outcome that lands on neither side of a split reads as covered by the other project and nothing fails.

**No FWD is a wait** -- the corpus is a static local library and every outcome is provable by a run a seat starts.
**No address is typed** (Rule 30: the manifest names builder ARGUMENTS; the cell prints `address()` output).
**The driver is UNSEATED by design** -- a third COO lane is asked of MSTR at the L4->L5 handoff, not before.

---

## STEP 4 -- COMPLETION TEST

**NOT DONE.** `AMGT_RESAPP` reads `status: active`, `dep_stage: EXECUTING` -- **0 of 1 project complete**. Round 30
is mid-flight: 7 of 7 orders pending, 5 worker branches live (`wk-amgt-30-116/117/120/121/122`), **all 0 commits
ahead of SITEZ** at `19:48Z`. No L8 packet, no slug and no round-30 analysis is owed by any seat yet.

The scope gained a sibling this tick (`AMGT_CORPUS`), which does **not** enter this loop's completion test: the
selector is the project `AMGT_RESAPP`, not the directive. If Andrew wants the loop widened to D5, that is his word
and it changes the denominator.

---

## CARD STANDING AT ANDREW (carried from R5; blocks nothing)

The CVO's second-order item, verbatim in intent: a task order's `<paths>` clause **admits a worker by order alone
and prints no lane**. Narrow remedy: admit a `<paths>` entry only where the ISSUING seat's lane admits it. That
remedy's cost: an order spanning a lane boundary must be cut or co-signed by a seat holding the lane. Nothing is
blocked while he decides -- R5 already routes this instance's act, and the CVO built no gate.

---

## Compiler Tools

`sequence-check.py` · `missions-tree-index.py derive --write` + `check` · `prd-signoff.py status` ·
`spawn-agent.ps1` · `safe-commit.sh -F` (message files authored by the Write tool) · `check_inbox` /
`get_agent_status` / `send_message` / `ack_messages` · `Glob` (the instrument that caught the wrong-domain zero).

**state: ARMED.** Push state: LOCAL at write time; no `ls-remote` read taken this tick.

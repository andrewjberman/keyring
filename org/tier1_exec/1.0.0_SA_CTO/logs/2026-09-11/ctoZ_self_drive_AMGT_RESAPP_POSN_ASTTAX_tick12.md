# 1.0.0_SA_CTO~Z -- /self-drive AMGT_RESAPP & POSN_ASTTAX, tick 12 (post-reboot re-arm)

**state:** `ARMED` · **cadence:** 30m, cron `254949d7` (`7,37 * * * *`) · **covers:** tick 12 only
(ticks 1-11 ran pre-reboot; last tick log @`17e1966cff`)

The loop died with the device at the 2026-09-11T14:10:36Z reboot and was **RE-ARMED off the
`org/XXX.md` carrier clause @`0fb2a1f0b0`** -- Andrew-direct, UNSTRUCK, stop-condition unmet. Per
s.0.4 that clause is the only thing a successor may re-arm from, and per s.0.5 it gates tick 1: the
carrier was already committed, so the tick was allowed to run. Recorded pre-reboot as SUSPENDED BY
REBOOT, never `STOPPED-BY-OPERATOR` -- Andrew stood down the DEVICE, not the scope.

> ⚠ **ONE TENSION, RESOLVED AND STATED RATHER THAN ABSORBED.** The relaunch instruction carried
> "ZERO crons at launch, every serial -- loops are operator-initiated" alongside a per-seat line
> reading "Event-driven via the inbox Monitor; /fabric-check + /stimulus-scan on signals, not
> timers." That same instruction names `org/XXX.md` Step 1b-F as **the only source of truth** for a
> live scoped loop authorization, and the carrier clause lives there, is Andrew-direct, and is not
> struck. So the cron was armed. **If 0.0.0_AB_MSTR~Z or Andrew intended the narrower reading, say
> so and this seat runs `CronDelete 254949d7` and goes event-driven** -- flagged in the open rather
> than decided silently, because a loop armed on a misread is exactly the standing-loop debt the
> NEVERs describe. Note the literal token "1b-F" does not appear in `org/XXX.md` (enumerate: 0 hits
> over 432 lines); the loop-arming rows are at lines ~290-326 and the clause for this scope is
> line 325.

## SCOPE

```
SELF-DRIVE AMGT_RESAPP & POSN_ASTTAX -- tick 12 (2026-09-11 ~15:3xZ)   state: ARMED
SCOPE: 2 project(s) -> AMGT_RESAPP (D5), POSN_ASTTAX (D4)   device: sitez   (denominator: 2 of 14 live directive rows touched)
COMPLETION TEST: NOT DONE -- 0 of 2 projects status:complete (both read `active`, dep_stage EXECUTING)
```
Device guard PASSED: `agentbus-sqs.sh device` = `sitez`, basis workspace path. Both directives are
SITEZ-placed (D4 Positioning, D5 Asset Management), so no cross-fabric refusal applies.

## OPEN CALLS IN SCOPE

**0 adjudicable, 0 reserved.** Andrew cleared all four AMGT_RESAPP calls at ~12:1xZ pre-reboot; no new
call arose this tick. Per the skill's zero-calls branch, no empty pitch was sent to the CVO.
The s.2 **CVO-DARK branch fired and then cleared inside the tick** -- see below. No calls were held,
so no `state: HELD` rows were appended to the verdict ledger.

## THE TICK'S SUBSTANCE: a dark critical path, found and cleared

**At tick start `3.0.0_SA_CVO~Z` was DOWN and was the SOLE gate on the whole AMGT_RESAPP scope.**
Measured on TWO INDEPENDENT INSTRUMENTS before reporting (Rule 22 -- a second read by the first
method is repetition, not corroboration):
- BROKER: `get_live_agents` = 5 rows, no CVO; `get_agent_status("3.0.0_SA_CVO~Z")` = NOT REGISTERED.
- OS PLANE: process table held 6 `inbox-watch.sh` streams, none for the CVO; zero CVO processes.

⚠ **THE OS INSTRUMENT HAS A BLIND SPOT THIS SEAT DID NOT KNOW AT THE TIME, recorded because the
verdict happened to be right and the reasoning happened to be incomplete.** A **codex** seat does not
run `inbox-watch.sh` at all -- it runs a bridge/detector pair. So "no `inbox-watch.sh` for the CVO"
is NOT evidence of a dead codex seat; it is the normal state of a live one. The verdict was correct
only because the broker independently said NOT REGISTERED. `4.0.0_SA_CRO~Z` closed a second grain
this seat had left open by querying the BASE serial `3.0.0_SA_CVO` explicitly (also NOT REGISTERED).
**For a codex seat the live grain is its runtime dir** -- `0.0.0_AB_MSTR~Z` used
`.runtime/codex-seats/<serial>/` file mtimes plus a growing `turn-bridge.stdout.log`.

Acts taken, in order:
1. **Escalated the hole to `0.0.0_AB_MSTR~Z`** (spawn is not this seat's -- `/mstr-spawn` is scoped to
   MSTR and COO), with the measurement and the reason no workaround exists: Rule 27 gives the
   ratified-text half to `3.0.0_SA_CVO` ALWAYS; only the BRIEF half may re-route, and it was already
   signed.
2. **Resolved the ambiguity that could have de-prioritised the spawn.** Read the relaunch record
   @`c00e5ee902`: its own roster table names FIVE seats and `3.0.0_SA_CVO~Z` is the fourth row, so
   the relaunch was ALREADY ORDERED by Andrew's word and was never a sovereign call. Withdrew the
   conditional park this seat had offered, and handed MSTR a ready-to-paste briefing (that seat has
   NO log of its own -- the one seat of five that never wrote one).
3. **Corrected the record.** @`c00e5ee902` said the CVO's owed acts are carried elsewhere "so nothing
   waits on it." False at the artifact: the L4-R gate read WITHHELD with two live seats parked
   behind it. `2.0.0_SA_COO~ZZZ` routed the identical correction independently; `0.0.0_AB_MSTR~Z`
   accepted it without reservation and is striking the line.
4. **When the seat came up parked on a STALE instruction**, relayed Andrew's superseding word
   VERBATIM (@`c00e5ee902`, "bring them back and get that device up to speed") and restated both
   obligations in full -- deliberately, because this seat's 20260911T131959Z send carrying them was
   still unread in that inbox. **Relayed, not adjudicated:** the seat reached its own conclusion and
   lifted its own park, which is the correct shape.

## VERDICT RECEIVED AND ACTED ON: the L4-R REFUSE

`3.0.0_SA_CVO~Z` REFUSED the AMGT_RESAPP v0.4 ratified-text half via the canonical stamp
@`1ec5ade3f5`; review `.../AMGT_RESAPP_v04_RATIFIED_TEXT_REVIEW_20260911_Z.md`@`cfaa24b7b8`.
Operative sentence, not paraphrased: *"L4-R forbids annotation, history or seat name inside the
ENDPOINT section, from its heading to the next heading."* Four contaminated regions named (67-69,
214-217, 220-228, 230-236).

**Acted the same turn -- amendment @`371286cf78`:**

| half | before | after |
|---|---|---|
| ratified-text | `f576e011be53` | **`8d2ae62e9834`** (moved, intended) |
| brief | `a5517057d99f` | **`a5517057d99f`** (UNCHANGED across all three edits) |

⭐ **THE DESIGN CHOICE: the removed history went to the PRD PREAMBLE, not to s.7 PROVENANCE.**
`half_of_section` returns `None` for pre-heading text, so the preamble is in NEITHER half. s.7 is a
BRIEF-half section; moving the same text there would have re-opened a half `4.0.0_SA_CRO~Z` had
already signed correctly and cost that seat a gratuitous re-sign cycle. Nothing was lost by removing
the attribution: the L2 pin @`3bc8f5f2c4` was already carried in the preamble's own table row.
Operative content preserved: 15 of 15 FWD cards verbatim, and the L5 bar ("no cell may claim an
EXERCISED outcome REALIZED on the strength of its own artifact"; "grade the DONE WHEN state line")
survived -- only the narrative wrapped around it moved.

⛔ **THE REVIEWER FOUND WHAT THE AUTHOR'S SELF-READ DID NOT, and that is the whole point of the
second signature.** This seat pre-reviewed its own half and DISCLOSED one contaminated region before
the CVO read it. The section had FOUR. The review closed: *"removing the incident block alone leaves
the seat name embedded in FWD-15's SOURCE and the attribution above the cards. Recheck the whole
section boundary, rather than only the disclosed blockquote."* The disclosure was still worth making
-- it was consumed explicitly ("including the disclosed ENDPOINT annotations") -- but **a
self-disclosure is not a self-certification, and the gap between one and four is the measurement.**
The reviewer ALSO caught a stale count the author had carried for a full version: the L5 bar read
"Thirteen outcomes" while the section holds FOURTEEN `EXERCISED` (15 total, `FWD-9` alone `APPLIED`).
Corrected. The neighbouring "like the other thirteen" was checked, is correct, and was left alone.

**Verification built so it could fail:** 6 contamination patterns over the 156-line ENDPOINT section
-> **0 hits**; POSITIVE CONTROL, identical patterns over the preamble now holding the history ->
**19 hits**. The zero is a measurement, not a silently broken matcher.

## SCOPE STATE

| project | status | dep_stage | L4-R | task orders | blocked on |
|---|---|---|---|---|---|
| AMGT_RESAPP (D5) | `active` | EXECUTING | **WITHHELD** -- ratified-text OWED BY `3.0.0_SA_CVO~Z` (live) at `8d2ae62e9834`; brief SIGNED current | 28 of 28 terminal, 0 open | CVO delta review, then r4 L8/L9/L10 |
| POSN_ASTTAX (D4) | `active` | EXECUTING | **ADMITTED** -- both halves signed at current bytes | 8 files: **2 complete, 6 `staged`** | `2.0.0_SA_COO~Z` to un-park round-2 wave 2 |

⚠ **POSN_ASTTAX carries SIX `staged` task orders, not the four the pre-reboot log predicted** for
wave 2. Surfaced, not acted on -- un-parking is `2.0.0_SA_COO~Z`'s act and that seat is LIVE and has
declared it is resuming POSN per its own pre-reboot log @`23783dd2b6`. Not escalated; it would be
this seat reaching into the COO's lane on a delta that seat can see.

⛔ **CARRIED FORWARD, UNCHANGED, because losing it is the expensive outcome -- `C-RETAG-SAFETY`.**
Fixed-key dicts `management_allocations {'active','passive'}` and the asset_class chain
`{cash, fixed_income, equity, hedge}` raise `KeyError` in `calculate_allocations()` and **blank the
page for all four partner firms.** NOT latent: VXX is already held, so the next generator run after a
retag fires it. **Order is load-bearing: (0) harden the generator, (1) fix management_style,
(2) verify the asset_class chain, (3) THEN retag.** Note `TO-S2-1.retag-the-hedge-bucket` sits in the
staged set -- step (3) -- so the ordering is live, not theoretical.

## ROUTED AND CLOSED WITHOUT MANUFACTURING WORK

`3.0.0_SA_CVO~Z` asked that a startup-parity FAIL (`ont-rulebank-version-current`, "source 1.8 marker
absent in all four required representation files") be routed to its owner. **No routing is owed --
it is already dispositioned, by this seat.** Cycle-27 ruling
(`org/tier1_exec/3.0.0_SA_CVO/logs/2026-07-25/cvoz_sysparity_cycle27_ont_rulebank_version_current.md`):
*"the FAIL is correct; its STATED REASON is FALSE"* -- the marker is ABSENT from the four files, not
STALE, measured then at `meta.version` 1.2 with 8 of 8 representation sites current and ZERO stale.
The CVO's own lane log of 2026-09-10 (cycle159) already records it as dispositioned and instructs
against manufacturing work off it. Real closure is `NFRA_SYSPARITY.DENOM` item A at
`0.8.0_AE_CloudComp`. Not a gate on anything in scope.

## OPEN AT ANDREW

**0 calls.** Nothing in this tick is sovereign-class. The one item this seat would flag if asked is
the loop-arming tension quoted at the top, which is `0.0.0_AB_MSTR~Z`'s to settle, not Andrew's.

## NOT DONE, AND WHY -- stated so the next tick does not rediscover it

`0.0.0_AB_MSTR~Z` routed a real tooling defect here (msg 21409): `spawn-agent.ps1` has **no codex
branch at all** -- measured, 304 lines, ZERO occurrences of "codex" or "ajb2" -- so it always runs
`ajb -Headless`, and a codex seat on a space-containing checkout **cannot be relaunched by the
standard primitive and fails SILENTLY** (right command line, right marker, zero children; three
failed attempts tonight). The 8.3-short-path guard already exists and is documented in that file's
own comments at lines 233-240, but only on the `wt` transport; the real codex launcher is
`org/mcp/start-codex-seat.ps1`. **Accepted as this seat's surface and STARTED, then set down when the
L4-R refusal landed** -- the refusal was on the critical path and the tooling defect is not.
It is NOT forgotten and NOT blocked: it is the next substantive act at this seat once the delta
review returns. Two hypotheses are already DISPROVEN and must not be retried: codex not resolving
under `-NoProfile` (FALSE), and the wt-vs-Start-Process transport (FALSE).

## Compiler Tools

`comp-read --enumerate` (XXX.md carrier clause; PRD section census; `spawn-agent.ps1` codex census)
· `comp-find --name` / content (codex launcher discovery, 58,145-file denominator; parity-finding
owner, 83 hits/56,080 files) · `python .tools/prd-signoff.py status` (both projects, read three
times: before, at the moment of acting, and after the amend) · `prd_signoff_lib.half_hashes`
(before/after on BOTH halves -- the instrument that proved the brief half never moved) ·
`.tools/directives-check.py --json` (scope resolution, 14 live rows) · `.tools/agentbus-sqs.sh
device` (device guard) · `.tools/safe-commit.sh -F` (msgfile authored by the Write tool, per Rule
14a) · `git ls-remote` + `git branch -r --contains` + `merge-base --is-ancestor` with a positive
control (push state) · `get_live_agents` / `get_agent_status` / `ack_messages` (READ clock: 21397,
21401, 21405, 21409).

**Push state:** LOCAL, MEASURED. `git ls-remote origin refs/heads/SITEZ` = `603dd7e700`;
`git branch -r --contains 371286cf78` returns EMPTY; local is 5 commits ahead. `0.0.0_AB_MSTR~Z`
pushes origin/SITEZ and Andrew authorized SITEZ tonight -- this seat does not push.

# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-20 2225–2300Z

**archetype:** MEASURE + BUILD
**Projects:** W-B floor question (D7 TICKET LIFECYCLE v2) · gateway `$select` (CTO~Z ruling 3399)

## Summary

Two ruled items, both closed. **The 30-second schedule is REFUTED, not merely unestablished** —
measured on all three planes with controls. **The `lastModifiedDateTime` build landed** @90d526c199,
mutant-controlled. And I **landed a false claim in the gateway README and corrected it four minutes
later** — the most instructive thing in this window and the only one that cost anyone else time.

## 1 — The sub-minute floor: REFUTED, three planes, three paths

2.0.0_SA_COO~Z found the CLI floors at one minute and correctly declined to assert the engine.
1.0.0_SA_CTO~Z measured `New-ScheduledTaskTrigger` ACCEPTING PT30S and correctly labelled it DESIRED.
I hold the intake lane on this box, so I ran the exercised-layer test.

| Plane | Call | Result |
|---|---|---|
| DESIRED | `New-ScheduledTaskTrigger -RepetitionInterval 30s` | OK, object carries `PT30S` — CTO~Z reproduced exactly |
| APPLIED | `Register-ScheduledTask` with that same object | **REFUSED** — `(7,27):Interval:PT30S` |
| EXERCISED | — | unreachable **by construction**; nothing was stored to fire |

**The two measurements compose rather than conflict.** `New-ScheduledTaskTrigger` is a local object
constructor with no connection to the scheduler service — structurally an instrument that *could not
have refused*. Naming its layer unprompted is why this resolved in one hop.

**Controls:** positive at 60s (both steps pass, so the refusal is the VALUE not the method) ·
adjacent value PT59S also refused (a sub-minute floor, not a PT30S quirk) · independent path
`schtasks /Create /XML` also refused, at *different* error coordinates — two distinct XML documents,
one validator, so the constraint is the **service's** · readback of PT1M returns `PT1M` · probe XML
mirrored the live task including `UseUnifiedSchedulingEngine=true`.

**EXERCISED at the established floor** — nobody else had this: PT1M fired 18:32:06.20 / 18:33:06.19 /
18:34:06.22 / 18:35:06.29 → deltas **59.99 / 60.03 / 60.07s**. Without it, "1-minute is established"
would have been an APPLIED-only claim wearing an EXERCISED label — tonight's error with a friendlier
number.

**And the failure mode is the good one:** it refuses loudly and names the value. COO~Z's feared silent
round-up does not happen.

**Consequences carried:** the 30s row leaves the table; CTO~Z's "margin ≈ the wake hop" sentence is dead
and cannot be revived from a rediscovered PT30S acceptance; ratio is ~4:1 under both arrival models;
**3.0.0_SA_CVO~Z's reopening trigger had to move from ~15s to ~45s** — a trigger set too low permanently
forecloses, which is the failure it was written to prevent. Offset-tasks workaround named and **refused
on correctness** (two unsynchronised writers to one unconditional-`put_item` cursor;
`MultipleInstancesPolicy: IgnoreNew` guards within one task, not across two).

**A contamination in my own apparatus.** My positive control pointed at the same probe script, hence the
same log, as the primary measurement. The merged log reads `59.99, 60.03, 26.47, 33.60` — a 26s and 33s
delta on a task registered at PT1M, i.e. **a fabricated confirmation of the exact hypothesis under test**.
Saved by phase, not care (four entries at `:06.2x`, one at `:32.69`; the `:06` series predates the
control). *A control that shares an output artifact with the thing it controls is not a control, it is a
second unlabelled input.*

## 2 — Gateway `$select` build @90d526c199

Two tokens, two message readers, per ruling 3399. AST verifier resolves all 23 `$select` literals and
exact-compares both targets: PASS/PASS, denominator unchanged. **Mutant control** (drop the trailing
comma → literals glue) FAILS with `createdDateTimelastModifiedDateTime` — a valid Python string and a
syntactically valid `$select`, so it raises nothing locally and would surface only on the box, later, to
someone else. Run on a copy. Gate rc=0, 0 non-ASCII added.

Corrected my own number that the ruling quoted: **SIX `$select`s, not seven** — L207 is a *response*
projection, not a `$select`. I counted token occurrences and reported them as projections.

Not deployed and not deployable here: no process runs from `infra/aws/ec2/opal-gateway/`, checked rather
than assumed, so unlike the intake runner **saving this file is not deploying it**.

## 3 — The false claim I landed, and the four minutes it lived

`f3c1ccbe20` asserted `/opt/m365-mcp-gateway` was still the on-box path and reaffirmed the README's
retained list as accurate. **Both false.** The 08-15 cutover removed that tree (142 MB, S6-15, 0332Z) and
deploys to `/opt/opal-gateway`; final census `0 m365 across 14 surfaces`. Corrected @`bbb6f2529d`.

Two independent defects, and only one is mine:
- **The record trap (blameless):** a *correct* citation of the 07-31 record, line 82, which a later closed
  record superseded 15 days on with no back-annotation. *The more precisely you cite, the more confidently
  you are wrong.* Banked by two other seats already.
- **The banner (mine):** I stamped "Measured at HEAD, not inferred" over a set where the three repo-side
  claims were real filesystem reads and the on-box one was lifted from prose. **One evidence banner over
  two evidence classes** — the measured neighbours lent authority to the unmeasured one, and the banner
  told the reader not to check. Written as two lists it would have been visibly unsupported *as I wrote
  it*. Banked: `memory/one-evidence-banner-over-two-evidence-classes.md`.

**The consequence inverted the purpose**: written to stop an applier hunting a dead directory, it would
have sent them to one — durably, in a README. Caught by 2.0.0_SA_COO~Z checking *before* their write while
mine was already landed. **That is scheduling luck, not a control.**

What *was* real and survives: the README's top block genuinely is obsolete (the whole live plane renamed,
not three items), and COO~Z's decoy-tree finding — `infra/aws/ec2/m365-mcp-gateway/` exists untracked,
holds no `tools.py`, and is invisible to `comp-find` because it is gitignored.

## 4 — Risk-reflex defect (routed, not built)

Two commits, **ten HOLDs, zero real**. It resolves claims by **basename** and fans them out to every repo
file sharing it: `tools.py` (7 collisions, 4 vendored pydantic, 1 phantom) then `README.md` (collides
estate-wide). Both citations were sentences that merely *mention* the filename — one was a `PASS` row —
against a banner reading "the estate has WRITTEN WARNINGS ABOUT" this node.

**The false HOLD did not merely waste time, it manufactured a finding**: I read the citation, it sent me
to a PASS row, and I built the §3 error on top of it. Withdrew my earlier staleness hypothesis — the
rename landed 08-14, six days before the 21.5h map. The fix is path resolution, not less alerting.

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| `comp-find "opt/m365-mcp-gateway"` (gateway tree) | DENOMINATOR 1 hit / 71 files, band DOC | PASS |
| `comp-find` vs the untracked decoy tree | **CANNOT SEE IT** (gitignore-aware) — COO~Z's finding, a real blind spot for stale-tree hunting | LIMITATION NAMED |
| rail gate on a `grep` under `infra/` | DENIED a README grep (fires on `infra/`, not just `.tf`); rerouted to `comp-find` rather than marker-overridden | GATE CORRECT |
| AST `$select` verifier + mutant | 23 resolved, 2 exact-match PASS; mutant FAILS on the glue | CONTROL FIRED |
| Scheduled-task probe, 3 paths + 3 controls | PT30S refused 3/3, PT1M accepted + honoured 59.99/60.03/60.07 | PASS |
| My own probe apparatus | control shared an output file with the measurement | **CONTROL FIRED ON MYSELF** |

## Operational

Zero crons armed, per the launch term. Scratch tasks enumerated before (2) and after (0); live
`OPAL_D7_ticket_intake` re-read after cleanup — still `PT5M`, command unchanged, never touched. **Nothing
here authorizes changing the runner's cadence**; option (ii) remains a recommendation in front of Andrew.

`MEMORY.md` lines 51/52 are a near-duplicate pair from two seats on the same lesson (the record-snapshot
trap) — flagged, not folded, since both were written minutes ago and may still be in flight.

## Blockers

None at this lane. W-B's transport is dropped on CTO~Z's recommendation (semantics kept, re-cut is
COO~Z's). The `$select` change waits on the laptop's next gateway touch, batched with S2's half — one
boot test. A1 still waits on real channel traffic.

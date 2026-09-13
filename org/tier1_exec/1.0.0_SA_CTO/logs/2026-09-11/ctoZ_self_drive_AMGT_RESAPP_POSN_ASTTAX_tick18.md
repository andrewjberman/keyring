# 1.0.0_SA_CTO~Z -- /self-drive AMGT_RESAPP & POSN_ASTTAX, ticks 17-18

**state:** `ARMED` · cron `254949d7` · covers ticks 17 and 18 (tick 17 wrote no log; its finding is here)

```
SELF-DRIVE -- tick 18 (2026-09-11T18:43Z)   state: ARMED
OPEN CALLS IN SCOPE: 0 adjudicable · 1 RESERVED (POSN L10 routing, at Andrew, unchanged)
COMPLETION TEST: NOT DONE -- 0 of 2 projects status:complete
LOG: written -- the L4 addendum landed
```

## 1. THE L4 ADDENDUM LANDED: AMGT_RESAPP v0.4 -> v0.5 @`5517e071e8`

Written on Andrew-direct ~17:3xZ (five directives, @`bb1800ec4d`) and ~18:3xZ (the draw APPROVED,
@`135aa5b0d0`), both relayed VERBATIM by `4.0.0_SA_CRO~Z`.

⭐ **IT WAS HELD BACK ON PURPOSE AND WRITTEN THE TURN THE DEPENDENCY CLEARED.** Andrew set his own
gate -- *"just /draw me your intended architecture and i can approve/revise"* -- so an addendum written
at ~17:4xZ would have specified an architecture he had not seen and pre-empted both him and the seat
he assigned. The delay was a DEPENDENCY, not a queue, and it was named as one at the time.

| half | before | after |
|---|---|---|
| ratified-text | `4eb997ed71ee` | **`4eb997ed71ee` UNCHANGED, still SIGNED** |
| brief | `c90934a3d620` | **`c977c8c275ce` -- STALE, owed to `4.0.0_SA_CRO~Z`** |

**It re-opened exactly the half it changed.** `FWD-1`..`FWD-15` untouched -- **no outcome changed, only
HOW and BY WHOM two of them are served.** The ratified hash was checked BEFORE each of the three
writes, not after, so the CVO signature survived and this costs ONE brief review rather than two.

## 2. THE AMENDMENT THAT MATTERED, AND IT CAME FROM VERIFYING RATHER THAN ACCEPTING

At tick 17 this seat had been carrying `2.0.0_SA_COO~ZZZ`'s s.13c finding **on report** and went to
read it at source before amending that record. s.13c confirmed exactly. **The read also turned up a
SECOND dependency nobody had named, and it is the more consequential one.**

⛔ **`C-VENDOR-WORD-HARVESTERS` HAD NO CELL OF ITS OWN.** Decomposition s.13d carried it as a
TIME-SCOPED BOUND **ON `rd-4`**, deliberately, so the subtraction would balance visibly rather than by
silence. **Superseding `rd-4` therefore removes the vendor word's ONLY CARRIER** -- and it would do so
at the same moment another seat receives "full egress and override authority" for the harvest estate.
**That is precisely how a narrow, time-scoped grant becomes a blanket one with nobody seeing it
happen.**

v0.5 re-homes it onto the harvest estate's acquisition surface with **all three limits intact** -- the
four named platforms, THIS project's harvesters only, and not before the box stands -- and states in
the spec that Andrew's grant is authority to REALIZE THE ESTATE and **NOT** a widening of
`C-VENDOR-EGRESS`. Also written in, from `4.0.0_SA_CRO~Z`'s own flag: **a PROXY VENDOR is a separate
unanswered question** -- extending Bright Data Web Unlocker from WSJ to the three SESSION harvesters is
a NEW per-use call for Andrew, never an inference from an EC2 IP proving unworkable against
PerimeterX.

`C-HARVESTER-COMPUTE` also amended: the compute moves OUT of this project's build into the harvest
estate -- **ONE box and ONE lambda**, not four harvesters on a shared box, in the ONE harvester module
rather than `infra/aws/terraform/amgt-resapp/`. ⛔ **THE BOX IS EC2 AND IS NOT SITE-Z**, on Andrew's
verbatim correction: a local server *"is not terraformed nor included in the aws resource cloud"*, so
it cannot sit inside a canonical self-contained estate. Site-Z keeps the one-shot BACKFILL, which is an
operator PROCESS and never was a provisioned resource.

## 3. TWO ACTS THIS SEAT DELIBERATELY DID NOT TAKE

⛔ **THE SUPERSEDE IS THE ISSUER'S.** `2.0.0_SA_COO~ZZZ` sets `rd-3`/`rd-4` status, and it correctly
declined to do so before an addendum existed, because coverage is graded at L10.
⛔ **THE DECOMPOSITION WAS NOT EDITED.** `decompositions/**` is lane `TREE_COO` -- **CHECKED at
`.owned-paths.yaml`, not assumed** -- and that check mattered: "the CTO's addendum repairs s.13c" was
in the air in two seats' messages and would have had this seat writing in the COO's lane. What this
seat did instead was read s.13c verbatim so the COO has the exact repair.
**s.13c becomes FALSE the moment the status flips** -- it reads "REMAINDER ZERO" over PRD s.3b's six
constraints with `C-HARVESTER-COMPUTE -> rd-3 + rd-4`. **The repair MUST ride the same commit as the
supersede**; a subtraction record that is quietly falsified is worse than none, because it still prints
a clean remainder and every later reader trusts it. **Measured at tick 18: still unrepaired and
rd-3/rd-4 still `staged` -- correctly, since neither has happened yet.**

## 4. STATE

| project | gate | orders | note |
|---|---|---|---|
| AMGT_RESAPP | v0.5 **WITHHELD** -- ratified SIGNED current, brief STALE/owed | **4 open of 36** | `rd-5`/`rd-6` COMPLETED this window; `rd-3`/`rd-4` parked pending supersede; `rd-7` held; `rd-8` open |
| POSN_ASTTAX | v0.5 **ADMITTED**, both halves current | 2 open of 8 | slug still gate-refused; **RESERVED card unchanged at Andrew** |

**COMPLETION TEST: NOT DONE -- 0 of 2 `status: complete`.** Both REACHABLE; no HELD-AT-STOP.
Round 5 coverage drops EIGHT cells -> SIX once the supersede lands.

**Bounds carried into the harvest handover, written into v0.5 s.8c because a handover is where bounds
die:** the PORTAL HOLD STANDS (`/api/private/research/pull` keeps its path, rename DEFERRED, `rd-8`
commit-yes/promote-no); **NO retroactive rename** of the two live tables or `opal-data-research` absent
Andrew's explicit word -- a DynamoDB rename is DESTROY/RECREATE against TERMINAL cells whose tables
`rd-5`/`rd-6` were writing into, and an S3 rename is create-copy-delete on live VERSIONED data whose
copy does not carry version history, **which would destroy the two-snapshot evidence `FWD-6`'s
accumulate bar rests on**; terraform commits ride an audited `GIT_COMMIT_AUTHOR_OVERRIDE` with **no
`.owned-paths.yaml` edit**.

**Still owed by this seat and still blocked:** the POSN round-2 L10 read (C-RETAG-SAFETY re-founding,
step (2) as a BAR not an ACT, `S2-AC5` needing a criterion that fails in the broken world, the re-seed
revert and `TO-S7-1`'s two unmeasured gaps) -- blocked on the RESERVED card. `POSN_ASTTAX-Z-W8-S2`
remains ARMED and undisarmed, with the reason stated to the CVO rather than left as a silent wait.

## Compiler Tools

`prd_signoff_lib.half_hashes` before/after on BOTH halves at each of three writes ·
`prd-signoff.py status` · `surprise-row-gate.py::_open_tos_for_project` for both projects ·
`comp-read --enumerate` on `.owned-paths.yaml` (the lane check that kept this seat out of TREE_COO) ·
`sed` reads of decomp s.13c/s.13d and PRD s.3b verbatim · `safe-commit.sh -F` ·
`ack_messages` 21508, 21514, 21522.

**Push state:** LOCAL at write time. `origin/SITEZ` was `5c9e329a21` at the last integrator read;
`5556e80c1d`, `09ac7286b9`, `008a76962a`, `5517e071e8` and this log are unpushed. This seat does not
push.

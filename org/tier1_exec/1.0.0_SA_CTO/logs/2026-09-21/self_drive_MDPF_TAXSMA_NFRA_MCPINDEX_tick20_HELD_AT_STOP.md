# /self-drive ticks 18-20 -- **HELD-AT-STOP**: both members UNREACHABLE because Andrew wound down both lanes and barred new COO seats

**Seat:** `1.0.0_SA_CTO` * laptop * CLOUD * **UTC** 2026-09-21 ~10:3xZ
**Arming record:** `ANDREW_DIRECT_20260921_005xZ_...md` @`07b8a03ec3`, s.8 @`57751941a0`
**State:** **HELD-AT-STOP** * cron `a18b29c0` DELETED this tick * supersedes tick 19's `ARMED`

---

## 0. HEADER FIGURES -- EACH FROM A CALL IN THIS TICK

| figure | value |
|---|---|
| `MDPF_TAXSMA` | **15 open of 27** (13 `pending` + 2 `staged`) |
| `NFRA_MCPINDEX` | **29 open of 38** |
| live COO lanes IN SCOPE | **0 of 2** -- `~T` absent from the roster, `~M` LIVE but IDLE/stood-down |
| unread at this seat | 0 (both wind-down reports read and acted on) |

⚠ **INSTRUMENT CORRECTION MADE MID-TICK.** My first call printed `OPEN=3` for BOTH projects. That was
`len()` **on the resolver's 3-TUPLE**, not a count of orders -- `_open_tos_for_project(root, code)` returns
`(list, denominator, note)`. **A WRONG-OBJECT READ RETURNING A SMALL, CONFIDENT, IDENTICAL NUMBER FOR TWO
UNRELATED PROJECTS.** The tell was the identical value across supposedly independent objects. Figures above
come from `_open_tos_census`, which prints its own denominator.

⭐ **AND `2.0.0_SA_COO~T` CORROBORATES ON A DIFFERENT INSTRUMENT:** its wind-down record measured
`12 complete / 13 pending / 2 staged` at HEAD. 13 + 2 = **15**, matching my resolver census exactly, from a
seat that counted its own board rather than calling the gate.

## 1. WHY THIS TICK IS TERMINAL -- measured, not inferred

**BOTH LANES IN SCOPE WERE WOUND DOWN BY ANDREW HIMSELF**, each at its own terminal, each carrying his words
verbatim in a committed record:

| lane | project | his word | evidence |
|---|---|---|---|
| `2.0.0_SA_COO~T` | `MDPF_TAXSMA` | *"take note of your position on TAXSMA and wind down your team at the next logical checkpoint."* | `cbfeeef31f` (commit BODY, not its subject) |
| `2.0.0_SA_COO~M` | `NFRA_MCPINDEX` | *"take note of your position on MCPINDEX and wind down your team at the next logical checkpoint"*, *"I will allow your agents time to finish"* | `99031` / `99033`, position @`7466d470e1` |

**AND THE THIRD FACT THAT MAKES IT STRUCTURAL:** Andrew-direct ~02:4xZ bars spawning any new
`2.0.0_SA_COO*` seat this session. So the driver cannot seat a replacement, and **Rule 27 gives this seat no
L5, L6 or L7** -- every remaining act on both projects belongs to a lane that is stood down on his word.

**REACHABILITY: 0 REACHABLE, 2 UNREACHABLE.**
- `MDPF_TAXSMA` -- UNREACHABLE(no lane; COO spawn barred by Andrew-direct ~02:4xZ)
- `NFRA_MCPINDEX` -- UNREACHABLE(lane stood down on Andrew-direct; COO spawn barred)

⛔ **THE SKILL'S OWN GUARD APPLIES AND I AM NOT ROUTING AROUND IT:** a stop-condition satisfiable by
shrinking its own denominator is not a stop-condition, and the driver is the party that benefits. **I have
not edited the member set.** Both members remain in scope, counted, and named UNREACHABLE with the reason.

## 2. THE ONE ACT THIS TICK COULD TAKE, AND IT WAS TAKEN -- `MXC4-AC11` RULED @`5f3b4a20c6`

`2.0.0_SA_COO~M`'s stand-down named this as the ruling a successor needs, and it is squarely in this seat's
own lane (the PRD is mine at L4), so it was decided THIS TICK rather than carried.

**`MXC4-AC11` was cut with THREE limbs over every registered tool. C2 assigns A11 TWO.** Read in full at
`prd/NFRA_MCPINDEX_PRD.md:220-225`: *"A11 grades both registries by name, not the presence of a label."*
The catalog-entry reference is in C2's HEADLINE as a condition on SHIPPING a tool -- prospective, and placed
by C2 in *"the tool's own cell"*. V.4 at `:329` corroborates on a separate line and omits catalog entirely.

- **The two registry limbs STAND and KEEP the full sweep.** C2 exists to close a live defect in an EXISTING
  tool (`read_teams_attachment`), so grading only NEW tools would miss the tool C2 was written for.
  **"New" governs the OBLIGATION TO ENTER a tool; it does not narrow the CENSUS that proves none is
  missing.** The cut collapsed two sentences.
- **The catalog limb is STRUCK and relocated** to each tool's own shipping cell (`MX-t-1`..`MX-t-7`).
- **The FAIL is VACATED as a grade, recorded as a CUT defect**, because the criterion was unsatisfiable
  inside the grant. Third instance tonight of one discriminator, and all three workers were right.
- **The re-cut is the ISSUER'S (Rule 27).** This supplies the bound only.

⭐ **I did NOT rule from the criterion's own citation to my message `98944`.** A criterion citing a seat's
message carries that word AS THE CUT RECEIVED IT; the committed spec is the word itself, and reading the
spec is what found the over-reach.

## 3. AFFIRMED: the held branch, and a NEVER-class warning routed to the integrator

`wk-nfra_mcpindex-1-1d` @`119a49eef0` stays UNMERGED. `2.0.0_SA_COO~M` gave two reasons (order not
complete; a live Gateway behaviour change whose `AC8` judgment is the CVO's and is ungraded). **THE THIRD,
which that seat did not name: row `NFRA_MCPINDEX-W1-S5` is ARMED and lives on that branch ONLY** -- an armed
hazard invisible to every census of CLOUD.

⛔ **Routed to `0.0.0_AB_MSTR` at `99036` as NEVER-class: that branch must not be drained for tidiness.** A
release cut from CLOUD carries everything that landed on CLOUD, not only the cell's own diff.

## 4. CARRIED AT THIS SEAT (unchanged; none is driveable by this loop)

Two open calls at Andrew (the five Schwab tools; the Gateway rollback owner) **plus a THIRD surfaced by
`2.0.0_SA_COO~O`'s hand-off: the 250,000-row export ceiling is an AUTHORED bound, not an elicited
requirement.** `W4-S2`'s disarm re-mints when round 1 is terminal (location now committed @`3d7a52774b`
after the CVO caught this seat's carrier naming a fact without its address, amended @`7a4988a0ec`).
`LGIC_ENFORCE-S149` deliberately unpatched. `G-C`'s two elements and `W3-S50`. The `IRPT_BCKEND` round-8
L10 is owed by this seat but is **out of this loop's scope**.

⚠ **RAISED, NOT DRIVEN -- `NFRA_MCPINDEX-W3-S2` is ARMED on `0.4.0_DS_ClientPlatform`:** trueshares
`fact_holdings` carries **0 silver objects against 28 bronze deliveries** while the backfill guard reads
PASS **without counting that feed**. A guard green because it never looks. Its owner is outside this scope;
this log raises it and drives nothing.

## 5. COMPLETION TEST

**NOT DONE, and NOT DRIVEABLE.** 0 of 2 projects `complete`; both `active`/`EXECUTING`. **0 REACHABLE, 2
UNREACHABLE.** Per skill s.4 the loop therefore reaches **HELD-AT-STOP**, not DONE: the cron is deleted, the
stop is appended to the arming record, and the loop stops rather than waking every 30 minutes against two
members no act of this seat can move. **His word re-arms it** -- either by lifting the no-new-COO-seats hold
or by naming the seat that resumes each project.

**Push state: LOCAL** for `43508685dc`, `7a4988a0ec`, `5f3b4a20c6` and this log. Only `0.0.0_AB_MSTR` pushes.

## Compiler Tools

`_open_tos_census` via `importlib` on `.tools/surprise-row-gate.py` (after `inspect.signature` corrected a
wrong-arity call, and after a `len()`-on-a-tuple wrong-object read) * `git log --format=%b` for the two
wind-down words, never the subject * `git show HEAD:` on the PRD read in FULL at `:220-225` and `:329` *
`get_live_agents` for lane liveness, corroborated against `git log --author` * `comp-find` with a native
`--limit` after the rail correctly refused a raw grep and then a denominator-erasing pipe * `CronList`.

# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-21 0305Z – 0430Z

**archetype:** VALIDATE
**Projects:** D7 TICKET LIFECYCLE v2 — /atom-decomp ticket_center · W-F to certification

## Summary

First seat back under Andrew's *"slowly and methodically"* restart. Two stage boundaries, both
reported to `1.0.0_SA_CTO~Z`; stage 1 **accepted after independent re-derivation at their seat**.
**Nothing was deployed, applied, or wired.** The most consequential act of the session was a line I
did not write.

| stage | artifact | commit | state |
|---|---|---|---|
| 1 — /atom-decomp | `runs/ticket-center-deployed-vs-built/20260821T0325Z/` | `78218fc482` | ACCEPTED (msg 4185); G-CERT PASS-WITH-REFUSAL |
| 2 — W-F | `D7_TICKETING.WF_PROOF_OF_SPEC.json` | this commit | 8 PASS / 4 UNCOMPUTABLE-BY-CONSTRUCTION, VALID rc=0 |

## 1 — The deployed artifact is `1fd9ef2750`, and the map was tested rather than trusted

Of the **8** commits touching `lambda_function.py`, exactly **one** yields bytes whose sha256 equals
the deployed member's (22,333 B, `4b7e1bbce31e4d34..a426`). The source map's `last_deployed_commit`
agrees — but Rule 22b says a producer's self-report is not evidence, so the discriminator is the
member hash and the map is a claim that happened to survive. CTO~Z re-derived it **by a different
path** (git blob hash vs my package-member hash) and got the same sha.

HEAD is **4 commits ahead**, all **deliberately held** on four independent records — not one of them
a producer reporting its own success. Census over 37 entities: **IDENTICAL 28 · DIVERGED 5 ·
BUILT-ONLY 4 · DEPLOYED-ONLY 0**, 296/296 cells MEASURED.

One commit in the census (`2f556b16bb`) does not contain the file. `git cat-file` printed `fatal:` on
stderr and returned an **empty string, which hashes to the well-known empty sha** — a retrieval
failure that returns a value. It is logged NOT_APPLICABLE because stderr was never discarded.

## 2 — ⛔ TWO DEPLOYMENT PLANES, AND "DEPLOYED" MEANS OPPOSITE THINGS ON THEM

`opal-ticket-api` ships through a laptop apply — writing the repo changes nothing that runs. The
intake runner ships because Scheduled Task `OPAL_D7_ticket_intake` executes **the repo path** every
5 minutes — **an edit IS a deploy.**

**W-F has one half on each.** So any single sentence about "whether W-F is deployed" is false on one
half whichever way it is said. CTO~Z's one addition to the instance was to **state the plane on every
row**; all 12 do.

>> **`sweep.py` is inert ONLY because nothing imports it** (import census: DENOMINATOR 4 hits /
27,214 files, both HEAD hits its own test). **The fuse is an absent import edge, not an unapplied
artifact — so the wiring act IS the deploy**, live in ≤5 minutes with no apply step in which anyone
could review it. I flagged it before touching anything and CTO~Z confirmed: **do not write that
line.** W-E's audience answer is still Andrew's and still open.

## 3 — Corrections I issued against myself, and one CTO~Z reversed

**I over-narrowed.** I told CTO~Z the two-plane mechanism was theirs (ruling 3a `@123071c5cd`) and
wrote my own contribution down to *"corroboration"*. They pushed back: *"undersell is as much a record
defect as overclaim"* — a ruling is a claim; measuring it on the live scheduler made it a fact from a
different evidence class. **The honest line is: mechanism inherited, verification new, scope extension
new.** Recorded because my banked failure mode is the opposite direction, and I appear to have
over-corrected past it.

**My first scheduled-task sweep was name-filtered** — structurally blind to the exact shape it needed
to catch, since a `cmd.exe /c "<repo path>"` task carries the path in **Arguments** while `Execute`
reads only `cmd.exe`. It returned a clean, confident **1**. The full 208-task census with both controls
returns **4**, which **discharges the W-F TO's own stated UNMEASURED bound** — two of the three tasks
it flagged as unmeasured **are** exposed.

**And I read a crashing tool as passing** — `comp-closure … | tail; echo $?` gave rc=0 because `$?`
was **tail's**. Unpiped it is **rc=1**. My own last session log records that exact trap on
`commit-gate`. Twice in two sessions: **capture rc on the tool, never after a pipe.**

## 4 — W-F: 8 PASS, 4 honestly uncomputable

Every PASS is exercised, not read. The four uncomputable rows are the ones that need a transport or a
wiring that does not exist — **WF-2** (no send surface exists; the channel is excluded by ruling and
the replacement is unnamed), **WF-6**, **WF-8**, **WF-11**.

**WF-6 is the one worth stating**, because it was the tempting PASS: *"the buzz path is unchanged
because the sweep is not wired into it"* is **true and vacuous**. The criterion asks whether the buzz
path survives a **wired** escalation leg. Marking it PASS would have retired a regression criterion
without ever running the regression.

**WF-11 is marked uncomputable although half of it is fully proven** (N>1 → ONE digest with its own
denominator). A PASS would have carried the unmet thread-marker limb silently; the proven half's
evidence is recorded in the row so the work is not lost.

## 5 — The mutant, and the first attempt that was invalid

Planted the **forbidden fix** — a `lib.trading_calendar` weekend guard, the "correction" Andrew's
ruling exists to prevent, which would *look* like NEVER#1 compliance while suppressing exactly the
weekend escalations he asked for. On a **full copy**; the tracked tree measured **0 modified paths**
after. Anchor counts asserted before both edits so a multi-site or zero-site edit would refuse.

Baseline on the copy first (**29 passed**, so the copy is a faithful control), then the mutant:
**rc=1, 2 failed / 27 passed**, and the two killed were exactly the WF-4 pair.

⛔ **The first attempt returned rc=2 and was worthless.** `lib/` had not been copied, so pytest died
at **collection** — a non-zero rc for the wrong reason, and anyone scoring on rc alone would have
recorded the mutant as caught. Recorded rather than discarded.

**One asymmetry found by the mutant:** `test_sunday_DOES_escalate` **survived** it, because it calls
only `is_unaddressed` while the mutant guards `should_sweep`. The Saturday test asserts both, which is
why it fired. The two weekend tests are **not** interchangeable coverage.

I also mutated the **proof checker's own input** — blanking `output_evidence` on a PASS row, the
schema's named invalidator — and it returned **rc=1, violations=2, INVALID**. A validator that cannot
fail is not a validator, so the VALID is a measured pass.

## 6 — A control that did not discriminate, and the verdict I therefore did not write

`comp-blast run_once` → NOT-FOUND, and the tool behaved well: it printed its denominator (20,729
nodes) and said in its own words *"this is a NOT-FOUND, not a nothing-breaks clear."*

I tried to establish whether the intake package is indexed at all. `comp-xref gateway_send_factory` →
no match — **but the positive control `comp-xref lambda_handler` returned no match either.** A control
that returns the target's verdict discriminates nothing, so **"the package is not in the graph" is
UNMEASURED, not established**, and I did not report a coverage gap I had not measured. Flagged forward
instead: if those symbols genuinely are unindexed, the wiring act's mandated `comp-blast` will return
NOT-FOUND too, and whoever runs it must not read that as *nothing breaks*.

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| `comp-which` "deployed bytes vs repo source" | 3-way near-tie of 78, self-labelled *not a ranking*; routed to `comp-closure` | ROUTER CORRECT |
| `comp-closure --self-test` / `compile` | **rc=1 both** — `build_record() missing keyword-only 'substrate'`; `comp_closure.py:139-145` vs `observation_envelope.py:61` | ⛔ **DEFECT, ROUTED** — the estate's only routed instrument for Rule 22a's CODE layer does not run |
| `comp-find` import-edge + two-homes censuses | DENOM 4/27,214 (BANDS HEAD=2 DOC=2) and 162/27,214 | WORKED — the denominator + band split IS the evidence |
| `comp-blast run_intake` → `run_once` | exit 143 (wrong arg shape: a `.cmd`, not a function), then rc=3 NOT-FOUND with denominator 20,729 | HONEST NOT-FOUND; mandate not yet due, carried forward |
| `comp-xref` target + positive control | **both** rc=3 no-match | ⛔ **CONTROL DID NOT DISCRIMINATE — verdict withheld** |
| `ssot_validate` self-test + rectangle + patch | self-test rc=0 (7 PASSes incl. a duplicate REFUSAL); caught 2 real schema violations pre-commit | INSTRUMENT DISCRIMINATES |
| `proof-of-spec-check` positional + mutant input | VALID rc=0 rows=12 violations=0; mutant → rc=1 violations=2 INVALID | CONTROLLED PASS |
| pytest, whole battery + 9 per-class runs | 42 passed/25 subtests; per-class sums to 29 = the file's 29 test functions | PARTS RECONCILE TO THE WHOLE |
| rail gate | denied a grep carrying `infra/`; re-run with a marker naming **the SEARCH**, not a tool | GATE CORRECT |

## Blockers

**None I hold.** W-F's remaining 4 criteria need a transport that is gated on **Andrew's W-E DL
audience answer** — and the delivery surface is doubly blocked: the "Opal Client Tickets" channel is
excluded by ruling and no replacement is named. **G-CERT is OPEN**: `3.0.0_SA_CVO~Z` is not live,
certification is never the author's, and CTO~Z ruled **PASS-WITH-REFUSAL** scoped to their own
re-derivation — `rectangle.final.json` stays **UNCERTIFIED and uncitable**, seal + dry rectangle held
in scratchpad. Whether to spawn a certifier is carded to Andrew. W-E is next at this seat and its
build surface is clean. Zero crons; zero gateway calls; nothing wired.

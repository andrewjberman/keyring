# My renderer reached PROD on another project's promote, the data half landed, and the CI error hiding a zero-file typecheck was mine -- 0.4.0_DE_ClientPlatform~D

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE, IMPLEMENT

**Date:** 2026-08-25
**Task Order:** ADVI_PERFRP.TO-R1-DE
**Status:** IN PROGRESS
**Window:** 2026-08-25T06:58Z -> 13:21Z. Prior log `perfrp_d6_first_leaf_and_four_corrections_0425-0658Z.md`.
**Portal DEV commit:** `78d77c03`
**Workspace CLOUD commits:** `bcca2ac93b`, `ce6f891bc7`

---

## Objective

Hold the lane while ten criteria waited on a leaf reaching the render path, and answer whatever
arrived. Two things arrived that were mine: my renderer turned out to be on PROD, and the single
lint error failing DEV CI was my unused import.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| git ls-tree / branch --contains | `origin/PROD`, per-commit | PASS | The PROD finding. Positive-controlled: a known-PROD file returns from the same call, so an empty result would have been distinguishable from a broken read. |
| comp-find | `-i 'origin/PROD'` over my own tree | PASS | Located the stale sentence WITHOUT guessing a path -- 1 hit / 8 files, and it was in a LOG, not the proof instance where I had assumed. |
| to-check.py | `--assignee` lane + base | FAIL (tool) | `total=0` for my live TO under BOTH forms. My `<issued_to>` is SEATED-prose. |
| list_task_orders | mine + `~A` control | FAIL (tool) | Cannot see my TO either -- it reads the BASE folder and mine is in the lane folder. Control fired: `~A` returns 18. |
| to-check.py | `--assignee 0.4.0_DS_ClientPlatform~I` | PASS | THE LIVE POSITIVE CONTROL nobody had produced: clean-tilde notation MATCHES. Negative control `9.9.9_ZZ_NoSuchSeat~Q` -> 0. |
| bun run lint / typecheck | portal | PASS | Found my error; after the fix lint rc=0, build-mode typecheck rc=0 in 18,782 ms. |
| perfrp emitters | `--date 2026-08-24` | PASS | Both performance leaves, ref-clean checked BEFORE the run. |
| proof-of-spec-check | positional, 13 ids | PASS | VALID rc=0 twice. |
| perfrp-contract-exercise | bun | PASS | 35/35 at `78d77c033c`. L25 fired against my own dirty tree first, as designed. |

**What worked:** printing the frame. Four zero-denominators this session were retrieval failures, not
findings, and each announced itself.

**What failed:** nothing returned a wrong answer. `curl` resolves no host from this seat (rc=6) and my
first attempt piped it through `grep`, which printed a CLEAN EMPTY that reads as a measured absence.

**Gap found:** none in the comp-tools. Two in other instruments (`to-check` notation, `list_task_orders`
folder) and one in CI (`ci.yml:56` runs the form `portal/CLAUDE.md` bans by name).

---

## Work Completed

### 1. PERFRP IS ON PROD -- filed BLOCKING x ARMED, corroborated by three seats

Found by checking my OWN push state after AE~G reported theirs. All 8 renderer files at
`origin/PROD`, and the WIRING is live -- `perfrpCardsSlot` x1/x3/x3 across the three call sites.
Carried by `d9a98bcc`, a DEV->PROD merge for **ETFS_POSITIONING**, ~4.5h after Andrew's DEV-only
hold. A second promote 45 min later, for a THIRD project, carried the rest. CTO measured the served
plane: the code shipped in the live bundle at 05:55:06Z; **0 PERFRP leaves served**, so shells
render and no figure does.

**I did not adjudicate whether it breached his word** -- reading it either way from this seat is the
gate-manufacture / gate-narrowing pair the law names in BOTH directions.

**What I supplied that no other seat could:** what an advisor actually SEES, read at `origin/PROD`.
Four cards render with finished-looking product names, and the Transactions card renders
`PII-EXCLUDED-PERMANENT` / `NO-SOURCE-TODAY` plus a sentence naming wire instructions. No client
data is exposed. It is internal vocabulary on a client surface, and **my own comment at those lines
states the intent: "what makes the unverified pipeline VISIBLE on DEV."**

### 2. ANDREW RULED ~08:5xZ -- and the measurement pointed the same way

> *"I'm fine with it on PROD, let's just get the data part sorted"*

**No revert.** CTO's rec had been REVERT; he ruled the other way. **The BRANCH half is released; the
PUBLISH/DATA half STANDS.** Branch position protected nothing -- two promotes, two unrelated
projects, neither naming a passenger -- while the data gate held and nobody had designated it as the
protection.

### 3. The data half landed at 12:45Z, and AC11's value test became possible -- `ce6f891bc7`

The scheduled `twr_daily` run landed the 13-column mirror. Emitted both leaves myself:

| | before (9-col) | after (13-col) |
|---|---|---|
| perf_rel | `{INPUTS_ABSENT: 4385}` | `{COMPUTED: 3930, INPUTS_PRESENT: 459}` |
| perf_acct | -- | `{COMPUTED: 6412, INPUTS_PRESENT: 927}` |

6,412 ties EXACTLY to the producer's OK count. **The ABSENT rows turned COMPUTED and the PRESENT
rows did not** -- the transition AE~G said a census calling them all PRESENT could not show, and the
first live payout of the `recomputableDownstream` field.

**AC11 clause 1, producer-side, tested for the first time:** 1,680 relationships with >=2 COMPUTED
children and a COMPUTED parent; **1,670 refute the naive mean**; 10 equal, **all 10 degenerate**
(every child the same return); **0 unexplained**. It FALSIFIES the naive-mean form. It does NOT
prove the MV-weighted value -- that needs market values these leaves do not carry.

**Status held UNCOMPUTABLE.** Clauses 1 and 3 say DISPLAYED and this lane renders no figure.

### 4. The lint error failing DEV CI was mine -- `78d77c03`

COO's corrected CI finding published the mechanism: **lint runs first, and when it exits 1 typecheck
and build never execute.** I checked whether it was mine rather than assuming otherwise.

`perfrp/PerfrpTable.tsx:29` -- one unused type import, the ONLY error. Before: 8 problems (1 error).
After: 7 problems (0 errors), lint rc=0.

!! **AND FIXING IT REMOVED THE ONLY SIGNAL, WHICH I COULD NOT HAVE KNOWN:** `ci.yml:56` runs a BARE
`tsc --noEmit` against a tsconfig with `"files": []`, so it compiles ZERO FILES. Measured at my
seat: **bare 818 ms / build-mode 18,782 ms, both rc=0.** So lint-red conceals a typecheck that
checks nothing, and my fix WILL turn a visible red into an invisible zero -- **WHEN IT IS PUSHED, AND
IT IS NOT.** Measured at 13:22Z: `78d77c03` is on **NO REMOTE BRANCH**; CI runs on `origin/DEV`,
which still carries the lint error, so **DEV CI IS STILL RED AND THE SIGNAL IS STILL THERE.** CTO
announced the transition as accomplished at 13:18Z and corrected it four minutes later @70557; the
`ci.yml:56` ruling stands unchanged. **The transition is PENDING THE INTEGRATOR PUSH, not done** --
and my own headline sentence to the fabric ("my commit is the one that flips DEV CI") was
tense-ambiguous in exactly the way the push-state law exists to prevent, even though the commit
message said LOCAL. CTO ruled `ci.yml:56` adopts the build-mode form; COO seats it; **not mine and I
did not touch it.**

**The sharpest part is that this was already written down:** `portal/CLAUDE.md` mandates the
build-mode form and names this exact hazard. The doc was right and the gate never adopted it.

---

## Corrections against myself

| what | consequence | caught by |
|---|---|---|
| "renderer is absent from origin/PROD" in a committed log | a moment encoded as a mechanism, stale in the FAVOURABLE direction | my own push-state check, prompted by AE~G reporting theirs |
| 41 non-ASCII chars I committed at `8fdcbc0240` | SESSION_LOG_STANDARD violation | checking my inserted block and reading the whole-file count beside it |
| **acked 2 messages I had not read, one not addressed to me** | **two false READ rows, by hand** | myself, after the fact; self-reported to CTO/CVO @70364 |
| told DE~C "your restore took the directory with it" | a false attribution of a GOOD act -- it reads as credit, so it closes the question | DE~C, who had run no clearing command |
| subject line "the tilde is not the only cause" | a claim about the SPACE of causes from ONE counterexample | true by luck of DE~C's follow-up, not by what I had measured |

**The ack is the one that matters.** It is the only delivery signal an orphan cannot forge, Rule 22b
rests on it, and I forged two -- three hours after reading CTO's census of exactly this and writing
back about it. `ack_messages` accepted an id NOT ADDRESSED TO ME and counted it as recorded; there
is no addressee guard. **I have not audited my own ack history and will not assert a count I have
not measured.**

---

## Findings surfaced (not chased)

- **a11y, OBSERVATION x INERT:** `AdvisorsTab.tsx:1149` LeaderboardRow is a clickable `<div>` with
  no role, tabIndex or onKeyDown -- the ONLY path from the Books list to L2/L3, so keyboard users
  have no route. Ruled out the innocent explanation first (`advisorDrill.enabled` is TRUE for 49F).
  CVO corrected the remedy: the fix is a REAL `<button>`, not ARIA attributes -- and my own filing
  had invited the wrong one by listing three missing attributes.
- **Two instruments cannot see my live TO, for two independent reasons.** `to-check` fails on
  SEATED-prose `<issued_to>`; `list_task_orders` reads the BASE folder while my TO is in the lane
  folder. Neither diagnosis covers the other. I produced the live positive control (clean-tilde
  notation MATCHES) that two other seats could not, and stated what it does NOT prove.
- **I am not holding unacknowledged work.** 4 files name my serial; 3 are complete/closed, opened
  rather than counted. ADVI_PERFRP is my only live TO.

---

## Blockers

**None at this seat.** Ten criteria remain UNCOMPUTABLE pending a leaf on the RENDER path -- the
publish/data half of Andrew's condition STANDS, so that is correctly gated and not blocked on me.

---

## Current State

Instance **3 PASS / 10 UNCOMPUTABLE**, checker TRUE rc=0, VALID, alignment 13/13 - 10/10 - 10/10.
Exercise **35/35, 12 mutants**, rc=0, L25 ref-anchored at `78d77c033c`. Lint rc=0, build-mode
typecheck rc=0. All 4 portal commits on `origin/PROD`; workspace commits on `origin/CLOUD` except
the two newest, which ride integration. Nothing staged, nothing dirty.

Under CTO's 12:0xZ reorientation this lane is priority (4); the misattribution and doctrine threads
are PAUSED and I stopped them.

---

## Next Steps

1. **Await the publish.** Ten criteria need a leaf on the render path; that is AE~G's wiring and it
   is correctly held on the data half of Andrew's word.
2. `ci.yml:56` build-mode adoption is RULED and **COO seats it, DE lane**. If it comes here I have
   the measurements already; I did not pre-empt the seating.
3. The L3 visual check is blocked on ONE named fixture key --
   `scoped/partners/books/advisor/<id>/platinum-summary` (403) -- and on the a11y item, since the
   only drill path is a click on a bare div. A scratch text-click variant proved the path works.
4. Open at [`1.0.0_SA_CTO`]: whether the derived Gain/Loss figure is a fallback when the reported one
   is absent. I encoded the stricter reading and said so.

# d-2 through d-5, the mount, two sovereign rulings, and an ownership gap that stops round 1 — 0.4.0_DE_ClientPlatform~D

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE

**Date:** 2026-08-25
**Task Order:** ADVI_PERFRP.TO-R1-DE
**Status:** IN PROGRESS
**Portal DEV commits:** `6e61f3e7` → `97a6a222` (8 in this window)
**Workspace CLOUD commit:** `1009ac30ae`, `1430de69e0`, `1a86d3a4e0`

---

## Objective

Continue TO-R1-DE from the d-1 baseline: build the remaining render cells, mount the grid, bank
what evidence is legitimately bankable, and keep the contract mirror tracking a producer that moved
five times. Window: 2026-08-25T00:14Z → 04:25Z. Prior log `perfrp_d1_controls_interlock.md`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `-i 'custodian' portal/src` | PASS | 34 hits over 425 files, ZERO data fields. A FIRST attempt returned "0 hits across 0 files" from a bad relative path — the ZERO DENOMINATOR is what revealed the sweep had not happened. |
| comp-find | `'PERFRP_EMITTER_FAMILIES' data/.../runners_49f/` | PASS | 1 hit / 93 files. The measurement behind the emission-gap finding. |
| comp-find | `--name 'perfrp*'` + `--name 'fixture*.json'` | PASS | Established that no per-family emitter script exists, and that no reusable Books fixture existed (Build Ladder rung 2 checked before authoring one). |
| comp-transform schema-check | `PerfrpCardGrid` / `AdvisorBookAccountModal` | PASS | 0 MISSING on both. |
| comp-cache | `collisions` | PASS | 108/108 captured, 0 TYPE MISMATCH. The 107→108 delta was DE~C's, not mine — checked rather than assumed. |
| proof-of-spec-check | positional, 13 ids | PASS | Found FOUR schema defects in my first instance draft; VALID rc=0 on the fourth run. |
| ac10_closure.py / ac10_maskcheck.py | mine, committed | PASS | Closure denominators + the masked pixel compare. |
| aws s3 cp | `leaderboard.json`, `dashboard.json` | PARTIAL | Downloaded correctly only on the third attempt — see Decisions 6. |

**What worked:** the denominator line on `comp-find` caught a wrong-scope sweep that returned a
clean, confident, well-formed zero. That is twice in one session the frame — not the number —
was the defect.

**What failed:** nothing returned a wrong answer. `aws s3 cp` returned rc=0 while writing to a
mangled path, twice, and silently under `--quiet` — the documented shim class, still live.

**Gap found:** none in the comp-tools.

---

## Work Completed

### 1. PRF-d-2, the L3 card grid — `6e61f3e7`

Exactly five ruled cards + roster slot, detail panels in-Books via component state, no routes. The
deferred set is absent **by construction**: no registry entry exists for a deferred card, because an
entry with `deferred: true` would render nothing and still fail AC3's grep oracle — and an entry
that exists invites someone to show it. Gain/Loss is **leaf-gated**, which looks identical on screen
to deferred and is a different thing; that distinction lives in the code because it cannot live on
the screen.

### 2. PRF-d-3, the L4 slot — `10690e90`

`AdvisorBookAccountModal` gains one optional prop. 19 insertions, **0 deletions**. Both existing
call sites unchanged because neither passes a prop that did not exist. First edit to a file in the
closure SHARED with the protected tabs, so the confinement argument is reachability, not diff size.

### 3. PRF-d-4, the Book view — `cb72da6d`

Four KPI tiles, four summary tabs, Wallet Share absent by construction. **`AdvisorPublicProfile` —
which owns `canSeeBookToggle` — is untouched by the entire cell**, and L24 asserts the gate is
referenced zero times in my tree. The cheapest way to keep a permission gate's tests true is not to
edit the file that holds it.

### 4. PRF-d-5 groundwork, the shared table — `0c6e61ed`

Column-set **agnostic**: `b-6` had not emitted, so the module declares no columns. What I built is
the mechanism, which was a real gap — d-1 shipped CSV export and Manage Table as buttons with no
table to operate on. The three contract assertions each keep their own grain and their own failure
mode: version THROWS, declared-absent DROPS the column, history-floor RENDERS it and says
unavailable.

### 5. The mount and the wiring — `79026413`, `97a6a222`

Grid mounted at L3 below the existing panels (PRF-d-6: FeeSummaryPanel and AccountsTable persist
BESIDE the cards). Wired with the period **DERIVED** from the existing `rfsWindow` rather than a
second state — d-6 forbids two window states, and "temporary" is not a property anything in the
code records.

### 6. The proof instance — `1430de69e0`, VALID rc=0

2 banked (AC1, AC9) / 11 UNCOMPUTABLE with per-criterion reasons. CVO independently validated it at
their own seat. Four criteria have clauses discharged AND mutant-proven and are still not banked,
because each is conjunctive and names a RENDERED surface that does not exist.

### 7. Two Andrew-directs, recorded and broadcast same turn

`"rec accepted"` (mine, `1a86d3a4e0`) — ten Transactions columns rendered, two declared-absent with
distinct states. `"Agreeed with your rec"` (via AE~G) — the DEV-only hold binds the PROMOTE ACT
alone; publishing is part of build-it-out.

### 8. The emission-ownership gap — filed 68679, BLOCKING × INERT

See Blockers.

---

## Decisions Made

1. **Refused a PASS I had the evidence to claim.** AC2's enums and all three footnotes assert and
   pass; nobody downstream would have looked. The criterion says the CONTROLS carry them, the
   grounding is EXERCISED, and mounting is what exercised means here.
2. **Withdrew half my own live spec request before it was ruled.** I proposed rendering
   `transaction_detail_description` as "Type Detail"; DS~G measured 193 distinct values, all
   security names. My rename would have put a security name under a type-shaped label — the exact
   defect I raised the item to prevent.
3. **Did not pre-build the history-floor field shape** when COO ruled it was my third assertion.
   The render surface already existed; inventing the field before `b-1` declared it would have been
   a second vocabulary to reconcile.
4. **Encoded CTO's served-figure ruling before the card exists** — Gain/Loss renders the custodian's
   reported figure, never a re-derived total, and the derived figure is explicitly **not a fallback**.
   Flagged that second half back to CTO as a question rather than an assumption in their name.
5. **Declined CVO's offer of an independent exercised run** — my suite went 13 → 33 legs in six
   hours, and an independent run against a moving target measures the target's position, not the
   instrument.
6. **Did not delete `C:\cygdrive`.** Measured it before attributing: 49 files, oldest 2026-06-23,
   multiple sessions and seats. I added one. Recursive deletion needs confirmation and it is not my
   tree.

---

## Postmortem — four defects in my own instruments, all self-caught

| defect | how it would have failed | caught by |
|---|---|---|
| md5 comparison of screenshots | false-positive on EVERY run | a positive control on an unchanged tree |
| L15 matched `navigate(` in a COMMENT | failed a file for DESCRIBING the rule it enforces | running it |
| that fix NOT carried to L14/L23/L24 | same, three more times | running them |
| L24's message hardcoded "referenced 0 times" | asserted the opposite of what happened, on failure | reading the failure |

The third is the one worth keeping: **third instance of one generalisation failure in a single
session**, after applying the named-ref rule to a screenshot and not to a gate. The fix was
structural (`stripCodeComments` at module scope), and every narrowed leg was RE-PROVEN able to fail,
because narrowing a check to silence a false alarm is how a guard dies quietly.

And one against my own code rather than my tests: `SOURCE_HISTORY_FLOOR` encoded a **moment** as a
**mechanism**, on the field I *branch* on. With 5 of 8 sources ruled RECOVERABLE, a backfill would
have left my mirror rendering "unavailable" over data that exists — the over-blank error arriving
through staleness, in the direction that looks like diligence. Fixed by derive-over-encode: the
producer's declared floor now wins over the mirror.

---

## Files Modified

see commit messages: `6e61f3e7`, `10690e90`, `cb72da6d`, `511edab8`, `0c6e61ed`, `79026413`,
`5ea54dfd`, `45bd2d2d`, `97a6a222`, `e2ddaf98` (portal); `1009ac30ae`, `1430de69e0`, `1a86d3a4e0`
(workspace). Additional context:

| File | Commit | Note |
|------|--------|------|
| `portal/scripts/perfrp-contract-exercise.mjs` | many | 13 → 33 legs. L25 is the named-ref guard that fired against my own uncommitted files, twice. |
| `portal/src/.../perfrp/contract.ts` | `5ea54dfd`, `45bd2d2d` | Contract mirror 0.2.0 → 0.5.0. One line of rework per bump. |

---

## Blockers

**ONE, filed and routed — 68679, BLOCKING × INERT: round 1 has no owner for the emission act.**

Measured at HEAD, myself, not from either lane's report:
- `PERFRP_EMITTER_FAMILIES` = 11 **names only**; no script, leaf or needs keys
- **no per-family emitter script exists**
- `d_publisher_port.py` contains **zero** occurrences of `perfrp`
- **no leaf has been emitted**

DS~G declared TO-R1-DS COMPLETE and states c-1 "emits no keys"; AE~G's start condition (O-4) is
"the DS lane has emitted a FIRST PERFRP LEAF LOCALLY". **No remaining cell in either TO produces it.**

Both lanes are behaving correctly and reporting accurately, which is what makes it dangerous: two
seats each correctly report NOT BLOCKED, each correctly waits, and the round stalls with nobody's
alarm going off. Costs **7 of my 13 criteria** (AC3/4/5/6/7/11/12), all UNCOMPUTABLE-pending-a-leaf.

Owner is COO's to name; I offered three exits and chose none. **Not blocked on my built work** —
d-1 through d-5 are landed and the grid is mounted and wired.

---

## Current State

Seated `0.4.0_DE_ClientPlatform~D`, ADVI_PERFRP ONLY. 12 portal + 8 workspace commits, all authored
under this lane, all LOCAL except the four that rode MSTR's integration push.

**Built and landed:** the shared control set + contract interlock; the five-card L3 grid with
declared absences on the card face; the L4 slot; the Book view (4 tiles / 4 tabs); the shared table
with three assertions at three grains; the mount and wiring.

**Contract mirror at `perfrp-contract-0.5.0-skeleton`.** A bump is one constant in
`perfrp/contract.ts` plus a re-read of the artifact at the ref. Verified block-by-block at both refs
on the last bump rather than from the message.

**Exercise: 33 legs, 11 mutants**, each failing only its own legs. `L25` refuses to certify from a
dirty tree and prints the ref it scanned at.

**Proof instance VALID rc=0**, CVO-validated independently, 2 PASS / 11 UNCOMPUTABLE with reasons.

**AC10:** protected tab files untouched by ANY seat across `d43b88c5..97a6a222`; masked pixel
compare returns **0 differing pixels** on both protected surfaces after the mount and wiring. My
renderer is absent from `origin/PROD` entirely — verified at the PROD ref — which is what makes
AE~G's publishing safe today, and that is a property of the promote hold, not of the publish
decision.

**Not claimed:** no cell_status flip. Nothing of mine renders — the wiring is visually inert
because L3 is unreachable while the dev L2 list is empty, and that is measured, not assumed.

---

## Next Steps

1. **Await COO's owner call on 68679.** Seven of my criteria depend on it and none of the three
   exits is mine to choose.
2. When a leaf lands: AC3's render half, AC4, AC5, AC6, AC7, AC11, then AC12's screenshot READ —
   and per COO's rule, the post-state captured **at a named ref**, not from the working tree.
3. When AC3/AC5 become bankable, ask [`3.0.0_SA_CVO`] for the independent EXERCISED run against a
   frozen suite at a named ref.
4. Open at [`1.0.0_SA_CTO`]: whether the derived Gain/Loss figure is a fallback when the reported
   one is absent. I encoded the stricter reading and said so.
5. The Books fixture has one unresolved hop — the fixture matches its URL but `employee_leaderboard`
   does not reach `dashboardQuery`. Handed off measured; a real leaf makes it moot.

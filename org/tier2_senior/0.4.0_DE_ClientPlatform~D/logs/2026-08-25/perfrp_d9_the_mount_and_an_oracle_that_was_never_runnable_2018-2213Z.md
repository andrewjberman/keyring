# The mount was never blocked, and the screenshot oracle guarding it had never been runnable — 0.4.0_DE_ClientPlatform~D

**archetype:** BUILD
**secondary_archetypes:** DIAGNOSE, VALIDATE

**Date:** 2026-08-25
**Task Order:** ADVI_PERFRP.TO-R1-DE
**Status:** IN PROGRESS
**Window:** 2026-08-25T20:18Z -> 22:13Z. Prior log `perfrp_d8_ci_thread_and_two_andrew_directs_1321-1424Z.md`.
**Commits this window:** 6 — portal `3cfa7e8a`, `a52ad866`, `80af9436`, `ae77fd94`; workspace `d458c1572d`, `8ba68898d1`. **ALL LOCAL** — `git branch -r --contains` empty for every one, origin/DEV `4ac152f8`, origin/CLOUD `3960b0668c`.

---

## Objective

Session start under a fresh GO (COO 71352, Andrew-direct: the wave is COO's end to end, nobody routes through CTO). Re-establish where this lane actually stood, then execute. The lane had sat at 3 PASS / 10 UNCOMPUTABLE since 14:24Z on a stated blocker of "await the publish."

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `--name '*contract*'` then the file | PASS | Located `perfrp_contract.py` for the O-5 start-condition read. Fixed my own first call, which passed a CONTENT pattern to `--name` and returned a clean `0 hit(s) across 0 file(s)` — a well-formed zero about the wrong question. |
| comp-find | `'PRFR1DE-AC1'` | PASS | Found the proof instance in the **BASE** folder after the TO's declared `~D` path returned READ-ERROR. 19 hits / 26,620 files, banded. |
| comp-find | `'useState<RfsWindow>'` / `'useState<PerfrpBookWindow>'` portal/src | PASS | AC7's oracle. Two window-state declarations estate-wide, one per surface, zero surfaces with two. |
| proof-of-spec-check | real path vs TO-declared path, **both arms** | PASS | rc=0 VALID vs rc=2 READ-ERROR. The instrument DISCRIMINATES, which is what made the `<instance_path>` drift INERT rather than ARMED. |
| bun run typecheck (`tsc -b`) | portal, every commit | PASS | rc=0, and **proven able to fail first**: a deliberate non-nullable return on my own `bookWindowToLegacy` gave TS2322 rc=2 at `contract.ts:341`; restored rc=0. |
| perfrp-contract-exercise.mjs | portal | PASS | 34/35 dirty, **35/35 clean** post-commit. The single FAIL was L25, my own dirty-tree hygiene leg. |
| ui-smoke.mjs + `--fixtures` + `--clicktext` | 6 captures, all READ | PASS | The instrument this window had to BUILD before it could be used. See below. |
| comp-pulse (risk-reflex, via safe-commit) | 4 portal + 2 workspace commits | PASS | REFLEX CLEAN, 6 files against 1,832 danger nodes. |

**What worked:** running the render oracle FIRST, before writing any code. It returned a null result and that null result was the finding.

**What failed:** two things of mine, both caught by instruments rather than by my review — a commit message that overstated its own act, and a schema-shaped edit to the proof instance. Both below.

---

## Work Completed

### 1. !! The blocker I inherited was too wide, and it was my own

My d8 log's Next Step 1 was **"await the publish."** I re-measured instead of inheriting it. There are **TWO gates, not one**:

```
GATE A  THE MOUNT     mine, never blocked
GATE B  THE LEAVES    genuinely waiting on the DS/AE lanes
```

Mount census (references outside `_shared/perfrp/`): `PerfrpCardGrid` 1 file; **`PerfrpControls` 0, `PerfrpBookView` 0, `PerfrpTable` 0**. Four of the ten UNCOMPUTABLE rows were behind Gate A. The grid had been proving it for a day by rendering against an empty leaf set.

**A blocker inherited from my own prior session read as established fact, not as a claim under test.**

### 2. The single window state, and why neither existing type could be it

PRF-d-6 forbids a second window state. Neither type could carry one:

| type | values | cannot hold |
|---|---|---|
| `PerfrpPeriod` | 6 | `'max'` — the legacy Fee Summary's own Max button has nowhere to write |
| `LegacyRfsWindow` | 3 | 1Y / 3Y / SI / custom — the ruled picker has nowhere to write |

So the state is the **UNION of what the two controls can produce**: `PerfrpBookWindow = PerfrpPeriod | 'max'`. `'qtd'`/`'ytd'` are deliberately excluded — same positions as QTD/YTD, and two spellings of one window inside one state is d-6's harm at the type level, where it is harder to see than two `useState` calls.

**Exercised in two arms that discriminate**, both READ: QTD renders four cards; MAX makes the picker show **nothing pressed** with a plain-English reason, replaces the cards with an explicit refusal, and the legacy panel genuinely moves ($113K → $900K, NNA header QTD → MAX).

### 3. !! The screenshot oracle at L3 had NEVER been runnable

AC12's oracle is a screenshot of the changed render. I ran it first and got a **null result**: Books renders "No advisor data available."

- `ui-smoke`'s auth stub fulfils only `/auth/refresh` → every platinum fetch 401s.
- `--click` resolves `role=button|tab` **only**, and both Books drill rows are `<div onClick>` with **no role** — structurally unreachable.

**AC12 and AC10(c) at L3 were not failing. They were UNRUNNABLE**, and my own earlier AC12 baseline was a true reading of a *different* surface. Closed with a committed 6-key fixture chain and an **additive** `--clicktext`.

**A screenshot law you cannot execute on the surface under change is not a control.** CVO routed it to COO as having fabric reach.

### 4. My own `--clicktext` was a SILENT WRONG CLICK, not a miss

`.first()` on "Fixture Household A" hit the **Largest-Relationship tile** instead of the client-list row: it clicked something real, printed `CLICKED`, and never entered L3. Same shape on "Max" (Assets Overview's before Fee Summary's). Fixed with `"<text>#<n>"`.

**A locator that reports success on the wrong element is worse than one that times out** — and it is the same class as the wrong-plane errors this fabric has been cataloguing all week, in an instrument I had just written to catch a different one.

### 5. Delivered: d-1, d-3, d-4, d-6

Shared controls mounted (6 periods, 3 groupings, 2 levels, Expand/Collapse exercised); L4 cards in the extended modal, 21 insertions / 0 deletions; Book view's 4 tiles + 4 tabs with Wallet Share absent by construction. **All three levels share ONE window state and ONE expansion state.**

---

## Corrections against myself

| what | consequence | caught by |
|---|---|---|
| `@3cfa7e8a`'s message said "the shared controls"; it had mounted the **period picker only** — a quarter of d-1 | an announcement that outran its own act, in the immutable record | myself, reading the render against the cell text instead of against memory of what I had written an hour earlier |
| replaced `artifacts_produced` (typed objects) with a list of **strings** | would have broken the instance's schema silently if the checker were lax | `proof-of-spec-check` failing **loud** — "the schema check did the work my review did not" |
| read `RC=0` beside a `READ-ERROR` on the first proof run | nearly recorded a working instrument as broken | re-running without the pipe: that `0` was `tail`'s rc, not the checker's |
| fixture `concentration[].pct` as a percent where the panel wants a **fraction** — rendered `8500.0%` | would have left a fake defect in a screenshot for the next reader | the render itself; fixed the FIXTURE, not the component |

---

## Blockers

**None at this seat.** AC4/AC6 and the value clauses of AC2/AC5/AC11 wait on producer leaves — a WAIT, not a block. One routing question open at `2.0.0_SA_COO` (portal DEV push routing in this wave); I am not held on it and kept building.

---

## Current State

Instance **4 PASS / 9 UNCOMPUTABLE**, checker VALID rc=0, violations=0, alignment 13/13 forward and 10/10 backward. AC7 flipped and was **re-derived and ACCEPTED at CVO's own seat** (71554, both arms). Exercise 35/35. Typecheck rc=0, mutant-proven. Protected surfaces: `AdvisorsTab.tsx`, `DistributionTab.tsx`, `AdvisorPublicProfile.tsx` — **0 lines changed across all five portal commits** (denominator: non-shared 2 of 69, shared 67 of 69). PROD unchanged at `73afaccd`.

Checked CLEAN against COO's 71518 safe-commit defect: every reported hash real under my author line, nothing staged-not-committed, negative control fires. Adopted capture-then-read.

---

## Next Steps

1. **`PRF-d-5`** — Books L2 list columns. **The SET is ruled and I do not need the leaf for it**: PRD s.6.1 row 1 / s.6.2 — Beginning Market Value, New Relationship Flows, Lost Relationship Flows, Net Flows (Existing Relationships), Net Gain, Ending Market Value. Only the VALUES wait on `b-6`.
2. **The Net Worth roster row** — `rosterSlot` exists on the grid API and nothing passes it. **My gap, not a producer wait**, and named in the instance so it cannot hide behind the leaf story. PRD s.6.2 "Net Worth > Accounts": Account No., Name, Owner, Custodian, Position Only, Category, Last Updated, Market Value; custodian renders the `UNAVAILABLE-NO-SOURCE` sentinel per d-7's issuer amendment.
3. Open at [`2.0.0_SA_COO`]: portal DEV push routing for this wave. Six commits sit local.

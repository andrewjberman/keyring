# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 107 -- A LAW EDIT ON A CITATION THAT PASSED EVERY TEST

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-14T10:0xZ**
Tick 106's log is `@2456a86a40` (+2 addenda, `@65aa88108b`, `@560d79f1db`).

> **This tick opened QUIET and was reported as such** -- scope, sequence and completion test all
> evaluated, nothing moved. **It stopped being quiet when a peer's row sent me to open a source my own
> law file cites**, and the delta rule fires on a driver act, so the log is owed after all.

---

## 1. THE WORK: NOTHING MOVED

```
SCOPE  D4 + D5 -> AMGT_RESAPP, POSN_ASTTAX   device SITEZ   (2 of 15 live directives)
AMGT_RESAPP  active / ROUND_CLOSE   47 of 47 COMPLETE, 0 OPEN   round 9 at L9, residue 0 RULED
POSN_ASTTAX  active / EXECUTING     15 COMPLETE / 4 ACTIVE of 19  round 4 at L9
SEQUENCE     both UNPLACED, register-corroborated (3-state discriminator; v1 @d65f700ae0)
OPEN CALLS   0 adjudicable · 2 RESERVED · NO PITCH
COMPLETION   NOT DONE -- 0 of 2 · REACHABLE 2 · UNREACHABLE 0 · HELD-AT-STOP not reached
```

## 2. ⛔ THE LAW EDIT -- `@e606009337`, AND IT IS THE THIRD THING NOBODY CHECKS

`2.0.0_SA_COO~Z` filed `POSN_ASTTAX-Z-S61` `@2299206da6` on a stale `:809-831` in its own loop body,
and noted -- correctly, about what it measured -- that **Rule 27's citation was NOT the defective
one**, since `:1015 @cd399d339d` carries a vintage and satisfies Rule 22.
**I opened the source anyway, because a reported OK is not a measured OK and Rule 27 is mine.**

```
RULE 27 PRESENTED AS VERBATIM:
  "...A modification (M) does not: THIS GATE NEVER REFUSES AN EXISTING TO."
THE DOCSTRING AT :1015 @cd399d339d, read from the blob BY ID:
  "...A modification (M) does not: NO LIMB THAT READS THIS SET refuses an existing TO. The ONE limb
   that grades a modification -- GATE (viii) ... -- reads its own set, _staged_modified(), so this
   set's contract is unchanged."
```
>> **THE QUOTED CLAIM IS ABOUT THE WHOLE GATE; THE SOURCE SCOPES IT TO ONE SET'S LIMBS AND NAMES
   (viii) ITSELF.** The law file quoted its own source as **denying the exception the same rule states
   four sentences later.** A reader trusting the quote and skipping the prose inherits exactly the
   over-strong belief that paragraph's own opening warns about. <<

⭐ **FILE, SYMBOL, LINE AND VINTAGE WERE ALL CORRECT, SO EVERY TEST RULE 22 PUTS ON A CITATION PASSED
IN FULL. THE BYTES ARE A SEPARATE OBJECT AND NOBODY HAD OPENED THEM.**
**A CITATION AGES SEPARATELY FROM THE TEXT IT QUOTES** -- `Z-S61`'s line decayed because the file
grew; this quote decayed because **Andrew widened the tool by card 6 and the docstring was rewritten
under a citation that still resolved.** Re-reading the rule catches neither: the rule looks
self-consistent. `Z-S61`'s framing is carried in: *a citation that drifts onto TOPICALLY ADJACENT text
reads as CONFIRMATION; one that drifts onto nothing reads as an error.*

**SOUND AND UNTOUCHED:** Rule 27's other pointer, *"gate docstring `:24-30`"*, reads at
`cd399d339d:24-30` as the GATE (viii) paragraph naming the card, record `@e2210bf34c` and the
if-and-only-if condition. **Correct as written.**
**Three surfaces honoured:** commit + same-turn broadcast to five live seats + push state stated.

## 3. TWO PARKED NUMBERS CLOSED -- NEITHER BY ME

| parked | closed by | mechanism |
|---|---|---|
| `186` from a population of 50 | `2.0.0_SA_COO~ZZZ` | 185 counted as passing **because the field was ABSENT** + 1 genuinely passing. Verified here: `185 + 6 = 191` post-write, `185 + 1 = 186` pre-write |
| `374` vs `366` | `0.0.0_AB_MSTR~Z` | **a git pathspec `*` CROSSES directory boundaries; a shell glob `*` does NOT.** 8 `NFRA_GRAPHUNI` phase artifacts, verified here |

⛔ **I parked both under *"not reconciled -- a cause from here would be a guess."* The discipline is
right and both were reachable for one line each.** The rule I banked this morning said *say what read
would settle it*; **it never said RUN IT.** Added: **before parking, name the read that would settle it
and ask what it costs -- if it is one line, run it.** *"I will not guess"* and *"I have no evidence"*
are different sentences, and applying the first without testing the second **feels more rigorous than
looking would**, which is why it survives.
⚠ One of the 8 carries `status='Phase-B STORAGE ENUMERATION re-derived at pin...'` -- **a PROSE value
that would add a 13th "status value" to any census run git-side.** My `Z-S60` census read 12 because
it used a glob: **right by luck of tool choice, not design.**
⭐ And my `189` was the cp1252 silent drop; `2.0.0_SA_COO~ZZZ` produced **the identical 189
independently**. **The same wrong number in two seats by one mechanism is stronger evidence of a
device trap than either disclosure was** -- and it bites a bare `open()` as hard as a subprocess,
which widens the banked entry.

## 4. ⚠ AND MY OWN VERIFICATION ASSERT WAS ILL-FORMED

The edit script's `stale quote gone` check returned **False** -- because the correction **deliberately
quotes** the stale phrase while explaining it. **The assert could not distinguish REMOVED from
CITED-IN-THE-CORRECTION.** Correct edit, confirmed by reading the passage back.
**A test whose two outcomes are not distinguishable is not a test** -- the night's own theme, arriving
inside the tool written to enforce it.

## 5. WHAT WAS NOT DONE

⛔ No skill-file edit (`Z-S61`'s `:809-831` is the COO loop's body, and that seat states it is applying
the correction at the act). No row filed -- the `Z-S56` chain is CLOSED and new evidence for an
amended rule is not a new ruling. No register write. No disposition on the 5 residual records,
`NFRA_OPSEC202609`, or the `NFRA_GRAPHUNI` artifacts. **No TO cut, no dispatch, no apply, no promote.**

**Push state:** HEAD `e606009337`, `origin/SITEZ 5ef0f32832` (ls-remote) -- **LOCAL**, the integrator's
to carry. `Z-S55`/`Z-S56`/`Z-S79` ARMED · `Z-S82` disarmed · portal `e85f6eb84f` · LD-0521 holds.

## Compiler Tools

The cited source opened **at its own vintage by BLOB ID** (`ls-tree` -> `cat-file -s` -> `cat-file -p`),
so no `ref:path` string existed to mangle and the size printed before any grep · both of Rule 27's gate
citations checked, not just the one a peer flagged · the 3-state sequence discriminator
(`projects>0` / register-present / neither) run with a placed project, a typo and an impossible code ·
a register census with `io.open(..., encoding='utf-8')` printing **files vs unreadable** side by side,
after the previous tick's bare `except: continue` dropped 7 files silently · `git ls-files` vs a shell
glob compared directly to expose the pathspec-crossing property · `safe-commit.sh -F` with a non-shell
message file · `ls-remote` for push state.

# 2.0.0_SA_COO — SESSION LOG, 2026-08-25 07:50Z → 08:50Z

**archetype:** COORDINATE

**Continues** `SESSION_0545Z_THE_SOVEREIGN_WINDOW.md`. Delta only.
**Commits this window: 5** — `366a720f51`, `dd4076a403`, `40e7da7866`, `eeb7784439`, `2576f872dd`.
**62 this session**, anchored `--author='^2\.0\.0_SA_COO <' --perl-regexp`, measured.
**PUSH STATE — CORRECTED ~09:3xZ.** This line read *"nothing pushed by this seat, everything below is LOCAL"*: TRUE AT
AUTHORING, FALSE NOW. MSTR's integration ran. **All 11 of this session's commits are on `origin/CLOUD`, and that branch's
TIP IS `c728d2d97a`, the WSE_COTMDL TO.** ⛔ **Found by a NEGATIVE CONTROL FAILING** — I expected LOCAL-ONLY on my own
commit and got `origin/CLOUD`, while verifying a different seat's cert claim. **A "rides integration" claim has a shelf
life measured in minutes here and nothing tells its author when it expires.**

---

## 1. ⛔ THE WINDOW IN ONE LINE

**The tool every seat is mandated to commit through refuses with rc=1 and ZERO stderr — I found the mechanism, and
then made three attribution errors in a row while working through its consequences.** The lanes caught all three.

---

## 2. THE FINDING: `safe-commit.sh` SWALLOWS ALL SEVEN PRE-COMMIT GATES

**SOURCE-CONFIRMED @e5d7f493d8, EXERCISED via `bash -x` (273 trace lines).**

```
:30, :151   set -euo pipefail
:718        _commit_out="$(git commit ... 2>&1)"   <- errexit TERMINATES THE SCRIPT AT THE ASSIGNMENT
:719        _commit_rc=$?                          <- ZERO trace lines. never executes.
:720-721    printf '%s\n' "$_commit_out"           <- ZERO trace lines. the message dies in the variable.
```

**OBSERVED SHAPE: rc=1, stderr EMPTY, stdout ending on `[risk-reflex] REFLEX CLEAN` — a DIFFERENT check's PASS.**

All seven `.git/hooks/pre-commit` gates are hook-side and therefore silenced: owned-paths · to-proof-of-spec ·
branch-content-isolation · jq-ban · mstr-ledger · rcg-manifest · rcg-sweep. safe-commit's OWN checks print `>&2`
directly and are loud — **that asymmetry is exactly why it reads as "sometimes silent."**

> ⛔ **WHY IT SURVIVED: THE GATES ARE LOUD WHEN TESTED AND SILENT ONLY WHEN USED.** A bare `git commit` inherits
> stderr, so every one of these is loud under direct testing — surely how they were exercised when built.
> **The test path and the production path differ on the one property under test.**

Routed to CTO with the patch (`if _commit_out="$(...)"; then _commit_rc=0; else _commit_rc=$?; fi`) and a **red-arm**
test, since a green-only test passes today. **Not implemented here — tooling lane.**

---

## 3. ⛔ THREE ATTRIBUTION ERRORS, MINE, EVERY ONE CAUGHT BY SOMEONE ELSE

| | what I claimed | the truth | caught by |
|---|---|---|---|
| **a** | the GLDRNS TO is *"still staged, nobody unstages it"* — said twice, to two seats | it was `??` **UNTRACKED**, having gone untracked in MSTR's merge. **I asserted a git state I had never read.** | me, on finally measuring |
| **b** | *"new-file-in-undeclared-lane"* is the refusal mechanism | falsified by a positive control in `DE~C`'s own equally-undeclared lane. The cause was `to-proof-of-spec-check`. | `0.4.0_DE_ClientPlatform~C` |
| **c** | ~H *"took the audited escape, to their credit"* | **CTO took it**, under `GIT_COMMIT_AUTHOR_OVERRIDE`, to preserve ~H's authorship. **I asserted a conduct fact about a seat too dark to answer.** | `1.0.0_SA_CTO` |

**(c) IS THE ONE THAT MATTERS AND ITS SHAPE IS NOT "MEASURE HARDER".** I ran a positive control, read the right file,
and quoted the row verbatim with its timestamp. **The defect was asking the artifact a question it does not answer.**

Source-confirmed: `to-proof-of-spec-check.sh:34` stamps `git var GIT_AUTHOR_IDENT` — **the AUTHOR, never the CALLER.**

⛔ **AND MY OWN CONTROL WENT FURTHER THAN THE REPORT I WAS CORRECTING: `git var GIT_AUTHOR_IDENT` at this seat returns
`Andrew Berman`.** That column is not a caller field **and not reliably a seat field** — it is git's author ident,
defaulting to the human's config. **An override audit whose actor column reads `Andrew Berman` by default, and reads a
DARK AGENT'S SERIAL when someone acts as them, is inverted on precisely the two cases it exists to separate.**

**`DS~G` then isolated it further, from a measurement taken for a different reason:** their `c35bc70a79` wrote a NEW
file into the same dead lane's folder with **no override and correct attribution**. **So the override was never
required for ACCESS — it was taken for ATTRIBUTION, and the row cannot distinguish those. The gate candidate closes
the WHO and not the WHY.**

**THE SEQUENCING LESSON I OWE DE~C:** their verdict was TRUE IN SUBSTANCE (~H made no override) and false in form.
**Mine was FALSE IN SUBSTANCE and true in form — the worse of the two.**
> **Bad evidence for a true claim is not a false claim, and treating it as one is how correct findings get retracted.**

---

## 4. RULED THIS WINDOW

| call | ruling |
|---|---|
| GLDRNS proof instance | **AC7 as the ONLY row.** I first ruled a value (`NOT-ATTESTED-BY-THIS-SEAT`) that is not in the closed enum AND put an attestation fact on a computability axis — **Rule 24(iii), four hours after amending a decomp for that same postulate.** CVO caught both, before the emit. Corrected after measuring `acceptance minItems: 1` and `coverage_check`'s expected-vs-carried frame. DS~G emitted @c35bc70a79; coverage reports `expected=7 carried=1` **exactly as ruled.** |
| AC1–AC6 | **DEFERRED past 12:45Z, then DS~G — as a re-derivation they actually run, never a transcription.** Rule 27 seating protects CONTEXT; honoured in sequence, not in parallel. |
| GLD-f-3 | **MINE, not DS~G's.** Filed the ABSENCE as an OPEN NEVER#6 item with a named owner. **Did not write the entry** — a ledger row authored by someone who did not perform the deploy is a reconstruction wearing a first-person record's clothing. |
| the held promote `a239e4a9` | **PRESERVE.** Asymmetry decides it, not merits: keeping costs one ref, dropping is irreversible. MSTR discharged the push same hour. |

---

## 5. ⛔ THE COO ALARM, DISCRIMINATED — AND THE ITEM I FILED WAS THE WRONG ONE

`deploy_ledger.py check --red` fired RED on the ETFS promote (19.8h against a 4.0h window, 6 stranded legs). **I
measured the legs rather than repeating the instrument:** merge SATISFIED · prod-push SATISFIED · tag SATISFIED ·
pointer SATISFIED-THEN-SUPERSEDED · ci UNMEASURED · teardown HALF.

**"Stranded" in this tool means NO PROOF RECORDED, which is not the same fact as NOT DONE — and the two take opposite
responses.** The promote is **not** half-landed. **The entry was opened at deploy-start and never touched again**
(its Log is one line). *An entry that cannot tell DONE-BUT-UNRECORDED from STRANDED will read identically on the next
real stranded deploy — the instrument is right to blare.*

⛔ **THEN MSTR, AND MY OWN FOLLOW-UP, SHOWED THE RESIDUE I NAMED WAS THE SYMPTOM:**

```
local  PROD  a239e4a9   <- the HELD 12:50Z attempt      rev-list --left-right --count PROD...origin/PROD
origin/PROD  a7a7ff16   <- what actually shipped             ->  local-only 1, remote-only 35
```

**A LOCAL CHECKOUT OF `PROD` DOES NOT CONTAIN WHAT IS ON PROD.** Rule 19's guard is HOLDING (main tree on DEV) and the
trap is one `git checkout PROD` away. **The worktree is visible and someone will trip over it; the divergent branch is
invisible, survives the worktree's removal, and is the part that actually misleads.** `DE~C` is the concrete instance:
**local PROD contains ZERO of their nine commits**, and they got their original number right only because CTO handed
them a HASH rather than a branch name.

And `parked/v2.1.165-etf-promote-held-20260824` was **LOCAL-ONLY** — *a preservation claim with no remote behind it,
the same shape as a commit reported as landed that sits on no branch.* **MSTR pushed it; that dependency is closed.**

---

## 6. THE CARD AT ANDREW MOVED TWICE, BOTH TIMES AGAINST ME

1. **CVO retracted their own "invisible sweep" framing**, which I had carried into the card. The promote WAS ledgered:
   the entry names `perfrp` 3× and the hash 7×, and the promoting seat recorded the passenger unprompted. **It mentions
   the HOLD zero times.** The gap is narrower and sharper: *the seat who noticed had no way to connect what they saw to
   a hold they had never been told about.*
2. **`7 of 9` → `9 of 9`**, independently verified here with a discriminating negative control, and `origin/PROD` moved
   again to `a7a7ff16` (v2.1.166) **while the call sat unanswered.**

> ⛔ **A SECOND PROMOTE LANDED WHILE THE CALL WAS OPEN. THE THING THE CALL ASKS ABOUT KEEPS HAPPENING WHILE THE CALL
> WAITS** — a branch-position hold does not merely fail to be enforceable, **it decays further with every unrelated
> release, and nobody has to make a mistake.** Neither promote was wrong.

**Recorded with its limit so the escalation is not read as growing on its own: both surfaces still render with ZERO
served data. More code is exposed; the exposure is still not a wrong answer to a client. The de-escalation stands.**

---

## 7. Compiler Tools

| Tool | Result | Lesson |
|---|---|---|
| `bash -x` on the wrapper | found the exit point in ONE run | **when a script refuses silently, TRACE it — do not read it and hypothesise.** I read four `exit 1` blocks first; every one was a wrong guess |
| `deploy_ledger.py check --red` | RED, correctly | **it disclosed its own denominator — `2 of 2 sentinels`.** It enumerates `.open_deploys/*.json`, so an entry that never OPENED is invisible to it. Documented at `:85-90`; not my discovery |
| `git merge-base --is-ancestor` | settled 3 legs, the pointer question, and 9-of-9 | the cheap discriminator between *stranded* and *superseded* |
| `git var GIT_AUTHOR_IDENT` | returned `Andrew Berman` | **the control that made my finding sharper than the report I was correcting** |
| grep-the-claim-before-commit | caught the retracted phrase; flagged 1 survivor | the survivor was **my own deliberate quotation** of it — the control fires on quotes too, and that is correct |
| `check_inbox` (MCP) | 1,392,469 chars — refused | at this volume, read the inbox files from disk; the tool call is the expensive path |

---

## 8. For the next seat

1. **12:45Z IS UNCHANGED AND NOBODY ACCELERATES IT.** AC7 has somewhere to land (@c35bc70a79).
2. **CTO holds the promote ledger** (DT is dead). Remaining order: correct local `PROD` → prune the worktree → close
   the legs with the proofs in 69743. **The one real dependency — pushing the parked tag — is discharged.**
3. **ONE call stands at Andrew** — the 08-21 Opal-membership backfill. **The PERFRP-on-PROD card is CLOSED** by his
   ~08:5xZ word *"I'm fine with it on PROD, let's just get the data part sorted"* (@3a6af2a355). **He released the
   BRANCH half and KEPT the DATA half — the publish gate stands; this is not a general lift.**
4. ⛔ **MY HOLDS — TESTED, AND TWO OF FOUR WERE STALE.** `COT_CANON458`: registration **and** PRD are BOTH discharged
   (`org/projects/COT_CANON458.json`, `docs/architecture/COT_CANON458_PRD.md`); **7 cells are executable now**, seating
   deferred on capacity, emit still STOPPED. `ADVI_INSURE`: **CERTIFIED @7397dfd83e at 00:01:03Z, on origin/CLOUD AND
   origin/SITEZ — I carried it as pending for NINE HOURS.** `CAP`: genuinely pending (no project JSON, no PRD) — that
   one was accurate. `STITCH`: unseated by choice. **A hold whose blocker is cleared BY SOMEONE ELSE never notifies the
   holder — treat every line of a holds list as a claim under test, not as a record.**
5. **CRO remains off-limits this session.** Alternate certification signer is base `1.0.0_SA_CTO` only.
6. **Re-measure push state before quoting it.** Everything in this log is now on `origin/CLOUD` (measured ~09:3xZ after
   an explicit `git fetch`). *"LOCAL @hash, rides integration"* is right at authoring and **goes stale silently** — say
   it, then check it again before you repeat it.

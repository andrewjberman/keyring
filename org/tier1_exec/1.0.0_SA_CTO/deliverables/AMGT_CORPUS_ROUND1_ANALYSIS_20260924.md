# AMGT_CORPUS -- ROUND 1 ANALYSIS (L10). ROUND 1 CLOSES; ROUND 2 IS ADDENDUM A

**Author** `1.0.0_SA_CTO~Z`, 2026-09-24 ~06:2xZ. **On** `3.0.0_SA_CVO~Z`'s L10 slug (msg 25288),
`ADJUDICATION_v4` @`96cbb2908d`, row `AMGT_CORPUS-Z-S11` @`0c2ccdf04b`. **Recut owner** `2.0.0_SA_COO~X`.

## 1. ROUND 1 IS TERMINAL, AND THE SLUG RE-MEASURED IT RATHER THAN ADOPTING IT

At `373c431072`: **11 order files, 11 carrying exactly ONE anchored status tag, 11 `complete`, 0 non-terminal.**
⭐ **And the slug states WHY the two possible reads cannot disagree** -- no order carries a second tag, so the
anchored read and the last-tag read coincide. **That is the discriminator this project has been bitten by before
and it was closed before it could be asked.**

**L9 on `CRPS-c-11` AC5: PASS on both questions, SCOPED.** Coverage exact by subtraction from the FULL file
denominator rather than the `.py` glob the census itself uses -- `git ls-tree` 30 files / 30 `.py` / 0 non-`.py`
against `files_scanned 30`, **so no fixture or data file can hide in the gap between the two denominators.**

## 2. ⛔ THE FINDING THAT LEADS THE ENRICHMENT LIST: AN INSTRUMENT WHOSE PERMISSIVE BRANCH HAS NO CONTROL

`readonly_proof.py:301` -- `reaches = LIBRARY in origins or (not is_test and UNKNOWN in origins)` --
is **fail-CLOSED for library code and fail-OPEN for test files.** Of the 27 flagged calls, **10 non-test sites are
a positive determination and 17 test sites read `origins ['unknown']`, `reaches_library False`, which is a DEFAULT
AND NOT A MEASUREMENT.**

⛔ **AND THE POSITIVE CONTROL PLANTS INTO `positive_control.py`, WHICH IS NOT A TEST FILE, SO IT TAKES THE
DETECTING BRANCH. THE EXEMPTING BRANCH HAS NO CONTROL AT ALL.** ⭐ **A control that exercises only the branch that
FIRES certifies nothing about the branch that EXEMPTS** -- and the exempting branch is where 17 of 27 sites landed.
**The scanner cannot fail on a test file, so its silence there is structural.**

⭐ **WHAT THE CVO DID INSTEAD IS THE MODEL AND IT IS WHY THE PASS STANDS: it established by hand the ground truth
the instrument declined to establish**, reading all 17 sites and finding every one rooted in pytest's `tmp_path`.
**The verdict rests on a human read, and the slug says so rather than letting the scanner's `False` carry it.**

⚠ **AND AC5's SCOPE IS NARROWER THAN IT READS:** it asks whether every call **IN THE LIST** is correctly judged,
never whether **THE LIST IS COMPLETE.** Rows `Z-S7/S8/S9` record **three successive rounds of binding-form false
negatives in this same scanner, each found by an independent reviewer rather than by the scanner's own controls**,
and `Z-S9`'s own standing is *"H re-review NOT_EVALUATED, prior scanner FAIL remains."* **Three independent catches
is a rate, not a coincidence.**

**WHAT CARRIES THE WEIGHT IS AC2's RUNTIME ARM ON A DIFFERENT INSTRUMENT:** `write_denied_probe PermissionError`,
`ingest_rc 0`, `stored 123`, `put_performed 0`, `existed 123`, `read_failed 0`. **EXPOSURE, not incident** -- every
ARMED row closes *"no actual source-library mutation inferred."*

## 3. ⛔ ONE DEFECT IS THIS SEAT'S, IT IS THE FOURTH INSTANCE OF ONE CLASS TONIGHT, AND IT IS ALREADY REMEDIED

`AMGT_CORPUS-Z-S11`: **every new and amended CONTRACT in both addenda hashed into the BRIEF half.**
`prd_signoff_lib.py:34` sets `RATIFIED_SECTIONS = ("ENDPOINT","CONTRACTS")`, matched on the heading's **FIRST
WORD** (`_first_word`, `:88-90`, backtick-insensitive), and my sections were headed `A.4`, `A.5`, `B.4` -- so
**one amendment to a HARD vendor-egress contract (`C-NO-VENDOR-CALL`) and EIGHT newly minted `C-` contracts sat
outside the bytes the CVO signature binds**, on a half the spine assigns elsewhere while assigning CONTRACTS to
the CVO *"always."*

⭐ **THE CVO'S OWN FRAMING IS THE LESSON AND IT IS SHARPER THAN A RESTATEMENT WOULD BE:** *"You solved the
identical carrier question for OUTCOMES in the same commit -- both fences say in terms that they are the only
carrier -- and the same care did not reach the contracts."* ⛔ **I FIXED THE CARRIER FOR THE THING I WAS LOOKING AT
AND NOT FOR ITS SIBLING, IN THE SAME EDIT.** R-26a -> R-27a -> R-32 -> this: same class, four times, and this is
the first instance where the correct fix was already in my hands and was applied to only one of two objects.

**REMEDIED AS THE CVO DIRECTED -- BUILD THE GUARD, NEVER RE-OPEN THE ADDENDUM.** The three headings are renamed so
their first word is `CONTRACTS`; substance is byte-unchanged. **VERIFY-AFTER on the real library, not the
description: contract-bearing sections read 5 RATIFIED-TEXT / 0 BRIEF.**
⚠ **THIS DELIBERATELY RE-OPENS THE RATIFIED HALF, AND THAT IS THE POINT** -- the bytes had to move INTO the half
the signature binds, so the just-signed half at `215e060a3b` is stale BY DESIGN and a re-sign is owed at the new
bytes. **Per R-10 no round is held on it.** ⭐ And the CVO's read of the nine contracts as sound is what makes this
an EXPOSURE rather than an incident: **nothing was admitted, so nothing re-opens.**

## 4. WHAT ELSE THE SLUG SETTLED, CARRIED SO NO CELL RE-DERIVES IT

- **L4-R: BOTH ratified halves SIGNED AND CURRENT** @`215e060a3b`, bound with `--expect-half-hash` *"so neither
  signature can silently bind to bytes I did not read."* ⭐ **`2.0.0_SA_COO~Z` NO LONGER NEEDS the audited
  pipeline-override it proposed** -- `prd-signoff` routes the ratified half to the CVO lane as live, which is the
  condition that seat named as missing. **The override should not be used.**
- **The nineteen new outcomes all grade EXERCISED** with a reader-language ACCEPT.
- ⭐ **`FWD-19`'s population is MECE over a printed denominator AND SUMS: 22 + 11 + 60 = 93, graded DISPOSITIONED
  rather than populated** -- the distinction ADDENDUM A insisted on, independently reproduced.
- **H03 served leg:** both 09-23 `_CURRENT` items byte-identical against pre-act pins, **with the discriminator
  that the change demonstrably landed** (`CodeSha256 I6eitcaI -> Xdwp7IrP`, size 669,924 -> 55,418,293, 128 -> 512,
  60 -> 120, `CHATTER_AXIS_SOURCE=legacy` read directly). ⛔ **Arm (b) is NOT measurable yet and must not be
  forced: a non-dry-run ad-hoc fire WOULD WRITE the 09-24 pointer and DESTROY the retained-pointer
  discriminator.** The leg stays open until 10:00Z. **That is the "ad-hoc would destroy the discriminator"
  exception CLAUDE.md names, and it is correctly invoked.**
- **Peers B04/P1** @`dab9d1238f`: consumer 2 PASS, case 1 PASS on both arms, case 2 PASS **scoped to OFFLINE**.
  ⚠ One artifact disclosed: the reactive PNG is filed under `CAT` while its panel shows `BA`, because a synthetic
  `pushState` + `popstate` did not drive the router -- **so that arm did not exercise the different-security case
  it appears to.** Not a grade change; a named limit.

## 5. ⛔ A THIRD LAYER ON FAILURE CASE 3, AND IT OUTLIVES THE FIX

R-30 ruled two layers (gateway route + handler decode). **The slug found a THIRD and it is the one that survives
the repair:** the `BP` render has **no error state and no terminal state at all -- three panels reading
"Loading..."** -- and it is **not a premature capture** (networkidle 60 s, `waitForSelector` 20 s,
`waitForLoadState` 30 s, then 1,200 ms). The mechanism is a **retry loop: 10 `BP` calls across ~6 s over three
routes, the last firing 2.07 s AFTER the trace's own `finished_at`.**

⛔ **SO A 404 ON THESE ROUTES PRODUCES AN INFINITE SPINNER RATHER THAN ANY TERMINAL STATE, AND THE SLASH-KEY REPAIR
WOULD REMOVE TODAY'S TRIGGER WHILE LEAVING THAT BEHAVIOUR IN PLACE -- UNTESTED AND UNREACHABLE BY THE ONE CASE THAT
EXPOSED IT.** ⭐ **That is the same shape as §2's uncontrolled branch: fixing the trigger retires the only test of
the handler.** **R-30 IS AMENDED: the parked act gains a THIRD clause -- a 404 on a security route renders a
TERMINAL state** -- and it is graded independently of the slash-key repair, because the repair removes its trigger.

## 6. THE ENRICHMENT LIST ROUND 2 CUTS

**ROUND 2 FOR `AMGT_CORPUS` IS ADDENDUM A ITSELF** (`FWD-10`..`FWD-19`, PRD v0.6/v0.7, already cut) -- **not a
re-opened round 1.** These ride it as enrichment:

1. **A CONTROL FOR THE EXEMPTING BRANCH** at `readonly_proof.py:301` -- a planted violation in a **TEST FILE**,
   which must be DETECTED or the exemption must be justified. ⭐ **Highest value on the list: it is the only item
   that makes the scanner able to fail where 17 of 27 sites live.**
2. **The `H` re-review** (`Z-S9`, `NOT_EVALUATED`, prior scanner FAIL stands) -- the fourth binding-form pass, and
   the first three were each found by a reviewer rather than by the scanner.
3. **`Z-S6`'s period ordering.**
4. **The contract-half GUARD** -- a check that refuses a PRD whose `C-` contracts classify `brief`. ⭐ **This
   round's own defect turned into a mechanism, which is the only durable form of a correction.**
5. **The router-driving fix** for the reactive arm, so the different-security case exercises what it claims.

⛔ **FOUR ROWS STAY ARMED AND ALL FOUR ARE `2.0.0_SA_COO~X`'s. A GRADE IS NOT A DISARM** -- the slug says so
explicitly and this analysis does not convert one into the other.

**CLOSED WHEN** every `FWD` in scope grades REALIZED. ⛔ **Round 1 closes; nothing in it re-opens.**

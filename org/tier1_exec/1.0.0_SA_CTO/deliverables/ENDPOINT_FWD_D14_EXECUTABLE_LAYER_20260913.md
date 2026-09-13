# ENDPOINT (step 2, `/endpoint --forward`) -- D14, the executable layer

> **NOT YET LANDED IN A PRD, AND THIS PROJECT CANNOT YET BE REGISTERED.** `org/missions/MACROS.yaml`
> carries a macro enum for seven directives -- D0, D5, D8, D9, D11, D12, D13 -- and **D14 is not among
> them.** `.tools/missions-tree-index.py:249-251` refuses any tree registration whose directive has no
> entry there. So neither D14 brief can pass L3 until a D14 enum is proposed with its Rule 24 record and
> ratified -- **and ratification is Andrew's alone.** Target section once L3/L4 run: `ENDPOINT (step 2,
> /endpoint --forward)` in this project's PRD.

**Cut by:** `1.0.0_SA_CTO` (L2), 2026-09-13.
**From:** `docs/briefs/d14-executable-layer-brief-20260913.md` @`fd579d3caf`, 20,292 bytes; that is the
file's latest commit. Author `4.0.0_SA_CRO~D`. Eight top-level headings, denominator printed. Seven outcomes
in Part I; FIVE bars in Part III.
**It consumes the naming brief** (@`bf21181208`), and the two are cut together: that endpoint's FWD-5 hands
its machine-run bar to this one's FWD-5.
**Andrew has NOT read this brief.** His 2026-09-03 word is that he confirms the CTO's DONE WHEN from this pass.

---

## AMENDMENT RECORD -- L1 FIXES ABSORBED 2026-09-13 ~06:1xZ (brief now @`1b42dbe758`)

**Measured @`fd579d3caf` -> @`b9335371e1` -> @`1b42dbe758`: Part I DIFFERS at both steps (O2's wording only), Part
III EQUAL at both, every other part EQUAL. No FWD id and no bar moves.**

- **s.1 RESOLVED.** The two D14 briefs no longer disagree: O2 now says `name()` takes the LONG key and emits the SHORT
  form, labelled PROPOSED and L4-ratified by this seat since @`1b42dbe758`. The first fix had called it ruled by Andrew;
  the naming endpoint's amendment record carries that correction.
- **s.2's consequence is now written into the D8 migration brief's Part II:** its registry-runtime claim is struck as
  superseded by ruling (a), and the D8 endpoint's FWD-3 is named as the second D14-before-D8 item.

---

## THE SEVEN OUTCOMES

```
  FWD-1  A pipeline never writes out where its data goes; it asks for the address
         and is given it
         DONE WHEN  EXERCISED -- a new pipeline for a new firm has been written this
                    way and a reviewer has checked it
         ACCEPT     a new pipeline for a firm never set up before is written without a
                    single storage location typed into it by hand, and a reviewer can
                    confirm that by searching its code -- where today every pipeline
                    carries a settings file with a storage location typed into it
         SOURCE     brief Part I O1; bar Part III O1

  FWD-2  Nobody creating infrastructure types its name; it is produced from one rule,
         and the rule keeping firms apart is produced from the same source
         DONE WHEN  EXERCISED -- a real piece of infrastructure has been named this way,
                    and the separation rule was produced from the same source and matched
         ACCEPT     someone setting up a new piece of infrastructure has its name produced
                    for them rather than typing it, and the rule keeping one firm's systems
                    away from another's comes from the same source -- so changing how a firm
                    is spelled changes both at once -- where today the name is typed by hand
                    and the separation rule is a separate hand-kept list of spellings
         SOURCE     brief Part I O2 -- NO Part III bar; cut from Part I alone (s.5)
         DEPENDS    the fence re-derivation, open at Andrew; and L4's form split (s.1)

  FWD-3  Everything that needs to know where a firm's data lives reads it from one
         list, and moving a firm is one change to that list
         DONE WHEN  EXERCISED -- someone has changed one firm's entry and watched every
                    dependent place follow in a single build
         ACCEPT     someone changes where one firm's data lives in a single list, and in one
                    build every place that routes, guards or maps that firm's data follows;
                    the five separate lists kept by hand today are either produced from the
                    one list or gone
         SOURCE     brief Part I O3; bar Part III O3

  FWD-4  Any change that writes a storage address or a name the rule would not have
         produced is stopped, and the stop says what the correct form is
         DONE WHEN  EXERCISED -- a deliberately wrong change has been stopped with the
                    correct form printed, and a correct one let through
         ACCEPT     someone tries to save a change containing a hand-typed old-style storage
                    address and it is refused, with the correct address printed in the
                    refusal; the same change written correctly goes through; and an old
                    spelling that is still permitted goes through with the correct spelling
                    printed beside it, so existing work keeps running -- where today the only
                    such check is a hand-kept list that stops protecting the moment a name
                    changes
         SOURCE     brief Part I O4; bar Part III O4

  FWD-5  Anyone can run the check over the whole estate and get the complete ranked list
         of names and addresses that break the pattern, each with its fix
         DONE WHEN  EXERCISED -- the full run has been done and its totals compared with
                    the hand-made ranking
         ACCEPT     someone runs the check over everything -- the stored code and what is
                    actually running -- and gets a ranked list of every name and address that
                    breaks the pattern, each paired with its correct form, totals shown; the
                    totals agree with the ranking the naming work produced by hand; and a name
                    the check cannot read stops the run loudly rather than being filed as
                    breaking the pattern -- this is the list clean-up projects start from
         SOURCE     brief Part I O5; bar Part III O5; CARRIES the naming endpoint's FWD-5
                    machine-run bar (s.6)

  FWD-6  A clean-up project cannot quietly stall half-done
         DONE WHEN  EXERCISED -- shown deliberately on a practice copy, with a clean-up
                    planted for the purpose
         ACCEPT     on a practice copy, a clean-up is set up that owns one area still
                    holding an old-style name, and a change touching that area without
                    removing the name is refused -- driven on purpose rather than waiting for
                    a real clean-up to stall; the first real clean-up project doing the same is
                    the confirmation, never the proof -- where today "we meant to fix it"
                    becomes a forgotten ticket
         SOURCE     brief Part I O6 -- NO Part III bar; cut from Part I alone (s.5)

  FWD-7  Taking on a new firm is one entry in one list, and everything else is produced
         from it
         DONE WHEN  EXERCISED -- a demonstration firm has been added on a practice copy and
                    every produced file checked
         ACCEPT     on a practice copy, a demonstration firm is added as a single entry and
                    every file that ought to change does, exactly as expected; and anywhere
                    someone types that firm's name by hand instead, the change is refused --
                    where today every new firm means editing its name into many places by hand
         SOURCE     brief Part I O7; bar Part III O7
```

---

## SIX THINGS THE CUT SURFACED

### 1. THE TWO D14 BRIEFS DISAGREE ON WHICH SPELLING GOES IN A RESOURCE NAME

This brief's O2 builder emits **`mdpf-cot-publisher-role`** -- the SHORT form, in an IAM role. The naming
brief's IV.2 lists the LONG forms as the scope keys for resource names. Andrew kept one sanctioned short form
per firm (~03:5xZ) but no section of either brief says which form goes where. **Either split, applied by a
builder, gives one spelling per slot; mixing them gives two, and then FWD-2's "the separation rule follows the
spelling" produces a pattern per spelling.** REC for the one-document L4 ratification: THIS brief's split --
short in every resource name, long in bucket names and key scope segments -- because it follows his ruling as
written. The full reasoning is the naming endpoint's s.1; this is the same finding from the other side.

### 2. ⛔ THIS BRIEF AND THE D8 MIGRATION BRIEF BOTH CLAIM TO OWN THE FIRM REGISTRY -- AND THAT CHANGES THE ORDER

This brief, Part II: OWNS *"the registry file and its generated views (O3)."* The D8 legacy-firm-buckets
brief, Part II: OWNS *"the identity-spine RUNTIME and the repoint of every firm-naming consumer to it (O3)."*
**Two projects, in two directives, each owning one thing.**

Andrew's remediation ruling (a) at ~03:5xZ settles it: **D14 owns the rule, the REGISTRY, the builders and the
flagger; each fix is minted where the resource lives.** The D8 brief was written at ~02:2xZ, before that ruling,
so its runtime claim is superseded and its REPOINT claim stands.

⭐ **CONSEQUENCE FOR THE QUESTION ANDREW ASKED -- "do we need to do D14 items first?"** `4.0.0_SA_CRO~D`'s answer
(96341) was that D8 needs nothing from D14 except the fence. **That is true of D8's KEYS and not of its registry
outcome.** The D8 endpoint's FWD-3 -- *every consumer that needs a firm's location reads one place* -- cannot be
met until THIS project's registry exists. **So there is a second D14-before-D8 item, scoped to one D8 outcome:**
the registry, ahead of D8's FWD-3. D8's other seven outcomes stay independent of it.

### 3. FWD-4 IS THE ENFORCEMENT THE CANON ENDPOINT SAID WAS MISSING

The D14 canon endpoint (@`ddf93b2165`) put a question to Andrew: none of its six outcomes makes the canon
ENFORCED -- is enforcement deliberately outside D14, or a gap? **This brief is the answer.** Its O4 refuses a
change the builder would not have produced, and its O6 refuses a clean-up left half-done. Andrew commissioned
it by name at ~03:2xZ (*"TWO briefs ... the EXECUTABLE-LAYER brief -- key/name builders off the identity spine, a
flagger at safe-commit/safe-apply"*, relayed 96332, "all recs approved"). **So enforcement is inside D14 by his
word, and that open question is closed rather than carried.**

### 4. PART V PRESENTS A MECHANISM THAT IS STILL OPEN

Part V's first bullet makes the fence re-derivation a MUST-BE-TRUE, with a specific mechanism: *"deny any
principal whose scope token is not the bucket's firm."* That mechanism is **not ruled at L4** -- it changes the
control Andrew ruled on with "C", so it goes to him as one card (this seat's reply to `4.0.0_SA_CRO~D`, msg 96342).
And its shared-principal branch is undecided: under the naming schema a shared resource has NO scope token by
design, and today three unscoped roles write these buckets, one of them feeding live-served client platinum.
**FWD-2 depends on how that card is answered.**

### 5. TWO OUTCOMES HAVE NO BAR -- AND ONE WAS CUT TO AVOID A TRAP

Seven outcomes, five bars (O1, O3, O4, O5, O7). **O2 and O6 are unbarred.** FWD-6 needed care: its natural proof
is a real clean-up project stalling and being refused -- **the same "met only by a project that does not exist yet"
shape that caught the canon and naming endpoints' FWD-6 tonight.** Rule 27's answer is to drive the mechanism
deliberately: FWD-6 is proven on a practice copy with a clean-up planted for the purpose, and the first real
project is the confirming arm. That keeps it gradeable inside this project.

### 6. THE NAMING ENDPOINT'S MACHINE-RUN BAR LANDS HERE, AS PROMISED

The naming endpoint re-cut its FWD-5 to the hand-applied specification because the grader is built here. **Its
machine-run bar -- every one of the 1,912 nameable live names judged -- is this endpoint's FWD-5.** The two FWD-5s
are the specification and its machine: one project's outcome each if the briefs register separately, one project's
two outcomes if they register together. **That registration choice is L3's, and L3 is blocked on the D14 macro
enum** (header). ⚠ The three-verdict set is sound only if an unreadable name stops the run loudly; FWD-5's ACCEPT
line says so, because otherwise "could not read it" and "breaks the pattern" become one answer.

---

## PROVENANCE

**READ, @`fd579d3caf`, from the record:** Part I, II, III (lines 25-108); Part V, VI, VII (183-end, with REFS).
**Also read, for the cross-brief findings:** the naming brief's IV.2 and IV.3 (@`bf21181208`); the D8
legacy-firm-buckets brief's Part II (@`2ffcf91342`, read at this seat's earlier cut); `org/missions/MACROS.yaml`'s
directive list, parsed this session (7 directives).

**NOT READ:** Part IV (109-182), including IV.2's five partial registries and IV.5's refuse/warn matrix. Part VII
names its own gaps, and three bear on FWD-4 directly: **`ds-precommit-check.py`, `commit-gate.sh` and `safe-apply`'s
internals were not read** -- so where the refusal is inserted is L5's read, not this brief's claim.

**NOT CLAIMED:** that these are the outcomes Andrew wants -- his confirmation, per his 2026-09-03 word. That the
form split in s.1 is settled. Or that the moratorium is at risk: every refusal here is a gate's exit and a printed
line; nothing in these seven outcomes sends a message to anyone.

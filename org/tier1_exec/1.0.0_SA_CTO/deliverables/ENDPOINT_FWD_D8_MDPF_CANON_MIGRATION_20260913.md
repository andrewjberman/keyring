# ENDPOINT (step 2, `/endpoint --forward`) -- D8, MDPF canon migration

> **EMITTED STANDALONE, DELIBERATELY -- EVEN THOUGH A PRD EXISTS.** The skill says an endpoint goes
> INTO an existing PRD, and `docs/architecture/MDPF_CANON_PRD.md` v1.0 exists. It is not inserted,
> for two reasons, both stated in s.1 below: **(1)** Rule 27 puts L4 after L3 and `MDPF_CANON` is
> unregistered; **(2)** that PRD's s.2 and AC5 CONTRADICT two of these outcomes, so inserting them
> would make the PRD disagree with itself. Target section once L4 runs: `ENDPOINT (step 2,
> /endpoint --forward)` in `MDPF_CANON_PRD.md`.

**Cut by:** `1.0.0_SA_CTO` (L2), 2026-09-13.
**From:** `docs/briefs/d8-mdpf-canon-migration-brief-20260913.md` @`c2884cbb19`, 29,273 bytes
(worktree and record read separately; they agree). Author `4.0.0_SA_CRO~D`. Nine top-level headings,
denominator printed -- **including a Part 0**, which records how the brief's blind constraint was
honoured and where it bent; read, and its bends are named rather than hidden.
**Directive:** D8, confirmed by Andrew ~03:2xZ (relayed 96332). **The PRD's header still says D10** --
one of three stale items in it (s.1).
**Andrew has NOT read this brief.** His 2026-09-03 word is that he confirms the CTO's DONE WHEN from
this pass.

---

## THE EIGHT OUTCOMES

```
  FWD-1  Anyone can tell how current any model-portfolio figure is from where it is
         kept, and every one of them is kept in the one place built for them
         DONE WHEN  EXERCISED -- someone has actually answered a dated question this way
         ACCEPT     asked "what did 49 Financial's total assets read on a particular day
                    last month", someone answers from the name of the stored file alone,
                    without opening it -- and every stored figure of this kind is in the
                    same one place, full history, one addition per day -- where today the
                    same figures sit in two places under two different naming habits, and
                    the place meant for them is empty
         SOURCE     brief Part I O1; bar Part III O1; PRD AC1, AC6

  FWD-2  A firm's advisors read their model-portfolio figures from that firm's own
         storage, and another firm's advisors cannot reach them even with the address
         DONE WHEN  EXERCISED -- someone has deliberately tried to reach one firm's
                    figures while signed in as another, and been refused
         ACCEPT     someone signed in as an Inflection advisor, holding the exact address
                    of 49 Financial's figures, tries to open them and cannot, because they
                    live in storage that is not Inflection's -- and a 49 Financial advisor
                    opening the same page sees their own figures exactly as before -- where
                    today all three firms' figures sit side by side in one shared place
                    that any signed-in advisor's page may ask for
         SOURCE     brief Part I O2; bar Part III O2
         DEPENDS    that firm's own storage existing and able to serve -- the sibling
                    migration's delivery, per firm (an act, not a wait; see s.5)

  FWD-3  The combined all-firms figure stays where it is, and anyone can read the
         written reason why
         DONE WHEN  EXERCISED -- someone asked why it did not move has pointed at the
                    written reason
         ACCEPT     someone asked why the combined figure across all firms was not moved
                    into any one firm's storage points at a written explanation of why it
                    reveals nothing about any single firm's clients -- so nobody moving data
                    later sweeps it into one firm's storage by mistake -- where today that
                    explanation is owed and not written
         SOURCE     brief Part I O3 -- NO Part III bar; cut from Part I alone (s.3)

  FWD-4  The one step that turns stored figures into what the page shows reads only
         from the model-portfolio store, and what people see does not change
         DONE WHEN  EXERCISED -- the before-and-after comparison has been run and read
         ACCEPT     someone compares what the page shows before and after the switch and
                    finds every figure identical -- comparing the figures people actually
                    read, never the timestamps that change every day anyway -- and the step
                    that prepares the page takes its input from the model-portfolio store
                    and nowhere else; it is the LAST thing switched over, not the first
         SOURCE     brief Part I O4; bar Part III O4; PRD AC3, AC7

  FWD-5  Everything that produces model-portfolio figures writes to the model-portfolio
         store and reads its raw inputs from the shared intake, and none of its working
         code is kept anywhere else
         DONE WHEN  EXERCISED -- the search has been run and read
         ACCEPT     a search of everything that builds these figures finds nothing still
                    writing to, reading from, or running code out of the old places -- any
                    leftover mention is history, not a live instruction -- while the saved
                    copies kept for rolling back stay exactly as they are
         SOURCE     brief Part I O5; bar Part III O5; PRD AC2, AC8

  FWD-6  A dedicated runner writes each firm's figures into that firm's storage, and
         the rule keeping firms' data apart was never loosened to allow it
         DONE WHEN  EXERCISED -- a run for one firm has written into that firm's storage
                    with the separation rule unchanged
         ACCEPT     a run for one firm writes that firm's figures into that firm's own
                    storage, and the rule stopping one firm's systems touching another
                    firm's data is word-for-word what it was before -- nobody loosened it to
                    make the run work -- where today the shared runner would be turned away
                    from that storage by that very rule
         SOURCE     brief Part I O6; bar Part III O6
         DEPENDS    as FWD-2, per firm

  FWD-7  Model-portfolio raw vendor data is received in the same place as everyone
         else's
         DONE WHEN  EXERCISED -- the receiving step has been run on demand and its output
                    read where it landed
         ACCEPT     the step that receives model-portfolio raw data is run deliberately and
                    its output lands in the shared intake alongside every other vendor's --
                    the next routine daily delivery landing there too is the confirmation,
                    never the proof
         SOURCE     brief Part I O7 -- NO Part III bar; cut from Part I alone (s.3)

  FWD-8  The two old copies are gone, and the protective hold no longer points at
         something that does not exist
         DONE WHEN  EXERCISED -- the retirement proof has been produced and read
         ⚠ INHERITS THE SIBLING'S DECOMMISSION STANDARD -- the brief says so itself (s.4)
         ACCEPT     before either old copy is removed, someone shows a record that nothing
                    read or wrote it for the agreed stretch, from a named instrument rather
                    than a list of the readers anyone happened to know about; and the
                    protective hold either points at the thing it exists to protect or is
                    formally closed with the reason written -- where today it names something
                    already gone while the real thing it should protect is written every day
         SOURCE     brief Part I O8 ("Decommission is a proof (sibling O6)"); bar Part III
                    O8 (which covers the hold half only); PRD AC4
```

---

## ⛔ FIVE THINGS THE CUT SURFACED

### 1. MY OWN PRD CONTRADICTS TWO OF THESE OUTCOMES -- AND THE PRD IS THE STALE PARTY

`MDPF_CANON_PRD.md` v1.0, **author `1.0.0_SA_CTO`**, opened 2026-08-25. Read at HEAD: its s.2 target
table sets `PLATINUM opal-data-portal-v2/platinum/mdpf/{scope}/ ... (unchanged, already conformant)`
and `COMPUTE ... (unchanged, already conformant)`, then says in bold that **"TWO TIERS ARE ALREADY
CORRECT AND ARE OUT OF SCOPE: PLATINUM AND COMPUTE."** AC5 makes it gradeable: *"Compute and platinum
tiers untouched. Any change there is a defect of this project."*

**So AC5 does not mean "platinum's SHAPE is untouched" -- s.2 names platinum's HOME and puts it out of
scope.** That settles the question I opened this cut to answer, and it answers it the uncomfortable
way:

| outcome | what it moves | AC5 as written grades it |
|---|---|---|
| FWD-2 | firm platinum slices, portal-v2 -> each firm's bucket | **DEFECT** (platinum touched) |
| FWD-6 | a new dedicated runner writing platinum per firm | **DEFECT on both axes** (platinum AND compute) |

**The brief is right and the PRD is stale.** Law moved after 2026-08-25: Andrew's 2026-09-12 ~16:01Z
ruling put client platinum per firm; Rule 17b was amended to per-tenancy platinum; his 09-12 ~13:4xZ
word asked for the dedicated runner. The PRD predates all three. **Three stale items in a document
this seat authored:** s.2's platinum and compute lines with AC5; s.3's layout
`opal-data-mdpf/gold/{scope}/{artifact}/date=...`, displaced by his ~03:2xZ source-first ruling; and
the header's directive (D10, now D8). **All three are L4 amendments and all three are mine.** They
are named here rather than fixed, because Rule 27 puts L4 after L3 -- and because a PRD edited to
agree with an endpoint in the same breath as the endpoint is cut is the builder grading its own work.

### 2. THE PRD'S NINE ACCEPTANCE CRITERIA AND THESE EIGHT OUTCOMES DO NOT COVER EACH OTHER

By subtraction, both directions, from printed denominators (9 ACs; 8 outcomes):

```
  AC1, AC6  -> FWD-1        AC2, AC8 -> FWD-5        AC3, AC7 -> FWD-4        AC4 -> FWD-8
  AC5       -> CONTRADICTS FWD-2 and FWD-6 (s.1)
  AC9       -> NO OUTCOME   (every silver-to-gold seam passes /seams, grounded on the DEPLOYED artifact)
  FWD-2, FWD-3, FWD-6, FWD-7 -> NO AC
```

**AC9 is the one to watch.** It is the control that would have caught the 08-25 outage -- a
deployed-versus-repo divergence -- and **the brief carries no outcome it would serve.** I have not
invented an FWD for it: L2 cuts from the brief and nowhere else. At L4 it either becomes a control
beneath FWD-5 or it is dropped, and **dropping it should be a decision someone makes, not a gap
nobody noticed.**

### 3. TWO OUTCOMES HAVE NO BAR IN THE BRIEF

Part I carries eight outcomes; Part III bars six (O1, O2, O4, O5, O6, O8). **O3 and O7 are unbarred.**
FWD-3 and FWD-7 are cut from Part I alone, and their DONE WHEN lines are mine rather than the brief's.
FWD-7 drives its mechanism deliberately (run the receiving step on demand) and keeps the routine daily
delivery as the confirming arm -- Rule 27's shape, and the same one applied to the sibling's FWD-4.

### 4. FWD-8 INHERITS THE SIBLING'S QUIET-WINDOW PROBLEM -- AND IT REACHES THE MONOLITH

The brief ties O8 to the sibling's standard in its own words: *"Decommission is a proof (sibling O6)."*
So FWD-8 inherits the D8 migration's FWD-6 in full: **a zero-reader claim is an absence claim, and an
absence claim needs an instrument that could have recorded the presence.**

The two retiring trees -- `gold/mdpf_revamp/` and `portal/gold/mdpf/` -- sit in `opal-data-assets`, the
estate's largest bucket. **This seat read the only CloudTrail read-side S3 data selector in full at
~03:1xZ tonight: its values are exactly two, `opal-data-bd/` and `opal-data-inf/`. `opal-data-assets`
is not among them.** (The trail denominator -- two trails -- is `3.0.0_SA_CVO`'s count, cited as
that seat's.) **S3 server access logging and request metrics on `opal-data-assets` were NOT measured**
by anyone; the CVO's sweep covered bd, inf and cot only. So of the three bucket-side instruments that
could bound this absence claim, one is measured absent and two are unmeasured.

**Part V's "every reader is named before either is retired" is a NAME census** -- consumer-side, which
proves presence and never absence. **The ACCEPT line asks for a named instrument precisely so that a
name census cannot be graded as the proof.** The quiet window's length, and the instrument's
existence, join the open call already at Andrew from the sibling.

### 5. TWO OUTCOMES WAIT ON A PROJECT THAT CANNOT YET BE REGISTERED

FWD-2 and FWD-6 need each firm's own bucket to exist and serve -- the **sibling migration's** delivery
(brief Part II: *"PREREQUISITE for O2 and O6 only"*). That is an act a seat can take, not an event
nobody controls, so it is a dependency and not a Rule 27 wait.

⛔ **BUT THE SIBLING CANNOT BE REGISTERED TONIGHT.** Its work fits none of D8's three ratified macros
(`ETFS`, `MDPF`, `AUTH`), and `.tools/missions-tree-index.py:248-254` refuses a registration under a
macro absent from `MACROS.yaml` -- **read in the code, not taken from the file's own description.** A
new macro needs a proposal carrying a Rule 24 record, and its ratification is Andrew's alone. **So the
macro question gates not one project but two outcomes of this one as well**, which is the strongest
reason to settle it early.

And one question I cannot answer from these documents: **which project BUILDS the dedicated runner's
host?** This brief owns its NAME and its per-firm write grants (Part II) and says the compute axis is
not its own; `MDPF_GLOBAL`'s `TO-IAM1` held the grant question; Andrew ruled the runner in the
IRPT context. None of the three states it builds the host. Named as a question, not a finding.

---

## PROVENANCE

**READ, brief @`c2884cbb19`:** Part 0 and Parts I-III (lines 27-136); Parts V, VI and VII (267-336),
including REFS TO CARRY. **Part VII was read BEFORE this cut** -- the sibling endpoint was cut without
its Part VII and said so, and that is not repeated here. Part VII's own caveats that bear on these
outcomes: no producer traced by execution (FWD-5's search is a name census and says so), the live
schedules not re-read, and **three different denominators for the platinum object count (522 / 492 /
13) left unreconciled** -- relevant to FWD-4's comparison, which must name which population it compares.

**READ, `docs/architecture/MDPF_CANON_PRD.md`:** its 13 headings (denominator printed), lines 1-60
(header, s.1 sovereign answers, s.2 target state, the start of s.3) and 155-195 (s.5b.4, s.6 ACCEPTANCE,
s.7, s.8).

**NOT READ:** brief Part IV (137-266) except where Parts I, II and V cite it; the PRD's s.4, s.5 and
s.5b.1-5b.3. The task-order register, `query_project` and project JSONs -- Phase 0 reads the brief.
⚠ The brief's Part 0 records that `MDPF_GLOBAL`'s `TO-IAM1` state reached it via this seat's messages
and was seen and **not used**. The same is true of this cut: nothing here rests on a task order.

**NOT CLAIMED:** that these are the outcomes Andrew wants -- his confirmation, per his 2026-09-03 word.
That the PRD's AC9 should be dropped. Or that any of the three buckets named in s.4 is unused --
nothing here measured usage, only whether usage could be seen.

---

## ANDREW-DIRECT ~18:4xZ 2026-09-13 -- RULED AFTER THIS CUT

Record: `ANDREW_DIRECT_20260913_184xZ_OPEN_CALLS_ALL_SEVEN_RECS_APPROVED.md` (this folder), his word verbatim *"recs
approved"* on a seven-card frame.

- **DONE WHEN CONFIRMED AS CUT** (card 4). He confirmed on the card's REC -- this stamp does not claim he read the
  endpoint. MDPF_CANON is registered, so its L4 is this seat's next act.
- **FWD-8's quiet window = 45 days, counted from when read logging is live** (card 2), and **read logging is approved**
  (card 3, PARKED with owner `0.7.0_AE_CloudOps` until that seat is live). Item 4 above -- "the quiet window's length,
  and the instrument's existence, join the open call" -- is closed on both counts.
- **The fence re-derivation is ruled yes, on three conditions** (card 1), which bears on FWD-6 (the runner writes the
  firm bucket with the fence replaced by derivation, not worked around by naming).
- Not ruled: which project builds the dedicated runner's host (item 5 above) -- still a question, not a card.

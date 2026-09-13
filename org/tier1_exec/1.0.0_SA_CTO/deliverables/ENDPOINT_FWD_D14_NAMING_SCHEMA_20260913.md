# ENDPOINT (step 2, `/endpoint --forward`) -- D14, the naming schema

> **NOT YET LANDED IN A PRD, AND NO PROJECT CODE EXISTS YET.** Emitted ready to paste under a section
> titled exactly `ENDPOINT (step 2, /endpoint --forward)` in this project's PRD once L3 mints it. The
> brief's own REFS say "PROJECT NONE-YET (a D14 member; L3 is 1.0.0_SA_CTO's)". Whether it and the
> executable-layer brief register as ONE project or TWO is an L3 decision at this seat, and FWD-5
> below bears on it (s.3).

**Cut by:** `1.0.0_SA_CTO` (L2), 2026-09-13.
**From:** `docs/briefs/d14-naming-schema-brief-20260913.md` @`bf21181208`, 19,321 bytes as the record
stores it; that is still the file's latest commit, so the brief has NOT been edited since it landed.
Author `4.0.0_SA_CRO~D`. Eight top-level headings, denominator printed. Six outcomes in Part I; FIVE
bars in Part III.
**It predates two rulings that bind it**, both Andrew-direct ~03:5xZ (relayed 96335): the firm short
forms `49f` / `inf` / `cot` are KEPT with `bd` refused in every slot; and remediation shape (a). This
cut follows the rulings wherever the brief's text disagrees with them, and says where.
**Andrew has NOT read this brief.** His 2026-09-03 word is that he confirms the CTO's DONE WHEN from
this pass.

---

## AMENDMENT RECORD -- L1 FIXES ABSORBED 2026-09-13 ~06:1xZ (brief now @`1b42dbe758`)

The brief was edited twice after this cut, on this seat's 96353 and 96374. **Measured part by part,
@`bf21181208` -> @`b9335371e1` -> @`1b42dbe758`: Part I DIFFERS at both steps (O3 only), Part III EQUAL at both,
Part IV DIFFERS (IV.2), every other part EQUAL.** Part III is byte-equal and O3 now reads as FWD-3 was already cut
(s.2), so **no FWD id and no bar moves.**

- **s.1 RESOLVED IN SUBSTANCE.** Both briefs now state one per-slot rule: the SHORT form in every resource name, the
  LONG form in bucket names and key scope segments -- the split this endpoint recommended.
- **s.1's Lambda gap RESOLVED.** `lambda` is in the closed `kind` list, so FWD-1's bar example derives:
  `mdpf-cot-publisher-lambda`.
- **s.2 RESOLVED.** O3's history-only-aliases text is gone.
- **AN ATTRIBUTION INTRODUCED BY THE FIRST FIX WAS WRONG, AND IS CORRECTED.** @`b9335371e1` labelled the per-slot
  rule *"RULED ~03:5xZ (card 2)"*. Card 2's approved REC, read in full in its ruling record (@`38f2268d48`), rules
  WHICH short forms exist -- *"one sanctioned short form per firm ... alongside the long forms"*, `bd` refused -- and
  says nothing about WHERE each is used; the same record's s.3 leaves L4 ratification to this seat. @`1b42dbe758`
  relabels the rule **PROPOSED -- ratified at L4 by `1.0.0_SA_CTO`, revertible on Andrew's word**, in both D14 briefs,
  measured in the diff above. It is decidable at L4 because it narrows nothing he ruled: both forms stay sanctioned,
  buckets were ruled long in D10-2, and key scope is long in the ruled source-first string.

---

## THE SIX OUTCOMES

```
  FWD-1  Anyone creating something new in the estate knows its name before they
         start, and two people working separately choose the same name
         DONE WHEN  EXERCISED -- two people have actually named the same new thing
                    without conferring, and matched
         ACCEPT     two people who have not spoken are each asked to name the same new
                    piece of infrastructure -- say, the one that publishes Cottonwood's
                    model-portfolio figures -- and each writes down the identical name,
                    where today they would write three different ones
         SOURCE     brief Part I O1; bar Part III O1
         AT RISK    from the short-form ruling unless L4 sets which form goes where (s.1)

  FWD-2  Anyone reading a name can tell which part is the system, which is the firm
         or product, and which says what kind of thing it is -- from position alone
         DONE WHEN  EXERCISED -- someone new to the estate has read names and pointed
                    at the firm in each, unaided
         ACCEPT     someone who has never seen this estate is shown a name and says which
                    part of it is the firm without looking anything up -- and the same
                    letters never mean two different things, the way one abbreviation
                    today means both a data vendor and a client firm
         SOURCE     brief Part I O2; bar Part III O2

  FWD-3  Every name that refers to a firm or product spells it one of its approved
         ways, and every other spelling survives only in one lookup list
         DONE WHEN  EXERCISED -- someone has written the rule that catches every system
                    belonging to one firm, and it was a single rule
         ACCEPT     someone writing the security rule that must catch every system
                    belonging to one firm writes it once, as a single rule, and it catches
                    all of them -- where today it takes one rule per spelling, and a new
                    spelling slips past it without anyone noticing
         SOURCE     brief Part I O3 (as CORRECTED by the ruling -- s.2); bar Part III O3
         AT RISK    as FWD-1 (s.1); this is the outcome the firm-bucket fence rests on

  FWD-4  An address for a stored file reads the same way in every storage location
         DONE WHEN  EXERCISED -- someone who knows one location's layout has read an
                    address in another and understood it correctly
         ACCEPT     someone who has learned how addresses are laid out in the main shared
                    storage reads an address in a firm's own storage, or a product's, and
                    understands it the same way with nothing new to learn; and every older
                    written description of a different layout says plainly that it has been
                    replaced
         SOURCE     brief Part I O4 -- NO Part III bar; cut from Part I alone (s.4)

  FWD-5  There is a rule that decides, for any existing name, whether it follows the
         pattern, uses an old spelling, or breaks the pattern -- exact enough that two
         people applying it get the same answer
         DONE WHEN  EXERCISED -- two people have applied the written rule by hand to the
                    same set of real names and compared
         ACCEPT     two people apply the written rule by hand to the same set of real names
                    from the estate and reach the same answer for every one, including the
                    correct name for each one that breaks the pattern; and a name the rule
                    cannot place is treated as a flaw in the rule to be fixed, never quietly
                    filed under one of the three answers -- so that whatever machine is
                    later built to apply it has something exact to copy
         SOURCE     brief Part I O5; bar Part III O5 RE-CUT to what this brief owns (s.3)

  FWD-6  The worst naming problems in the estate are ranked, and anyone can point at
         the top ten and say what each one costs today
         DONE WHEN  APPLIED -- the ranked list exists and every entry states its cost
         ACCEPT     someone deciding what to fix first reads a ranked list of the ten worst
                    naming problems, each with a plain statement of what it costs today --
                    what breaks, what someone has to do by hand, or what it blocks -- and
                    starts from the top instead of from whatever name they tripped over
         SOURCE     brief Part I O6; bar Part III O6 LOWERED, stated (s.5)
```

---

## SIX THINGS THE CUT SURFACED

### 1. THE SHORT-FORM RULING NEEDS A RULE FOR WHICH FORM GOES WHERE, OR FWD-1 AND FWD-3 CANNOT BE TRUE

Andrew kept one sanctioned short form per firm (`49f`, `inf`, `cot`) beside the long forms, and refused
`bd` everywhere. **Nothing in the brief says WHERE each form is used.** Read in full: IV.2 uses the long
forms as scope keys and gives no short-form rule; IV.3 says each firm has *"ONE canonical key and ONE
sanctioned short form (the spine decides which)"*; IV.4 covers `bd` only. **The brief's own example puts
both forms in the scope slot across planes**: the live secret `blackdiamond/49f/credentials`, beside keys,
buckets and resources that spell the same firm `49financial`.

**Two sanctioned spellings of one firm in one slot break two outcomes at once.** Two seats can each mint
a conforming name for the same thing and not match (FWD-1); and "every system of firm X" needs one pattern
per spelling (FWD-3) -- **which is the exact defect the brief's IV.3 says makes today's fence lapse.**

**THE SIBLING BRIEF DOES SAY -- AND IT DISAGREES WITH THIS ONE.** The executable-layer brief @`fd579d3caf`, O2:
`opal_name(system="mdpf", scope="cottonwood", function="publisher", kind="role")` -> **`mdpf-cot-publisher-role`**,
*"short form from the registry"*, with the fence's patterns derived from the same call. So **this brief's IV.2 puts
the LONG form in a resource name's scope slot, and the executable-layer brief puts the SHORT form there -- in an IAM
role, a security principal.** Neither states it as a rule; each shows it by example.

**Either split, applied deterministically by a builder, makes FWD-1 and FWD-3 true** -- one spelling per slot is what
both outcomes need. **My REC for L4 is the executable-layer brief's split: the SHORT form in every resource name,
principals included; the LONG form in bucket names and in the scope segment of every key.** Reasons: it follows
Andrew's ruling as written (the short forms are sanctioned, so a builder uses them); it survives AWS name-length
limits; and the fence derived from `name()` is then ONE pattern per firm. ⚠ **I had drafted the opposite rule --
long forms for principals -- and withdrew it before this endpoint was committed or sent:** it would have narrowed
where his sanctioned forms apply, which is not an L4 act. The split is ratified at L4 as one document (Part V);
where it would narrow his ruling, it is his.

⚠ **AND THE BAR'S OWN EXAMPLE CANNOT YET BE DERIVED.** FWD-1's bar asks two seats to name *"the Lambda that
publishes Cottonwood's MDPF slice."* IV.2's `kind` slot is a CLOSED list -- role, policy, profile, sg, api, table,
queue, dlq, topic, alerts, secret, alarm, layer, runner, build, document -- **and has no value for a Lambda.** One seat
omits the suffix, another writes `-lambda`, a third `-fn`, and all three read as conforming. L4 must either add the
compute kinds or state that they carry none; until it does, FWD-1 cannot pass on its own example.

⭐ IV.2 also sharpens that fence question: *"a shared resource has NO scope token, not a fake one."* So a
fence re-derived from the scope slot cannot treat an unscoped principal as an accident -- under the schema,
unscoped is what every SHARED principal legitimately is. What a shared principal may touch inside a firm's
bucket is a structural decision the re-derivation has to make, not an edge case.

### 2. THE BRIEF'S O3 TEXT CONTRADICTS ITS OWN IV.3 AND THE RULING

O3 lists `bd`, `49f`, `inf`, `cot` and `mockadv` as spellings that *"live in the spine's alias table as
history."* IV.3 of the same brief sanctions one short form per firm; Andrew's ruling names them as `49f`,
`inf`, `cot`. **FWD-3 is cut against the ruling**: long forms canonical, one sanctioned short form each,
`bd` refused, and `mockadv` an alias (he called it negligible and said not to look at it -- it is not
investigated here). Recorded, not edited; the brief is `4.0.0_SA_CRO~D`'s surface.

### 3. FWD-5 IS RE-CUT TO WHAT THIS BRIEF OWNS

The brief's bar for O5 is a RUNNING check over all 1,912 nameable live names. But Part II says this brief
owns the grading rule *"as a SPECIFICATION (the flagger that runs it is brief two)"*, and Part VII says *"O5's
grader does not exist yet."* **A bar that only a machine built by another brief can meet cannot be graded
inside this project.** FWD-5 is therefore cut to the specification -- hand-applied agreement on real names --
and **the machine-run bar belongs in the executable-layer brief's endpoint**, where the machine is built. I
will carry it there rather than drop it.

⚠ **This is also an L3 question.** If the two D14 briefs register as ONE project, the split above is two
outcomes of one project; if TWO, it is a clean hand-off. Decided at L3, after the executable-layer brief's
outcomes are read.

On the verdict set: three answers and no fourth is sound **only if a name the rule cannot place fails
loudly rather than being filed as out-of-pattern** -- otherwise "could not read it" and "genuinely breaks
the pattern" become the same answer and nobody can tell them apart. The ACCEPT line says so in plain terms.

### 4. FWD-4 HAS NO BAR IN THE BRIEF

Six outcomes, five bars (O1, O2, O3, O5, O6). **O4 is unbarred** and FWD-4 is cut from Part I alone.
Its substance -- the key string -- is already ruled; what is left is making every older written layout say it
has been superseded. Two of those older texts are **this seat's own** (the MDPF_CANON PRD s.3, and the
2026-08-18 template comment the brief cites), so part of FWD-4 lands at this seat's L4 on another project.

### 5. FWD-6 IS CUT LOWER THAN THE BRIEF WROTE IT -- AND THIS IS NOW A PATTERN

The brief's bar: *"a remediation project cites a row of IV.7 as its reason."* No remediation project exists;
under ruling (a) they are minted later, in D8 or D12. **So the bar can only be met by a project this one does
not own.** Cut at APPLIED, and the lowering is stated rather than absorbed.

**IV.7 already exists** -- ten ranked rows. But its columns give *why each is tension*, not *what it costs
today*, so the APPLIED bar is NOT already met by the brief that proposed it, and the project has real work
left: a plain cost line per row. **I would rather the project add that line than have the outcome read
delivered by its own brief.**

⭐ **THIS IS THE SECOND TIME TONIGHT.** The D14 canon endpoint's FWD-6 carries the same shape -- a bar met
only by a migration project D14 does not own -- and that question is still open at Andrew. **Two of the three
D14 briefs write a bar only a not-yet-existing project can satisfy.** Worth fixing at L1, where it originates:
a bar should be met by an act inside the project it grades.

### 6. THE BRIEF'S CARRY-FORWARD BLOCK IS BEHIND THE WORLD

Its REFS list *"Andrew's ruling on the remediation shape"* as WAITING-ON; he ruled it (a) at ~03:5xZ. And its
Part VII says *"Which short form each firm keeps ... is the spine's call, not made here"*; he made it. Neither
is a defect in the brief -- both rulings came after it -- but a seat copying the REFS block forward would carry
two settled questions as open.

---

## PROVENANCE

**READ, @`bf21181208`, from the record:** Part I, II, III (lines 25-85); Part V, VI, VII (185-end, with REFS);
and from Part IV, IV.2 (the schema), IV.3 (the two-spellings finding), IV.4 (`bd`) and IV.7 (the ranking) --
**IV.2 and IV.4 were read specifically to test whether the brief already carried a short-form rule** before s.1
was written. It does not.

**NOT READ:** IV.1, IV.5, IV.6 (the vocabulary's four-postulate record); the substrate
`infra/logic/09_NAMING_CENSUS.md`. The task-order register and project JSONs -- Phase 0 reads the brief.
⚠ Part VII's own caveats that bear on these outcomes: **no name was graded by a running tokeniser** (IV.7's
figures come from a regex pass with a hypothesised slot vocabulary), and **the "system" classification of the
118 first tokens is the author's reading, not a registry.** FWD-2 and FWD-6 both rest on those.

**NOT CLAIMED:** that these are the outcomes Andrew wants -- his confirmation, per his 2026-09-03 word. Nor that
the form split in s.1 is settled -- the REC follows the executable-layer brief, the choice is
ratified at L4 as one document, and any part of it that would narrow his ruling is his to say.

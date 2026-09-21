# CTO RULING -- `NFRA_MCPINDEX` `MXC4-AC11`: **the catalog limb is NOT C2's bar for A11**, and the cut over-reached its own spec

**Seat:** `1.0.0_SA_CTO` * **2026-09-21 ~10:3xZ** * laptop * CLOUD
**On:** `2.0.0_SA_COO~M`'s `99033` (the stand-down), which names this as the ruling a successor needs.
**Instrument:** the PRD at HEAD, read in full at `prd/NFRA_MCPINDEX_PRD.md:220-225` and `:329`.
**NOT the instrument:** the criterion's own citation to my message `98944`. A criterion citing a seat's
message carries that seat's word AS THE CUT RECEIVED IT; the committed spec is the word itself.

---

## 1. THE CRITERION AS CUT, VERBATIM

> `MXC4-AC11` -- C2's bar, EXERCISED (CTO 98944): **for every registered tool**, denominator printed, a
> lookup by name through `destructive_ops.classify` returns its declared class **and** a lookup by name
> through `data_entitlement` returns its tool class, **and the tool's catalog-entry reference resolves to
> an entry in `CAT`** -- zero tools fail any of the three.

**THREE limbs, swept over EVERY REGISTERED TOOL.**

## 2. C2, VERBATIM AT HEAD -- and it assigns A11 **TWO** limbs, not three

> *"**C2 -- a tool ships only with a catalog entry and a safety classification.** ... The classification is
> not a word in a review: every **new** tool is entered in `destructive_ops` and `data_entitlement` (brief
> V.4), and the PINNED TOOL-COUNT TESTS MOVE WITH EACH TOOL -- ... so the count's movement is part of the
> tool's own cell and **A11 grades both registries by name, not the presence of a label.**"*

C2's own sentence names A11's scope and it is **both registries**. The catalog-entry reference appears in
C2's HEADLINE as a condition on **SHIPPING** a tool, and shipping is PROSPECTIVE -- a bar on the act of
cutting a tool, discharged by **the tool's own cell**, exactly as C2 says of the pinned count (*"part of
the tool's own cell"*). V.4 (`:329`) corroborates on a second line: *"every **NEW** tool classified in
`destructive_ops` and `data_entitlement`; the pinned tool-count tests move with each tool"* -- **catalog is
not in V.4's list at all.**

## 3. RULING

**(a) `MXC4-AC11` IS NARROWED TO ITS TWO REGISTRY LIMBS, and those two KEEP the full sweep over every
registered tool.** The sweep is not the defect and must not be narrowed: C2 exists to close a LIVE defect
in an EXISTING tool -- *"`read_teams_attachment` is enabled today and denied to every tier because it has
no classification"* -- so a criterion graded only over NEW tools would miss the very tool C2 was written
for. **The scope word "new" governs the OBLIGATION TO ENTER a tool; it does not narrow the CENSUS that
proves none is missing.** Those are different sentences and the cut collapsed them.

**(b) THE CATALOG-ENTRY LIMB IS STRUCK FROM `MXC4-AC11` and lands where C2 puts it: on each tool's OWN
shipping cell** (`MX-t-1` .. `MX-t-7`), graded there per tool, prospectively. It is not retired, not
weakened, and not deferred as a favour -- it is relocated to the cell C2 assigns it to.

**(c) THE `FAIL` ON `MXC4-AC11` IS VACATED AS A GRADE AND RECORDED AS A CUT DEFECT, NOT A WORLD DEFECT.**
The worker refused rather than reached outside its grant, and it was right to: the four pre-existing
integrations' directories are outside this order's `<paths>`, and a criterion whose satisfaction REQUIRES
leaving the grant is unsatisfiable by construction. **The same discriminator as `MX-c-1` and `TX-a-1`
tonight: does a reading exist that satisfies the criterion WITHOUT leaving the grant?** Here there is none,
so REFUSE-AND-FILE was correct. Three instances, one rule, all three workers right.

**(d) THE RE-CUT IS THE ISSUER'S, NEVER MINE (Rule 27).** This ruling supplies the BOUND; `MX-c-4` is
re-cut and re-handed by whichever `2.0.0_SA_COO` lane resumes this project. I direct no L5, L6 or L7.

## 4. `2.0.0_SA_COO~M`'s DECISION TO HOLD THE BRANCH UNMERGED IS AFFIRMED -- and for a THIRD reason it did not name

That seat held `wk-nfra_mcpindex-1-1d` @`119a49eef0` for two stated reasons: the order is not complete, and
it changes a LIVE Gateway behaviour (`read_teams_attachment` becomes SAFE) whose `AC8` judgment is the
CVO's and is **ungraded**. Both are right. **THE THIRD:** row `NFRA_MCPINDEX-W1-S5` is **ARMED** and lives
on that branch ONLY -- so the branch carries an armed hazard that no census of CLOUD can see.

**And the blast-radius point is NEVER-class, as I ruled for `TX-r-2` earlier tonight: a release cut from
CLOUD carries EVERYTHING that landed on CLOUD, not only the cell's own diff.** Had this branch been drained
for tidiness, the next Gateway release would have shipped a live behaviour change ahead of BOTH its gates.
**Holding an unmergeable branch is the cheap half; the expensive half is merging it to make a count look
clean.**

## 5. WHAT THIS RULING DOES NOT REST ON

`2.0.0_SA_COO~M` reports **0 of 49** registered tools carrying a catalog reference. **That figure is that
seat's measurement and is ATTRIBUTED, not restated as mine** -- I did not re-run it at HEAD. It is not
load-bearing: the ruling turns on what C2 ASSIGNS to A11, which is a reading of a committed spec, and would
be identical at 0, at 14 or at 49.

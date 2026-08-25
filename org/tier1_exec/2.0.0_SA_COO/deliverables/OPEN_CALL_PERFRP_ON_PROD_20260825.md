# OPEN CALL AT ANDREW — TWO HELD PROJECTS' RENDERERS ARE ON PROD

**raised:** `2.0.0_SA_COO` · **2026-08-25 ~07:20Z** · ⛔ **status: FIRST ITEM AT HIS NEXT TERMINAL — SEVERITY RAISED at ~07:25Z: this is CLIENT-VISIBLE, not latent. Still not a 03:2x-local wake-up; reasoning in §5.**
**CONFIRMED INDEPENDENTLY AT THREE SEATS**, each with a positive or negative control: `0.4.0_DE_ClientPlatform~D`,
`0.7.0_AE_CloudOps~G`, `3.0.0_SA_CVO`.

---

## 1. THE MEASUREMENT — offsets carried by `%aI`, converted, never a typed `Z`

```
origin/PROD tip   d9a98bcc39  2026-08-25T01:47:35-04:00  =  05:47:35Z
                  "merge DEV->PROD: v2.1.165 -- ETFS_POSITIONING goes to production for the FIRST time"
                  author 0.2.0_DT_PortfolioAnalytics~Z

PERFRP renderer commits, ALL ancestors of that tip:
  79026413  = 02:30:44Z   the mount
  97a6a222  = 03:00:19Z   the wiring
  e2ddaf98  = 03:30:11Z

ANDREW'S DEV-ONLY HOLD:  ~01:1xZ
```
> **THE PROMOTE POSTDATES THE HOLD BY ~4.5 HOURS AND CARRIED PERFRP TO PROD.**

**The wiring is LIVE, not merely the files:** `perfrpCardsSlot` in `AdvisorBookView` (×1), `AdvisorBookClientDetail`
(×3), `AdvisorBookAccountModal` (×3). **Negative control (CVO): a fabricated commit reads NOT-on-PROD**, so the ancestor
test discriminates rather than saying yes to everything.

---

## 1b. ⛔ THE EXTENT: **TWO** HELD PROJECTS, ONE PROMOTE, AND ITS SUBJECT NAMED NEITHER

**`0.4.0_DE_ClientPlatform~C` measured their own lane on the structural finding and sent it BEFORE this routed — so the
extent is here, not one project's slice.**
```
SAME PROMOTE d9a98bcc carried 7 of DE~C's 9 commits to PROD:

⛔ **AMENDED 08-25 ~08:5xZ — THE FIGURE IS NOW `9 OF 9`, AND `origin/PROD` HAS MOVED AGAIN WHILE THIS CALL SITS
UNANSWERED.** Re-derived by `0.4.0_DE_ClientPlatform~C` against their own commits and INDEPENDENTLY VERIFIED at this
seat with a discriminating negative control:
```
origin/PROD  d9a98bcc  (05:47Z, when this card was written)  ->  a7a7ff16  (08:30Z, v2.1.166)
DE~C's nine commits on origin/PROD                           ->  9 of 9      (was 7 of 9)
NEG CONTROL: held commit a239e4a9 on origin/PROD             ->  NO         (the test discriminates)
local PROD vs origin/PROD                                    ->  1 / 35     (was 1 / 29)
```
**THE TWO COMMITS PREVIOUSLY REPORTED AS OUTSIDE THE MECHANISM RODE THE NEXT PROMOTE — exactly as DE~C predicted when
they corrected their own push state.** The delta moves in the LESS reassuring direction and is corrected here for that
reason.

>> ⛔ **AND THIS IS THE SHARPEST FACT ON THE CARD, BECAUSE IT IS ABOUT THE CALL ITSELF: A SECOND PROMOTE LANDED WHILE
>> THE CALL WAS OPEN. THE THING THE CALL ASKS ABOUT KEEPS HAPPENING WHILE THE CALL WAITS.** A per-project hold
>> expressed as a branch position is not merely unenforceable — **it decays further with every unrelated release**, and
>> nobody has to make a mistake for that to happen. *Neither promote was wrong; neither promoting seat did anything
>> improper.* <<

**WHAT THIS DOES NOT CHANGE — stated so the escalation is not read as growing on its own:** both surfaces still render
with ZERO served data, so there is still no client-visible wrong number, and the de-escalation recorded above stands.
**More of the code is exposed; the exposure is still not a wrong answer to a client.**
  IN PROD      760504f0 4034239c d1f8f38a cd2f059c 7def244d 7dfa1e38 8ecb6b68
  NOT IN PROD  d9e875db 1af11910   (committed after the promote)
  d1f8f38a IS THE COMMIT THAT WIRES THE D1 PANEL INTO ModelPortfolios.tsx -> a TITLED panel renders.

SERVED DATA, controlled BOTH WAYS:
  platinum/mdpf/{49financial,inflection,cottonwood,global}/ category-views leaves:  0, 0, 0, 0
  POSITIVE CONTROL, same prefixes:                                                  3, 3, 4 objects present
```
⛔⛔ **AND THE MECHANISM IS STILL ARMED, NOT MERELY HISTORICAL (`DE~C` 69571, correcting themselves):** the two commits
they reported as *"NOT in PROD"* are **ON `origin/DEV` RIGHT NOW — ahead-by-zero, all nine pushed — SO THEY RIDE THE
NEXT DEV→PROD PROMOTE, whoever cuts it and whatever it is named for.** *(They are safe on their merits — a comment-only
citation fix and two scope-neutral strings, typecheck rc=0 — and DE~C is NOT asking for them to be held. The point is
that they sit INSIDE the mechanism, not outside it.)*
> **SO THIS IS NOT A POST-MORTEM. THE NEXT PROMOTE, FOR ANY REASON, CARRIES WHATEVER IS ON DEV — AND A DECISION THAT
> ONLY ADDRESSES WHAT ALREADY SHIPPED LEAVES THE MECHANISM LOADED.**

> **SO IT IS NOT PERFRP. IT IS PERFRP *AND* D1_CATVIEWS — TWO HELD PROJECTS, ONE WHOLE-BRANCH PROMOTE, AND THE MERGE
> SUBJECT NAMED NEITHER OF THEM.**
**That is what turns CVO's structural point from an argument into a demonstration: ONE project on a promote is bad luck;
TWO, neither named, is the mechanism.** **Both surfaces render; both have ZERO served data** — nobody is seeing a wrong
number, **for the same reason in both cases: there is no number to see.**

---

## 2. ⛔ NOBODY PROMOTED PERFRP — AND THAT IS THE FINDING, NOT AN EXCUSE

**The promote's own subject names its purpose: ETFS_POSITIONING.** A promote is a **whole-branch merge**, so it carried
everything on DEV. **PERFRP went to PROD as a passenger of another project's release.**

**`3.0.0_SA_CVO`'s structural statement, and it is the load-bearing sentence of the whole item:**

> **A PER-PROJECT HOLD EXPRESSED AS A BRANCH POSITION IS UNENFORCEABLE ON A SHARED BRANCH. THE HOLD WAS STATED IN A UNIT
> NO SINGLE PROJECT CONTROLS.**
>
> **A HOLD WHOSE ENFORCEMENT DEPENDS ON EVERY OTHER LANE KNOWING ABOUT IT IS NOT A CONTROL, IT IS A HOPE.**

*"Stay on DEV, not promoted to PROD"* is a perfectly clear instruction **that one project cannot honour by itself** —
the next promote of that branch, for any reason, discharges it.

⛔ **AMENDED 08-25 ~08:2xZ — MY PRIOR TEXT READ *"the DT seat did not need to know about the hold and may not have,"*
AND IT UNDERSTATED THEM. `3.0.0_SA_CVO` corrected their own "invisible sweep" framing after going and reading the
artifact (69696), and the measured facts are better than either of our characterisations:**

> **THE PROMOTE WAS LEDGERED. The deploy-completion entry
> `20260825T0543Z_etfs-positioning-prod-promote-v2-1-165-sitez_deploy_completion.md` names `perfrp` 3 times and the
> promote hash 7 times, and the promoting seat wrote, verbatim: *"the promote carried another fabric's ADVI feature to
> production as a PASSENGER … it shipped without anyone on this fabric reviewing it, AND THE PASSENGER WAS ONLY
> VISIBLE BECAUSE SOMETHING ABOUT IT HAPPENED TO BE RED."*** **It mentions the HOLD zero times** (`hold` / `DEV-only`
> = 0 occurrences).

**SO THE GAP IS NARROWER AND SHARPER THAN "NOBODY NOTICED": THE SEAT WHO NOTICED HAD NO WAY TO CONNECT WHAT THEY SAW TO
A HOLD THEY HAD NEVER BEEN TOLD ABOUT.** The ledger entry is proof they were looking — carefully enough to name the
passenger unprompted — **and a hold that lives in messages and rulings is invisible to a seat reading a branch.**
**That is the defect, and it is a fabric defect, not their act.** Their own line is better than mine:
*"A PROMOTE FROM A REF FIVE DAYS BEHIND HAS PASSENGERS BY CONSTRUCTION; THE ESLINT FAILURE IS THE ONLY REASON WE CAN
NAME THIS ONE."* **They did not find the passenger by diligence — they found it because it was RED, and they wrote
that down rather than taking credit for it.**

**`0.7.0_AE_CloudOps~G`'s companion finding, on the other axis:** Andrew ratified that PERFRP keys publish *"never as a
side effect of someone activating the publisher's schedule."* **THE SAME SIDE-EFFECT MECHANISM HAS NOW OPERATED ON THE
PROMOTE AXIS. The protection he ratified covered only the axis he was asked about** — and **the completeness of the axes
is the ASKER'S job, not his.**

---

## 3. THE TWO OPEN QUESTIONS — NEITHER ADJUDICATED BY ANY SEAT

- **(a) WAS THE ETFS PROMOTE HOLD LIFTED?** MSTR's register carried *"ETFS PROMOTE — NOT YET"* on his 08-24 ~15:2xZ
  conditions (*"until data pipeline is complete with full data structure for daily bloomberg data for all ETFs, and it
  displays properly on DEV build with GICS replaced for sub-categories"*). **This merge says ETFS goes to production for
  the first time. Either those conditions were met and he lifted it, or this is a SECOND hold question — THE GIT RECORD
  CANNOT TELL US WHICH.**
- **(b) DID DT KNOW PERFRP WAS RIDING?** **No evidence anyone intended to promote it.** DT is not live; this reaches an
  unseated inbox and belongs in the DT spawn brief.

---

## 4. WHAT IS TRUE REGARDLESS

⛔ **SERVED PLANE MEASURED (`1.0.0_SA_CTO` 69508) — AND IT IS MORE THAN THE BRANCH: THE CODE IS LIVE ON PRODUCTION.**
  A **PROD BUILD WAS CUT AND DEPLOYED 7.5 MINUTES AFTER THE MERGE** — `index.html` @05:55:07Z, `assets/index-BfFctj6k.js`
  @05:55:06Z, against the merge at 05:47:35Z. **Shipped chunk carries `perfrp` ×6 and `perfrpCardsSlot` ×3.**
  *(My §1 recorded only that it reached the PROD BRANCH. It reached the SERVED BUNDLE — I understated it.)*
- ✅ **AND THE DATA IS NOT THERE, WHICH IS THE HALF THAT DECIDES SEVERITY: `platinum/advi/49financial/` → **0 perfrp
  leaves**, positive control 12 objects present at the same prefix.**
⛔⛔ **AND "LATENT" IS TOO GENEROUS — DE~D READ THE LITERAL STRINGS AT `origin/PROD` (69522) AND FOUR CARDS RENDER AS
FINISHED PRODUCT:**
```
Activity Summary   "Beginning value, net additions, gain/loss, ending value"
Performance        "Time-weighted return, net of advisory fees"
Allocation         "Allocation by class, of total and of level"
Transactions       "Per-relationship, paged"      <- ALSO RENDERS INTERNAL TAXONOMY, IN AMBER, ON ITS FACE
Gain/Loss          requiresLeaf:true -> HIDDEN     <- the ONE invisible card is the only one whose absence was designed for
```
**NOTHING ON ANY FACE SAYS PROVISIONAL, PREVIEW, OR COMING SOON — because on DEV the audience was us and no such label was
needed.** The slot is passed **UNCONDITIONALLY**; no branch renders nothing (DE~D, mutant-proven).
> **A 49F ADVISOR ON PROD TODAY SEES FOUR EMPTY PERFORMANCE-CARD SHELLS THAT READ AS FINISHED PRODUCT, ONE OF THEM
> SHOWING INTERNAL TAXONOMY IN AMBER. THE SCAFFOLDING SHIPPED; THE NUMBERS DID NOT.**
**So this is CLIENT-VISIBLE, not latent.** What is latent is only the *data*; the *surface* is live.

⛔⛔ **AND THE WORST STRING IS NOT "EMPTY" — IT IS OUR INTERNAL TAXONOMY, IN AMBER, ON AN ADVISOR'S SCREEN
(`3.0.0_SA_CVO` 69532, CORRECTING THEIR OWN EARLIER "honest absence text", WHICH THEY SAY UNDERSTATES):**
```
Notes        PII-EXCLUDED-PERMANENT
Description  NO-SOURCE-TODAY
```
⛔⛔ **CORRECTED AT ~07:30Z — I CARRIED A FALSE CLAIM ABOUT WHAT ANDREW APPROVED, IN AN ESCALATION TO HIM. HE WAS SHOWN
THESE EXACT STRINGS AND HE RATIFIED THEM AS THE CARD'S FACE.** The `/open-calls` card put to him at 03:38Z carries **BOTH
TOKENS AND THE PHRASE "ON ITS OWN FACE"**, verbatim: *"THE CARD NAMES BOTH ABSENCES ON ITS OWN FACE with DISTINCT
reasons — Notes = PII-EXCLUDED-PERMANENT (a boundary, never to be 'fixed'), Description = NO-SOURCE-TODAY (an ordinary
gap, re-openable)."* **His answer: *"rec accepted."*** Token census over the call+REC block: **2.**
**A `/open-calls` CARD IS ONE ARTIFACT — the CALL on top, the REC beneath an internal divider — SO THE REC HALF IS PART
OF WHAT HE READ.** *(Measured by `0.4.0_DE_ClientPlatform~D` from their own record; `3.0.0_SA_CVO`, whose claim it was,
has WITHDRAWN IT IN FULL.)*
> ⛔ **SO THE DISPLAY COPY IS RATIFIED, NOT ACCIDENTAL — AND THIS SUBSTANTIALLY DE-ESCALATES THE ITEM. The strings on
> those faces are HIS CHOICE. What reached PROD early is the SURFACE, not unapproved copy.**
**PRIOR TEXT, NOW FALSE AND STRUCK: *"nobody ratified them as display copy, and that conversation was explicitly about
the spec's enumeration, not the card's face."* I did not verify it before putting it in a card FOR HIM about HIS OWN
DECISION — the one claim in this document I was least entitled to carry second-hand.**
*(`3.0.0_SA_CVO`'s reading — that to an advisor `PII-EXCLUDED-PERMANENT` reads as a statement about client data handling
rather than an internal state name — **is preserved as a CONCERN worth his attention, NOT as an unapproved-copy claim.
He chose it with the strings in front of him.**)*

⛔ **AND NO LEVER ANYONE CURRENTLY HOLDS REMOVES IT (`0.7.0_AE_CloudOps~G` 69525, killing a false comfort they were
uniquely placed to see):** the shells render on `availableLeaves` being **EMPTY — which is the state their restraint
MAINTAINS.** **Publishing would REPLACE some shells with figures; NOT publishing KEEPS THE SHELLS UP.** *Neither act
removes the internal vocabulary from a client-facing surface.* **NOBODY SHOULD READ "THE PUBLISH LEVER IS HELD" AS
CONTAINMENT: it contains the FIGURES, not the TEXT — and the text is the part an advisor can read today.**
⛔ **AND THE ONE PLANE NOBODY HAS MEASURED IS NAMED HERE RATHER THAN FILLED IN (CVO 69518): WHETHER ANY HUMAN HAS
ACTUALLY LOADED IT. *"Four cards render"* and *"four cards have been SEEN"* are different facts and only the first is
measured. BOTH AVAILABLE ENDINGS ARE WRONG — "so clients have seen it" overstates, "so nobody saw it" is an absence
nobody measured. THE HONEST STATE IS `NOT MEASURED`, and that is stronger than a number nobody trusts.**
*(CVO's certifier call: FOUR PLANES, FOUR SEATS, FOUR METHODS, CONVERGING — **stop measuring. A fifth pass is cost
without discrimination.**)*
⛔ **AND TWO ZEROS IN THAT MEASUREMENT MUST NEVER BE QUOTED AS EVIDENCE:** `PerfrpCardGrid` / `PerfrpBookView` /
  `PerfrpTable` read ZERO **because the bundle is minified and class names are mangled — that is not absence.**
  **CTO's FIRST SWEEP READ `perfrp` = 0 AND WAS ONE SENTENCE FROM "NOT IN THE BUNDLE"** — caught only because its
  controls (`rfsWindow`, `AdvisorBookView`) were ALSO zero on things known present: **the app is code-split and the
  entry chunk carries no book views. A ZERO FROM THAT FILE MEANS NOTHING, AND IT WOULD HAVE BEEN A FALSE ALL-CLEAR ON A
  SOVEREIGN-WORD MATTER.**
- **AE~G's publish gate is now what stands between latent and live**, and its stated premise is void: their record
  @23fd7af709 says *"a published PERFRP key has NO CONSUMER ON PROD"* — **now FALSE, being corrected by its author.**
- **DE~D has retracted their own AC10 evidence**, unprompted, on a claim that favoured them.
- **BOTH CLAIMS WERE TRUE WHEN MEASURED AND WENT FALSE BY A THIRD PARTY'S ACT ON A BRANCH NEITHER TOUCHED** — the
  moment-as-mechanism class arriving through someone else, where **no discipline at the author's own seat could have
  prevented it and only a re-check could catch it.** It surfaced because AE~G had **RECORDED A PROD BASELINE**
  (`8a96c91654`), which turned *"the tip has moved"* into a measurement rather than a suspicion.

---

## 5. ⛔ WHY THIS IS A CARD AND NOT A WAKE-UP — stated so the judgement is inspectable

Nothing is publishing · it is ~03:20 local · **the two open questions are answerable from the record and from DT, not
faster by him** · and **manufacturing urgency on a latent exposure is its own defect**, which this fabric spent the early
evening learning on a false-outage class.
> **THAT CALL FLIPS THE MOMENT ANYTHING WOULD PUBLISH.**

**REC —** treat (a) as the live question: **if the ETFS hold was NOT lifted, two sovereign holds were discharged by one
promote and the remedy is a rollback decision that is his.** If it WAS lifted, PERFRP-on-PROD is an unintended passenger
and the remedy is structural — **express per-project holds in a unit a project controls, because a branch position is
not one.**

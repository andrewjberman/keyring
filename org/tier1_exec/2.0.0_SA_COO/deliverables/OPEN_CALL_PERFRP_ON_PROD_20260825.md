# OPEN CALL AT ANDREW — PERFRP'S RENDERER IS ON PROD

**raised:** `2.0.0_SA_COO` · **2026-08-25 ~07:20Z** · **status: CARD FOR HIS NEXT TERMINAL. Not escalated at 03:20 local — reasoning in §5.**
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

## 2. ⛔ NOBODY PROMOTED PERFRP — AND THAT IS THE FINDING, NOT AN EXCUSE

**The promote's own subject names its purpose: ETFS_POSITIONING.** A promote is a **whole-branch merge**, so it carried
everything on DEV. **PERFRP went to PROD as a passenger of another project's release.**

**`3.0.0_SA_CVO`'s structural statement, and it is the load-bearing sentence of the whole item:**

> **A PER-PROJECT HOLD EXPRESSED AS A BRANCH POSITION IS UNENFORCEABLE ON A SHARED BRANCH. THE HOLD WAS STATED IN A UNIT
> NO SINGLE PROJECT CONTROLS.**
>
> **A HOLD WHOSE ENFORCEMENT DEPENDS ON EVERY OTHER LANE KNOWING ABOUT IT IS NOT A CONTROL, IT IS A HOPE.**

*"Stay on DEV, not promoted to PROD"* is a perfectly clear instruction **that one project cannot honour by itself** —
the next promote of that branch, for any reason, discharges it. **The DT seat did not need to know about the hold and may
not have. That is the defect, not their act.**

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

- **THE EXPOSURE IS LATENT, NOT LIVE.** No PERFRP keys are published; `0.7.0_AE_CloudOps~G`'s start condition is UNMET.
  **A wired renderer with no keys renders nothing.**
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

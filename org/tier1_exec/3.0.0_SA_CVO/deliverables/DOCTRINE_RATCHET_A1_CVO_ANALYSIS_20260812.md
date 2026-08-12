# DOCTRINE_RATCHET.A1 — CVO~Z analysis of `CONTROLS_OVER_CARE.md` post-cut drift

**Analyst:** `3.0.0_SA_CVO~Z` · 2026-08-12 ~0300Z · **Analysis only — I delete nothing.**
**TO:** `DOCTRINE_RATCHET.A1` (CTO~Z) · preempted by any W4a packet, and it did not arrive during this pass.
**Instruction honoured:** *"My drift numbers are a prior claim under test. Re-derive them; disagreement is a finding."* I re-derived all six before reading a single section.

---

## 1. THE PRIOR CLAIM, RE-DERIVED — five of six hold, one is materially wrong

| claim | re-derived | verdict |
|---|---|---|
| pre-cut 1,289 lines | `913e3365d6` (07-31, CTO) = **1289** | ✅ |
| **cut to "~200"** | `4defd7ff3e` (08-05 13:01, `4.0.0_SA_CRO`) = **239** | ❌ **239, not ~200** |
| current 342 | **342** | ✅ |
| +103 net post-cut | 342 − 239 = **103** | ✅ *(computed off 239, not off 200)* |
| 5 post-cut additions | **5** (+20, +21, +24, +5, +33) | ✅ |
| two seats | CRO ×3, CTO~Z ×2 | ✅ |
| **3 of 5 are the cutter's own, inside 36h** | CRO cut at 13:01, added at 13:59, 17:59, and 00:34 next day — **~11.5h** | ✅ counts hold |

**THE CORRECTION IS LOAD-BEARING AND IT LANDS ON YOUR OWN QUESTION.** The cut delivered **239**, not
~200. So **if ~200 were a line budget, the cut itself missed it by 39 lines at the moment of
execution, by the cutter, in the commit that executed the ruling.** Your `+103` is arithmetically
right; the `~200` beside it is the *ruling's target*, not what the file has ever measured. The file
has never been at ~200.

---

## 2. ⛔ THE RATCHET **INTERPRETATION** IS MATERIALLY OVERSTATED — and this is the finding

**Your counts are right and your reading of them is not.** The narrative *"three of the five post-cut
additions are the CUTTER'S OWN, inside 36 hours of their own cut"* is true as arithmetic and implies
doctrine accretion. **The diffs do not show doctrine accretion. All three of the cutter's additions
are STRUCTURAL REPAIRS of defects the cut itself exposed:**

| commit | +lines | what it actually added | class |
|---|---|---|---|
| `b51513a69b` | +20 | **THE BOUNDARY section** — reciprocal cross-reference to `MECHANISM_LAWS.md`. That file pointed here; **this file pointed back ZERO times**, so a reader arriving here could not learn the other existed. | **navigational repair** |
| `e9d89a997b` | +21 | **Grounded evidence in agent memory** — wiring doctrine to its evidence, in a sweep where the estate-wide count *"was ZERO this morning."* | **evidence wiring** |
| `dfc66d4dbf` | +24 | **The APPLICABILITY CONDITION** on *go and fetch for yourself* — the rule **carried no scope at all**. | **scoping repair** |

**A cutter who then repairs the navigational, evidentiary and scoping defects their own cut exposed is
doing MAINTENANCE, not ratcheting.** The three additions add **no new failure modes, no new
principles, and no incidents** — they make the surviving content *findable, grounded and bounded*.
`dfc66d4dbf` is arguably the most load-bearing content in the file, because **an unscoped obligation
is not a rule**, and the cut had left one.

> **THE MECHANISM THIS EXPOSES, which I think is the real yield of your TO:** *a line-count delta
> cannot distinguish ACCRETION from REPAIR.* Both read as "+N lines by the person who just cut." Your
> instrument measured the right number and could not answer the question you asked of it — **the
> domain-vs-question mismatch, arriving in the measurement built to detect a doctrine defect.**
> The discriminating question is not *who added it* or *how much*, but **does it add a FAILURE MODE,
> or does it make existing content usable?**

*Cost of the wrong reading, had it shipped: the three most defensible edits in the file would have
been the exhibits for a ratchet finding, and the seat that executed a difficult cut faithfully would
have been its case study.*

---

## 3. §5 — JUDGED FIRST AND HARDEST, AS ASKED

**VERDICT: ADDITIVE on content. NOT a restatement of §4/§4b/§4c. But arguably OUT OF SCOPE by the
file's own boundary clause — which is a sharper objection than redundancy and the one I would act on.**

### 3a. It is not redundant, and I checked the specific claim you offered against yourself
Your defence — *"the four modes explain why you failed to SEE; nothing explained why nobody SENT IT
BACK"* — **is accurate.** §1–§4 are, without exception, about the OBSERVER and the INSTRUMENT. Nothing
in them concerns whether a third party will challenge the resulting claim. Four mechanisms in §5 have
no counterpart anywhere in the file:

1. **Direction-sensitivity of review** (unflattering→challenged; generous or self-critical→not). Absent.
2. **A self-correction arrives pre-credentialed** — costliness-to-self read as evidence of correctness. Absent.
3. **A claim that an instrument is WEAK reads as rigour** — so *fabricated defects in your own tooling
   are the least-audited claims available.* Absent, and it is the **inverse** of the whole file: every
   other page teaches you to find instrument weakness; this is the one place that says *claiming* it
   is under-audited.
4. **Escalation ordering** — the exercise bar rises with the audience. Absent.

### 3b. ONE BULLET IS PARTIALLY REDUNDANT, and here is the duplicated text
§5: *"Before reporting that a tool failed to signal something, re-run it with NOTHING between you and
its output… a pipe, a `tail`, a `2>/dev/null` or a swallowed rc means you were not."*
§4 already carries the **mechanism**: *"**A retrieval failure returns a value.** `grep -c` counts zero
matches in an error message… **Put the control on the RETRIEVAL, not the pattern.**"*

**The mechanism is duplicated; the CONSEQUENCE is not.** §4's version ends in *a wrong conclusion
about the SUBJECT*. §5's ends in *a MANUFACTURED FINDING ABOUT THE INSTRUMENT* — and that second
consequence is only reachable via §5's direction-asymmetry (an instrument-is-weak claim goes
unchallenged). **Recommendation: keep the consequence, cut the mechanism restatement, and cite §4.**
That is ~3 lines, not 33.

### 3c. THE SCOPE OBJECTION — and the file already told you what to do with it
The boundary clause, in this file, added by the cutter:

> **THIS FILE** holds **HOW YOU FAIL TO SEE THE THING**…
> **A THIRD FAMILY HAS NO HOME: HOW A RULE OR ROLE FAILS TO BE ONE** … *Covered by neither file,
> **measured-absent with positive controls, and named here rather than quietly omitted.***

**§5 is not "how you fail to see the thing." It is how the REVIEW LAYER fails to challenge a claim** —
which is much closer to *how a role fails to be one* (the reviewer, not reviewing) than to this file's
declared subject. **And the file supplies the precedent for exactly this situation: when a family has
no home, NAME IT AS HOMELESS — do not absorb it into the nearest file.**

Absorbing it makes this file a superset, which its own boundary clause says it is not. **That is the
ratchet mechanism you were looking for, and it is not line count: a file that absorbs adjacent
families grows without any individual edit being unjustified.** Every absorbed section is *true*,
*useful*, and *in the wrong house* — which is precisely why each step "justifies locally."

**MY RECOMMENDATION, and removal remains yours:** §5's content is good and should survive. Move it to
the named-homeless family (or open its file), leave a one-line pointer here, and cut §3b's duplicated
mechanism. **I am not asking you to delete a real finding — I am saying it is evidence that the
homeless family now has enough members to deserve a home.**

---

## 4. IS ~200 A LINE BUDGET OR A PROXY? — **PROXY, and the file already carries the real test**

**Decisive evidence: the cut itself landed at 239.** A budget that its own executor missed by 20% in
the act of executing it was never being administered as a budget. Nobody has ever measured this file
against 200.

**And the operative rule is already written, in the section Andrew's ruling produced:**

> **Rule for editing this file:** *a principle earns its place by being **actionable without its
> incident**. If you cannot state the mechanism without retelling what happened, the mechanism is not
> yet extracted.*

**That IS the mechanisms-only test.** So the answer to your question is that the file already answers
it, and the line count is a **symptom** whose only diagnostic value is prompting the audit — which is
exactly what it just did.

**Scored against the real test, all five post-cut additions PASS**: each states a mechanism without
requiring its incident, including §5. **342 lines of mechanism is not the same finding as 342 with 140
of restatement, and this is the first case.** The one genuine defect I found is **~3 duplicated lines
in §5** — and a scope question that is not about size at all.

**Consequence for the remedy: there is no line-count remedy to apply.** Cutting to 200 would remove
working mechanisms to satisfy a number nobody has ever enforced. If the file should be smaller, the
argument has to be *"these specific mechanisms belong in another family"* — which is §3c, and which is
a **relocation**, not a cut.

---

## 5. WHAT I WOULD FLAG ABOUT THE AUDIT ITSELF

**You asked for your section first and hardest and I have given you that** — but the more useful
finding went the other way, and I want to be explicit that **the strongest critique in this analysis
is of the FRAMING, not of §5.** §5 survives on content and is questionable only on address. The
cutter's three additions, which the framing cast as the damning exhibit, are the three most defensible
edits in the file.

**Two conduct notes, recorded because you recorded yours:**
- You told MSTR~Z the file was one *"Andrew personally cut"*, caught it before routing, and corrected
  to Andrew-**directed**, executed by CRO. **I confirm the correction: `4defd7ff3e` is authored
  `4.0.0_SA_CRO`.** The distinction is load-bearing exactly as you said — a directed outcome is
  maintainable as execution, which is *also the strongest argument that the cutter's three repairs
  were legitimate*.
- Your TO's first commit was refused by the stage-8 lint and you caught it only via `${PIPESTATUS[0]}`
  rather than `$?` through a pipe — **the binding you had restated twenty minutes earlier, catching
  its first live instance on its own author.** That is the same shape as the finding above: the
  instrument was fine and the reading was one layer off.

---

*Analysis only. No line of `CONTROLS_OVER_CARE.md` was edited by me. Removal, relocation and the
~200 ruling's status remain with their owners; the ~200 question is arguably Andrew's, and this
analysis was written to make that decision cheap rather than to pre-empt it.*

# CVO — **CORRECTION 4.** My P0 headline was false. The tool HAS run on SEV1 surfaces — **by hand**. It is a *convention*, not an absent tool. Shape D, mine, again.

**archetype:** VALIDATE

**Date:** 2026-07-10 ~03:21–03:26Z · **Agent:** 3.0.0_SA_CVO
**Corrects:** the headline of my own P0 log + commit (`comp-surface-check … has never once run on a SEV1 surface`).
**Raised by:** `1.0.0_SA_CTO` `031945Z` — *"62 rows name `ModelPortfolios`. The TOOL has run on those paths, many times."*

---

## 1. The false sentence, and it is mine

> **"`comp-surface-check` has never once been invoked on a commit that touched a SEV1 surface."** — my commit message,
> and the title of `cvo_P0_ANDREW-DIRECT_…`.

**FALSE.** Measured (controls first: `surface-check` overall = 5,392 rows; negative control `zzz_nonexistent` = 0):

    rows in org/compiler-tools-log.md naming ModelPortfolios          : 73
    ...of those, also naming comp-surface-check                       : 36
    rows naming surface-check AND a SEV1 watch file, recorded as FAIL : >= 4

**The tool has run on SEV1 surfaces, repeatedly, and it has recorded FAIL.** It ran because **CLAUDE.md Rule 20 tells
an agent to run it by hand** when touching MP / benchmarks / ADVI.

## 2. What is actually true — CTO's framing, and it is better than mine

> **The SEV1 "gate" is a MANUAL CONVENTION. The automation that appears to enforce it is structurally incapable of
> reaching the files it names.**

Both halves survive, and only the second was ever mine:

- **Never invoked by any automated gate.** `safe-commit` is parent-scoped with **zero** submodule handling and can
  only ever hand it the gitlink `portal`, never a file inside it. Portal has **no pre-commit hook**. Pre-push is
  VALGATE + `tsc`. **Portal CI: 0 of 3 workflows invoke any `comp-` tool.** Every zero controlled.
- **Frequently invoked by hand**, per Rule 20, and it correctly returns `rc=2` / `CRITICAL … BLOCKED (SEV1)`.

**A convention is not a control.** It holds exactly as long as every agent remembers, and it leaves no artifact when
someone forgets. But *"the gate has never run"* is a different and false claim, and I made it.

## 3. My body was right. My headline was not. **Shape D, third instance, mine.**

My log's §2 says, accurately: *"invoked at NO point in the portal lifecycle — not at commit, not at push, not in
CI."* That is correct and it is what I measured. **The title generalized "no automated invocation" to "no
invocation."**

Forty minutes ago I named this shape for Andrew and put it in the record:

> *"the BODY carries the correct disjunction; the HEADLINE picks one branch, because a headline is rewarded for
> being decisive; downstream readers quote the HEADLINE."*

I then committed it, in the commit **message**, which is the single most-quoted artifact I produce. **The
countermeasure I proposed — a claim's headline may not be more decisive than the weakest limb of its grounding
block — would have caught this, and I had not applied it to myself.**

## 4. And a second error, inside the check of the first

I measured the verdict distribution with `awk -F'|' '{print $(NF-1)}'`. **28 rows returned the literal string
`VERDICT`** — a column header. The log's rows have variable width, so a positional field index binds to different
columns on different rows. **My verdict distribution is unreliable and I am not reporting it.** Only the floor
survives: **≥ 4 FAIL rows exist**, which is sufficient for the correction and nothing more.

Shape A (over-broad / mis-bound match rule), in the instrument built to check Shape D. **Sixth of the night, fourth
of mine.**

I also cannot reproduce CTO's `62`. Under my rule it is `73` / `36`. **Neither of us stated the rule.** I am not
adjudicating it; the number is not load-bearing for the correction and **a number without a rule is not a number.**

## 5. What survives, unchanged

- `comp-surface-check` **is correct and discriminating**: `rc=2` on 3/3 SEV1 files, `rc=0` on 2/2 non-critical,
  `selfcheck` clean. **CTO's original premise — "decorative" — remains falsified.**
- **Nothing automated gates the SEV1 surfaces.** Not `safe-commit`, not a portal pre-commit, not pre-push, not CI.
  **The exposure is unbounded**, not bounded to local-commit-to-push.
- **`SURFACE_ACK` is dead code** — `safe-commit` never reads the exit status, so the audited-override branch is
  unreachable.
- **P0-b (the `|| true` repair) is a placebo** for the SEV1 surfaces and must not be certified as a restoration.
- **Harm is NOT demonstrated.** No served value is shown to have changed. The absence of the control is the finding.
- CLAUDE.md:38 (`Gates: … comp-surface-check`) and :68 (`auto in safe-commit`) are **false as built.**

## grounding

- **applied:** `org/compiler-tools-log.md` — 73 rows name `ModelPortfolios`, 36 of those name `comp-surface-check`,
  ≥4 recorded FAIL; controls: 5,392 surface-check rows overall, `zzz_nonexistent` → 0
- **exercised:** the `awk` field-index shown to bind `VERDICT` (a header) as a verdict on 28 rows
- **NOT established:** the true verdict distribution of the manual runs (**my measurement is broken**); whether any of
  the 17 SEV1-touching commits was preceded by a hand-run of the tool; CTO's `62` under any stated rule

## What you should have asked but did not

**"Which of my sentences is the one that will be quoted?"**

Not the log body — nobody reads a log body. **The commit message.** It is what `git log` prints, what the next
agent greps, what a review cites, and what survives the session. It is the single artifact of mine with the widest
reach and the least scrutiny, and **it is the one place I write in headlines.**

Tonight I put *"the SEV1 gate has never once run on a SEV1 surface"* into the permanent record of this repository,
one commit after publishing the law that a headline may not out-run its grounding block. The body beneath it was
correct, controlled, and hedged. **Nobody would ever have read far enough to find that out.**

**Every countermeasure I have proposed tonight lints a finding. Not one of them lints a commit message.**

— 3.0.0_SA_CVO

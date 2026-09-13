# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 53 (covers ticks 52-53)

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-13T07:02:01Z**
Tick 51's log is `@962bacecac`, committed `2026-09-13T02:22:32-04:00` (author time, not the
filename). Tick 52 was QUIET and wrote nothing; the ruling below arrived after its output.

---

## 1. `Z-W17-S3` RULED -- `Z-S48` `@b516193123`

`2.0.0_SA_COO~Z` (22320) measured a **second live ticker-keyed `asset_class` store** and routed the
question here rather than ruling it, which was correct: `C-ONE-SOURCE` is a PRD constraint and its
reading is the author's.

**Read at source, not from the paraphrase.** PRD s.4 `:150-156`: *"the classification originates in
ONE place and flows to every surface; no surface re-implements it"*, settled at v0.4 to mean the
served table `etf-classifications`. Positive control: the token appears 4 times, so the section
exists and the grep is not vacuous.

**Then measured in SOURCE rather than inferred from a table name:**
```
opal-partners-data/etf_classifier.py:36    table_name='bd-securities'  (default)
                            :27            "Full table scan of bd-securities on first instantiation"
opal-partners-data/lambda_function.py:1026 "Classify a holding via ETFClassifier (bd-securities)"
```
⛔ **NOT MERELY A SECOND STORE -- A SECOND MODULE NAMED `ETFClassifier`, RE-IMPLEMENTED, ON A
DIFFERENT TABLE.** That is exactly the act the constraint's second clause forbids.

> **BOTH HALVES ARE TRUE AND THEY ARE NOT IN TENSION.** Within the domain `C-ONE-SOURCE` was SETTLED
> over -- POSN's own two surfaces -- **it HOLDS.** Read literally and unqualified, **the SENTENCE IS
> FALSE.** The defect is the constraint's SCOPE, not its substance: **the same shape as the MECE
> check corrected at v0.6**, where a true statement about one population read as a claim about a
> wider one. That is twice on this document now, and both were this seat's text.

**RULING:** (a) scope `C-ONE-SOURCE` to the surfaces this project owns; (b) disclose `bd-securities`
and the partners `ETFClassifier` on the `Z-S42` pattern, out of POSN's write scope, carrying the
measured **0 of 13 agreement**; (c) **name the non-discriminating check in the same breath.**

⭐ **(c) IS WORTH MORE THAN (a) AND (b) TOGETHER.** Ten of the thirteen disagreements carry
`alternatives`, **which IS one of the five ratified classes** -- so a bar shaped *"the served value is
one of the five"* **PASSES on all ten.** A check that cannot fail in the broken world, and **the
third time this project has recorded that shape.** Naming it now is what stops a cell being cut on it.

**Carrier:** s.4 is frozen mid-round-4, so the text lands in the round-4 L10 addendum exactly as
`Z-S42`'s line landed in v0.6. The ruling is made now and any seat may cut from it today.

## 2. TWO THINGS DELIBERATELY NOT RULED

⚠ **CROSS-FIRM: NOT ALLEGED.** `bd` **is** a firm token here (`opal-data-bd`; the guard's own comments
treat bd/cot/inf as firms), which is why the question arose. But `ds-precommit-check.py`'s
`_CROSS_FIRM_FOREIGN_BUCKETS` and `_CROSS_FIRM_FOREIGN_KEY_PREFIXES` enumerate **buckets and key
prefixes, not DynamoDB tables** -- so a cross-firm read through a table sits outside that guard
entirely. **No measured basis to allege a violation, and none is alleged.** The table-blindness is
recorded as a fact for the gate's owner, not as a finding against anyone.

⚠ **A NEAR-MISS RECORDED RATHER THAN BURIED.** This seat first read the partners lambda as the SAME
publisher `Z-C-S55` named -- which would have unified two findings neatly and satisfyingly. `Z-C-S55`
describes a four-key book allocation at lines 469-472; **those lines in this file are a
`serve_s3_json_nocache` helper.** The line numbers refused the unification and the claim was dropped
before it was written. Whether the two are nonetheless related is NOT settled here.

**Accepted as measured and NOT re-ruled:** 22320's twelve-member retag set (VNQ, reachable only
because round 3 keyed on `sub_asset_class`), and VNQ as the only member arming `C-RETAG-SAFETY`
(1 of 12 trips where round 3 read 0 of 11 -- a control whose DOMAIN was short, Rule 24 one layer
down). Retag stays **NO-GO**; a twelfth member licenses nothing.

## 3. OPEN CALLS / COMPLETION

```
OPEN CALLS IN SCOPE: 0 adjudicable · 2 RESERVED · NO PITCH   (all-reserved tell does not fire)
COMPLETION TEST: NOT DONE -- 0 of 2 complete (denominator: 2 projects, 2 of 14 live directives)
  AMGT_RESAPP  EXECUTING  REACHABLE  0 OPEN of 47 -- L8/L9 awaiting the CVO keystroke, with Andrew
  POSN_ASTTAX  EXECUTING  REACHABLE  6 OPEN of 19 -- round 4 draining (was 8; AT4-s-1, AT4-s-4 done)
  UNREACHABLE: 0   HELD-AT-STOP: not reached
```
`3.0.0_SA_CVO~Z` re-measured this tick: ALIVE as `python` at 17848, **`bridge-state.json` still
ABSENT** -- unbound, needing the human keystroke MSTR has already put in front of Andrew. **No nudge
and no second escalation:** mail cannot reach an unbound seat and MSTR said so explicitly.
**Push state:** `origin/SITEZ 246b1d35c8`, local ahead 8. `HEAD:portal e85f6eb84f`, unmoved.
No TO cut, no dispatch, no apply, no retag, no deploy, no promote.

## Compiler Tools

`C-ONE-SOURCE` read at source with a token-count positive control before ruling on it · a native
`Grep` over `infra/aws/lambda` for the second store, then the two consuming files read at their own
lines rather than trusted from the routing message · `ds-precommit-check.py`'s cross-firm
enumerations read directly, which is what turned an allegation into a recorded fact · `Z-C-S55`'s
stated line numbers checked against the candidate file, which killed a tidy but false unification ·
`Get-Process` on the CVO PID **with the process name**, per the two-field rule · the fence-line
channel reader admitting both block shapes · `git status --porcelain` before the append · `date -u`
at the write · post-commit `git show HEAD:` with a `Z-S99` negative control · `safe-commit.sh -F`
with a non-shell-written message file · short send subjects.

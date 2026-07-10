# CVO — **CERT AMENDED: `comp-iam` CERTIFIED** (scoped) @ HEAD `40e28fe1f` ⊃ `2119e91af`. P1a **closed and guarded**. And **I RETRACT my P1b** — it matched a **docstring**.

**archetype:** VALIDATE

**Date:** 2026-07-10 ~04:05–04:12Z · **Agent:** 3.0.0_SA_CVO
**Amends:** my cert of `6f3751a34` (P1a OPEN, P1b "demoted, still exists").
**Subject:** `_iam_resource_matches` + the `resource_verdict` surface, at HEAD `40e28fe1f` (contains `2119e91af`). Fix files clean.

---

## 1. **I RETRACT P1b. My claim matched a MENTION, not an instance.**

I wrote, in a signed cert: *"`assert len(st['dropped_detail']) == st['dropped']` still exists at `:505`."*

**AST parse of the test module:**

    REAL `ast.Assert` nodes matching that literal : 0
    GREP count of the literal (incl. docstrings)  : 1   <- line 505, INSIDE the docstring

The only live assertion mentioning `dropped_detail` is `:652`,
`assert not any('aws_iam_policy' in d for d in st['dropped_detail'])` — substantive, and not mine.

**He deleted the tautology.** My `grep -c` matched the passage in his docstring where he **quotes the assertion he
removed, and explains why.**

> **I asserted that a vacuous control survived, on the strength of a text match against a passage documenting its
> deletion.**

This is the deny-matcher firing on a quoted `echo`. It is `grep -ic 'CRITICAL'` matching *"no **critical** surface."*
It is `ps|grep` matching its own command line. **Committed by me, in the cert whose §4 says a test inherits every
blindness of the instrument it imports** — and the instrument I imported was `grep`.

**Seventh error. The most on-the-nose of the night.** The correct tool was `ast`, and it took one call.

## 2. P1a — **CLOSED, and GUARDED.** My probe was aimed one layer too low.

I probed the **private** `_iam_resource_matches` and got `False`. The defect and the fix both live on the **public**
surface. The do-er found the real shape and it is sharper than my finding:

> **`exact` was a caller-supplied FLAG. The invariant "a `*` in the ARN implies `exact is False`" was ASSUMED and
> never ASSERTED.** A literal `Key="prefix/*"` resolves `exact=True` *with a `*` in the ARN*, and the exact branch
> emits a confident `UNGRANTED-RESOURCE` against a **pattern**.

Fix, `extract_iam.py:751`: `exact = exact and '*' not in arn` — **derive the property from the evidence; never trust
a flag over the string it describes.**

**Exercised at the public surface:**

    resolved key, granted                    -> GRANTED
    resolved key, not granted                -> GRANTED-ACTION / UNGRANTED-RESOURCE
    UNRESOLVED BUCKET, exact=True   (P1a)    -> UNRESOLVABLE-RESOURCE        <- CLOSED
    UNRESOLVED KEY inside a granted prefix   -> GRANTED                      <- correct; see below

**Guarded — mutation M8, "trust the flag":**

    M0 (unmutated scratch)  3 failed   (the estate-reading tests; scratch has no TF tree)
    M8 (exact = exact)      4 failed
    DELTA = 1, by name:  test_the_exact_flag_is_never_trusted_over_the_ARN_itself

**And I nearly filed a false positive on him.** I expected the fourth case (`opal-data-inf/gold/*`, unresolved key)
to read `UNRESOLVABLE`. It reads `GRANTED`, and **`GRANTED` is right**: the policy pattern covers the *entire* ARN
pattern, so every key it could resolve to is granted. An unresolved **bucket** cannot be covered; an unresolved
**key inside a granted prefix** can. My expectation was wrong, not the tool. **Recorded, because a verifier's false
positive costs a do-er a night.**

## 3. My §4 finding — the recount that shared its parser — is **fixed at the root**

    :69   comment: "The census recount used to re-derive its total with `E._TF_POLICY_RESOURCE` --"
    :85   def _count_policy_blocks(hcl: str) -> int:      <- a hand-written, line-based counter IN THE TEST
    :583  independent_blocks += _count_policy_blocks(...)

**The recount now uses a block-finder the module does not own.** That was the deepest thing I found in that suite
and he did not patch around it — he built the second instrument. Test count 41 → 44.

## VERDICT

> **CERTIFIED**, scoped: `_iam_resource_matches` + the `resource_verdict` surface, at HEAD `40e28fe1f` (⊃
> `2119e91af`). P0, P1a, P1b, P2 all closed; **P0 and P1a additionally proven GUARDED by mutation with a
> control-attributed delta.**

**EXPLICITLY OUT OF SCOPE, and unverified:**
- **The `grants()` coverage surface** (`iam_cli.py:578`) — still resource-blind by design; never in this cert.
- **The two further defects the do-er reports** (the regex counting commented-out blocks; 5 of 26 "drops" being
  standalone policies with a false reason). **He found them by pulling my thread and he tested them. I have not
  re-derived them.** They are his evidence, not my cert.

## grounding

- **applied:** HEAD `40e28fe1f`; the three fix files clean; `extract_iam.py:751`
- **exercised:** public-surface `resource_verdict` on 4 cases; **AST parse** for real `Assert` nodes (0) vs grep (1);
  **M0/M8 mutation with delta attribution** (3 → 4, one new RED by name)
- **NOT established:** the `grants()` surface; the do-er's two new defects; whether `_count_policy_blocks` itself
  misses block forms (**a second instrument is not an infallible one**)

## What you should have asked but did not

**"Which tool did I use to check for a tool's misuse?"**

I spent this night establishing that a text-matcher cannot distinguish a mention from an instance. MSTR proved it of
`permissions.deny`; I proved it of CTO's `grep -ic`; the deny hook refused a pure `echo`. Then I ran `grep -c` over a
Python file to ask whether an assertion existed — **and it answered by finding the sentence in which its author
explained that it does not.**

`ast` was available. It took one call. It cost nothing. **I did not reach for it because I was not looking for a
defect in my own instrument — I was looking for a defect in his code, and the instrument is invisible when you are
using it to see.**

That is the whole night in one sentence, and it is the reason the do-er, who asked to be attacked at his own weakest
point before anyone found it, has finished this session with a certified tool while the verifier who attacked him
has finished it with seven retractions.

— 3.0.0_SA_CVO

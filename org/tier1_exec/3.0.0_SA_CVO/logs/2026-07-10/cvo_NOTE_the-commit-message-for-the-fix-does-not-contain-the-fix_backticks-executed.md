# CVO — NOTE: **the commit message certifying the fix does not contain the fix.** Backticks inside a double-quoted `-m` were **executed**, not quoted.

**archetype:** SCRIBE

**Date:** 2026-07-10 ~04:09–04:14Z · **Agent:** 3.0.0_SA_CVO
**Concerns:** the commit message of the amended `comp-iam` cert. **The log FILE is intact; only the `git log` summary is damaged.**

---

## What happened

I passed the cert summary to `safe-commit.sh -m "…"` in **double quotes**, containing two backticked literals:

    `exact`
    `exact = exact and '*' not in arn`

Bash performs command substitution on backticks inside double quotes. It **ran them**:

    /usr/bin/bash: line 2: exact: command not found      (x2)

and substituted the empty output. The commit landed. Verified:

    git log -1 --format=%B | grep -c "exact = exact and"   -> 0
    git log -1 --format=%B | grep -c ":751"                -> 1     (the line number survived)
    CONTROL: grep -c "CERTIFIED"                            -> 1     (the message is otherwise intact)

The recorded message now reads *"a caller-supplied  flag"* and *"fix at :751  --"*. **The name of the flag and the
text of the fix are gone.**

## Why it matters, and it is my own finding turned on me

Four hours ago I wrote, about my own P0 headline:

> *"Which of my sentences is the one that will be quoted? Not the log body — nobody reads a log body. **The commit
> message.** It is what `git log` prints, what the next agent greps, what a review cites, and what survives the
> session. It is the single artifact of mine with the widest reach and the least scrutiny."*

**The commit message certifying a fix now omits the fix.** A future agent grepping `git log` for
`exact = exact and` — the sentence the do-er and I both called the finding — will get **zero**, and a zero from a
`git log` grep is indistinguishable from *"this repair never happened."*

## The class

MSTR, ninety minutes ago, on LD-0274: *"the commit message could not quote the banned literal — a control that
forbids the record of the thing it controls."*

Same shape, different mechanism. **There it was a deny rule; here it is the shell.** Both times, a string intended
as a **mention** was taken as an **instruction**, and the record of a control lost the control's own text.

    deny matcher    fires on a quoted `echo`                    (MSTR, exercised)
    grep -ic        matches "no CRITICAL surface"               (CTO, retracted)
    ps | grep       counts its own command line                 (COO, retracted)
    grep -c         matches the docstring quoting a deletion    (mine, retracted, one commit ago)
    backticks in -m EXECUTES the fix it is quoting              (mine, this note)

**Five layers — a permission matcher, a search tool, a process lister, a source grep, and the shell itself — and not
one of them can distinguish quoting a thing from doing it.** That is not five bugs. It is one property of the
substrate we build controls on, and every control we own inherits it.

## Disposition

- **No amend, no rebase.** `git commit --amend` is gated (ADHC_OWNPTH.010) and `CLOUD` is shared. **The record is
  append-only and this note is the append.**
- The two lost strings, recorded here in a file the shell never parsed:
  - the flag is named **`exact`**
  - the fix is **`exact = exact and '*' not in arn`** at `extract_iam.py:751`
  - the rule is: **derive the property from the evidence; never trust a flag over the string it describes.**
- The amended cert's **content is unaffected** — it lives in
  `cvo_CERT_AMENDED_comp-iam_CERTIFIED_scoped_and_I_RETRACT_my_P1b_which_matched_a_DOCSTRING.md`, written by the
  `Write` tool, which does not pass through a shell.
- **Practice, effective now:** every `-m` carrying code goes in **single quotes** or a heredoc. Backticks and `$(...)`
  in a double-quoted commit message are executed.

## grounding

- **exercised:** `git log -1 --format=%B` grepped for the two literals (0 and 1) with a positive control (`CERTIFIED`
  → 1); the two `bash: exact: command not found` lines in the `safe-commit` output are the substitution firing
- **NOT established:** how many earlier commit messages in this repo lost content the same way. **Nobody would know.
  A commit message that lost a word looks exactly like a commit message that never had it.**

## What you should have asked but did not

**"How would we ever detect this?"**

We would not. A truncated commit message is syntactically valid, semantically plausible, and has no oracle. The only
reason I caught it is that `bash` happened to print `command not found` to stderr — **the failure announced itself
by accident, because `exact` is not a command.** Had my flag been named `test`, or `time`, or `printf`, the
substitution would have succeeded silently, replaced the fix with that command's output, and I would have committed
it without a word of warning.

**Every commit message in this repository that ever contained a backtick is suspect, and there is no census of them
that is not itself a grep.**

— 3.0.0_SA_CVO

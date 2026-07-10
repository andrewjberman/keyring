# CVO — NEVER#7 is **UNVIOLATED**, established with a **pattern-validated** detector. And my own first detector reported **the commit that created NEVER#7** as a violation of it.

**archetype:** VALIDATE

**Date:** 2026-07-10 ~04:18–04:26Z · **Agent:** 3.0.0_SA_CVO
**Amends:** my *"there is no post-hoc oracle"* (too strong — CTO, correct) **and** CTO's `^rebase` detector (blind to the form the rule names first).
**Scope:** this machine's two reflogs, within retention. Nothing else.

---

## 1. CTO's correction accepted: an oracle exists

*"There is no post-hoc oracle"* is **false**. Every agent shares one working tree on one machine, and its reflog is
a post-hoc oracle. Weak, local, bounded — but real. **My sentence was too strong in the direction that matters.**

## 2. But his detector is blind to the operation the rule names FIRST

**Exercised** — a real `git pull --rebase` in a scratch repo writes:

    pull --rebase (finish): returning to refs/heads/master
    pull --rebase (pick): local
    pull --rebase (start): checkout ca40a626...

    `grep -cE '^rebase'` against those three  ->  0

**A `git pull --rebase` never writes a reflog subject beginning `rebase`.** CTO's `^rebase → 0` is therefore silent
about `pull --rebase`. **His `^pull → 0` is what actually covers it**, and it does — my scratch shows `^pull` catches
all three. **His conclusion holds; one of his two controls was doing all the work and neither of us knew which.**

His control was `^commit → 5,436`. **That controls the RECORDER, not the PATTERN.** It proves the reflog records
things. It cannot prove that `^rebase` would match a rebase. *Same law, one turn later, and I repeated it.*

## 3. My "corrected" detector flagged the rule's own founding commit

I proposed `grep -ciE '(^|[[:space:]])rebase'` as the fix. It returned **4** on the workspace reflog. All four are
**commit messages**:

    4841: commit: claude-md(NEVER, Andrew-direct): no rebasing on shared branches -- git rebase AND git pull --rebase both b...
    5119: commit: log(ADHC_GLDINC 2240Z): A_01 incremental rebased+PROVEN 3/3 byte-identical ...
       3: commit: verify(F-004 pass2 NEVER#7): I RAN THE BANNED OPERATION ...        <- mine, tonight
       5: commit: note(record integrity): ... git pull --rebase ...                   <- mine, tonight

> **Line 4841 is the commit that CREATED NEVER#7.** My detector reported the rule's founding commit as a violation
> of the rule. Two more hits are my own commits *about this finding*.

**Ninth instance tonight of a text-matcher taking a mention for an instance — inside the detector I proposed one
command earlier as the correction to CTO's.** CTO predicted it in his subject line before I ran it.

## 4. The validated detector, and the answer

**Anchor on the operation, not the word.** And control the *pattern*, not just the recorder:

    detector:  grep -cE '^(rebase|pull --rebase)'

    PATTERN CONTROL  scratch repo in which a real `pull --rebase` executed  ->  3   (it can see a one)
    workspace reflog (5,448 entries)                                        ->  0
    portal submodule reflog (144 entries)  [CTO had not checked this]       ->  0

> **NEVER#7 has NOT been violated in this working tree, nor in the portal submodule, within reflog reach.**

## 5. The oracle's scope, stated so nobody over-reads it

- **Local.** One machine, one tree. Blind to any other clone, worktree (`feature_clb`), or agent's machine.
- **Bounded.** `gc.reflogExpire` unset → ~90d default; the **oldest workspace entry is `2026-06-09`**, so reach is
  ~31 days. **The DT incident is dated 2026-06-12 — inside that window — and this tree shows no rebase.** The
  incident therefore did not occur in *this* tree, or did not occur as a HEAD-moving op here. **Not adjudicated.**
- **Demonstrated sensitivity is narrow.** The workspace reflog's subject distribution is **`commit` ×5,438 and
  `reset` ×12 — nothing else.** No `checkout`, no `merge`, no `pull`, ever. Its sensitivity to `pull`/`rebase` is
  established **only by my scratch control**, never by an in-tree instance. **It has never been asked the question
  in anger.**

## 6. What survives, unchanged

The enforcement finding is untouched by the good news:

    git rebase         BLOCKED (bash, exercised) / UNGATED (PowerShell) / 0 deny rules
    git pull --rebase  UNGATED (bash, EXERCISED: HEAD rewritten) / UNGATED (PowerShell) / 0 deny rules

**The tree is clean. The gate is still absent.** *"We have not been robbed"* is not *"the door is locked."*

## grounding

- **exercised:** a real `git pull --rebase` in a scratch repo → reflog subjects captured verbatim; the anchored
  detector run against that scratch repo → 3 (pattern control passes)
- **applied:** workspace reflog 5,448 entries (`^commit` 5,436 positive control, `^zzz` 0 negative control);
  portal reflog 144 (`^commit` 140, `^zzz` 0); subject-prefix distribution; oldest entry `2026-06-09`
- **NOT established:** whether a rebase occurred in `feature_clb`, another clone, or before 2026-06-09; where the
  2026-06-12 DT incident actually occurred; whether `git config pull.rebase true` is set anywhere (**residual**)

## What you should have asked but did not

**"What did my detector's ZERO ever have the power to say?"**

CTO's `^rebase` could never have caught the operation NEVER#7 names first. Mine caught the sentence that forbids it.
The anchored one catches both — and I only know that because I made a rebase happen and read what git wrote down.

Three of us, in ninety minutes, built three detectors for one rule. **The first was blind, the second was
self-incriminating, and the third is trustworthy only because a real rebase was performed in a scratch repo so the
pattern could be validated against an instance rather than an intention.**

Every zero in this estate is one of those three, and **from the outside they are identical.** We have spent the
night learning that instruments cannot audit their own completeness. **The nearer truth is simpler: a search pattern
is a hypothesis about what the world writes down, and almost nobody ever tests it against a world that wrote.**

— 3.0.0_SA_CVO

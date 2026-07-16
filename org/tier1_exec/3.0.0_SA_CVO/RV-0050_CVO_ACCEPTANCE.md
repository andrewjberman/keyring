# RV-0050 — CVO independent acceptance pass

**archetype:** VALIDATE

```
record:        RV-0050 CVO acceptance
reviewer:      3.0.0_SA_CVO (independent; Andrew-direct, this session)
subject:       org/tier0/reviews/RV-0050.md  (window mstr-review-0045..67aa99d3f)
verdict:       ACCEPTED-CVO -- on independently re-derived grounds, with 5 carried findings.
watermark:     ADVANCE AUTHORIZED. Tag `mstr-review-0046` at 67aa99d3f -- MSTR applies it
               (tagging is MSTR's mechanism + the comp-tagauthz gate; the CVO does not tag).
re-measured:   2026-07-16, at live HEAD 0b3786846 (NOT RV-0050's pinned END) per LD-0278.
```

## 0. Independence disclosure — READ THIS FIRST

**I am independent of the RECORD'S AUTHOR (MSTR). I am NOT independent of the WINDOW.**
`3.0.0_SA_CVO` authored **109** commits in this window and `3.0.0_SA_CVO~B` a further **92** —
**201 of 2,296 (8.8%)**. For those, this pass is self-review, and it carries exactly the weakness
that makes MSTR proxy-ineligible. The CVO route cures the *authorship* conflict RV-0050 named; it
does not cure mine. **Andrew should know the 8.8% is unreviewed by a disinterested party** — I
surface it rather than let the word "independent" cover it.

## 1. What I re-derived (not read) — every number reproduces

Measured from the workspace root (RV-0050 caught a CWD pathspec artifact in its own pass; I
controlled for the same).

| Claim | RV-0050 | My measure | |
|---|---|---|---|
| window commits `f02eab077..67aa99d3f` | 2,296 | **2,296** | exact |
| author identities | 38 | **38** | exact |
| top-committer table (10 rows) | — | **all 10 exact** | exact |
| constitutional log in-window lines | 2,329 | **2,329** | exact |
| constitutional in-window OVERRIDE | 0 | **0** | exact |
| commit-scope log in-window lines | 2,407 | **2,407** | exact |
| OVERRIDE / NEVER-OVERRIDE / SENSITIVE-OVERRIDE | 36 / 2 / 1 | **36 / 2 / 1** | exact |
| TAGAUTHZ_OVERRIDE / REDACTION / WARN / SENSITIVE-BLOCK | 1 / 1 / 4 / 1 | **1 / 1 / 4 / 1** | exact |
| S-distribution | S1 8 / S2 22 / S3 3 / S4 3 | **8 / 22 / 3 / 3** | exact |
| LD census LD-0261..0296 | 36 | **36** | exact |
| law docs untouched | untouched | **0 in-window, 0 post-END-to-HEAD** | holds at live HEAD |
| F-002 (RV-0048 landed unmodified) | landed | **1 commit, never re-touched** | true |

**Negative claims re-measured at LIVE HEAD, not the pinned END** (the LD-0278 / RV-0047 F-015 rule
RV-0050 itself invokes): the constitutional-log zero holds across **359 further lines** to
2026-07-16T14:42Z. RV-0050 re-measured at *its* write-time; that is stale for *my* verdict, so I
re-ran it. It holds.

**Field-parse, not token-grep.** My first tally used `grep -oE '\bOVERRIDE\b'` and was **wrong** —
`\bOVERRIDE\b` matches inside `NEVER-OVERRIDE`, `\bBLOCK\b` inside `SENSITIVE-BLOCK`. Parsing
field 2 whole fixed it, and the tally then **reconciles to the denominator** (2269+84+36+6+4+2+1+
1+1+1+1+1 = 2,407 = the in-window line count). That reconciliation is what surfaced F-B below —
a tally that sums to its denominator cannot hide a token.

## 2. Why I accept despite F-A: I re-grounded the fact the instrument only asserted

RV-0050's append-only PASS is void (F-A). But the *underlying question* — was the audit base
tampered with — I answered substantively, which is why the window can be accepted on **my**
grounding rather than RV-0050's:

- The 17-record redaction was **Andrew-authorized** (verbatim: *"clean up the noise overrides (the
  testing ones)"*), and the pre-cleanup file was **archived FIRST to a tracked path**
  (`org/audit/archive/2026-07-13T144931Z/…`, commit `fcff61ebc`, 13,373 lines — present, and the
  archive itself has exactly 1 commit and is clean vs HEAD).
- The phantoms were **not real bypasses**: 12 were `test_never_rules_gate.sh` fixture runs, 5 an
  RV-0048 exercise harness — the F-019/F-020 marker-scope bug scoring a *mention* as a *bypass*.
  Only **3** OVERRIDE lines are dated 07-13, all MSTR BASE_EXEC, all legitimate.
- **Content-membership control, positive-controlled: 40/40 sampled historical records present in
  the archive; 0 missing.** No record loss.

**A false positive I walked into and had to kill.** My first archive-vs-live diff read
**DIVERGENT (~550 records)** and I nearly reported tampering. It was **my instrument**: the
archive is `Non-ISO extended-ASCII + LF`, the live log is `UTF-8 + CRLF`, so `grep -E` flipped to
binary mode on the archive and my `$1 <` filter also swallowed indented continuation lines. The
membership test — which is encoding-neutral — settled it. **The divergence is encoding; the
records are all there.** I record the near-miss because the mislabelled artifact in F-D is what
set the trap, and the next reviewer will walk into it too.

## 3. Scope limit on my own acceptance (the coverage denominator)

**My no-tampering finding covers the PRE-07-13 region ONLY** — that is the only region with a
tracked baseline to compare against. **The 07-13 → 07-15 remainder is unverifiable by any
instrument the fabric currently has**: the logs are untracked, so git cannot diff them, and no
snapshot exists after `fcff61ebc`. I am not asserting that region is clean; I am asserting **no
instrument can presently tell**, and that this is F-A's real cost. Ratifying the window does not
close that gap — F-A does, and it is owed.

## 4. Findings

```
- id:              F-A
  severity:        high
  type:            audit_integrity
  linked_ld:       null
  required_action: RV-0050 sec-3 asserts "Append-only integrity: PASS both logs -- every in-window
                   commit touching either log shows zero deletions (numstat walk)". BOTH logs are
                   UNTRACKED AND GITIGNORED: in-window commits touching them = 0 and 0. The walk
                   measures an EMPTY SET -- it is vacuously true and CANNOT FAIL ("an instrument
                   that cannot fail is not an instrument"). It is also DEMONSTRABLY WRONG in
                   substance: a real non-append edit (17 records removed, 07-13T16:16Z, MSTR
                   REDACTION) happened IN-WINDOW and the instrument reported PASS. Worse, CTO had
                   already established the fact two days earlier -- fcff61ebc (07-13): "THE ENTIRE
                   AUDIT EVIDENCE BASE WAS UNTRACKED ... the census found 4 logs when there are 13.
                   The ones missed are MASS-DELETION, SOVEREIGN-OVERRIDE, DEPLOY-BYPASS and
                   HALT-GATE." The review ran a git-based control over files git cannot see, after
                   a peer had published that git cannot see them. ACTION: (a) strike/restate the
                   PASS as UNVERIFIED before it is cited as ratified history; (b) give the review a
                   control that can fail -- track the logs, or periodic tracked snapshot + the
                   encoding-neutral membership diff used in sec-2; (c) 9 further audit logs
                   (incl. MASS-DELETION, DEPLOY-BYPASS, HALT-GATE) are named in fcff61ebc and are
                   reviewed by NOTHING -- no RV has ever walked them.
  owner:           1.0.0_SA_CTO (mechanism) / 0.0.0_AB_MSTR (record correction)
  due:             before the next mstr-review cites an append-only verdict

- id:              F-B
  severity:        medium
  type:            override
  linked_ld:       null
  required_action: The OVERRIDE_REVIEW is INCOMPLETE. The skill mandates a finding per override
                   line; RV-0050's F-001 covers 41 override-class lines. The true in-window
                   bypass-class population is 49 -- 8 lines are enumerated NOWHERE in the record:
                   FORCE-HEADMOVE x6 (12 commits discarded; 07-10 x3, 07-14 x2 incl. ONE
                   DISCARDING 7), FORCE-BYPASS x1 (07-09T19:18:59Z, 0.7.0_AE_CloudOps~A, 11 paths),
                   DISCLOSURE x1 (07-13, CTO, the phantom disclosure). FORCE-BYPASS is narrated in
                   sec-2 as RV-0046-dispositioned but is absent from the sec-3 tally -- and since
                   the watermark never advanced, RV-0046's window is INSIDE this one, so it is
                   owed enumeration here. ACTION: enumerate + disposition all 8.
  owner:           0.0.0_AB_MSTR
  due:             next mstr-review

- id:              F-C
  severity:        medium
  type:            audit_integrity
  linked_ld:       null
  required_action: NEVER#7 COMPLIANCE OF THE 6 FORCE-HEADMOVE LINES IS **UNDETERMINED** -- stated
                   as a question, NOT a breach (Rule 22: a causal claim is a hypothesis until
                   source-confirmed). Measured: the discarded commits are orphaned (reachable from
                   no branch); at least 2 resulting heads ARE on CLOUD/origin/CLOUD. Benign
                   readings dominate -- 3 lines say "-> amended" (an amend of an unpushed commit is
                   not a rebase and is legal), and `backup-pre-strip-20260714` indicates a
                   deliberate, backed-up history strip (CTO~Z .terraform untrack). But I CANNOT
                   CONFIRM ANY OF THAT FROM THE LOG, because **the FORCE-HEADMOVE audit line
                   records no branch field** -- the one field that decides legality is the one the
                   instrument omits. On a fabric whose #1 history rule is NEVER#7, a force
                   head-move discarding 7 commits should not be un-adjudicable from its own audit
                   record. ACTION: CTO disposition the 6; add a branch field to the line.
  owner:           1.0.0_SA_CTO
  due:             next window

- id:              F-D
  severity:        medium
  type:            truth_gap
  linked_ld:       null
  required_action: `fcff61ebc` labels the archive "Snapshot archived, byte-verified, tracked." It
                   is NOT byte-faithful: archive = Non-ISO extended-ASCII + LF (161 CR); live =
                   UTF-8 + CRLF (13,373 CR -- and 13,373 is EXACTLY the archive's line count, i.e.
                   the file was wholly re-encoded, CRLF->LF, at snapshot or at redaction). Content
                   survived (40/40 membership), so this is a LABEL defect, not a loss -- but the
                   label invites a byte-level comparison that produces a FALSE TAMPERING POSITIVE.
                   I hit it (sec-2) and only escaped via a membership control. NOTE the second-order
                   point: the redaction of 17 lines appears to have REWRITTEN ALL 13,373 LINES'
                   BYTES -- in an append-only log that is the maximum-blast-radius operation, and it
                   is invisible precisely because the file is untracked (F-A). ACTION: correct the
                   label to "content-verified, re-encoded"; if a byte-faithful baseline is wanted,
                   re-snapshot with `-Encoding utf8` (CLAUDE.md Git/PowerShell note) and byte-verify
                   for real.
  owner:           1.0.0_SA_CTO
  due:             next window

- id:              F-E
  severity:        low
  type:            drift
  linked_ld:       null
  required_action: `.tools/hooks/tests/test_never_rules_gate.sh` DOES NOT TERMINATE -- exit 124 at
                   both 120s and 240s. Its 9 positive-control arms all PASS (rebase x4, bare
                   terraform apply/destroy, .tools/terraform.exe apply, commit -m backtick, commit
                   -m $( ) -> the gate genuinely denies on a shared branch. But the suite hangs
                   after that section, so I COULD NOT EXERCISE THE MARKER-SCOPE ARMS -- the arms
                   that specifically close F-019. RV-0050's F-019 closure is therefore
                   SOURCE-CONFIRMED (never-rules-gate.sh:205-216 at HEAD documents same-simple-
                   command marker scope -- I read it and it is correct) but NOT
                   EXERCISE-CONFIRMED, while sec-2/F-007 render it as "closed", a behavioral claim
                   (Rule 22a: behavior -> exercise, never a config read). A suite that cannot run
                   to completion cannot gate anything ("a guard nothing invokes == no guard").
                   ACTION: fix the hang, then re-assert F-019 closure on a completed run.
  owner:           1.0.0_SA_CTO
  due:             next window
```

Minor, not findings: BLOCK is **84** in-window, not the 79 RV-0050 reports (BLOCKs are gates
working; the count is cosmetic, but it is the one census number that did not reproduce).
Instrument caveat for the next reviewer: the commit-scope log carries **two timestamp formats**
(`2026-07-13T16:16:00Z` and colonless `2026-07-14T022605Z`), so the `awk '$1>=S && $1<E'` filter
the skill *mandates* is doing a lexical compare across incompatible formats — harmless here (no
colonless line sits near a boundary) but a latent boundary defect in the review mechanism itself.

## 5. Verdict

**ACCEPTED-CVO.** The window's **conduct** is clean and independently verified: every material
census number reproduces exactly, the constitutional log carries **zero** overrides across 2,329
lines (still zero 359 lines later), all 41 enumerated override-class lines carry audited reasons,
the law docs are untouched at live HEAD, and the one CRITICAL in the chain (F-019) is
source-confirmed fixed. The 17-phantom redaction — the scariest-looking thing in the window — is
**exemplary practice**: Andrew-authorized, archived-before-cleanup to a tracked path, controls
stated, and the record even avoids the literal token names so a grep census would not miscount
itself. That is a fabric catching its own instrument error and documenting it honestly.

**The defects I found are in RV-0050's INSTRUMENTS and COMPLETENESS, not in the fabric's
behaviour** — and holding the watermark (already 7d / 2,296 commits stale against a 24h bound,
RV-0050's own high-severity F-003) would punish the fabric for the reviewer's tooling gap while
fixing nothing. F-A..F-E are carried, owned, and dated; **F-A is owed regardless of this
acceptance, and my sec-3 scope limit stands: the 07-13→07-15 audit region is unverifiable by any
instrument that currently exists.**

**RV-0050's F-003 is CLOSED by this pass** — the dead ACCEPTED-CVO route is live and has rendered.
F-001 (MSTR BASE_EXEC override class) and F-004 (D-003 hold-vs-retire) remain **at Andrew**; I do
not adjudicate them.

## What you should have asked but did not

**Not "is the append-only walk right?" but "how many audit logs does the review cover at all?"**
The answer is **2 of 13**. `fcff61ebc` names the missed ones — **MASS-DELETION, SOVEREIGN-OVERRIDE,
DEPLOY-BYPASS, HALT-GATE** — and no RV in the series has ever walked them. Every review to date,
mine included, has reported an override census whose **denominator is 2/13 of the evidence base**,
and has never printed that denominator. F-A fixes an instrument on the two logs we do read; it does
nothing about the eleven we do not. The four unread ones are, by name, precisely where a real
bypass would land — a deploy bypass or a halt-gate breach is *invisible to every governance review
the fabric has ever run*, and that is not a gap in a control, it is the **absence of one**. The
override count the whole review series rests on has never been a count of overrides; it has been a
count of the overrides that happened to land in the two files somebody thought to look at.

— 3.0.0_SA_CVO

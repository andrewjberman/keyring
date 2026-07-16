# F-A validation, the prefix test, and the redaction audit — 1700-1835Z

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE

## Summary

Continuation of `rv0050_cvo_acceptance_pass_1555-1700Z.md`. **Zero commits by me this window** —
the work was validation, and the deliverables landed in other agents' lanes by design (I am F-A's
validator and declined to be its author). Outcomes: **the watermark actually advanced**
(`mstr-review-0046` verified at `67aa99d3f`), **F-A validated and closed**, the escalation I raised
was **cured not merely owned**, and the append-only control the RV series never had now exists,
is ratified, and has been exercised against a real event.

**The instrument I proposed replaced the one I had banked as permanent** — and it exists only
because I tried to prove a colleague's claim false and it came back proving him right.

## Work Completed

### 1. F-A: NOT LANDED -> LANDED -> VALIDATED

- **Caught my own validation criterion certifying a phantom.** I had told CTO F-A validates on
  `git ls-files`. It **PASSED at ~1702Z on a fix that no longer existed.** Two independent
  defects: `git ls-files` reads the **INDEX, not HEAD** (a `git add -f` satisfies it with zero
  commits), and in a shared worktree **the index is not your own state** — it is a shared mutable
  a concurrent agent flips under you. **Retracted publicly; replaced with
  `git cat-file -e origin/CLOUD:<path>`** (the pushed durable record, immune to both).
- **The "ghost":** three probes ~2min apart showed a staged `.gitignore` block, then unstaged,
  then gone from the working tree / index / HEAD / all refs. I reported **MECHANISM: UNKNOWN and
  refused to guess** (Rule 22). Cause was `0.7.0_AE_CloudOps~B`'s own disciplined revert
  (owned-paths gate correctly blocked an AE from a BASE_EXEC file; they refused to force it),
  disclosed to CTO and not to me — **a routing gap, not a tree failure.** My "silently severed"
  framing was **wrong and withdrawn.** Rule 22 is the only reason "peer interference" was never
  published as a cause.
- **Declined to author the fix though I am in the lane** (`.owned-paths.yaml:1527-1528`,
  `.gitignore` = BASE_EXEC = CTO+COO+**CVO**). **I am F-A's validator; authoring it would close
  the finding with no independent eye** — the exact shape that made RV-0050 proxy-ineligible,
  90 minutes after I ratified a finding about it. Precedent honored: MSTR routed its own
  ANY_EXEC_OR_AE grant to COO to land (`7882fbbbd`). **Routed, not halted.**
- **VALIDATED** at `d8b34eaf3` + `b150952ba`: 4/4 durable at origin/CLOUD · **negative control
  narrow** (`comp-which-rail.log`, a non-audit `.log`, correctly still absent) · big two correctly
  still untracked · **SEMANTIC: the durable halt-gate log carries the 2 REAL sovereign-STOP
  overrides**, which existed in **no durable record anywhere** 20 minutes earlier.

### 2. The line-52 catch -> ~B's archive-rot escalation (theirs, downstream of mine)

`.owned-paths.yaml:52` carried a **CTO ruling from 07-13 saying the opposite**: *"The LIVE logs
stay gitignored (ten agents append continuously) -- we track only the SNAPSHOT."* Neither today's
ruling nor mine cited it. **Reconciliation: correct reasoning, wrong population** — true for the
big two (589 + 413 lines/day), false for four logs totalling **25 lines across ALL history**. That
over-generalization is *why* the four stayed invisible: `*.log` severed the trail by **pattern**,
then the blanket rationale severed it again by **rationale**. Without the description
reconciliation the fix would have been **housekeeper-reverted by the record**.

Chasing it, **~B found the rot** (their find, not mine): `org/audit/archive/` held **ONE** snapshot,
build day, **zero invokers** — and its halt-gate log's only entry was the `TEST_SERIAL` fixture. So
CTO's own (correct) fixture-filter applied to the archive returned **ZERO halt-gate overrides
ever**: **Andrew's exact stated 07-13 failure mode reproduced BY the remedy for it, in 3 days.**
Two individually-correct decisions composing into the defect.

### 3. The prefix test — proposed, ratified, exercised

Built only to check CTO's `13/13 byte-verified` claim on snapshot #2 (the exact label F-D proved
FALSE on #1). **My byte-compare returned "2 DIFFER" and the obvious headline was "byte-verified is
false AGAIN."** That would have been a **FALSE REFUTATION of a true claim, from the validator, with
a citation** — the third species, fired at the fix, by the agent who put the species in the cell 20
minutes earlier. **Stopped by asking what DISCRIMINATES churn from corruption before writing the
finding.** The archive is a byte-exact **PREFIX** of live; deltas +7 lines each, all timestamped
after the snapshot. **Pure append. Claim TRUE. F-D cured** (#2 is UTF-8+CRLF == live; #1 was
extended-ASCII).

```
                        byte?  order?  insertion?  churn-tolerant?
membership diff (mine)   NO     NO        NO            yes
byte-compare             yes    yes       yes           NO
PREFIX TEST              YES    YES       YES           YES     <- ratified, replaces mine
    head -n <archive_lines> <live> | cmp -s - <archive>
```
**`archive MUST be a byte-exact prefix of live`** is the append-only assertion F-A wanted: growth
at the tail is the ONLY thing it permits, which is precisely and only what an append-only log may
do — **so a prefix violation is DEFINITIONALLY a non-append edit.** CTO ratified it verbatim and
**retired my membership diff from the F-A record**; it lands in ~B's invoker as the integrity half
(age-of-newest = the liveness half).

### 4. The redaction: (recorded) -> AUDITED

Exercised the ratified instrument against the fabric's one known non-append edit:
```
EVENT: the Andrew-authorized 17-phantom redaction, 2026-07-13T16:16Z
  RV-0050's numstat walk  ->  PASS   (vacuous: empty set, cannot fail)
  PREFIX TEST             ->  FIRES  + localizes to line 12925 + enumerates all 17
                              (fires on the ONE file with an edit; SILENT on the three without)
REMOVED, classified:  12 x serial=1.0.0_SA_CTO  (test_never_rules_gate.sh fixtures)
                       5 x serial=0.0.0_AB_MSTR (RV-0048 harness)     = EXACTLY as MSTR claimed
```
I chased the one line that looked wrong — a removed record reading `reason=scratch branch cleanup`
that I suspected was a **real** CTO override swept in with fixtures. **It was not:** that is the
test suite's canned fixture string, which is why it repeats **12x byte-identical with an identical
`cmd=git rebase -i HEAD~2`**. **No real record was taken. MSTR's claim is now independently
verified byte-exactly, by an outside party, with an instrument that did not exist two hours ago.**

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| raw git plumbing (`cat-file -e`, `ls-tree`, `cmp`, numstat) | PASS | the validation mechanics; **no comp-tool fronts durable-record or append-only verification** — this window's standing gap, and the prefix test is the first instrument that closes it |
| raw grep on gate/lane internals | PASS | `# rail-checked:` markers carried (`.owned-paths.yaml` lane resolution, `halt-gate-check.sh:128`) — no comp-tool fronts classifier/lane-model reads |
| comp-pulse + comp-surface-check | n/a | **no commits by me this window** — the deliverables landed in CTO's and ~B's lanes by design (SoD: I validate, I do not author) |

**What worked:** *discriminate BEFORE refuting.* Churn and corruption produce an **identical**
signal under a byte-compare; asking what separates them turned a false refutation into the
session's best instrument. Also: the **prefix test as its own positive control** — it fired on the
one file with a known edit and stayed silent on three without.

**What failed:** two more of my own instruments. (1) `git ls-files` as a durability criterion —
**index, not HEAD, and a shared mutable besides**; it PASSED on a reverted fix. (2) `grep -vc
'TEST_SERIAL'` -> 12 on a 16-line file whose 13-line **header is indistinguishable from its data**
to a pattern match. ~B independently hit the same surface in the **opposite** direction
(`grep -c 'HALT-OVERRIDE'` -> 4 vs 3 true). **Three wrong counts, one 16-line file, one afternoon,
by finder and validator: that is a property of the FILE — a census-poisoning surface — not three
slips.** Both converged independently on `^[0-9]{4}-`.

**Gap found:** ASK-3 as first ruled covered the **inclusion** grep and missed the **exclusion**
grep. **Direction-independent form (adopted verbatim, and it is already CLAUDE.md law):** *resolve
the record set FIRST (anchor `^[0-9]{4}-`), then apply any predicate, inclusion or exclusion* —
"put the control on the RETRIEVAL, not the pattern."

## MCP Traffic

~15 messages. Significant: F-A **VALIDATED + RAVC-4 CLOSED** to CTO · the declining-to-author
routing (SoD) to CTO + ~B · the URGENT ghost report (**mechanism honestly UNKNOWN**, later resolved
as ~B's own disclosed revert) · snapshot #2 verification + the prefix-test proposal (**ratified,
replaced my membership diff**) · the redaction audit · **BINDING build note to ~B** (S2-forward
baseline). Two corrections **accepted against myself** (attribution drift; the "slip" framing) and
one **withdrawn in my favour by ~B** (a false credit they corrected unprompted).

## Blockers

**None.** Thread closed both directions; CTO confirms nothing owed either way.

## Current State

- **RV-0050 = ACCEPTED-CVO, CLOSED.** Watermark **`mstr-review-0046` VERIFIED APPLIED at
  `67aa99d3f`** (the authorized commit — checked, not assumed). First advance in 7 days.
- **F-A = VALIDATED + CLOSED** (`d8b34eaf3`, `b150952ba`). Four bypass-class logs durable at
  origin/CLOUD; the 2 real sovereign-STOP overrides safe; `.owned-paths.yaml:52` reconciled; four
  path rules closing ~B's UNDEFINED.
- **The rot is CURED, not just owned:** snapshot #2 at `ca6485e55`
  (`org/audit/archive/2026-07-16T175907Z`, 13 files, F-D's encoding defect repaired). Three days of
  the fabric's busiest window had been sitting only on this disk.
- **The prefix test is the ratified F-A append-only instrument**; my membership diff is **retired
  from the record**. It lands in ~B's invoker as the integrity half.
- **KNOWN-DIVERGENT BASELINE (binding, or the first alarm is a false alarm):** the `S1 -> S2` chain
  check on `git-author-override-audit.log` **fails legitimately and always will** — the authorized
  redaction sits between them AND S1's encoding is broken (F-D). **Baseline from S2 forward**; S1 =
  known-divergent pre-redaction, with authority citation, never a tamper.
- **Design law for the invoker:** the prefix test **detects the EDIT; a human rules on the
  AUTHORITY.** It has no opinion on who was allowed to do what — which is exactly why it cannot be
  argued into a PASS.
- **Lane:** registered, Monitor `blahiq3oa` live, zero crons, inbox clear. `3.0.0_SA_CVO~B` is a
  separate live lane (V4, event-armed) — untouched all session.

## Next Steps

- **[andrew]** F-001 — now with the corrected count (**10 BASE_EXEC / 12 total**, not the 6 or 7 in
  the records). **The direction favours the grant:** ENUMERATE was chosen on an understated
  denominator, so it is better supported than it was argued. And **F-004** (D-003 hold-vs-retire).
  Nothing else from this lane.
- **[0.7.0_AE_CloudOps~B]** the snapshot invoker — prefix test (integrity) + age-of-newest
  (liveness), **baselined from S2**, alarm-on-its-own-death per CTO. My baseline-freshness caveat
  becomes a **first-class alarm, not a note** — *a caveat with no instrument behind it is a
  hypothesis, and the estate reads hypotheses as clean.*
- **[1.0.0_SA_CTO]** F-B/F-C/F-D/F-E carried per Task #18; the 2/13 headline is in the SCTY
  foundation cell with 0.7.0~B.
- **[me]** nothing open. RAVC 4 closed on F-A. CVO~B's V4 stays event-gated on the served spine.

— 3.0.0_SA_CVO

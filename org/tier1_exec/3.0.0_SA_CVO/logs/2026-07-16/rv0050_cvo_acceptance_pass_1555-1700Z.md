# RV-0050 independent CVO acceptance pass — 1555-1700Z

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, COORDINATE

## Summary

Andrew-direct: independent acceptance pass on RV-0050 (MSTR proxy-ineligible; watermark stuck at
`mstr-review-0045`, 7d / 2,296 commits stale against a 24h bound). **Rendered ACCEPTED-CVO** on
independently re-derived grounds, with **6 findings** carried. Watermark advance authorized at
`67aa99d3f`; MSTR applies tag `mstr-review-0046` (tagging is MSTR's mechanism + the comp-tagauthz
gate — the CVO does not tag). RV-0050's own F-003 (the dead ACCEPTED-CVO route) is closed by this
pass.

The verdict was the small part. The pass found (a) the review's integrity control is structurally
incapable of failing, (b) the override count sitting under Andrew's F-001 ruling is wrong in all
three records that carry it, and (c) the governance series has never read 11 of the 13 audit logs
— including the four where a real bypass would land.

## Work Completed

### 1. Startup (org/XXX.md)

- `/watcher`: no orphan. `ps` showed a watcher for `3.0.0_SA_CVO~B` — **the V4 lane's own serial,
  not mine**; left untouched (self-scoped only, and it is LIVE by design). No process for the base
  serial + broker read NOT REGISTERED = genuine fresh session, so arming was correct rather than
  the 07-14 dual-COO collision case.
- Registered `3.0.0_SA_CVO` (PID 29904); LD-0290 session serial file written; persistent inbox
  Monitor armed (task `blahiq3oa`); `CronList` clean — **zero crons**, per the XXX.md CVO row.
- **Identity note:** `.comp-graph/.agent_context` reads `SERIAL=2.0.0_SA_COO` (shared file,
  last-writer-wins). Not an identity source per XXX.md Step 1; serial resolved from Andrew's word
  + the session serial file + the armed Monitor.

### 2. The acceptance pass — re-derived, not read

Every material census number in RV-0050 **reproduces exactly**: 2,296 commits / 38 identities /
all 10 top-committer rows / 2,329 constitutional lines with 0 overrides / 2,407 commit-scope lines
/ 36 OVERRIDE / 2 NEVER-OVERRIDE / 1 SENSITIVE-OVERRIDE / 1 TAGAUTHZ_OVERRIDE / 1 REDACTION / 4
WARN / 1 SENSITIVE-BLOCK / S1 8 S2 22 S3 3 S4 3 / 36 LDs / law docs untouched / RV-0048 landed
unmodified. Negatives re-measured at **live HEAD** (`0b3786846`), not RV-0050's pinned END, per
LD-0278 — the constitutional zero holds across 359 further lines.

**Two of my own instruments were wrong first and had to be fixed before they could be trusted:**

1. **Token-grep contamination.** `grep -oE '\bOVERRIDE\b'` also matches inside `NEVER-OVERRIDE`
   (hyphen is a word boundary); same for `\bBLOCK\b` inside `SENSITIVE-BLOCK`. Fixed by parsing
   **field 2 whole**. The corrected tally then **reconciled to the denominator** (2269+84+36+6+4+
   2+1+1+1+1+1+1 = 2,407 = the in-window line count) — and that reconciliation is what surfaced
   F-B. A tally that sums to its denominator cannot hide a token.
2. **A near-miss false tampering finding.** My first archive-vs-live diff read **DIVERGENT across
   ~550 records**. It was the instrument: the archive is `Non-ISO extended-ASCII + LF`, the live
   log `UTF-8 + CRLF`, so `grep -E` flipped to binary mode and my `$1 <` filter also swallowed
   indented continuation lines. An encoding-neutral **content-membership test** (positive-
   controlled) settled it: **40/40 records present, 0 missing.** I was one control away from
   putting a tampering claim in a governance record.

### 3. Findings issued (6)

| id | sev | subject |
|---|---|---|
| F-A | high | Append-only PASS is **vacuous** — both audit logs untracked+gitignored, in-window commits touching them = 0 and 0. The numstat walk measures an **empty set** and cannot fail; it reported PASS through a real in-window 17-record deletion. CTO had published the untracked fact 2 days earlier (`fcff61ebc`). |
| F-B | med | OVERRIDE_REVIEW incomplete — true bypass-class population **49, not 41**. Unenumerated: FORCE-HEADMOVE x6 (12 commits discarded), FORCE-BYPASS x1, DISCLOSURE x1. |
| F-C | med | NEVER#7 status of the 6 FORCE-HEADMOVE lines **UNDETERMINED** (stated as a question, not a breach — Rule 22). Benign readings dominate (3 are amends; `backup-pre-strip-20260714`), but **the audit line records no branch field** — the one field deciding legality is the one omitted. |
| F-D | med | `fcff61ebc` labels the archive "byte-verified"; it is **not byte-faithful**. Content survived (40/40); the label invites the false-tampering trap I hit. 2nd-order: the 17-line redaction appears to have **rewritten all 13,373 lines' bytes**, invisible because untracked. |
| F-E | low | `test_never_rules_gate.sh` **does not terminate** (exit 124 at 120s and 240s). Its 9 positive-control arms PASS, but the marker-scope arms closing F-019 could not be exercised → F-019 closure is SOURCE-confirmed, not EXERCISE-confirmed (Rule 22a). |
| F-F | high | **The count under Andrew's F-001 ruling is wrong in all 3 records, all understating.** RV-0050 says 6; grant `7882fbbbd` says 7; measured = **10 BASE_EXEC / 12 total** (3 on 07-13, 7 on 07-14). The 7 is the **07-14 day quoted as a window**. Direction **favours the grant**. |

### 4. Two corrections that stopped wrong records from landing

- **COO's self-correction — KILLED before landing.** COO was about to file a permanent correction
  impeaching their own "7" because "the census does not walk the SOVEREIGN-OVERRIDE log." A
  mis-mapping: author overrides land in `org/git-author-override-audit.log`, which **is** walked;
  `org/mcp/sovereign-registry-override-audit.log` holds **exactly 1 line** — COO's own
  `SOVEREIGN_UNFILTERED_READ` from 07-13, not an override. One read killed it. COO honored inside
  4 minutes, filed my framing instead, and retracted the bad mechanism to CTO.
- **COO's thanks to me — also corrected.** COO credited "the [STOP]". **No gate fired.** My
  subject began with a bare `STOP --`; the classifier at `halt-gate-check.sh:128` is
  `grep -qE '^\*\*Subject:\*\* *\[(STOP|HALT)\]'` and requires **literal brackets**. COO stopped it
  by *reading* it. Crediting the token would attribute the outcome to a mechanism not involved —
  the same class of error we had just killed. (Also: I got the proportionality right **by
  accident** — brackets would have hard-blocked COO's lane over a documentation error.)

### 5. CTO's open track-vs-snapshot determination — answered by measurement

CTO deferred the call to the SCTY cell's verification. Measured instead; it splits cleanly:

```
THE TWO WALKED (high-churn)              lines    last 24h
  org/git-author-override-audit.log     14,617      +589
  org/tier0/audit/ledger-hook-audit.log 10,732      +413
THE FOUR NEVER-WALKED                    lines    ALL HISTORY
  halt-gate / mass-deletion / safe-deploy-bypass / sovereign-registry-override
  COMBINED, ENTIRE HISTORY                  25
```

**TRACK the four** (25 lines ever; zero churn; not on the commit path). **DO NOT track the big
two** — `safe-commit.sh:121` writes the git-author log **during the commit** (`:338/:344/:392`),
so tracking it dirties every commit's own tree and turns every pull across ~15 concurrent agents
into a conflict at 589 lines/day — on a shared branch where NEVER#7 forbids the rebase people
would reach for. **Their gitignore is structural, not an oversight; the remedy would manufacture
the hazard.**

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-pulse (via safe-commit risk-reflex) | PASS x2 | denominator printed each run (1 file vs 1,239 danger nodes); danger map 57.7h stale — noted, not blocking a doc-only commit |
| comp-surface-check (auto in safe-commit) | PASS x2 | 1 changed file touches no critical surface; advisory-only, output read by hand per Rule 20 |
| raw git/awk window walks | PASS | the deterministic review mechanics — **no comp-tool fronts the RV window walk** (standing gap, unchanged since RV-0043 and re-noted by RV-0050 itself) |
| raw grep on hook/gate internals | PASS | `# rail-checked:` markers carried — comp-tools do not front hook-internal regex/classifier logic (`halt-gate-check.sh:128`, `never-rules-gate.sh:205-216`, `safe-commit.sh:121`) |

**What worked:** parsing **field 2** rather than grepping tokens, then **reconciling the tally to
its denominator** — that single control surfaced F-B (8 unenumerated bypass-class lines) and
nothing else would have. The encoding-neutral membership test with a **planted-mutation positive
control** is the only reason F-D was recorded as a label defect instead of a tampering claim.

**What failed:** my own first-cut instruments, twice — `\bOVERRIDE\b` matching inside
`NEVER-OVERRIDE`, and a byte-diff going binary-mode on a re-encoded archive. Both self-caught by
controls, neither by care. Also `test_never_rules_gate.sh` (exit 124, F-E) — could not exercise
the arms I needed.

**Gap found:** **the review series walks 2 of 13 audit logs.** `fcff61ebc` names the missed ones —
MASS-DELETION, SOVEREIGN-OVERRIDE, DEPLOY-BYPASS, HALT-GATE — all live, all real, verified this
pass. Every override census the RV series has published, **including the one I just ratified**,
carries an undeclared 2/13 denominator. Those four total **25 lines between them, ever** — they
were never unwalked because they were expensive. **Nobody looked.** Routed to CTO; landing in the
SCTY foundation cell with 0.7.0~B.

## MCP Traffic

7 messages total. Significant: verdict + tag authorization to MSTR; 4 findings + the 2/13 headline
to CTO (**all taken**, Task #18, F-A owner named provisionally = 0.7.0~B); F-F to MSTR + COO; the
STOP that killed COO's self-correction (honored, killed, retracted to CTO); ACK of the ANDREW-
DIRECT 15:43Z push-contention binding (batching; pushed **once** under rule 1 as gate-bearing,
landed first try, no contention). RAVC 4 **stays open** on all findings — I validate on artifacts,
not commitments.

## Blockers

**None.** Nothing in this lane is blocked. F-001 and F-004 sit at Andrew by design (his ruling,
not a blocker on me); F-A/F-C/F-D/F-E are owned at CTO with named windows.

## Current State

- **RV-0050 = ACCEPTED-CVO.** Record: `org/tier1_exec/3.0.0_SA_CVO/RV-0050_CVO_ACCEPTANCE.md` @
  `e1caaa6db` (verdict + F-A..F-E) and `1f91c5ab6` (+F-F). Both pushed to `origin/CLOUD`.
- **Watermark:** advance AUTHORIZED at `67aa99d3f`. **NOT YET APPLIED** — MSTR must tag
  `mstr-review-0046`. Until it does, the watermark is still `mstr-review-0045` and still stale.
  **This is the one open mechanical step of the whole pass.**
- **Two disclosures ride the acceptance and must not be dropped by whoever reads it next:**
  1. **I am independent of the RECORD'S AUTHOR, not the WINDOW** — CVO+CVO~B authored **201 of
     2,296 commits (8.8%)**; for those this pass is self-review, carrying the same weakness that
     makes MSTR proxy-ineligible.
  2. **Scope limit:** the no-tampering finding covers the **pre-07-13 region ONLY** (sole region
     with a tracked baseline, `fcff61ebc` @ 07-13T14:49Z). **07-13 → 07-15 is unverifiable by any
     instrument that currently exists.** Ratification did not close that; F-A does.
- **Finding ownership:** F-A → 0.7.0~B (provisional, mechanism gates at CTO) · F-B → MSTR · F-C,
  F-D, F-E → CTO (Task #18) · F-F → MSTR (RV record) + COO (grant justification) · F-001, F-004 →
  Andrew.
- **Lane state:** registered, Monitor `blahiq3oa` live, zero crons, inbox empty. `3.0.0_SA_CVO~B`
  is a separate live lane (V4, event-armed) — untouched by this session.

## Next Steps

- **[0.0.0_AB_MSTR]** apply tag `mstr-review-0046` at `67aa99d3f` — the watermark does not advance
  until you do. Correct sec-3/F-001 to **10 BASE_EXEC / 12 total** BEFORE Andrew rules F-001, and
  strike/restate the append-only PASS as UNVERIFIED before a later RV cites it as ratified history.
  **Do not close F-001 on the `0 overrides since END` reading** — the grant landed 07-16T14:52Z and
  that zero mostly predates it; it is a window measuring a boundary (the RV-0047 F-015 shape).
- **[1.0.0_SA_CTO]** F-C forensics + branch field on the FORCE-HEADMOVE audit line; F-D relabel;
  F-E test-suite hang; F-A mechanism choice — **the split is measured: track the four (25 lines),
  snapshot-with-cadence the big two.**
- **[2.0.0_SA_COO]** file the corrected framing (a day quoted as a window; window = 10) forward on
  the next record — `7882fbbbd` is immutable, NEVER#7 forbids rewriting shared history.
- **[andrew]** F-001 (now with the corrected count: 10-12, not 6-7 — the gap bites harder than any
  record said, so the grant is **better** supported than it was argued) and F-004 (D-003
  hold-vs-retire). Nothing else from this lane.
- **[me]** RAVC 4 open — validate on artifacts, not commitments: F-D on the corrected label, F-E on
  a completed suite run, F-C on the disposition + a branch field in a real audit line, F-A on a
  tracked path in `git ls-files` (not a plan). CVO~B's V4 remains event-gated on the served spine.

— 3.0.0_SA_CVO

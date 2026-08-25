# /estate-pull — the CVO daily ESTATE REPORT adjudication loop

**Authority:** Andrew-direct rulings 1-4a, 2026-07-30 (verbatim record:
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_RULING_SEMANTIC_EVOLUTION_PIPELINE_20260730.md`).
Ruling 3: **"CVO owns the loop, MSTR is backstop."** CVO-ONLY — any other serial invoking this
skill halts at Step 0 (the loop has ONE operational owner; MSTR's LD-0356 backstop rule is the
governance check, not a second operator).

## What this loop is

The estate-report pipeline (0.7.0_AE_CloudOps~B build) lands a DAILY report at 9a Eastern
(wall-clock, DST-following) in `s3://opal-estate-report/`:

```
daily/YYYY/MM/DD/estate-report-YYYY-MM-DD.{md,json}   <- pipeline writes: Kimi/K3 exec summary
                                                         + DETERMINISTIC changed-resource list
                                                         (git-commit-derived, ladder-bucketed)
                                                         + day-over-day SET-delta
manifest/YYYY-MM-DD.json                              <- pipeline writes FIRST (status RUNNING at
                                                         run start); rewrites PENDING on success,
                                                         FAILED (+failure_reason) on caught error;
                                                         hard crash leaves RUNNING + stale
                                                         started_at (loud and true)
config/_EPOCH.json                                  <- CVO writes ONCE at go-live flip (first
                                                         expected date; makes ABSENCE computable)
adjudicated/YYYY/MM/DD/estate-report-YYYY-MM-DD.md    <- CVO writes (this skill, Step 4)
```

**The manifest is a gate whose default state is the alarming one** (~B's formulation, design
canon): a missed day is not something a detector notices — it is the ABSENCE of an affirmative
flip. No SNS, no alarm, no notification machinery anywhere in this design (moratorium-clean by
construction; the report itself is Andrew-asked by name).

## Invocation

| Form | Behavior |
|---|---|
| `/estate-pull` | Full loop: enumerate PENDING days -> pull -> adjudicate with Andrew -> land -> flip. |
| `/estate-pull status` | Report-only: PENDING-day census, no changes. This is also the FIRST-ON-LOAD check form. |

## Step 0 — Identity + pipeline-exists gate

- Registered serial must be `3.0.0_SA_CVO` (base). Anyone else: halt, point at this header.
- `aws s3api head-bucket --bucket opal-estate-report` — **absent bucket = INERT**: the pipeline
  has not shipped yet; print one line and stop. (Same inertness contract as MSTR's backstop rule.)

## Step 1 — Enumerate + CLASSIFY every expected day (the manifest IS the oracle, and ABSENCE
## is a state — contract v2, 2026-07-30, the guard-shares-failure-mode fix)

```bash
aws s3api list-objects-v2 --bucket opal-estate-report --prefix manifest/ \
  --query "Contents[].Key" --output json
```
Compute the EXPECTED sequence: every date from `config/_EPOCH.json`'s first report date
through today. Diff against the objects present and classify each expected day — print the
full census with denominators:

| State | Meaning | Action |
|---|---|---|
| **MISSING** (no object, past day) | the run NEVER STARTED (scheduler/orchestrator/boot failure) | LOUD producer finding -> ~B lane; never absorbed |
| **RUNNING** + stale `started_at` | started, DIED before rewrite — "says exactly what happened" | LOUD producer finding -> ~B lane |
| **FAILED** (+ `failure_reason`) | producer caught its own failure (e.g. SecretUnset) | LOUD producer finding -> ~B lane; the reason string is the artifact |
| **PENDING** | report landed, awaiting adjudication | the normal loop: pull -> adjudicate -> land -> flip |
| ADJUDICATED / NO_SEMANTIC_CHANGES | done | nothing |

⛔ **ALSO READ THREE FIELDS THIS TABLE HAS NO STATE FOR. THE RUNNER WRITES THEM AND, UNTIL
2026-08-25, THIS SKILL DID NOT KNOW THEY EXISTED** (`OPAL_KIMIPIPELINE-S4`). They ride ALONGSIDE
`status`, not on it — a day can be `PENDING` **and** carry a superseded verdict, and the status
alone cannot tell you:

| Field | Meaning | Action |
|---|---|---|
| `readjudication_required: true` + `superseded_verdict{}` | a producer re-run OVERWROTE a prior CVO verdict; the block carries `{status, by, at, repo_commit, superseded_at}` | **NOT a fresh day.** Read the superseded verdict FIRST, then adjudicate the NEW report on its own merits. Record the supersession in the day record |
| `superseded_check: "FAILED …"` | the runner could not READ the prior manifest before overwriting it | **the carry-forward is BLIND for that day** — a verdict may have been lost with no block to show it. Treat the day's history as unknown, not as clean |

**AND THE ABSENCE OF ALL THREE PROVES NOTHING.** On a day with no prior verdict the runner's
carry-forward returns `{}` and writes none of them — **so they are absent whether the mechanism is
working or not.** The read is silent in both worlds; it is not a health check and must never be
quoted as one. *(Measured 2026-08-25: 0 of 23 days carried any of the three, positive-controlled
against `contract`=v2 — a correct and completely uninformative zero.)*

**WHY THIS MATTERS TO THE ORACLE:** the ledger is this pipeline's ONLY miss-detector by design, so a
day reset to `PENDING` after a real adjudication reads as un-adjudicated and the MSTR backstop
false-fires on work that was in fact done. Producer mechanism + its own limits:
`estate_report_runner.py` `_carry_forward_verdict()`. **DISARMED != REMEDIATED: the disarm stops NEW
clobbers; the already-clobbered 2026-08-06 entry is a separate repair.**

**Why manifest-first + epoch, stated so nobody reverts it:** the v1 contract wrote the manifest
LAST, so a dying run left the day ABSENT — and the default-alarming gate failed because the
alarming entry was written by the process that died (A GUARD MUST NOT SHARE A FAILURE MODE WITH
THE THING IT GUARDS — third measured instance of the shape, 2026-07-30, found by ~B exercising
A11). Manifest-first makes every STARTED run durably present in an honest state; `_EPOCH.json`
(CVO-written ONCE at the go-live flip; the pipeline never touches it) makes NEVER-STARTED days
computable. Adjudicate PENDING oldest-first.

## Step 2 — Pull

For each PENDING day: fetch `daily/YYYY/MM/DD/estate-report-YYYY-MM-DD.md` (the .json sibling
carries the machine form). Verify BOTH halves are present: the deterministic changed-resource
list (must exist — it compiles independently of Kimi) and the AI section (may carry the LOUD
"AI section absent" marker on a Kimi-side failure; an absent-marker absent-section is a
producer defect, route it).

## Step 3 — Adjudicate with Andrew

Render the report (deterministic list first, then the AI summary + its semantic-prose-evolution
suggestions, each citing its exact prose home: catalog entry / registry row / chain description).
Andrew rules per suggestion: adopt / amend / reject — or rules the day **NO SEMANTIC CHANGES**.
Semantic edits are NAMING ACTS: the AI proposes, Andrew ratifies, CVO lands. Never auto-apply.

## Step 4 — Land (three writes, all CVO-side)

1. **Repo commit** (ruling 2's "accruing in the repo"): the adjudicated file to
   `org/estate-reports/YYYY-MM-DD.md` — the day's decision record (what was adopted/rejected/
   no-changes + commit hashes of any prose edits landed). Commit via safe-commit under the CVO
   author line, together with any ratified prose edits themselves.
2. **S3 adjudicated copy**: `aws s3 cp` the same file to
   `s3://opal-estate-report/adjudicated/YYYY/MM/DD/estate-report-YYYY-MM-DD.md`.
3. **Manifest flip**: rewrite `manifest/YYYY-MM-DD.json` to
   `{"status":"ADJUDICATED"|"NO-SEMANTIC-CHANGES","by":"3.0.0_SA_CVO","at":"<ISO8601Z>","repo_commit":"<hash>"}`.
   The flip is LAST — a crash before it leaves the day honestly PENDING (fail-pending, never
   fail-adjudicated).

## Step 5 — Report

```
/estate-pull
  PENDING before: <N> (<dates>)   MISSED-DAY findings: <n>
  adjudicated: <dates + verdict each>
  landed: repo <hash> | s3 adjudicated/ | manifest flipped
  PENDING after: <should be 0 or named>
```

## Standing charter duty (the carrier that survives sessions)

`org/tier1_exec/3.0.0_SA_CVO/prompt.md` (LANE: BASE) carries the FIRST-ON-LOAD duty: run
`/estate-pull status` at every load once the pipeline is live; un-flipped past days are loud
before other work. MSTR-base's backstop (LD-0356 as amended) independently verifies the flips
and escalates gaps — watcher-of-the-watcher, one operator.

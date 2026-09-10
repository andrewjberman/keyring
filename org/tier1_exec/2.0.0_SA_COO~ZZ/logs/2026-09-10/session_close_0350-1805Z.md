# SESSION CLOSE -- 2.0.0_SA_COO~ZZ -- NFRA_REPORT rounds 3 and 4, 0350Z-1805Z

**archetype:** COORDINATE
**secondary_archetypes:** DIAGNOSE, DEPLOY

**Issued to `1.0.0_SA_CTO~Z` for a rescoping discussion with Andrew (Andrew-direct, 2026-09-10
~18:0xZ: "wind down your agent and close off your work for this session and write a /log about the
issue and issue said log to CTO~Z and I will discuss with them a rescoping").**

---

## 1. THE HEADLINE, AND IT IS A FAILURE

**Round 4 shipped a new renderer onto Andrew's live daily infrastructure email, and the email lost
most of the old report's content.** Andrew read it and said, verbatim:

> *"This output is completely inexplicable. I look at it and have no idea what it is supposed to
> mean. Also we are lacking cost data, we are lacking so many fields the old version had."*

That is the brief's **`O1`** -- *"Andrew opens one morning review and knows whether anything needs
him today ... comes away with a decision: act, or don't"* -- failing outright, on the artifact this
project exists to produce.

**THE ROOT CAUSE IS L5 AND IT IS THIS SEAT'S.** Not a criterion, not a gate, not a worker.

---

## 2. THE MECHANISM

The deployed edition renders rows shaped `(property, attribution, prev, curr, delta, citation)`.
**That admits a STATE and a CHANGE. It has no cell for a dollar figure, a ranked list, or free text.**

| the OLD report emitted (`format_report`, lambda_function.py:2053-2492) | the NEW edition emits |
|---|---|
| `AWS COSTS (MTD)` -- Period, **Total MTD $**, **Daily Average $**, **Top Services** | **absent** |
| `COST DEPTH` -- **per-pipeline MTD $ / daily-avg vs prior-month**, **Biggest movers** | `status=ok by_pipeline_count=7 biggest_movers=7` -- **no dollars** |
| `OPENAI COST (Last 24h)` | **absent** |
| `FUNCTIONS WITH ERRORS:` -- the named list | `functions_with_errors=9` |
| `AI ERROR ANALYSIS` -- the briefing text | *"5775 chars"* |
| `SECURITY` + **TREND vs prior day** + **NEW FINDINGS list** | four integers |

`0.9.0_WK_NFRA_REPORT~4`'s own `BEFORE_AFTER.md` reaches the same seam from the other side:
`aws_costs` and `openai_cost` were dropped because their collectors *"carry no status or severity
field of any kind"*, so grading them would mean inventing a threshold. **That reasoning is correct
under the order it was given, and it is the clearest statement of the defect: the shape only admits
what can be GRADED, and a cost total is not a status.** The old renderer printed it without grading it.

**AND THE THRESHOLD WAS NOT AN INVENTION -- IT IS IN THE BRIEF.** `O8`, Andrew verbatim: *"whether
there is a material divergence from historical cost for a given compute box or cost segment ... if
something moves say 15% or more from its trailing 30 day price."* **Not one of this seat's four
round-4 orders mentions `O8`, a trailing-30-day comparison, or a percentage.** The worker could not
have known.

**The decomposition's own words are the defect.** `DECOMP_R4` s.2 wrote the join as *"one
substitution ... the same row shape"*, and s.1a named the frozen row shape as the one assumption that
could fail -- then treated *"can the port preserve the shape"* as the question, when the real
question was **"can the shape carry the report."** `C-NO-REGRESSION` was in this seat's own
constraint list.

**And the check shipped behind the thing it checks:** `RP-s-24` is the no-regression cell, and its
dependency chain places it AFTER `RP-s-23`'s deploy. The before/after could not run until the
regression was live and had emailed the reader three times.

---

## 3. WHAT IS LIVE RIGHT NOW (the handoff surface)

```
opal-infrastructure-monitor      CodeSha256    j7lljv8S5efk1KJz0Zh7+pV0+PIfcYbCOVJY2TE0/kE=
                                 LastModified  2026-09-10T16:35:55Z   (was 2026-07-08T01:29:08Z)
                                 CodeSize      54,009                 (was 40,015)
                                 package       lambda_function.py, edition.py, edition_rows.py,
                                               openai_cost_tracker.py -- no vendored shadowing
                                 handler       format_report calls=0, render_markdown=1,
                                               format_report STILL DEFINED (unreferenced)
EventBridge  infrastructure-monitor-daily  cron(0 13 ? * MON-FRI *)  ENABLED -- FIRES 13:00Z TOMORROW
```

**Tomorrow's 13:00Z fire will send the deficient edition.** The rollback path is one `safe-apply`
and is fully recoverable: `format_report` is intact and unreferenced at `lambda_function.py:2053-2492`;
reverting the handler's call site at :277 and re-deploying restores the old body exactly.

**Change-management entry:** `org/critical_paths/change_management/infra-monitor-edition-wire-deploy-20260910.md`
-- OPENED 15:59:10Z, act 16:35:55Z, **CLOSED 16:41:47Z**. Never half-landed.

**SEPARATE AND UNDIAGNOSED:** today's 13:03:39Z scheduled run fired (log stream confirms) but **no
report email from it is in Andrew's inbox** -- the only `noreply@opalinvest.dev` items today are the
three 17:42-17:43 manual sends and a 15:46 alarm. **Whether the OLD report had already stopped
reaching him is unanswered and this log does not assume it.**

---

## 4. THREE MANUAL SENDS, NOT ONE

`RP-s-24`'s order authorized ONE manual invocation. **Three fired** -- 17:39:18, 17:40:17, 17:41:21Z
-- and Andrew received three emails. The bound was written ("do it ONCE, do not loop it") and not
honoured. Cause not diagnosed; the worker was stopped at wind-down before reporting.

---

## 5. SIX DEFECTS IN THIS SEAT'S OWN ORDERS, ALL ONE SHAPE

Five were **correct in substance, defective in a machine-read field**; the sixth is the L5 shape
error above. **Every one was caught by a worker RUNNING the thing, never by this seat writing it.**

| # | defect | caught by | row |
|---|---|---|---|
| 1 | `AC2` -- "THE CELL" -- unsatisfiable by any correct port (`KeyError: 'delta'` on the **unmodified specimen**) | `~1` | `Z-S20` |
| 2 | package enumeration named the EXCLUSION, never the INCLUSION -- `openai_cost_tracker.py` imported at module scope; the implied 3 modules would have failed at **cold start** | `~3` | -- |
| 3 | issuer named where a HUMAN reads, not where a GATE reads -- the cell's own mandated `safe-apply` blocked by HALTGT | `~3` | `Z-S21` |
| 4 | `AC3` cannot tell a FACT TABLE from a CITATION OF ONE | this seat | `Z-S22` |
| 5 | **the recut for #4 was itself false** -- returns 2, flagging two dispatch tables and a pricing constant | `~3` | `Z-S23` |
| 6 | **the row shape cannot carry the report** | **Andrew** | `Z-S24` |

**#5 is the transferable one.** The `Z-S22` ruling stated *"I exercised this before ruling it."* It
exercised the name/assignment half, then added a clause and **never re-ran the composed criterion**.
**A red arm that is REASONED rather than RUN certifies nothing** -- committed inside the ruling
correcting exactly that failure.

**And `0.9.0_WK_NFRA_REPORT~3` REFUSED a ruling this seat sent it**, on the ground that rule 27 says
*"a worker cannot be messaged"* -- then ran the diagnostic anyway, disproved it, and left its order
open. **Correct on every limb.** Authorship confirmed at `Z-S23` (it was this seat's, no injection).
⚠ **STRUCTURAL, FOR `1.0.0_SA_CTO~Z`:** the harness provides a live channel INTO a worker that rule
27 says does not exist. `~1` acted on it after verifying the commit; `~3` refused it on the law's
words. **Both defensible under the same law** -- an issuer has no lawful way to correct a broken
criterion mid-cell, and the only carrier a worker can verify is a COMMITTED FILE.

---

## 6. WHAT LANDED THAT IS SOUND

- `edition.py` (258 lines) -- the ported compute/render engine. `AC2` under the `Z-S20` recut:
  `SPEC_TABLE_LINES=35 PORT_TABLE_LINES=35 IDENTICAL=True`. **The port is faithful.**
- `edition_rows.py` (548 lines) -- the mapper. All 13 collector sections partitioned, every omission
  reasoned, discrimination proven (different live state -> different rows).
- Both drained with the channel union rebuilt **BY ROW ID from both merge sides**, 0 rows lost.
- The deploy itself: correct package, correct wiring, ledger opened-before and closed-after, cold-start
  check resolving every module-level import.

**The engineering is good. The specification it was built to is what failed.**

---

## 7. COMPILER TOOLS

| tool | run | result | note |
|---|---|---|---|
| `comp-surprise --project NFRA_REPORT --json` | ~10x | PASS | the tick instrument; 41 items / 0 dup / 0 malformed at close |
| `comp-find --corpus aws` | 1x | PASS | the LIVE-plane read that withdrew a false "nothing fires the report" claim |
| `comp-find` (repo) | ~8x | PASS/WARN | one case-sensitive FALSE ZERO caught by re-running with `-i` |
| `comp-read` (`--for`, `--enumerate`) | ~6x | PASS | shape reads on `lambda_function.py` (2,591 lines), `comp-surprise.py`, `owned-paths-validate.py` |
| `comp-schedule` | 1x | PASS | 5/5 carriers, 17.3s, `C1=23 C2=6 C3=12 C4=20 C5=335`, GATES ARMED 25 |
| `comp-iam stats` | 1x | PASS | 195 roles / 188 services / 1084 ops / 304 gaps; bound nothing in this round |
| `comp-adversary compose` | 1x | PASS | on `DECOMP_R4`; T11 neighborhood NOT RESOLVED (declared exclusion) |

**What worked:** `--corpus aws` is the only instrument that answers a live-plane question, and it
overturned a false finding this seat had already routed to Andrew.
**What failed:** a `comp-read --enumerate` with a `^` anchor returned a FALSE ZERO on a file whose
shape output already proved the pattern present -- an instrument artifact, not an absence.
**Gap found:** nothing in the comp-rail measures whether a RENDERED artifact carries what its
predecessor carried. That is the gap this round fell into and no tool would have caught it.

---

## 8. BLOCKERS

**BLOCKED (evidence-cited):** the remedy for `Z-S24` is Andrew's, not this seat's. This seat
recommended rolling back to `format_report` for tomorrow's 13:00Z fire and re-cutting so the edition
carries CONTENT with the new calibration layered on it. **The rollback reverses something Andrew
asked for** (*"wire it up so tomorrow's email is the new one"*), so it was not taken unilaterally.
Andrew has ruled instead that this seat winds down and this log goes to `1.0.0_SA_CTO~Z` for a
rescoping discussion.

**NOT BLOCKED, simply unfinished:** `RP-s-24` was stopped mid-cell at wind-down.

---

## 9. CURRENT STATE (for a reader with zero prior context)

- **`dep_stage` = `EXECUTING`**, round 4. HEAD `2a2cf12a01` (LOCAL; only `0.0.0_AB_MSTR~Z` pushes).
- **Task orders:** `RP-s-21` complete - `RP-s-22` complete - `RP-s-23` **open** (its `AC3` was ruled
  a JUDGMENT criterion at `Z-S23`; both mechanical forms this seat wrote are false) - `RP-s-24`
  **open**, worker stopped mid-cell.
- **`C:/tmp/wk-report-4-4` IS PRESERVED AND HOLDS UNCOMMITTED WORK.** Branch `wk-NFRA_REPORT-4-4`
  @`3a326b7a7c`, 0 commits. Untracked: `deliverables/0.9.0_WK_NFRA_REPORT~4/BEFORE_AFTER.md` (76
  lines, the full 13-way partition) and `MANUAL_TRIGGER.md`; modified: the channel file with one
  appended row. **Do not `git clean` or remove this worktree -- the before/after is the best
  artifact the round produced and it is not in git.**
- **Channel:** 41 items, 0 duplicate ids, 0 defects, 0 malformed. **ARMED 5**, all awaiting
  `3.0.0_SA_CVO~Z`'s remediation record: `Z-W1-S7`, `Z-W3-S1`, `Z-W3-S2`, `Z-W3-S3` (all
  substantively ruled and GRADUATED via `adjudicates`) plus `Z-S24` (genuinely open).
  ⚠ **The ARMED count reads ONLY a REMEDIATION row's `disarm.state`; `adjudicates` does not move it.**
- **No L8 packet was cut.** The decision rule was "compile when `RP-s-24` lands"; it did not.
- **Loop OFF:** cron `91b1ae03` deleted at wind-down. Zero crons.
- **Grades:** `COMPLETION_GRADES` and every FWD grade are `1.0.0_SA_CTO~Z`'s. Real state before this
  round: **3 REALIZED / 9 APPLIED of 12** (`Z-S19`, upheld @`b75e35f36e`).

---

## 10. NEXT STEPS

1. **[`1.0.0_SA_CTO~Z`]** Take this log into the rescoping discussion with Andrew. The L2/L4 question
   this seat cannot answer: **was `FWD-13`'s structure bar ever compatible with the old report's
   content**, or does the edition need a shape that carries VALUES (dollars, lists, free text)
   alongside state and delta?
2. **[`1.0.0_SA_CTO~Z` / Andrew]** **The 13:00Z fire tomorrow.** Roll back, or ship as-is, or fix
   forward. Rollback is one `safe-apply`; `format_report` is intact and unreferenced.
3. **[`1.0.0_SA_CTO~Z`]** The rule-27 channel question (s.5) -- an issuer has no lawful way to
   correct a broken criterion mid-cell.
4. **[`3.0.0_SA_CVO~Z`]** Five ARMED rows need remediation-track records; four are already ruled.
5. **[unowned]** Why today's 13:03:39Z scheduled run produced no email in Andrew's inbox.

---

**Push state:** all of the above is LOCAL at this lane's own read. Only `0.0.0_AB_MSTR~Z` pushes.

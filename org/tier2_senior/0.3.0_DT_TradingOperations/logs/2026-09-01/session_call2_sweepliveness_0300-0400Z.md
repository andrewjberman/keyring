# DT~Z SESSION LOG — CALL2_SWEEPLIVENESS.M1-SITEZ — 2026-09-01 03:00–04:0xZ

**Seat:** `0.3.0_DT_TradingOperations~Z` (lane Z, PID 19544). **archetype:** DIAGNOSE.
**secondary_archetypes:** MEASURE, REPORT. **Window:** 2026-09-01 ~03:00Z → ~04:0xZ.
**Project:** `CALL2_SWEEPLIVENESS` — one project, this one (Rule 27).

**MANDATE:** `CALL2_SWEEPLIVENESS.M1-SITEZ` @`0b555d6d2c`, issued by `2.0.0_SA_COO~Z`, P0 —
**is the 2026-08-25 cleanup that closed 99 projects a standing scheduled job, a script someone runs,
or a one-off act?** CALL 1 (reopening a named short list) was HELD at `0.0.0_AB_MSTR~Z` pending M1-1.

---

## 1. THE ANSWER, AND THE ONE THING THAT DECIDED IT

**ONE-OFF ACT.** Reported to `0.0.0_AB_MSTR~Z` + `2.0.0_SA_COO~Z` at 03:21Z (17768/17769) ahead of the
write-up because a held sovereign act was waiting on it. **Validated by `2.0.0_SA_COO~Z` (17779).**

The sweep is four commits by `1.0.0_SA_CTO~X` on 2026-08-25 (`d5e5790970` / `5823436d60` /
`2f0ad6d1c8` / `f7c9130f14`; 56 + 45 − 2 = 99). **Every file in all four is `.json` or `.md`.**

The deciding measurement was not "no schedule exists" — it was one level down: **no committed code in
this repo can write a project closure at all.** 1 of 82 code files across three differently-keyed
censuses writes anything under `org/projects`, and that one writes the derived `REGISTRY.md`, not a
project JSON. **A schedule with no possible target cannot fire**, which makes the two EventBridge
zeros corroborating rather than load-bearing.

## 2. THE CONTROL THAT EARNED ITS PLACE

My first project-JSON-writer detector returned a clean **`0 of 45`** and was **DEAD** — it required
the projects path and the write call on the same line; the planted mutant assigns on one line and
writes on the next. **The mutant caught it before the zero was reported anywhere.** Re-armed as a
multi-line taint check: ARM 1 fires, ARM 2 returns 1 of 82.

This is the whole reason M1-3 is written the way it is. **A positive control proves the ENGINE, not
your PATTERN** — so the pattern arm was stated separately: the register-domain regex *did* match 8
EventBridge rules, so its zero on the register domain is an empty domain, not a broken regex.

## 3. THE MEASUREMENT THAT MADE M1-4 DECISIVE

Complete census of every commit in **all history, all branches** touching ≥15 project JSONs:

```
 56  5823436d60  2026-08-25T18:35:46Z  TRANCHE A
 45  2f0ad6d1c8  2026-08-25T18:48:55Z  TRANCHE B
 19  44c6925b35  2026-05-22T13:39:05Z  the prior dormancy close-out, 95 days earlier
 17  409321a5cb  2026-08-25T19:29:26Z  back-pointer write, NOT a close
```

**Bulk project closure has happened exactly twice, ever, 95 days apart, both on explicit
contemporaneous human approval.** A standing job produces a cadence; this produces two points.

**The surface choice is the point:** git, whose retention is the full repository history. Every log
surface on this estate carries a retention *ratio*, and an absence inside a window shorter than the
question is not an absence. Git has no such window — **and because git is shared, this single
instrument answers the firing question for BOTH devices**, which is what let M1-5 resolve without
crossing the device boundary.

## 4. FOUR ERRORS I MADE, ALL CAUGHT IN-SESSION

1. **`--date=format:'...Z'` renders LOCAL time and stamps a literal `Z`.** My first UTC read labelled
   the sweep commits `14:31:52Z`; true UTC is `18:31:52Z`. **The wrong times reached msgs 17768/17769
   and were corrected in msgs 17927/17928/17929 -- sent AFTER the first commit, not before it. My
   first draft of this line asserted the correction had already been sent; it had not. A
   completed-act report for an act not yet performed, caught on re-read and left visible.** Substance unaffected — but the corrected times are what
   make the commit clock reconcile with Andrew's ~18:24Z / ~18:4xZ anchors, so the fix strengthened
   the finding. CLAUDE.md Rule 22a names this exact trap; I walked into it anyway.
2. **A `0` from an unresolved path is OUT-OF-CORPUS, not absence.** I ran `comp-find` inside native
   Python, which cannot resolve the `~/bin` bash forwarder → `DENOMINATOR: 0`. **Printing the
   denominator is what caught it**; a boolean would have shipped as a finding.
3. **Native Python cannot read MSYS `/tmp`** — same class, one layer over.
4. **`comm` reported two sorted lists as totally disjoint** because Python's `print` emitted CRLF.
   The tell was both directions being non-empty *and equal in size* — a real diff is asymmetric.

Also: the comp-rail correctly refused a raw `find` and routed it to `comp-find --name`. And the
proof-of-spec checker refuted my first artifact pins (I declared HEAD for files that do not exist at
HEAD) — corrected to the `PENDING-THIS-COMMIT` sentinel.

## 5. WHAT I DID NOT DO

- **Did not re-run the 2026-08-25 predicate** (Andrew-direct standing prohibition).
- **Did not close, reopen, or edit any project status.** Read the register; never wrote it.
- **Proposed no alarm, monitor, notifier, SNS or freshness-checker** for the operator residual. The
  TO named this seat as specifically tempted; the residual landed as a line in the report.
- **Read-only on AWS throughout** — no apply, no schedule created, disabled, enabled or deleted.
- **Zero crons.** `/watcher` armed once at load (task `bx8qukyo3`, banner `parent-tied: pid 557498`).

## 6. THE RESIDUAL AND THE HANDED-BACK HALF

**The ACT is one-off; the PREDICATE is durable prose.** No mechanism re-closes a reopened row; an
*operator* told to "re-run the spring clean" would. `1.0.0_SA_CTO~X` reached this contemporaneously
(`826f6608c9`: "ANYONE RE-RUNNING THAT PREDICATE WOULD CLOSE THEM") and protected the three held
projects with a note in the existing `phase` field, minting no new field. **Relayed as precedent, not
proposed as a control** — CALL 1's shape is `0.0.0_AB_MSTR~Z`'s.

**Handed back to the laptop (M1-5), neither blocking CALL 1:** the laptop's Windows Scheduled Tasks
plane (device denominator is **1 of 2 devices**, stated not hidden) and whether an uncommitted mutator
persists in its working tree. Both bound *where an operator's tooling might sit*; neither can bound
the firing history, which §3 answers for both devices.

## 7. COMPILER TOOLS

- **`comp-find`** — primary census, three differently-keyed runs unioned to 82 files (`--files`,
  `--all`, `--band`, `--name`). Located the origin artifact and the CTO~X log. Denominators printed
  every run; nothing `head`ed.
- **`comp-find --corpus aws`** — both EventBridge planes as distinct node types. **It disclosed its
  own 75.7h staleness**, which is the only reason the live re-read happened; that read found a real
  +1 drift (`bd-49f-insurance-session-daily`).
- **`.tools/aws` shim** (read-only) — `events list-rules`, `scheduler list-schedules`,
  `scheduler get-schedule`; auto-paginated, counted client-side, `NextToken` checked not assumed.
- **`Get-ScheduledTask`** — device plane, read by ACTION and TRIGGER rather than by name.
- **`git log --name-only` single-pass + awk** — the all-history census, after a per-commit `git show`
  loop timed out at 2m. The single pass is also sounder: it cannot silently truncate.
- **`.tools/to-check.py --all --assignee`** — startup holdings, run on both suffixed and base serial
  as a control on the known `SEATED:`-prose defect. total=1, scanned=2230.
- **`.tools/proof-of-spec-check.py`** — instance validation, run **with** the TO's declared
  `M1-1..M1-5` so coverage was checked rather than left unchecked. VALID (rc=0), 0 violations.

## 8. STATE AT CLOSE

- **M1-1 … M1-5 all answered; none deferred.** Deliverable +
  `CALL2_SWEEPLIVENESS.M1_PROOF_OF_SPEC.json` (VALID, coverage-checked) committed this session.
- **Surprises:** none warranting the channel. Startup A.2 emitted the documented site-Z device-axis
  class (18 findings = 5 COVERAGE + 8 NON-APPEND-EDIT + 5 ERROR-FAILCLOSED; **8 of 8 shrank, 0 grew,
  0 unchanged** — the benign direction). Known, owned under `rv0057-f001`; not re-filed per XXX.md.
- **Blockers:** none at this seat.

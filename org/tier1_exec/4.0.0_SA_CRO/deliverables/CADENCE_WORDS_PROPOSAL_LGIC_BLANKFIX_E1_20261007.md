# PROPOSAL -- cadence words for the schedules the naming check cannot name (LGIC_BLANKFIX round 2, E1)

**Author:** `4.0.0_SA_CRO` (Chief Research Officer), 2026-10-07 ~13:3xZ.
**Asked by:** `2.0.0_SA_COO~G` msg 106251, at `1.0.0_SA_CTO`'s instruction (msg 106248;
`org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round1.md`, item E1).
**Status:** a PROPOSAL for `1.0.0_SA_CTO` to ratify. Nothing in `org/standards/NAMING_SCHEMA.json` is changed by this file.

## 1. The answer

Three rules close the eight lines. They add **no new enumerated word**. Two widen what an existing word or form covers; one
uses a form the grammar already has.

| # | Rule | Closes, of the 8 | Closes, of the 47 undecided estate-wide |
|---|---|---|---|
| P1 | `daily` means: fires at most once per calendar day, on five or more days of the week. A weekday restriction is a calendar, not a cadence. | 6 (five Monday-to-Friday, one Monday-to-Saturday) | 17 |
| P2 | The interval form is a rule, not a list: `{N}min` for a fixed interval of N minutes, N from 1 to 59; `{N}h` for a fixed interval of N hours, N from 2 to 23. `5min` and `1min` become instances of it. `hourly` and `daily` keep 60 minutes and 24 hours. | 1 (`15min`) | 6 |
| P3 | A rule with an event pattern and no schedule expression takes the existing event form `on-{event}`. The event token is decided per rule, by reading what the rule waits for (section 4). | 1 | 13 take the form; 1 token is proposed here, 12 are owed |

After P1 to P3, **11 of the 142** schedules the reader sees stay undecided, and are listed in section 5. None is in
`bd-pipeline`.

## 2. The eight lines, filled

Source: `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round1_bd-pipeline.txt` @40a21e850b.

| Current name | Expression | Rule | Proposed complete name |
|---|---|---|---|
| `bd-49f-keepalive-sched` | `rate(15 minutes)` | P2 | `blackdiamond-49f-keepalive-sched-15min` |
| `bd-49f-session-complete` | event pattern, no schedule | P3 | `blackdiamond-49f-runner-on-session-complete` |
| `bd-allocation-pipeline-trigger` | `cron(0 22 ? * MON-FRI *)` | P1 | `blackdiamond-49f-allocation-pipeline-trigger-daily` |
| `bd-unrealized-pipeline-trigger` | `cron(38 21 ? * MON-FRI *)` | P1 | `blackdiamond-49f-unrealized-pipeline-trigger-daily` |
| `bd-realized-pipeline-trigger` | `cron(45 21 ? * MON-FRI *)` | P1 | `blackdiamond-49f-realized-pipeline-trigger-daily` |
| `bd-asset-dim-pipeline-trigger` | `cron(10 22 ? * MON-FRI *)` | P1 | `blackdiamond-49f-asset-dim-pipeline-trigger-daily` |
| `bd-transaction-pipeline-trigger` | `cron(53 21 ? * MON-FRI *)` | P1 | `blackdiamond-49f-transaction-pipeline-trigger-daily` |
| `bd-gold-nightly-fallback` | `cron(0 23 ? * MON-SAT *)` | P1 | `advi-49f-gold-nightly-fallback-daily` |

The system, scope and function parts of each name are the trace's own; only the last slot is filled here.

## 3. Past patterns (what the estate already does)

Measured 2026-10-07 from two reads. (a) `python lib/opal_naming_cadence.py estate`: 142 Terraform-declared schedules, 95
decided, 47 undecided. (b) A word-boundary token count over the 1,927 distinct (name, type) pairs of the whole-estate
naming check run at HEAD today (163 of them schedule-typed).

**P1, weekday-restricted schedules.** 17 rows: Monday-to-Friday 14, Tuesday-to-Saturday 2, Monday-to-Saturday 1.
- 9 of the 17 names already carry `daily`: `bd-49f-fees-session-daily`, `bd-49f-fees-runner-daily`,
  `bd-allocation-file-check-daily`, `mdpf-secclass-sector-writer-daily`, `amgt-global-freshness-snapshot-daily`,
  `volatility-daily-update`, `irpt-directory-refresh-retry-daily`, `wsb-49f-model-aua-pull-daily`,
  `wsd-49f-partner-held-etf-pull-daily`.
- 0 of the 1,927 names carry `weekday`, `weekdays`, `tradingday` or `businessday`.
- The estate's own law reads a trading-day job as daily: CLAUDE.md, "Everything is `T-1` unless declared; Friday IS
  Monday's answer", with the calendar held in one place (`lib/trading_calendar.py`), not in a name.
- The round-1 analysis notes that two Monday-to-Friday rules already print a finished name ending `-daily`. Under P1 that
  output is correct, and the two readers agree instead of one being wrong. They must still be one reader.

**P2, fixed intervals.** `5min` and `1min` are already values. Names already built the same way: `15min` (1 name),
`6h` (2 names: `opal-ms-ingest-liveness-6h`, `opal-otp-liveness-6h`). Every token of the shape digits plus `min` or `h`
found in the 1,927 names sits in a schedule-typed name (6 of 6), so the form collides with nothing.

**P3, event rules.** 9 names already carry an `on-` run, for example `rivalfunds-build-silver-on-marker-created` and
`opal-49f-served-guard-on-write`. 13 Terraform rules have an event pattern and no schedule; 1 of them already carries
its run (`inf-gold-full-on-bronze-complete`). 7 schedule-typed names end in `complete` with no `on-`.

**Refused as cadence words, by pattern:** `nightly` (7 names), `morning`, `0900et`, `0830et`. Each names a time of day, not
a period. They stay free words inside the function part, as `GRADING_RULE.md` already allows for a cadence word there.

## 4. P3 in detail: the event token

The grammar's last slot for an event rule is `on-{event}`; the part before it is the function, what the rule starts.
A name such as `bd-49f-session-complete` gives the event and no function, so the reader cannot fill it from the name.

Proposed for the one `bd-pipeline` row: `infra/aws/terraform/bd-pipeline/bd-49f-session-chain.tf:243-263` waits for the
session-fetch command to succeed and starts the runner (target input `mode = "runner-run"`). Function `runner`, event
`session-complete`: `blackdiamond-49f-runner-on-session-complete`.

Proposed reader behaviour for the other 12: print the form `{function}-on-{event}` with the reason "event rule: the
function and the event are read from the rule's target and pattern, per rule", and list the row. This is one decision per
rule, 12 in all, none in round 2's root. I will propose each when its root is cut.

One grammar question for `1.0.0_SA_CTO`, not decided here: whether an event rule may have an EMPTY function, giving
`blackdiamond-49f-on-session-complete`. I recommend no: two rules waiting for the same event would then share a name.

## 5. What stays undecided (11 rows, none proposed now)

| Rows | Shape | Names | Note |
|---|---|---|---|
| 7 | several listed hours a day | `finbert-scoring-post-ingestion`, `finbert-scoring-post-ingestion-45min`, `keyword-intelligence-generator-daily`, `trending-topics-portal-publisher-daily`, `news-trending-analysis-daily`, `keyword-drilldown-generator-daily`, `fear-greed-daily-update` | 5 of 7 say `daily` today. A word such as `intraday` has 0 uses. Not needed by the thread; a later proposal. |
| 1 | first Friday of the month (`6#1`) | `fred-ingestion-monthly-early` | plausibly `monthly`; the reader's month rule would need widening. |
| 1 | `rate(72 hours)` | `ycharts-session-capture-schedule` | outside P2's range on purpose; one row does not earn a `{N}d` form. |
| 2 | the expression is not a literal | `consolidation-gold-runner-scheduled-start`, `daily-sprint-generator-schedule` | the reader cannot see a variable; an instrument limit, not a vocabulary gap. |

## 6. The rule 24 record (CLAUDE.md, four postulates) for the cadence value set after P1 to P3

**Value set:** `daily`, `weekly`, `monthly`, `hourly`, `{N}min` (N 1-59), `{N}h` (N 2-23), and the event form `on-{event}`.

**(i) MECE over a declared domain.**
- Declared domain: the 142 EVENT_RULE and SCHEDULE names that `lib/opal_naming_cadence.py` reads from Terraform text.
- Subtraction, printed: 142 - 95 decided today - 17 (P1) - 6 (P2) - 13 (P3, the form) = **11 uncovered**, each named in
  section 5. Check on the 47: 17 + 13 + 7 + 3 + 2 + 2 + 2 + 1 = 47.
- The domain is NARROWER than "every schedule". The whole-estate check sees 163 schedule-typed names across the live and
  repository planes; the reader sees only Terraform text. A live-only schedule (for example the three
  `ldo001-...-expire` schedules) is outside this record. The proposal makes no claim about those.
- Exclusive: an expression matches at most one value. Once a day on five or more days is `daily`; one day a week is
  `weekly`; a fixed interval under a day is `{N}min`, `hourly` or `{N}h`. Once a day on two to four days a week matches
  nothing and stays undecided by design: 0 such rows exist in the 142.

**(ii) Same grain.** Every value names how often a rule fires. A time of day (`nightly`), a clock time (`0900et`) and a
calendar (`weekdays`) are other grains and are not admitted. That is the reason P1 widens `daily` and does not add
`weekdays`.

**(iii) Intent coherence.** One axis, one intent: the firing period a reader should expect. Which days are trading days
is a second axis; it lives in the expression and in `lib/trading_calendar.py`.

**(iv) State coherence -- what one remedy does NOT move.**
- The 95 rows already decided: unchanged.
- The 11 rows of section 5: unchanged.
- No resource is renamed. The proposal changes what the check PRINTS as the complete name; the rename is each
  clean-up project's.
- 12 event rules get the form and still lack their token.
- A schedule whose live expression differs from its Terraform text is not seen (the reader's own declared exclusion).

**Word-boundary token census** (denominator: 1,927 distinct (name, type) pairs; tokens split on every non-alphanumeric
character, lower-cased):

| token | all names | schedule-typed | note |
|---|---|---|---|
| `daily` | 170 | 85 | 85 uses are a free word inside a function, already allowed |
| `weekly` | 4 | 3 | |
| `monthly` | 6 | 5 | |
| `hourly` | 3 | 3 | |
| `5min`, `1min`, `15min`, `45min` | 1 each | 1 each | `45min` names a rule that fires three times a day (section 5) |
| `6h` | 2 | 2 | |
| `on` | 9 | 9 | every use is an `on-` run |
| `nightly` | 7 | 7 | refused as a cadence, section 3 |
| `weekday`, `weekdays`, `tradingday`, `businessday`, `intraday`, `72h`, `3d`, `quarterly`, `yearly` | 0 | 0 | |

## 7. The alternative not recommended

A new word `weekdays` for P1. It would be precise about the calendar. Against it: 0 existing uses; 9 names that say
`daily` today would become wrong; Tuesday-to-Saturday and Monday-to-Saturday would each need another word or a
misfit; and it puts a second grain into the value set (postulate ii).

## 8. If ratified, what changes and who writes it

- `org/standards/NAMING_SCHEMA.json` block `cadence`: the definition of `daily`, and the interval rule beside `values`.
  `4.0.0_SA_CRO` wrote the last edit of that file (v1.14) and can write this one on the CTO's word.
- `infra/logic` generated naming section and `GRADING_RULE.md` V6: restated to match (round 2 cell E5 already touches
  both).
- `lib/opal_naming_cadence.py` and the fix path in `lib/opal_naming.py`: the round-2 cadence cell. Outside this lane.

## 9. Not measured

- Whether the Terraform expression of each of the eight equals its live expression.
- The 21 schedule-typed names the whole-estate check sees and the Terraform reader does not (163 against 142).
- The targets of the 12 other event rules.

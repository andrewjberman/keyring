# 0.7.0_AE_CloudOps~MI -- NFRA_MCPINDEX.TO-MX-a-1 -- BD morning vs evening run shape

**archetype:** TRACE

Session 2026-10-06 19:55-21:10Z. Site Z. Read-only throughout; no call to Black Diamond, no publish,
apply, invoke, rule change, instance start/stop or SSM send-command.

## Current State

PHASE A is COMPLETE and both records are written and committed.

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MI/BD_RUN_SHAPE_COMPARISON.json`
  -- the machine-readable record. `a1.AC1.sh` reads `morning tables: 4 (allocations, realized,
  transactions, unrealized) / evening fetches_from_bd=False; verdict evening_extraneous=True /
  RESULT: PASS / exit=0`. Run three times across three states of the record; PASS each time, exit
  code read from `$?` and never through a `tail` pipe.
- `.../BD_RUN_SHAPE_COMPARISON.md` -- one page for Andrew, structured on his three questions.
- `.../NFRA_MCPINDEX.TO-MX-a-1.bd-run-shape-morning-vs-evening.proof_of_spec.json` --
  `proof-of-spec-check.py` reads `violations=0`, `VALID (rc=0)`, surprises limb `5 entries; 5 open
  with a row id; 5 resolve to a channel row`.
- Rows `NFRA_MCPINDEX-Z-S77..Z-S81` appended to the project channel in the SHARED tree (CLAUDE.md 14b
  inverts for an append-only channel).

**The three answers.** Transport: REST, four DataMining endpoints on `https://bd3.bdreporting.com`, a
Secrets-Manager cookie jar minting a bearer per run, no browser anywhere. Fields: 4 tables, 71 / 13 /
15 / 92 columns, read from the landed workbooks' own header rows. BD-side as-of provenance: **PRESENT**
-- every workbook carries a BD-written `Timestamps` worksheet (`Created (Eastern)`, `Template Name`,
`Start Date`, `End Date`, `Date Range`), plus an `As of Date` data column in transactions and
allocations. `End Date` keys the silver partition on both merge paths; `Created (Eastern)` is read by
neither and never reaches silver; HTTP response headers are discarded entirely (0 hits for
`resp.headers`/`getheader`/`info()` in the engine's one request function).

**Verdict: `evening_extraneous: true`** -- extraneous as a SOURCE and as a SCHEMA, not yet redundant as
a SCHEDULER. The evening documents fetch nothing from BD on their SERVED Default version 3; they
re-merge the morning run's own bronze; nothing is in their output that the morning's lacks, and the
transactions leg is one column NARROWER (`cusip` absent, 73 vs 74). Their one live function is the
same-day merge on dates the morning sentinel is withheld -- 11 of 34 dates 09-03..10-06. Seven
preconditions are in the record; P1/P2 are MX-s-18 landing and its IAM blocker `Z-W24-S11`.

Three corrections to the issuer's picture, all measured: the two merge scripts are **different code**
(43,492 B @2026-06-29 evening vs 59,820 B @2026-10-01 morning, 695 differing lines); there are **three**
EC2 instances, not one, and the realized document runs on the box named `bd-allocations`; and the
morning run's two SNAPSHOT tables have landed **weekly** since as-of 2026-07-10, cause measured from
the runner's own `REJECTED ... empty snapshot export` lines.

## Blockers

**None owed by this seat.** PHASE B (the decommission) is a later order's act under never-widen halves,
explicitly out of this cell.

Two items are owed by `2.0.0_SA_COO~MI`:
1. **The order's prescribed surprise-row id form is unmeetable.** `NFRA_MCPINDEX-Z-AEMI-S<k>` is
   refused by BOTH gates -- `surprise-row-gate.py:105` and `proof-of-spec-check.py:1198` admit only an
   optional `W<n>-` or `C-` segment. Of the channel's 243 rows, the 5 AEMI-form ids were the only 5
   `ID_RE` refused; 238 use an accepted form. Had they stood, the 5 ENFORCE violations on the
   SURPRISES limb would have blocked this tree TO's `complete` flip -- verified by running the
   checker, which read exactly those 5 and nothing else. Rows renumbered to `Z-S77..Z-S81`; the lane
   identity the `AEMI` segment carried is preserved in each row's `surfaced_by`. Reported under
   BOUNDS clause 3; the order template is the issuer's to correct.
2. **Disposition of rows `Z-S77..Z-S81`**, and the `MX-a-1` cell-id collision (`Z-S81`).

## Next Steps

1. **[`2.0.0_SA_COO~MI`]** Read the verdict and rule on PHASE B. Precondition order matters: MX-s-18
   must land, then one real Monday AND one real Tuesday must fill in on their own, before either
   evening rule is disabled. Disabling a rule is reversible; deleting a document is not.
2. **[`2.0.0_SA_COO~MI`]** Disarm or route `Z-W24-S11` -- the `s3:GetObject` grant on
   `bronze/*/_BRONZE_COMPLETE.json` that MX-s-18's read-back needs. Nothing in PHASE B can start
   before it.
3. **[`2.0.0_SA_COO~MI`]** Rule on MX-s-17: the documents already read the morning bronze on their
   served version, so there is nothing left to repoint.
4. **[owner unassigned]** The weekly allocations/unrealized cadence (`Z-S78`). Not caused by the
   evening run and not fixed by retiring it. Two candidate remedies, neither this cell's call: a 2-
   business-day as-of lag, or a later run time.
5. **[`1.0.0_SA_CTO` / whoever owns the gate pair]** The two surprise-id regexes and the order
   template disagree; one of them should move.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-which` | `comp-which "how do I grep the repo"` (startup A.3) | `PATH: 104 of 104 comp-tools resolve bare`; `EXERCISE: a forwarder RAN`. Rail live this session. |
| `comp-to` | `comp-to NFRA_MCPINDEX.TO-MX-a-1.bd-run-shape-morning-vs-evening` | OK, session TO_ID set race-free per seat+session. |
| `comp-schedule` | n/a | DECLARED-NOT-APPLICABLE in the order preflight, and correct: nothing published, applied or invoked, so no gate or hold is in this act's path. Recorded as declared-not-applicable, never as skipped. |
| `comp-iam` | n/a | DECLARED-NOT-APPLICABLE, correct: no role or policy change. The one IAM fact the verdict rests on is cited from `ANNOUNCE_MX-s-18` (row `Z-W24-S11`), not re-derived. |
| `comp-adversary` | n/a | DECLARED-NOT-APPLICABLE: an investigation record whose answers are graded at L9 as AC2. The instance's `controls` block carries the self-falsification this cell could do alone. |
| `comp-pipescript` | NOT RUN | The AE role minimum (`deployed`, `postdeps`) is gated on a gold-run trigger. This cell fires nothing, so the minimum has no object. Named as not-applicable rather than skipped. |
| `proof-of-spec-check.py` | `python .tools/proof-of-spec-check.py <instance>` | Refused the first draft on **12** violations, every one real: 3 enum values (`phase`, `method`, `status`), 1 missing `result`, 3 `PENDING-COMMIT` instead of `PENDING-THIS-COMMIT`, and 5 surprise-id-form. The last 5 are the gate conflict in Blockers. Final run: `violations=0`, `VALID (rc=0)`. |
| `surprise-row-gate.py` | run at commit via the hook | Graded the 5 new rows; the pre-commit run is the authority, and it is what made the id-form conflict measurable rather than theoretical. |
| `a1.AC1.sh` | `bash .../round7/checks/a1.AC1.sh; echo "exit=$?"` | PASS, `exit=0`, three times across three record states. 24 graded assertions, 0 failures. |

### Instrument traps worth carrying forward

- **A descending key sort put the live feed below the page.** `reverse(sort_by(Contents,&Key))[:4]` on
  `forwardfill_v2/transactions/` and `/allocations/` returned `TXN_DAILY_2026-06-18` and
  `ALLOC_DAILY_2026-06-18` as newest, and I read that as two dead feeds. `TXN` sorts above
  `TRANSACTIONS` and `ALLOC_` above `ALLOCATIONS` (`_` is 0x5F, `A` is 0x41), so the current names sat
  below a 4-row page. The full census corrected it: 202 transactions xlsx in two name patterns (105
  current, 97 retired), 132 allocations xlsx in three. A page is not an answer, and the denominator
  with the pattern distribution is what caught it.
- **The deployed engine is not the repo file.** `bd-49f-runner` downloads
  `s3://opal-data-bd/code/bronze/cot_bronze_ingest.py` at RUNTIME, so the repo copy under `data/cot/`
  is not the bytes that execute. Reading the S3 object satisfied CLAUDE.md 22a CODE and the order's
  `data/cot/` bound at the same time.
- **The SERVED SSM version, not the repo JSON.** `describe-document` first (Default 3 == Latest 3),
  then `get-document --document-version 3`. This is the step that turned "the repo says the portal
  download was removed" into "the running document fetches nothing from BD".
- **Site Z: MSYS mangled a leading-slash log group name.** `aws logs filter-log-events
  --log-group-name /aws/lambda/bd-49f-runner` failed `InvalidParameterException` from Git Bash;
  CLAUDE.md forbids bare `MSYS_NO_PATHCONV=1` with `aws`, so the call moved to PowerShell, which does
  no such conversion. Also measured: `--filter-pattern '"RESULT:"'` is refused -- `Invalid
  character(s) in term ':'` -- the pattern must be `RESULT` with no colon.
- **A `\b` in a Python non-raw string became a literal backspace (0x08) inside a JSON value**, and an
  `ord(ch) > 127` ASCII check does not see it -- 0x08 is ASCII. The check that caught it was reading
  the stored value back with `repr()`. A control-character check needs `ord(c) < 32` as well as
  `> 126`.
- **The channel already carried 6 non-ASCII characters** (U+00E2 x2, U+20AC x2, U+201D x2) at offsets
  450372-450403. They are the QUOTED SUBJECT of a pre-existing row about a mojibake incident, so they
  are the record and must not be stripped -- CLAUDE.md's "never a subset" rule points the same way.
  Reads and writes were explicit `encoding='utf-8'`; count before 6, after 6.

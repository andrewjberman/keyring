# TO NFRA_TRNSPT.TO-TR-t4 -- thread hop 5: the reader route, who said what from a seat shell

<to_id>NFRA_TRNSPT.TO-TR-t4</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~2</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>transcripts</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `TR-t-4` (`decompositions/NFRA_TRNSPT_DECOMP.md`) |
**outcome_ref:** FWD-1, FWD-5 | **depends_on:** TR-t-3 (drained; the silver parquet of `MM-20260928-0858` is in the bucket)

---

## WORKER FACE

### THE CELL

`TR-t-4`, thread hop 5 (PRD section 2): "Silver -> the reader: Andrew opens the meeting through the reader route he uses (the
route is a C-READERS decision: the gateway tool or a dedicated AWS role) and reads who said what." Round-1 form of the route
(decomposition ruling): a CLI from an ordinary seat shell under Andrew's own AWS identity, the one key grantee. The second
reader's route is round 2 (FWD-8). FWD-4's answer shape starts here: an absent meeting gets a CAUSE, never a shrug.

**Build:**
1. `data/transcripts/scripts/teams/read_meeting.py`: `python data/transcripts/scripts/teams/read_meeting.py --series <s> --date YYYY-MM-DD
   [--speaker "<name>"] [--grep "<word>"]`. Lists the silver partition `address("teams","transcripts","silver",<s>,"date=<date>","")`
   (strip the trailing object; list by prefix), reads each parquet with pyarrow, prints a first line
   `MEETING <series> <date> turns=<n> speakers=<k> transcripts=<m>` and then one line per turn `HH:MM:SSZ  <speaker>: <text>`
   in `turn_index` order, filtered by `--speaker` / `--grep` (case-insensitive) when given. When the partition holds no parquet:
   look at bronze for the same series and date; print `NOT-HELD <series> <date> cause=not_parsed` when bronze has it and
   `NOT-HELD <series> <date> cause=not_in_bronze` when neither tier has it, and exit 4. No other output shape.
2. Tests `data/transcripts/scripts/tests/test_teams_read_meeting.py` on the fake-S3 pattern with a SYNTHETIC parquet (invented
   speakers, 6 turns): the header line, order, `--speaker` and `--grep` filters, and both NOT-HELD causes. Never real text.

### ACCEPTANCE

<criterion id="TR1-t4-AC1" cell_refs="TR-t-4"><invocation>python -m pytest data/transcripts/scripts/tests/test_teams_read_meeting.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`TR1-t4-AC1` -- the reader over a synthetic parquet: header, order, filters, the two causes.

<criterion id="TR1-t4-AC2" cell_refs="TR-t-4"><invocation>python data/transcripts/scripts/teams/read_meeting.py --series monday_meeting --date 2026-09-28 --grep "the"</invocation><expect>MEETING monday_meeting 2026-09-28</expect></criterion>
`TR1-t4-AC2` -- the REAL read of the held Monday meeting from a seat shell (record the header line and the turn COUNT in your
proof; never paste turn text into any deliverable).

<criterion id="TR1-t4-AC3" cell_refs="TR-t-4" judgment="true"/>
`TR1-t4-AC3` -- JUDGMENT (FWD-5 ACCEPT): an analyst who wants what was said about one company gets it from the reader without
opening a file. Record the invocation you would hand an analyst (`--grep <a company named in the meeting>`) and its header line;
NO verdict -- the CVO grades it at L9 on the real run.

<expected_criteria>TR1-t4-AC1,TR1-t4-AC2,TR1-t4-AC3</expected_criteria>

Dry-run at the base 2026-09-30 14:0xZ: AC1 "no tests ran", AC2 "No such file" -- FAIL as expected; AC3 judgment, no base run.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **Read-only against the bucket.** This order writes no object.
- **The thread trace (TR-t-5) is the next order in your queue** and drives this CLI as a subprocess: keep the output shapes exact.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `NFRA_TRNSPT-W2-S<k>`), and do not weaken the test to pass.

<paths>
data/transcripts/scripts/teams/read_meeting.py
data/transcripts/scripts/tests/test_teams_read_meeting.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP.md</decomp_doc> (round 1), cell `TR-t-4`.
<owned_cells>TR-t-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR1-t4-AC1, TR1-t4-AC2, TR1-t4-AC3. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/NFRA_TRNSPT.TO-TR-t4.reader-route.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR1-t4-AC1,TR1-t4-AC2,TR1-t4-AC3` BEFORE the flip. AC3 is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming 3.0.0_SA_CVO; PASS or FAIL on it is INVALID.
</proof_of_spec>

**REPORT:** the header line of the real read, the turn count, the analyst invocation, the pytest line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round.
comp-iam: RUN -- the read runs under Andrew's IAM user; the second reader (C-READERS route A or B) is round 2.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 section 2 hop 5 (S06 reader half, S21 round-1 form); decomposition round 1 cell TR-t-4.

# TO ADVI_COTBKF.TO-CB-cv-1.completion-report-fwd-1-to-9 -- round 100 CB-cv-1: the completion report, one row per outcome FWD-1 to FWD-9, each with its grading artifact, the grade read from it, and the act that would realize any NOT_REALIZED one; read-only, counts only

<to_id>ADVI_COTBKF.TO-CB-cv-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~189</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>100</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-cv-1` (`decompositions/ADVI_COTBKF_DECOMP.round100.md`) |
**outcome_ref:** FWD-1..FWD-9 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** ADVI_COTBKF is Cottonwood's Commonwealth backfill. Its PRD (`org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`, section 1, lines 27-96) states nine outcomes. The project closes only when every one grades REALIZED, and the CTO grades each at his next analysis from a completion report. You write that report: for each of FWD-1 to FWD-9, which committed artifact or versioned S3 object records that the outcome was exercised, what that artifact says its grade is, and for any outcome that is not REALIZED, the act that would realize it and who owns it. **You read; you do not grade by your own judgment, run an exercise yourself, write to S3, serve anything or change any code.** You report what the artifacts say. An outcome with no artifact that records its exercise is NOT_REALIZED, and the act is to exercise it.

**The nine outcomes and their DONE WHEN (all EXERCISED; PRD v0.11):**
- FWD-1 an analyst reads one Cottonwood account's whole transaction history from Opal's store and traces a row to the delivered file. DONE WHEN: one real account's history read end to end and one row traced back.
- FWD-2 the whole Commonwealth delivery is in Opal's store as it arrived. DONE WHEN: each delivered file found and its size and fingerprint matched (five files, byte for byte, with size and fingerprint beside them).
- FWD-3 each account's returns day by day, after fees, back to 2013, checked against Commonwealth's monthly figures. DONE WHEN: one account's daily returns read across the whole span and checked against the monthly figures.
- FWD-4 Cottonwood's client relationship records as Commonwealth held them. DONE WHEN: one household read with its people, relationships and activity.
- FWD-5 any client document found by account, type and date, and opened. DONE WHEN: one statement and one tax form found by account and date and opened.
- FWD-6 what the backfill covers and what it does not. DONE WHEN: the coverage read by someone who was not told it.
- FWD-7 the most sensitive personal details held only where Andrew decided, and a reader can say who can see them. DONE WHEN: the places listed and an unauthorised read refused.
- FWD-8 an old Commonwealth account lined up with the same client's account today, or shown as not yet matched. DONE WHEN: the match list read for every account in the delivery.
- FWD-9 a client's history follows them across a Commonwealth account change. DONE WHEN: one client read across an account change, oldest account to newest.

**Where the grades and the exercises are recorded (READ-ONLY; use the native Grep and Glob tools, not `find`; names and counts only, never an account number, name, tax number, cusip or dollar value):**
1. The CVO's adjudications: `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/adjudications/ADJUDICATION_v1.md` to `ADJUDICATION_v66.md` (and their rows). Grep them for `FWD-1` to `FWD-9`, `REALIZED`, `MET`, `EXERCISED`.
2. The CTO's round analyses: `org/missions/D8/ADVI/ADVI_COTBKF/ledger/ROUND_ANALYSIS.*.md` (round 88, rounds 96-98, round 99 and earlier ones that exist), which state where each outcome stood.
3. The worker deliverables under `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~*/` and the CloudOps seats' folders beside them (records, controls, read-backs), the project's `project.json` and PRD, and the round decompositions under `decompositions/`.
4. Versioned S3 objects: you may `head-object` (metadata only) a key and VersionId you have found cited in an artifact, to record its current VersionId; the served FWD-3 keys are `s3://opal-data-assets/commonwealth/cottonwood/silver/{daily_returns,account_day_value,month_grades}/date=2026-06-23/part-00000.parquet` at VersionIds `lNzQMjfx6uX2zdFdWKsDANboShtDUz2N`, `ObKZXku7Am.QGjO.oSAsIScy8IcJxN5a`, `nkTE.F82uFSboXr9PEamIENCwFL9cwcC`.

**Your items.**

1. **One row per outcome.** For each FWD-n find the artifact that records its EXERCISE (a committed record or a versioned object that shows the read, listing or refusal DONE WHEN names) and the artifact in which a grade for it is stated (the same one, or a CVO adjudication or a CTO analysis). Cite the grading artifact as `kind` = `s3_key_version` (`ref` = `s3://bucket/key`, `version_or_commit` = the VersionId) or `commit` (`ref` = a short note, `version_or_commit` = a full commit hash) or `file_at_commit` (`ref` = the repo-relative path, `version_or_commit` = the full hash of the latest commit that touched it: `git log -1 --format=%H -- <path>`). A cited commit hash must be the FULL 40-character hash.
2. **The grade, read from the artifact.** `grade` is REALIZED only when the cited artifact itself states that this outcome's DONE WHEN was exercised and met (give the file and the locator inside it: a heading, a row id, a line range, plus a few words it says; no value). If the artifact says anything weaker (planned, built, "held", a status word with no exercise), or you cannot find an artifact that records the exercise, the grade is NOT_REALIZED. Never infer a grade from the existence of a table; never grade from this order's own text. A grade that changed over the rounds takes the LATEST one; say in `note` if an earlier artifact graded otherwise.
3. **The act for a NOT_REALIZED row.** `act` is the one act that would realize it (for example: the exercise that has not been run, or Andrew's send of the match packet and its one ask for Commonwealth's account-registration file) and `act_owner` is who does it (a serial, or `Andrew`). FWD-8 and FWD-9 are carried on Andrew's packet send (no contact with Cottonwood); report what the artifacts say about them like any other row, and name that act if they are NOT_REALIZED.
4. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~189/COMPLETION_REPORT.json` with exactly these top-level keys: `measured`, `reason` (when not measured), `rows` (nine objects, each with exactly: `fwd` ("FWD-1".."FWD-9"), `grade`, `artifact` (`{"kind","ref","version_or_commit"}`), `grade_read` (`{"file","locator","words"}`), `exercised` (`{"what","record"}`: what was exercised and the artifact that records it, no identifiers), `act`, `act_owner`, `note`), `not_established`; and a short `.md` beside it with the nine rows as a table. Counts and names only: no account number, name, tax number, cusip or dollar value in either file.

### ACCEPTANCE

<criterion id="CB100cv1-AC1" cell_refs="CB-cv-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~189/COMPLETION_REPORT.json',encoding='utf-8'));m=d['measured'];r=d.get('rows') or [];print('COMPLETION-REPORT measured=%s' % m + ((' rows=%d realized=%d not_realized=%d' % (len(r),sum(1 for x in r if x['grade']=='REALIZED'),sum(1 for x in r if x['grade']=='NOT_REALIZED'))) if m else ' reason=%s' % d['reason']))"</invocation><expect>^COMPLETION-REPORT measured=(True rows=9 realized=\d+ not_realized=\d+|False reason=.+)$</expect></criterion>
`CB100cv1-AC1` -- the report states nine rows and how many are REALIZED and NOT_REALIZED, or states plainly why nothing could be measured.

<criterion id="CB100cv1-AC2" cell_refs="CB-cv-1"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cv1_ac2_report_shape_check.py</invocation><expect>^REPORT-SHAPE rows=9 ids_ok=True grades_ok=True artifacts_ok=True grade_read_ok=True acts_ok=True$</expect></criterion>
`CB100cv1-AC2` -- the issuer's script (in your worktree; read it, do not edit it) checks the report's shape: exactly FWD-1..FWD-9 once each, every grade REALIZED or NOT_REALIZED, every row citing an artifact and the place its grade was read, and every NOT_REALIZED row naming an act and an owner.

<criterion id="CB100cv1-AC3" cell_refs="CB-cv-1"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cv1_ac3_artifacts_exist_check.py</invocation><expect>^ARTIFACTS exist=9 of 9$</expect></criterion>
`CB100cv1-AC3` -- the issuer's script checks that all nine cited artifacts exist at the cited version or commit (a VersionId that answers `head-object`; a commit or a file at a commit that `git cat-file` finds). Metadata and object existence only.

<expected_criteria>CB100cv1-AC1,CB100cv1-AC2,CB100cv1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below only: your deliverables folder and your own NEW channel row. You change no code, test, order or committed file besides your record. No scratch is needed; if you make any, keep it under `C:/Dev/ajb_workspace/.scratch/cotbkf_r100/` (gitignored, never committed).
- **AWS: READ-ONLY and METADATA ONLY** (`head-object` on a key and VersionId an artifact cites); no object body, no list of a client prefix, no write, no vendor call, no Bloomberg. You do not contact Cottonwood or Commonwealth.
- **No account number, name, tax number, date of birth, cusip or dollar value** in the record, the report or any message. The received dell2 run data and the private sweeps config are off git and not needed here: do not open them.
- **NEVER** serve, apply, overwrite, push, override a gate or `--force`; never edit any module; never grade by your own judgment; never copy a grade from this order.
- **Time.** Reading about a hundred rounds of records takes many greps; run each bounded and move on. A row you cannot ground in the time is NOT_REALIZED with `act` = "exercise it and record it", never a guess.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W189-S<k>` (`date -u +%FT%TZ` for `surfaced_at`), APPENDED to the channel file with `open(path, 'ab')` writing LF bytes only (the file holds CRLF lines from earlier rows: never read and rewrite it); `git diff --numstat` must show added lines only.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round100.md</decomp_doc> (round 100), cell `CB-cv-1`.
<owned_cells>CB-cv-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB100cv1-AC1, CB100cv1-AC2, CB100cv1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~189/ADVI_COTBKF.TO-CB-cv-1.completion-report-fwd-1-to-9.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB100cv1-AC1,CB100cv1-AC2,CB100cv1-AC3` BEFORE the flip. The `output_evidence` of each criterion must equal its `expect` pattern exactly (no suffix); put any note in `denominator`. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when all three PASS** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the `COMPLETION-REPORT` line. Then: the nine rows as a table (fwd, grade, grading artifact, where the grade was read, the act and owner for a NOT_REALIZED row); any row you could not ground and why; the three criterion lines; commits; every gate refusal and hook denial, verbatim. No account number or value.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of committed records and object metadata; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE head-object on versions an artifact already cites, under the existing role; no new permission.
comp-adversary: RUN -- the grade is read from an artifact and never from the order; two checks are the issuer's (shape, and existence of every cited artifact at its version or commit); BLIND: whether an artifact that states REALIZED was itself right is not re-exercised here (the CTO grades each row at the next analysis, and an exercise is a different cell), and the worker's search over about a hundred rounds of records can miss a later artifact that supersedes the one it cites.
lane: the <paths> block IS the grant (worker RULING 1). A read and a record: nothing outside the deliverables folder and one channel row is written to the repo.
</preflight>

**ISSUER NOTES:** Source: `1.0.0_SA_CTO~DELL1` msg 6601 (ROUND_ANALYSIS.round99). The report is evidence for the CTO's grade; the issuer reads it and spot-checks rows against their artifacts before it goes on. Mechanical checks dry-run at the base (the record file is absent): AC1, AC2 and AC3 FAIL there as expected; both scripts were run against a synthetic report as positive and negative controls (shape: good all-true, bad `ids_ok=False grades_ok=False`; existence: 8 of 9 with one absent commit).

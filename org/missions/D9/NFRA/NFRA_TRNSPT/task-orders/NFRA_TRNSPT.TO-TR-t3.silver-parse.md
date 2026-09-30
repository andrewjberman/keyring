# TO NFRA_TRNSPT.TO-TR-t3 -- thread hop 4: bronze to silver, one meeting's speaker turns as parquet

<to_id>NFRA_TRNSPT.TO-TR-t3</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~2</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-30</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>transcripts</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `TR-t-3` (`decompositions/NFRA_TRNSPT_DECOMP.md`) |
**outcome_ref:** FWD-1, FWD-5 | **depends_on:** none (the bronze objects it reads exist since 2026-09-29)

---

## WORKER FACE

### THE CELL

`TR-t-3`, thread hop 4 (PRD section 2): "Bronze -> silver: the parsed speaker turns as parquet (speaker, order, time), for one
meeting (FWD-5's first exercise)." Andrew-direct 2026-09-30: "Silver is typed and deduplicated bronze in parquet with PII wiped."
(No wipe on transcripts this round: an internal meeting transcript carries staff names, which are the data; the PII wipe is
C-WIPE's rule for the mail source.) FWD-5 ACCEPT: "an analyst who now opens a file to find what was said about one company gets
it without opening the file."

**What exists (read, never edit).** Bronze objects at `s3://opal-data-transcripts/teams/transcripts/bronze/<series>/date=YYYY-MM-DD/<ID>.vtt`,
`<ID>.metadata.vtt`, `<ID>.graph.json`. The content WebVTT carries `<v Speaker Name>text</v>` cues with offsets from recording
start. The metadata WebVTT carries, per cue, a JSON payload `{"startDateTime","endDateTime","speakerName","spokenText","spokenLanguage"}`
with WALL-CLOCK UTC times -- OBSERVED values; use them for `start_utc`/`end_utc` and never derive a clock from an operator-stated
start (the three-clock trap in `research_transcripts/README.md`). Prior art for the cue grammar: `research_transcripts/bin/ingest_vtt.py`
`parse_vtt` (vendor the regexes with a provenance comment; do not import from that closed project's `bin/`). Your seat shell
reads the bucket as Andrew's IAM user, the one key grantee.

**Build:**
1. `data/transcripts/scripts/teams/parse_silver.py`: `parse(vtt_bytes, metadata_bytes) -> (rows, warnings)` with one row per cue:
   `transcript_id, series, meeting_date, turn_index (0-based, cue order), speaker, start_utc, end_utc (from the metadata cue
   with the same offsets; ISO strings), start_s, end_s (float offsets), text`. `CONFERENCE ROOM` stays as the speaker string (a
   device, not a person -- carry it, do not resolve it). Count `unparsed` cues (a cue whose line the grammar did not consume)
   and put every one in `warnings`; never drop silently. `write(rows, series, transcript_id, meeting_date, *, s3, kms_key_arn,
   apply) -> key` writes ONE parquet (pyarrow, the schema above, strings UTF-8, floats float64, `turn_index` int32) at
   `lib.opal_naming.address("teams","transcripts","silver",series,"date=<meeting_date>","<transcript_id>.parquet")` with
   `ServerSideEncryption="aws:kms"` and `SSEKMSKeyId` resolved from `alias/opal-data-transcripts` at run time. `parse_and_write(series,
   transcript_id, *, s3, kms_key_arn, apply)` reads the sidecar to find the date and the two objects, parses, writes, and returns
   `{"key","rows","speakers","unparsed"}` (this is the entry the pull job calls in-process, TR-t-1 `with_silver`).
2. CLI: `python data/transcripts/scripts/teams/parse_silver.py --series <s> --transcript <ID> [--apply]` prints one line
   `SILVER-WRITTEN unparsed=<n> rows=<r> speakers=<k> key=<s3 address>` (`SILVER-DRY ...` without `--apply`).
3. Fixtures `data/transcripts/scripts/tests/fixtures/teams_vtt/sample.vtt` + `sample.metadata.vtt`: SYNTHETIC, invented speakers
   ("Speaker One", "CONFERENCE ROOM"), 6-8 cues, matching offsets and wall-clock payloads, one deliberately malformed cue line
   for the `unparsed` path. NEVER put real transcript text in the repository (the three non-research archetypes are barred from git).
4. Tests `data/transcripts/scripts/tests/test_teams_parse_silver.py`: row count and order, speaker tags, wall-clock from the metadata
   file (not derived), the malformed line counted and reported, parquet schema and the KMS headers on the fake-S3 put, and
   `parse_and_write` reading bronze through the sidecar.

### ACCEPTANCE

<criterion id="TR1-t3-AC1" cell_refs="TR-t-3"><invocation>python -m pytest data/transcripts/scripts/tests/test_teams_parse_silver.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`TR1-t3-AC1` -- the parse on synthetic cues: order, speakers, observed wall-clock, the unparsed path, the parquet schema.

<criterion id="TR1-t3-AC2" cell_refs="TR-t-3"><invocation>python data/transcripts/scripts/teams/parse_silver.py --series monday_meeting --transcript MM-20260928-0858 --apply</invocation><expect>SILVER-WRITTEN unparsed=0</expect></criterion>
`TR1-t3-AC2` -- the REAL run: the held Monday meeting (290 cues, 7 speakers per its sidecar) parses with zero unparsed cues and its
parquet lands at the builder's silver address.

<criterion id="TR1-t3-AC3" cell_refs="TR-t-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R1_CHECKS/r1_silver_check.py monday_meeting MM-20260928-0858 2026-09-28</invocation><expect>SILVER-OK</expect></criterion>
`TR1-t3-AC3` -- read back from the bucket: the declared columns, rows present, encrypted under the transcripts key.

<expected_criteria>TR1-t3-AC1,TR1-t3-AC2,TR1-t3-AC3</expected_criteria>

Dry-run at the base 2026-09-30 14:0xZ: AC1 "no tests ran", AC2 "No such file", AC3 SILVER-MISSING -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **SERVED.** The one real write is the silver parquet of `MM-20260928-0858` (a new tier nobody serves yet); nothing else is
  written to the bucket; nothing in bronze is touched; no deploy.
- **The reader (TR-t-4) is the next order in your queue** and reads this parquet by the same address: keep the schema exactly.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `NFRA_TRNSPT-W2-S<k>`), and do not weaken the test to pass.

<paths>
data/transcripts/scripts/teams/parse_silver.py
data/transcripts/scripts/tests/test_teams_parse_silver.py
data/transcripts/scripts/tests/fixtures/teams_vtt/
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP.md</decomp_doc> (round 1), cell `TR-t-3`.
<owned_cells>TR-t-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR1-t3-AC1, TR1-t3-AC2, TR1-t3-AC3. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/NFRA_TRNSPT.TO-TR-t3.silver-parse.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR1-t3-AC1,TR1-t3-AC2,TR1-t3-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the schema, the SILVER-WRITTEN line (rows, speakers, key), the SILVER-OK line, the pytest line, commits. Counts and keys only, never cue text.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the event-triggered silver Lambda of PRD section 4 is a round-2 item (decomposition ruling: the pull job parses in-process).
comp-iam: RUN -- infra/aws/terraform/transcripts/main.tf read at the cut: 1 KMS key policy with 2 statements and 1 reader principal (arn:aws:iam::313476888478:user/Andrew_Berman, the var.reader_principal_arns default), 1 bucket policy with 2 Deny statements (TLS-only, key-only); BLIND: the live IAM plane outside this root was not scanned (0 of the account's roles read). The real silver write runs under that one grantee; this cell adds no principal.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the metadata WebVTT's wall-clock payload and the three-clock trap are inlined.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 section 2 hop 4 (S06); decomposition round 1 cell TR-t-3.

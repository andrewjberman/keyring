# TO NFRA_TRNSPT.TO-TR-v2 -- FWD-2 beyond Monday: silver for every held transcript of the three reachable meetings

<to_id>NFRA_TRNSPT.TO-TR-v2</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~3</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>transcripts</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `TR-v-2` (`decompositions/NFRA_TRNSPT_DECOMP_R2.md`) |
**outcome_ref:** FWD-2, FWD-5 | **depends_on:** none (the bronze objects exist since 2026-09-29)

---

## WORKER FACE

### THE CELL

`TR-v-2` (CTO analysis section 4 item 5: "FWD-2's first archetype beyond Monday, as the transcript tools allow"). No new pull is
possible (the gateway has no transcript tools yet), but bronze already holds 30 transcripts of three meetings: `monday_meeting` 15,
`ocio_ic` 7, `asset_management_ic` 8 (measured at the cut: `SILVER-CENSUS bronze=30 silver=1`). FWD-5 ACCEPT: "an analyst who now
opens a file to find what was said about one company gets it without opening the file" -- today only one Monday meeting is readable.

**What exists (read, never edit):** `data/transcripts/scripts/teams/parse_silver.py` -- `parse_and_write(series, transcript_id, *, s3,
kms_key_arn, apply)` reads the sidecar and both WebVTT objects, parses, writes ONE parquet per transcript at
`lib.opal_naming.address("teams","transcripts","silver",series,"date=<meeting_date>","<transcript_id>.parquet")` with SSE-KMS, and returns
`{"key","rows","speakers","unparsed"}`; `resolve_kms_key_arn` resolves `alias/opal-data-transcripts`. Bronze keys are
`address("teams","transcripts","bronze",series,"date=YYYY-MM-DD","<ID>.graph.json" | "<ID>.vtt" | "<ID>.metadata.vtt")`. Your seat shell
reads and writes the bucket as Andrew's IAM user, the one key grantee.

**Build:** `data/transcripts/scripts/teams/backfill_silver.py --series <comma list> [--apply | --dry-run]`:
1. For each series, list the bronze prefix (build it from `address()`; paginate `list_objects_v2`), collect every `<ID>.graph.json`,
   and call `parse_silver.parse_and_write(series, ID, ..., apply=<flag>)` for each (idempotent: re-writing the same parquet is allowed).
2. One line per transcript: `BACKFILL <series> <ID> rows=<r> speakers=<k> unparsed=<u> action=<WRITTEN|DRY|FAILED:<reason>>`
   (counts only, never cue text), then `BACKFILL-SILVER transcripts=N written=W unparsed_total=U failed=F`.
3. A transcript that fails to parse is reported and the run continues; a non-zero `unparsed` is reported, never dropped. If any
   transcript reports `unparsed > 0`, write a surprise row naming it and the count, and do NOT change the parser (another order owns it).
4. Run it for real: `--series monday_meeting,ocio_ic,asset_management_ic --apply`, then the census check.

### ACCEPTANCE

<criterion id="TR2-v2-AC1" cell_refs="TR-v-2"><invocation>python data/transcripts/scripts/teams/backfill_silver.py --series monday_meeting,ocio_ic,asset_management_ic --apply</invocation><expect>BACKFILL-SILVER transcripts=30 written=30 unparsed_total=0 failed=0</expect></criterion>
`TR2-v2-AC1` -- the REAL run: every held transcript parsed and written to silver.

<criterion id="TR2-v2-AC2" cell_refs="TR-v-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R2_CHECKS/r2_silver_census_check.py</invocation><expect>SILVER-CENSUS bronze=30 silver=30 missing=0 empty=0</expect></criterion>
`TR2-v2-AC2` -- read back from the bucket: every bronze transcript has a readable, non-empty parquet.

<expected_criteria>TR2-v2-AC1,TR2-v2-AC2</expected_criteria>

Dry-run at the base c31230ea02: AC1 backfill_silver.py absent rc 2; AC2 `SILVER-CENSUS bronze=30 silver=1 missing=29 empty=0` -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **SERVED.** The only writes are silver parquets of transcripts already in bronze; nothing in bronze is touched; no deploy.
- **Never** put a cue's text in any file, report or row: counts and ids only.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `NFRA_TRNSPT-W3-S<k>`, next unused after W3-S2), and do not weaken the test to pass.

<paths>
data/transcripts/scripts/teams/backfill_silver.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R2.md</decomp_doc> (round 2), cell `TR-v-2`.
<owned_cells>TR-v-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR2-v2-AC1, TR2-v2-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~3/NFRA_TRNSPT.TO-TR-v2.silver-every-held-transcript.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR2-v2-AC1,TR2-v2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** per-series transcripts, rows and speakers totals, any unparsed or failed transcript by id, the two check lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-time backfill; no schedule touched.
comp-iam: RUN -- infra/aws/terraform/transcripts/main.tf read at the cut: 1 KMS key policy with 2 statements and 1 reader principal (Andrew's IAM user), 1 bucket policy with 2 Deny statements; BLIND: the live IAM plane outside this root (0 of the account's roles read). The silver writes run under that one grantee; nothing is granted.
comp-adversary: DECLARED-NOT-APPLICABLE -- the parser is round 1's, exercised on the real Monday meeting (unparsed=0).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-1 analysis @acd1033e60 section 4 item 5; decomposition round 2 cell TR-v-2.

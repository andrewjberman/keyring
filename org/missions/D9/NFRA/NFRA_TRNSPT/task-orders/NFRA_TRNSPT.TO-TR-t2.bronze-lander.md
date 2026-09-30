# TO NFRA_TRNSPT.TO-TR-t2 -- thread hop 3: the bronze lander for Teams transcripts

<to_id>NFRA_TRNSPT.TO-TR-t2</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-30</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>transcripts</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `TR-t-2` (`decompositions/NFRA_TRNSPT_DECOMP.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-t-2`, thread hop 3 (PRD `org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md` section 2): "The gateway -> bronze
landing under the builder-produced address for source `teams`, scope `transcripts`, table for the meeting: the raw WebVTT,
the raw metadata WebVTT and the sidecar, byte for byte." FWD-1: "Andrew opens the database on a Monday afternoon and finds
that morning's meeting, with who said what, and nobody touched anything."

Andrew-direct 2026-09-29, verbatim: "just create an s3 bucket, opal-data-transcripts and house it there encrypted". Bronze
holds each object exactly as received (C-TIERS). Never overwrite (the bucket is versioned; the rule stands).

**What exists (read, never edit):** 91 objects under `s3://opal-data-transcripts/teams/transcripts/bronze/` landed by hand on
2026-09-29 (30 transcripts x `<ID>.vtt`, `<ID>.metadata.vtt`, `<ID>.graph.json`). One sidecar, `MM-20260928-0858.graph.json`,
is the shape to reproduce: `transcript_id, archetype, teams_subject, organizer, source, graph{meetingId,id,createdDateTime,endDateTime},
content{object,bytes,sha256,cues,speaker_tagged_cues,distinct_speakers,last_cue_end}, metadata_content{object,http,bytes,sha256},
id_clock{basis,claim}, pulled_utc, pulled_by`. Prior art for the refusals and the id clock:
`research_transcripts/bin/land_graph_transcript.py` (WEBVTT check, speaker-tag check, `<PREFIX>-<YYYYMMDD>-<HHMM>` Eastern).
The bucket policy (`infra/aws/terraform/transcripts/main.tf`) refuses a PutObject whose KMS key header is not the transcripts
key, and every read needs key use; your seat shell runs as the one grantee.

**Build (LOCAL: code + tests; the only S3 act is a READ probe):**
1. `data/transcripts/scripts/teams/land_bronze.py` with `land(series, vtt_bytes, metadata_bytes, graph_row, *, s3, kms_key_arn,
   pulled_by, apply=False) -> LandResult(action, transcript_id, keys, sidecar, reason)`, action one of `LANDED`, `DRY`,
   `SKIP-IDENTICAL`, `REFUSED`. Rules: refuse a body not starting `WEBVTT` (after an optional BOM); refuse a body with zero
   `<v ` tags (an unattributed transcript is a different artifact); `series` is one of `monday_meeting`, `ocio_ic`,
   `asset_management_ic`, `research_meeting` with prefixes `MM`, `ICO`, `ICA`, `RT`; `transcript_id` = `<prefix>-<YYYYMMDD>-<HHMM>`
   from `graph_row["createdDateTime"]` in `America/New_York`; the partition is `date=<that Eastern date>`; keys are
   `lib.opal_naming.address("teams", "transcripts", "bronze", series, "date=YYYY-MM-DD", object)` for the three objects (import
   `lib.opal_naming` from the repo root; never type a key). Sidecar per the shape above with `cues`, `speaker_tagged_cues`,
   `distinct_speakers`, `last_cue_end` computed from the body and sha256 of both bodies. Existing key: `head_object`; identical
   sha256 -> `SKIP-IDENTICAL`; different -> `REFUSED` (never overwrite); absent -> put all three with
   `ServerSideEncryption="aws:kms"` and `SSEKMSKeyId=<kms_key_arn>` when `apply`, else `DRY`. Resolve the key ARN at run time
   from `alias/opal-data-transcripts` (`kms.describe_key`), never a typed ARN.
2. A CLI: `python data/transcripts/scripts/teams/land_bronze.py --probe-held <series> <transcript_id>` reads that transcript's
   real sidecar and `.vtt` from the bucket, recomputes the sha256, and prints `LAND-PROBE held=1 sha_match=1 write=0`
   (`held=0` when absent). It never writes.
3. Tests `data/transcripts/scripts/tests/test_teams_land_bronze.py` on an in-memory fake S3 (a small class with `put_object`,
   `head_object`, `get_object`, raising a `ClientError`-shaped 404 on a missing key; `moto` is not installed) and SYNTHETIC
   WebVTT bytes (invented speakers): the three keys are `address()` output; the sidecar fields; the two refusals; `DRY` writes
   nothing; `LANDED` puts three objects with both encryption headers; a second identical land is `SKIP-IDENTICAL`; a changed body
   on an existing key is `REFUSED`. Never put real transcript text in the repository.

### ACCEPTANCE

<criterion id="TR1-t2-AC1" cell_refs="TR-t-2"><invocation>python -m pytest data/transcripts/scripts/tests/test_teams_land_bronze.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`TR1-t2-AC1` -- addresses from the builder, the sidecar shape, both refusals, idempotence and never-overwrite, on a fake S3.

<criterion id="TR1-t2-AC2" cell_refs="TR-t-2"><invocation>python data/transcripts/scripts/teams/land_bronze.py --probe-held monday_meeting MM-20260928-0858</invocation><expect>LAND-PROBE held=1 sha_match=1 write=0</expect></criterion>
`TR1-t2-AC2` -- the seam against the REAL bucket: the served `.vtt` bytes hash to the sidecar's sha256; nothing written.

<expected_criteria>TR1-t2-AC1,TR1-t2-AC2</expected_criteria>

Dry-run at the base 2026-09-30 14:0xZ: AC1 "no tests ran" (file absent), AC2 "No such file" -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL.** Reads the bucket; writes no object; no deploy; no Terraform.
- **The pull job (TR-t-1) is the next order in your queue** and will import this module: keep `land()` importable with the
  signature above and put nothing at import time that opens a network connection.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `NFRA_TRNSPT-W1-S<k>`), and do not weaken the test to pass.

<paths>
data/transcripts/scripts/teams/land_bronze.py
data/transcripts/scripts/tests/test_teams_land_bronze.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP.md</decomp_doc> (round 1), cell `TR-t-2`.
<owned_cells>TR-t-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR1-t2-AC1, TR1-t2-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-t2.bronze-lander.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR1-t2-AC1,TR1-t2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the `land()` signature, the three keys the probe read, the probe line, the pytest line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no schedule is touched.
comp-iam: RUN -- key use is Andrew's IAM user only (main.tf reader_principal_arns default); this cell writes nothing and runs under that identity. The writer principal is drafted in TR-i-1.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the 09-29 sidecar shape and the never-overwrite rule are inlined.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 section 2 hop 3 (S03 landing half); decomposition round 1 cell TR-t-2.

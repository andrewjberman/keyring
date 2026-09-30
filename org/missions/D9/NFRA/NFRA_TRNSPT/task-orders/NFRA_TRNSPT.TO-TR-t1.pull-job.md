# TO NFRA_TRNSPT.TO-TR-t1 -- thread hops 1-2: the scheduled pull job and its gateway client

<to_id>NFRA_TRNSPT.TO-TR-t1</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>transcripts</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `TR-t-1` (`decompositions/NFRA_TRNSPT_DECOMP.md`) |
**outcome_ref:** FWD-1 | **depends_on:** TR-t-2 (drained; `land_bronze.land()` exists on your branch)

---

## WORKER FACE

### THE CELL

`TR-t-1`, thread hops 1-2 (PRD section 2): "1. The meeting ends -> a SCHEDULED pull notices it (a listing of the meeting's
series by its meeting id; no change notification is claimed; the cadence is a schedule on its own clock). 2. The pull -> the
Opal gateway's transcript tools under Andrew's account (the tools are NFRA_OPLGTW's parked spec
`docs/briefs/opal-gateway-meeting-transcript-tools-spec-20260929.md`; built on site Z)."

The gateway tools do NOT exist on the deployed gateway (measured at the cut: zero transcript tools in `infra/aws/ec2/opal-gateway/app/tools.py`).
This cell builds the job against the spec's tool SHAPES with a fixture transport; the real transport is wired when site Z lands
the tools (S04). Andrew-direct: "for now we just need to wing it through my account".

**Build (LOCAL):**
1. `data/transcripts/scripts/teams/series.json`: the four series rows copied from `research_transcripts/schema/series.json`
   (`online_meeting_id`, `teams_subject`, `organizer_name`, `id_prefix`, plus `table` = `monday_meeting` | `ocio_ic` |
   `asset_management_ic` | `research_meeting`) with a `_provenance` line naming that file and this order. A copy, stated as one.
2. `data/transcripts/scripts/teams/gateway_client.py`: a `TranscriptTransport` protocol with
   `list_meeting_transcripts(meeting_id) -> {"rows": [{"id","createdDateTime","endDateTime"}], "count": n}` (spec 4.2; a 403
   raises `Refused(code)`), and `read_meeting_transcript(meeting_id, transcript_id, fmt) -> bytes` with `fmt` in `vtt` |
   `metadata` (spec 4.3; a 404 raises `Expired`). `FixtureTransport(dir)` replays files from a directory
   (`<meeting_id>.list.json`, `<meeting_id>.<transcript_id>.vtt`, `.metadata.vtt`; a `.refused` marker file -> `Refused`; a
   missing content file -> `Expired`). `GatewayTransport(base_url, bearer)` is a STUB: each method raises
   `GatewayToolsAbsent("S04 not landed: <the route it would call>")` and makes no network call.
3. `data/transcripts/scripts/teams/pull.py`: `run(transport, s3, *, kms_key_arn, apply, now, pulled_by, with_silver=False) -> RunRecord`.
   For each series: list; for each row derive the transcript id the lander would mint and `head_object` its sidecar key
   (`land_bronze` computes both -- import it, do not re-derive); HELD -> skip; new -> read `vtt` and `metadata`, `land()`;
   outcomes per row typed `LANDED | HELD | EXPIRED | REFUSED`, per series `REFUSED` when the list is refused. Write the run
   record `{run_id, started_utc, ended_utc, no_person: true, transport, series: [{table, listed, landed, held, expired,
   refused, transcript_ids}]}` at `address("teams","transcripts","state","pull_runs","run=<started ISO>","run.json")` (R21:
   state is the fifth class, never inside a tier) with the KMS headers when `apply`. `with_silver=True` imports
   `data.transcripts.scripts.teams.parse_silver` LAZILY and calls `parse_and_write(...)` for each LANDED transcript (that module
   is another chain's cell; it may be absent on your branch -- the lazy import and a typed `SILVER-SKIPPED` outcome keep this
   cell independent of it).
4. CLI: `python data/transcripts/scripts/teams/pull.py --transport fixture --fixture <dir> --dry-run` prints one line
   `PULL-DRY series=4 listed=N new=A held=B expired=C refused=D`; `--transport gateway` prints `GATEWAY-TOOLS ABSENT <route>`
   and exits 3 while the stub stands.
5. Fixture `data/transcripts/scripts/tests/fixtures/teams_pull/` (SYNTHETIC bodies with invented speakers): monday_meeting 2
   rows (one HELD -- its sidecar preloaded into the fake S3 by the test, one new), ocio_ic 1 row whose content is EXPIRED,
   asset_management_ic 1 new, research_meeting REFUSED (403 3003, the measured refusal). So `listed=4 new=2 held=1 expired=1 refused=1`.
6. Tests `data/transcripts/scripts/tests/test_teams_pull.py` on the fake S3 pattern of `test_teams_land_bronze.py`: `apply=True`
   lands 2 transcripts (6 objects) and one run record; HELD skipped; EXPIRED and REFUSED typed; `no_person` true; `--dry-run`
   writes nothing.

### ACCEPTANCE

<criterion id="TR1-t1-AC1" cell_refs="TR-t-1"><invocation>python -m pytest data/transcripts/scripts/tests/test_teams_pull.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`TR1-t1-AC1` -- the job lands what is new, skips what is held, types expired and refused, and writes a run record.

<criterion id="TR1-t1-AC2" cell_refs="TR-t-1"><invocation>python data/transcripts/scripts/teams/pull.py --transport fixture --fixture data/transcripts/scripts/tests/fixtures/teams_pull --dry-run</invocation><expect>PULL-DRY series=4 listed=4 new=2 held=1 expired=1 refused=1</expect></criterion>
`TR1-t1-AC2` -- the entry point the schedule will call, over the typed fixture, with the held case pre-seeded by the CLI's `--seed-held` flag or the fixture's `held.json` (your choice; state it).

<expected_criteria>TR1-t1-AC1,TR1-t1-AC2</expected_criteria>

Dry-run at the base 2026-09-30 14:0xZ: AC1 "no tests ran", AC2 "No such file" -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL.** No network call to the gateway; no object written to the bucket by any test or by `--dry-run`. Do not run
  `--apply` against the real bucket: the real pull waits on S04/S05 and on TR-i-1's release.
- **The Lambda handler (TR-i-1) is the next order in your queue** and wraps `run()`; keep the signature above.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `NFRA_TRNSPT-W1-S<k>`), and do not weaken the test to pass.

<paths>
data/transcripts/scripts/teams/pull.py
data/transcripts/scripts/teams/gateway_client.py
data/transcripts/scripts/teams/series.json
data/transcripts/scripts/tests/test_teams_pull.py
data/transcripts/scripts/tests/fixtures/teams_pull/
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP.md</decomp_doc> (round 1), cell `TR-t-1`.
<owned_cells>TR-t-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR1-t1-AC1, TR1-t1-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-t1.pull-job.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR1-t1-AC1,TR1-t1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the transport protocol, the routes the stub names, the run-record address, the PULL-DRY line, the pytest line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the schedule is DESIRED in TR-i-1 and applied on a later release.
comp-iam: RUN -- nothing granted; the run record's write needs key use, which the drafted writer role (TR-i-1) carries desired.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the Research Meeting refusal and the 4 expired rows of the first pull are typed into the fixture.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 section 2 hops 1-2 (S03, S04 consumed, S05 consumed); decomposition round 1 cell TR-t-1.

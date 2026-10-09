# TO NFRA_TRNSPT.TO-TR-t20 -- the Teams gateway transport to the /hx/transcripts contract + the owner-named bearer (row D2-S10)

<to_id>NFRA_TRNSPT.TO-TR-t20</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~2</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>transport</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-t-20` (`decompositions/NFRA_TRNSPT_DECOMP_R20.md`) | **outcome_ref:** FWD-1, FWD-2, FWD-3 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-t-20` (CTO ADDENDUM 9 @f586e1e6e7; row NFRA_TRNSPT-D2-S10): the Teams pull cannot land a meeting: `data/transcripts/scripts/teams/gateway_client.py`
`GatewayTransport` is a STUB that raises `GatewayToolsAbsent` (:5, :81), and `infra/aws/terraform/transcripts/pull.tf` names a bearer secret that
does not exist (`teams/global/gateway-token`). The gateway owner answered (site Z `1.0.0_SA_CTO~Z`, relayed MSTR msg 3074): read the contract in
full, `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/HX_TRANSCRIPTS_ROUTE_CONTRACT_COPY_f67fbc2390.md` -- base
`https://mcp.opalinvest.dev`, prefix `/hx/transcripts`, GET only, bearer `gateway/transcripts/bearer`, two paths, answer shapes and every refusal.

**Build (the pattern of `data/transcripts/scripts/outlook/gateway_mail.py`, which reads its bearer by name at call time):**
1. `gateway_client.py` `GatewayTransport`: implement `list_meeting_transcripts(meeting_id)` (GET `.../meetings/{id}/transcripts` -> the
   contract's `rows`/`count`) and `read_meeting_transcript(meeting_id, transcript_id, fmt)` (GET `.../meetings/{id}/transcripts/{tid}` -> the
   `content` bytes, verified against `byte_count` and `sha256`). Base URL and prefix are the contract's literals; the bearer is read BY NAME
   (`BEARER_SECRET = "gateway/transcripts/bearer"`) at call time, held in memory only, never printed or in an exception. Every non-200 in the
   contract's table raises a typed error carrying status and the route's error code (never the bearer, never content); `needs_login` and
   `meeting_not_allowed` are distinct. Ids are validated against `[A-Za-z0-9_\-=]+`. The `FixtureTransport` stays as is.
2. `pull.tf`: replace the `pull_secret_name` local with a `data "aws_secretsmanager_secret"` on `gateway/transcripts/bearer` (as `mail_pull.tf:28-30`
   does), its ARN in the role's GetSecretValue statement and its name in `BEARER_SECRET_NAME`; nothing else in pull.tf changes.
3. `data/transcripts/scripts/tests/test_teams_gateway_transport.py` (new; a fake HTTP opener and fake secrets reader, NO network):
   `test_transport_follows_route_contract` (the two GETs hit exactly the contract's URLs with the bearer header; a body whose sha256 or length
   mismatches is refused); `test_refusals_raise_typed_errors` (401, 403 meeting_not_allowed, 503 needs_login, 502 graph_error each raise their own
   type with no bearer in the message); `test_pull_tf_reads_transcripts_bearer_by_data_source`. Keep `test_teams_pull.py` and every other test green.

### ACCEPTANCE

<criterion id="TR20-t20-AC1" cell_refs="TR-t-20"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R20_CHECKS/r20_checks.py t20</invocation><expect>R20-T20-OK</expect></criterion>
`TR20-t20-AC1` -- the three named tests pass and the file is green.

<expected_criteria>TR20-t20-AC1</expected_criteria>

Dry-run at the base (box/dell2 e18849b58c): `R20-T20-FAIL absent` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **WORLD by path floor (pull.tf), LOCAL in act.** Fakes and synthetic fixtures only; no AWS, HTTP, plan or apply; no transcript, email or client content anywhere.
- **Refusal clause.** A builder refusal for a new name or address: add nothing typed; file a surprise row (`NFRA_TRNSPT-D2-W2-S<k>`, next unused across every document under `surprise-channel/`) and stop that piece.

<paths>
data/transcripts/scripts/teams/gateway_client.py
infra/aws/terraform/transcripts/pull.tf
data/transcripts/scripts/tests/test_teams_gateway_transport.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R20.md</decomp_doc> (round 20), cell `TR-t-20`.
<owned_cells>TR-t-20</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR20-t20-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/NFRA_TRNSPT.TO-TR-t20.teams-gateway-transport.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR20-t20-AC1` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, any address or name with its builder call, the test names, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a local build, no schedule created.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no grant change.
comp-adversary: RUN -- sources: CTO ADDENDUM 10 @200cbac519, TR-q-19 and TR-e-19 as merged and the modules named in the face; BLIND to live data (fakes only). Traps: content in output or fixtures, a typed address, a behavior change in an existing reader; the face and the three named tests fix each.
lane: the paths block.
</preflight>

Source: CTO msgs 2986, 3012 (ADDENDUM 9, 10); gateway owner contract (MSTR msg 3074); decomposition round 20 cell TR-t-20.

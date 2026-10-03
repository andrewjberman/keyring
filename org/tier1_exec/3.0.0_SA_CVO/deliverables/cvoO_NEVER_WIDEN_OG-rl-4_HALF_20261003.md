# NEVER-WIDEN half -- NFRA_OPLGTW OG-rl-4, the round-14 gateway release on live 4231bd2ddc -- SIGNED (3.0.0_SA_CVO~O, 2026-10-03 ~02:3xZ)

**Asked:** `2.0.0_SA_COO~O` msg 28873. Ask:
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-4_20261003.md` @2d94823961. The half
is required by ruling 4 of the round-13 analysis, because the symmetric refusal changes whom `/hx/mail` and
`/hx/transcripts` admit.

**VERDICT: SIGNED** with guards P1-P2, on these pins:
- release `rel-nfra-oplgtw-r14` HEAD `af2d762970`;
- live base `4231bd2ddc`;
- rollback `/c/tmp/og-rb9` at `4231bd2ddc`.

## Independently measured (2026-10-03 ~02:0xZ-02:3xZ)

**Bytes.**
- `4231bd2ddc` is an ancestor of `af2d762970`, through 2 commits by `0.9.0_WK_NFRA_OPLGTW~15` (`25335f8ac3`,
  `af2d762970`).
- Census: 9 files, +225/-22, all under `infra/aws/ec2/opal-gateway`. 0 paths outside it.
- `ms_ingest.py`, `taxsma_workbook.py` and `teams_route.py` are not in the census.

**The capability change, read in code.**
- `mail_route.py` and `transcript_route.py` each gain `OTHER_ROUTE_BEARERS`:
  - each lists the six other route bearers;
  - each gains a constant-time `_shared_elsewhere`;
  - `match_bearer` returns `None` when the matched value is shared.
- This is the `teams_route` pattern, unchanged. With distinct values, admission is identical.
- This closes the latent gap in my OG-rl-3 half (@e13f0910d4), and guard N1 there lapses when this ships.

**Audit.**
- `log_call` gains two optional keys, added only when given: `bytes` and `principal` (`<tid>/<oid>`, an id, not
  content).
- `tools._run` passes them for `read_meeting_transcript` ok results only. Every other record is unchanged.

**The `.env` instrument can see the property.**
- The unit (`deploy/opal-gateway.service`) loads `.env` via `EnvironmentFile=`.
- `config.py`'s `load_dotenv()` does not override keys that are already set.
- So `/proc/<MainPID>/environ`, which is what `rl4_verify.py:65-69` hashes, holds the values the app actually uses.
- The issuer's pre-deploy negative control (`rl4_verify_negative_control.out`) fails md5 on exactly the 4 changed app
  files. It passes 50 of 50 value hashes and the own-bearer reads: mail 200, teams 200, transcripts 403
  `meeting_not_allowed`.

**Rosters secret.**
- Only the deploy template reads `gateway/principals/rosters` (Grep over `infra/`: the template, the TF definition and
  the manifest). The app takes its rosters from `.env`, so a new key widens no reader.
- Current state: one version, AWSCURRENT, last changed 2026-10-01 07:29Z.

**Base.** S3 `opal-gateway-latest.tar.gz` ETag `90196691...` equals `opal-gateway-4231bd2ddc.tar.gz`; no newer key exists.

## The one branch the ask leaves to the verify

Property (a), whom `/hx/mail` and `/hx/transcripts` admit, is graded only AFTER the deploy (own bearer 401 -> roll back).

The distinctness of `MAIL_BEARER` and `TRANSCRIPT_BEARER` from the other route bearers is only partly measured:
- `TEAMS_BEARER` is distinct from both: the teams route admits its holder (200), and it refuses a shared value.
- `MAIL` vs `TRANSCRIPT`, and either of them vs `OTP`/`MS_INGEST`/`GRAPH_READ`: no instrument has read these pairs.

If any pair is equal, the release refuses that route's live holder (NFRA_TRNSPT's pull) until the rollback lands. P1
reads it before the act, at the cost of one SSM call.

## Guards

- **P1 -- distinct values, read before the act.**
  - On the host over SSM, compare the live `.env` value of each of `MAIL_BEARER` and `TRANSCRIPT_BEARER` against every
    whitespace-split value of the other six route bearers.
  - Use a constant-time compare and print `EQUAL`/`DIFFER` per pair only. Never print a value.
  - Any `EQUAL`: STOP, no deploy. That value must be rotated first, and the rotation is its own act.
- **P2 -- base at the act.** If the host md5 or S3 `latest` has moved off `4231bd2ddc` when PHASE B starts, this half is
  VOID.

## Covers / does not cover

**Covers:** every key in section 2 of the ask, both branches of each property in its section 3, and P1.
- (b): the 50 process-value hashes catch any systemd 252 quote handling, `FIRM_ROLE_ARNS` included, with a rollback.
- (c): a missing key refuses rc 3 before any write.

**Rollbacks named:** og-rb9 (code and `.env`) and `put-secret-value` of the prior roster value. Each stands alone.

**Does NOT cover:** a moved base, a changed release pin, a rotation, any Terraform, IAM or ALB write, or the CTO half.

-- 3.0.0_SA_CVO~O

# Deploy Completion Record
**Date opened:** 2026-10-09T14:14:25.738253+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPORTAL MP-x-4 (round 5, E2): the narrow gateway release that serves the Control Plane page -- MP-x-1's four files onto the live r29 base, dashboard bundle mcportal d60b4e0
**Authored by:** 0.7.0_AE_CloudOps~MP
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | bundle build: mcportal d60b4e0 built by deploy-to-ec2.sh from EC2_MANIFEST.json services.opal-gateway.mcportal_commit (never the checkout's HEAD); bun cache pre-check must pass so no package is fetched | pre-check 77 of 77 rc=0 against d60b4e0's own bun.lock; INFO: building mcportal @ d60b4e0 then dist/index.html present |  | OPEN |
| L2 | s3-prefix | release build and upload: artifact opal-gateway-<sha>.tar.gz to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ with git-ref metadata, + latest | head-object ContentLength/ETag and Metadata.git-ref == the release sha |  | OPEN |
| L3 | activation | SSM pull and restart on i-07dccb1615503ac99, then /health 200 within 90 s or the named rollback runs AT ONCE | ssm:<command_id> Status=Success; /health=200; MainPID moves off 857046 |  | OPEN |
| L4 | verify | manifest record + MCP tool surface unmoved + the three ACs | EC2_MANIFEST deployed_commit=<release sha>, previous_deployed_commit=91811b648a, mcportal_commit=d60b4e0; tools 66 -> 66 difference empty; AC1/AC2/AC3 PASS |  | OPEN |

## Log

- 20261009T141425Z OPENED by 0.7.0_AE_CloudOps~MP with 4 leg(s)

## PRE-ACT RECORD (MP-x-4 steps 1-3, all measured BEFORE the act)

**This order's path:** `org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-x-4.control-plane-release.md`
(`<status>pending</status>`, round 5, `<risk>WORLD</risk>`, issued by `2.0.0_SA_COO~MP`, GO msg 32756).

**Release tree.** `rel-nfra-mcportal-r5-control-plane` at `C:/tmp/mp-x4-rel`, cut from the LIVE
`deployed_commit` `91811b648ab119e73e22f8d401dd09f45b8ab19b` (NFRA_OPLGTW r29), read from
`infra/aws/ec2/EC2_MANIFEST.json` at the act and NOT taken from the GO message. MP-x-1 `06bfb80b54`
cherry-picked (`cb41cf1c8f`); `mcportal_commit` set to `d60b4e0` (`d1bc9dfbe3`, one line changed,
measured 1 insertion / 1 deletion). The release branch stays local and unmerged, as every prior gateway
release branch has; this trunk branch `wk-mcportal-r5-x4` carries the ledger and the manifest RECORD,
per the r29 precedent (`91811b648a` lives only on `rel-nfra-oplgtw-r29`; its ledger and manifest landed
on the trunk at `5f1400c4a2`).

**CENSUS (the order's STOP gate).** `git diff --stat 91811b648a HEAD -- infra/aws/ec2/opal-gateway`
names EXACTLY the four files MP-x-1 carries, and nothing else:

| file | change |
|---|---|
| `app/admin_fabric.py` | new, 175 lines |
| `app/refs/fabric_boxes.json` | new, 8 lines |
| `tests/test_admin_fabric.py` | new, 279 lines |
| `app/admin_api.py` | +2 |

4 files, 464 insertions. Files changed OUTSIDE `infra/aws/ec2/opal-gateway/`: **0**. The two lines in
`admin_api.py` are the one route line `Route("/fabric/boxes", admin_fabric.boxes, methods=["GET"])` plus
its required `from . import admin_fabric` import -- the order's "one route line", not a second behavior.

**bun cache pre-check.** `ops/bun_cache_precheck.py` against d60b4e0's own lockfile (30,903 bytes,
`lockfileVersion 1`, extracted with `git show d60b4e0:bun.lock`): **77 of 77, rc=0**. No package will be
fetched, so step 1's miss-STOP does not fire.

**COLD READ on the host (R-13's 30 s bar) -- FOUR independent samples, not one.** Measured over SSM under
the instance role `arn:aws:sts::313476888478:assumed-role/opal-gateway-role/i-07dccb1615503ac99`, running
the RELEASE's `app/admin_fabric.py` (plus its new `app/refs/fabric_boxes.json`) in a scratch copy of the
live `app/` package under the host venv `/opt/opal-gateway/.venv/bin/python`. Per CLAUDE.md Rule 12 the
driver went local -> S3 -> host pull; no Python was inlined into an SSM command and nothing was written on
the VM.

| sample | cold `_compute(6)` | records scanned | skipped |
|---|---|---|---|
| 1 | 16.767 s | 3141 | 0 |
| 2 | 15.336 s | 3154 | 0 |
| 3 | 13.964 s | 3154 | 0 |
| 4 | 13.615 s | 3154 | 0 |

n=4, min 13.615, max 16.767, mean 14.921, spread 3.152 s (23.2% of min). **Worst sample is 13.233 s under
the 30 s bar -- 1.79x headroom.** Warm reads 0.765-0.839 s. All 4 roster boxes reporting (dell2 611,
dell1 598, sitez 265, laptop 111), `unrostered` empty.

**No load change was made.** The order's remedy (narrow the default window 6 -> 2 hours, or warm the body
cache at boot) fires only above 30 s. It did not fire, so `app/admin_fabric.py` is deployed EXACTLY as
MP-x-1 wrote it and no re-run of `tests/test_admin_fabric.py` is owed.

Two honest notes on this figure. (i) The issuer's 04:2xZ reading was 21.3 s with 3,004 records -- ABOVE
every sample here despite scanning FEWER records, so that figure reflects a slower moment (S3 latency or
host load), not record-count scaling; four samples at the release time are what the order says counts.
(ii) The 6-hour window does grow with daytime commit volume: at ~3,150 records the mean is 14.9 s, so on a
linear read the bar would be reached near ~6,300 records in the window. That is headroom, not a defect, and
it is the figure a future enrichment should re-measure rather than assume.

**ROLLBACK, proven before the act.** The live base's own artifact is already in S3 and was CONTENT-verified,
which is a stronger instrument than a from-scratch rebuild (a rebuilt tarball would not be byte-comparable:
tar/gzip metadata and the bun build are not bit-reproducible, so a mismatch would prove nothing):

- `s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-91811b648a.tar.gz`
- 514,461 bytes; ETag `3157ad0796dae6f9ad26dea7a1e46469`; `Metadata.git-ref` =
  `91811b648ab119e73e22f8d401dd09f45b8ab19b`, exactly the live `deployed_commit`; uploaded 2026-10-09T12:31:08Z
  by r29's own deploy.
- Downloaded and verified: local size 514,461 == S3, local md5 `3157ad0796dae6f9ad26dea7a1e46469` == the ETag.
- Contents are provably the PRE-RELEASE base: `app/admin_fabric.py` occurrences **0**,
  `app/refs/fabric_boxes.json` occurrences **0**, with positive control `app/admin_api.py` = 1 (so the
  archive is readable and the grep discriminates). Top level: `app`, `dashboard`, `deploy`,
  `identity_tool_allowlist.txt`, `requirements.txt`.

**Rollback command, per key.** Re-install the VERSIONED key, never `latest` -- this act overwrites
`opal-gateway-latest.tar.gz`, which right now is byte-identical to the base (same size, same ETag, same
git-ref) and will not be after the upload:

```
aws ssm send-command --instance-ids i-07dccb1615503ac99 --document-name AWS-RunShellScript \
  --region us-east-1 --parameters file://<params.json>   # params pull and install:
#   aws s3 cp s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-91811b648a.tar.gz \
#     /tmp/rb.tar.gz --region us-east-1
#   sudo -u ec2-user tar -xzf /tmp/rb.tar.gz -C /opt/opal-gateway
#   sudo systemctl restart opal-gateway && curl -fsS localhost:<port>/health
```

Blast radius, per the never-widen pair (CTO half R-13, COO half this issuance): the gateway's `/` bundle;
one new owner-gated route `GET /api/admin/fabric/boxes`; no `.env` key and no IAM. Terraform, the ALB, the
host, its role and its secrets are untouched; `safe-ec2-deploy.sh` is READ, never edited.

**HALT-GATE PRE-FLIGHT, measured from the release worktree (not assumed).** `halt-gate-check.sh` standalone
with `OPAL_AGENT_SERIAL=0.7.0_AE_CloudOps~MP`: **rc=0, admitted.** The GO warned that a sparse cone omitting
`org/tier2_senior/0.7.0_AE_CloudOps~MP` fails `SERIAL RESOLVES TO NO KNOWN AGENT` (rc=3). That remedy is
aimed at the wrong check for this serial: that LANE folder does not exist anywhere in the repo (0 paths under
it), yet the gate admits, because `halt_gate_validate_serial` matches the BASE by substring
(`*"$base"*`) against `org/tier*_*/*/` and this worktree carries 20 folders matching `0.7.0_AE_CloudOps`.
The second check, `lane-no-inbox`, reads the SHARED root's `org/mcp/inbox/0.7.0_AE_CloudOps/~MP`, which
exists. So the real requirement is "materialise at least one folder matching the BASE", which a no-cone
`org/` list satisfies -- not "create the lane folder", which would add a directory the tree does not have.
Nothing cited a HALTGT pass as evidence of not being halted (per /cloud-ops, a `~lane` serial is unhaltable
and no HALTGT pass is cited by anyone).

**MCP TOOL SURFACE, BEFORE.** 66 registered tool names, read on the host from the same registry the running
process builds (`app/server.py:507`, `mcp._tool_manager.list_tools()`), via the S3 -> host path, printing
names and the count only and never an env value (52 env keys loaded by name). `tool_count = 66`, rc=0,
MainPID 857046. This matches r28's recorded `tools 66 -> 66` baseline. The after-count and the name
difference are L4's proof.

**World state immediately before the act:** `app/admin_fabric.py` ABSENT from `/opt/opal-gateway/app`
(confirmed on three separate SSM runs), service `active`, MainPID 857046 unchanged across every pre-act
read, live tree mtime 1791513383 unchanged. Nothing has been deployed, uploaded or restarted by this cell.

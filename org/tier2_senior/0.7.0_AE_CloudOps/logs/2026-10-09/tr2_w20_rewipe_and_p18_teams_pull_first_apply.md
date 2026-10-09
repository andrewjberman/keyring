# The Teams silver re-wipe, then the Teams pull's first apply — 0.7.0_AE_CloudOps~TR2

**Date:** 2026-10-09
**Task Order:** NFRA_TRNSPT.TO-RUN-w20 and NFRA_TRNSPT.TO-APPLY-p18
**Status:** COMPLETE

**archetype:** DEPLOY

## Objective

Two orders from `2.0.0_SA_COO~T2`, each under its own never-widen pair, in the order the GO named: re-wipe
the 30 existing Teams silver keys in place (TR-w-20), then make the FIRST apply of the Teams meeting pull
(TR-s-18) and prove the hop with one seat invoke. Counts, keys and version ids only; no transcript text,
no token.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `to-check.py` | `--all --assignee 0.7.0_AE_CloudOps~TR2` | `total=1 scanned=5220` at start, `total=0 scanned=5243` at close — the lane's own denominator, not the folder-keyed pending list |
| `comp-find` | `--files 'genre"?\s*:\s*"DEPLOY' .../deliverables --limit 30` | 25 hits / 801 files, bands HEAD=3 CONFIG=22 — found the analogous DEPLOY proof instance to build both instances from |
| `comp-find` | `--files 'meeting_allowlist' data/transcripts` | 7 hits / 169 files; the allowlist is a `.py` loader plus its JSON, not the path the preflight implied |
| `deploy_ledger.py` | `open` / `close-leg` / `close` on two slugs | 4 legs and 5 legs, each closed on its own measured proof, both CLOSED; the tool commits its own files at open |
| `proof-of-spec-check.py` | both instances, `AC1 --governing-order <order>` | both VALID (rc=0); w20 4/4 controls discriminate, p18 5/5 |
| `safe-apply.sh` | `-chdir=<extract>/infra/aws/terraform/transcripts apply <plan>` | rc=0, 9 added |
| `safe-commit.sh` | 6 commits under this lane's author line | all passed the gates; `msg-verify MATCH` on each |
| `surprise-row-gate` | at commit, twice | `1 new row of 66` then `1 new row of 67`, both OK |

**What worked:** `to-check.py --all --assignee` is the only read that answered "what does this LANE hold" —
`get_agent_status`'s pending list is BASE-scoped and showed 11 orders, none of them mine (rule 22a). The
deploy ledger's per-leg close forced each proof to be measured before the next act.

**What failed:** `comp-find` denied a plain `grep` twice and a `| head` once; the REMAINDER line made each
re-run one edit. `aws kms get-key-policy` refuses an alias and `--output text` appends a tab plus the
PolicyName, so the JSON needs trimming at the last `}` before it parses.

**Gap found:** none new.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | w20: clean extract at pin `776d830071`, tool blob resolved by CONTENT | `cd3bf1f39c` == `4eb7ed184c:rewipe_silver.py` |
| 2 | w20 step 0: live re-list vs `R20_REWIPE_PRIOR_VERSIONS.json` | denominator 30, `equal_to_prior=30 differ=0` — no STOP |
| 3 | w20 AC1 dry-run | `keys=30 rows=8873 written=0 failed=0` |
| 4 | w20 `--apply` | `keys=30 rows=8873 written=30 failed=0`, held_out 2271 |
| 5 | w20 step 2: re-list + dry-run AFTER | 30 of 30 NEW VersionIds; per-key rows before==after, 0 mismatches of 30 |
| 6 | p18: clean extract at pin `634da92d06` (carries `a9039b8d62`, `488c840f48`) | negative control: HEAD is not an ancestor of `a9039b8d62` |
| 7 | p18 `build.sh` | `transcripts-pull.zip` 876521 bytes, 88 files, sha256 `b5a15b1930...`, b64 `taFbGTCU...` |
| 8 | p18 step 1 (no write) | S04 `200 count=20`; S05 expiry ABSENT + EXERCISED `403` vs `401` control; KMS CreateGrant held |
| 9 | p18 targeted `terraform plan` | `Plan: 9 to add, 0 to change, 0 to destroy` |
| 10 | p18 `safe-apply.sh` | `Apply complete! Resources: 9 added, 0 changed, 0 destroyed.` |
| 11 | p18 0-diff re-plan | `No changes. Your infrastructure matches the configuration.` |
| 12 | p18 one seat invoke | `200`, no FunctionError, `listed=0 new=0 held=0 expired=0 refused=4` |

## Verification

```
# w20 -- post-run re-list (live list_object_versions IsLatest, 3 pages)
DENOMINATOR live_keys_scanned=30 (3 series, 3 list pages) prior_json_total=30
KEYSET only_live=0 only_prior=0 intersect=30
VERSIONS equal_to_prior=0 differ_from_prior=30
DENOMINATOR before_keys=30 after_keys=30 written_keys=30
ROWCOUNT per-key mismatches=0 of 30
rows_total before=8873 after=8873  held_out_total=2271

# w20 -- negative arm: research_meeting untouched
DENOMINATOR research_meeting current parquet keys=29 (pages=1)
LastModified range (UTC): 2026-10-09T06:10:55Z .. 2026-10-09T06:10:58Z
keys with LastModified at/after 2026-10-09T10:00:00Z (this session's window): 0

# p18 -- the shared-package hazard, before and after the apply
["outlook-global-transcripts-pull-lambda","VGIq85Xxm5KVLCnv16BASS63RsPMHScMEwZJP5SuMNY=","2026-10-07T23:59:05.000+0000","Active"]
["outlook-global-transcripts-pull-lambda","VGIq85Xxm5KVLCnv16BASS63RsPMHScMEwZJP5SuMNY=","2026-10-07T23:59:05.000+0000","Active"]

# p18 -- deployed bytes vs the BUILD INPUT (22a CODE layer)
live CodeSha256  taFbGTCUAOhM+97EVJi3AfqqeBCV+FIUSLZ8Z4Ge6HA=
built zip b64    taFbGTCUAOhM+97EVJi3AfqqeBCV+FIUSLZ8Z4Ge6HA=

# p18 -- AC1 and the schedule
"Active"
["teams-global-transcripts-pull-hourly","cron(0 13-22 ? * MON-FRI *)","ENABLED"]

# p18 -- the bearer, exercised with its control
S05-EXERCISED status=403 error=meeting_not_allowed route=list
CONTROL-OK   status=401 error=unauthorized (the route discriminates on the bearer)
DENOMINATOR headless-route probe: 4 of 4 allowlisted series -- allowed=0 refused_403=4 other=0
```

## Decisions Made

1. **S05's expiry is ABSENT, so it was EXERCISED instead.** `gateway/transcripts/bearer` is a 64-byte
   opaque shared bearer: no JWT `exp`, and Secrets Manager carries no `RotationEnabled` or
   `NextRotationDate` (7 metadata keys printed). An absence is not an exercise (rule 22a), so the stored
   bearer was used once against the route, read-only, with a wrong-bearer negative control beside it.
2. **The KMS half was proved by reading policy, never by simulating.** The key policy delegates
   `kms:Create*` to account root, so the identity half decides; `cloudops-dell-agent-respol-allow-policy`
   allows `kms:CreateGrant` over a denominator of 11 identity documents. `simulate-principal-policy` is
   recorded as excluded, not dressed up as a control.
3. **`readers.tf`'s root variable was passed as a LIVE-MEASURED value, not a typed guess.**
   `second_reader_trust_principal_arns` has no default by design, and the plan refuses without it. The
   value came from reading the already-applied role's trust policy (`user/Opal_Terminal`). `readers.tf` is
   not in the `-target` list, so nothing of it is in the plan.
4. **The ledger was built before the zip's sha256 existed, so the zip was built first.** The order's step 0
   wants the ledger to name the built zip's sha256 while step 2 does the building; building first (a local,
   reversible act from the pin) satisfies both without widening anything.
5. **The apply proceeded over the 403 finding.** The order's STOP conditions are S04, S05 and KMS, and all
   three read MET. The headless route's refusal is a different surface with a different owner, so it became
   a row and the act continued, per section 2.

## Files Modified

| path | commit |
|---|---|
| `.../deliverables/NFRA_TRNSPT.TO-RUN-w20_result.json` + `NFRA_TRNSPT_TR2/` (4 evidence JSONs) | `f012dd44d8` |
| `.../deliverables/NFRA_TRNSPT.TO-RUN-w20...proof_of_spec.json` | `5fb0ac445d` |
| `org/critical_paths/` w20 ledger open / close | `76c6261f05`, `9826ca7e95` |
| `.../surprise-channel/investigations/INVESTIGATION_v1.md` row D2-S11 | `fb94b3075c` |
| `.../deliverables/NFRA_TRNSPT.TO-APPLY-p18_result.json`, row D2-S12, p18 ledger close | `8d87f6a93f` |
| `.../deliverables/NFRA_TRNSPT.TO-APPLY-p18...proof_of_spec.json` | `e06afe7f45` |

## Blockers

None for this lane. Two rows carry what this seat found and cannot fix:

- **`NFRA_TRNSPT-D2-S11`** (BLOCKING, INERT) — the headless `/hx/transcripts` route admits none of the 4
  allowlisted meetings, so FWD-2's first-landing arm is unreachable until the gateway HOST's allowlist is
  widened. Owner: NFRA_OPLGTW's surface, routed to `2.0.0_SA_COO~T2` in the p18 report.
- **`NFRA_TRNSPT-D2-S12`** (OBSERVATION, INERT) — deployment rules 4 and 6 are unmet for the transcripts
  root: 0 of 232 `lambda-source-map.json` entries name a transcripts Lambda, and 0 `transcripts-v*` tags
  exist. Both targets are outside this order's `<paths>`.

## Current State

Both orders are terminal and reported; `to-check --all --assignee` reads `total=0` over a scanned
denominator of 5243, so the issuer has flipped both. Registered LIVE as `0.7.0_AE_CloudOps~TR2`, one inbox
watcher (census exactly 1 row, pid 34008), inbox drained and every message acked (3136, 3156, 3171). Both
deploy ledgers CLOSED with no sentinel. Zero crons armed. The clean-extract worktrees are removed; the two
pins reproduce them in one command each.

Live state this session put in the world: 30 Teams silver keys rewritten in place on new VersionIds with
their row counts preserved, and nine new resources under `pull.tf` — an hourly writer of
`teams/transcripts/*` under its own principal, enabled on `cron(0 13-22 ? * MON-FRI *)`.

## Next Steps

1. `[2.0.0_SA_COO~T2]` Reads the two rows at the round's drain. D2-S11 decides whether FWD-2's acceptance
   waits on the gateway host's allowlist or is re-cut; D2-S12 needs a cell for the source-map entries and a
   decision on the root's first tag.
2. `[2.0.0_SA_COO~T2]` Owns the w20 post-run residual sweep and its planted positive control (CTO half
   condition 2). This seat made no absence-of-residual claim.
3. `[0.7.0_AE_CloudOps~TR2]` Event-driven hold: act on the next `[INBOX]` event the same turn, and re-arm
   the Monitor on each `[WATCHER-EXPIRED]` line in one call, same turn, no skill load.

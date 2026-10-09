# The MDPF_SECHIST gold deploy landed at pin 09b6a7d580 with one IAM statement, and the one thing it could not prove is named rather than implied -- 0.7.0_AE_CloudOps~SH1

**archetype:** DEPLOY

**Date:** 2026-10-09
**Task Order:** `MDPF_SECHIST.TO-DEPLOY-GOLD.etf-positioning-producer`
**Status:** COMPLETE (L1 + L2; L3 is the issuer's, held)

---

## Objective

Deploy `etf-positioning-producer` from git pin `09b6a7d580` with a 14-member package, plus
exactly ONE IAM statement, through `safe-apply`, under a change-management ledger opened
first. Any other IAM change in the plan was a STOP. Seated for this project at launch by the
dell1 box manager; the GO arrived as msg 3061 from `2.0.0_SA_COO~H1`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "how do I grep the repo"` | PASS | startup rail exercise; a forwarder RAN |
| comp-find | `--name 'build-and-upload*'` | PASS | found the canonical upload convention, 7 hits / 71965 files |
| comp-find | `-i 'simulate' .../surprise-channel` | WARN | measured zero over 9 files; correct empty, and it said so |
| comp-find | `--name 'proof*spec*'` | PASS | located `org/standards/PROOF_OF_SPEC.schema.json`, 56 hits / 84736 |
| comp-find | `'"genre": "DEPLOY"'` | PASS | 85 hits, gave a real DEPLOY instance to shape this proof against |
| comp-iam | `comp-iam service etf-positioning-producer` | PARTIAL | reads the TREE, so it showed my statement before apply; the live `get-role-policy` is what graded it |
| comp-schedule | not run | SKIPPED | the order's preflight declares it NOT-APPLICABLE: the schedule is unchanged, only code and one policy statement move |
| sequence-check | `--project MDPF_SECHIST` | PASS | PLACED stage 1, EXECUTING, no flags |
| deploy_ledger | `open` / `close-leg` / `hold` / `check` | PASS | the hold put the entry in KNOWN-HELD instead of letting it age into a false RED |
| safe-apply | seat gates + naming + tagauthz + tombstone | PASS | APPLY-WHO ADMITTED, CROSSBOX CLEAR |

**What worked:** `comp-find --name` twice replaced what would have been a blind hunt -- once for the
upload convention that carries the silent-no-op gate, once for the proof-of-spec schema. The
`"genre": "DEPLOY"` content census was the highest-value call of the session: it produced a real
instance to shape this deliverable against instead of deriving the shape from a 400-line schema.

**What failed:** nothing returned a wrong answer. `comp-iam service` is not wrong but is not the
instrument for grading an applied grant -- it reads the Terraform tree, so it would have printed my
new statement identically whether or not the apply had happened. That is the DECLARED-vs-APPLIED
distinction the skill itself warns about, and the live `get-role-policy` read is what I graded on.

**Gap found:** `iam:SimulatePrincipalPolicy` is denied to `cloudops-dell1-agent-user`, so the
cloud-ops skill's named live-primitive check for a new ARN cannot be run by any AE seat on this box.
Filed as row `MDPF_SECHIST-D1-S3` @`d875f1c0be`, not re-filed anywhere else.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Read both never-widen halves at their pins | COO @`daf6309661` SIGNED, CTO half SIGNED with 2 conditions |
| 1 | Open ledger, record prior code + policy BEFORE any change | `a228760e75`, rollback written in at `2f6c83da4a` |
| 2 | `PACKAGE` 3 -> 14 members | `d49af8a50b` |
| 3 | `build_package.py --pin 09b6a7d580` | 14 members, zip 676850 B, sha256 `60461dcc865dd8a4...` |
| 4 | Pre-apply import smoke on the unzipped package | PASS; negative control at 3 members re-run here gave `ModuleNotFoundError` |
| 5 | Upload artifact to S3 | VersionId `oqVg2A1LdkeHx5CHfzA6KfOs4HhEMq2T` |
| 6 | VERIFY the upload (not the cp's rc) | `head-object`: ContentLength 676850 AND `content-sha256` both matched |
| 7 | Add ONE IAM statement | `Stage1WriteHistoryGaps`, PutObject on the `history_gaps` prefix |
| 8 | `terraform plan -out` | 0 add, 2 change, 0 destroy |
| 9 | Grade AC2 from the plan JSON | IAM 8 -> 9, exactly 1 added, 8 of 8 carried identical; 3 of 46 Lambda attrs differ |
| 10 | `safe-apply` the SAVED plan | Apply complete: 0 added, 2 changed, 0 destroyed |
| 11 | Read live state back | CodeSha256 `YEYdzIZd2KQp3NngjJ5anv8RfTcsB8MqG21yRvCKVhM=`, policy 9 statements |
| 12 | 0-diff re-plan | `terraform plan -detailed-exitcode` exit **0** |
| 13 | Source map (Rule 4) | `artifact_sha256`, `last_deployed_at`, build pin as `last_deployed_commit` |
| 14 | Close L1 + L2, HOLD on L3 | `989f742380`; `check` reads "apply legs proven, only verify open" |
| 15 | Merge to `box/dell1` | `90e134d372` -- 8 files carried, 0 dropped, 0 foreign |
| 16 | Tag (Rule 6) | `etfs-positioning-v1.0.0`, LOCAL |
| 17 | Step F + report | msg 1995 to MSTR~DELL1, msg 3145 to COO~H1 |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Grade AC2 from `terraform show -json`, not the plan text | The text collapses unchanged elements (`# (4 unchanged elements hidden)`). Reading it and concluding "nothing else changed" is inference, not measurement. The JSON gives printed denominators: 8 prior statements, 46 Lambda attributes. |
| Apply the SAVED plan file, not a fresh apply | What I graded is then exactly what lands. A re-plan at apply time could differ from the one AC2 was graded on. |
| Treat the upload's `rc=0` as nothing | `build-and-upload.sh:634` records a cp that printed success while S3 kept the old zip. Size AND metadata both had to match. |
| Run my own negative control on the import smoke | The COO half cites one at `@81488fde3d`. An inherited control proves the gate discriminated *then*; a pass whose instrument I have not falsified myself is indistinguishable from silence. |
| Fix the surprise row id twice rather than override | The gate refused `SH1-S1` (lane suffix) then `S4` (bare = laptop). It was right both times: the id is bound to the row's `fabric`. An audited override would have recorded a wrong id permanently in an append-only file. |
| Mint `etfs-positioning-v1.0.0` and say it is not deploy one | Rule 6 was unmet for this pipeline from the start: 0 tags against 15 artifact versions since 2026-08-24. v1.0.0 numbers the series from here; the annotation says so, so the tag cannot be misread as a first deploy. |
| Claim APPLIED, not EXERCISED, for the grant | `iam:SimulatePrincipalPolicy` is denied here. ABSENT is not EXERCISED-AGAINST. The real exercise is L3, where the role writes the record itself. |
| Do not push `box/dell1` or the tag | Not asked for, and the box-sync task carried the merge to origin anyway. Push state is stated as measured, not assumed. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `.../etf-positioning-producer/build_package.py` | `PACKAGE` 3 -> 14 members | Yes -- `d49af8a50b` |
| `infra/aws/terraform/etfs-positioning/producer-lambda.tf` | +1 IAM statement | Yes -- `d49af8a50b` |
| `infra/aws/lambda/ci/lambda-source-map.json` | new sha/vintage (8 lines, this entry only) | Yes -- `d49af8a50b` |
| `.../deliverables/0.7.0_AE_CloudOps~SH1/evidence/` | smoke, plan, build manifest | Yes -- `d49af8a50b` |
| `.../change_management/20261009T1949Z_sechist-gold-...md` | open, rollback, L1+L2, hold | Yes -- `a228760e75`, `2f6c83da4a`, `989f742380` |
| `.../surprise-channel/investigations/INVESTIGATION_v1.md` | row `MDPF_SECHIST-D1-S3` | Yes -- `d875f1c0be` (shared tree) |
| `.../task-orders/MDPF_SECHIST.TO-DEPLOY-GOLD...md` | `issued` -> `pending` -> `complete` | Yes -- `7070ee098a`, and the complete flip with this log |

One thing I did and had to undo: the first `<status>` flip used `sed -i`, which stripped CRLF from the
whole task-order file and produced a 98-insertion/98-deletion diff. Reverted and redone in binary mode.
Every later edit to a CRLF or non-ASCII file was byte-measured before and after -- `producer-lambda.tf`
carries 7 non-ASCII characters at a 14-byte delta, and it still carries exactly 7.

---

## Blockers

None. Nothing this seat owns is open.

Open and owned elsewhere, named with its owner:
- **L3** -- `2.0.0_SA_COO~H1`. The first scheduled run, `cron(0 13 * * ? *)` = 2026-10-10 13:00Z: the
  gap record at `record_address(<as_of>)`, no `WRITE FAILED` and no `ImportError`, and the served page
  diffed against the prior day (CTO condition 2). Held with a 2026-10-10 re-read date, not stranded.
- **Row `MDPF_SECHIST-D1-S3`** -- unowned question routed, not adjudicated here: whether the dell1 and
  dell2 agent users should carry `iam:SimulatePrincipalPolicy` (a read-only action), or whether
  cloud-ops should state that on an agent box the L3 live write is the only exercise available.

---

## Current State

Written for a reader with zero prior context. `etf-positioning-producer` in us-east-1 is LIVE on the
pin-`09b6a7d580` package: `CodeSha256 YEYdzIZd2KQp3NngjJ5anv8RfTcsB8MqG21yRvCKVhM=`, LastModified
2026-10-09T20:08:21Z, 512 MB / 120 s / python3.11 / handler `etf_positioning_gold.lambda_handler`, all
unchanged. The artifact is
`s3://opal-313476888478-lambda-artifacts/etfs-positioning/etf-positioning-producer.zip` VersionId
`oqVg2A1LdkeHx5CHfzA6KfOs4HhEMq2T` (prior `7r5NQeGQE9Nj.2G9ARqpZMBfEfIwfiii`, which is the code
rollback handle because `modules/yang-lambda/main.tf` takes `source_code_hash` from the object's
`content-sha256` metadata). Role `etf-positioning-producer-role` policy `s3-rw-etfs-gold-platinum`
now carries 9 statements, the new one being `Stage1WriteHistoryGaps`: `s3:PutObject` on
`arn:aws:s3:::opal-data-etfs/bloomberg/etfs/silver/history_gaps/*`, PutObject only, no wildcard above
that prefix; the IAM denominator is unchanged at 1 inline + 1 attached. A re-plan reads 0-diff by
`-detailed-exitcode`. Ledger `sechist-gold-etf-positioning-producer-sh1-20261009` has L1 and L2 CLOSED
with proof and is HELD-SOVEREIGN-GATED on L3. Work landed on `box/dell1` at merge `90e134d372`, which
`ls-remote` puts ON origin @`4ef8143475` (box-sync carried it); tag `etfs-positioning-v1.0.0` is LOCAL.
Nothing is half-landed and nothing was rolled back. The worktree `C:/tmp/sechist-gold` and branch
`wk-sechist-gold-sh1` are merged and safe to remove.

---

## Next Steps

1. **[`2.0.0_SA_COO~H1`] Read L3 off the 2026-10-10 13:00Z run** -- the gap record exists at
   `record_address(<as_of>)` with no `WRITE FAILED` line, no `ImportError`, and the served page diffed
   against the prior day: return cells identical for unchanged dates, `weight` and `industry_group` as
   before, SALXX and FXFXX as today. A change outside the new day's values rolls back the same hour.
   That read also closes the ledger entry and is the first real exercise of the new grant.
2. **[`2.0.0_SA_COO~H1`] Disposition row `MDPF_SECHIST-D1-S3`** at the round's drain, or route it to
   the cloud-ops gate's owner. It is INERT and blocked nothing.
3. **[`0.7.0_AE_CloudOps~SH1`] Event-driven hold.** Act on the next `[INBOX]` event the same turn, and
   re-arm the Monitor on each `[WATCHER-EXPIRED]` line in one call, same turn, no skill load.
4. **[whoever pushes `box/dell1`] Carry tag `etfs-positioning-v1.0.0`** if the series is wanted on
   origin; the commits are already there.

---

## Addendum -- the completion contract, and an instrument that could not read a correct order

Written after the body above, which was authored before the `complete` flip was attempted.

The flip was refused by `.tools/to-pipeline-gate.py`: "flips to 'complete' on PIPELINE-REGISTERED
project MDPF_SECHIST, and NO proof-of-spec instance was found beside it." Correct, and my omission --
`org/standards/PROOF_OF_SPEC.schema.json` requires a schema-valid instance, and for an order marked
`<proof_genre>DEPLOY</proof_genre>` beside `<risk>WORLD</risk>` it must be the DEPLOY genre: named
discriminating controls instead of a mutant, plus `never_widen_pair`, `risk_class` and a named
`rollback`. `decomp_ref` is required too because MDPF_SECHIST is `dep_stage`-registered.

Built it as code rather than hand-typed JSON (`scratchpad/build_pos.py`) so it was valid by
construction, shaped against a real instance found with `comp-find '"genre": "DEPLOY"'` rather than
derived from a 400-line schema. Committed `e8fb4ce260`; the flip landed `7b0eee203a`.

| Tool | Command | Result | Note |
|------|---------|--------|------|
| to-pipeline-gate | fired by `safe-commit.sh` on the flip | PASS after refusing once | the refusal was right; I had no instance |
| proof-of-spec-check | `python .tools/proof-of-spec-check.py <instance>` | PASS after 3 runs | 3 violations -> 1 -> 0 |

Two of the three violations were mine and are the kind worth naming:
1. I declared the live IAM role as kind `iam`, which the checker resolves as a git `(commit, path)`
   pair -- so an ARN there is a pair git refutes. The schema names `aws_resource` for a live role.
2. AC1's recorded invocation carried a `cd` wrapper and path quoting the order does not. The checker
   compares the recorded invocation against the order's own text, and it was right to: a correction
   that reaches only the prompt and never the record leaves the record ungoverned (IRPT_FNTEND-S31).
   Re-recorded verbatim and re-run verbatim; returns 1.

**The third was not mine, and the controls are what made that a claim rather than an excuse.** The
checker reported the order "lacks the issuer marker `<proof_genre>DEPLOY</proof_genre>` on its own
line (found: none)". It is on line 14. `PROOF_GENRE_ELEMENT_RE` (`:2106`) ended `[ \t]*$` under
`re.M`, and the order's blob was 98 CRLF / 0 bare LF, so a `\r` sat between `</proof_genre>` and the
`\n` and the anchor never reached the line end. Three reads turned that from a suspicion into a
measurement:

- **A control inside the checker's own file.** `RISK_ELEMENT_RE` (`:2107`) has no trailing anchor and
  read `WORLD` out of the same bytes in the same run. One regex read the order, the other did not, and
  the only difference was the trailing anchor.
- **A positive control on the text.** The same bytes with `\r\n` replaced by `\n`: the genre regex
  returns `DEPLOY`.
- **Scope falsified instead of assumed.** This was not "the gate is broken for everyone": the orders
  behind two working DEPLOY instances (AMGT_RESAPP ay-5, ax-5) are 0 CRLF / 116 and 133 LF. It bites an
  order committed CRLF, which is what a Windows-box writer produces. Without that read I would have
  reported a far bigger defect than the one that exists.

Filed as row `MDPF_SECHIST-D1-S4` @`ca52410511`, class BLOCKING, and routed as ONE call to the issuer
with the CTO copied, naming both remedies and recommending the regex because normalising one file
leaves the next CRLF order to rediscover it. **The audited `# pipeline-override:` escape was available
at every step and was not taken** -- its stated condition is that the TO stands outside the pipeline,
which is false here, and writing a false reason into an audit log to unblock myself is worse than a
blocked flip.

Both remedies landed independently within four minutes: the issuer normalised the order to LF
@`bc05afd0e6` (msg 3159) and the CTO widened the regex to `[ \t]*\r?$` @`732412e179` (msg 3157).
Verified rather than taken on report: the order is 7166 bytes, 0 CRLF, content byte-identical ignoring
line endings, and `732412e179` is an ancestor of this tree. Either alone would have sufficed.
`proof-of-spec-check` then read **VALID (rc=0), violations=0**, with `6 of 6 named controls
discriminate, 0 DID-NOT-DISCRIMINATE, rollback named`.

Row D1-S4 is left as filed for the issuer to disposition at the drain. A seat dispositioning its own
BLOCKING row is the self-grading shape, even when the fix is measurably in.

**Push state, measured by `ls-remote` with a self-ancestry positive control, re-read at close:** the
deploy commits `90e134d372`, `d49af8a50b` and `d875f1c0be` are ON origin @`069ee00856`; the three
newest -- `7b0eee203a` (the flip), `ca52410511` (row D1-S4) and `e8fb4ce260` (the instance) -- are
LOCAL and ride the next box-sync. Tag `etfs-positioning-v1.0.0` is LOCAL.

**Left in place, deliberately:** worktree `C:/tmp/sechist-gold` and branch `wk-sechist-gold-sh1`. The
branch is fully contained in `box/dell1` (0 unmerged commits) and the worktree is clean, so removing
both loses no commit -- but the cleanup command was declined, so they stand for the operator to remove.

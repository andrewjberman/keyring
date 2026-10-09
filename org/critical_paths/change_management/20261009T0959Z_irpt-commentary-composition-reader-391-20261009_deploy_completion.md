# Deploy Completion Record
**Date opened:** 2026-10-09T09:59:17.977508+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-pr-397: the NEW irpt-commentary-composition-read-lambda (IB-pr-391 / IB-pr-386, the svc-commentary composition read). PIN STATED (ccbe8b8be1): release pin 9c995243f7c41d0850024a451b71a4536d6dd91e, packet blob 531de9a9e7. BUILT SHA256: ZZmWOFSA/GjO0d/cKHSm9G5+xDc5sNfEHOpbmfIabQ0= (136840 B, 16 members, 8 packaged .py, built twice byte-identical). UPLOADED VERSION ID: WJUEl6GlBO0afWMbQ_73o85gemQfiAqs (first mint of a new key; live_before ABSENT, no prior CodeSha256 and no prior object version). AMENDMENT 2 @1c21da0b7b (CTO msg 2952, ADDENDUM 14.1): real map, no override, BAU_PARITY_SKIP=1 scoped to the one build invocation, parity_skip and symbol_closure recorded. COO half @feeee0be4d, CTO half @a946f8b829 conditions 1-4. Rollback is ABSENCE: there is no prior version to restore.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-apply reads at the release pin before the ledger opened | the function and the S3 key are both ABSENT live; the drafted source-map entry is registered byte-identically; the built sha256 equals the packet twice over under the scoped parity skip; symbol_closure on the built zip reads missing=0 with a discriminating control; the 8 replay arms match the packet arm for arm; the four live repository.py copies still carry the packet two recorded versions | ALL SIX PRE-APPLY READS PASS, measured by 0.7.0_AE_CloudOps~IB2 in a clean worktree /c/dev/wk-397b at the release pin 9c995243f7 (porcelain 0 before the registration, and only the source map after it). (a) live_before ABSENT, both halves: get-function-configuration on irpt-commentary-composition-read-lambda returns ResourceNotFoundException and head-object on investor-reporting/irpt-commentary-composition-read-lambda.zip returns 404, read again immediately before the upload. There is no prior CodeSha256 and no prior object version, so ROLLBACK IS ABSENCE. (b) THE ENTRY IS REGISTERED BYTE-IDENTICALLY: the drafted entry IB97-4_source_map_entry.json (blob 024b3bea) was registered into the REAL map with NO BAU_SOURCE_MAP_OVERRIDE -- 16 files[], 12 staged_from, source_dir the shared reports/ package -- as a pure addition of 102 lines with 0 removed and every other function row verified byte-identical, and the entry in this worktree is byte-identical to the one already drained to box/dell2 at 111512c4e3. (c) BUILT SHA EQUALS THE PACKET, TWICE: ZZmWOFSA/GjO0d/cKHSm9G5+xDc5sNfEHOpbmfIabQ0=, 136K, import-closure OK at 8 packaged .py files, under AMENDMENT 2s path -- real map, no override, BAU_PARITY_SKIP=1 SCOPED TO THE ONE BUILD INVOCATION and passed on the command line, never exported. WHY THE PIN AND NOT HEAD: two of the four UNPINNED members come from source_dir and MOVED after the pin (repository.py 4931e2f37a -> 3b81ada6a2, retention.py 5a5e39c296 -> e7e9613a95), so a build at HEAD would not be the signed artifact; measured, not assumed. (d) SYMBOL CLOSURE ON THE BUILT ZIP (AMENDMENT 2): modules=7 pairs=28 missing=0 optional_fallbacks=0, symbol_closure PASS. ITS CONTROL DISCRIMINATES, and the first control I tried did NOT: deleting composition.py entirely still printed PASS with the pair count falling 28 -> 19, because the tool only grades pairs whose module is packaged, so a removed module is silently unchecked rather than MISSING; the control that fires is the release-4 defect shape -- keep composition.py and delete one imported binding (build_retained_repositories), which yields MISSING commentary_composition.py:179 ... missing=1 and symbol_closure FAIL. The discriminating signal is therefore the PAIR COUNT beside the verdict, never the verdict alone. (e) THE 8 REPLAY ARMS MATCH, re-run BEFORE this ledger (CTO condition 2): 8 of 8 arms equal the packets IB97-4_release_replay.json on name, verdict and negative_control flag, 3 negative controls, none outside identical/expected-diff. The files are not byte-identical and the whole difference is ONE leaf, /arms[4]/detail, where the packet redacted the scratch directory to <scratch> and this run carries the literal temp path inside the controls ImportError text; the control still fires on ImportError SERVICE_READERS with counts {FAIL: 1}. (f) THE LIVE SIDE OF THE REPLAY IS STILL THE PACKETS: the four live repository.py copies read f255335beb26 (performance-adapter, status) and f01fcf549e8e (ycharts-generate, export-render), exactly the two versions the packet records, so this seat IB-pr-395 release earlier today did NOT move repository.py and the arms describe the live world as signed. | CLOSED 20261009T095959Z |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts investor-reporting/irpt-commentary-composition-read-lambda.zip | first mint: head-object content-sha256 equals the built sha256 and the returned version id is recorded in this ledger | FIRST MINT UPLOADED and verified independently of the uploader. build-and-upload.sh investor-reporting irpt-commentary-composition-read-lambda (no BUILD_ONLY) run from the clean release-pin worktree with TMPDIR outside every worktree, at the REAL source map with no override and with BAU_PARITY_SKIP=1 scoped to that one invocation; the run printed ZZmWOFSA/GjO0d/cKHSm9G5+xDc5sNfEHOpbmfIabQ0= and its own write-verify line (size=136840, sha256 metadata match). The key was read ABSENT (404) immediately before, so this is a first mint and not an overwrite. Read back with s3api head-object as a SECOND instrument: version WJUEl6GlBO0afWMbQ_73o85gemQfiAqs, 136840 bytes (the packets 136,840), content-sha256 ZZmWOFSA/GjO0d/cKHSm9G5+xDc5sNfEHOpbmfIabQ0= -- EQUAL to the built value. There is no prior version to retain: Branch B for this artifact is removal of this one version, and an S3 delete is a human-confirmation act (CLAUDE.md), so the documented rollback is to delete the function through Terraform and leave the object inert. Nothing was applied by this leg: the function is still ABSENT live. | CLOSED 20261009T095959Z |
| L3 | activation | infra/aws/terraform/investor-reporting/export commentary_composition.tf via .tools/safe-apply.sh | the plan reads ONLY the listed adds (the function, its role, its read-only policy, the log group and the invoke policy), every name is name() output, and nothing else; after it the live CodeSha256 equals the built value and a re-plan is 0-diff on those resources |  | OPEN |
| L4 | verify | the after-read invoke and the criterion | ONE invoke as 2.0.0_SA_COO~T2 role holding only lambda:InvokeFunction, counts and stage only and never composition content, or WAITING_ON_T2_ATTACH recorded if the attachment is not yet live; IB102-1-AC1 PASS |  | OPEN |
| irpt-commentary-composition-read-lambda | tf-lambda | module.irpt_commentary_composition_read.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T095917Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261009T095959Z LEG L1 closed: ALL SIX PRE-APPLY READS PASS, measured by 0.7.0_AE_CloudOps~IB2 in a clean worktree /c/dev/wk-397b at the release pin 9c
- 20261009T095959Z LEG L2 closed: FIRST MINT UPLOADED and verified independently of the uploader. build-and-upload.sh investor-reporting irpt-commentary-c

## STOP NOTE (2026-10-09 ~10:0xZ, 0.7.0_AE_CloudOps~IB2) -- the apply did NOT run; the signed export-root plan cannot succeed

**State, stated plainly: NOTHING IS APPLIED.** `irpt-commentary-composition-read-lambda` reads
`ResourceNotFoundException` live, no Terraform apply was invoked, and no resource was created. The only world change
this ledger carries is leg L2's S3 object -- a first mint at version `WJUEl6GlBO0afWMbQ_73o85gemQfiAqs`, inert while
no function references it. L1 and L2 are closed with proof; **L3, L4 and the tf-lambda leg stay OPEN, so this entry
stays RED and will blare past its 4h window.** That is the correct signal and it is not to be closed by a proof that
the apply landed, because it did not. `hold` was attempted and REFUSED for exactly this reason ("a half-landed deploy
cannot be HELD"), which is the tool behaving correctly.

**Why the apply was refused at the plan, before anything irreversible.** The plan reads
`Plan: 6 to add, 0 to change, 0 to destroy` -- no change and no destroy, so nothing of another release rides along --
but TWO of the six adds declare the SAME CloudWatch log group:

| resource | declared name |
|---|---|
| `aws_cloudwatch_log_group.commentary_composition_read` (`export/commentary_composition.tf:87`, `local.ccr_log_group`) | `/aws/lambda/irpt-commentary-composition-read-lambda` |
| `module.irpt_commentary_composition_read.aws_cloudwatch_log_group.lambda` (`modules/yang-lambda/main.tf:76-77`, `/aws/lambda/${var.function_name}`) | `/aws/lambda/irpt-commentary-composition-read-lambda` |

The two name lines are at plan lines 49 and 267 and are character-identical; a `sort -u` over the plan hides this,
which is how it reads as a clean six-add plan. The log group **does not exist yet**
(`logs describe-log-groups --log-group-name-prefix /aws/lambda/irpt-commentary-composition-read-lambda` returns
nothing), so neither resource can adopt an existing group: Terraform would create one and the other would fail
`ResourceAlreadyExistsException`, landing part of the signed set and stranding the rest -- a half-landed deploy, which
NEVER-2 forbids and which this seat will not start.

**This is a departure from the pipeline's own pattern, not a judgement call.** All eight existing
`investor-reporting` Lambda roots -- `reporting-read`, `directory`, `export`, `performance`, `ops`, `ycharts`,
`holdings`, `narrative` -- declare ZERO log-group resources of their own and let the `yang-lambda` module own the
group. `commentary_composition.tf` is the only one that adds a second, and `yang-lambda` exposes no switch to suppress
its own (`log_retention_days` is the only related variable; there is no `create_log_group`).

**What is NOT the cause.** The build is sound and so is the artifact: the built sha256 equals the signed
`ZZmWOFSA/GjO0d/cKHSm9G5+xDc5sNfEHOpbmfIabQ0=` twice over under AMENDMENT 2's scoped parity skip, symbol_closure reads
`missing=0` with a discriminating control, and all 8 replay arms match the packet arm for arm. The defect is in the
Terraform of the signed set, and it is the issuer's or the CTO's to rule.

**The ruling needed (one line):** drop `aws_cloudwatch_log_group.commentary_composition_read` from
`commentary_composition.tf` and let the module own the group as the other eight roots do -- the role policy already
grants on `${local.ccr_log_group}:*`, which the module's group satisfies unchanged -- or re-sign the export-root plan
against whatever shape the CTO prefers. Row `IRPT_BCKEND-D2-S41`.

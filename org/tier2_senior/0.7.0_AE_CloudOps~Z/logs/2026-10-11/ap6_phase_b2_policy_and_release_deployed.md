# OG-ap-6 PHASE B2 -- the E2 grant and the gateway release are LIVE; order complete

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

Serial `0.7.0_AE_CloudOps~Z`, site Z. Window: 2026-10-11 ~01:20Z to ~12:20Z, i.e. everything since
`530c4aa2e2`. Most of that window was a timed hold; the work is 11:00Z to 12:20Z.

Third and final entry for this session. Read after `ap5_converter_apply_and_ap6_b1_recut.md` and
`ap6_step5b_head_plan.md`. **Both of this lane's orders are now `complete`.**

## The hold, and what the GO carried

`2.0.0_SA_COO~O` msg 33127 delivered AMENDMENT 2 @e1cfff0023 as the B2 GO, effective at or after
11:00Z. A2 says "nothing in B2 starts earlier", so nothing did. The window was confirmed on an
INDEPENDENT clock read at 11:01:24Z, not only from the armed waiter, and against the order's own
11:00Z-23:00Z bound.

Before the window this seat verified the GO's own claims rather than taking them on report: all
three re-pins present in HEAD and each naming `6aadf7db37` (CTO `b2bb4caabf`, COO `3d5fc13ecf`,
CVO `b8b7ab0f11`); MP-r-2's drain `189979795d` in HEAD with its ledger reading
`**Status:** CLOSED` and `EC2_MANIFEST` at `2a5966dfbd`. A2 also carried CTO C3's ruling
@eb37eb2e29, which binds BOTH the `1/0/0` summary AND `rc=0` -- adopted, in its own words,
because "a failed data source drops rows", which is the trap this seat measured at step 5b.

## ONE RELEASE IN FLIGHT (A2's precondition), measured at the act

Not a shared-tree read. `git worktree list --porcelain` enumerated **22** live worktrees and each
was `ls-tree`'d at its OWN HEAD, with the per-tree sentinel denominator printed (19, 22, 19, 25,
20, 20, 20, 18, 21, 20, 20, 20, 21, 20, 28, 20, 21, 23, 19, 25, 24, 22). Union: **101** distinct
sentinel names, **0** gateway/oplgtw sentinels anywhere, and both e2 slugs absent. `ls-tree` rather
than `ls -1`, which hides `.unindexed_red_state.json`.

## Step 6 -- the grant

`C:/tmp/og-tf-e2` was REMOVED and RE-CREATED detached at the HEAD of the act
`4344db632f8c7da29d6bdb47f05581ac62266fa4`. Before removing the prior one this seat established it
held nothing: 0 unique commits, and 0 files differing once CR/space is ignored -- git's own
warnings showed a CRLF working copy against LF blobs and `--numstat` showed equal add/delete counts
per file (388/388, 240/240, 708/708), the signature of a line-ending rewrite, not authored work.
A2's blob check was re-run at the new commit: `49c420acbce7cfb99c8726f5439b3f2cc6ea9f5a`, equal to
the signed release's.

BEFORE state of the exact object, with a positive control: `get-role-policy` for
`gateway-49f-advi-billing-put-policy` returned **NoSuchEntity** while the same call on
`gateway-mcportal-fabric-read-policy` returned its name -- so the absence was real, not an
instrument that cannot see policies. Inline count **21**, the same figure CTO Half 1 read at
signing.

Pre-apply targeted plan, captured to `W/ap6_plan_target.txt` and committed @`8a79550c21` BEFORE
the apply, with both of C3's limbs asserted separately:
```
  # aws_iam_role_policy.advi_billing_gateway_put will be created
  Plan: 1 to add, 0 to change, 0 to destroy.
  summary exactly 1/0/0 : yes    plan exit code 0 : yes
  planned rows          : 1      Error: lines     : 0
```
Applied through `safe-apply` against the SAVED plan: `Apply complete! Resources: 1 added, 0
changed, 0 destroyed.` Live read-back -- ONE statement, Sid `AdviBillingPutFeeStatementBronzeOnly`,
Action exactly `["s3:PutObject"]`, Resource exactly
`["arn:aws:s3:::opal-data-assets/smartx/49financial/bronze/fee_statement/*"]`, no Get/List/Delete,
no other prefix; count **21 -> 22**. Post-apply re-plan `No changes.` at rc=0.

## Steps 7-9 -- the deploy

The first deploy attempt **REFUSED before any upload**: `REFUSED (no upload):
meeting_allowlist.json unreadable`, because `data/transcripts` was outside the worktree's sparse
cone. The script fails closed, so nothing was uploaded and the host was unchanged, which is why the
`before` state stayed valid and did not need re-reading. Cone widened (`data/transcripts`, full
`infra/aws/ec2`), deploy re-run, rc=0. No `HALT_OVERRIDE`; the halt gate returned rc=0 with zero
output and is cited for nothing.

Read-back IMMEDIATELY, every count RELATIVE to the base read at the act -- **6 of 6 PASS**:
```
/health 200, active, MainPID 919385 -> 941937
shipped md5   106 of 106 identical to the re-cut release, not-ok []
MCP tools     66 -> 67, added exactly ['copy_site_file_to_s3'], removed []
.env names    52 -> 53, added exactly ['ADVI_FEE_STATEMENT_S3_ROOT'], removed []
.env values   all 52 pre-existing sha256 digests UNCHANGED, changed []
dashboard/    unchanged, 7 files before and after -- all four orphans (A1)
```

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `terraform` | targeted plan / apply / re-plan | PASS | 1/0/0 rc=0, then 1 added, then No-changes rc=0. Both C3 limbs asserted on both sides. |
| `safe-apply.sh` | `-chdir=C:/tmp/og-tf-e2/... apply ap6_target.tfplan` | PASS | SAVED plan, so the apply ran exactly the reviewed row. HALTGT pass not cited. |
| `safe-ec2-deploy.sh` | from `C:/tmp/og-rel16c`, `DEPLOY_BASE_REF=2a5966dfbd...` | PARTIAL then PASS | First run refused pre-upload on the sparse cone; fails closed; re-run rc=0. Its own manifest commit failed (`.tools` outside the cone), which it anticipates with "record manually". |
| `ap6_verify.py` | `before` / `after` | PASS | BEFORE PASS, AFTER 6 of 6. Adapted to RELATIVE counts; see below. |
| `deploy_ledger.py` | 2 ledgers, 9 legs total | PASS | Both opened with entry AND sentinel committed before their acts; both CLOSED, every leg proven. |
| `aws iam` | `get-role-policy`, `list-role-policies` | PASS | NoSuchEntity before with a positive control; one exact statement after; 21 -> 22. |
| `proof-of-spec-check.py` | instance + `--governing-order` | PASS | VALID rc=0 after three genuine refusals. |
| `surprise-row-gate.py` | row Z-S84 at commit | PASS | 1 new of 479. Next free k re-read at commit time, which mattered -- a peer took Z-S83 mid-session. |
| `comp-iam` | not run | SKIP | RUN-BY-ISSUER by the preflight. Recorded as not-run, never as a pass. |

**What worked.** Asserting C3's rc limb separately from the summary line. And keeping the `before`
state valid through a failed deploy attempt by checking WHY it failed -- it refused pre-upload, so
the host was untouched and re-reading would have been wasted work.

**What failed, and it is the headline of this entry.** The inherited `rl16_verify.py` hardcodes
Phase A's absolutes, including `md5_listed == 102`. This release's shipped list is **106**, because
MX-r-9/MP-r-2 moved the base from 100 to 104 shipped files. **Run as inherited, the verifier would
have FAILED a correct deploy** -- and on the single axis that actually moved. The COO half's
condition 3 already required the counts to come from the base read at the act, so the copy was made
relative, with the only absolutes being the two names the halves give. Two further own-goals: the
sixth and seventh sparse-cone failures of the session (`meeting_allowlist.json`,
`infra/aws/ec2/EC2_MANIFEST.json` for `build_package.py`), and `rc=$?` read through a pipe again,
which once reported `INIT_RC=0` on a terraform init that had failed.

**Gap found.** `deploy_ledger.py` regenerates its manifest table on every leg close, so a hand
correction to an entry does not survive -- discovered when MSYS path conversion mangled L2's
declared `C:/tmp/og-rel16c` into `C;C:\Users\OPALBL~1\AppData\Local\Temp\og-rel16c` at open time and
the fix was reverted by the next `close-leg`. The correction now lives in L2's PROOF text, which the
tool preserves. Anything a leg's declared text must say correctly has to be right at `open` time.

## Blockers

**None for this lane.** Both orders are `complete` and this lane holds no open deploy ledger.

Open and owned elsewhere, each named: row **Z-S84** (`file_checksums` stale on 8 of 10 entries, six
of them files E2 never touched) with `2.0.0_SA_COO~O`; row **Z-S82**'s two unnamed dashboard
orphans, adopted into step 8 by A1 but not themselves dispositioned; and the
`mcportal_grant_writer` `source_code_hash` drift, which A2 assigns to round-34 cell E2 and which was
never applied here.

## Current State

- **OG-ap-5** `complete` @`c2a23a0a6d`. Unchanged by this window.
- **OG-ap-6** `complete` @`cefab0bf26`, proof instance VALID rc=0, AC1 and AC2 PASS.
- **Live:** inline policy `gateway-49f-advi-billing-put-policy` on `opal-gateway-role` (one
  statement, `s3:PutObject`, fee_statement prefix only). `opal-gateway` on instance
  `i-07dccb1615503ac99` runs release `6aadf7db37a8605389110e08bb64f6e15e1d3026` with
  `copy_site_file_to_s3` registered and `ADVI_FEE_STATEMENT_S3_ROOT` set; `/health` 200.
- **Both ledgers CLOSED, both sentinels removed:** `nfra-oplgtw-e2-put-policy` @`4445f7a50b` (4
  legs), `nfra-oplgtw-gateway-release-e2` @`a54fa42da7` (5 legs). Nothing half-landed; nothing was
  overwritten and no object was deleted.
- **Rollback, one act per side:** re-deploy with `DEPLOY_BASE_REF` set to the release sha from a tree
  at `2a5966dfbd`, and destroy the single policy through the same Terraform path from
  `C:/tmp/og-tf-e2`.
- **Worktrees held, NOT interchangeable:** `C:/tmp/og-tf-e2` detached at `4344db632f` (the policy
  path; A1 forbids applying the policy from the release tree) and `C:/tmp/og-rel16c` on
  `rel-nfra-oplgtw-r16c` at the release sha (the deploy's app code). Both may be removed once the
  issuer has no further use; neither holds a commit that is not already on its branch.
- **Commits this window:** `8a79550c21` plan, `4445f7a50b` policy ledger close, `cb80fa4a7c` manifest
  + row Z-S84 + the adapted verifier and its two md5 lists, `a54fa42da7` deploy ledger close,
  `cefab0bf26` status + proof instance. Push state by `git ls-remote` at report time: all but
  `cefab0bf26` on origin.

## Next Steps

1. `[2.0.0_SA_COO~O]` MX-r-10 is UNBLOCKED -- it was queued behind this deploy ledger's close, and
   the issuer was told at that close.
2. `[OG-rl-16 Phase C]` The SERVED read: exercise `copy_site_file_to_s3` end to end and settle CTO
   C4 (whether the host's botocore accepts `IfNoneMatch` on `put_object`). This order ran neither and
   claims nothing about either.
3. `[2.0.0_SA_COO~O]` Disposition row Z-S84, and Z-S82's two orphans with NFRA_MCPINDEX.
4. `[2.0.0_SA_COO~O]` Round-34 cell E2 owns the `mcportal_grant_writer` `source_code_hash` drift.
5. `[0.7.0_AE_CloudOps~Z]` Event-driven hold; re-arm the Monitor on each `[WATCHER-EXPIRED]` line in
   one call, same turn.

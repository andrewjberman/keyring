# dell2 can read two of the three fenced firm buckets -- and the third was refused on purpose, not missed -- 0.7.0_AE_CloudOps~E

**archetype:** DEPLOY

**Date:** 2026-10-07
**Task Order:** `NFRA_CTLPLN.TO-APPLY-4.dell2-fence-join-apply-laptop` (issuer `2.0.0_SA_COO~C`; GO msg 106132, then
AMENDMENT 1 @aefcf32c11 as its own GO, msg 106153 -- both acked)
**Status:** COMPLETE as amended
**Workspace CLOUD commits:** `54295756ad` (the STOP) -> `dc52a0a501` + `a162b02c50` (surprise row + its byte-append
fix) -> `e332c94f2a` (ledger OPEN) -> `c0986d54e0` (apply, ledger CLOSE, proof instance)
**Push state:** `c0986d54e0` LOCAL; the four earlier commits are ON ORIGIN. Origin CLOUD read `f90db47701` by
`git ls-remote` at report time. `CLOUD` is pushed only by `0.0.0_AB_MSTR` on Andrew's word.

---

## Objective

Join `cloudops-dell2-agent-user` to the fenced firm-data bucket policies so the five projects placed on dell2 can
read the firm data they are placed on, instead of asking the laptop to proxy reads. A cross-firm access change, so
the plan's exact shape gated the apply.

---

## The headline: the gate refused the order as issued, and that was correct

The order asked for a three-bucket apply. **This seat refused it at the plan gate and applied nothing.** The counts
were right (`0 to add, 3 to change, 0 to destroy`) and all three fences did gain the dell2 principal -- but the
cottonwood policy's diff ALSO added three whole statements, `DenyRestrictedReadExceptReaders`,
`DenyRestrictedListExceptReaders` and `DenyRestrictedWriteExceptBreakglass`, restricting
`opal-data-cottonwood/commonwealth/cottonwood/bronze/crm/*` to two named principals.

Those statements belong to `ADVI_COTBKF.TO-CB-d-4` at `8e58736597`, whose own commit subject ends
**"nothing applied"**. That commit is an ancestor of `526a1a27ac` -- the trunk the COO half cites as its read point
-- so they were already in `s3-lgic-firm-buckets.tf` when both halves were authored. Neither half saw them, because
neither seat planned the root: both say so in writing, and both stopped at the same "Backend initialization
required" the order describes. **The halves bound on a predicted plan shape that nobody had ever measured.**

Had it applied, this act would have landed another project's deliberately-unapplied access restriction, refused every
current reader of that CRM prefix that is not one of two principals, and left a later ADVI_COTBKF apply reading
0-diff on work it never signed off as landed.

`2.0.0_SA_COO~C` and `1.0.0_SA_CTO` both answered within the hour and both wrote the same sentence into their
amendments: **"The stop was the half working."**

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| check_dell_fence_join.py | `python infra/aws/terraform/shared-infra/tests/check_dell_fence_join.py` | PASS | AC1, run before and after: `FENCE-JOIN pairs=3 rows=3/3 typed_in_tf=0 cross_firm_leaks=0 evaluator_allowed=3/3 negative_arm=denied other_rows_changed=0 validator=ok ok=True`. Its `terraform_validate` limb went from **SKIPPED** (`init rc=1`) to **OK** after my init -- a limb that was silently inert is now exercised. |
| dell_fence_census.py --live | `python .../tests/dell_fence_census.py --live` | PASS, one divergence | 24 of 24 buckets read, 0 unreadable, denominator printed. `gap_dell2=1`, `dell2_admitted=23/24`, `dell1_admitted=21/24` all match AMENDMENT 1. `gap_dell1` reads 1 where the report clause expects 0 -- see Decisions. |
| lib/opal_naming.py validate | `python lib/opal_naming.py validate` | PASS | CTO condition 4: `OK 53 system row(s), 13 scope row(s), 41 warning(s)`, **0 refusals**. Warnings are inferred `owner_directive` rows; the warning/refusal distinction IS the condition. |
| comp-iam | not run | SKIPPED, with reason | `comp-iam gaps` is the instrument for an `iam.tf` change. This act changed no IAM object and no `.tf` file -- it changed two S3 **bucket** policies. Running it would have produced a repo-wide report with nothing in this blast radius and invited a reader to treat it as coverage. The applied-plane instrument here is the live simulator with each bucket policy as the resource policy, which is leg V3. |
| comp-tool rail (HUD) | several DENY + 2 advisories | PASS as designed | Gated every raw-`aws` IAM/S3 inspection. Reads re-run under `# rail-checked:` were IAM role **existence** probes (required by the false-ALLOW trap) and enumerations of untracked local `.terraform` metadata, which `comp-find` cannot see because it searches the git corpus. |
| deploy_ledger.py | `open` / `close-leg` x5 / `close` | PASS | 5 legs opened before the apply, each closed with proof, entry CLOSED `20261007T110309Z`, sentinel removed. On the STOP **no entry was opened at all**, which is correct: step 4 sits behind the plan gate. |
| surprise-row-gate.py | `python .tools/surprise-row-gate.py <channel>` | PASS after a fix it earned | It REFUSED my first append because `surfaced_at` carried a prose placeholder (`10:1xZ`) instead of a timestamp. Corrected the value rather than reaching for the audited override. |
| proof-of-spec-check.py | `<instance> AC1,AC2,AC3 --governing-order <order>` | PASS | `violations=0`, **VALID rc=0**, genre DEPLOY admitted, `controls: 7 of 7 named discriminate`. It caught 5 real defects on the first pass -- see Decisions. |

**What worked:** the plan gate, which is the whole story of this session -- a shape rule the order gave me caught a
cross-project rider that two signed never-widen halves had both missed. `proof-of-spec-check` earned its keep too: it
refused a `introduces` claim I had made on the wrong commit.

**What failed:** nothing returned a wrong answer. Two self-inflicted defects, both caught by measuring my own output
rather than trusting it: the channel append rewrote 798 CRLF endings (fixed at `a162b02c50`), and the first proof
instance pinned a token to the commit that did not introduce it.

**Gap found:** no comp-tool exposes an **S3 bucket policy** document, and none exposes an IAM managed policy's
default version either (raised in the TO-APPLY-3 instance). Both gaps bite the same class: a never-widen half that
binds on "the live document equals the saved/repo bytes" must leave the rail for `s3api` / `iam` to be verified at
all. Raised for the tool's owner; not implemented here.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Gate the inputs | `exemptions.json` last touched exactly `e7ac51a04c`, git author `4.0.0_SA_CRO` (CTO condition 4). The two `.tf` blobs **hash-EQUAL** at `3ec42c56bf` and HEAD (`3832128f348b`, `706663b99f6d`) -- proven POSITIVELY, because `3ec42c56bf` never touched those files, so the order's "diff prints nothing" gate passes for a different reason than it reads. Control: `8e58736597^..HEAD` on the same pathspec is non-empty, so the instrument works. |
| 1 | AC1 | `FENCE-JOIN ... ok=True` |
| 1a | Resolve the init question (the order's named first read) | **NOT a stop.** Lock pins `hashicorp/aws 5.100.0`; the local plugin cache holds exactly that binary. Init ran with registry installation **disabled** (`-plugin-dir`) and reported "Using hashicorp/aws v5.100.0 from the shared cache directory", rc=0. **No fetch.** |
| 1b | `-reconfigure`, checked before use | The on-disk backend record's bucket/key/region are identical to `main.tf:11-15`, so it re-pointed at the SAME state. Control: `state list` returned **252** resources including all three fence policies. |
| 2 | Save ALL THREE live policy documents with SHA-256 | S3 versions no bucket policy, so these files ARE the rollback. dell2 confirmed absent from each before the apply. |
| 3 | Plan, three targets | **REFUSED.** 0/3/0 but cottonwood's diff carried three unapplied ADVI_COTBKF statements. Applied nothing, opened no entry, reported (`54295756ad`, msg 106147). |
| -- | AMENDMENT 1 arrives | Two-resource form; cottonwood excluded; both halves amended and re-signed. |
| 3' | Echo the argv back, then plan two targets | argv intact through MSYS. `Plan: 0 to add, 2 to change, 0 to destroy`; 2 blocks (`grep -c`); 19 changed lines, EVERY added line the dell2 principal, **0 removed**; cottonwood POLICY address absent (0 matches, control: inflection matches 2); 0 rider Sids; 0 replace markers. |
| 4 | NEVER-2 entry opened, 5 legs | `20261007T1031Z_...`, committed `e332c94f2a` |
| 5 | ONE targeted `safe-apply` | **`Apply complete! Resources: 0 added, 2 changed, 0 destroyed.`** |
| 6 | Read-backs | below |

---

## Verification

```
49financial   admitted 19 -> 20 (+1)   statements 4 -> 4      PRIOR+1dell2 == LIVE : True
inflection    admitted  5 ->  6 (+1)   statements 1 -> 1      PRIOR+1dell2 == LIVE : True
  negative control, same comparator, one Sid renamed:         LIVE == mutated PRIOR : False (both)

COTTONWOOD, the untouched control:
  prior 501 B / live 501 B   BYTE-EQUAL = True
  sha256 49f1cf260f0f18d5f52244c2a48bb5159765dd293633b750a9f0fbad39dcc7ae on BOTH
  statements=1   dell2 admitted live=False   rider Sids live = []

V3, LIVE bucket policy supplied as the RESOURCE POLICY, one ARN per call, decisions ATTRIBUTED:
  dell2            49financial / inflection   allowed        [matched: IAM Policy]
  dell2            cottonwood                 explicitDeny   [matched: RESOURCE POLICY]  <- the fence
  dell1            all three                  explicitDeny   [matched: RESOURCE POLICY]
  opal-gateway-role (unlisted)  all three      explicitDeny   [matched: RESOURCE POLICY]
  Opal_Terminal (control)       all three      allowed        [matched: IAM Policy]
  12/12 arms as expected

AC2  FENCE-CENSUS buckets=24 read=24 unreadable=0 fenced=3 dell1_admitted=21/24
     dell2_admitted=23/24 disagree=0 gap_dell1=1 gap_dell2=1 ok=True
AC3  No changes. ... exit=0   (targeted pair; NOT a whole-root 0-diff)
EXPECTED, not drift: a plan of lgic_firm["cottonwood"] alone reads 0 to add, 1 to change,
     0 to destroy, carrying the dell2 principal AND all three rider statements.
```

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Refused the three-bucket plan and applied nothing | Both halves say "any other statement: apply NOTHING". I did not weigh whether the rider was harmless -- that judgement was not mine to make, and the shape rule exists precisely so it isn't. |
| Did NOT try to engineer a narrower target to exclude the rider | The rider sits inside the SAME resource as the dell2 change, so no `-target` separates them. Saying so plainly let the CTO choose the route; inventing a workaround would have been me deciding a cross-firm access question. |
| Did NOT prefix the stop report with `[STOP]` | `org/XXX.md` makes `[STOP]`/`[HALT]` a STOP-class token that hard-blocks the recipient's own `safe-apply`. My act stopped; I was not halting the issuer. Using the token would have manufactured a gate on another seat (CLAUDE.md "do not manufacture friction"). |
| Reported `gap_dell1=1` as a divergence and proved it pre-existed, rather than reporting the three figures that matched | AMENDMENT 1's report clause expects `gap_dell1` still 0. The pre-apply census **that both halves cite** already records `MDPF_SECCLASS` on dell1 citing `opal-data-49financial:1`, so the inherited figure was wrong when written. Independently, this act only ADDED ARNs to admit-lists, which can never newly deny; `dell1_admitted` is unchanged at 21/24; and dell1's `explicitDeny` there printed both before and after. Quoting only the matching figures would have been true and misleading. |
| Named the census gap instead of silently substituting a principal | The order says pick the unlisted refused principal "from `tests/dell_fence_census.json`". It names none: the census carries only dell1 and dell2 as principals, and of the 21 distinct IAM ARNs across its 24 policies, **0** concrete non-dell ARNs are refused by all three fences -- its ARNs come from the admit-lists themselves. Used `opal-gateway-role` and proved BOTH halves: it exists (`get-role`, created 2026-08-15) and matches no list or wildcard. |
| Paired every simulation with an existence read and read `MatchedStatements` on every arm | The false-ALLOW mode measured on this project means an `allowed` proves the pattern matches a string, not that the resource exists. And a deny from an identity policy reads identically to a deny from the fence -- attribution is what makes the 12 arms evidence rather than assertion. |
| Fixed the channel append instead of leaving a passing-but-wrong commit | `dc52a0a501` showed 843/809 for one appended row: the write rewrote 798 CRLF endings, so the prior content was no longer a byte prefix (first divergence byte 18951). Every reader and the row gate passed it. On an append-only channel that destroys the one property an integrity checker can verify, so `a162b02c50` restored the exact prior bytes and re-appended in CRLF. |
| Dropped the `introduces` claim rather than re-pin to make it resolve | The checker refused `NFRA_CTLPLN-S12` as already present at `a162b02c50`'s parent -- correct, since `dc52a0a501` introduced it. I kept the pin on the **corrected** bytes and claimed no token, because moving the pin back to make the claim resolve would have cited bytes I had deliberately replaced. |
| Waited out the index lock rather than removing it | `.git/index.lock` was ~4 minutes old with other seats actively committing. Asked the repository (not the wrapper's stdout) whether my commit had landed -- it had not -- then retried when the lock cleared. |
| Did not act on the CTO's AMENDMENT 2 | It landed at `2714b7df72` (cottonwood fence, dell2's read-only Cottonwood price-store scan) but is not in my order and no GO arrived for it. Not mine to adjudicate; if it is, a GO will come. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/critical_paths/change_management/20261007T1031Z_nfra-ctlpln-dell2-fence-join-laptop-20261007_deploy_completion.md` | entry opened (box, blast radius, rollback-per-key, cottonwood exclusion), 5 legs closed, CLOSED | Yes -- `e332c94f2a`, `c0986d54e0` |
| `org/critical_paths/.open_deploys/nfra-ctlpln-dell2-fence-join-laptop-20261007.json` | sentinel created, then removed at close | Yes -- `e332c94f2a`, `c0986d54e0` |
| `.../deliverables/PRIOR_bucket_policy_*_20261007.json` (3) + manifest | the three live documents with SHA-256, saved pre-apply | Yes -- `54295756ad` |
| `.../deliverables/PLAN_shared-infra_dell2_fence_join_20261007.txt` | the REFUSED three-target plan | Yes -- `54295756ad` |
| `.../deliverables/PLAN_shared-infra_dell2_fence_join_TWOBUCKET_20261007.txt` | the gating two-target plan | Yes -- `e332c94f2a` |
| `.../deliverables/V2V3_fence_readback_20261007.txt` | document comparison + 12 simulator arms | Yes -- `c0986d54e0` |
| `.../deliverables/CENSUS_live_after_apply_20261007.txt` | AC2's live census | Yes -- `c0986d54e0` |
| `.../deliverables/PLAN_cottonwood_still_pending_EXPECTED_20261007.txt` | the deliberately-pending plan | Yes -- `c0986d54e0` |
| `.../deliverables/NFRA_CTLPLN.TO-APPLY-4...proof_of_spec.json` | genre DEPLOY instance, VALID rc=0 | Yes -- `c0986d54e0` |
| `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` | row `NFRA_CTLPLN-S12` | Yes -- `dc52a0a501`, corrected `a162b02c50` |

**No `.tf` file and no registry file was edited** -- the bound held by measurement (blob hashes equal, porcelain
empty), not by intent. The apply wrote two S3 bucket policies and nothing else.

---

## Blockers

**None.** Nothing is owed by this seat on this order.

---

## Current State

`cloudops-dell2-agent-user` is now admitted to the `opal-data-49financial` and `opal-data-inflection` fences, applied
from the laptop at ~10:3xZ by one targeted `safe-apply` of `infra/aws/terraform/shared-infra` (`0 added, 2 changed,
0 destroyed`). Both live policies equal their pre-apply documents plus exactly one ARN with statement counts
unchanged, and a live-principal simulation with each bucket policy as the resource policy reads 12 of 12 arms as
required with every decision attributed to its source policy. **`opal-data-cottonwood` was deliberately NOT applied**
and is provably untouched -- its live document is byte-identical to the copy saved before the apply -- because its
policy carries three unapplied `ADVI_COTBKF` CRM statements that no `-target` can separate from the dell2 change; the
CTO ruled it applies later, once, carrying both, under `1.0.0_SA_CTO~DELL2` / `2.0.0_SA_COO~C2`. The NEVER-2 entry is
CLOSED with all 5 legs proven and nothing stranded; the proof-of-spec instance is VALID rc=0 at genre DEPLOY with 7
of 7 controls discriminating. `c0986d54e0` is LOCAL at origin CLOUD `f90db47701`.

**Nothing here was EXERCISED and none is claimed.** No object was read in any firm bucket -- the order forbids this
seat -- so the grant is proven at the policy plane only. The box arm (dell2 reading an object from dell2) is the
fabric managers' route.

---

## Next Steps

1. **[`2.0.0_SA_COO~C`] Flip `<status>` on `NFRA_CTLPLN.TO-APPLY-4`** -- the report landed (msg delivered, 1346 B)
   and the genre-DEPLOY instance is VALID rc=0 beside the order. The flip is the issuer's, never the assignee's.
2. **[`1.0.0_SA_CTO~DELL2` / `2.0.0_SA_COO~C2`] The cottonwood apply is a TWO-change apply, not one.** A plan of
   `lgic_firm["cottonwood"]` alone carries the dell2 principal AND all three `ADVI_COTBKF` rider statements. Its only
   rollback that will ever exist is
   `deliverables/PRIOR_bucket_policy_opal-data-cottonwood_20261007.json` (501 B, sha256 `49f1cf26...dcc7ae`), because
   S3 versions no bucket policy.
3. **[the `ADVI_COTBKF` lane] Three restricted-CRM-prefix statements are committed and unapplied in a SHARED root.**
   Any seat that applies `lgic_firm["cottonwood"]` for any other reason lands them as a rider. That is how this act
   nearly landed them. The exposure stands until they are applied or reverted.
4. **[`1.0.0_SA_CTO` / `2.0.0_SA_COO~C`] `gap_dell1=1` is a decision, not a regression.** Either dell1 gets a row on
   `opal-data-49financial` (a CRO-lane write plus a new never-widen pair, since it widens access) or the
   `MDPF_SECCLASS` reference moves. Not this cell's to choose.
5. **[`0.0.0_AB_MSTR`] Push CLOUD on Andrew's word** -- `c0986d54e0` is LOCAL.

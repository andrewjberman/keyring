# OW-d-1 resumed under AMENDMENT 1 and closed: applied 0/3/0 branch A, ledger closed 5 of 5, instance VALID -- 0.7.0_AE_CloudOps~OW2

**Date:** 2026-10-09
**Task Order:** NFRA_OPSWKF.TO-APPLY-D1.trade-lambdas-ticket-bridge-ow2
**Status:** COMPLETE
**archetype:** DEPLOY

> SUPERSEDES the status line of this seat's earlier log today,
> `ow_d1_apply_blocked_on_dell2_plan_reads_gap.md`, which was accurate when written (BLOCKED at step 4)
> and remains the record of that phase. Everything it recorded about steps 0-3 still stands.

---

## Objective

Resume step 4 of OW-d-1 after the issuer amended the order, and carry the act to its close: the one
`safe-apply` of `infra/aws/terraform/trade-pipeline` at pin `71a1877db0` over K1-K4, the step-5
after-reads, the ledger close, the record and the tag.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| safe-apply | `-chdir=infra/aws/terraform/trade-pipeline apply <saved planfile>` | PASS | succeeded under the authorised override; bypass recorded id=20261009T100240Z-269670 result=SUCCESS rc=0 |
| terraform | `plan -target x3 -out`, `show -json`, targeted replan | PASS | the saved plan was the apply's input, so the apply ran the diff that was read; `show -json` supplied the by-hand tagauthz read |
| deploy_ledger | `close-leg L3/L4/L5`, `close` | PASS | closed with all 5 legs proven; sentinel removed |
| record-terraform-deploy | `trade-pipeline --version trade-pipeline-v1.21.0 --author ...` | PASS | committed `ecf96b66ae`; its reconcile read "4 already-in-parity -- reconcile: OK (deployed set in parity)" |
| proof-of-spec-check | `<instance> --governing-order <order>` | PASS | INVALID twice, then VALID (rc=0). Both refusals were mine: `decomp_ref.owned_cells` is not a permitted property, and a `terraform`/`iam` row's `path_or_key` is resolved as a REPO PATH at its pin, so a Terraform resource ADDRESS is refused there |
| surprise-row-gate | at commit, rows D2-S2/S3/S4 | PASS | refused the first attempt on `/class` and `/disposition`: the enums are OBSERVATION/BLOCKING and UNDER_INVESTIGATION/GRADUATED/DISMISSED_WITH_REASON/DECOMP_INVALIDATING |
| to-pipeline-gate | at the `complete` flip | PASS | refused the flip until a proof-of-spec INSTANCE existed beside the order; that refusal is what produced the instance |
| comp-find | `'"genre": "DEPLOY"'`, `'"judgment": true'` | PASS | found the DEPLOY-genre and judgment-criterion shapes to model the instance on; denominators printed |
| comp-iam | not run | SKIPPED | declared NOT-APPLICABLE by the order's preflight; and as a substitute for the unavailable simulation it would have hit its own false-allow mode, since it models `(action)` and not `(action, resource)`. The HUD advised it twice |

**What worked:** every gate that refused me was right, and three of them produced better artifacts than
I would have written unprompted — the pipeline gate produced the proof-of-spec instance, `deploy_ledger
hold` kept a half-landed deploy loudly RED instead of parked, and `proof-of-spec-check` caught two
structural errors in my own instance.
**What failed:** nothing produced a wrong answer.
**Gap found:** one of my own making, recorded because it is a live trap: **backticks inside a
double-quoted `--proof` argument are evaluated by the shell.** A `` `terraform show -json` `` in the L3
proof became a `terraform: command not found` line beside the close and two words silently vanished
from the stored text. Found by reading the stored proof back; repaired in both carriers. A proof that
loses the name of its instrument still reads as a complete sentence, which is why this is worth a line.

---

## Work Completed

### 1. The amendment, read at its carrier rather than from the message

Issuer msg 3070 pointed at `<amendment_1>` of the order; the authority is CTO ruling AMENDMENT 1
`@bff4e48547`, read at that commit. Four conditions: the override line names row D2-S3 and the ruling;
the targeted plan still reads exactly 0/3/0 at apply; the tagauthz check's own question is answered by
hand for the three resources; the override is never reused. All four met.

Re-verified before acting, because HEAD had moved under me: STOP 1 is still empty at the new HEAD
(positive control 1384 files differ pin..HEAD repo-wide), and both uploaded artifact versions are still
the latest on their keys.

### 2. The by-hand tagauthz check

Read off the plan artifact, not the source text — which is what the gate's own DETECTOR CAVEAT
recommends. `terraform show -json` of the applied planfile: 4 `resource_changes` as the printed
candidate denominator, **zero** of type `aws_instance`, the gate's candidate type. Its question — does
any `aws_instance` this plan creates or updates carry an access-granting tag `default_tags` would
overwrite — is therefore answered NO by construction, not by assertion. `tags` and `tags_all` are
byte-identical before and after on all four; `tags_all` already carries the tree's `default_tags`
(`Project=OpalPortal`, `ManagedBy=Terraform`, `Environment=Production`, `System=TradePipeline`) plus
`Name`. The apply writes no tag at all.

### 3. The apply

`Apply complete! Resources: 0 added, 3 changed, 0 destroyed` at 10:02:52Z — branch A exactly. The
apply consumed the **saved** planfile, so it executed the diff that had been read rather than a
re-plan seconds later.

### 4. After-reads

| Arm | Verdict | Instrument |
|---|---|---|
| (a) deployed bytes | MET | not CodeSha256 alone: the deployed zips were downloaded from Lambda, re-hashed and extracted, and each handler file inside hashes to the objective |
| (b) env | MET | the three prior keys plus `TICKETS_TABLE=opal-tickets`, nothing else |
| (c) grant arms | **PARTIAL** | the prescribed instrument is denied — see below |
| (d) unauthenticated POST | MET | 401 with no header, 401 on a bogus bearer, two distinct bodies, against a `GET /` = 200 reachability control |
| (e) 0-diff | MET | targeted replan rc=0, "No changes." |

**(c) is the one arm that is not what the order asked for, and it is not dressed up as such.** All nine
`simulate-principal-policy` invocations — six arms and three controls — returned the identical
`AccessDenied` on `iam:SimulatePrincipalPolicy`. That the *controls* failed too is the evidence it is
the instrument and not the world; an instrument that denies its own controls is not reporting on its
subject, and reading those nine as six DENIEDs would have "satisfied" the CTO's negative arm on a tool
that never evaluated anything. Substituted an evaluation of the **applied** document over an enumerated
denominator: 2 of 2 inline policies, 0 attached managed, `PermissionsBoundary` null. That yields
GetItem allowed, conditioned UpdateItem allowed, `UpdateItem` naming `answers` denied, and
Delete/Put/Scan denied — **by document, not by simulation.** One arm cannot be closed from this device
at all: `dynamodb:GetResourcePolicy` is also denied, so a table resource-based policy that could widen
the role beyond its identity policies is unreadable here. Row `NFRA_OPSWKF-D2-S4`.

### 5. Close, record, tag, instance

Legs L3/L4/L5 closed with proof; ledger CLOSED, all 5 proven, sentinel removed. `ecf96b66ae` records
the deploy. Tag `trade-pipeline-v1.21.0` cut from the **measured** latest tag (v1.20.1 local and on
origin) rather than from the order's prose, which names a `v1.22.0` that is not a tag on either side.
Proof-of-spec instance written and VALID (rc=0): genre DEPLOY, risk WORLD, 12 of 12 controls
discriminate, rollback named, 2 artifacts resolved at pin, 3 surprises resolving to channel rows.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Took the override only after an authority ruled, having first stopped and reported | The wrapper's own text says it "is not the remedy for this error". A seat granting itself a bypass to land its own deploy is the shape the no-manufactured-friction law exists to prevent |
| Answered the tagauthz question off the plan JSON rather than the `.tf` source | The gate's own caveat says a grep of the source is a text proxy whose negative is never proof. The plan artifact is the thing the gate would have graded |
| Recorded AC2 with **no** verdict, status `UNVERIFIABLE-BY-INSTRUMENT` | It is `judgment="true"`; L9 says judgment criteria are never self-graded. The substitute oracle is named as the issuer |
| Reported (c) as PARTIAL rather than MET | A document read inspects the rule; it does not evaluate it. Calling it MET would have transferred the simulation's authority to a weaker instrument silently |
| Left the tag on `2efb289ea8` after the destructive-git guard declined the re-point | The guard is right, the tag is local-only, and it provably contains the record commit (`--is-ancestor` passes, the reverse fails). Documented rather than forced |
| Did not push | This seat does not push a shared branch; `box-sync` and the MSTR lane carry `box/dell2` and will carry the tag |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| the NEVER-2 ledger entry + sentinel | L3/L4/L5 closed, entry CLOSED, sentinel removed | Yes — `6c3220281b`, `d3243d4873` |
| `.../deliverables/NFRA_OPSWKF.TO-APPLY-D1....proof_of_spec.json` | new, VALID | Yes — `d3243d4873` |
| `.../surprise-channel/investigations/INVESTIGATION_v1.md` | row D2-S4 appended | Yes — `d3243d4873` |
| the task order | `<status>` pending -> complete | Yes — `d3243d4873` |
| `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/terraform/trade-pipeline/CHANGELOG.json` | the recorder's own write | Yes — `ecf96b66ae` |
| `infra/aws/terraform/trade-pipeline/secrets.auto.tfvars` | hydrated per the tree's README | No — gitignored, verified with `git check-ignore -v`. Holds a live signing secret at rest on this device; disclosed rather than left silent |

---

## Blockers

None on this order; it is complete and its ledger closed.

- **Routed, not blocking:** the dell2 CloudOps principal was provisioned to APPLY but not for the READS
  that grade an apply — `ses:DescribeConfigurationSet` (row D2-S3, blocks any untargeted plan of this
  tree), `iam:SimulatePrincipalPolicy` and `dynamodb:GetResourcePolicy` (row D2-S4, block after-read
  (c)). The issuer has routed the first to the laptop fabric via `0.0.0_AB_MSTR~DELL2`; the
  recommendation that it carry all three is in row D2-S4 and the instance's forward notes.
- **Still OPEN, and not this order's to discharge:** CTO half condition 2 holds the PROD promotion of
  the OW-p-1 portal form until these after-reads AND a live 409 on one ticket-origin Execute. That
  live 409 is the issuer's OW-r-1.

---

## Current State

NFRA_OPSWKF OW-d-1 is DEPLOYED AND CLOSED. `trade-submission-handler` and `trade-workflow-handler` run
`CodeSha256` `Mw5sshdjyyuObV6J1tcbz4sSnD5yoNQUh9Bp2HW3Ifs=` and
`uWqGvRL/HfP6crogFOCkjRVfkNTxOH4jab/g+atRXzQ=` as of 2026-10-09T10:02:52Z, each carrying
`TICKETS_TABLE=opal-tickets` alongside its three prior env keys, and the deployed bytes were verified
by downloading them back from Lambda. `trade-submission-policy` now has 7 statements: the prior 5 plus
`TicketBridgeOpalTicketsRead` (GetItem) and `TicketBridgeOpalTicketsWrite` (UpdateItem under
`ForAllValues:StringEquals` `dynamodb:Attributes` in `[ticket_id, linked_submission_id, events,
status]`). Ledger `nfra-opswkf-ow-d1-trade-lambdas-20261009` is CLOSED with all 5 legs proven and its
sentinel removed; the one authorised `TAGAUTHZ_OVERRIDE` is spent (`id=20261009T100240Z-269670`) and
will not be reused. Rollback remains available per key in one window from the recorded
`s3_object_version` pins `S4xlyU0kBjVqTfqywTwhAb6nHmuSK4Fs` and `nGDl6NWpkMdQLwcCSIE92YRuh71vabEO`.
The order reads `complete`; `OW-d1-AC2` is the issuer's to grade and was reported with the instrument
behind each verdict named. Push state: LOCAL @`f5d18eb809`, origin `box/dell2` @`081a3efa22`
(`git ls-remote` read).

---

## Next Steps

1. **[2.0.0_SA_COO~O2] Grade `OW-d1-AC2`** — the judgment criterion, reported 10:32Z with the
   instrument behind each after-read named, including that (c) rests on a document evaluation rather
   than the simulation the criterion asks for.
2. **[2.0.0_SA_COO~O2 / NFRA_CTLPLN identity owner] Let the routed grant carry all three actions** —
   `ses:DescribeConfigurationSet`, `iam:SimulatePrincipalPolicy`, `dynamodb:GetResourcePolicy` — so the
   next trade-pipeline deploy from dell2 needs no override and can run after-read (c) as written.
3. **[0.7.0_AE_CloudOps~OW2] Hold event-driven** — seated for NFRA_OPSWKF only, zero task orders open,
   broker summary IDLE. Act on the next `[INBOX]` event the same turn and re-arm the Monitor on each
   `[WATCHER-EXPIRED]` line in one call.
4. **[owner of `.tools/safe-apply.sh`, via 1.0.0_SA_CTO] Consider letting the tagauthz limb read the
   caller's saved planfile** the way the naming limb already does at `:285`; `:342` records it as
   DEFERRED. One unreadable resource anywhere in a tree currently blocks every apply to that tree.
   Proposing only — implementing a gate change is not this lane's act.

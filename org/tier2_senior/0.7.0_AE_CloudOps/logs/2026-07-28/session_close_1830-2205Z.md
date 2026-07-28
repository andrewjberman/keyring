# 0.7.0_AE_CloudOps~C -- SESSION CLOSE (1830-2205Z): INFRA.TOOLS come-up, Stage-6 grant, one-plan registry fix, R14 fence

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, IMPLEMENT, DIAGNOSE, VALIDATE

## Objective

Come up as the `~C` successor lane to the context-exhausted `0.7.0_AE_CloudOps` base on mission tag
`INFRA.TOOLS` (CONTINUITY spawn path -- successor inherits the predecessor's tag, no COO
transcription step), then execute `1.0.0_SA_CTO`'s dispatches to completion.

**Detail logs, not restated here:**
- `infra_tools_registry_divergence_1830-2020Z.md` -- the findings pass
- `dispatch_execution_stage6_grant_and_one_plan_schema_2013-2110Z.md` (+ R14 appendix) -- execution
- Deliverable (3 parts, 549 lines): `deliverables/INFRA_TOOLS_REGISTRY_DIVERGENCE_20260728.md`

## Commits this session (13, all pushed; HEAD == origin/CLOUD, 0 ahead / 0 behind)

| commit | what |
|---|---|
| `92e41ad1b3` | INFRA.TOOLS findings Part I |
| `7d4eeefac6` -> `be4032a57c` | Stage-6 cottonwood gold grant: staged -> applied -> verified -> ledger CLOSED |
| `b17260251c` | Phantom `cron_schedule` deleted from `EC2_MANIFEST` + the 5-of-27 census |
| `85a64cadaa` + `d11b98e2ae` | `CODE_TREES`: one declaration, three registries derive; artifacts modelled |
| `8292f4dce1` | Deliverable Part II + the 22-of-27 census made durable |
| `9818f7b473` | Dispatch-execution session log |
| `6ce5c45f7c` | Router + canonicalizer false-clean closed (two halves) |
| `b2e3d9f5df` | Deliverable Part III |
| `aa739a36eb` -> `9fe9bf51de` | R14 latent-capability fence: staged -> applied -> verified -> ledger CLOSED |
| `61d8b8a0c3` | R14 appended to the execution log |

**Two deploy ledgers opened at deploy-start and CLOSED in-session on proven legs. NEVER#6 discharged
twice. No open deploy of mine.**

## What was delivered

**1. INFRA.TOOLS findings.** The mdpf code-deploy surface was described by three machine-readable
authorities that each restated the layout at their own call site, all three wrong differently.
Crucially: **mdpf's absence from `PIPELINE_MAP` is a DOCUMENTED DECISION** (`pipeline_cli.py:54-60`),
not an oversight -- the recorded reason is that `file_to_s3_target` is single-layout. **Nobody removed
the constraint, so the tree was excused from the gate: mdpf has a checker and no deploy path.**

**2. Stage-6 grant (IAM, applied).** Three grants not one -- `GetObject` is required because `:383`
head-objects after the put and **HeadObject IS `s3:GetObject`**, so PutObject alone relocates the
AccessDenied by one line. 8 isolated controls incl. a pre-apply baseline, a separately-invoked
positive control, and `accessanalyzer validate-policy` for action-name validity.
**`C3` = `explicitDeny`: the protected serve was NOT widened.**

**3. Record corrections.** Deleted a PHANTOM SCHEDULE from the Rule-8 source of truth -- `EC2_MANIFEST`
asserted a `mdpf-freshness-check-trigger` cron that does not exist on the applied plane (verified
against the **full 100-rule** inventory, not a name-prefix query -- **which is how it survived for
weeks**). Corrected a second false clause in the same field, declared as beyond-scope; CTO ruled
explicitly *do not split it*.

**4. One-plan registry fix.** `CODE_TREES` is now the single declaration; three consumers derive.
Rule-13 deploy gate **test-proven byte-identical** against a frozen literal fixture. `mdpf` declared
`deploy_gated: False` -- check-only, does **not** activate a deploy path.

**5. Router + canonicalizer false-clean closed.** Two halves; see the lesson below.

**6. R14 latent-capability fence (IAM, applied).** Two more served keys denied to the runner, with
the limit carried **in the Sid** because a TF comment is invisible to `get-role-policy`.

## THE FIVE THINGS WORTH CARRYING FORWARD

**a. A dispatched control that could not fail.** CTO's `C1` returned `allowed`, not deny -- a true
reading of a *pre-existing* statement, so it could not distinguish "my statement leaked" from
"something already allowed it." Replaced with controls that can fail. **I did not catch it by
suspicion -- I ran it because it was on the list, got an unexpected result, and then asked which
statement matched. The generalisable rule is: when a control returns unexpectedly, identify the
MATCHING STATEMENT before interpreting the verdict** -- a control that passes for the *wrong reason*
is invisible, and that case I still did not test for.

**b. The ruling's obvious implementation was the mutant.** "Correct the layer count" would have added
two names to a tuple that globs a nonexistent directory, hit `continue`, and reported a clean sweep --
**converting a visible gap into an invisible one.** Root: **one S3 code tree is fed by TWO repo
trees**, so a layer *list* cannot express it. Stopped and priced the grown scope to CTO before writing
code.

**c. A half-fix can RAISE a false clean's credibility.** Fixing only the routing half produced a
**correct header over an empty result** -- worse than the wrong header, because it looks authoritative.
Found only by running CTO's exact invocation end-to-end instead of trusting the passing unit test.
**A unit test that passes on the MECHANISM you repaired is silent about the OUTCOME.**

**d. I shipped three tests that never ran.** Written, not registered in `main_test()`; the suite
printed a clean `11/11` over checks it never executed. **Caught only because I expected 14.** A guard
nothing invokes is not a guard -- committed inside the change whose subject is guards that cannot
fire. **The COUNT caught it, not the result.**

**e. Test your own by-construction claims.** For R14 I argued the literal-key form spares the
`account_distribution.json` underscore twin "by construction." That was an argument. I added control
`C2` to measure it (`allowed` -- untouched). **A claim I make about my own change is exactly the one I
should not leave untested.**

## Compiler Tools

| Tool | Where | Result | Note |
|---|---|---|---|
| `comp-tagauthz` (via `safe-apply`) | mdpf-pipeline x2 applies | PASS, **self-ran, ZERO override** | `TMPDIR` export fixes the cygwin `/tmp` defect; the audited bypass stays retired |
| `comp-pipescript deployed` | no-arg sweep, `--pipeline mdpf`, path forms | PASS + GAPS | Found the 4-vs-6 layer blindness; after the fix surfaced 2 STALE cottonwood scripts invisible before |
| `comp-grep` | PIPELINE_MAP consumers, key attribution | PASS | **WARNED my `\|` was a Python-re literal** rather than silently returning 0; prints its own working set. Cite as the in-house retrieval-control good example |
| `deploy_ledger.py` | open / close-leg x8 / close x2 | PASS | NEVER#6 mechanism, both entries CLOSED |
| `commit-gate.sh` | 5 `.py` across 3 commits | PASS | |
| `comp-which` rail | ~10 raw `aws` inspections | PASS | each carried `# rail-checked:` -- routed tools model TF-DESIRED and cannot answer applied-plane questions |
| `comp-iam` | NOT used, deliberately | n/a | Models `(action)` never `(action, resource)` and fails GREEN; grounded on `simulate-principal-policy` + `get-role-policy` (Rule 22a) |

**What worked:** isolated `simulate-principal-policy` batteries with separately-invoked positive
controls; `accessanalyzer validate-policy` for action-name validity (which `simulate` structurally
cannot answer); frozen literal fixtures + source-file mutants.

**What failed / gap found (INFRA.TOOLS.O2, the mission's own subject):** `comp-pipescript deployed`
has **no progress contract** -- >4 minutes of silence then a full report, so **silence and failure are
byte-indistinguishable to the caller.** I misread that as a hang and said so to CTO before it
finished; corrected unprompted within the hour.

## MCP traffic

~22 messages. Significant: CTO dispatch `201342Z` (order-is-the-ruling), rulings `203649Z` /
`204454Z` / `204943Z` / `213109Z` / `214924Z`; my ACKs + 3 RAVC evidence reports (all VALIDATED,
RAVC closed); AE-base `210149Z` config-artifact input (folded into `CODE_TREES`); one stop-and-tell
that grew scope before code (`204756Z`) and one pre-apply hold (`214631Z`).

## Blockers

**None of mine.** Open at `1.0.0_SA_CTO`, evidence-cited:
- mdpf `deploy_gated` -- recorded OPEN, owner CTO, trigger = the canonical publisher work
- `partner_roster` `s3_key` -- confirmed it CANNOT be chosen yet (the runtime receives exactly one
  synced prefix with `--delete`, so it needs a dispatch change, not a table entry)
- the two STALE cottonwood scripts -- DO NOT DEPLOY, coupled to DS's held `_interpolated`
  read-preference; **neither moves alone**

**Surfaced, not acted on:** three OTHER open deploy ledgers (oldest 98.6h; the 07-28 one malformed --
no `Status:`, no close-date). **Not mine; NEVER#6 only works if the opener closes it with proof.**

## Current State (handoff surface)

**Live IAM on `mdpf-daily-runner-ec2-role` (`mdpf-runner-scoped`, 26 statements):**
- `AssetsCottonwoodGoldWrite` Allow `[PutObject, GetObject]` on
  `opal-data-assets/blackdiamond/cottonwood/gold/*`
- `AssetsCottonwoodGoldList` Allow `[ListBucket]`, prefix-conditioned to that one tree
- 3 Deny statements live: `P0DenyJsonMdpfClobber20260728`, `P0DenyLegacyPortfoliosClobber20260728`,
  and `R14LatentFenceOnlyNOTAPROTECTIONRunnerIsNotADemonstratedWriterObservedWriterUnidentified20260728`

**`mdpf-pipeline` is FROZEN to targeted applies.** Full plan shows exactly row 10's four pending
(3 add + the DLQ queue policy). Both my applies were `-target=aws_iam_role_policy.mdpf_runner`.

**Tooling:** `.tools/safe_deploy_core.py` `CODE_TREES` is the one declaration (4 trees, 15
`(tree,layer)` cells); `PIPELINE_MAP`/`VALID_LAYERS` derive; `org/modules/graph/pipeline_cli.py`
derives its mdpf layer set, its routing (`resolve_pipeline_from_arg`) and its filter canonicalization
from it. `.tools/test_code_trees_invariant.py` = **18/18**; `.tools/test_safe_deploy.py` = **14/14**.

**PENDING ACCEPTANCE, and it is not mine to fire:** the Stage-6 grant's acceptance is the **next
SCHEDULED run** -- `:523` passes -> `:524`/`:525` execute -> cottonwood artifact under
`gold/mdpf_revamp/cottonwood/` -> Stage 6 rc=0 -> **`cycle-complete.json` emitted for the first time
ever.** **No ad-hoc run was fired and none should be** (an ad-hoc run is a QA instrument, never
production evidence). Per CTO, a persisting gold-DDB stall after this is a **separate legacy-lineage
defect** (Stage 3 / WS-A `mdpf_aggregate_aua.py`) and is **not** this grant failing.

**`R14` is a FENCE, not a protection.** The runner is not a demonstrated writer of
`aum-metrics.json` / `account-distribution.json`; the observed writer (2026-07-23 16:57) is
UNIDENTIFIED; the `portal-v2` bucket policy carries ZERO denies; `>=6` other principals retain
PutObject. **Those keys are not safe.**

## Next Steps

1. **[0.7.0_AE_CloudOps~C or successor]** Report the next scheduled run's Stage-6 verdict on its own
   terms. Procedure + baselines are in the 1341-1435Z log's DURABLE CHECK section.
2. **[1.0.0_SA_CTO]** The three open calls above.
3. **[0.4.0_DS]** Still HELD -- production before consumption; not signalled, and must not start on
   the apply alone.
4. **[unowned]** The `EC2_MANIFEST` trigger-field schema change (REQUIRED + declared-unknown
   sentinel) -- CTO recorded it as **his to route**, explicitly not this session's build.

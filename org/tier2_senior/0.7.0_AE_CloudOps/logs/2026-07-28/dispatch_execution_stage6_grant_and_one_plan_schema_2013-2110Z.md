# 0.7.0_AE_CloudOps~C -- CTO dispatch execution: Stage-6 grant, the phantom cron, and the one-plan schema fix (2013-2110Z)

**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, VALIDATE, DIAGNOSE

## Objective

Execute `1.0.0_SA_CTO`'s dispatch `201342Z` and the follow-on rulings `203649Z` / `204454Z` /
`204943Z`. Order was the ruling, not a preference: land the findings, then IAM, then the record
corrections, then the schema fix.

## What landed

| # | commit | what |
|---|---|---|
| 1 | `92e41ad1b3` | INFRA.TOOLS findings (deliverable Part I + log + compiler rows) |
| 2 | `7d4eeefac` -> `be4032a57c` | Stage-6 cottonwood gold grant: staged, applied, verified, ledger CLOSED |
| 3 | `b17260251c` | Phantom `cron_schedule` deleted from `EC2_MANIFEST` + the 5-of-27 census |
| 4 | `85a64cada` + `d11b98e2ae` + `8292f4dce1` | `CODE_TREES`: one declaration, three registries derive; tests; Part II |

## Stage-6 grant -- NEVER#6 discharged

Three grants, not one: `PutObject` (`:382`), `GetObject` (`:383` head_object -- **HeadObject IS
`s3:GetObject`, so PutObject alone moves the failure one line down**), prefix-conditioned `ListBucket`
(`:116`). Ledger opened at deploy-start, 4 legs closed with proof, entry CLOSED.

`0 added, 1 changed, 0 destroyed`; targeted re-plan `No changes`; full-tree plan still shows **exactly
row 10's four** pending -- tree still FROZEN. `comp-tagauthz` **self-ran, PASSED, zero override**
(TMPDIR to scratchpad; the audited bypass used twice earlier today stays retired). Applied truth from
`get-role-policy`, not the plan. **Both P0 Denies still live.**

**8 isolated invocations, one `--resource-arns` each**, plus a pre-apply baseline
(`implicitDeny`/`implicitDeny`), a positive control in a **separate** invocation (`allowed`), and
`accessanalyzer validate-policy` for action-name validity -- which `simulate-principal-policy`
structurally cannot answer. **`C3` = `explicitDeny`: the protected serve was NOT widened.**

**No run fired.** The apply is not the acceptance; the next scheduled run is.

## >> THE C1 CATCH -- a dispatched control that could not fail <<

`C1` as dispatched (`ListBucket +context schwab/08242234/silver/`) returned **`allowed`**, not deny.
**Not a leak in my statement** -- a true reading of a *pre-existing* one, `AssetsRevampListScoped`
(MDPF_REVAMP.S4), which already carries that prefix. Established by enumerating **every** live
`ListBucket` statement on the bucket, not by assuming.

**So C1 could not distinguish "my new statement leaked" from "something already allowed it" -- the one
thing a control must do.** Replaced with **C1'** (another firm's *gold* tree, granted by nothing) and
**C4** (write axis). Both `implicitDeny`; firm separation now demonstrated on both axes, neither of
which C1 touched. CTO took the defect as his (relayed a pre-computed battery without testing a control
in it) and adopted C1'+C4 as the standard shape; C1 retired.

**I declined part of the credit and it matters for the next battery:** I did not run C1 out of
suspicion -- I ran it because it was on the list, got an unexpected result, and *then* asked which
statement matched. **The generalisable control is "when a control returns unexpectedly, identify the
matching statement before interpreting the verdict"** -- because a control that passes for the *wrong
reason* is invisible, and that case I did not test for.

## The phantom cron

`EC2_MANIFEST.mdpf-daily-runner.cron_schedule` asserted `mdpf-freshness-check-trigger cron(45 16 * * ? *)`.
**No such rule exists** -- verified against the **full 100-rule** inventory rather than a name-prefix
query, **which is how it survived a `--name-prefix mdpf` check for weeks.** Corrected a **second**
false clause in the same field (the dead `opal-data-bd` custody path row 13 re-pointed today),
declared as beyond-scope rather than smuggled; CTO ruled explicitly **do not split it**.

Raw-text edit, **not** a JSON round-trip -- AE-base mojibake'd six unrelated entries in this same file
today that way. Verified after: parses, 27 intact, zero non-ASCII, diff = 1 line.

**Census (predicate printed): 5 of 27 carry a schedule assertion; 1 was false; 1 is not adjudicable by
`list-rules` and was left UNVERIFIED rather than counted clean.** The load-bearing number is the other
one: **22 of 27 assert nothing at all about how they are triggered.** CTO ruled the field becomes
REQUIRED with a declared-unknown sentinel permitted; build routed to a fresh session.

## The one-plan schema fix

**I stopped and told CTO before writing a line, because his ruling's obvious implementation was the
mutant:** adding `assets_gold`/`silver` to `pipeline_cli:1945` globs a nonexistent
`data/mdpf/scripts/<layer>/`, hits `:1947 continue`, and **skips both silently** -- converting a
visible 4-vs-6 gap into an invisible one. **One S3 code tree is fed by TWO repo trees**
(`data/assets/`, not `data/mdpf/`), so a layer *list* cannot express it. CTO approved the grown scope
and added a mandatory requirement: **prove the `PIPELINE_MAP` invariant, do not assert it.**

`CODE_TREES` is now the one declaration; `PIPELINE_MAP`/`VALID_LAYERS`/`pipeline_cli`/`EC2_MANIFEST`
derive from or point at it. `mdpf` is `deploy_gated: False` -- **CHECK-ONLY, does not activate a deploy
path**; gating it would silently upload on DS pushes. Fail-loudly upstream of the skip (**the fix for
my own `:1929` finding**). No fallback copy in `pipeline_cli`.

**14 cases against a FROZEN LITERAL FIXTURE** (a fixture computed from the code under test cannot
detect that code changing) + pre-existing 14/14, no regression. **Three source-file mutants, each
detected, restore byte-verified.**

**Found the moment the tool could see:** `build_cottonwood_mdpf_pair.py` and
`build_cottonwood_mdpf_slice.py` **STALE on S3**. Reported, not fixed.

## Compiler Tools

| Tool | Where | Result | Note |
|---|---|---|---|
| `comp-tagauthz` (via safe-apply) | mdpf-pipeline | PASS, **self-ran, ZERO override** | TMPDIR export fixes the cygwin `/tmp` defect; keeps the audited bypass retired |
| `comp-pipescript deployed --pipeline mdpf` | exercise CODE_TREES | PASS 6/6 layers | Surfaced 2 STALE cottonwood scripts invisible before; also exposed a false-positive class I introduced |
| `comp-grep` | PIPELINE_MAP consumers | PASS | **WARNED that my `\|` was a Python-re literal** instead of silently returning 0 -- a tool naming its own misuse mode |
| `commit-gate.sh` | 3 + 2 `.py` | PASS | |
| `deploy_ledger.py` | open/close-leg x4/close | PASS | NEVER#6 mechanism |
| `comp-iam` | NOT used, deliberately | n/a | Models `(action)` never `(action, resource)` and fails GREEN; grounded on `simulate-principal-policy` + `get-role-policy` instead (Rule 22a) |

## My errors this window

1. **I shipped three tests that never ran.** Written, not registered in `main_test()`. The suite
   printed a clean `11/11` over checks it never executed. **I caught it only because I expected 14.**
   A guard nothing invokes is not a guard -- committed inside the change whose subject is guards that
   cannot fire. **The COUNT caught it, not the result: a passing suite is silent about what it did not
   run.** Fixed, then exercised (Mutant C).
2. **My own `184924Z` schema recommendation** (`tree -> layers`) could not have expressed the defect it
   was designed for. Corrected before writing code, not after.
3. **Introduced a false-positive class** (shared repo homes -> ~16 bogus `MISSING_ON_S3`). Caught and
   fixed before commit. A sweep with more false positives than findings trains people to ignore it --
   the same end state as the blindness it replaced.

## Blockers

**None of mine.** Open at `1.0.0_SA_CTO`: mdpf `deploy_gated`; the `partner_roster` target key;
whether the two STALE cottonwood scripts get deployed. Items 3 and 4 parked -- AE-base is on 3.

## Current State

All dispatched items complete, committed and pushed through `8292f4dce1`. Deploy ledger CLOSED, no
open deploy. Event-driven on Monitor `blq7dkh1y`.

## Next Steps

1. **[0.7.0_AE_CloudOps~C]** Report the next SCHEDULED run's Stage-6 verdict on its own terms --
   `cycle-complete.json` emitting for the first time is the acceptance. Per CTO, a persisting gold-DDB
   stall is a separate legacy-lineage defect and is **not** this grant failing.
2. **[1.0.0_SA_CTO]** The three open calls above.
3. **[0.4.0_DS]** Still HELD -- production before consumption; not signalled.

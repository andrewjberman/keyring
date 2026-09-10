# Session log -- 0.7.0_AE_CloudOps~V -- 2026-09-09 1810-2015Z

## NFRA_OPSEC202609.TO-OP-S-10B -- two slots and a TTL for the JWT consumers: DEPLOYED

**archetype:** DEPLOY

## What this session was handed

Seated 18:1xZ by `2.0.0_SA_COO~Z` because the prior instance of this lane died with two faces
staged. The queue: `TO-OP-S-10B` (BLOCKER NONE, GO immediately), then `TO-OP-S-10` which is gated
on it.

**The predecessor had already done the hard half.** `26ffa22b79` carries the shared two-slot module
and both consumers' integration, exercised 17/17 with a planted mutant -- **SOURCE ONLY, nothing
deployed.** Its own commit body names what was left: the two deploys, the per-consumer ledgers, the
live-path probes, `S10B-AC2`'s warm-environment convergence, and the proof-of-spec. That is what
this session did.

## Outcome

**Both consumers are DEPLOYED and verified. `FWD-10`'s enabling capability is live, and nothing was
rotated.** Proof-of-spec VALID rc=0 on all six criteria; both deploy ledgers CLOSED on 5 proven legs
each; TO flipped `complete`.

| criterion | verdict | the load-bearing evidence |
|---|---|---|
| S10B-AC0 | PASS | The STOP branch had fired: the set is FOUR, not the two the face was cut with, over an upper bound of 31 across FIVE granting roles. The re-cut came from the issuer. |
| S10B-AC1 | PASS | Two slots at source, in both **deployed** artifacts, and a **real production token accepted** through the new path 45 s after the apply. Negative control at each consumer. |
| S10B-AC2 | PASS | One warm environment held across two TTL boundaries, no redeploy: re-reads at 19:21:03 / 19:26:11 / 19:31:25 (308 s, 314 s vs a 300 s TTL). |
| S10B-AC3 | PASS | One authored copy; the second on-disk copy characterized as a gitignored build mirror. |
| S10B-AC4 | PASS | Both secrets byte-identical across the whole face. |
| S10B-AC5 | PASS | Nine routes 9/9 403 on three runs; both ledgers closed; supersession ISO-vintaged; push state measured with a control. |

## The three things worth carrying forward

**1. THE PIN TRAP WAS EXHIBITED, NOT MERELY AVOIDED.** `auth-validator-edge` carried
`ignore_changes = [qualified_arn, ...]`, which its own file documents as publishing a new Lambda
version while CloudFront keeps serving the old one -- passing DESIRED, APPLIED and EXERCISED at
once. The pin was dropped in the same commit as the code, and the deploy was split into two scoped
applies so the intermediate state could be *read*:

```
apply 1  function only        -> version 19 published, Active
READ     live distribution    -> auth-validator-edge:18 on 24 behaviors   <-- the trap, visible
apply 2  distribution         -> repoint
READ     live distribution    -> auth-validator-edge:19 on 24, :18 on ZERO
```

Stopping at "the version is published and the re-plan is clean" would have reported a deploy
CloudFront was ignoring. **The instrument is the live distribution config; `comp-routes
edge-versions` cannot catch it** because it reads the `qualified_arn` reference in the locals block
and cannot see the `ignore_changes` that defeats it (rail-checked marker used, with that reason).

**2. MY OWN NEGATIVE CONTROL KILLED MY FIRST AC2 INSTRUMENT.** REPORT `Duration` on the warm
environment gave a textbook result -- ~1.4-2.5 ms steady state, spikes at t+0 / t+308 / t+621 s
against a 300 s TTL. Then the control: the **pre-deploy** code, on an environment that lived 6687 s,
returns **21 spikes** -- and under that code the JWT cache had *no TTL* and could re-read at most
once per environment. Cause: `originVerify.mjs:39` is a **second 300 s cache in the same handler**,
deliberately given the same number so a rotation runbook reasons about one window. The consistency
that makes the runbook safe is what makes the timing signal blind. Re-graded on CloudTrail, which
carries the `secretId` and therefore discriminates. **Row Z-S155.**

**3. I MISREAD A TERRAFORM SET DIFF AS A SECURITY REGRESSION, AND THE MEASUREMENT CORRECTED ME.**
The distribution `-target` pulls the WAF chain it depends on. The plan renders three
`- rule { ... -> null }` blocks naming `AWSManagedRulesCommonRuleSet`, `AmazonIpReputationList` and
`KnownBadInputsRuleSet` -- which reads as managed security rules being stripped off the live edge,
and I said so. Counting **both** halves gives 3 removals and 3 additions of the same three names:
`rule` is a SET, so a nested change renders as remove+add. Net rule set unchanged, confirmed on the
live plane after the apply (same 6 rules, same priorities). The same shape then recurred in the
distribution's own `lambda_function_association` blocks, where I checked both halves first.
**Reading the `-` half alone is the error; it cost one wrong sentence and would have cost a false
STOP.** Filed as **row Z-S156** because the *ride* is structural and the next edge deploy inherits
whatever state those resources are in then.

## Blockers

**None.** `TO-OP-S-10B` is terminal and `TO-OP-S-10` is unblocked on this axis. Not started this
session -- reported to the issuer rather than begun, because the GO sequences it after this face is
terminal and the report is the handoff.

## Not obtained, named rather than papered over

- **The valid-fixture 200-through-CloudFront arm.** Row Z-S51's MFA gate re-measured live: `POST
  /auth/login` with the committed `internal_admin` credential returns 200 `mfaRequired=true`,
  `channel=email`, a `challengeId`, and **no accessToken**. What stands in its place is stronger on
  the axis that matters -- a **real production token accepted** in the authorizer's own log on the
  new artifact.
- **An observed key-A-to-key-B value substitution for AC2.** Deliverable 4 forbids writing the
  secret and `S10B-AC4` requires it unchanged; the two criteria are in deliberate tension. What is
  proven is that the same warm environment's cache **expires and returns to Secrets Manager** three
  times -- the convergence mechanism, which was flatly impossible before this face.

## Other lanes' open ledgers seen while checking my own (surfaced, NOT chased)

`deploy_ledger.py check` reports PAST-WINDOW open entries belonging to other seats:
`opsec-s10c-session-analytics-act2` (~W, L1), `opsec-s15-reconciler-function` (~T, L6),
`advi-insure-gold-chain-membership` (~R, L4), `advi-insure-iam-insurance-silver-read` (base, L4).
Not mine; named here so the reading is not lost.

## A defect in my own tooling path, recorded

`git reset HEAD --` on a staged-added-then-deleted ledger sentinel, followed by a merge, left
`org/critical_paths/.open_deploys/opsec-s10b-edge-two-slot.json` back on disk at status `OPEN` with
zero legs proven, while the committed `.md` read CLOSED. `deploy_ledger.py check` flagged it exactly
right: **"DRIFT-DANGEROUS ... entry reads terminal while legs carry NO proof -- a NEVER#6 bypass
wearing a compliance mask."** Removing the stale sentinel restored what `close` had already done, and
a re-check shows neither of my ledgers open. **The gate caught it; I did not.**

## Compiler Tools

| tool | invocation | result | gap found |
|---|---|---|---|
| `comp-routes` | `comp-routes behaviors` | Confirmed the edge is viewer-request across the auth-gated surface and `/auth/*` carries no auth Lambda. AE-mandated before a Lambda@Edge change. | **YES, and it is documented in the tree already:** it cannot read the live association *version*, so it cannot catch the pin trap. Used the live distribution read under a `# rail-checked:` marker naming that reason. |
| `comp-find` | `'export async function getJwtKeySlots' --limit 20`; `'getJwtKeySlots' --band SURFACED`; `'jwtPublicKeys' --files`; `'enable_lambda_edge' --band SURFACED` | S10B-AC3's census, denominators printed (53,044 files). | The `corpus=all` default **includes gitignored content**, which is the only reason the session-analytics build mirror surfaced -- that is what turned "one copy" from an assumption into a measured claim with a characterized exception. Re-run after the merge window closed, because 25 files moved under `.tools/`. |
| `comp-read` | `originVerify.mjs --for '...'`; `cloudfront-distribution.tf --enumerate 'auth_validator_edge'` | The first surfaced the qualifier at `:97` establishing that the origin check **precedes** the key read -- which is what forced AC2 onto direct invoke. The second printed 26 hits and WARNed every hit is a fragment. | None. The QUALIFIERS section did the work here. |
| `deploy_ledger.py` | `open` / `close-leg` / `close` x2 | Both ledgers opened before their deploy with rollback named, closed on 5 proven legs each. | **YES** -- see the sentinel-resurrection note above; the tool's `check` caught the drift my own git handling created. |
| `safe-apply.sh` | `HALT_ACK=1 ... apply <saved plan>` x3 | All three ran the SAVED plan, so what shipped is what was read. | The HALT gate **blocked the first invocation correctly** -- the session-serial file lived in the shared tree and a linked worktree carries its own checkout. Per LD-0267 a HALTGT pass is never cited; recorded because the block was real and self-inflicted. |
| `proof-of-spec-check.py` | on TO-OP-S-3's instance, then on this one | S-3 re-validates VALID rc=0 after the supersession note, S3-AC3 untouched at PASS. This instance VALID rc=0 on all six ids, 3/3 surprises resolve. | Schema shapes are not guessable: `declared_exclusions` items are objects, `controls` is `additionalProperties:false` with a required `determinism` block, and `kind`/`deployed_state` have closed enums. Four rounds to VALID. |
| `surprise-row-gate.py` | via `safe-commit` | **REFUSED** the first attempt: `class 'NON_BLOCKING'` is not in the ratified enum `['OBSERVATION','BLOCKING']`. Fixed rather than overridden (an audited override exists and was not used), then PASSED. | The enum is narrower than it reads. |
| `safe-commit.sh` | x5 | Four landed; one **correctly refused** an owned-paths lane violation. | The supersession target lives in another lane's `deliverables/` folder. Resolved with the sanctioned, audited, SINGULAR `GIT_COMMIT_AUTHOR_OVERRIDE` -- **not** `--force`, which by rule does not bypass an owned-paths refusal. Two lanes, two commits. |

## Commits (push state MEASURED, `origin/SITEZ` = `3054872f2b`)

| commit | tree | what | push state |
|---|---|---|---|
| `960921ba9c` | worktree | authorizer deploy carriers + ledger | LOCAL |
| `44db4f2099` | worktree | S3-AC3 supersession (lane override) | LOCAL |
| `3eed6f77dc` | worktree | edge deploy: pin drop + carriers + ledger | LOCAL |
| `9bd2fce772` | shared | surprise rows Z-S154/155/156 | LOCAL |

Positive control: the origin tip tested against `origin/SITEZ` reads ON ORIGIN, so the LOCAL
verdicts are real absences. Push is the integrator's under LD-0367 / GATE 5 and this claim ages the
moment an integrator runs.

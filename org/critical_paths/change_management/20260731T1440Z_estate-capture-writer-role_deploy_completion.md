# DEPLOY-COMPLETION LEDGER -- estate-capture-writer role

**Opened:** 2026-07-31T14:40Z (at apply-start, per CLAUDE.md NEVER-rule 5 + CTO 142530Z)
**Owner:** `0.7.0_AE_CloudOps~B`
**Module:** `infra/aws/terraform/estate-report/` (state key `estate-report/tfstate`)
**Change commit:** `@888c2fd4e5`
**Status:** `OPEN`

---

## Authorization chain

- **Andrew-direct**, 2026-07-31 ~1358Z at the CTO terminal, VERBATIM: **"yes on estate capture writer"**
  (relayed by `1.0.0_SA_CTO` 142530Z).
- **CVO** hold (a) v3 = CREATE-PRINCIPAL -> AUTHOR -> exercise (134724Z).
- **Scope FENCED** by CTO: role + device-assume from Andrew's existing user + sole `s3:PutObject`
  on `text-input/` + versioned bucket. **Anything beyond returns to CTO.**

## What is being applied

`Plan: 2 to add, 0 to change, 0 to destroy.`

| Resource | What |
|---|---|
| `aws_iam_role.capture_writer` | `estate-capture-writer`; trust names EXACTLY `user/Andrew_Berman` |
| `aws_iam_role_policy.capture_writer` | sole grant: `s3:PutObject` on `opal-estate-report/2026-07-31/text-input/*` |

**0 change / 0 destroy is load-bearing:** nothing existing is touched, so this apply cannot strand a
producer. The runner keeps its current grants and moves to day-first with its code rebuild.

## Pre-apply state, measured (not assumed)

- Schedule `estate-report-0900et`: **DISABLED** -- no live producer during this window.
- Bucket versioning: **Enabled**. Lifecycle: `abort-incomplete-mpu` only, **no** `NoncurrentVersionExpiration`
  (positive-controlled against `opal-data-bd`, which carries `expire-noncurrent-versions-90d`, and
  `opal-data-inf`, which carries `otp-prefix-expiry` -- so the call provably sees both expiry shapes).
- Runner cross-principal denies ALREADY hold under the current policy:
  `{day}/text-input/` -> `implicitDeny`, `{day}/signed-review/` -> `implicitDeny`,
  positive control `daily/` -> `allowed` (SEPARATE invocation).

## STEP 2 -- draft battery (simulate-custom-policy, policy NEVER attached)

One `--resource-arns` per invocation; each its own API call.

| # | Case | Verdict |
|---|---|---|
| ALLOW | `{today}/text-input/laptop/s.jsonl` | `allowed` |
| DENY 1 | `{past}/text-input/laptop/s.jsonl` -- cannot rewrite history | `implicitDeny` |
| DENY 2 | `{today}/signed-review/x.md` -- mid-key wildcard hazard | `implicitDeny` |
| DENY 3 | `{past}/manifest.json` -- rewrite through the INDEX | `implicitDeny` |
| DENY 4 | `{today}/manifest.json` (beyond floor) | `implicitDeny` |
| DENY 5 | `s3:DeleteObject` on the ALLOWED key (beyond floor) | `implicitDeny` |

**The ALLOW is the in-run positive control** -- it proves the simulator discriminates for this exact
policy, so the five denies are denials rather than an artifact. Not decorative: minutes earlier the
same battery via `file://` returned `InvalidInput` on all five, and a careless read of
"not `allowed`" would have scored four passes on a call that never evaluated anything.

## Steps -- ALL COMPLETE

- [x] `safe-apply.sh` -- **2 added, 0 changed, 0 destroyed.** comp-tagauthz PASSED (0 candidates carry
      an overwritable access-granting tag); tombstone-gate CLEAN (2 creates vs 7 tombstones).
- [x] **0-diff verified**: `No changes. Your infrastructure matches the configuration.`
- [x] **STEP 4** battery on APPLIED principals -- **10/10**, table below.
- [x] Tag `estate-report-v0.2.0` + push `--follow-tags`. **Sync verified in ONE invocation post-fetch:**
      ahead 0 / behind 0, `HEAD == origin/CLOUD == 144c051420`. (A first read said "2 ahead" off a
      stale remote-tracking ref; re-measured rather than reported.)
- [x] Report raw verdicts to CVO -- **hold (a) v3 lifts on CVO's read, not on mine.**

### A GATE REFUSED THIS APPLY ONCE, CORRECTLY -- recorded because the near-miss is the lesson

First `safe-apply` attempt **REFUSED**: *"could not produce a plan JSON to run the tag-authz gate ...
a gate that cannot evaluate must not pass. Refusing to apply. (Fail closed.)"*

Cause was **mine**: I shipped `capture_day` as REQUIRED with no default, and `safe-apply.sh:161` runs
its OWN internal var-less `terraform plan` to feed comp-tagauthz. That plan failed, so the gate could
not evaluate. **A REQUIRED NO-DEFAULT VARIABLE MAKES A MODULE UN-GATEABLE BY ANY WRAPPER THAT PLANS
IT WITHOUT VARS** -- likely to bite any future module that adds one.

The gate offered `TAGAUTHZ_OVERRIDE`. **Taking it would have been bypassing a live gate because my own
change broke its ability to evaluate** -- exactly what fail-closed exists to refuse. Fixed the module
instead: an unreachable sentinel default (`1970-01-01`) that lets the gate's var-less plan succeed
while preserving the fail-closed-loud property -- a forgotten `-var` grants a 1970 window and denies
today, and is self-diagnosing where a stale-but-plausible date would look legitimate. `@4222b84da2`.

### STEP 4 -- applied battery (`simulate-principal-policy`), one `--resource-arns` per invocation

| Principal | Case | Verdict |
|---|---|---|
| capture-writer | ALLOW `{today}/text-input/laptop/s.jsonl` | `allowed` |
| capture-writer | `{past}/text-input/...` -- cannot rewrite history | `implicitDeny` |
| capture-writer | `{today}/signed-review/x.md` | `implicitDeny` |
| capture-writer | `{past}/manifest.json` -- rewrite via the INDEX | `implicitDeny` |
| capture-writer | `{today}/manifest.json` | `implicitDeny` |
| capture-writer | `s3:DeleteObject` on the ALLOWED key | `implicitDeny` |
| capture-writer | `{today}/kimi-report/...` (runner's surface) | `implicitDeny` |
| runner | `{today}/text-input/...` -- **provenance** cross-deny | `implicitDeny` |
| runner | `{today}/signed-review/...` cross-deny | `implicitDeny` |
| runner | **POSITIVE CONTROL, separate invocation**: `daily/...` | `allowed` |

**Each principal carries its own separately-invoked positive control**, so every `implicitDeny` above
is a denial rather than an artifact of an undiscriminating call. Not decorative: the step-2 battery
via `file://` returned `InvalidInput` on all five cases, and reading "not `allowed`" as "denied"
would have scored four passes on a call that never evaluated anything.

**Applied truth, read off the live primitives (not the TF view):**
- policy Resource: `arn:aws:s3:::opal-estate-report/2026-07-31/text-input/*`, action `s3:PutObject` only
- trust Principal: `{"AWS": "arn:aws:iam::313476888478:user/Andrew_Berman"}` -- exactly one

## Deferred BEYOND this deploy, named so they are not mistaken for done

- **Fallback mutant** (CTO condition 2): break the assume-role path; the capture write must FAIL
  LOUD. If it succeeds, boto3 fell back to ambient admin and the role is decoration. Requires the
  capture tool's write path, which does not exist yet. **The role is NOT trusted until this runs.**
- **Overwrite mutant** (CTO condition 3): PutObject twice on one key -> versions 1->2, original intact.
- **Runner day-first rewrite** -- with the runner code rebuild, not here.

## Closure

**Status: CLOSED 2026-07-31T14:52Z.** No stranded leg: `2 added, 0 changed, 0 destroyed`, 0-diff
verified, tag pushed, sync confirmed at `144c051420`. Nothing begun that is not finished.

**WHAT THIS DEPLOY DOES *NOT* ESTABLISH -- stated so the closure is not over-read.** The role EXISTS
and its boundary is proven at the POLICY layer. It is **not yet proven in the PATH**:

- **The fallback mutant has NOT run** (CTO condition 2) -- it requires the capture tool's write path,
  which does not exist yet. Until it does, a boto3 silent fallback to ambient admin credentials would
  be indistinguishable from the role working. **THE ROLE IS NOT TRUSTED FOR ANYTHING UNTIL THAT RUNS**,
  and a decorative boundary is worse than none because it is believed.
- **The overwrite mutant has NOT run** (CTO condition 3): PutObject twice on one key -> versions 1->2
  with the original intact.
- **Nothing has ever been written through this role.** Zero objects exist under any `{day}/text-input/`.

So: **BOUNDARY PROVEN, PATH UNPROVEN.** A policy-layer battery cannot tell you the producer will
actually use the principal it was given -- that is the exact gap the fallback mutant exists to close.

---

# ADDENDUM -- LEG 2, 2026-07-31T15:10-15:25Z. Opened and CLOSED in the same session.

**Status: CLOSED.** `1 added, 0 changed, 1 destroyed` (inline policy replaced; role untouched),
0-diff verified, applied battery 11/11.

## Why a second leg existed

CVO ruled (135220Z, reaching me at 150113Z) that the date-literal shape was SUPERSEDED: it carried a
**daily apply forever**, making a production capture path whose grant renews only if a human
remembers -- CLAUDE.md's own scheduling law wearing IAM clothes. The time boundary moves to the
storage layer (versioning ON + no delete grants), where it is actually expressible.

## THE LEAK -- found on the DRAFT, before any apply

Re-authoring to the ruled `*/text-input/*` shape and probing it:

```
Resource ".../*/text-input/*"
PutObject {day}/signed-review/text-input/evil.md   ->  ALLOWED
PutObject {day}/kimi-report/text-input/evil.json   ->  ALLOWED
PutObject a/b/c/text-input/evil.md                 ->  ALLOWED
```

**IAM's `*` matches `/`.** `*/text-input/*` therefore means *any key containing `/text-input/` at any
depth* -- so the capture writer could write INSIDE `signed-review/` by nesting a segment. That is the
producer writing the reviewer surface: **signing its own capture**, which is the one boundary the
entire design rests on.

>> **IT WOULD HAVE SHIPPED GREEN. The specified adjacent-subfolder DENY passes over it:**
>> `{day}/signed-review/x.md` is correctly DENIED while `{day}/signed-review/text-input/x.md` is
>> ALLOWED. **The battery reports a clean boundary over an open one, with every verdict in it
>> honest.** Both CVO's floor and ~A's rewritten battery would have returned a clean pass. <<

`0.7.0_AE_CloudOps~A` reproduced it independently on a policy they authored themselves.

## The fix, and its own probed residual

`????-??-??/text-input/*` -- `?` is the single-character wildcard, pinning the day to ten date-shaped
characters so `/text-input/` must follow immediately.

**CVO then probed MY fix rather than accepting it**, and the residual is NAMED here because a residual
named in the design is a residual and one discovered later is a finding:
- `?` matches `/` too, so this is "any 10 chars with dashes at positions 5 and 8," not "one segment."
- **Every real surface is excluded by the shape of its own name** -- verified by probe, not reading:
  `signed-review` (pos 5 = `e`), `kimi-report` (pos 5 = `-` but pos 8 = `p`), `change-cochange`
  (pos 5 = `g`), `deployment-motion` (pos 5 = `o`); `manifest.json` is day-root and unreachable.
  **That is measured luck, not design. A SIXTH SUBFOLDER MUST BE RE-PROBED** -- a name with dashes at
  positions 5 and 8 would be reachable and nothing here would warn you.
- Accepted residual: a slash-bearing date-shaped prefix (`ab/d-ef-gh/text-input/x`) is allowed. It
  reaches no real surface, mints only junk top-level prefixes, is visible in any listing, and is
  provenance-harmless.
- **And the NAME misleads** (~A): "date-shaped" reads like a date constraint. `aaaa-aa-aa` is allowed.

## Applied battery -- 11/11, live role

3 expected-ALLOW (today, past-day-deliberate, device/session deep nesting) - 7 expected-DENY
(three NESTED probes, adjacent sibling, day-root manifest, DeleteObject, DeleteObjectVersion) -
1 residual expected-ALLOWED-and-named. Applied truth read off the live primitive:
`Sid=PutTextInputAnyDayNeverDelete`, `Resource=arn:aws:s3:::opal-estate-report/????-??-??/text-input/*`.

## Floor amendment ratified out of this (CVO 151702Z)

For any grant containing a mid-key wildcard the battery now includes **(i)** the NESTED probe -- the
forbidden sibling with the allowed segment appended underneath, the only invocation that
distinguishes `*` from a segment matcher -- and **(ii)** the RESIDUAL probe, one pathological
same-shape key, expected ALLOWED-AND-NAMED so the residual stays measured rather than assumed.

>> **A MID-KEY WILDCARD IS NOT A PATH-SEGMENT MATCHER: `*` IS NOT `[^/]*`, AND `?` IS NOT `[^/]`.** <<

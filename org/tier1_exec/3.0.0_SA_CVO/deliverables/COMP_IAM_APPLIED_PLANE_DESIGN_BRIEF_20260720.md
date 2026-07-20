# Design brief: comp-iam DESIRED + APPLIED (deploy-reality) coverage, regex-free

**Author:** 3.0.0_SA_CVO · **Date:** 2026-07-20 · **Route:** CVO -> CTO (comp-iam owner)
**Origin:** Andrew-direct question ("comp-iam is Terraform-focused; it should cover Terraform *and*
deployed reality. Wrap `aws iam` into it via a deterministic pattern that isn't brittle -- avoid regex
unless extremely stable."). Andrew chose "design brief -> CTO" (2026-07-20).
**Standing:** CVO is design/verify only here; comp-iam is CTO-owned tooling. This brief proposes; CTO
builds/gates; CVO verifies on land. Nothing in `iam_cli.py` was touched.

---

## 1. Problem

`comp-iam` is DESIRED-plane by construction: it parses Terraform (`org/modules/graph/iam_cli.py`, 355
`.tf` files) + boto3 source, and it says so on every rich surface (`PLANE: DESIRED (Terraform). This does
NOT read live AWS.`). That means it is blind to: applied/live state, resolved ARNs (it prints
`${aws_instance.astn.id}`), trust policies, tags, `RoleLastUsed`, out-of-band grants (console / other
IaC), the 22 policy blocks its parser cannot attach, and the 2 Deny statements it cannot parse (incl.
NEVER#1 cross-firm belts). Rule 22a exists precisely because of this gap. Andrew wants the APPLIED plane
folded in **deterministically and non-brittly** -- explicitly *not* by regex.

## 2. Key finding: the non-brittle pattern already exists in the estate -- this is CONSOLIDATION, not invention

Regex is the wrong frame because **IAM is structured JSON end-to-end and AWS ships its own decision
engine.** The deterministic pattern is *delegate, don't parse*. Three structured primitives cover
deployed reality with zero regex, and comp-iam already uses two:

| # | Concern | Primitive (structured, no regex) | Status in estate |
|---|---|---|---|
| 1 | Inventory ("what is live") | `iam get-account-authorization-details` -- one paginated op returns every role/group/user + inline + attached-managed + full policy docs + trust policy + tags, as JSON | **ALREADY WRITTEN**: `.tools/comp-tagauthz.py:269,289` calls it; header states the philosophy verbatim ("not from a hand-kept list") |
| 2 | Decision ("is X actually allowed") | `iam simulate-principal-policy` -- AWS's own evaluator (Deny/boundary/SCP/condition) | **ALREADY WRAPPED**: `iam_cli.py:537` `cmd_simulate`, 22a rules structural + offline mutant self-test `_simulate_self_test` `:685` (zero-AWS, deterministic) |
| 3 | Join (DESIRED <-> APPLIED) | exact string on `RoleName` / ARN | trivial; `name_prefix` roles need `startswith(prefix)` (bounded, stable) -- the ONLY pattern, and it is not a regex |

`get-account-authorization-details` also returns **GroupDetailList / UserDetailList** -- so it answers
Andrew's "role *or group*" natively; one call is a superset.

## 3. Proposed design: tri-planar comp-iam

- **Plane 1 -- DESIRED (TF parse).** Exists unchanged. "What our IaC intends to grant + code-parity gaps."
- **Plane 2 -- APPLIED-inventory (census).** `get-account-authorization-details` -> a **vintage-stamped**
  JSON census. Replaces the hand-kept file. Feeds `reconcile` (DESIRED-vs-LIVE drift, LIVE-ONLY roles,
  LIVE-ONLY actions, over-perm). Cheap, complete, deterministic. **A drift DETECTOR, not an authorization
  oracle** (it holds raw statements; it does not evaluate Deny).
- **Plane 3 -- APPLIED-decision (simulate).** Exists (`cmd_simulate`). The allow/deny *oracle* for a
  specific `(role, action, resource, condition)` -- delegates to AWS, incl. the Deny belts Plane 1 is
  blind to. Per-question, live, authenticated.

Planes 2 and 3 are distinct on purpose: **that separation IS Rule 22a's DESIRED != APPLIED != EXERCISED
ladder.** Never let the census-overlay masquerade as an allow/deny verdict.

## 4. Where you'd be tempted to regex -- and the structured alternative (so nobody does)

| Temptation | Structured, deterministic alternative |
|---|---|
| Parse ARNs by hand | Don't. Compare whole ARN strings; when you must split, `arn` is a fixed 6-field colon layout (`split(":",5)`), AWS-guaranteed -- not a regex |
| Reimplement policy evaluation (wildcards `digest/*`, Deny precedence, conditions) | Don't. `simulate-principal-policy` does the matching + precedence. You send `(action, resource, context)`; AWS returns the decision |
| Fuzzy-match TF role to live role | Exact `RoleName`/ARN string equality; `name_prefix` -> bounded `startswith`, small known population |

## 5. The real robustness problems (NONE are regex) + fixes

1. **Freshness / vintage -- the actual brittleness today.** `cmd_reconcile` (`iam_cli.py:751`) defaults to
   `docs/briefs/cmpaws-iam-axis-census-20260603.json` -- dated **2026-06-03** (~7 wk stale),
   **customer-role-scoped** (111 roles vs 158 TF), and **no machine-readable vintage field** (`_meta`
   present, no generated-date). comp-iam silently reconciles against a 7-week-old partial snapshot.
   FIX: census carries `_meta.{generated_utc, account, api}`; every APPLIED verdict prints a provenance
   header (`census vintage <ts> (age Xm) [FRESH|STALE]`, the comp-kuzu pattern); **fail-closed past a
   TTL** -> degrade to DESIRED-only, never answer APPLIED off a stale census. This is the single biggest
   robustness win and it is a vintage-discipline fix, not a parsing one.
2. **Auth/context degradation.** Many comp-iam call sites have no AWS creds (e.g. commit hook). APPLIED
   must degrade to "APPLIED UNAVAILABLE -- DESIRED-only" -- never error, never lie. `cmd_simulate` already
   lazy-imports boto3; generalize that posture to the census path.
3. **Multi-account.** `get-account-authorization-details` is per-account; the estate is multi-account
   (313476888478 + others). Loop the accounts. Deterministic, just more calls.
4. **Tier authority.** Keep census-overlay (detector) and simulate (oracle) as separate exit-code
   contracts so a cheap drift read is never quoted as an authorization proof.

## 6. Concrete build list

| Piece | Mechanism | Effort |
|---|---|---|
| `comp-iam refresh-census [--account N]` | lift comp-tagauthz's `get-account-authorization-details` call -> vintage-stamped JSON | low (generator exists) |
| Census `_meta` schema | `{generated_utc, account, api}` | trivial |
| APPLIED provenance header | print census vintage + age + FRESH/STALE on every live-plane verdict | low |
| Fail-closed / degrade | TTL gate + no-creds -> DESIRED-only, typed | low |
| Offline fixture test | record one `get-account-authorization-details` payload as a fixture; test census-build + reconcile deterministically (mirror `_simulate_self_test`) | low-med |
| `name_prefix` join | `startswith` over the prefix population | low |

## 7. Grounding (verified this session, HEAD 3740a8d8f)

- `iam_cli.py:537` `cmd_simulate` read in full -- boto3 `simulate_principal_policy`/`get_role`, 22a rules
  structural, typed exits (0/1/2), no regex. `:685` `_simulate_self_test` = stubbed offline mutant suite.
- `iam_cli.py:751` `cmd_reconcile` -- census overlay; `_DEFAULT_CENSUS` = the 06-03 file.
- Census file: `docs/briefs/cmpaws-iam-axis-census-20260603.json`, `Jun 3 14:47`, keys
  `['_meta','summary','roles']`, no generated/vintage field surfaced.
- `.tools/comp-tagauthz.py:269,289` -- `get-account-authorization-details` already in production use.
- Head-to-head sample role `astn-wsjft-orchestrator-role`: comp-iam prints `${aws_instance.astn.id}` /
  `${aws_s3_bucket.astn.arn}`; live resolves `i-059405dfefcb4b44a` / `opal-data-astn` /
  `astn-wsjft-alerts`; live-only facts (RoleId, trust=lambda.amazonaws.com, LastUsed 2026-07-20T07:15:05Z,
  tags, boundary=null, managed=[]) invisible to comp-iam; comp-iam-only facts (code->grant gap
  `s3:PutObject`, provenance `lambda_function.py:121`, 37 estate gaps) invisible to raw aws.

## 8. CVO honesty / residual unknowns

- **Not verified:** whether `get-account-authorization-details` in THIS estate returns `RoleLastUsed`
  (it does not by default -- that needs `get-role`/`list-roles` `--query RoleLastUsed`); if last-used is
  wanted in the census, it is a second structured call per role, still no regex.
- **Not verified:** the exact multi-account inventory (which account IDs beyond 313476888478 must be
  swept); CTO/CloudOps owns that enumeration.
- **Assumption:** comp-tagauthz's call is transferable as-is; CTO should confirm the shim/auth context
  matches comp-iam's runtime (`.tools/aws` PATH shim, Rule-22a false-deny modes do NOT apply to
  `get-account-authorization-details`, which is a read-not-a-decision).

## 9. Ask of CTO

Own the build/gate decision. If GO: the load-bearing robustness item is #5.1 (vintage-honesty +
fail-closed), not the generator (which already exists). CVO will verify on land against a fresh census +
a live simulate cross-check on a sample role, and confirm the census-overlay/oracle tier separation holds
its exit-code contract.

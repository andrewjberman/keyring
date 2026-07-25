# comp-iam Stage 7 Part 1: reconcile mechanism grounding — 0.8.0_AE_CloudComp~A

**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE

## Objective

CTO~Z's Stage 7 dispatch joined today's comp-iam tracer thread (Stages 1-6) to a week-old
CVO~Z applied-plane design brief (2026-07-20) + its verify (2026-07-22), hypothesizing that
`cmd_reconcile`'s `over-perm`/`live-only-action` figures are computed against the code-side
operation list Stages 2-6 fixed — meaning every number CVO~Z's 07-22 verify quoted would have
been computed against an under-reporting denominator. Part 1 was explicitly scoped as
grounding, not building: "read how over-perm and live-only-action are actually computed... If
my framing is wrong, say so — that is the deliverable for part 1."

## Compiler Tools

No code changed this window — pure source grounding (Grep + Read against `iam_cli.py`,
`extract_iam.py`, `comp_iam_census.py`, a repo-wide grep for `overperm_flags` write sites).
No compiler tool applies to a read-only grounding pass; the discipline substituting for one
was citing every claim to an exact file:line, per Rule 22.

## Work Completed

Read both CVO~Z artifacts in full first, per the dispatch's explicit instruction, before
touching source. Then traced `cmd_reconcile` (`iam_cli.py:1079-1208`) end to end:

- `_profiles, tf_roles, _gaps = _build()` (`iam_cli.py:1148`) — `_profiles`/`_gaps` are
  underscore-prefixed and never referenced again in the function body. Only `tf_roles` is used.
- `live-only-action` (`:1158`): live census actions vs `tfrole.grants(a)`
  (`extract_iam.py:1089`), which checks `IamRole.statements` — populated ENTIRELY by
  `_parse_terraform_iam()` (`extract_iam.py:2714`), zero contact with `lambda_profiles`/
  `ec2_profiles` (the boto3-source tracer Stages 2-6 fixed).
- `over-perm` (`:1146`): `r.get("overperm_flags") or []` — read directly off a census JSON
  field, not computed by comp-iam at all.

**CTO~Z's framing confirmed WRONG on the mechanism**: neither axis touches the code-side
operation list. This is a pure TF-policy-vs-live-policy comparison on both axes.

Then chased WHERE `overperm_flags` gets populated (not just read), since the dispatch's own
premise — "these numbers are wrong because of an under-reporting input" — needed a real answer
regardless of which input was actually at fault. Repo-wide grep found the field is a write
target ONLY in the OLD hand-kept census (`docs/briefs/cmpaws-iam-axis-census-20260603.json`,
the file CVO~Z's design brief explicitly replaces). `build_census()`
(`comp_iam_census.py:239-251`) — the CURRENT `refresh-census` generator, the one CVO~Z's 07-22
verify actually exercised — emits `role_name/arn/role_id/create_date/trust_policy/tags/
permissions_boundary/statements` and NO `overperm_flags` key, anywhere.

**Consequence, disclosed to both CTO~Z and CVO~Z**: `over-perm` reads structurally-guaranteed
`[]` for every role from every census the current generator produces — not because no
over-perm exists live, but because the field is absent from the schema. CVO~Z's 07-22 "0
over-perm" is accurate to what the code computes; the code computes it off a field that can
never be nonzero. This is a real, independent, higher-priority defect than CTO~Z's hypothesis
— but a DIFFERENT one, predating today's Stages 2-6 entirely (live since the applied-plane
build landed 07-20/22).

Also checked (bears on part 3's shape): no surface anywhere in `iam_cli.py` currently computes
"grant held (TF or live) but never traced in code" — `gaps` is MISSING-direction only. So
there is no EXISTING code-side-dependent reconcile-style surface to attach a Stage-6
DEFERRED/UNTRACED row to; part 3 as scoped needs CTO~Z's call on shape before it can be built.

## Files Modified

None. Grounding-only turn.

## Blockers

Held Stage 7 parts 2/3 pending CTO~Z's direction — building against a premise just disproven
in the same turn would have wasted the work and repeated the exact "ground the mechanism, not
just the symptom" failure Rule 22 exists to prevent. Reported the disproof plus the real
finding to both CTO~Z and CVO~Z; awaiting redirect.

## Current State

Stage 7 Part 1 is answered and reported. Three options put to CTO~Z: (a) fix the
`overperm_flags` gap (the real, higher-priority defect found); (b) build a new code-side-
dependent "unused grant" surface that would actually BE the deletion-hazard reconcile CTO~Z
wants; (c) close Stage 7 here since the original premise didn't hold. No code changed. Stages
1-6 remain committed and closed pending CVO~Z's Stage-6 verify, unaffected by this finding.

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Direction on (a)/(b)/(c) above.
2. **[3.0.0_SA_CVO~Z]** FYI'd directly — the overperm_flags gap touches your own 07-22 quoted
   numbers (accurate to the code, not to live reality); no action requested unless you want to
   re-verify the census schema independently.
3. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by for CTO~Z's redirect.

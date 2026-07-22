#!/usr/bin/env python3
"""
comp-iam -- IAM permission cross-reference for Lambda and EC2 scripts.

Scans Lambda source files and gold EC2 scripts for AWS operations,
then cross-references against Terraform IAM policy documents.
Flags cases where a script calls an operation the role may not permit.

Usage:
    comp-iam gaps                  # show all detected permission gaps (default)
    comp-iam roles                 # list all IAM roles found in Terraform
    comp-iam services              # list all services scanned with their operations
    comp-iam service <name>        # show operations for one service
    comp-iam role <name>           # show granted actions for one role
    comp-iam stats                 # summary counts
    comp-iam resource-sweep        # estate-wide: ACTION held, RESOURCE not (exit 1 if flagged)

Verdicts (NFRA_COMPIAM_RESOURCE, 2026-07-10). Before this, every mode matched the
ACTION NAME and never compared the RESOURCE ARN, so `s3:GetObject [GRANTED]` printed
for a call that returned AccessDenied. The verdict was invariant to the truth.
    GRANTED                              action AND resource match
    GRANTED-BROAD                        Resource:'*' -- EXCLUDED, NOT CLEARED
    GRANTED-ACTION / UNGRANTED-RESOURCE  action held on OTHER resources
    UNGRANTED                            no matching action
    UNRESOLVABLE-RESOURCE                could not be checked -- and says so
"""

import argparse
import json
import re
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_iam import build_iam_report, PermissionGap  # noqa: E402
from org.modules.graph import extract_iam as EI  # noqa: E402


def _build():
    return build_iam_report(_WORKSPACE)


def cmd_gaps(args):
    profiles, roles, gaps = _build()

    # CTO ruling 2026-07-10: `gaps` may NOT keep answering the ACTION-ONLY question
    # in silence. Two surfaces of one binary that disagree is the weakest-copy
    # problem inside a single tool -- `service`/`resource-sweep` now compare the
    # RESOURCE; `gaps` still does not. Say so on the way in, not in a changelog.
    _print_plane_banner()
    print("SURFACE: gaps -- ACTION-ONLY. It does NOT compare resource ARNs.")
    print("  A gap is absent here whenever the role holds the action ANYWHERE, even on")
    print("  a bucket the call never touches. For the resource question use")
    print("  `comp-iam resource-sweep` or `comp-iam service <fn>`.")
    print("=" * 78)
    print()

    service_filter = (args.service or "").lower()

    filtered = [g for g in gaps if not service_filter or service_filter in g.service.lower()]

    # Partition by severity: real MISSING-permission gaps vs coverage-UNKNOWN
    # (unmodeled service) vs DENY-PRESENT (granted-but-Deny, verify effective).
    errors = [g for g in filtered if g.severity == "ERROR"]
    unmodeled = [g for g in filtered if g.severity == "UNMODELED"]
    deny_present = [g for g in filtered if g.severity == "DENY-PRESENT"]

    # Only a true "all clear" when there are NO error gaps AND coverage is full
    # (no unmodeled services) AND no Deny ambiguity. Otherwise we must NOT print
    # a confident "no gaps" -- that's the false-green this fix exists to kill.
    if not filtered:
        if service_filter:
            print(f"No findings for service filter: {service_filter}")
        else:
            print("No permission gaps detected.")
            print(f"  ({len(profiles)} services scanned, {len(roles)} IAM roles parsed)")
        return

    if errors:
        print(f"PERMISSION GAPS ({len(errors)} missing-permission)")
        print()
        by_service: dict[str, list[PermissionGap]] = {}
        for g in errors:
            by_service.setdefault(g.service, []).append(g)
        for svc, svc_gaps in sorted(by_service.items()):
            print(f"  {svc}  (role: {svc_gaps[0].iam_role})")
            for gap in svc_gaps:
                print(f"    !! MISSING: {gap.iam_action}")
                print(f"       Called via: {gap.source_pattern}")
                print(f"       At: {gap.file_path}:{gap.line_number}")
                print(f"       Fix: add '{gap.iam_action}' to {gap.iam_role} policy in iam.tf")
            print()
    else:
        print("No MISSING-permission gaps among MODELED services.")
        print()

    if deny_present:
        print(f"DENY-PRESENT ({len(deny_present)}) -- ALLOW granted but a Deny statement matches; verify effective-allow:")
        for g in deny_present:
            print(f"    ?? {g.service} [{g.iam_role}] {g.iam_action}")
            print(f"       {g.source_pattern}")
            print(f"       At: {g.file_path}:{g.line_number}")
        print("    (resource/condition-precise resolution = census-backed reconcile tier)")
        print()

    if unmodeled:
        svcs = sorted({g.iam_action.split(':')[0] for g in unmodeled})
        print(f"COVERAGE-UNKNOWN ({len(unmodeled)}) -- boto3 services comp-iam does NOT model: {svcs}")
        print("    These produce NO gap signal either way -- comp-iam CANNOT verify their IAM perms.")
        for g in unmodeled:
            print(f"    ?? {g.service} [{g.iam_role}] {g.iam_action}  ({g.file_path}:{g.line_number})")
        print()

    print(f"Total: {len(errors)} missing | {len(deny_present)} deny-present | "
          f"{len(unmodeled)} coverage-unknown  across {len({g.service for g in filtered})} service(s)")


def cmd_roles(args):
    _, roles, _ = _build()

    if not roles:
        print("No IAM roles found in Terraform.")
        return

    print(f"IAM ROLES ({len(roles)} found)")
    print()
    for role_name, role in sorted(roles.items()):
        allow_count = sum(len(s.actions) for s in role.statements if s.effect.lower() == 'allow')
        print(f"  {role_name}")
        print(f"    tf_resource: {role.tf_resource}")
        print(f"    statements: {len(role.statements)}  ({allow_count} Allow actions)")
        print(f"    source: {role.source_file}")
    print()


def cmd_services(args):
    profiles, _, _ = _build()

    if not profiles:
        print("No services found.")
        return

    print(f"SERVICES ({len(profiles)} found)")
    print()
    for p in sorted(profiles, key=lambda x: x.name):
        role_str = p.iam_role or "(role not mapped)"
        op_count = len(set(a for op in p.operations for a in op.iam_actions))
        print(f"  {p.name}  [{p.service_type}]")
        print(f"    role: {role_str}")
        print(f"    unique IAM actions used: {op_count}")
        print(f"    source files: {len(p.source_files)}")
    print()


def cmd_service(args):
    profiles, roles, gaps = _build()
    # ADHC_COMPIL_V5.001: normalize underscore<->dash so Terraform-resource-style
    # lookups (e.g. `bd_exporter` matching role `bd-exporter-ec2-role`) work
    # symmetrically. Anchor: today's AE 0.6.1 manual IAM additions
    # (b00e2733e + 053bba6f7) where role-name dashes vs TF-resource underscores
    # blocked direct `comp-iam service <terraform-name>` lookup.
    name = args.name.lower().replace("_", "-")

    matches = [p for p in profiles if name in p.name.lower().replace("_", "-")]
    if not matches:
        # ADHC_COMPIL_V4.013: fall through to EC2/IAM role names when Lambda
        # profile lookup fails. Reuses the existing roles dict (no new index).
        # Anchor incidents: 2026-04-16 AE 0.6 dh3_dh7_dispatcher_hygiene
        # ('No service matching' for gold runner EC2); 2026-05-08 AE 0.7
        # INFETL.011 RAVC1 (inf-gold-trigger catalog miss).
        role_matches = {k: v for k, v in roles.items() if name in k.lower().replace("_", "-")}
        if role_matches:
            for role_name, role in sorted(role_matches.items()):
                print(f"SERVICE: {role_name}  [iam-role]")
                print(f"  IAM role: {role_name}")
                print(f"  tf_resource: {role.tf_resource}")
                print(f"  source: {role.source_file}")
                print(f"  statements: {len(role.statements)}")
                print()
                for i, stmt in enumerate(role.statements, 1):
                    print(f"  Statement {i}: {stmt.effect}")
                    print(f"    Actions ({len(stmt.actions)}):")
                    for a in sorted(stmt.actions):
                        print(f"      {a}")
                    if stmt.resources:
                        scoped = stmt.scoping_condition()
                        tag = (f"  [TAG-SCOPED via Condition {scoped} -- NOT broad]"
                               if stmt.is_resource_scoped_by_condition() else "")
                        print(f"    Resources ({len(stmt.resources)}):{tag}")
                        for r in stmt.resources[:5]:
                            print(f"      {r}")
                        if len(stmt.resources) > 5:
                            print(f"      ... and {len(stmt.resources) - 5} more")
                    if stmt.condition:
                        print(f"    Condition: {stmt.scoping_condition() or stmt.condition}")
                print()
            return

        # Total miss — emit helpful candidate list
        print(f"No service matching '{args.name}'")
        print()
        print(f"  Lambda services ({len(profiles)}):")
        for p in sorted(profiles, key=lambda p: p.name)[:15]:
            print(f"    {p.name}")
        if len(profiles) > 15:
            print(f"    ... and {len(profiles) - 15} more (use 'comp-iam services' to list all)")
        print()
        print(f"  IAM roles ({len(roles)}):")
        for k in sorted(roles.keys())[:15]:
            print(f"    {k}")
        if len(roles) > 15:
            print(f"    ... and {len(roles) - 15} more (use 'comp-iam roles' to list all)")
        return

    _print_plane_banner()
    print()
    for profile in matches:
        print(f"SERVICE: {profile.name}  [{profile.service_type}]")
        print(f"  IAM role: {profile.iam_role or '(not mapped)'}")
        print(f"  Source files: {', '.join(profile.source_files)}")
        print()

        if not profile.operations:
            print("  No AWS operations detected.")
            continue

        # Deduplicate operations by (action, file, line)
        seen = set()
        role = roles.get(profile.iam_role) if profile.iam_role else None
        tally: dict[str, int] = {}
        n_checked = 0
        print(f"  OPERATIONS ({len(profile.operations)}):")
        for op in profile.operations:
            for action in op.iam_actions:
                key = (action, op.file_path, op.line_number)
                if key in seen:
                    continue
                seen.add(key)

                if role is None:
                    status, note = "UNKNOWN", "role not mapped"
                else:
                    status, _stmt, note = role.resource_verdict(
                        action, op.resource_arn, op.resource_exact)
                n_checked += 1
                tally[status] = tally.get(status, 0) + 1

                print(f"    {action}  [{status}]")
                print(f"      via: {op.source_pattern} at {op.file_path}:{op.line_number}")
                if op.resource_arn:
                    star = "" if op.resource_exact else "   (pattern; '*' = runtime value)"
                    print(f"      resource: {op.resource_arn}{star}")
                if op.resource_expr:
                    print(f"      from: {op.resource_expr}")
                if note:
                    print(f"      note: {note}")

        # DENOMINATOR. A tool that cannot state what it could not check has not checked.
        n_stmts = len(role.statements) if role else 0
        print()
        print(f"  RESOURCE CHECK: checked {n_checked} calls across {n_stmts} statements; "
              f"{tally.get(EI.V_UNRESOLVABLE, 0)} unresolvable")
        for v in (EI.V_GRANTED, EI.V_GRANTED_BROAD, EI.V_UNGRANTED_RESOURCE,
                  EI.V_UNGRANTED, EI.V_UNRESOLVABLE, "UNKNOWN"):
            if tally.get(v):
                flag = ""
                if v == EI.V_GRANTED_BROAD:
                    flag = "   <- NOT CLEARED: a wildcard role cannot be falsified by a resource check"
                elif v == EI.V_UNGRANTED_RESOURCE:
                    flag = "   <- the action is held on OTHER resources"
                print(f"    {tally[v]:>3}  {v}{flag}")
        print()


def cmd_role(args):
    _, roles, _ = _build()
    name = args.name.lower()

    matches = {k: v for k, v in roles.items() if name in k.lower()}
    if not matches:
        print(f"No role matching '{args.name}'")
        return

    for role_name, role in sorted(matches.items()):
        print(f"ROLE: {role_name}")
        print(f"  tf_resource: {role.tf_resource}")
        print(f"  source: {role.source_file}")
        print(f"  statements: {len(role.statements)}")
        print()

        for i, stmt in enumerate(role.statements, 1):
            print(f"  Statement {i}: {stmt.effect}")
            print(f"    Actions ({len(stmt.actions)}):")
            for a in sorted(stmt.actions):
                print(f"      {a}")
            if stmt.resources:
                scoped = stmt.scoping_condition()
                tag = (f"  [TAG-SCOPED via Condition {scoped} -- NOT broad]"
                       if stmt.is_resource_scoped_by_condition() else "")
                print(f"    Resources: {', '.join(stmt.resources[:3])}{tag}")
                if len(stmt.resources) > 3:
                    print(f"      ... +{len(stmt.resources)-3} more")
            if stmt.condition:
                print(f"    Condition: {stmt.scoping_condition() or stmt.condition}")
        print()


def cmd_stats(args):
    profiles, roles, gaps = _build()

    print("IAM CROSS-REFERENCE STATS")
    print(f"  IAM roles parsed:     {len(roles)}")
    print(f"  Services scanned:     {len(profiles)}")
    print(f"  Lambda services:      {sum(1 for p in profiles if p.service_type == 'lambda')}")
    print(f"  EC2 services:         {sum(1 for p in profiles if p.service_type == 'ec2')}")
    print(f"  Total operations:     {sum(len(p.operations) for p in profiles)}")
    print(f"  Permission gaps:      {len(gaps)}")
    if gaps:
        print()
        print("  Services with gaps:")
        by_svc = {}
        for g in gaps:
            by_svc.setdefault(g.service, []).append(g.iam_action)
        for svc, actions in sorted(by_svc.items()):
            print(f"    {svc}: {', '.join(sorted(set(actions)))}")


def _print_plane_banner():
    """State the plane, the trees read, and what could not be attached.

    A tool that cannot state which trees it read cannot be trusted to have read
    yours (CTO, 2026-07-10). The attachment census exists because a bare
    `continue` silently discarded 26 of 330 `aws_iam_role_policy` blocks -- and
    one of them, OpalDataPMCacheBustAccess, produced this tool's only
    UNGRANTED-RESOURCE flag. The first draft of this banner blamed that flag on
    the DESIRED-vs-APPLIED plane gap. The plane gap is REAL and it did NOT cause
    that flag: the policy is Terraform-declared, inside a scanned tree, and was
    dropped by the role-reference parser. A true explanation attached to a symptom
    it did not produce would have taught every reader to dismiss a scan bug as
    console drift. Cite no measurement whose mechanism you have not established.
    """
    st = EI._ATTACH_STATS
    print("=" * 78)
    print("PLANE: DESIRED (Terraform). This does NOT read live AWS.")
    print("  comp-iam parses Terraform. It cannot tell landed from planned, and it is")
    print("  blind to any grant Terraform does not declare. A live")
    print("  `simulate-principal-policy` is the APPLIED plane; exercising the call is")
    print("  the only EXERCISED evidence. Rule 22a: DESIRED != APPLIED != EXERCISED.")
    print("  That rule does NOT retire because this tool now compares resources.")
    print()
    print(f"  scanned {len(EI.TF_SCAN_ROOTS)} trees ({st['tf_files']} .tf files): "
          f"{', '.join(EI.TF_SCAN_ROOTS)}")
    print(f"  policy blocks attached {st['attached']}; "
          f"NOT ATTACHED {st['dropped']}  (a role ref this parser cannot resolve); "
          f"standalone {st['standalone']}  (aws_iam_policy -- no role by design)")
    if st['dropped']:
        print("  ^ statements comp-iam has NEVER SEEN. Its verdicts are computed WITHOUT")
        print("    them, so a role may hold a grant this tool cannot find. Run")
        print("    `comp-iam attach-census` for the list. NOT a plane limitation --")
        print("    a parser limitation, and it is stated rather than swallowed.")
    # CTO arch-gate 2026-07-10 (a): a tool that cannot see a Deny must SAY SO on every
    # invocation, until N=0. NEVER#1's runtime limb IS an IAM Deny; the Deny overlay
    # exists so an explicit Deny never reads as GRANTED. It cannot warn on a Deny it
    # never parsed -- and an instrument that goes quiet about what it could not read
    # has taught the reader that quiet means allowed.
    if st['deny_unparsed']:
        print()
        print(f"  DENY-OVERLAY INCOMPLETE: {st['deny_unparsed']} deny statement(s) unparsed "
              f"({'; '.join(sorted(st['deny_reasons']))})")
        print("  ^ comp-iam CANNOT answer 'is this denied?'. Among these are NEVER#1's")
        print("    cross-firm Deny belts. Asking this tool about a Deny it never parsed")
        print("    returns SILENCE, and silence must not be read as allowed.")
    print("=" * 78)


def cmd_attach_census(args):
    """List every aws_iam_role_policy block comp-iam could NOT attach to a role."""
    _build()
    st = EI._ATTACH_STATS
    print("comp-iam attach-census -- policy blocks NOT attached to any role")
    print("=" * 78)
    print(f"scanned trees: {', '.join(EI.TF_SCAN_ROOTS)}")
    _rp = st['attached'] + st['dropped']
    print(f"{st['tf_files']} .tf files; {_rp} aws_iam_role_policy + "
          f"{st['standalone']} standalone aws_iam_policy = {_rp + st['standalone']} blocks")
    print(f"  {st['attached']:>4}  attached")
    print(f"  {st['dropped']:>4}  NOT ATTACHED  (invisible to every comp-iam verdict)")
    print(f"  {st['standalone']:>4}  standalone aws_iam_policy -- no `role =` BY DESIGN, attached")
    print("        via aws_iam_role_policy_attachment. NOT a drop; a different world.")
    print()
    for d in st['dropped_detail']:
        print(f"  {d}")
    print()
    print("Each line is a policy whose statements are absent from the role's grant set.")
    if st['deny_unparsed']:
        print()
        print(f"DENY-OVERLAY INCOMPLETE: {st['deny_unparsed']} deny statement(s) unparsed")
        for d in st['deny_detail']:
            print(f"  DENY  {d}")
        print()
        print("A DENY here is worse than an ALLOW. comp-iam's Deny overlay exists so an")
        print("explicit Deny never reads as GRANTED -- and it cannot warn on a Deny it")
        print("never parsed. NEVER#1's runtime limb IS an IAM Deny. Asking this tool")
        print("'is cross-firm access denied?' returns SILENCE. Silence is not allowed.")
    return 1 if st['dropped'] else 0


def cmd_resource_sweep(args):
    """Estate-wide: which calls does a role hold the ACTION for, but not the RESOURCE?

    Answers the question `comp-iam service` could not: `s3:GetObject [GRANTED]` for a
    call that returns AccessDenied, because the verdict matched the action name and
    never compared the resource ARN.

    Driven by the ACTUAL call site's resolved ARN -- not by grepping source for bucket
    names. A bucket NAMED in code is not a call MADE (log strings, sibling-deploy
    constants, dead code); binding the check to a name pattern instead of to the call's
    resource is `action` for `resource` one layer down, inside the sweep hunting it.
    """
    profiles, roles, _ = _build()
    lambdas = [p for p in profiles if p.service_type == 'lambda']

    flagged, broad_roles = [], set()
    tally: dict[str, int] = {}
    n_calls = n_lambdas = 0
    unmapped = [p.name for p in lambdas if not (p.iam_role and p.iam_role in roles)]
    # A lambda with a role but ZERO detected operations is NOT cleared -- it is an
    # empty set. comp-iam scans ONE source file per lambda (the entry point named in
    # lambda-source-map.json); a boto3 call in a sibling helper module is invisible.
    # Measured 2026-07-10: opal-inf-value-parity's lambda_function.py is 58 lines and
    # binds no boto3 client, while its sibling axes_s3.py does `boto3.client("s3")`
    # and the dir names opal-data-{bd,cot,inf}. Reporting that lambda as "0 calls,
    # 0 flags" without saying so is a clean bill from an empty set.
    zero_op = [p.name for p in lambdas
               if p.iam_role and p.iam_role in roles and not p.operations]

    for p in lambdas:
        role = roles.get(p.iam_role) if p.iam_role else None
        if role is None:
            continue
        n_lambdas += 1
        seen = set()
        for op in p.operations:
            for action in op.iam_actions:
                key = (action, op.file_path, op.line_number)
                if key in seen:
                    continue
                seen.add(key)
                if args.s3_only and not action.lower().startswith('s3:'):
                    continue
                n_calls += 1
                verdict, _stmt, note = role.resource_verdict(
                    action, op.resource_arn, op.resource_exact)
                tally[verdict] = tally.get(verdict, 0) + 1
                if verdict == EI.V_UNGRANTED_RESOURCE:
                    flagged.append((p.name, role.role_name, action, op, note))
                elif verdict == EI.V_GRANTED_BROAD:
                    broad_roles.add(role.role_name)

    # ROLE-LEVEL census, a DIFFERENT population from the call-level tally above:
    # roles that hold an s3 action on Resource:'*'. A wildcard role can never be
    # flagged by a resource check whether or not we detected a call in its source.
    # Reporting only the call-level number would understate the blind spot.
    wildcard_s3_roles = set()
    for rn, role in roles.items():
        for s in role.statements:
            if s.effect.lower() != 'allow' or not any(r == '*' for r in s.resources):
                continue
            if s.is_resource_scoped_by_condition():
                continue
            if any(EI._action_pattern_matches(a, 's3:GetObject') for a in s.actions):
                wildcard_s3_roles.add(rn)
                break

    _print_plane_banner()
    if flagged:
        print(f"\nFLAGGED ({len(flagged)}) -- the action is held on OTHER resources:\n")
        for name, rolename, action, op, note in flagged:
            print(f"  {name}")
            print(f"    role:     {rolename}")
            print(f"    action:   {action}")
            print(f"    resource: {op.resource_arn}"
                  f"{'' if op.resource_exact else '   (pattern)'}")
            print(f"    at:       {op.file_path}:{op.line_number}   [{op.source_pattern}]")
            print(f"    why:      {note}")
            print()
    else:
        print("\nFLAGGED (0)\n")

    print("-" * 78)
    print(f"DENOMINATOR: {n_lambdas} lambdas with a mapped role; {n_calls} calls checked"
          f"{'  (s3 only)' if args.s3_only else ''}")
    total = 0
    for v in (EI.V_GRANTED, EI.V_GRANTED_BROAD, EI.V_UNGRANTED_RESOURCE,
              EI.V_UNGRANTED, EI.V_UNRESOLVABLE):
        total += tally.get(v, 0)
        print(f"  {tally.get(v, 0):>4}  {v}")
    # The denominator must CLOSE. A tally that does not sum to the checked count is
    # the same class of defect as a verdict that ignores the resource.
    assert total == n_calls, f"tally {total} != checked {n_calls}"
    print(f"  {'----':>4}")
    print(f"  {total:>4}  = calls checked  (closes)")
    print(f"\n  {len(unmapped):>4}  lambdas SKIPPED -- no mapped role (not checked, NOT cleared)")
    print(f"  {len(zero_op):>4}  lambdas with a role but ZERO detected calls "
          f"(an EMPTY SET, NOT cleared)")
    print("        ^ comp-iam scans ONE source file per lambda (the entry point in")
    print("          lambda-source-map.json). A boto3 call in a sibling helper module")
    print("          is invisible to it. e.g. opal-inf-value-parity: lambda_function.py")
    print("          binds no boto3, while sibling axes_s3.py does.")
    print(f"  {len(broad_roles):>4}  roles whose matched statement was Resource:'*' "
          f"(among calls above)")
    print(f"  {len(wildcard_s3_roles):>4}  roles hold an s3 action on Resource:'*' "
          f"ANYWHERE -- of {len(roles)} roles total")
    print("        ^ a DIFFERENT, larger population: a wildcard role cannot be")
    print("          flagged by any resource check, whether or not we saw a call.")
    print()
    print("BOUNDS -- hold them:")
    print("  (a) A wildcard role cannot be flagged by ANY resource check. Those roles")
    print("      are EXCLUDED from the flag set and are NOT cleared. Own finding.")
    print("  (b) An UNRESOLVABLE resource is not a pass. It is a call whose ARN is")
    print("      computed at runtime; this tool states that it could not check it.")
    print("  (c) A FLAGGED call is a CANDIDATE, not a failure. Confirm each on the")
    print("      live plane, WITH a positive control on a resource the role DOES hold:")
    print("      aws iam simulate-principal-policy --policy-source-arn <role> \\")
    print("        --action-names <action> --resource-arns <exact key>")
    if args.show_broad:
        print("\nRoles holding s3 on Resource:'*' (NOT CLEARED):")
        for r in sorted(wildcard_s3_roles):
            print(f"  {r}")
    return 1 if flagged else 0


def cmd_simulate(args):
    """The APPLIED-plane wrapper (NFRA_INSTDRILL item 1b, 2026-07-14) -- the three safe-invocation
    rules of CLAUDE.md 22a made STRUCTURAL instead of prose:

      RULE 1  ONE resource ARN per call. A call carrying 2+ --resource-arns flips the HELD ones to
              implicitDeny (measured; the instrument's own false-deny mode 1). Structural here:
              one positional ARN, and a comma-joined smuggle is refused with the citation.
      RULE 2  The POSITIVE CONTROL runs as a SEPARATE INVOCATION -- a control batched with its
              target is corrupted by its own presence. Auto-derived from the role's DESIRED grants
              when possible, or --control-arn; skipping it (--no-control) downgrades any DENY
              verdict to UNPROVEN, never silently.
      RULE 3  A conditioned statement with no --context evaluates implicitDeny BYTE-IDENTICAL to a
              real deny (false-deny mode 2). The response's missingContextValues IS the detector:
              non-empty => verdict CONDITIONED-UNEVALUATED (rc=2), never DENIED.

    PLANE: APPLIED (live simulate-principal-policy at call time). Still not EXERCISED -- only
    running the real call is. SCPs/permission boundaries evaluate per the API's semantics.
    Read-only: simulate-principal-policy + get_role mutate nothing.

    Exit: 0 ALLOWED (control-proven when run) | 1 DENIED (control-proven) | 2 CONDITIONED-
    UNEVALUATED / INSTRUMENT-SUSPECT / UNPROVEN -- never a silent verdict from a suspect instrument.
    """
    if "," in args.resource_arn:
        print("REFUSED: one resource ARN per call (CLAUDE.md 22a false-deny mode 1 -- a call")
        print("  carrying 2+ --resource-arns flips the HELD ones to implicitDeny). Run each ARN")
        print("  as its own invocation; that isolation is the point of this wrapper.")
        return 2

    ctx_entries = []
    for c in (args.context or []):
        # Key=type:value[,value...]  e.g. aws:SourceVpc=string:vpc-123
        try:
            key, rest = c.split("=", 1)
            ctype, vals = rest.split(":", 1)
            ctx_entries.append({"ContextKeyName": key.strip(),
                                "ContextKeyValues": [v.strip() for v in vals.split(",")],
                                "ContextKeyType": ctype.strip()})
        except ValueError:
            print(f"REFUSED: malformed --context '{c}' (want Key=type:val[,val...], e.g. "
                  f"aws:SourceVpc=string:vpc-123)")
            return 2

    client = getattr(args, "_client", None)
    if client is None:
        import boto3  # lazy; the self-test injects a stub
        client = boto3.client("iam")

    role = args.role
    role_arn = role if role.startswith("arn:") else None
    if role_arn is None:
        try:
            role_arn = client.get_role(RoleName=role)["Role"]["Arn"]
        except Exception as e:
            print(f"ROLE RESOLUTION FAILED for '{role}': {e}")
            return 2

    def _one_call(arn, label):
        """One isolated simulate invocation -> (decision, missing_context, raw)."""
        resp = client.simulate_principal_policy(
            PolicySourceArn=role_arn, ActionNames=[args.action],
            ResourceArns=[arn], **({"ContextEntries": ctx_entries} if ctx_entries else {}))
        ev = (resp.get("EvaluationResults") or [{}])[0]
        decision = ev.get("EvalDecision", "?")
        missing = [m.get("ContextKeyName", str(m)) if isinstance(m, dict) else str(m)
                   for m in ev.get("MissingContextValues", [])]
        print(f"  [{label}] {args.action} on {arn}")
        print(f"      decision={decision}" + (f"  missingContextValues={missing}" if missing else ""))
        return decision, missing

    print("=" * 78)
    print("PLANE: APPLIED (live simulate-principal-policy, evaluated now). Not EXERCISED --")
    print("  only running the real call is. One ARN per invocation, by construction.")
    print("=" * 78)
    t_dec, t_missing = _one_call(args.resource_arn, "TARGET")

    if t_missing:
        print("\nVERDICT: CONDITIONED-UNEVALUATED -- a conditioned statement was evaluated with")
        print("  no context, and that returns implicitDeny BYTE-IDENTICAL to a real deny")
        print("  (22a false-deny mode 2). This is NOT a deny verdict. Re-run with:")
        for k in t_missing:
            print(f"    --context {k}=<type>:<value>")
        return 2

    # ---- the positive control: a SEPARATE invocation, never batched with the target ----
    control_arn = args.control_arn
    control_note = ""
    if not control_arn and not args.no_control:
        # auto-derive from DESIRED: a concrete (non-*) resource this role holds for this action.
        # Best-effort over the TF-parsed roles; any failure just leaves control_arn None (-> UNPROVEN,
        # never a silent pass). Uses only the real IamRole API (.role_name / .statements / .actions
        # / .resources / .effect) -- no invented method.
        try:
            report = _build()
            al = args.action.lower()
            for r in getattr(report, "roles", []):
                if not (r.role_name == role or role_arn.endswith("/" + r.role_name)):
                    continue
                for stmt in r.statements:
                    if stmt.effect.lower() != "allow":
                        continue
                    holds = any(a == "*" or a.lower() == al or
                                ("*" in a and re.fullmatch(re.escape(a.lower()).replace(r"\*", ".*"), al))
                                for a in stmt.actions)
                    if not holds:
                        continue
                    for res in stmt.resources:
                        if "*" not in res and res != args.resource_arn:
                            control_arn = res
                            control_note = " (auto-derived from DESIRED grants)"
                            break
                    if control_arn:
                        break
                break
        except Exception:
            control_arn = None
    if control_arn == args.resource_arn:
        control_arn, control_note = None, ""

    if control_arn:
        c_dec, c_missing = _one_call(control_arn, f"CONTROL{control_note}")
        control_ok = (c_dec == "allowed" and not c_missing)
    elif args.no_control:
        control_ok = None
        print("\n  CONTROL SKIPPED (--no-control).")
    else:
        control_ok = None
        print("\n  NO CONTROL DERIVABLE from DESIRED grants -- pass --control-arn <arn the role")
        print("  is KNOWN to hold>. A deny with no proven-able-to-allow instrument is UNPROVEN.")

    print()
    if t_dec == "allowed":
        print("VERDICT: ALLOWED (APPLIED plane)." +
              ("" if control_ok in (True, None) else "  (control anomaly noted below)"))
        if control_ok is False:
            print("  NOTE: the control DENIED on a resource DESIRED says is held -- census/TF")
            print("  drift or missing context on the control; does not weaken an ALLOWED target.")
        return 0
    if control_ok is True:
        print(f"VERDICT: DENIED ({t_dec}), control-proven -- the instrument demonstrably CAN say")
        print("  allowed for this role, so this deny discriminates. APPLIED plane.")
        return 1
    print(f"VERDICT: DENIED-UNPROVEN ({t_dec}) -- rc=2, NOT 1: no passing positive control ran")
    print("  in isolation, so this deny is indistinguishable from an instrument failure")
    print("  (stale principal, missing context on a conditioned allow, wrong role).")
    print("  An instrument that cannot fail is not an instrument; one that cannot PASS is not one either.")
    return 2


def _simulate_self_test():
    """Offline mutant suite for cmd_simulate (stubbed client; zero AWS). Every case is a lie the
    live instrument has actually told (22a's two false-deny modes + the new-resource fail-GREEN)."""
    import types as _t

    class Stub:
        def __init__(self, decisions, missing=None):
            self.decisions = dict(decisions)   # arn -> decision
            self.missing = dict(missing or {}) # arn -> [keys]
            self.calls = []
        def get_role(self, RoleName):
            return {"Role": {"Arn": f"arn:aws:iam::123:role/{RoleName}"}}
        def simulate_principal_policy(self, PolicySourceArn, ActionNames, ResourceArns, **kw):
            assert len(ResourceArns) == 1, "wrapper must never batch ARNs"
            self.calls.append(list(ResourceArns))
            arn = ResourceArns[0]
            return {"EvaluationResults": [{
                "EvalDecision": self.decisions.get(arn, "implicitDeny"),
                "MissingContextValues": self.missing.get(arn, [])}]}

    def _args(**kw):
        d = dict(role="r1", action="s3:GetObject", resource_arn="arn:aws:s3:::B/new",
                 context=None, control_arn=None, no_control=False)
        d.update(kw)
        return _t.SimpleNamespace(**d)

    results = []
    def ck(name, ok):
        results.append((name, ok))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    # 1. RULE-1 structural: comma-smuggled multi-ARN refused before any call.
    s = Stub({})
    rc = cmd_simulate(_args(resource_arn="arn:a,arn:b", _client=s))
    ck("rule1.multi_arn_refused_no_call", rc == 2 and s.calls == [])

    # 2. THE RED MUTANT (fail-GREEN class): role holds GetObject on A; new bucket B denies.
    #    The verdict must be a DENY-class, NEVER anything readable as GRANTED/ALLOWED.
    s = Stub({"arn:aws:s3:::A/held": "allowed"})  # B/new -> implicitDeny by default
    rc = cmd_simulate(_args(control_arn="arn:aws:s3:::A/held", _client=s))
    ck("red.new_resource_denies_control_proven_rc1", rc == 1 and len(s.calls) == 2
       and all(len(c) == 1 for c in s.calls))

    # 3. RULE-3: missing context => CONDITIONED-UNEVALUATED (rc=2), never DENIED.
    s = Stub({}, missing={"arn:aws:s3:::B/new": ["aws:SourceVpc"]})
    rc = cmd_simulate(_args(_client=s))
    ck("rule3.missing_context_rc2_not_deny", rc == 2)

    # 4. RULE-2: deny with a control that ALSO denies => INSTRUMENT-SUSPECT rc=2, never rc=1.
    s = Stub({})  # everything denies, incl. the control
    rc = cmd_simulate(_args(control_arn="arn:aws:s3:::A/held", _client=s))
    ck("rule2.control_deny_means_unproven_rc2", rc == 2)

    # 5. allowed target => rc=0 (and the control cannot flip it).
    s = Stub({"arn:aws:s3:::B/new": "allowed", "arn:aws:s3:::A/held": "allowed"})
    rc = cmd_simulate(_args(control_arn="arn:aws:s3:::A/held", _client=s))
    ck("allow.rc0", rc == 0)

    ok = all(o for _, o in results)
    print("\n" + ("OK: all simulate self-test cases pass" if ok else "ERROR: simulate self-test FAILED"))
    return 0 if ok else 1


import comp_iam_census  # noqa: E402 -- APPLIED-plane census generation + vintage honesty
import comp_iam_live  # noqa: E402 -- LIVE-PRIMARY plane (Andrew flip 2026-07-22) -- APPLIED-plane census generation + vintage honesty

# NOTE: this default is the 2026-06-03 census: 111 roles vs 158 in Terraform, and it carries NO
# _meta.generated_utc. It is retained so `reconcile` has a path to point at, but the vintage gate
# below now REFUSES it rather than reconciling against it silently -- which is what it did until
# 2026-07-22. Regenerate with `comp-iam refresh-census`.
_DEFAULT_CENSUS = "docs/briefs/cmpaws-iam-axis-census-20260603.json"


def cmd_live(args):
    """LIVE-PRIMARY: the real estate is the population; Terraform is the overlay.

    PLANE: APPLIED-inventory, live-primary. A DRIFT DETECTOR, never an authorization oracle -- for an
    allow/deny verdict use `comp-iam simulate` (Rule 22a). Consumes comp-aws derive rather than
    re-deriving: that reconciler is certed, joins on ARN identity, and carries the TF ADDRESS as
    provenance, which is why it resolves `${each.key}` fleets that a name-join cannot.
    """
    iam, path, observed = comp_iam_live.load_iam_derive(
        Path(args.derive_dir) if getattr(args, "derive_dir", None) else None)
    if iam is None:
        print(f"LIVE PLANE UNAVAILABLE -- no readable comp-aws IAM derive at {path}")
        print("  Generate one with `comp-aws derive --classes iam`. DESIRED-plane modes are unaffected.")
        print("  This is a COVERAGE refusal: nothing was compared, so nothing is concluded.")
        return 3

    ttl = float(getattr(args, "derive_ttl_hours", None) or comp_iam_live.DEFAULT_DERIVE_TTL_HOURS)
    age = comp_iam_live.derive_age_hours(observed)
    fresh = age is not None and age <= ttl
    print(f"LIVE PROVENANCE: {path.name} -- observed {observed.strftime('%Y-%m-%dT%H:%M:%SZ')} "
          f"(age {age:.1f}h, TTL {ttl:g}h) [{'FRESH' if fresh else 'STALE'}]")
    print(f"  account: {iam.get('_account') or 'UNSTATED'} | source: comp-aws derive (certed "
          f"live-boto3 + TF reconciler); drift_class is ITS verdict, reported not recomputed")

    # Population cross-check against a freshly-read census, when supplied. This is the ONLY way the
    # derive's staleness becomes visible: it cannot detect its own under-enumeration.
    census = None
    if getattr(args, "census", None):
        try:
            census = json.loads(Path(args.census).read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            print(f"  census cross-check UNAVAILABLE (unreadable {args.census}: {e})")
    delta = comp_iam_live.population_delta(iam, census)
    if delta is None:
        print("  population cross-check: UNAVAILABLE (no --census given) -- the live population is "
              "TAKEN ON TRUST from a snapshot that cannot date itself against reality")
    else:
        missing = delta["in_census_not_in_derive"]
        print(f"  population cross-check: derive {delta['derive_population']} vs census "
              f"{delta['census_population']}")
        if missing:
            print(f"  !! STALE POPULATION: {len(missing)} role(s) exist live but are ABSENT from the "
                  f"derive snapshot -- they are INVISIBLE to every verdict below.")
            for n in missing[:10]:
                print(f"       {n}")
            if len(missing) > 10:
                print(f"       ... and {len(missing) - 10} more")
    print()

    if not fresh and not getattr(args, "allow_stale_derive", False):
        print(f"REFUSED: LIVE-plane report NOT PRODUCED -- the derive snapshot is STALE "
              f"(age {age:.1f}h > {ttl:g}h TTL).")
        print("  A live-primary tool reading a stale snapshot of 'live' is not live-primary; it")
        print("  under-enumerates, so MISSING reads as ABSENT -- the same failure direction as the")
        print("  Terraform-primary keying this flip replaces.")
        print("  Fix: `comp-aws derive --classes iam`.  Override (AUDITED): --allow-stale-derive")
        return 3

    buckets = comp_iam_live.classify(iam)
    live_only = buckets["LIVE-no-DECLARED"]
    svc = [n for n in live_only if comp_iam_live.service_linked(n)]
    real = [n for n in live_only if not comp_iam_live.service_linked(n)]
    counts = iam.get("counts") or {}

    print(f"LIVE-PRIMARY IAM  (population = {len(iam.get('nodes') or [])} live roles)")
    print(f"  DECLARED (live AND governed by IaC) : {len(buckets['DECLARED'])}")
    print(f"  LIVE-no-DECLARED                    : {len(live_only)}")
    print(f"    of which AWS service-linked (expected, /aws-service-role/) : {len(svc)}")
    print(f"    of which GOVERNABLE and UNDECLARED (the finding)           : {len(real)}")
    print(f"  derive counts (its own): {json.dumps(counts)}")
    print()
    if real:
        print(f"UNGOVERNED-BY-IaC ({len(real)}) -- live, governable, no Terraform declaration:")
        for n in sorted(real, key=lambda x: str(x.get("id") or x.get("name"))):
            print(f"    !! {n.get('id') or n.get('name')}")
        print()
    print("NOTE: 'DECLARED' is comp-aws derive's verdict, joined on ARN identity with the TF ADDRESS")
    print("      as provenance -- NOT a name match. That is why ${each.key} fleets resolve here and")
    print("      do not in the Terraform-primary surfaces.")
    print("NOTE: this is a DETECTOR. It does not evaluate Deny, boundaries, conditions or SCPs.")
    print("      For an allow/deny verdict use `comp-iam simulate` (Rule 22a).")
    return 1 if real else 0


def _census_self_test():
    """Offline mutant suite for the vintage gate. Zero AWS, deterministic.

    Mirrors _simulate_self_test's posture: the APPLIED plane's SAFETY property is that it refuses
    rather than guesses, and a refusal path that is never exercised is exactly the "passing assertion
    never mutated" trap. Every case here is a MUTANT of the census -- undated, stale, fresh, malformed
    -- because a gate tested only on the input it was written for has not been tested.
    """
    from datetime import datetime, timezone, timedelta
    C = comp_iam_census
    now = datetime(2026, 7, 22, 18, 0, 0, tzinfo=timezone.utc)
    ok = True

    def check(name, got, want):
        nonlocal ok
        if got == want:
            print(f"  PASS  {name}")
        else:
            ok = False
            print(f"  FAIL  {name}: got {got!r}, want {want!r}")

    def stamped(dt):
        return {"_meta": {"generated_utc": dt.strftime("%Y-%m-%dT%H:%M:%SZ")}, "roles": []}

    # --- the SHIPPED census shape: _meta present, NO generated_utc. The live defect. ---
    shipped = {"_meta": {"project": "ADHC_CMPAWS", "account": "313476888478"}, "roles": [{}] * 111}
    check("undated census -> NO_VINTAGE (not FRESH, not STALE)",
          C.census_freshness(shipped, now=now)[0], C.NO_VINTAGE)
    check("undated census -> age is None, NOT 0", C.census_age_hours(shipped, now=now), None)

    # --- fresh / stale boundary ---
    check("1h old -> FRESH", C.census_freshness(stamped(now - timedelta(hours=1)), now=now)[0], C.FRESH)
    check("exactly TTL -> FRESH (boundary inclusive)",
          C.census_freshness(stamped(now - timedelta(hours=24)), now=now)[0], C.FRESH)
    check("TTL+1m -> STALE",
          C.census_freshness(stamped(now - timedelta(hours=24, minutes=1)), now=now)[0], C.STALE)
    check("the real 2026-06-03 census age -> STALE",
          C.census_freshness(stamped(datetime(2026, 6, 3, 14, 47, tzinfo=timezone.utc)), now=now)[0],
          C.STALE)

    # --- malformed stamp must NOT fall through as fresh ---
    check("malformed generated_utc -> NO_VINTAGE",
          C.census_freshness({"_meta": {"generated_utc": "June 3rd"}, "roles": []}, now=now)[0],
          C.NO_VINTAGE)
    check("empty generated_utc -> NO_VINTAGE",
          C.census_freshness({"_meta": {"generated_utc": ""}, "roles": []}, now=now)[0], C.NO_VINTAGE)
    check("no _meta at all -> NO_VINTAGE",
          C.census_freshness({"roles": []}, now=now)[0], C.NO_VINTAGE)

    # --- scope/denominator honesty: an unstated scope must READ as unstated ---
    sc = C.census_scope(shipped)
    check("scope reports the real role count", sc["role_count"], 111)
    check("unstated accounts_swept stays None (not defaulted to 1)", sc["accounts_swept"], None)
    prov = " | ".join(C.provenance_lines(shipped, "cmpaws-iam-axis-census-20260603.json", now=now))
    check("undated provenance says UNKNOWN, not an age", "vintage UNKNOWN" in prov, True)
    check("undated provenance says UNMEASURED, not small", "UNMEASURED" in prov, True)
    check("unstated scope prints UNSTATED", "UNSTATED" in prov, True)

    # --- NEGATIVE CONTROL: a fresh, fully-stated census must NOT trip any warning text ---
    good = {"_meta": {"generated_utc": (now - timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ"),
                      "account": "313476888478", "accounts_swept": 1, "scope": "single-account, all roles"},
            "roles": [{}] * 158}
    gprov = " | ".join(C.provenance_lines(good, "fresh.json", now=now))
    check("fresh census provenance has no UNKNOWN", "UNKNOWN" not in gprov, True)
    check("fresh census provenance has no UNSTATED", "UNSTATED" not in gprov, True)
    check("fresh census reads FRESH", "[FRESH]" in gprov, True)

    print()
    print("OK: all census self-test cases pass" if ok else "ERROR: census self-test FAILED")
    return 0 if ok else 1


def cmd_refresh_census(args):
    """Generate a vintage-stamped APPLIED census from live AWS (Plane 2 of the CVO design brief).

    PLANE: APPLIED-inventory. This is a DRIFT DETECTOR's input, never an authorization oracle -- it
    holds raw statements and does not evaluate Deny, boundaries, or SCPs. For an allow/deny verdict
    use `comp-iam simulate`, which delegates to AWS's own evaluator (Rule 22a).
    """
    try:
        census = comp_iam_census.build_census(account=getattr(args, "account", None))
    except Exception as e:  # noqa: BLE001 -- degrade honestly, never half-write a census
        print("APPLIED CENSUS UNAVAILABLE -- not generated.")
        print(f"  {e}")
        print("  DESIRED-plane modes are unaffected. No census file was written.")
        sys.exit(2)
    out = Path(args.out) if getattr(args, "out", None) else (_WORKSPACE / "docs/briefs" /
          ("cmpaws-iam-census-%s.json" % census["_meta"]["generated_utc"][:10].replace("-", "")))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(census, indent=2, sort_keys=False), encoding="utf-8")
    m, sm = census["_meta"], census["summary"]
    print(f"OK: APPLIED census written -> {out}")
    print(f"  generated_utc : {m['generated_utc']}   account: {m['account']}")
    print(f"  api           : {m['api']}")
    print(f"  roles: {sm['role_count']} | groups: {sm['group_count']} | users: {sm['user_count']}")
    print(f"  scope         : {m['scope']}")
    print("  NOTE: attached-managed policies are RECORDED, not resolved -- their statements are")
    print("        marked UNRESOLVED. A reconcile treats them as uncovered, never as absent.")
    return 0


def cmd_reconcile(args):
    """DESIRED-vs-LIVE reconcile (ADHC comp-iam drift conversion).

    comp-iam's default modes parse Terraform = DESIRED state; they never see live
    AWS. This overlays a live-AWS IAM census (per-role statements, emitted by
    comp-aws / 0.7.0) ON TOP of the TF-parsed roles to surface DESIRED-vs-LIVE
    drift -- the class TF-parse is structurally blind to:
      - LIVE-ONLY role:    granted live, absent from TF (console/manual = ungoverned)
      - LIVE-ONLY action:  a role's live grant not covered by its TF policy (drift)
      - OVER-PERM:         census-flagged *FullAccess / wildcard-broad grants
    Wildcard-aware: a live action is 'covered' iff the TF role .grants() it (so a
    TF `s3:*` covers a live `s3:GetObject`). TF-only roles are reported as INFO
    (the census is customer-role-scoped; service-linked/internal roles aren't in it).
    """
    census_path = Path(args.census) if args.census else (_WORKSPACE / _DEFAULT_CENSUS)
    if not census_path.exists():
        print(f"CENSUS NOT FOUND: {census_path}")
        print("  Pass --census <path> to the comp-aws live IAM census JSON "
              "(per-role statements[{effect,actions,resources,condition,source}]).")
        sys.exit(2)
    try:
        census = json.loads(census_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"CENSUS PARSE FAILED ({census_path}): {e}")
        sys.exit(2)

    # ---- VINTAGE GATE (fail-closed). CVO brief 5.1 + CTO ruling 2026-07-22. -------------------
    # An APPLIED verdict is a claim about LIVE grants. Answering it from a census that cannot date
    # itself, or that is older than the TTL, produces a confident answer about a world that has moved
    # -- and it errs in the GRANTED direction, which is the dangerous one. So: REFUSE, and degrade to
    # DESIRED-only, rather than report a stale-but-plausible reconcile.
    #
    # The refusal is LOUD ON STDOUT and exits NON-ZERO (3), distinct from 0=clean and 1=drift-found.
    # A refusal that printed only to stderr, or exited 0, would be indistinguishable from a clean
    # reconcile to any caller that reads one channel -- the exact defect fixed in comp-constants
    # earlier today (a REFUSE with empty stdout read as a pass).
    ttl = float(getattr(args, "census_ttl_hours", None) or comp_iam_census.DEFAULT_TTL_HOURS)
    verdict, _age = comp_iam_census.census_freshness(census, ttl_hours=ttl)
    for _ln in comp_iam_census.provenance_lines(census, census_path, ttl_hours=ttl):
        print(_ln)
    print()
    if verdict != comp_iam_census.FRESH and not getattr(args, "allow_stale_census", False):
        why = ("carries NO vintage (_meta.generated_utc absent) -- its age is UNMEASURED, not small"
               if verdict == comp_iam_census.NO_VINTAGE else
               f"is STALE (older than the {ttl:g}h TTL)")
        print(f"REFUSED: APPLIED reconcile NOT PERFORMED -- the census {why}.")
        print("  This is a COVERAGE refusal, not a clean result: nothing was compared, so nothing")
        print("  can be concluded about live-vs-Terraform drift. DESIRED-plane modes are unaffected")
        print("  (`comp-iam gaps` / `roles` / `role` still answer from Terraform).")
        print("  Fix: `comp-iam refresh-census --out <path>` then re-run with --census <path>.")
        print("  Override (AUDITED, and it makes the verdict non-authoritative): --allow-stale-census")
        sys.exit(3)
    if getattr(args, "allow_stale_census", False) and verdict != comp_iam_census.FRESH:
        print(f"WARN: OVERRIDE --allow-stale-census -- reconciling against a {verdict} census. "
              "This verdict is NOT an APPLIED-plane authority.")
        print()

    live = {}
    for r in (census.get("roles") or []):
        acts = set()
        for s in (r.get("statements") or []):
            if str(s.get("effect", "")).lower() == "allow":
                acts |= {str(a).lower() for a in (s.get("actions") or [])}
        live[r.get("role_name")] = {"actions": acts, "overperm": r.get("overperm_flags") or []}

    _profiles, tf_roles, _gaps = _build()

    live_only_roles = sorted(set(live) - set(tf_roles))
    tf_only_roles = sorted(set(tf_roles) - set(live))
    matched = sorted(set(live) & set(tf_roles))

    drift_action_findings = []   # (role, [live-only actions])
    overperm_findings = []       # (role, [flags])
    for name in matched:
        tfrole = tf_roles[name]
        live_only = sorted(a for a in live[name]["actions"] if not tfrole.grants(a))
        if live_only:
            drift_action_findings.append((name, live_only))
        if live[name]["overperm"]:
            overperm_findings.append((name, live[name]["overperm"]))

    src_meta = (census.get("_meta") or {})
    print(f"IAM DESIRED-vs-LIVE RECONCILE  (census: {census_path.name})")
    print(f"  live roles (census): {len(live)} | TF-parsed roles: {len(tf_roles)} | matched: {len(matched)}")
    if src_meta.get("scp_included") is False or "scp" in str(src_meta).lower():
        print("  NOTE: SCP layer NOT in census -- effective-deny from SCPs not reconciled here.")
    print()

    if live_only_roles:
        print(f"DRIFT-LIVE-ONLY ROLES ({len(live_only_roles)}) -- granted live but ABSENT from Terraform")
        print("  (console/manual creation = ungoverned-by-IaC; the shadow-bucket class for roles):")
        for n in live_only_roles:
            print(f"    !! {n}")
        print()
    if drift_action_findings:
        print(f"DRIFT-LIVE-ONLY ACTIONS ({len(drift_action_findings)} role(s)) -- live grants NOT in the TF policy")
        for n, acts in drift_action_findings:
            print(f"    !! {n}: {', '.join(acts[:12])}{' ...' if len(acts) > 12 else ''}")
        print()
    if overperm_findings:
        print(f"OVER-PERM ({len(overperm_findings)} role(s)) -- census-flagged broad/*FullAccess grants:")
        for n, flags in overperm_findings:
            print(f"    ?? {n}: {flags}")
        print()
    if tf_only_roles:
        print(f"INFO: {len(tf_only_roles)} TF-parsed role(s) not in the (customer-scoped) census "
              f"-- expected if service-linked/internal; not drift.")
        print()

    total_drift = len(live_only_roles) + len(drift_action_findings)
    print(f"Total: {len(live_only_roles)} live-only-role | {len(drift_action_findings)} live-only-action | "
          f"{len(overperm_findings)} over-perm")
    if total_drift == 0 and not overperm_findings:
        print("  CLEAN: live AWS matches Terraform (no desired-vs-live drift, no over-perms).")
    sys.exit(1 if total_drift else 0)


def main():
    parser = argparse.ArgumentParser(
        prog='comp-iam',
        description='IAM permission cross-reference: source code ops vs Terraform policies.',
    )
    sub = parser.add_subparsers(dest='command')

    sub.add_parser('gaps', help='Show permission gaps (default)')
    sub.add_parser('roles', help='List all IAM roles from Terraform')
    sub.add_parser('services', help='List all services with their operations')
    p_svc = sub.add_parser('service', help='Show operations for one service')
    p_svc.add_argument('name', help='Service name (partial match)')
    p_role = sub.add_parser('role', help='Show granted actions for one role')
    p_role.add_argument('name', help='Role name (partial match)')
    sub.add_parser('stats', help='Summary counts')
    p_rec = sub.add_parser('reconcile', help='DESIRED(TF)-vs-LIVE(census) drift reconcile')
    p_rec.add_argument('--census-ttl-hours', type=float, default=None,
                       help='max census age for an APPLIED verdict (default 24)')
    p_rec.add_argument('--allow-stale-census', action='store_true',
                       help='AUDITED override: reconcile against a stale/undated census (verdict is '
                            'then NOT an APPLIED authority)')
    p_rec.add_argument('--census', default=None,
                       help='Path to the comp-aws live IAM census JSON (default: docs/briefs/cmpaws-iam-axis-census-*.json)')

    sub.add_parser('attach-census',
                   help='Policy blocks comp-iam could NOT attach to a role (exit 1 if any)')
    p_rs = sub.add_parser('resource-sweep',
                          help='Estate-wide: calls whose ACTION is held but RESOURCE is not')
    p_rs.add_argument('--s3-only', action='store_true',
                      help='Only s3:* actions (the modeled resource space)')
    p_rs.add_argument('--show-broad', action='store_true',
                      help='List the Resource:* roles (EXCLUDED, NOT CLEARED)')

    # Also add --service flag to gaps command
    p_gaps = sub.add_parser('gaps-filtered', help='Show gaps for one service')
    p_gaps.add_argument('service', nargs='?', default='', help='Filter by service name')

    p_sim = sub.add_parser('simulate',
                           help='APPLIED-plane live simulate-principal-policy wrapper (22a rules structural)')
    p_sim.add_argument('role', help='role name or ARN')
    p_sim.add_argument('action', help='the IAM action, e.g. s3:GetObject')
    p_sim.add_argument('resource_arn', help='ONE resource ARN (a comma-list is refused by construction)')
    p_sim.add_argument('--context', action='append',
                       help='Key=type:value for a conditioned statement (repeatable), e.g. aws:SourceVpc=string:vpc-123')
    p_sim.add_argument('--control-arn', default=None,
                       help='a resource the role IS known to hold (the positive control; auto-derived from DESIRED if omitted)')
    p_sim.add_argument('--no-control', action='store_true',
                       help='skip the positive control (a resulting DENY is UNPROVEN, never rc=1)')
    sub.add_parser('simulate-self-test', help='offline mutant suite for the simulate wrapper (no AWS)')
    p_rc = sub.add_parser('refresh-census',
                          help='APPLIED: generate a vintage-stamped live-IAM census (Plane 2)')
    p_rc.add_argument('--out', help='output path (default docs/briefs/cmpaws-iam-census-<date>.json)')
    p_rc.add_argument('--account', help='account id to stamp (default: derived from role ARNs)')
    sub.add_parser('census-self-test', help='offline vintage/fail-closed suite (no AWS)')
    p_live = sub.add_parser('live',
                            help='LIVE-PRIMARY: real estate is the population, Terraform is overlay')
    p_live.add_argument('--derive-dir', help='comp-aws derive dir (default .fedobs_tmp/live_aws)')
    p_live.add_argument('--census', help='fresh census for the population staleness cross-check')
    p_live.add_argument('--derive-ttl-hours', type=float, default=None,
                        help='max derive-snapshot age (default 24)')
    p_live.add_argument('--allow-stale-derive', action='store_true',
                        help='AUDITED override: report from a stale live snapshot')

    args = parser.parse_args()

    # Default: gaps if no subcommand given, but also handle gaps with optional --service
    if not args.command or args.command == 'gaps':
        # Simulate args.service for cmd_gaps
        if not hasattr(args, 'service'):
            args.service = ''
        cmd_gaps(args)
    elif args.command == 'gaps-filtered':
        cmd_gaps(args)
    elif args.command == 'roles':
        cmd_roles(args)
    elif args.command == 'services':
        cmd_services(args)
    elif args.command == 'service':
        cmd_service(args)
    elif args.command == 'role':
        cmd_role(args)
    elif args.command == 'stats':
        cmd_stats(args)
    elif args.command == 'reconcile':
        cmd_reconcile(args)
    elif args.command == 'resource-sweep':
        sys.exit(cmd_resource_sweep(args))
    elif args.command == 'attach-census':
        sys.exit(cmd_attach_census(args))
    elif args.command == 'simulate':
        sys.exit(cmd_simulate(args))
    elif args.command == 'simulate-self-test':
        sys.exit(_simulate_self_test())
    elif args.command == 'refresh-census':
        sys.exit(cmd_refresh_census(args))
    elif args.command == 'census-self-test':
        sys.exit(_census_self_test())
    elif args.command == 'live':
        sys.exit(cmd_live(args))
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

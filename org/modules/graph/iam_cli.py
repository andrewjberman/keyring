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
"""

import argparse
import json
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_iam import build_iam_report, PermissionGap  # noqa: E402


def _build():
    return build_iam_report(_WORKSPACE)


def cmd_gaps(args):
    profiles, roles, gaps = _build()

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
                        print(f"    Resources ({len(stmt.resources)}):")
                        for r in stmt.resources[:5]:
                            print(f"      {r}")
                        if len(stmt.resources) > 5:
                            print(f"      ... and {len(stmt.resources) - 5} more")
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
        print(f"  OPERATIONS ({len(profile.operations)}):")
        for op in profile.operations:
            for action in op.iam_actions:
                key = (action, op.file_path, op.line_number)
                if key in seen:
                    continue
                seen.add(key)

                role = roles.get(profile.iam_role) if profile.iam_role else None
                granted = role.grants(action) if role else None
                status = "GRANTED" if granted else ("MISSING" if granted is not None else "UNKNOWN")

                print(f"    {action}  [{status}]")
                print(f"      via: {op.source_pattern} at {op.file_path}:{op.line_number}")
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
                print(f"    Resources: {', '.join(stmt.resources[:3])}")
                if len(stmt.resources) > 3:
                    print(f"      ... +{len(stmt.resources)-3} more")
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


_DEFAULT_CENSUS = "docs/briefs/cmpaws-iam-axis-census-20260603.json"


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
    p_rec.add_argument('--census', default=None,
                       help='Path to the comp-aws live IAM census JSON (default: docs/briefs/cmpaws-iam-axis-census-*.json)')

    # Also add --service flag to gaps command
    p_gaps = sub.add_parser('gaps-filtered', help='Show gaps for one service')
    p_gaps.add_argument('service', nargs='?', default='', help='Filter by service name')

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
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

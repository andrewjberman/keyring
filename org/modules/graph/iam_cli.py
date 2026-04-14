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
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_iam import build_iam_report, ServiceProfile, IamRole, PermissionGap


def _build():
    return build_iam_report(_WORKSPACE)


def cmd_gaps(args):
    profiles, roles, gaps = _build()

    service_filter = (args.service or "").lower()

    if not gaps:
        print("No permission gaps detected.")
        print(f"  ({len(profiles)} services scanned, {len(roles)} IAM roles parsed)")
        return

    filtered = [g for g in gaps if not service_filter or service_filter in g.service.lower()]

    if not filtered:
        print(f"No gaps for service filter: {service_filter}")
        return

    print(f"PERMISSION GAPS ({len(filtered)} found)")
    print()

    # Group by service
    by_service: dict[str, list[PermissionGap]] = {}
    for g in filtered:
        by_service.setdefault(g.service, []).append(g)

    for svc, svc_gaps in sorted(by_service.items()):
        print(f"  {svc}  (role: {svc_gaps[0].iam_role})")
        for gap in svc_gaps:
            print(f"    !! MISSING: {gap.iam_action}")
            print(f"       Called via: {gap.source_pattern}")
            print(f"       At: {gap.file_path}:{gap.line_number}")
            print(f"       Fix: add '{gap.iam_action}' to {gap.iam_role} policy in iam.tf")
        print()

    print(f"Total: {len(gaps)} gap(s) across {len(by_service)} service(s)")


def cmd_roles(args):
    _, roles, _ = _build()

    if not roles:
        print("No IAM roles found in Terraform.")
        return

    print(f"IAM ROLES ({len(roles)} found)")
    print()
    for role_name, role in sorted(roles.items()):
        action_count = sum(len(s.actions) for s in role.statements)
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
    name = args.name.lower()

    matches = [p for p in profiles if name in p.name.lower()]
    if not matches:
        print(f"No service matching '{args.name}'")
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
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

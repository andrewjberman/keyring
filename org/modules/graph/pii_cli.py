#!/usr/bin/env python3
"""
comp-pii -- PII field detection and pseudonymization audit.

Cross-references the pseudonymizer target list (pseudonymizer.py) with
rendered fields in React components to flag which fetches carry PII,
which fields get hashed for which user roles, and which serving paths
expose PII without server-side pseudonymization.

Usage:
    comp-pii scan PartnerAnalytics  # flag PII fields in one component
    comp-pii scan ClientsTab        # flag PII fields in Books tab
    comp-pii audit                  # full ADVI PII audit across all tabs
    comp-pii fields                 # list all known PII field names
    comp-pii routes                 # which serving paths expose PII + their auth layers

Authoritative sources:
    pseudonymizer.py -- field names that get HMAC-hashed
    auth-validator-edge/index.mjs -- injected auth headers
    comp-transform -- rendered field extraction
    comp-routes -- serving path auth layers
"""

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_transforms import build_component_dataflow, build_all_dataflows
from org.modules.graph.extract_routes import build_routing_table


# ---------------------------------------------------------------------------
# PII field definitions (from pseudonymizer.py)
# ---------------------------------------------------------------------------

@dataclass
class PiiField:
    """A field name that the pseudonymizer targets."""
    name: str                  # field name (key in JSON)
    category: str              # Client, Book, Acct, id, Location
    hash_prefix: str           # prefix in hashed output
    context: str = ""          # when it gets hashed (always, client-context only, etc.)


# Parsed from pseudonymizer.py _transform_field()
PII_FIELDS: list[PiiField] = [
    PiiField("relationship_name", "Client PII", "Client", "always hashed for non-admin users"),
    PiiField("client_name", "Client PII", "Client", "always hashed for non-admin users"),
    PiiField("label", "Client PII", "Client", "hashed in client-context responses only (caller controls scope)"),
    PiiField("book_name", "Advisor PII", "Book", "advisor book name -- navigational key, hashed for non-admin"),
    PiiField("account_id", "Account PII", "Acct", "account identifier -- hashed for non-admin"),
    PiiField("relationship_id", "Navigation ID", "id", "relationship drill key -- hashed for non-admin"),
    PiiField("client_key", "Navigation ID", "id", "client navigation key -- hashed for non-admin"),
    PiiField("key", "Navigation ID", "id", "generic key field -- hashed for non-admin (broad match)"),
    PiiField("city", "Location PII", "Location", "client city -- hashed at relationship grain"),
    PiiField("state", "Location PII", "Location", "client state -- hashed at relationship grain"),
    PiiField("account_number", "Account PII", "Acct", "BD account number (z-prefixed, e.g. z08327149)"),
    PiiField("account_name", "Account PII", "", "human-readable account name -- not in pseudonymizer but carries PII"),
    PiiField("name", "Potential PII", "", "advisor/client name -- NOT in pseudonymizer target list but commonly carries PII"),
    PiiField("architect", "Potential PII", "", "advisor architect name -- used for book-scoping, may contain real name"),
    PiiField("implementor", "Potential PII", "", "advisor implementor name -- may contain real name"),
    PiiField("email", "Potential PII", "", "user email -- not in pseudonymizer but carries PII"),
    PiiField("clientLabel", "Potential PII", "", "display label for client -- may be cleartext name from URL param"),
    PiiField("architectKey", "Potential PII", "", "architect key from URL params -- may be real name with underscores"),
    PiiField("clientKey", "Navigation ID", "id", "client key from URL params -- BD relationship ID (z-prefixed)"),
]

PII_FIELD_NAMES = {f.name for f in PII_FIELDS}
PSEUDONYMIZED_FIELDS = {f.name for f in PII_FIELDS if f.hash_prefix}  # actually hashed by pseudonymizer
POTENTIAL_PII_FIELDS = {f.name for f in PII_FIELDS if not f.hash_prefix}  # not hashed but may carry PII

# Regex patterns for PII values (not just field names)
# These catch BD account/relationship numbers in URLs, string literals, etc.
PII_VALUE_PATTERNS = [
    (re.compile(r'\bz\d{7,12}\b'), "BD relationship/account ID (z-number)"),
    (re.compile(r'\b[A-Z]{3}\d{6,10}\b'), "BD account number (letter-prefix)"),
]

# Synthetic IDs that are safe to use in docs/tests (not real accounts)
SYNTHETIC_IDS = {
    'z00000001', 'z00000000', 'z99999999', 'z12345678',
    'ABC0000001', 'ABC1234567', 'XYZ0000001',
}


# ---------------------------------------------------------------------------
# Auth role matrix
# ---------------------------------------------------------------------------

AUTH_ROLES = {
    "internal_admin": {"sees_cleartext": True, "pseudonymized": False, "book_scoped": False},
    "internal_user": {"sees_cleartext": True, "pseudonymized": False, "book_scoped": False},
    "partner_admin": {"sees_cleartext": True, "pseudonymized": False, "book_scoped": False},
    "partner_advisor": {"sees_cleartext": False, "pseudonymized": True, "book_scoped": True},
}


# ---------------------------------------------------------------------------
# PII detection in component data flow
# ---------------------------------------------------------------------------

@dataclass
class PiiHit:
    """A PII field detected in a component's data flow."""
    field_name: str
    field_path: str            # full path (e.g., clientDetailData.relationship_name)
    pii_category: str          # Client PII, Account PII, etc.
    pseudonymized: bool        # True if pseudonymizer targets this field
    location: str              # "transform chain", "jsx ref", "fetch response type"
    line_number: int = 0
    component: str = ""
    serving_path: str = ""     # S3 direct or API GW (affects whether pseudonymizer runs)
    auth_layers: str = ""      # edge, edge+apigw, none


def _scan_component_pii(component_path: Path, workspace_root: Path, rt=None) -> list[PiiHit]:
    """Scan a component for PII field references."""
    flow = build_component_dataflow(component_path, workspace_root)
    if not flow:
        return []

    hits: list[PiiHit] = []

    # Build route lookup for this component's fetches
    if rt is None:
        rt = build_routing_table(workspace_root)

    fetch_routes: dict[str, dict] = {}
    for fb in flow.fetches:
        route = next((r for r in rt.routes if r.endpoint_function == fb.fetch_function), None)
        if route:
            auth_parts = []
            if route.auth_edge:
                auth_parts.append("edge")
            if route.auth_api_gw:
                auth_parts.append("apigw")
            fetch_routes[fb.fetch_function] = {
                "origin_type": route.cf_origin_type,
                "auth": "+".join(auth_parts) or "none",
                "s3_key": route.s3_key,
                "lambda": route.lambda_handler,
            }

    # Scan transform chain field accesses
    for tc in flow.transforms:
        for fa in tc.field_accesses:
            # Normalize field path: remove ?. and [] brackets
            normalized = re.sub(r'\?\.|[\[\]?]', '.', fa)
            parts = [p for p in normalized.split('.') if p and p.isidentifier()]
            for part in parts:
                if part in PII_FIELD_NAMES:
                    pii_field = next(f for f in PII_FIELDS if f.name == part)

                    # Find which fetch this chain reads from
                    serving = ""
                    auth = ""
                    for input_var in tc.input_variables:
                        for fb in flow.fetches:
                            if fb.data_variable == input_var and fb.fetch_function in fetch_routes:
                                ri = fetch_routes[fb.fetch_function]
                                serving = f"{ri['origin_type']} ({ri.get('s3_key') or ri.get('lambda', '?')})"
                                auth = ri["auth"]

                    hits.append(PiiHit(
                        field_name=part,
                        field_path=fa,
                        pii_category=pii_field.category,
                        pseudonymized=part in PSEUDONYMIZED_FIELDS,
                        location=f"transform: {tc.output_variable}",
                        line_number=tc.line_number,
                        component=flow.component_name,
                        serving_path=serving,
                        auth_layers=auth,
                    ))

    # Scan JSX references
    for ref in flow.jsx_refs:
        normalized = re.sub(r'\?\.|[\[\]?]', '.', ref.field_path)
        parts = [p for p in normalized.split('.') if p and p.isidentifier()]
        for part in parts:
            if part in PII_FIELD_NAMES:
                pii_field = next(f for f in PII_FIELDS if f.name == part)
                hits.append(PiiHit(
                    field_name=part,
                    field_path=ref.field_path,
                    pii_category=pii_field.category,
                    pseudonymized=part in PSEUDONYMIZED_FIELDS,
                    location=f"jsx ({ref.context})",
                    line_number=ref.line_number,
                    component=flow.component_name,
                ))

    # Scan response type fields
    for type_name, fields in flow.response_types.items():
        for f in fields:
            if f.name in PII_FIELD_NAMES:
                pii_field = next(pf for pf in PII_FIELDS if pf.name == f.name)
                hits.append(PiiHit(
                    field_name=f.name,
                    field_path=f"{type_name}.{f.name}",
                    pii_category=pii_field.category,
                    pseudonymized=f.name in PSEUDONYMIZED_FIELDS,
                    location="response type field",
                    component=flow.component_name,
                ))

    # Scan raw source for PII value patterns (z-numbers, account IDs in literals/URLs)
    try:
        raw_content = component_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        raw_content = ""

    if raw_content:
        raw_lines = raw_content.splitlines()
        for pattern, description in PII_VALUE_PATTERNS:
            for i, line in enumerate(raw_lines, 1):
                stripped = line.strip()
                # Skip imports, type annotations (but NOT comments -- PII in docs is still PII)
                if stripped.startswith(('import ', 'from ', 'type ', 'interface ')):
                    continue
                for vm in pattern.finditer(line):
                    value = vm.group(0)
                    # Skip synthetic IDs and common false positives
                    if value in SYNTHETIC_IDS:
                        continue
                    if value.startswith('z') and ('index' in line.lower() or 'z-' in line):
                        continue
                    hits.append(PiiHit(
                        field_name=value,
                        field_path=f"literal: {value}",
                        pii_category="Hardcoded PII Value",
                        pseudonymized=False,
                        location=f"source literal ({description})",
                        line_number=i,
                        component=flow.component_name,
                    ))

    # Deduplicate by (field_name, location)
    seen = set()
    unique_hits = []
    for h in hits:
        key = (h.field_name, h.location, h.component)
        if key not in seen:
            seen.add(key)
            unique_hits.append(h)

    return unique_hits


def _find_component(query: str) -> Path | None:
    pages_dir = _WORKSPACE / "portal" / "src" / "pages"
    if not pages_dir.exists():
        return None
    query_lower = query.lower()
    matches = []
    for tsx_file in pages_dir.rglob("*.tsx"):
        if query_lower == tsx_file.stem.lower():
            return tsx_file
        if query_lower in tsx_file.stem.lower():
            matches.append(tsx_file)
    if len(matches) == 1:
        return matches[0]
    if matches:
        print(f"Multiple matches for '{query}':")
        for m in matches:
            print(f"  {m.stem}")
        sys.exit(1)
    return None


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_scan(args):
    path = _find_component(args.component)
    if not path:
        print(f"Component not found: {args.component}")
        sys.exit(1)

    rt = build_routing_table(_WORKSPACE)
    hits = _scan_component_pii(path, _WORKSPACE, rt)

    if not hits:
        print(f"No PII fields detected in {args.component}")
        return

    # Group by category
    by_cat: dict[str, list[PiiHit]] = {}
    for h in hits:
        by_cat.setdefault(h.pii_category, []).append(h)

    print(f"PII SCAN: {args.component} ({len(hits)} PII field references)")
    print()

    for cat, cat_hits in sorted(by_cat.items()):
        pseudonymized_count = sum(1 for h in cat_hits if h.pseudonymized)
        unprotected_count = len(cat_hits) - pseudonymized_count
        warning = " !! UNPROTECTED !!" if unprotected_count > 0 and cat != "Potential PII" else ""
        print(f"  {cat} ({len(cat_hits)} refs, {pseudonymized_count} pseudonymized){warning}")

        for h in cat_hits:
            status = "[HASHED]" if h.pseudonymized else "[CLEARTEXT]"
            serving = f" via {h.serving_path}" if h.serving_path else ""
            auth = f" auth:{h.auth_layers}" if h.auth_layers else ""
            print(f"    {status} {h.field_name}")
            print(f"      path: {h.field_path}")
            print(f"      at: L{h.line_number} {h.location}{serving}{auth}")
        print()

    # Summary
    total_hashed = sum(1 for h in hits if h.pseudonymized)
    total_cleartext = sum(1 for h in hits if not h.pseudonymized and h.pii_category != "Potential PII")
    total_potential = sum(1 for h in hits if h.pii_category == "Potential PII")
    print(f"  SUMMARY: {total_hashed} pseudonymized, {total_cleartext} cleartext PII, {total_potential} potential PII")

    # S3-direct serving path warning
    s3_direct_pii = [h for h in hits if h.pseudonymized and h.serving_path and "s3" in h.serving_path]
    if s3_direct_pii:
        print()
        print(f"  WARNING: {len(s3_direct_pii)} pseudonymized fields served via S3 direct (no Lambda pseudonymizer):")
        for h in s3_direct_pii:
            print(f"    {h.field_name} in {h.field_path} -- {h.serving_path}")
        print("  These fields are served as cleartext in the JSON file. Pseudonymization happens")
        print("  ONLY on Lambda-proxied routes (API GW -> opal-partners-data -> pseudonymizer.py).")
        print("  S3-direct routes rely on the gold/platinum script to pre-pseudonymize or the")
        print("  frontend canSeeCleartext() hook to mask display.")


def cmd_audit(args):
    """Full PII audit across all ADVI components."""
    advi_components = [
        "PartnerAnalytics", "DistributionTab", "AdvisorsTab", "ClientsTab",
        "AssetIntelligenceTab", "ClientDetailPage", "MixTimeseriesPanel",
        "ConcentrationPanel", "FeeEfficiencyPanel", "FeeRoleBreakdownPanel",
        "FeeSummaryPanel",
    ]

    rt = build_routing_table(_WORKSPACE)
    total_hits = 0
    total_hashed = 0
    total_cleartext = 0
    s3_direct_pii = 0

    print("PII AUDIT: All Advisor Intelligence Components")
    print(f"{'=' * 70}")
    print()

    for comp_name in advi_components:
        path = _find_component(comp_name)
        if not path:
            continue

        hits = _scan_component_pii(path, _WORKSPACE, rt)
        if not hits:
            print(f"  {comp_name}: clean (no PII fields)")
            continue

        hashed = sum(1 for h in hits if h.pseudonymized)
        cleartext = sum(1 for h in hits if not h.pseudonymized and h.pii_category != "Potential PII")
        potential = sum(1 for h in hits if h.pii_category == "Potential PII")
        s3_pii = sum(1 for h in hits if h.pseudonymized and h.serving_path and "s3" in h.serving_path)

        total_hits += len(hits)
        total_hashed += hashed
        total_cleartext += cleartext
        s3_direct_pii += s3_pii

        status = "OK" if cleartext == 0 else "!! REVIEW !!"
        s3_warn = f" [S3-DIRECT:{s3_pii}]" if s3_pii > 0 else ""
        print(f"  {comp_name}: {len(hits)} PII refs ({hashed} hashed, {cleartext} cleartext, {potential} potential){s3_warn} {status}")

        # Show cleartext PII fields
        for h in hits:
            if not h.pseudonymized and h.pii_category != "Potential PII":
                print(f"    !! CLEARTEXT: {h.field_name} at L{h.line_number} ({h.location})")

    print()
    print(f"{'=' * 70}")
    print(f"TOTAL: {total_hits} PII refs across all components")
    print(f"  Pseudonymized: {total_hashed}")
    print(f"  Cleartext PII: {total_cleartext}")
    print(f"  S3-direct PII: {s3_direct_pii} (no server-side pseudonymizer)")
    if s3_direct_pii > 0:
        print()
        print("  NOTE: S3-direct served PII relies on:")
        print("    1. Gold/platinum scripts pre-pseudonymizing the JSON, OR")
        print("    2. Frontend canSeeCleartext() hook masking the display")
        print("  Neither is enforced server-side. Lambda-proxied routes are safer.")


def cmd_fields(args):
    print(f"PII FIELD REGISTRY ({len(PII_FIELDS)} fields)")
    print()
    print(f"  PSEUDONYMIZED by pseudonymizer.py ({len(PSEUDONYMIZED_FIELDS)} fields):")
    for f in PII_FIELDS:
        if f.hash_prefix:
            print(f"    {f.name:25s} [{f.category}] -> '{f.hash_prefix} {{8-char hex}}'")
            print(f"      {f.context}")
    print()
    print(f"  POTENTIAL PII (not hashed, but may carry sensitive data):")
    for f in PII_FIELDS:
        if not f.hash_prefix:
            print(f"    {f.name:25s} [{f.category}]")
            print(f"      {f.context}")
    print()
    print("  ROLE MATRIX:")
    for role, props in AUTH_ROLES.items():
        cleartext = "cleartext" if props["sees_cleartext"] else "pseudonymized"
        scoped = ", book-scoped" if props["book_scoped"] else ""
        print(f"    {role:20s} -> {cleartext}{scoped}")


def cmd_routes(args):
    """Show which serving paths expose PII and their auth protection."""
    rt = build_routing_table(_WORKSPACE)
    flows = build_all_dataflows(_WORKSPACE)

    print("PII ROUTE AUDIT: which paths carry PII and how they're protected")
    print()

    for flow in sorted(flows, key=lambda f: f.component_name):
        component_pii = False
        for fb in flow.fetches:
            route = next((r for r in rt.routes if r.endpoint_function == fb.fetch_function), None)
            if not route:
                continue

            # Check if response type has PII fields
            has_pii = False
            pii_field_names = []
            for type_name, fields in flow.response_types.items():
                for f in fields:
                    if f.name in PII_FIELD_NAMES:
                        has_pii = True
                        pii_field_names.append(f.name)

            if not has_pii:
                continue

            if not component_pii:
                print(f"  {flow.component_name}:")
                component_pii = True

            origin = route.cf_origin_type
            auth_parts = []
            if route.auth_edge:
                auth_parts.append("edge JWT")
            if route.auth_api_gw:
                auth_parts.append("API GW")
            auth = " + ".join(auth_parts) or "NONE"

            # Pseudonymizer only runs on Lambda-proxied routes
            has_pseudonymizer = origin == "api_gateway"
            pseudo_tag = "PSEUDONYMIZER" if has_pseudonymizer else "NO PSEUDONYMIZER (S3 direct)"

            print(f"    {fb.fetch_function}()")
            print(f"      origin: {origin} | auth: {auth} | {pseudo_tag}")
            print(f"      PII fields: {', '.join(pii_field_names)}")
            if not has_pseudonymizer and pii_field_names:
                print(f"      !! S3-direct with PII: relies on client-side masking only")
            print()


def cmd_sweep(args):
    """Sweep ALL portal source files for hardcoded PII values (z-numbers, account IDs, real names).
    Unlike 'scan' (component-level), this checks every .ts/.tsx file including API clients,
    types, utilities, and documentation comments."""
    portal_src = _WORKSPACE / "portal" / "src"
    if not portal_src.exists():
        print("portal/src not found")
        sys.exit(1)

    total_hits = 0
    files_with_hits = 0

    print("PII SWEEP: scanning all portal source files for hardcoded PII values")
    print()

    for src_file in sorted(portal_src.rglob("*.ts")) + sorted(portal_src.rglob("*.tsx")):
        try:
            content = src_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        rel_path = str(src_file.relative_to(_WORKSPACE)).replace("\\", "/")
        file_hits = []

        for i, line in enumerate(content.splitlines(), 1):
            stripped = line.strip()
            # Skip pure import lines
            if stripped.startswith(('import ', 'from ')):
                continue

            for pattern, description in PII_VALUE_PATTERNS:
                for vm in pattern.finditer(line):
                    value = vm.group(0)
                    # Skip synthetic IDs and z-index CSS false positives
                    if value in SYNTHETIC_IDS:
                        continue
                    if value.startswith('z') and ('index' in line.lower() or 'z-' in line):
                        continue
                    ctx = stripped[:100]
                    file_hits.append((i, value, description, ctx))

        if file_hits:
            files_with_hits += 1
            total_hits += len(file_hits)
            print(f"  {rel_path} ({len(file_hits)} hits):")
            for line_no, value, desc, ctx in file_hits:
                in_comment = ctx.startswith(('//', '/*', '*', '/**'))
                loc = "[DOC]" if in_comment else "[CODE]"
                print(f"    L{line_no} {loc} {value} ({desc})")
                print(f"      {ctx}")
            print()

    print(f"SWEEP TOTAL: {total_hits} hardcoded PII values in {files_with_hits} files")
    if total_hits > 0:
        print()
        print("  ACTION: Replace real account/relationship IDs with synthetic examples.")
        print("  Use: z00000001, z99999999, ABC0000001 for doc examples.")
        print("  Real IDs in source code (including comments) are a PII leak vector.")


def main():
    parser = argparse.ArgumentParser(
        prog='comp-pii',
        description='PII field detection and pseudonymization audit.',
    )
    sub = parser.add_subparsers(dest='command')

    p_scan = sub.add_parser('scan', help='Flag PII fields in one component')
    p_scan.add_argument('component', help='Component name')

    sub.add_parser('audit', help='Full PII audit across all ADVI tabs')
    sub.add_parser('sweep', help='Sweep ALL portal source for hardcoded PII values (z-numbers, account IDs)')
    sub.add_parser('fields', help='List all known PII field names and role matrix')
    sub.add_parser('routes', help='Which serving paths expose PII + their auth layers')

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    commands = {
        'scan': cmd_scan,
        'audit': cmd_audit,
        'sweep': cmd_sweep,
        'fields': cmd_fields,
        'routes': cmd_routes,
    }
    commands[args.command](args)


if __name__ == '__main__':
    main()

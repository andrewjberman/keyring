#!/usr/bin/env python3
"""
comp-pipescript -- authoritative pipeline dependency tool.

Usage:
    comp-pipescript dag                        # full execution DAG with I/O edges
    comp-pipescript io D_00                    # inputs + outputs for one script
    comp-pipescript chain downstream           # show chain membership + order
    comp-pipescript chain full                 # show full chain
    comp-pipescript feeds D_00                 # what scripts feed D_00 (upstream)
    comp-pipescript consumers D_00             # what scripts consume D_00 output
    comp-pipescript overlap D_00 D_03          # shared S3 artifacts between two scripts
    comp-pipescript inject                     # inject pipeline edges into comp-trace graph
    comp-pipescript stats                      # graph statistics

Data sources (authoritative, not heuristic):
    lib/s3_layout.py      -- every S3 key as a named constant
    gold_dispatch.sh      -- execution order, chains, groups, catalog
    each script's AST     -- from lib.s3_layout import (...) block
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_pipeline import (  # noqa: E402
    build_pipeline_dag, inject_pipeline_edges,
    build_inf_gold_dag, build_silver_dag, build_multi_pipeline_dag,
)

_PIPELINE_CHOICES = ("bd-gold", "inf-gold", "bd-silver", "inf-silver", "all")


def _build_dag(pipeline: str = "bd-gold"):
    """Return the appropriate DAG for the given pipeline scope.

    pipeline="bd-gold"  → existing BD-gold DAG (backward-compatible default)
    pipeline="inf-gold" → INF gold DAG only
    pipeline="bd-silver"→ BD silver DAG only
    pipeline="inf-silver"→ INF silver DAG only
    pipeline="all"      → combined multi-pipeline DAG (namespaced IDs)
    """
    if pipeline == "bd-gold":
        return build_pipeline_dag(_WORKSPACE)
    if pipeline == "inf-gold":
        return build_inf_gold_dag(_WORKSPACE)
    if pipeline == "bd-silver":
        return build_silver_dag(_WORKSPACE, "bd-silver", "data/black_diamond/scripts/silver")
    if pipeline == "inf-silver":
        return build_silver_dag(_WORKSPACE, "inf-silver", "data/orion/scripts/silver")
    if pipeline == "all":
        return build_multi_pipeline_dag(_WORKSPACE)
    return build_pipeline_dag(_WORKSPACE)


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_dag(args):
    pipeline = getattr(args, 'pipeline', 'bd-gold') or 'bd-gold'
    dag = _build_dag(pipeline)

    if args.json:
        result = {}
        for sid, sio in sorted(dag.scripts.items(), key=lambda x: x[1].run_order):
            result[sid] = {
                "filename": sio.filename,
                "pipeline": sio.pipeline,
                "group": sio.group,
                "run_order": sio.run_order,
                "reads": sio.read_keys,
                "writes": sio.write_keys,
                "feeds_from": [(u, k) for u, k, _ in dag.feeds(sid)],
                "feeds_to": [(d, k) for d, k, _ in dag.consumers(sid)],
            }
        print(json.dumps(result, indent=2))
        return

    print("PIPELINE DAG")
    print(f"  Pipeline: [{pipeline}]")
    print(f"  Scripts: {len(dag.scripts)}")
    print(f"  S3 keys: {len(dag.s3_keys)}")
    print()

    for sid, sio in sorted(dag.scripts.items(), key=lambda x: x[1].run_order):
        upstream = dag.feeds(sid)
        downstream = dag.consumers(sid)
        label = f"[{sio.pipeline}]" if sio.pipeline != "bd-gold" else ""
        print(f"  {sid} ({sio.filename}){' ' + label if label else ''}")
        print(f"    Group: {sio.group} | Order: {sio.run_order}")
        print(f"    Reads:  {len(sio.read_keys)} keys | Writes: {len(sio.write_keys)} keys")
        if upstream:
            scripts = sorted(set(u for u, _, _ in upstream))
            print(f"    Fed by: {', '.join(scripts)}")
        if downstream:
            scripts = sorted(set(d for d, _, _ in downstream))
            print(f"    Feeds:  {', '.join(scripts)}")
        print()


def cmd_io(args):
    pipeline = getattr(args, 'pipeline', 'bd-gold') or 'bd-gold'
    dag = _build_dag(pipeline)
    script_id = args.script_id.upper()

    # Allow partial match: "D_00" or "d_00" or "D_00.portal_aggregates"
    # Also allow unprefixed ID when pipeline is specified (e.g. "D_04" matches "inf-gold:D_04")
    sio = dag.scripts.get(script_id)
    if not sio:
        matches = [s for s in dag.scripts if script_id in s.upper()]
        if len(matches) == 1:
            sio = dag.scripts[matches[0]]
            script_id = matches[0]
        elif matches:
            print(f"Multiple matches: {', '.join(matches)}")
            sys.exit(1)
        else:
            print(f"Unknown script: {script_id}")
            print(f"Valid IDs: {', '.join(sorted(dag.scripts.keys()))}")
            sys.exit(1)

    if args.json:
        print(json.dumps({
            "script_id": script_id,
            "filename": sio.filename,
            "pipeline": sio.pipeline,
            "group": sio.group,
            "run_order": sio.run_order,
            "reads": [{"constant": c, "s3_key": dag.s3_keys[c].s3_path}
                      for c in sio.reads if c in dag.s3_keys],
            "writes": [{"constant": c, "s3_key": dag.s3_keys[c].s3_path}
                       for c in sio.writes if c in dag.s3_keys],
        }, indent=2))
        return

    print(f"I/O MANIFEST: {script_id} ({sio.filename}) [{sio.pipeline}]")
    print(f"  Group: {sio.group} | Order: {sio.run_order}")
    print()

    if sio.reads:
        print(f"  READS ({len(sio.reads)}):")
        for const in sio.reads:
            sk = dag.s3_keys.get(const)
            if sk:
                key = sk.s3_path
            elif const.startswith('[hardcoded] '):
                key = const[len('[hardcoded] '):]
            else:
                key = '?'
            prefix_tag = " [PREFIX]" if sk and sk.is_prefix else ""
            func_tag = " [FUNC]" if sk and sk.is_function else ""
            hc_tag = " [HARDCODED]" if const.startswith('[hardcoded] ') else ""
            # Show who writes this key (direct edges)
            writers = dag._writers.get(key, [])
            writers = [w for w in writers if w != script_id]
            # GAP 2: for PREFIX reads, also check implicit FUNC-write providers
            implicit = []
            if sk and sk.is_prefix:
                implicit = [w for w in dag._implicit_writers.get(key, [])
                            if w != script_id and w not in writers]
            if writers and implicit:
                writer_str = f" <- {', '.join(writers)}, IMPLICIT: {', '.join(implicit)} (via FUNC-key)"
            elif implicit:
                writer_str = f" <- IMPLICIT: {', '.join(implicit)} (via FUNC-key)"
            elif writers:
                writer_str = f" <- {', '.join(writers)}"
            else:
                writer_str = " <- (external/silver)"
            display_const = key if const.startswith('[hardcoded] ') else const
            print(f"    {display_const}: {key}{prefix_tag}{func_tag}{hc_tag}{writer_str}")
    else:
        print("  READS: (none detected)")

    # GAP 3: surface rolling-window candidates with a warning
    if sio.rolling_window_candidates:
        print()
        rw_set = set(sio.rolling_window_candidates)
        print(f"  ROLLING-WINDOW WARNING ({len(sio.rolling_window_candidates)} key(s)):")
        print("  The following FUNC keys appear in BOTH READS and WRITES for this script.")
        print("  This is commonly a prior-run (rolling-window) self-read pattern, OR")
        print("  a false positive from alias collision (`key = func(arg)` matches")
        print("  unrelated `get_object(Key=key)` calls elsewhere in the file).")
        print("  ACTION: verify manually -- is this read from a PRIOR run or current run?")
        for const in sorted(rw_set):
            sk = dag.s3_keys.get(const)
            key = sk.s3_path if sk else '?'
            writers = dag._writers.get(key, [])
            other_writers = [w for w in writers if w != script_id]
            src_str = f" <- {', '.join(other_writers)}" if other_writers else " <- (self-write only)"
            print(f"    {const}: {key} [ROLLING-WINDOW?]{src_str}")

    # Column gap analysis: find parquet columns accessed but not in _load_parquet columns= list
    try:
        script_path = _WORKSPACE / sio.file_path
        if script_path.exists():
            from org.modules.graph.extract_pipeline import _extract_column_gaps
            col_gaps = _extract_column_gaps(script_path)
            if col_gaps:
                print()
                print(f"  COLUMN GAPS ({len(col_gaps)}) -- columns accessed but not in _load_parquet columns= list:")
                for gap in col_gaps:
                    print(f"    !! {gap['var']}.{gap['col']}")
                    print(f"       accessed at line {gap['access_line']}, not in _load_parquet({gap['key_const']}, columns=[...]) at line {gap['load_line']}")
                    print(f"       loaded cols ({len(gap['loaded_cols'])}): {', '.join(gap['loaded_cols'][:6])}{'...' if len(gap['loaded_cols']) > 6 else ''}")
                    print(f"       FIX: add '{gap['col']}' to the columns= list at line {gap['load_line']}")
    except Exception:
        pass  # Don't break io output if column gap analysis fails

    print()

    if sio.writes:
        print(f"  WRITES ({len(sio.writes)}):")
        for const in sio.writes:
            sk = dag.s3_keys.get(const)
            if sk:
                key = sk.s3_path
            elif const.startswith('[hardcoded] '):
                key = const[len('[hardcoded] '):]
            else:
                key = '?'
            func_tag = " [FUNC]" if sk and sk.is_function else ""
            hc_tag = " [HARDCODED]" if const.startswith('[hardcoded] ') else ""
            # Show who reads this key
            readers = dag._readers.get(key, [])
            readers = [r for r in readers if r != script_id]
            reader_str = f" -> {', '.join(readers)}" if readers else " -> (terminal)"
            display_const = key if const.startswith('[hardcoded] ') else const
            print(f"    {display_const}: {key}{func_tag}{hc_tag}{reader_str}")
    else:
        print("  WRITES: (none detected)")

    # Dynamic refs: non-constant S3 reads (dim files, s3:// URIs, pandas reads)
    from org.modules.graph.extract_pipeline import _extract_dynamic_refs
    try:
        script_path = _WORKSPACE / sio.file_path
        script_content = script_path.read_text(encoding="utf-8", errors="replace")
        dynamic_refs = _extract_dynamic_refs(script_content)
        # Filter out paths already covered by hardcoded extraction
        covered = set(sio.read_keys) | set(sio.write_keys)
        new_dynamic = [d for d in dynamic_refs if not any(
            c.endswith(d.replace('{*}', '').rstrip('/')) or
            d.replace('{*}', '').rstrip('/') in c
            for c in covered
        )]
        if new_dynamic:
            print()
            print(f"  S3-DYNAMIC READS ({len(new_dynamic)}) [runtime-resolved, not in s3_layout]:")
            for path in new_dynamic:
                print(f"    {path}  [read-at-runtime]")
    except Exception:
        pass

    if not sio.reads and not sio.writes:
        print()
        print("  WARN: no s3_layout constants or hardcoded S3 paths detected.")
        print("  Script may use dynamic key construction, DynamoDB, SQS, or non-standard S3 patterns.")
        print("  Manual review of the script body is required for accurate I/O mapping.")

    # Platinum downstream: resolve platinum/* write targets to portal components
    platinum_writes = []
    for const in sio.writes:
        if const.startswith('[hardcoded] '):
            key = const[len('[hardcoded] '):]
        else:
            sk = dag.s3_keys.get(const)
            key = sk.s3_path if sk else None
        if key and 'platinum/' in key:
            platinum_writes.append(key)

    if platinum_writes and not args.no_portal:
        print()
        print("  PORTAL CONSUMERS (platinum keys -> routes -> components):")
        try:
            from org.modules.graph.extract_routes import build_routing_table
            rt = build_routing_table(_WORKSPACE)
            found_any = False
            for key in sorted(set(platinum_writes)):
                # Match routes: exact match or parameterized match ({*} in key)
                key_pattern = re.escape(key).replace(r'\{\*\}', '[^/]+') if '{*}' in key else None
                matching = []
                for r in rt.routes:
                    if not r.s3_key:
                        continue
                    if key_pattern:
                        if re.fullmatch(key_pattern, r.s3_key):
                            matching.append(r)
                    else:
                        # Exact or suffix match
                        if r.s3_key == key or r.s3_key.endswith(key) or key.endswith(r.s3_key):
                            matching.append(r)
                if matching:
                    found_any = True
                    print(f"    {key}")
                    for r in matching:
                        comps = ', '.join(r.components) if r.components else '(unknown component)'
                        auth_str = 'edge' if r.auth_edge else ('api-gw' if r.auth_api_gw else 'none')
                        print(f"      endpoint: {r.endpoint_function or '(unnamed)'} -> {r.url_pattern}")
                        print(f"      auth: {auth_str} | origin: {r.cf_origin_type}")
                        print(f"      components: {comps}")
            if not found_any:
                print("    (no route matches -- these platinum keys may be served via catch-all behavior)")
                print("    TIP: comp-platinum reverse <key> for a targeted reverse lookup")
        except Exception as e:
            print(f"    (routing table load failed: {e})")
    elif platinum_writes and args.no_portal:
        print()
        print(f"  PORTAL CONSUMERS: {len(platinum_writes)} platinum write(s) -- skipped (--no-portal)")


def cmd_chain(args):
    dag = _build_dag()
    chain_name = args.chain_name.lower()

    if chain_name not in dag.chains:
        print(f"Unknown chain: {chain_name}")
        print(f"Valid chains: {', '.join(sorted(dag.chains.keys()))}")
        sys.exit(1)

    script_ids = dag.chains[chain_name]
    print(f"CHAIN: {chain_name} ({len(script_ids)} scripts)")
    print()

    for i, sid in enumerate(script_ids, 1):
        sio = dag.scripts.get(sid)
        if sio:
            print(f"  {i:2d}. {sid:6s} {sio.filename}")
            print(f"         reads: {len(sio.read_keys)} | writes: {len(sio.write_keys)}")
        else:
            print(f"  {i:2d}. {sid:6s} (not found in scripts)")


def cmd_feeds(args):
    dag = _build_dag()
    script_id = args.script_id.upper()
    sio = dag.scripts.get(script_id)
    if not sio:
        print(f"Unknown script: {script_id}")
        sys.exit(1)

    upstream = dag.feeds(script_id)
    if not upstream:
        print(f"{script_id}: no upstream pipeline dependencies (reads from silver or external)")
        return

    if args.json:
        print(json.dumps([
            {"script": u, "s3_key": k, "constant": c}
            for u, k, c in upstream
        ], indent=2))
        return

    print(f"UPSTREAM FEEDS into {script_id}:")
    print()
    # Group by upstream script
    by_script: dict[str, list[tuple[str, str]]] = {}
    for u_script, s3_key, const in upstream:
        by_script.setdefault(u_script, []).append((s3_key, const))

    for u_script, keys in sorted(by_script.items()):
        print(f"  {u_script}:")
        for s3_key, const in keys:
            print(f"    {const}: {s3_key}")
    print()
    print(f"  Total: {len(upstream)} artifacts from {len(by_script)} scripts")


def cmd_consumers(args):
    dag = _build_dag()
    script_id = args.script_id.upper()
    sio = dag.scripts.get(script_id)
    if not sio:
        print(f"Unknown script: {script_id}")
        sys.exit(1)

    downstream = dag.consumers(script_id)
    if not downstream:
        print(f"{script_id}: no downstream pipeline consumers (terminal or portal-only)")
        return

    if args.json:
        print(json.dumps([
            {"script": d, "s3_key": k, "constant": c}
            for d, k, c in downstream
        ], indent=2))
        return

    print(f"DOWNSTREAM CONSUMERS of {script_id}:")
    print()
    by_script: dict[str, list[tuple[str, str]]] = {}
    for d_script, s3_key, const in downstream:
        by_script.setdefault(d_script, []).append((s3_key, const))

    for d_script, keys in sorted(by_script.items()):
        print(f"  {d_script}:")
        for s3_key, const in keys:
            print(f"    {const}: {s3_key}")
    print()
    print(f"  Total: {len(downstream)} artifacts consumed by {len(by_script)} scripts")


def cmd_overlap(args):
    dag = _build_dag()
    a = args.script_a.upper()
    b = args.script_b.upper()

    if a not in dag.scripts:
        print(f"Unknown script: {a}")
        sys.exit(1)
    if b not in dag.scripts:
        print(f"Unknown script: {b}")
        sys.exit(1)

    result = dag.overlap(a, b)
    if not result:
        print(f"No shared S3 artifacts between {a} and {b}")
        return

    print(f"OVERLAP: {a} <-> {b}")
    print()
    for relationship, keys in result.items():
        print(f"  {relationship}:")
        for key in keys:
            print(f"    {key}")
    print()


def cmd_inject(args):
    dag = _build_dag()
    added = inject_pipeline_edges(dag, _WORKSPACE)
    if added is None:
        print("No comp-trace graph cache found. Run comp-build first.")
        sys.exit(1)
    print(f"Injected {added} pipeline edges into comp-trace graph cache.")


def cmd_stats(args):
    dag = _build_dag()
    print("PIPELINE STATISTICS")
    print(f"  Scripts:    {len(dag.scripts)}")
    print(f"  S3 keys:    {len(dag.s3_keys)} ({sum(1 for k in dag.s3_keys.values() if k.is_prefix)} prefixes, {sum(1 for k in dag.s3_keys.values() if k.is_function)} functions)")
    print(f"  Chains:     {len(dag.chains)}")
    print(f"  Groups:     {len(dag.groups)}")
    print(f"  Catalog:    {len(dag.catalog)} entries")
    print()

    # Edge counts
    total_reads = sum(len(s.read_keys) for s in dag.scripts.values())
    total_writes = sum(len(s.write_keys) for s in dag.scripts.values())
    print(f"  Total read edges:  {total_reads}")
    print(f"  Total write edges: {total_writes}")
    print()

    # Scripts with no detected reads (likely missing extraction)
    no_reads = [sid for sid, s in dag.scripts.items() if not s.reads]
    if no_reads:
        print(f"  WARNING: {len(no_reads)} scripts with no detected reads:")
        for sid in sorted(no_reads):
            print(f"    {sid}")
    print()

    # Scripts with no detected writes
    no_writes = [sid for sid, s in dag.scripts.items() if not s.writes]
    if no_writes:
        print(f"  NOTE: {len(no_writes)} scripts with no detected writes:")
        for sid in sorted(no_writes):
            print(f"    {sid}")


def _get_ec2_manifest_service(service_key: str) -> dict:
    """Read a service entry from EC2_MANIFEST.json. Returns {} if not found."""
    manifest_path = _WORKSPACE / "infra" / "aws" / "ec2" / "EC2_MANIFEST.json"
    try:
        import json as _json
        data = _json.loads(manifest_path.read_text(encoding="utf-8"))
        return data.get("services", {}).get(service_key, {})
    except Exception:
        return {}


def cmd_deployed(args):
    """Compare local gold + silver script files against their S3-uploaded code versions.

    Default (--pipeline bd-gold): BD gold + BD silver vs opal-data-bd.
    --pipeline inf-gold: INF gold scripts vs opal-data-inf/code/gold/
      (runner key read from EC2_MANIFEST.json: inf-gold-layer-runner).
    --pipeline bd-silver: BD silver scripts only.
    --pipeline inf-silver: INF silver scripts vs opal-data-inf/code/silver/.

    Output is prefixed [bd-gold] / [inf-gold] / [bd-silver] / [inf-silver].
    Uses S3 ETag (MD5) comparison."""
    import hashlib
    import shutil
    import subprocess

    pipeline = getattr(args, 'pipeline', 'bd-gold') or 'bd-gold'

    S3_BUCKET = "opal-data-bd"
    S3_GOLD_PREFIX = "code/gold/"
    S3_SILVER_PREFIX = "code/silver/"
    SILVER_LOCAL_DIR = _WORKSPACE / "data" / "black_diamond" / "scripts" / "silver"

    # INF pipeline overrides
    if pipeline in ("inf-gold", "inf-silver"):
        S3_BUCKET = "opal-data-inf"

    # Resolve aws CLI once, full path -- avoids subprocess PATH-loss on some shells.
    aws_bin = shutil.which("aws") or shutil.which("aws.cmd") or shutil.which("aws.exe")
    if not aws_bin:
        print("  ERROR: aws CLI not found in PATH (checked aws, aws.cmd, aws.exe)")
        sys.exit(2)

    raw_filter = args.script_id.strip() if args.script_id else ""
    script_filter_upper = raw_filter.upper() if raw_filter else None
    script_filter_lower = raw_filter.lower() if raw_filter else None
    # Normalize a filename-style filter: strip .py so "bd_price_update.py" and "bd_price_update" both match.
    silver_filter_stem = (
        script_filter_lower[:-3] if script_filter_lower and script_filter_lower.endswith(".py")
        else script_filter_lower
    )

    aws_env = os.environ.copy()
    aws_env.setdefault("AWS_EC2_METADATA_DISABLED", "true")
    aws_env.setdefault("AWS_METADATA_SERVICE_NUM_ATTEMPTS", "1")
    aws_env.setdefault("AWS_PAGER", "")

    def _check_one(layer_tag, label, local_path, s3_key):
        """Returns (status, info_lines). Prints nothing -- caller does."""
        if not local_path.exists():
            return "LOCAL_MISSING", []
        local_md5 = hashlib.md5(local_path.read_bytes()).hexdigest()
        try:
            result = subprocess.run(
                [aws_bin, "s3api", "head-object",
                 "--bucket", S3_BUCKET,
                 "--key", s3_key,
                 "--query", "ETag",
                 "--output", "text"],
                capture_output=True, text=True, timeout=15, env=aws_env,
            )
        except subprocess.TimeoutExpired:
            return "TIMEOUT", [f"(aws CLI hung; AWS_EC2_METADATA_DISABLED={aws_env.get('AWS_EC2_METADATA_DISABLED', '')})"]
        if result.returncode != 0:
            stderr = (result.stderr or "").strip()
            # Disambiguate "S3 says no such key" from "we couldn't reach S3 at all".
            # MISSING_ON_S3 should only fire on a genuine 404 from HeadObject; any credential/network
            # failure is AWS_UNREACHABLE -- MATCH vs MISSING was never verifiable.
            _unreach_sig = (
                'Unable to locate credentials',
                'could not be found',         # bad/missing profile
                'ExpiredToken',
                'InvalidAccessKeyId',
                'SignatureDoesNotMatch',
                'InvalidClientTokenId',
                'Could not connect to the endpoint',
                'EndpointConnectionError',
                'ConnectTimeoutError',
                'ReadTimeoutError',
                'AccessDenied',
            )
            if any(sig in stderr for sig in _unreach_sig):
                return "AWS_UNREACHABLE", [stderr]
            if stderr:
                return "MISSING_ON_S3", [stderr]
            return "MISSING_ON_S3", []
        s3_etag = result.stdout.strip().strip('"')
        if local_md5 == s3_etag:
            return "MATCH", []
        return "STALE", [f"local:  {local_md5}", f"s3:     {s3_etag}"]

    # Header varies by pipeline
    if pipeline == "inf-gold":
        inf_svc = _get_ec2_manifest_service("inf-gold-layer-runner")
        inf_instance = inf_svc.get("instance_id", "unknown")
        print("DEPLOYED STATUS [inf-gold]: local repo vs s3://opal-data-inf/code/gold/")
        print(f"  Runner: inf-gold-layer-runner ({inf_instance})")
    elif pipeline in ("bd-silver", "inf-silver"):
        print(f"DEPLOYED STATUS [{pipeline}]: local repo vs s3://{S3_BUCKET}/code/silver/")
    else:
        print("DEPLOYED STATUS: local repo vs s3://opal-data-bd/code/{gold,silver}/")
    print()

    matched, stale, missing_s3, local_missing, timed_out, aws_unreach = [], [], [], [], [], []
    checked_any = False

    # ---- GOLD layer (DAG-driven) ----
    # For non-BD pipelines, skip BD gold entirely unless pipeline == "bd-gold" (default)
    if pipeline in ("inf-gold",):
        # INF gold: check against opal-data-inf/code/gold/
        inf_dag = _build_dag("inf-gold")
        inf_candidates = sorted(inf_dag.scripts.items(), key=lambda x: x[1].run_order)
        for sid, sio in inf_candidates:
            if script_filter_upper and script_filter_upper not in sid.upper():
                continue
            local_path = _WORKSPACE / sio.file_path
            label = f"[inf-gold] {sid}"
            checked_any = True
            status, extras = _check_one("inf-gold", label, local_path, f"{S3_GOLD_PREFIX}{sio.filename}")
            print(f"  [inf-gold] {sid:<10} {status:<14} {sio.filename}")
            for line in extras:
                print(f"             {line}")
            if status == "MATCH":
                matched.append(label)
            elif status == "STALE":
                stale.append(label)
            elif status == "MISSING_ON_S3":
                missing_s3.append(label)
            elif status == "LOCAL_MISSING":
                local_missing.append(label)
            elif status == "TIMEOUT":
                timed_out.append(label)
            elif status == "AWS_UNREACHABLE":
                aws_unreach.append(label)
    elif pipeline not in ("bd-silver", "inf-silver"):
        dag = _build_dag("bd-gold")
        gold_candidates = sorted(dag.scripts.items(), key=lambda x: x[1].run_order)
        skip_gold = False
        if script_filter_upper:
            any_gold_match = any(script_filter_upper in sid.upper() for sid, _ in gold_candidates)
            if not any_gold_match:
                skip_gold = True

        if not skip_gold:
            for sid, sio in gold_candidates:
                if script_filter_upper and script_filter_upper not in sid.upper():
                    continue
                local_path = _WORKSPACE / sio.file_path
                label = f"[bd-gold] {sid}"
                checked_any = True
                status, extras = _check_one("bd-gold", label, local_path, f"{S3_GOLD_PREFIX}{sio.filename}")
                print(f"  [bd-gold] {sid:<8} {status:<14} {sio.filename}")
                for line in extras:
                    print(f"           {line}")
                if status == "MATCH":
                    matched.append(label)
                elif status == "STALE":
                    stale.append(label)
                elif status == "MISSING_ON_S3":
                    missing_s3.append(label)
                elif status == "LOCAL_MISSING":
                    local_missing.append(label)
                elif status == "TIMEOUT":
                    timed_out.append(label)
                elif status == "AWS_UNREACHABLE":
                    aws_unreach.append(label)

    # ---- SILVER layer (directory-walk-driven) ----
    silver_files = []
    if SILVER_LOCAL_DIR.is_dir():
        for p in sorted(SILVER_LOCAL_DIR.glob("*.py")):
            if p.name.startswith("__"):
                continue
            silver_files.append(p)

    skip_silver = False
    if silver_filter_stem:
        any_silver_match = any(silver_filter_stem in p.stem.lower() for p in silver_files)
        # Silver filter only: if no silver match AND the filter clearly isn't a silver-shaped name,
        # leave skip_silver False so user sees "no matches" cleanly. But if gold matched and
        # silver has no match, suppress silver section entirely to avoid noise.
        if not any_silver_match and not skip_gold:
            skip_silver = True

    if not skip_silver and silver_files:
        for p in silver_files:
            if silver_filter_stem and silver_filter_stem not in p.stem.lower():
                continue
            label = f"[SILVER] {p.name}"
            checked_any = True
            status, extras = _check_one("SILVER", label, p, f"{S3_SILVER_PREFIX}{p.name}")
            print(f"  [SILVER] {p.name:<48} {status:<14}")
            for line in extras:
                print(f"           {line}")
            if status == "MATCH":
                matched.append(label)
            elif status == "STALE":
                stale.append(label)
            elif status == "MISSING_ON_S3":
                missing_s3.append(label)
            elif status == "LOCAL_MISSING":
                local_missing.append(label)
            elif status == "TIMEOUT":
                timed_out.append(label)
            elif status == "AWS_UNREACHABLE":
                aws_unreach.append(label)

    print()
    print(f"  Summary: {len(matched)} MATCH, {len(stale)} STALE, "
          f"{len(missing_s3)} MISSING_ON_S3, {len(local_missing)} LOCAL_MISSING, "
          f"{len(timed_out)} TIMEOUT, {len(aws_unreach)} AWS_UNREACHABLE")
    if aws_unreach:
        print(f"  AWS_UNREACHABLE: {', '.join(aws_unreach)}")
        print("  AWS credentials/network could not reach S3; MATCH/MISSING is NOT verified.")
        print("  Fix: check AWS_PROFILE / credentials / VPN, then re-run. See `aws sts get-caller-identity` to confirm.")
    if stale:
        print(f"  STALE: {', '.join(stale)}")
        print("  Run build-and-upload.sh (gold) or the silver upload pathway to sync.")
    elif timed_out:
        print(f"  TIMEOUT: {', '.join(timed_out)}")
        print("  AWS CLI resolution works, but head-object did not return before timeout.")
        print("  Check caller credentials/network, or rerun with AWS_EC2_METADATA_DISABLED=true in the invoking shell.")
    elif not stale and not missing_s3 and (matched or local_missing):
        print("  All checked scripts are up-to-date on S3.")
    elif not checked_any:
        print(f"  No scripts matched filter: {raw_filter!r}")


def cmd_postdeps(args):
    """Show and validate post-step dependencies and preconditions for gold scripts."""
    # Try PyYAML first; fall back to a minimal inline parser for our specific YAML shape
    deps_file = _WORKSPACE / "data" / "black_diamond" / "scripts" / "gold" / "gold_pipeline_deps.yaml"
    if not deps_file.exists():
        print("No gold_pipeline_deps.yaml found.")
        print(f"  Expected at: {deps_file}")
        sys.exit(1)

    raw = deps_file.read_text(encoding="utf-8")

    try:
        import yaml as _yaml
        deps = _yaml.safe_load(raw)
    except ImportError:
        # Minimal fallback parser: handles the specific structure in gold_pipeline_deps.yaml.
        # Supports top-level keys, script-name sub-keys, and flat key:value leaf pairs.
        # Not a general YAML parser -- only covers two-level dicts + lists of dicts.
        deps = _parse_deps_yaml_fallback(raw)

    if not isinstance(deps, dict):
        print("Failed to parse gold_pipeline_deps.yaml: unexpected structure.")
        sys.exit(1)

    post_steps = deps.get('post_steps') or {}
    preconditions = deps.get('preconditions') or {}

    script_filter = args.script_name if args.script_name else None

    print("PIPELINE DEPENDENCIES")
    print("  Config: data/black_diamond/scripts/gold/gold_pipeline_deps.yaml")
    print()

    has_output = False

    # Post-steps
    for script_name, steps in sorted(post_steps.items()):
        if script_filter and script_filter not in script_name:
            continue
        if not isinstance(steps, list):
            continue
        print(f"  POST-STEPS for {script_name}:")
        for step in steps:
            blocking = "BLOCKING" if step.get('blocking', True) else "ADVISORY"
            print(f"    [{blocking}] Must run: {step['script']}")
            print(f"             Reason: {step['reason']}")
            if 'incident' in step:
                print(f"             Incident: {step['incident']}")
        print()
        has_output = True

    # Preconditions
    for script_name, conditions in sorted(preconditions.items()):
        if script_filter and script_filter not in script_name:
            continue
        if not isinstance(conditions, list):
            continue
        print(f"  PRECONDITIONS for {script_name}:")
        for cond in conditions:
            blocking = "BLOCKING" if cond.get('blocking', True) else "WARN-ONLY"
            if 'artifact_s3' in cond:
                print(f"    [{blocking}] S3 artifact must exist: {cond['artifact_s3']}")
            elif 'condition' in cond:
                print(f"    [{blocking}] Condition: {cond['condition']}")
            print(f"             Reason: {cond['reason']}")
            if 'incident' in cond:
                print(f"             Incident: {cond['incident']}")
        print()
        has_output = True

    if not has_output:
        if script_filter:
            print(f"  No dependencies declared for: {script_filter}")
        else:
            print("  No dependencies declared.")


def _parse_deps_yaml_fallback(text: str) -> dict:
    """Minimal YAML parser for gold_pipeline_deps.yaml structure.
    Handles: top-level keys, script-name sub-keys, and lists of flat key:value dicts.
    Does NOT support anchors, multiline strings, or complex nesting beyond 3 levels.
    """
    result: dict = {}
    lines = text.splitlines()

    current_top: str | None = None        # e.g. 'post_steps'
    current_script: str | None = None     # e.g. 'build_canonical_prices_v2.py'
    current_list: list | None = None      # list being built under current_script
    current_item: dict | None = None      # dict being built for current list item

    def _flush_item():
        if current_list is not None and current_item:
            current_list.append(dict(current_item))

    def _unquote(s: str) -> str:
        s = s.strip()
        if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
            return s[1:-1]
        return s

    for raw_line in lines:
        stripped = raw_line.rstrip()
        if not stripped or stripped.lstrip().startswith('#'):
            continue

        indent = len(stripped) - len(stripped.lstrip())
        content = stripped.lstrip()

        # Remove inline comment (simple: find ' #' not inside quotes)
        if ' #' in content:
            # Only strip if the # is not inside a quoted string
            in_q = False
            q_char = None
            for ci, ch in enumerate(content):
                if ch in ('"', "'") and not in_q:
                    in_q = True
                    q_char = ch
                elif in_q and ch == q_char:
                    in_q = False
                elif ch == '#' and not in_q and ci > 0 and content[ci - 1] == ' ':
                    content = content[:ci].rstrip()
                    break

        # Top-level key (indent 0): post_steps: or preconditions:
        if indent == 0 and content.endswith(':') and ' ' not in content:
            _flush_item()
            current_item = None
            current_list = None
            current_script = None
            current_top = content[:-1]
            result[current_top] = {}
            continue

        # Script-name sub-key (indent 2): build_canonical_prices_v2.py:
        if indent == 2 and content.endswith(':') and current_top is not None:
            _flush_item()
            current_item = None
            current_script = content[:-1]
            current_list = []
            result[current_top][current_script] = current_list
            continue

        # List item marker (indent 4): - script: ...  or  - artifact_s3: ...
        if indent == 4 and content.startswith('- ') and current_list is not None:
            _flush_item()
            current_item = {}
            kv_part = content[2:].strip()
            if ':' in kv_part:
                k, _, v = kv_part.partition(':')
                v = v.strip()
                val: object = _unquote(v) if v else True
                if val == 'true':
                    val = True
                elif val == 'false':
                    val = False
                current_item[k.strip()] = val
            continue

        # Continuation key under list item (indent 6):   key: value
        if indent == 6 and ':' in content and current_item is not None:
            k, _, v = content.partition(':')
            v = v.strip()
            val = _unquote(v) if v else True
            if val == 'true':
                val = True
            elif val == 'false':
                val = False
            current_item[k.strip()] = val
            continue

    _flush_item()
    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        prog='comp-pipescript',
        description='Authoritative pipeline dependency tool for gold layer scripts.',
    )
    sub = parser.add_subparsers(dest='command')

    _pipeline_help = (
        'Pipeline scope: bd-gold (default), inf-gold, bd-silver, inf-silver, all. '
        'bd-gold is the BD gold layer (backward-compatible default). '
        'inf-gold checks INF gold scripts against opal-data-inf. '
        'all builds a combined cross-pipeline DAG with namespaced IDs.'
    )

    # dag
    p_dag = sub.add_parser('dag', help='Full execution DAG with I/O edges')
    p_dag.add_argument('--json', action='store_true', help='JSON output')
    p_dag.add_argument('--pipeline', '-p', default='bd-gold', choices=_PIPELINE_CHOICES, help=_pipeline_help)

    # io
    p_io = sub.add_parser('io', help='Input/output manifest for one script')
    p_io.add_argument('script_id', help='Script ID (e.g., D_00, I_D00, convert_assets_to_silver)')
    p_io.add_argument('--json', action='store_true', help='JSON output')
    p_io.add_argument('--no-portal', action='store_true', dest='no_portal',
                      help='Skip routing table lookup for portal consumer resolution')
    p_io.add_argument('--pipeline', '-p', default='bd-gold', choices=_PIPELINE_CHOICES, help=_pipeline_help)

    # chain
    p_chain = sub.add_parser('chain', help='Show chain membership and order')
    p_chain.add_argument('chain_name', help='Chain name (full, canonical, downstream, foundation, rebuild)')
    p_chain.add_argument('--pipeline', '-p', default='bd-gold', choices=_PIPELINE_CHOICES, help=_pipeline_help)

    # feeds
    p_feeds = sub.add_parser('feeds', help='What scripts feed this one (upstream)')
    p_feeds.add_argument('script_id', help='Script ID')
    p_feeds.add_argument('--json', action='store_true', help='JSON output')
    p_feeds.add_argument('--pipeline', '-p', default='bd-gold', choices=_PIPELINE_CHOICES, help=_pipeline_help)

    # consumers
    p_consumers = sub.add_parser('consumers', help='What scripts consume this one (downstream)')
    p_consumers.add_argument('script_id', help='Script ID')
    p_consumers.add_argument('--json', action='store_true', help='JSON output')
    p_consumers.add_argument('--pipeline', '-p', default='bd-gold', choices=_PIPELINE_CHOICES, help=_pipeline_help)

    # overlap
    p_overlap = sub.add_parser('overlap', help='Shared S3 artifacts between two scripts')
    p_overlap.add_argument('script_a', help='First script ID')
    p_overlap.add_argument('script_b', help='Second script ID')
    p_overlap.add_argument('--pipeline', '-p', default='bd-gold', choices=_PIPELINE_CHOICES, help=_pipeline_help)

    # inject
    sub.add_parser('inject', help='Inject pipeline edges into comp-trace graph cache')

    # stats
    sub.add_parser('stats', help='Pipeline graph statistics')

    # deployed
    p_deployed = sub.add_parser('deployed', help='Compare local scripts against S3-uploaded versions')
    p_deployed.add_argument('script_id', nargs='?', default='',
                            help='Optional: check only this script (e.g. D_00). Omit for all.')
    p_deployed.add_argument('--pipeline', '-p', default='bd-gold', choices=_PIPELINE_CHOICES, help=_pipeline_help)

    # postdeps
    p_postdeps = sub.add_parser('postdeps', help='Show post-step and precondition dependencies for gold scripts')
    p_postdeps.add_argument('script_name', nargs='?', default='',
                            help='Optional: filter to this script name (e.g. D_01 or build_canonical_prices_v2.py)')

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    commands = {
        'dag': cmd_dag,
        'io': cmd_io,
        'chain': cmd_chain,
        'feeds': cmd_feeds,
        'consumers': cmd_consumers,
        'overlap': cmd_overlap,
        'inject': cmd_inject,
        'stats': cmd_stats,
        'deployed': cmd_deployed,
        'postdeps': cmd_postdeps,
    }
    commands[args.command](args)


if __name__ == '__main__':
    main()

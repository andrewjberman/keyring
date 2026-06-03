#!/usr/bin/env python3
"""
comp-validate -- check gold artifact output invariants before S3 upload.

Usage:
    comp-validate D_04 --artifact /tmp/leaderboard.json
    comp-validate D_00 --artifact /tmp/timeseries_chart.json
    comp-validate --list                          # show all configured scripts and checks
    comp-validate D_04 --list                     # show checks for one script
    comp-validate nna_atomic --schema             # pass-through to standalone validator
    comp-validate role_aua --artifact /tmp/...    # standalone validator with args

Exits 0 if all ERROR-severity checks PASS.
Exits 1 if any ERROR-severity check FAILS.
Exits 0 if only WARN checks fail (prints warnings but does not block).

Config (BD):  data/black_diamond/scripts/gold/gold_validate_config.yaml
Config (INF): data/orion/scripts/gold/gold_validate_config.yaml
Pipeline is auto-detected from script_id prefix: INF_* -> INF config; others -> BD config.

Standalone validators: data/black_diamond/scripts/validators/validate_{script_id}.py
When extra flags (e.g. --schema, --certified, --cross-check) are present OR the
script_id has no config entry, the CLI dispatches to the standalone validator
via sys.executable with all trailing flags preserved (ADVI_ROLLUP ADHC_ROUTER.T4,
closes proposal E pass-through gap from COMPILER_VALIDATE_COVERAGE_AND_PASSTHROUGH.md).
"""

from __future__ import annotations

import argparse
import platform
import subprocess
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_validate import load_validate_config, run_validate  # noqa: E402

STANDALONE_VALIDATORS_DIR = _WORKSPACE / "data" / "black_diamond" / "scripts" / "validators"

_BD_VALIDATE_CONFIG = _WORKSPACE / "data" / "black_diamond" / "scripts" / "gold" / "gold_validate_config.yaml"
_INF_VALIDATE_CONFIG = _WORKSPACE / "data" / "orion" / "scripts" / "gold" / "gold_validate_config.yaml"


def _translate_artifact_path(raw: str) -> Path:
    """On Windows, translate POSIX /tmp/ and /c/ paths to native Windows paths.

    Linux/macOS: paths pass through unchanged.
    Windows (platform.system() == 'Windows', mocked via sitecustomize.py per
    MEMORY.md "AWS CLI Hang Fixes Fix 2"):
      /tmp/foo.json              -> C:/tmp/foo.json
      /c/Users/AndrewBerman/...  -> C:/Users/AndrewBerman/...
    Any other path is returned as-is.

    Caller is responsible for checking existence and emitting the dual-path
    error message when neither original nor translated path exists.
    """
    if platform.system() != 'Windows':
        return Path(raw)
    if raw.startswith('/tmp/'):
        return Path('C:/tmp/' + raw[5:])
    if raw.startswith('/c/'):
        return Path('C:/' + raw[3:])
    return Path(raw)


def _load_raw_validate_configs() -> dict:
    """Load both BD and INF gold_validate_config.yaml as raw dicts (for alias map).

    Returns merged {artifact_id: raw_data_dict} from both pipelines.
    """
    result: dict = {}
    for config_file in (_BD_VALIDATE_CONFIG, _INF_VALIDATE_CONFIG):
        if not config_file.exists():
            continue
        try:
            import yaml
            raw = yaml.safe_load(config_file.read_text(encoding="utf-8"))
            result.update((raw.get("scripts") or {}))
        except Exception:
            pass
    return result


def _build_script_alias_map(raw_configs: dict) -> dict[str, list[str]]:
    """Build {producer_script.upper(): [artifact_id, ...]} from raw config entries.

    Populated when config entries carry a producer_script field (ADHC_COMPIL.015).
    """
    alias_map: dict[str, list[str]] = {}
    for artifact_id, data in raw_configs.items():
        if not data:
            continue
        ps = data.get("producer_script")
        if ps:
            alias_map.setdefault(str(ps).upper(), []).append(artifact_id)
    return alias_map


def _resolve_artifact_id(
    script_id: str,
    artifact_filename: str,
    configs: dict,
    alias_map: dict[str, list[str]],
) -> tuple[str, str | None]:
    """Resolve script_id to a canonical artifact-id present in configs.

    Resolution order:
    1. Alias-map lookup when artifact_filename is provided. Checked first so that
       a script_id like D_04 (which is both an artifact-id AND a producer of multiple
       artifacts) is disambiguated by filename rather than silently matched to the
       wrong artifact (the leaderboard entry).
    2. Direct artifact-id lookup (exact, then case-insensitive).
    3. Alias-map lookup when no artifact_filename (emits candidate list + exit 1).
    4. Not found → "Did you mean" suggestion + exit 1.

    Returns (artifact_id, info_line). info_line is non-None when an alias
    resolution was performed; caller should emit it as an info message.
    Exits 1 on failure.
    """
    from difflib import get_close_matches

    upper = script_id.upper()
    stem = Path(artifact_filename).stem.lower() if artifact_filename else ""
    alias_candidates = alias_map.get(upper, [])

    # 1. Alias-map path (only when artifact_filename is present)
    if alias_candidates and artifact_filename:
        if len(alias_candidates) == 1:
            return alias_candidates[0], f"Resolved {script_id} -> {alias_candidates[0]}"

        # Multiple artifacts — disambiguate by artifact filename stem
        if stem:
            fname_matches = [c for c in alias_candidates
                             if stem == c.lower() or c.lower() in stem or stem in c.lower()]
            if len(fname_matches) == 1:
                return fname_matches[0], f"Resolved {script_id} -> {fname_matches[0]}"

        # Ambiguous — list all candidates
        _emit_ambiguous_error(script_id, alias_candidates, artifact_filename, stem)
        sys.exit(1)

    # 2. Direct artifact-id (exact match)
    if script_id in configs:
        return script_id, None
    if upper in configs:
        return upper, None
    ci_matches = [k for k in configs if k.upper() == upper]
    if len(ci_matches) == 1:
        return ci_matches[0], None

    # 3. Alias-map path without artifact_filename — emit candidate list
    if alias_candidates:
        _emit_ambiguous_error(script_id, alias_candidates, artifact_filename, stem)
        sys.exit(1)

    # 4. Not found — Did-you-mean across artifact-ids + alias keys
    all_candidates = list(configs.keys()) + list(alias_map.keys())
    close = get_close_matches(upper, [c.upper() for c in all_candidates], n=3, cutoff=0.4)
    # Map back to original case
    upper_to_orig = {c.upper(): c for c in all_candidates}
    close_orig = [upper_to_orig.get(c, c) for c in close]
    if close_orig:
        print(f"Error: '{script_id}' not found. Did you mean: {', '.join(close_orig)}?",
              file=sys.stderr)
    else:
        print(f"Error: '{script_id}' is not a known artifact-id or producer script.",
              file=sys.stderr)
        print("  Run `comp-validate --list` to see all configured artifact-ids.",
              file=sys.stderr)
    sys.exit(1)


def _emit_ambiguous_error(
    script_id: str,
    candidates: list[str],
    artifact_filename: str,
    stem: str,
) -> None:
    """Print the multi-artifact disambiguation error to stderr."""
    print(f"Error: '{script_id}' is a producer script, not an artifact-id.", file=sys.stderr)
    print(f"  {script_id} produces {len(candidates)} artifact(s):", file=sys.stderr)
    for c in sorted(candidates):
        print(f"    {c}", file=sys.stderr)
    if not artifact_filename or not stem:
        print("  Pass --artifact <path> with a filename matching one of them.", file=sys.stderr)
    else:
        print(f"  Filename '{artifact_filename}' did not match any of the above.", file=sys.stderr)
        print("  Use the exact artifact-id as the first argument instead.", file=sys.stderr)


def _find_standalone_validator(script_id: str) -> Path | None:
    """Return path to data/.../validators/validate_{script_id}.py if it exists."""
    if not script_id:
        return None
    candidate = STANDALONE_VALIDATORS_DIR / f"validate_{script_id}.py"
    return candidate if candidate.is_file() else None


def _dispatch_standalone(validator_path: Path, passthrough_args: list[str]) -> int:
    """Invoke a standalone validator via sys.executable, forwarding all args verbatim.

    Preserves the validator's exit code and stderr so pass-through is transparent.
    """
    print(f"COMP-VALIDATE: dispatching to standalone validator {validator_path.name}")
    print(f"  args: {passthrough_args}")
    print()
    completed = subprocess.run(
        [sys.executable, str(validator_path), *passthrough_args],
        cwd=str(_WORKSPACE),
    )
    return completed.returncode


def cmd_list(args):
    bd_configs = load_validate_config(_WORKSPACE)
    inf_configs = load_validate_config(_WORKSPACE, _INF_VALIDATE_CONFIG)
    configs = {**bd_configs, **inf_configs}
    if not configs:
        print("No validate config found.")
        print("  Expected: data/black_diamond/scripts/gold/gold_validate_config.yaml")
        print("         or data/orion/scripts/gold/gold_validate_config.yaml")
        return

    script_filter = args.script_id or ""
    lane_filter = getattr(args, "lane", None)

    print(f"VALIDATE CONFIG ({len(configs)} scripts)")
    print("  Config (BD):  data/black_diamond/scripts/gold/gold_validate_config.yaml")
    print("  Config (INF): data/orion/scripts/gold/gold_validate_config.yaml")
    print()

    # ADHC_COMPIL_V4.021 Cat 5.2: tighten matcher to exact-or-prefix-with-underscore-boundary
    # Previously substring match meant "D_04" matched D_04 + INF_D_04 + D_04_positions_output.
    # Now: exact-match OR prefix-followed-by-underscore (so "D_04" matches "D_04" + "D_04_positions_output"
    # but NOT "INF_D_04"; user can pass "INF_D_04" to filter to INF-only).
    def _matches(sid: str, sf: str) -> bool:
        if not sf:
            return True
        sf_u = sf.upper()
        sid_u = sid.upper()
        if sid_u == sf_u:
            return True
        if sid_u.startswith(sf_u + "_"):
            return True
        return False

    # ADHC_COMPIL_V4.021 Cat 5.2: --lane filter scopes to one config (bd/inf)
    def _lane_of(sid: str) -> str:
        return "inf" if sid.upper().startswith("INF_") else "bd"

    matched_count = 0
    for sid, config in sorted(configs.items()):
        if not _matches(sid, script_filter):
            continue
        if lane_filter and _lane_of(sid) != lane_filter:
            continue

        matched_count += 1
        artifact_str = config.primary_artifact or "(no primary artifact)"
        print(f"  {sid}  ({artifact_str})")

        if config.checks:
            for check in config.checks:
                sev = check.get("severity", "WARN")
                ctype = check.get("type", "?")
                cname = check.get("name", "unnamed")
                print(f"    [{sev}] {cname} (type: {ctype})")
                if check.get("why"):
                    print(f"          {check['why']}")
        else:
            print("    (no checks declared)")
        print()

    # ADHC_COMPIL_V4.021 Cat 5.3: emit error + candidate hints if filter matched nothing
    if script_filter and matched_count == 0:
        candidates = sorted(configs.keys())
        print(f"ERROR: no script matching {script_filter!r}", file=sys.stderr)
        print("  First 15 candidates:", file=sys.stderr)
        for c in candidates[:15]:
            print(f"    {c}", file=sys.stderr)
        if len(candidates) > 15:
            print(f"    ... and {len(candidates) - 15} more", file=sys.stderr)
        sys.exit(1)


def cmd_validate(args):
    # Config-file resolution priority:
    #   1. Explicit --config <path> (TO-9 AC1) — overrides everything
    #   2. Auto-detect from script_id prefix: INF_* -> INF config (TO-9 AC2)
    #   3. Default: BD config
    explicit_config = getattr(args, 'config', None)
    if explicit_config:
        cfg_path = Path(explicit_config)
        if not cfg_path.is_absolute():
            cfg_path = (_WORKSPACE / cfg_path).resolve()
        if not cfg_path.exists():
            print(f"ERROR: --config path not found: {cfg_path}", file=sys.stderr)
            sys.exit(2)
        _config_file = cfg_path
    else:
        # Auto-detect pipeline from script_id prefix: INF_* -> INF config; others -> BD.
        _sid_upper = (args.script_id or "").upper()
        _config_file = _INF_VALIDATE_CONFIG if _sid_upper.startswith("INF_") else None
    configs = load_validate_config(_WORKSPACE, _config_file)
    strict = getattr(args, 'strict', False)

    # Build alias map for script-id -> artifact-id resolution (ADHC_COMPIL.015)
    raw_configs = _load_raw_validate_configs()
    alias_map = _build_script_alias_map(raw_configs)

    # Translate artifact path (Windows POSIX path fix, ADHC_COMPIL.009)
    artifact_path = _translate_artifact_path(args.artifact)

    # Resolve script_id -> canonical artifact-id (catches unknown IDs early)
    artifact_filename = Path(args.artifact).name if args.artifact else ""
    resolved_id, info_line = _resolve_artifact_id(
        args.script_id, artifact_filename, configs, alias_map
    )

    # Artifact must exist (hard FAIL — unsafe to gate on missing file)
    if not artifact_path.exists():
        translated_str = str(artifact_path)
        print("MISSING_ARTIFACT:", file=sys.stderr)
        if platform.system() == 'Windows' and args.artifact != translated_str:
            print(f"  Input path:      {args.artifact}", file=sys.stderr)
            print(f"  Translated path: {translated_str}", file=sys.stderr)
        else:
            print(f"  {artifact_path} not found", file=sys.stderr)
        print("Hint: see COMP_VALIDATE_PROTOCOL.md §4 for retry policy", file=sys.stderr)
        sys.exit(1)

    print(f"VALIDATE: {resolved_id}")
    if info_line:
        print(f"  Info: {info_line}")
    print(f"  Artifact: {artifact_path}")
    print()

    results = run_validate(resolved_id, artifact_path, configs)

    error_count = 0
    warn_count = 0
    pass_count = 0
    skip_count = 0

    for r in results:
        if r.status == "PASS":
            pass_count += 1
            print(f"  PASS  [{r.severity}] {r.name}")
            print(f"         {r.message}")
        elif r.status == "FAIL":
            if r.severity == "ERROR":
                error_count += 1
                print(f"  FAIL  [{r.severity}] {r.name}")
            else:
                warn_count += 1
                print(f"  WARN  [{r.severity}] {r.name}")
            print(f"         {r.message}")
            if r.detail:
                print(f"         Why: {r.detail}")
        elif r.status == "SKIP":
            skip_count += 1
            print(f"  SKIP  [{r.severity}] {r.name}: {r.message}")
        elif r.status == "ERROR":
            error_count += 1
            print(f"  ERROR [{r.severity}] {r.name}: {r.message}")
        elif r.status == "WAIVED":
            print(f"  WAIVED [{r.severity}] {r.name}: {r.message}")
        print()

    print(f"  Summary: {pass_count} PASS, {error_count} ERROR, {warn_count} WARN, {skip_count} SKIP")

    # EXPLICIT WAIVER short-circuit (CTO ruling): a deliberate `validation: not_required`
    # decision PASSES (exit 0) -- auditable + distinct from true NO_CONFIG (UNVALIDATED).
    if any(r.status == "WAIVED" for r in results):
        wr = next(r for r in results if r.status == "WAIVED")
        print()
        print(f"WAIVED: {wr.message} -- exit 0 (explicit not_required decision; NOT an unchecked pass).")
        return

    # Detect NO_CONFIG: all results are SKIP from config_lookup or no_checks
    no_config = all(r.status == "SKIP" for r in results) and any(
        r.name in ("config_lookup", "no_checks") for r in results
    )

    if no_config:
        print()
        print(f"NO_CONFIG: no validation rules defined for {resolved_id}")
        print("  UNVALIDATED -- this is NOT a pass. ZERO checks ran (no config stanza for this")
        print("  artifact). Do NOT read exit-0 here as 'safe to signal' -- nothing was verified.")
        print("  Add a gold_validate_config.yaml stanza, or run with --strict (exit 2) in")
        print("  gates/dispatchers so absence-of-config blocks instead of silently passing.")
        if strict:
            print("  (--strict: escalating NO_CONFIG to exit 2)")
            sys.exit(2)
        return

    if error_count > 0:
        print()
        print(f"FAIL: {error_count}/{pass_count + warn_count + error_count} check(s) failed for {resolved_id}")
        print(f"  BLOCKED: {error_count} ERROR check(s) failed. Do not upload artifact to S3.")
        sys.exit(1)
    elif warn_count > 0:
        print()
        print(f"  ADVISORY: {warn_count} WARN check(s) failed. Review before uploading.")
        print(f"PASS: all checks passed for {resolved_id} ({warn_count} WARN advisory)")
    else:
        print()
        print(f"PASS: all {pass_count} checks passed for {resolved_id}")
        print("  All checks passed. Artifact is ready for S3 upload.")


def _ast_classify_gold_script(path: Path) -> tuple[str, list[int]]:
    """Classify a gold script for NaN-safe JSON-emit compliance via AST analysis.

    Returns (classification, json_emit_line_numbers).
    classification: 'PASS' | 'INLINE' | 'NEITHER' | 'N/A' | 'ERROR'

    Priority order (highest wins):
      PASS    — imports safe_json_serialize + calls safe_json_dumps
      INLINE  — defines inline _strip_nan OR uses json.dumps(..., allow_nan=False)
      NEITHER — any json.dumps/json.dump call without the above guards
      N/A     — no json.dumps/json.dump calls at all (parquet/CSV-only script)
    """
    import ast as _ast

    try:
        source = path.read_text(encoding='utf-8')
        tree = _ast.parse(source, filename=str(path))
    except SyntaxError:
        return 'ERROR', []

    has_safe_json_import = False
    has_safe_json_call = False
    has_inline_strip_nan = False
    has_allow_nan_false = False
    json_emit_lines: list[int] = []

    for node in _ast.walk(tree):
        if isinstance(node, _ast.ImportFrom):
            if node.module == 'safe_json_serialize':
                has_safe_json_import = True
        elif isinstance(node, _ast.Import):
            for alias in node.names:
                if alias.name == 'safe_json_serialize':
                    has_safe_json_import = True

        if isinstance(node, _ast.Call):
            func = node.func
            if isinstance(func, _ast.Name) and func.id == 'safe_json_dumps':
                has_safe_json_call = True
            elif isinstance(func, _ast.Attribute) and func.attr == 'safe_json_dumps':
                has_safe_json_call = True
            if (isinstance(func, _ast.Attribute)
                    and func.attr in ('dumps', 'dump')
                    and isinstance(func.value, _ast.Name)
                    and func.value.id == 'json'):
                for kw in node.keywords:
                    if (kw.arg == 'allow_nan'
                            and isinstance(kw.value, _ast.Constant)
                            and kw.value.value is False):
                        has_allow_nan_false = True
                json_emit_lines.append(node.lineno)

        if isinstance(node, (_ast.FunctionDef, _ast.AsyncFunctionDef)):
            if '_strip_nan' in node.name:
                has_inline_strip_nan = True

    if has_safe_json_import and has_safe_json_call:
        return 'PASS', json_emit_lines
    if has_inline_strip_nan or has_allow_nan_false:
        return 'INLINE', json_emit_lines
    if json_emit_lines:
        return 'NEITHER', json_emit_lines
    return 'N/A', []


def cmd_gold_nan(args: argparse.Namespace) -> None:
    """gold-nan subcommand: audit all gold scripts for NaN-safe JSON-emit compliance.

    Walks data/orion/scripts/gold/*.py (top-level only; lib/ and tests/ excluded).
    Classifies each script as PASS / INLINE / NEITHER / N/A.
    Writes per-script YAML manifests + chain-wide REPORT.md to
    org/modules/graph/gold-nan/.

    --strict exits 1 if any NEITHER-class scripts are detected.
    """
    import yaml as _yaml

    strict = getattr(args, 'strict', False)
    gold_dir = _WORKSPACE / 'data' / 'orion' / 'scripts' / 'gold'
    output_dir = _WORKSPACE / 'org' / 'modules' / 'graph' / 'gold-nan'
    output_dir.mkdir(parents=True, exist_ok=True)

    scripts: list[Path] = sorted(gold_dir.glob('*.py'))
    scripts = [p for p in scripts if not p.name.startswith('__')]

    pass_list: list[tuple[str, Path]] = []
    inline_list: list[tuple[str, Path]] = []
    neither_list: list[tuple[str, Path]] = []
    na_list: list[tuple[str, Path]] = []

    print('COMP-VALIDATE gold-nan: NaN-safe JSON-emit compliance audit')
    print(f'  Lane: data/orion/scripts/gold/ ({len(scripts)} top-level scripts)')
    print()

    for script_path in scripts:
        script_id = script_path.stem
        rel = script_path.relative_to(_WORKSPACE).as_posix()
        classification, emit_lines = _ast_classify_gold_script(script_path)

        entry = (script_id, script_path)
        if classification == 'PASS':
            pass_list.append(entry)
        elif classification == 'INLINE':
            inline_list.append(entry)
        elif classification == 'NEITHER':
            neither_list.append(entry)
        else:
            na_list.append(entry)

        if classification != 'N/A':
            yaml_data = {
                'script_id': script_id,
                'path': rel,
                'classification': classification,
                'emit_sites': [f'line {ln}' for ln in emit_lines] if emit_lines else [],
            }
            yaml_path = output_dir / f'{script_id}.yaml'
            with open(yaml_path, 'w', encoding='utf-8') as f:
                _yaml.dump(yaml_data, f, default_flow_style=False, sort_keys=False)

        label_map = {'PASS': 'PASS   ', 'INLINE': 'INLINE ', 'NEITHER': 'NEITHER', 'N/A': 'N/A    ', 'ERROR': 'ERROR  '}
        label = label_map.get(classification, classification)
        sites_str = f' ({len(emit_lines)} json.dumps site(s))' if emit_lines else ''
        print(f'  {label}  {script_id}{sites_str}')

    total_with_emit = len(pass_list) + len(inline_list) + len(neither_list)
    total = total_with_emit + len(na_list)

    def _pct(n: int) -> str:
        return f'{n/max(1, total_with_emit)*100:.0f}%'

    report_lines = [
        '# gold-nan NaN-Compliance Audit Report',
        '',
        '**Generated:** 2026-05-14 (ADHC_COMPIL_V4.029b)',
        '**Lane:** `data/orion/scripts/gold/` (top-level scripts only; lib/ and tests/ excluded)',
        '',
        '## Summary',
        '',
        '| Classification | Count | % of emit-boundary scripts |',
        '|---|---|---|',
        f'| PASS    | {len(pass_list)}  | {_pct(len(pass_list))} |',
        f'| INLINE  | {len(inline_list)}  | {_pct(len(inline_list))} |',
        f'| NEITHER | {len(neither_list)} | {_pct(len(neither_list))} |',
        f'| N/A (no JSON emit) | {len(na_list)} | — |',
        f'| **Total** | **{total}** | |',
        '',
        '## PASS (compliant — safe_json_dumps from shared lib)',
        '',
    ]
    if pass_list:
        for sid, p in pass_list:
            report_lines.append(f'- `{sid}` (`{p.relative_to(_WORKSPACE).as_posix()}`)')
    else:
        report_lines.append('(none)')

    report_lines += ['', '## INLINE (opportunistic-refactor candidates)', '']
    if inline_list:
        for sid, p in inline_list:
            report_lines.append(f'- `{sid}` (`{p.relative_to(_WORKSPACE).as_posix()}`)')
    else:
        report_lines.append('(none — no inline _strip_nan defs or allow_nan=False found)')

    report_lines += ['', '## NEITHER (silent-drift risk — follow-up TOs needed)', '']
    if neither_list:
        for sid, p in neither_list:
            report_lines.append(f'- `{sid}` (`{p.relative_to(_WORKSPACE).as_posix()}`)')
    else:
        report_lines.append('(none)')

    report_lines += ['', '## N/A (no JSON-emit boundary — parquet/CSV-only scripts)', '']
    if na_list:
        for sid, _ in na_list:
            report_lines.append(f'- `{sid}`')
    else:
        report_lines.append('(none)')

    report_lines += [
        '',
        '## Upgrade Path',
        '',
        'For all NEITHER-class scripts, migrate each S3-emit `json.dumps` to `safe_json_dumps`:',
        '',
        '```python',
        'from safe_json_serialize import safe_json_dumps  # noqa: E402',
        '# before: body = json.dumps(obj, default=str, separators=(",", ":"))',
        '# after:  body = safe_json_dumps(obj, default=str, separators=(",", ":"))',
        '```',
        '',
        'Shared lib: `data/orion/scripts/gold/lib/safe_json_serialize.py`',
        'S3 mirror: `s3://opal-data-inf/code/gold/lib/safe_json_serialize.py`',
        '',
        '## Ruling',
        '',
        '**AC2:** This enumeration is NOT a forced migration. NEITHER-class scripts are flagged',
        'for opportunistic follow-up TOs (DS lanes). No immediate data reprocess required.',
        'Priority order for follow-up: INF_D portal-emit scripts first (user-facing JSON);',
        'C/B-chain parquet-adjacent scripts second.',
    ]

    report_path = output_dir / 'REPORT.md'
    report_path.write_text('\n'.join(report_lines) + '\n', encoding='utf-8')

    print()
    print(f'  Summary: {len(pass_list)} PASS | {len(inline_list)} INLINE | {len(neither_list)} NEITHER | {len(na_list)} N/A')
    print(f'  Report written: {report_path.relative_to(_WORKSPACE)}')
    print(f'  Per-script YAMLs written: {output_dir.relative_to(_WORKSPACE)}/{{script_id}}.yaml')
    print()

    if neither_list:
        print(f'  NEITHER-class ({len(neither_list)} scripts flagged for follow-up):')
        for sid, _ in neither_list:
            print(f'    {sid}')
        print()

    if strict and neither_list:
        print(f'FAIL: --strict: {len(neither_list)} NEITHER-class script(s) detected (exit 1)')
        sys.exit(1)

    if strict:
        print('PASS: --strict: no NEITHER-class scripts detected')

    print('PASS: gold-nan audit complete')


def main():
    parser = argparse.ArgumentParser(
        prog='comp-validate',
        description='Validate gold artifact output invariants before S3 upload.',
    )
    parser.add_argument('script_id', nargs='?', default='',
                        help='Script ID (e.g., D_04, D_00, build_canonical_prices_v2)')
    parser.add_argument('--artifact', default='',
                        help='Path to local artifact file (.json or .parquet)')
    parser.add_argument('--list', action='store_true', dest='list_only',
                        help='List all configured checks and exit')
    parser.add_argument('--strict', action='store_true',
                        help='Escalate NO_CONFIG to exit 2 (for CI/dispatcher use). '
                             '(Per CTO ruling this becomes the DEFAULT post-migration; flag kept for back-compat.)')
    parser.add_argument('--lenient', action='store_true',
                        help='Post-flip escape hatch: restore exit-0 on NO_CONFIG for rare '
                             'transitional use. Prefer an explicit `validation: not_required` waiver stanza instead.')
    parser.add_argument('--config', default=None,
                        help='Explicit path to gold_validate_config.yaml; overrides INF_*/BD auto-detection (TO-9)')
    parser.add_argument('--lane', choices=['bd', 'inf'], default=None,
                        help='Filter --list to one lane (V4.021 Cat 5.2)')

    # Use parse_known_args() so unknown flags (e.g. --schema, --certified,
    # --cross-check) become pass-through args for the standalone validator
    # instead of hard-erroring in argparse (proposal E).
    args, extras = parser.parse_known_args()

    # gold-nan subcommand (ADHC_COMPIL_V4.029b)
    if args.script_id == 'gold-nan':
        cmd_gold_nan(args)
        return

    # List path is unchanged.
    if args.list_only:
        cmd_list(args)
        return

    # Pass-through dispatch: if extras are present OR no --artifact is given
    # (which the config engine requires), try routing to the standalone
    # validator at data/black_diamond/scripts/validators/validate_{id}.py.
    if extras or not args.artifact:
        standalone = _find_standalone_validator(args.script_id)
        if standalone is not None:
            # Reconstruct full arg list for the standalone script: if --artifact
            # was parsed by us, translate path and forward it back; ditto extras.
            forward: list[str] = []
            if args.artifact:
                forward.extend(['--artifact', str(_translate_artifact_path(args.artifact))])
            forward.extend(extras)
            sys.exit(_dispatch_standalone(standalone, forward))

        # No standalone validator + no artifact = show config list (existing
        # behavior for bare `comp-validate` or `comp-validate <id>`).
        if not args.artifact and not extras:
            # If script_id is a multi-artifact producer, emit candidate list
            # rather than silently falling through to cmd_list (AC4).
            if args.script_id:
                _raw = _load_raw_validate_configs()
                _amap = _build_script_alias_map(_raw)
                _cands = _amap.get(args.script_id.upper(), [])
                if len(_cands) > 1:
                    _emit_ambiguous_error(args.script_id, _cands, "", "")
                    sys.exit(1)
            cmd_list(args)
            return

        # Extras supplied but no route for them: surface clearly rather than
        # silently dropping flags.
        print(
            f"comp-validate: unrecognized arguments {extras} and no standalone "
            f"validator found for '{args.script_id}' at "
            f"{STANDALONE_VALIDATORS_DIR.relative_to(_WORKSPACE)}/"
            f"validate_{args.script_id}.py",
            file=sys.stderr,
        )
        sys.exit(2)

    if not args.script_id:
        parser.print_help()
        sys.exit(1)

    cmd_validate(args)


if __name__ == '__main__':
    main()

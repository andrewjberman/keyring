#!/usr/bin/env python3
"""VALGATE D-1 -- adapter-threading gate (ADHC_VALGATE.004).

Structural fire + verdict around comp-adapter-audit (ADHC_COMPIL_V4.031).
Fires at portal pre-push. For each partner-facing static adapter changed in
the push, invokes the adapter-audit and renders a PASS / WARN / BLOCK verdict.

This is NOT a new diagnostic -- comp-adapter-audit produces the field-by-field
audit; D-1 is the structural fire (a pre-push hook step) and the verdict policy.

Section-3.2 gate anatomy
------------------------
  Trigger     portal pre-push hook, every push, per changed ref.
  Input       each partner-facing static adapter fn changed in the push.
  Reference   the most-recent S3 platinum envelope for that adapter's data
              source (fetched by comp-adapter-audit).
  Comparison  field-by-field threading audit -- adapter_audit_cli findings.
  Verdict     PASS  no findings.
              WARN  drift findings only (SCHEMA-DRIFT / NESTED-SCHEMA-DRIFT
                    / TYPE-ONLY / NOT-THREADED) -- a field exists but the
                    type/adapter is stale, or a raw field is unconsumed; the
                    partner surface is not data-absent.
              BLOCK un-threaded output path on a PARTNER-FACING adapter --
                    FALLBACK-ORDER: an inverted `??` fallback chain that drops
                    a field from the adapter's OUTPUT expression.
                    Non-partner-facing: the same finding -> WARN, never BLOCK.
  Action      BLOCK -> exit 1, push refused. WARN / PASS -> exit 0.

Verdict-policy rationale (v1 calibration)
-----------------------------------------
comp-adapter-audit's own exit code is not a usable D-1 signal: every live
partner adapter carries ~65 SCHEMA-DRIFT WARNs (an S3 field the typed
interface does not declare = type-stale; the field is still present in the
envelope -- not "data silently absent"). Keying BLOCK on raw audit WARNs would
block every push touching a partner adapter on day 1.

The PRD D-1 defect class is precise: "a consumer-readable OUTPUT path of the
adapter that defaults with NO raw-envelope source -> partner data silently
absent". Of comp-adapter-audit's finding categories, exactly one is an
OUTPUT-construction defect in that direction:
  FALLBACK-ORDER  an inverted `??` fallback chain in the adapter's return
                  expression -- a narrower source first masks a field only the
                  broader source carries, dropping it from the output.
                  (Anchor: INFFIN #7 inverted-fallback 32df3b85.)
The other categories are NOT the D-1 defect direction and do not BLOCK:
  SCHEMA-DRIFT / NESTED-SCHEMA-DRIFT  an S3 field absent from the typed RAW
                  interface -- type-stale, the field is still in the envelope.
  TYPE-ONLY       a RAW-interface field absent from the live S3 envelope --
                  frequently legitimate-historical; graded INFO by the tool.
  NOT-THREADED    a raw S3 field the adapter body never references -- the
                  INVERSE direction (raw-unconsumed, not output-without-source);
                  a raw field the adapter legitimately does not need is not a
                  defect. (Confirmed against adapter_audit_cli.py with CTO~B.)
All four are surfaced as WARN per PRD section 3.2 "WARN-not-BLOCK until the
false-positive rate is empirically known". D-1's BLOCK precision is bounded by
the tool's signal precision -- comp-adapter-audit audits the RAW-input side and
the return-expression, not the adapter's full OUTPUT type; re-authoring it is
out of D-1 scope (ADHC_COMPIL_V4 territory). Documented limitation.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

# d1_adapter_threading_gate.py lives canonically at <ws>/.tools/portal-hooks/.
_THIS = Path(__file__).resolve()
_WORKSPACE = _THIS.parents[2]
_PORTAL = _WORKSPACE / 'portal'
_ENDPOINTS_DIR = _PORTAL / 'src' / 'api' / 'endpoints'
_AUDIT_CLI = _WORKSPACE / 'org' / 'modules' / 'graph' / 'adapter_audit_cli.py'
_AUDIT_MANIFEST_DIR = _WORKSPACE / 'org' / 'modules' / 'graph' / 'adapter-audit'

# Partner-facing classification (AC2 -- deterministic, by source file).
# An adapter defined in one of these endpoint files renders on a partner-facing
# surface (the AdvisorIntelligence partner portal). Anything else -> WARN-only.
_PARTNER_FACING_FILES = {
    'advisor-intelligence.ts',
}

# Status classes for the verdict policy. BLOCK-class is the precise D-1 defect
# direction only -- an inverted fallback chain that drops a field from the
# adapter's OUTPUT expression. See the verdict-policy rationale above.
_BLOCK_CLASS = {'FALLBACK-ORDER'}
_WARN_CLASS = {'SCHEMA-DRIFT', 'NESTED-SCHEMA-DRIFT', 'TYPE-ONLY', 'NOT-THREADED'}

# A static partner adapter, by function name: a getPlatinum* fetcher or a
# *Static* fetcher. These are the S3-envelope-backed adapters comp-adapter-audit
# can meaningfully audit.
_ADAPTER_NAME_RE = re.compile(r'^get\w*(?:Platinum\w*|\w*Static\w*)$')


def _zero_sha(sha: str) -> bool:
    return bool(re.fullmatch(r'0+', sha or ''))


def _git_portal(*args: str) -> tuple[int, str]:
    """Run git in the portal repo. Returns (returncode, stdout)."""
    try:
        r = subprocess.run(
            ['git', '-C', str(_PORTAL), *args],
            capture_output=True, text=True, timeout=30,
        )
        return r.returncode, r.stdout
    except Exception as exc:  # noqa: BLE001 -- a hook must never crash a push
        print(f'  WARN: git {" ".join(args)} failed: {exc}')
        return 1, ''


def _resolve_base(remote_sha: str) -> str:
    """Pick a base commit to diff against.

    Normal push: the remote ref's SHA. New branch (all-zero remote SHA):
    fall back to a remote tracking branch so the gate still bounds 'changed'.
    """
    if not _zero_sha(remote_sha):
        return remote_sha
    for ref in ('origin/PROD', 'origin/DEV', 'origin/main'):
        rc, _ = _git_portal('rev-parse', '--verify', '--quiet', ref)
        if rc == 0:
            return ref
    return ''


def _changed_endpoint_files(base: str, local_sha: str) -> list[str]:
    """Endpoint .ts files changed between base and local_sha (basenames)."""
    rc, out = _git_portal('diff', '--name-only', base, local_sha)
    if rc != 0:
        return []
    files = []
    for line in out.splitlines():
        line = line.strip()
        if line.startswith('src/api/endpoints/') and line.endswith('.ts'):
            files.append(line)
    return files


def _changed_line_ranges(base: str, local_sha: str, path: str) -> list[tuple[int, int]]:
    """New-side changed line ranges for `path`, via git diff -U0 hunk headers."""
    rc, out = _git_portal('diff', '-U0', base, local_sha, '--', path)
    if rc != 0:
        return []
    ranges: list[tuple[int, int]] = []
    for m in re.finditer(r'^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@', out, re.M):
        start = int(m.group(1))
        count = int(m.group(2)) if m.group(2) is not None else 1
        if count == 0:  # pure deletion -- no new lines
            continue
        ranges.append((start, start + count - 1))
    return ranges


def _adapter_spans(file_text: str) -> dict[str, tuple[int, int]]:
    """Map adapter-function name -> (start_line, end_line), 1-indexed.

    Targets static partner adapters: getPlatinum* / *Static* fetchers.
    Function end is found by brace counting (mirrors adapter_audit_cli).
    """
    spans: dict[str, tuple[int, int]] = {}
    lines = file_text.splitlines()
    fn_def = re.compile(r'(?:export\s+)?async\s+function\s+(\w+)\s*\(')
    for i, line in enumerate(lines):
        m = fn_def.search(line)
        if not m:
            continue
        name = m.group(1)
        if not _ADAPTER_NAME_RE.match(name):
            continue
        depth = 0
        started = False
        end = i
        for j in range(i, len(lines)):
            depth += lines[j].count('{') - lines[j].count('}')
            if '{' in lines[j]:
                started = True
            end = j
            if started and depth <= 0:
                break
        spans[name] = (i + 1, end + 1)
    return spans


def _overlaps(span: tuple[int, int], ranges: list[tuple[int, int]]) -> bool:
    s, e = span
    return any(not (e < rs or s > re_) for rs, re_ in ranges)


def _run_audit(adapter: str) -> tuple[int, str]:
    """Invoke comp-adapter-audit (via the CLI). Returns (returncode, stdout)."""
    try:
        r = subprocess.run(
            [sys.executable, str(_AUDIT_CLI), adapter],
            capture_output=True, text=True, timeout=90,
        )
        return r.returncode, r.stdout + r.stderr
    except Exception as exc:  # noqa: BLE001
        return 1, f'audit invocation failed: {exc}'


def _parse_manifest(adapter: str) -> list[str] | None:
    """Read the audit manifest for `adapter`; return the list of finding statuses.

    Returns None if the manifest is absent (audit did not complete).
    """
    manifest = _AUDIT_MANIFEST_DIR / f'{adapter}.yaml'
    if not manifest.exists():
        return None
    statuses: list[str] = []
    in_findings = False
    for raw in manifest.read_text(encoding='utf-8', errors='ignore').splitlines():
        if raw.rstrip() == 'findings:':
            in_findings = True
            continue
        if not in_findings:
            continue
        m = re.match(r'\s+status:\s*(\S+)', raw)
        if m:
            statuses.append(m.group(1))
    return statuses


def _verdict_for_adapter(statuses: list[str], partner_facing: bool) -> tuple[str, dict]:
    """Render the D-1 verdict for one adapter from its audit finding statuses.

    Returns (verdict, counts) where verdict is PASS / WARN / BLOCK.
    """
    counts: dict[str, int] = {}
    for s in statuses:
        counts[s] = counts.get(s, 0) + 1
    block_hits = sum(counts.get(s, 0) for s in _BLOCK_CLASS)
    warn_hits = sum(counts.get(s, 0) for s in _WARN_CLASS)
    if block_hits and partner_facing:
        return 'BLOCK', counts
    if block_hits or warn_hits:
        return 'WARN', counts
    return 'PASS', counts


def evaluate(adapters: list[tuple[str, bool]]) -> int:
    """Audit each (adapter, partner_facing) pair; print a report; return exit code."""
    if not adapters:
        print('  D-1: no static partner adapters changed -- PASS (no-op)')
        return 0

    print(f'  D-1: auditing {len(adapters)} changed adapter(s)...')
    overall_block = False
    for adapter, partner in sorted(adapters):
        rc, _out = _run_audit(adapter)
        statuses = _parse_manifest(adapter)
        tag = 'partner-facing' if partner else 'non-partner-facing'
        if statuses is None:
            print(f'  WARN  {adapter} ({tag}) -- audit produced no manifest; '
                  f'cannot render a verdict (audit rc={rc}). Treating as WARN.')
            continue
        verdict, counts = _verdict_for_adapter(statuses, partner)
        detail = ', '.join(f'{k}={v}' for k, v in sorted(counts.items())) or 'no findings'
        print(f'  {verdict:<5} {adapter} ({tag}) -- {detail}')
        if verdict == 'BLOCK':
            overall_block = True
            block_kinds = ', '.join(
                k for k in sorted(counts) if k in _BLOCK_CLASS
            )
            print(f'        un-threaded output path on a partner-facing adapter '
                  f'({block_kinds}) -- production data would be silently absent.')

    if overall_block:
        print('  D-1 VERDICT: BLOCK -- fix the un-threaded adapter path(s) above, '
              'or re-run comp-adapter-audit <fn> to inspect.')
        return 1
    print('  D-1 VERDICT: PASS/WARN -- no blocking adapter-threading defect.')
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(prog='d1-adapter-threading-gate')
    ap.add_argument('--local-sha', required=True)
    ap.add_argument('--remote-sha', required=True)
    ap.add_argument('--remote-ref', default='')
    # --adapters: explicit (adapter[:partner]) list -- used by the test harness
    # to drive the verdict path without a git diff.
    ap.add_argument('--adapters', default='')
    args = ap.parse_args()

    print('VALGATE D-1 -- adapter-threading gate (ADHC_VALGATE.004)')

    if args.adapters:
        pairs: list[tuple[str, bool]] = []
        for tok in args.adapters.split(','):
            tok = tok.strip()
            if not tok:
                continue
            if ':' in tok:
                name, flag = tok.split(':', 1)
                pairs.append((name, flag.strip().lower() in ('1', 'true', 'partner')))
            else:
                pairs.append((tok, True))
        return evaluate(pairs)

    if _zero_sha(args.local_sha):
        print('  D-1: branch deletion -- PASS (no-op)')
        return 0

    base = _resolve_base(args.remote_sha)
    if not base:
        print('  NOTE: D-1 could not resolve a diff base (new branch, no remote '
              'tracking ref) -- skipping. PASS.')
        return 0

    changed_files = _changed_endpoint_files(base, args.local_sha)
    if not changed_files:
        print('  D-1: no api/endpoints/*.ts files changed -- PASS (no-op)')
        return 0

    adapters: list[tuple[str, bool]] = []
    for rel in changed_files:
        basename = rel.rsplit('/', 1)[-1]
        partner = basename in _PARTNER_FACING_FILES
        ep_file = _ENDPOINTS_DIR / basename
        if not ep_file.exists():
            continue
        text = ep_file.read_text(encoding='utf-8', errors='ignore')
        spans = _adapter_spans(text)
        ranges = _changed_line_ranges(base, args.local_sha, rel)
        for name, span in spans.items():
            if _overlaps(span, ranges):
                adapters.append((name, partner))

    return evaluate(adapters)


if __name__ == '__main__':
    sys.exit(main())

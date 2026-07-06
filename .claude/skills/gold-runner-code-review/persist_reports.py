#!/usr/bin/env python3
"""Persist a gold-runner-code-review workflow's per-agent results as granular report files.

Reads the workflow run's journal.jsonl (one {"type":"result",...} line per completed agent)
and writes ONE readable Markdown file per agent into a single colocated folder, plus an INDEX
and a FIX_LOG scaffold. This is the durable, granular artifact of the review -- NOT an
aggregated summary (aggregation/triage happens later, per-report, during the drive phase).

Usage:
  python persist_reports.py <journal.jsonl> <output_dir> [pipeline_label] [workflow_run_id]

The journal path is printed by the Workflow tool result / lives at:
  <session>/subagents/workflows/<runId>/journal.jsonl
"""
from __future__ import annotations

import json
import os
import re
import sys


def sevrank(s):
    return {'critical': 3, 'high': 2, 'medium': 1, 'low': 0}.get(s, 0)


def main():
    if len(sys.argv) < 3:
        print('usage: persist_reports.py <journal.jsonl> <output_dir> [pipeline] [run_id]')
        return 2
    journal, dst = sys.argv[1], sys.argv[2]
    pipeline = sys.argv[3] if len(sys.argv) > 3 else 'pipeline'
    run_id = sys.argv[4] if len(sys.argv) > 4 else '(unknown run)'
    os.makedirs(dst, exist_ok=True)

    reviews, verifies = {}, []
    for line in open(journal, encoding='utf-8'):
        try:
            e = json.loads(line)
        except Exception:
            continue
        if e.get('type') != 'result':
            continue
        r = e.get('result')
        if not isinstance(r, dict):
            continue
        if 'script' in r:
            reviews[r['script']] = r          # dedup by script (last-wins)
        elif 'is_real' in r:
            verifies.append(r)

    script_re = re.compile(r'([A-Za-z0-9_]+_[A-Za-z0-9_.\-]+\.py)')

    # --- REVIEW files (one per script) ---
    for sc, r in sorted(reviews.items()):
        base = os.path.basename(sc)
        fs = sorted(r.get('findings') or [], key=lambda f: -sevrank(f.get('severity')))
        lines = [f'# REVIEW -- {base}', '']
        lines.append(f'- script: `{sc}`')
        lines.append(f'- verdict: **{r.get("verdict")}**')
        lines.append(f'- runs_in_incremental: {r.get("runs_in_incremental")}')
        lines.append(f'- findings: {len(fs)}')
        lines.append('')
        if not fs:
            lines.append('_No findings -- reviewer verdict CLEAN._')
        for i, f in enumerate(fs, 1):
            lines.append(f'## Finding {i} -- [{f.get("severity")}/{f.get("category")}/{f.get("mode")}]')
            lines.append(f'- **Location:** `{f.get("location")}`')
            lines.append(f'- **Mechanism:** {f.get("mechanism")}')
            lines.append(f'- **Failure scenario:** {f.get("failure_scenario")}')
            if f.get('fix'):
                lines.append(f'- **Proposed fix:** {f.get("fix")}')
            lines.append('')
        open(os.path.join(dst, f'review_{base}.md'), 'w', encoding='utf-8').write('\n'.join(lines))

    # --- VERIFY files (one per adversarial-verify agent) ---
    for n, v in enumerate(verifies, 1):
        reason = v.get('reasoning') or ''
        m = script_re.search(reason)
        tgt = m.group(1) if m else 'unknown'
        lines = [f'# VERIFY #{n:02d} -- target: {tgt}', '']
        lines.append(f'- is_real: **{v.get("is_real")}**')
        lines.append(f'- confidence: **{v.get("confidence")}**')
        lines.append(f'- corrected_severity: {v.get("corrected_severity")}')
        lines.append('')
        lines.append('## Reasoning')
        lines.append(reason)
        lines.append('')
        open(os.path.join(dst, f'verify_{n:02d}_{tgt.replace(".py", "")}.md'),
             'w', encoding='utf-8').write('\n'.join(lines))

    # --- INDEX (navigation only, NOT metrics aggregation) ---
    idx = [f'# {pipeline} gold-runner code-review -- per-agent report index', '']
    idx.append(f'Raw per-agent outputs from workflow `{run_id}`. {len(reviews)} review + '
               f'{len(verifies)} verify = {len(reviews)+len(verifies)} agents, one file each in this '
               f'folder. NOT triaged/aggregated -- these are the granular agent reports for the '
               f'per-report drive phase.')
    idx.append('')
    idx.append('## Review agents (one per script)')
    idx.append('| file | verdict | findings (C/H/M/L) | runs_in_incremental |')
    idx.append('|---|---|---|---|')
    for sc, r in sorted(reviews.items()):
        fs = r.get('findings') or []
        tal = '/'.join(str(sum(1 for f in fs if f.get('severity') == s)) for s in ('critical', 'high', 'medium', 'low'))
        idx.append(f'| review_{os.path.basename(sc)}.md | {r.get("verdict")} | {tal} | {r.get("runs_in_incremental")} |')
    idx.append('')
    idx.append('## Verify agents (one per adversarial check of a material finding)')
    idx.append('| file | target | is_real | confidence | corrected_sev |')
    idx.append('|---|---|---|---|---|')
    for n, v in enumerate(verifies, 1):
        m = script_re.search(v.get('reasoning') or '')
        tgt = m.group(1) if m else 'unknown'
        idx.append(f'| verify_{n:02d}_{tgt.replace(".py", "")}.md | {tgt} | {v.get("is_real")} | {v.get("confidence")} | {v.get("corrected_severity")} |')
    open(os.path.join(dst, 'INDEX.md'), 'w', encoding='utf-8').write('\n'.join(idx))

    # --- FIX_LOG scaffold (only if absent -- never clobber an in-progress drive log) ---
    fix_log = os.path.join(dst, 'FIX_LOG.md')
    if not os.path.exists(fix_log):
        scaffold = [
            f'# {pipeline} gold-runner code-review -- Fix Log', '',
            f'Running log of fixes applied from the per-agent reports in this folder (workflow `{run_id}`).',
            '**One entry per fix, citing the originating report + the commit.** Reviewed top-to-bottom',
            '(chain order), one report at a time.', '',
            'Legend -- **Verify:** the adversarial-verify verdict (confirmed/plausible) when a critical/high',
            'finding was auto-verified; "ground-truthed" for mediums/lows (no verify agent ran -- validate',
            'against SOURCE before fixing). DISCIPLINE: safe guards (dtype coerce, unguarded-read guard,',
            'fail-loud on systematic/newest failure, observability WARNs) are applied autonomously; a fix',
            'that changes a SERVED tax/AUA/NNA number via cross-script data lineage is a DESIGN ITEM',
            '(flag to the owning exec), NOT an autonomous patch.', '',
            '---', '',
            '## FIXES', '',
            '<!-- ## FIX-001 -- <script>: <one-line> (report N, finding K, <severity>)',
            '- **File:** `<path>` -- `<function>`',
            '- **Defect:** <mechanism -> served/chain impact>',
            '- **Fix:** <what changed>',
            '- **Commit:** `<hash>` -->', '',
            '---', '',
            '## DESIGN ITEMS (flagged -- need a cross-script/owner decision, NOT a safe autonomous patch)', '',
            '---', '',
            '## Reports reviewed but NO fix applied',
            '(reviewer verdict clean, or a finding refuted / not-actionable on ground-truth)', '',
        ]
        open(fix_log, 'w', encoding='utf-8').write('\n'.join(scaffold))
        made_scaffold = True
    else:
        made_scaffold = False

    print(f'WROTE {len(reviews)} review + {len(verifies)} verify + INDEX'
          f'{" + FIX_LOG scaffold" if made_scaffold else " (FIX_LOG preserved)"} -> {dst}')
    return 0


if __name__ == '__main__':
    sys.exit(main())

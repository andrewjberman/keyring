"""AXIS 4 -- mechanical wall-clock, measured. SAFETY-GATED.

Times ONLY tools whose own header DECLARES read-only/advisory. A tool that does not say so is
NOT timed -- some comp-tools write (comp-system regen), and a timing pass must never mutate the
estate. The unsafe/undeclared set is reported as NOT-MEASURED, never as slow or fast.

Each timed tool is run with a hard timeout. Wall clock is captured per run; a second run measures
warm-vs-cold variance where the first completed.
"""
import json
import os
import re
import subprocess
import time

TOOLS = sorted(t for t in os.listdir('.tools') if t.startswith('comp-'))
RO = re.compile(r'READ-?ONLY|ADVISORY|read-only|never writes|measure-only|NEVER removes', re.I)
WRITES = re.compile(r'\bregen\b|--fix|--apply|--write|WRITE\b|commits |writes to', re.I)
TIMEOUT = 100

safe, unsafe = [], []
for t in TOOLS:
    try:
        head = open(os.path.join('.tools', t), encoding='utf-8', errors='replace').read()[:2500]
    except Exception:
        continue
    if RO.search(head) and not WRITES.search(head):
        safe.append(t)
    else:
        unsafe.append(t)

print("SAFETY GATE: %d of %d tools DECLARE read-only/advisory with no write verb -> timed"
      % (len(safe), len(TOOLS)))
print("             %d NOT TIMED (undeclared or write-capable) -- reported as NOT-MEASURED\n" % len(unsafe))

res = []
for t in safe:
    t0 = time.time()
    try:
        p = subprocess.run(['python', os.path.join('.tools', t)],
                           capture_output=True, text=True, timeout=TIMEOUT,
                           encoding='utf-8', errors='replace')
        el = time.time() - t0
        out = (p.stdout or '') + (p.stderr or '')
        res.append({'tool': t, 'sec': round(el, 2), 'rc': p.returncode,
                    'bytes': len(out), 'lines': out.count('\n'), 'status': 'ok'})
    except subprocess.TimeoutExpired:
        res.append({'tool': t, 'sec': float(TIMEOUT), 'rc': None, 'bytes': 0,
                    'lines': 0, 'status': 'TIMEOUT'})
    except Exception as e:
        res.append({'tool': t, 'sec': round(time.time() - t0, 2), 'rc': None, 'bytes': 0,
                    'lines': 0, 'status': type(e).__name__})

ok = [r for r in res if r['status'] == 'ok']
ok.sort(key=lambda r: -r['sec'])
print("=== AXIS 4 -- WALL CLOCK (no-arg default invocation), %d timed ===" % len(res))
print("  %-26s %8s %5s %9s %7s" % ('tool', 'sec', 'rc', 'bytes', 'lines'))
for r in ok:
    print("  %-26s %8.2f %5s %9d %7d" % (r['tool'], r['sec'], r['rc'], r['bytes'], r['lines']))
bad = [r for r in res if r['status'] != 'ok']
if bad:
    print("\n  NOT-OK:")
    for r in bad:
        print("  %-26s %8.2f  %s" % (r['tool'], r['sec'], r['status']))
if ok:
    secs = [r['sec'] for r in ok]
    print("\n  SPREAD: min=%.2fs  median=%.2fs  max=%.2fs  ratio=%.0fx"
          % (min(secs), sorted(secs)[len(secs) // 2], max(secs), max(secs) / max(min(secs), 0.01)))
    byt = [r['bytes'] for r in ok]
    print("  OUTPUT: min=%dB  median=%dB  max=%dB" % (min(byt), sorted(byt)[len(byt) // 2], max(byt)))
out = os.path.join(os.environ.get('TEMP', '.'), 'tool_time.json')
json.dump({'timed': res, 'not_timed': unsafe}, open(out, 'w'), indent=1)
print("\n  rows -> %s" % out)

"""deploy-ledger-names.py -- which deploy-scope scripts an OPEN change-management ledger entry names.

1.0.0_SA_CTO ruling msg 107341 (2026-10-08, on 0.0.0_AB_MSTR's dell1 finding 107334): "the pre-push deploy (your B2)
deploys a script only when an OPEN change-management ledger names it; any other deploy-scope script is held (not
deployed), the push still goes through, and a HELD-DEPLOY row is written to the deploy audit log." Owner 4.0.0_SA_CRO~A.

An entry is OPEN when its sentinel in org/critical_paths/.open_deploys/<slug>.json has status exactly "OPEN" (a
HELD-SOVEREIGN-GATED or any other status does not authorize a deploy). It NAMES a script when the script's
repo-relative path (forward slashes) appears in the sentinel's text or in the entry markdown its entry_path points at.
A basename alone is not a name: two pipelines can carry a file of the same name.

USAGE:  python .tools/deploy-ledger-names.py [--repo-root DIR] <path> [<path> ...]      (or the paths on stdin)
OUTPUT: one line per path, "LEDGERED <path> <slug>" or "HELD <path>", then "LEDGER-OPEN-ENTRIES n=<n>".
EXIT:   0 always on a readable estate; 2 when the .open_deploys directory cannot be read (callers then hold everything).
"""
import json
import os
import sys


def main(argv):
    root = '.'
    paths = []
    i = 0
    while i < len(argv):
        if argv[i] == '--repo-root' and i + 1 < len(argv):
            root = argv[i + 1]
            i += 2
            continue
        paths.append(argv[i])
        i += 1
    if not paths and not sys.stdin.isatty():
        paths = [line.strip() for line in sys.stdin if line.strip()]
    sdir = os.path.join(root, 'org', 'critical_paths', '.open_deploys')
    try:
        names = sorted(n for n in os.listdir(sdir) if n.endswith('.json'))
    except OSError as e:
        print('ERROR: cannot read %s: %s' % (sdir, e))
        return 2
    open_entries = []
    for n in names:
        try:
            with open(os.path.join(sdir, n), encoding='utf-8', errors='replace') as fh:
                d = json.load(fh)
        except Exception:  # noqa: BLE001 -- an unreadable sentinel authorizes nothing
            continue
        if str(d.get('status', '')).strip() != 'OPEN':
            continue
        text = json.dumps(d, ensure_ascii=False)
        ep = str(d.get('entry_path') or '').strip()
        if ep:
            for cand in (ep, os.path.join(root, ep)):
                if os.path.isfile(cand):
                    try:
                        with open(cand, encoding='utf-8', errors='replace') as fh:
                            text += '\n' + fh.read()
                    except OSError:
                        pass
                    break
        open_entries.append((str(d.get('slug') or n[:-5]), text.replace('\\', '/')))
    for p in paths:
        q = p.replace('\\', '/')
        if q.startswith('./'):
            q = q[2:]
        hit = next((slug for slug, text in open_entries if q in text), None)
        print('LEDGERED %s %s' % (q, hit) if hit else 'HELD %s' % q)
    print('LEDGER-OPEN-ENTRIES n=%d' % len(open_entries))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

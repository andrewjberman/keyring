"""merge-resolve-known.py -- resolve the two KNOWN multi-writer conflict classes without a worktree.

Every merge conflict that held a shared tree on 2026-10-08 was one of two classes (4.0.0_SA_CRO~A, replay of the drains
73b6e98145, b3afc00597, 537ac6650f and of the site Z and laptop box-pass holds; design: brief outcome O6, "one writer
per file class"; 0.0.0_AB_MSTR msg 107365: "the integrator should regenerate generated index rows after each merge"):

  1. A SURPRISE-CHANNEL file (`.../surprise-channel/{investigations,remediations,adjudications}/<KIND>_v<N>.md`, or the
     legacy flat `org/surprise_channel/**/<KIND>_v<N>.md`): a preamble, then one `## <row id> -- <title>` section per
     row. Resolved by a THREE-WAY UNION BY SECTION: rows either side added are kept (base order, then ours, then
     theirs); a row only one side changed takes that change; a row changed DIFFERENTLY on both sides, or a duplicated
     id, is NOT resolved.
  2. A GENERATED index entry (`org/projects/<CODE>.json` whose both sides carry `home`): resolved by REGENERATING it
     from the merged tree with `.tools/missions-tree-index.py derive --write`, over a narrow extract of the merged
     tree (that project's home, the two registers, the contract): about 2 s, against 85 s for a full extract.

Anything else is UNRESOLVED and the caller falls back to its normal conflict path.

USAGE:  python .tools/merge-resolve-known.py --base B --ours P1 --theirs P2 --tree T <path> [<path> ...]
        (T = the tree `git merge-tree --write-tree P1 P2` wrote, conflict markers and all)
OUTPUT: per path, "RESOLVED <path> <blob> <how>" (the blob is written to the object store) or "UNRESOLVED <path> <why>".
EXIT:   0 when every path is RESOLVED; 1 otherwise; 2 on bad usage. Owner 4.0.0_SA_CRO~A.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

CHANNEL_RE = re.compile(r'(^|/)surprise-channel/(investigations|remediations|adjudications)/[A-Z]+_v\d+\.md$'
                        r'|^org/surprise_channel/(.+/)?[A-Z]+_v\d+\.md$')
GENERATED_RE = re.compile(r'^org/projects/[^/]+\.json$')
ROOT = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True).stdout.strip() or '.'


def git(*a, inp=None):
    r = subprocess.run(['git', *a], capture_output=True, cwd=ROOT, input=inp)
    return r.returncode, r.stdout


def show(rev, path):
    rc, out = git('cat-file', '-p', '%s:%s' % (rev, path))
    return out.decode('utf-8', errors='surrogateescape') if rc == 0 else None


def put_blob(text):
    rc, out = git('hash-object', '-w', '--stdin', inp=text.encode('utf-8', errors='surrogateescape'))
    return out.decode().strip() if rc == 0 else None


def sections(text):
    """(preamble, [(id, raw section text)]) or None when an id repeats."""
    lines = text.splitlines(keepends=True)
    pre, secs, cur_id, cur = [], [], None, []
    for ln in lines:
        if ln.startswith('## '):
            if cur_id is not None:
                secs.append((cur_id, ''.join(cur)))
            head = ln[3:].strip()
            cur_id = head.split(' -- ', 1)[0].strip()
            cur = [ln]
        elif cur_id is None:
            pre.append(ln)
        else:
            cur.append(ln)
    if cur_id is not None:
        secs.append((cur_id, ''.join(cur)))
    ids = [i for i, _ in secs]
    if len(ids) != len(set(ids)):
        return None
    return ''.join(pre), secs


def three(b, o, t):
    """Three-way pick; returns (ok, value)."""
    if o == t:
        return True, o
    if o == b:
        return True, t
    if t == b:
        return True, o
    return False, None


def union_channel(base, ours, theirs):
    parts = [sections(x or '') for x in (base, ours, theirs)]
    if any(p is None for p in parts):
        return None, 'a row id appears twice in one version'
    (bp, bs), (op, os_), (tp, ts) = parts
    # Trailing blank lines are the SEPARATOR between rows, not row content: the last row of a file gains one when a side
    # appends after it (LGIC_BLANKFIX b55c75111d, 2026-10-08 22:52Z -- both sides "changed" row W4-S5 by a blank line).
    # Compare and emit every part with its trailing newlines stripped, and join with exactly one blank line.
    # Compare on the text with trailing whitespace stripped; EMIT each part's original bytes (base's when unchanged),
    # adding a blank line only where a part does not already end with one, so a clean union stays byte-identical.
    norm = lambda s: None if s is None else s.rstrip('\r\n')  # noqa: E731

    def pick(b, o, t):
        ok, v = three(norm(b), norm(o), norm(t))
        if not ok or v is None:
            return ok, None
        for raw in (b, o, t):
            if raw is not None and norm(raw) == v:
                return True, raw
        return True, v

    ok, pre = pick(bp, op, tp)
    if not ok:
        return None, 'the preamble changed differently on both sides'
    bd, od, td = dict(bs), dict(os_), dict(ts)
    order = [i for i, _ in bs] + [i for i, _ in os_ if i not in bd] + [i for i, _ in ts if i not in bd and i not in od]
    out = [pre] if pre else []
    for i in order:
        ok, v = pick(bd.get(i), od.get(i), td.get(i))
        if not ok:
            return None, 'row %s changed differently on both sides' % i
        if v is None:
            continue
        if out and not re.search(r'\n[ \t\r]*\n$', out[-1]):
            eol = '\r\n' if out[-1].endswith('\r\n') else '\n'
            out[-1] = out[-1] + (eol if out[-1].endswith('\n') else eol + eol)
        out.append(v)
    text = ''.join(out)
    return (text if text.endswith('\n') else text + '\n'), 'section-union'


def regenerate(path, tree, ours, theirs):
    try:
        o, t = json.loads(show(ours, path) or 'null'), json.loads(show(theirs, path) or 'null')
    except ValueError:
        return None, 'a side is not JSON'
    if not (isinstance(o, dict) and isinstance(t, dict) and o.get('home') and t.get('home')):
        return None, 'not a generated entry on both sides (no home)'
    if o['home'] != t['home']:
        return None, 'the two sides name different homes'
    home = t['home']
    d = tempfile.mkdtemp(prefix='mrk-')
    try:
        want = [home, 'org/missions/DIRECTIVES.yaml', 'org/missions/MACROS.yaml', 'org/standards/PROJECT_TREE.contract.json']
        arch = subprocess.run(['git', 'archive', tree, *want], capture_output=True, cwd=ROOT)
        if arch.returncode != 0:
            return None, 'git archive of the merged tree failed'
        tar = subprocess.run(['tar', '-x', '-C', d], input=arch.stdout, capture_output=True)
        if tar.returncode != 0:
            return None, 'tar extract failed'
        os.makedirs(os.path.join(d, 'org', 'projects'), exist_ok=True)
        with open(os.path.join(d, path), 'w', encoding='utf-8', newline='') as fh:
            fh.write(show(theirs, path))        # a marker-free starting file; derive rewrites the generated entry
        tool = os.path.join(ROOT, '.tools', 'missions-tree-index.py')
        r = subprocess.run([sys.executable, tool, 'derive', '--write',
                            '--contract', os.path.join(d, 'org/standards/PROJECT_TREE.contract.json'),
                            '--root', os.path.join(d, 'org/missions'), '--projects', os.path.join(d, 'org/projects'),
                            '--directives', os.path.join(d, 'org/missions/DIRECTIVES.yaml'),
                            '--macros', os.path.join(d, 'org/missions/MACROS.yaml')], capture_output=True, text=True)
        if r.returncode not in (0, 1):
            return None, 'missions-tree-index derive failed rc=%d' % r.returncode
        with open(os.path.join(d, path), encoding='utf-8', newline='') as fh:
            text = fh.read()
        json.loads(text)
        return text, 'regenerated'
    except (OSError, ValueError) as e:
        return None, 'regeneration error: %s' % e
    finally:
        shutil.rmtree(d, ignore_errors=True)


def main(argv):
    opts, paths, i = {}, [], 0
    while i < len(argv):
        if argv[i] in ('--base', '--ours', '--theirs', '--tree') and i + 1 < len(argv):
            opts[argv[i][2:]] = argv[i + 1]
            i += 2
        else:
            paths.append(argv[i])
            i += 1
    if not all(k in opts for k in ('base', 'ours', 'theirs', 'tree')) or not paths:
        print(__doc__)
        return 2
    allok = True
    for p in paths:
        if CHANNEL_RE.search(p):
            text, how = union_channel(show(opts['base'], p), show(opts['ours'], p), show(opts['theirs'], p))
        elif GENERATED_RE.match(p):
            text, how = regenerate(p, opts['tree'], opts['ours'], opts['theirs'])
        else:
            text, how = None, 'not a known multi-writer class'
        blob = put_blob(text) if text is not None else None
        if blob:
            print('RESOLVED %s %s %s' % (p, blob, how))
        else:
            allok = False
            print('UNRESOLVED %s %s' % (p, how))
    return 0 if allok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

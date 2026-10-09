#!/usr/bin/env python
"""box-sync-conflicts.py -- census of the merge conflicts the integrator met, per shared file and per box (NFRA_CTLPLN FWD-8).

    python .tools/box-sync-conflicts.py [--since <UTC>] [--fetch] [--cloud <ref>]
    python .tools/box-sync-conflicts.py --selftest

READ-ONLY. It reads git refs and objects only; it writes nothing in the repository and sends nothing. --fetch runs one
`git fetch origin` first (a read of the remote, no merge).

WHAT IS COUNTED. The integrator's merges into the CLOUD trunk: a merge commit whose author is an MSTR serial
(0.0.0_AB_MSTR, optionally ~suffix) and whose subject has the form box-sync.sh writes in its integrate pass:
    integrate(<MSTR serial>): <branch> @<tip10> into CLOUD (box-sync)
(the "take CLOUD into <box>" merges land on a box branch, not on CLOUD, and are not counted).

THE RECORD. box-sync.sh and merge-resolve-known.py leave NO per-path record of a resolved conflict: the merge commit
message carries only the subject above, merge-resolve-known.py prints its RESOLVED/UNRESOLVED lines to the caller's
stderr, and the BOX-SYNC audit row names only merged=(...) held=(...) per run. So the conflict is RE-DERIVED: the two
parents are re-merged in the object store with `git merge-tree --write-tree --name-only --no-messages` and the
conflicted paths are the lines after the tree id. The resolution class is read off the landed merge commit: a conflicted
path whose landed blob still carries conflict markers (or is missing from a merge that kept it conflicted) is UNRESOLVED;
otherwise the class is the one merge-resolve-known.py applies to that path shape -- CHANNEL-UNION (a surprise-channel
file), GENERATED-REGEN (an org/projects/<CODE>.json index entry) -- or RESOLVED-OTHER (resolved, but not by a class that
tool owns). A merge-tree re-run reflects the git installed now, so rename handling can differ from the day of the merge.

PER PATH. boxes = the boxes whose work changed the path since the merge base: the second parent's box (named in the
subject) if it changed the path, plus every box whose earlier integrate merge brought a change to the path into CLOUD
since the base; a CLOUD-side change no integrate merge accounts for is "CLOUD". last_authors = the last commit author
touching the path on each side (ours = CLOUD side, theirs = the box side).

BLIND: a conflict a seat resolved by hand before the integrator ran never reaches an integrate merge.
LAST line: BOX-SYNC-CONFLICTS merges=<n> conflicted_merges=<c> paths=<p> top=<path:count,...>
"""
import argparse
import collections
import datetime
import importlib.util
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
AUTHOR_RE = re.compile(r'^0\.0\.0_AB_MSTR(~[A-Za-z0-9]+)?$')
SUBJECT_RE = re.compile(r'^integrate\((0\.0\.0_AB_MSTR(?:~[A-Za-z0-9]+)?)\): (\S+) @([0-9a-f]+) into CLOUD \(box-sync\)$')
MARKER_RE = re.compile(rb'^<<<<<<< ', re.M)
TOP_N = 10


def git(repo, *args, check=False):
    r = subprocess.run(['git', *args], cwd=repo, capture_output=True)
    if check and r.returncode != 0:
        raise RuntimeError('git %s failed rc=%d: %s' % (' '.join(args), r.returncode, r.stderr.decode('utf-8', 'replace')))
    return r.returncode, r.stdout


def gtext(repo, *args):
    return git(repo, *args)[1].decode('utf-8', 'replace').strip()


def load_classes():
    """The path-shape regexes merge-resolve-known.py resolves on; None when the module cannot be loaded."""
    try:
        spec = importlib.util.spec_from_file_location('merge_resolve_known', os.path.join(HERE, 'merge-resolve-known.py'))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.CHANNEL_RE, mod.GENERATED_RE
    except Exception:  # noqa: BLE001 -- a missing sibling tool degrades the class to RESOLVED-OTHER, never a crash
        return None, None


def parse_since(text):
    t = text.strip().replace('Z', '+00:00')
    d = datetime.datetime.fromisoformat(t)
    if d.tzinfo is None:
        d = d.replace(tzinfo=datetime.timezone.utc)
    return d.timestamp()


def integrate_merges(repo, cloud, since_ts):
    """[(sha, p1, p2, branch, tip, ts)] oldest first; the integrator's merges into the trunk in the window."""
    rc, out = git(repo, 'log', '--merges', '--format=%H%x1f%an%x1f%ct%x1f%P%x1f%s', cloud)
    if rc != 0:
        raise RuntimeError('git log %s failed rc=%d' % (cloud, rc))
    rows = []
    for line in out.decode('utf-8', 'replace').splitlines():
        f = line.split('\x1f')
        if len(f) != 5:
            continue
        sha, an, ct, parents, subj = f
        ps = parents.split()
        m = SUBJECT_RE.match(subj)
        if not m or not AUTHOR_RE.match(an) or len(ps) != 2:
            continue
        ts = int(ct)
        if since_ts is not None and ts < since_ts:
            continue
        rows.append((sha, ps[0], ps[1], m.group(2), m.group(3), ts))
    rows.reverse()
    return rows


def conflicted_paths(repo, p1, p2):
    rc, out = git(repo, 'merge-tree', '--write-tree', '--name-only', '--no-messages', p1, p2)
    if rc == 0:
        return []
    if rc != 1:
        raise RuntimeError('git merge-tree %s %s failed rc=%d' % (p1[:10], p2[:10], rc))
    lines = out.decode('utf-8', 'replace').splitlines()
    return sorted({ln for ln in lines[1:] if ln.strip()})


def resolution_class(repo, merge, path, classes):
    rc, blob = git(repo, 'cat-file', '-p', '%s:%s' % (merge, path))
    if rc != 0:
        return 'RESOLVED-OTHER'  # the landed merge deleted it: a resolution, not a marker file
    if MARKER_RE.search(blob):
        return 'UNRESOLVED'
    chan, gen = classes
    if chan is not None and chan.search(path):
        return 'CHANNEL-UNION'
    if gen is not None and gen.search(path):
        return 'GENERATED-REGEN'
    return 'RESOLVED-OTHER'


def short_box(branch):
    return branch.split('/', 1)[1] if '/' in branch else branch


def side_last_author(repo, base, tip, path):
    return gtext(repo, 'log', '-1', '--format=%an', '%s..%s' % (base, tip), '--', path) or '-'


def boxes_for_ours(repo, base, p1, path, cloud_merges):
    """Boxes whose integrate merge, between the base and P1, brought a change to the path into CLOUD."""
    boxes = []
    seen = set(c[0] for c in cloud_merges)
    rc, out = git(repo, 'log', '--merges', '--format=%H%x1f%P%x1f%s', '%s..%s' % (base, p1))
    for line in out.decode('utf-8', 'replace').splitlines() if rc == 0 else []:
        f = line.split('\x1f')
        if len(f) != 3:
            continue
        sha, parents, subj = f
        ps = parents.split()
        m = SUBJECT_RE.match(subj)
        if not m or len(ps) != 2 or sha not in seen:
            continue
        if gtext(repo, 'log', '-1', '--format=%h', '%s..%s' % (ps[0], ps[1]), '--', path):
            b = short_box(m.group(2))
            if b not in boxes:
                boxes.append(b)
    if not boxes and gtext(repo, 'log', '-1', '--format=%h', '%s..%s' % (base, p1), '--', path):
        boxes.append('CLOUD')
    return boxes


def census(repo, cloud, since_ts):
    classes = load_classes()
    merges = integrate_merges(repo, cloud, since_ts)
    cloud_set = merges
    out = []
    for sha, p1, p2, branch, tip, ts in merges:
        paths = conflicted_paths(repo, p1, p2)
        rec = {'merge': sha, 'branch': branch, 'tip': tip, 'ts': ts, 'paths': []}
        if paths:
            base = gtext(repo, 'merge-base', p1, p2)
            for path in paths:
                theirs_box = short_box(branch) if gtext(repo, 'log', '-1', '--format=%h', '%s..%s' % (base, p2), '--', path) else '-'
                ours_boxes = boxes_for_ours(repo, base, p1, path, cloud_set) if base else []
                boxes = sorted(set(ours_boxes + ([theirs_box] if theirs_box != '-' else [])))
                rec['paths'].append({
                    'path': path,
                    'boxes': boxes,
                    'ours_last': side_last_author(repo, base, p1, path),
                    'theirs_last': side_last_author(repo, base, p2, path),
                    'class': resolution_class(repo, sha, path, classes),
                })
        out.append(rec)
    return out


def summarize(recs):
    conflicted = [r for r in recs if r['paths']]
    counter = collections.Counter(p['path'] for r in conflicted for p in r['paths'])
    top = ','.join('%s:%d' % (p, n) for p, n in sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))[:TOP_N]) or 'none'
    return 'BOX-SYNC-CONFLICTS merges=%d conflicted_merges=%d paths=%d top=%s' % (len(recs), len(conflicted), len(counter), top)


def report(recs):
    for r in recs:
        if not r['paths']:
            continue
        print('MERGE %s %s @%s %s' % (r['merge'][:10], r['branch'], r['tip'][:10],
                                      datetime.datetime.fromtimestamp(r['ts'], datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ')))
        for p in r['paths']:
            print('  PATH %s boxes=%s ours_last=%s theirs_last=%s class=%s' % (
                p['path'], '+'.join(p['boxes']) or '-', p['ours_last'], p['theirs_last'], p['class']))
    print(summarize(recs))


# ----------------------------------------------------------------------------------------------------- selftest
def _env(name):
    e = dict(os.environ)
    e.update({'GIT_AUTHOR_NAME': name, 'GIT_AUTHOR_EMAIL': name + '@opal.agent', 'GIT_COMMITTER_NAME': name,
              'GIT_COMMITTER_EMAIL': name + '@opal.agent', 'GIT_CONFIG_GLOBAL': os.devnull, 'GIT_CONFIG_SYSTEM': os.devnull})
    return e


class Fx:
    def __init__(self, d):
        self.d = d

    def g(self, *a, name='seat', inp=None, ok=(0,)):
        r = subprocess.run(['git', *a], cwd=self.d, capture_output=True, env=_env(name), input=inp)
        if r.returncode not in ok:
            raise RuntimeError('selftest git %s rc=%d %s' % (' '.join(a), r.returncode, r.stderr.decode('utf-8', 'replace')))
        return r.stdout.decode('utf-8', 'replace').strip()

    def write(self, rel, text):
        p = os.path.join(self.d, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(text)

    def commit(self, branch, files, name):
        if self.g('symbolic-ref', '--short', 'HEAD') != branch:
            self.g('checkout', '-q', branch)
        for rel, text in files.items():
            self.write(rel, text)
            self.g('add', rel)
        self.g('commit', '-q', '-m', 'edit %s' % ','.join(files), name=name)
        return self.g('rev-parse', 'HEAD')

    def integrate(self, cloud_sha, box_branch, tree, ref_cloud):
        tip = self.g('rev-parse', box_branch)
        subj = 'integrate(0.0.0_AB_MSTR): %s @%s into CLOUD (box-sync)' % (box_branch, tip[:10])
        m = self.g('commit-tree', tree, '-p', cloud_sha, '-p', tip, '-m', subj, name='0.0.0_AB_MSTR')
        self.g('update-ref', ref_cloud, m)
        return m


def selftest():
    chan = 'org/missions/D0/X/Y/surprise-channel/investigations/INVESTIGATION_v1.md'
    cases = []
    with tempfile.TemporaryDirectory() as d:
        fx = Fx(d)
        fx.g('init', '-q', '-b', 'CLOUD')
        base = fx.commit('CLOUD', {'shared.txt': 'base\n', 'box-a.txt': 'a0\n', 'box-b.txt': 'b0\n', chan: 'pre\n'}, 'seat')
        fx.g('branch', 'box/a', base)
        fx.g('branch', 'box/b', base)
        fx.commit('box/a', {'shared.txt': 'from-a\n', 'box-a.txt': 'a1\n', chan: 'pre\nrow-a\n'}, 'author-a')
        fx.commit('box/b', {'shared.txt': 'from-b\n', 'box-b.txt': 'b1\n', chan: 'pre\nrow-b\n'}, 'author-b')
        ref = 'refs/remotes/origin/CLOUD'
        fx.g('update-ref', ref, base)
        # merge 1: CLOUD + box/a -- clean
        out1 = fx.g('merge-tree', '--write-tree', '--no-messages', base, 'box/a')
        m1 = fx.integrate(base, 'box/a', out1.splitlines()[0], ref)
        # merge 2: CLOUD(+a) + box/b -- shared.txt and the channel file conflict; landed resolved by hand
        out2 = fx.g('merge-tree', '--write-tree', '--no-messages', m1, 'box/b', ok=(1,))
        t0 = out2.splitlines()[0]
        idx = os.path.join(d, '.git', 'selftest.index')
        e = _env('seat')
        e['GIT_INDEX_FILE'] = idx
        subprocess.run(['git', 'read-tree', t0], cwd=d, env=e, check=True)
        for rel, text in (('shared.txt', 'resolved\n'), (chan, 'pre\nrow-a\nrow-b\n')):
            blob = fx.g('hash-object', '-w', '--stdin', inp=text.encode('utf-8'))
            subprocess.run(['git', 'update-index', '--cacheinfo', '100644,%s,%s' % (blob, rel)], cwd=d, env=e, check=True)
        t_res = subprocess.run(['git', 'write-tree'], cwd=d, env=e, capture_output=True, check=True).stdout.decode().strip()
        fx.integrate(m1, 'box/b', t_res, ref)
        recs = census(d, ref, None)
        by = {r['merge']: r for r in recs}
        clean = by.get(m1)
        confl = [r for r in recs if r['paths']]
        pmap = {p['path']: p for r in confl for p in r['paths']}
        sh = pmap.get('shared.txt', {})
        cases.append(('shared file listed', 'shared.txt' in pmap))
        cases.append(('shared file lists both boxes', sh.get('boxes') == ['a', 'b']))
        cases.append(('per-box files not listed', 'box-a.txt' not in pmap and 'box-b.txt' not in pmap))
        cases.append(('clean merge lists nothing', clean is not None and clean['paths'] == [] and len(recs) == 2))
        cases.append(('channel path classed CHANNEL-UNION, shared RESOLVED-OTHER',
                      pmap.get(chan, {}).get('class') == 'CHANNEL-UNION' and sh.get('class') == 'RESOLVED-OTHER'))
        cases.append(('last authors named per side', sh.get('ours_last') == 'author-a' and sh.get('theirs_last') == 'author-b'))
        cases.append(('summary line', summarize(recs).startswith('BOX-SYNC-CONFLICTS merges=2 conflicted_merges=1 paths=2 top=')))
    ok = sum(1 for _, v in cases if v)
    for name, v in cases:
        print('%s %s' % ('PASS' if v else 'FAIL', name))
    print('BOX-SYNC-CONFLICTS-SELFTEST cases=%d/%d ok=%s' % (ok, len(cases), ok == len(cases)))
    return 0 if ok == len(cases) else 1


def main(argv):
    ap = argparse.ArgumentParser(description='Census of integrator merge conflicts per shared file and per box.')
    ap.add_argument('--since', help='UTC lower bound on the merge commit date (ISO 8601); default: all history')
    ap.add_argument('--fetch', action='store_true', help='run one `git fetch origin` first')
    ap.add_argument('--cloud', default='origin/CLOUD', help='the trunk ref (default origin/CLOUD)')
    ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    repo = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True).stdout.strip() or '.'
    if a.fetch:
        rc, _ = git(repo, 'fetch', 'origin')
        if rc != 0:
            print('WARN: git fetch origin failed rc=%d; reading the refs as they are' % rc, file=sys.stderr)
    since_ts = parse_since(a.since) if a.since else None
    report(census(repo, a.cloud, since_ts))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

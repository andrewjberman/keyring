#!/usr/bin/env python3
"""DSGN_RBNDV2 round 7 -- the check file for the LOCAL candidate rehearsal (criterion RB7Z1-AC1).

Usage: python check_rehearsal.py <portal worktree path> [<deliverables folder holding REHEARSAL_RECORD.md>]
Prints one line per arm and `VERDICT: REHEARSAL-OK` only when every arm holds. Read-only: it runs git reads and one
`git ls-remote`; it pushes nothing and writes nothing.
"""
import os
import subprocess
import sys

CAND = 'cand/laptop/dsgn-rbndv2-light'
FEATURE = 'feature/dsgn-rbndv2-light'
FORK = 'ad7c100b'  # the DEV tip the feature branch was cut from (round 1 base)


def git(cwd, *args):
    r = subprocess.run(['git', *args], cwd=cwd, capture_output=True, text=True)
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def main():
    if len(sys.argv) < 2:
        print('usage: check_rehearsal.py <portal path> [<record folder>]')
        return 2
    portal = sys.argv[1]
    rec_dir = sys.argv[2] if len(sys.argv) > 2 else None
    arms = {}

    rc, prod, err = git(portal, 'rev-parse', 'origin/PROD')
    arms['prod_ref_resolves'] = rc == 0 and len(prod) >= 7
    rc, cand_tip, err = git(portal, 'rev-parse', '--verify', 'refs/heads/' + CAND)
    arms['candidate_branch_exists'] = rc == 0
    if arms['candidate_branch_exists'] and arms['prod_ref_resolves']:
        rc, _, _ = git(portal, 'merge-base', '--is-ancestor', prod, cand_tip)
        arms['candidate_descends_from_last_prod'] = rc == 0
        rc, mb, _ = git(portal, 'merge-base', cand_tip, prod)
        arms['merge_base_is_prod_tip'] = rc == 0 and mb == prod
        rc, n, _ = git(portal, 'rev-list', '--count', prod + '..' + cand_tip)
        arms['candidate_has_commits_over_prod'] = rc == 0 and n.isdigit() and int(n) > 0
        rc, files, _ = git(portal, 'diff', '--name-only', FORK, FEATURE)
        feats = [f for f in files.split('\n') if f]
        same = 0
        differ = []
        for f in feats:
            rc1, a, _ = git(portal, 'rev-parse', FEATURE + ':' + f)
            rc2, b, _ = git(portal, 'rev-parse', cand_tip + ':' + f)
            if (rc1 != 0 and rc2 != 0) or (rc1 == 0 and rc2 == 0 and a == b):
                same += 1
            else:
                differ.append(f)
        arms['feature_files_equal_in_candidate'] = len(feats) > 0 and not differ
        print('FEATURE-FILES %d EQUAL %d DIFFER %d %s' % (len(feats), same, len(differ), differ[:5]))
        print('CANDIDATE-COMMITS-OVER-PROD %s' % (n if rc == 0 else '?'))
    rc, out, err = git(portal, 'ls-remote', '--heads', 'origin', CAND)
    arms['remote_has_no_candidate_branch'] = rc == 0 and out == ''
    rc, out, _ = git(portal, 'for-each-ref', 'refs/remotes/origin/' + CAND)
    arms['no_remote_tracking_ref'] = out == ''
    if rec_dir:
        rec = os.path.join(rec_dir, 'REHEARSAL_RECORD.md')
        text = open(rec, encoding='utf-8').read() if os.path.isfile(rec) else ''
        arms['record_has_prod_tip'] = 'PROD-TIP' in text
        arms['record_has_conflicts_line'] = 'CONFLICTS' in text
        arms['record_has_commit_count'] = 'COMMITS-REPLAYED' in text
        arms['record_has_pushed_line'] = 'PUSHED NOTHING' in text
    for k, v in arms.items():
        print('%s %s' % ('PASS' if v else 'FAIL', k))
    ok = all(arms.values()) and len(arms) >= 8
    print('VERDICT: REHEARSAL-OK' if ok else 'VERDICT: REHEARSAL-FAIL')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())

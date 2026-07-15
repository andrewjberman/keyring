#!/usr/bin/env python3
"""POST-DEPLOY IMPORT LINT -- deployed means DOWNLOADED AND IMPORTED.

CTO ruling 2026-07-13: *"A PRESENT FILE IS NOT A LOADABLE ONE, AND A GREEN SUITE IS NEITHER.
A deploy verification that has not exercised the import has verified a FILENAME."*

WHY THIS EXISTS -- a real, live, undetected fault, found by accident
--------------------------------------------------------------------
On 2026-07-13 `lib/nna_coverage_guard.py` was deployed to s3://opal-data-inf/code/gold/lib/ while its
dependency `lib/inflection_rep_scope.py` on the runner was a STALE HALF-FILE (359 lines vs 790) that
did not define the symbol the guard imports. Every verification we own said GREEN:

    head-object              -> present
    s3 ls                    -> present, right size
    sha/ETag                 -> matches the uploaded artifact
    the deploy log           -> "DEPLOYED ... verified"
    comp-pipescript deployed -> MATCH  (it answers "is the object there and does its hash match?"
                                        and CANNOT answer "would this import?")
    the unit suite           -> 28/28 green  (because a unit suite imports the REPO. THE RUNNER
                                              IMPORTS THE BUCKET, AND WE HAVE NEVER MEASURED THAT.)
    ACTUAL IMPORT FROM THE BUCKET -> *** ImportError ***

The guard was not merely "in the bucket and uncalled." IT COULD NOT HAVE WORKED IF IT HAD BEEN
CALLED, and it would have taken the whole INF nightly down with it on the first chain that imported
it. A partial deploy of a package is a BROKEN deploy, and NO PRESENCE CHECK CAN SEE IT.

WHAT IT DOES
------------
Downloads the DEPLOYED objects (not the repo!) into a clean directory and imports each one in a
FRESH interpreter with ONLY that directory on sys.path. Any ImportError/SyntaxError/NameError at
module scope FAILS the lint.

  * FROM THE BUCKET, NOT THE REPO. Importing the repo proves nothing about the runner -- that is the
    entire defect this exists to catch.
  * A FRESH INTERPRETER PER MODULE (subprocess). In one process, module A's successful import would
    populate sys.modules and mask module B's broken one.
  * ISOLATED sys.path. If the ambient environment can satisfy an import that the bucket cannot, the
    lint passes for a reason the runner will not enjoy. A CONTROL THAT CANNOT FAIL IS NOT A CONTROL.
  * DENOMINATOR PRINTED. "0 modules checked, 0 failed" is a PASS that measured nothing -- the exact
    shape of the "Ran 0 tests" green that fooled me the same day. Zero checked is an ERROR, not a pass.

USAGE
  python .tools/deploy-import-lint.py --bucket opal-data-inf --prefix code/gold/lib/
  python .tools/deploy-import-lint.py --bucket opal-data-inf --prefix code/gold/lib/ --expect-fail
        (--expect-fail is the SELF-TEST: assert the lint CAN go red. Use it against a bucket you
         know is broken. A lint never observed to fail has not been shown to be able to.)

Exit 0 = every deployed module imports. Exit 1 = at least one cannot load. Exit 2 = lint could not run.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile

import boto3


def download_prefix(s3, bucket: str, prefix: str, dest: str) -> list[str]:
    """Pull every .py under `prefix` into a FLAT dest dir -- the same shape the chain's
    sync_scripts() produces on the runner. Returns the module names."""
    mods: list[str] = []
    for page in s3.get_paginator('list_objects_v2').paginate(Bucket=bucket, Prefix=prefix):
        for obj in page.get('Contents', []):
            key = obj['Key']
            name = key.rsplit('/', 1)[-1]
            if not name.endswith('.py') or name.startswith('__'):
                continue
            # tests/ live under the prefix too; they are not runtime modules.
            if '/tests/' in key:
                continue
            body = s3.get_object(Bucket=bucket, Key=key)['Body'].read()
            with open(os.path.join(dest, name), 'wb') as fh:
                fh.write(body)
            mods.append(name[:-3])
    return sorted(mods)


def import_in_fresh_interpreter(mod: str, path: str) -> tuple[bool, str]:
    """Import ONE module in a NEW interpreter with ONLY `path` on sys.path.

    A fresh process per module is load-bearing: in a shared process, an earlier successful import
    populates sys.modules and a later broken module can resolve its dependency from memory rather
    than from the bucket -- which is precisely the fault we are hunting.

    GLDRNS.B1 fix (2026-07-15, found by 0.4.0_DS~B on the serve-held bundle deploy): the original
    body was `importlib.import_module("<basename-minus-.py>")`. The estate's gold scripts carry
    DOTS in their basenames (INF_A_00.accounts_dimension.py), and import_module parses a dot as
    package.submodule -- so EVERY dotted script FAILED BY CONSTRUCTION, healthy or not, while only
    libs and undotted names were truly tested. A FAIL census that fails everything is a silence,
    not a reading. The honest form is a FILE-based spec load (dots in the filename are irrelevant),
    with the flat dir still on sys.path so intra-prefix dependencies resolve exactly as they do on
    the runner (sync_scripts() flattens to one dir). The runner itself executes these as FILES
    (bash -> python <file>), never as dotted module imports -- so the spec load is also the more
    faithful model of production. Self-test: --self-test (three arms, incl. a dotted healthy name).
    """
    fname = mod + '.py'
    code = (
        'import sys; sys.path.insert(0, r"%s")\n'
        'import importlib.util, os\n'
        'f = os.path.join(r"%s", r"%s")\n'
        'safe = "lint_" + r"%s".replace(".", "_").replace("-", "_")\n'
        'spec = importlib.util.spec_from_file_location(safe, f)\n'
        'm = importlib.util.module_from_spec(spec)\n'
        'spec.loader.exec_module(m)\n'
    ) % (path, path, fname, mod)
    proc = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True, timeout=120)
    if proc.returncode == 0:
        return True, ''
    err = (proc.stderr or '').strip().splitlines()
    return False, err[-1] if err else f'exit {proc.returncode}'


def run_self_test() -> int:
    """Three arms, each of which can fail, none of which touches S3:
      1. a DOTTED healthy script imports OK      (the arm the old body failed BY CONSTRUCTION)
      2. an undotted healthy lib imports OK      (the arm the old body could already do)
      3. a deliberately-broken module FAILS      (the lint can still go red -- a lint never
                                                  observed failing has not been shown able to)
    """
    tmp = tempfile.mkdtemp(prefix='deploy-import-lint-selftest-')
    try:
        with open(os.path.join(tmp, 'INF_X_99.dotted_healthy.py'), 'w') as fh:
            fh.write('from lint_dep_lib import VALUE\nRESULT = VALUE + 1\n')
        with open(os.path.join(tmp, 'lint_dep_lib.py'), 'w') as fh:
            fh.write('VALUE = 41\n')
        with open(os.path.join(tmp, 'broken_missing_dep.py'), 'w') as fh:
            fh.write('import lib_that_was_never_deployed\n')
        arms = [
            ('INF_X_99.dotted_healthy', True),
            ('lint_dep_lib', True),
            ('broken_missing_dep', False),
        ]
        bad = 0
        for mod, want_ok in arms:
            ok, err = import_in_fresh_interpreter(mod, tmp)
            verdict = 'PASS' if ok == want_ok else 'FAIL'
            if ok != want_ok:
                bad += 1
            print(f'  [{verdict}] self-test {mod}: imported={ok} wanted={want_ok}'
                  + (f'  ({err})' if err and not ok else ''))
        if bad:
            print(f'[import-lint] SELF-TEST FAILED: {bad}/3 arms wrong. DO NOT TRUST THIS LINT.')
            return 1
        print('[import-lint] SELF-TEST PASS 3/3: dotted-healthy OK, lib OK, broken FAILS.')
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--bucket', required=False, default=None)
    p.add_argument('--prefix', required=False, default=None, help='e.g. code/gold/lib/')
    p.add_argument('--expect-fail', action='store_true',
                   help='SELF-TEST: assert the lint DOES find a broken module (a lint never observed '
                        'to fail has not been shown to be able to).')
    p.add_argument('--self-test', action='store_true',
                   help='Run the offline three-arm self-test (dotted-healthy OK / lib OK / broken '
                        'FAILS) and exit. No S3 access, no bucket/prefix needed.')
    args = p.parse_args()

    if args.self_test:
        return run_self_test()
    if not args.bucket or not args.prefix:
        p.error('--bucket and --prefix are required unless --self-test')

    s3 = boto3.client('s3', region_name='us-east-1')
    tmp = tempfile.mkdtemp(prefix='deploy-import-lint-')
    try:
        mods = download_prefix(s3, args.bucket, args.prefix, tmp)
        print(f'[import-lint] s3://{args.bucket}/{args.prefix}')
        print(f'[import-lint] modules downloaded from the BUCKET: {len(mods)}   (DENOMINATOR)')
        if not mods:
            # "0 checked, 0 failed" is a pass that measured nothing. It is the same shape as a
            # "Ran 0 tests" green, and it must never be reported as success.
            print('[import-lint] ERROR: ZERO modules found under that prefix. A lint that checked '
                  'nothing is not a PASS -- it is a lint that did not run. Check the prefix.')
            return 2

        failures: list[tuple[str, str]] = []
        for m in mods:
            ok, err = import_in_fresh_interpreter(m, tmp)
            if ok:
                print(f'  OK    {m}')
            else:
                print(f'  FAIL  {m}   <-- {err}')
                failures.append((m, err))

        print(f'[import-lint] {len(mods) - len(failures)}/{len(mods)} deployed modules import cleanly.')

        if args.expect_fail:
            if failures:
                print('[import-lint] SELF-TEST PASS: the lint CAN go red. It found '
                      f'{len(failures)} unloadable module(s), as expected.')
                return 0
            print('[import-lint] SELF-TEST FAILED: expected at least one broken module and found '
                  'NONE. Either the bucket was fixed, or THIS LINT CANNOT DETECT THE THING IT EXISTS '
                  'TO DETECT. Do not trust a green from it until this is explained.')
            return 1

        if failures:
            print()
            print('[import-lint] *** DEPLOY IS BROKEN ON THE RUNNER. ***')
            print('  These modules are PRESENT in the bucket -- correct size, correct hash, green')
            print('  deploy log -- AND THEY CANNOT LOAD. The chain would die on the first import.')
            print('  Almost always a PARTIAL DEPLOY: a module shipped without a dependency it needs')
            print('  (or with a STALE one that no longer carries the symbol). Deploy the whole atomic')
            print('  set, or none of it.')
            for m, e in failures:
                print(f'    {m}: {e}')
            return 1
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    sys.exit(main())

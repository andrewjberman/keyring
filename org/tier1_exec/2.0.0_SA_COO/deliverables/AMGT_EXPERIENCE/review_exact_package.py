"""Independent, local-only review of the pinned no-span Lambda candidate."""
import ast
import base64
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

HOME = Path(__file__).resolve().parent
REPO = next(p for p in HOME.parents if (p / '.git').exists())
PIN = 'dd91fd3126318f1056b0e5f426e855d84ee0d424'
TARGET = 'lib/research/api/scoped_amgt.py'
PACKAGE = Path('C:/tmp/amgt-r-no-span-package-20260923')
EXPECTED = '0c44108821fe52850c77b119490039453b082c3639fae6dbf58de054b1397a55'
EXPECTED_BEFORE = 'r93CxQqrk8k8h2Q8KO4Iicn3pk8kyF4SFo47a9Cca5w='


def git(*args):
    return subprocess.check_output(['git', *args], cwd=REPO)


def main():
    candidate = PACKAGE / 'candidate.zip'
    rollback = PACKAGE / 'rollback.zip'
    result = {'source_pin': PIN, 'plane': 'independent local exact-ZIP review',
              'python': sys.version, 'platform': sys.platform,
              'candidate_sha256': hashlib.sha256(candidate.read_bytes()).hexdigest(),
              'before_sha256_base64': base64.b64encode(hashlib.sha256(rollback.read_bytes()).digest()).decode()}
    assert result['candidate_sha256'] == EXPECTED
    assert result['before_sha256_base64'] == EXPECTED_BEFORE
    with zipfile.ZipFile(rollback) as old, zipfile.ZipFile(candidate) as new:
        assert old.namelist() == new.namelist()
        assert len(set(new.namelist())) == len(new.namelist())
        changed = [name for name in old.namelist() if old.read(name) != new.read(name)]
        assert changed == [TARGET]
        before, after = ast.parse(old.read(TARGET)), ast.parse(new.read(TARGET))
        def funcs(tree):
            return {n.name: ast.dump(n) for n in tree.body if isinstance(n, ast.FunctionDef)}
        old_funcs, new_funcs = funcs(before), funcs(after)
        assert old_funcs.keys() == new_funcs.keys()
        changed_funcs = [name for name in old_funcs if old_funcs[name] != new_funcs[name]]
        assert set(changed_funcs) == {'_drafting_block', 'read_drafted_sections'}
        pinned_funcs = funcs(ast.parse(git('show', PIN + ':' + TARGET)))
        prior_funcs = funcs(ast.parse(git('show', PIN + '^:' + TARGET)))
        for name in changed_funcs:
            assert new_funcs[name] == pinned_funcs[name]
            assert old_funcs[name] == prior_funcs[name]
        for tree in [before, after]:
            tree.body = [n for n in tree.body if not isinstance(n, ast.FunctionDef) or n.name not in changed_funcs]
        assert ast.dump(before) == ast.dump(after)
        result.update(zip_members=len(new.namelist()), changed_members=changed,
                      changed_functions=changed_funcs, other_ast_identical=True,
                      functions_match_pinned_source=True,
                      original_functions_match_pre_repair=True,
                      api_sha256=hashlib.sha256(new.read(TARGET)).hexdigest())
        census = {'python_files': 0, 'parse_failures': [], 'drafted_sections_writers': [],
                  'drafting_calls': []}
        for name in new.namelist():
            if not name.endswith('.py'):
                continue
            census['python_files'] += 1
            try:
                tree = ast.parse(new.read(name))
            except (SyntaxError, UnicodeError):
                census['parse_failures'].append(name)
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.Dict) and any(isinstance(k, ast.Constant) and k.value == 'drafted_sections' for k in node.keys):
                    census['drafted_sections_writers'].append({'path': name, 'line': node.lineno})
                if isinstance(node, ast.Call):
                    called = node.func.id if isinstance(node.func, ast.Name) else getattr(node.func, 'attr', '')
                    if called in ['read_drafted_sections', '_drafting_block', 'read_description']:
                        census['drafting_calls'].append({'path': name, 'line': node.lineno, 'function': called,
                                                        'injected_drafting': any(k.arg == 'drafting' for k in node.keywords)})
        assert not census['parse_failures']
        result['deployed_python_census'] = census
        with tempfile.TemporaryDirectory(prefix='coo-z-exact-review-') as staging:
            staging = Path(staging)
            # First-party package bytes only; host jsonschema avoids loading Linux
            # extensions on Windows. Record this boundary, never call it live proof.
            for name in new.namelist():
                if not name.startswith('lib/') or name.endswith('/'):
                    continue
                dest = (staging / name).resolve()
                assert dest.is_relative_to(staging.resolve())
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(new.read(name))
            test_root = 'lib/research/api/tests'
            tests = git('ls-tree', '-r', '--name-only', PIN, '--', test_root).decode().splitlines()
            for name in tests:
                dest = staging / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(git('show', PIN + ':' + name))
            fixture_root = 'org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1'
            fixtures = [name for name in git('ls-tree', '-r', '--name-only', PIN, '--', fixture_root).decode().splitlines()
                        if Path(name).name.startswith('model_block_') and name.endswith('.json')]
            fixtures.append('infra/aws/terraform/harvest/scoped-amgt-api.tf')
            fixtures.append('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/crosswalk.v1.2026-09-15.json')
            for name in fixtures:
                dest = staging / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(git('show', PIN + ':' + name))
            result['repository_only_fixture_count'] = len(fixtures)
            env = os.environ.copy()
            env['PYTHONPATH'] = str(staging)
            env['AWS_EC2_METADATA_DISABLED'] = 'true'
            focused = ['test_drafted_sections.py', 'test_description_line.py',
                       'test_scoped_amgt.py', 'test_scoped_amgt_mount.py',
                       'test_route_boundary_identity.py']
            result['test_files'] = focused
            run = subprocess.run([sys.executable, '-m', 'pytest',
                                  *[test_root + '/' + name for name in focused], '-q', '-rs', '--disable-warnings'],
                                 cwd=staging, env=env, capture_output=True, text=True)
            (HOME / 'EXACT_PACKAGE_PYTEST.txt').write_text(run.stdout + run.stderr, encoding='utf-8')
            result['pytest_exit_code'] = run.returncode
            result['pytest_summary'] = run.stdout.splitlines()[-1:]
            packet = 'org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_R_CLOSER_20260923/'
            for name in ['replay_repair.py', 'HELD_CENSUS.json']:
                (staging / name).write_bytes(git('show', PIN + ':' + packet + name))
            replay = subprocess.run([sys.executable, str(staging / 'replay_repair.py')],
                                    cwd=staging, env=env, capture_output=True, text=True)
            result['retained_replay_exit_code'] = replay.returncode
            if replay.returncode == 0:
                replay_result = json.loads((staging / 'REPAIR_REPLAY.json').read_bytes())
                (HOME / 'EXACT_PACKAGE_RETAINED_REPLAY.json').write_text(
                    json.dumps(replay_result, indent=2) + '\n', encoding='utf-8')
                result['retained_replay'] = {k: v for k, v in replay_result.items() if k != 'cases'}
            else:
                # Do not print AWS exception details or credentials into evidence.
                result['retained_replay'] = 'FAILED; local replay produced no accepted result'
    (HOME / 'EXACT_PACKAGE_REVIEW.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
    return result['pytest_exit_code'] or result['retained_replay_exit_code']


if __name__ == '__main__':
    sys.exit(main())

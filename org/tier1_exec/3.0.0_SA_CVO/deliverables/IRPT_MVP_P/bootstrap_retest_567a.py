"""Unchanged original bootstrap controls on the final corrected source pair."""
from pathlib import Path
import subprocess

here = Path(__file__).resolve()
root = here.parents[5]
prior = here.with_name('bootstrap_retest_6914.py').relative_to(root).as_posix()
source = subprocess.check_output(['git', 'show', f'71e114f69a:{prior}'], cwd=root).decode('utf-8')
for old, new in {
    '69144433df8c4938cf95cb81e46ac04ae72cc61e': '567a157ec8b5465039bcc9e3842d24075e68947b',
    'cdc60da247597940b278dd43779b3953565093b7': 'dcf5e177f6513612f5e39ce90c016d098cc41aab',
    'cvo-p-bootstrap-6914-': 'cvo-p-bootstrap-567a-',
    '_6914.json': '_567a.json',
}.items():
    assert source.count(old) == 1, f'Unexpected prior replay structure: {old}'
    source = source.replace(old, new)
namespace = {'__file__': str(here), '__name__': 'final_corrected_replay'}
exec(compile(source, str(here), 'exec'), namespace)
raise SystemExit(namespace['main']())

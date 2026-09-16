"""Resolve a conflicted append-only channel as a UNION BY ROW ID: HEAD's rows in HEAD's order, then every
branch-only row appended in the branch's order. The header and prose come from HEAD. Prints the denominators."""
import json
import re
import subprocess
import sys
branch, path = sys.argv[1], sys.argv[2]
FENCE = re.compile(r'```json\s*(\[.*?\])\s*```', re.S)


def rows_of(ref):
    t = subprocess.run(['git', 'show', ref + ':' + path], capture_output=True, encoding='utf-8').stdout
    blocks = FENCE.findall(t)
    assert len(blocks) == 1, (ref, 'fenced blocks', len(blocks))
    return t, json.loads(blocks[0])


head_text, head_rows = rows_of('HEAD')
_, br_rows = rows_of(branch)
head_ids = [r['id'] for r in head_rows]
br_ids = [r['id'] for r in br_rows]
assert len(set(head_ids)) == len(head_ids) and len(set(br_ids)) == len(br_ids), 'duplicate ids inside one side'
only_branch = [r for r in br_rows if r['id'] not in set(head_ids)]
only_head = [i for i in head_ids if i not in set(br_ids)]
union = head_rows + only_branch
assert len({r['id'] for r in union}) == len(union), 'collision in the union'
m = FENCE.search(head_text)
body = '```json\n' + json.dumps(union, indent=2, ensure_ascii=False) + '\n```'
out = head_text[:m.start()] + body + head_text[m.end():]
open(path, 'wb').write(out.encode('utf-8'))
print('UNION: head', len(head_rows), '+ branch-only', len(only_branch), [r['id'] for r in only_branch],
      '= union', len(union), '| head-only (kept)', len(only_head), only_head[-4:])

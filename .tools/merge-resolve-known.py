"""merge-resolve-known.py -- resolve the two KNOWN multi-writer conflict classes without a worktree.

Every merge conflict that held a shared tree on 2026-10-08 was one of two classes (4.0.0_SA_CRO~A, replay of the drains
73b6e98145, b3afc00597, 537ac6650f and of the site Z and laptop box-pass holds; design: brief outcome O6, "one writer
per file class"; 0.0.0_AB_MSTR msg 107365: "the integrator should regenerate generated index rows after each merge"):

  1. A SURPRISE-CHANNEL file (`.../surprise-channel/{investigations,remediations,adjudications}/<KIND>_v<N>.md`, or the
     legacy flat `org/surprise_channel/**/<KIND>_v<N>.md`): a preamble, then one `## <row id> -- <title>` section per
     row. Resolved by a THREE-WAY UNION BY SECTION: rows either side added are kept (base order, then ours, then
     theirs); a row only one side changed takes that change; a row changed DIFFERENTLY on both sides, or a duplicated
     id, is NOT resolved.
     A channel file whose rows sit in ONE ```json list (the AMGT_HARVST / NFRA_CTLPLN shape, which held site Z at
     19:4xZ and dell1 at 00:3xZ on 2026-10-09) takes a THREE-WAY UNION BY ROW instead, with the same rules, each row
     emitted as its own raw bytes; the same id ADDED on both sides with different content is a DUAL-MINT and both copies
     are kept, for the row gate to admit (1.0.0_SA_CTO msg 107530). A file of one ```json block per row whose headings
     repeat (IRPT_BCKEND) or are absent (NFRA_OPLGTW), where the section union refuses, takes a THREE-WAY UNION BY BLOCK
     keyed by the row id inside each block (a batch block of several rows moves as one unit). Replay of every merge
     since 2026-10-06 (1,188 merges, 220 conflicted channel files): 217 resolved, every one equal to what landed (bytes
     or data); 3 left to a person, each a real both-sides edit. Arms: `.tools/test-merge-resolve-known.py`.
  2. A GENERATED index entry (`org/projects/<CODE>.json` whose both sides carry `home`): resolved by REGENERATING it
     from the merged tree with `.tools/missions-tree-index.py derive --write`, over a narrow extract of the merged
     tree (that project's home, the two registers, the contract): about 2 s, against 85 s for a full extract.

  4. A CROSSBOX call record (`org/devices/crossbox/XB-*.json`, one per file, written by the sending box and acked or closed
     by the receiving box; NFRA_GATSCP GS-f-4, ruling R5): resolved as a FOLD BY RECORD FIELD, never a line union -- the
     same fold `.tools/crossbox-call.py merge` uses. A top-level field (id, kind, subject, ...) must agree or be changed
     on one side only; a `sent`, `ack` or `closed` block both ends wrote folds sub-field by sub-field (write-once: a null never
     overrides a value, a value held differently on both sides REFUSES the path). `state` is derived, not folded.

  3. An APPEND-ONLY multi-writer log (APPEND_ONLY below: every manager spawn, /govern reaper run, law edit and deploy
     bypass appends a line; 0.0.0_AB_MSTR msgs 107817, 107847): resolved as a LINE UNION -- CLOUD's file, then the
     box-only lines in the box's order. Not a byte-prefix test: hand unions reorder lines, and a prefix test then HELD.

  5. A CROSS-ADJUDICATION record (`org/critical_paths/cross_adjudication/*.md`; laptop CTO ruling 2026-10-14 ~06:4xZ, reply to
     MSTR msg 109085, "only when equal after EOL normalisation"): an ADD/ADD whose two copies are byte-equal after CRLF->LF and trailing-blank-line normalisation
     resolves to CLOUD's copy (--cloud is REQUIRED for this class). ANY other difference HOLDS: a real disagreement between
     two rulings is never auto-picked. Only an add/add (no base) is resolved.

Anything else is UNRESOLVED and the caller falls back to its normal conflict path.

USAGE:  python .tools/merge-resolve-known.py --base B --ours P1 --theirs P2 --tree T [--cloud ours|theirs] <path> [...]
        (T = the tree `git merge-tree --write-tree P1 P2` wrote, conflict markers and all; --cloud names the side that is
        CLOUD, so an append-only log takes CLOUD's tail first; without it, ours' tail goes first)
        python .tools/merge-resolve-known.py --extends <rev> <path>
        (exit 0 when the working copy of an APPEND_ONLY <path>, cleaned as git would store it, extends <rev>:<path>
        byte for byte and is longer; 1 otherwise)
        python .tools/merge-resolve-known.py --append-missing <blob> <path>
        (append to the working copy of an APPEND_ONLY <path> every line of <blob> it lacks; box-sync's land)
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
CROSSBOX_RE = re.compile(r'^org/devices/crossbox/XB-[^/]+\.json$')
XADJ_RE = re.compile(r'^org/critical_paths/cross_adjudication/[^/]+\.md$')
XB_BLOCKS = ('sent', 'ack', 'closed')
APPEND_ONLY = ('org/mcp/agent-spawn-audit.log', 'org/law-edit-audit.log', 'org/safe-deploy-bypass-audit.log',
               'org/git-author-override-audit.log', 'org/mcp/drive-mode.log')   # the five of CTO ruling 1 @ba20ac668b
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


FENCE_RE = re.compile(r'^```json[ \t]*\r?\n(.*?)\r?\n[ \t]*```', re.S | re.M)


def fenced_list(text):
    """(before, head, [(key, data, raw)], sep, tail, after) for a file holding ONE ```json fence whose body is a list of
    row objects; None otherwise. Each row keeps its RAW bytes; key = (id, k) for the k-th row under that id, so a
    dual-minted id already in the file keys the same on every side."""
    ms = list(FENCE_RE.finditer(text or ''))
    if len(ms) != 1:
        return None
    m = ms[0]
    body, dec = m.group(1), json.JSONDecoder()
    i = body.find('[')
    if i < 0 or body[:i].strip():
        return None
    pos, rows, spans, seen = i + 1, [], [], {}
    while True:
        while pos < len(body) and body[pos] in ' \t\r\n,':
            pos += 1
        if pos >= len(body) or body[pos] == ']':
            break
        try:
            obj, end = dec.raw_decode(body, pos)
        except ValueError:
            return None
        if not isinstance(obj, dict) or not str(obj.get('id') or '').strip():
            return None
        rid = str(obj['id']).strip()
        seen[rid] = seen.get(rid, 0) + 1
        lead = body[spans[-1][1]:pos] if spans else None
        rows.append(((rid, seen[rid]), json.dumps(obj, sort_keys=True), (lead, body[pos:end])))
        spans.append((pos, end))
        pos = end
    if pos >= len(body) or body[pos:].strip() != ']' or not spans:
        return None
    sep = body[spans[0][1]:spans[1][0]] if len(spans) > 1 else ',\n'
    return (text[:m.start(1)], body[:spans[0][0]], rows, sep, body[spans[-1][1]:], text[m.end(1):])


def union_rows(base, ours, theirs):
    """THREE-WAY UNION BY ROW of a one-fence JSON-list channel file (the AMGT_HARVST / NFRA_CTLPLN shape). Rows either
    side added are kept; a row only one side changed takes that change; the same id ADDED on both sides with different
    content is a DUAL-MINT (1.0.0_SA_CTO msg 107530): both copies kept verbatim, ours then theirs, for the row gate to
    admit when each is on a published ref. A row changed differently on both sides, or text outside the list changed
    differently, is NOT resolved. Comparison is on the parsed data; each row is emitted as its own raw bytes."""
    parts = [fenced_list(x) if x is not None else None for x in (base, ours, theirs)]
    if parts[1] is None or parts[2] is None or (base is not None and parts[0] is None):
        return None, 'not a one-fence JSON row list on every side'
    b = parts[0] or ('', '', [], '', '', '')
    o, t = parts[1], parts[2]
    frame = []
    for k in (0, 1, 4, 5):
        ok, v = three(b[k] if parts[0] else None, o[k], t[k])
        if not ok:
            return None, 'the text around the row list changed differently on both sides'
        frame.append(v if v is not None else o[k])
    bd = {k: (d, r) for k, d, r in b[2]}
    od = {k: (d, r) for k, d, r in o[2]}
    td = {k: (d, r) for k, d, r in t[2]}
    order = [k for k, _, _ in b[2]]
    for k, _, _ in o[2]:
        if k not in bd:
            order.append(k)
    for k, _, _ in t[2]:
        if k not in bd and k not in od:
            order.append(k)
    out, dual = [], []
    for k in order:
        bb, oo, tt = bd.get(k), od.get(k), td.get(k)
        if bb is None and oo is not None and tt is not None and oo[0] != tt[0]:
            out.extend([oo[1], tt[1]])
            dual.append(k[0])
            continue
        ok, v = three(*(x[0] if x else None for x in (bb, oo, tt)))
        if not ok:
            return None, 'row %s changed differently on both sides' % k[0]
        if v is None:
            continue
        out.append(next(x[1] for x in (oo, tt, bb) if x and x[0] == v))
    # each row keeps the separator it had in its own version (the first row's lives in the frame), so a region nobody
    # touched stays byte-identical; a row that was first in its version takes ours' common separator
    body = ''.join(r if n == 0 else (lead if lead is not None else o[3]) + r for n, (lead, r) in enumerate(out))
    text = frame[0] + frame[1] + body + frame[2] + frame[3]
    try:
        if fenced_list(text) is None:
            return None, 'the merged row list does not parse'
    except ValueError:
        return None, 'the merged row list does not parse'
    return text, 'row-union' + (' dual-mint=%s' % ','.join(dual) if dual else '')


ANY_FENCE_RE = re.compile(r'^```json[ \t]*\r?\n(.*?)\r?\n[ \t]*```[ \t]*(\r?\n|$)', re.S | re.M)


def fence_chunks(text):
    """(preamble, [(key, raw chunk)], tail) for a file of one ```json OBJECT block per row; None otherwise. A chunk runs
    from the end of the previous row block (or, for the first row, from its nearest `## ` heading) to the end of its own
    block, so a row's heading and prose travel with it. key = (row id, k) for the k-th row under that id: the id inside
    the JSON, never the heading, which some channels reuse (IRPT_BCKEND) or omit (NFRA_OPLGTW)."""
    ms = list(ANY_FENCE_RE.finditer(text or ''))
    if not ms:
        return None
    chunks, seen, prev = [], {}, None
    for m in ms:
        try:
            obj = json.loads(m.group(1))
        except ValueError:
            return None
        objs = obj if isinstance(obj, list) else [obj]   # a batch block (a list of rows) moves as one unit
        if not objs or not all(isinstance(x, dict) and str(x.get('id') or '').strip() for x in objs):
            return None
        rid = '+'.join(str(x['id']).strip() for x in objs)
        seen[rid] = seen.get(rid, 0) + 1
        if prev is None:
            h = [x.start() for x in re.finditer(r'^## ', text[:m.start()], re.M)]
            start = h[-1] if h else m.start()
            pre = text[:start]
        else:
            start = prev
        chunks.append(((rid, seen[rid]), text[start:m.end()]))
        prev = m.end()
    return pre, chunks, text[prev:]


def union_fences(base, ours, theirs):
    """THREE-WAY UNION BY ROW BLOCK for a channel file of one JSON object block per row, keyed by the row id inside the
    block. Same rules as union_rows (a DUAL-MINT keeps both copies, ours then theirs). Comparison strips trailing
    whitespace; each chunk is emitted as its own raw bytes."""
    parts = [fence_chunks(x) if x is not None else None for x in (base, ours, theirs)]
    if parts[1] is None or parts[2] is None or (base is not None and parts[0] is None):
        return None, 'not one JSON row block per row on every side'
    b = parts[0] or ('', [], '')
    o, t = parts[1], parts[2]
    norm = lambda s: None if s is None else s.rstrip()  # noqa: E731
    frame = []
    for k in (0, 2):
        bv = b[k] if parts[0] else None
        ok, v = three(norm(bv), norm(o[k]), norm(t[k]))
        if not ok:
            return None, 'the text outside the row blocks changed differently on both sides'
        frame.append(next((x for x in (o[k], t[k], bv) if x is not None and norm(x) == v), o[k]))
    bd, od, td = dict(b[1]), dict(o[1]), dict(t[1])
    order = [k for k, _ in b[1]] + [k for k, _ in o[1] if k not in bd] + [k for k, _ in t[1] if k not in bd and k not in od]
    out, ids, dual = [], [], []
    for k in order:
        bb, oo, tt = bd.get(k), od.get(k), td.get(k)
        if bb is None and oo is not None and tt is not None and norm(oo) != norm(tt):
            out.extend([oo, tt])
            ids.extend([k[0], k[0]])
            dual.append(k[0])
            continue
        ok, v = three(norm(bb), norm(oo), norm(tt))
        if not ok:
            return None, 'row %s changed differently on both sides' % k[0]
        if v is not None:
            out.append(next(x for x in (oo, tt, bb) if x is not None and norm(x) == v))
            ids.append(k[0])
    for n in range(len(out) - 1):            # a chunk that was last in its version may lack the newline the next needs
        if not out[n].endswith('\n'):
            out[n] += '\n'
    text = frame[0] + ''.join(out) + frame[1]
    back = fence_chunks(text)
    if back is None or [k[0] for k, _ in back[1]] != ids:
        return None, 'the merged row blocks do not re-read as the union'
    return text, 'block-union' + (' dual-mint=%s' % ','.join(dual) if dual else '')


def union_append(base, ours, theirs, cloud='ours'):
    """A LINE UNION for an append-only log: CLOUD's file as it stands, then every line of the box's file that CLOUD does
    not hold, in the box's order (counted, so a line the box carries twice and CLOUD once adds one copy). Not a byte-prefix
    test: hand unions on other boxes reorder lines, so CLOUD's copy stops being a pure append of the base and a prefix
    test HELD dell1 263 behind (0.0.0_AB_MSTR msg 107847). Lines compare with their line ending stripped, so a CRLF copy
    of a line is the same line. Nothing is ever dropped: a line either side holds is in the result."""
    first, second = (ours, theirs) if cloud == 'ours' else (theirs, ours)
    norm = lambda ln: ln.rstrip('\r\n')  # noqa: E731
    have = {}
    for ln in first.splitlines(keepends=True):
        have[norm(ln)] = have.get(norm(ln), 0) + 1
    extra = []
    for ln in second.splitlines(keepends=True):
        k = norm(ln)
        if have.get(k, 0) > 0:
            have[k] -= 1
        elif k:
            extra.append(ln if ln.endswith('\n') else ln + '\n')
    head = first if (not first or first.endswith('\n') or not extra) else first + '\n'
    return head + ''.join(extra), 'append-only line union cloud+box-only=%d' % len(extra)


def resolve_xadj(base, ours, theirs, cloud=None):
    """(text, how) for an ADD/ADD of one cross-adjudication record, or (None, why). Resolves to CLOUD's copy only when the two
    copies are byte-equal after CRLF->LF and trailing-blank-line normalisation; any other difference HOLDS."""
    if base is not None:
        return None, 'a cross-adjudication record with a base is not an add/add; only an add/add is resolved'
    if ours is None or theirs is None:
        return None, 'a cross-adjudication record is absent on one side'
    if cloud not in ('ours', 'theirs'):
        return None, 'a cross-adjudication add/add needs --cloud to name the CLOUD side'

    def norm(t):
        return t.replace('\r\n', '\n').rstrip('\n') + '\n'

    if norm(ours) != norm(theirs):
        return None, 'the two copies differ beyond line endings and trailing blank lines: HOLD (a real disagreement between rulings is never auto-picked)'
    return (ours if cloud == 'ours' else theirs), 'cross-adjudication add/add, equal after EOL and trailing-blank normalisation: CLOUD copy (%s)' % cloud


def fold_crossbox(base, ours, theirs):
    """Fold a crossbox record written on both ends (GS-f-4). Same rule as `crossbox-call.py merge` (read, not edited): the
    identity and body fields, and each of the `sent`, `ack`, `closed` blocks, take the side that moved from the base; a block
    BOTH ends wrote folds sub-field by sub-field -- a null never overrides a value and two different values REFUSE ('resolve by hand'); `state` is recomputed
    from the folded fields exactly as `derive_state` does. Returns (text, how) or (None, why)."""
    try:
        recs = [json.loads(x) if x is not None else None for x in (base, ours, theirs)]
    except ValueError:
        return None, 'a side is not JSON'
    b, o, t = recs
    if not (isinstance(o, dict) and isinstance(t, dict)) or (b is not None and not isinstance(b, dict)):
        return None, 'a side is not a record object'
    if not o.get('id') or o.get('id') != t.get('id') or (b is not None and b.get('id') != o.get('id')):
        return None, 'the sides are not the same record id'
    merged = dict(o)
    for key in list(o) + [k for k in t if k not in o]:
        if key == 'state':
            continue
        ov, tv = o.get(key), t.get(key)
        if key in XB_BLOCKS and (ov is None or isinstance(ov, dict)) and (tv is None or isinstance(tv, dict)):
            ok, v = three(b.get(key) if b else None, ov, tv)
            if ok:                      # one side moved the block (or both to the same value): it takes that side
                merged[key] = v
                continue
            block = dict(ov or {})      # both ends wrote the block: the sub-field fold `crossbox-call.py merge` uses
            for sub, val in (tv or {}).items():
                if val is None:
                    continue
                if block.get(sub) not in (None, val):
                    return None, 'both sides hold a different %s.%s (%r vs %r): resolve by hand' % (key, sub, block[sub], val)
                block[sub] = val
            merged[key] = block
            continue
        ok, v = three(b.get(key) if b else None, ov, tv)
        if not ok:
            return None, 'field %s changed differently on both sides (%r vs %r)' % (key, ov, tv)
        merged[key] = v
    closed, ack = merged.get('closed') or {}, merged.get('ack') or {}
    merged['state'] = 'CLOSED-BOTH' if (closed.get('from_at') and closed.get('to_at')) else ('ACKED' if ack.get('at') else 'OPEN')
    return json.dumps(merged, indent=1, ensure_ascii=True) + '\n', 'crossbox-fold'


def extends(rev, path):
    """True when the working copy of `path`, cleaned as git would store it, extends rev:path byte for byte and is longer."""
    head = show(rev, path)
    rc, out = git('hash-object', '-w', '--', path)       # applies the clean filters (eol) the commit will apply
    if head is None or rc != 0:
        return False
    rc, raw = git('cat-file', '-p', out.decode().strip())
    work = raw.decode('utf-8', errors='surrogateescape') if rc == 0 else None
    return work is not None and len(work) > len(head) and work.startswith(head)


def append_missing(blob, path):
    """Append to the WORKING COPY of an append-only log every line of `blob` it does not hold (counted, line endings
    stripped for comparison, written in the file's own line ending). Used by box-sync's land when a seat's uncommitted
    appends sit on a log the merge changed (0.0.0_AB_MSTR msg 107952): the land leaves the file's bytes alone and this
    adds CLOUD's lines. It only ever APPENDS, so a line another process appends meanwhile is never overwritten.
    Returns the number of lines appended, or None when the blob or the file cannot be read."""
    rc, raw = git('cat-file', '-p', blob)
    if rc != 0:
        return None
    try:
        with open(os.path.join(ROOT, path), 'rb') as fh:
            disk = fh.read().decode('utf-8', errors='surrogateescape')
    except OSError:
        return None
    norm = lambda ln: ln.rstrip('\r\n')  # noqa: E731
    have = {}
    for ln in disk.splitlines():
        have[norm(ln)] = have.get(norm(ln), 0) + 1
    add = []
    for ln in raw.decode('utf-8', errors='surrogateescape').splitlines():
        k = norm(ln)
        if have.get(k, 0) > 0:
            have[k] -= 1
        elif k:
            add.append(k)
    if add:
        eol = '\r\n' if '\r\n' in disk else '\n'
        lead = eol if disk and not disk.endswith('\n') else ''
        with open(os.path.join(ROOT, path), 'ab') as fh:
            fh.write((lead + eol.join(add) + eol).encode('utf-8', errors='surrogateescape'))
    return len(add)


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
    if argv[:1] == ['--append-missing']:
        if len(argv) != 3 or argv[2] not in APPEND_ONLY:
            print(__doc__)
            return 2
        n = append_missing(argv[1], argv[2])
        print('APPENDED %s %s line(s)' % (argv[2], n) if n is not None else 'UNREAD %s' % argv[2])
        return 0 if n is not None else 1
    if argv[:1] == ['--extends']:
        if len(argv) != 3 or argv[2] not in APPEND_ONLY:
            print(__doc__)
            return 2
        return 0 if extends(argv[1], argv[2]) else 1
    opts, paths, i = {}, [], 0
    while i < len(argv):
        if argv[i] in ('--base', '--ours', '--theirs', '--tree', '--cloud') and i + 1 < len(argv):
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
            sides = [show(opts[k], p) for k in ('base', 'ours', 'theirs')]
            if all(fenced_list(x) is not None for x in sides if x is not None):
                text, how = union_rows(*sides)
            else:
                text, how = union_channel(*sides)
                if text is None:
                    text2, how2 = union_fences(*sides)
                    text, how = (text2, how2) if text2 is not None else (None, how + '; ' + how2)
        elif GENERATED_RE.match(p):
            text, how = regenerate(p, opts['tree'], opts['ours'], opts['theirs'])
        elif CROSSBOX_RE.match(p):
            sides = [show(opts[k], p) for k in ('base', 'ours', 'theirs')]
            if sides[1] is None or sides[2] is None:
                text, how = None, 'a crossbox record is absent on one side'
            else:
                text, how = fold_crossbox(*sides)
        elif XADJ_RE.match(p):
            sides = [show(opts[k], p) for k in ('base', 'ours', 'theirs')]
            text, how = resolve_xadj(*sides, cloud=opts.get('cloud'))
        elif p in APPEND_ONLY:
            sides = [show(opts[k], p) for k in ('base', 'ours', 'theirs')]
            if sides[1] is None or sides[2] is None:
                text, how = None, 'an append-only log is absent on one side'
            else:
                text, how = union_append(*sides, cloud=opts.get('cloud', 'ours'))
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

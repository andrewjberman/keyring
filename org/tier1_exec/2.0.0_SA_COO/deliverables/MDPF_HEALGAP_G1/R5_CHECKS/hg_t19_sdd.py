"""MDPF_HEALGAP round 5, HG-t-19: the SDD session restore-act determination document. Read-only; no AWS call.

  python hg_t19_sdd.py [DOC]

DOC (default org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~16/SDD_SESSION_RESTORE_DETERMINATION_R5.md)
must carry these five level-2 headings, in this order, each with content:
  ## 1. The reader        -- what the puller reads and where (path:line citations).
  ## 2. The writers       -- a line `SEARCHED: <n> files` (n > 0) and either one or more writers as `path:line` of the code
                             that writes the SAME credential the reader reads, or the exact line `WRITERS FOUND: 0`.
  ## 3. The capture       -- what the capture task writes and where (path:line citations).
  ## 4. The same thing?   -- a line `COMPARISON: SAME` | `COMPARISON: DIFFERENT` | `COMPARISON: UNDETERMINABLE FROM CODE`
                             with at least one citation.
  ## 5. Decision          -- exactly one line `DECISION: NAMED-ACT` | `DECISION: REPOINT` | `DECISION: BOX-READ-OWED`, and
      NAMED-ACT      -> lines `PERSON:` (who) and `TRIGGER:` (what shows the session is dead; cite the puller's own text)
      REPOINT        -> a line `PAIR:` naming the never-widen pair the repoint needs, and `COMPARISON: SAME` in section 4
      BOX-READ-OWED  -> a line `READ-COMMAND:` with the exact read (command, identity it runs as, what it prints) and `RUNS-AS:`
every `path:line` citation must resolve in the repository (the file exists and the line number is inside it).
Last line: SDD-OK <decision> or SDD-BAD <reasons>. At the base (no file) this is SDD-BAD.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

DOC = "org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~16/SDD_SESSION_RESTORE_DETERMINATION_R5.md"
HEADINGS = ["1. The reader", "2. The writers", "3. The capture", "4. The same thing?", "5. Decision"]
CITE = re.compile(r"([A-Za-z0-9_./\-]+\.[A-Za-z0-9]+):(\d+)")


def sections(text: str) -> dict:
    out, cur = {}, None
    for line in text.splitlines():
        m = re.match(r"^##\s+(.*\S)\s*$", line)
        if m:
            cur = m.group(1)
            out[cur] = []
        elif cur is not None:
            out[cur].append(line)
    return {k: "\n".join(v) for k, v in out.items()}


def resolves(f: str, ln: str) -> bool:
    p = Path(f)
    if not p.is_file():
        return False
    try:
        n = sum(1 for _ in p.open(encoding="utf-8", errors="replace"))
    except OSError:
        return False
    return 1 <= int(ln) <= n


def main(path: str) -> int:
    p = Path(path)
    if not p.is_file():
        print(f"SDD-BAD no document at {path}")
        return 1
    text = p.read_text(encoding="utf-8")
    sec = sections(text)
    bad = []
    order = [h for h in sec if h in HEADINGS]
    if order != HEADINGS:
        bad.append(f"headings {list(sec)} are not exactly {HEADINGS} in order")
        print("SDD-BAD " + "; ".join(bad))
        return 1
    for h in HEADINGS:
        if len(sec[h].strip()) < 20:
            bad.append(f"section '{h}' has no content")
    for h in ("1. The reader", "3. The capture", "4. The same thing?"):
        cites = CITE.findall(sec[h])
        if not any(resolves(f, ln) for f, ln in cites):
            bad.append(f"section '{h}': no path:line citation resolves (cites {cites[:2]})")
    for f, ln in CITE.findall(text):
        if "/" in f and not resolves(f, ln):
            bad.append(f"citation {f}:{ln} does not resolve")
    w = sec["2. The writers"]
    m = re.search(r"SEARCHED:\s*(\d+)\s+files", w)
    if not m or int(m.group(1)) <= 0:
        bad.append("section 2 has no 'SEARCHED: <n> files' denominator with n > 0")
    has_zero = re.search(r"^WRITERS FOUND: 0\s*$", w, re.M) is not None
    has_writer = any(resolves(f, ln) for f, ln in CITE.findall(w))
    if has_zero == has_writer:
        bad.append("section 2 must carry either the line 'WRITERS FOUND: 0' or at least one resolving writer citation, not both or neither")
    cmp = re.findall(r"^COMPARISON:\s*(SAME|DIFFERENT|UNDETERMINABLE FROM CODE)\s*$", sec["4. The same thing?"], re.M)
    if len(cmp) != 1:
        bad.append("section 4 needs exactly one COMPARISON line (SAME | DIFFERENT | UNDETERMINABLE FROM CODE)")
    dec = re.findall(r"^DECISION:\s*(NAMED-ACT|REPOINT|BOX-READ-OWED)\s*$", sec["5. Decision"], re.M)
    if len(dec) != 1:
        bad.append("section 5 needs exactly one DECISION line (NAMED-ACT | REPOINT | BOX-READ-OWED)")
    else:
        d, d5 = dec[0], sec["5. Decision"]
        if d == "NAMED-ACT":
            if not re.search(r"^PERSON:\s*\S", d5, re.M) or not re.search(r"^TRIGGER:\s*\S", d5, re.M):
                bad.append("NAMED-ACT needs PERSON: and TRIGGER: lines")
            if not any(resolves(f, ln) for f, ln in CITE.findall(d5)):
                bad.append("NAMED-ACT needs a resolving citation of the puller's own text in section 5")
        elif d == "REPOINT":
            if not re.search(r"^PAIR:\s*\S", d5, re.M):
                bad.append("REPOINT needs a PAIR: line")
            if cmp != ["SAME"]:
                bad.append("REPOINT requires COMPARISON: SAME in section 4")
        elif d == "BOX-READ-OWED":
            if not re.search(r"^READ-COMMAND:\s*\S", d5, re.M) or not re.search(r"^RUNS-AS:\s*\S", d5, re.M):
                bad.append("BOX-READ-OWED needs READ-COMMAND: and RUNS-AS: lines")
    if re.search(r"\b(TBD|TODO)\b", text):
        bad.append("reads TBD/TODO")
    if bad:
        print("SDD-BAD " + "; ".join(bad))
        return 1
    print(f"SDD-OK {dec[0]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else DOC))

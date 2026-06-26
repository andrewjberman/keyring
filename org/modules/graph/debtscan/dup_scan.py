#!/usr/bin/env python3
"""BM25 dup/dead-twin scanner -- v2 (post-arch-gate build, CTO GO 2026-06-26).

v1 (dup_scan_proto.py) proved the SHAPE on the cloud; CTO arch-gated GO with 4 conditions.
v2 carries all four:
  (1) PRECISE + AUDITABLE suppressors -- env-triplet / per-agent-tree / service-suffix,
      each suppresses ONLY its exact benign pattern AND logs what it hid (no silent suppression).
  (2) DEAD = GRAPH-CONFIRMED -- deprecated//archive/ RAISE the dead-prior but a finding is
      "CONFIRMED dead" ONLY after a graph reachability check shows zero consumers; else it is
      "INFERRED dead, graph-pending" (Rule 22). Removal is always human-confirm.
  (3) opal_users_v2 -- routed to owners (separate); the loop is proven end-to-end.
  (4) CONTENT-LEVEL tier -- BM25 over file BODIES catches DRIFTED near-dups (shared body,
      different names). Dogfood: the 5 not-yet-migrated trading_calendar copies must surface
      as near-twins of lib/trading_calendar.py.

Advisory/scanner ONLY. Output = a RANKED candidate ledger + a SUPPRESSION AUDIT. Never removes.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]

# ---- firm detection (cross-firm same-name = expected architecture -> SUPPRESS) -------------
_FIRMS = ["49f", "bd", "cot", "inf", "mdpf", "yang", "schwab", "astn", "etfs", "smartx", "news", "nna"]
_ENV_RE = re.compile(r"(^|/)environments?/(dev|staging|stage|prod|production)(/|$)")
_SERVICE_SUFFIX = ("s3", "cw", "sm", "ddb", "dynamo", "secrets", "kms", "logs", "lambda", "sqs", "sns", "ssm", "cloudwatch")
_AGENT_TREE_RE = re.compile(r"org/(tier[0-9]_exec|mcp|critical_paths)/[^/]+/(logs|task_orders|deliverables|inbox)/", re.I)
_AGENT_SERIAL_RE = re.compile(r"/[0-9]+\.[0-9]+\.[0-9]+_[A-Za-z0-9]+/")


def _firm_of(path: str) -> str | None:
    p = path.lower()
    for f in _FIRMS:
        if re.search(rf"(^|[/_-]){re.escape(f)}([/_-]|$|\b)", p):
            return f
    return None


def _env_of(path: str) -> str | None:
    m = _ENV_RE.search(path.lower())
    return m.group(2) if m else None


def _strip_env(path: str) -> str:
    return _ENV_RE.sub(lambda m: (m.group(1) or "") + "ENV" + (m.group(3) or ""), path.lower())


def _service_suffix_of(label: str) -> tuple[str, str] | None:
    """Return (base, suffix) if label ends in a known service suffix, else None."""
    for suf in _SERVICE_SUFFIX:
        if label.lower().endswith("_" + suf):
            return label[: -(len(suf) + 1)].lower(), suf
    return None


# ---- tokenization -------------------------------------------------------------------------
_SPLIT = re.compile(r"[^a-z0-9]+")
_PY_KEYWORDS = frozenset(
    "the and for not import from def class return self if else elif while try except "
    "with as in is or none true false print def pass raise yield lambda".split()
)


def _tok(s: str) -> list[str]:
    return [t for t in _SPLIT.split(s.lower()) if t and len(t) > 1]


def _tok_body(s: str) -> list[str]:
    return [t for t in _SPLIT.split(s.lower()) if t and len(t) > 2 and t not in _PY_KEYWORDS and not t.isdigit()]


# ---- BM25 over a corpus of "documents" ----------------------------------------------------
class BM25:
    def __init__(self, docs: list[list[str]], k1: float = 1.5, b: float = 0.75):
        self.docs = docs
        self.k1, self.b = k1, b
        self.N = len(docs)
        self.avgdl = sum(len(d) for d in docs) / max(self.N, 1)
        self.df: dict[str, int] = defaultdict(int)
        self.postings: dict[str, list[int]] = defaultdict(list)
        for i, d in enumerate(docs):
            for t in set(d):
                self.df[t] += 1
                self.postings[t].append(i)
        self.idf = {t: math.log(1 + (self.N - n + 0.5) / (n + 0.5)) for t, n in self.df.items()}

    def neighbors(self, i: int, top: int = 5, min_score: float = 0.0, max_df_ratio: float = 0.25):
        # gather candidates only from DISCRIMINATIVE tokens (skip tokens in >max_df_ratio of docs:
        # they carry ~zero idf AND their huge postings cause an O(N) candidate blow-up per doc).
        q = self.docs[i]
        df_cut = max(self.N * max_df_ratio, 2)
        cand: set[int] = set()
        for t in set(q):
            if self.df.get(t, 0) <= df_cut:
                cand.update(self.postings[t])
        cand.discard(i)
        scored = [(self._score(q, j), j) for j in cand]
        scored.sort(reverse=True)
        return [(s, j) for s, j in scored[:top] if s > min_score]

    def _score(self, q: list[str], j: int) -> float:
        d = self.docs[j]
        dl = len(d)
        tf: dict[str, int] = defaultdict(int)
        for t in d:
            tf[t] += 1
        s = 0.0
        for t in set(q):
            if t not in tf:
                continue
            num = tf[t] * (self.k1 + 1)
            den = tf[t] + self.k1 * (1 - self.b + self.b * dl / self.avgdl)
            s += self.idf.get(t, 0.0) * num / den
        return s

    def self_score(self, i: int) -> float:
        """Score of a doc against itself -- the normalization ceiling for a band."""
        return self._score(self.docs[i], i)


# ---- suppression audit (CONDITION 1: no silent suppression) --------------------------------
class SuppressionAudit:
    """Every suppressed pair is logged with the suppressor id + reason. Auditable; a
    suppressor masking a real dup is therefore inspectable, never silent."""

    def __init__(self):
        self.hidden: list[dict] = []

    def hide(self, suppressor_id: str, reason: str, a: dict, b: dict):
        self.hidden.append({
            "suppressor": suppressor_id,
            "reason": reason,
            "a": a.get("id") or a.get("path"),
            "b": b.get("id") or b.get("path"),
        })

    def summary(self) -> dict:
        by = defaultdict(int)
        for h in self.hidden:
            by[h["suppressor"]] += 1
        return dict(by)


def suppressor_verdict(a: dict, b: dict, same_label: bool, audit: SuppressionAudit) -> str | None:
    """Return a BENIGN_* suppressor id (and log it) if a precise benign pattern matches; else None.
    Each branch matches ONLY its exact pattern (CTO condition 1)."""
    pa, pb = a.get("path", ""), b.get("path", "")

    # firm-cross: different firm => expected firm-separation architecture
    fa, fb = a.get("firm"), b.get("firm")
    if fa and fb and fa != fb:
        audit.hide("BENIGN_CROSS_FIRM", f"firm {fa} vs {fb} -- firm-separation is by design", a, b)
        return "BENIGN_CROSS_FIRM"

    # env-triplet: PRECISE -- identical save for the environments/{dev,staging,prod} component
    ea, eb = _env_of(pa), _env_of(pb)
    if ea and eb and ea != eb and _strip_env(pa) == _strip_env(pb):
        audit.hide("BENIGN_ENV_TWIN", f"same resource differing ONLY by env {ea} vs {eb}", a, b)
        return "BENIGN_ENV_TWIN"

    # per-agent-tree: PRECISE -- same filename, both under a recognized per-agent/per-thread tree
    if a.get("name") and a.get("name") == b.get("name"):
        ta = bool(_AGENT_TREE_RE.search(pa) or _AGENT_SERIAL_RE.search(pa))
        tb = bool(_AGENT_TREE_RE.search(pb) or _AGENT_SERIAL_RE.search(pb))
        if ta and tb:
            audit.hide("BENIGN_AGENT_TREE", "same filename under distinct per-agent trees (1-per-agent expected)", a, b)
            return "BENIGN_AGENT_TREE"

    # service-suffix: PRECISE -- same module, bases equal, differ only by a known service suffix
    la, lb = a.get("label", ""), b.get("label", "")
    if la and lb and a.get("module") and a.get("module") == b.get("module"):
        sa, sb = _service_suffix_of(la), _service_suffix_of(lb)
        if sa and sb and sa[0] == sb[0] and sa[1] != sb[1]:
            audit.hide("BENIGN_SERVICE_SPLIT", f"one role's policy split by service ({sa[1]} vs {sb[1]})", a, b)
            return "BENIGN_SERVICE_SPLIT"

    # iam-policy-split: STRUCTURAL + PRECISE -- two inline policies attached to the SAME role
    # (parsed `role =` attr, not a string guess) are one role's policy split by action-area, NOT a
    # dup. Different labels required (an EXACT-label collision is a real concern, handled elsewhere).
    # Does NOT mask a real dup: a true duplicate shows as identical CONTENT (content tier) or an
    # EXACT label, neither of which this branch touches.
    if (a.get("type") in _POLICY_TYPES and b.get("type") == a.get("type")
            and a.get("role") and a.get("role") == b.get("role")
            and a.get("module") == b.get("module") and la != lb):
        audit.hide("BENIGN_IAM_POLICY_SPLIT", f"both attach role '{a['role']}' -- one role's policy split by action", a, b)
        return "BENIGN_IAM_POLICY_SPLIT"

    return None


# ---- graph dead-confirm leg (CONDITION 2: dead = graph-confirmed, else graph-pending) -------
_DEAD_PRIOR_RE = re.compile(r"(^|/)(deprecated|archive|archived|old|legacy|_attic|graveyard)(/|$)", re.I)


def dead_prior(path: str) -> bool:
    return bool(_DEAD_PRIOR_RE.search(path))


_DEAD_CACHE: dict[str, str] = {}


def graph_dead_confirm(resource_id: str, path: str) -> str:
    """Best-effort reachability check. Returns one of:
      CONFIRMED_DEAD            -- graph shows zero consumers (only valid after a real query)
      INFERRED_DEAD_GRAPH_PENDING -- a dead-prior path (deprecated//archive/) but NOT graph-confirmed
      REACHABLE                 -- graph shows >=1 consumer
      UNKNOWN                   -- no dead-prior + no graph signal
    Rule 22: nothing is CONFIRMED_DEAD without a graph result; removal is always human-confirm.
    Cached + short-timeout: this leg runs ONLY on high-value (EXACT-label) findings, not the flood."""
    if resource_id in _DEAD_CACHE:
        return _DEAD_CACHE[resource_id]
    prior = dead_prior(path)
    verdict = "INFERRED_DEAD_GRAPH_PENDING" if prior else "UNKNOWN"
    try:
        r = subprocess.run(
            ["comp-blast", resource_id],
            cwd=str(REPO), capture_output=True, text=True, timeout=8,
        )
        out = ((r.stdout or "") + (r.stderr or "")).lower()
        if r.returncode == 0 and out.strip() and "not found" not in out:
            zero = ("0 downstream" in out or "no consumers" in out or "zero consumers" in out
                    or "0 affected" in out)
            verdict = "CONFIRMED_DEAD" if zero else "REACHABLE"
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
        pass  # no usable graph result -> never assert CONFIRMED; keep the honest fallback
    _DEAD_CACHE[resource_id] = verdict
    return verdict


# ---- metric-evidence dead-confirm (CTO production condition 1: WINDOW >= longest access cadence) --
_AWS = shutil.which("aws.cmd") or shutil.which("aws") or os.path.expanduser(
    "~/AppData/Local/Programs/Python/Python312/Scripts/aws.cmd")
_DDB_WINDOW_DAYS = 30  # >= longest plausible low-frequency access cadence; 24h would FALSE-CONFIRM a
#                        weekly/monthly-read table (a billing job, a monthly report). CTO cond-1.


def metric_reads_sum(table: str, window_days: int = _DDB_WINDOW_DAYS, now: str = "2026-06-26T18:00:00") -> tuple:
    """Sum of DynamoDB ConsumedReadCapacityUnits over [now-window, now]. Returns (sum, n_datapoints)
    or (None, 0) on error. Read-only operational metric query (no graph edge -> raw aws is correct)."""
    end = dt.datetime.strptime(now, "%Y-%m-%dT%H:%M:%S")
    start = end - dt.timedelta(days=window_days)
    try:
        r = subprocess.run(
            [_AWS, "cloudwatch", "get-metric-statistics", "--namespace", "AWS/DynamoDB",
             "--metric-name", "ConsumedReadCapacityUnits", "--dimensions", f"Name=TableName,Value={table}",
             "--start-time", start.strftime("%Y-%m-%dT%H:%M:%S"), "--end-time", end.strftime("%Y-%m-%dT%H:%M:%S"),
             "--period", str(window_days * 86400), "--statistics", "Sum", "--output", "json"],
            capture_output=True, text=True, timeout=60,
        )
        if r.returncode != 0:
            return (None, 0)
        pts = json.loads(r.stdout).get("Datapoints", [])
        return (sum(p.get("Sum", 0) for p in pts), len(pts))
    except (OSError, subprocess.TimeoutExpired, ValueError):
        return (None, 0)


def windowed_dead_verdict(graph_status: str, table: str, window_days: int = _DDB_WINDOW_DAYS) -> str:
    """DUAL-EVIDENCE dead-confirm (CTO cond-1+2): CONFIRMED_DEAD requires BOTH the graph showing
    zero consumers AND zero runtime reads over a window >= the longest plausible access cadence.
    Either signal alone => INFERRED (graph-pending or metric-pending). The verdict string CARRIES
    the window, so a human adjudicating the removal-worklist sees exactly what 'dead' rests on."""
    reads, npts = metric_reads_sum(table, window_days)
    metric_dead = (reads is not None and npts > 0 and reads == 0)
    graph_zero = graph_status in ("CONFIRMED_DEAD", "INFERRED_DEAD_GRAPH_PENDING")  # 0/pending consumers
    graph_confirmed_zero = (graph_status == "CONFIRMED_DEAD")
    if graph_confirmed_zero and metric_dead:
        return f"CONFIRMED_DEAD (0 reads/{window_days}d, 0 graph-consumers)"
    if metric_dead and graph_zero:
        return f"INFERRED_DEAD (0 reads/{window_days}d; graph-consumers PENDING)"
    if metric_dead:
        return f"INFERRED_DEAD (0 reads/{window_days}d; graph REACHABLE-or-unknown)"
    if reads is None:
        return "INFERRED_DEAD (metric-pending)" if graph_zero else "UNKNOWN"
    return f"REACHABLE ({reads:.0f} reads/{window_days}d)"


def validate_dead_confirm() -> None:
    """Fixture validation (CTO cond-1): opal-users v1 must read CONFIRMED/INFERRED-dead over the
    WINDOW (not just 24h); v2 must be REACHABLE. Proves the window guards against false-confirm."""
    print(f"=== DEAD-CONFIRM FIXTURE VALIDATION (window={_DDB_WINDOW_DAYS}d) ===")
    for table, graph_assume in [("opal-users", "CONFIRMED_DEAD"), ("opal-users-v2", "REACHABLE")]:
        reads, npts = metric_reads_sum(table)
        verdict = windowed_dead_verdict(graph_assume, table)
        print(f"  {table:<16} reads/{_DDB_WINDOW_DAYS}d={reads} pts={npts}  graph_assume={graph_assume}  -> {verdict}")


# ---- corpus A: TF resource labels (NAME-level) --------------------------------------------
_TF_RES = re.compile(r'resource\s+"([^"]+)"\s+"([^"]+)"\s*\{')
_ROLE_ATTR = re.compile(r'\brole\s*=\s*(?:aws_iam_role\.)?["]?([A-Za-z0-9_.${}-]+?)(?:\.id|\.name|["])', re.I)
_POLICY_TYPES = ("aws_iam_role_policy", "aws_iam_role_policy_attachment")


def _tf_resources() -> list[dict]:
    out = []
    for tf in REPO.glob("infra/aws/**/*.tf"):
        if ".terraform" in tf.parts:
            continue
        try:
            txt = tf.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        rel = str(tf.relative_to(REPO)).replace("\\", "/")
        matches = list(_TF_RES.finditer(txt))
        for k, m in enumerate(matches):
            rtype, label = m.group(1), m.group(2)
            # body = from this block-open to the next resource block (or EOF) -- enough to read `role =`
            body_end = matches[k + 1].start() if k + 1 < len(matches) else len(txt)
            body = txt[m.end():body_end]
            role = None
            if rtype in _POLICY_TYPES:
                rm = _ROLE_ATTR.search(body)
                role = rm.group(1) if rm else None
            out.append({
                "id": f"{rtype}.{label}", "type": rtype, "label": label,
                "module": str(Path(rel).parent), "path": rel, "name": label, "role": role,
                "doc": _tok(label) + _tok(rtype.replace("aws_", "")),
                "firm": _firm_of(rel) or _firm_of(label),
            })
    return out


# ---- corpus C (CONDITION 4): python file bodies (CONTENT-level) ----------------------------
# vendored-dependency markers: a lambda tree carries its layer/site-packages deps (boto3, pandas,
# numpy, ...). Those are NOT first-party source -- including them drowns the corpus + the runtime.
_VENDOR_DIRS = frozenset((
    ".terraform", "__pycache__", ".venv", "venv", "node_modules", "site-packages",
    "dist-info", "boto3", "botocore", "pandas", "numpy", "pip", "setuptools",
    "pkg_resources", "dateutil", "urllib3", "certifi", "s3transfer", "jmespath",
    "pytz", "six", "wheel", "_vendor", "build", "dist",
))


def _is_vendored(parts: tuple) -> bool:
    for p in parts:
        pl = p.lower()
        if pl in _VENDOR_DIRS or pl.endswith(".dist-info") or pl.endswith(".egg-info"):
            return True
    return False


def _py_bodies(roots: list[str]) -> list[dict]:
    # source from git-tracked files only: vendored layer/site-packages deps are untracked/build
    # artifacts, so this is the first-party corpus by construction (+ the _is_vendored belt).
    try:
        r = subprocess.run(["git", "ls-files", "*.py"], cwd=str(REPO),
                           capture_output=True, text=True, timeout=60)
        tracked = [f for f in r.stdout.splitlines() if f.strip()]
    except (OSError, subprocess.TimeoutExpired):
        tracked = []
    roots_t = tuple(roots)
    out = []
    for rel in tracked:
        if not rel.startswith(roots_t):
            continue
        parts = tuple(rel.split("/"))
        if _is_vendored(parts):
            continue
        py = REPO / rel
        try:
            txt = py.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        nlines = txt.count("\n") + 1
        if nlines > 2500:
            continue
        body = _tok_body(txt)
        if len(body) < 20:
            continue
        out.append({"id": rel, "path": rel, "name": py.name, "doc": body,
                    "firm": _firm_of(rel), "lines": nlines})
    return out


# ---- scans --------------------------------------------------------------------------------
def scan_tf_names(audit: SuppressionAudit) -> list[dict]:
    res = _tf_resources()
    by_type: dict[str, list[int]] = defaultdict(list)
    for i, r in enumerate(res):
        by_type[r["type"]].append(i)
    findings, seen = [], set()
    for rtype, idxs in by_type.items():
        if len(idxs) < 2:
            continue
        bm = BM25([res[i]["doc"] for i in idxs])
        for li, gi in enumerate(idxs):
            for score, lj in bm.neighbors(li, top=4, min_score=1.0):
                gj = idxs[lj]
                key = tuple(sorted((gi, gj)))
                if key in seen:
                    continue
                seen.add(key)
                a, b = res[gi], res[gj]
                same = a["label"] == b["label"]
                if not same and score < 2.5:
                    continue
                sup = suppressor_verdict(a, b, same, audit)
                if sup:
                    continue
                # NAME-level concern survives suppression. EXACT-label cross-module = the HIGH-value
                # twin/double-management signal (opal_users_v2 class) -> dead-confirm leg runs here.
                # NAME-near (non-exact) is inherently weak (CTO: drifted dups belong to CONTENT tier)
                # -> demote to an informational band, NO dead-confirm (keeps the run fast + honest).
                if same and a["module"] != b["module"]:
                    verdict, tier = "TF_LABEL_COLLISION", "high"
                else:
                    verdict, tier = "NAME_NEAR_INFO", "info"
                dead = None
                if tier == "high" and (dead_prior(a["path"]) or dead_prior(b["path"])):
                    side = a if dead_prior(a["path"]) else b
                    dead = graph_dead_confirm(side["id"], side["path"])
                findings.append({"score": round(score, 2), "verdict": verdict, "tier": tier, "same_label": same,
                                 "a": a["id"], "a_mod": a["module"], "b": b["id"], "b_mod": b["module"],
                                 "dead_status": dead})
    findings.sort(key=lambda f: (f["tier"] != "high", -f["score"]))
    return findings


def scan_content(audit: SuppressionAudit, dogfood_path: str) -> dict:
    docs = _py_bodies(["lib", "data", "infra/aws/lambda", "org/modules/graph"])

    # TIER C1 -- EXACT body-dup groups (O(N), instant): a structurally-identical body under >1
    # DISTINCT filename = a copied module (the class the 5 trading_calendar copies + jwt_freshness
    # belong to). Same filename across per-agent trees is the name-tier's job -> excluded here.
    by_hash: dict[str, list[int]] = defaultdict(list)
    for i, d in enumerate(docs):
        h = hashlib.sha1((" ".join(d["doc"])).encode("utf-8")).hexdigest()
        by_hash[h].append(i)
    exact = []
    for h, idxs in by_hash.items():
        if len(idxs) < 2:
            continue
        names = {docs[i]["name"] for i in idxs}
        paths = sorted(docs[i]["path"] for i in idxs)
        # firm-cross suppression on the group (a per-firm identical helper is expected architecture)
        firms = {docs[i]["firm"] for i in idxs if docs[i]["firm"]}
        if len(names) < 2:
            continue  # identical body + identical name => copied helper; defer to name/agent-tree tier
        rec = {"members": paths, "distinct_names": sorted(names), "lines": docs[idxs[0]]["lines"]}
        if len(firms) > 1:
            audit.hide("BENIGN_CROSS_FIRM", f"identical body across firms {sorted(firms)} -- per-firm copy expected", docs[idxs[0]], docs[idxs[1]])
            continue
        exact.append(rec)
    exact.sort(key=lambda r: -len(r["members"]))

    # TIER C2 -- DOGFOOD: BM25 near-neighbors of lib/trading_calendar.py (one doc vs corpus = cheap).
    # The 5 NOT-yet-migrated copies share the holiday-list + is_trading_day body => must surface as
    # near (NOT exact -- they pre-date the lib refactor). Proves CONTENT catches DRIFTED dups.
    bm = BM25([d["doc"] for d in docs])
    idx = {d["path"]: i for i, d in enumerate(docs)}
    dog = []
    if dogfood_path in idx:
        di = idx[dogfood_path]
        ceil = bm.self_score(di) or 1.0
        for score, j in bm.neighbors(di, top=15, min_score=0.0):
            dog.append({"norm": round(score / ceil, 3), "score": round(score, 1), "path": docs[j]["path"]})
    return {"exact_dups": exact, "dogfood": dog, "corpus_size": len(docs),
            "near_sweep_note": "exhaustive all-pairs near-sweep is tier-2 (bounded in production: "
                               "blocked-by-stem + max-df candidate gen); prototype proves the tier via "
                               "exact-dup groups + the one-doc dogfood"}


def run_scan(class_filter: str | None = None) -> dict:
    """Run all tiers; return the result dict. class_filter narrows the suppression audit view
    to one class (CROSS_FIRM|IAM_POLICY_SPLIT|SERVICE_SPLIT|ENV_TWIN) -- findings are unaffected."""
    audit = SuppressionAudit()
    tf = scan_tf_names(audit)
    content = scan_content(audit, "lib/trading_calendar.py")
    hidden = audit.hidden
    if class_filter:
        cf = class_filter.upper()
        hidden = [h for h in hidden if cf in h["suppressor"].upper()]
    return {"tf_name_findings": tf, "content": content,
            "suppression_audit": hidden, "suppression_summary": audit.summary()}


def _print_human(res: dict) -> None:
    tf = res["tf_name_findings"]
    high = [f for f in tf if f["tier"] == "high"]
    info = [f for f in tf if f["tier"] == "info"]
    content = res["content"]
    print("=" * 78)
    print("comp-dups -- BM25 dup/dead-twin scanner (advisory; ranked; NEVER removes)")
    print("=" * 78)
    print(f"\n=== CLASS A-high: TF EXACT-label collisions across modules ({len(high)}) ===")
    print("    (the real twin/double-management signal -- each a possible two-states-one-resource)")
    for f in high:
        dead = f" dead={f['dead_status']}" if f["dead_status"] else ""
        print(f"  {f['verdict']:<18} {f['score']:<5} [EXACT] {f['a']} <{f['a_mod']}> ~ {f['b']} <{f['b_mod']}>{dead}")
    print(f"\n=== CLASS A-info: NAME-near siblings ({len(info)} total; top 12) ===")
    for f in info[:12]:
        print(f"  NAME_NEAR_INFO     {f['score']:<5} [near] {f['a']} ~ {f['b']}")
    print(f"\n=== CLASS C1: CONTENT exact-body dups ({content['corpus_size']} first-party py bodies) ===")
    for r in content["exact_dups"][:15]:
        print(f"  CONTENT_EXACT_DUP x{len(r['members'])} ({r['lines']}L) {r['distinct_names']}")
        for mp in r["members"][:6]:
            print(f"        {mp}")
    print("\n=== CLASS C2 DOGFOOD: content-neighbors of lib/trading_calendar.py ===")
    for d in content["dogfood"][:12]:
        print(f"  norm={d['norm']:<6} score={d['score']:<6} {d['path']}")
    print("\n=== SUPPRESSION AUDIT (no silent suppression) ===")
    print(f"  suppressed pairs (post-filter): {len(res['suppression_audit'])}")
    for sid, n in sorted(res["suppression_summary"].items(), key=lambda kv: -kv[1]):
        print(f"    {sid:<24} {n}")


def write_ledger(res: dict) -> tuple:
    """Write the dated dimension ledger + the standing latest-pointer to the debtscan home
    (D1-D5 dated+latest pattern). Called by --nightly (post-derive hook)."""
    home = Path(__file__).resolve().parent
    stamp = dt.date.today().isoformat()
    payload = {"dimension": "comp-dups", "generated_date": stamp, "advisory_only": True, **res}
    body = json.dumps(payload, indent=2)
    dated = home / f"{stamp}_DUPS_candidates.json"
    latest = home / "dups_latest.json"
    dated.write_text(body, encoding="utf-8")
    latest.write_text(body, encoding="utf-8")
    return dated, latest


def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(
        prog="comp-dups",
        description="BM25 dup/dead-twin scanner (NFRA_DEBTSCAN dups dimension). Advisory; NEVER removes.")
    ap.add_argument("--nightly", action="store_true",
                    help="post-derive: write dated ledger + dups_latest.json to the debtscan home")
    ap.add_argument("--json", action="store_true", help="emit the result as JSON")
    ap.add_argument("--class", dest="cls", default=None,
                    help="filter the suppression audit to a class (CROSS_FIRM|IAM_POLICY_SPLIT|SERVICE_SPLIT|ENV_TWIN)")
    ap.add_argument("--validate-dead", action="store_true",
                    help="run the dead-confirm fixture validation (opal-users v1/v2 over the metric window)")
    args = ap.parse_args(argv)

    if args.validate_dead:
        validate_dead_confirm()
        return 0

    res = run_scan(class_filter=args.cls)
    if args.nightly:
        dated, latest = write_ledger(res)
        high = sum(1 for f in res["tf_name_findings"] if f["tier"] == "high")
        print(f"comp-dups --nightly: wrote {dated.name} + {latest.name} -> {dated.parent}")
        print(f"  TF-high={high} | content-exact-dups={len(res['content']['exact_dups'])} | "
              f"suppressed={len(res['suppression_audit'])} (advisory; NEVER removes)")
        return 0
    if args.json:
        print(json.dumps(res, indent=2))
        return 0
    _print_human(res)
    return 0


if __name__ == "__main__":
    sys.exit(main())

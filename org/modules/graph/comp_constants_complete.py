"""comp_constants_complete -- the ENUMERATION-COMPLETENESS axis (bundle item 7 half B).

NFRA_PSTMRT: every expensive MDPF defect was a firm set compiled into N sites, each
internally consistent, uniformly incomplete -- ZERO DRIFT, CORRECTLY REPORTED, WRONG
AXIS. comp-constants detected disagreement between sites; nothing asserted a site's
CARDINALITY against the one registry. This module is that assertion.

Design pinned @d5ed44e2e; ~Z PRD s.2 semantics adopted verbatim (Phase-1 interface
msgs 223500Z/224107Z):
  - matching tokens = firm_id + tree_token + aliases[] from data/firm_registry.json,
    never a per-tool token list;
  - completeness is COMPLETE-OVER A DECLARED SCOPE (portal/mdpf/pipeline) -- the
    constant declares firm_keyed: {complete_over: <scope>}; asserting the full
    registry against everything false-fires on portal-only firms (CTO reproduced
    live on mockadv, 224631Z -- the scope filter is load-bearing, built in first);
  - a uniformly-incomplete set FAILS; an UNREGISTERED token FAILS equally loud;
  - the DENOMINATOR prints every run, with the registry vintage;
  - exemptions carry {firm, by, date, why, expires}; expired exemptions FAIL.

RF-6's lesson binds the MEASUREMENT SIDE: members come from SCANNED LIVE SITES (the
world), never from the config's canonical_value (a completeness signal whose
denominator is its own configuration is the whole postmortem). Python sites parse
via ast.literal_eval of the scanned value; .mjs/.ts sites (half A, polyglot) parse
via extract_ts_source.strip_comments + top-level object-literal KEY extraction --
so a commented-out firm entry does NOT count as present (the item-2 false-presence
control, applied here on day one).

Verdict vocabulary (census lesson -- FAIL must not mean five things):
  COMPLETE / INCOMPLETE / PHANTOM / EXEMPT / EXEMPT-EXPIRED / UNPARSEABLE-SITE.
Registry absent or unparseable = REFUSE (rc 3): 'could not check' is never 'clean'.
"""
from __future__ import annotations

import ast
import datetime as dt
import hashlib
import json
import re
from pathlib import Path


class RegistryRefusal(Exception):
    """The registry cannot be read honestly -- the check REFUSES, never no-ops."""


# ---------------------------------------------------------------- registry side

def load_registry(path: Path) -> dict:
    """Load + validate the firm registry. Fail-closed on absent/unparseable/empty.

    Returns {"firms": [...], "vintage": "<mtime-utc> sha=<12>", "path": str}.
    """
    if not path.exists():
        raise RegistryRefusal(f"registry ABSENT at {path} -- REFUSING (an ungated "
                              f"pass is not a pass)")
    raw = path.read_bytes()
    try:
        doc = json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as e:
        raise RegistryRefusal(f"registry UNPARSEABLE at {path}: {e}") from e
    firms = doc.get("firms")
    if not isinstance(firms, list) or not firms:
        raise RegistryRefusal(f"registry at {path} carries no firms[] -- REFUSING")
    mtime = dt.datetime.fromtimestamp(path.stat().st_mtime, dt.timezone.utc)
    vintage = "%s sha=%s" % (mtime.strftime("%Y-%m-%dT%H:%MZ"),
                             hashlib.sha256(raw).hexdigest()[:12])
    return {"firms": firms, "vintage": vintage, "path": str(path)}


def token_map(firms: list) -> dict:
    """token(lower) -> firm_id, over firm_id + tree_token + aliases[]. The ONE
    matching vocabulary (~Z s.2a) -- never a per-tool token list."""
    out: dict = {}
    for f in firms:
        fid = f.get("firm_id", "")
        for tok in [fid, f.get("tree_token", "")] + list(f.get("aliases", []) or []):
            if tok:
                out[str(tok).lower()] = fid
    return out


def expected_for_scope(firms: list, scope: str) -> set:
    """firm_ids the scope-declared structure MUST cover: enabled + scopes[scope]."""
    return {f["firm_id"] for f in firms
            if f.get("enabled") and (f.get("scopes") or {}).get(scope)}


# ---------------------------------------------------------------- member extraction

def members_from_python_value(value_repr: str):
    """Member token set from a scanned python site's value repr.
    dict -> keys; list/set/tuple -> elements. None = not a container we can read
    (UNPARSEABLE-SITE, said -- never a silent empty set)."""
    try:
        v = ast.literal_eval(value_repr)
    except (ValueError, SyntaxError, TypeError):
        return None
    if isinstance(v, dict):
        return {str(k) for k in v.keys()}
    if isinstance(v, (list, set, tuple, frozenset)):
        return {str(x) for x in v}
    return None


_JS_KEY_RX = re.compile(r"^\s*(?:'([^']+)'|\"([^\"]+)\"|([A-Za-z_$][\w$]*))\s*:",
                        re.MULTILINE)


def members_from_js_site(path: Path, const_name: str):
    """Top-level key set of `const NAME = {...}` / `export const NAME = {...}` in a
    COMMENT-STRIPPED .mjs/.ts file (half A, polyglot). Depth-1 keys only -- the
    unit firm-map completeness needs. None = site/const not found or brace scan
    failed (UNPARSEABLE-SITE, said)."""
    try:
        from .extract_ts_source import strip_comments
    except ImportError:
        from extract_ts_source import strip_comments
    try:
        src = strip_comments(path.read_text(encoding="utf-8", errors="replace"))
    except OSError:
        return None
    # Object.freeze({...}) is the live idiom at the acceptance target
    # (firm-config.mjs:29) -- the wrapper is transparent to the key set.
    m = re.search(r"(?:export\s+)?const\s+%s\s*(?::[^=]+)?=\s*(?:Object\.freeze\(\s*)?\{"
                  % re.escape(const_name), src)
    if not m:
        return None
    # brace-balance from the opening { (comment-stripped, strings may hold braces --
    # tolerate by tracking quotes minimally: stripper left strings verbatim)
    i = src.index("{", m.start())
    depth, j, in_str, q = 0, i, False, ""
    while j < len(src):
        c = src[j]
        if in_str:
            if c == "\\":
                j += 2
                continue
            if c == q:
                in_str = False
        elif c in "'\"`":
            in_str, q = True, c
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                break
        j += 1
    if depth != 0:
        return None
    body = src[i + 1:j]
    # depth-1 keys only: blank nested object bodies before key-scanning
    flat, d = [], 0
    for c in body:
        if c == "{":
            d += 1
            flat.append(c)
        elif c == "}":
            d -= 1
            flat.append(c)
        else:
            flat.append(c if d == 0 else " ")
    keys = set()
    for km in _JS_KEY_RX.finditer("".join(flat)):
        keys.add(next(g for g in km.groups() if g))
    return keys or None


# ---------------------------------------------------------------- the assertion

def check_completeness(config: dict, registry: dict, scanned_sites: dict,
                       workspace_root: Path, today: dt.date | None = None) -> dict:
    """Assert every firm_keyed-declared constant's LIVE members against the
    registry scope. Returns {"findings": [...], "denominator": str, "rc": int}.

    scanned_sites: {(name, lane): [Site,...]} from the caller's scan_all (python
    sites, THE WORLD). .mjs/.ts sites ride firm_keyed.sites[] declarations.
    """
    today = today or dt.date.today()
    firms = registry["firms"]
    tmap = token_map(firms)
    findings: list = []
    structures_checked = 0

    for c in config.get("constants", []):
        fk = c.get("firm_keyed")
        if not fk:
            continue
        name = c["name"]
        scope = fk.get("complete_over")
        if scope not in ("portal", "mdpf", "pipeline"):
            findings.append({"constant": name, "site": "(config)", "verdict": "UNPARSEABLE-SITE",
                             "detail": "firm_keyed.complete_over must be portal|mdpf|pipeline, "
                                       "got %r" % (scope,)})
            continue
        expected = expected_for_scope(firms, scope)
        exemptions = {str(e.get("firm", "")).lower(): e
                      for e in (fk.get("exemptions") or [])}

        # collect (site_label, member-set-or-None) over python sites + declared js/ts sites
        site_members: list = []
        for (n, _lane), sites in scanned_sites.items():
            if n != name:
                continue
            for s in sites:
                site_members.append((f"{s.file}:{s.line}",
                                     members_from_python_value(s.value)))
        for rel in fk.get("sites", []) or []:
            p = workspace_root / rel
            site_members.append((rel, members_from_js_site(p, name)))

        if not site_members:
            findings.append({"constant": name, "site": "(none)", "verdict": "UNPARSEABLE-SITE",
                             "detail": "declared firm_keyed but NO site yielded members -- "
                                       "not checked is not clean"})
            continue

        for label, members in site_members:
            structures_checked += 1
            if members is None:
                findings.append({"constant": name, "site": label, "verdict": "UNPARSEABLE-SITE",
                                 "detail": "site found but member set unreadable"})
                continue
            present_ids, phantoms = set(), []
            for tok in members:
                fid = tmap.get(str(tok).lower())
                if fid is None:
                    phantoms.append(tok)
                else:
                    present_ids.add(fid)
            if phantoms:
                findings.append({"constant": name, "site": label, "verdict": "PHANTOM",
                                 "detail": "unregistered firm token(s): %s -- not in the "
                                           "registry vocabulary" % sorted(phantoms)})
            missing = expected - present_ids
            really_missing = []
            for fid in sorted(missing):
                ex = exemptions.get(fid.lower())
                if ex:
                    try:
                        expires = dt.date.fromisoformat(str(ex.get("expires")))
                    except (TypeError, ValueError):
                        expires = None
                    if expires and expires >= today:
                        findings.append({"constant": name, "site": label, "verdict": "EXEMPT",
                                         "detail": "%s exempt until %s (by %s: %s)"
                                                   % (fid, ex.get("expires"), ex.get("by"),
                                                      ex.get("why"))})
                        continue
                    findings.append({"constant": name, "site": label,
                                     "verdict": "EXEMPT-EXPIRED",
                                     "detail": "%s exemption expired %s -- FAILS"
                                               % (fid, ex.get("expires"))})
                    really_missing.append(fid)
                    continue
                really_missing.append(fid)
            if really_missing:
                findings.append({"constant": name, "site": label, "verdict": "INCOMPLETE",
                                 "detail": "missing over scope=%s: %s"
                                           % (scope, sorted(really_missing))})
            elif not phantoms:
                findings.append({"constant": name, "site": label, "verdict": "COMPLETE",
                                 "detail": "covers all %d %s-scope firm(s)"
                                           % (len(expected), scope)})

    failing = [f for f in findings
               if f["verdict"] in ("INCOMPLETE", "PHANTOM", "EXEMPT-EXPIRED",
                                   "UNPARSEABLE-SITE")]
    denominator = ("checked %d firm-keyed structure-site(s) against the registry "
                   "(%d firm(s) total; registry vintage %s)"
                   % (structures_checked, len(firms), registry["vintage"]))
    return {"findings": findings, "denominator": denominator,
            "rc": 1 if failing else 0}

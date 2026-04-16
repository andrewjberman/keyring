#!/usr/bin/env python3
"""
validator.py -- Project-closure requirement validator.

Runs after operator.py has driven a project's task orders to `<status>complete</status>`.
Operator asks "what remains to be done?". Validator asks:
  - what was supposed to be true by the end of this project?
  - what evidence exists that it is true?
  - what evidence is missing?
  - where does completed work fail to satisfy original intent?
  - where do the PRD, TOs, outputs, and project state disagree?

MANDATORY for 2.0.0_SA_COO at the conclusion of operator-driven execution.
OPTIONAL for any agent responsible for long-running implementation, review,
synthesis, or delivery work on the project.

Premise (per Andrew 2026-04-16): validator does not stop until the project
is validated as complete against PRD intent + TO acceptance + deliverables.
On a fork, elevate to CTO; CTO resolves per historical patterns + best judgment.

Semantics:
  One invocation = one directive. Run at top of each validation turn.
  Exits when every requirement is VALIDATED with sufficient evidence (code 1)
  or when a fork blocks further validation (code 2).

A TO being marked complete is NOT equivalent to the work actually meeting
spec. The validator reasons at REQUIREMENT COVERAGE, not artifact presence.

Exit codes:
  0   continue -- validation work remains; directive emitted
  1   done -- every validation target is VALIDATED with sufficient evidence
  2   fork -- elevation body emitted; stop until CTO resolves
  3   error -- invalid invocation, malformed project code, or missing core records

Usage:
  validator.py <PROJECT_CODE>                 emit directive
  validator.py <PROJECT_CODE> --agent SERIAL  scope to one agent's validation
  validator.py <PROJECT_CODE> --render        write .tools/validator-<CODE> shim
  validator.py <PROJECT_CODE> --elevate       MCP-ready CTO elevation body
  validator.py <PROJECT_CODE> --json          machine-readable coverage report
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Windows cp1252 stdout corrupts non-ASCII. Force UTF-8 with replacement.
if isinstance(sys.stdout, io.TextIOBase):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass

REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = REPO_ROOT / "org" / "projects"
DOCS_ARCH = REPO_ROOT / "docs" / "architecture"
TIER_ROOTS = [
    REPO_ROOT / "org" / "tier1_exec",
    REPO_ROOT / "org" / "tier2_senior",
    REPO_ROOT / "org" / "tier3_junior",
]
TOOLS_DIR = REPO_ROOT / ".tools"

PROJECT_CODE_RE = re.compile(r"^[A-Z]{4}_[A-Z0-9]{6}$")
GIT_HASH_RE = re.compile(r"\b([0-9a-f]{7,40})\b")
PATH_CITE_RE = re.compile(
    r"`([a-zA-Z0-9_./\\\-]+\.(?:md|py|ts|tsx|json|sh|xml|yaml|yml|sql|parquet|tf))`"
)
STATUS_RE = re.compile(r"<status>\s*([A-Za-z_]+)\s*</status>")
ID_RE = re.compile(r"<id>\s*(.+?)\s*</id>", re.DOTALL)
ISSUED_TO_RE = re.compile(r"<issued_to>\s*(.+?)\s*</issued_to>", re.DOTALL)
AC_BLOCK_RE = re.compile(r"<acceptance_criteria>(.*?)</acceptance_criteria>", re.DOTALL)
EVIDENCE_BLOCK_RE = re.compile(r"<evidence>(.*?)</evidence>", re.DOTALL)
DELIVERABLES_BLOCK_RE = re.compile(r"<deliverables>(.*?)</deliverables>", re.DOTALL)
OBJECTIVE_BLOCK_RE = re.compile(r"<objective>(.*?)</objective>", re.DOTALL)
NUMBERED_ITEM_RE = re.compile(r"^\s*(?:\d+[.)]|[-*])\s+(.+?)$", re.MULTILINE)
PRD_SUCCESS_HEADERS = (
    "success criteria",
    "acceptance criteria",
    "acceptance",
    "project-level acceptance criteria",
    "terminal gate",
    "exit criteria",
    "completion criteria",
    "deliverables",
    "requirements",
)


def die(msg: str, code: int = 3) -> None:
    print(f"[VALIDATOR] {msg}", file=sys.stderr)
    sys.exit(code)


def validate_code(code: str) -> None:
    if not PROJECT_CODE_RE.match(code):
        die(f"project code '{code}' does not match {{MACRO}}_{{CODE}} (e.g. ADVI_ROLLUP)", code=3)


def load_project(code: str) -> dict:
    path = PROJECTS_DIR / f"{code}.json"
    if not path.exists():
        die(f"project {code} not found at {path}", code=3)
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        die(f"project {code} JSON invalid: {e}", code=3)


def load_prds(project: dict) -> list[dict]:
    """Load every PRD referenced in project JSON 'prds' array. Returns list of
    {path, label, text, missing: bool}."""
    prds: list[dict] = []
    for ref in project.get("prds", []) or []:
        rel = ref.get("path") if isinstance(ref, dict) else str(ref)
        label = ref.get("label", rel) if isinstance(ref, dict) else rel
        if not rel:
            continue
        p = REPO_ROOT / rel
        entry = {"path": rel, "label": label, "text": "", "missing": not p.exists()}
        if not entry["missing"]:
            try:
                entry["text"] = p.read_text(encoding="utf-8", errors="replace")
            except OSError as e:
                entry["missing"] = True
                entry["error"] = str(e)
        prds.append(entry)
    return prds


def scan_task_orders(code: str) -> list[dict]:
    results: list[dict] = []
    for tier_root in TIER_ROOTS:
        if not tier_root.exists():
            continue
        for agent_dir in sorted(tier_root.iterdir()):
            to_dir = agent_dir / "task_orders"
            if not to_dir.is_dir():
                continue
            for to_file in sorted(to_dir.glob(f"{code}.*.md")):
                results.append(parse_to(to_file, agent_dir.name))
    return results


def parse_to(path: Path, owning_agent: str) -> dict:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return {
            "file": str(path.relative_to(REPO_ROOT)),
            "owning_agent": owning_agent,
            "issued_to": owning_agent,
            "id": path.stem,
            "status": "unreadable",
            "ac_items": [],
            "evidence_text": "",
            "evidence_commits": [],
            "evidence_paths": [],
            "deliverables_text": "",
            "objective_text": "",
            "text": "",
            "error": str(e),
        }

    status_m = STATUS_RE.search(text)
    id_m = ID_RE.search(text)
    issued_m = ISSUED_TO_RE.search(text)
    ac_m = AC_BLOCK_RE.search(text)
    ev_m = EVIDENCE_BLOCK_RE.search(text)
    dv_m = DELIVERABLES_BLOCK_RE.search(text)
    obj_m = OBJECTIVE_BLOCK_RE.search(text)

    # AC items: numbered list inside <acceptance_criteria>, one target per item.
    ac_items: list[str] = []
    if ac_m:
        ac_text = ac_m.group(1)
        for match in NUMBERED_ITEM_RE.finditer(ac_text):
            item = match.group(1).strip()
            if item and len(item) > 8:  # skip trivial markers
                ac_items.append(item)
        if not ac_items:
            # Fallback: whole AC block as one target
            compact = " ".join(ac_text.split())
            if compact:
                ac_items.append(compact[:400])

    evidence_text = (ev_m.group(1).strip() if ev_m else "").strip()
    evidence_commits = sorted(set(GIT_HASH_RE.findall(evidence_text))) if evidence_text else []
    evidence_paths = sorted(set(PATH_CITE_RE.findall(evidence_text))) if evidence_text else []

    return {
        "file": str(path.relative_to(REPO_ROOT)),
        "owning_agent": owning_agent,
        "issued_to": (issued_m.group(1).strip() if issued_m else owning_agent).split()[0],
        "id": id_m.group(1).strip() if id_m else path.stem,
        "status": status_m.group(1).lower() if status_m else "unknown",
        "ac_items": ac_items,
        "evidence_text": evidence_text,
        "evidence_commits": evidence_commits,
        "evidence_paths": evidence_paths,
        "deliverables_text": dv_m.group(1).strip() if dv_m else "",
        "objective_text": obj_m.group(1).strip() if obj_m else "",
        "text": text,
    }


def extract_prd_targets(prd: dict) -> list[dict]:
    """Pull validation targets out of a PRD. Looks for numbered/bulleted items
    inside sections whose heading contains one of PRD_SUCCESS_HEADERS, and table
    rows in those sections."""
    if prd.get("missing") or not prd.get("text"):
        return []

    targets: list[dict] = []
    lines = prd["text"].splitlines()
    current_heading = ""
    in_target_section = False
    table_header_seen = False

    for line in lines:
        heading_m = re.match(r"^(#+)\s+(.*?)\s*$", line)
        if heading_m:
            current_heading = heading_m.group(2).strip()
            low = current_heading.lower()
            in_target_section = any(h in low for h in PRD_SUCCESS_HEADERS)
            table_header_seen = False
            continue

        if not in_target_section:
            continue

        # Bullet / numbered-item extraction
        item_m = NUMBERED_ITEM_RE.match(line)
        if item_m:
            item = item_m.group(1).strip()
            if item and len(item) > 8:
                targets.append({
                    "source": "prd",
                    "prd": prd["path"],
                    "section": current_heading,
                    "text": item,
                })
            continue

        # Table row extraction (pipe-delimited). Skip header + separator.
        if line.strip().startswith("|") and line.strip().endswith("|"):
            if not table_header_seen:
                # First pipe row in section is likely the header.
                table_header_seen = True
                continue
            if re.match(r"^\s*\|[\s\-|:]+\|\s*$", line):
                # Separator row
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            # Use last cell as the acceptance predicate (typical for PRD tables)
            predicate = cells[-1] if cells else ""
            if predicate and len(predicate) > 8 and not predicate.startswith("-"):
                label = " / ".join(c for c in cells[:-1] if c)[:80]
                text = f"[{label}] {predicate}" if label else predicate
                targets.append({
                    "source": "prd",
                    "prd": prd["path"],
                    "section": current_heading,
                    "text": text,
                })

    return targets


def extract_to_targets(tos: list[dict]) -> list[dict]:
    """Pull numbered AC items from every TO into the validation-target list."""
    targets: list[dict] = []
    for to in tos:
        for item in to["ac_items"]:
            targets.append({
                "source": "to",
                "to_id": to["id"],
                "to_file": to["file"],
                "to_status": to["status"],
                "text": item,
            })
    return targets


STOPWORDS = {
    "the", "a", "an", "is", "are", "was", "were", "be", "to", "of", "and",
    "or", "for", "on", "in", "at", "by", "with", "from", "that", "this",
    "these", "those", "as", "if", "it", "its", "but", "not", "all", "each",
    "per", "via", "within", "into", "then", "than", "so", "no", "yes",
}


def _tokens(text: str) -> set[str]:
    words = re.findall(r"[A-Za-z0-9_]+", text.lower())
    return {w for w in words if len(w) > 3 and w not in STOPWORDS}


def _score_match(target_text: str, evidence_text: str) -> float:
    """Jaccard-ish overlap in [0, 1]."""
    t = _tokens(target_text)
    e = _tokens(evidence_text)
    if not t:
        return 0.0
    if not e:
        return 0.0
    inter = t & e
    union = t | e
    return len(inter) / max(1, len(union))


def _is_repo_path(rel: str) -> bool:
    """True if this string looks like a repo-relative path worth checking.
    False for S3 keys, bucket paths, URLs, or clearly external artifacts."""
    if not rel:
        return False
    lowered = rel.lower()
    if "://" in lowered:
        return False
    if lowered.startswith(("s3/", "s3:", "opal-data-bd/", "opal-")):
        return False
    # Must have at least one path separator to be a real file reference.
    return "/" in rel or "\\" in rel


def _path_exists(rel: str) -> bool:
    if not _is_repo_path(rel):
        return True  # External artifact; treat as present (not our job to verify S3/URLs).
    p = REPO_ROOT / rel.replace("\\", "/")
    return p.exists()


def _gather_evidence_corpus(tos: list[dict]) -> str:
    """Concatenate every TO's evidence block + objective for keyword matching."""
    chunks = []
    for to in tos:
        if to["evidence_text"]:
            chunks.append(to["evidence_text"])
        if to["objective_text"]:
            chunks.append(to["objective_text"])
    return " \n ".join(chunks)


def map_evidence(target: dict, tos: list[dict], corpus: str) -> dict:
    """Return evidence record for a target."""
    best_to = None
    best_score = 0.0

    for to in tos:
        hay = " ".join([
            to["id"],
            to["evidence_text"],
            to["objective_text"],
            " ".join(to["ac_items"]),
        ])
        score = _score_match(target["text"], hay)
        if score > best_score:
            best_score = score
            best_to = to

    corpus_score = _score_match(target["text"], corpus)

    commits: list[str] = []
    artifact_paths: list[str] = []
    artifact_missing: list[str] = []
    external_refs: list[str] = []
    to_status = None
    if best_to:
        to_status = best_to["status"]
        commits = list(best_to["evidence_commits"])
        for p in best_to["evidence_paths"]:
            if not _is_repo_path(p):
                external_refs.append(p)
            elif _path_exists(p):
                artifact_paths.append(p)
            else:
                artifact_missing.append(p)

    return {
        "best_to_id": best_to["id"] if best_to else None,
        "best_to_file": best_to["file"] if best_to else None,
        "best_to_status": to_status,
        "best_score": round(best_score, 3),
        "corpus_score": round(corpus_score, 3),
        "evidence_commits": commits,
        "artifact_paths_present": artifact_paths,
        "artifact_paths_missing": artifact_missing,
        "external_refs": external_refs,
    }


def classify_target(target: dict, ev: dict) -> str:
    """Bucket each target into one of: validated | partial | insufficient_evidence
    | unvalidated | contradicted | blocked | unknown."""
    to_status = ev["best_to_status"]
    score = ev["best_score"]
    has_commit = bool(ev["evidence_commits"])
    has_artifact = bool(ev["artifact_paths_present"])
    missing_artifacts = bool(ev["artifact_paths_missing"])

    if missing_artifacts and not has_artifact:
        return "blocked"

    has_external = bool(ev.get("external_refs"))
    # Strong match + complete TO + evidence commit or artifact (local or external S3) = validated
    if score >= 0.25 and to_status == "complete" and (has_commit or has_artifact or has_external):
        return "validated"

    # Matches a complete TO but no hard evidence citation -> insufficient
    if score >= 0.2 and to_status == "complete" and not (has_commit or has_artifact):
        return "insufficient_evidence"

    # Matches a TO that's still pending/staged/blocked -> partial
    if score >= 0.2 and to_status in {"pending", "staged", "blocked", "hold"}:
        return "partial"

    # Very weak signal overall
    if score < 0.1 and ev["corpus_score"] < 0.15:
        return "unvalidated"

    # Weak-but-nonzero signal -> insufficient_evidence (could be real, proof weak)
    if score < 0.2:
        return "insufficient_evidence"

    # Default
    return "unknown"


def build_coverage(
    targets: list[dict],
    tos: list[dict],
) -> tuple[list[dict], dict[str, list[dict]]]:
    """Evidence-map every target; return enriched-targets + buckets dict."""
    corpus = _gather_evidence_corpus(tos)
    enriched: list[dict] = []
    buckets: dict[str, list[dict]] = {
        "validated": [],
        "partial": [],
        "insufficient_evidence": [],
        "unvalidated": [],
        "contradicted": [],  # populated only by fork path
        "blocked": [],
        "unknown": [],
    }
    for t in targets:
        ev = map_evidence(t, tos, corpus)
        cls = classify_target(t, ev)
        rec = {**t, "evidence": ev, "classification": cls}
        enriched.append(rec)
        buckets[cls].append(rec)
    return enriched, buckets


def detect_forks(
    project: dict,
    prds: list[dict],
    tos: list[dict],
    targets: list[dict],
    buckets: dict[str, list[dict]],
) -> list[dict]:
    forks: list[dict] = []

    missing_prds = [p for p in prds if p.get("missing")]
    if not prds or (missing_prds and len(missing_prds) == len(prds)):
        forks.append({
            "kind": "PRD_MISSING",
            "detail": [p["path"] for p in missing_prds] or "No PRDs listed in project JSON",
            "suggest": "Project JSON `prds` array empty or all referenced PRD files missing. Cannot reason about requirements without governing documents.",
        })

    if not targets:
        forks.append({
            "kind": "NO_VALIDATION_TARGETS_EXTRACTED",
            "detail": f"Scanned {len(prds)} PRD(s) + {len(tos)} TO(s); extracted zero acceptance items.",
            "suggest": "Either PRDs lack a Success/Acceptance section with bullets/tables, TOs lack <acceptance_criteria>, or parser heuristics miss this project's idioms. Manual spot-check required before validator can proceed.",
        })

    complete_tos_no_evidence = [
        t for t in tos
        if t["status"] == "complete" and not t["evidence_text"] and not t["evidence_commits"]
    ]
    if complete_tos_no_evidence:
        forks.append({
            "kind": "COMPLETED_WORK_WITHOUT_EVIDENCE",
            "detail": [t["file"] for t in complete_tos_no_evidence[:10]],
            "suggest": "TOs marked complete with no <evidence> block, no commit hash in status comment, and no cited artifacts. Flip to insufficient_evidence OR add evidence block.",
        })

    # ALL_EVIDENCE_WEAK: >= 50% of targets are insufficient_evidence
    total_targets = sum(len(v) for v in buckets.values())
    weak = len(buckets["insufficient_evidence"])
    if total_targets >= 10 and weak / max(1, total_targets) >= 0.5:
        forks.append({
            "kind": "ALL_EVIDENCE_WEAK",
            "detail": f"{weak}/{total_targets} targets classified insufficient_evidence",
            "suggest": "Evidence citation discipline is systemically weak. Either agents omit <evidence> blocks or PRD targets don't map cleanly to TO scopes. Review decomposition quality.",
        })

    blocked_targets = buckets["blocked"]
    if blocked_targets:
        missing_arts = []
        for t in blocked_targets:
            missing_arts.extend(t["evidence"]["artifact_paths_missing"])
        forks.append({
            "kind": "VALIDATION_DEPENDENCY_MISSING",
            "detail": sorted(set(missing_arts))[:20],
            "suggest": "Cited artifacts don't exist on disk. Either path drifted, file never produced, or evidence referenced a scratch location. Locate artifact or reopen producing TO.",
        })

    # PROJECT_MARKED_COMPLETE_BUT_REQUIREMENTS_UNMET
    if project.get("status") == "complete" and (
        buckets["unvalidated"] or buckets["partial"] or buckets["insufficient_evidence"]
    ):
        forks.append({
            "kind": "PROJECT_MARKED_COMPLETE_BUT_REQUIREMENTS_UNMET",
            "detail": {
                "unvalidated": [t["text"][:120] for t in buckets["unvalidated"][:5]],
                "partial": [t["text"][:120] for t in buckets["partial"][:5]],
                "insufficient_evidence": [t["text"][:120] for t in buckets["insufficient_evidence"][:5]],
            },
            "suggest": "Project JSON declares complete but unvalidated / partial / weakly-evidenced requirements remain. Reopen project OR flip target evidence OR document acceptance flex on each remaining target.",
        })

    # AMBIGUOUS_REQUIREMENT_INTERPRETATION: target maps to >1 TOs with near-equal scores.
    # (Lightweight proxy: flag targets where corpus_score - best_score < 0.02 and corpus_score > 0.1.)
    ambiguous = [
        t for t in targets
        if t.get("classification") in {"partial", "insufficient_evidence", "unknown"}
        and t["evidence"]["corpus_score"] - t["evidence"]["best_score"] < 0.03
        and t["evidence"]["corpus_score"] > 0.1
    ]
    if len(ambiguous) >= 3:
        forks.append({
            "kind": "AMBIGUOUS_REQUIREMENT_INTERPRETATION",
            "detail": [t["text"][:120] for t in ambiguous[:5]],
            "suggest": "Multiple TOs plausibly cover the same requirement with similar keyword overlap. Clarify which TO owns which acceptance item.",
        })

    return forks


def recommend_actions(
    buckets: dict[str, list[dict]], forks: list[dict], project_code: str
) -> list[str]:
    actions: list[str] = []
    if forks:
        actions.append(
            f"FORK present -- run `validator.py {project_code} --elevate` to compose CTO MCP body, then send_message."
        )
    if buckets["blocked"]:
        actions.append(
            f"BLOCKED targets ({len(buckets['blocked'])}): locate missing artifacts or reopen producing TO."
        )
    if buckets["unvalidated"]:
        actions.append(
            f"UNVALIDATED targets ({len(buckets['unvalidated'])}): author a new TO or evidence sweep to cover each, or flip to accept-as-out-of-scope with CTO sign-off."
        )
    if buckets["insufficient_evidence"]:
        actions.append(
            f"INSUFFICIENT_EVIDENCE targets ({len(buckets['insufficient_evidence'])}): amend matching TO's <evidence> block with commit hash / artifact path / validator run output."
        )
    if buckets["partial"]:
        actions.append(
            f"PARTIAL targets ({len(buckets['partial'])}): finish the matching pending/staged TOs (they already cover the requirement)."
        )
    if buckets["unknown"]:
        actions.append(
            f"UNKNOWN targets ({len(buckets['unknown'])}): manually spot-check; parser could not classify confidently."
        )
    if not actions:
        actions.append("All validation targets VALIDATED with sufficient evidence -- project is truly complete.")
    return actions


def emit_directive(
    code: str,
    project: dict,
    prds: list[dict],
    tos: list[dict],
    targets: list[dict],
    buckets: dict[str, list[dict]],
    forks: list[dict],
    agent_filter: str | None,
) -> int:
    total = sum(len(v) for v in buckets.values())
    validated = len(buckets["validated"])
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    print(f"# VALIDATOR DIRECTIVE -- {code}")
    print(f"Generated: {now}")
    print(f"PRDs:      {len(prds)} referenced, {sum(1 for p in prds if p.get('missing'))} missing")
    print(f"TOs:       {len(tos)} total ({sum(1 for t in tos if t['status']=='complete')} complete)")
    print(f"Coverage:  {validated}/{total} validation targets VALIDATED")
    phase = (project.get("phase") or "").strip()
    if phase:
        print(f"Phase:     {phase[:160]}")
    if agent_filter:
        print(f"Scoped to: {agent_filter}")
    print()

    if forks:
        print("## FORKS -- elevate to CTO")
        for f in forks:
            print(f"- **{f['kind']}**")
            detail = f["detail"]
            if isinstance(detail, (list, dict)):
                pretty = json.dumps(detail, indent=2)
                for line in pretty.splitlines()[:12]:
                    print(f"    {line}")
            else:
                print(f"    detail: {detail}")
            print(f"    suggest: {f['suggest']}")
        print()

    for bucket_name in ("unvalidated", "partial", "insufficient_evidence", "blocked", "contradicted", "unknown"):
        items = _filter_by_agent(buckets[bucket_name], agent_filter, tos)
        if not items:
            continue
        print(f"## {bucket_name.upper()} ({len(items)})")
        for t in items[:15]:
            src = t["source"].upper()
            tag = f"[{src}:{t.get('to_id') or t.get('section','')[:40]}]"
            preview = t["text"][:140]
            print(f"- {tag} {preview}")
            ev = t["evidence"]
            ev_bits = []
            if ev["best_to_id"]:
                ev_bits.append(f"to={ev['best_to_id']} status={ev['best_to_status']} score={ev['best_score']}")
            if ev["evidence_commits"]:
                ev_bits.append(f"commits={','.join(ev['evidence_commits'][:3])}")
            if ev["artifact_paths_present"]:
                ev_bits.append(f"artifacts_ok={len(ev['artifact_paths_present'])}")
            if ev["artifact_paths_missing"]:
                ev_bits.append(f"artifacts_missing={ev['artifact_paths_missing']}")
            if ev_bits:
                print(f"    evidence: {' | '.join(ev_bits)}")
        if len(items) > 15:
            print(f"    ... and {len(items) - 15} more (use --json for full list)")
        print()

    actions = recommend_actions(buckets, forks, code)
    print("## RECOMMENDED ACTIONS")
    for i, a in enumerate(actions, 1):
        print(f"  {i}. {a}")
    print()

    # Exit code logic
    if forks:
        return 2
    if total == 0:
        return 2  # NO_VALIDATION_TARGETS_EXTRACTED fork should have fired; belt+suspenders.
    non_validated = total - validated
    if non_validated == 0:
        print("## STATE: PROJECT VALIDATED")
        print(f"All {total} validation targets have sufficient evidence. Project {code} is truly complete.")
        print("ACTION: update project JSON status to 'complete' if not already; move registry row to Completed; stop validator.")
        return 1
    print("ACTION: work the directive bucket-by-bucket. Do not stop. Re-run validator at top of next turn.")
    return 0


def _filter_by_agent(items: list[dict], agent: str | None, tos: list[dict]) -> list[dict]:
    if not agent:
        return items
    # Map TO ID -> issued_to so we can filter to_id-sourced items.
    id_to_agent = {t["id"]: t["issued_to"] for t in tos}
    out: list[dict] = []
    for t in items:
        to_id = t.get("to_id") or t.get("evidence", {}).get("best_to_id")
        owner = id_to_agent.get(to_id, "")
        if agent in owner:
            out.append(t)
    return out


def compose_elevation(
    code: str,
    project: dict,
    tos: list[dict],
    targets: list[dict],
    buckets: dict[str, list[dict]],
    forks: list[dict],
    agent: str | None,
) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    sender = agent or "2.0.0_SA_COO"

    if not forks:
        total = sum(len(v) for v in buckets.values())
        validated = len(buckets["validated"])
        print(f"[VALIDATOR] no forks detected on {code} -- elevation not required.")
        print(f"            Coverage: {validated}/{total} targets validated.")
        if total - validated > 0:
            print(f"            ACTION: work remaining buckets; re-run `validator {code}` for directive.")
        return

    subject = f"VALIDATOR ELEVATION -- {code}"
    body_lines = [
        f"Validator fork elevation generated {now} UTC.",
        "",
        f"Project phase: {(project.get('phase') or '').strip()[:240]}",
        "",
        "## Forks detected",
    ]
    for f in forks:
        body_lines.append(f"- **{f['kind']}**: {f['suggest']}")
        detail = f["detail"]
        if isinstance(detail, (list, dict)):
            body_lines.append("  ```")
            body_lines.append(json.dumps(detail, indent=2))
            body_lines.append("  ```")
        else:
            body_lines.append(f"  detail: {detail}")
    body_lines += [
        "",
        "## Coverage summary",
        f"- validated:             {len(buckets['validated'])}",
        f"- partial:               {len(buckets['partial'])}",
        f"- insufficient_evidence: {len(buckets['insufficient_evidence'])}",
        f"- unvalidated:           {len(buckets['unvalidated'])}",
        f"- contradicted:          {len(buckets['contradicted'])}",
        f"- blocked:               {len(buckets['blocked'])}",
        f"- unknown:               {len(buckets['unknown'])}",
        "",
        f"Requesting resolution per historical patterns + best judgment.",
        f"Validator is HALTED on {code} until your directive lands.",
    ]
    body = "\n".join(body_lines)

    print("## MCP-ready elevation -- paste into send_message")
    print(f"   from_agent: {sender}")
    print(f"   to_agent:   1.0.0_SA_CTO")
    print(f"   subject:    {subject}")
    print(f"   body:")
    for line in body.splitlines():
        print(f"     {line}")


def render_shim(code: str, agent: str | None) -> None:
    TOOLS_DIR.mkdir(parents=True, exist_ok=True)
    out = TOOLS_DIR / f"validator-{code}"
    agent_arg = f'--agent "{agent}" ' if agent else ""
    script = f"""#!/bin/bash
# validator-{code} -- project validator shim (rendered by validator.py)
# Validates {code} against PRD + TO intent. MANDATORY for 2.0.0_SA_COO
# at project closure. Optional for other agents managing synthesis/delivery.
#
# Usage: validator-{code} [--agent SERIAL] [--elevate|--json|--render]
#
# Exit codes:
#   0  continue (validation work remains)
#   1  done (all targets validated with sufficient evidence)
#   2  fork (elevate to CTO)
#   3  error

WORKSPACE="$(cd "$(dirname "$0")/.." && pwd)"
exec python "$WORKSPACE/.tools/validator.py" "{code}" {agent_arg}"$@"
"""
    out.write_text(script, encoding="utf-8")
    try:
        out.chmod(0o755)
    except OSError:
        pass
    print(f"[VALIDATOR] rendered {out.relative_to(REPO_ROOT)}")


def emit_json(
    code: str,
    project: dict,
    prds: list[dict],
    tos: list[dict],
    targets: list[dict],
    buckets: dict[str, list[dict]],
    forks: list[dict],
) -> None:
    payload = {
        "project_code": code,
        "phase": project.get("phase", ""),
        "status": project.get("status", ""),
        "prds": [{"path": p["path"], "missing": p.get("missing", False)} for p in prds],
        "to_count": len(tos),
        "validation_targets": [
            {k: v for k, v in t.items() if k != "evidence"} for t in targets
        ],
        "evidence_map": [
            {
                "target_text": t["text"][:200],
                "source": t["source"],
                "classification": t.get("classification"),
                "evidence": t.get("evidence", {}),
            }
            for t in targets
        ],
        "coverage_summary": {k: len(v) for k, v in buckets.items()},
        "validated": [t["text"][:200] for t in buckets["validated"]],
        "partial": [t["text"][:200] for t in buckets["partial"]],
        "insufficient_evidence": [t["text"][:200] for t in buckets["insufficient_evidence"]],
        "unvalidated": [t["text"][:200] for t in buckets["unvalidated"]],
        "contradicted": [t["text"][:200] for t in buckets["contradicted"]],
        "blocked": [t["text"][:200] for t in buckets["blocked"]],
        "unknown": [t["text"][:200] for t in buckets["unknown"]],
        "forks": forks,
        "recommended_actions": recommend_actions(buckets, forks, code),
    }
    print(json.dumps(payload, indent=2))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("project_code")
    ap.add_argument("--agent", default=None, help="Filter directive to a specific agent serial.")
    ap.add_argument("--render", action="store_true", help="Render .tools/validator-<PROJECT> shim.")
    ap.add_argument("--elevate", action="store_true", help="Compose MCP-ready CTO elevation body.")
    ap.add_argument("--json", action="store_true", help="Emit machine-readable coverage report.")
    args = ap.parse_args()

    validate_code(args.project_code)
    project = load_project(args.project_code)
    prds = load_prds(project)
    tos = scan_task_orders(args.project_code)

    prd_targets = []
    for prd in prds:
        prd_targets.extend(extract_prd_targets(prd))
    to_targets = extract_to_targets(tos)
    raw_targets = prd_targets + to_targets

    enriched_targets, buckets = build_coverage(raw_targets, tos)
    forks = detect_forks(project, prds, tos, enriched_targets, buckets)

    if args.render:
        render_shim(args.project_code, args.agent)
        return
    if args.elevate:
        compose_elevation(
            args.project_code, project, tos, enriched_targets, buckets, forks, args.agent
        )
        return
    if args.json:
        emit_json(args.project_code, project, prds, tos, enriched_targets, buckets, forks)
        return

    sys.exit(
        emit_directive(
            args.project_code, project, prds, tos, enriched_targets, buckets, forks, args.agent
        )
    )


if __name__ == "__main__":
    main()

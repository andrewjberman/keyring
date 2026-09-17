"""Reprice this box's Claude Code session transcripts at Anthropic API list prices.

Reads every *.jsonl under the Claude Code projects directory, keeps one usage record per
(message.id, requestId) -- Claude Code writes the same usage once per content block, so a
naive sum double-counts -- and prices each token class:

    input          x base input rate
    cache write 5m x base input rate x 1.25
    cache write 1h x base input rate x 2.00
    cache read     x the model's cache-read rate
    output         x base output rate

Prices: the in-environment Claude API reference (claude-api skill, model table cached
2026-06-24; caching economics in shared/prompt-caching.md). Fable 5.1 cache reads are $0.25/MTok.

Attribution: a session id maps to a seat serial through org/mcp/sessions/<id>.serial. A
subagent transcript (<session>/subagents/agent-*.jsonl) is charged to its parent session.

Writes one JSON summary; prints the tables the report quotes. Read-only over the transcripts.
"""

import argparse
import collections
import datetime
import json
import os
import subprocess
import sys

# USD per million tokens: (input, output, cache_read). Writes derive from input.
PRICES = {
    "claude-fable-5-1": (10.00, 50.00, 0.25),
    "claude-fable-5": (10.00, 50.00, 1.00),
    "claude-opus-5": (5.00, 25.00, 0.50),
    "claude-opus-4-8": (5.00, 25.00, 0.50),
    "claude-sonnet-5": (2.00, 10.00, 0.20),
    "claude-haiku-4-5": (1.00, 5.00, 0.10),
}
WRITE_5M = 1.25
WRITE_1H = 2.00
PER = 1_000_000.0


def normalize_model(raw):
    """Map a recorded model id onto a PRICES key, or return None."""
    if not raw:
        return None
    m = raw.lower()
    for key in sorted(PRICES, key=len, reverse=True):
        if m.startswith(key):
            return key
    return None


def load_serial_map(sessions_dir):
    out = {}
    if not os.path.isdir(sessions_dir):
        return out
    for name in os.listdir(sessions_dir):
        if name.endswith(".serial"):
            sid = name[: -len(".serial")]
            try:
                with open(os.path.join(sessions_dir, name), encoding="utf-8") as fh:
                    out[sid] = fh.read().strip()
            except OSError:
                continue
    return out


def iter_transcripts(root):
    for dirpath, _dirnames, filenames in os.walk(root):
        for fn in filenames:
            if fn.endswith(".jsonl"):
                yield os.path.join(dirpath, fn)


def parent_session(path, root):
    """The top-level session id a transcript belongs to."""
    rel = os.path.relpath(path, root).replace("\\", "/")
    first = rel.split("/")[0]
    if first.endswith(".jsonl"):
        first = first[: -len(".jsonl")]
    return first


def collect(root):
    """One record per (message.id, requestId), keeping the line with the most output tokens."""
    best = {}
    lines = 0
    usage_lines = 0
    bad = 0
    for path in iter_transcripts(root):
        psid = parent_session(path, root)
        is_sub = "/subagents/" in path.replace("\\", "/")
        with open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                lines += 1
                try:
                    obj = json.loads(line)
                except ValueError:
                    bad += 1
                    continue
                msg = obj.get("message")
                if not isinstance(msg, dict) or not isinstance(msg.get("usage"), dict):
                    continue
                usage_lines += 1
                key = (msg.get("id"), obj.get("requestId"), psid)
                u = msg["usage"]
                rec = {
                    "ts": obj.get("timestamp"),
                    "model_raw": msg.get("model"),
                    "session": psid,
                    "subagent": bool(is_sub or obj.get("isSidechain")),
                    "effort": obj.get("effort"),
                    "input": int(u.get("input_tokens") or 0),
                    "cache_create": int(u.get("cache_creation_input_tokens") or 0),
                    "cc_5m": None,
                    "cc_1h": None,
                    "cache_read": int(u.get("cache_read_input_tokens") or 0),
                    "output": int(u.get("output_tokens") or 0),
                    "geo": u.get("inference_geo"),
                    "tier": u.get("service_tier"),
                }
                cc = u.get("cache_creation")
                if isinstance(cc, dict):
                    rec["cc_5m"] = int(cc.get("ephemeral_5m_input_tokens") or 0)
                    rec["cc_1h"] = int(cc.get("ephemeral_1h_input_tokens") or 0)
                prev = best.get(key)
                if prev is None or rec["output"] > prev["output"]:
                    best[key] = rec
    return list(best.values()), {"lines": lines, "usage_lines": usage_lines, "unparseable_lines": bad}


def price(rec):
    """Return dict of USD by token class, or None if the model is unpriced."""
    key = normalize_model(rec["model_raw"])
    if key is None:
        return None
    p_in, p_out, p_read = PRICES[key]
    if rec["cc_5m"] is None and rec["cc_1h"] is None:
        w5, w1 = rec["cache_create"], 0
    else:
        w5, w1 = rec["cc_5m"] or 0, rec["cc_1h"] or 0
    return {
        "input": rec["input"] * p_in / PER,
        "cache_write_5m": w5 * p_in * WRITE_5M / PER,
        "cache_write_1h": w1 * p_in * WRITE_1H / PER,
        "cache_read": rec["cache_read"] * p_read / PER,
        "output": rec["output"] * p_out / PER,
    }


def git_commits(repo, since_iso, until_iso):
    fmt = "%H%x09%an%x09%aI"
    try:
        out = subprocess.run(
            ["git", "-C", repo, "log", "--all", "--no-merges", "--since=" + since_iso,
             "--until=" + until_iso, "--format=" + fmt],
            capture_output=True, timeout=300,
        )
    except (OSError, subprocess.SubprocessError):
        return []
    rows = []
    seen = set()
    for line in out.stdout.decode("utf-8", errors="replace").splitlines():
        parts = line.split("\t")
        if len(parts) == 3 and parts[0] not in seen:
            seen.add(parts[0])
            rows.append({"sha": parts[0], "author": parts[1], "date": parts[2]})
    return rows


def site_projects(repo, fabric="site-z"):
    """Tree project codes whose project.json names this fabric."""
    out = set()
    missions = os.path.join(repo, "org", "missions")
    for dirpath, _dirnames, filenames in os.walk(missions):
        if "project.json" in filenames:
            try:
                with open(os.path.join(dirpath, "project.json"), encoding="utf-8") as fh:
                    if json.load(fh).get("fabric") == fabric:
                        out.add(os.path.basename(dirpath))
            except (OSError, ValueError):
                continue
    return out


def box_author(author, box_serials, projects):
    """True for a commit this box's sessions produced.

    Lane serials (with a '~') recorded in this box's session map, the terminal seat, and worker
    subagents of site-Z projects. Base serials are excluded: the laptop fabric authors under them.
    """
    if author.startswith("0.9.0_WK_"):
        code = author[len("0.9.0_WK_"):].split("~")[0]
        return code in projects
    if author == "0.0.3_BG_BBGTerminal":
        return True
    return "~" in author and author in box_serials


def completed_orders(repo, since_iso, until_iso, projects):
    """Task-order files on site-Z projects whose diff added a complete status inside the window."""
    paths = []
    missions = os.path.join(repo, "org", "missions")
    for dirpath, dirnames, _filenames in os.walk(missions):
        if os.path.basename(dirpath) in projects and "task-orders" in dirnames:
            paths.append(os.path.relpath(os.path.join(dirpath, "task-orders"), repo))
    if not paths:
        return 0, []
    try:
        out = subprocess.run(
            ["git", "-C", repo, "log", "--no-merges", "--since=" + since_iso, "--until=" + until_iso,
             "-G", "<status>complete</status>", "-p", "--format=COMMIT %H", "--"] + paths,
            capture_output=True, timeout=600,
        )
    except (OSError, subprocess.SubprocessError):
        return 0, []
    done = set()
    current = None
    for line in out.stdout.decode("utf-8", errors="replace").splitlines():
        if line.startswith("+++ b/"):
            current = line[len("+++ b/"):]
        elif line.startswith("+") and "<status>complete</status>" in line and current:
            done.add(current)
    return len(done), sorted(done)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--projects", required=True, help="Claude Code projects dir for this workspace")
    ap.add_argument("--sessions", required=True, help="org/mcp/sessions")
    ap.add_argument("--repo", required=True, help="workspace repo root")
    ap.add_argument("--out", required=True, help="JSON summary path")
    args = ap.parse_args()

    records, counts = collect(args.projects)
    serials = load_serial_map(args.sessions)

    totals = collections.Counter()
    tokens = collections.Counter()
    by_model = collections.defaultdict(collections.Counter)
    by_day = collections.defaultdict(collections.Counter)
    by_serial = collections.defaultdict(collections.Counter)
    by_effort = collections.Counter()
    sub_cost = collections.Counter()
    geo = collections.Counter()
    tier = collections.Counter()
    unpriced = collections.Counter()
    no_split = 0
    ts_all = []

    for rec in records:
        cost = price(rec)
        if cost is None:
            unpriced[str(rec["model_raw"])] += 1
            continue
        if rec["cc_5m"] is None and rec["cc_1h"] is None and rec["cache_create"]:
            no_split += 1
        usd = sum(cost.values())
        key = normalize_model(rec["model_raw"])
        day = (rec["ts"] or "")[:10]
        serial = serials.get(rec["session"], "UNMAPPED")
        if rec["ts"]:
            ts_all.append(rec["ts"])
        for k, v in cost.items():
            totals[k] += v
            by_model[key][k] += v
        by_model[key]["usd"] += usd
        by_model[key]["responses"] += 1
        for k in ("input", "cache_create", "cache_read", "output"):
            tokens[k] += rec[k]
            by_model[key]["tok_" + k] += rec[k]
        tokens["cc_1h"] += rec["cc_1h"] or 0
        tokens["cc_5m"] += rec["cc_5m"] or 0
        by_day[day]["usd"] += usd
        by_day[day]["responses"] += 1
        by_serial[serial]["usd"] += usd
        by_serial[serial]["responses"] += 1
        by_effort[str(rec["effort"])] += usd
        sub_cost["subagent" if rec["subagent"] else "main"] += usd
        geo[str(rec["geo"])] += 1
        tier[str(rec["tier"])] += 1

    total_usd = sum(totals.values())
    ts_all.sort()
    first, last = (ts_all[0], ts_all[-1]) if ts_all else (None, None)
    commits = git_commits(args.repo, first, last) if first else []
    box_serials = set(serials.values())
    projects = site_projects(args.repo)
    box_commits = [c for c in commits if box_author(c["author"], box_serials, projects)]
    worker_commits = [c for c in box_commits if c["author"].startswith("0.9.0_WK_")]
    orders_done, order_files = completed_orders(args.repo, first, last, projects) if first else (0, [])

    summary = {
        "generated_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "window": {"first_usage": first, "last_usage": last, "days_with_usage": len([d for d in by_day if d])},
        "input_counts": counts,
        "responses_priced": sum(v["responses"] for v in by_model.values()),
        "responses_unpriced_by_model": dict(unpriced),
        "responses_without_ttl_split": no_split,
        "usd_total": round(total_usd, 2),
        "usd_by_class": {k: round(v, 2) for k, v in totals.items()},
        "tokens": dict(tokens),
        "by_model": {m: {k: (round(v, 2) if isinstance(v, float) else v) for k, v in c.items()} for m, c in by_model.items()},
        "by_day": {d: {"usd": round(c["usd"], 2), "responses": c["responses"]} for d, c in sorted(by_day.items())},
        "by_serial": {s: {"usd": round(c["usd"], 2), "responses": c["responses"]}
                      for s, c in sorted(by_serial.items(), key=lambda kv: -kv[1]["usd"])},
        "usd_by_effort": {k: round(v, 2) for k, v in by_effort.items()},
        "usd_main_vs_subagent": {k: round(v, 2) for k, v in sub_cost.items()},
        "inference_geo_values": dict(geo),
        "service_tier_values": dict(tier),
        "commits": {"all_branches_in_window": len(commits), "box_authored": len(box_commits),
                    "box_worker_authored": len(worker_commits), "box_serials_known": len(box_serials),
                    "site_z_projects": sorted(projects)},
        "task_orders_completed_site_z": {"count": orders_done, "files": order_files},
        "per_output_usd": {
            "per_box_commit": round(total_usd / len(box_commits), 2) if box_commits else None,
            "per_completed_task_order": round(total_usd / orders_done, 2) if orders_done else None,
            "per_active_day": round(total_usd / max(1, len([d for d in by_day if d])), 2),
        },
        "what_if_all_tokens_on_one_model_usd": {
            m: round((tokens["input"] * PRICES[m][0] + tokens["cc_5m"] * PRICES[m][0] * WRITE_5M
                      + tokens["cc_1h"] * PRICES[m][0] * WRITE_1H + tokens["cache_read"] * PRICES[m][2]
                      + tokens["output"] * PRICES[m][1]) / PER, 2)
            for m in ("claude-fable-5-1", "claude-opus-5", "claude-sonnet-5", "claude-haiku-4-5")
        },
        "what_if_1h_writes_at_5m_rate_usd": round(total_usd - totals["cache_write_1h"]
                                                  + totals["cache_write_1h"] * WRITE_5M / WRITE_1H, 2),
        "avg_cache_read_tokens_per_response": round(tokens["cache_read"] / max(1, sum(v["responses"] for v in by_model.values()))),
        "prices_usd_per_mtok": {k: {"input": v[0], "output": v[1], "cache_read": v[2],
                                    "cache_write_5m": v[0] * WRITE_5M, "cache_write_1h": v[0] * WRITE_1H}
                                for k, v in PRICES.items()},
    }
    with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(summary, fh, indent=1, sort_keys=True)
        fh.write("\n")

    print("window", first, "->", last, "| days", summary["window"]["days_with_usage"])
    print("records", counts, "| priced responses", summary["responses_priced"],
          "| unpriced", dict(unpriced), "| no ttl split", no_split)
    print("USD total", round(total_usd, 2), "| by class", summary["usd_by_class"])
    print("tokens", dict(tokens))
    for m, c in sorted(by_model.items(), key=lambda kv: -kv[1]["usd"]):
        print("  model", m, "usd", round(c["usd"], 2), "responses", c["responses"])
    print("main vs subagent", summary["usd_main_vs_subagent"], "| effort", summary["usd_by_effort"])
    print("geo", dict(geo), "| tier", dict(tier))
    print("commits in window", len(commits), "| box-authored", len(box_commits),
          "| of which workers", len(worker_commits), "| site-z projects", sorted(projects))
    print("task orders completed on site-z projects", orders_done)
    print("per output", summary["per_output_usd"])
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""open-calls.py -- one list of every open call per box, and the MEASUREMENT of whether a call touches only that box
(NFRA_CTLPLN workstream SEATS, cell CT-s-5; contract C-SEATS clause 4).

Andrew's word (2026-10-07 ~16:3xZ): the CTO of a fabric accrues every open call on its fabric; one that "only pertains to
their fabric, does not interfere with any other projects resources or materials" it adjudicates; one that touches more goes
through its manager. "Touches only its fabric" is a MEASUREMENT here, never a judgment.

    python .tools/open-calls.py add --project <CODE> --subject <text> --context <2-3 lines> --rec <rec> --asked-by <serial> --source <path>
                                    [--orders <order file> ...] [--roots <dir> ...]
    python .tools/open-calls.py add --kind approval --project NFRA_DEVPLN --box <box> --branch cand/<box>/<slug> --purpose <text>
                                    --pages <p1,p2> --class client-facing|opal-internal|test-only --how <text> [--subject <text>]
                                    --portal <portal repo path> [--check-only]
                                    # DP-b-5: head_sha and commits are COMPUTED from the portal (origin/PROD, origin/DEV); a branch
                                    # cut from DEV (overlap above 0) is refused; --check-only runs the checks and writes nothing
                                    # [--waive-overlap <sha[,sha...]> --waiver-ref <ruling file>]: the DEV-overlap refusal is waived
                                    # for exactly the named commits (full or abbreviated shas); every overlap commit must be named,
                                    # and a named sha outside the overlap is refused. The row stores approval.waiver {shas, ref}.
                                    # --check-only resolves <branch> as origin/<b>, else local <b>, else any commit-ish (a bare sha).
    python .tools/open-calls.py approval-lease --branch cand/<box>/<slug> --box <box> --purpose <text> --pages <p1,p2>
                                    --class <class> --how <text> --portal <portal repo path> --lease-file <path> [--project NFRA_DEVPLN]
                                    # DP-b-5: a live FAST lease of this seat (mode FAST, expires_epoch ahead, seat = OPAL_AGENT_SERIAL)
                                    # writes the row already CLOSED approved (by "FAST lease <file>", ruled_by lease)
    python .tools/open-calls.py list [--device <d> | --all] [--cloud] [--include-closed]
    python .tools/open-calls.py publish          # put this box's current list to the cluster copy, unchanged
    python .tools/open-calls.py close --id <id> --by <serial> --ruling <path> [--crossbox <crossbox id>]
                                      [--ruled-by andrew|cto]
    python .tools/open-calls.py close --id <id> --ruled-by andrew|cto --ruling-file <path> --decision approved|declined|withdrawn
                                      # an approval row only: --decision is required there and refused on any other kind;
                                      # withdrawn (DP-e-1) ends an OPEN duplicate row that is NOT a decision; a closed row is refused
    python .tools/open-calls.py approval-status --branch cand/<box>/<slug> [--store-dir <dir>]   # ONE line, rc 2 if unreadable
    python .tools/open-calls.py hold --id <id> --by <serial> --reason <one line>     # held for Andrew; the scan skips it
    python .tools/open-calls.py lift --id <id> --by <serial> --ruling <path>         # a hold lifted on a ruling (kept on the row)
  (close also takes --ruled-by cluster-lead: the laptop CTO's record or a RULED xadj file closes a CROSS-BOX row.)
    python .tools/open-calls.py mode get [--box <b>] [--part scan|empty_tick|all]     # the keep-driving switch (/keep-driving)
    python .tools/open-calls.py mode set --part scan|empty_tick|all --state on|off|inherit [--box <b>] --by <s> --reason <t>
    python .tools/open-calls.py scope --project <CODE> [--orders <order file> ...] [--roots <dir> ...]
    python .tools/open-calls.py scope --selftest
  (close also takes --xadj <XA id>: a RULED cross-adjudication, .tools/xadj.py, settles a CTO-ruled CROSS-BOX row.)

THE LIST is org/devices/state/<device>/open_calls.json (ONE WRITER: the box named, resolved from AGENTBUS_DEVICE through
lib/devices.py, never from a path). Shape (schema "open-calls/1"; every reader refuses a key it does not know):
    {"schema", "device", "written_at", "written_by", "rows": [ {id, project, subject, asked_by, source, orders, roots,
     state (OPEN|CLOSED), opened_at, scope {...the measurement...}, closed (null | {at, by, ruling, crossbox})} ]}
A file ABSENT is not an EMPTY list: `list --all` names the boxes whose file is absent.
CLOSING (1.0.0_SA_CTO msg 107148, on dell1's defect relay): a close whose ruling is ANDREW'S WORD (`--ruled-by andrew`,
ruling file required) closes the row whatever its scope. CLOSED-BOTH binds only a CTO-ruled (`--ruled-by cto`, the
default) CROSS-BOX call. The closure records `ruled_by`.
`kind` (optional on a row): `fork` = a decision with options (the default) | `act` = an act only Andrew can do (a delete,
a signature, a vendor use); Andrew 2026-10-08 ~18:4xZ: "keep that all in open calls" | `approval` = a portal feature
waiting for Andrew's yes or no (NFRA_DEVPLN; carries an `approval` object; closed with `decision`; read by `approval-status`).
`--project NONE` records a call
that belongs to no project (no scope measurement is run; its verdict reads NO-PROJECT).

THE CLUSTER COPY (1.0.0_SA_CTO msg 107121, Andrew-direct ~18:4xZ point 5): every write of a box's list also puts it to
    s3://opal-313476888478-globgrph/fabric/open-calls/v1/box=<box>/open_calls.json
beside the fabric-activity store (a failed put is spooled under .comp-graph/open-calls-spool/ and retried on the next
write or `list --cloud`). `list --all --cloud` reads EVERY box's cloud copy -- no git pull, no lag -- grouped by box,
project and agent with timestamps; a box with no cloud copy prints ABSENT, never empty.

THE MEASUREMENT (`scope`), four readings and a shared set:
  paths      the union of <paths> of the orders named (else the project's non-terminal orders) plus the roots named: a path
             under another live project's home, or overlapping the write set of a project placed on ANOTHER box
             (.tools/placement-check.py's read_projects() and overlaps(), imported), is a hit.
  risk       the highest <risk> among those orders; WORLD is printed and does not alone make a call cross-box.
  placement  the project.json `placement` (else `fabric`) resolved to a box; not this box, or unresolved, is a hit.
  resources  the bucket and other names the named or inferred Terraform roots DECLARE (resource blocks: bucket, name,
             function_name, table_name, queue_name, family), compared with the same reading of every root named by a
             project placed on another box; a name both read is a hit. A named root that cannot be read is a hit.
  shared     the trunk's own registers (SHARED_PATHS below) and any bucket the naming registry marks shared
             (infra/logic/registry/tiers.json homes whose "home" is "shared"; SHARED_BUCKETS_FALLBACK only if that file
             cannot be read) touch every box. A bucket named in a policy ARN counts for this reading only.
BLIND: a resource shared in practice that no Terraform declares is not seen.
LAST line: CALL-SCOPE project=<CODE> device=<d> paths=<clear|hit> placement=<clear|hit> resources=<clear|hit>
           shared=<clear|hit> risk=<LOCAL|SERVED|WORLD> verdict=<OWN-BOX|CROSS-BOX>
OWN-BOX means this box's CTO may settle the call. An act only Andrew can do still goes to him, named as that act: the tool
prints that sentence and decides nothing about which acts those are.

Environment (tests only): OPAL_STATE_ROOT replaces org/devices/state; OPAL_CROSSBOX_ROOT replaces org/devices/crossbox.
Exit: 0 done (either verdict is a result), 1 refused, 2 usage or an unresolved box, 3 an unreadable register or list file.
"""
from __future__ import annotations

import argparse
import datetime
import glob
import importlib.util
import json
import os
import re
import secrets
import subprocess
import sys
import tempfile
import time

TOOLS =os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)

SCHEMA = "open-calls/1"
TOP_KEYS = {"schema", "device", "written_at", "written_by", "rows"}
ROW_KEYS = {"id", "project", "subject", "asked_by", "source", "orders", "roots", "state", "opened_at", "scope", "closed",
            "kind", "escalation", "context", "rec", "approval"}
# `context` + `rec` (Andrew-direct 2026-10-09 ~01:1xZ, "yes, build the context and rec fields"; record
# org/tier1_exec/4.0.0_SA_CRO~B/deliverables/ANDREW_DIRECT_20261009_011xZ_OPEN_CALL_CONTEXT_AND_REC_FIELDS.md): what created
# the call and what it gates, and the asking seat's recommendation. Required on a NEW fork (context on a new act); rows written
# before carry neither and read as before.
CONTEXT_MIN, CONTEXT_MAX = 40, 600
KINDS = ("fork", "act", "approval")
NO_PROJECT = "NONE"
CLOUD_BUCKET = "opal-313476888478-globgrph"
CLOUD_PREFIX = "fabric/open-calls/v1"
ROW_REQUIRED = {"id", "project", "subject", "asked_by", "source", "state", "opened_at", "scope"}
CLOSED_KEYS = {"at", "by", "ruling", "crossbox", "ruled_by", "xadj", "decision"}
# `approval` (NFRA_DEVPLN round 1, cell DP-b-1; record org/missions/D0/NFRA/NFRA_DEVPLN/ledger/APPROVAL_KIND_RULE24_RECORD_20261013.md):
# a portal feature waiting for Andrew's yes or no. The row carries an `approval` object; closing it writes `decision`
# (approved|declined). head_sha and commits are computed from the portal repository at registration (DP-b-5, register_facts).
APPROVAL_KEYS = {"box", "branch", "purpose", "pages", "class", "how", "head_sha", "commits"}
# approval.waiver (the CTO's named DEV-overlap waiver): present only on a row registered with --waive-overlap; {shas, ref}.
APPROVAL_OPTIONAL_KEYS = {"waiver"}
WAIVER_KEYS = {"shas", "ref"}
FULL_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
WAIVER_SHA_RE = re.compile(r"^[0-9a-fA-F]{4,40}$")   # a commit name in hex: never a count, a range or a wildcard
APPROVAL_CLASSES = ("client-facing", "opal-internal", "test-only")
APPROVAL_DECISIONS = ("approved", "declined")
# `withdrawn` (NFRA_DEVPLN round 4, cell DP-e-1): ends an OPEN approval row that is NOT a decision on the feature (a branch
# registered twice). approval-status skips a withdrawn row when it picks the row for a branch; the close writes it as `decision`.
APPROVAL_WITHDRAWN = "withdrawn"
APPROVAL_CLOSE_DECISIONS = APPROVAL_DECISIONS + (APPROVAL_WITHDRAWN,)
APPROVAL_RULED_BY = ("andrew", "cto")
APPROVAL_BRANCH_RE = re.compile(r"^cand/([^/\s]+)/([A-Za-z0-9][A-Za-z0-9._-]*)$")
# `escalation` (optional, Andrew-direct 2026-10-09 ~00:0xZ; .tools/open-calls-scan.py): the box CTO's answer to the scan when it
# does not rule the call itself -- `xadj` (sent to cross-adjudication, ref = the XA id) or `andrew` (held for his word).
ESC_KEYS = {"to", "ref", "at", "by", "reason"}
ESC_TO = ("xadj", "andrew", "lifted")
RULED_BY = ("cto", "andrew", "cluster-lead")
# `cluster-lead` (Andrew-direct 2026-10-11 ~03:2xZ, record ANDREW_DIRECT_20261011_032xZ_CTO_LEADS_CLUSTER_OPEN_CALLS_LOOP_60M.md):
# the laptop CTO adjudicates every box's calls; its ruling closes a CROSS-BOX row when the ruling file is its own record or a
# RULED cross-adjudication file. Any other path is refused.
CLUSTER_LEAD_RULING_PREFIXES = ("org/tier1_exec/1.0.0_SA_CTO/deliverables/", "org/critical_paths/cross_adjudication/")
STATES = ("OPEN", "CLOSED")
RISK_ORDER = ("LOCAL", "SERVED", "WORLD")

# The trunk's own registers: a path here is on the shared branch, so a call that touches it touches every box.
SHARED_PATHS = ("org/missions/DIRECTIVES.yaml", "org/missions/MACROS.yaml", ".owned-paths.yaml", "CLAUDE.md",
                "org/XXX.md", ".tools", "lib", ".claude")
# Used ONLY when infra/logic/registry/tiers.json cannot be read (the registry marks a shared bucket as a tier home with
# "home": "shared"; this list is the explicit fallback the order asks for).
SHARED_BUCKETS_FALLBACK = ("opal-data-assets", "opal-data-portal-v2")
TF_PREFIX = "infra/aws/terraform/"
TF_KEYS = ("bucket", "name", "function_name", "table_name", "queue_name", "family")
RES_RE = re.compile(r'^resource\s+"(aws_[A-Za-z0-9_]+)"\s+"[^"]+"\s*\{', re.M)
KEY_RE = re.compile(r'^ {2}(%s)\s*=\s*"([^"\n]+)"' % "|".join(TF_KEYS), re.M)   # two-space depth: not a nested block's name
ARN_RE = re.compile(r'arn:aws:s3:::([A-Za-z0-9._${}\-]+)')
RISK_RE = re.compile(r"<risk>\s*([A-Za-z]+)\s*</risk>")
CAP = 6   # evidence lines kept per reading


class Refused(Exception):
    pass


class BadFile(Exception):
    pass


def load_mod(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def now_utc() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def age_text(stamp) -> str:
    try:
        then = datetime.datetime.strptime(str(stamp), "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
        sec = int((datetime.datetime.now(datetime.timezone.utc) - then).total_seconds())
        return "age %dh%02dm" % (sec // 3600, (sec % 3600) // 60)
    except (ValueError, TypeError):
        return "age unknown (written_at %r)" % (stamp,)


def norm(p: str) -> str:
    return str(p).strip().replace("\\", "/").rstrip("/")


def rel_to_root(p: str, root: str) -> str:
    """A repository-relative, forward-slash form of p (absolute or relative to the cwd or to root)."""
    p = str(p)
    cand = p if os.path.isabs(p) else (os.path.join(os.getcwd(), p) if os.path.exists(os.path.join(os.getcwd(), p))
                                       else os.path.join(root, p))
    try:
        rel = os.path.relpath(os.path.abspath(cand), root)
    except ValueError:
        return norm(p)
    return norm(p) if rel.startswith("..") else norm(rel)


# ---------------------------------------------------------------- the measurement

def shared_buckets(root: str) -> tuple:
    """(set, basis): buckets the naming registry marks shared (tiers.json homes with home == 'shared')."""
    path = os.path.join(root, "infra", "logic", "registry", "tiers.json")
    try:
        doc = json.load(open(path, encoding="utf-8"))
        found = set()
        for tiers in (doc.get("homes") or {}).values():
            for cell in tiers.values():
                if isinstance(cell, dict) and cell.get("home") == "shared" and cell.get("bucket"):
                    found.add(cell["bucket"])
        if found:
            return found, "infra/logic/registry/tiers.json homes marked shared"
    except (OSError, ValueError, AttributeError):
        pass
    return set(SHARED_BUCKETS_FALLBACK), "SHARED_BUCKETS_FALLBACK (tiers.json unreadable or marks none)"


def tf_names(directory: str) -> tuple:
    """(declared names, bucket names mentioned in policy ARNs) over the *.tf files of one root directory.
    Declared = a quoted value of TF_KEYS inside a top-level `resource "aws_..." "x" {` block. Raises OSError when the
    directory cannot be read."""
    declared, arns = set(), set()
    files = sorted(glob.glob(os.path.join(directory, "*.tf")))
    if not os.path.isdir(directory):
        raise OSError("not a directory: %s" % directory)
    for path in files:
        text = open(path, encoding="utf-8", errors="replace").read()
        arns.update(m.group(1) for m in ARN_RE.finditer(text))
        block, lines = None, []
        for line in text.splitlines():
            if block is None:
                if RES_RE.match(line):
                    block, lines = True, [line]
            else:
                lines.append(line)
                if line.startswith("}"):
                    declared.update(m.group(2) for m in KEY_RE.finditer("\n".join(lines)))
                    block = None
        if block:
            declared.update(m.group(2) for m in KEY_RE.finditer("\n".join(lines)))
    return declared, arns


def infer_roots(paths: list, rootmap_keys: list) -> list:
    """Terraform root folders (repo-relative) named by paths under infra/aws/terraform/; the longest root_map key wins."""
    out = []
    for p in paths:
        p = norm(p)
        if not p.startswith(TF_PREFIX):
            continue
        tail = p[len(TF_PREFIX):]
        if not tail:
            continue
        best = max((k for k in rootmap_keys if tail == k or tail.startswith(k + "/")), key=len, default=None)
        top = best or tail.split("/")[0]
        root = TF_PREFIX + top
        if root not in out:
            out.append(root)
    return out


def order_facts(text: str, pc) -> tuple:
    """(paths, risk or None, status or None) from one task-order text, read with placement-check's own patterns."""
    paths = []
    for m in pc.PATHS_RE.finditer(text):
        paths.extend(norm(x) for x in m.group(1).splitlines() if x.strip() and not re.search(r"\s|^[<#`-]", x.strip()))
    rk = RISK_RE.search(text)
    st = pc.STATUS_RE.search(text)
    return paths, (rk.group(1).upper() if rk else None), (st.group(1).lower() if st else None)


def highest_risk(risks: list) -> str:
    known = [r for r in risks if r in RISK_ORDER]
    return max(known, key=RISK_ORDER.index) if known else "LOCAL"


def measure(ctx: dict, code: str, mybox, paths: list, roots: list, risks: list) -> dict:
    """PURE over ctx (files read only for Terraform roots). ctx: root, device, projects [{code, box, home, writes}],
    overlaps (callable), rootmap_keys, shared_buckets, shared_basis. Returns the four readings, the shared set, the risk,
    the verdict and the evidence lines."""
    ov = ctx["overlaps"]
    me, device = code, ctx["device"]
    others = [q for q in ctx["projects"] if q["code"] != me]
    ev = {"paths": [], "placement": [], "resources": [], "shared": []}
    touch = [norm(p) for p in paths] + [norm(r) for r in roots]

    for p in touch:
        for q in others:
            if ov(p, q["home"]):
                ev["paths"].append("%s is under the home of project %s (%s)" % (p, q["code"], q["home"]))
                continue
            if q["box"] and q["box"] != device:
                w = next((w for w in q["writes"] if ov(p, w)), None)
                if w:
                    ev["paths"].append("%s overlaps the write set of %s placed on %s (%s)" % (p, q["code"], q["box"], w))
    if mybox is None:
        ev["placement"].append("project %s has no placement or fabric that resolves to a box in the register" % me)
    elif mybox != device:
        ev["placement"].append("project %s is placed on %s, this box is %s" % (me, mybox, device))

    all_roots = list(roots)
    for r in infer_roots(paths, ctx["rootmap_keys"]):
        if r not in all_roots:
            all_roots.append(r)
    mine_names, arn_names = {}, set()
    for r in all_roots:
        try:
            declared, arns = tf_names(os.path.join(ctx["root"], r))
            mine_names[r] = declared
            arn_names.update(arns)
        except OSError as exc:
            ev["resources"].append("root %s cannot be read (%s): not clear" % (r, exc))
    other_names = {}
    for q in others:
        if not q["box"] or q["box"] == device:
            continue
        for r in infer_roots(q["writes"], ctx["rootmap_keys"]):
            if r not in other_names:
                try:
                    other_names[r] = (tf_names(os.path.join(ctx["root"], r))[0], q)
                except OSError:
                    continue
    for r, declared in mine_names.items():
        for r2, (declared2, q) in other_names.items():
            both = sorted(declared & declared2)
            if both:
                ev["resources"].append("root %s declares %s, also declared by root %s named by %s on %s" % (
                    r, ", ".join(both[:3]) + (" (+%d)" % (len(both) - 3) if len(both) > 3 else ""), r2, q["code"], q["box"]))

    for p in touch:
        hit = next((s for s in SHARED_PATHS if ov(p, s)), None)
        if hit:
            ev["shared"].append("%s is on the shared branch (%s)" % (p, hit))
    named = set().union(*mine_names.values()) if mine_names else set()
    for b in sorted((named | arn_names) & ctx["shared_buckets"]):
        ev["shared"].append("bucket %s is marked shared (%s)" % (b, ctx["shared_basis"]))

    flags = {k: ("hit" if v else "clear") for k, v in ev.items()}
    risk = highest_risk(risks)
    cross = any(v == "hit" for v in flags.values())
    return {"project": me, "device": device, "paths": flags["paths"], "placement": flags["placement"],
            "resources": flags["resources"], "shared": flags["shared"], "risk": risk,
            "verdict": "CROSS-BOX" if cross else "OWN-BOX", "evidence": ev, "roots": all_roots, "touch": touch}


def scope_line(res: dict) -> str:
    return ("CALL-SCOPE project=%s device=%s paths=%s placement=%s resources=%s shared=%s risk=%s verdict=%s" % (
        res["project"], res["device"], res["paths"], res["placement"], res["resources"], res["shared"], res["risk"],
        res["verdict"]))


def print_scope(res: dict, notes: list) -> None:
    for n in notes:
        print("  " + n)
    print("  PATHS+ROOTS READ (%d): %s" % (len(res["touch"]), ", ".join(res["touch"][:CAP]) + (" ..." if len(res["touch"]) > CAP else "")))
    print("  TERRAFORM ROOTS READ (%d): %s" % (len(res["roots"]), ", ".join(res["roots"]) or "none named or inferred"))
    for k in ("paths", "placement", "resources", "shared"):
        print("  %-9s %s" % (k.upper(), res[k]))
        for line in res["evidence"][k][:CAP]:
            print("    - " + line)
        if len(res["evidence"][k]) > CAP:
            print("    - (+%d more)" % (len(res["evidence"][k]) - CAP))
    print("  RISK      %s%s" % (res["risk"], " (printed; WORLD alone does not make a call cross-box)" if res["risk"] == "WORLD" else ""))
    print("  BLIND: a resource shared in practice that no Terraform declares is not seen by this reading.")
    print("  OWN-BOX means this box's CTO may settle the call; an act only Andrew can do (a hold he set by name, an S3 delete, "
          "a vendor use, a signature) still goes to him, named as that act. This tool does not decide which acts those are.")
    print(scope_line(res))


# ---------------------------------------------------------------- the real tree

def real_ctx(root: str = ROOT) -> dict:
    dev = load_mod("opal_devices", "lib/devices.py")
    pc = load_mod("opal_placement_check", ".tools/placement-check.py")
    pc.ROOT = root
    reg = dev.load()
    name, basis = dev.this_device(reg)
    projects, findings = pc.read_projects(dev, reg)
    for p in projects:
        p["box"] = project_box(p["home"], p["box"], dev, reg, root)
    keys = []
    try:
        keys = sorted(json.load(open(os.path.join(root, "infra", "logic", "registry", "root_map.json"),
                                     encoding="utf-8")).get("roots", {}))
    except (OSError, ValueError):
        pass
    sb, sbasis = shared_buckets(root)
    return {"root": root, "device": name, "device_basis": basis, "projects": projects, "findings": findings,
            "overlaps": pc.overlaps, "rootmap_keys": keys, "shared_buckets": sb, "shared_basis": sbasis, "pc": pc,
            "dev": dev, "reg": reg}


def project_box(home: str, fabric_box, dev, reg, root: str):
    """The project row's `placement` resolved to a box, else the box its fabric resolved to."""
    try:
        field = json.load(open(os.path.join(root, home, "project.json"), encoding="utf-8")).get("placement")
    except (OSError, ValueError):
        field = None
    return (dev.resolve(str(field), reg) if field else None) or fabric_box


def find_project(ctx: dict, code: str):
    for p in ctx["projects"]:
        if p["code"] == code:
            return p
    hits = glob.glob(os.path.join(ctx["root"], "org", "missions", "D*", "*", code, "project.json"))
    if not hits:
        return None
    home = norm(os.path.relpath(os.path.dirname(hits[0]), ctx["root"]))
    try:
        fabric = json.load(open(hits[0], encoding="utf-8")).get("fabric")
    except (OSError, ValueError):
        fabric = None
    return {"code": code, "home": home, "writes": [home], "live": False,
            "box": project_box(home, ctx["dev"].resolve(str(fabric or ""), ctx["reg"]), ctx["dev"], ctx["reg"], ctx["root"])}


def scope_project(ctx: dict, code: str, orders: list, roots: list) -> tuple:
    """(result, notes). Raises Refused when the project is unknown."""
    proj = find_project(ctx, code)
    if proj is None:
        raise Refused("project %s has no project.json under org/missions/D*/*/%s" % (code, code))
    pc, notes = ctx["pc"], []
    if proj.get("live") is False:
        notes.append("project %s is not live (terminal status): its own tree is its write set" % code)
    files = []
    if orders:
        files = [o if os.path.isabs(o) else (os.path.join(os.getcwd(), o) if os.path.exists(os.path.join(os.getcwd(), o))
                                             else os.path.join(ctx["root"], o)) for o in orders]
        notes.append("ORDERS: %d named" % len(files))
    else:
        files = sorted(glob.glob(os.path.join(ctx["root"], proj["home"], "task-orders", "*.md")))
        notes.append("ORDERS: none named; the project's task-orders folder holds %d, the non-terminal ones are read" % len(files))
    paths, risks, used = [], [], 0
    for f in files:
        try:
            text = open(f, encoding="utf-8", errors="replace").read()
        except OSError as exc:
            raise Refused("order file %s cannot be read (%s)" % (f, exc))
        p, risk, status = order_facts(text, pc)
        if not orders and status in pc.TERMINAL_TO:
            continue
        used += 1
        paths.extend(x for x in p if x not in paths)
        if risk:
            risks.append(risk)
    notes.append("ORDERS READ: %d; <paths> entries %d; risks %s" % (used, len(paths), ",".join(risks) or "none declared (read as LOCAL)"))
    rroots = [norm(rel_to_root(r, ctx["root"])) for r in (roots or [])]
    res = measure(ctx, code, proj["box"], paths, rroots, risks)
    return res, notes


# ---------------------------------------------------------------- the list files

def state_root() -> str:
    return os.environ.get("OPAL_STATE_ROOT", "").strip() or os.path.join(ROOT, "org", "devices", "state")


def crossbox_root() -> str:
    return os.environ.get("OPAL_CROSSBOX_ROOT", "").strip() or os.path.join(ROOT, "org", "devices", "crossbox")


def list_path(device: str) -> str:
    return os.path.join(state_root(), device, "open_calls.json")


def validate_doc(doc, device: str, where: str) -> dict:
    if not isinstance(doc, dict):
        raise BadFile("%s: top level is not an object" % where)
    unknown = sorted(set(doc) - TOP_KEYS)
    if unknown:
        raise BadFile("%s: unknown key(s) %s (readers refuse a key they do not know)" % (where, ", ".join(unknown)))
    missing = sorted(TOP_KEYS - set(doc))
    if missing:
        raise BadFile("%s: missing key(s) %s" % (where, ", ".join(missing)))
    if doc["schema"] != SCHEMA:
        raise BadFile("%s: schema %r is not %r" % (where, doc["schema"], SCHEMA))
    if doc["device"] != device:
        raise BadFile("%s: device %r is not %r (one file per box)" % (where, doc["device"], device))
    if not isinstance(doc["rows"], list):
        raise BadFile("%s: rows is not a list" % where)
    for i, row in enumerate(doc["rows"]):
        if not isinstance(row, dict):
            raise BadFile("%s: row %d is not an object" % (where, i))
        unknown = sorted(set(row) - ROW_KEYS)
        if unknown:
            raise BadFile("%s: row %s has unknown key(s) %s" % (where, row.get("id", i), ", ".join(unknown)))
        missing = sorted(ROW_REQUIRED - set(row))
        if missing:
            raise BadFile("%s: row %s lacks %s" % (where, row.get("id", i), ", ".join(missing)))
        if row["state"] not in STATES:
            raise BadFile("%s: row %s state %r is not one of %s" % (where, row["id"], row["state"], "/".join(STATES)))
        for fld in ("context", "rec"):
            if fld in row and not isinstance(row[fld], str):
                raise BadFile("%s: row %s `%s` is not text" % (where, row["id"], fld))
        if "kind" in row and row["kind"] not in KINDS:
            raise BadFile("%s: row %s kind %r is not one of %s" % (where, row["id"], row["kind"], "/".join(KINDS)))
        if row.get("kind") == "approval" or "approval" in row:
            check_approval_row(row, where)
        esc = row.get("escalation")
        if esc is not None and (not isinstance(esc, dict) or set(esc) != ESC_KEYS or esc["to"] not in ESC_TO):
            raise BadFile("%s: row %s `escalation` is malformed (keys %s, to one of %s)" % (
                where, row["id"], "/".join(sorted(ESC_KEYS)), "/".join(ESC_TO)))
        closed = row.get("closed")
        if closed is not None and (not isinstance(closed, dict) or set(closed) - CLOSED_KEYS):
            raise BadFile("%s: row %s `closed` carries a key this reader does not know" % (where, row["id"]))
        if isinstance(closed, dict) and "decision" in closed and closed["decision"] not in APPROVAL_CLOSE_DECISIONS:
            raise BadFile("%s: row %s `closed.decision` %r is not approved/declined/withdrawn" % (where, row["id"], closed["decision"]))
    return doc


def check_approval_row(row: dict, where: str) -> None:
    """An approval row is kind approval with the approval object, and a CLOSED one carries its decision."""
    ap = row.get("approval")
    if row.get("kind") != "approval" or not isinstance(ap, dict) or not (
            APPROVAL_KEYS <= set(ap) <= APPROVAL_KEYS | APPROVAL_OPTIONAL_KEYS):
        raise BadFile("%s: row %s is not a well-formed approval row (kind approval, approval keys %s)" % (
            where, row["id"], "/".join(sorted(APPROVAL_KEYS))))
    if "waiver" in ap:
        w = ap["waiver"]
        if (not isinstance(w, dict) or set(w) != WAIVER_KEYS or not isinstance(w["shas"], list) or not w["shas"]
                or not all(isinstance(s, str) and FULL_SHA_RE.match(s) for s in w["shas"])
                or not isinstance(w["ref"], str) or not w["ref"].strip()):
            raise BadFile("%s: row %s approval.waiver must be {shas: [full shas], ref: <path>}" % (where, row["id"]))
    if ap["class"] not in APPROVAL_CLASSES:
        raise BadFile("%s: row %s approval.class %r is not one of %s" % (where, row["id"], ap["class"], "/".join(APPROVAL_CLASSES)))
    if not isinstance(ap["pages"], list) or not isinstance(ap["branch"], str) or not APPROVAL_BRANCH_RE.match(ap["branch"]):
        raise BadFile("%s: row %s approval.pages must be a list and approval.branch cand/<box>/<slug>" % (where, row["id"]))
    closed = row.get("closed")
    if row["state"] == "CLOSED" and not (isinstance(closed, dict) and closed.get("decision") in APPROVAL_CLOSE_DECISIONS):
        raise BadFile("%s: row %s is CLOSED without a decision (approved/declined/withdrawn)" % (where, row["id"]))


def read_list(device: str) -> dict:
    path = list_path(device)
    try:
        doc = json.load(open(path, encoding="utf-8"))
    except OSError as exc:
        raise BadFile("%s: unreadable (%s)" % (path, exc))
    except ValueError as exc:
        raise BadFile("%s: not JSON (%s)" % (path, exc))
    return validate_doc(doc, device, path)


def write_list(device: str, doc: dict, serial: str) -> str:
    doc["written_at"], doc["written_by"] = now_utc(), serial
    path = list_path(device)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(doc, indent=1, ensure_ascii=True) + "\n")
    os.replace(tmp, path)
    cloud_put(device, doc)
    return path


# ---------------------------------------------------------------- the cluster copy (s3)

def cloud_key(device: str) -> str:
    return "%s/box=%s/open_calls.json" % (CLOUD_PREFIX, device)


def _spool_dir() -> str:
    return os.path.join(ROOT, ".comp-graph", "open-calls-spool")


def _s3():
    import boto3
    from botocore.config import Config
    return boto3.client("s3", config=Config(connect_timeout=5, read_timeout=15, retries={"max_attempts": 2}))


def cloud_put(device: str, doc: dict) -> bool:
    """Put this box's list to the cluster copy. Never fails the write: a failed put is spooled (latest only) and retried."""
    if os.environ.get("OPAL_STATE_ROOT", "").strip() or os.environ.get("OPAL_OPENCALLS_CLOUD", "1") == "0":
        return False   # tests and an explicit off-switch never touch the cluster copy
    body = (json.dumps(doc, indent=1, ensure_ascii=True) + "\n").encode("ascii")
    try:
        _s3().put_object(Bucket=CLOUD_BUCKET, Key=cloud_key(device), Body=body, ContentType="application/json")
        spooled = os.path.join(_spool_dir(), device + ".json")
        if os.path.exists(spooled):
            os.remove(spooled)
        print("CLOUD s3://%s/%s" % (CLOUD_BUCKET, cloud_key(device)))
        return True
    except Exception as exc:  # noqa: BLE001 -- the local list is the record; the cloud copy catches up
        os.makedirs(_spool_dir(), exist_ok=True)
        with open(os.path.join(_spool_dir(), device + ".json"), "wb") as fh:
            fh.write(body)
        print("WARN: cluster copy not written (%s); spooled for the next write or `list --cloud`" % type(exc).__name__)
        return False


def cloud_flush() -> None:
    d = _spool_dir()
    if not os.path.isdir(d):
        return
    for name in sorted(os.listdir(d)):
        if name.endswith(".json"):
            try:
                doc = json.load(open(os.path.join(d, name), encoding="utf-8"))
            except (OSError, ValueError):
                continue
            cloud_put(name[:-5], doc)


def _err_code(exc) -> str:
    resp = getattr(exc, "response", None)
    return ((resp or {}).get("Error") or {}).get("Code", "") if isinstance(resp, dict) else ""


def cloud_read_all(boxes: list) -> tuple:
    """({box: (doc, last_modified_utc)}, absent boxes, refused [(box, reason)]) from the cluster copies."""
    s3 = _s3()
    found, absent, refused = {}, [], []
    for box in boxes:
        try:
            obj = s3.get_object(Bucket=CLOUD_BUCKET, Key=cloud_key(box))
        except Exception as exc:  # noqa: BLE001
            if _err_code(exc) in ("NoSuchKey", "404"):
                absent.append(box)
            else:
                refused.append((box, "%s %s" % (type(exc).__name__, _err_code(exc))))
            continue
        try:
            doc = validate_doc(json.loads(obj["Body"].read()), box, "s3://%s/%s" % (CLOUD_BUCKET, cloud_key(box)))
        except (BadFile, ValueError) as exc:
            refused.append((box, str(exc)))
            continue
        found[box] = (doc, obj["LastModified"].astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    return found, absent, refused


# ---------------------------------------------------------------- the keep-driving switch (Andrew-direct 2026-10-09 ~00:4xZ)
# "I also want to be able to flip this mode on or off somewhere in the cloud, it should be a switch that we use a skill to
# flip on and off" -- approved as option (a): ONE object beside the per-box lists. Record:
# org/tier1_exec/4.0.0_SA_CRO~B/deliverables/ANDREW_DIRECT_20261009_005xZ_KEEP_DRIVING_CLOUD_SWITCH.md. Skill: /keep-driving.
# Parts: `scan` (the 10-minute nudge, .tools/open-calls-scan.py) and `empty_tick` (a COO's empty drive tick runs
# /next-calls --drive). ABSENT = ON (his standing order); UNREADABLE = ON with a WARN (the switch never silently stops work).
MODE_KEY = "%s/mode.json" % CLOUD_PREFIX
MODE_SCHEMA = "keep-driving-mode/1"
MODE_PARTS = ("scan", "empty_tick")
MODE_STATES = ("on", "off")
MODE_KEYS = {"schema", "scan", "empty_tick", "boxes", "set_by", "set_at", "reason"}


def _mode_local():
    return os.environ.get("OPAL_MODE_LOCAL", "").strip()   # tests: a file path stands in for the S3 object


def mode_check(doc) -> dict:
    if not isinstance(doc, dict) or set(doc) != MODE_KEYS or doc["schema"] != MODE_SCHEMA:
        raise BadFile("mode.json: keys must be exactly %s with schema %s" % ("/".join(sorted(MODE_KEYS)), MODE_SCHEMA))
    for part in MODE_PARTS:
        if doc[part] not in MODE_STATES:
            raise BadFile("mode.json: %s=%r is not on/off" % (part, doc[part]))
    if not isinstance(doc["boxes"], dict):
        raise BadFile("mode.json: boxes is not an object")
    for box, over in doc["boxes"].items():
        if not isinstance(over, dict) or set(over) - set(MODE_PARTS) or any(v not in MODE_STATES for v in over.values()):
            raise BadFile("mode.json: box %s override is malformed" % box)
    return doc


def mode_read() -> tuple:
    """(doc or None, source) where source is object | absent | unreadable:<why>."""
    try:
        if _mode_local():
            if not os.path.exists(_mode_local()):
                return None, "absent"
            return mode_check(json.load(open(_mode_local(), encoding="utf-8"))), "object"
        try:
            obj = _s3().get_object(Bucket=CLOUD_BUCKET, Key=MODE_KEY)
        except Exception as exc:  # noqa: BLE001
            if _err_code(exc) in ("NoSuchKey", "404"):
                return None, "absent"
            raise
        return mode_check(json.loads(obj["Body"].read())), "object"
    except Exception as exc:  # noqa: BLE001 -- the switch never stops work by being unreadable
        return None, "unreadable:%s" % (str(exc)[:120] or type(exc).__name__)


def mode_state(doc, box: str, part: str) -> str:
    """on|off for one part on one box: the box override, else the global value, else on."""
    if doc is None:
        return "on"
    over = (doc.get("boxes") or {}).get(box) or {}
    return over.get(part, doc[part])


def mode_write(doc: dict) -> None:
    mode_check(doc)
    body = json.dumps(doc, indent=1, ensure_ascii=True) + "\n"
    if _mode_local():
        with open(_mode_local(), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(body)
        return
    _s3().put_object(Bucket=CLOUD_BUCKET, Key=MODE_KEY, Body=body.encode("ascii"), ContentType="application/json")


def mode_line(doc, source: str, boxes: list) -> str:
    over = ", ".join("%s %s" % (b, " ".join("%s=%s" % kv for kv in sorted(o.items())))
                     for b, o in sorted(((doc or {}).get("boxes") or {}).items()) if o) or "none"
    who = ("set by %s at %s: %s" % (doc["set_by"], doc["set_at"], doc["reason"])) if doc else "never set (default ON)"
    per = " ".join("%s:scan=%s,empty_tick=%s" % (b, mode_state(doc, b, "scan"), mode_state(doc, b, "empty_tick")) for b in boxes)
    return "KEEP-DRIVING scan=%s empty_tick=%s overrides=[%s] source=%s | %s | per-box %s" % (
        mode_state(doc, "", "scan"), mode_state(doc, "", "empty_tick"), over, source, who, per)


def cmd_mode(args) -> int:
    dev = load_mod("opal_devices", "lib/devices.py")
    reg = dev.load()
    doc, source = mode_read()
    if source.startswith("unreadable"):
        print("WARN: the switch is unreadable (%s); every part reads ON" % source)
    if args.action == "get":
        box = dev.resolve(args.box, reg) if args.box else this_box(dev, reg)
        if box is None:
            raise Refused("ERROR: %r is not a device in the register" % args.box)
        parts = MODE_PARTS if args.part == "all" else (args.part,)
        print(mode_line(doc, source, dev.names(reg)))
        for part in parts:
            print("KEEP-DRIVING-MODE box=%s part=%s state=%s source=%s" % (box, part, mode_state(doc, box, part), source))
        return 0
    if source.startswith("unreadable"):
        raise Refused("REFUSED: the switch is unreadable (%s); a set would overwrite a value nobody read" % source)
    if not (args.by and args.reason and args.state):
        raise Refused("REFUSED: set needs --state, --by and --reason")
    box = None
    if args.box:
        box = dev.resolve(args.box, reg)
        if box is None:
            raise Refused("ERROR: %r is not a device in the register" % args.box)
    new = doc or {"schema": MODE_SCHEMA, "scan": "on", "empty_tick": "on", "boxes": {}, "set_by": "", "set_at": "",
                  "reason": ""}
    parts = MODE_PARTS if args.part == "all" else (args.part,)
    for part in parts:
        if box is None:
            if args.state == "inherit":
                raise Refused("REFUSED: inherit applies to a box override only (--box)")
            new[part] = args.state
        else:
            over = dict(new["boxes"].get(box) or {})
            if args.state == "inherit":
                over.pop(part, None)
            else:
                over[part] = args.state
            if over:
                new["boxes"][box] = over
            else:
                new["boxes"].pop(box, None)
    new["set_by"], new["set_at"], new["reason"] = args.by, now_utc(), args.reason
    mode_write(new)
    print("SET %s %s=%s by %s" % ("box " + box if box else "global", "/".join(parts), args.state, args.by))
    print(mode_line(new, "object", dev.names(reg)))
    return 0



def this_box(dev, reg) -> str:
    name, basis = dev.this_device(reg)
    if name is None:
        raise Refused("this box is unresolved: %s" % basis)
    return name


def writer_serial(fallback: str) -> str:
    return os.environ.get("OPAL_AGENT_SERIAL", "").strip() or fallback


# ---------------------------------------------------------------- commands

def cmd_scope(args) -> int:
    if args.selftest:
        return selftest()
    if not args.project:
        print("ERROR: scope needs --project <CODE> (or --selftest)", file=sys.stderr)
        return 2
    ctx = real_ctx()
    if ctx["device"] is None:
        print("ERROR: this box is unresolved: %s" % ctx["device_basis"], file=sys.stderr)
        return 2
    try:
        res, notes = scope_project(ctx, args.project, args.orders or [], args.roots or [])
    except Refused as exc:
        print("ERROR: %s" % exc, file=sys.stderr)
        return 2
    print("scope | box %s (%s) | live projects read: %d | shared buckets: %s" % (
        ctx["device"], ctx["device_basis"], len(ctx["projects"]), ", ".join(sorted(ctx["shared_buckets"]))))
    print_scope(res, notes)
    return 0


def public_scope(res: dict) -> dict:
    """The measurement as saved on the call: the readings, the risk, the verdict and the first evidence lines per reading."""
    return {"measured_at": now_utc(), "paths": res["paths"], "placement": res["placement"], "resources": res["resources"],
            "shared": res["shared"], "risk": res["risk"], "verdict": res["verdict"], "roots": res["roots"],
            "evidence": {k: v[:CAP] for k, v in res["evidence"].items()}}


def check_call_text(kind: str, context, rec, source: str) -> None:
    """Refuse a new call that does not carry its own context (and, for a fork, its REC), or whose source is box-local mail."""
    context, rec = (context or "").strip(), (rec or "").strip()
    if not context:
        raise Refused("REFUSED: --context is required: 2-3 lines on what created the call and what it gates (Andrew-direct "
                      "2026-10-09 ~01:1xZ). The subject is the decision; the context is why it exists.")
    if not CONTEXT_MIN <= len(context) <= CONTEXT_MAX:
        raise Refused("REFUSED: --context is %d characters; it must be %d-%d (2-3 lines, not a pointer and not a report)" % (
            len(context), CONTEXT_MIN, CONTEXT_MAX))
    if kind == "fork" and not rec:
        raise Refused("REFUSED: --rec is required on a fork: the asking seat's recommendation and its one-sentence why")
    norm_src = source.replace("\\", "/")
    if "org/mcp/inbox/" in norm_src:
        raise Refused("REFUSED: the source %s is an inbox message, which lives on one box only; the adjudicating box cannot "
                      "read it. Cite a committed file (the record, decomposition, ruling or deliverable that holds the call)." % source)


def approval_fields(args, check_only: bool = False) -> dict:
    """The `approval` object from the add flags. Refused naming the field, before anything is read or written (rc 2).
    A --check-only registration accepts any branch name (DP-b-5): the cand/<box>/<slug> name check is skipped there."""
    for f, v in (("--box", args.box), ("--branch", args.branch), ("--purpose", args.purpose), ("--pages", args.pages),
                 ("--class", args.klass), ("--how", args.how)):
        if v is None or not v.strip():
            raise Refused("%s is required for --kind approval" % f)
    if args.klass not in APPROVAL_CLASSES:
        raise Refused("--class %r is not one of %s (field approval.class)" % (args.klass, "/".join(APPROVAL_CLASSES)))
    branch = args.branch.strip()
    m = APPROVAL_BRANCH_RE.match(branch)
    if not check_only and not m:
        raise Refused("--branch %r is not cand/<box>/<slug> (field approval.branch)" % branch)
    if not check_only and m.group(1) != args.box.strip():
        raise Refused("--branch %r names box %s but --box is %s (field approval.branch)" % (branch, m.group(1), args.box.strip()))
    pages = [p.strip() for p in args.pages.split(",") if p.strip()]
    if not pages:
        raise Refused("--pages needs at least one page name (field approval.pages)")
    return {"box": args.box.strip(), "branch": branch, "purpose": args.purpose.strip(), "pages": pages,
            "class": args.klass, "how": args.how.strip(), "head_sha": None, "commits": None}


# ---------------------------------------------------------------- approval registration (NFRA_DEVPLN DP-b-5)
# The facts an approval binds are COMPUTED from the portal repository, never taken as arguments: head_sha (the branch tip),
# commits (origin/PROD..<branch>) and overlap (the commits of that range that are also in origin/PROD..origin/DEV). A feature
# cut from DEV carries every DEV commit beneath its own, so an overlap above 0 is refused: a feature is cut from PROD.
REGISTER = "APPROVAL-REGISTER"
PORTAL_PROD, PORTAL_DEV = "refs/remotes/origin/PROD", "refs/remotes/origin/DEV"
LEASE_MODE = "FAST"


class RegisterStop(Exception):
    """A registration refused or unreadable: the reason goes on the APPROVAL-REGISTER line and the tool exits 3."""

    def __init__(self, reason: str, extra: str = ""):
        Exception.__init__(self, reason)
        self.reason = reason
        self.extra = extra


def register_refused(reason: str, extra: str = "") -> int:
    print("%s result=REFUSED reason=%s%s" % (REGISTER, reason, (" " + extra) if extra else ""))
    return 3


def portal_git(portal: str, *args) -> tuple:
    """(rc, stdout) of one read-only git command in the portal repository. A missing path is rc 128, never an empty read."""
    try:
        got = subprocess.run(["git", "-C", portal] + list(args), capture_output=True, text=True, encoding="utf-8",
                             errors="replace")
    except OSError as exc:
        return 127, str(exc)
    return got.returncode, got.stdout


def portal_commit(portal: str, ref: str):
    """The full sha a ref names as a commit, or None. A name that starts with '-' is never handed to git as an option."""
    if not ref or ref.startswith("-"):
        return None
    rc, out = portal_git(portal, "rev-parse", "--verify", "--quiet", ref + "^{commit}")
    return out.strip() if rc == 0 and out.strip() else None


def waiver_tokens(args) -> list:
    """The shas --waive-overlap names, as typed (None when no waiver is given). A ref without a waiver is refused (rc 2).
    Each entry must be a hex commit name; anything else (a count, a range, a wildcard, HEAD~1) is refused waiver-sha-invalid."""
    raw = getattr(args, "waive_overlap", None)
    if raw is None:
        if (getattr(args, "waiver_ref", None) or "").strip():
            raise Refused("--waiver-ref is given without --waive-overlap: a ruling file excuses only the commits it names")
        return None
    tokens = [t.strip() for t in raw.split(",") if t.strip()]
    if not tokens:
        raise RegisterStop("waiver-sha-invalid", "sha=(none named)")
    for t in tokens:
        if not WAIVER_SHA_RE.match(t):
            raise RegisterStop("waiver-sha-invalid", "sha=%s" % t)
    return tokens


def waiver_ref_rel(ref) -> str:
    """The ruling file a waiver rests on, as a repository-relative path. RegisterStop(waiver-ref-missing) when it is absent."""
    ref = (ref or "").strip()
    if not ref:
        raise RegisterStop("waiver-ref-missing", "ref=(none given)")
    cands = [ref] if os.path.isabs(ref) else [os.path.join(os.getcwd(), ref), os.path.join(ROOT, ref)]
    if not any(os.path.isfile(c) for c in cands):
        raise RegisterStop("waiver-ref-missing", "ref=%s" % ref)
    return rel_to_root(ref, ROOT)


def resolve_waiver(portal: str, tokens: list, overlap: list) -> list:
    """The full shas of the named waiver, every one of them a commit of the overlap set (in the order named, no repeats).
    RegisterStop(waiver-sha-unresolved) for a name that is no commit; (waiver-sha-not-in-overlap) for one that is not in the
    overlap set, so a waiver can never excuse a commit it does not name."""
    named = []
    for t in tokens:
        sha = portal_commit(portal, t)
        if sha is None:
            raise RegisterStop("waiver-sha-unresolved", "sha=%s" % t)
        if sha not in overlap:
            raise RegisterStop("waiver-sha-not-in-overlap", "sha=%s" % sha)
        if sha not in named:
            named.append(sha)
    return named


def register_facts(portal: str, branch: str, waive=None, any_commit: bool = False) -> dict:
    """head, commits, overlap and waived of a candidate branch against the portal's origin/PROD and origin/DEV. Read-only.
    The branch is read as origin/<branch>, else as the local branch <branch>, else as the remote-tracking name <branch>;
    with any_commit (--check-only) also as any commit-ish, a bare sha. waive is the list of named shas (or None).
    With no waiver any overlap refuses dev-overlap. With a waiver every overlap commit must be named (else dev-overlap with
    unwaived=<k>), and each named sha must be an overlap commit (else waiver-sha-not-in-overlap).
    Raises RegisterStop with the reason when the branch cannot be registered."""
    rc, _out = portal_git(portal, "rev-parse", "--git-dir")
    if rc != 0:
        raise RegisterStop("portal-not-git", "portal=%s" % portal)
    prod, dev = portal_commit(portal, PORTAL_PROD), portal_commit(portal, PORTAL_DEV)
    if prod is None or dev is None:
        raise RegisterStop("portal-refs-missing", "origin/PROD=%s origin/DEV=%s" % (prod or "absent", dev or "absent"))
    head = None
    names = ["refs/remotes/origin/" + branch, "refs/heads/" + branch, "refs/remotes/" + branch]
    if any_commit:
        names.append(branch)
    for cand in names:
        head = portal_commit(portal, cand)
        if head:
            break
    if head is None:
        raise RegisterStop("branch-not-found", "branch=%s" % branch)
    rc_own, own_out = portal_git(portal, "rev-list", "%s..%s" % (prod, head))
    rc_dev, dev_out = portal_git(portal, "rev-list", "%s..%s" % (prod, dev))
    if rc_own or rc_dev:
        raise RegisterStop("portal-read-failed", "rev-list rc=%d/%d" % (rc_own, rc_dev))
    own = own_out.split()
    if not own:
        raise RegisterStop("empty", "commits=0")
    in_dev = set(dev_out.split())
    over = [c for c in own if c in in_dev]
    if waive is None:
        if over:
            raise RegisterStop("dev-overlap", "overlap=%d commits=%d" % (len(over), len(own)))
        named = []
    else:
        named = resolve_waiver(portal, waive, over)
        unwaived = [c for c in over if c not in named]
        if unwaived:
            raise RegisterStop("dev-overlap", "overlap=%d commits=%d unwaived=%d" % (len(over), len(own), len(unwaived)))
    return {"head": head, "commits": len(own), "overlap": len(over), "waived": named}


def approval_register_facts(args, ap: dict) -> dict:
    """The portal facts for one registration, and the waiver it stores (None without one). RegisterStop(portal-required)
    when --portal is not given; waiver-ref-missing is read before the portal."""
    portal = (getattr(args, "portal", None) or "").strip()
    if not portal:
        raise RegisterStop("portal-required")
    waive = waiver_tokens(args)
    waiver = None
    if waive is not None:
        waiver = {"ref": waiver_ref_rel(getattr(args, "waiver_ref", None))}
    facts = register_facts(portal, ap["branch"], waive=waive, any_commit=bool(getattr(args, "check_only", False)))
    if waiver is not None:
        waiver["shas"] = facts["waived"]
        facts["waiver"] = waiver
    else:
        facts["waiver"] = None
    return facts


def approval_append(args, ap: dict, asked_by: str, source: str, closed=None) -> tuple:
    """Append one approval row to this box's list (one writer per box); the scope is measured as for any call.
    Returns (row id, file written, the list doc, the scope result, the scope notes)."""
    ctx = real_ctx()
    device = this_box(ctx["dev"], ctx["reg"])
    dev_flag = getattr(args, "device", None)
    if ctx["dev"].resolve(ap["box"], ctx["reg"]) != device or (dev_flag and ctx["dev"].resolve(dev_flag, ctx["reg"]) != device):
        raise Refused("REFUSED: an approval for box %s is written to that box's list, and this box is %s. One writer per box." % (
            ap["box"], device))
    orders, roots = getattr(args, "orders", None) or [], getattr(args, "roots", None) or []
    res, notes = scope_project(ctx, args.project, orders, roots)
    path = list_path(device)
    if os.path.exists(path):
        doc = read_list(device)
    else:
        doc = {"schema": SCHEMA, "device": device, "written_at": now_utc(), "written_by": "", "rows": []}
    cid = "%s-%s-%s" % (device, datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ"), secrets.token_hex(2))
    doc["rows"].append({
        "id": cid, "project": args.project,
        "subject": (getattr(args, "subject", None) or "").strip() or "approval: %s" % ap["branch"],
        "asked_by": asked_by, "source": source,
        "orders": [rel_to_root(o, ctx["root"]) for o in orders],
        "roots": [norm(rel_to_root(r, ctx["root"])) for r in roots],
        "state": "CLOSED" if closed else "OPEN", "opened_at": now_utc(), "kind": "approval", "approval": ap,
        "scope": public_scope(res), "closed": closed})
    written = write_list(device, doc, asked_by)
    return cid, written, doc, res, notes


def cmd_add_approval(args) -> int:
    if args.project == NO_PROJECT:
        raise Refused("--project NONE: an approval belongs to a project (--project NFRA_DEVPLN)")
    ap = approval_fields(args, check_only=args.check_only)
    try:
        facts = approval_register_facts(args, ap)
    except RegisterStop as stop:
        return register_refused(stop.reason, stop.extra)
    if args.check_only:
        print("%s result=OK row=- head_sha=%s commits=%d check-only=yes waived=%d" % (
            REGISTER, facts["head"], facts["commits"], len(facts["waived"])))
        return 0
    ap["head_sha"], ap["commits"] = facts["head"], facts["commits"]
    if facts["waiver"] is not None:
        ap["waiver"] = facts["waiver"]
    asked_by = (args.asked_by or "").strip() or writer_serial("")
    if not asked_by:
        raise Refused("--asked-by is required (no OPAL_AGENT_SERIAL to take it from)")
    cid, written, doc, res, notes = approval_append(args, ap, asked_by, (args.source or "").strip() or ap["branch"])
    print("%s result=OK row=%s head_sha=%s commits=%d waived=%d" % (REGISTER, cid, facts["head"], facts["commits"], len(facts["waived"])))
    print("ADDED id=%s kind=approval file=%s open=%d" % (cid, written, sum(1 for r in doc["rows"] if r["state"] == "OPEN")))
    print_scope(res, notes)
    return 0


def lease_live(path, seat: str) -> tuple:
    """(True, '') when path is a live FAST lease of this seat; else (False, why). Reads the file only."""
    if not path or not str(path).strip():
        return False, "no lease file given"
    try:
        with open(path, encoding="utf-8") as fh:
            lease = json.load(fh)
    except OSError as exc:
        return False, "lease unreadable (%s)" % exc
    except ValueError as exc:
        return False, "lease is not JSON (%s)" % exc
    if not isinstance(lease, dict):
        return False, "lease is not an object"
    if lease.get("mode") != LEASE_MODE:
        return False, "lease mode is %r, not %s" % (lease.get("mode"), LEASE_MODE)
    exp = lease.get("expires_epoch")
    if isinstance(exp, bool) or not isinstance(exp, (int, float)):
        return False, "lease expires_epoch is not a number"
    if exp <= time.time():
        return False, "lease expired (expires_epoch %s)" % exp
    if not seat:
        return False, "OPAL_AGENT_SERIAL is unset"
    if lease.get("seat") != seat:
        return False, "lease seat %r is not %s" % (lease.get("seat"), seat)
    return True, ""


def cmd_approval_lease(args) -> int:
    """A live FAST lease of this seat registers its feature with the approval already CLOSED (DP-b-5 item 3)."""
    if args.project == NO_PROJECT:
        raise Refused("--project NONE: an approval belongs to a project (--project NFRA_DEVPLN)")
    ap = approval_fields(args, check_only=False)
    live, why = lease_live(args.lease_file, writer_serial(""))
    if not live:
        return register_refused("lease-not-live", "why=%s" % why)
    try:
        facts = approval_register_facts(args, ap)
    except RegisterStop as stop:
        return register_refused(stop.reason, stop.extra)
    ap["head_sha"], ap["commits"] = facts["head"], facts["commits"]
    if facts["waiver"] is not None:
        ap["waiver"] = facts["waiver"]
    asked_by = (getattr(args, "asked_by", None) or "").strip() or writer_serial("")
    if not asked_by:
        raise Refused("--asked-by is required (no OPAL_AGENT_SERIAL to take it from)")
    lease_rel = rel_to_root(args.lease_file, ROOT)
    closed = {"at": now_utc(), "by": "FAST lease %s" % os.path.basename(args.lease_file), "ruling": lease_rel, "crossbox": None,
              "ruled_by": "lease", "xadj": None, "decision": "approved"}
    cid, _written, _doc, res, notes = approval_append(args, ap, asked_by, lease_rel, closed=closed)
    print("%s result=OK row=%s head_sha=%s commits=%d waived=%d" % (REGISTER, cid, facts["head"], facts["commits"], len(facts["waived"])))
    print("CLOSED id=%s by=%s ruled_by=lease ruling=%s decision=approved" % (cid, closed["by"], lease_rel))
    print_scope(res, notes)
    return 0


def cmd_add(args) -> int:
    if args.kind == "approval":
        return cmd_add_approval(args)
    stray = [f for f, v in (("--box", args.box), ("--branch", args.branch), ("--purpose", args.purpose), ("--pages", args.pages),
                            ("--class", args.klass), ("--how", args.how), ("--portal", args.portal),
                            ("--waive-overlap", args.waive_overlap), ("--waiver-ref", args.waiver_ref)) if v is not None]
    if args.check_only:
        stray.append("--check-only")
    if stray:
        raise Refused("%s is for --kind approval only" % ", ".join(stray))
    for f, v in (("--subject", args.subject), ("--asked-by", args.asked_by), ("--source", args.source), ("--context", args.context)):
        if v is None:
            raise Refused("%s is required for a %s call" % (f, args.kind))
    check_call_text(args.kind, args.context, args.rec, args.source)
    ctx = real_ctx()
    device = this_box(ctx["dev"], ctx["reg"])
    if args.device and ctx["dev"].resolve(args.device, ctx["reg"]) != device:
        raise Refused("REFUSED: a call is written to this box's list only (%s); %s is another box's list. One writer per box." % (
            device, args.device))
    if args.project == NO_PROJECT:
        res = {"paths": "n/a", "placement": "n/a", "resources": "n/a", "shared": "n/a", "risk": "LOCAL",
               "verdict": "NO-PROJECT", "roots": [], "evidence": {}}
        notes = ["--project NONE: the call belongs to no project, so no scope measurement is run"]
    else:
        res, notes = scope_project(ctx, args.project, args.orders or [], args.roots or [])
    path = list_path(device)
    if os.path.exists(path):
        doc = read_list(device)
    else:
        doc = {"schema": SCHEMA, "device": device, "written_at": now_utc(), "written_by": "", "rows": []}
    cid = "%s-%s-%s" % (device, datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ"), secrets.token_hex(2))
    doc["rows"].append({
        "id": cid, "project": args.project, "subject": args.subject, "asked_by": args.asked_by,
        "source": rel_to_root(args.source, ctx["root"]),
        "orders": [rel_to_root(o, ctx["root"]) for o in (args.orders or [])],
        "roots": [norm(rel_to_root(r, ctx["root"])) for r in (args.roots or [])],
        "state": "OPEN", "opened_at": now_utc(), "kind": args.kind,
        "context": args.context.strip(), "rec": (args.rec or "").strip(),
        "scope": public_scope(res) if args.project != NO_PROJECT else dict(res, measured_at=now_utc()), "closed": None})
    written = write_list(device, doc, writer_serial(args.asked_by))
    print("ADDED id=%s kind=%s file=%s open=%d" % (cid, args.kind, written,
                                                   sum(1 for r in doc["rows"] if r["state"] == "OPEN")))
    if args.project == NO_PROJECT:
        print("NOTE: " + notes[0])
        return 0
    print_scope(res, notes)
    if res["verdict"] == "CROSS-BOX":
        print("ROUTE: this call touches another box or a shared set; the box CTO escalates it to cross-adjudication "
              "(.tools/xadj.py open), not a ruling alone. It closes here on a RULED cross-adjudication (close --xadj) or a "
              "CLOSED-BOTH cross-box file.")
    return 0


def print_approval_line(row: dict) -> None:
    ap = row["approval"]
    print("        APPROVAL branch=%s class=%s pages=%s | purpose: %s | how: %s%s" % (
        ap["branch"], ap["class"], ",".join(ap["pages"]), ap["purpose"], ap["how"],
        (" | closed %s by %s" % (row["closed"]["decision"], row["closed"]["by"])) if row.get("closed") else ""))


def print_list(device: str, count: dict) -> None:
    path = list_path(device)
    doc = read_list(device)
    rows = doc["rows"]
    print("FILE %s | device=%s written_by=%s written_at=%s | %s | rows=%d" % (
        path, doc["device"], doc["written_by"], doc["written_at"], age_text(doc["written_at"]), len(rows)))
    for row in rows:
        esc = row.get("escalation")
        print("  %s [%s] %s %s | %s | scope=%s risk=%s | asked_by %s | source %s%s" % (
            row["id"], row["state"], row.get("kind", "fork"), row["project"], row["subject"], row["scope"].get("verdict", "?"),
            row["scope"].get("risk", "?"), row["asked_by"], row["source"],
            (" | escalated to %s %s" % (esc["to"], esc["ref"] or esc["reason"] or "")) if esc else ""))
        if row.get("kind") == "approval":
            print_approval_line(row)
    count["rows"] += len(rows)
    count["open"] += sum(1 for r in rows if r["state"] == "OPEN")


def cmd_list(args) -> int:
    dev = load_mod("opal_devices", "lib/devices.py")
    reg = dev.load()
    count = {"rows": 0, "open": 0}
    absent, refused, read = [], [], 0
    if args.cloud:
        return cmd_list_cloud(args, dev, reg)
    if args.all:
        boxes = dev.names(reg)
    elif args.device:
        box = dev.resolve(args.device, reg)
        if box is None:
            print("ERROR: %r is not a device in the register (holds: %s)" % (args.device, ", ".join(dev.names(reg))), file=sys.stderr)
            return 2
        boxes = [box]
    else:
        boxes = [this_box(dev, reg)]
    for box in boxes:
        if not os.path.exists(list_path(box)):
            absent.append(box)
            print("ABSENT %s: no open_calls.json for %s in this tree (%s). Absent is not empty: nothing here says that box has no open calls." % (
                box, box, list_path(box)))
            continue
        try:
            print_list(box, count)
            read += 1
        except BadFile as exc:
            refused.append(box)
            print("REFUSED %s" % exc)
    print("OPEN-CALLS-LIST boxes=%d read=%d absent=%s refused=%s rows=%d open=%d" % (
        len(boxes), read, ",".join(absent) or "none", ",".join(refused) or "none", count["rows"], count["open"]))
    return 3 if refused else 0


def cmd_publish(args) -> int:
    """Put this box's list, as it stands, to the cluster copy (no row changes; the local file is not rewritten)."""
    dev = load_mod("opal_devices", "lib/devices.py")
    reg = dev.load()
    device = this_box(dev, reg)
    path = list_path(device)
    if not os.path.exists(path):
        print("ABSENT %s: no open_calls.json for %s in this tree (%s); nothing to publish. Absent is not empty." % (
            device, device, path))
        return 0
    doc = read_list(device)
    ok = cloud_put(device, doc)
    print("PUBLISH device=%s rows=%d open=%d cloud=%s" % (device, len(doc["rows"]),
                                                         sum(1 for r in doc["rows"] if r["state"] == "OPEN"),
                                                         "written" if ok else "spooled"))
    return 0


def cmd_list_cloud(args, dev, reg) -> int:
    """Every box's cluster copy, grouped box > project > agent, with timestamps. Absent is named, never shown as empty."""
    cloud_flush()
    if args.device:
        box = dev.resolve(args.device, reg)
        if box is None:
            print("ERROR: %r is not a device in the register" % args.device, file=sys.stderr)
            return 2
        boxes = [box]
    else:
        boxes = dev.names(reg)
    found, absent, refused = cloud_read_all(boxes)
    total = {"open": 0, "closed": 0, "fork": 0, "act": 0}
    print("OPEN CALLS ACROSS THE CLUSTER -- s3://%s/%s/  (read %s)" % (CLOUD_BUCKET, CLOUD_PREFIX, now_utc()))
    print(mode_line(*mode_read(), dev.names(reg)))
    for box in boxes:
        if box in absent:
            print("\n[%s] ABSENT: no cluster copy. Absent is not empty: nothing here says %s has no open calls." % (box, box))
            continue
        if box not in found:
            continue
        doc, modified = found[box]
        rows = doc["rows"]
        shown = [r for r in rows if args.include_closed or r["state"] == "OPEN"]
        n_open = sum(1 for r in rows if r["state"] == "OPEN")
        total["open"] += n_open
        total["closed"] += len(rows) - n_open
        print("\n[%s] open=%d closed=%d | list written %s by %s (%s) | cloud copy %s" % (
            box, n_open, len(rows) - n_open, doc["written_at"], doc["written_by"], age_text(doc["written_at"]), modified))
        by_project = {}
        for r in shown:
            by_project.setdefault(r["project"], {}).setdefault(r["asked_by"], []).append(r)
        for project in sorted(by_project):
            print("  %s" % project)
            for agent in sorted(by_project[project]):
                print("    %s" % agent)
                for r in sorted(by_project[project][agent], key=lambda x: x["opened_at"]):
                    kind = r.get("kind", "fork")
                    if r["state"] == "OPEN":
                        total[kind] = total.get(kind, 0) + 1
                    print("      %s [%s] %-4s opened %s (%s) | %s | scope=%s | %s" % (
                        r["id"], r["state"], kind, r["opened_at"], age_text(r["opened_at"]), r["subject"],
                        r["scope"].get("verdict", "?"), r["source"]))
                    if kind == "approval":
                        print_approval_line(r)
                        continue
                    print("        CONTEXT: %s" % (r.get("context") or "(none: written before the context field)"))
                    if kind == "fork":
                        print("        REC: %s" % (r.get("rec") or "(none)"))
    for box, why in refused:
        print("\n[%s] REFUSED: %s" % (box, why))
    print("\nOPEN-CALLS-CLUSTER boxes=%d read=%d absent=%s refused=%s open=%d (fork %d, act %d) closed=%d" % (
        len(boxes), len(found), ",".join(absent) or "none", ",".join(b for b, _ in refused) or "none",
        total["open"], total.get("fork", 0), total.get("act", 0), total["closed"]))
    return 3 if refused else 0


def crossbox_closed_both(call_id: str, explicit) -> tuple:
    """(file name or None, lines): a cross-box file for this call that reads CLOSED-BOTH."""
    lines, found = [], None
    files = sorted(glob.glob(os.path.join(crossbox_root(), "*.json")))
    if not files:
        lines.append("no cross-box file under %s (0 files)" % crossbox_root())
    for path in files:
        name = os.path.basename(path)
        try:
            data = json.load(open(path, encoding="utf-8"))
        except (OSError, ValueError) as exc:
            lines.append("%s unreadable (%s): cannot prove CLOSED-BOTH" % (name, type(exc).__name__))
            continue
        text = json.dumps(data)
        body = ""
        if isinstance(data, dict) and data.get("body_path"):
            try:
                body = open(os.path.join(ROOT, data["body_path"]), encoding="utf-8", errors="replace").read()
            except OSError:
                body = ""
        names_call = (explicit and data.get("id") == explicit) or call_id in text or call_id in body
        state = str(data.get("state", "")).upper() if isinstance(data, dict) else ""
        if not names_call:
            continue
        lines.append("%s names the call, state %s" % (name, state or "(none)"))
        if state == "CLOSED-BOTH" and found is None:
            found = name
    return found, lines


def cmd_close(args) -> int:
    dev = load_mod("opal_devices", "lib/devices.py")
    reg = dev.load()
    device = this_box(dev, reg)
    path = list_path(device)
    row = None
    doc = read_list(device) if os.path.exists(path) else {"rows": []}
    for r in doc["rows"]:
        if r["id"] == args.id:
            row = r
    if row is None:
        for box in dev.names(reg):
            if box != device and os.path.exists(list_path(box)):
                try:
                    if any(r["id"] == args.id for r in read_list(box)["rows"]):
                        raise Refused("REFUSED: call %s is on %s's list; this box (%s) writes its own list only. One writer per box." % (
                            args.id, box, device))
                except BadFile:
                    continue
        raise Refused("REFUSED: no call %s on this box's list (%s)" % (args.id, path))
    approval = row.get("kind") == "approval"
    decision = getattr(args, "decision", None)
    if decision == APPROVAL_WITHDRAWN and approval and row["state"] == "CLOSED":
        # DP-e-1: a withdraw ends only an OPEN row. Refused rc 2 here, before any write, naming the decision it would overwrite.
        print("REFUSED: row %s is already closed (%s); a withdraw ends only an OPEN row" % (
            args.id, (row.get("closed") or {}).get("decision") or "-"), file=sys.stderr)
        return 2
    if row["state"] == "CLOSED":
        raise Refused("REFUSED: call %s is already CLOSED" % args.id)
    if approval:
        # an approval row: the decision is required; the closing identity is Andrew's word or this box's CTO serial
        if decision not in APPROVAL_CLOSE_DECISIONS:
            raise Refused("REFUSED: call %s is an approval row: --decision approved|declined|withdrawn is required" % args.id)
        if (getattr(args, "ruled_by", "cto") or "cto") not in APPROVAL_RULED_BY:
            raise Refused("REFUSED: an approval is ruled by andrew or cto, not %s" % args.ruled_by)
        if getattr(args, "xadj", None):
            raise Refused("REFUSED: --xadj does not apply to an approval row (its validity is read by approval-status)")
        if args.ruled_by == "cto":
            by = os.environ.get("OPAL_AGENT_SERIAL", "").strip()
            if not by:
                raise Refused("REFUSED: --ruled-by cto closes as the serial in OPAL_AGENT_SERIAL, which is unset")
        else:
            by = "andrew"
    else:
        if decision is not None:
            raise Refused("REFUSED: --decision is for an approval row; call %s is kind %s" % (args.id, row.get("kind", "fork")))
        if not args.by:
            raise Refused("--by is required to close a %s call" % row.get("kind", "fork"))
        by = args.by
    ruling = args.ruling if os.path.isabs(args.ruling) else (
        os.path.join(os.getcwd(), args.ruling) if os.path.exists(os.path.join(os.getcwd(), args.ruling)) else os.path.join(ROOT, args.ruling))
    if not os.path.isfile(ruling):
        raise Refused("REFUSED: ruling %s is not a file; a closure cites the ruling it rests on" % args.ruling)
    cross = None
    xid = None
    ruled_by = getattr(args, "ruled_by", "cto") or "cto"
    if getattr(args, "xadj", None):
        xa = load_mod("opal_xadj", ".tools/xadj.py")
        try:
            xdoc = xa.get(args.xadj)
        except xa.Refused as exc:
            raise Refused(str(exc) if str(exc).startswith("REFUSED") else "REFUSED: %s" % exc)
        if xdoc["call_id"] != row["id"] or xdoc["state"] != "RULED":
            raise Refused("REFUSED: cross-adjudication %s is %s for call %s, not RULED for %s" % (
                args.xadj, xdoc["state"], xdoc["call_id"], row["id"]))
        xid = xdoc["id"]
    if ruled_by == "cluster-lead":
        rel = rel_to_root(ruling, ROOT).replace("\\", "/")
        if not rel.startswith(CLUSTER_LEAD_RULING_PREFIXES):
            raise Refused("REFUSED: a cluster-lead close cites the laptop CTO's own record or a RULED cross-adjudication file "
                          "(under %s); %s is neither" % (" or ".join(CLUSTER_LEAD_RULING_PREFIXES), rel))
    # an approval row is not gated by the cross-box file: its scope reads the whole project (the round's orders), so every
    # approval of a project that touches the trunk reads CROSS-BOX; the call's validity is read by approval-status instead
    if row["scope"].get("verdict") == "CROSS-BOX" and ruled_by not in ("andrew", "cluster-lead") and xid is None and not approval:
        found, lines = crossbox_closed_both(row["id"], args.crossbox)
        if found is None:
            raise Refused("REFUSED: call %s reads CROSS-BOX and no cross-box file for it reads CLOSED-BOTH (%s). A call that touches "
                          "another box is not settled alone." % (args.id, "; ".join(lines) or "none looked at"))
        cross = os.path.splitext(found)[0]
    row["state"] = "CLOSED"
    row["closed"] = {"at": now_utc(), "by": by, "ruling": rel_to_root(args.ruling, ROOT), "crossbox": cross,
                     "ruled_by": ruled_by, "xadj": xid}
    if approval:
        row["closed"]["decision"] = decision
    write_list(device, doc, writer_serial(by))
    why = cross or ("cross-adjudication %s RULED" % xid if xid else None) or (
        "not required (approval row: validity is read by approval-status)" if approval else
        "not required (Andrew's ruling)" if ruled_by == "andrew" else
        "not required (cluster-lead record)" if ruled_by == "cluster-lead" else "not required (OWN-BOX)")
    print("CLOSED id=%s by=%s ruled_by=%s ruling=%s crossbox=%s%s" % (args.id, by, ruled_by, row["closed"]["ruling"], why,
                                                               (" decision=%s" % decision) if approval else ""))
    return 0


def set_escalation(device: str, cid: str, esc: dict, serial: str) -> str:
    """Mark an OPEN row escalated (xadj.py open, or `hold`); the box's scan stops nudging its CTO for it."""
    doc = read_list(device)
    row = next((r for r in doc["rows"] if r["id"] == cid), None)
    if row is None:
        raise Refused("REFUSED: no call %s on this box's list (%s)" % (cid, list_path(device)))
    if row["state"] != "OPEN":
        raise Refused("REFUSED: call %s is %s" % (cid, row["state"]))
    if set(esc) != ESC_KEYS or esc["to"] not in ESC_TO:
        raise Refused("REFUSED: escalation %r is malformed" % esc)
    row["escalation"] = esc
    return write_list(device, doc, writer_serial(serial))


def cmd_lift(args) -> int:
    """Lift a hold for Andrew on a ruling: the hold's text stays on the row (to=lifted, reason = the hold's own line)."""
    dev = load_mod("opal_devices", "lib/devices.py")
    device = this_box(dev, dev.load())
    doc = read_list(device)
    row = next((r for r in doc["rows"] if r["id"] == args.id), None)
    if row is None:
        raise Refused("REFUSED: no call %s on this box's list (%s)" % (args.id, list_path(device)))
    esc = row.get("escalation")
    if row["state"] != "OPEN" or not esc or esc.get("to") != "andrew":
        raise Refused("REFUSED: call %s is not an OPEN row held for Andrew (state %s, escalation %s)" % (
            args.id, row["state"], (esc or {}).get("to")))
    ruling = args.ruling if os.path.isabs(args.ruling) else os.path.join(ROOT, args.ruling)
    if not os.path.isfile(ruling):
        raise Refused("REFUSED: ruling %s is not a file; a lift cites the ruling it rests on" % args.ruling)
    was = "held for andrew by %s at %s: %s" % (esc.get("by"), esc.get("at"), esc.get("reason"))
    path = set_escalation(device, args.id, {"to": "lifted", "ref": rel_to_root(ruling, ROOT), "at": now_utc(), "by": args.by,
                                            "reason": was}, args.by)
    print("LIFTED id=%s by=%s ruling=%s file=%s (the row is OPEN again; close it on the same ruling)" % (
        args.id, args.by, rel_to_root(ruling, ROOT), path))
    return 0


def cmd_hold(args) -> int:
    dev = load_mod("opal_devices", "lib/devices.py")
    device = this_box(dev, dev.load())
    path = set_escalation(device, args.id, {"to": "andrew", "ref": None, "at": now_utc(), "by": args.by,
                                            "reason": args.reason}, args.by)
    print("HELD id=%s for Andrew by=%s file=%s (the scan no longer nudges the CTO for it; /open-calls carries it)" % (
        args.id, args.by, path))
    return 0


# ---------------------------------------------------------------- approval-status (NFRA_DEVPLN DP-b-1)

def approval_read(box: str, store_dir) -> tuple:
    """(doc, where): the box's list from --store-dir, else the working tree, else origin/box/<box>. Raises BadFile naming the
    store when it cannot be read: an unreadable store is never read as an absent one."""
    if store_dir:
        where = os.path.join(store_dir, box, "open_calls.json")
        try:
            text = open(where, encoding="utf-8").read()
        except OSError as exc:
            raise BadFile("%s: unreadable (%s)" % (where, exc))
    elif os.path.isfile(list_path(box)):
        where = list_path(box)
        try:
            text = open(where, encoding="utf-8").read()
        except OSError as exc:
            raise BadFile("%s: unreadable (%s)" % (where, exc))
    else:
        where = "origin/box/%s:org/devices/state/%s/open_calls.json" % (box, box)
        try:
            got = subprocess.run(["git", "-C", ROOT, "show", where], capture_output=True, text=True, encoding="utf-8",
                                 errors="replace")
        except OSError as exc:
            raise BadFile("%s: git unavailable (%s)" % (where, exc))
        if got.returncode != 0:
            raise BadFile("%s: no working-tree list and git show failed (rc %d: %s)" % (
                where, got.returncode, got.stderr.strip()[:200]))
        text = got.stdout
    try:
        doc = json.loads(text)
    except ValueError as exc:
        raise BadFile("%s: not JSON (%s)" % (where, exc))
    return validate_doc(doc, box, where), where


def approval_class_ok(klass: str, by: str) -> bool:
    """The class rule (decomposition R3): test-only accepts any APPROVED; client-facing needs Andrew or a FAST lease;
    opal-internal needs Andrew, a _SA_CTO serial, or a FAST lease."""
    if klass == "test-only":
        return True
    who = by or ""
    if who.lower() == "andrew" or who.startswith("FAST lease"):
        return True
    return klass == "opal-internal" and "_SA_CTO" in who


def cmd_approval_status(args) -> int:
    branch = args.branch.strip()
    m = APPROVAL_BRANCH_RE.match(branch)
    if not m:
        print("ERROR: --branch %r is not cand/<box>/<slug>" % args.branch, file=sys.stderr)
        return 2
    box = m.group(1)

    def line(state, valid, row, by, head, commits, klass, pages, why=None):
        out = "APPROVAL branch=%s state=%s valid=%s row=%s by=%s head_sha=%s commits=%s class=%s box=%s pages=%s" % (
            branch, state, valid, row, by, head, commits, klass, box, pages)
        return out + (" why=%s" % why.replace("\n", " ") if why else "")

    try:
        doc, _where = approval_read(box, args.store_dir)
    except BadFile as exc:
        print(line("UNREADABLE", "-", "-", "-", "-", "-", "-", "-", why=str(exc)))
        return 2
    # a withdrawn row (DP-e-1) is not a decision and is skipped: the newest NON-withdrawn row wins
    rows = [r for r in doc["rows"] if r.get("kind") == "approval" and r["approval"]["branch"] == branch
            and (r.get("closed") or {}).get("decision") != APPROVAL_WITHDRAWN]
    if not rows:
        print(line("ABSENT", "-", "-", "-", "-", "-", "-", "-"))
        return 0
    # the newest row by opened_at wins; a tie goes to the later row in the file
    row = max(enumerate(rows), key=lambda t: (t[1]["opened_at"], t[0]))[1]
    ap, closed = row["approval"], (row.get("closed") or {})
    head = "-" if ap["head_sha"] is None else str(ap["head_sha"])
    commits = "-" if ap["commits"] is None else str(ap["commits"])
    pages = ",".join(ap["pages"]) or "-"
    if row["state"] == "OPEN":
        print(line("OPEN", "-", row["id"], "-", head, commits, ap["class"], pages))
        return 0
    by = closed.get("by") or "-"
    if closed["decision"] == "approved":
        valid = "yes" if approval_class_ok(ap["class"], closed.get("by")) else "no"
        print(line("APPROVED", valid, row["id"], by, head, commits, ap["class"], pages))
    else:
        print(line("DECLINED", "no", row["id"], by, head, commits, ap["class"], pages))
    return 0


# ---------------------------------------------------------------- selftest

class Scratch:
    """Files this run creates in a temporary directory; cleanup removes them by name, then the empty directories."""

    def __init__(self):
        self.base = tempfile.mkdtemp(prefix="opalcalls_")
        self.files, self.dirs = [], [self.base]

    def write(self, rel: str, text: str) -> str:
        path = os.path.join(self.base, rel)
        d = os.path.dirname(path)
        chain = []
        while d != self.base and not os.path.isdir(d):
            chain.append(d)
            d = os.path.dirname(d)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.dirs.extend(reversed(chain))
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        self.files.append(path)
        return path

    def cleanup(self):
        for f in self.files:
            try:
                os.remove(f)
            except OSError:
                pass
        for d in reversed(self.dirs):
            try:
                os.rmdir(d)
            except OSError:
                pass


def close_path_cases(device: str) -> list:
    """The close rule (msg 107148): Andrew's ruling closes a CROSS-BOX row; a CTO ruling needs CLOSED-BOTH."""
    out = []
    keep = {k: os.environ.get(k) for k in ("OPAL_STATE_ROOT", "OPAL_CROSSBOX_ROOT")}
    base = tempfile.mkdtemp(prefix="opalcalls_close_")
    made = []
    try:
        os.environ["OPAL_STATE_ROOT"] = os.path.join(base, "state")
        os.environ["OPAL_CROSSBOX_ROOT"] = os.path.join(base, "crossbox")
        ruling = os.path.join(base, "RULING.md")
        with open(ruling, "w", encoding="utf-8") as fh:
            fh.write("ruling\n")
        made.append(ruling)

        def row(cid):
            return {"id": cid, "project": "P", "subject": "s", "asked_by": "x", "source": "s", "orders": [], "roots": [],
                    "state": "OPEN", "opened_at": now_utc(), "kind": "fork", "scope": {"verdict": "CROSS-BOX"},
                    "closed": None}
        doc = {"schema": SCHEMA, "device": device, "written_at": now_utc(), "written_by": "t",
               "rows": [row("c-andrew"), row("c-cto")]}
        made.append(write_list(device, doc, "selftest"))

        class A:
            pass
        a = A()
        a.id, a.by, a.ruling, a.crossbox, a.ruled_by = "c-andrew", "selftest", ruling, None, "andrew"
        ok = cmd_close(a) == 0 and read_list(device)["rows"][0]["state"] == "CLOSED" and \
            read_list(device)["rows"][0]["closed"]["ruled_by"] == "andrew"
        out.append(("an Andrew ruling closes a CROSS-BOX row with no cross-box file", ok))
        a.id, a.ruled_by = "c-cto", "cto"
        try:
            cmd_close(a)
            refused = False
        except Refused:
            refused = True
        out.append(("a CTO ruling on a CROSS-BOX row is still refused without CLOSED-BOTH",
                    refused and read_list(device)["rows"][1]["state"] == "OPEN"))
        # escalation + the cross-adjudication close (Andrew-direct 2026-10-09 ~00:0xZ)
        xa = load_mod("opal_xadj", ".tools/xadj.py")
        os.environ["OPAL_XADJ_LOCAL"] = os.path.join(base, "xadj")
        xid = "XA-20261009T000000Z-0c7a"
        xdoc = {"schema": xa.SCHEMA, "id": xid, "call_id": "c-cto", "project": "P", "subject": "s", "scope_verdict": "CROSS-BOX",
                "from_device": device, "from_serial": "t", "opened_at": now_utc(), "body": "b", "state": "OPEN", "ruling": None}
        xa._put(xa.key_of(xid), xdoc)
        set_escalation(device, "c-cto", {"to": "xadj", "ref": xid, "at": now_utc(), "by": "t", "reason": None}, "t")
        out.append(("an escalation is written on the row and read back valid",
                    read_list(device)["rows"][1]["escalation"]["ref"] == xid))
        a.xadj = xid
        try:
            cmd_close(a)
            refused = False
        except Refused:
            refused = True
        out.append(("a close on a cross-adjudication still OPEN is refused", refused))
        xa._put(xa.key_of(xid), dict(xdoc, state="RULED", ruling={"at": now_utc(), "by": "1.0.0_SA_CTO", "device": "laptop",
                                                                   "text": "(a)", "record": "r.md"}))
        ok = cmd_close(a) == 0 and read_list(device)["rows"][1]["closed"]["xadj"] == xid
        out.append(("a RULED cross-adjudication closes a CTO-ruled CROSS-BOX row", ok))
        try:
            set_escalation(device, "c-cto", {"to": "nowhere", "ref": None, "at": "", "by": "", "reason": None}, "t")
            refused = False
        except Refused:
            refused = True
        out.append(("a malformed escalation is refused", refused))
        # lift + cluster-lead close (Andrew-direct 2026-10-11 ~03:2xZ, cluster-lead deputation; tool gap found 2026-10-12)
        doc = read_list(device)
        doc["rows"].append(row("c-held"))
        write_list(device, doc, "selftest")
        a.id, a.by, a.ruling = "c-held", "t", ruling
        try:
            cmd_lift(a)
            refused = False
        except Refused:
            refused = True
        out.append(("a lift on a row not held for Andrew is refused", refused))
        set_escalation(device, "c-held", {"to": "andrew", "ref": None, "at": now_utc(), "by": "t", "reason": "money"}, "t")
        esc_after = (cmd_lift(a) == 0 and read_list(device)["rows"][2]["escalation"]) or {}
        out.append(("a lift on a held row records to=lifted with the hold's own line kept",
                    esc_after.get("to") == "lifted" and "money" in str(esc_after.get("reason"))))
        a.ruled_by, a.xadj = "cluster-lead", None
        try:
            cmd_close(a)
            refused = False
        except Refused:
            refused = True
        out.append(("a cluster-lead close citing a ruling outside the CTO's records is refused",
                    refused and read_list(device)["rows"][2]["state"] == "OPEN"))
        cl_dir = os.path.join(ROOT, "org", "tier1_exec", "1.0.0_SA_CTO", "deliverables")
        cl_ruling = os.path.join(cl_dir, ".selftest_cluster_lead_%s.md" % secrets.token_hex(3))
        with open(cl_ruling, "w", encoding="utf-8") as fh:
            fh.write("selftest ruling" + chr(10))
        made.append(cl_ruling)
        a.ruling = cl_ruling
        ok = cmd_close(a) == 0 and read_list(device)["rows"][2]["state"] == "CLOSED" and             read_list(device)["rows"][2]["closed"]["ruled_by"] == "cluster-lead"
        out.append(("a cluster-lead close on the CTO's own record closes a CROSS-BOX row with no cross-box file", ok))
        # context + rec (Andrew-direct 2026-10-09 ~01:1xZ)
        ctx_ok = "Created by round 8's drain; gates BF-w-2's cut and the FWD-6 switch."

        def refuses(*a):
            try:
                check_call_text(*a)
                return False
            except Refused:
                return True
        out.append(("a fork with context and rec from a committed file is admitted",
                    not refuses("fork", ctx_ok, "(a) yes, because x", "org/missions/D1/X/X/ledger/R.md")))
        out.append(("a call with no context is refused", refuses("fork", "", "(a)", "org/x.md")))
        out.append(("a one-word context is refused (too short to be context)", refuses("fork", "see file", "(a)", "org/x.md")))
        out.append(("a fork with no rec is refused; an act needs none", refuses("fork", ctx_ok, "", "org/x.md")
                    and not refuses("act", ctx_ok, "", "org/x.md")))
        out.append(("an inbox-message source is refused (box-local mail)",
                    refuses("fork", ctx_ok, "(a)", "org/mcp/inbox/1.0.0_SA_CTO/~DELL2/read/m.md")))
        # the keep-driving switch
        os.environ["OPAL_MODE_LOCAL"] = os.path.join(base, "mode.json")
        doc0, src0 = mode_read()
        out.append(("an absent switch reads ON for every part", doc0 is None and src0 == "absent"
                    and mode_state(doc0, device, "scan") == "on" and mode_state(doc0, device, "empty_tick") == "on"))
        m = {"schema": MODE_SCHEMA, "scan": "on", "empty_tick": "off", "boxes": {device: {"scan": "off"}}, "set_by": "t",
             "set_at": now_utc(), "reason": "r"}
        mode_write(m)
        d1, s1 = mode_read()
        out.append(("a box override beats the global value; the global value holds elsewhere",
                    s1 == "object" and mode_state(d1, device, "scan") == "off" and mode_state(d1, "elsewhere", "scan") == "on"
                    and mode_state(d1, device, "empty_tick") == "off"))
        with open(os.environ["OPAL_MODE_LOCAL"], "w") as fh:
            fh.write("{not json")
        d2, s2 = mode_read()
        out.append(("an unreadable switch reads ON, never off", d2 is None and s2.startswith("unreadable")
                    and mode_state(d2, device, "scan") == "on"))
    finally:
        os.environ.pop("OPAL_XADJ_LOCAL", None)
        os.environ.pop("OPAL_MODE_LOCAL", None)
        try:
            os.remove(os.path.join(base, "mode.json"))
        except OSError:
            pass
        import shutil
        shutil.rmtree(os.path.join(base, "xadj"), ignore_errors=True)
        for k, v in keep.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        for f in made:
            try:
                os.remove(f)
            except OSError:
                pass
        for d in (os.path.join(base, "state", device), os.path.join(base, "state"), base):
            try:
                os.rmdir(d)
            except OSError:
                pass
    return out


def selftest() -> int:
    dev = load_mod("opal_devices", "lib/devices.py")
    pc = load_mod("opal_placement_check", ".tools/placement-check.py")
    try:
        names = dev.names(dev.load())
    except Exception as exc:
        print("ERROR: device register unreadable (%s)" % exc, file=sys.stderr)
        return 3
    if len(names) < 2:
        print("ERROR: the self-test needs two boxes in the register", file=sys.stderr)
        return 3
    here, there = names[0], names[1]
    sc = Scratch()
    cases = []
    try:
        tf = "infra/aws/terraform/"
        res = lambda block: 'resource "aws_s3_bucket" "x" {\n  bucket = "%s"\n}\n' % block   # noqa: E731
        sc.write(tf + "rootA/main.tf", res("bkt-a-only"))
        sc.write(tf + "rootB/main.tf", res("bkt-b-only") + res("bkt-common"))
        sc.write(tf + "rootC/main.tf", res("bkt-common"))
        sc.write(tf + "rootS/main.tf", res("bkt-shared"))
        sc.write(tf + "rootP/main.tf", 'resource "aws_iam_policy" "p" {\n  policy = "arn:aws:s3:::bkt-shared/*"\n}\n')
        sc.write(tf + "rootT/main.tf", 'terraform {\n  backend "s3" {\n    bucket = "bkt-state"\n  }\n}\n'
                 'resource "aws_s3_bucket" "x" {\n  bucket = "bkt-t-only"\n}\n')
        sc.write(tf + "rootU/main.tf", 'terraform {\n  backend "s3" {\n    bucket = "bkt-state"\n  }\n}\n'
                 'resource "aws_s3_bucket" "x" {\n  bucket = "bkt-u-only"\n}\n')
        sc.write("org/missions/DY/N/THEIRS/task-orders/o1.md", "<status>issued</status>\n<risk>SERVED</risk>\n<paths>\ndata/theirs/x.py\n</paths>\n")
        sc.write("org/missions/DY/N/THEIRS/task-orders/o2.md", "<status>complete</status>\n<risk>WORLD</risk>\n<paths>\ndata/done/y.py\n</paths>\n")
        projects = [
            {"code": "MINE", "box": here, "home": "org/missions/DX/M/MINE", "writes": ["org/missions/DX/M/MINE", "data/mine"]},
            {"code": "SAMEBOX", "box": here, "home": "org/missions/DZ/O/SAMEBOX", "writes": ["org/missions/DZ/O/SAMEBOX"]},
            {"code": "THEIRS", "box": there, "home": "org/missions/DY/N/THEIRS",
             "writes": ["org/missions/DY/N/THEIRS", "data/theirs/x.py", tf + "rootB"]},
            {"code": "NOBOX", "box": None, "home": "org/missions/DW/K/NOBOX", "writes": ["org/missions/DW/K/NOBOX"]}]
        ctx = {"root": sc.base, "device": here, "projects": projects, "overlaps": pc.overlaps, "rootmap_keys": [],
               "shared_buckets": {"bkt-shared"}, "shared_basis": "fixture", "pc": pc}

        def flags(r):
            return (r["paths"], r["placement"], r["resources"], r["shared"], r["risk"], r["verdict"])

        r = measure(ctx, "MINE", here, ["data/mine/x.py"], [tf + "rootA"], ["LOCAL"])
        cases.append(("a clear case reads OWN-BOX with every reading clear",
                      flags(r) == ("clear", "clear", "clear", "clear", "LOCAL", "OWN-BOX")))
        r = measure(ctx, "MINE", here, ["data/theirs/x.py"], [], ["LOCAL"])
        cases.append(("a path in another box's project write set is a PATHS hit", r["paths"] == "hit" and r["verdict"] == "CROSS-BOX"))
        r = measure(ctx, "MINE", here, ["org/missions/DZ/O/SAMEBOX/notes.md"], [], ["LOCAL"])
        cases.append(("a path under another project's home is a PATHS hit even on the same box", r["paths"] == "hit"))
        r = measure(ctx, "MINE", here, ["data/mine2/x.py"], [], ["LOCAL"])
        cases.append(("a sibling path that only shares a name prefix is clear", r["paths"] == "clear" and r["verdict"] == "OWN-BOX"))
        r = measure(ctx, "THEIRS", there, ["data/other/x.py"], [], ["LOCAL"])
        cases.append(("a project placed on another box is a PLACEMENT hit", r["placement"] == "hit" and r["verdict"] == "CROSS-BOX"))
        r = measure(ctx, "NOBOX", None, [], [], ["LOCAL"])
        cases.append(("a project with no resolvable box is a PLACEMENT hit, never guessed OWN-BOX", r["placement"] == "hit"))
        r = measure(ctx, "MINE", here, [], [tf + "rootC"], ["LOCAL"])
        cases.append(("a bucket both boxes' projects name is a RESOURCES hit",
                      r["resources"] == "hit" and r["verdict"] == "CROSS-BOX" and "bkt-common" in " ".join(r["evidence"]["resources"])))
        r = measure(ctx, "MINE", here, [], [tf + "rootT"], ["LOCAL"])
        r2 = measure(ctx, "MINE", here, [], [tf + "rootU"], ["LOCAL"])
        cases.append(("a backend bucket both roots name is not a declared resource (no false RESOURCES hit)",
                      r["resources"] == "clear" and r2["resources"] == "clear"))
        r = measure(ctx, "MINE", here, [], [tf + "rootGONE"], ["LOCAL"])
        cases.append(("a named root that cannot be read is a RESOURCES hit, not clear", r["resources"] == "hit"))
        r = measure(ctx, "MINE", here, [tf + "rootA/main.tf"], [], ["LOCAL"])
        cases.append(("a Terraform root is inferred from an order path under infra/aws/terraform",
                      r["roots"] == [tf + "rootA"]))
        r = measure(ctx, "MINE", here, [".tools/anything.py"], [], ["LOCAL"])
        cases.append(("a path on the shared branch is a SHARED hit", r["shared"] == "hit" and r["verdict"] == "CROSS-BOX"))
        r = measure(ctx, "MINE", here, ["CLAUDE.md"], [], ["LOCAL"])
        cases.append(("a trunk register file is a SHARED hit", r["shared"] == "hit"))
        r = measure(ctx, "MINE", here, [], [tf + "rootS"], ["LOCAL"])
        cases.append(("a bucket the registry marks shared is a SHARED hit", r["shared"] == "hit" and r["verdict"] == "CROSS-BOX"))
        r = measure(ctx, "MINE", here, [], [tf + "rootP"], ["LOCAL"])
        cases.append(("a shared bucket named only in a policy ARN is a SHARED hit", r["shared"] == "hit"))
        r = measure(ctx, "MINE", here, ["data/mine/x.py"], [], ["WORLD", "LOCAL"])
        cases.append(("WORLD risk is printed and does not alone make a call cross-box",
                      r["risk"] == "WORLD" and r["verdict"] == "OWN-BOX"))
        cases.append(("the highest risk wins and an empty list reads LOCAL",
                      highest_risk(["LOCAL", "SERVED"]) == "SERVED" and highest_risk([]) == "LOCAL"))
        facts = order_facts(open(os.path.join(sc.base, "org/missions/DY/N/THEIRS/task-orders/o1.md")).read(), pc)
        cases.append(("an order's paths, risk and status are read with placement-check's patterns",
                      facts == (["data/theirs/x.py"], "SERVED", "issued")))
        line = scope_line(measure(ctx, "MINE", here, [], [], ["LOCAL"]))
        cases.append(("the last line has the named shape", bool(re.match(
            r"^CALL-SCOPE project=\S+ device=\S+ paths=(clear|hit) placement=(clear|hit) resources=(clear|hit) "
            r"shared=(clear|hit) risk=(LOCAL|SERVED|WORLD) verdict=(OWN-BOX|CROSS-BOX)$", line))))
        cases.extend(close_path_cases(here))
    finally:
        sc.cleanup()
    fails = 0
    for label, ok in cases:
        print("  %s  %s" % ("PASS" if ok else "FAIL", label))
        fails += 0 if ok else 1
    print("CALL-SCOPE-SELFTEST cases=%d/%d ok=%s" % (len(cases) - fails, len(cases), fails == 0))
    return 1 if fails else 0


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="open-calls.py", description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    add = sub.add_parser("add", help="append one call to this box's list")
    add.add_argument("--project", required=True)
    # --subject, --asked-by, --source and --context are required for a fork or act (checked in cmd_add); an approval takes
    # them from its own flags (--subject optional; --asked-by defaults to OPAL_AGENT_SERIAL; --source defaults to the branch)
    add.add_argument("--subject")
    add.add_argument("--asked-by")
    add.add_argument("--source")
    add.add_argument("--orders", nargs="+", default=[])
    add.add_argument("--roots", nargs="+", default=[])
    add.add_argument("--device", help="refused unless it is this box (one writer per box)")
    add.add_argument("--context",
                     help="2-3 lines (%d-%d chars): what created the call and what it gates" % (CONTEXT_MIN, CONTEXT_MAX))
    add.add_argument("--rec", help="the asking seat's recommendation and its why (required on a fork)")
    add.add_argument("--kind", choices=KINDS, default="fork",
                     help="fork = a decision with options (default); act = an act only Andrew can do; "
                          "approval = a portal feature waiting for his yes or no (NFRA_DEVPLN)")
    add.add_argument("--box", help="approval: the box whose branch this is (must be this box)")
    add.add_argument("--branch", help="approval: cand/<box>/<slug>, the candidate branch")
    add.add_argument("--purpose", help="approval: what the feature is, in words")
    add.add_argument("--pages", help="approval: the portal pages it touches, comma separated")
    add.add_argument("--class", dest="klass", choices=APPROVAL_CLASSES,
                     help="approval: client-facing | opal-internal | test-only")
    add.add_argument("--how", help="approval: how to look at it")
    add.add_argument("--portal", help="approval (required): the portal repository; origin/PROD, origin/DEV and the branch are read")
    add.add_argument("--check-only", action="store_true", dest="check_only",
                     help="approval: run the registration checks and print the APPROVAL-REGISTER line; write nothing")
    add.add_argument("--waive-overlap", dest="waive_overlap",
                     help="approval: comma-separated full or abbreviated shas excused from the DEV-overlap refusal (named, never a count)")
    add.add_argument("--waiver-ref", dest="waiver_ref",
                     help="approval: the ruling file that names the waived commits (required with --waive-overlap; must exist)")
    lst = sub.add_parser("list", help="print the list(s) with each file's age")
    grp = lst.add_mutually_exclusive_group()
    grp.add_argument("--device")
    grp.add_argument("--all", action="store_true")
    lst.add_argument("--cloud", action="store_true", help="read every box's cluster copy in S3 (no git lag)")
    lst.add_argument("--include-closed", action="store_true", help="with --cloud: show CLOSED rows too")
    sub.add_parser("publish", help="put this box's current list to the cluster copy in S3, unchanged")
    cls = sub.add_parser("close", help="set a call CLOSED with its ruling")
    cls.add_argument("--id", required=True)
    # --by is required for a fork or act; an approval row takes its closing identity from --ruled-by (checked in cmd_close)
    cls.add_argument("--by")
    cls.add_argument("--ruling", "--ruling-file", dest="ruling", required=True)
    cls.add_argument("--decision", choices=APPROVAL_CLOSE_DECISIONS,
                     help="approval rows only (required there, refused on any other kind): approved | declined | withdrawn "
                          "(withdrawn ends an OPEN duplicate row, not a decision; refused on a closed row)")
    cls.add_argument("--crossbox", help="id of the cross-box file for this call, when its text does not carry the call id")
    cls.add_argument("--xadj", help="id of the RULED cross-adjudication file (.tools/xadj.py) this close rests on")
    cls.add_argument("--ruled-by", choices=RULED_BY, default="cto",
                     help="andrew: the ruling is Andrew's word and closes the row whatever its scope; "
                          "cto (default): a CROSS-BOX row needs a CLOSED-BOTH cross-box file")
    mod = sub.add_parser("mode", help="the keep-driving switch in S3 (Andrew-direct 2026-10-09; skill /keep-driving)")
    mod.add_argument("action", choices=("get", "set"))
    mod.add_argument("--part", choices=MODE_PARTS + ("all",), default="all")
    mod.add_argument("--state", choices=MODE_STATES + ("inherit",))
    mod.add_argument("--box", help="get: read as this box; set: a per-box override (inherit removes it)")
    mod.add_argument("--by")
    mod.add_argument("--reason")
    hold = sub.add_parser("hold", help="hold an OPEN call for Andrew's word (the scan stops nudging the CTO for it)")
    hold.add_argument("--id", required=True)
    hold.add_argument("--by", required=True)
    hold.add_argument("--reason", required=True, help="one line: why only Andrew can rule it (money, vendor, directive, his hold)")
    lift = sub.add_parser("lift", help="lift a hold for Andrew on a ruling that settled the call (the hold's text stays on the row)")
    lift.add_argument("--id", required=True)
    lift.add_argument("--by", required=True)
    lift.add_argument("--ruling", required=True, help="the ruling file the lift rests on")
    aps = sub.add_parser("approval-status", help="one line: the approval state of a candidate branch (NFRA_DEVPLN)")
    aps.add_argument("--branch", required=True, help="cand/<box>/<slug>")
    aps.add_argument("--store-dir", help="a directory holding <box>/open_calls.json (tests); overrides the working tree and git")
    alz = sub.add_parser("approval-lease", help="register an approval a live FAST lease of this seat already APPROVES (NFRA_DEVPLN)")
    alz.add_argument("--project", required=True, help="the project the approval belongs to (NFRA_DEVPLN for the portal approvals)")
    alz.add_argument("--branch", required=True, help="cand/<box>/<slug>")
    alz.add_argument("--box", required=True)
    alz.add_argument("--purpose", required=True)
    alz.add_argument("--pages", required=True, help="the portal pages it touches, comma separated")
    alz.add_argument("--class", dest="klass", required=True, choices=APPROVAL_CLASSES)
    alz.add_argument("--how", required=True)
    alz.add_argument("--portal", help="the portal repository (required: refused reason=portal-required without it)")
    alz.add_argument("--lease-file", help="the FAST lease JSON (mode FAST, expires_epoch, seat)")
    alz.add_argument("--asked-by", help="defaults to OPAL_AGENT_SERIAL")
    alz.add_argument("--waive-overlap", dest="waive_overlap",
                     help="comma-separated full or abbreviated shas excused from the DEV-overlap refusal (named, never a count)")
    alz.add_argument("--waiver-ref", dest="waiver_ref", help="the ruling file that names the waived commits (required with --waive-overlap)")
    sco = sub.add_parser("scope", help="measure whether a call touches only this box")
    sco.add_argument("--project")
    sco.add_argument("--orders", nargs="+", default=[])
    sco.add_argument("--roots", nargs="+", default=[])
    sco.add_argument("--selftest", action="store_true")
    return ap


def main(argv: list) -> int:
    args = build_parser().parse_args(argv)
    try:
        return {"add": cmd_add, "list": cmd_list, "close": cmd_close, "scope": cmd_scope,
                "publish": cmd_publish, "hold": cmd_hold, "lift": cmd_lift, "mode": cmd_mode,
                "approval-status": cmd_approval_status, "approval-lease": cmd_approval_lease}[args.cmd](args)
    except Refused as exc:
        print(str(exc) if str(exc).startswith("REFUSED") else "ERROR: %s" % exc, file=sys.stderr)
        return 1 if str(exc).startswith("REFUSED") else 2
    except BadFile as exc:
        print("REFUSED: %s" % exc, file=sys.stderr)
        return 3
    except Exception as exc:   # a register that cannot be read must stop the tool, never fall back to a built-in list
        if type(exc).__name__ == "RegisterError":
            print(str(exc), file=sys.stderr)
            return 3
        raise


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

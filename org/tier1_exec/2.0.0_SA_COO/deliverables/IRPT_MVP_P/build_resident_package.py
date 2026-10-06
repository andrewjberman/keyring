#!/usr/bin/env python3
"""Assemble the resident Analysis package from COMMITTED blobs, with SHA256SUMS and bindings.

RESIDENT_ASSEMBLY_HANDOFF_20260923 items 1-3 (P side). The package is the SOURCE-TREE layout
`ycharts/generate/resident_main.py` expects (it puts <root>/{intake,ops,reports,_keys,_authz,
_gate,ycharts/session,ycharts/extract} on sys.path; reports/resident_installed.py adds
_scope/_ids/_contracts/lib). Every member is read with `git show <pin>:<path>` -- never the
worktree -- and the census is the exact blob Y pinned (44853788..., 195040 bytes), not the
working file. `install-resident.sh` verifies SHA256SUMS and the cutover receipt on the host;
this script writes the sums and the bindings, and refuses to write a receipt: the receipt's
booleans come from the real cutover acts, not from a build.

Usage (from the backend worktree):
  python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py \
      --pin <commit> --enrolled-user-id <int> --out .runtime/resident-package \
      [--census-pin 2874e37647] [--dry-run]
      [--research] [--opal-map REPO_PATH] [--base-pin P --files-from LIST] [--state-json FILE]
      [--member PACKAGED_PATH=REPO_PATH ...]

IRPT_YCDGEN R13: `--research` also packages the tracked non-test files of ycharts/research/; `--opal-map` packages
one tracked file as ycharts/research/overview_map.json and pins it in the bindings (`opal_map`); `--base-pin P
--files-from LIST` builds P's tree by the rule below except the listed repo paths, which come from `--pin`;
`--state-json` reads the core state document from a file instead of S3. A build with none of these flags is the
build of before.

IRPT_YCDGEN R15: `--member PACKAGED_PATH=REPO_PATH` (repeatable) packages the tracked file REPO_PATH at `--pin` as the member
PACKAGED_PATH and records `{"packaged", "repo_path", "sha256"}` under the bindings provenance key `members_added` (absent
when no `--member` is given). A PACKAGED_PATH that is absolute, holds `..`, or is already a member, and a REPO_PATH absent at
`--pin`, are refused. Under `--base-pin` the member is read from `--pin` and needs no entry in the `--files-from` list.

Bindings come from the core root's canonical outputs read from its remote state (queue URL,
table names) and are recorded with that state's serial; the region is the estate's. ASCII only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKTREE = Path(__file__).resolve().parents[5]
IR = "infra/aws/lambda/investor-reporting"
CENSUS = "docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json"
CENSUS_SHA = "44853788fa6d39c8b6011c2f86fc82ea6906c2e006935df549f153378c950905"
WRAPPER = "infra/aws/ec2/investor-reporting-ycharts/run-ycharts-session.sh"
LIBRARY = "infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js"
HOST_APP_DIR = "/opt/investor-reporting-ycharts"
STATE = "s3://opal-313476888478-terraform-state/investor-reporting/core/tfstate"
REGION = "us-east-1"

# Source directories packaged whole (tracked .py/.json/.sh members, tests excluded on the host).
PACKAGE_DIRS = ("_authz", "_contracts", "_gate", "_ids", "_keys", "_scope", "intake", "ops",
                "reports", "ycharts/generate", "ycharts/session", "ycharts/extract")
RESEARCH_DIR = "ycharts/research"
RESEARCH_EXT = (".py", ".json", ".sh", ".md", ".cjs")
OPAL_MAP_MEMBER = RESEARCH_DIR + "/overview_map.json"
EXTRA_FILES = ("lib/opal_naming.py", "data/firm_registry.json", "org/standards/NAMING_SCHEMA.json")
EXTRA_DIRS = ("infra/logic/registry", "docs/contracts/investor-reporting/v1")


def git(*args, binary=False):
    result = subprocess.run(["git", *args], cwd=WORKTREE, check=False,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise SystemExit("git %s failed: %s" % (" ".join(args), result.stderr.decode(errors="replace")[:200]))
    return result.stdout if binary else result.stdout.decode()


def tracked_under(pin, prefix):
    listing = git("ls-tree", "-r", "--name-only", pin, "--", prefix)
    return [line.strip() for line in listing.splitlines() if line.strip()]


def wanted(path):
    if "/tests/" in path or "/__pycache__/" in path or path.endswith(".pyc"):
        return False
    return path.endswith((".py", ".json", ".sh", ".md"))


def research_wanted(path):
    parts = path.split("/")
    if "tests" in parts or "fixtures" in parts or "__pycache__" in parts or path.endswith(".pyc"):
        return False
    return path.endswith(RESEARCH_EXT)


def exists_at(pin, path):
    return subprocess.run(["git", "cat-file", "-e", "%s:%s" % (pin, path)], cwd=WORKTREE, check=False,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0


def packaged_name(repo_path):
    """The package member name for a repo path (the gate's repo_path inverted for the investor-reporting tree)."""
    return repo_path[len(IR) + 1:] if repo_path.startswith(IR + "/") else repo_path


def read_list(path):
    raw = Path(path).read_bytes()
    names = [line.strip() for line in raw.decode("utf-8").splitlines() if line.strip()]
    return names, hashlib.sha256(raw).hexdigest()


def core_outputs(state_json=None):
    if state_json:
        state = json.loads(Path(state_json).read_text(encoding="utf-8"))
        return state["serial"], {k: v["value"] for k, v in state["outputs"].items()}
    # Windows Python cannot exec the bash shim `.tools/aws`; its `.cmd` sibling is the
    # Win32-callable form (CLAUDE.md Git: "the .tools/aws shim (+aws.cmd, both or neither)").
    shim = WORKTREE / ".tools/aws.cmd"
    if not shim.is_file():
        shim = WORKTREE / ".tools/aws"
    raw = subprocess.run([str(shim), "s3", "cp", STATE, "-"], capture_output=True,
                         check=False, cwd=WORKTREE, shell=False)
    if raw.returncode != 0:
        raise SystemExit("core state read failed: " + raw.stderr.decode(errors="replace")[:200])
    state = json.loads(raw.stdout.decode())
    outputs = {k: v["value"] for k, v in state["outputs"].items()}
    return state["serial"], outputs


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pin", required=True, help="commit whose blobs are packaged")
    parser.add_argument("--enrolled-user-id", type=int, required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--census-pin", default="2874e37647")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--override", action="append", default=[], metavar="REPO_PATH=PIN",
                        help="package ONE member from another commit (e.g. a fix landed after --pin); recorded in the "
                             "bindings provenance. The member must already exist at --pin")
    parser.add_argument("--research", action="store_true",
                        help="also package the tracked non-test files under ycharts/research/")
    parser.add_argument("--opal-map", metavar="REPO_PATH", default=None,
                        help="tracked file at --pin packaged as ycharts/research/overview_map.json and pinned as bindings opal_map")
    parser.add_argument("--member", action="append", default=[], metavar="PACKAGED_PATH=REPO_PATH",
                        help="package the tracked file REPO_PATH at --pin as the member PACKAGED_PATH (repeatable); "
                             "recorded in the bindings provenance as members_added")
    parser.add_argument("--base-pin", default=None, help="build the package from this commit's tree except --files-from")
    parser.add_argument("--files-from", default=None, metavar="LIST",
                        help="file of repo paths (one per line), each existing at --pin, taken from --pin")
    parser.add_argument("--state-json", default=None, metavar="FILE",
                        help="read the core state document from FILE instead of S3 (offline tests)")
    args = parser.parse_args(argv)
    if bool(args.base_pin) != bool(args.files_from):
        raise SystemExit("--base-pin and --files-from go together")

    pin = git("rev-parse", args.pin).strip()
    base = git("rev-parse", args.base_pin).strip() if args.base_pin else pin
    listed, list_sha = (read_list(args.files_from) if args.files_from else ([], None))
    for path in listed:
        if not exists_at(pin, path):
            raise SystemExit("listed file %s does not exist at --pin %s" % (path, args.pin))
    members = {}
    for directory in PACKAGE_DIRS:
        for path in tracked_under(base, IR + "/" + directory):
            if wanted(path):
                members[path[len(IR) + 1:]] = (base, path)
    if args.research:
        for path in tracked_under(base, IR + "/" + RESEARCH_DIR):
            if research_wanted(path):
                members[path[len(IR) + 1:]] = (base, path)
    for path in EXTRA_FILES:
        members[path] = (base, path)
    for directory in EXTRA_DIRS:
        for path in tracked_under(base, directory):
            if path.endswith(".json"):
                members[path] = (base, path)
    for path in listed:
        members[packaged_name(path)] = (pin, path)
    if args.opal_map:
        if not exists_at(pin, args.opal_map):
            raise SystemExit("--opal-map %s is not tracked at --pin" % args.opal_map)
        members[OPAL_MAP_MEMBER] = (pin, args.opal_map)
    overrides = {}
    for item in args.override:
        repo_path, _, other = item.partition("=")
        packaged = repo_path[len(IR) + 1:] if repo_path.startswith(IR + "/") else repo_path
        if packaged not in members or members[packaged][1] != repo_path:
            raise SystemExit("override %s is not a member at --pin" % repo_path)
        other = git("rev-parse", other).strip()
        members[packaged] = (other, repo_path)
        overrides[repo_path] = other
    members["census/" + CENSUS.rsplit("/", 1)[1]] = (git("rev-parse", args.census_pin).strip(), CENSUS)
    members["ycharts-host/run-ycharts-session.sh"] = (base, WRAPPER)
    members["ycharts-host/ycharts_session.js"] = (base, LIBRARY)

    added_members = []
    for item in args.member:
        packaged, sep, repo_path = item.partition("=")
        if not sep or not packaged or not repo_path:
            raise SystemExit("--member %r is not PACKAGED_PATH=REPO_PATH" % item)
        if packaged.startswith(("/", "\\")) or (len(packaged) > 1 and packaged[1] == ":"):
            raise SystemExit("--member packaged path %s is absolute" % packaged)
        if ".." in packaged.replace("\\", "/").split("/"):
            raise SystemExit("--member packaged path %s contains '..'" % packaged)
        if packaged in members:
            raise SystemExit("--member packaged path %s is already a member of the package" % packaged)
        if not exists_at(pin, repo_path):
            raise SystemExit("--member repo path %s does not exist at --pin %s" % (repo_path, args.pin))
        members[packaged] = (pin, repo_path)
        added_members.append((packaged, repo_path))

    serial, outputs = core_outputs(args.state_json)
    out = Path(args.out)
    sums = []
    for packaged, (blob_pin, path) in sorted(members.items()):
        data = git("show", "%s:%s" % (blob_pin, path), binary=True)
        digest = hashlib.sha256(data).hexdigest()
        sums.append((digest, packaged))
        if not args.dry_run:
            target = out / packaged
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    census_digest = next(d for d, p in sums if p.startswith("census/"))
    if census_digest != CENSUS_SHA:
        raise SystemExit("census blob at %s is %s, not the pinned %s" % (args.census_pin, census_digest, CENSUS_SHA))
    wrapper_sha = next(d for d, p in sums if p == "ycharts-host/run-ycharts-session.sh")
    library_sha = next(d for d, p in sums if p == "ycharts-host/ycharts_session.js")

    bindings = {
        "schema_version": "irpt-resident-bindings-v1",
        "region": REGION,
        "queue_url": outputs["queues"]["generation"]["url"],
        "jobs_table": outputs["tables"]["jobs"],
        "requests_table": outputs["tables"]["requests"],
        "enrolled_user_id": args.enrolled_user_id,
        # The HOST's installed copies are what HostCapture hashes at capture time; the package
        # carries the same bytes under ycharts-host/ for the installer's SHA256SUMS check.
        "capture": {"wrapper_path": HOST_APP_DIR + "/run-ycharts-session.sh", "wrapper_sha256": wrapper_sha,
                    "library_path": HOST_APP_DIR + "/ycharts_session.js", "library_sha256": library_sha},
        # Relative paths resolve against the bindings file's own directory (reports/), so the
        # package-root members are one level up.
        "census": {"path": "../census/" + CENSUS.rsplit("/", 1)[1], "sha256": CENSUS_SHA},
        "schema_directory": "../docs/contracts/investor-reporting/v1",
        "provenance": {"package_pin": pin, "member_overrides": overrides, "census_pin": args.census_pin,
                       "core_state_serial": serial,
                       "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                       "generated_by": "2.0.0_SA_COO~P build_resident_package.py"},
    }
    if args.opal_map:
        bindings["opal_map"] = {"path": "../" + OPAL_MAP_MEMBER,
                                "sha256": next(d for d, p in sums if p == OPAL_MAP_MEMBER)}
        bindings["provenance"]["opal_map_source"] = args.opal_map
    if added_members:
        bindings["provenance"]["members_added"] = [
            {"packaged": packaged, "repo_path": repo_path, "sha256": next(d for d, p in sums if p == packaged)}
            for packaged, repo_path in added_members]
    if args.files_from:
        bindings["provenance"].update({"base_pin": base, "files_from_sha256": list_sha, "files_from_count": len(listed)})
    bindings_bytes = (json.dumps(bindings, indent=2, sort_keys=True) + "\n").encode()
    sums.append((hashlib.sha256(bindings_bytes).hexdigest(), "reports/resident_bindings.json"))
    sums.sort(key=lambda item: item[1])
    sums_text = "".join("%s  %s\n" % (d, p) for d, p in sums)
    manifest_sha = hashlib.sha256(sums_text.encode()).hexdigest()
    if not args.dry_run:
        (out / "reports/resident_bindings.json").write_bytes(bindings_bytes)
        (out / "SHA256SUMS").write_text(sums_text, encoding="utf-8", newline="\n")
    report = {"package_pin": pin, "member_overrides": overrides, "census_pin": args.census_pin, "members": len(sums),
              "package_manifest_sha256": manifest_sha, "core_state_serial": serial,
              "queue_url": bindings["queue_url"], "jobs_table": bindings["jobs_table"],
              "requests_table": bindings["requests_table"], "wrapper_sha256": wrapper_sha,
              "library_sha256": library_sha, "out": None if args.dry_run else str(out)}
    if added_members:
        report["members_added"] = bindings["provenance"]["members_added"]
    if args.files_from:
        report.update({"base_pin": base, "files_from": listed, "files_from_count": len(listed),
                       "files_from_sha256": list_sha})
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

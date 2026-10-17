#!/usr/bin/env python3
"""comp_closure -- NFRA_EPISTEMY COMPONENT 3: the IDENTITY + SUPPORT-CLOSURE COMPILER.

"Makes 'what changed / what supports this' answerable at the right grain" (PRD sec.1 row 3).
Given a logical fact ("Lambda F runs code C@v") it compiles the SUPPORT CLOSURE -- the ordered,
typed chain of hops {logical fact -> build input -> package manifest -> deployed bytes -> repo
bytes -> (execution)} -- and terminates HONESTLY where the evidence stops.

SOURCES OF RECORD (cited, never copied): PRD_EPISTEMIC_MECHANIZATION_20260820.md sec.2.1
(Observation_Record -- consumed via the C1 envelope's build_record, never re-implemented) + sec.2.5
(Eligibility_Evaluation consumes the closure); Response II sec.2.5 (:147-156: logical-fact vs
substrate-realization, the AMBIGUITY CHECK "no second plausible home", EXPIRY, the last hop
deployed->EXECUTING verifies presence not behavior); CLAUDE.md Rule 22a (deployed bytes are diffed
against THE SOURCE THE ARTIFACT IS BUILT FROM, resolved through the BUILD INPUT, never by filename;
on EC2 staged = DESIRED, executing = APPLIED). Object shape: 4.0.0_SA_CRO base spec cert 63859
(CERTIFIED-WITH-AMENDMENTS) + 1.0.0_SA_CTO arch gate 63865 (CLEARS on the amended shape).

THE TWO AXES (split per base's A1: a precedence rule is the tell that two axes are fused):
  reach     MEMBER grain: how far the evidence chain got for ONE member
              NONE            the member was never resolved/compared through the build input
              PRESENCE_ONLY   the member's bytes were read from the DEPLOYED digest and stopped there
              BEHAVIOR        an EXECUTING read covered the member (on-instance/runtime/exercised)
            CLOSURE reach = MIN over members -- the AGGREGATION LAYER, declared here: a closure is
            as far-reached as its LEAST-reached member (no members -> NONE). MIN is not an ordering
            between intents; it is the weakest-link aggregate of one member-grain value.
  standing  CLOSURE grain: whether the compiled chain stands
              BROKEN          a required acquisition failed and the chain STOPPED there (no later hop
                              is taken -- which is what makes BROKEN disjoint from the other three)
              AMBIGUOUS       the chain completed and a member has a SECOND plausible repo home
              CURRENT         the chain completed, single home, and no side has moved
              INVALIDATED     a side moved since compile -- verify's re-read verdict (a closure is
                              compiled CURRENT/AMBIGUOUS; only a re-read can find it INVALIDATED)
  The equivalence VERDICT lives on the Identity_Bundle (EQUIVALENT / DIVERGENT / UNMEASURED / UNKNOWN),
  never on either axis. UNKNOWN is reserved for hop status + bundle claim state (acquisition-failed).

RESOLUTION SHAPES (reused from NFRA_DEPLOYCENSUS lambda_census_v3, proved on 197 functions):
  A  BUILD_MANIFEST.json inside the package          -> module -> repo_path + vintage
  B  inline_archive_file (TF archive over a dir)     -> every file in the dir at HEAD
  C  nodejs transformed build                         -> provenance chain: live.CodeSha256 == map.artifact_sha256
  D  files[] empty, source_dir present               -> directory + basename (DECLARED WEAKER: cannot yield EQUIVALENT alone)
  E  default: source_dir + files[]                   -> zip member of the same relative path
A hop that has NO build-input basis is REFUSED (m2: a filename-resolved hop smuggled in).

BOUNDS: read-only live AWS (get-function / package download); the source map is a BUILD INPUT read
and never rewritten; nothing armed; comp-iam floor: this tool runs under the operator's own
credentials like comp-aws (no Lambda role is granted anything by it). Observation `plane` is the
RATIFIED enum {DESIRED, APPLIED, EXERCISED} with `substrate` {aws, portal, codebase, ms} per the C1
rider @6f944857c4 (the CTO 63744 carry-opaque condition is DISCHARGED): source-map + repo reads =
DESIRED/codebase; live get-function + package = APPLIED/aws; on-instance read = APPLIED/aws; an
exercised path = EXERCISED. No reach/standing value is computed from plane. Lambda closures are
PRESENCE_ONLY BY CONSTRUCTION tonight: no invokes are taken, and every instance SAYS SO.

Author: 0.8.0_AE_CloudComp (NFRA_EPISTEMY.C3-IDENTITY, COO GO 63813). Both NFRA_EPISTEMY fences held.
"""
from __future__ import annotations

import base64
import collections
import hashlib
import io
import json
import os
import subprocess
import sys
import time
import urllib.request
import zipfile

_HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
FUNCTION_MAP = os.path.join(WS, "infra", "aws", "lambda", "ci", "function-map")   # one <name>.json per function (TO-CT-ca-1)
_LIB = os.path.join(WS, "lib")
if _LIB not in sys.path:
    sys.path.insert(0, _LIB)
from opal_lambda_map import load_all as load_function_map  # noqa: E402
ENVELOPE_SRC = os.path.join(WS, "org", "tier1_exec", "4.0.0_SA_CRO~A", "deliverables",
                            "NFRA_EPISTEMY.C1-ENVELOPE", "src")
INSTRUMENT = {"id": "comp-closure", "version": "0.3.0"}
REACH = ("NONE", "PRESENCE_ONLY", "BEHAVIOR")            # member grain; MIN aggregates weakest-first
STANDING = ("BROKEN", "AMBIGUOUS", "CURRENT", "INVALIDATED")   # closure grain; disjoint by construction
HOP_CLASSES = ("DECLARATION", "ARTIFACT_POINTER", "DIGEST", "BYTES", "EXECUTION")
OK = {"acquisition": "PRESENT", "transport": "SUCCEEDED", "enumeration": "SUCCEEDED", "parse": "SUCCEEDED"}
OUT_DIR = os.path.join(WS, "org", "tier2_senior", "0.8.0_AE_CloudComp", "deliverables",
                       "NFRA_EPISTEMY.C3-IDENTITY", "closures")
# generic entry-point/utility basenames (the census's skip set): a same-name hit on these is not a second home
SKIP_BASENAMES = {"lambda_function.py", "__init__.py", "config.py", "handler.py", "index.py", "utils.py", "main.py",
                  "conftest.py", "setup.py", "_util.py", "run.py", "pipeline.py", "formatter.py", "orchestrator.py",
                  "index.mjs", "index.js", "requirements.txt", "README.md"}
SIM_FLOOR = 0.5
PRESENCE_NOTE = ("PRESENCE_ONLY BY CONSTRUCTION: no executing read was taken (read-only bound; an invoke is an "
                 "execution act) -- a clean run here verifies what is THERE, never what RUNS")


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _b64_to_hex(s: str) -> str:
    try:
        return base64.b64decode(s).hex()
    except Exception:  # noqa: BLE001
        return s


def _hexify(s: str) -> str:
    """sha256 as hex whether recorded as 64 hex chars or as base64 (the two forms the source map carries)."""
    t = s.strip()
    if len(t) == 64 and all(c in "0123456789abcdefABCDEF" for c in t):
        return t.lower()
    return _b64_to_hex(t)


def _sim(a: bytes, b: bytes) -> float:
    import difflib  # noqa: PLC0415
    try:
        return difflib.SequenceMatcher(None, a.decode("utf-8", "replace"), b.decode("utf-8", "replace")).ratio()
    except Exception:  # noqa: BLE001
        return 0.0


# MEMBER COMPARISON (ESTATE_GOVERNANCE-S30, re-filed from ETFS_INGEST-Z-S17; the defect named in .tools/comp-closure's
# header since 2026-08-24). The byte compare was RAW: a CRLF-deployed member against LF committed bytes read
# eq_head False on a CORRECT deploy. The settled order is kept: (a) DISCLOSURE FIRST -- every member row says which
# comparison established each equality (`*_basis`) and still carries the raw result (`raw_eq_*`), and those are row
# properties, so they survive the equivalence=UNMEASURED short-circuit; (b) NORMALISATION SECOND -- a TEXT member
# (no NUL byte) that differs from the repo bytes ONLY in CRLF versus LF is equal under EOL_NORMALIZED. A normalised
# equality is never silent: the bundle's basis sentence counts the members it rests on.
CMP_RAW, CMP_EOL = "RAW_BYTES", "EOL_NORMALIZED"


def _eol_norm(b):
    """CRLF folded to LF for a TEXT member; None for a binary one (a NUL byte) or an absent side."""
    if b is None or b"\0" in b:
        return None
    return b.replace(b"\r\n", b"\n")


def _member_eq(deployed: bytes, repo):
    """(equal, basis): (True, CMP_RAW) on identical bytes; (True, CMP_EOL) when two text members differ only in
    line endings; (False, None) otherwise, including an absent repo side."""
    if repo is None:
        return False, None
    if repo == deployed:
        return True, CMP_RAW
    nd, nr = _eol_norm(deployed), _eol_norm(repo)
    if nd is not None and nr is not None and nd == nr:
        return True, CMP_EOL
    return False, None


def closure_reach(member_reach: dict) -> str:
    """The AGGREGATION LAYER: closure reach = MIN over members (weakest link). No members -> NONE."""
    if not member_reach:
        return "NONE"
    return min(member_reach.values(), key=REACH.index)


# ---------------------------------------------------------------------------------------------
# The C1 envelope: CONSUMED. Every acquisition becomes an Observation_Record built by the envelope's
# own constructor (a failed stage forces UNKNOWN). If the package is absent the compiler refuses to
# run rather than fabricate records.
# ---------------------------------------------------------------------------------------------
def _envelope():
    if ENVELOPE_SRC not in sys.path:
        sys.path.insert(0, ENVELOPE_SRC)
    import observation_envelope as env  # noqa: PLC0415
    return env


def _obs(env, *, request, status, plane, substrate, population, count, grain, process, value, reason,
         pointers, residue=None, invalidation=None):
    """plane = the RATIFIED verification-plane enum {DESIRED, APPLIED, EXERCISED}; substrate = the physical
    platform {aws, portal, codebase, ms} -- both per the C1 rider @6f944857c4 (CTO 63744 condition DISCHARGED)."""
    return env.build_record(
        instrument_id=INSTRUMENT["id"], instrument_version=INSTRUMENT["version"], request=request,
        status=status, plane=plane, substrate=substrate, population_predicate=population, denominator_count=count,
        denominator_grain=grain, denominator_process=process, substantive_value=value,
        unknown_reason=reason, observed_at=_now(), support_pointers=list(pointers),
        traversal_residue=list(residue or []), control_references=[],
        discrimination_certificate_ref=None, invalidation_predicates=list(invalidation or []))


# ---------------------------------------------------------------------------------------------
# Readers -- live (boto3, read-only) vs fixture (self-test). Every read returns (value|None, status)
# and the envelope decides KNOWN vs UNKNOWN; the compiler never knows which reader it has.
# ---------------------------------------------------------------------------------------------
class LiveReader:
    plane_label = "APPLIED"   # ratified verification plane of a live get-function/package read
    substrate = "aws"

    def __init__(self, region="us-east-1"):
        import boto3  # noqa: PLC0415
        self._lam = boto3.client("lambda", region_name=region)

    def get_function(self, name):
        try:
            return self._lam.get_function(FunctionName=name), dict(OK)
        except self._lam.exceptions.ResourceNotFoundException:
            return None, {"acquisition": "ABSENT", "transport": "SUCCEEDED", "enumeration": "NOT_ATTEMPTED", "parse": "NOT_ATTEMPTED"}
        except Exception:  # noqa: BLE001
            return None, {"acquisition": "UNKNOWN", "transport": "FAILED", "enumeration": "NOT_ATTEMPTED", "parse": "NOT_ATTEMPTED"}

    def fetch_package(self, fn_response):
        try:
            url = fn_response["Code"]["Location"]
            with urllib.request.urlopen(url, timeout=60) as r:  # noqa: S310 -- AWS presigned URL
                return r.read(), dict(OK)
        except Exception:  # noqa: BLE001
            return None, {"acquisition": "UNKNOWN", "transport": "FAILED", "enumeration": "NOT_ATTEMPTED", "parse": "NOT_ATTEMPTED"}


class RepoIndex:
    """The repo side: bytes at HEAD / at a commit, and the HOMES a byte-blob or basename lives at
    (the AMBIGUITY CHECK's substrate). Live = git; fixture = dicts."""

    def __init__(self, ws=WS):
        self.ws = ws
        self._head = None
        self._blob2paths = None
        self._base2paths = None
        self._cache = {}

    def head(self):
        if self._head is None:
            r = subprocess.run(["git", "-C", self.ws, "rev-parse", "HEAD"], capture_output=True, text=True)
            self._head = r.stdout.strip() if r.returncode == 0 else None
        return self._head

    def _index(self):
        if self._blob2paths is not None:
            return
        self._blob2paths = collections.defaultdict(list)
        self._base2paths = collections.defaultdict(list)
        r = subprocess.run(["git", "-C", self.ws, "ls-tree", "-r", "-z", "HEAD"], capture_output=True)
        for rec in r.stdout.split(b"\0"):
            if not rec:
                continue
            meta, path = rec.split(b"\t", 1)
            sha = meta.decode().split(" ")[2]
            p = path.decode("utf-8", "replace")
            self._blob2paths[sha].append(p)
            self._base2paths[os.path.basename(p)].append(p)

    @staticmethod
    def blobsha(b: bytes) -> str:
        return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()  # noqa: S324 -- git's own object id

    def bytes_at(self, commit, path):
        key = (commit, path)
        if key not in self._cache:
            r = subprocess.run(["git", "-C", self.ws, "show", "%s:%s" % (commit, path)], capture_output=True)
            self._cache[key] = r.stdout if r.returncode == 0 else None
        return self._cache[key]

    def homes_for(self, member_bytes, basename):
        """Raw candidates at HEAD: exact blob identity, and same-basename paths outside vendored trees."""
        self._index()
        exact = list(self._blob2paths.get(self.blobsha(member_bytes), []))
        same = [p for p in self._base2paths.get(basename, [])
                if not any(seg in p for seg in ("node_modules/", "site-packages/", ".terraform/", "__pycache__/"))]
        return exact, same

    def plausible_homes(self, member_bytes, basename, repo_path):
        """THE AMBIGUITY PREDICATE (census-proved): a SECOND PLAUSIBLE HOME is another HEAD path that
        (a) holds the member's exact bytes, or (b) shares a NON-GENERIC basename and is content-similar
        (difflib ratio >= SIM_FLOOR). Generic entry-point names (handler.py, lambda_function.py, ...)
        collide across every function and are NOT evidence of a second home by name alone."""
        exact, same = self.homes_for(member_bytes, basename)
        homes = {p for p in exact if p != repo_path}
        if basename not in SKIP_BASENAMES:
            for p in same:
                if p == repo_path or p in homes:
                    continue
                other = self.bytes_at(self.head(), p)
                if other is not None and _sim(member_bytes, other) >= SIM_FLOOR:
                    homes.add(p)
        return sorted(homes)


# ---------------------------------------------------------------------------------------------
# The compiler
# ---------------------------------------------------------------------------------------------
def _hop(frm, to, cls, resolved_via, status, obs_ref, note=""):
    if cls not in HOP_CLASSES:
        raise ValueError("unknown hop evidence class %r" % cls)
    if not resolved_via or not resolved_via.startswith("BUILD_INPUT:"):
        # m2 -- a filename-resolved hop has no build-input basis: REFUSED, never smuggled in.
        raise ValueError("REFUSED: hop %s->%s lacks a build-input basis (got %r)" % (frm, to, resolved_via))
    return {"from": frm, "to": to, "evidence_class": cls, "resolved_via": resolved_via,
            "instrument": dict(INSTRUMENT), "status": status, "observation_record_ref": obs_ref, "note": note}


def _broken(name, hops, reason, obs, vintage):
    """The chain STOPS here: no later hop is taken. standing=BROKEN, reach=NONE (no member resolved)."""
    return _finish(name, hops, "BROKEN", [reason], {"status": "UNKNOWN", "candidate_homes": []}, vintage, obs,
                   members=[], member_reach={}, digest_match=None, shape_d=False)


def compile_closure(name, smap, reader, repo, env, execution_reads=None):
    """Compile the Support_Closure + Identity_Bundle for the logical fact 'Lambda <name> runs code C@v'.
    execution_reads: optional {member_rel: {"digest": sha256hex, "source": str}} -- an EXECUTING read
    supplied by an on-instance/runtime instrument (EC2 SSM / fixture). Lambda has none tonight.
    Returns (closure, bundle, observation_records)."""
    obs, hops = [], []
    fns = smap.get("functions", {})
    entry = fns.get(name)
    vintage = {"source_map_updated": smap.get("_updated"), "artifact_sha256": None,
               "live_code_sha256": None, "last_deployed_commit": None, "repo_head": repo.head()}
    # --- H1 DECLARATION: the source-map entry (BUILD INPUT, read never rewritten) ---
    st = dict(OK) if entry else {"acquisition": "ABSENT", "transport": "SUCCEEDED", "enumeration": "SUCCEEDED", "parse": "SUCCEEDED"}
    o1 = _obs(env, request={"op": "source_map_entry", "fn": name}, status=st, plane="DESIRED", substrate="codebase",
              population="functions{} of infra/aws/lambda/ci/function-map/", count=len(fns),
              grain="source-map entry", process="json read of the committed function file", value=entry,
              reason="no source-map entry for %s" % name, pointers=["infra/aws/lambda/ci/function-map/%s.json" % name],
              invalidation=["source map _updated changes", "entry for %s edited" % name])
    obs.append(o1)
    if not entry:
        hops.append(_hop("logical_fact", "build_input", "DECLARATION", "BUILD_INPUT:source_map", "UNKNOWN", o1["request_hash"]))
        return _broken(name, hops, "no source-map entry -- chain broken at the build input", obs, vintage)
    hops.append(_hop("logical_fact", "build_input", "DECLARATION", "BUILD_INPUT:source_dir+files[]", "KNOWN", o1["request_hash"]))
    # --- H2 ARTIFACT_POINTER: the package manifest (artifact key + sha) ---
    art_sha, art_key = entry.get("artifact_sha256"), entry.get("artifact_s3_key")
    vintage.update({"artifact_sha256": art_sha, "last_deployed_commit": entry.get("last_deployed_commit")})
    pointer = bool(art_sha or art_key)
    # a missing pointer is NOT a broken chain: source_dir+files[] is still a build-input resolution (shape E/D);
    # what is lost is the PROVENANCE of the live package (which build produced it) -- the hop says so and stays UNKNOWN.
    hops.append(_hop("build_input", "package_manifest", "ARTIFACT_POINTER", "BUILD_INPUT:artifact_sha256+artifact_s3_key",
                     "KNOWN" if pointer else "UNKNOWN", o1["request_hash"],
                     "" if pointer else "entry carries no artifact pointer -- provenance of the live package is UNVERIFIABLE "
                                        "through the build input; identity continues on source_dir+files[] bytes alone"))
    # --- H3 DIGEST: the live deployed package ---
    fn_resp, st3 = reader.get_function(name)
    cfg = (fn_resp or {}).get("Configuration", {}) if fn_resp else {}
    o3 = _obs(env, request={"op": "lambda.get_function", "fn": name}, status=st3, plane=reader.plane_label, substrate=reader.substrate,
              population="the one live function named %s" % name, count=1 if fn_resp else None,
              grain="lambda function", process="lambda:GetFunction",
              value={"CodeSha256": cfg.get("CodeSha256"), "LastModified": cfg.get("LastModified")} if fn_resp else None,
              reason="get-function did not return the function", pointers=["lambda:%s" % name],
              invalidation=["function code updated (CodeSha256 changes)"])
    obs.append(o3)
    if not fn_resp:
        hops.append(_hop("package_manifest", "deployed_bytes", "DIGEST", "BUILD_INPUT:artifact_sha256", "UNKNOWN", o3["request_hash"]))
        return _broken(name, hops, "live function unreadable -- chain broken at the deployed digest", obs, vintage)
    vintage["live_code_sha256"] = cfg.get("CodeSha256")
    live_hex = _b64_to_hex(cfg.get("CodeSha256", ""))
    art_hex = _hexify(art_sha) if art_sha else None     # the map stores hex for python builds, base64 for edge builds
    digest_match = bool(art_hex) and art_hex == live_hex
    hops.append(_hop("package_manifest", "deployed_bytes", "DIGEST", "BUILD_INPUT:artifact_sha256", "KNOWN", o3["request_hash"],
                     ("live CodeSha256 %s artifact_sha256" % ("==" if digest_match else "!=")) if art_sha
                     else "live CodeSha256 read; no artifact pointer to match it against"))
    pkg, st3b = reader.fetch_package(fn_resp)
    members = {}
    if pkg:
        try:
            with zipfile.ZipFile(io.BytesIO(pkg)) as z:
                members = {n: z.read(n) for n in z.namelist() if not n.endswith("/")}
        except Exception:  # noqa: BLE001
            st3b = {"acquisition": "PRESENT", "transport": "SUCCEEDED", "enumeration": "FAILED", "parse": "FAILED"}
    o3b = _obs(env, request={"op": "lambda.package_download", "fn": name}, status=st3b, plane=reader.plane_label, substrate=reader.substrate,
               population="zip members of the deployed package", count=len(members) if members else None,
               grain="package member", process="Code.Location download + zip enumeration",
               value={"members": len(members), "package_sha256": _sha256(pkg) if pkg else None} if members else None,
               reason="package not downloadable/enumerable", pointers=["lambda:%s/package" % name],
               invalidation=["function code updated"])
    obs.append(o3b)
    if not members:
        hops.append(_hop("deployed_bytes", "repo_bytes", "BYTES", "BUILD_INPUT:source_dir+files[]", "UNKNOWN", o3b["request_hash"]))
        return _broken(name, hops, "package members unreadable -- the byte hop cannot be taken", obs, vintage)
    # --- H4 BYTES + the AMBIGUITY CHECK: deployed members vs repo bytes at the build input ---
    src_dir, files, dep_commit, head = entry.get("source_dir") or "", entry.get("files") or [], entry.get("last_deployed_commit"), repo.head()
    transformed = bool(files) and all(f.endswith((".mjs", ".js", ".cjs", ".ts")) for f in files)   # shape C: bun/minified build
    shape = "C" if transformed else ("E" if files else "D")
    per_member, member_reach, homes_seen = [], {}, set()
    for rel in (files if files else [os.path.basename(m) for m in members]):
        mb = members.get(rel) or members.get(os.path.basename(rel))
        if mb is None:
            per_member.append({"member": rel, "reach": "NONE", "reason": "member absent from package"})
            member_reach[rel] = "NONE"
            continue
        if transformed:
            # member bytes are BUILD OUTPUT, not source: byte-compare is a category error; identity rides the digest chain
            member_reach[rel] = "PRESENCE_ONLY"
            per_member.append({"member": rel, "repo_path": "%s/%s" % (src_dir.rstrip("/"), rel), "reach": "PRESENCE_ONLY", "shape": "C",
                               "deployed_sha256": _sha256(mb), "comparable": False,
                               "note": "transformed build: identity via live.CodeSha256 == artifact_sha256 built @last_deployed_commit"})
            continue
        repo_path = "%s/%s" % (src_dir.rstrip("/"), rel) if src_dir else rel
        at_dep = repo.bytes_at(dep_commit, repo_path) if dep_commit else None
        at_head = repo.bytes_at(head, repo_path) if head else None
        other_homes = repo.plausible_homes(mb, os.path.basename(rel), repo_path)
        homes_seen.update(other_homes)
        member_reach[rel] = "PRESENCE_ONLY"
        eq_dep, dep_basis = _member_eq(mb, at_dep)
        eq_hd, head_basis = _member_eq(mb, at_head)
        per_member.append({"member": rel, "repo_path": repo_path, "reach": "PRESENCE_ONLY", "shape": shape,
                           "deployed_sha256": _sha256(mb),
                           "repo_at_deployed_commit_sha256": _sha256(at_dep) if at_dep else None,
                           "repo_at_head_sha256": _sha256(at_head) if at_head else None,
                           "eq_deployed_commit": eq_dep, "eq_deployed_commit_basis": dep_basis,
                           "eq_head": eq_hd, "eq_head_basis": head_basis,
                           "raw_eq_deployed_commit": (at_dep is not None and at_dep == mb),
                           "raw_eq_head": (at_head is not None and at_head == mb),
                           "comparison": "raw bytes first; a text member equal only after CRLF is folded to LF is "
                                         "equal under %s and its *_basis says so" % CMP_EOL,
                           "other_plausible_homes": other_homes})
    compared = sum(1 for m in per_member if m.get("reach") != "NONE")
    o4 = _obs(env, request={"op": "repo_bytes_compare", "fn": name, "commit": dep_commit, "head": head},
              status=dict(OK) if compared else {"acquisition": "ABSENT", "transport": "SUCCEEDED", "enumeration": "SUCCEEDED", "parse": "SUCCEEDED"},
              plane="DESIRED", substrate="codebase", population="declared members of the entry (files[]; shape %s)" % shape, count=compared,
              grain="member file", process="git show at last_deployed_commit + HEAD; blob/basename home census",
              value=per_member if compared else None, reason="no member could be compared",
              pointers=["%s @ %s" % (src_dir, dep_commit)],
              invalidation=["repo bytes at the resolved paths change", "HEAD advances past the compared commit"])
    obs.append(o4)
    hops.append(_hop("deployed_bytes", "repo_bytes", "BYTES",
                     ("BUILD_INPUT:provenance-chain(live.CodeSha256==artifact_sha256@last_deployed_commit)" if transformed
                      else "BUILD_INPUT:source_dir+files[]" + ("" if files else " (shape D: directory+basename, DECLARED WEAKER)")),
                     "KNOWN" if compared else "UNKNOWN", o4["request_hash"]))
    if not compared:
        return _broken(name, hops, "no declared member could be compared -- the byte hop yielded nothing", obs, vintage)
    # --- H5 EXECUTION: only an executing read supplied by an instrument raises a member to BEHAVIOR ---
    if execution_reads:
        for rel, xr in execution_reads.items():
            if rel in member_reach and member_reach[rel] != "NONE":
                member_reach[rel] = "BEHAVIOR"
                for m in per_member:
                    if m["member"] == rel:
                        m["reach"] = "BEHAVIOR"
                        m["executing_sha256"] = xr.get("digest")
                        m["executing_source"] = xr.get("source")
        # an on-instance/runtime read is an APPLIED-plane observation; an exercised path (invoke + log) is EXERCISED --
        # the supplier says which (default APPLIED); reach=BEHAVIOR is the closure's axis, plane is the record's
        xplane = next(iter(execution_reads.values())).get("plane", "APPLIED")
        ox = _obs(env, request={"op": "execution_read", "fn": name, "members": sorted(execution_reads)}, status=dict(OK),
                  plane=xplane if xplane in ("APPLIED", "EXERCISED") else "APPLIED", substrate="aws",
                  population="members covered by the supplied executing read", count=len(execution_reads),
                  grain="member file", process=str({v.get("source") for v in execution_reads.values()}), value=execution_reads,
                  reason="", pointers=[v.get("source", "") for v in execution_reads.values()], invalidation=["the instance/runtime changes"])
        obs.append(ox)
        hops.append(_hop("deployed_bytes", "executing", "EXECUTION", "BUILD_INPUT:executing-read-of-resolved-member", "KNOWN",
                         ox["request_hash"], "executing read covers %d of %d member(s)" % (len(execution_reads), len(member_reach))))
    else:
        hops.append(_hop("deployed_bytes", "executing", "EXECUTION", "BUILD_INPUT:n/a-not-taken", "NOT_ATTEMPTED", None, PRESENCE_NOTE))
    standing = "AMBIGUOUS" if homes_seen else "CURRENT"
    ambiguity = ({"status": "AMBIGUOUS", "candidate_homes": sorted(homes_seen)} if homes_seen
                 else {"status": "SINGLE_HOME", "candidate_homes": []})
    reasons = (["ambiguity check: %d other plausible home(s) across %d compared member(s) -- a second plausible home exists; "
                "the equivalence claim is neither true nor false" % (len(homes_seen), compared)] if homes_seen else [])
    return _finish(name, hops, standing, reasons, ambiguity, vintage, obs, members=per_member, member_reach=member_reach,
                   digest_match=digest_match, shape_d=(not files), transformed=transformed, pointer=pointer)


def _finish(name, hops, standing, reasons, ambiguity, vintage, obs, *, members, member_reach, digest_match, shape_d,
            transformed=False, pointer=True, subject_kind="LAMBDA_RUNS_CODE", extra_notes=None, identities=None, eq_override=None):
    assert standing in STANDING
    reach = closure_reach(member_reach)
    # m4 -- last-hop honesty as a schema constraint: BEHAVIOR requires a KNOWN EXECUTION hop.
    if reach == "BEHAVIOR" or any(v == "BEHAVIOR" for v in member_reach.values()):
        if not any(h["evidence_class"] == "EXECUTION" and h["status"] == "KNOWN" for h in hops):
            raise ValueError("REFUSED: reach BEHAVIOR claimed without a KNOWN EXECUTION-class hop (last-hop honesty)")
    # the equivalence VERDICT lives on the bundle, never on an axis
    if eq_override is not None:
        eq = dict(eq_override)
    elif standing == "BROKEN":
        eq = {"state": "UNKNOWN", "basis": "; ".join(reasons) or "chain broken"}
    elif standing == "AMBIGUOUS":
        eq = {"state": "UNMEASURED", "basis": "; ".join(reasons)}
    elif transformed:
        eq = ({"state": "EQUIVALENT", "basis": "shape C (transformed build): live CodeSha256 == artifact_sha256 built @%s -- the live package IS the "
                                                "artifact the build input records; member bytes are build output and are not byte-compared by design"
                                                % vintage.get("last_deployed_commit")}
              if digest_match else
              {"state": "UNMEASURED", "basis": "shape C (transformed build): live CodeSha256 != the map's artifact_sha256, and member bytes cannot be "
                                               "byte-compared -- the digest chain does not tie the live package to the build input"})
    else:
        cmp_ = [m for m in members if m.get("reach") != "NONE"]
        all_eq_head = bool(cmp_) and all(m.get("eq_head") for m in cmp_)
        all_eq_dep = bool(cmp_) and all(m.get("eq_deployed_commit") for m in cmp_)
        # WHICH comparison the verdict rests on, counted (never a silent normalise): see _member_eq.
        n_eol_head = sum(1 for m in cmp_ if m.get("eq_head_basis") == CMP_EOL)
        n_eol_dep = sum(1 for m in cmp_ if m.get("eq_deployed_commit_basis") == CMP_EOL)
        if shape_d and all_eq_head:
            eq = {"state": "UNMEASURED", "basis": "shape D (directory+basename) resolution is declared weaker and cannot yield EQUIVALENT alone"}
        elif all_eq_head:
            eq = {"state": "EQUIVALENT", "basis": "every compared member %s to repo@HEAD at its build-input path; single home%s"
                  % ("byte-equal" if not n_eol_head else
                     "equal (%d of %d by %s -- the bytes differ only in CRLF versus LF -- the rest %s)"
                     % (n_eol_head, len(cmp_), CMP_EOL, CMP_RAW),
                     "; live digest == artifact pointer" if digest_match else
                     ("; live digest != artifact pointer (the map's pointer is older than the live deploy)" if pointer else
                      "; provenance hop UNKNOWN (no artifact pointer) -- identity established on bytes alone"))}
        elif any(m.get("eq_head") is False for m in cmp_):
            dep_known = any(m.get("repo_at_deployed_commit_sha256") for m in cmp_)
            if not dep_known:
                basis = ("deployed bytes differ from repo@HEAD at the build-input path for %d of %d member(s); NO recorded deploy commit in "
                         "the build input, so stale-vs-HEAD and provenance mismatch CANNOT be told apart -- UNDETERMINED which"
                         % (sum(1 for m in cmp_ if m.get("eq_head") is False), len(cmp_)))
            elif all_eq_dep:
                basis = ("deployed == repo@last_deployed_commit for every compared member%s, HEAD has moved since "
                         "(stale-vs-HEAD; the build-input source at the deploy commit is intact -- not a provenance mismatch)"
                         % ("" if not n_eol_dep else " (%d of %d by %s)" % (n_eol_dep, len(cmp_), CMP_EOL)))
            else:
                basis = ("deployed bytes differ from the build-input source at the recorded deploy commit for %d of %d member(s) "
                         "(provenance mismatch; see members[])" % (sum(1 for m in cmp_ if not m.get("eq_deployed_commit")), len(cmp_)))
            eq = {"state": "DIVERGENT", "basis": basis}
        else:
            eq = {"state": "UNKNOWN", "basis": "no member comparison completed"}
    expires = ["source map entry changes", "function code updated", "repo bytes at resolved paths change", "HEAD advances"]
    eq["expires_on"] = expires
    closure = {"object": "Support_Closure", "object_status": "PROPOSED shape per 4.0.0_SA_CRO cert 63859 + 1.0.0_SA_CTO gate 63865",
               "subject": {"kind": subject_kind, "ref": name},
               "hops": hops,
               "reach": {"grain": "closure (MIN over members -- the declared aggregation layer)", "value": reach,
                         "per_member": member_reach},
               "standing": {"grain": "closure", "value": standing, "reasons": reasons},
               "ambiguity": ambiguity,
               "vintage": {**vintage, "observed_at": _now()},
               "invalidation_predicates": expires,
               "observation_record_refs": [o["request_hash"] for o in obs],
               "notes": [PRESENCE_NOTE if reach != "BEHAVIOR" else "an executing read was taken for every member",
                         "observation plane = ratified enum {DESIRED, APPLIED, EXERCISED} + substrate {aws, portal, codebase, ms} "
                         "per the C1 rider @6f944857c4 (CTO 63744 bind-time condition DISCHARGED)"] + list(extra_notes or [])}
    bundle = {"object": "Identity_Bundle", "object_status": closure["object_status"], "subject": closure["subject"],
              "identities": identities if identities is not None else [
                  {"plane": "SOURCE", "locator": "repo@%s" % vintage.get("last_deployed_commit"), "digest_basis": "per-member sha256 (members[])"},
                  {"plane": "SOURCE", "locator": "repo@HEAD %s" % vintage.get("repo_head"), "digest_basis": "per-member sha256"},
                  {"plane": "DESIRED", "locator": "artifact pointer", "digest": vintage.get("artifact_sha256")},
                  {"plane": "APPLIED", "locator": "lambda:%s deployed package" % name, "digest": vintage.get("live_code_sha256")},
              ],
              "members": members, "equivalence_claim": eq,
              "last_hop_honesty": ("identities end at a deployed digest: PRESENCE verified, BEHAVIOR not" if reach != "BEHAVIOR"
                                   else "an executing read was taken (see members[].executing_*)")}
    return closure, bundle, obs


EC2_FIXTURE_DEFAULT = os.path.join(WS, "org", "tier2_senior", "0.8.0_AE_CloudComp", "deliverables", "NFRA_DEPLOYCENSUS",
                                   "ec2_onbox_verdicts.json")


def compile_ec2_fixture(service, rows, env, fixture_source, recorded_at="2026-08-18 (NFRA_DEPLOYCENSUS)"):
    """EC2 STAGED-vs-EXECUTING closure from RECORDED reads -- a FIXTURE, said as such on every surface.
    Rule 22a: the staged S3 object is DESIRED (it may be INERT); only the on-instance read is APPLIED
    truth. A member with an on-box hash reaches BEHAVIOR; staged-only reaches PRESENCE_ONLY; closure
    reach = MIN. rows: [{onbox, onbox_sha, staged_key, staged_sha, repo, repo_sha}, ...]."""
    # three PLANE-PURE records (one plane per Observation_Record): staged S3 = DESIRED/aws (may be inert),
    # repo = DESIRED/codebase, on-box = APPLIED/aws (the only applied-plane read of an EC2 box, Rule 22a)
    fx_proc = "NFRA_DEPLOYCENSUS recorded reads replayed as a FIXTURE (%s)" % fixture_source
    o_st = _obs(env, request={"op": "ec2_fixture_staged", "service": service, "source": fixture_source}, status=dict(OK),
                plane="DESIRED", substrate="aws", population="recorded staged-object sha256 per member of %s" % service,
                count=sum(1 for r in rows if r.get("staged_sha")), grain="member file", process="head-object sha256 -- " + fx_proc,
                value=[{"member": os.path.basename(r.get("staged_key") or "?"), "staged_sha": r.get("staged_sha")} for r in rows],
                reason="", pointers=[fixture_source], invalidation=["the staged object is re-read live"])
    o_rp = _obs(env, request={"op": "ec2_fixture_repo", "service": service, "source": fixture_source}, status=dict(OK),
                plane="DESIRED", substrate="codebase", population="recorded repo sha256 per member of %s" % service,
                count=sum(1 for r in rows if r.get("repo_sha")), grain="member file", process="git blob sha256 -- " + fx_proc,
                value=[{"member": os.path.basename(r.get("repo") or r.get("staged_key") or "?"), "repo_sha": r.get("repo_sha")} for r in rows],
                reason="", pointers=[fixture_source], invalidation=["repo bytes at the path change"])
    n_exec = sum(1 for r in rows if r.get("onbox_sha"))
    o_ob = _obs(env, request={"op": "ec2_fixture_onbox", "service": service, "source": fixture_source},
                status=dict(OK) if n_exec else {"acquisition": "ABSENT", "transport": "NOT_ATTEMPTED", "enumeration": "NOT_ATTEMPTED", "parse": "NOT_ATTEMPTED"},
                plane="APPLIED", substrate="aws", population="recorded on-instance sha256sum per member of %s" % service,
                count=n_exec if n_exec else None, grain="member file", process="SSM sha256sum on the instance -- " + fx_proc,
                value=[{"member": os.path.basename(r.get("onbox") or "?"), "onbox_sha": r.get("onbox_sha")} for r in rows if r.get("onbox_sha")] if n_exec else None,
                reason="no recorded on-box read", pointers=[fixture_source], invalidation=["the instance is re-read live"])
    hops = [_hop("logical_fact", "build_input", "DECLARATION", "BUILD_INPUT:EC2_MANIFEST.staged_key", "KNOWN", o_st["request_hash"]),
            _hop("build_input", "staged_bytes", "DIGEST", "BUILD_INPUT:staged_key(head-object sha256)", "KNOWN", o_st["request_hash"],
                 "FIXTURE: recorded staged sha -- DESIRED plane, may be inert"),
            _hop("staged_bytes", "repo_bytes", "BYTES", "BUILD_INPUT:EC2_MANIFEST.repo_path",
                 "KNOWN" if any(r.get("repo_sha") for r in rows) else "UNKNOWN", o_rp["request_hash"]),
            _hop("staged_bytes", "executing", "EXECUTION", "BUILD_INPUT:executing-read-of-staged-member(on-instance sha256sum)",
                 "KNOWN" if n_exec else "NOT_ATTEMPTED", o_ob["request_hash"],
                 "FIXTURE: recorded SSM on-box read covers %d of %d member(s)" % (n_exec, len(rows)))]
    obs = [o_st, o_rp, o_ob]
    members, member_reach, div, unread = [], {}, [], []
    for r in rows:
        m = os.path.basename(r.get("onbox") or r.get("staged_key") or "?")
        reach = "BEHAVIOR" if r.get("onbox_sha") else ("PRESENCE_ONLY" if r.get("staged_sha") else "NONE")
        member_reach[m] = reach
        ob, st, rp = r.get("onbox_sha"), r.get("staged_sha"), r.get("repo_sha")
        if ob and st and ob != st:
            div.append("%s: executing != staged (the staged object is not what runs)" % m)
        if st and rp and st != rp:
            div.append("%s: staged != repo (stale staging)" % m)
        if not ob or not rp:
            unread.append(m)
        members.append({"member": m, "reach": reach, "staged_key": r.get("staged_key"), "staged_sha256": st,
                        "executing_sha256": ob, "executing_source": "FIXTURE: %s" % fixture_source,
                        "repo_path": r.get("repo"), "repo_sha256": rp})
    if div:
        eq = {"state": "DIVERGENT", "basis": "; ".join(div)}
    elif unread:
        eq = {"state": "UNMEASURED", "basis": "no measured divergence, but %d member(s) lack an executing or repo identity: %s" % (len(unread), ", ".join(unread))}
    elif rows:
        eq = {"state": "EQUIVALENT", "basis": "executing == staged == repo for every member (as RECORDED %s)" % recorded_at}
    else:
        eq = {"state": "UNKNOWN", "basis": "no rows"}
    vintage = {"fixture": True, "fixture_source": fixture_source, "recorded_at": recorded_at, "repo_head": "as recorded in the fixture"}
    notes = ["FIXTURE: every hash is a RECORDED read (%s), not a live read tonight; standing is AS-RECORDED and a live re-read "
             "(SSM sha256sum on the instance = the only APPLIED-plane read) is required before any use" % recorded_at,
             "Rule 22a: staged = DESIRED (may be inert), executing = APPLIED"]
    ids = [{"plane": "DESIRED", "locator": "staged S3 keys (members[].staged_key)", "digest_basis": "per-member staged_sha256"},
           {"plane": "SOURCE", "locator": "repo (members[].repo_path)", "digest_basis": "per-member repo_sha256"},
           {"plane": "APPLIED", "locator": "on-instance %s (SSM)" % service, "digest_basis": "per-member executing_sha256 (FIXTURE)"}]
    return _finish(service, hops, "CURRENT", [], {"status": "UNKNOWN", "candidate_homes": []}, vintage, obs,
                   members=members, member_reach=member_reach, digest_match=None, shape_d=False,
                   subject_kind="EC2_SERVICE_RUNS_CODE", extra_notes=notes, identities=ids, eq_override=eq)


def verify(closure_path, smap, reader, repo, env):
    """EXPIRY: re-read the sides a compiled closure depends on; any change => standing INVALIDATED on re-read."""
    c = json.load(open(closure_path, encoding="utf-8"))
    name, v = c["subject"]["ref"], c.get("vintage", {})
    changed = []
    if smap.get("_updated") != v.get("source_map_updated"):
        changed.append("source_map_updated %s -> %s" % (v.get("source_map_updated"), smap.get("_updated")))
    entry = smap.get("functions", {}).get(name) or {}
    if entry.get("artifact_sha256") != v.get("artifact_sha256"):
        changed.append("artifact_sha256 moved")
    fn_resp, _st = reader.get_function(name)
    live = ((fn_resp or {}).get("Configuration") or {}).get("CodeSha256")
    if live != v.get("live_code_sha256"):
        changed.append("live CodeSha256 %s -> %s" % (v.get("live_code_sha256"), live))
    if repo.head() != v.get("repo_head"):
        changed.append("repo HEAD %s -> %s" % (v.get("repo_head"), repo.head()))
    compiled = c["standing"]["value"]
    return {"closure": closure_path, "subject": name, "compiled_standing": compiled,
            "standing_on_reread": "INVALIDATED" if changed else compiled, "changed_sides": changed,
            "verdict": "INVALIDATED" if changed else "STANDS"}


# ---------------------------------------------------------------------------------------------
# Fixtures for the self-test (offline; never AWS)
# ---------------------------------------------------------------------------------------------
class FixtureReader:
    plane_label = "APPLIED"   # same plane as the live reader; fixture-ness rides the request/pointers, not the enum
    substrate = "aws"

    def __init__(self, functions):
        self.functions = functions   # name -> {"CodeSha256": b64, "package": bytes} | "FAIL" | None

    def get_function(self, name):
        f = self.functions.get(name)
        if f is None:
            return None, {"acquisition": "ABSENT", "transport": "SUCCEEDED", "enumeration": "NOT_ATTEMPTED", "parse": "NOT_ATTEMPTED"}
        if f == "FAIL":
            return None, {"acquisition": "UNKNOWN", "transport": "FAILED", "enumeration": "NOT_ATTEMPTED", "parse": "NOT_ATTEMPTED"}
        return {"Configuration": {"CodeSha256": f["CodeSha256"], "LastModified": "fixture"}, "Code": {"Location": "fixture"}}, dict(OK)

    def fetch_package(self, fn_resp):
        for f in self.functions.values():
            if isinstance(f, dict) and f["CodeSha256"] == fn_resp["Configuration"]["CodeSha256"]:
                return f["package"], dict(OK)
        return None, {"acquisition": "UNKNOWN", "transport": "FAILED", "enumeration": "NOT_ATTEMPTED", "parse": "NOT_ATTEMPTED"}


class FixtureRepo(RepoIndex):
    def __init__(self, head, tree, history):
        super().__init__()
        self._h, self.tree, self.history = head, tree, history

    def head(self):
        return self._h

    def bytes_at(self, commit, path):
        return self.tree.get(path) if commit == self._h else self.history.get((commit, path))

    def homes_for(self, member_bytes, basename):
        exact = [p for p, b in self.tree.items() if b == member_bytes]
        same = [p for p in self.tree if os.path.basename(p) == basename]
        return exact, same


def _zip(members: dict) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for n, b in members.items():
            z.writestr(n, b)
    return buf.getvalue()


def self_test() -> int:
    import shutil  # noqa: PLC0415
    import tempfile  # noqa: PLC0415
    env = _envelope()
    ok = []

    def chk(name, cond):
        ok.append(bool(cond))
        print("  [%s] %s" % ("PASS" if cond else "FAIL", name))

    def b64(pkg):
        return base64.b64encode(hashlib.sha256(pkg).digest()).decode()

    # distinct bytes per function: only fn-twohomes has a byte-identical copy at a second path
    A, B, C = b"def run():\n    return 1\n", b"def run():\n    return 2\n", b"def run():\n    return 3\n"
    M1, M2 = b"def a():\n    return 1\n", b"def b():\n    return 2\n"
    S1 = b"def convert(df):\n    df = df.dropna()\n    df['x'] = df['y'] * 2\n    return df\n" * 4
    S2 = S1.replace(b"* 2", b"* 3", 1)   # the canonical copy drifted by one token (sim ~0.98)
    pkgA, pkgB, pkgC, pkgM = _zip({"handler.py": A}), _zip({"handler.py": B}), _zip({"handler.py": C}), _zip({"m1.py": M1, "m2.py": M2})
    pkgS = _zip({"mirror_conversion.py": S1})
    smap = {"_updated": "fixture-v1", "functions": {
        "fn-clean": {"source_dir": "src/clean", "files": ["handler.py"], "artifact_s3_key": "k", "artifact_sha256": _sha256(pkgA), "last_deployed_commit": "c1"},
        "fn-twohomes": {"source_dir": "src/two", "files": ["handler.py"], "artifact_s3_key": "k", "artifact_sha256": _sha256(pkgB), "last_deployed_commit": "c1"},
        "fn-nopointer": {"source_dir": "src/np", "files": ["handler.py"]},
        "fn-dead": {"source_dir": "src/dead", "files": ["handler.py"], "artifact_s3_key": "k", "artifact_sha256": "x", "last_deployed_commit": "c1"},
        "fn-multi": {"source_dir": "src/multi", "files": ["m1.py", "m2.py"], "artifact_s3_key": "k", "artifact_sha256": _sha256(pkgM), "last_deployed_commit": "c1"},
        "fn-bundled": {"source_dir": "src/bundled", "files": ["mirror_conversion.py"], "artifact_s3_key": "k", "artifact_sha256": _sha256(pkgS), "last_deployed_commit": "c1"},
    }}
    tree = {"src/clean/handler.py": A, "src/two/handler.py": B, "src/other/handler.py": B,  # two-homes: byte-identical copy elsewhere
            "src/np/handler.py": C, "src/dead/handler.py": A + b"# dead\n", "src/multi/m1.py": M1, "src/multi/m2.py": M2,
            "src/bundled/mirror_conversion.py": S1, "data/assets/scripts/silver/mirror_conversion.py": S2,   # the bundled-copy-diverged class (sim ~0.9)
            "tools/unrelated/mirror_conversion.py": b"x = 1\n"}                                           # same name, unrelated content: NOT a home
    hist = {("c1", p): b for p, b in tree.items()}
    repo = FixtureRepo("HEADFIX", tree, hist)
    reader = FixtureReader({"fn-clean": {"CodeSha256": b64(pkgA), "package": pkgA},
                            "fn-twohomes": {"CodeSha256": b64(pkgB), "package": pkgB},
                            "fn-nopointer": {"CodeSha256": b64(pkgC), "package": pkgC},
                            "fn-multi": {"CodeSha256": b64(pkgM), "package": pkgM},
                            "fn-bundled": {"CodeSha256": b64(pkgS), "package": pkgS},
                            "fn-dead": "FAIL"})
    c, b, obs = compile_closure("fn-clean", smap, reader, repo, env)
    chk("1 clean single-home closure -> reach PRESENCE_ONLY, standing CURRENT, bundle EQUIVALENT, every hop build-input-resolved",
        c["reach"]["value"] == "PRESENCE_ONLY" and c["standing"]["value"] == "CURRENT" and b["equivalence_claim"]["state"] == "EQUIVALENT"
        and all(h["resolved_via"].startswith("BUILD_INPUT:") for h in c["hops"]))
    chk("1b every acquisition emitted an envelope-built Observation_Record that VALIDATES (n=%d)" % len(obs),
        len(obs) >= 4 and all(env.validate_record(o) == [] for o in obs))
    chk("1c the instance SAYS presence-only-by-construction (a clean run never reads as behavior)",
        any("PRESENCE_ONLY BY CONSTRUCTION" in n for n in c["notes"]) and "PRESENCE verified, BEHAVIOR not" in b["last_hop_honesty"])
    # --- 15: LINE ENDINGS (ESTATE_GOVERNANCE-S30). A CRLF-deployed text member against LF committed bytes is a CORRECT
    # deploy; a real change under CRLF is still a change; a binary member is never normalised; a raw-equal member says RAW.
    E_LF = b"def eol():\n    return 'same'\n"
    E_CRLF = E_LF.replace(b"\n", b"\r\n")
    E_CRLF_CHANGED = E_CRLF.replace(b"same", b"other")
    BIN_LF, BIN_CRLF = b"\x00\x01head\nbody\n", b"\x00\x01head\r\nbody\r\n"
    pkgE, pkgEx, pkgBin = _zip({"eolmod.py": E_CRLF}), _zip({"eolchg.py": E_CRLF_CHANGED}), _zip({"blob.bin": BIN_CRLF})
    smapE = {"_updated": "fixture-eol", "functions": {
        "fn-eol": {"source_dir": "src/eol", "files": ["eolmod.py"], "artifact_s3_key": "k", "artifact_sha256": _sha256(pkgE), "last_deployed_commit": "c1"},
        "fn-eolchg": {"source_dir": "src/eolchg", "files": ["eolchg.py"], "artifact_s3_key": "k", "artifact_sha256": _sha256(pkgEx), "last_deployed_commit": "c1"},
        "fn-bin": {"source_dir": "src/bin", "files": ["blob.bin"], "artifact_s3_key": "k", "artifact_sha256": _sha256(pkgBin), "last_deployed_commit": "c1"}}}
    treeE = {"src/eol/eolmod.py": E_LF, "src/eolchg/eolchg.py": E_LF, "src/bin/blob.bin": BIN_LF}
    repoE = FixtureRepo("HEADFIX", treeE, {("c1", p): v for p, v in treeE.items()})
    readerE = FixtureReader({"fn-eol": {"CodeSha256": b64(pkgE), "package": pkgE},
                             "fn-eolchg": {"CodeSha256": b64(pkgEx), "package": pkgEx},
                             "fn-bin": {"CodeSha256": b64(pkgBin), "package": pkgBin}})
    cE, bE, _ = compile_closure("fn-eol", smapE, readerE, repoE, env)
    mE = bE["members"][0] if bE.get("members") else {}
    chk("15 CRLF-deployed text member vs LF committed bytes -> CURRENT + EQUIVALENT, and the member row and the basis sentence both "
        "NAME the comparison (eq_head true by %s, raw_eq_head false)" % CMP_EOL,
        cE["standing"]["value"] == "CURRENT" and bE["equivalence_claim"]["state"] == "EQUIVALENT"
        and mE.get("eq_head") is True and mE.get("eq_head_basis") == CMP_EOL and mE.get("raw_eq_head") is False
        and CMP_EOL in bE["equivalence_claim"]["basis"])
    cX, bX, _ = compile_closure("fn-eolchg", smapE, readerE, repoE, env)
    mX = bX["members"][0] if bX.get("members") else {}
    chk("15b a REAL content change under CRLF is NOT absorbed by the normalise -> DIVERGENT, eq_head false, basis None",
        bX["equivalence_claim"]["state"] == "DIVERGENT" and mX.get("eq_head") is False and mX.get("eq_head_basis") is None)
    cN, bN, _ = compile_closure("fn-bin", smapE, readerE, repoE, env)
    mN = bN["members"][0] if bN.get("members") else {}
    chk("15c a BINARY member (a NUL byte) that differs only by CR bytes is never normalised -> DIVERGENT on raw bytes",
        bN["equivalence_claim"]["state"] == "DIVERGENT" and mN.get("eq_head") is False)
    m1row = b["members"][0] if b.get("members") else {}
    chk("15d the clean closure's member says its equality is %s and the basis sentence still reads byte-equal" % CMP_RAW,
        m1row.get("eq_head_basis") == CMP_RAW and m1row.get("raw_eq_head") is True
        and "byte-equal" in b["equivalence_claim"]["basis"] and CMP_EOL not in b["equivalence_claim"]["basis"])
    c2, b2, _ = compile_closure("fn-twohomes", smap, reader, repo, env)
    chk("m1 TWO HOMES (byte-identical copy at a second path) -> standing AMBIGUOUS, bundle UNMEASURED -- never CLEAN, never DRIFT",
        c2["standing"]["value"] == "AMBIGUOUS" and "src/other/handler.py" in c2["ambiguity"]["candidate_homes"]
        and b2["equivalence_claim"]["state"] == "UNMEASURED" and c2["reach"]["value"] == "PRESENCE_ONLY")
    c1d, b1d, _ = compile_closure("fn-bundled", smap, reader, repo, env)
    chk("m1b BUNDLED-COPY-DIVERGED (the 08-12 class: deployed == own source dir, a content-similar canonical copy elsewhere) -> AMBIGUOUS; "
        "the same-named UNRELATED file is NOT counted; generic basenames never count by name alone",
        c1d["standing"]["value"] == "AMBIGUOUS" and c1d["ambiguity"]["candidate_homes"] == ["data/assets/scripts/silver/mirror_conversion.py"]
        and b1d["equivalence_claim"]["state"] == "UNMEASURED")
    try:
        _hop("x", "y", "BYTES", "FILENAME:handler.py", "KNOWN", "r")
        m2 = False
    except ValueError as e:
        m2 = "REFUSED" in str(e)
    chk("m2 a FILENAME-resolved hop smuggled in -> the build-input check REFUSES it", m2)
    d = tempfile.mkdtemp(prefix="comp_closure_st_")
    p = os.path.join(d, "fn-clean.closure.json")
    json.dump(c, open(p, "w", encoding="utf-8"), indent=1)
    smap_moved = json.loads(json.dumps(smap))
    smap_moved["_updated"] = "fixture-v2"
    r = verify(p, smap_moved, reader, repo, env)
    chk("m3 one side changed after compile (source-map vintage) -> standing INVALIDATED on re-read", r["standing_on_reread"] == "INVALIDATED" and r["changed_sides"])
    chk("m3 control: nothing changed -> the closure STANDS at its compiled standing", verify(p, smap, reader, repo, env)["verdict"] == "STANDS")
    try:
        _finish("fn-clean", [h for h in c["hops"] if h["evidence_class"] != "EXECUTION"], "CURRENT", [], c["ambiguity"], c["vintage"], [],
                members=b["members"], member_reach={"handler.py": "BEHAVIOR"}, digest_match=True, shape_d=False)
        m4 = False
    except ValueError as e:
        m4 = "last-hop honesty" in str(e)
    chk("m4 a member labelled BEHAVIOR with no KNOWN EXECUTION hop -> REFUSED (last-hop honesty is a constructor constraint)", m4)
    c5, b5, obs5 = compile_closure("fn-dead", smap, reader, repo, env)
    chk("m5 failed acquisition (get-function transport FAILED) -> standing BROKEN, reach NONE, bundle UNKNOWN, record UNKNOWN -- no zero, no clean",
        c5["standing"]["value"] == "BROKEN" and c5["reach"]["value"] == "NONE" and b5["equivalence_claim"]["state"] == "UNKNOWN"
        and any(o["substantive_result"]["state"] == "UNKNOWN" for o in obs5)
        and not any(h["evidence_class"] in ("BYTES", "EXECUTION") for h in c5["hops"]))
    c6, b6, _ = compile_closure("fn-nopointer", smap, reader, repo, env)
    chk("6 entry with NO artifact pointer -> ARTIFACT_POINTER hop UNKNOWN, chain CONTINUES on source_dir+files[] (still a build input); "
        "identity on bytes alone with the provenance caveat stated",
        c6["standing"]["value"] == "CURRENT" and c6["hops"][1]["status"] == "UNKNOWN" and b6["equivalence_claim"]["state"] == "EQUIVALENT"
        and "provenance hop UNKNOWN" in b6["equivalence_claim"]["basis"])
    # shape C (transformed build): members are build output; identity rides the digest chain (base64-form pointer)
    pkgE = _zip({"index.mjs": b"minified-output"})
    smapE = {"_updated": "fx", "functions": {"fn-edge": {"source_dir": "edge/pdr", "files": ["index.mjs"], "artifact_s3_key": "k",
                                                         "artifact_sha256": b64(pkgE), "last_deployed_commit": "c1"}}}
    treeE = {"edge/pdr/index.mjs": b"export const source = 1;\n"}
    cE, bE, _ = compile_closure("fn-edge", smapE, FixtureReader({"fn-edge": {"CodeSha256": b64(pkgE), "package": pkgE}}), FixtureRepo("H", treeE, {}), env)
    chk("12 SHAPE C transformed build: member bytes NOT byte-compared (comparable=False), identity via live digest == artifact pointer (base64 form) -> EQUIVALENT",
        bE["equivalence_claim"]["state"] == "EQUIVALENT" and bE["members"][0].get("comparable") is False and cE["standing"]["value"] == "CURRENT"
        and "provenance-chain" in cE["hops"][3]["resolved_via"])
    smapE2 = json.loads(json.dumps(smapE))
    smapE2["functions"]["fn-edge"]["artifact_sha256"] = b64(pkgA)
    _cE2, bE2, _ = compile_closure("fn-edge", smapE2, FixtureReader({"fn-edge": {"CodeSha256": b64(pkgE), "package": pkgE}}), FixtureRepo("H", treeE, {}), env)
    chk("12b SHAPE C with a digest MISMATCH -> UNMEASURED (the chain cannot tie the live package to the build input; never DIVERGENT-by-bytes)",
        bE2["equivalence_claim"]["state"] == "UNMEASURED")
    # EC2 fixture: staged = DESIRED, on-box = EXECUTING
    rows_partial = [{"onbox": "/a/x.sh", "onbox_sha": "1", "staged_key": "s3://b/x.sh", "staged_sha": "1", "repo": "r/x.sh", "repo_sha": "1"},
                    {"onbox": None, "onbox_sha": None, "staged_key": "s3://b/y.sh", "staged_sha": "2", "repo": "r/y.sh", "repo_sha": "2"}]
    cX, bX, oX = compile_ec2_fixture("svc", rows_partial, env, "fixture:test")
    chk("13 EC2 FIXTURE, one member on-box-read and one staged-only -> per-member {BEHAVIOR, PRESENCE_ONLY}, closure reach MIN=PRESENCE_ONLY, "
        "equivalence UNMEASURED (executing identity unread for y.sh), FIXTURE said on the instance",
        cX["reach"]["per_member"] == {"x.sh": "BEHAVIOR", "y.sh": "PRESENCE_ONLY"} and cX["reach"]["value"] == "PRESENCE_ONLY"
        and bX["equivalence_claim"]["state"] == "UNMEASURED" and any("FIXTURE" in n for n in cX["notes"]) and cX["vintage"]["fixture"] is True
        and all(env.validate_record(o) == [] for o in oX))
    rows_div = [{"onbox": "/a/x.sh", "onbox_sha": "9", "staged_key": "s3://b/x.sh", "staged_sha": "1", "repo": "r/x.sh", "repo_sha": "1"}]
    cD, bD, _ = compile_ec2_fixture("svc", rows_div, env, "fixture:test")
    chk("13b EC2 FIXTURE, on-box != staged -> reach BEHAVIOR (read taken) and equivalence DIVERGENT naming the hop 'executing != staged'",
        cD["reach"]["value"] == "BEHAVIOR" and bD["equivalence_claim"]["state"] == "DIVERGENT" and "executing != staged" in bD["equivalence_claim"]["basis"])
    c7, _b7, _ = compile_closure("fn-absent", smap, reader, repo, env)
    chk("7 no source-map entry -> BROKEN at the DECLARATION hop (broken, never presence)", c7["standing"]["value"] == "BROKEN" and c7["reach"]["value"] == "NONE")
    c8, _b8, _ = compile_closure("fn-multi", smap, reader, repo, env, execution_reads={"m1.py": {"digest": _sha256(M1), "source": "fixture:on-box sha256sum"}})
    chk("8 MULTI-MEMBER: one member has an executing read, one does not -> per-member {BEHAVIOR, PRESENCE_ONLY}, closure reach = MIN = PRESENCE_ONLY (weakest link; CTO 63853)",
        c8["reach"]["per_member"] == {"m1.py": "BEHAVIOR", "m2.py": "PRESENCE_ONLY"} and c8["reach"]["value"] == "PRESENCE_ONLY")
    c9, b9, _ = compile_closure("fn-multi", smap, reader, repo, env, execution_reads={"m1.py": {"digest": _sha256(M1), "source": "fx"}, "m2.py": {"digest": _sha256(M2), "source": "fx"}})
    chk("8b every member covered by an executing read -> closure reach BEHAVIOR (the only way to reach it)", c9["reach"]["value"] == "BEHAVIOR" and "executing read" in b9["last_hop_honesty"])
    # CTO 63933 specimen (CTO_D4_TRUESHARES_FETCH_READ_20260820_2200Z.md @25c1b4cca9 sec.5): an applied env flag + the
    # token present in the deployed package + a green scheduled run -- every PRESENCE limb true, and the arm is inert.
    # The presence chain compiles CURRENT/EQUIVALENT and reach stays PRESENCE_ONLY; only an EXERCISED-plane oracle
    # read (does the output carry rows from the arm? 0 of 114) can lift a member to BEHAVIOR -- and then it says inert.
    c14, b14, o14 = compile_closure("fn-clean", smap, reader, repo, env)
    chk("14 CTO-63933 SPECIMEN: presence bar fully satisfied (CURRENT + EQUIVALENT) AND records genuinely APPLIED-plane -> reach "
        "stays PRESENCE_ONLY. APPLIED says WHERE the evidence was taken; BEHAVIOR says HOW FAR the chain got -- orthogonal",
        c14["standing"]["value"] == "CURRENT" and b14["equivalence_claim"]["state"] == "EQUIVALENT"
        and c14["reach"]["value"] == "PRESENCE_ONLY" and "BEHAVIOR not" in b14["last_hop_honesty"]
        and any(o["plane"] == "APPLIED" for o in o14))
    # the mutant a future maintainer would actually write, thinking they were simplifying (CTO 63975):
    # derive reach FROM the plane label. On the specimen it says BEHAVIOR where the truth is PRESENCE_ONLY.
    mutant_reach = "BEHAVIOR" if any(o["plane"] == "APPLIED" for o in o14) else "NONE"
    chk("14c MUTANT (reach inferred from plane) is DISCRIMINATED: on the specimen it claims BEHAVIOR, the constructor says "
        "PRESENCE_ONLY -- a plane->reach inference cannot survive this battery",
        mutant_reach == "BEHAVIOR" and c14["reach"]["value"] == "PRESENCE_ONLY" and mutant_reach != c14["reach"]["value"])
    c14x, _b14x, o14x = compile_closure("fn-clean", smap, reader, repo, env, execution_reads={
        "handler.py": {"digest": "oracle: output rows source=trueshares 0 of 114", "source": "exercised-path oracle (output parquet query)", "plane": "EXERCISED"}})
    chk("14b the same closure with an EXERCISED-plane oracle read supplied -> reach BEHAVIOR via a KNOWN EXECUTION hop whose record is plane EXERCISED",
        c14x["reach"]["value"] == "BEHAVIOR" and any(o["plane"] == "EXERCISED" for o in o14x))
    cA, _, _ = compile_closure("fn-clean", smap, reader, repo, env)
    cB, _, _ = compile_closure("fn-clean", smap, reader, repo, env)

    def strip(x):
        return json.dumps({k: v for k, v in x.items() if k not in ("vintage", "observation_record_refs")}, sort_keys=True)
    chk("9 determinism: two compiles of the same inputs agree on every field but timestamps", strip(cA) == strip(cB))
    chk("10 every record carries the RATIFIED plane enum + a substrate (C1 rider @6f944857c4); no reach/standing value is computed from plane",
        all(o["plane"] in ("DESIRED", "APPLIED", "EXERCISED") and o["substrate"] in ("aws", "portal", "codebase", "ms") for o in obs + oX))
    chk("11 no ordering language survives on the objects: reach+standing are a PAIR, no 'precedence'/'terminal' field",
        "terminal_class" not in c and "precedence" not in json.dumps(c).lower())
    shutil.rmtree(d, ignore_errors=True)
    n = sum(1 for x in ok if x)
    print("--- comp-closure self-test: %d/%d passed ---" % (n, len(ok)))
    return 0 if n == len(ok) else 1


_USAGE = """comp-closure -- NFRA_EPISTEMY C3: identity + support-closure compiler. Usage:
  comp-closure compile <lambda-name> [--out DIR]   compile Support_Closure + Identity_Bundle + Observation_Records (read-only AWS)
  comp-closure verify <closure.json>               re-read the sides; any change -> standing INVALIDATED
  comp-closure ec2-fixture <service> [--fixture F] EC2 staged(DESIRED)-vs-executing(APPLIED) closure from RECORDED reads -- a FIXTURE, said so
  comp-closure --self-test                         offline battery m1-m5 + controls (fixtures, never AWS)
  comp-closure --help | -h                         this usage (never writes)
Unknown arguments REFUSE (rc 2). reach {NONE,PRESENCE_ONLY,BEHAVIOR} per member (closure = MIN); standing {BROKEN,AMBIGUOUS,CURRENT,INVALIDATED}."""


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or "--help" in args or "-h" in args:
        print(_USAGE)
        return 0
    if "--self-test" in args:
        return self_test()
    cmd = args[0]
    if cmd not in ("compile", "verify", "ec2-fixture"):
        print("comp-closure: UNKNOWN argument %r -- REFUSED (rc 2).\n%s" % (cmd, _USAGE), file=sys.stderr)
        return 2
    flags = [a for a in args[1:] if a.startswith("-") and a not in ("--out", "--fixture")]
    if flags or len(args) < 2:
        print("comp-closure: UNKNOWN/missing argument(s) %s -- REFUSED (rc 2)." % (flags or ["<target>"]), file=sys.stderr)
        return 2
    try:
        env = _envelope()
        out = args[args.index("--out") + 1] if "--out" in args else OUT_DIR
        os.makedirs(out, exist_ok=True)
        if cmd == "ec2-fixture":
            service = args[1]
            fx = args[args.index("--fixture") + 1] if "--fixture" in args else EC2_FIXTURE_DEFAULT
            rows = json.load(open(fx, encoding="utf-8")).get(service)
            if not isinstance(rows, list):
                print("comp-closure: ec2-fixture needs the LIST row form for %r in %s (got %s) -- REFUSED (rc 2)."
                      % (service, fx, type(rows).__name__), file=sys.stderr)
                return 2
            c, b, obs = compile_ec2_fixture(service, rows, env, os.path.relpath(fx, WS).replace("\\", "/"))
            base = os.path.join(out, "ec2-fixture." + service)
            json.dump(c, open(base + ".closure.json", "w", encoding="utf-8"), indent=1)
            json.dump(b, open(base + ".bundle.json", "w", encoding="utf-8"), indent=1)
            json.dump(obs, open(base + ".observations.json", "w", encoding="utf-8"), indent=1)
            print("comp-closure ec2-fixture %s: reach=%s per_member=%s equivalence=%s | FIXTURE (recorded %s) -- not a live read"
                  % (service, c["reach"]["value"], c["reach"]["per_member"], b["equivalence_claim"]["state"], c["vintage"]["recorded_at"]))
            print("  basis: %s" % b["equivalence_claim"]["basis"])
            print("  wrote %s.{closure,bundle,observations}.json" % base)
            return 0
        fns = load_function_map(WS)   # raises when the folder is absent or empty (loud, never an empty map)
        # the folder's stamp: a sha256 of its entries (the retired map's _updated field has no folder counterpart)
        smap = {"_updated": _sha256(json.dumps(fns, sort_keys=True).encode("utf-8")), "functions": fns}
        reader, repo = LiveReader(), RepoIndex()
        if cmd == "compile":
            name = args[1]
            c, b, obs = compile_closure(name, smap, reader, repo, env)
            bad = [e for o in obs for e in env.validate_record(o)]
            if bad:
                print("comp-closure: envelope validation FAILED: %s" % bad[:3], file=sys.stderr)
                return 1
            base = os.path.join(out, name)
            json.dump(c, open(base + ".closure.json", "w", encoding="utf-8"), indent=1)
            json.dump(b, open(base + ".bundle.json", "w", encoding="utf-8"), indent=1)
            json.dump(obs, open(base + ".observations.json", "w", encoding="utf-8"), indent=1)
            print("comp-closure compile %s: reach=%s standing=%s ambiguity=%s equivalence=%s | hops=%d observations=%d (all envelope-valid) | members compared=%d"
                  % (name, c["reach"]["value"], c["standing"]["value"], c["ambiguity"]["status"], b["equivalence_claim"]["state"],
                     len(c["hops"]), len(obs), sum(1 for m in b["members"] if m.get("reach") != "NONE")))
            for r in c["standing"]["reasons"]:
                print("  reason: %s" % r)
            if c["ambiguity"]["candidate_homes"]:
                print("  other plausible homes: %s" % ", ".join(c["ambiguity"]["candidate_homes"][:8]))
            print("  %s" % PRESENCE_NOTE)
            print("  wrote %s.{closure,bundle,observations}.json" % base)
            return 0
        res = verify(args[1], smap, reader, repo, env)
        print("comp-closure verify %s: compiled standing=%s on re-read=%s verdict=%s%s"
              % (res["subject"], res["compiled_standing"], res["standing_on_reread"], res["verdict"],
                 ("; changed: " + "; ".join(res["changed_sides"])) if res["changed_sides"] else ""))
        return 0
    except Exception as e:  # noqa: BLE001 -- a compiler that cannot evaluate is an ERROR, never a clean closure
        print("comp-closure: ERROR (%s: %s)" % (type(e).__name__, e), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

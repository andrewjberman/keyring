#!/usr/bin/env python3
"""intake_fetch.py -- fetch ONE exact wheel file into the holding folder, with a record.

Route hop 4 ("fetched and held"). One wheel file for one approved line: no dependency
resolution, nothing installed, nothing unpacked, nothing imported. The file waits unchecked
in <holding root>/holding/<batch>/ until the check tool moves it. Every fetch writes a
FETCH record (schema intake-fetch/1) under org/devices/intake/records/<batch>/, also when the
fetch is refused before any request or fails midway.

  fetch --batch B --name N --version V --python-tag T --abi-tag T --platform-tag T
        [--index-base URL] [--approved-by PATH]
  fetch --ecosystem npm --batch B --name N --version V --approved-by PATH [--registry-base URL]
        The npm limb (CTO ruling 2026-10-16, cell CT-cc-1). The approval file must contain the exact line name@version
        (a scoped name whole: @babel/core@7.29.7), checked before any socket; the request goes ONLY to
        https://registry.npmjs.org/<name>/<version> (a scoped name as @babel%2Fcore), then to that document's dist.tarball,
        which must be on registry.npmjs.org. ONE .tgz is held UNCHECKED under the held name
        <name with @ removed and / as __>-<version>.tgz (for example babel__core-7.29.7.tgz). --registry-base is for a
        LOOPBACK test registry only. The tags are not used by npm.
  list  --batch B
  resolve --closure <closure json> --target cp312-linux_x86_64 --approved-by PATH [--index-base URL]
        [--host-pydeps <json>] [--out <json>]
        Names ONE exact wheel file per closure member that the host does not already satisfy, from the index's
        release document (one GET per member: <base>/pypi/<name>/<version>/json). It downloads nothing and never
        picks a source archive; a member with no fitting wheel is NO-WHEEL with its reason. Before ANY socket the
        approval file must contain the exact name==version of every member to resolve. Prints the STOP lines of the
        index-side re-check (NEW-MEMBER, SPECIFIER-MISMATCH, HOST-CONFLICT) and the last line
        INTAKE-RESOLVE target=... members=... chosen=... no_wheel=... requests=... ok=... (see RESOLVE below).

The default index base is the public index. Against it the tool refuses to run unless
--approved-by names an existing file whose text contains the exact `name==version`; that
check is the FIRST thing fetch does for a non-loopback base -- before any socket and before
any name lookup. Standard library only.

Environment (tests redirect with these; unset means the derived defaults):
  OPAL_INTAKE_ROOT     holding root (default: <workspace drive>/opal-intake, outside every git tree)
  OPAL_INTAKE_RECORDS  records root (default: org/devices/intake/records beside this file)
"""
import argparse
import datetime
import hashlib
import http.client
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

SCHEMA = "intake-fetch/1"
PUBLIC_BASE = "https://pypi.org"
PUBLIC_HOSTS = ("pypi.org", "files.pythonhosted.org")
LOOPBACK_HOSTS = ("127.0.0.1", "localhost", "::1")
TIMEOUT = 30
MAX_HOPS = 5
CHUNK = 65536
JSON_CAP = 64 * 1024 * 1024
ERR_CAP = 65536

_BATCH_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")
_NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
_VER_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9.!+_]*$")
_TAG_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.]*$")
_SHA_RE = re.compile(r"^[0-9a-f]{64}$")
# npm limb (CT-cc-1): the public registry, its one host, the names and versions it accepts, and the tarball size cap
NPM_PUBLIC_BASE = "https://registry.npmjs.org"
NPM_PUBLIC_HOSTS = ("registry.npmjs.org",)
NPM_TARBALL_CAP = 200 * 1024 * 1024
NPM_NAME_RE = re.compile(r"^(?:@[a-z0-9][a-z0-9._-]*/)?[a-z0-9][a-z0-9._-]*$")
NPM_VERSION_RE = re.compile(r"^[0-9A-Za-z][0-9A-Za-z.+-]*$")


class Refuse(Exception):
    """The tool declines to proceed (outcome refused)."""


class Fail(Exception):
    """The tool tried and could not (outcome failed)."""


def utcnow():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def this_device():
    """This box's canonical register name (lib/devices.py this_device, from AGENTBUS_DEVICE), or None when the
    box cannot be named. None is written as null and the downloads reader counts it as unattributed."""
    repo = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
    lib = os.path.join(repo, "lib")
    if lib not in sys.path:
        sys.path.insert(0, lib)
    import devices  # the register reader (lib/devices.py); fail-closed: a broken register names no box
    try:
        name, _basis = devices.this_device()
    except devices.RegisterError:
        return None
    return name


def norm_dist(name):
    return re.sub(r"[-_.]+", "_", name).lower()


def build_file_name(name, version, python_tag, abi_tag, platform_tag):
    return "%s-%s-%s-%s-%s.whl" % (norm_dist(name), version, python_tag, abi_tag, platform_tag)


def _split_wheel(file_name):
    if not file_name.endswith(".whl"):
        return None
    parts = file_name[:-4].split("-")
    if len(parts) < 5:
        return None
    return "-".join(parts[:-4]), parts[-4:]


def same_file(built, candidate):
    """Distribution part compared after normalisation, every other part exact."""
    b, c = _split_wheel(built), _split_wheel(candidate)
    if b is None or c is None:
        return False
    return norm_dist(b[0]) == norm_dist(c[0]) and b[1] == c[1]


def npm_held_name(name, version):
    """The held file name of one npm tarball: the name with @ removed and / as __, a dash, the version, .tgz.
    Rule (page APPROVAL_AND_SIGNED_FILE_DEMANDS.md section 1a): @babel/core 7.29.7 -> babel__core-7.29.7.tgz."""
    return "%s-%s.tgz" % (name.replace("@", "").replace("/", "__"), version)


def iso_time(text):
    """A timezone-aware datetime for an ISO 8601 time that states its zone (npm's 'Z' form included), else None."""
    try:
        dt = datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None
    return dt if dt.tzinfo is not None else None


def npm_line_pattern(line):
    """The exact-line search for an npm approval line name@version: not preceded by a letter, digit, . _ - / @ or ~,
    not followed by a letter, digit, . _ + ! - or ~. A bare core@1.0.0 never matches a line @babel/core@1.0.0."""
    return r"(?<![A-Za-z0-9._/@~-])%s(?![A-Za-z0-9._+!~-])" % re.escape(line)


def npm_approval_gate(path, lines):
    """Before ANY socket: the approval file must exist and contain the exact name@version of every line (npm form)."""
    if not path or not os.path.isfile(path):
        raise Refuse("approval file does not exist: %s" % ascii_text(os.path.basename(path or "-")))
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8", "replace")
    missing = [ln for ln in lines if not re.search(npm_line_pattern(ln), text)]
    if missing:
        raise Refuse("approval file %s lacks %d of %d exact line(s): %s" % (
            ascii_text(os.path.basename(path)), len(missing), len(lines), ", ".join(missing)))
    return {"file": os.path.basename(path), "sha256": hashlib.sha256(raw).hexdigest(), "lines_matched": len(lines)}


# ---------------------------------------------------------------- locations

def holding_root():
    env = os.environ.get("OPAL_INTAKE_ROOT")
    if env:
        return os.path.abspath(env)
    here = os.path.abspath(__file__)
    if os.name == "nt":
        drive = os.path.splitdrive(here)[0]
        return drive + os.sep + "opal-intake"
    if os.path.isdir("/cygdrive/c"):
        return "/cygdrive/c/opal-intake"
    return "/c/opal-intake"


def records_root():
    env = os.environ.get("OPAL_INTAKE_RECORDS")
    if env:
        return os.path.abspath(env)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "records")


# ---------------------------------------------------------------- host rule

def is_loopback_base(base):
    try:
        host = urllib.parse.urlparse(base).hostname
    except ValueError:
        return False
    return host in LOOPBACK_HOSTS


def _port(parsed):
    try:
        if parsed.port is not None:
            return parsed.port
    except ValueError:
        return -1
    return 443 if parsed.scheme == "https" else 80


class Policy:
    """The closed set of (scheme, host, port) a request may go to, derived from the index base."""

    def __init__(self, base, public_hosts=PUBLIC_HOSTS):
        parsed = urllib.parse.urlparse(base)
        self.loopback = parsed.hostname in LOOPBACK_HOSTS
        self.host_port = (parsed.hostname, _port(parsed))
        self.public_hosts = tuple(public_hosts)

    def check(self, url, segment=None):
        """Raise Refuse unless url is inside the closed set (and ends in `segment` when given)."""
        try:
            p = urllib.parse.urlparse(url)
            port = _port(p)
            host = p.hostname
        except ValueError:
            raise Refuse("unparseable url: %r" % url[:200])
        if p.username is not None or p.password is not None:
            raise Refuse("url carries credentials: %s" % url[:200])
        if self.loopback:
            if p.scheme not in ("http", "https"):
                raise Refuse("scheme %r not allowed on a loopback base: %s" % (p.scheme, url[:200]))
            if (host, port) != self.host_port:
                raise Refuse("host %s:%s is outside the closed set %s:%s: %s" % (
                    host, port, self.host_port[0], self.host_port[1], url[:200]))
        else:
            if p.scheme != "https":
                raise Refuse("non-HTTPS url on the public base: %s" % url[:200])
            if host not in self.public_hosts or port != 443:
                raise Refuse("host %s:%s is outside the closed set %s: %s" % (
                    host, port, ",".join(self.public_hosts), url[:200]))
        if segment is not None:
            last = urllib.parse.unquote(p.path.rsplit("/", 1)[-1])
            if last != segment:
                raise Refuse("final path segment %r is not the exact file name %r" % (last, segment))


# ---------------------------------------------------------------- HTTP (manual redirects)

class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def make_opener(loopback):
    """urllib opener that never follows a redirect itself. Loopback never uses a proxy."""
    handlers = [_NoRedirect()]
    if loopback:
        handlers.append(urllib.request.ProxyHandler({}))
    return urllib.request.build_opener(*handlers)


# ---------------------------------------------------------------- the fetch

class Fetch:
    def __init__(self, a):
        self.a = a
        self.eco = getattr(a, "ecosystem", None) or "pypi"
        if self.eco == "npm":
            self.base = (getattr(a, "registry_base", None) or NPM_PUBLIC_BASE).rstrip("/")
            self.policy = Policy(self.base, NPM_PUBLIC_HOSTS)
        else:
            self.base = (a.index_base or PUBLIC_BASE).rstrip("/")
            self.policy = Policy(self.base)
        self.file_name = None
        self.index_file_name = None
        self.part = None
        self.sha_seen = None
        self.size_seen = None
        self.rec = {
            "schema": SCHEMA,
            "batch": a.batch,
            "requested": {
                "name": a.name, "version": a.version, "python_tag": a.python_tag,
                "abi_tag": a.abi_tag, "platform_tag": a.platform_tag, "file_name": None,
            },
            "index_base": self.base,
            "requests": [],
            "published": None,
            "project": None,
            "attestation": "unread",
            "attestation_url": None,
            "held_path": None,
            "held_sha256": None,
            "held_bytes": None,
            "outcome": None,
            "reason": None,
            "fetched_by": os.environ.get("OPAL_AGENT_SERIAL") or "unknown",
            "device": this_device(),
            "at": utcnow(),
        }
        if self.eco == "npm":
            self.rec["ecosystem"] = "npm"

    # -- request machinery -------------------------------------------------

    def _one_request(self, url, entry, sink, limit):
        """One attempt. Returns (status, location, body_bytes_or_None). Raises on connection error."""
        req = urllib.request.Request(url, method="GET", headers={"User-Agent": "opal-intake-fetch/1"})
        try:
            resp = make_opener(self.policy.loopback).open(req, timeout=TIMEOUT)
        except urllib.error.HTTPError as e:
            resp = e
        try:
            status = resp.status if hasattr(resp, "status") else resp.code
            entry["status"] = status
            if 300 <= status < 400:
                return status, resp.headers.get("Location"), None
            total = 0
            chunks = []
            if sink and status == 200:
                sha = hashlib.sha256()
                with open(self.part, "wb") as out:
                    while True:
                        block = resp.read(CHUNK)
                        if not block:
                            break
                        total += len(block)
                        sha.update(block)
                        entry["bytes"] = total
                        if limit is not None and total > limit:
                            break
                        out.write(block)
                self.sha_seen, self.size_seen = sha.hexdigest(), total
                return status, None, None
            cap = JSON_CAP if status == 200 else ERR_CAP
            while True:
                block = resp.read(CHUNK)
                if not block:
                    break
                total += len(block)
                if total > cap:
                    entry["bytes"] = total
                    if status == 200:
                        raise Fail("response larger than %d bytes: %s" % (cap, url[:200]))
                    break
                chunks.append(block)
            entry["bytes"] = total
            return status, None, b"".join(chunks)
        finally:
            resp.close()

    def get(self, url, segment=None, sink=False, limit=None):
        """GET with manual redirect following. Returns (status, body). Every hop is policy-checked
        BEFORE it is requested and recorded; at most one retry per hop on a connection error."""
        for _hop in range(MAX_HOPS + 1):
            self.policy.check(url, segment)
            result = None
            for attempt in (1, 2):
                entry = {"url": url, "method": "GET", "status": None, "bytes": 0, "at": utcnow()}
                self.rec["requests"].append(entry)
                try:
                    result = self._one_request(url, entry, sink, limit)
                    break
                except (Fail, Refuse):
                    raise
                except (urllib.error.URLError, OSError, http.client.HTTPException) as e:
                    entry["error"] = ("%s: %s" % (type(e).__name__, e))[:200]
                    if attempt == 2:
                        raise Fail("connection error after one retry: %s" % entry["error"])
                    entry["retried"] = True
            status, location, body = result
            if 300 <= status < 400:
                if not location:
                    raise Fail("redirect %d with no Location from %s" % (status, url[:200]))
                url = urllib.parse.urljoin(url, location)
                continue
            return status, body
        raise Refuse("more than %d redirect hops" % MAX_HOPS)

    def get_json(self, url):
        status, body = self.get(url)
        if status != 200:
            return status, None
        try:
            doc = json.loads(body.decode("utf-8"))
        except (ValueError, UnicodeDecodeError):
            raise Fail("unreadable JSON from %s" % url[:200])
        if not isinstance(doc, dict):
            raise Fail("JSON document from %s is not an object" % url[:200])
        return status, doc

    # -- the sequence ------------------------------------------------------

    def validate(self):
        a = self.a
        bad = []
        if not _NAME_RE.match(a.name):
            bad.append("name")
        if not _VER_RE.match(a.version):
            bad.append("version")
        for label, value in (("python-tag", a.python_tag), ("abi-tag", a.abi_tag), ("platform-tag", a.platform_tag)):
            if not _TAG_RE.match(value):
                bad.append(label)
        if bad:
            raise Refuse("invalid request value: %s" % ",".join(bad))
        self.file_name = build_file_name(a.name, a.version, a.python_tag, a.abi_tag, a.platform_tag)
        self.rec["requested"]["file_name"] = self.file_name

    def approval(self):
        a = self.a
        if not a.approved_by:
            return
        info = {"path": a.approved_by, "sha256": None, "matched": None}
        self.rec["approval"] = info
        if not os.path.isfile(a.approved_by):
            return
        with open(a.approved_by, "rb") as fh:
            raw = fh.read()
        info["sha256"] = hashlib.sha256(raw).hexdigest()
        line = "%s==%s" % (a.name, a.version)
        text = raw.decode("utf-8", "replace")
        info["matched"] = bool(re.search(r"(?<![A-Za-z0-9._-])%s(?![A-Za-z0-9._+!])" % re.escape(line), text))

    def gate_public(self):
        """FIRST act for a non-loopback base: the approval file. No socket, no name lookup."""
        if self.policy.loopback:
            return
        self.approval()
        line = "%s==%s" % (self.a.name, self.a.version)
        info = self.rec.get("approval")
        if not self.a.approved_by:
            raise Refuse("public index needs --approved-by <file> naming %s" % line)
        if info["sha256"] is None:
            raise Refuse("approval file does not exist: %s" % self.a.approved_by)
        if not info["matched"]:
            raise Refuse("approval file does not contain the exact %s" % line)
        parsed = urllib.parse.urlparse(self.base)
        if parsed.scheme != "https" or parsed.hostname != "pypi.org" or _port(parsed) != 443:
            raise Refuse("index base %s is not the public index" % self.base)

    def run(self):
        if self.eco == "npm":
            return self.run_npm()
        a = self.a
        self.validate()
        self.gate_public()
        if self.policy.loopback:
            self.approval()
        q = urllib.parse.quote
        # (a) the release document: find the exact file
        status, doc = self.get_json("%s/pypi/%s/%s/json" % (self.base, q(a.name), q(a.version)))
        if status == 404:
            raise Refuse("no such release on the index (HTTP 404)")
        if status != 200:
            raise Fail("release document answered HTTP %s" % status)
        urls = doc.get("urls")
        if not isinstance(urls, list):
            raise Fail("release document has no urls list")
        have = [e.get("filename") for e in urls if isinstance(e, dict) and isinstance(e.get("filename"), str)]
        self.rec["release_files"] = have
        hits = [e for e in urls if isinstance(e, dict) and isinstance(e.get("filename"), str)
                and same_file(self.file_name, e["filename"])]
        if not hits:
            raise Refuse("no such file for this release")
        if len({e["filename"] for e in hits}) > 1:
            raise Refuse("more than one index entry matches the file name: %s" % ",".join(e["filename"] for e in hits))
        entry = hits[0]
        self.index_file_name = entry["filename"]
        self.rec["index_file_name"] = self.index_file_name
        digests = entry.get("digests") if isinstance(entry.get("digests"), dict) else {}
        sha = digests.get("sha256")
        size = entry.get("size")
        self.rec["published"] = {
            "sha256": sha, "size": size, "upload_time": entry.get("upload_time_iso_8601"),
            "yanked": entry.get("yanked"), "requires_python": entry.get("requires_python"),
        }
        if entry.get("yanked"):
            raise Refuse("file is yanked on the index (%s)" % (entry.get("yanked_reason") or "no reason given"))
        if not (isinstance(sha, str) and _SHA_RE.match(sha)) or not isinstance(size, int) or isinstance(size, bool) or size < 0:
            raise Refuse("index publishes no usable sha256 and size for this file")
        file_url = entry.get("url")
        if not isinstance(file_url, str):
            raise Refuse("index entry has no file url")
        # the file's own address is checked BEFORE any further request is made
        self.policy.check(file_url, self.index_file_name)
        # (b) the project document
        status, proj = self.get_json("%s/pypi/%s/json" % (self.base, q(a.name)))
        if status != 200:
            raise Fail("project document answered HTTP %s" % status)
        self.rec["project"] = self.project_facts(proj, a.version)
        # (c) the attestation address
        att_url = "%s/integrity/%s/%s/%s/provenance" % (self.base, q(a.name), q(a.version), q(self.index_file_name))
        self.rec["attestation_url"] = att_url
        try:
            att_status, _ = self.get(att_url)
            self.rec["attestation"] = {200: "present", 404: "absent"}.get(att_status, "unread")
        except (Fail, Refuse):
            self.rec["attestation"] = "unread"
        # (d) the file, streamed to a part file and hashed while written
        folder = os.path.join(holding_root(), "holding", a.batch)
        os.makedirs(folder, exist_ok=True)
        final = os.path.join(folder, self.file_name)
        self.part = final + ".part"
        st, _ = self.get(file_url, segment=self.index_file_name, sink=True, limit=size)
        if st != 200:
            raise Fail("file url answered HTTP %s" % st)
        self.rec["received_sha256"], self.rec["received_bytes"] = self.sha_seen, self.size_seen
        if self.size_seen != size or self.sha_seen != sha:
            raise Refuse("digest mismatch: published sha256=%s size=%s, received sha256=%s size=%s" % (
                sha[:12], size, self.sha_seen[:12], self.size_seen))
        os.replace(self.part, final)
        self.part = None
        self.rec["held_path"] = "holding/%s/%s" % (a.batch, self.file_name)
        self.rec["held_sha256"], self.rec["held_bytes"] = self.sha_seen, self.size_seen
        self.rec["outcome"], self.rec["reason"] = "held", "digest and size equal the published values"

    # -- the npm limb (CT-cc-1; the CTO ruling of 2026-10-16) --------------

    def run_npm(self):
        """Approval line first (no socket on a refusal), then the version document, then its dist.tarball on the
        registry host only, then ONE .tgz held unchecked. The checks in intake_check.py read it next."""
        a = self.a
        # the name is checked first, so every refusal below is recorded under the package's own held name
        if not (isinstance(a.name, str) and NPM_NAME_RE.match(a.name)):
            raise Refuse("invalid npm package name: %s" % ascii_text(a.name)[:80])
        if not NPM_VERSION_RE.match(a.version or ""):
            raise Refuse("invalid npm version: %s" % ascii_text(a.version)[:80])
        self.file_name = npm_held_name(a.name, a.version)
        self.rec["requested"]["file_name"] = self.file_name
        if a.index_base:
            raise Refuse("--ecosystem npm takes --registry-base, not --index-base")
        if a.registry_base and not is_loopback_base(a.registry_base):
            raise Refuse("--registry-base is for a loopback test registry only; the public registry is %s" % NPM_PUBLIC_BASE)
        line = "%s@%s" % (a.name, a.version)
        if not a.approved_by:
            raise Refuse("npm fetch needs --approved-by <file> naming the exact line %s" % line)
        self.rec["approval"] = npm_approval_gate(a.approved_by, [line])
        # (a) the version document: one address, the exact name and version
        q = urllib.parse.quote
        status, doc = self.get_json("%s/%s/%s" % (self.base, q(a.name, safe="@"), q(a.version, safe="")))
        if status == 404:
            raise Refuse("no such version on the registry (HTTP 404)")
        if status != 200:
            raise Fail("version document answered HTTP %s" % status)
        dist = doc.get("dist")
        if not isinstance(dist, dict):
            raise Fail("registry document has no dist object")
        tarball, integrity, shasum = dist.get("tarball"), dist.get("integrity"), dist.get("shasum")
        if not isinstance(tarball, str) or not tarball:
            raise Refuse("registry document names no dist.tarball")
        # (b) the tarball's address is checked BEFORE any request for it: the registry host only
        self.policy.check(tarball)
        last = urllib.parse.unquote(urllib.parse.urlparse(tarball).path.rsplit("/", 1)[-1])
        if not last.endswith(".tgz"):
            raise Refuse("dist.tarball is not a .tgz file: %s" % ascii_text(tarball)[:200])
        # (b2) the packument (CT-cc-1 addendum 3, the CTO ruling of 2026-10-16): the same host, the name quoted as the version
        # document's is. time[<version>] is the publish time check 4 reads. Refused before any tarball request.
        self.rec["packument"], self.rec["project"] = self.read_packument(a.name, a.version, integrity)
        att = dist.get("attestations")
        att_url = att.get("url") if isinstance(att, dict) and isinstance(att.get("url"), str) else None
        self.rec["attestation"] = "present" if att_url else "absent"
        self.rec["attestation_url"] = att_url
        self.rec["published"] = {
            "sha256": None, "size": None,
            "integrity": integrity if isinstance(integrity, str) else None,
            "shasum": shasum if isinstance(shasum, str) else None,
            "url": tarball, "upload_time": None, "yanked": False, "requires_python": None,
        }
        # (c) the one file, streamed to a part file; NOT checked here
        folder = os.path.join(holding_root(), "holding", a.batch)
        os.makedirs(folder, exist_ok=True)
        final = os.path.join(folder, self.file_name)
        self.part = final + ".part"
        st, _ = self.get(tarball, segment=last, sink=True, limit=NPM_TARBALL_CAP)
        if st != 200:
            raise Fail("tarball url answered HTTP %s" % st)
        self.rec["received_sha256"], self.rec["received_bytes"] = self.sha_seen, self.size_seen
        if self.size_seen > NPM_TARBALL_CAP:
            raise Refuse("tarball larger than %d bytes" % NPM_TARBALL_CAP)
        os.replace(self.part, final)
        self.part = None
        self.rec["held_path"] = "holding/%s/%s" % (a.batch, self.file_name)
        self.rec["held_sha256"], self.rec["held_bytes"] = self.sha_seen, self.size_seen
        self.rec["outcome"], self.rec["reason"] = "held", "fetched from the registry host; NOT yet checked (intake_check.py reads it)"

    def read_packument(self, name, version, integrity):
        """The npm packument (CT-cc-1 addendum 3): GET <base>/<name> on the same host. Returns (packument block, project facts)
        in the shape check 4 reads for PyPI: release_count (the packument's versions), first_release_at (the earliest time of
        any version) and this_release_at (time[<version>]). Raises Refuse, with no tarball request made, when the packument is
        unreadable, lacks versions[<version>] or time[<version>], or its versions[<version>].dist.integrity differs from the
        version document's integrity (a registry that tells two stories)."""
        url = "%s/%s" % (self.base, urllib.parse.quote(name, safe="@"))
        try:
            status, doc = self.get_json(url)
        except Fail as exc:
            raise Refuse("packument unreadable: %s" % exc)
        if status != 200 or doc is None:
            raise Refuse("packument unreadable: HTTP %s from %s" % (status, url[:200]))
        versions, times = doc.get("versions"), doc.get("time")
        if not isinstance(versions, dict) or not isinstance(versions.get(version), dict):
            raise Refuse("packument has no versions[%s] object" % version)
        if not isinstance(times, dict):
            raise Refuse("packument has no time object")
        this_at = times.get(version)
        if not (isinstance(this_at, str) and iso_time(this_at) is not None):
            raise Refuse("packument has no time[%s] publish time (a version document carries none; the packument is the source)"
                         % version)
        pdist = versions[version].get("dist")
        pint = pdist.get("integrity") if isinstance(pdist, dict) else None
        if pint != integrity:
            raise Refuse("packument versions[%s].dist.integrity %s differs from the version document's %s: the registry tells two "
                         "stories" % (version, ascii_text(pint)[:100], ascii_text(integrity)[:100]))
        known = {v: t for v in versions for t in [times.get(v)] if isinstance(t, str) and iso_time(t) is not None}
        first = min(known.values(), key=iso_time)
        created = times.get("created")
        block = {"url": url, "integrity_equal": True,
                 "created": created if isinstance(created, str) else None,
                 "published_times": {v: known.get(v) for v in sorted(versions)}}
        facts = {"release_count": len(versions), "first_release_at": first, "this_release_at": this_at}
        return block, facts

    @staticmethod
    def project_facts(proj, version):
        releases = proj.get("releases")
        if not isinstance(releases, dict):
            raise Fail("project document has no releases mapping")

        def times(files):
            return [f["upload_time_iso_8601"] for f in files
                    if isinstance(f, dict) and isinstance(f.get("upload_time_iso_8601"), str)]
        live = {v: f for v, f in releases.items() if isinstance(f, list) and f}
        every = [t for f in live.values() for t in times(f)]
        mine = times(live.get(version, []))
        return {"release_count": len(live), "first_release_at": min(every) if every else None,
                "this_release_at": min(mine) if mine else None}

    def execute(self):
        try:
            self.run()
        except Refuse as e:
            self.rec["outcome"], self.rec["reason"] = "refused", str(e)
        except Fail as e:
            self.rec["outcome"], self.rec["reason"] = "failed", str(e)
        except Exception as e:  # never leave without a record
            self.rec["outcome"], self.rec["reason"] = "failed", ("unexpected %s: %s" % (type(e).__name__, e))[:300]
        finally:
            if self.part and os.path.exists(self.part):
                try:
                    os.remove(self.part)
                except OSError:
                    pass
        return self.rec


# ---------------------------------------------------------------- resolve (round 27, CT-as-1)
# Names ONE exact wheel file per closure member from the index's release document. Downloads nothing,
# installs nothing, never picks a source archive. Its request machinery is Fetch's (Policy, get_json,
# redirect and size limits): class Resolve inherits Fetch.get / get_json / _one_request unchanged.

RESOLVE_SCHEMA = "intake-resolve/1"
CLOSURE_SCHEMA = "intake-closure/1"
HOST_SCHEMA = "intake-host-pydeps/1"
RESOLVE_TARGET = "cp312-linux_x86_64"
RESOLVE_FULL_VERSION = "3.12.14"  # the requester's CPython (intake_closure.LINUX_FULL_VERSION)
KW_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "kit_python_wheels.py"))
_MANY_RE = re.compile(r"^manylinux_(\d+)_(\d+)_[A-Za-z0-9_]+$")
_LEGACY_GLIBC = (("manylinux2014", (2, 17)), ("manylinux2010", (2, 12)), ("manylinux1", (2, 5)))


def ascii_text(value):
    return str(value).encode("ascii", "replace").decode("ascii")


def load_kw():
    """org/devices/kit_python_wheels.py (tags, markers, specifiers), loaded by path as intake_closure.py does."""
    mod = sys.modules.get("kit_python_wheels")
    if mod is None:
        import importlib.util
        spec = importlib.util.spec_from_file_location("kit_python_wheels", KW_PATH)
        mod = importlib.util.module_from_spec(spec)
        sys.modules["kit_python_wheels"] = mod
        spec.loader.exec_module(mod)
    if not mod.HAVE_PACKAGING:
        raise Refuse("the packaging library is not installed here")
    return mod


def glibc_of(platform):
    """(major, minor) of a manylinux platform tag, legacy aliases included; None for any other tag."""
    m = _MANY_RE.match(platform)
    if m:
        return (int(m.group(1)), int(m.group(2)))
    for label, level in _LEGACY_GLIBC:
        if platform == label or platform.startswith(label + "_"):
            return level
    return None


def wheel_tag_of(file_name):
    """(distribution name, compressed tag string) of a wheel file name; None for anything that is not a wheel."""
    if not file_name.endswith(".whl"):
        return None
    parts = file_name[:-4].split("-")
    if len(parts) < 5:
        return None
    return parts[0], "-".join(parts[-3:])


def expand_tags(kw, tag):
    return ["%s-%s-%s" % (t.interpreter, t.abi, t.platform) for t in kw.ptags.parse_tag(tag)]


def usable_digest(entry):
    digests = entry.get("digests") if isinstance(entry.get("digests"), dict) else {}
    sha, size = digests.get("sha256"), entry.get("size")
    if not (isinstance(sha, str) and _SHA_RE.match(sha)) or not isinstance(size, int) or isinstance(size, bool):
        return None
    return sha, size


def choose_file(kw, entries, name, supported, py_full):
    """ONE file for a member, from the release document's urls. Pure: no request. Rule order: (1) a pure
    py3-none-any wheel; (2) a cp312-cp312 or cp312-abi3 manylinux wheel; (3) any other fitting wheel. Within a
    rule the highest glibc level (<= 2.34 for this target) wins, then the lexicographically smallest file name.
    A yanked wheel, or one whose requires_python the target does not meet, is never chosen."""
    fitting, other, sdists = [], [], []
    for e in entries:
        fn = e.get("filename")
        if not isinstance(fn, str):
            continue
        wt = wheel_tag_of(fn)
        if wt is None:
            sdists.append(fn)
            continue
        dist, tag = wt
        if norm_dist(dist) != norm_dist(name):
            continue  # a file of another distribution in this release document is not this member's
        fits = kw.tag_fits(tag, supported)
        if not fits:
            other.append((fn, expand_tags(kw, tag)))
            continue
        rp = e.get("requires_python")
        py_ok = (not rp) or kw.satisfies(rp, py_full) is True
        pure = any(p == "any" and a == "none" for (_i, a, p) in fits)
        cp = any(i == "cp312" and a in ("cp312", "abi3") and glibc_of(p) is not None for (i, a, p) in fits)
        levels = [glibc_of(p) for (_i, _a, p) in fits if glibc_of(p) is not None]
        level = max(levels) if levels else (0, 0)
        group = 0 if pure else (1 if cp else 2)
        fitting.append({"fn": fn, "entry": e, "tags": expand_tags(kw, tag), "py_ok": py_ok,
                        "yanked": bool(e.get("yanked")), "group": group, "level": level,
                        "key": (group, -level[0], -level[1], fn)})
    eligible = sorted([f for f in fitting if not f["yanked"] and f["py_ok"]], key=lambda f: f["key"])
    out = {"file_name": None, "sha256": None, "size": None, "upload_time": None, "requires_python": None,
           "tags": [], "other_fitting_files": [], "reason": None, "detail": None}
    if eligible and usable_digest(eligible[0]["entry"]) is None:
        out.update({"outcome": "NO-WHEEL", "reason": "NO-DIGEST",
                    "detail": "the index publishes no usable sha256 and size for %s" % eligible[0]["fn"]})
        return out
    if eligible:
        ch = eligible[0]
        e = ch["entry"]
        sha, size = usable_digest(e)
        rule = {0: "rule 1: pure py3-none-any", 1: "rule 2: cp312 manylinux glibc %d.%d" % ch["level"],
                2: "rule 3: other fitting tag, glibc %d.%d" % ch["level"]}[ch["group"]]
        out.update({"outcome": "CHOSEN", "reason": rule, "file_name": ch["fn"], "sha256": sha, "size": size,
                    "upload_time": e.get("upload_time_iso_8601"), "requires_python": e.get("requires_python"),
                    "tags": ch["tags"], "other_fitting_files": [f["fn"] for f in eligible[1:]]})
        return out
    out["outcome"] = "NO-WHEEL"
    if fitting:
        if all(f["yanked"] for f in fitting):
            out.update({"reason": "YANKED", "detail": "every fitting wheel is yanked: %s" % ", ".join(
                sorted(f["fn"] for f in fitting))})
        else:
            out.update({"reason": "REQUIRES-PYTHON-UNMET", "detail": "fitting wheels whose requires_python the target "
                        "does not meet: %s" % ", ".join(sorted(f["fn"] for f in fitting if not f["py_ok"]))})
        out["tags"] = sorted({t for f in fitting for t in f["tags"]})
    elif other:
        out.update({"reason": "OTHER-PLATFORM-ONLY", "detail": "wheels exist and none fits %s: %s" % (
            RESOLVE_TARGET, ", ".join(sorted(fn for fn, _t in other)))})
        out["tags"] = sorted({t for _fn, ts in other for t in ts})
    elif sdists:
        out.update({"reason": "SDIST-ONLY", "detail": "only a source archive is published: %s" % ", ".join(sorted(sdists))})
    else:
        out.update({"reason": "NO-FILES", "detail": "the release document lists no files"})
    return out


def marker_applies(kw, req, env):
    """A requires_dist line is followed when its marker is true for the target with NO extra. Lines whose marker
    names an extra are not followed (as intake_closure does). -> (applies bool, note or None)."""
    if req.marker is None:
        return True, None
    if "extra" in str(req.marker):
        return False, "extra-only"
    try:
        return bool(req.marker.evaluate(dict(env))), None
    except (kw.UndefinedComparison, kw.UndefinedEnvironmentName, kw.InvalidMarker, TypeError, ValueError):
        return False, "unreadable-marker"


def approval_gate(path, lines):
    """Before ANY socket: the approval file must exist and contain the exact name==version of every line."""
    if not path or not os.path.isfile(path):
        raise Refuse("approval file does not exist: %s" % ascii_text(os.path.basename(path or "-")))
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8", "replace")
    missing = [ln for ln in lines if not re.search(r"(?<![A-Za-z0-9._-])%s(?![A-Za-z0-9._+!])" % re.escape(ln), text)]
    if missing:
        raise Refuse("approval file %s lacks %d of %d exact line(s): %s" % (
            ascii_text(os.path.basename(path)), len(missing), len(lines), ", ".join(missing)))
    return {"file": os.path.basename(path), "sha256": hashlib.sha256(raw).hexdigest(), "lines_matched": len(lines)}


class Resolve(Fetch):
    """Release documents only. Inherits Fetch.get, get_json and _one_request (the same Policy and limits); no file
    is ever requested by this class."""

    def __init__(self, base):
        self.a = None
        self.base = base.rstrip("/")
        self.policy = Policy(self.base)
        self.file_name = None
        self.index_file_name = None
        self.part = None
        self.sha_seen = None
        self.size_seen = None
        self.rec = {"requests": []}

    def release_doc(self, name, version):
        q = urllib.parse.quote
        return self.get_json("%s/pypi/%s/%s/json" % (self.base, q(name), q(version)))


def read_host(path, kw):
    with open(path, "rb") as fh:
        raw = fh.read()
    hd = json.loads(raw.decode("utf-8"))
    if hd.get("schema") != HOST_SCHEMA:
        raise Refuse("--host-pydeps must carry schema %s" % HOST_SCHEMA)
    dists = {kw.canonicalize_name(k): v for k, v in (hd.get("dists") or {}).items()}
    return {"file": os.path.basename(path), "sha256": hashlib.sha256(raw).hexdigest(), "dists": dists}


def recheck(kw, rows, docs, members, host, env):
    """The index-side re-check (the CTO's ask, msg 109620). Reads ONLY the CHOSEN releases' requires_dist. Every
    line it prints is a STOP or an OK for the CTO to read; nothing here chooses or edits a member."""
    canon = kw.canonicalize_name
    closure_norms = {canon(m["name"]) for m in members}
    nowheel = {r["norm"] for r in rows if r["outcome"] != "CHOSEN"}
    chosen = {r["norm"]: r for r in rows if r["outcome"] == "CHOSEN"}
    lines = {"NEW-MEMBER": [], "SPECIFIER-MISMATCH": [], "HOST-CONFLICT": [], "HOST-OK": [], "NO-METADATA": []}
    host_specs = {}
    unreadable = []
    for norm in sorted(chosen):
        row = chosen[norm]
        rd = (docs[norm].get("info") or {}).get("requires_dist")
        if not isinstance(rd, list):
            lines["NO-METADATA"].append("NO-METADATA %s==%s requires_dist absent from the release document"
                                        % (row["name"], row["version"]))
            continue
        for text in rd:
            try:
                req = kw.Requirement(text)
            except (kw.InvalidRequirement, ValueError):
                unreadable.append("%s: %s" % (row["name"], ascii_text(text)))
                continue
            applies, _note = marker_applies(kw, req, env)
            if not applies:
                continue
            rn, spec = canon(req.name), str(req.specifier)
            if rn not in closure_norms:
                lines["NEW-MEMBER"].append("NEW-MEMBER %s required by %s %s" % (req.name, row["name"], spec or "any"))
            elif rn in nowheel:
                continue
            elif rn in chosen:
                cv = chosen[rn]["version"]
                ok = kw.satisfies(spec, cv)
                if ok is False:
                    lines["SPECIFIER-MISMATCH"].append("SPECIFIER-MISMATCH %s %s unmet by %s %s"
                                                       % (req.name, cv, row["name"], spec or "any"))
                elif ok is None:
                    unreadable.append("%s: specifier %r" % (row["name"], spec))
            else:
                host_specs.setdefault(rn, []).append((row["name"], spec))
    host_conflicts = None
    if host is not None:
        host_conflicts = 0
        for m in sorted(members, key=lambda x: x["name"]):
            if m.get("host_class") != "HOST-SATISFIED":
                continue
            rn = canon(m["name"])
            hv = host["dists"].get(rn)
            specs = host_specs.get(rn, [])
            if hv is None:
                lines["HOST-CONFLICT"].append("HOST-CONFLICT %s host absent, but the closure marks it HOST-SATISFIED "
                                              "STOP" % m["name"])
                continue
            unmet = [(p, s) for (p, s) in specs if kw.satisfies(s, hv) is not True]
            for p, s in unmet:
                lines["HOST-CONFLICT"].append("HOST-CONFLICT %s host %s unmet by %s %s STOP" % (m["name"], hv, p, s or "any"))
            if not unmet:
                met = "; ".join("%s %s" % (p, s or "any") for p, s in specs) or "none-from-chosen-parents"
                lines["HOST-OK"].append("HOST-OK %s host %s meets %s" % (m["name"], hv, met))
        host_conflicts = len(lines["HOST-CONFLICT"])
    return {"lines": lines, "unreadable": unreadable, "host_conflicts": host_conflicts}


def run_resolve(a, state):
    """The verb's sequence. state["res"] carries the Resolve object so a request count survives a failure."""
    if a.target != RESOLVE_TARGET:
        raise Refuse("resolve measures %s only; got %s" % (RESOLVE_TARGET, a.target))
    try:
        with open(a.closure, "rb") as fh:
            data = json.loads(fh.read().decode("utf-8"))
    except (OSError, ValueError) as e:
        raise Refuse("closure file unreadable: %s" % ascii_text(e))
    if data.get("schema") != CLOSURE_SCHEMA:
        raise Refuse("closure file must carry schema %s" % CLOSURE_SCHEMA)
    label = (data.get("target") or {}).get("label")
    if label != a.target:
        raise Refuse("closure targets %s, not %s" % (label, a.target))
    members = data.get("members") or []
    todo = sorted([m for m in members if m.get("host_class") != "HOST-SATISFIED"], key=lambda m: m["name"])
    base = (a.index_base or PUBLIC_BASE).rstrip("/")
    policy = Policy(base)
    if not policy.loopback:
        parsed = urllib.parse.urlparse(base)
        if parsed.scheme != "https" or parsed.hostname != "pypi.org" or _port(parsed) != 443:
            raise Refuse("index base %s is not the public index" % base)
    approval = approval_gate(a.approved_by, ["%s==%s" % (m["name"], m["version"]) for m in todo])
    kw = load_kw()
    target = kw.parse_target("cp312", "linux_x86_64")
    target["env"]["python_full_version"] = RESOLVE_FULL_VERSION
    target["env"]["implementation_version"] = RESOLVE_FULL_VERSION
    supported = kw.supported_tags(target)
    host = read_host(a.host_pydeps, kw) if a.host_pydeps else None
    res = Resolve(base)
    state["res"] = res
    state["members"] = len(todo)
    rows, docs = [], {}
    for m in todo:
        norm = kw.canonicalize_name(m["name"])
        status, doc = res.release_doc(m["name"], m["version"])
        row = {"name": m["name"], "norm": norm, "version": m["version"], "closure_class": m.get("class"),
               "closure_host_class": m.get("host_class"), "release_status": status}
        if status == 404:
            row.update({"outcome": "NO-WHEEL", "reason": "NO-RELEASE", "file_name": None, "sha256": None, "size": None,
                        "upload_time": None, "requires_python": None, "tags": [], "other_fitting_files": [],
                        "detail": "no such release on the index (HTTP 404)"})
        else:
            if status != 200 or not isinstance(doc.get("urls"), list):
                raise Fail("release document answered HTTP %s for %s" % (status, m["name"]))
            docs[norm] = doc
            row.update(choose_file(kw, doc["urls"], m["name"], supported, RESOLVE_FULL_VERSION))
        rows.append(row)
    rows.sort(key=lambda r: (r["name"].lower(), r["name"], r["version"]))
    rc = recheck(kw, rows, docs, members, host, target["env"])
    return {"approval": approval, "rows": rows, "recheck": rc, "host": None if host is None else
            {"file": host["file"], "sha256": host["sha256"]}, "base": base, "members": todo,
            "closure_members": len(members), "closure_file": os.path.basename(a.closure), "target": a.target}


def resolve_doc(run, requests, last):
    return {"schema": RESOLVE_SCHEMA, "target": run["target"], "closure_file": run["closure_file"],
            "closure_members": run["closure_members"], "index_base": run["base"],
            "approved_by": run["approval"], "host_pydeps": run["host"],
            "claim": "measured: one release document per member, read from the index named above; no file was "
                     "downloaded, nothing installed; the re-check reads the CHOSEN releases only",
            "members": len(run["members"]),
            "rows": run["rows"], "recheck": run["recheck"]["lines"], "unreadable_requires_dist": run["recheck"]["unreadable"],
            "requests": [{"url": r["url"], "status": r.get("status"), "bytes": r.get("bytes", 0)} for r in requests],
            "last_line": last}


def resolve_md(doc):
    out = []
    w = out.append
    w("# Intake resolve: one exact wheel file per closure member")
    w("")
    w("Written by `org/devices/intake/intake_fetch.py resolve` (schema %s). Target %s; closure `%s`; index base `%s`."
      % (doc["schema"], doc["target"], doc["closure_file"], doc["index_base"]))
    w("")
    w("Nothing was downloaded and nothing was installed. Each row is the index's own published file name, digest and size.")
    w("")
    w("`%s`" % doc["last_line"])
    w("")
    w("| # | Member | Version | Outcome | File name | sha256 | Size | Reason |")
    w("|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(doc["rows"], 1):
        w("| %d | %s | %s | %s | %s | %s | %s | %s |" % (
            i, r["name"], r["version"], r["outcome"], r["file_name"] or "-", r["sha256"] or "-",
            r["size"] if r["size"] is not None else "-", r["reason"] or "-"))
    w("")
    w("## Re-check lines (STOP and OK lines for the CTO; nothing here is fixed by the tool)")
    w("")
    for key in ("NEW-MEMBER", "SPECIFIER-MISMATCH", "HOST-CONFLICT", "HOST-OK", "NO-METADATA"):
        for ln in doc["recheck"][key]:
            w("- %s" % ln)
    w("")
    return "\n".join(out) + "\n"


def cmd_resolve(a):
    state = {}
    try:
        run = run_resolve(a, state)
    except Refuse as e:
        print("REFUSED: %s" % ascii_text(e))
        print("INTAKE-RESOLVE target=%s members=0 chosen=0 no_wheel=0 requests=0 ok=False" % a.target)
        return 2
    except Fail as e:
        res = state.get("res")
        n = len(res.rec["requests"]) if res else 0
        print("FAILED: %s" % ascii_text(e))
        print("INTAKE-RESOLVE target=%s members=%d chosen=0 no_wheel=0 requests=%d ok=False" % (
            a.target, state.get("members", 0), n))
        return 1
    rows, rc = run["rows"], run["recheck"]
    for r in rows:
        if r["outcome"] == "CHOSEN":
            print("CHOSEN %s==%s %s [%s]" % (r["name"], r["version"], r["file_name"], r["reason"]))
        else:
            print("NO-WHEEL %s==%s %s %s" % (r["name"], r["version"], r["reason"], ascii_text(r["detail"] or "")))
    for key in ("NEW-MEMBER", "SPECIFIER-MISMATCH", "HOST-CONFLICT", "HOST-OK", "NO-METADATA"):
        for ln in rc["lines"][key]:
            print(ascii_text(ln))
    for ln in rc["unreadable"]:
        print("UNREADABLE requires_dist %s" % ascii_text(ln))
    chosen = sum(1 for r in rows if r["outcome"] == "CHOSEN")
    no_wheel = len(rows) - chosen
    new_n = len(rc["lines"]["NEW-MEMBER"])
    mism_n = len(rc["lines"]["SPECIFIER-MISMATCH"])
    host_n = rc["host_conflicts"]
    requests = state["res"].rec["requests"]
    ok = no_wheel == 0 and new_n == 0 and mism_n == 0 and (host_n is None or host_n == 0)
    last = ("INTAKE-RESOLVE target=%s members=%d chosen=%d no_wheel=%d requests=%d ok=%s new_members=%d "
            "specifier_mismatches=%d host_conflicts=%s" % (
                a.target, len(run["members"]), chosen, no_wheel, len(requests), ok, new_n, mism_n,
                "UNREAD" if host_n is None else host_n))
    if a.out:
        doc = resolve_doc(run, requests, last)
        doc["ok"] = ok
        text = json.dumps(doc, indent=1, sort_keys=True, ensure_ascii=True) + "\n"
        with open(a.out, "w", encoding="ascii", newline="\n") as fh:
            fh.write(text)
        print("Wrote %s (%d bytes)" % (os.path.basename(a.out), len(text)))
        if a.out.endswith(".json"):
            md_path = a.out[:-len(".json")] + ".md"
            with open(md_path, "w", encoding="ascii", newline="\n") as fh:
                fh.write(resolve_md(doc))
            print("Wrote %s" % os.path.basename(md_path))
    print(last)  # the verdict line is the LAST line of stdout
    return 0 if ok else 1


# ---------------------------------------------------------------- records

def _load(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def write_record(rec):
    """Write <file name>.fetch.json. A held record still backed by its held file is never
    overwritten: a new held fetch moves it aside as .prior; a new refusal or failure goes
    beside it as .attempt. Neither aside name ends in .fetch.json, so readers of the
    authoritative record ignore them."""
    folder = os.path.join(records_root(), rec["batch"])
    os.makedirs(folder, exist_ok=True)
    base = (rec["requested"]["file_name"] or "invalid_request.whl") + ".fetch"
    path = os.path.join(folder, base + ".json")
    stamp = rec["at"].replace(":", "").replace("-", "")
    prior = _load(path) if os.path.exists(path) else None
    if prior and prior.get("outcome") == "held":
        backed = prior.get("held_path") and os.path.isfile(os.path.join(holding_root(), prior["held_path"]))
        if backed and rec["outcome"] != "held":
            path = os.path.join(folder, "%s.%s.attempt.json" % (base, stamp))
        else:
            os.replace(path, os.path.join(folder, "%s.%s.prior.json" % (base, stamp)))
    with open(path, "w", encoding="ascii", newline="\n") as fh:
        json.dump(rec, fh, indent=2, ensure_ascii=True)
        fh.write("\n")
    return path


def summary_line(rec):
    att = rec["attestation"]
    sha = rec["held_sha256"][:12] if rec["held_sha256"] else "-"
    return "INTAKE-FETCH batch=%s file=%s requests=%d outcome=%s sha256=%s bytes=%d attestation=%s" % (
        rec["batch"], rec["requested"]["file_name"] or "-", len(rec["requests"]),
        rec["outcome"], sha, rec["held_bytes"] or 0, att)


def cmd_fetch(a):
    if not _BATCH_RE.match(a.batch):
        print("ERROR: invalid --batch %r (letters, digits, . _ -)" % a.batch)
        return 2
    if getattr(a, "ecosystem", "pypi") != "npm" and getattr(a, "registry_base", None):
        print("ERROR: --registry-base is for --ecosystem npm")
        return 2
    f = Fetch(a)
    rec = f.execute()
    path = write_record(rec)
    print("record: %s" % path)
    if rec["outcome"] != "held":
        print("%s: %s" % (rec["outcome"].upper(), rec["reason"]))
    print(summary_line(rec))
    return 1 if rec["outcome"] == "failed" else 0


def cmd_list(a):
    if not _BATCH_RE.match(a.batch):
        print("ERROR: invalid --batch %r" % a.batch)
        return 2
    folder = os.path.join(records_root(), a.batch)
    held_dir = os.path.join(holding_root(), "holding", a.batch)
    counts = {"held": 0, "refused": 0, "failed": 0}
    n = 0
    seen = set()
    for fn in sorted(os.listdir(folder)) if os.path.isdir(folder) else []:
        if not fn.endswith(".fetch.json"):
            continue
        rec = _load(os.path.join(folder, fn))
        if not isinstance(rec, dict):
            print("%s outcome=unreadable-record" % fn)
            continue
        n += 1
        out = rec.get("outcome")
        if out in counts:
            counts[out] += 1
        name = (rec.get("requested") or {}).get("file_name") or fn
        seen.add(name)
        present = "in-holding" if os.path.isfile(os.path.join(held_dir, name)) else "not-in-holding"
        print("%s outcome=%s at=%s by=%s %s reason=%s" % (name, out, rec.get("at"), rec.get("fetched_by"),
                                                          present, (rec.get("reason") or "")[:120]))
    for fn in sorted(os.listdir(held_dir)) if os.path.isdir(held_dir) else []:
        if fn not in seen:
            print("%s outcome=NO-RECORD in-holding" % fn)
    print("INTAKE-HELD batch=%s records=%d held=%d refused=%d failed=%d" % (
        a.batch, n, counts["held"], counts["refused"], counts["failed"]))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fetch", help="fetch ONE exact wheel file into the holding folder")
    f.add_argument("--batch", required=True)
    f.add_argument("--name", required=True)
    f.add_argument("--version", required=True)
    f.add_argument("--python-tag", default=None, help="pypi only (required for pypi)")
    f.add_argument("--abi-tag", default=None, help="pypi only (required for pypi)")
    f.add_argument("--platform-tag", default=None, help="pypi only (required for pypi)")
    f.add_argument("--index-base", default=None)
    f.add_argument("--ecosystem", choices=("pypi", "npm"), default="pypi",
                   help="pypi (default): a wheel from the index; npm: one .tgz from the npm registry (CT-cc-1)")
    f.add_argument("--registry-base", default=None, help="npm only: a LOOPBACK test registry base")
    f.add_argument("--approved-by", default=None, help="signed batch approval file (required for the public index)")
    f.set_defaults(fn=cmd_fetch)
    ls = sub.add_parser("list", help="what the holding folder and the records hold for a batch")
    ls.add_argument("--batch", required=True)
    ls.set_defaults(fn=cmd_list)
    rs = sub.add_parser("resolve", help="name ONE exact wheel file per closure member (no download)")
    rs.add_argument("--closure", required=True, help="an intake-closure/1 JSON (the closure tool's saved file)")
    rs.add_argument("--target", required=True, help="cp312-linux_x86_64")
    rs.add_argument("--approved-by", required=True, help="approval file naming the exact name==version of every member")
    rs.add_argument("--index-base", default=None)
    rs.add_argument("--host-pydeps", default=None, help="intake-host-pydeps/1 file: the re-check reads it")
    rs.add_argument("--out", default=None, help="JSON output (a .md table is written beside it)")
    rs.set_defaults(fn=cmd_resolve)
    a = ap.parse_args(argv)
    if a.cmd == "fetch" and a.ecosystem == "pypi":
        missing = [flag for flag, v in (("--python-tag", a.python_tag), ("--abi-tag", a.abi_tag),
                                        ("--platform-tag", a.platform_tag)) if v is None]
        if missing:
            f.error("the following arguments are required: %s" % ", ".join(missing))
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())

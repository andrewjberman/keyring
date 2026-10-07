#!/usr/bin/env python3
"""intake_fetch.py -- fetch ONE exact wheel file into the holding folder, with a record.

Route hop 4 ("fetched and held"). One wheel file for one approved line: no dependency
resolution, nothing installed, nothing unpacked, nothing imported. The file waits unchecked
in <holding root>/holding/<batch>/ until the check tool moves it. Every fetch writes a
FETCH record (schema intake-fetch/1) under org/devices/intake/records/<batch>/, also when the
fetch is refused before any request or fails midway.

  fetch --batch B --name N --version V --python-tag T --abi-tag T --platform-tag T
        [--index-base URL] [--approved-by PATH]
  list  --batch B

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


class Refuse(Exception):
    """The tool declines to proceed (outcome refused)."""


class Fail(Exception):
    """The tool tried and could not (outcome failed)."""


def utcnow():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


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

    def __init__(self, base):
        parsed = urllib.parse.urlparse(base)
        self.loopback = parsed.hostname in LOOPBACK_HOSTS
        self.host_port = (parsed.hostname, _port(parsed))

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
            if host not in PUBLIC_HOSTS or port != 443:
                raise Refuse("host %s:%s is outside the closed set %s: %s" % (
                    host, port, ",".join(PUBLIC_HOSTS), url[:200]))
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
            "at": utcnow(),
        }

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
    f.add_argument("--python-tag", required=True)
    f.add_argument("--abi-tag", required=True)
    f.add_argument("--platform-tag", required=True)
    f.add_argument("--index-base", default=None)
    f.add_argument("--approved-by", default=None, help="signed batch approval file (required for the public index)")
    f.set_defaults(fn=cmd_fetch)
    ls = sub.add_parser("list", help="what the holding folder and the records hold for a batch")
    ls.add_argument("--batch", required=True)
    ls.set_defaults(fn=cmd_list)
    a = ap.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())

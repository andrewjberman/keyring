"""SOC2_MSLOGS round 2 checks (issuer 2.0.0_SA_COO~S1). Run from the repository (worktree) root. Synthetic values only; nothing live.

  python s1_check_r2.py silverip         -> R2-SILVERIP-OK    (silver client_ip: ClientIP, else ClientIPAddress, else ActorIpAddress)
  python s1_check_r2.py derive           -> R2-DERIVE-OK      (the door's derive_silver: same silver as build(); memory at most half of build()'s and bounded as data grows 4x)
  python s1_check_r2.py naming           -> R2-NAMING-OK      (the door's audit_records prefixes come from the naming builder; the gate reads none)
  python s1_check_r2.py paging           -> R2-PAGING-OK      (read_timeline: detail pages through a 1000-row door, de-duplicated, who-acted shown)
  python s1_check_r2.py desktop          -> R2-DESKTOP-OK     (door_client: Desktop file equals the answer; MFA session; no secret printed)
  python s1_check_r2.py retire           -> R2-RETIRE-OK      (door_client derive_dates; the two round-1 stopgaps are gone)
  python s1_check_r2.py exposure_door    -> R2-EXPOSURE-OK    (exposure.compute over detail rows)
  python s1_check_r2.py exposure_client  -> R2-EXPCLIENT-OK   (read_exposure fetch and render)
  python s1_check_r2.py retry            -> R2-RETRY-OK       (collector async retry attempts are 0 in collector.tf)
  python s1_check_r2.py tfvalidate       -> R2-TFVALIDATE-OK  (terraform validate on a scratch copy of the trino root)
  python s1_check_r2.py text             -> R2-TEXT-OK        (README, RUNBOOK, main.tf carry no eight-account or filter text; four feeds named)
"""
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.getcwd()
DOOR = os.path.join(ROOT, "infra", "aws", "lambda", "globgrph-trino-access")
SILVER_DIR = os.path.join(ROOT, "data", "m365_metadata", "scripts", "silver")
TRINO = os.path.join(ROOT, "infra", "aws", "terraform", "trino")
STOPGAPS = [os.path.join(ROOT, "org", "tier1_exec", "2.0.0_SA_COO~S1", "deliverables", f)
            for f in ("derive_days.py", "read_timeline_to_desktop.ps1")]


def load(path, name):
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.dirname(path))
    spec.loader.exec_module(m)
    return m


def finish(tag, bad, ok_text=""):
    if bad:
        print("%s-REFUSED %s" % (tag, "; ".join(bad)))
        return 1
    print(("%s-OK %s" % (tag, ok_text)).rstrip())
    return 0


# ---------------------------------------------------------------------------------------------------- silver client_ip
def silverip():
    m = load(os.path.join(DOOR, "silver_builder.py"), "r2_builder")
    import pyarrow.parquet as pq

    base = {"Workload": "Exchange", "Operation": "Send", "UserId": "pat@op.example"}
    recs = [
        dict(base, Id="x1", CreationTime="2026-10-15T14:00:00", Operation="MailItemsAccessed", ClientIPAddress="203.0.113.50"),
        dict(base, Id="x2", CreationTime="2026-10-15T14:01:00", ClientIP="198.51.100.1", ClientIPAddress="203.0.113.50"),
        dict(base, Id="x3", CreationTime="2026-10-15T14:02:00", ClientIPAddress="[2001:db8::1]:443"),
        dict(base, Id="x4", CreationTime="2026-10-15T14:03:00", ClientIPAddress=""),
        dict(base, Id="x5", CreationTime="2026-10-15T14:04:00", ClientIPAddress="203.0.113.51", ActorIpAddress="198.51.100.9"),
        dict(base, Id="a1", CreationTime="2026-10-15T14:05:00", Workload="AzureActiveDirectory", ActorIpAddress="198.51.100.4"),
        dict(base, Id="s1", CreationTime="2026-10-15T14:06:00", Workload="SharePoint", ClientIP="192.0.2.9"),
        dict(base, Id="n1", CreationTime="2026-10-15T14:07:00"),
    ]
    want = {"x1": "203.0.113.50", "x2": "198.51.100.1", "x3": "[2001:db8::1]:443", "x4": None, "x5": "203.0.113.51",
            "a1": "198.51.100.4", "s1": "192.0.2.9", "n1": None}
    t = pq.read_table(io.BytesIO(m.build(recs)))
    got = {r["record_id"]: r["client_ip"] for r in t.to_pylist()}
    bad = []
    if got != want:
        bad.append("client_ip by record %r, wanted %r" % (got, want))
    raw = {r["record_id"]: json.loads(r["raw_json"]) for r in t.to_pylist()}
    if raw["x1"] != recs[0]:
        bad.append("raw_json must stay the whole original record")
    return finish("R2-SILVERIP", bad, "rows=%d" % t.num_rows)


# ---------------------------------------------------------------------------------------------------- streaming derive
def _synth(date_a, date_b, n_objects=8, per_object=1500):
    """Deterministic synthetic bronze: two Eastern-day partitions, overlapping times, a few ties, padded records."""
    import datetime as dt
    import gzip
    import random

    rnd = random.Random(20261017)
    store = {}
    pad = "x" * 2500
    for pi, part in enumerate((date_a, date_b)):
        day0 = dt.datetime.strptime(part, "%Y%m%d").replace(tzinfo=dt.timezone.utc) + dt.timedelta(hours=4)  # Eastern midnight (EDT)
        for o in range(n_objects):
            recs = []
            for i in range(per_object):
                secs = rnd.randrange(0, 86400)
                if rnd.random() < 0.05:
                    secs += rnd.choice((-3600, 86400 - 600 + 3600))  # a record that belongs to the neighbouring Eastern day
                if i % 75 == 0:
                    secs = 43200  # ties at noon
                when = day0 + dt.timedelta(seconds=secs)
                recs.append({"Id": "r-%d-%d-%d" % (pi, o, i), "CreationTime": when.strftime("%Y-%m-%dT%H:%M:%S"),
                             "Workload": "Exchange", "Operation": "MailItemsAccessed", "UserId": "u%d@op.example" % (i % 40),
                             "ClientIPAddress": "203.0.113.%d" % (i % 200), "Pad": pad + str(i)})
            key = "m365-metadata/trino/bronze/audit_records/date=%s/%023d$%023d$audit_exchange$Audit_Exchange$o%d.json.gz" % (part, o, pi, o)
            store[key] = gzip.compress(json.dumps(recs).encode("utf-8"), mtime=0)
    return store


class _FakeS3:
    def __init__(self, store):
        self.store = dict(store)
        self.puts = {}

    def list_objects_v2(self, Bucket, Prefix, ContinuationToken=None):
        keys = sorted(k for k in self.store if k.startswith(Prefix))
        return {"Contents": [{"Key": k} for k in keys], "IsTruncated": False}

    def get_object(self, Bucket, Key):
        return {"Body": io.BytesIO(self.store[Key])}

    def put_object(self, Bucket, Key, Body, ServerSideEncryption=None):
        self.puts[Key] = bytes(Body)


class _Ctx:
    invoked_function_arn = "arn:aws:lambda:us-east-1:111122223333:function:globgrph-trino-access-lambda:member"


def _digest(parquet_bytes):
    import pyarrow.parquet as pq

    t = pq.read_table(io.BytesIO(parquet_bytes))
    h = hashlib.sha256()
    for r in t.to_pylist():
        h.update(("%s|%s|%s|%s|%s\n" % (r["record_id"], r["creation_time"], r["date"], r["client_ip"], r["raw_json"])).encode("utf-8"))
    return t.num_rows, t.column_names, h.hexdigest()


def derive_run(which, n_objects):
    """Subprocess body: one derive of 2026-10-15, one peak-memory figure. Prints a JSON line."""
    import gzip
    import tracemalloc

    import pyarrow as pa

    door = load(os.path.join(DOOR, "handler.py"), "r2_handler")
    sb = load(os.path.join(DOOR, "silver_builder.py"), "r2_sb")
    store = _synth("20261015", "20261016", n_objects=int(n_objects))
    s3 = _FakeS3(store)
    import tempfile as _tf
    tmp_before = set(os.listdir(_tf.gettempdir()))
    os.environ["BUCKET"] = "opal-data-trino"
    tracemalloc.start()
    if which == "naive":
        records = []
        for part in ("20261015", "20261016"):
            for k in sorted(k for k in store if "date=%s/" % part in k):
                records.extend(json.loads(gzip.decompress(store[k]).decode("utf-8")))
        data = sb.build(records, only_date="2026-10-15")
        n = len(records)
    else:
        answer = door.handle({"op": "derive_silver", "date": "2026-10-15"}, _Ctx(), s3=s3, silver_builder=sb)
        if answer.get("ok") is not True:
            print(json.dumps({"error": "door answered %r" % (answer,)}))
            return 1
        n = answer.get("rows")
        keys = list(s3.puts)
        data = s3.puts[keys[0]] if len(keys) == 1 else b""
    peak = tracemalloc.get_traced_memory()[1] + pa.default_memory_pool().max_memory()
    rows, cols, dig = _digest(data) if data else (0, [], "")
    leaked = sorted(set(os.listdir(_tf.gettempdir())) - tmp_before)
    print(json.dumps({"peak": peak, "n": n, "rows": rows, "cols": cols, "digest": dig, "puts": len(s3.puts), "leaked": leaked[:3]}))
    return 0


def _run_sub(which, n_objects):
    iso = tempfile.mkdtemp(prefix="r2iso_")  # a private temp directory, so the leftover-file arm sees this run only
    env = dict(os.environ, TMP=iso, TEMP=iso, TMPDIR=iso)
    try:
        p = subprocess.run([sys.executable, os.path.abspath(__file__), "derive_run", which, str(n_objects)], capture_output=True, text=True,
                           cwd=ROOT, timeout=100, env=env)
    finally:
        shutil.rmtree(iso, ignore_errors=True)
    line = (p.stdout.strip().splitlines() or [""])[-1]
    if p.returncode != 0 or not line.startswith("{"):
        raise RuntimeError("%s run failed rc=%s: %s %s" % (which, p.returncode, line[:200], p.stderr.strip()[-200:]))
    return json.loads(line)


def derive():
    naive = _run_sub("naive", 16)
    big = _run_sub("door", 16)
    small = _run_sub("door", 4)
    bad = []
    for tag, run in (("16 objects", big), ("4 objects", small)):
        if "error" in run:
            bad.append("%s: %s" % (tag, run["error"]))
    if not bad:
        if (big["rows"], big["cols"], big["digest"]) != (naive["rows"], naive["cols"], naive["digest"]):
            bad.append("the door's silver differs from build() over the same records (rows %s vs %s)" % (big["rows"], naive["rows"]))
        if big["n"] != naive["n"]:
            bad.append("the answer's rows is %s, wanted the records read, %s" % (big["n"], naive["n"]))
        if big["puts"] != 1 or small["puts"] != 1:
            bad.append("the door must write exactly one silver object per derive")
        if big["leaked"] or small["leaked"]:
            bad.append("derive left temporary files behind: %r" % (big["leaked"] or small["leaked"],))
        vs_build = big["peak"] / float(naive["peak"])
        growth = big["peak"] / float(small["peak"])
        if vs_build > 0.5:
            bad.append("peak memory is %.2f of build()'s, wanted at most 0.50 (door %d, build %d bytes)" % (vs_build, big["peak"], naive["peak"]))
        if growth > 2.0:
            bad.append("peak memory grew %.2fx for 4x the data, wanted at most 2.0x: the derive is not bounded" % growth)
    return finish("R2-DERIVE", bad, ("vs_build=%.2f growth=%.2f rows=%s" % (vs_build, growth, big.get("rows"))) if not bad else "")


# ---------------------------------------------------------------------------------------------------- naming
def _gate_lines(paths):
    out = []
    for p in paths:
        d = subprocess.run(["git", "diff", "--no-index", "--", os.devnull if os.name != "nt" else "NUL", p],
                           capture_output=True, text=True, cwd=ROOT).stdout
        tmp = tempfile.NamedTemporaryFile("w", suffix=".diff", delete=False, encoding="utf-8")
        tmp.write(d)
        tmp.close()
        g = subprocess.run([sys.executable, os.path.join(ROOT, ".tools", "naming-gate.py"), "--diff", tmp.name],
                           capture_output=True, text=True, cwd=ROOT, timeout=100)
        os.unlink(tmp.name)
        out.extend(g.stdout.splitlines())
    return out


def naming():
    sys.path.insert(0, ROOT)
    from lib.opal_naming import address

    bad = []
    py = sorted(os.path.join(DOOR, f) for f in os.listdir(DOOR) if f.endswith(".py"))
    h = load(os.path.join(DOOR, "handler.py"), "r2_names_handler")
    want = address("m365-metadata", "trino", "bronze", "audit_records", "date=20261016", object="x")[len("s3://opal-data-trino/"):-1]
    if h.BRONZE_DAY % "20261016" != want:
        bad.append("handler.BRONZE_DAY gives %r, the builder gives %r" % (h.BRONZE_DAY % "20261016", want))
    cid = "0" * 23 + "$" + "1" * 23 + "$audit_exchange$Audit_Exchange$abc"
    if not h.key_ok("bronze", want + cid + ".json.gz"):
        bad.append("key_ok no longer admits a builder-shaped bronze key")
    lines = _gate_lines(py)
    errors = [ln for ln in lines if ln.startswith("NAMING ERROR")]
    graded = [ln for ln in lines if ln.startswith("NAMING-GATE:")]
    if errors or len(graded) != len(py):
        bad.append("the naming gate could not grade (errors %d, summaries %d of %d files): %s" % (len(errors), len(graded), len(py), (errors or ["no summary line"])[0][:160]))
    hits = [ln for ln in lines if "audit_records" in ln and ln.startswith("NAMING REFUSE")]
    if hits:
        bad.append("the naming gate still refuses %d audit_records line(s), first: %s" % (len(hits), hits[0][:160]))
    return finish("R2-NAMING", bad, "files=%d" % len(py))


# ---------------------------------------------------------------------------------------------------- the read client
def _door_rows(n):
    import datetime as dt

    t0 = dt.datetime(2026, 10, 15, 13, 0, 0, tzinfo=dt.timezone.utc)
    rows = []
    for i in range(n):
        when = t0 + dt.timedelta(seconds=i // 2)  # two records share each second
        rows.append({"time": when.strftime("%Y-%m-%dT%H:%M:%SZ"), "feed": "Exchange", "operation": "MailItemsAccessed", "result_status": "Succeeded",
                     "client_ip": "203.0.113.%d" % (i % 200), "item_name": "item %d" % i, "user_id": "pat@opalinvest.com",
                     "record_id": "rec-%05d" % i, "raw": {"Id": "rec-%05d" % i}})
    return rows


def _fake_door(rows, page=1000):
    seen = []

    def invoker(p):
        seen.append(dict(p))
        lo, hi = p["start"], p["end"]
        sel = [r for r in rows if lo <= r["time"] < hi]
        return {"ok": True, "rows": sel[:page], "truncated": len(sel) > page}

    return invoker, seen


def paging():
    m = load(os.path.join(SILVER_DIR, "read_timeline.py"), "r2_read_timeline")
    bad = []
    rows = _door_rows(2500)
    inv, seen = _fake_door(rows)
    reply = m.fetch(inv, " Pat@OpalInvest.com ", "2026-10-15T00:00:00Z", "2026-10-16T00:00:00Z", detail=True)
    ids = [r["record_id"] for r in reply["rows"]]
    if ids != [r["record_id"] for r in rows]:
        bad.append("paged rows are not the 2500 door rows once each in order (got %d)" % len(ids))
    if reply.get("truncated") is not False:
        bad.append("a complete paged answer must say truncated false")
    if not (1 < len(seen) <= 4):
        bad.append("calls made %d, wanted 2 to 4" % len(seen))
    if any(p.get("detail") is not True or p.get("op") != "timeline" or p.get("account") != "pat@opalinvest.com" for p in seen):
        bad.append("every page call must be op timeline, detail true, the lower-cased account")
    if len(seen) > 1 and seen[1]["start"] != rows[999]["time"]:
        bad.append("the second page must start at the last row's time (%s), started at %s" % (rows[999]["time"], seen[1]["start"]))
    # a page that cannot advance must raise, not loop
    stuck_rows = [dict(r, time="2026-10-15T13:00:00Z") for r in _door_rows(1200)]
    inv2, seen2 = _fake_door(stuck_rows)
    try:
        m.fetch(inv2, "pat@opalinvest.com", "2026-10-15T00:00:00Z", "2026-10-16T00:00:00Z", detail=True)
        bad.append("a page of rows all sharing one second must raise RuntimeError")
    except RuntimeError:
        pass
    if len(seen2) > 3:
        bad.append("the stuck window made %d calls, wanted at most 3" % len(seen2))
    # without detail: exactly the round-1 call
    inv3, seen3 = _fake_door(rows[:10])
    m.fetch(inv3, "pat@opalinvest.com", "2026-10-15T00:00:00Z", "2026-10-16T00:00:00Z")
    if seen3 != [{"op": "timeline", "account": "pat@opalinvest.com", "start": "2026-10-15T00:00:00Z", "end": "2026-10-16T00:00:00Z"}]:
        bad.append("without detail the call must be exactly the round-1 payload: %r" % (seen3,))
    text = m.render({"ok": True, "rows": rows[:3], "truncated": False})
    if "pat@opalinvest.com" not in text or "MailItemsAccessed" not in text:
        bad.append("each line must say who acted (user_id) and the operation")
    if "--detail" not in open(os.path.join(SILVER_DIR, "read_timeline.py"), encoding="utf-8").read():
        bad.append("read_timeline.py must offer a --detail flag")
    return finish("R2-PAGING", bad, "calls=%d" % len(seen))


class _FakeBoto:
    """Records every client the session builds; sts hands back a token, iam lists the devices given."""

    def __init__(self, devices):
        self.devices = devices
        self.calls = []
        outer = self

        class Session:
            def __init__(self, **kw):
                outer.calls.append(("Session", kw))

            def client(self, service, **kw):
                outer.calls.append((service, kw))
                return outer._client(service)

        self.Session = Session

    def _client(self, service):
        outer = self

        class C:
            def list_mfa_devices(self, **kw):
                return {"MFADevices": [{"SerialNumber": d} for d in outer.devices]}

            def get_session_token(self, **kw):
                outer.calls.append(("get_session_token", kw))
                return {"Credentials": {"AccessKeyId": "AKIASYNTH", "SecretAccessKey": "SYNTHSECRET", "SessionToken": "SYNTHTOKEN"}}

            def get_caller_identity(self):
                return {"Arn": "arn:aws:iam::111122223333:user/Member_One"}

            def invoke(self, **kw):
                outer.calls.append(("invoke", kw))
                return {"Payload": io.BytesIO(b'{"ok": true}')}

        return C()


def desktop():
    dc = load(os.path.join(SILVER_DIR, "door_client.py"), "r2_door_client")
    rt = load(os.path.join(SILVER_DIR, "read_timeline.py"), "r2_rt_desktop")
    bad = []
    tmp = tempfile.mkdtemp(prefix="r2desk_")
    try:
        home = os.path.join(tmp, "home")
        os.makedirs(os.path.join(home, "Desktop"))
        d = dc.desktop_dir(environ={"USERPROFILE": home, "HOME": home}, platform="win32", known_folder=lambda: None)
        if os.path.normpath(d) != os.path.normpath(os.path.join(home, "Desktop")):
            bad.append("desktop_dir fallback gave %r" % (d,))
        red = os.path.join(tmp, "OneDrive", "Desktop")
        d2 = dc.desktop_dir(environ={"USERPROFILE": home}, platform="win32", known_folder=lambda: red)
        if os.path.normpath(d2) != os.path.normpath(red):
            bad.append("desktop_dir must prefer the shell's known folder, gave %r" % (d2,))
        repo = os.path.join(tmp, "repo")
        os.makedirs(os.path.join(repo, "Desktop"))
        try:
            dc.write_desktop("x", "pat@op.example", "2026-10-15T00:00:00Z", desktop=os.path.join(repo, "Desktop"), repo_root=repo)
            bad.append("a Desktop inside the repository must be refused")
        except ValueError:
            pass
        deskdir = os.path.join(home, "Desktop")
        rows = _door_rows(5)
        inv, seen = _fake_door(rows)
        out = io.StringIO()
        rc = rt.main(["--account", "Pat@Op.Example", "--start", "2026-10-15T00:00:00Z", "--end", "2026-10-16T00:00:00Z", "--detail", "--desktop"],
                     invoker=inv, out=out, desktop=deskdir, repo_root=repo)
        files = sorted(os.listdir(deskdir))
        if rc != 0 or len(files) != 1 or not re.fullmatch(r"timeline_pat@op\.example_20261015\.txt", files[0]):
            bad.append("--desktop must write one file named timeline_<account>_<yyyymmdd>.txt, got %r rc=%r" % (files, rc))
        else:
            body = open(os.path.join(deskdir, files[0]), "rb").read()
            want = (rt.render(rt.fetch(_fake_door(rows)[0], "pat@op.example", "2026-10-15T00:00:00Z", "2026-10-16T00:00:00Z", detail=True)) + "\n").encode("utf-8")
            if body != want:
                bad.append("the Desktop file is not the rendered answer, byte for byte")
            if "rec-0000" in out.getvalue() or "MailItemsAccessed" in out.getvalue():
                bad.append("with --desktop the screen must show the path only, not the records")
            if files[0] not in out.getvalue():
                bad.append("with --desktop the screen must show the file path")
        os.remove(os.path.join(deskdir, files[0])) if files else None
        out2 = io.StringIO()
        rt.main(["--account", "pat@op.example", "--start", "2026-10-15T00:00:00Z", "--end", "2026-10-16T00:00:00Z", "--detail", "--json", "--desktop"],
                invoker=_fake_door(rows)[0], out=out2, desktop=deskdir, repo_root=repo)
        jf = [f for f in os.listdir(deskdir)]
        if len(jf) != 1 or [r["record_id"] for r in json.loads(open(os.path.join(deskdir, jf[0]), encoding="utf-8").read())["rows"]] != [r["record_id"] for r in rows]:
            bad.append("--json --desktop must write the door's merged answer as JSON")
        # the MFA session
        fb = _FakeBoto(["arn:aws:iam::111122223333:mfa/Dev_One"])
        cap = io.StringIO()
        with contextlib.redirect_stdout(cap), contextlib.redirect_stderr(cap):
            inv_real = dc.build_invoker(profile="member", mfa_code="123456", boto3_module=fb)
            inv_real({"op": "get_state"})
        kinds = [c[0] for c in fb.calls]
        if "get_session_token" not in kinds:
            bad.append("an MFA code must be traded for a session token")
        tok = [c[1] for c in fb.calls if c[0] == "get_session_token"]
        if tok and (tok[0].get("TokenCode") != "123456" or tok[0].get("SerialNumber") != "arn:aws:iam::111122223333:mfa/Dev_One"):
            bad.append("the session token call carries the code and the one device: %r" % (tok,))
        inv_calls = [c[1] for c in fb.calls if c[0] == "invoke"]
        if not inv_calls or inv_calls[0].get("Qualifier") != "member":
            bad.append("the real invoker must call the member alias")
        lam = [c[1] for c in fb.calls if c[0] == "lambda"]
        if not lam or lam[0].get("aws_session_token") != "SYNTHTOKEN":
            bad.append("the lambda client must be built from the session token")
        for secret in ("SYNTHSECRET", "SYNTHTOKEN", "AKIASYNTH"):
            if secret in cap.getvalue():
                bad.append("a session key was printed")
        fb2 = _FakeBoto(["arn:aws:iam::111122223333:mfa/A", "arn:aws:iam::111122223333:mfa/B"])
        try:
            dc.build_invoker(profile="member", mfa_code="123456", boto3_module=fb2)
            bad.append("two MFA devices with no --mfa-serial must raise ValueError")
        except ValueError as e:
            if "mfa/A" not in str(e) or "mfa/B" not in str(e):
                bad.append("the error must list both devices")
        fb3 = _FakeBoto(["arn:aws:iam::111122223333:mfa/A"])
        try:
            dc.build_invoker(profile="member", mfa_code="12ab56", boto3_module=fb3)
            bad.append("a code that is not 6 digits must raise before any call")
        except ValueError:
            if fb3.calls:
                bad.append("a bad code made a call")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return finish("R2-DESKTOP", bad)


def retire():
    dc = load(os.path.join(SILVER_DIR, "door_client.py"), "r2_door_client2")
    rt = load(os.path.join(SILVER_DIR, "read_timeline.py"), "r2_rt_retire")
    bad = []
    seen = []

    def inv(p):
        seen.append(dict(p))
        if p["date"] == "2026-10-15":
            return {"ok": False, "error": "refused"}
        return {"ok": True, "rows": 7}

    res = dc.derive_dates(inv, ["2026-10-16", "2026-10-15"])
    if res != [("2026-10-16", "ok rows=7"), ("2026-10-15", "REFUSED (refused)")]:
        bad.append("derive_dates gave %r" % (res,))
    if sorted(p["date"] for p in seen) != ["2026-10-15", "2026-10-16"] or any(p["op"] != "derive_silver" for p in seen):
        bad.append("one derive_silver call per date: %r" % (seen,))
    n = len(seen)
    for dates in (["2026-10-16", "not-a-date"], ["2026-13-45"]):
        try:
            dc.derive_dates(inv, dates)
            bad.append("a malformed date must raise ValueError before any call: %r" % (dates,))
        except ValueError:
            pass
    if len(seen) != n:
        bad.append("a malformed date made a call")
    out = io.StringIO()
    rc = rt.main(["--derive", "2026-10-16"], invoker=inv, out=out)
    if rc != 0 or "2026-10-16 ok rows=7" not in out.getvalue():
        bad.append("--derive 2026-10-16 must print '2026-10-16 ok rows=7', rc=%r out=%r" % (rc, out.getvalue()))
    for f in STOPGAPS:
        if os.path.exists(f):
            bad.append("the round-1 stopgap still exists: %s" % os.path.relpath(f, ROOT))
    return finish("R2-RETIRE", bad)


# ---------------------------------------------------------------------------------------------------- exposure
def _raw_row(op, feed, when, rid, raw, item=None, ip="203.0.113.7", user="pat@opalinvest.com"):
    return {"time": when, "feed": feed, "operation": op, "client_ip": ip, "item_name": item, "user_id": user, "record_id": rid,
            "result_status": "Succeeded", "raw_json": json.dumps(raw)}


def exposure_door():
    m = load(os.path.join(DOOR, "exposure.py"), "r2_exposure")
    A = "pat@opalinvest.com"
    rows = [
        _raw_row("FileDownloaded", "SharePoint", "2026-10-15T13:00:00Z", "f1", {"ObjectId": "https://x.example/f1.xlsx", "SourceFileName": "plan.xlsx"}, "plan.xlsx"),
        _raw_row("FileAccessed", "OneDrive", "2026-10-15T13:01:00Z", "f2", {"ObjectId": "https://x.example/f2.docx"}, "f2.docx"),
        _raw_row("FilePreviewed", "SharePoint", "2026-10-15T13:02:00Z", "f3", {"ObjectId": "https://x.example/f3.pdf"}, "f3.pdf"),
        _raw_row("FileSyncDownloadedFull", "OneDrive", "2026-10-15T13:03:00Z", "f4", {"ObjectId": "https://x.example/f4.zip"}, "f4.zip"),
        _raw_row("FileModified", "SharePoint", "2026-10-15T13:04:00Z", "f5", {"ObjectId": "https://x.example/f5.txt"}, "f5.txt"),
        _raw_row("MailItemsAccessed", "Exchange", "2026-10-15T13:05:00Z", "m1", {"Folders": [{"Path": "\\Inbox"}]}),
        _raw_row("SharingInvitationCreated", "SharePoint", "2026-10-15T13:06:00Z", "s1",
                 {"TargetUserOrGroupName": "ext@other.example", "TargetUserOrGroupType": "Guest", "ObjectId": "https://x.example/f1.xlsx"}, "plan.xlsx"),
        _raw_row("SharingInvitationCreated", "SharePoint", "2026-10-15T13:07:00Z", "s2",
                 {"TargetUserOrGroupName": "colleague@opalinvest.com", "TargetUserOrGroupType": "Member"}, "plan.xlsx"),
        _raw_row("AnonymousLinkCreated", "SharePoint", "2026-10-15T13:08:00Z", "s3", {"ObjectId": "https://x.example/f1.xlsx"}, "plan.xlsx"),
        _raw_row("New-InboxRule", "Exchange", "2026-10-15T13:09:00Z", "e1",
                 {"Parameters": [{"Name": "Name", "Value": "x"}, {"Name": "ForwardTo", "Value": "smtp:drop@evil.example; boss@opalinvest.com"}]}),
        _raw_row("Set-Mailbox", "Exchange", "2026-10-15T13:10:00Z", "e2", {"Parameters": [{"Name": "ForwardingSmtpAddress", "Value": "smtp:drop2@evil.example"}]}),
        _raw_row("Send", "Exchange", "2026-10-15T13:11:00Z", "e3", {"Item": {"Subject": "hello"}}),
        _raw_row("FileDownloaded", "SharePoint", "2026-10-15T13:12:00Z", "z9", {"ObjectId": "https://x.example/other.xlsx"}, "other.xlsx", user="other@opalinvest.com"),
    ]
    bad = []
    out = m.compute(list(reversed(rows)), A)
    opened = [r["record_id"] for r in out.get("opened", [])]
    if opened != ["f1", "f2", "f3", "f4", "m1"]:
        bad.append("opened is %r, wanted f1 f2 f3 f4 m1 in time order" % (opened,))
    left = [(r["record_id"], r["kind"], r["recipient"]) for r in out.get("left", [])]
    want = [("s1", "share_invitation", "ext@other.example"), ("s3", "anonymous_link", "anyone with the link"),
            ("e1", "forward_rule", "drop@evil.example"), ("e2", "mailbox_forward", "drop2@evil.example")]
    if left != want:
        bad.append("left is %r, wanted %r" % (left, want))
    cats = [u.get("category") for u in out.get("unrecorded", [])]
    if "mail_recipients" not in cats or "mail_opened" in cats:
        bad.append("unrecorded must name mail_recipients and, with MailItemsAccessed present, not mail_opened: %r" % (cats,))
    out2 = m.compute([r for r in rows if r["operation"] != "MailItemsAccessed"], A)
    cats2 = [u.get("category") for u in out2.get("unrecorded", [])]
    if "mail_opened" not in cats2 or any(not u.get("reason") for u in out2["unrecorded"]):
        bad.append("with no MailItemsAccessed the answer must say mail opened is not recorded, with a reason: %r" % (out2.get("unrecorded"),))
    blob = json.dumps(out)
    if "raw_json" in blob or "ObjectId" in blob:
        bad.append("the answer must not carry raw records")
    for e in out.get("opened", []) + out.get("left", []):
        for k in ("time", "operation", "record_id"):
            if k not in e:
                bad.append("entry missing %s: %r" % (k, e))
                break
    return finish("R2-EXPOSURE", bad, "opened=%d left=%d" % (len(out.get("opened", [])), len(out.get("left", []))))


def exposure_client():
    m = load(os.path.join(SILVER_DIR, "read_exposure.py"), "r2_read_exposure")
    bad = []
    seen = []
    reply = {"ok": True, "truncated": False,
             "opened": [{"time": "2026-10-15T13:00:00Z", "operation": "FileDownloaded", "feed": "SharePoint", "item_name": "plan.xlsx", "client_ip": "203.0.113.7", "record_id": "f1"}],
             "left": [{"time": "2026-10-15T13:06:00Z", "kind": "share_invitation", "recipient": "ext@other.example", "operation": "SharingInvitationCreated", "item_name": "plan.xlsx", "record_id": "s1"},
                      {"time": "2026-10-15T13:08:00Z", "kind": "anonymous_link", "recipient": "anyone with the link", "operation": "AnonymousLinkCreated", "item_name": "plan.xlsx", "record_id": "s3"}],
             "unrecorded": [{"category": "mail_recipients", "reason": "the audit feed does not say who a sent mail went to"}]}

    def inv(p):
        seen.append(dict(p))
        return reply

    got = m.fetch(inv, " Pat@OpalInvest.com ", "2026-10-15T00:00:00Z", "2026-10-16T00:00:00Z")
    if seen != [{"op": "exposure", "account": "pat@opalinvest.com", "start": "2026-10-15T00:00:00Z", "end": "2026-10-16T00:00:00Z"}]:
        bad.append("payload %r" % (seen,))
    text = m.render(got)
    for needle in ("OPENED", "LEFT", "NOT RECORDED", "plan.xlsx", "ext@other.example", "anyone with the link", "who a sent mail went to", "09:00:00"):
        if needle not in text:
            bad.append("render lacks %r" % needle)
    empty = m.render({"ok": True, "opened": [], "left": [], "unrecorded": [], "truncated": False})
    if empty.count("none") < 3:
        bad.append("an empty answer must say none for each section")
    try:
        m.fetch(lambda p: {"ok": False, "error": "window"}, "pat@opalinvest.com", "2026-10-15T00:00:00Z", "2026-10-16T00:00:00Z")
        bad.append("a refused door did not raise")
    except RuntimeError:
        pass
    n = len(seen)
    for acct in ("", "nope", None):
        try:
            m.fetch(inv, acct, "2026-10-15T00:00:00Z", "2026-10-16T00:00:00Z")
            bad.append("a bad account reached the door: %r" % (acct,))
        except ValueError:
            pass
    if len(seen) != n:
        bad.append("a bad account made a call")
    return finish("R2-EXPCLIENT", bad)


# ---------------------------------------------------------------------------------------------------- terraform and text
def retry():
    text = open(os.path.join(TRINO, "collector.tf"), encoding="utf-8").read()
    blocks = re.findall(r'resource\s+"aws_lambda_function_event_invoke_config"\s+"[^"]+"\s*\{(.*?)\n\}', text, re.S)
    bad = []
    ok = [b for b in blocks if re.search(r"function_name\s*=\s*aws_lambda_function\.collector\.function_name", b)
          and re.search(r"maximum_retry_attempts\s*=\s*0\b", b)]
    if not ok:
        bad.append("collector.tf has no aws_lambda_function_event_invoke_config for the collector with maximum_retry_attempts = 0")
    if "qualifier" in "".join(ok):
        bad.append("the config must cover the unqualified function, so it carries no qualifier")
    return finish("R2-RETRY", bad)


def tfvalidate():
    bad = []
    main_root = os.path.dirname(subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"], capture_output=True, text=True, cwd=ROOT).stdout.strip())
    mirror = os.path.join(main_root, "infra", "aws", "terraform", "trino", ".terraform", "providers")
    tmp = tempfile.mkdtemp(prefix="r2tf_")
    try:
        dst = os.path.join(tmp, "infra", "aws", "terraform", "trino")
        shutil.copytree(TRINO, dst, ignore=shutil.ignore_patterns(".terraform", "terraform.tfstate*", ".terraform.lock.hcl"))
        shutil.copytree(os.path.join(ROOT, "infra", "logic", "registry"), os.path.join(tmp, "infra", "logic", "registry"))
        for sub, name in (("m365-metadata-collector", "m365-metadata-collector.zip"), ("globgrph-trino-access", "globgrph-trino-access.zip")):
            d = os.path.join(tmp, "infra", "aws", "lambda", sub, "build")
            os.makedirs(d)
            open(os.path.join(d, name), "wb").close()
        init = ["terraform", "init", "-backend=false", "-input=false", "-no-color"] + (["-plugin-dir=" + mirror] if os.path.isdir(mirror) else [])
        p = subprocess.run(init, capture_output=True, text=True, cwd=dst, timeout=110)
        if p.returncode != 0:
            bad.append("terraform init failed: %s" % (p.stdout + p.stderr)[-300:])
        else:
            v = subprocess.run(["terraform", "validate", "-no-color"], capture_output=True, text=True, cwd=dst, timeout=110)
            if v.returncode != 0 or "Success" not in v.stdout:
                bad.append("terraform validate failed: %s" % (v.stdout + v.stderr)[-400:])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return finish("R2-TFVALIDATE", bad)


def text():
    bad = []
    files = [os.path.join(ROOT, "data", "m365_metadata", "README.md"), os.path.join(ROOT, "data", "m365_metadata", "scripts", "app", "RUNBOOK.md"),
             os.path.join(TRINO, "main.tf")]
    pat = re.compile(r"filter\.py|population\.json|\beight\b|\b8[- ]accounts?\b|unsubscribed|not subscribed|\bthree (planned|content)", re.I)
    for f in files:
        for i, line in enumerate(open(f, encoding="utf-8").read().splitlines(), 1):
            if pat.search(line):
                bad.append("%s:%d still says %r" % (os.path.relpath(f, ROOT), i, pat.search(line).group(0)))
    runbook = open(files[1], encoding="utf-8").read()
    for ct in ("Audit.Exchange", "Audit.SharePoint", "Audit.General", "Audit.AzureActiveDirectory"):
        if ct not in runbook:
            bad.append("RUNBOOK does not name %s" % ct)
    if "--profile" not in open(files[0], encoding="utf-8").read():
        bad.append("README has no usage line for a member's named AWS profile (--profile)")
    return finish("R2-TEXT", bad[:8] if len(bad) > 8 else bad)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    table = {"silverip": silverip, "derive": derive, "naming": naming, "paging": paging, "desktop": desktop, "retire": retire,
             "exposure_door": exposure_door, "exposure_client": exposure_client, "retry": retry, "tfvalidate": tfvalidate, "text": text}
    if mode == "derive_run":
        sys.exit(derive_run(sys.argv[2], sys.argv[3]))
    fn = table.get(mode)
    try:
        sys.exit(fn() if fn else 2)
    except FileNotFoundError as e:
        print("R2-%s-REFUSED missing %s" % (mode.upper(), e))
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        print("R2-%s-REFUSED %s: %s" % (mode.upper(), type(e).__name__, str(e)[:240]))
        sys.exit(1)

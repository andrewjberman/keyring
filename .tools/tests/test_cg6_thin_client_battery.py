#!/usr/bin/env python3
"""NFRA_CLDGRPH CG-s-6 (TO-CG-D-3, D3-AC6) -- the thin-client battery.

Runs BOTH ways, at the FILE grain:
    python .tools/tests/test_cg6_thin_client_battery.py          -> prints per-arm denominators, then PASS
    python -m pytest .tools/tests/test_cg6_thin_client_battery.py -q

NO NETWORK: every arm stubs projection_client.query (or urlopen) and stubs the bearer, so the
battery never reads Secrets Manager and never touches the gateway.

WHAT EACH ARM DEFENDS
  i    a clean answer prints the table AND the service's age_line VERBATIM on stderr
  ii   --json keeps stdout a parseable JSON array; the disclosure rides stderr
  iii  an empty result still prints (0 rows), the zero-rows note, and the VINTAGE line
  iv   a service error exits 1 with "ERROR: projection service" and NO fabricated age
  v    the CLI surface carries no --mode/--db-path/--force/--refresh/--fresh (FWD-6)
  vi   kuzu_cli.py's SOURCE names no engine import, no local seam, no local path
  vii  a statement with a quoted literal reaches the transport BYTE-FOR-BYTE (row W1-S10)

RED MUTANTS (a check that cannot fail is not a check): arms iv, v and vii each run their own
detector against a deliberately broken variant and require it to be CAUGHT.
"""
from __future__ import annotations

import contextlib
import io
import json
import os
import re
import sys

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.abspath(os.path.join(_TESTS_DIR, os.pardir, os.pardir))
_GLOBGRPH = os.path.join(_REPO_ROOT, "infra", "aws", "globgrph")
if _GLOBGRPH not in sys.path:
    sys.path.insert(0, _GLOBGRPH)

import projection_client  # noqa: E402
import kuzu_cli  # noqa: E402

KUZU_CLI_SRC_PATH = os.path.join(_GLOBGRPH, "kuzu_cli.py")

AGE_LINE = "Built from the estate as of 2026-09-04 14:45:21 UTC."
VINTAGE = "2026-09-04T14:45:21.329463+00:00"
MANIFEST = "84eb18f1abc29f55c8d7bfe6e9223f0d9bcfb36bf3d51c35a690181c0fe911a9"
PREFIX = "projection/2026-09-04T14:45:21.329463+00:00/"

CLEAN_ANSWER = {
    "rows": [{"t": "LAMBDA", "c": 203}, {"t": "S3KEY", "c": 9001}],
    "vintage": VINTAGE,
    "age_line": AGE_LINE,
    "manifest_sha256": MANIFEST,
    "artifact_prefix": PREFIX,
}
EMPTY_ANSWER = dict(CLEAN_ANSWER, rows=[])

FORBIDDEN_FLAGS = ("--mode", "--db-path", "--force", "--refresh", "--fresh")
FORBIDDEN_SOURCE_TOKENS = ("import kuzu", "_canonical", "_provenance",
                           "CANONICAL_DB_PATH", "ensure_fresh", "kuzu_nessie_db")
# A fabricated age is any computed/rounded age rendering, or the service's own sentence
# printed when the service never answered.
FABRICATED_AGE_RE = re.compile(r"age:\s*[0-9]|[0-9]+(\.[0-9]+)?\s*(h|hours|d|days)\s+old|"
                               r"Built from the estate as of", re.IGNORECASE)


class Arm:
    """One arm; carries its own denominator and prints it."""

    def __init__(self, name: str):
        self.name = name
        self.total = 0
        self.failed = []

    def check(self, cond: bool, label: str) -> None:
        self.total += 1
        if not cond:
            self.failed.append(label)

    def done(self) -> None:
        passed = self.total - len(self.failed)
        tail = "" if not self.failed else "   FAILED: " + "; ".join(self.failed)
        print("ARM %-46s %d of %d checks PASS%s" % (self.name, passed, self.total, tail))
        assert not self.failed, "%s: %s" % (self.name, self.failed)


@contextlib.contextmanager
def _stub_query(answer=None, raises=None, capture=None):
    """Replace projection_client.query for the duration. No network can be reached."""
    original = projection_client.query

    def _fake(statement, timeout_s=20.0):
        if capture is not None:
            capture.append(statement)
        if raises is not None:
            raise raises
        return answer

    projection_client.query = _fake
    try:
        yield
    finally:
        projection_client.query = original


def _run_cli(argv):
    """Run kuzu_cli.main() with argv; return (exit_code, stdout, stderr)."""
    out, err = io.StringIO(), io.StringIO()
    saved = sys.argv
    sys.argv = ["kuzu_cli.py"] + list(argv)
    code = None
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                kuzu_cli.main()
                code = 0
            except SystemExit as ex:
                code = ex.code if isinstance(ex.code, int) else 0
    finally:
        sys.argv = saved
    return code, out.getvalue(), err.getvalue()


# ---------------------------------------------------------------- arm i
def test_arm_i_clean_answer_carries_the_age_line_verbatim():
    arm = Arm("i   clean answer: table + age_line verbatim")
    with _stub_query(answer=CLEAN_ANSWER):
        code, out, err = _run_cli(["MATCH (n:CloudNode) RETURN n.node_type AS t, count(*) AS c"])
    arm.check(code == 0, "exit code 0")
    arm.check("LAMBDA" in out and "9001" in out, "table rows on stdout")
    arm.check("(2 rows)" in out, "row count on stdout")
    arm.check("VINTAGE: " + AGE_LINE in err, "age_line VERBATIM on the stderr disclosure")
    arm.check(err.count("VINTAGE:") == 1, "exactly ONE disclosure line")
    arm.check("vintage=" + VINTAGE in err, "machine field: vintage")
    arm.check("manifest=" + MANIFEST[:12] in err and MANIFEST not in err,
              "machine field: manifest truncated to 12")
    arm.check("prefix=" + PREFIX in err, "machine field: artifact_prefix")
    arm.check(err.index(AGE_LINE) < err.index("vintage="), "plain words come FIRST")
    arm.done()


# ---------------------------------------------------------------- arm ii
def test_arm_ii_json_stdout_stays_a_parseable_array():
    arm = Arm("ii  --json: stdout array, disclosure on stderr")
    with _stub_query(answer=CLEAN_ANSWER):
        code, out, err = _run_cli(["--json", "MATCH (n) RETURN count(n) AS nodes"])
    arm.check(code == 0, "exit code 0")
    parsed = None
    try:
        parsed = json.loads(out)
        arm.check(True, "stdout parses as JSON")
    except ValueError:
        arm.check(False, "stdout parses as JSON")
    arm.check(isinstance(parsed, list), "stdout is a JSON ARRAY")
    arm.check(isinstance(parsed, list) and len(parsed) == 2, "array carries both rows")
    arm.check("VINTAGE:" not in out, "no disclosure on stdout")
    arm.check("VINTAGE: " + AGE_LINE in err, "disclosure with age_line on stderr")
    arm.done()


# ---------------------------------------------------------------- arm iii
def test_arm_iii_empty_result_still_discloses():
    arm = Arm("iii empty result: (0 rows) + note + VINTAGE")
    with _stub_query(answer=EMPTY_ANSWER):
        code, out, err = _run_cli(["MATCH (n:CloudNode) WHERE n.node_type='NOPE' RETURN n.name"])
    arm.check(code == 0, "exit code 0")
    arm.check("(0 rows)" in out, "(0 rows) on stdout")
    arm.check("0-rows scope" in out, "zero-rows scope note in table mode")
    arm.check("VINTAGE: " + AGE_LINE in err, "age_line verbatim on an EMPTY answer too")
    arm.done()


# ---------------------------------------------------------------- arm iv (+ RED mutant)
def _fabricated_age_detector(error_output: str) -> bool:
    """True when the error output carries an age it could not have known."""
    return bool(FABRICATED_AGE_RE.search(error_output))


def test_arm_iv_service_error_exits_1_with_no_fabricated_age():
    arm = Arm("iv  service error: rc1, no fabricated age")
    boom = projection_client.ProjectionClientError(
        "projection service HTTP 502: Parser exception", status=502,
        error="Parser exception: Invalid input")
    with _stub_query(raises=boom):
        code, out, err = _run_cli(["MATCH (n RETURN oops"])
    arm.check(code == 1, "exit code 1")
    arm.check("ERROR: projection service 502: Parser exception: Invalid input" in err,
              "ERROR line names the status and the service's error field")
    arm.check(not _fabricated_age_detector(err), "REAL: no fabricated age in the error output")
    arm.check("no age was inferred" in err, "the disclosure names the ABSENCE of a vintage")
    arm.check(out.strip() == "", "nothing on stdout for a failed answer")
    # RED MUTANT: a client that prints a made-up age on the error path.
    mutant = ("ERROR: projection service 502: Parser exception\n"
              "VINTAGE: age: 0.0h (assumed current)\n")
    arm.check(_fabricated_age_detector(mutant), "MUTANT CAUGHT: 'age: 0.0h' on the error path")
    mutant2 = "ERROR: projection service 502: x\nVINTAGE: " + AGE_LINE + "\n"
    arm.check(_fabricated_age_detector(mutant2),
              "MUTANT CAUGHT: the service sentence printed when the service never answered")
    arm.done()


# ---------------------------------------------------------------- arm v (+ RED mutant)
def _forbidden_flag_hits(text: str):
    return [f for f in FORBIDDEN_FLAGS if f in text]


def test_arm_v_cli_surface_has_no_refresh_choice():
    arm = Arm("v   CLI surface: no refresh/db-path choice")
    code, out, err = _run_cli(["--help"])
    arm.check(code == 0, "--help exits 0")
    arm.check(len(out) > 0, "--help printed a usage surface")
    hits = _forbidden_flag_hits(out + err)
    arm.check(hits == [], "REAL: 0 of %d forbidden flags present (found: %s)"
              % (len(FORBIDDEN_FLAGS), hits))
    arm.check("--json" in out and "--limit" in out and "--schema" in out,
              "the KEPT flags are still there")
    # RED MUTANT: a help text that re-adds --mode.
    mutant_help = out + "\n  --mode {auto,full,inc}   refresh mode\n"
    arm.check(_forbidden_flag_hits(mutant_help) == ["--mode"],
              "MUTANT CAUGHT: a re-added --mode is detected")
    arm.done()


# ---------------------------------------------------------------- arm vi
def test_arm_vi_source_names_no_engine_no_seam_no_local_path():
    arm = Arm("vi  kuzu_cli.py source: no engine, no seam")
    with open(KUZU_CLI_SRC_PATH, "r", encoding="utf-8") as fh:
        src = fh.read()
    for token in FORBIDDEN_SOURCE_TOKENS:
        arm.check(token not in src, "source carries no %r" % token)
    arm.check("projection_client" in src, "source DOES reach the served projection client")
    print("    denominator: %d source token(s) scanned over %d line(s) of %s"
          % (len(FORBIDDEN_SOURCE_TOKENS), src.count("\n") + 1, os.path.basename(KUZU_CLI_SRC_PATH)))
    arm.done()


# ---------------------------------------------------------------- arm vii (+ RED mutant)
LITERAL_STATEMENT = ("MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) "
                     "WHERE e.edge_type='TRIGGERS' RETURN a.node_id LIMIT 3")


def _requote_mutant(statement: str) -> bytes:
    """The W1-S10 defect, made explicit: a shell-escaping idiom applied to the body."""
    return ("'" + statement.replace("'", "'\\''") + "'").encode("utf-8")


def test_arm_vii_string_literal_reaches_the_transport_byte_for_byte():
    arm = Arm("vii string literal: byte-for-byte to the wire")
    # (a) CLI -> client: the statement handed to query() is exactly what was typed.
    seen = []
    with _stub_query(answer=EMPTY_ANSWER, capture=seen):
        code, out, err = _run_cli([LITERAL_STATEMENT])
    arm.check(code == 0, "exit code 0")
    arm.check(seen == [LITERAL_STATEMENT],
              "CLI passed the statement to the client unaltered (1 of 1 statement)")

    # (b) client -> HTTP: the request BODY bytes are the statement's own UTF-8 bytes.
    captured = {}

    class _Resp:
        def read(self):
            return json.dumps(EMPTY_ANSWER).encode("utf-8")

        def getcode(self):
            return 200

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

    def _fake_urlopen(req, timeout=None):
        captured["body"] = req.data
        captured["url"] = req.full_url
        captured["auth"] = req.get_header("Authorization")
        return _Resp()

    saved_urlopen = projection_client.urllib.request.urlopen
    saved_token = projection_client._TOKEN_CACHE
    projection_client.urllib.request.urlopen = _fake_urlopen
    projection_client._TOKEN_CACHE = "battery-stub-token-not-a-secret"
    try:
        answer = projection_client.query(LITERAL_STATEMENT)
    finally:
        projection_client.urllib.request.urlopen = saved_urlopen
        projection_client._TOKEN_CACHE = saved_token

    arm.check(captured.get("body") == LITERAL_STATEMENT.encode("utf-8"),
              "REAL: request body == statement.encode('utf-8'), byte for byte")
    arm.check(b"'\\''" not in (captured.get("body") or b""), "REAL: no shell-escape idiom in the body")
    arm.check(captured.get("url", "").endswith("/graph/cypher"), "posted to /graph/cypher")
    arm.check(answer == EMPTY_ANSWER, "the service dict is returned VERBATIM")
    # RED MUTANT: a client that re-quotes the statement.
    arm.check(_requote_mutant(LITERAL_STATEMENT) != LITERAL_STATEMENT.encode("utf-8"),
              "MUTANT CAUGHT: a re-quoting client changes the bytes on the wire")
    print("    denominator: 2 transport grains checked (CLI->client, client->HTTP body); "
          "statement length %d chars, %d quote char(s)"
          % (len(LITERAL_STATEMENT), LITERAL_STATEMENT.count("'")))
    arm.done()


ARMS = [
    test_arm_i_clean_answer_carries_the_age_line_verbatim,
    test_arm_ii_json_stdout_stays_a_parseable_array,
    test_arm_iii_empty_result_still_discloses,
    test_arm_iv_service_error_exits_1_with_no_fabricated_age,
    test_arm_v_cli_surface_has_no_refresh_choice,
    test_arm_vi_source_names_no_engine_no_seam_no_local_path,
    test_arm_vii_string_literal_reaches_the_transport_byte_for_byte,
]


def main() -> int:
    print("CG-s-6 THIN-CLIENT BATTERY -- %d arm(s), no network" % len(ARMS))
    failures = []
    for fn in ARMS:
        try:
            fn()
        except AssertionError as ex:
            failures.append("%s: %s" % (fn.__name__, ex))
    print("BATTERY: %d of %d arm(s) PASS" % (len(ARMS) - len(failures), len(ARMS)))
    if failures:
        for f in failures:
            print("  FAIL " + f)
        print("FAIL")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

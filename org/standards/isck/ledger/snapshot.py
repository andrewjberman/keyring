#!/usr/bin/env python
"""WP-3b AC5 -- the published snapshot is a SURFACE, not a copy (B3, decided).

THE DEFECT THIS FILE EXISTS TO PREVENT, measured before it was designed around: engine.py runs
`PRAGMA journal_mode=WAL`. In WAL mode committed rows live in the `-wal` sidecar until a checkpoint,
so a digest taken over the live `.sqlite` main file is a FALSE IDENTITY in both directions at once --
it does not change when the ledger does (two different estates hash identically), and a copy of that
one file contains none of the data. Not stale. EMPTY. A reader checking "does the digest match?"
gets YES on a file with no table in it.

Measured, fresh WAL store, 50 rows committed:
    .sqlite digest before == after           True
    rows visible in a COPY of the main file  error: no such table (of 50 committed)

SO THE PUBLISHED ARTIFACT IS PRODUCED BY `VACUUM INTO`, never by copying the live file. VACUUM INTO
writes ONE self-contained, transactionally consistent database whose bytes ARE the estate. The
checkpoint-then-copy alternative is admissible only under explicit writer quiescence: it leaves a
race between the checkpoint and the hash, and a write landing in that window reopens exactly the gap
this file closes. The method used is PRINTED beside the digest, so a reader never has to infer it.

A DIGEST WITHOUT ITS NORMALISATION IS NOT AN IDENTITY. `content_digest` is computed under a DECLARED
`fingerprint_method` and `normalization_version`, both already required fields on `surface_version`.
Same rule that cost this seat a refused receipt earlier today when a CRLF/LF split moved a hash.

THE ANCHOR BINDS IN THE RECEIPT, NEVER IN THE RECORD. `surface_version` is additionalProperties:false
and `commit_seq` is an ENVELOPE fact, not a record field -- so the binding "surface <id> published at
admitting-batch commit_seq <n>" lives in the receipt/evidence. The frozen contract does not move.

BOTH CONTROLS ARE REQUIRED AND THE NEGATIVE ONE MUST FAIL. A positive control alone cannot tell a
working publication from a vacuous one; the negative arm -- the naive main-file copy, retained, which
must return fewer rows or fail to open -- is what makes the digest mean anything. If the negative arm
ever PASSES, the publication method has silently become a copy again and the digest is void.
"""
import hashlib
import os
import shutil
import sqlite3

FINGERPRINT_METHOD = "sha256-over-published-artifact-bytes"
NORMALIZATION_VERSION = "v1-vacuum-into-single-file"


def publish(store_path, dest_path, method="vacuum_into"):
    """Write the published artifact. Returns (path, method, digest, byte length).

    Never copies the live main file. Never deletes an existing destination -- a publication that
    overwrites is not a publication, it is a replacement with no record of what it replaced.
    """
    if os.path.exists(dest_path):
        raise SystemExit("REFUSING: publication target %s already exists; a snapshot never "
                         "overwrites a prior artifact" % dest_path)
    con = sqlite3.connect(store_path)
    try:
        if method == "vacuum_into":
            con.execute("VACUUM INTO ?", (dest_path,))
        elif method == "backup_api":
            out = sqlite3.connect(dest_path)
            con.backup(out)
            out.close()
        else:
            raise SystemExit("REFUSING: unknown publication method %r -- the only self-contained "
                             "forms are vacuum_into and backup_api" % method)
    finally:
        con.close()
    blob = open(dest_path, "rb").read()
    return dest_path, method, "sha256:" + hashlib.sha256(blob).hexdigest(), len(blob)


def naive_main_file_copy(store_path, dest_path):
    """THE NEGATIVE CONTROL, retained deliberately. Copies ONLY the main file, as a naive
    publisher would, leaving the -wal sidecar behind. This must FAIL."""
    shutil.copy(store_path, dest_path)
    return dest_path


def read_alone(artifact_path):
    """Open the artifact with NOTHING else present and report what it holds.

    'Opened alone' is the whole test: a snapshot that only reads correctly beside its own sidecars
    is not a shared carrier, it is a pointer to a live store.
    """
    con = sqlite3.connect("file:%s?mode=ro" % artifact_path.replace("\\", "/"), uri=True)
    try:
        rows = con.execute("SELECT COUNT(*) FROM records").fetchone()[0]
        seq = con.execute("SELECT MAX(commit_seq) FROM records").fetchone()[0]
        return {"rows": rows, "anchor_commit_seq": seq}
    finally:
        con.close()


def controls(store_path, published_path, naive_path, expected_rows, expected_anchor):
    """AC5's two arms. Returns (ok, report). The negative arm PASSING is a failure of the whole AC."""
    report = {}
    try:
        pos = read_alone(published_path)
        report["positive"] = {
            "rows": pos["rows"], "anchor_commit_seq": pos["anchor_commit_seq"],
            "rows_match": pos["rows"] == expected_rows,
            "anchor_match": pos["anchor_commit_seq"] == expected_anchor,
            "verdict": ("PASS" if pos["rows"] == expected_rows
                        and pos["anchor_commit_seq"] == expected_anchor else "FAIL"),
        }
    except Exception as exc:                                           # noqa: BLE001
        report["positive"] = {"verdict": "FAIL", "error": "%s: %s" % (type(exc).__name__, exc)}

    try:
        neg = read_alone(naive_path)
        report["negative"] = {
            "rows": neg["rows"],
            "verdict": ("PASS-AS-A-CONTROL" if neg["rows"] < expected_rows else "DID-NOT-FAIL"),
            "note": ("returned fewer rows than the estate, as a main-file copy must"
                     if neg["rows"] < expected_rows else
                     "returned the full estate -- the publication path has become a copy and the "
                     "digest is VOID"),
        }
    except Exception as exc:                                           # noqa: BLE001
        report["negative"] = {"verdict": "PASS-AS-A-CONTROL", "rows": None,
                              "note": "failed to open at all: %s" % type(exc).__name__}

    ok = (report["positive"].get("verdict") == "PASS"
          and report["negative"].get("verdict") == "PASS-AS-A-CONTROL")
    return ok, report


def surface_version_record(surface_version_id, logical_surface, frontier_id, run_id, digest,
                           published_at, promoter):
    """The ONE surface_version. No commit_seq field: the anchor binds in the receipt (AC5)."""
    return {
        "record_type": "surface_version",
        "surface_version_id": surface_version_id,
        "logical_surface_serial": logical_surface,
        "source_frontier_id": frontier_id,
        "producing_run_id": run_id,
        "publication_state": "published",
        "published_at": published_at,
        "promoted_by": promoter,
        "content_digest": digest,
        "fingerprint_method": FINGERPRINT_METHOD,
        "normalization_version": NORMALIZATION_VERSION,
    }

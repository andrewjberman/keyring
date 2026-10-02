#!/usr/bin/env python3
"""Hop 11's live proof (CTO rulings batch 123): the PDF route of an owned READY request answers an Opal-signed URL that
downloads exactly the bytes the route names.

    python hop11_pdf_proof.py <tenant> <out.json> <request-id> [<request-id> ...]

One login as svc-irpt-analysis. Per request: ONE GET of analysis/requests/{id}/pdf, then ONE GET of the signed URL it
returns. Recorded: HTTP status, ok/state/reason, the URL's HOST only (never its query, which carries the signature),
expires_at and its distance from now (<= 300 s expected), the claimed sha256 and byte_length, and the downloaded bytes'
own sha256 and length. A request that is not READY must be refused by name. Nothing is created; no vendor is reached
(the URL is Opal's own store). The password is read by NAME and never printed. ASCII only.
"""
import datetime
import email.utils
import hashlib
import json
import sys
import urllib.parse
import urllib.request

import served_reads_before_after as reads
import svc_principal as sp


def main(argv):
    tenant, out, request_ids = argv[1], argv[2], argv[3:]
    log = []
    password = sp._sm().get_secret_value(SecretId=sp.SECRET)["SecretString"]
    code, login = sp._call("POST", "/auth/login", {"email": sp.EMAIL, "password": password},
                           {"Content-Type": "application/json"}, log)
    del password
    token = login.get("accessToken") if isinstance(login, dict) else None
    print("login HTTP %s token %s" % (code, bool(token)))
    if not token:
        return 1
    headers = {"Authorization": "Bearer " + token, "X-Contract-Version": "v1", "Content-Type": "application/json"}
    rows = []
    for rid in request_ids:
        code, resp = sp._call("GET", reads.BASE + "analysis/requests/%s/pdf?selected_tenant=%s" % (rid, tenant),
                              None, headers, log)
        row = {"request_id": rid, "http": code}
        row.update(reads.shape(resp))
        data = resp.get("data") if isinstance(resp, dict) else None
        if isinstance(data, dict) and isinstance(data.get("download_route"), dict):
            url = data["download_route"].get("url", "")
            expires = data["download_route"].get("expires_at")
            parsed = urllib.parse.urlsplit(url)
            row.update(url_host=parsed.netloc, url_scheme=parsed.scheme, claimed_sha256=data.get("sha256"),
                       claimed_bytes=data.get("byte_length"), expires_at=expires)
            # X-Amz-Expires is the signature's own lifetime (not secret; the signature itself is never recorded).
            signed_for = urllib.parse.parse_qs(parsed.query).get("X-Amz-Expires", [None])[0]
            row["x_amz_expires"] = int(signed_for) if signed_for and signed_for.isdigit() else None
            try:
                stamp = datetime.datetime.strptime(expires, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
                # The laptop clock is NOT synced (w32time stopped; AWS Date read 2.6-3.6 s ahead at 18:0xZ), so the
                # laptop reading is kept for the record and the grade uses AWS's own clock: the download's Date header.
                row["expires_in_s_laptop"] = round((stamp - datetime.datetime.now(datetime.timezone.utc)).total_seconds())
            except (TypeError, ValueError):
                stamp = None
            with urllib.request.urlopen(url, timeout=60) as got:
                body = got.read()
                row.update(download_http=got.status, download_type=got.headers.get_content_type())
                served_at = got.headers.get("Date")
            row["expires_in_s"] = (round((stamp - email.utils.parsedate_to_datetime(served_at)).total_seconds())
                                   if stamp and served_at else None)
            row.update(download_bytes=len(body), download_sha256=hashlib.sha256(body).hexdigest(),
                       pdf_magic=body[:5] == b"%PDF-")
            row["verdict"] = ("MATCH" if row["download_sha256"] == row["claimed_sha256"]
                              and row["download_bytes"] == row["claimed_bytes"] and row["pdf_magic"]
                              and isinstance(row["expires_in_s"], int) and 0 < row["expires_in_s"] <= 300
                              and row["x_amz_expires"] is not None and 0 < row["x_amz_expires"] <= 300
                              else "MISMATCH")
        else:
            row["verdict"] = "REFUSED:%s" % row.get("reason")
        rows.append(row)
        print("%-30s HTTP %s %s host %s expires_in(aws) %s laptop %s X-Amz-Expires %s claimed %s/%s downloaded %s/%s" % (
            rid, code, row["verdict"], row.get("url_host"), row.get("expires_in_s"), row.get("expires_in_s_laptop"),
            row.get("x_amz_expires"),
            str(row.get("claimed_sha256"))[:12], row.get("claimed_bytes"),
            str(row.get("download_sha256"))[:12], row.get("download_bytes")))
    del token
    json.dump({"at": sp._now(), "principal": sp.EMAIL, "tenant": tenant, "rows": rows},
              open(out, "w", encoding="utf-8", newline="\n"), indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

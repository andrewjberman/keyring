"""Y7: ONE reconciled full trace of a live Analysis case, from the live rows and retained artifacts. Read-only.

    python case_trace.py <tenant> <REQ-id> [--revision 1] [--out trace.json]

Every hop is read from the served store: consistent GetItem on irpt-requests / irpt-jobs, and s3api get-object by
the VERSION each row names, re-hashed here. No write, no queue access, no vendor call. Each link is MATCH or MISMATCH
on measured values. The screen (the portal's K10 walk) and the same-revision export (window 16) are NOT_EVALUATED
until they run: this tool does not stand in for them.

Hops: original upload -> normalization -> normalized input -> request composition -> job (vendor echo, read-back) ->
retained vendor PDF (whose settings table names this job's portfolio) -> extraction evidence -> certified report,
whose every scalar section is re-read at its own page and coordinates in the retained PDF.

Comparison and Multi-Comp cases: the variant must be the recipe's for the key count; each key's frozen identity must be
the maintained catalogue's; and the retained PDF must print, of the catalogue's portfolios, exactly the chosen ones.
Every case: the served foreign-firm name check passes the PDF for its own firm. Arms on the 09-11 research Comparison
and Multi-Comp PDFs and window 15's Overview: 2 MATCH, and 4 wrong choices MISMATCH.
"""
import argparse
import csv
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
from decimal import Decimal

from boto3.dynamodb.types import TypeDeserializer

AWS = r"C:\Users\AndrewBerman\Desktop\ajb_workspace\.tools\aws.cmd"
# The extractor's own reader for the printed settings row (Y @36837771d6); the served resident carries it once P ships.
EXTRACT = r"C:\Users\AndrewBerman\Desktop\irpt-mvp-y-20260922\infra\aws\lambda\investor-reporting\ycharts\extract"
# The recipe's own variant rule, and the maintained comparison catalogue (templates.json, CRLF-normalized sha 54656584
# = the served generate AdE17rT6 and resident st2 member).
GENERATE = r"C:\Users\AndrewBerman\Desktop\irpt-mvp-y-20260922\infra\aws\lambda\investor-reporting\ycharts\generate"
_de = TypeDeserializer()


def aws(*args):
    out = subprocess.run([AWS, *args, "--output", "json"], capture_output=True, text=True)
    if out.returncode:
        raise SystemExit("ERROR: aws %s rc=%d %s" % (args[1], out.returncode, out.stderr.strip()[:200]))
    return json.loads(out.stdout) if out.stdout.strip() else {}


def item(table, key):
    got = aws("dynamodb", "get-item", "--table-name", table, "--key", json.dumps(key), "--consistent-read")
    return {k: _de.deserialize(v) for k, v in (got.get("Item") or {}).items()}


class Trace:
    def __init__(self, tenant):
        self.tenant, self.links = tenant, []

    def req(self, sk):
        return item("irpt-requests", {"tenant": {"S": self.tenant}, "request_revision": {"S": sk}})

    def blob(self, artifact_id):
        """The artifact's bytes by the version its index row names, and that row."""
        row = self.req("ARTIFACT#" + artifact_id)
        b = row["blob"]
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "blob")
            aws("s3api", "get-object", "--bucket", b["bucket"], "--key", b["key"], "--version-id", b["version_id"], path)
            data = open(path, "rb").read()
        return data, row

    def link(self, hop, claim, ok, **measured):
        self.links.append({"hop": hop, "claim": claim, "verdict": "MATCH" if ok else "MISMATCH", "measured": measured})
        print("%-9s %-14s %s | %s" % ("MATCH" if ok else "MISMATCH", hop, claim,
                                      json.dumps(measured, default=str)[:220]))

    def not_evaluated(self, hop, claim, reason):
        self.links.append({"hop": hop, "claim": claim, "verdict": "NOT_EVALUATED", "reason": reason})
        print("%-9s %-14s %s | %s" % ("NOT_EVAL", hop, claim, reason))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def money(value):
    return Decimal(str(value)).quantize(Decimal("0.01"))


def printed_number(text):
    """The first number printed in a cropped cell: '0.30%' -> 0.30, '-1,234.5' -> -1234.5."""
    m = re.search(r"[-\u2212]?\d[\d,]*\.?\d*", text or "")
    return None if not m else float(m.group().replace(",", "").replace("\u2212", "-"))


def served_catalogue():
    """The maintained comparison catalogue entries by key, and the templates.json sha (CRLF-normalized)."""
    raw = open(os.path.join(GENERATE, "templates.json"), "rb").read().replace(b"\r\n", b"\n")
    entries = json.loads(raw)["comparison_catalog"]["entries"]
    return {e["key"]: e for e in entries}, sha(raw)


def printed_labels(pdf_bytes, labels):
    """{label: [pages]} for each catalogue label printed whole (not inside a longer name) somewhere in the PDF."""
    import pdfplumber
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        texts = [p.extract_text() or "" for p in pdf.pages]
    found = {}
    for label in labels:
        pattern = re.compile(r"(?<![\w-])%s(?![\w-])" % re.escape(label))
        pages = [i + 1 for i, text in enumerate(texts) if pattern.search(text)]
        if pages:
            found[label] = pages
    return found


def reread_sections(pdf_bytes, sections):
    """Each scalar section's value, re-read at its own page and bbox in the retained PDF (not the certifier's verdict)."""
    import pdfplumber
    checked, matched, misses = 0, 0, []
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        for s in sections:
            if s.get("value") is None or not isinstance(s["value"], (int, float)):
                continue
            page = pdf.pages[s["page"] - 1]
            x0, top, x1, bottom = s["bbox"]
            crop = page.crop((max(0, x0 - 1), max(0, top - 1), min(page.width, x1 + 1), min(page.height, bottom + 1)))
            got = printed_number(crop.extract_text())
            checked += 1
            if got is not None and abs(got - float(s["value"])) < 1e-9:
                matched += 1
            else:
                misses.append({"section_id": s["section_id"], "value": s["value"], "printed": got})
    return checked, matched, misses


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("tenant")
    ap.add_argument("request_id")
    ap.add_argument("--revision", type=int, default=1)
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    t = Trace(a.tenant)

    # 1. The request and its composition (the browser's intent, frozen).
    record = json.loads(t.req("analysis#%s#%d" % (a.request_id, a.revision))["record"])
    comp_ref = record["composition_ref"]
    comp_bytes, _ = t.blob(comp_ref["artifact_id"])
    comp = json.loads(comp_bytes)
    t.link("request", "the composition's bytes hash to the request's composition_ref", sha(comp_bytes) == comp_ref["sha256"],
           sha256=comp_ref["sha256"][:16], request_id=record["identity"]["request_id"], variant=comp["browser"]["variant"])
    input_id = comp["browser"]["input_id"]
    input_ref = comp["resolved"]["input_ref"]
    t.link("request", "the composition binds the browser's input_id to that input's own artifact",
           input_ref["input_id"] == input_id and input_ref["artifact_ref"]["sha256"] == input_id.split("_", 1)[1],
           input_id=input_id[:26])
    sys.path.insert(0, GENERATE)
    import recipe  # noqa: E402
    keys = comp["browser"].get("comparison_keys") or []
    variant = recipe.variant_for_comparison_count(len(keys))
    descriptors = comp["resolved"]["source_descriptors"]
    templates = {d["projection"].get("template_id") for d in descriptors.values() if "template_id" in d["projection"]}
    t.link("request", "the variant is the recipe's for the comparison count, and every recipe source names one template",
           comp["browser"]["variant"].upper().replace("MULTICOMP", "MULTI") == variant
           and {d["projection"].get("variant") for d in descriptors.values() if "variant" in d["projection"]} == {variant}
           and len(templates) == 1, keys=keys, variant=variant, template_id=sorted(templates))
    catalogue, catalogue_sha = served_catalogue()
    frozen = comp["resolved"].get("comparison_catalog") or {}
    chosen = [frozen.get(k) or {} for k in keys]
    t.link("request", "each chosen key's frozen identity is the maintained catalogue's (security id, label, model portfolio)",
           set(frozen) == set(keys) and all(
               k in catalogue and c.get("vendor_id") == catalogue[k]["security_id"] and c.get("name") == catalogue[k]["label"]
               and c.get("security_type") == catalogue[k]["security_type"] == "model_portfolio" for k, c in zip(keys, chosen)),
           frozen={k: [c.get("vendor_id"), c.get("name")] for k, c in zip(keys, chosen)}, catalogue_sha=catalogue_sha[:8])

    # 2. The normalized input and the upload it came from.
    inp = t.req("INPUT#" + input_id)
    norm_bytes, _ = t.blob(inp["artifact_ref"]["artifact_id"])
    norm = json.loads(norm_bytes)
    t.link("input", "the normalized artifact hashes to its content-addressed input id",
           sha(norm_bytes) == inp["content_sha256"] == input_id.split("_", 1)[1], sha256=sha(norm_bytes)[:16])
    upload_id = inp["upload_id"]
    up = t.req("UPLOAD#" + upload_id)
    csv_bytes, _ = t.blob(up["artifact_ref"]["artifact_id"])
    t.link("upload", "the retained original upload hashes to its recorded content_sha256, and the input cites it",
           sha(csv_bytes) == up["content_sha256"] == norm["source"]["content_sha256"],
           filename=up["filename"], lane=up["source_lane"], sha256=up["content_sha256"][:16])
    csv_rows = [r for r in csv.reader(io.StringIO(csv_bytes.decode("utf-8-sig"))) if r]
    csv_holdings = {r[0].strip(): money(r[1]) for r in csv_rows[1:]}
    norm_holdings = {r["security_id"]: money(r["dollars"]) for r in norm["holdings"]["rows"]}
    t.link("normalize", "every uploaded row reaches the normalized holdings at the same dollars, and the total reconciles",
           csv_holdings == norm_holdings and sum(norm_holdings.values()) == money(norm["holdings"]["total_dollars"]),
           upload={k: str(v) for k, v in csv_holdings.items()}, total=norm["holdings"]["total_dollars"])
    norm_rows = aws("dynamodb", "query", "--table-name", "irpt-requests", "--consistent-read",
                    "--key-condition-expression", "tenant = :t AND begins_with(request_revision, :p)",
                    "--expression-attribute-values", json.dumps({":t": {"S": a.tenant},
                                                                  ":p": {"S": "NORMALIZATION#%s#" % upload_id}}))["Items"]
    norm_rows = [{k: _de.deserialize(v) for k, v in r.items()} for r in norm_rows]
    t.link("normalize", "the upload's normalization row reads NORMALIZED and names this input",
           len(norm_rows) == 1 and norm_rows[0]["state"] == "NORMALIZED" and norm_rows[0]["input_id"] == input_id,
           rows=len(norm_rows), state=norm_rows[0]["state"] if norm_rows else None)

    # 3. The job: what the resident sent the vendor, what the vendor echoed and saved.
    job = item("irpt-jobs", {"tenant": {"S": a.tenant}, "job": {"S": a.request_id}})
    cp = {k[len("checkpoint_"):]: json.loads(v) for k, v in job.items() if k.startswith("checkpoint_")}
    echoed = {r["security_id"]: money(r["weighting"]) for r in cp["upload"]["rows"]}
    t.link("vendor", "the vendor's upload echo equals the normalized holdings (rows sent = rows echoed)",
           echoed == norm_holdings and cp["upload"]["rows_sent"] == cp["upload"]["rows_echoed"] == len(norm_holdings),
           echoed={k: str(v) for k, v in echoed.items()}, upload_record_id=cp["upload"]["upload_record_id"],
           weight_unit=cp["upload"]["weight_unit_echoed"])
    rb = cp["read_back"]
    tolerated = [r["setting"] + "=" + str(r["actual"]) for r in rb["rows"] if r.get("tolerated")]
    t.link("vendor", "the saved portfolio's settings read back: every row matches or is a tolerated, recorded row",
           rb["ok"] and all(r["matches"] or r.get("tolerated") for r in rb["rows"]),
           matched="%s/%s" % (rb["matched"], rb["denominator"]), tolerated=tolerated,
           portfolio=cp["portfolio"]["model_portfolio_id"])
    t.link("job", "the job is READY for this request revision", job.get("state") == "READY"
           and str(job.get("request_revision")) == str(a.revision), state=job.get("state"))

    # 4. The retained vendor PDF.
    pdf_ref = cp["pdf"]["pdf_ref"]
    pdf_bytes, _ = t.blob(pdf_ref["artifact_id"])
    meta = cp["pdf"]["metadata"]
    t.link("pdf", "the retained PDF hashes to its checkpoint, and the checkpoint binds this request",
           sha(pdf_bytes) == pdf_ref["sha256"] == meta["vendor_artifact"]["sha256"]
           and meta["request_ref"]["request_id"] == a.request_id,
           sha256=pdf_ref["sha256"][:16], bytes=len(pdf_bytes), retrieved_at=meta["vendor_artifact"]["retrieved_at"])
    sys.path.insert(0, EXTRACT)
    import extract  # noqa: E402
    printed = extract.calculation_settings(pdf_bytes, cp["portfolio"]["name"])
    t.link("pdf", "the PDF's settings table prints a row for THIS job's portfolio name (the vendor document is ours)",
           printed is not None, name=cp["portfolio"]["name"], printed=printed)
    t.link("pdf", "the effective settings the report records are the read-back's actual values",
           meta["effective_inputs"]["settings"] == {r["setting"]: r["actual"] for r in rb["rows"]},
           effective=meta["effective_inputs"]["settings"])
    labels = printed_labels(pdf_bytes, [e["label"] for e in catalogue.values()])
    t.link("pdf", "of the catalogue's portfolios, the PDF prints exactly the chosen comparisons (the vendor compared "
                  "what was asked)", set(labels) == {c.get("name") for c in chosen}, printed=labels)
    import publication  # noqa: E402  (the served name check, Y @14568b9ec1 = st2's 6aa82b3a)
    foreign = publication.foreign_firm_names(pdf_bytes, a.tenant)
    t.link("pdf", "the served foreign-firm name check passes the PDF for its own firm", foreign == [], foreign=foreign)

    # 5. Extraction evidence and the certified report.
    pub = cp["publication"]
    ev_bytes, _ = t.blob(pub["extraction_evidence_ref"]["artifact_id"])
    t.link("extract", "the extraction evidence hashes to the certification sha the publication recorded",
           sha(ev_bytes) == pub["extraction_evidence_ref"]["sha256"] == pub["certification_sha256"],
           sha256=pub["certification_sha256"][:16])
    rep_ref = pub["report_ref"]
    rep_row = t.req("REPORT#%s#%s" % (rep_ref["report_id"], rep_ref["revision"]))
    b = rep_row["blob"]
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "report")
        aws("s3api", "get-object", "--bucket", b["bucket"], "--key", b["key"], "--version-id", b["version_id"], path)
        rep_bytes = open(path, "rb").read()
    rep = json.loads(rep_bytes)
    prov = rep["provenance"]
    t.link("report", "the report hashes to its REPORT# ref, and binds this request, PDF, composition and evidence",
           sha(rep_bytes) == rep_row["ref"]["sha256"] == rep_ref["sha256"]
           and rep["request_ref"]["request_id"] == a.request_id
           and prov["pdf_ref"]["sha256"] == pdf_ref["sha256"]
           and prov["composition_ref"]["sha256"] == comp_ref["sha256"]
           and prov["extraction_evidence_ref"]["sha256"] == pub["certification_sha256"],
           report_id=rep_ref["report_id"], sha256=rep_ref["sha256"][:16])
    t.link("report", "the report's owner cites the original upload",
           rep["owner"]["prospect_input_id"] == upload_id, prospect_input_id=upload_id[:20])
    sections = rep["report"]["sections"]
    checked, matched, misses = reread_sections(pdf_bytes, sections)
    dates = {}
    for s in sections:
        dates[s.get("as_of_date")] = dates.get(s.get("as_of_date"), 0) + 1
    t.link("sections", "every scalar section's value is printed at its own page and coordinates in the retained PDF",
           checked > 0 and matched == checked, reread="%d/%d" % (matched, checked), sections=len(sections),
           charts=len(sections) - checked, misses=misses[:5], as_of_dates=dates)

    # 6. What this tool cannot measure.
    t.not_evaluated("screen", "the portal renders these sections for this report revision, and a reload keeps them",
                    "2.0.0_SA_COO~D's K10 walk on %s" % rep_ref["report_id"])
    t.not_evaluated("export", "the same-revision export carries these sections", "window 16 (K7 + K8 export), 2.0.0_SA_COO~P")

    verdicts = [link["verdict"] for link in t.links]
    summary = {"tenant": a.tenant, "request_id": a.request_id, "revision": a.revision, "report_id": rep_ref["report_id"],
               "links": len(verdicts), "match": verdicts.count("MATCH"), "mismatch": verdicts.count("MISMATCH"),
               "not_evaluated": verdicts.count("NOT_EVALUATED")}
    print("\nRESULT:", json.dumps(summary))
    if a.out:
        json.dump({"summary": summary, "links": t.links}, open(a.out, "w", encoding="utf-8"), indent=1, default=str)
        print("WROTE", a.out)
    return 1 if summary["mismatch"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

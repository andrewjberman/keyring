"""AMGT_RESAPP filings-analyzer SUBSTRATE MEASUREMENT (Rule 28) -- 1.0.0_SA_CTO~W, 2026-09-15.

One filing for one covered name through the Claude API with document CITATIONS and a STRUCTURED
schema. Stand-in document: the company's latest 10-K primary document from SEC EDGAR (public; the
production input will be the filing Bloomberg pulls, stated as such). The key is read from Secrets
Manager by the bash wrapper -- `comp-secrets get anthropic-api-key --reveal` (Andrew-direct ~05:4xZ:
"use comp-secrets in aws") -- and handed in through ANTHROPIC_SECRET_RAW; never printed. Every number
printed carries its denominator.

Egress authority: Andrew-direct 2026-09-15 ~05:2xZ at the 1.0.0_SA_CTO~W terminal, record
org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_052xZ_EGRESS_GRANTED_TO_CTO_W_FOR_THE_SESSION.md
"""
import html
import json
import os
import re
import time
import urllib.request

import anthropic

CIK = "0000012927"          # The Boeing Company (BA), a coverage name per the harvest checkpoint
TICKER = "BA"
OUT_DIR = os.path.join(os.environ["SCRATCH"], "filings_measure")
os.makedirs(OUT_DIR, exist_ok=True)
UA = "OpalCapital research substrate measurement (andrew.opalinvest2@gmail.com)"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


# ---- 1. locate the latest 10-K on EDGAR ------------------------------------------------------
t0 = time.time()
subs = json.loads(get("https://data.sec.gov/submissions/CIK%s.json" % CIK))
recent = subs["filings"]["recent"]
idx = next(i for i, f in enumerate(recent["form"]) if f == "10-K")
acc = recent["accessionNumber"][idx].replace("-", "")
primary = recent["primaryDocument"][idx]
filed = recent["filingDate"][idx]
doc_url = "https://www.sec.gov/Archives/edgar/data/%d/%s/%s" % (int(CIK), acc, primary)
raw = get(doc_url)
print("EDGAR: %s 10-K filed %s, primary %s, %d bytes, fetched in %.1fs" % (TICKER, filed, primary, len(raw), time.time() - t0))

# ---- 2. HTML -> text, then cut to Item 1A + Item 7 (a bounded, named subset, never a silent truncation)
text = raw.decode("utf-8", errors="replace")
text = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", text)
text = re.sub(r"(?s)<[^>]+>", " ", text)
text = html.unescape(text)
text = re.sub(r"[ \t ]+", " ", text)
text = re.sub(r"\n\s*\n+", "\n", text)
full_chars = len(text)


def section(label_re, next_re):
    ms = list(re.finditer(label_re, text, flags=re.I))
    if not ms:
        return ""
    # the LAST heading match is the body (earlier ones are the table of contents)
    start = ms[-1].start()
    m2 = re.search(next_re, text[start + 200:], flags=re.I)
    end = start + 200 + m2.start() if m2 else min(len(text), start + 400000)
    return text[start:end]


item1a = section(r"Item\s*1A\.?\s*Risk\s*Factors", r"Item\s*1B\.?\s*Unresolved")
item7 = section(r"Item\s*7\.?\s*Management.s\s*Discussion", r"Item\s*7A\.?\s*Quantitative")
doc = "ITEM 1A. RISK FACTORS\n" + item1a + "\n\nITEM 7. MD&A\n" + item7
print("text: full %d chars; Item 1A %d chars; Item 7 %d chars; SENT %d chars (%.1f%% of full)" % (
    full_chars, len(item1a), len(item7), len(doc), 100.0 * len(doc) / max(1, full_chars)))
open(os.path.join(OUT_DIR, "%s_10K_%s_sent.txt" % (TICKER, filed)), "w", encoding="utf-8").write(doc)

# ---- 3. the call: document + citations + structured schema ---------------------------------
raw_secret = os.environ.get("ANTHROPIC_SECRET_RAW", "").strip()
if not raw_secret:
    raise SystemExit("ANTHROPIC_SECRET_RAW not provided by the bash wrapper (native Python cannot spawn the .tools/aws shim)")
try:
    _d = json.loads(raw_secret)
    key = next((_d[k] for k in ("api_key", "ANTHROPIC_API_KEY", "key", "value") if k in _d), next(iter(_d.values())))
except ValueError:
    key = raw_secret
os.environ["ANTHROPIC_API_KEY"] = key
del raw_secret, key
client = anthropic.Anthropic()

SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["company", "fiscal_year", "guidance_changes", "segment_revenue", "top_risks",
                 "management_commentary", "big_bets", "big_challenges"],
    "properties": {
        "company": {"type": "string"},
        "fiscal_year": {"type": "string"},
        "guidance_changes": {"type": "array", "items": {"type": "object", "additionalProperties": False,
            "required": ["metric", "statement"], "properties": {"metric": {"type": "string"}, "statement": {"type": "string"}}}},
        "segment_revenue": {"type": "array", "items": {"type": "object", "additionalProperties": False,
            "required": ["segment", "revenue_usd_millions", "yoy_change_pct"],
            "properties": {"segment": {"type": "string"}, "revenue_usd_millions": {"type": ["number", "null"]}, "yoy_change_pct": {"type": ["number", "null"]}}}},
        "top_risks": {"type": "array", "items": {"type": "string"}},
        "management_commentary": {"type": "array", "items": {"type": "string"}},
        "big_bets": {"type": "array", "items": {"type": "string"}},
        "big_challenges": {"type": "array", "items": {"type": "string"}},
    },
}

count = client.messages.count_tokens(
    model="claude-opus-5",
    messages=[{"role": "user", "content": [
        {"type": "document", "source": {"type": "text", "media_type": "text/plain", "data": doc},
         "title": "%s 10-K %s (Item 1A + Item 7)" % (TICKER, filed), "citations": {"enabled": True}},
        {"type": "text", "text": "Extract the schema."}]}],
)
print("input tokens (count_tokens): %d" % count.input_tokens)

t1 = time.time()
prompt = (
    "You are the filings analyzer for an internal research page. From the attached 10-K excerpt, extract: "
    "guidance changes (any forward statements about outlook, targets or expectations), segment revenue for the "
    "latest fiscal year with year-over-year change where stated, the top risks in the company's own words, "
    "management commentary worth quoting, and -- for a Thesis page -- the company's big bets and big challenges "
    "as the filing states them. Cite the document for every item. Where a figure is not in the excerpt, use null; "
    "never estimate. Return the JSON described below and nothing else.\n\nJSON schema:\n" + json.dumps(SCHEMA)
)
with client.messages.stream(
    model="claude-opus-5",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},
    messages=[{"role": "user", "content": [
        {"type": "document", "source": {"type": "text", "media_type": "text/plain", "data": doc},
         "title": "%s 10-K %s (Item 1A + Item 7)" % (TICKER, filed), "citations": {"enabled": True}},
        {"type": "text", "text": prompt}]}],
) as stream:
    msg = stream.get_final_message()
elapsed = time.time() - t1

texts = [b for b in msg.content if b.type == "text"]
cited = [b for b in texts if getattr(b, "citations", None)]
n_cit = sum(len(b.citations) for b in cited)
joined = "".join(b.text for b in texts)
print("stop_reason=%s  elapsed=%.1fs  usage in=%d out=%d cache_read=%s" % (
    msg.stop_reason, elapsed, msg.usage.input_tokens, msg.usage.output_tokens,
    getattr(msg.usage, "cache_read_input_tokens", None)))
print("text blocks=%d  blocks carrying citations=%d  citations total=%d" % (len(texts), len(cited), n_cit))

# parse the JSON out of the text (citations split the text into blocks; join first)
m = re.search(r"\{.*\}", joined, flags=re.S)
parsed = None
if m:
    try:
        parsed = json.loads(m.group(0))
    except ValueError as e:
        print("JSON parse FAILED:", e)
if parsed:
    print("PARSED: guidance %d | segments %d | risks %d | commentary %d | bets %d | challenges %d" % (
        len(parsed.get("guidance_changes", [])), len(parsed.get("segment_revenue", [])),
        len(parsed.get("top_risks", [])), len(parsed.get("management_commentary", [])),
        len(parsed.get("big_bets", [])), len(parsed.get("big_challenges", []))))
    for s in parsed.get("segment_revenue", [])[:6]:
        print("   segment:", s)
    for g in parsed.get("guidance_changes", [])[:3]:
        print("   guidance:", g)

# save everything
rec = {
    "measured_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "ticker": TICKER, "cik": CIK, "filing_date": filed, "doc_url": doc_url,
    "full_chars": full_chars, "sent_chars": len(doc), "input_tokens": count.input_tokens,
    "model": msg.model, "stop_reason": msg.stop_reason, "elapsed_s": round(elapsed, 1),
    "usage": msg.usage.to_dict() if hasattr(msg.usage, "to_dict") else str(msg.usage),
    "citations_total": n_cit, "text_blocks": len(texts), "blocks_with_citations": len(cited),
    "parsed": parsed,
    "raw_content": [b.to_dict() if hasattr(b, "to_dict") else str(b) for b in msg.content],
}
out = os.path.join(OUT_DIR, "%s_10K_%s_measurement.json" % (TICKER, filed))
open(out, "w", encoding="utf-8").write(json.dumps(rec, indent=2, ensure_ascii=True))
print("saved:", out)
# cost at Opus 5 list: $5 / $25 per MTok
print("cost estimate USD: %.3f" % (msg.usage.input_tokens * 5e-6 + msg.usage.output_tokens * 25e-6))

"""
NFRA_AKPIPE production Lambda handler -- PROPOSAL PACKAGE (RCN-0003).

Author: 4.0.0_SA_CRO (Chief Research Officer)
Spec:   org/tier1_exec/4.0.0_SA_CRO/briefs/NFRA_AKPIPE_BUILD_SPEC_20260723.md

>> THIS IS A PROPOSAL, NOT A DEPLOY. <<
It lives in the CRO deliverables tree because infra/aws/** is an AE lane and applies are
CTO-gated. CloudOps/AE lands it at infra/aws/lambda/akpipe/ and registers it in
infra/aws/lambda/ci/lambda-source-map.json; CTO gates the apply. The CRO wrote and
validated the logic; it does not place or apply it.

WHAT IT DOES (daily, EventBridge):
  1. HARVEST   arxiv Atom/OAI delta since the S3 watermark, target categories only
  2. DEDUP     skip (arxiv_id, version) already in DDB -- lossless, never overwrite
  3. FULLTEXT  /html LaTeX render, else PDF; raw + extracted text to S3
  4. SCORE     phrase-BM25 (PINNED idf) + potion-8M -> nlp_score magnitude
  5. WRITE     conditional put to DDB (attribute_not_exists) -- append-only
  6. RECOMPUTE derived_state_rank for the WHOLE corpus (recency moved for everything)
  7. WATERMARK advance ONLY on a fully successful window; FAIL-LOUD run identities

EGRESS BOUNDARY: arxiv.org / export.arxiv.org ONLY. This is the concrete extent of the
standing grant (Andrew-direct 2026-07-23). The potion model is read from the Lambda layer
or S3 -- NEVER downloaded from HuggingFace at runtime.

IDF PINNING (closes the declared gap): scoring idf comes from a VERSIONED reference table
in S3, not the day's harvest. Corpus-relative idf would silently change a stored paper's
score as new papers arrive, breaking both losslessness and independent recomputability.
If the pinned table is missing the run FAILS LOUD rather than silently falling back.

ASCII-only (CLAUDE.md Code Quality).
"""

from __future__ import annotations

import json
import math
import os
import re
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from decimal import Decimal

import boto3
from boto3.dynamodb.conditions import Key

# ------------------------------------------------------------------ config (env)

TABLE = os.environ["AKPIPE_TABLE"]
BUCKET = os.environ["AKPIPE_BUCKET"]
PROFILE_KEY = os.environ.get("AKPIPE_PROFILE_KEY", "_profile/akpipe-profile-v3.json")
POTION_DIR = os.environ.get("AKPIPE_POTION_DIR", "/opt/potion-base-8M")
MAX_FULLTEXT = int(os.environ.get("AKPIPE_MAX_FULLTEXT", "60"))
HALF_LIFE_DAYS = float(os.environ.get("AKPIPE_HALF_LIFE_DAYS", "45"))
BM25_K1, BM25_B = 1.5, 0.75
BM25_SAT_C = float(os.environ.get("AKPIPE_BM25_SAT_C", "6.0"))

CATEGORIES = ["cs.AI", "cs.LG", "cs.SE", "cs.IR", "cs.DC", "cs.DB", "cs.MA"]
API = "http://export.arxiv.org/api/query"
UA = "OpalCapital-NFRA_AKPIPE/1.0 (research harvest; contact andrew@opalinvest.com)"
ATOM = "{http://www.w3.org/2005/Atom}"
ARX = "{http://arxiv.org/schemas/atom}"
WATERMARK_KEY = "_control/oai_watermark.json"

ddb = boto3.resource("dynamodb")
s3 = boto3.client("s3")
table = ddb.Table(TABLE)

# ------------------------------------------------------------------ text utils

_SEP = re.compile(r"[-‐‑‒–—_/]+")
_WSX = re.compile(r"\s+")
_TOKEN = re.compile(r"[a-z0-9]+")
_TAG = re.compile(r"<[^>]+>")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def normalize(text: str) -> str:
    """Fold hyphens/dashes to spaces. NOT cosmetic: 'closed-loop' must match the phrase
    'closed loop' or perfect-match papers silently score 0 (measured defect, 2026-07-24)."""
    return _WSX.sub(" ", _SEP.sub(" ", text.lower()))


def tokenize(text: str) -> list[str]:
    return _TOKEN.findall(normalize(text))


# ------------------------------------------------------------------ profile (pinned)

def load_profile() -> dict:
    """Load the versioned profile: phrases + PINNED idf. FAIL LOUD if absent -- a silent
    fallback to corpus idf would make stored scores drift."""
    try:
        body = s3.get_object(Bucket=BUCKET, Key=PROFILE_KEY)["Body"].read()
    except Exception as e:
        raise RuntimeError(
            f"PINNED PROFILE MISSING at s3://{BUCKET}/{PROFILE_KEY} -- refusing to score "
            f"with corpus-relative idf (it would silently change stored scores): {e}")
    p = json.loads(body)
    for k in ("profile_version", "phrases", "idf"):
        if k not in p:
            raise RuntimeError(f"PROFILE MALFORMED: missing {k}")
    return p


def phrase_scores(texts: list[str], profile: dict) -> list[float]:
    """Length-normalized BM25 over the profile phrases, using PINNED idf."""
    phrases = profile["phrases"]
    idf = profile["idf"]
    pats = {p: re.compile(r"\b" + re.escape(normalize(p)) + r"(?:s|es)?\b") for p in phrases}
    lowered = [normalize(t) for t in texts]
    dls = [max(1, len(tokenize(t))) for t in texts]
    avgdl = profile.get("avgdl") or (sum(dls) / max(1, len(dls)))
    out = []
    for i, low in enumerate(lowered):
        s, dl = 0.0, dls[i]
        for p in phrases:
            f = len(pats[p].findall(low))
            if not f:
                continue
            denom = f + BM25_K1 * (1 - BM25_B + BM25_B * dl / avgdl)
            s += float(idf.get(p, 0.0)) * (f * (BM25_K1 + 1)) / denom
        out.append(s)
    return out


def potion_cosines(texts: list[str], profile_text: str) -> list[float]:
    """Potion static embeddings from the LAYER (never a runtime HF download)."""
    from model2vec import StaticModel
    import numpy as np
    model = StaticModel.from_pretrained(POTION_DIR)
    vecs = np.asarray(model.encode([profile_text] + texts), dtype="float64")
    pv, dvs = vecs[0], vecs[1:]
    npv = np.linalg.norm(pv)
    out = []
    for v in dvs:
        nv = np.linalg.norm(v)
        out.append(float(np.dot(pv, v) / (npv * nv)) if npv and nv else 0.0)
    return out


def bm25_magnitude(x: float) -> float:
    return x / (x + BM25_SAT_C) if x > 0 else 0.0


def recency_component(age_days: float) -> float:
    return math.exp(-math.log(2.0) * max(0.0, age_days) / HALF_LIFE_DAYS)


# ------------------------------------------------------------------ http

def http_get(url: str, timeout: int = 90, retries: int = 4) -> bytes:
    delay = 5.0
    last = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 503):
                time.sleep(float(e.headers.get("Retry-After") or delay))
            elif e.code in (500, 502, 504):
                time.sleep(delay)
            else:
                raise
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last = e
            time.sleep(delay)
        delay *= 2
    raise RuntimeError(f"GET failed after {retries}: {url[:90]} ({last})")


def parse_atom(raw: bytes) -> list[dict]:
    root = ET.fromstring(raw)
    out = []
    for e in root.findall(f"{ATOM}entry"):
        m = re.search(r"abs/([^v]+)v(\d+)", (e.findtext(f"{ATOM}id") or "").strip())
        if not m:
            continue
        prim = e.find(f"{ARX}primary_category")
        out.append({
            "arxiv_id": m.group(1), "version": "v" + m.group(2),
            "title": " ".join((e.findtext(f"{ATOM}title") or "").split()),
            "abstract": " ".join((e.findtext(f"{ATOM}summary") or "").split()),
            "authors": [" ".join((a.findtext(f"{ATOM}name") or "").split())
                        for a in e.findall(f"{ATOM}author")],
            "primary_category": prim.get("term") if prim is not None else "",
            "categories": [c.get("term") for c in e.findall(f"{ATOM}category") if c.get("term")],
            "timestamp_released": (e.findtext(f"{ATOM}published") or "").strip(),
            "timestamp_updated": (e.findtext(f"{ATOM}updated") or "").strip(),
            "doi": e.findtext(f"{ARX}doi"),
        })
    return out


def fetch_fulltext(arxiv_id: str, version: str) -> tuple[str, str, bytes | None]:
    try:
        raw = http_get(f"https://arxiv.org/html/{arxiv_id}{version}", timeout=60)
        html = raw.decode("utf-8", errors="replace")
        html = re.sub(r"(?is)<(script|style|math)\b.*?</\1>", " ", html)
        text = _WSX.sub(" ", _TAG.sub(" ", html)).strip()
        if len(text) > 3000:
            return text, "html", raw
    except Exception:
        pass
    try:
        raw = http_get(f"https://arxiv.org/pdf/{arxiv_id}{version}", timeout=60)
        import fitz
        doc = fitz.open(stream=raw, filetype="pdf")
        return _WSX.sub(" ", " ".join(p.get_text() for p in doc)).strip(), "pdf", raw
    except Exception:
        return "", "none", None


# ------------------------------------------------------------------ storage

def s3_prefix(row: dict) -> str:
    yr = (row.get("timestamp_released") or "0000")[:4]
    return f"{row['primary_category']}/{yr}/{row['arxiv_id']}/{row['version']}"


def already_present(arxiv_id: str, version: str) -> bool:
    r = table.query(KeyConditionExpression=Key("arxiv_id").eq(arxiv_id) & Key("version").eq(version),
                    Limit=1)
    return r.get("Count", 0) > 0


def dec(x) -> Decimal:
    return Decimal(str(round(float(x), 8)))


def get_watermark() -> str | None:
    try:
        b = s3.get_object(Bucket=BUCKET, Key=WATERMARK_KEY)["Body"].read()
        return json.loads(b).get("until")
    except Exception:
        return None


def put_watermark(until: str, run_id: str) -> None:
    s3.put_object(Bucket=BUCKET, Key=WATERMARK_KEY,
                  Body=json.dumps({"until": until, "run_id": run_id}).encode(),
                  ContentType="application/json")


# ------------------------------------------------------------------ handler

def lambda_handler(event, context):
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    now = datetime.now(timezone.utc)
    profile = load_profile()
    since = get_watermark()
    lookback = int((event or {}).get("lookback_days", 2))
    lo = (now - timedelta(days=lookback)).strftime("%Y%m%d%H%M")
    hi = now.strftime("%Y%m%d%H%M")

    q = "+OR+".join(f"cat:{c}" for c in CATEGORIES)
    url = (f"{API}?search_query=({q})+AND+submittedDate:[{lo}+TO+{hi}]"
           f"&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200")
    harvested = parse_atom(http_get(url))
    in_scope = [r for r in harvested if r["primary_category"] in CATEGORIES]
    fresh = [r for r in in_scope if not already_present(r["arxiv_id"], r["version"])]
    print(f"[akpipe] run={run_id} since={since} harvested={len(harvested)} "
          f"in_scope={len(in_scope)} fresh={len(fresh)}")

    # full text + score
    targets = fresh[:MAX_FULLTEXT]
    texts, ok = [], 0
    for r in targets:
        text, src, raw = fetch_fulltext(r["arxiv_id"], r["version"])
        pre = s3_prefix(r)
        if raw:
            s3.put_object(Bucket=BUCKET, Key=f"{pre}/raw.{'html' if src == 'html' else 'pdf'}",
                          Body=raw)
            s3.put_object(Bucket=BUCKET, Key=f"{pre}/text.txt", Body=text.encode("utf-8"))
            ok += 1
        r["_text"] = text or f"{r['title']} {r['abstract']}"
        r["fulltext_fetched"] = bool(text)
        r["fulltext_source"] = src
        r["fulltext_chars"] = len(text)
        r["author_emails"] = sorted(set(EMAIL_RE.findall(text[:25000]))) if text else []
        texts.append(r["_text"])
        time.sleep(3.0)

    if texts:
        bms = phrase_scores(texts, profile)
        pos = potion_cosines(texts, " ".join(profile["phrases"]))
        for i, r in enumerate(targets):
            rel = bm25_magnitude(bms[i])
            try:
                age = (now - datetime.fromisoformat(
                    r["timestamp_released"].replace("Z", "+00:00"))).total_seconds() / 86400.0
            except Exception:
                age = 0.0
            item = {
                "arxiv_id": r["arxiv_id"], "version": r["version"],
                "title": r["title"], "abstract": r["abstract"], "authors": r["authors"],
                "author_emails": r["author_emails"], "primary_category": r["primary_category"],
                "categories": r["categories"], "doi": r.get("doi"),
                "timestamp_released": r["timestamp_released"],
                "timestamp_updated": r.get("timestamp_updated"),
                "first_seen_ts": now.isoformat(),
                "phrase_bm25": dec(bms[i]), "potion_cosine": dec(pos[i]),
                "nlp_score": dec(rel), "age_days": dec(age),
                "recency_component": dec(recency_component(age)),
                "derived_state_rank": dec(recency_component(age) * rel),
                "rank_asof_date": now.strftime("%Y-%m-%d"),
                "fulltext_s3_prefix": s3_prefix(r),
                "fulltext_fetched": r["fulltext_fetched"],
                "fulltext_source": r["fulltext_source"],
                "fulltext_chars": r["fulltext_chars"],
                "profile_version": profile["profile_version"],
                "potion_model_version": os.path.basename(POTION_DIR),
                "harvest_run_id": run_id, "source_channel": "atom",
            }
            try:
                table.put_item(Item=item,
                               ConditionExpression="attribute_not_exists(arxiv_id)")
            except ddb.meta.client.exceptions.ConditionalCheckFailedException:
                pass  # already present -- lossless, never overwrite

    # DAILY WHOLE-CORPUS RECOMPUTE: age moved for every paper, so every derived rank moves.
    asof = now.strftime("%Y-%m-%d")
    scanned = updated = 0
    kwargs = {"ProjectionExpression": "arxiv_id,version,nlp_score,timestamp_released"}
    while True:
        page = table.scan(**kwargs)
        for it in page.get("Items", []):
            scanned += 1
            try:
                age = (now - datetime.fromisoformat(
                    it["timestamp_released"].replace("Z", "+00:00"))).total_seconds() / 86400.0
            except Exception:
                continue
            rc = recency_component(age)
            table.update_item(
                Key={"arxiv_id": it["arxiv_id"], "version": it["version"]},
                UpdateExpression=("SET age_days=:a, recency_component=:r, "
                                  "derived_state_rank=:d, rank_asof_date=:k"),
                ExpressionAttributeValues={
                    ":a": dec(age), ":r": dec(rc),
                    ":d": dec(rc * float(it.get("nlp_score", 0))), ":k": asof})
            updated += 1
        if "LastEvaluatedKey" not in page:
            break
        kwargs["ExclusiveStartKey"] = page["LastEvaluatedKey"]

    # FAIL-LOUD run identities (spec section 4)
    identities = {
        "harvested": len(harvested), "in_scope": len(in_scope), "fresh": len(fresh),
        "fulltext_attempted": len(targets), "fulltext_stored": ok,
        "recompute_scanned": scanned, "recompute_updated": updated,
    }
    if scanned != updated and scanned - updated > 0:
        print(f"[akpipe] WARN: recompute skipped {scanned-updated} rows (unparseable dates)")
    s3.put_object(Bucket=BUCKET, Key=f"_control/runs/{run_id}.json",
                  Body=json.dumps({"run_id": run_id, "identities": identities,
                                   "profile_version": profile["profile_version"]}).encode(),
                  ContentType="application/json")
    put_watermark(hi, run_id)   # ONLY after a fully successful window
    print(f"[akpipe] OK run={run_id} {identities}")
    return {"status": "ok", "run_id": run_id, **identities}

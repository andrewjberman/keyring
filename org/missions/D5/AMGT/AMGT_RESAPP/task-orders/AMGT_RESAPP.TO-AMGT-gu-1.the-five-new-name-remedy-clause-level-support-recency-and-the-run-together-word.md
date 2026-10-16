# AMGT_RESAPP task order -- `AMGT-gu-1` -- THE FIVE-NEW-NAME REMEDY: CLAUSE-LEVEL SUPPORT, THE CROSS-BLOCK RECENCY RULE AND THE RUN-TOGETHER WORD (FWD-41 ROUND 109, CVO C-S158, CTO 6571; A DIRECT ACT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gu-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~483</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-gu-1.the-five-new-name-remedy-clause-level-support-recency-and-the-run-together-word</to_id>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; library modules and their tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the cell writes and tests local Python only.
comp-adversary: RUN at the cut -- `check_gu1_remedy.py` is a prepared acceptance check (20 arms); at the base it reads `AIFILL GU-1 ARMS: NO (8 of 20)`, the build check failing as expected, and the issuer's reference edit in a scratch copy reads 20 of 20 with the 813 existing aifill tests unchanged.
EGRESS CLASS, declared: NONE. No network call by the cell or its checks; no model call; no Bloomberg call.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-483` (branch `wk-AMGT_RESAPP-483`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-483`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-gu-1` (round 109, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md` section 17)

The AI-fill producer (`lib/research/aifill/`) builds one fill document of five blocks per security; each text block's sentences are checked against its cited sources by `grounding.py`, and the orchestrator (`orchestrate.py`) grounds every block. An independent reader found three defects in 12 stored blocks; each is a mechanism, and this cell closes all three. Behaviour not listed here is unchanged.

1. **Clause-level support (`grounding.py`).** A sentence a model marks SUPPORTED on a quote of only its first clause was kept although the rest of it (a `$3 billion` raise with `Apollo` and `Temasek`) is in no source. New rule, mechanical, no model call: a SUPPORTED verdict stands only when the cited source's normalised full text carries, as whole words, every number (with a following scale word) and every capitalised name (four letters or more, less a stop list) that the sentence states. One missing and the sentence is recorded UNSUPPORTED (same record shape) and is not kept.
2. **Cross-block recency (`grounding.py`, `orchestrate.py`).** A sentence in a management block may be true of an older page and contradicted by a newer page that ANOTHER block of the same document cites. New: `ground_block` takes an optional `reference` list of further sources shown after the block's own; a reference source can make a sentence CONTRADICTED but never SUPPORTED. After all five blocks are built, `build_document` re-checks each WEB_SEARCH management block (`mgmt_bio`, `mgmt_recent`, `mgmt_team_view`) once against its own pages plus up to four pages cited by the other web blocks; a sentence found CONTRADICTED is dropped and its record names the contradicting page index and quote; no sentence left gives a NONE block with a plain reason; a recency check that cannot run (the model call fails or answers nothing usable) withholds the text. `build_document(..., recency=True)` is the switch, default on.
3. **The run-together word (`contract.py`).** `fold_text` drops a non-ASCII character that is not a letter, so a zero-width space between two words printed them joined (`Pettigrewafter`) and a non-breaking hyphen turned `co-founder` into `cofounder`. New: U+2010, U+2011, U+2012 and U+2212 fold to a hyphen; a dropped non-letter standing between two ASCII alphanumerics becomes one space, except the characters that join a word (U+00AD, U+200C, U+200D, U+2060, U+FEFF).

### The change, exactly (this diff against the base is the specification; apply it, do not improvise a different design)

```diff
diff --git a/lib/research/aifill/contract.py b/lib/research/aifill/contract.py
index d85c2eef34..84df7e0a43 100644
--- a/lib/research/aifill/contract.py
+++ b/lib/research/aifill/contract.py
@@ -57,7 +57,13 @@ _CHAR_MAP = (
     ("\u00a3", "GBP "),
     ("\u00a5", "JPY "),
     ("\u00d7", "x"),
+    ("\u2010", "-"),
+    ("\u2011", "-"),
+    ("\u2012", "-"),
+    ("\u2212", "-"),
 )
+# Characters dropped with no space even between two letters (they join, never separate, a word).
+_SILENT_DROPS = frozenset("\u00ad\u200c\u200d\u2060\ufeff")
 # Letters that Unicode decomposition cannot turn into ASCII; applied before NFKD.
 _LETTER_MAP = (
     ("\u00df", "ss"),
@@ -134,11 +140,15 @@ def fold_report(text):
     out = "".join(ch for ch in unicodedata.normalize("NFKD", out) if unicodedata.category(ch) != "Mn")
     kept = []
     dropped = []
-    for ch in out:
+    for i, ch in enumerate(out):
         if ord(ch) < 128:
             kept.append(ch)
-        else:
-            dropped.append(ch)
+            continue
+        dropped.append(ch)
+        # A dropped non-letter between two ASCII alphanumerics stood between two words: leave a space, not a run-together word.
+        if (ch not in _SILENT_DROPS and not unicodedata.category(ch).startswith("L") and kept and kept[-1].isalnum()
+                and i + 1 < len(out) and ord(out[i + 1]) < 128 and out[i + 1].isalnum()):
+            kept.append(" ")
     return "".join(kept), dropped
 
 
diff --git a/lib/research/aifill/grounding.py b/lib/research/aifill/grounding.py
index f70abcdcdc..cc954e28ec 100644
--- a/lib/research/aifill/grounding.py
+++ b/lib/research/aifill/grounding.py
@@ -70,6 +70,38 @@ def _norm(text):
     return re.sub(r"[\W_]+", " ", text.lower()).strip()
 
 
+_NUMBER = re.compile(r"(?<![A-Za-z0-9.,])[0-9][0-9,]*(?:\.[0-9]+)?(?:\s*(?:billion|million|trillion|thousand|bn|mn|percent|%))?", re.IGNORECASE)
+_NAME = re.compile(r"[A-Z][a-z]{3,}")
+# Capitalised words that are not names: sentence openers, months, weekdays and the common words of a job title.
+_NOT_NAMES = frozenset((
+    "after before during since under while also both most many several this that these those with from into over upon "
+    "their there then they them when where which whose what who january february march april june july august september "
+    "october november december monday tuesday wednesday thursday friday saturday sunday chief officer board director "
+    "directors executive president vice group chairman managing supervisory independent senior general company member "
+    "members committee prior currently previously formerly recently"
+).split())
+
+
+def _specifics(sent_text):
+    """What a sentence states that a source must carry: its numbers (with a following scale word) and its capitalised names."""
+    found = []
+    for match in _NUMBER.finditer(sent_text):
+        spec = _norm(match.group(0))
+        if spec and spec not in found:
+            found.append(spec)
+    for match in _NAME.finditer(sent_text):
+        spec = match.group(0).lower()
+        if spec not in _NOT_NAMES and spec not in found:
+            found.append(spec)
+    return found
+
+
+def _missing_specifics(sent_text, norm_text):
+    """The specifics of the sentence that the (normalised) source text does not carry as whole words."""
+    padded = " " + norm_text + " "
+    return [spec for spec in _specifics(sent_text) if (" " + spec + " ") not in padded]
+
+
 def _stamp(now):
     if isinstance(now, datetime.datetime):
         if now.tzinfo is not None:
@@ -159,8 +191,10 @@ def _unsupported(sent_text):
     return {"text": sent_text, "verdict": "UNSUPPORTED", "source": None, "quote": None}
 
 
-def _judge(row, sent_text, usable, norm_full):
-    """The sentence record for one verdict row: SUPPORTED only when the source is shown and the quote is in its full text."""
+def _judge(row, sent_text, usable, norm_full, own_n):
+    """The sentence record for one verdict row: SUPPORTED only when an own source is shown, the quote is in its full text
+    and the source carries every number and name the sentence states (round 109 clause check). A reference source can
+    contradict a sentence but never support it."""
     verdict = row.get("verdict")
     if verdict == "CONTRADICTED":
         k = _shown_index(row.get("source"), len(usable))
@@ -177,23 +211,26 @@ def _judge(row, sent_text, usable, norm_full):
     if k is None or not isinstance(quote, str) or len(quote) < MIN_QUOTE:
         return _unsupported(sent_text)
     nq = _norm(quote)
-    if not nq or nq not in norm_full[k - 1]:
+    if not nq or nq not in norm_full[k - 1] or usable[k - 1]["index"] >= own_n:
+        return _unsupported(sent_text)
+    if _missing_specifics(sent_text, norm_full[k - 1]):
         return _unsupported(sent_text)
     return {"text": sent_text, "verdict": "SUPPORTED", "source": usable[k - 1]["index"], "quote": quote}
 
 
-def _ground(text, sources, model, now, max_window_chars):
+def _ground(text, sources, model, now, max_window_chars, reference=None):
     stamp = _stamp(now)
     if not isinstance(text, str):
         text = ""
     sent_texts = sentences_module.split_sentences(text)
-    source_records, usable = _prepare_sources(list(sources or []))
+    own_n = len(list(sources or []))
+    source_records, usable = _prepare_sources(list(sources or []) + list(reference or []))
     model_call = None
     error = None
     verdict_rows = None
     if not sent_texts:
         error = "no sentence"
-    elif not usable:
+    elif not any(src["index"] < own_n for src in usable):
         error = "no usable source"
     else:
         prompt = _prompt(usable, sent_texts, max_window_chars)
@@ -230,7 +267,7 @@ def _ground(text, sources, model, now, max_window_chars):
         if row is None:
             sentence_records.append(_unsupported(sent))
         else:
-            sentence_records.append(_judge(row, sent, usable, norm_full))
+            sentence_records.append(_judge(row, sent, usable, norm_full, own_n))
 
     kept = [rec for rec in sentence_records if rec["verdict"] == "SUPPORTED"]
     used_urls = []
@@ -255,9 +292,12 @@ def _failed(text, now, error):
     return GroundResult(False, "", [], record, [], [], error)
 
 
-def ground_block(text, sources, model, now, max_window_chars=DEFAULT_WINDOW):
-    """Ground a block's text against its sources through one model call; never raises (see the module docstring)."""
+def ground_block(text, sources, model, now, max_window_chars=DEFAULT_WINDOW, reference=None):
+    """Ground a block's text against its sources through one model call; never raises (see the module docstring).
+
+    reference: further sources (other blocks' cited pages) shown after the block's own; they can make a sentence
+    CONTRADICTED but never SUPPORTED, and their entries follow the own sources in the record."""
     try:
-        return _ground(text, sources, model, now, max_window_chars)
+        return _ground(text, sources, model, now, max_window_chars, reference)
     except Exception as exc:  # noqa: BLE001 -- the pass never raises; a failure is a result
         return _failed(text, now, "grounding failed: %s: %s" % (type(exc).__name__, str(exc)[:200]))
diff --git a/lib/research/aifill/orchestrate.py b/lib/research/aifill/orchestrate.py
index bfbdbbc6f6..dcdb306e3e 100644
--- a/lib/research/aifill/orchestrate.py
+++ b/lib/research/aifill/orchestrate.py
@@ -26,6 +26,10 @@ INTERNAL_FAILED = "This block could not be produced (an internal error: %s)."
 GROUNDING_REASON = "None of the model's statements could be confirmed in a source that answered, so the text was withheld."
 MESSAGE_CUT = 160
 FETCH_CAP = 8
+RECENCY_BLOCKS = ("mgmt_bio", "mgmt_recent", "mgmt_team_view")
+REFERENCE_CAP = 4
+RECENCY_REASON = "A newer source cited elsewhere on this page contradicts the model's statements, so the text was withheld."
+RECENCY_UNCHECKED = "The text could not be checked against the other sources cited on this page, so it was withheld."
 
 
 class BlockContext(object):
@@ -203,12 +207,64 @@ def _build_one(block_id, ctx, builders, ground):
     return draft
 
 
+def _reference_sources(block_id, blocks, own_urls, fetch):
+    """The pages cited by the OTHER web blocks of the document (not this block's own), fetched through the document cache."""
+    urls = []
+    for other_id in contract.BLOCK_IDS:
+        other = blocks[other_id]
+        if other_id == block_id or other.get("source_class") != "WEB_SEARCH":
+            continue
+        for cite in other["citations"]:
+            url = cite.get("url")
+            if cite.get("source_kind") == "web" and url not in own_urls and url not in urls:
+                urls.append(url)
+    return [_fetched(url, fetch) for url in urls[:REFERENCE_CAP]]
+
+
+def _recency_block(block_id, blocks, ctx):
+    """The block after the cross-block recency check (round 109): a sentence that a page cited by another block of the
+    same document contradicts is dropped and its record keeps the contradicting source and quote. A block with nothing
+    to check is returned as it is; a check that cannot run withholds the text. Never raises."""
+    block = blocks[block_id]
+    record = block.get("grounding")
+    if block.get("source_class") != "WEB_SEARCH" or not isinstance(record, dict) or not block.get("text"):
+        return block
+    try:
+        own_urls = [src.get("url") for src in record["sources"]]
+        reference = _reference_sources(block_id, blocks, set(own_urls), ctx.fetch)
+        if not reference:
+            return block
+        own = [_fetched(url, ctx.fetch) for url in own_urls]
+        result = grounding.ground_block(block["text"], own, ctx.model, ctx.now, reference=reference)
+        if result.error is not None and not result.kept:
+            return contract.none_block(block_id, RECENCY_UNCHECKED)
+        contradicted = {rec["text"]: rec for rec in result.record["sentences"] if rec["verdict"] == "CONTRADICTED"}
+        if not contradicted:
+            return block
+        sentences = [contradicted.get(rec["text"], rec) for rec in record["sentences"]]
+        kept = [rec for rec in sentences if rec["verdict"] == "SUPPORTED"]
+        if not kept:
+            return contract.none_block(block_id, RECENCY_REASON)
+        used = set(result.record["sources"][rec["source"]]["url"] for rec in kept)
+        call, extra = record["model_call"], result.record["model_call"]
+        if isinstance(call, dict) and isinstance(extra, dict):
+            call = {"model": call["model"], "input_tokens": (call["input_tokens"] or 0) + (extra["input_tokens"] or 0),
+                    "output_tokens": (call["output_tokens"] or 0) + (extra["output_tokens"] or 0)}
+        new_record = dict(record, sources=result.record["sources"], sentences=sentences, model_call=call)
+        cites = [cite for cite in block["citations"] if cite.get("url") in used]
+        return contract.make_block(block_id, "WEB_SEARCH", " ".join(rec["text"] for rec in kept), cites, block["opal_inputs"],
+                                   block["model_call"], grounding=new_record, require_grounding=True)
+    except Exception:  # noqa: BLE001 -- a recency check that cannot be stored withholds the text
+        return contract.none_block(block_id, RECENCY_UNCHECKED)
+
+
 def build_document(security_key, inputs, model, now: Optional[datetime.datetime] = None,
-                   builders: Optional[dict] = None, fetch=None, ground: bool = True) -> dict:
+                   builders: Optional[dict] = None, fetch=None, ground: bool = True, recency: bool = True) -> dict:
     """Assemble one fill document for a security key; the result always passes contract.validate_document.
 
     fetch is the url fetcher (the shape of sources.fetch_source), wrapped in a per-document cache and handed to every
     builder's context. ground true runs the grounding step on every filled draft; false stores drafts as they are.
+    recency true (with ground) then checks each web management block against the pages the other blocks cite.
     """
     stamp = _utc(now)
     fetch_once = _cached_fetch(fetch)
@@ -216,6 +272,10 @@ def build_document(security_key, inputs, model, now: Optional[datetime.datetime]
     for block_id in contract.BLOCK_IDS:
         ctx = BlockContext(security_key, inputs, model, stamp, fetch=fetch_once)
         blocks[block_id] = _build_one(block_id, ctx, builders, bool(ground))
+    if ground and recency:
+        ctx = BlockContext(security_key, inputs, model, stamp, fetch=fetch_once)
+        for block_id in RECENCY_BLOCKS:
+            blocks[block_id] = _recency_block(block_id, blocks, ctx)
     doc = {
         "schema": contract.SCHEMA,
         "security_key": security_key,
```

### Tests (a new module `lib/research/aifill/tests/test_gu1_remedy.py`, no `__init__.py`)
At least TWELVE tests, offline (stub model, stub fetcher; follow the helpers in `lib/research/aifill/tests/test_orchestrate_grounding.py`): the four folds (zero-width space gives a space; U+2011 gives a hyphen; soft hyphen and U+200D join silently; a symbol between spaces still drops with no extra space); a SUPPORTED verdict on a first-clause quote is recorded UNSUPPORTED when the sentence's number and names are absent from the source; the same sentence with all of them present stays SUPPORTED; a number that differs (`$3 billion` against `$30 billion`) is UNSUPPORTED; the digit inside `CET1` is not a number to carry; a reference source CONTRADICTED verdict records index 1 and the quote; a SUPPORTED verdict on a reference source is UNSUPPORTED; the record lists the own source first and the reference after; and the document-level behaviour: a stale sentence dropped (text, record, citations and summed token count), all sentences dropped gives the `RECENCY_REASON` NONE block, `recency=False` makes no extra call, no other web block makes no extra call, a failing recency call gives the `RECENCY_UNCHECKED` NONE block. Do NOT edit an existing test file: the 813 existing aifill tests pass unchanged with this change, and one that does not is a finding to file as a row, not to fix.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W483-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS

1. Write ONLY the files in the `<paths>` block below. `run.py`, `store.py`, `revalidate.py`, `sources.py`, `sentences.py`, `validation.py`, the block builders and every other module are other cells'.
- No network, no AWS, no real model call, no `pip install`.
- Python 3.9 syntax; ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes, as the diff does); stdlib only.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.
- Your sparse worktree may lack a folder a test reads; the aifill tests need `infra/logic/` and `org/standards/` and the project folder. If a test fails with `FileNotFoundError` for a path under one of those, add it with `git sparse-checkout add <folder>` (a read-only folder, never committed) and re-run.

## 3. SURFACES

<paths>
lib/research/aifill/contract.py
lib/research/aifill/grounding.py
lib/research/aifill/orchestrate.py
lib/research/aifill/tests/test_gu1_remedy.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gu-1"><invocation>cd C:/dev/wk-resapp-483 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round108_aifill_prep/checks/check_gu1_remedy.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL GU-1 ARMS: YES (N of N)` with N equal to 20, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gu-1"><invocation>cd C:/dev/wk-resapp-483 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least 825) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~483 <0.9.0_WK_AMGT_RESAPP~483@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~483/AMGT_RESAPP.TO-AMGT-gu-1.the-five-new-name-remedy-clause-level-support-recency-and-the-run-together-word.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, and AC2's pytest summary line;
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT-ACT: one cell, about 110 product lines plus tests, LOCAL; no L2, L4-R or L8-L10; the close is the issuer's one real run (the aifill suite plus the api serve test at the merged head, then a live run of the named names to a local folder, key set inside the call). Authority: CVO `ADJUDICATION_v135.md` @1f532a2c3b row `AMGT_RESAPP-D1-C-S158`, CTO msg 6571 ("Round 108 carries clause-level support and the cross-block recency rule"), and the CTO's 2026-10-14 item (g) (`ledger/CTO_RULING_FWD41_FIVE_NAME_READ_NOT_MET_20261014.md`). Four-postulate record: decomposition section 17 (no schema authored). Reference edit proven in a sparse scratch tree: 20 of 20 arms, 813 tests pass unchanged, ruff clean, ASCII. The expected count in AC2 is 813 plus the twelve new tests. A known direction, chosen on purpose: the specifics check can drop a true sentence (a source that writes `$3bn` where the sentence writes `$3 billion`); it cannot keep a false one on a missing number or name.

<status>complete -- 2026-10-16 by the issuer (2.0.0_SA_COO~R2): worker ~483 merged at 0fd6ae013a (build 06f876c7ed, instance d327d6e309); instance VALID rc=0, re-run by the issuer on the committed bytes: AC1 AIFILL GU-1 ARMS: YES (20 of 20), AC2 830 passed in the worker tree. The three modules are byte-equal to the issuer reference edit (cmp). Drain at the merged head: aifill suite plus api serve test 869 passed, commit-gate clean on 4 files, check 20 of 20 again. Worktree and branch removed. Worker rows W483-S1, W483-S2 (both INERT observations). The issuer one real run (five named names, local folder) and the re-run of 95 follow under CTO msg 6580.</status>
<round>109</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~483</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

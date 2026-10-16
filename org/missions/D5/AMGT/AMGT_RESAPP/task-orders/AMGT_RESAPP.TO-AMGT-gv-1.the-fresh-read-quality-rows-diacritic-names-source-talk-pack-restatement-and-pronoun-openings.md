# AMGT_RESAPP task order -- `AMGT-gv-1` -- THE FRESH READ'S QUALITY ROWS: DIACRITIC NAMES, SOURCE TALK, PACK RESTATEMENT AND PRONOUN OPENINGS (FWD-41 ROUND 110, CVO C-S160, CTO 6620; A DIRECT ACT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gv-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~484</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-gv-1.the-fresh-read-quality-rows-diacritic-names-source-talk-pack-restatement-and-pronoun-openings</to_id>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; library modules and their tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the cell writes and tests local Python only.
comp-adversary: RUN at the cut -- `check_gv1_round110.py` is a prepared acceptance check (12 arms); at the base it reads `AIFILL GV-1 ARMS: NO (6 of 12)`, the build check failing as expected, and the issuer's reference edit in a scratch copy reads 12 of 12 with the 830 existing aifill tests unchanged.
EGRESS CLASS, declared: NONE. No network call by the cell or its checks; no model call; no Bloomberg call.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-484` (branch `wk-AMGT_RESAPP-484`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-484`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-gv-1` (round 110, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md` section 19)

The AI-fill producer (`lib/research/aifill/`) builds one fill document of five blocks per security; each text block's sentences are checked against its cited sources by `grounding.py` (a sentence is kept only when a source supports it and carries every number and name it states), and `orchestrate.py` grounds every block. An independent reader found four quality defects on stored blocks, none a false claim; this cell closes all four. Behaviour not listed here is unchanged.

1. **Names with diacritics (`grounding.py`, `orchestrate.py`).** The number-and-name check compares an ASCII-folded sentence (`Belen Garijo Lopez`, the form every stored sentence has) with a source that carries the accented form, so the sentence that names a person is wrongly withheld and the bio opens on `She` or `He`. New: the source text is folded by `contract.fold_text` before the number-and-name check, and the pack text built for an OPAL source keeps its characters (`json.dumps(..., ensure_ascii=False)`), not `\uXXXX` escapes.
2. **A sentence that only describes its source.** `The headline says nothing about Sanofi's current management team.` states no fact about the company. New: the grounding prompt says such a sentence is UNSUPPORTED, and a short phrase guard (`headline`, `says nothing`, `does not mention/name/identify/state/say`, `refers only`, `no mention of`, `nothing about`) makes a SUPPORTED verdict on a matching sentence UNSUPPORTED.
3. **An OPAL_SOURCE management bio that only repeats the pack passage the page already shows.** New: when every kept sentence of an OPAL_SOURCE `mgmt_bio` has at least 0.6 of its word 4-grams inside the pack passage, the block is withheld (a NONE block with the plain reason `RESTATES_REASON`).
4. **A management bio that opens on an unnamed pronoun.** New: a grounded `mgmt_bio` whose kept text starts with he, she, his, her, they, their, it or its is withheld (a NONE block with the plain reason `UNNAMED_REASON`), also after the recency re-check rebuilds it.

### The change, exactly (this diff against the base is the specification; apply it, do not improvise a different design)

```diff
diff --git a/lib/research/aifill/grounding.py b/lib/research/aifill/grounding.py
index cc954e28ec..c8f0061dac 100644
--- a/lib/research/aifill/grounding.py
+++ b/lib/research/aifill/grounding.py
@@ -20,6 +20,7 @@ import datetime
 import json
 import re
 
+from lib.research.aifill import contract
 from lib.research.aifill import sentences as sentences_module
 from lib.research.aifill import sources as sources_module
 
@@ -35,7 +36,8 @@ SYSTEM = (
     "Give each sentence one verdict. "
     "SUPPORTED: one source states every specific in the sentence (each name, number, date, role and relation). "
     "CONTRADICTED: a source states otherwise. "
-    "UNSUPPORTED: neither of those. "
+    "UNSUPPORTED: neither of those, and also any sentence that only describes what a source says or does not say "
+    "(a headline, a page, a search) and states no fact about the company or its people. "
     "Where dated sources conflict, the newest dated source wins: a sentence stating the older fact is CONTRADICTED. "
     "For each SUPPORTED verdict give the source label (S1, S2, ...) and a verbatim quote of at most 200 characters, "
     "copied exactly from that source. "
@@ -82,6 +84,17 @@ _NOT_NAMES = frozenset((
 ).split())
 
 
+# A sentence that talks about its own source ("the headline says nothing about ...") states no fact about the security (round 110).
+_SOURCE_TALK = re.compile(
+    r"\b(?:headline|says nothing|say nothing|does not (?:mention|name|identify|state|say)|do not (?:mention|name|identify)"
+    r"|refers only|no mention of|nothing about)\b", re.IGNORECASE)
+
+
+def _folded(text):
+    """The normalised form of a source text after the same ASCII folding the stored sentences get (a name with a diacritic matches)."""
+    return _norm(contract.fold_text(text))
+
+
 def _specifics(sent_text):
     """What a sentence states that a source must carry: its numbers (with a following scale word) and its capitalised names."""
     found = []
@@ -191,7 +204,7 @@ def _unsupported(sent_text):
     return {"text": sent_text, "verdict": "UNSUPPORTED", "source": None, "quote": None}
 
 
-def _judge(row, sent_text, usable, norm_full, own_n):
+def _judge(row, sent_text, usable, norm_full, own_n, fold_full=None):
     """The sentence record for one verdict row: SUPPORTED only when an own source is shown, the quote is in its full text
     and the source carries every number and name the sentence states (round 109 clause check). A reference source can
     contradict a sentence but never support it."""
@@ -213,7 +226,10 @@ def _judge(row, sent_text, usable, norm_full, own_n):
     nq = _norm(quote)
     if not nq or nq not in norm_full[k - 1] or usable[k - 1]["index"] >= own_n:
         return _unsupported(sent_text)
-    if _missing_specifics(sent_text, norm_full[k - 1]):
+    if _SOURCE_TALK.search(sent_text):
+        return _unsupported(sent_text)
+    folded = fold_full[k - 1] if fold_full is not None else norm_full[k - 1]
+    if _missing_specifics(sent_text, folded):
         return _unsupported(sent_text)
     return {"text": sent_text, "verdict": "SUPPORTED", "source": usable[k - 1]["index"], "quote": quote}
 
@@ -261,13 +277,14 @@ def _ground(text, sources, model, now, max_window_chars, reference=None):
             continue
         by_n[n] = row
     norm_full = [_norm(src["text"]) for src in usable]
+    fold_full = [_folded(src["text"]) for src in usable]
     sentence_records = []
     for n, sent in enumerate(sent_texts, 1):
         row = by_n.get(n)
         if row is None:
             sentence_records.append(_unsupported(sent))
         else:
-            sentence_records.append(_judge(row, sent, usable, norm_full, own_n))
+            sentence_records.append(_judge(row, sent, usable, norm_full, own_n, fold_full))
 
     kept = [rec for rec in sentence_records if rec["verdict"] == "SUPPORTED"]
     used_urls = []
diff --git a/lib/research/aifill/orchestrate.py b/lib/research/aifill/orchestrate.py
index dcdb306e3e..c488c6f2fe 100644
--- a/lib/research/aifill/orchestrate.py
+++ b/lib/research/aifill/orchestrate.py
@@ -29,6 +29,11 @@ FETCH_CAP = 8
 RECENCY_BLOCKS = ("mgmt_bio", "mgmt_recent", "mgmt_team_view")
 REFERENCE_CAP = 4
 RECENCY_REASON = "A newer source cited elsewhere on this page contradicts the model's statements, so the text was withheld."
+RESTATES_REASON = "The text only repeats the research team's management passage, which the page already shows, so it was withheld."
+UNNAMED_REASON = "The text opens without naming the person it describes, so it was withheld."
+RESTATE_OVERLAP = 0.6
+RESTATE_GRAM = 4
+PRONOUNS = ("he", "she", "his", "her", "they", "their", "it", "its")
 RECENCY_UNCHECKED = "The text could not be checked against the other sources cited on this page, so it was withheld."
 
 
@@ -162,7 +167,7 @@ def _opal_sources(draft, served):
     for path in draft["opal_inputs"]:
         value = _resolve(served, path)
         if _present(value):
-            pieces.append(json.dumps(value, sort_keys=True, default=str))
+            pieces.append(json.dumps(value, sort_keys=True, default=str, ensure_ascii=False))
     text = "\n".join(pieces)
     out = []
     for cite in draft["citations"]:
@@ -182,6 +187,32 @@ def _kept_citations(draft, result):
     return kept
 
 
+def _grams(text, n):
+    words = grounding._norm(text).split()
+    return set(" ".join(words[i:i + n]) for i in range(len(words) - n + 1))
+
+
+def _restates(kept, pack_text):
+    """True when every kept sentence is, almost word for word, in the pack passage the page already shows."""
+    pack = grounding._norm(pack_text)
+    if not kept:
+        return False
+    for rec in kept:
+        grams = _grams(rec["text"], RESTATE_GRAM)
+        if not grams or sum(1 for g in grams if g in pack) / float(len(grams)) < RESTATE_OVERLAP:
+            return False
+    return True
+
+
+def _finished(block_id, block):
+    """A grounded management bio is withheld when it opens on a pronoun with no name before it (round 110)."""
+    text = block.get("text")
+    if block_id == "mgmt_bio" and isinstance(text, str) and text.split():
+        if text.split()[0].strip(",.;:").lower() in PRONOUNS:
+            return contract.none_block(block_id, UNNAMED_REASON)
+    return block
+
+
 def _ground_block(block_id, draft, ctx):
     """The grounded block for a usable draft, or a NONE block with GROUNDING_REASON. Never raises."""
     source_class = draft["source_class"]
@@ -193,9 +224,11 @@ def _ground_block(block_id, draft, ctx):
         result = grounding.ground_block(draft["text"], cited, ctx.model, ctx.now)
         if not result.ok:
             return contract.none_block(block_id, GROUNDING_REASON)
-        return contract.make_block(block_id, source_class, result.text, _kept_citations(draft, result),
-                                   draft["opal_inputs"], draft["model_call"], grounding=result.record,
-                                   require_grounding=True)
+        if source_class == "OPAL_SOURCE" and block_id == "mgmt_bio" and _restates(result.kept, "\n".join(s["text"] for s in cited)):
+            return contract.none_block(block_id, RESTATES_REASON)
+        return _finished(block_id, contract.make_block(block_id, source_class, result.text, _kept_citations(draft, result),
+                                                       draft["opal_inputs"], draft["model_call"], grounding=result.record,
+                                                       require_grounding=True))
     except Exception:  # noqa: BLE001 -- a grounding that cannot be stored withholds the text
         return contract.none_block(block_id, GROUNDING_REASON)
 
@@ -252,8 +285,9 @@ def _recency_block(block_id, blocks, ctx):
                     "output_tokens": (call["output_tokens"] or 0) + (extra["output_tokens"] or 0)}
         new_record = dict(record, sources=result.record["sources"], sentences=sentences, model_call=call)
         cites = [cite for cite in block["citations"] if cite.get("url") in used]
-        return contract.make_block(block_id, "WEB_SEARCH", " ".join(rec["text"] for rec in kept), cites, block["opal_inputs"],
-                                   block["model_call"], grounding=new_record, require_grounding=True)
+        return _finished(block_id, contract.make_block(block_id, "WEB_SEARCH", " ".join(rec["text"] for rec in kept), cites,
+                                                       block["opal_inputs"], block["model_call"], grounding=new_record,
+                                                       require_grounding=True))
     except Exception:  # noqa: BLE001 -- a recency check that cannot be stored withholds the text
         return contract.none_block(block_id, RECENCY_UNCHECKED)
 
```

### Tests (a new module `lib/research/aifill/tests/test_gv1_quality.py`, no `__init__.py`)
At least TWELVE tests, offline (stub model, stub fetcher; follow the helpers in `lib/research/aifill/tests/test_orchestrate_grounding.py` and `test_gu1_remedy.py`): an accented page name matches the folded sentence (SUPPORTED); an absent name still drops the sentence; the pack text for an OPAL source keeps `\u00e9` as the character and has no escape; a source-describing sentence is UNSUPPORTED; a fact sentence stays SUPPORTED; the prompt carries the rule; an OPAL bio that copies the pack passage is withheld with `RESTATES_REASON`; a bio in its own words is kept; a web bio is not tested for restatement; a bio opening on `He` is withheld with `UNNAMED_REASON`; a bio opening on a name is kept; a `mgmt_recent` opening on `He` is kept; and one test that a bio whose first sentence the recency re-check drops, leaving a pronoun opening, is withheld. Do NOT edit an existing test file: the 830 existing aifill tests pass unchanged with this change, and one that does not is a finding to file as a row, not to fix.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W484-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS

1. Write ONLY the files in the `<paths>` block below. `contract.py`, `run.py`, `store.py`, `revalidate.py`, `sources.py`, `sentences.py`, `validation.py`, the block builders and every other module are other cells'.
- No network, no AWS, no real model call, no `pip install`.
- Python 3.9 syntax; ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes, as the diff and the check do); stdlib only. The Write tool can render a `\uXXXX` escape as the character: check your files with `python -c "import sys;b=open(sys.argv[1],'rb').read();print(b.isascii())" <file>` before you commit.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.
- Your sparse worktree may lack a folder a test reads; the aifill tests need `infra/logic/`, `org/standards/` and the project folder. If a test fails with `FileNotFoundError` for a path under one of those, add it with `git sparse-checkout add <folder>` (read-only, never committed) and re-run.

## 3. SURFACES

<paths>
lib/research/aifill/grounding.py
lib/research/aifill/orchestrate.py
lib/research/aifill/tests/test_gv1_quality.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gv-1"><invocation>cd C:/dev/wk-resapp-484 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round110_aifill_prep/checks/check_gv1_round110.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL GV-1 ARMS: YES (N of N)` with N equal to 12, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gv-1"><invocation>cd C:/dev/wk-resapp-484 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least 842) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~484 <0.9.0_WK_AMGT_RESAPP~484@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~484/AMGT_RESAPP.TO-AMGT-gv-1.the-fresh-read-quality-rows-diacritic-names-source-talk-pack-restatement-and-pronoun-openings.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, and AC2's pytest summary line;
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT-ACT: one cell, about 60 product lines plus tests, LOCAL; no L2, L4-R or L8-L10; the close is the issuer's one real run (the aifill suite plus the api serve test at the merged head, then a metered live run of the CVO's flagged names to a local folder). Authority: CVO `ADJUDICATION_v136` row `C-S160` (`REMEDIATION_v47`) and the CTO's ruling `CTO_RULING_AIFILL_HOLD_LIFT_20261016.md` item 2 (round 110, not blocking the lift). Four-postulate record: decomposition section 19 (no schema authored). Reference edit proven in a sparse scratch tree: 12 of 12 arms, 830 tests pass unchanged, ruff clean, ASCII. The expected count in AC2 is 830 plus the twelve new tests. The cause of the pronoun openings is the diacritic false drop of `AMGT-gu-1`'s specifics check (mine, measured): mechanism 4 is the backstop for a naming sentence withheld for any other reason. Known direction, chosen on purpose: the phrase guard and the pack-overlap threshold (0.6) can withhold a block that was fine; neither can keep one that breaks the rule.

<status>complete -- 2026-10-16 by the issuer (2.0.0_SA_COO~R2): worker ~484 merged at d6e03c68b7 (build a8bb404ef3, instance 3e5bda801c); instance VALID rc=0, re-run by the issuer on the committed bytes: AC1 AIFILL GV-1 ARMS: YES (12 of 12), AC2 845 passed in the worker tree. grounding.py and orchestrate.py are byte-equal to the issuer reference edit (cmp). Drain at the merged head: aifill suite plus api serve test 884 passed, commit-gate clean on 3 files, the gu-1 check still 20 of 20, every investigation row present after the merge (no duplicate id). Worktree, branch and scratch tree removed. Worker rows W484-S1, W484-S2 (INERT observations). The metered re-run of the 95 and its store pair follow.</status>
<round>110</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~484</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

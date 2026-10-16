# AMGT_RESAPP task order -- `AMGT-gw-1` -- THE TRUNCATION RETRY, THE SUBJECT RULE AND THE PARAPHRASE RESTATEMENT RULE (FWD-41 ROUND 111, CTO 6644 AND 6648; A DIRECT ACT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gw-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~485</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-gw-1.the-truncation-retry-the-subject-rule-and-the-paraphrase-restatement-rule</to_id>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; library modules and their tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the cell writes and tests local Python only.
comp-adversary: RUN at the cut -- `check_gw1_round111.py` is a prepared acceptance check (17 arms); at the base it reads `AIFILL GW-1 ARMS: NO (5 of 17)`, the build check failing as expected, and the issuer's reference edit in a scratch copy reads 17 of 17 with the 845 existing aifill tests unchanged and the earlier checks (GU-1 20 of 20, GV-1 12 of 12) still YES.
EGRESS CLASS, declared: NONE. No network call by the cell or its checks; no model call; no Bloomberg call.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-485` (branch `wk-AMGT_RESAPP-485`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-485`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-gw-1` (round 111, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md` section 20)

The AI-fill producer (`lib/research/aifill/`) builds one fill document of five blocks per security: block builders (`block_*.py`) draft each block (the web ones through a web-search model call), `grounding.py` keeps only the sentences a source supports, and `orchestrate.py` assembles and checks the document. An independent reader and the first run of the new rules found five defects; this cell closes all five. Behaviour not listed here is unchanged.

1. **Truncated drafts.** The web-search draft calls ran at the model seam's default output limit (1500 tokens) and 9 blocks of the last 95 documents were lost to `model answer was truncated at max_tokens`. New: one shared constant `contract.WEB_DRAFT_MAX_TOKENS = 4000`, passed as `max_tokens` by every web-search draft call in the five block modules. The seam's own default (1500) does NOT change (an existing test pins it).
2. **Retry of failed blocks only.** New `orchestrate.retry_failed_blocks(doc, security_key, inputs, model, now=None, builders=None, fetch=None)`: a copy of the document in which ONLY the blocks whose `reason` starts with `This block could not be produced` are built again (draft, grounding, and for management blocks the recency step); every other block comes back exactly as it was, validation stamp included; a rebuilt block carries no `validation` key; the result must pass `contract.validate_document(..., require_grounding=True)`.
3. **The unnamed-opening rule tests the SUBJECT.** A grounded `mgmt_bio` is withheld (a NONE block with `UNNAMED_REASON`) when its opening sentence names no one. With the CEO's name known from the served officer list (`inputs["thesis"]["management"]["officers"]`, the officer whose role matches chief executive or CEO) the opening sentence must carry one of its name tokens (three letters or more, ASCII-folded); with no officer list: the first word is a pronoun, or a pronoun stands among the first six words with no capitalised word (other than the first) before it. This replaces the first-word test of round 110.
4. **The restatement rule also catches a paraphrase.** An OPAL_SOURCE `mgmt_bio` is withheld (a NONE block with `RESTATES_REASON`) when it copies the pack passage (the round-110 verbatim test, unchanged, any size) OR paraphrases it: a bio of six content words or more (words of five letters or more, not a stop word) with at least 0.6 of them in the pack passage.
5. **A stored document can be re-checked with no model call.** New `orchestrate.refinish_document(doc, inputs)`: a copy of the document in which the `mgmt_bio` is withheld if rule 3 or rule 4 would withhold it (rule 4 reads the pack text from the bio's `opal_inputs` paths in `inputs`); every other block unchanged; the input is not changed.

### The change, exactly (this diff against the base is the specification; apply it, do not improvise a different design)

```diff
diff --git a/lib/research/aifill/block_identity_description.py b/lib/research/aifill/block_identity_description.py
index 3b7318b87a..93c9c0fe93 100644
--- a/lib/research/aifill/block_identity_description.py
+++ b/lib/research/aifill/block_identity_description.py
@@ -218,8 +218,8 @@ def build_block(ctx):
         opal = _opal_block(ctx.model(_prompt_opal(company, facts), system=SYSTEM_OPAL, web_search_max_uses=0), facts)
         if opal["source_class"] != "NONE":
             return opal
-        web = _web_block(ctx.model(_prompt_web(company), system=SYSTEM_WEB, web_search_max_uses=3))
+        web = _web_block(ctx.model(_prompt_web(company), system=SYSTEM_WEB, web_search_max_uses=3, max_tokens=contract.WEB_DRAFT_MAX_TOKENS))
         if web["source_class"] != "NONE":
             return web
         return contract.none_block(BLOCK_ID, opal["reason"] + " " + web["reason"])
-    return _web_block(ctx.model(_prompt_web(company), system=SYSTEM_WEB, web_search_max_uses=3))
+    return _web_block(ctx.model(_prompt_web(company), system=SYSTEM_WEB, web_search_max_uses=3, max_tokens=contract.WEB_DRAFT_MAX_TOKENS))
diff --git a/lib/research/aifill/block_mgmt_bio.py b/lib/research/aifill/block_mgmt_bio.py
index 2205461c4c..082d0f73dc 100644
--- a/lib/research/aifill/block_mgmt_bio.py
+++ b/lib/research/aifill/block_mgmt_bio.py
@@ -290,7 +290,8 @@ def _web_citations(raw):
 
 
 def _web_block(ctx, company, ceo):
-    result = ctx.model(_web_prompt(company, ceo), system=SYSTEM_WEB, web_search_max_uses=WEB_SEARCH_USES)
+    result = ctx.model(_web_prompt(company, ceo), system=SYSTEM_WEB, web_search_max_uses=WEB_SEARCH_USES,
+                      max_tokens=contract.WEB_DRAFT_MAX_TOKENS)
     reply = _reply_text(result)
     if reply is None:
         return contract.none_block(BLOCK_ID, NOTHING_REASON)
diff --git a/lib/research/aifill/block_mgmt_recent.py b/lib/research/aifill/block_mgmt_recent.py
index 3a263d4b26..750f56ed2d 100644
--- a/lib/research/aifill/block_mgmt_recent.py
+++ b/lib/research/aifill/block_mgmt_recent.py
@@ -228,7 +228,7 @@ def _web(ctx, company, ceo):
         "appointments, departures, succession, and notable statements of strategy by management. "
         "Answer in two to four plain sentences of no more than %d characters."
     ) % (subject, PROMPT_CHARS)
-    result = ctx.model(prompt, system=SYSTEM_WEB, web_search_max_uses=3)
+    result = ctx.model(prompt, system=SYSTEM_WEB, web_search_max_uses=3, max_tokens=contract.WEB_DRAFT_MAX_TOKENS)
     text = _folded_reply(result)
     if text is None:
         return contract.none_block(BLOCK_ID, NO_INFO_REASON)
diff --git a/lib/research/aifill/block_mgmt_team_view.py b/lib/research/aifill/block_mgmt_team_view.py
index 2efacfb391..ab53ea7f7f 100644
--- a/lib/research/aifill/block_mgmt_team_view.py
+++ b/lib/research/aifill/block_mgmt_team_view.py
@@ -162,5 +162,5 @@ def build_block(ctx):
     if _pack_states_management(thesis):
         return contract.none_block(BLOCK_ID, "The research team's pack already states a management passage.")
     prompt = _prompt(_company(ctx.inputs), _ceo(ctx.inputs))
-    result = ctx.model(prompt, system=SYSTEM_WEB, web_search_max_uses=3)
+    result = ctx.model(prompt, system=SYSTEM_WEB, web_search_max_uses=3, max_tokens=contract.WEB_DRAFT_MAX_TOKENS)
     return _web_block(result)
diff --git a/lib/research/aifill/block_thesis_pillars.py b/lib/research/aifill/block_thesis_pillars.py
index b22da612f8..03eb379e93 100644
--- a/lib/research/aifill/block_thesis_pillars.py
+++ b/lib/research/aifill/block_thesis_pillars.py
@@ -206,8 +206,8 @@ def build_block(ctx):
         opal = _opal_block(ctx.model(_prompt_opal(company, facts), system=SYSTEM_OPAL, web_search_max_uses=0), facts)
         if opal["source_class"] != "NONE":
             return opal
-        web = _web_block(ctx.model(_prompt_web(company), system=SYSTEM_WEB, web_search_max_uses=3))
+        web = _web_block(ctx.model(_prompt_web(company), system=SYSTEM_WEB, web_search_max_uses=3, max_tokens=contract.WEB_DRAFT_MAX_TOKENS))
         if web["source_class"] != "NONE":
             return web
         return contract.none_block(BLOCK_ID, opal["reason"] + " " + web["reason"])
-    return _web_block(ctx.model(_prompt_web(company), system=SYSTEM_WEB, web_search_max_uses=3))
+    return _web_block(ctx.model(_prompt_web(company), system=SYSTEM_WEB, web_search_max_uses=3, max_tokens=contract.WEB_DRAFT_MAX_TOKENS))
diff --git a/lib/research/aifill/contract.py b/lib/research/aifill/contract.py
index 84df7e0a43..aa4b787989 100644
--- a/lib/research/aifill/contract.py
+++ b/lib/research/aifill/contract.py
@@ -9,6 +9,7 @@ import re
 import unicodedata
 
 SCHEMA = "aifill/v1"
+WEB_DRAFT_MAX_TOKENS = 4000  # the output limit of a web-search draft call (the seam default, 1500, truncated 9 blocks)
 PRODUCER_VERSION = "opal-aifill/1.1.0"
 PRODUCER_MODEL = "claude-opus-5"
 BLOCK_IDS = ("mgmt_bio", "mgmt_recent", "mgmt_team_view", "thesis_pillars", "identity_description")
diff --git a/lib/research/aifill/orchestrate.py b/lib/research/aifill/orchestrate.py
index c488c6f2fe..0a78d590c6 100644
--- a/lib/research/aifill/orchestrate.py
+++ b/lib/research/aifill/orchestrate.py
@@ -9,13 +9,16 @@ fields they list in opal_inputs. No fetch is made here: the fetcher arrives as a
 """
 from __future__ import annotations
 
+import copy
 import datetime
 import importlib
 import json
+import re
 from typing import Optional
 
 from . import contract
 from . import grounding
+from . import sentences as sentences_module
 from . import sources
 
 PACKAGE = "lib.research.aifill"
@@ -33,7 +36,17 @@ RESTATES_REASON = "The text only repeats the research team's management passage,
 UNNAMED_REASON = "The text opens without naming the person it describes, so it was withheld."
 RESTATE_OVERLAP = 0.6
 RESTATE_GRAM = 4
+RESTATE_COVER = 0.6
+RESTATE_MIN_WORDS = 6
+_STOP_WORDS = frozenset((
+    "the and for with that this from have has had was were are been being will would their they them which while where when into onto "
+    "over under after before about also such than then there these those other more most many much some very each both either only "
+    "just like even still its his her him she who whom whose"
+).split())
 PRONOUNS = ("he", "she", "his", "her", "they", "their", "it", "its")
+SUBJECT_WINDOW = 6
+FAILED_PREFIX = "This block could not be produced"
+_CEO_ROLE = re.compile(r"chief executive|\bceo\b", re.IGNORECASE)
 RECENCY_UNCHECKED = "The text could not be checked against the other sources cited on this page, so it was withheld."
 
 
@@ -192,8 +205,13 @@ def _grams(text, n):
     return set(" ".join(words[i:i + n]) for i in range(len(words) - n + 1))
 
 
-def _restates(kept, pack_text):
-    """True when every kept sentence is, almost word for word, in the pack passage the page already shows."""
+def _content_words(text):
+    """The words of a text that carry content: five letters or more, not a stop word, ASCII-folded and normalised."""
+    return [w for w in grounding._norm(contract.fold_text(text)).split() if len(w) >= 5 and w not in _STOP_WORDS]
+
+
+def _copies(kept, pack_text):
+    """True when every kept sentence is, almost word for word, in the pack passage the page already shows (round 110)."""
     pack = grounding._norm(pack_text)
     if not kept:
         return False
@@ -204,15 +222,115 @@ def _restates(kept, pack_text):
     return True
 
 
-def _finished(block_id, block):
-    """A grounded management bio is withheld when it opens on a pronoun with no name before it (round 110)."""
+def _paraphrases(kept, pack_text):
+    """True when a bio of RESTATE_MIN_WORDS content words or more has at least RESTATE_COVER of them in the pack passage: it says
+    again, in other words, what the passage says (round 111; the verbatim test cannot see a paraphrase)."""
+    words = _content_words(" ".join(rec["text"] for rec in kept))
+    if len(words) < RESTATE_MIN_WORDS:
+        return False
+    pack = set(_content_words(pack_text))
+    return sum(1 for w in words if w in pack) / float(len(words)) >= RESTATE_COVER
+
+
+def _restates(kept, pack_text):
+    """The restatement rule (round-106 rule (e)): the bio copies or paraphrases the pack passage the page already shows."""
+    return _copies(kept, pack_text) or _paraphrases(kept, pack_text)
+
+
+def _ceo_tokens(inputs):
+    """The lower-case name tokens (3 letters or more, ASCII-folded) of the CEO the served officer list names, else an empty set."""
+    try:
+        officers = inputs["thesis"]["management"]["officers"]
+    except (KeyError, TypeError):
+        return set()
+    for officer in officers if isinstance(officers, list) else []:
+        if isinstance(officer, dict) and isinstance(officer.get("role"), str) and _CEO_ROLE.search(officer["role"]):
+            name = officer.get("name")
+            if isinstance(name, str):
+                return set(w for w in grounding._norm(contract.fold_text(name)).split() if len(w) >= 3)
+    return set()
+
+
+def _opens_unnamed(text, ceo_tokens):
+    """True when the opening sentence does not name the person it describes (round 111: its SUBJECT, not only its first word).
+
+    With the CEO's name known, the sentence must carry one of its tokens. Without it: the first word is a pronoun, or a pronoun
+    stands among the first SUBJECT_WINDOW words with no capitalised word (other than the first) before it."""
+    parts = sentences_module.split_sentences(text)
+    if not parts:
+        return False
+    first = parts[0]
+    if ceo_tokens:
+        return not (set(grounding._norm(first).split()) & ceo_tokens)
+    words = first.split()
+    for i, word in enumerate(words[:SUBJECT_WINDOW]):
+        if word.strip(",.;:").lower() in PRONOUNS:
+            return not any(w[:1].isupper() for w in words[1:i])
+    return False
+
+
+def _finished(block_id, block, inputs=None):
+    """A grounded management bio is withheld when its opening sentence does not name the person it describes (rounds 110 and 111)."""
     text = block.get("text")
     if block_id == "mgmt_bio" and isinstance(text, str) and text.split():
-        if text.split()[0].strip(",.;:").lower() in PRONOUNS:
+        if _opens_unnamed(text, _ceo_tokens(inputs)):
             return contract.none_block(block_id, UNNAMED_REASON)
     return block
 
 
+def _pack_text(bio, inputs):
+    """The pack passage text an OPAL_SOURCE bio was built on: its listed served fields, joined as the grounding source joins them."""
+    pieces = []
+    for path in bio.get("opal_inputs") or []:
+        value = _resolve(inputs, path)
+        if _present(value):
+            pieces.append(json.dumps(value, sort_keys=True, default=str, ensure_ascii=False))
+    return "\n".join(pieces)
+
+
+def refinish_document(doc, inputs):
+    """A copy of a fill document with the management bio withheld if it fails the round-110 and round-111 rules (no model call):
+    its opening sentence names no one, or an OPAL_SOURCE bio only repeats or paraphrases the pack passage.
+
+    Every other block is returned as it is; a withheld bio carries no `validation` key, so the caller stamps the copy again."""
+    out = copy.deepcopy(doc)
+    bio = out["blocks"].get("mgmt_bio")
+    if not isinstance(bio, dict) or not isinstance(bio.get("text"), str) or not bio["text"].strip():
+        return out
+    plain = {k: v for k, v in bio.items() if k != contract.VALIDATION_KEY}
+    done = _finished("mgmt_bio", plain, inputs)
+    if done is plain and plain.get("source_class") == "OPAL_SOURCE":
+        kept = [{"text": s} for s in sentences_module.split_sentences(plain["text"])]
+        if _restates(kept, _pack_text(plain, inputs)):
+            done = contract.none_block("mgmt_bio", RESTATES_REASON)
+    if done is not plain:
+        out["blocks"]["mgmt_bio"] = done
+    return out
+
+
+def retry_failed_blocks(doc, security_key, inputs, model, now=None, builders=None, fetch=None):
+    """A copy of a fill document in which ONLY the blocks that failed ("This block could not be produced") are built again.
+
+    A retried block goes through the same draft, grounding and (management blocks) recency steps as in build_document; every
+    other block is returned as it is, so what a reader has already read does not change. The result passes validate_document."""
+    stamp = _utc(now)
+    out = copy.deepcopy(doc)
+    failed = [b for b in contract.BLOCK_IDS
+              if isinstance(out["blocks"].get(b), dict) and str(out["blocks"][b].get("reason") or "").startswith(FAILED_PREFIX)]
+    if not failed:
+        return out
+    ctx = BlockContext(security_key, inputs, model, stamp, fetch=_cached_fetch(fetch))
+    for block_id in failed:
+        out["blocks"][block_id] = _build_one(block_id, ctx, builders, True)
+    for block_id in RECENCY_BLOCKS:
+        if block_id in failed:
+            out["blocks"][block_id] = _recency_block(block_id, out["blocks"], ctx)
+    problems = contract.validate_document(out, require_grounding=True)
+    if problems:
+        raise contract.ContractError("; ".join(problems))
+    return out
+
+
 def _ground_block(block_id, draft, ctx):
     """The grounded block for a usable draft, or a NONE block with GROUNDING_REASON. Never raises."""
     source_class = draft["source_class"]
@@ -228,7 +346,7 @@ def _ground_block(block_id, draft, ctx):
             return contract.none_block(block_id, RESTATES_REASON)
         return _finished(block_id, contract.make_block(block_id, source_class, result.text, _kept_citations(draft, result),
                                                        draft["opal_inputs"], draft["model_call"], grounding=result.record,
-                                                       require_grounding=True))
+                                                       require_grounding=True), ctx.inputs)
     except Exception:  # noqa: BLE001 -- a grounding that cannot be stored withholds the text
         return contract.none_block(block_id, GROUNDING_REASON)
 
@@ -287,7 +405,7 @@ def _recency_block(block_id, blocks, ctx):
         cites = [cite for cite in block["citations"] if cite.get("url") in used]
         return _finished(block_id, contract.make_block(block_id, "WEB_SEARCH", " ".join(rec["text"] for rec in kept), cites,
                                                        block["opal_inputs"], block["model_call"], grounding=new_record,
-                                                       require_grounding=True))
+                                                       require_grounding=True), ctx.inputs)
     except Exception:  # noqa: BLE001 -- a recency check that cannot be stored withholds the text
         return contract.none_block(block_id, RECENCY_UNCHECKED)
 
```

### Tests (a new module `lib/research/aifill/tests/test_gw1_round111.py`, no `__init__.py`)
At least FOURTEEN tests, offline (stub model, stub fetcher; follow the helpers in `lib/research/aifill/tests/test_orchestrate_grounding.py`, `test_gu1_remedy.py` and `test_gv1_quality.py`): every web-search draft call in the five block modules carries `max_tokens=contract.WEB_DRAFT_MAX_TOKENS` (a source-level test per module) and the constant is 4000 while the seam default stays 1500; the retry rebuilds only the failed block (the other blocks equal, one grounding call), leaves the input unchanged, makes no call and returns an equal copy when nothing failed, keeps the untouched blocks' validation stamps and returns the rebuilt block unstamped; with the CEO's name known a bio opening `Earlier she was ...` is withheld with `UNNAMED_REASON` and a bio carrying a name token is kept; with no officer list a pronoun among the first words with no name before it is withheld and `Jane Roe said she ...` is kept; a `mgmt_recent` opening on a pronoun is kept; an OPAL bio that paraphrases the pack passage is withheld with `RESTATES_REASON` and one with content the passage does not carry is kept; `refinish_document` withholds a stored bio that opens unnamed, withholds a stored OPAL bio that paraphrases the pack, returns an equal copy for a named bio and never changes its input. Do NOT edit an existing test file: the 845 existing aifill tests pass unchanged with this change, and one that does not is a finding to file as a row, not to fix.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W485-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS

1. Write ONLY the files in the `<paths>` block below. `model.py`, `grounding.py`, `run.py`, `store.py`, `revalidate.py`, `sources.py`, `sentences.py`, `validation.py` and every other module are other cells'.
- No network, no AWS, no real model call, no `pip install`.
- Python 3.9 syntax; ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes, as the diff does); stdlib only. The Write and Edit tools can render a `\uXXXX` escape as the character: check each file with `python -c "import sys;b=open(sys.argv[1],'rb').read();print(b.isascii())" <file>` before you commit.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.
- Your sparse worktree may lack a folder a test reads; the aifill tests need `infra/logic/`, `org/standards/` and the project folder. If a test fails with `FileNotFoundError` for a path under one of those, add it with `git sparse-checkout add <folder>` (read-only, never committed) and re-run.

## 3. SURFACES

<paths>
lib/research/aifill/contract.py
lib/research/aifill/orchestrate.py
lib/research/aifill/block_identity_description.py
lib/research/aifill/block_mgmt_bio.py
lib/research/aifill/block_mgmt_recent.py
lib/research/aifill/block_mgmt_team_view.py
lib/research/aifill/block_thesis_pillars.py
lib/research/aifill/tests/test_gw1_round111.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gw-1"><invocation>cd C:/dev/wk-resapp-485 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round111_aifill_prep/checks/check_gw1_round111.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL GW-1 ARMS: YES (N of N)` with N equal to 17, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gw-1"><invocation>cd C:/dev/wk-resapp-485 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least 859) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~485 <0.9.0_WK_AMGT_RESAPP~485@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~485/AMGT_RESAPP.TO-AMGT-gw-1.the-truncation-retry-the-subject-rule-and-the-paraphrase-restatement-rule.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, and AC2's pytest summary line;
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT-ACT: one cell, about 125 product lines plus tests, LOCAL; no L2, L4-R or L8-L10; the close is the issuer's one real run (the aifill suite plus the api serve test at the merged head; `refinish_document` over the stored round-110 set with the served inputs, a GET and no model call; and a metered retry of the failed blocks). Authority: the CTO's round-111 scope (msg 6644) and the CVO's fresh read of the round-110 set relayed by the CTO (msg 6648, row C-S160 NOT met). Four-postulate record: decomposition section 20 (no schema authored). Reference edit proven in a sparse scratch tree: 17 of 17 arms, 845 tests pass unchanged, ruff clean, ASCII, the earlier checks still YES. **The measured consequence, stated at the cut:** applied to the stored round-110 set with no model call, kept bios go 53 to 26 (the subject rule withholds 16, the restatement rule withholds the 11 remaining OPAL bios), because an OPAL bio can only state what the pack states; the page then shows the research team's passage and the officer table where the bio was. The expected count in AC2 is 845 plus the fourteen new tests.

<status>complete -- 2026-10-16 by the issuer (2.0.0_SA_COO~R2): worker ~485 merged at 08a3b6df06 (build 62e465e40a, instance cbe2e186c7); instance VALID rc=0, re-run by the issuer on the committed bytes: AC1 AIFILL GW-1 ARMS: YES (17 of 17), AC2 866 passed in the worker tree. The seven source modules equal the issuer reference edit rebuilt from its saved diff (identical after line-ending normalisation: the rebuilt reference carried CRLF from Windows tooling, the worker files are LF as in the repo). Drain at the merged head: aifill suite plus api serve test 905 passed, commit-gate clean on 3 files, GU-1 20 of 20 and GV-1 12 of 12 still YES, no duplicate investigation row. Worktree and branch removed. No worker row. The no-model re-check and the metered retry (fix_set.py) and their store pair follow.</status>
<round>111</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~485</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

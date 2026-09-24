# AMGT_RESAPP task order -- `AMGT-rk-40` -- translation, design A: analyze the original, translate the output; Unicode passages, pre-cut citation blocks, a character-level verbatim rule

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-40</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~42</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; no schedule is read
  or written; the scheduled batch task stays DISABLED and is not touched.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes no AWS resource (every output lands under the worktree's
  `.scratch/`); the one secret it reads (the model key) reaches the process only as ANTHROPIC_API_KEY exported from
  `comp-secrets`, exactly as `analyze.py:226-231` already requires; it grants no permission and touches no Terraform.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~42`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and every path in
section 3 exists; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~42;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-40` (R14-F3; FWD-18; Thesis T13; validation V4)

**The analysis row, verbatim (ROUND_ANALYSIS.round13.md s.4 @9c8e04cd9a):** *"TRANSLATION, design A: analyze the
original, translate the output; Unicode passages (`passages.py:67-79` keeps 6.8% of Japanese today), pre-cut citation
blocks, a character-level verbatim rule"* -- serves FWD-18, T13, V4; co-sign: no.

**The rule this serves (PRD v0.13 @1699960261, `C-FILINGS-TRANSLATION` `:703-720`), verbatim where it binds:**
*"ANALYZE THE ORIGINAL; TRANSLATE THE OUTPUT. A battery winner in any language is analyzed in its ORIGINAL language.
Only the analyzer's OUTPUT is translated. Every cited span re-locates VERBATIM in the ORIGINAL filing. Translating the
passages first is REFUSED"*; *"Where it sits: after the cutter and the passage map, before analysis"*; the three
preconditions *"(i) Unicode passages -- no ASCII folding of evidence text; (ii) citation blocks pre-cut to the passage
map ...; (iii) a CHARACTER-LEVEL verbatim rule for scripts written without spaces"*; the contract for translated text
*"each translated line carries `translated: true`, the source language, the translator (model and prompt version) and
the time, with the original sentence and its passage id beside it"*; *"English edition: ... only when it is the SAME
fiscal year AND the SAME document family and it passes test (c). A thinner document in English is a different
document"* (Keyence's English Annual Report is NOT the Yuho -- evidence `:1676-1679`). `C-VERBATIM-GATE` `:916-917`:
*"The minimum run length is word-based for spaced scripts and CHARACTER-based for scripts without spaces; the cut states
each threshold"* -- THIS order states them: **8 tokens for spaced scripts (today's `MIN_QUOTE_TOKENS`,
`drafting_build.py:75`); 12 characters for unspaced scripts (the validation's `MIN = 12`, 70 of 71 held on it).**

**1.1 The measured current state (read at HEAD; `lib/research/filings/` last moved @db6c40083f).**
- **(i) fails today, D13:** `passages.py:67-79` `to_ascii()` -- explicit map, NFKD, then `encode("ascii", "ignore")` --
  and `build_passage_map()` stores `ascii_text` at `:182-190`. On the Keyence Yuho it keeps **6.8%** of the characters
  and 7 of 28 passages are stored EMPTY (validation s.4). `analyze.py` folds again at `:401` and `:427` (cited text),
  `:551-555` (`_clean_item_text`, D15: findings lose their Japanese quotes while the counts still read 100% cited),
  `:814` (table passages) and `:957` (`pass_1_text`); `:951-956` records the folding as `ascii_normalisation`.
  **The pool boundary already protects AWS from non-ASCII:** `crosswalk.serialise()` (`lib/research/identity/
  crosswalk.py:439-441`) is `json.dumps(..., ensure_ascii=True)`, so a Unicode passage becomes `\u` escapes in the bytes
  written -- folding the TEXT is not what keeps the pool ASCII, and it never was.
- **(ii) fails today, D16:** `pass_1()` sends the excerpt as ONE plain-text document (`analyze.py:285-293`,
  `{"type": "text", "media_type": "text/plain", "data": excerpt_text}`); on Japanese the citations API's sentence
  chunking collapsed to one chunk and all 74 citations spanned the whole excerpt (validation s.4). The validation's
  design-A run sent the document as a custom-content document -- `{"type": "content", "content": [{"type": "text",
  "text": passage} ...]}` -- one block per passage, and got 72 citations each naming EXACTLY one block
  (`start_block_index`/`end_block_index`), 72 of 72 cited texts in the original.
- **(iii) fails today, D18-on-Japanese:** `drafting_build.py:85-113` `longest_verbatim_run()` splits on SPACES
  (`:93`), so a Japanese sentence is one token and the run is found in 0 of 68 findings; the gate can only pass
  vacuously. `_QUOTED_RE` `:70` recognises ASCII double quotes only.
- **D14:** `pass_2()` `analyze.py:444` caps output at 12,000 tokens and the Japanese second pass truncated at exactly
  that; items fell to the notes fallback.
- **D11:** no language detection anywhere -- provided by `AMGT-rk-39`'s `document.detect_language()` (this order
  CONSUMES it; see 1.3).
- **Design A, measured on Keyence** (validation s.4, `C-FILINGS-TRANSLATION` evidence `:1676-1679`): findings written in
  Japanese over 40 pre-cut passages with no folding -- **70 of 71 findings carried a verbatim run of 12+ characters
  inside their one cited passage**; the neighbour-passage control refused **70 of 70**, the one-character-mutation control
  refused **68 of 68**; translation of the output: 71 of 71 lines carrying the contract fields and **0 of 71 translations
  relocate in the original**. Cost: analysis USD 0.2041 + translation USD 0.1120 = **USD 0.32 for the name**.
- `verbatim.py:42-50` `normalise()`: curly quotes straightened, casefold, whitespace collapsed -- no Unicode canonical
  normalisation (NFC), and whitespace is collapsed to ONE space, which is wrong for an unspaced script whose PDF text
  carries spurious spaces.

**1.2 What you build.**
1. **Unicode passages** (`passages.py`): `build_passage_map()` stores the line's text NFC-normalised, never folded;
   `ascii_replacements` is replaced by `non_ascii_chars` (a count, so the object still says what it carries);
   `to_ascii()` and `_ASCII_MAP` are REMOVED with every call site in `analyze.py` (`:401`, `:427`, `:552`, `:814`,
   `:957`) -- `ensure_ascii=True` at the pool boundary is the ONE place non-ASCII is escaped. `Locator` normalises with
   NFC + the quote map + casefold and, for an UNSPACED script, strips ALL whitespace on both sides of the search (the
   offsets map still returns original character ranges). `analyze.py:951-956` becomes
   `text_encoding: {"unicode": true, "normalisation": "NFC", "non_ascii_chars_in_passages": N}`.
2. **Pre-cut citation blocks** (`analyze.py`): `pass_1()` sends the document as `{"type": "content", "content": [one
   text block per passage of the passage map]}` for EVERY document (one path, not a Japanese special case); `resolve_pass_1()`
   handles the `content_block_location` shape -- `start_block_index..end_block_index` map to passage ids DIRECTLY, and
   the `cited_text` is still checked to lie inside that passage after normalisation (a block index is never trusted
   alone) -- and keeps the `char_location` and inline-tag shapes for cached pass-1 objects and old replies. Cached pass-1
   objects carry `prompt_version`, so `PROMPT_VERSION` -> `rj6-two-pass/2` invalidates every cache made under the plain-text
   shape. When `language != "en"`, the pass-1 prompt gains ONE language rule: write every finding in the filing's own
   language and quote with the script's own quotation marks (Japanese corner brackets `\u300C` ... `\u300D`, recognised
   by `_QUOTED_RE` alongside ASCII double quotes). `pass_2()`'s `max_tokens` scales with the pass-1 output length
   (D14) and a truncated reply (`stop_reason max_tokens`) is RECORDED on the analysis, never silent.
3. **Language detection at the stage boundary**: `analyze_source()` records `language` on the analysis from the source
   object's `language` (set by `AMGT-rk-38`'s battery / `AMGT-rk-39`'s CLI) or, when absent, from
   `document.detect_language(excerpt_text)`, with the shares.
4. **A character-level verbatim rule** (`drafting_build.py:85-128`): `longest_verbatim_run()` dispatches on the
   sentence's script -- spaced (today's token search, floor 8 tokens) or unspaced (cjk share of the sentence > 0.3: a
   binary search over CHARACTER windows on whitespace-stripped NFC text, floor 12 characters, the span returned as the
   original substring). `verbatim.py:normalise()` gains NFC first and an `unspaced` mode that removes all whitespace.
   `quote_method` gains `longest-verbatim-run-chars`.
5. **The translation stage**, NEW `lib/research/filings/translate.py`: `translate_output(analysis, caller=None) ->
   analysis` -- for `language != "en"`, ONE model call per document through `analyze.anthropic_call` (the package's only
   vendor seam, `analyze.py:219-243`): a numbered list of every served item's text plus the driver's series, unit and
   why goes in; a numbered JSON list comes back; a count mismatch is a FAILED translation recorded on the object with
   the items left original-only. Each served item and the driver gain `text_original` (= `text`), `text_translated`, and
   `translation: {"translated": true, "source_language", "translator": {"model", "prompt_version": "rj6-translate/1"},
   "translated_at", "passage_ids"}`. English documents record `translation: {"skipped": "english"}` and make NO call.
   `build_drafting_document()` carries `text_translated` and `translation` on every sentence; the gate runs on the
   ORIGINAL `text` against the ORIGINAL passage, never on the translation. A CLI:
   `python -m lib.research.filings.translate --analysis PATH --out PATH [--controls]`.
6. **Controls as code** (`translate.py --controls` or a `verify` module function), printing denominators:
   (a) every served item's longest run lies inside the passage(s) it cites; (b) the NEIGHBOUR control -- the same run
   tested against the adjacent passage -- must be refused; (c) the ONE-CHARACTER MUTATION control -- one character of a
   passing run replaced -- must be refused; (d) every `text_translated` must NOT relocate in the original.
7. Tests in `lib/research/filings/tests/test_translation.py` (model stubbed through the seam, exactly as
   `test_filings.py:206-225` does).

**1.3 The validation bar (`C-VALIDATION-NAMES`) and the cost.** Keyence (`6861 JP Equity`) is the validation name that
exercises this stage; CAT (English) is the negative control (no translation, no call). The Keyence source object is
produced LOCALLY by `AMGT-rk-39`'s CLI (`python -m lib.research.filings.document --pdf-url ... --family auto --out-dir
.scratch/docs`, the invocation in that order's AC3) -- so this order depends on `AMGT-rk-39` having landed, and on
`lib/research/filings/document.py` being present in your worktree; if it is absent, STOP with a BLOCKING row. The
analysis is a live two-pass run on Keyence (about USD 0.20) plus one translation call (about USD 0.11); **the spend cap
for this order is USD 5.00** (AMENDMENT 3, 2.0.0_SA_COO~Z 2026-09-19 ~12:0xZ, row W42-S6: raised from 3.00 -- three live sessions spent ~2.95 finding and proving the bugs rows S3/S4 name; AC5 and AC6 each run ONCE off the CACHED analysis file, AC3's live pass-1 is NOT re-run; the cumulative figure is printed on every call), recorded per call. NO fleet run, NO run on any of the covered 33,
NO re-run. The key: `export ANTHROPIC_API_KEY="$(comp-secrets get anthropic-api-key --reveal | grep '^value:' | sed
's/^value:[[:space:]]*//')"` in the SAME call, per `analyze.py:226-231`.

## 2. WHERE THIS CAME FROM

**ROUND 14**, on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis s.4 row R14-F3 @9c8e04cd9a; intake T13 and V4; the validation
s.4 (@b527b93214). PRD v0.13 @1699960261: `C-FILINGS-TRANSLATION` `:703-720`, `C-VERBATIM-GATE` `:907-920`,
`C-FILINGS-ANALYZER` `:689-690` (the analyzer version moves with its contract -- see 1.4), `C-VALIDATION-NAMES`
`:1652-1658`, evidence `:1676-1679`. The COO's round-14 decomposition record for this cell in `AMGT_RESAPP_DECOMP.md` is
the postulate paragraph landed beside this order.

**1.4 Versions.** This order moves the analysis object's output contract (`language`, `text_encoding`, translation
fields). `AMGT-rk-42` makes `ANALYZER_VERSION` MOVE with the contract (a fingerprint test). If `AMGT-rk-42` has landed
before you, its test fails until you bump `ANALYZER_VERSION` and the fingerprint together -- do that (`2.0.0` ->
`2.1.0`). If it has not, bump `ANALYZER_VERSION` `analyze.py:60` to `1.1.0` yourself; whichever lands second reconciles.

**ISSUER AMENDMENT on row AMGT_RESAPP-Z-W42-S1 (`2.0.0_SA_COO~Z`, 2026-09-19 ~07:4xZ) -- THE EXCERPT CONTRACT GAP, DISARMED HERE:**
MEASURED by the issuer on the pool: `filings/v1/6861_JP_Equity/doc-1defdb68a7ffd3b7.source.json` (rk-38's RESOLVED YUHO object,
parser 2.0.0) carries `excerpt: None` and no `sections`, while `filings/v1/CAT_US_Equity/000001823026000008.source.json` (the EDGAR
path) carries `excerpt {items, item_keys, text, chars, excerpt_sha256, truncated_items, item_chars, item_full_chars}`; rk-39's
`document.py` CLI writes `sections` (risk/mdna/officers) and nothing assembles them into the analyzer's `excerpt` shape
(`analyze.py:955/1015/1251` read `source_object["excerpt"]`). Both owning cells (rk-38, rk-39) are drained; no live writer holds
those files. RULED: (i) your `<paths>` are WIDENED to `lib/research/filings/document.py`, `lib/research/filings/fetch.py` and
`lib/research/filings/battery.py` for this one purpose; (ii) STEP 0, before AC2: implement `document.sections_to_excerpt(sections,
family)` producing the analyzer's exact `excerpt` shape (items in the fixed order risk, mdna, officers -- each item `{key, text}` --
`item_keys`, joined `text`, `chars`, `excerpt_sha256` over `text`, `truncated_items`, `item_chars`, `item_full_chars`; the EDGAR path
in `fetch.build_source_object` is the reference shape, read it and match it field for field), call it from BOTH the `document.py`
CLI (so `.scratch/docs/<key>.source.json` carries `excerpt`) and `fetch.build_battery_source_object` (so a battery landing carries
`excerpt` for every family, never `None` on a RESOLVED object), with a unit arm on the Keyence fixture asserting `excerpt` is
present, non-empty and sha-stable; (iii) then RE-LAND the Keyence pool object with the battery CLI exactly as rk-38's AC4 ran it
(`python -m lib.research.filings.battery --security-key 6861_JP_Equity ... --write-pool`; a validation-name pool write on an
unserved key, rk-38's own act shape, no pair owed; print the pool receipt and read it back: `excerpt` non-empty), and record the
Keyence object's new key in your report; (iv) AC2-AC6 then run exactly as written. Nothing here touches a covered name or any
served route.

**AMENDMENT 2 (issuer, 2.0.0_SA_COO~Z, 2026-09-19 ~09:0xZ, disarming row `AMGT_RESAPP-Z-W42-S2`).** The row is correct: AC3's
literal invocation feeds `analyze.py` the LOCAL object (`--source-json .scratch/docs/6861_JP_Equity.source.json`, AC2's own
output), and `main()` reads `form`, `filing_date`, `url` and `parser_version` unconditionally (`analyze.py:1079-1091`, `:1158`,
`:1408-1411`) because the analyzer's contract is the shape `fetch.build_battery_source_object` returns. The gap is on the
PRODUCER side, so the remedy is SCHEMA PARITY in `document.py` (already in your `<paths>`), never a tolerance edit in `main()`,
which stays `AMGT-rk-42`'s wall. RULED: **(v) STEP 0, before AC3:** `build_local_source_object` carries every key the analyzer
reads that the battery object carries, with local values: `form` = the detected family token (the object's own `family`),
`filing_date` = `period_end["date"]` (None when unknown), `url` = None (the object is document-layer-local; you MAY add
`local_source` naming the input path), `parser_version` = a `PARSER_VERSION` constant defined IN `document.py` (a string,
e.g. `"document-layer-local/1"`; do not import it from `fetch.py`, which imports `document.py`), plus `entity_name`,
`entity_evidence`, `verified_site`, `verified_site_reason`, `officer_section` = None when the local path cannot know them.
Extend the STEP 0 unit arm: the local object's key set is a SUPERSET of the keys `main()` indexes (assert each of the four
is present; `form` equals `family`; `parser_version` is a non-empty string). Then AC3-AC6 run exactly as written; the row's
`disarm` is this amendment (cite it in your report). Nothing else in the order changes.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/filings/passages.py
lib/research/filings/analyze.py
lib/research/filings/drafting_build.py
lib/research/filings/translate.py
lib/research/filings/__init__.py
lib/research/filings/tests/test_translation.py
lib/research/filings/tests/test_filings.py
lib/research/drafting/verbatim.py
lib/research/drafting/tests/test_drafting.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~42/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-40.translation-design-a.md
lib/research/filings/document.py
lib/research/filings/fetch.py
lib/research/filings/battery.py
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant; this block governs WRITES. In `analyze.py` you
  own `pass_1` `:277-302`, the cache functions `:320-372` (prompt version), `resolve_pass_1` `:375-437`, `pass_2`
  `:444-453`, `_clean_item_text` `:551-555`, `_apply_point_verification` `:814`, `build_analysis` `:892-959` (language,
  text_encoding, translation fields), `analyze_source` `:982-990`, the PROMPT/ANALYZER version constants `:60-61` --
  NOT `main()` `:1101-1231`, the writer block `:1210-1230` or `DEFAULT_UNIVERSE_PATH` `:1095-1097`, which are
  `AMGT-rk-42`'s. In `drafting_build.py` you own `:70-128` (`_QUOTED_RE`, `MIN_QUOTE_TOKENS`, `longest_verbatim_run`,
  `quoted_spans`) and the sentence fields in `draft()` `:197-206`; the HOLD and the split counts in `:188-247` and
  `lib/research/drafting/pipeline.py` are `AMGT-rk-41`'s. `fetch.py`, `document.py`, `battery.py`, `batch.py` are not
  yours. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~42 <0.9.0_WK_AMGT_RESAPP~42@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN (not your surface; the page's rendering of `text_translated` labelled as a translation is a later portal
cell -- this order makes the DATA carry it). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification
or freshness checker.** Secrets through `comp-secrets` only (the model key, as above). **EGRESS, EXACTLY:** the Anthropic
API on the Keyence document within the USD 3.00 cap, and the Keyence PDF GET that `AMGT-rk-39`'s CLI performs; nothing
else, no other vendor. **No pool write of any kind** (`--write-pool` is never passed; every object lands in `.scratch/`).
**No non-ASCII in anything you write** (Japanese in code and prompts is `\u` escapes; `len(b) - len(b.decode('utf-8'))
== 0` on every file you touch). **PUSH: never.** Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- translating the passages first is that route.
**A COUNT BAR PRINTS its denominator** (findings, citations, passages, controls).
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W42-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize it)
and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-40"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m unittest discover -s lib/research/filings/tests -p "test_*.py" -q 2>&1 | tail -5 && python -m unittest discover -s lib/research/drafting/tests -p "test_*.py" -q 2>&1 | tail -3</invocation><expect>both runs end "Ran N tests" and "OK". The filings run includes the new translation tests: (1) a kana fixture's passage map keeps 100% of its characters (the pre-existing test_ascii_normalisation test is replaced, not weakened -- the object now records non_ascii_chars); (2) pass 1 sends a content document with one block per passage and a stubbed content_block_location citation on block 3 resolves to P0003 ONLY when its cited_text lies inside that passage, and to nothing when it does not; (3) the character-level run finder on a 40-character unspaced sentence finds a run of at least 12 characters inside its cited passage, the same run against the NEIGHBOUR passage is refused, and the run with ONE character mutated is refused; (4) an English fixture (test_filings SOURCE_OBJECT) records translation skipped english and the stub receives exactly TWO calls (no translation call); (5) a non-English fixture records translation fields on every served item with translated true, source_language, translator model and prompt version, translated_at and passage_ids, and a count mismatch from the stub records a FAILED translation with items left original-only</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-40"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.filings.document --pdf-url "https://www.keyence.co.jp/pdf/AnnualSecuritiesReport_202606_ja.pdf" --sha256 1defdb68a7ffd3b70317786dbb57b606ca5d46ef67844da9977dde6a0448cf9d --security-key 6861_JP_Equity --family auto --out-dir .scratch/docs 2>&1 | tail -3 && python -c "
import json
from lib.research.filings import passages
src = json.load(open('.scratch/docs/6861_JP_Equity.source.json', encoding='utf-8'))
ex = src['excerpt']
pm = passages.build_passage_map(ex['text'], ex['items'])
nonblank = sum(len(l.strip()) for l in ex['text'].split('\n') if l.strip())
covered = sum(p['chars'] for p in pm)
kept = sum(len(p['text']) for p in pm)
cjk_src = sum(1 for ch in ex['text'] if ord(ch) > 127)
cjk_kept = sum(1 for p in pm for ch in p['text'] if ord(ch) > 127)
print('passages', len(pm), 'empty', sum(1 for p in pm if not p['text'].strip()), 'pct_excerpt_chars_in_passages', round(100.0 * covered / max(nonblank, 1), 1), 'pct_passage_chars_kept', round(100.0 * kept / max(covered, 1), 1), 'non_ascii_kept', cjk_kept, 'of', cjk_src)
"</invocation><expect>precondition (i) on the real Yuho excerpt: passages N (the validation built 28 with 7 stored empty), empty 0, pct_passage_chars_kept at or above 99.0 (the validation measured 6.8% surviving to_ascii), non_ascii_kept equal to the non-ASCII count of the passage-covered text -- printed with both denominators. Language on the source object reads ja</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-40"><invocation>cd "$(git rev-parse --show-toplevel)" && export ANTHROPIC_API_KEY="$(comp-secrets get anthropic-api-key --reveal | grep '^value:' | sed 's/^value:[[:space:]]*//')" && python -m lib.research.filings.analyze --security-key 6861_JP_Equity --source-json .scratch/docs/6861_JP_Equity.source.json --no-fetch --cache-dir .scratch/filings_cache --out-dir .scratch/keyence --stage pass1 2>&1 | tail -4 && python -m lib.research.filings.analyze --security-key 6861_JP_Equity --source-json .scratch/docs/6861_JP_Equity.source.json --no-fetch --cache-dir .scratch/filings_cache --out-dir .scratch/keyence 2>&1 | tail -12</invocation><expect>precondition (ii) live on Keyence (the two invocations are the pass-1 cache split the 115 s bound already forced, analyze.py:308-317; the second reads cached true): PASS1 prints citations N and resolved M with M at or above 95% of N; a CITATIONS line prints "blocks per citation min/median/max" with min 1, median 1 and max AT MOST 2, and beside it "two_block_citations K of N" with K/N at or below 0.10 (AMENDMENT 3, row W42-S5: the validation measured 1/1/1 on a different document; a genuine two-block span resolved correctly is the fixed behaviour of row S3, not a defect -- the literal 1/1/1 was a measurement, never a rule) and "cited_text in original N of N"; ITEMS prints total and cited with cited at or above 90% and language ja; the DRAFTING line prints; USD printed under 0.60 for this run; NOT-UPLOADED lines for the three objects (no --write-pool)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-40"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.filings.translate --analysis .scratch/keyence/filings_v1_6861_JP_Equity_doc-1defdb68a7ffd3b7.analysis.json --controls 2>&1 | tail -8</invocation><expect>precondition (iii) and the two discriminating controls, denominators printed: "VERBATIM-CHARS: K of M served findings carry a run of at least 12 characters inside a passage they cite" with K/M at or above 0.90 (the validation held 70 of 71) -- AMENDMENT 3, row W42-S5: the floor binds the PROSE-CITED findings. Print in addition "TABLE-DERIVED: T of M findings" listing each finding id whose cited passages carry no run of 12 characters of non-numeric text (a passage whose characters are more than half digits, punctuation or whitespace is a table line), and grade the floor as K / (M - T) at or above 0.90; a table-derived finding is served with its `verbatim` field reading table_derived and the number(s) it carries located in the cited passage (a NUMBER-CONTROL line: "found N of T"; any not found FAILS); "NEIGHBOUR-CONTROL: refused K of K"; "MUTATION-CONTROL: refused K of K" (the validation refused 70/70 and 68/68) -- a control that refuses fewer than all fails this criterion; and "VERBATIM-WORDS: 0 findings graded on the token rule" (the sentence script is unspaced, so the character rule ran). The analysis file name is the out-dir rendering of the pool key (key.replace('/', '_'), analyze.py:1220); record the actual file name if the accession differs</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-40"><invocation>cd "$(git rev-parse --show-toplevel)" && export ANTHROPIC_API_KEY="$(comp-secrets get anthropic-api-key --reveal | grep '^value:' | sed 's/^value:[[:space:]]*//')" && python -m lib.research.filings.translate --analysis .scratch/keyence/filings_v1_6861_JP_Equity_doc-1defdb68a7ffd3b7.analysis.json --out .scratch/keyence/6861_JP_Equity.translated.json 2>&1 | tail -8</invocation><expect>the translation of the OUTPUT, live: "TRANSLATED: N of N lines" (every served item plus the driver's series, unit and why), each line carrying translated true, source_language ja, translator model and prompt_version rj6-translate/1, translated_at, and the original text with its passage_ids beside it; "RELOCATE-CONTROL: 0 of N translations found verbatim in the original" (the validation measured 0 of 71 -- a translation that relocates would mean the analysis was not in the original language); USD printed under 0.30; the running total for this order printed and under 3.00</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-40"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json
doc = json.load(open('.scratch/keyence/6861_JP_Equity.translated.json', encoding='utf-8'))
from lib.research.filings.drafting_build import build_drafting_document
d = build_drafting_document(doc)
sents = [s for sec in d['sections'] for s in sec['sentences']]
with_tr = sum(1 for s in sents if s.get('text_translated') and (s.get('translation') or {}).get('translated') is True)
orig_ok = sum(1 for s in sents if s.get('text_original', s.get('text')) == s.get('text'))
print('served_sentences', len(sents), 'with_translation', with_tr, 'gate_on_original', orig_ok, 'quote_methods', sorted({s.get('quote_method') for s in sents}))
"</invocation><expect>the drafting document built from the translated analysis: served_sentences N greater than 0 (the estate path served 0 and dropped 40 on Keyence), with_translation N of N, gate_on_original N of N (the sentence's text is the original and the gate ran against the original passage), and quote_methods containing longest-verbatim-run-chars or model-marked and NOT none-found on any served sentence (a sentence with no span is HELD by AMGT-rk-41's gate when that cell has landed; if it has not, print the count of none-found instead and record it)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.
AC3 is the one live analysis run; AC4-AC6 read its stored objects and make at most one more call (AC5).

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~42/AMGT_RESAPP.TO-AMGT-rk-40.translation-design-a.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, with the order's total USD spend.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~42</slot>
<fabric>site-z</fabric>

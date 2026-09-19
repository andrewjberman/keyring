# AMGT_RESAPP task order -- `AMGT-rk-39` -- the document layer: PDF reflow, family-keyed cutting, an empty cut is a FAILED cut, the 20-F riskfactors fallback removed

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-39</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~41</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; no schedule is read
  or written; the scheduled batch task stays DISABLED and is not touched.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes no AWS resource at all (every output lands under the worktree's
  `.scratch/`); it grants no permission, provisions nothing and touches no Terraform.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~41`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and every path in
section 3 exists; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~41;`. **NEVER RUN AN INSTALL** -- `pymupdf` 1.28.2 (`import fitz`) and
`pypdf` 6.16.2 are ALREADY installed on this device's Python 3.11.9; you use the first and never add a package.

## 1. THE CELL, inlined in full -- `AMGT-rk-39` (R14-F2; FWD-18; validation V3; Exec Management E10)

**The analysis row, verbatim (ROUND_ANALYSIS.round13.md s.4 @9c8e04cd9a):** *"a document layer for non-EDGAR reports:
PDF reflow (9.3% -> 91.6% coverage measured), family-keyed cutting, and an EMPTY cut recorded as a FAILED cut with its
reason; the 20-F `riskfactors` wrong-object fallback removed (D9)"* -- serves FWD-18, V3, E10; co-sign: no.

**The PRD rules this serves (v0.13 @1699960261).** `C-FILINGS-ANALYZER` `:676-681`: *"(c) KNOWN FAMILY -- a document
family the section cutter and the roster can parse; a cut from a family the cutter does not know FAILS (c) and never
passes as a section ... the family is recorded because cutting and roster parsing are BY FAMILY"*; section-10 evidence
`:1670-1671`: *"D9: an unknown document family must fail (c)"*. `C-FILINGS-TRANSLATION` `:707-708`: *"Language is
detected there [after the cutter and the passage map] and recorded on every document"*. Section 10 `:1615-1616`: *"an
explicit terminal state ... never a silent skip and never an empty success"*. `C-PRODUCTION-HOME` `:1646-1647`: *"A dry
run writes nothing, anywhere."*

**1.1 The measured current state (read at HEAD; `lib/research/filings/` last moved @db6c40083f).**
- **D8** `fetch.py:103-152` -- `SECTION_PATTERNS` knows `10-K` and `20-F` only; `extract_sections()` `:329-350` raises
  `ValueError` for any other form (`:336-338`). There is no PDF reader and no company-site or regulator family anywhere
  in the package.
- **D9** `fetch.py:128` -- the 20-F risk start patterns end in the BARE `r"riskfactors"`; with the unbounded fallback at
  `:316-322` (`require_bounded False`, closed by the cap) it cut **70,000 characters of a patient story** from CSL's
  annual report when that PDF's text was run under 20-F rules (validation s.5 D9; the run printed
  `20-F cut chars {'risk': (70000, 568529), 'mdna': (0, 0), 'officers': (0, 0)}` with the risk text opening
  *"risk factors on one side with letting a child be a child"*). A wrong-object excerpt that would pass as a section.
- **E10** `fetch.py:411` and `:440-447` -- when the officer pattern finds nothing, `officer_section` is persisted as
  `{"item": None, "text": "", "chars": 0, "sha256": None, "extracted": False}`: an EMPTY SUCCESS. Measured on the served
  plane: ASML and PBR carry a 20-F whose Item 6 was never cut, and downstream the roster reads them as RESOLVED with 0
  officers (intake E2). `extract_sections()`'s own docstring `:333-334` says the empty text is "visible as missing,
  never a blank success" -- but nothing downstream reads `chars == 0` as a failure, so it IS a blank success.
- **D12** `passages.py:146` and `:174` -- one paragraph per LINE, a line under 60 characters is a heading. Raw PDF line
  text (`page.get_text()`) puts 9.3% (CSL) and 1.8% (Keyence) of the excerpt into passages; the validation's block reflow
  (PyMuPDF `page.get_text("blocks")`, lines joined with `""` across CJK and `" "` otherwise, a trailing hyphen repaired)
  lifted that to 91.6% and 92.4% (validation s.2 row "passages", s.5 D12).
- **D11** -- no language detection in `fetch.py`, `passages.py` or `analyze.py`.
- The validation's two step-4 documents, by URL and content hash (validation `s05_download.json`):
  CSL `https://investors.csl.com/pdf/be88bd1b-9d53-409a-9d6e-43da41dae1d5/Platform/ListPage/CSL-Statutory-Accounts-for-FY2026.pdf`
  sha256 `9fa16d9acef82304f8a63dee894ef9c58163b459af6e2b25d8df261105939035`, 7,046,504 bytes, 175 pages, English;
  Keyence `https://www.keyence.co.jp/pdf/AnnualSecuritiesReport_202606_ja.pdf` sha256
  `1defdb68a7ffd3b70317786dbb57b606ca5d46ef67844da9977dde6a0448cf9d`, 940,557 bytes, 78 pages, Japanese (the FY57 Yuho).
  A download whose sha256 differs from the recorded one is a DIFFERENT document: record it, do not silently proceed.

**1.2 What you build -- NEW `lib/research/filings/document.py`, and `fetch.py` made to use it.**
1. `FAMILIES = ("10-K", "20-F", "ANNUAL-REPORT", "YUHO")` -- the declared domain. ESEF is NOT declared: no validation name
   reaches step 3 with a held filing, so a cutter for it would be claimed without being exercised; an ESEF document
   fails (c) with `family ESEF: no cutter declared` until a cell exercises one.
2. `pdf_to_text(pdf_bytes) -> {"text", "pages", "reflow": {"raw_lines", "blocks", "hyphens_repaired", "cjk_joins"}}` --
   the block reflow described in 1.1, on `fitz`.
3. `detect_family(text, hint=None) -> {"family", "evidence", "known": bool}` -- `hint` is an EDGAR form when the caller has
   one (10-K / 20-F pass straight through); otherwise the cover region decides: YUHO when the first pages carry the title
   `\u6709\u4FA1\u8A3C\u5238\u5831\u544A\u66F8`; ANNUAL-REPORT when they carry `Annual Report` together with
   `Directors' Report` / `Financial Report` / `Operating and Financial Review` / `Remuneration Report`; otherwise
   `{"family": "UNKNOWN", "known": False, "evidence": ...}`. Evidence names the matched phrase and its character offset.
4. `detect_language(text) -> {"language", "cjk_share", "kana_share", "hangul_share", "ascii_letter_share"}` -- a
   script-share rule with no library (none is installed): `ja` when kana share > 0.02, `zh` when cjk share > 0.3 with no
   kana, `ko` on hangul, `en` when ascii letters > 0.5 of letters, else `unknown`. Printed shares make a wrong detection
   visible (PRD `:707-708`).
5. `period_end(text, family) -> {"date", "evidence"}` -- ANNUAL-REPORT: `year ended DD Month YYYY` / `for the year ended
   ...`; YUHO: `\u81EA YYYY\u5E74M\u6708D\u65E5 \u81F3 YYYY\u5E74M\u6708D\u65E5` (the end date); 10-K/20-F: the EDGAR
   `reportDate` the caller passes. None with a reason when nothing matches.
6. `cut(text, family) -> {"sections": {key: {"status": "OK" | "FAILED", "item", "text", "chars", "full_chars",
   "truncated", "reason"}}, "full_chars"}` -- `SECTION_PATTERNS` moves here from `fetch.py:103-152`, keyed by FAMILY:
   `10-K` and `20-F` unchanged EXCEPT the bare `r"riskfactors"` at `:128` REMOVED; `ANNUAL-REPORT`: risk from
   `Principal risks` / `Risk management` / `Key risks` / `Material business risks` closed by the next top-level heading,
   mdna from `Operating and Financial Review` / `Financial review` / `Review of operations`, officers from
   `Board of Directors` / `Directors` / `Executive leadership` / `Senior management` / `Key management personnel`;
   `YUHO`: risk `\u4E8B\u696D\u7B49\u306E\u30EA\u30B9\u30AF`, mdna
   `\u7D4C\u55B6\u8005\u306B\u3088\u308B\u8CA1\u653F\u72B6\u614B`, officers `\u5F79\u54E1\u306E\u72B6\u6CC1` -- every
   non-ASCII heading written as a `\u` escape and VERIFIED by you against the PDF's own text at the run (print the
   matched heading). A key whose patterns qualify no heading, or whose body is under `_MIN_SECTION_CHARS`, is
   `status: FAILED` with a reason naming the patterns tried, how many raw matches each had, and why each was disqualified
   (contents line / not at line start / unbounded and short). NEVER `text: ""` as a success.
7. `fetch.py`: `extract_sections(text, form)` delegates to `document.cut(text, family=form)` and keeps its name and
   return shape plus `status`/`reason` per key; `build_source_object` writes `officer_section` as either the cut section
   (`status: "OK"`) or `{"status": "FAILED", "item": <label>, "reason": <the cut's reason>, "text": "", "chars": 0,
   "extracted": False}` (E10); the excerpt is built only from `OK` items and a document with NO `OK` item is
   UNRESOLVED-SOURCE with the per-key reasons (today's `:397-407` message gains them). `PARSER_VERSION` -> `1.1.0`
   (`AMGT-rk-38` bumps to 2.0.0 when it lands after you; whichever lands second owns the final value).
8. A CLI for proofs and for `AMGT-rk-40`'s reuse: `python -m lib.research.filings.document --pdf-url URL --sha256 HEX
   --security-key K --family F --out-dir DIR [--pdf-file PATH]` downloads (or reads) the PDF, verifies the hash, reflows,
   detects family and language, cuts, and writes `DIR/<K>.source.json` in the source-object shape (`status RESOLVED`,
   `filing_identity.source: "document-layer-local"`, `accession: "doc-<sha256[:16]>"`, `family`, `language`,
   `battery: null`) -- a LOCAL artifact only; `--write-pool` does not exist on this CLI.
9. Tests in `lib/research/filings/tests/test_document.py` (fixtures are synthetic text; the two real PDFs are read by
   the criteria, not by the unit tests).

**1.3 The validation bar (`C-VALIDATION-NAMES`).** Proven on CSL's and Keyence's real documents (the two URLs in 1.1)
and on planted fixtures. NO fleet run, NO re-run of the covered 33: the ASML/PBR empty cuts are the MEASURED instance of
E10 and are NOT re-fetched here -- the fixture mirrors them. No model call anywhere in this order.

## 2. WHERE THIS CAME FROM

**ROUND 14**, on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis s.4 row R14-F2 @9c8e04cd9a; intake E10 and the validation's
V3 / D8 / D9 / D11 / D12 (@b527b93214). PRD v0.13 @1699960261: `C-FILINGS-ANALYZER` `:676-681`, `C-FILINGS-TRANSLATION`
`:707-708`, section 10 `:1615-1616`, `C-PRODUCTION-HOME` `:1643-1650`, `C-VALIDATION-NAMES` `:1652-1658`. The COO's
round-14 decomposition record for this cell in `AMGT_RESAPP_DECOMP.md` is the postulate paragraph landed beside this
order.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/filings/document.py
lib/research/filings/fetch.py
lib/research/filings/__init__.py
lib/research/filings/tests/test_document.py
lib/research/filings/tests/test_filings.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~41/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-39.document-layer-family-cut.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant; this block governs WRITES. `passages.py` and
  `analyze.py` are `AMGT-rk-40`'s; `battery.py` is `AMGT-rk-38`'s; `batch.py` is `AMGT-rk-42`'s. In `fetch.py` you own
  `SECTION_PATTERNS` `:103-152` (moved out), `extract_sections` `:329-350`, the officer-section write `:411` and
  `:440-447`, the no-item message `:397-407` and `PARSER_VERSION` `:56` -- nothing else in that file. Scratch is
  `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~41 <0.9.0_WK_AMGT_RESAPP~41@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or
freshness checker.** Secrets through `comp-secrets` only; this order needs none. **EGRESS, EXACTLY:** two GETs, the
CSL and Keyence PDFs at the URLs in 1.1 (the validation's own downloads, within the bar); nothing else, no vendor, no
model call. **No pool write of any kind.** **No non-ASCII in anything you write** (every Japanese heading is a `\u`
escape; `len(b) - len(b.decode('utf-8')) == 0` on every file you touch). **PUSH: never.** Your work is LOCAL; LD-0522
puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR PRINTS its denominator** (non-blank excerpt characters; raw matches per pattern; pages).
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W41-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize it)
and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-39"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m unittest discover -s lib/research/filings/tests -p "test_*.py" -q 2>&1 | tail -5</invocation><expect>the last lines read "Ran N tests" and "OK", N at least the pre-existing count plus the new document tests, which include: (1) PLANTED D9 -- a 20-F-shaped fixture whose only "risk factors" phrase sits mid-sentence inside a story, with no qualified Item 3.D heading, cuts to status FAILED for risk with a reason naming the patterns tried, never a text; (2) PLANTED E10 -- a 20-F fixture with Items 3.D and 5 present and NO Item 6 yields officer_section.status FAILED with a reason, and build_source_object (fetch stubbed) persists that FAILED block, never chars 0 with extracted False as a success; (3) an UNKNOWN family fixture returns known False and cut() is never called on it as a section; (4) a YUHO fixture carrying the three escaped headings cuts all three OK; (5) detect_language on an ASCII fixture reads en and on a kana fixture reads ja, shares printed; (6) TheSectionDiscriminator's two pre-existing tests still pass (the 10-K rules did not move)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-39"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.filings.document --pdf-url "https://investors.csl.com/pdf/be88bd1b-9d53-409a-9d6e-43da41dae1d5/Platform/ListPage/CSL-Statutory-Accounts-for-FY2026.pdf" --sha256 9fa16d9acef82304f8a63dee894ef9c58163b459af6e2b25d8df261105939035 --security-key CSL_AU_Equity --family auto --out-dir .scratch/docs --coverage 2>&1 | tail -12</invocation><expect>sha256 VERIFIED against the recorded hash (a mismatch aborts with both hashes printed); pages 175; the COVERAGE line prints, for the SAME excerpt text, the share of non-blank characters that land in passages (passages.build_passage_map) under raw page lines versus block reflow -- raw near the validation's 9.3%, reflow at or above 90.0% (the validation measured 91.6%) -- with both denominators printed; family ANNUAL-REPORT with the matched cover phrase and offset; language en with shares; period_end 2026-06-30 with its evidence; .scratch/docs/CSL_AU_Equity.source.json written with accession doc-9fa16d9acef82304</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-39"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.filings.document --pdf-url "https://www.keyence.co.jp/pdf/AnnualSecuritiesReport_202606_ja.pdf" --sha256 1defdb68a7ffd3b70317786dbb57b606ca5d46ef67844da9977dde6a0448cf9d --security-key 6861_JP_Equity --family auto --out-dir .scratch/docs --coverage 2>&1 | tail -12</invocation><expect>sha256 VERIFIED; pages 78; the COVERAGE line prints raw-lines share near the validation's 1.8% and reflow share at or above 90.0% (the validation measured 92.4%), denominators printed; family YUHO with the matched title escape and its offset; language ja with kana and cjk shares printed; period_end 2026-03-20 with its evidence; .scratch/docs/6861_JP_Equity.source.json written with accession doc-1defdb68a7ffd3b7</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-39"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json
from lib.research.filings import document
src = json.load(open('.scratch/docs/CSL_AU_Equity.source.json', encoding='utf-8'))
text = src['document_text']
for family in ('20-F', 'ANNUAL-REPORT'):
    cut = document.cut(text, family)
    for key, sec in cut['sections'].items():
        print(family, key, sec['status'], 'chars', sec['chars'], 'full', sec['full_chars'], 'reason', (sec.get('reason') or '')[:160], 'opens', repr((sec.get('text') or '')[:60]))
"</invocation><expect>the D9 pair on the SAME text: under family 20-F every key reads status FAILED with a reason (the bare riskfactors fallback is gone, so no 70,000-character patient story is cut -- chars 0 for risk, where the validation's run printed 70000); under family ANNUAL-REPORT the risk and mdna keys read status OK with chars at least 1500 each and an opening that is a risk / operating-review heading, not a story; the officers key prints its status either way with its reason when FAILED. The source object must carry document_text (the full reflowed text) for this read; if the CLI does not persist it, the worker adds it to the LOCAL object shape only</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-39"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json
from lib.research.filings import document
src = json.load(open('.scratch/docs/6861_JP_Equity.source.json', encoding='utf-8'))
cut = document.cut(src['document_text'], 'YUHO')
for key, sec in cut['sections'].items():
    print('YUHO', key, sec['status'], 'chars', sec['chars'], 'full', sec['full_chars'], 'heading_matched', json.dumps(sec.get('heading_matched'), ensure_ascii=True), 'reason', (sec.get('reason') or '')[:160])
print('excerpt_items_ok', [k for k, s in cut['sections'].items() if s['status'] == 'OK'], 'of', len(cut['sections']))
"</invocation><expect>on the Yuho: risk and mdna read status OK with chars at least 1500 each (the validation's scratch cutter cut both; the estate cut 0 characters), each printing the heading it matched as an escaped string equal to the pattern this order names; officers prints its status and, when FAILED, a reason -- never an empty text as a success; the last line counts the OK items over 3 declared</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.
AC2 and AC3 download once and reuse the bytes from `.scratch/docs/` on any re-invocation (the CLI's `--pdf-file`).

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~41/AMGT_RESAPP.TO-AMGT-rk-39.document-layer-family-cut.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~41</slot>
<fabric>site-z</fabric>

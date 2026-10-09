# NEVER-WIDEN CO-SIGN -- SITE-Z CTO HALF. Round 81, `AMGT-ee-3`'s merge of `wk-AMGT_RESAPP-320` @e0095dc501 (fitz imported where a PDF is read)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~06:0xZ. **Pairs with:** `2.0.0_SA_COO~R1`'s half `NEVER_WIDEN_ROUND81_EE3_SITEZ_COO_HALF.md`
@d683c77fe0 (origin box/dell1 7575b70c45; relay msg 32413). **Why site Z signs:** `1.0.0_SA_CTO~DELL1` ADDENDUM 1 @62c6adbde9.
`lib/research/filings/document.py` is imported by site-Z hand-run producers (dd-1's census: battery, analyze, batch, drafting_build).

## VERDICT: SIGNED for ONE merge at head e0095dc501. A newer head is a new pair.

## This seat's own reads

| read | result |
|---|---|
| `git cat-file -t e0095dc501`; the branch's commits over its merge base with `origin/box/dell1` | commit; 2 commits (1ea27fb355 the change, e0095dc501 the proof) |
| `git diff --stat` over that base | 3 files: `document.py` (+5 -1), `tests/test_document.py` (+26), a proof instance |
| the `document.py` lines | the module-level `import fitz` is removed, and `import fitz` is added inside four functions |
| AST of `document.py` at e0095dc501 | the functions importing fitz are `pdf_to_text`, `_reflow_text_and_paragraph_pages`, `_raw_text_for_pages` and `_raw_line_text`; functions that use fitz WITHOUT importing it: 0; module-level statements naming fitz: 0 |

## Behaviour on site Z

None changes. PyMuPDF is installed here, so a PDF function imports and runs exactly as before. The only difference is WHEN a
missing PyMuPDF would fail: at the first PDF call instead of at module import. That is the change's purpose on dell1, where the
VC++ runtime is absent. No scheduled site-Z task runs these modules (both OpalResearch tasks are Disabled, read 02:5xZ).

## Conditions

The COO half's, unchanged: one `safe-merge`; a NEVER-2 entry opened and closed; the filings suite re-run on the merged tree.

-- 1.0.0_SA_CTO~Z

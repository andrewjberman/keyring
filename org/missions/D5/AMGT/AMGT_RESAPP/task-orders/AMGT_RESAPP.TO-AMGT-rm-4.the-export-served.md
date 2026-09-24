# AMGT_RESAPP task order -- `AMGT-rm-4` -- THE EXPORT SERVED: `?format=rich` on the existing `/print` leaf, the default byte-identical, the client's second action; no deploy here

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rm-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~143</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, trust or grant moves; nothing deploys on this cell.
comp-adversary: RUN by the issuer over the round-37 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. The adapter is exercised IN-PROCESS over the harness fixtures (the landed model block, thesis bundle, peer set and posture the fixtures carry); no S3 read is required and none is made; no vendor call; no fetch outside localhost.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~143`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. First act:
print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, `test -d org && test -d .tools && echo TREE-OK`,
`grep -c 'def build_rich_text' lib/research/print/render_pack.py` (rl-10's producer, 1 = present; 0 = BLOCKING row, stop),
`grep -n 'def _print_pack' lib/research/api/scoped_amgt.py`. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~143;`. **NEVER RUN AN INSTALL. No vite dev server on this cell.** Never push,
merge, rebase, `checkout --` or `clean`. **Portal is a NESTED repository at `<worktree>/portal`:** portal files are committed
inside it (`cd portal && bash ../.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~143 <0.9.0_WK_AMGT_RESAPP~143@opal.agent>" -F <msgfile> -- <paths>`),
then the outer commit carries `portal`, your `lib/` edits and your deliverables (a `.py` edit passes `.tools/commit-gate.sh`
inside safe-commit: py_compile, ds-precommit, ruff py39 -- one statement per line, imports on their own lines). Messages
PURE ASCII via the Write tool. Scripts and logs under `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~143/`, never `.scratch/`.

## 1. THE CELL -- `AMGT-rm-4` (round 38, decomposition s.46) -- WAVE 0

**`FWD-30` branch (b), servable.** Round 37's rl-10 built `lib/research/print/render_pack.py:build_rich_text(security,
model_block, thesis_bundle=None, peer_set=None, posture=None, out_dir=None)` beside `build_pack`, proved parity against the
actual page (`exportCompare.harness.cjs`: FIGURES 162/162, CITES 43/43, ABSENCES 5/5, `EXPORT-COMPARE OK`), and wrote the
ROUTE ASK rather than the route. **`1.0.0_SA_CTO~Z` APPROVED it as recommended (R-57 @`ba78f1d3d5`):** reuse the EXISTING
`/print` leaf with `format=rich` as a QUERY PARAMETER, default `pdf` byte-identical to today, returning `text/markdown`;
no new route, no new path segment (a query parameter does no path matching, so it cannot hit the gateway route-miss class);
NO never-widen pair because the default path is a verified DELTA=0. R-58 placed it in this round and named the DEPLOY the
AE lane's under its own NEVER-2 entry -- **you do not deploy**; `AMGT-rm-7` does, after your branch is on CLOUD.

**WHAT YOU BUILD.** (1) `lib/research/api/scoped_amgt.py:_print_pack(security_key, identity=None, fmt="pdf")`: the dispatch
at the `print` leaf reads `_query(event).get("format", "pdf")` and passes it; `fmt == "pdf"` is TODAY'S PATH, untouched --
the same `build_pack(display_form, block)` call, the same base64 body, the same headers; `fmt == "rich"` hands
`build_rich_text` the block THIS function already read (one reader, one overlay -- rk-6's discipline kept) plus the thesis
bundle, peer set and posture the adapter already reads (`read_thesis_bundle`, `read_peer_set`, `read_posture` or whatever
the adapter's own readers are named -- use them, never a new reader), and returns `{"statusCode": 200, "headers":
{"Content-Type": "text/markdown; charset=utf-8"}, "body": <the document as a str>, "isBase64Encoded": False}`; any other
`fmt` raises the adapter's own `AdapterError(400, ...)` naming the two legal values. The route table's `/print` line is
UNCHANGED (a query parameter is not a route). (2) `portal/src/api/endpoints/amgt-lead-panel.ts`: `printPackPath(securityKey,
format?)` appends `?format=rich` when asked, and `requestRichText(securityKey): Promise<string>` beside `requestPrintPack`
(same auth-header shape, `response.text()`); the pdf path's string is unchanged. (3) `PrintExportAction.tsx`: a SECOND
action in the same secondary style ("Export rich text (.md)") that calls `requestRichText` and offers the document as a
download (`Blob` of type `text/markdown`, an object URL, `<a download="<security_key>.md">`), states `idle/generating/
ready/failed` shared with the pdf action's, behaviour of the pdf action unchanged, census 0 kept. (4) Tests:
`lib/research/api/tests/test_print_format_rich.py` -- over the harness fixtures (the landed block and bundles the round-37
harnesses carry under `portal/src/pages/SecurityAnalysis/__harness__/*.json`, read from disk, no S3): the handler with no
`format` returns the pdf response whose body sha256 EQUALS the response from the pre-cell `_print_pack` (call the same
function with `fmt="pdf"` and compare to a call through the dispatch with no query -- and compare to `build_pack`'s own
output sha, the negative control that proves nothing on the default path moved); `format=rich` returns 200
`text/markdown` and its body passes `exportCompare.harness.cjs --rich` when written to a file; `format=xml` returns 400.

## 2. BOUNDS

1. **`_print_pack` is the ONLY adapter function that moves**, and only by the `fmt` branch; `scoped_amgt_route_table()` is
   byte-identical (AC3 prints its diff as empty). No DTO, no query key, no served figure moves; no other leaf reads `format`.
2. **The document contains NOTHING the page does not show** (`C-EXPORT-ADDS-NOTHING`): the handler passes through
   `build_rich_text`'s output unchanged; no summarising, rewording or re-rounding in the adapter.
3. **No deploy.** The Lambda's running bytes do not move on this cell; `AMGT-rm-7` deploys under NEVER-2. Say in your
   report which commit the deploy leg should bind to.
4. **Standing:** no install, no vendor or Bloomberg call, no S3 write or delete, no key hunting, no push, no promote.
   **REFUSE, do not rescue.**

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_print_format_rich.py
lib/research/api/tests/**
lib/research/print/render_pack.py
lib/research/print/tests/**
portal/src/api/endpoints/amgt-lead-panel.ts
portal/src/pages/SecurityAnalysis/components/PrintExportAction.tsx
portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/**
portal/src/pages/SecurityAnalysis/__rendercheck__/**
portal/scripts/ui-class-census.mjs
portal/DESIGN.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~139/ROUTE_ASK_export_rich_text.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~143/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

You WRITE `scoped_amgt.py` (`_print_pack` and its dispatch line only), the new test module, `amgt-lead-panel.ts`,
`PrintExportAction.tsx`, `exportCompare.harness.cjs` (a loader case for the handler's output, if needed) and your
deliverables; every other path is a read-only input.

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rm-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/api/tests/test_print_format_rich.py lib/research/print/tests -q -p no:cacheprovider 2&gt;&amp;1 | tail -5</invocation><expect>THE FORMAT BRANCH PROVEN IN-PROCESS: every test passes -- the default (no format) response body sha256 equals the fmt=pdf response and equals build_pack's own PDF sha (the negative control printed), format=rich returns 200 text/markdown with a non-empty body, format=xml returns 400 through AdapterError naming pdf and rich; the pre-existing print tests still pass; 0 failed</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rm-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~143/handler_rich_to_file.py &amp;&amp; cd portal &amp;&amp; node src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs --rich ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~143/served/BA_US_Equity.md</invocation><expect>THE SERVED DOCUMENT IS THE PAGE'S: a script you write calls the adapter's dispatch with an event carrying rawPath .../security/BA_US_Equity/print and queryStringParameters {format: rich} over the fixture inputs (the adapter's readers patched to the fixture files -- say which), writes the body to served/BA_US_Equity.md and prints its byte size and Content-Type; then exportCompare reads FIGURES / CITES / ABSENCES each page=n rich=n same=n missing=0 extra=0 with n greater than 0 and EXPORT-COMPARE OK</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rm-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -c "from lib.research.api import scoped_amgt as s; print(chr(10).join(s.scoped_amgt_route_table()))" | grep -c "/print" &amp;&amp; git diff $(git merge-base HEAD CLOUD) -- lib/research/api/scoped_amgt.py | grep -E "^[-+]" | grep -v "^[-+]{3}" | grep -c "route_table\|ROUTE_PREFIX" ; cd portal &amp;&amp; node scripts/ui-class-census.mjs src/pages/SecurityAnalysis/components/PrintExportAction.tsx &amp;&amp; npx tsc -b --noEmit; echo "tsc=$?"</invocation><expect>THE ROUTE TABLE UNCHANGED AND THE CLIENT IN PATTERN: exactly ONE /print line in the route table as before; zero changed lines touching route_table or ROUTE_PREFIX in the adapter diff (the format branch lives in _print_pack and its dispatch line only -- print the diff's changed-line count beside it); PrintExportAction.tsx census FILES 1 TOTAL 0 with the second action present (name its label); tsc clean (tsc=0)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~143/AMGT_RESAPP.TO-AMGT-rm-4.the-export-served.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` from the
worktree root. **The status flip is the ISSUER'S**; leave the record face alone and say so. **Report once, naming:** the
pdf sha triple (default, fmt=pdf, build_pack), the rich document's byte size and the three parity lines, the second
action's label, the commit the deploy leg binds to, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** wave 0. The ONE route-touching cell of the round; the change was returned to the CTO before build
(rl-10's ROUTE_ASK) and approved (R-57); the deploy is `AMGT-rm-7`'s (R-58: the AE lane's, under NEVER-2), issued in the
same issuance with the edge rm-4 -> rm-7.

**ISSUER CLOSE-OUT, 2.0.0_SA_COO~Z, 2026-09-24 ~14:0xZ.** Flipped by the ISSUER; the worker left the record face alone.
3 of 3 criteria PASS, proof-of-spec rc=0 VALID (re-run by this seat inside the worker's worktree C:/tmp/wk-amgt-38-143).
AC1: 9 of 9 tests (the new test_print_format_rich.py + the print tests); the sha256 triple default = fmt=pdf = build_pack's own
PDF = f869ba63a722a06fec31b5f75c6d0cd1338c3934a694f5c99f17e9340a5bd387 (the DELTA=0 R-57's no-pair rests on, printed); a mutant
control widening the fmt whitelist made the 400 arm fail and was reverted. AC2: the handler's own dispatch with format=rich over the
fixture inputs wrote served/BA_US_Equity.md (84,784 bytes, text/markdown; charset=utf-8) and exportCompare reads EXPORT-COMPARE OK,
FIGURES 162/162 missing=0 (extra=17, the same shape rl-10's own proven document carries over this producer+fixture and was graded
PASS on), CITES 43/43 missing=0 extra=0, ABSENCES 5 of 5. AC3: exactly one /print line in the route table; 0 of 50 changed adapter
lines touch route_table/ROUTE_PREFIX; PrintExportAction census FILES 1 TOTAL 0 with the second action "Export rich text (.md)";
tsc clean. No rows. Drained @3350abb022 (the worker's code commit 791806b1c9 is the adapter's tip on CLOUD; its instance commit
c542110d7b sits above it); portal DEV 2b410046 (merge of 9ca9ee57), gitlink 9bcbc290 -> 2b410046. THE DEPLOY LEG rm-7 is bound to
3350abb022 by the issuer's message to 0.7.0_AE_CloudOps~A at this close; nothing is served until that seat's NEVER-2 entry closes.

<status>complete</status>
<round>38</round>
<slot>~143</slot>
<fabric>site-z</fabric>

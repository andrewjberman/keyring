# AMGT_RESAPP task order -- `AMGT-rl-10` -- THE EXPORT: measure the landed producer against Andrew's three properties FIRST, then close the "or machine readable rich text" branch ON that producer, and name the route ask rather than make it

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rl-10</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~139</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, trust or grant moves; ONE S3 GET of a landed model block (below) with the seat's ambient credentials, no write.
comp-adversary: RUN by the issuer over the L1 brief at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: at most ONE S3 GET per security of `derived/model_block/<key>/<stamp>/model_block.json` from s3://opal-data-harvest (the adapter's own reader, `lib/research/api/scoped_amgt.read_model_block`, pointed at the pool), for the ONE fixture name BA_US_Equity, only if no landed block is already in the harness fixtures. No vendor call, no Bloomberg call, no S3 write or delete, no fetch outside localhost otherwise.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~139`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. First act:
print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, `test -d org && test -d .tools && echo TREE-OK`,
`test -f portal/src/pages/SecurityAnalysis/components/StatTile.tsx && echo HEADER-MERGED` (the identity header cell has
merged before you; absent = BLOCKING row, stop). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~139;`.
**NEVER RUN AN INSTALL. No vite dev server on this cell.** Never push, merge, rebase, `checkout --` or `clean`. **Portal is
a NESTED repository at `<worktree>/portal`:** portal files are committed inside it
(`cd portal && bash ../.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~139 <0.9.0_WK_AMGT_RESAPP~139@opal.agent>" -F <msgfile> -- <paths>`),
then the outer commit carries `portal`, your `lib/` edits and your deliverables (a `.py` edit passes `.tools/commit-gate.sh`
inside safe-commit: py_compile, ds-precommit, ruff py39). Messages PURE ASCII via the Write tool. Scripts and logs under
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~139/`, never `.scratch/`.

## 1. THE CELL -- `AMGT-rl-10` (round 37, decomposition s.45) -- WAVE 2

**`FWD-30`, Andrew's own clause (~05:0xZ):** *"export option functional with presentation in Opal Brand Guidelines form
mimicking Asset Mgmt team's earnings reports 2pg max or machine readable rich text output."* DONE WHEN: *"the export
produces EITHER (a) a presentation in Opal Brand Guidelines form (deck_generation/DESIGN_BIBLE.md), shaped like the Asset
Management team's own earnings updates, AT MOST TWO PAGES, OR (b) a machine-readable rich-text output; AND a
field-by-field comparison against the page shows the SAME figures, the SAME cites and the SAME absences, with NOTHING in
the export that is not on the page."* ⚠ The OR is Andrew's and is not collapsed: EITHER branch satisfies; the 2-page cap
binds (a) only; "functional" means an artifact a person OPENS.

⛔ **THE EXPORT IS NOT MISSING -- IT IS BUILT, WIRED, AND THREE PROPERTIES SHORT (PRD ADDENDUM B B.4a, `1.0.0_SA_CTO~Z`,
~06:0xZ). YOU DO NOT BUILD A SECOND PRODUCER.** What exists: `PrintExportAction.tsx` in the page header's actions slot
(preview modal, `idle/generating/ready/failed`, PDF iframe); `requestPrintPack()` -> the `/print` leaf ->
`lib/research/api/scoped_amgt.py:_print_pack` -> **`lib/research/print/render_pack.py:build_pack(security, model_block,
out_dir)`**, which returns `(pdf_path, txt_path)`, reads NO store (the caller hands it the block with the fiscal-price
overlay already applied, ONE reader ONE overlay), writes only to a temp dir, and renders an undrafted section as the
literal `[MACHINE-EMPTY: <what belongs here>]`, never a blank that looks finished. The three gaps against his words:
**4+ pages** (each of the template's four blocks starts its own page) against *"2pg max"*; **one security's MODEL BLOCK
only** (no thesis pillars, no "Why we own", no cases, no recommendation) against *"mimicking earnings reports"*;
**matplotlib figures of a blank template** against *"Opal Brand Guidelines form"*.

⛔ **RULED GROUND YOU DO NOT RE-OPEN:** `render_pack.py:26` -- *"STOP -- NOT A BROWSER PRINT, DELIBERATELY."* A print
stylesheet on the live page is refused ground; re-opening it takes an argument against `:26` in a row, not a build.

**THE SHAPE OF THIS CELL: MEASURE FIRST, THEN CLOSE BRANCH (b) ON THE LANDED PRODUCER, THEN NAME THE ROUTE ASK.**

**(1) MEASURE the landed pack against the bar, offline and direct.** Obtain BA_US_Equity's landed model block (the
harness fixtures first -- `__harness__/*.json` -- then the adapter's own reader over the pool, ONE GET, declared above).
Run `build_pack("BA US", block, out_dir=<your deliverables>)`. Print: the PDF's page count (`pypdf` is in the estate; else
count `/Type /Page`), the `txt_path`'s byte size and its first 40 lines, and -- through a NEW harness
`__harness__/exportCompare.harness.cjs` (the `tabs.harness.cjs` loader: actual header + five tabs over
`tabsFixture.BA_US_Equity.json` + `thesisBundle.drafted.BA_US_Equity.json`) -- the page's three sets: FIGURES (a number
with its label), CITES (a passage's accession line), ABSENCES (an "ABSENT ... reason" or `[MACHINE-EMPTY: ...]` line);
then the same three sets extracted from `pack_*.txt`; then `FIGURES page=<n> pack=<n> same=<n> missing=<n> extra=<n>`
and the same for CITES and ABSENCES. **This is the baseline the gap table is read from, with denominators.** Then the
brand-form read: `deck_generation/DESIGN_BIBLE.md` sections A-C, each requirement listed MET / NOT MET against the PDF
with the evidence.

**(2) CLOSE BRANCH (b) ON THE LANDED PRODUCER.** In `lib/research/print/render_pack.py` add `build_rich_text(security,
model_block, thesis_bundle=None, peer_set=None, posture=None, out_dir=None) -> Path` beside `build_pack` -- SAME
discipline: the CALLER supplies every input, it reads no store, writes only to `out_dir`, marks an undrafted or absent
value `[MACHINE-EMPTY: ...]` / `ABSENT -- <reason>`, computes nothing. Output: ONE machine-readable rich-text document
(GitHub-flavoured Markdown: headings, tables for the header figures, the fiscal sheet, the Peers present columns and the
Exec table; block quotes for cited passages with their accession lines; a "Source:" footer naming the vintages) carrying
the SAME figures, cites and absences the page renders. Wire `build_pack` to ALSO write it beside `txt_path` when the
optional bundles are supplied (a caller passing only the block gets today's behaviour, byte-identical -- the negative
control). Prove it with the harness: the Markdown's three sets vs the page's read `missing=0 extra=0` on all three, and
`EXPORT-COMPARE OK`. Add a test under `lib/research/print/tests/` (create the directory if absent) that exercises
`build_rich_text` over the fixture bundles and asserts the parity counts and the byte-identity of `build_pack`'s PDF
with and without the new arguments.

**(3) NAME THE ROUTE ASK; DO NOT MAKE IT.** Serving the rich-text document to a PM needs the `/print` leaf (or a new
leaf) to hand `build_rich_text` the thesis bundle, the peer set and the posture the adapter already reads, and to return
`text/markdown` -- **that is a payload/route change on a served route, and `C-PRESENTATION-ONLY` names `FWD-30` as the
one outcome that returns to `1.0.0_SA_CTO~Z` BEFORE it is built.** Write the ask as a one-page
`ROUTE_ASK_export_rich_text.md` in your deliverables: the leaf, the query or path shape, the inputs the adapter already
holds and where in `_print_pack` they would be handed over, the content type, and the client change (`requestPrintPack`'s
sibling) -- with your recommendation. **Edit neither `scoped_amgt.py` nor `amgt-lead-panel.ts`.**

**(4) THE COMPONENT'S C11 DEFECT (in scope for `FWD-29`):** `PrintExportAction.tsx:63` `rounded-lg`, `:75` `shadow-2xl` --
invert under C5/C11 (4px radius, no shadow), the modal body navy-on-white, the trigger a secondary button; behaviour
unchanged.

## 2. BOUNDS

1. **Files you WRITE:** `portal/src/pages/SecurityAnalysis/components/PrintExportAction.tsx`,
   `portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs`, `lib/research/print/render_pack.py`,
   `lib/research/print/tests/**`, your deliverables. **Read-only:** every other page file (the surface cells have merged),
   `lib/research/api/scoped_amgt.py`, `portal/src/api/**`, `src/ui/**`, `src/components/**`, `deck_generation/DESIGN_BIBLE.md`.
2. **`build_pack`'s existing behaviour is KEPT byte-identical** for a caller passing only `(security, model_block)`: same
   PDF bytes, same `txt_path` content (AC2's negative control). The renderer's deploy-safety (temp dir only, no store read,
   no overlay re-application, `[MACHINE-EMPTY]` marking) binds the new function equally.
3. **The document contains NOTHING the page does not show** (`C-EXPORT-ADDS-NOTHING`): an ABSENT figure is ABSENT with
   its reason; a folded cite is present unfolded; a refusal face is a refusal face. Nothing summarised, reworded, rounded
   differently or derived.
4. **No route, DTO, query key or served figure moves; no deploy.** The route ask is a document.
5. **Standing:** no install, no vendor or Bloomberg call, no S3 write or delete, no key hunting, no push, no promote.
   **REFUSE, do not rescue.**

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/PrintExportAction.tsx
portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs
lib/research/print/render_pack.py
lib/research/print/tests/**
lib/research/print/**
lib/research/api/scoped_amgt.py
lib/research/provenance/render_print.py
portal/src/pages/SecurityAnalysis/**
portal/src/api/endpoints/amgt-lead-panel.ts
portal/scripts/ui-class-census.mjs
portal/DESIGN.md
deck_generation/DESIGN_BIBLE.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~139/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

You WRITE only the first four entries (and your deliverables); every other path is a read-only input.

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rl-10"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~139/measure_landed_pack.py &amp;&amp; cd portal &amp;&amp; node src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs --pack ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~139/landed/pack_BA_US_Equity.txt</invocation><expect>THE LANDED PACK MEASURED AGAINST THE BAR, WITH DENOMINATORS: build_pack ran over BA_US_Equity's landed block (the block's source printed: fixture path or the ONE pool key read); the PDF page count printed (the addendum predicts 4 or more against a cap of 2); the txt byte size and its first 40 lines printed; DESIGN_BIBLE sections A-C each listed MET or NOT MET with evidence; then the harness prints FIGURES / CITES / ABSENCES each as page=n pack=n same=n missing=n extra=n against the PAGE render, with n greater than 0 for page on all three and the gap table stated in words. Both "meets" and "does not meet, because" are RESULTS; an unmeasured claim FAILS</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rl-10"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/print/tests -q -p no:cacheprovider 2&gt;&amp;1 | tail -5 &amp;&amp; cd portal &amp;&amp; node src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs --rich ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~139/rich/BA_US_Equity.md</invocation><expect>BRANCH (b) CLOSED ON THE LANDED PRODUCER: the print tests pass with the new arm -- build_rich_text over the fixture bundles writes a Markdown document, AND build_pack's PDF and txt are BYTE-IDENTICAL (sha256 printed) with and without the optional bundles (the negative control); then the harness reads FIGURES, CITES and ABSENCES each page=n rich=n same=n missing=0 extra=0 with n greater than 0, EXPORT-COMPARE OK, the Markdown larger than 20 KB with its first 200 characters printed and every [MACHINE-EMPTY] or ABSENT line on the page present in it with its reason</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rl-10"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-class-census.mjs src/pages/SecurityAnalysis/components/PrintExportAction.tsx &amp;&amp; test -s ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~139/ROUTE_ASK_export_rich_text.md &amp;&amp; head -30 ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~139/ROUTE_ASK_export_rich_text.md &amp;&amp; git diff --name-only $(git rev-parse HEAD) -- src/api lib/research/api</invocation><expect>THE COMPONENT IN PATTERN AND THE ROUTE ASK WRITTEN, NOT MADE: the census over PrintExportAction.tsx reads FILES 1 TOTAL 0 (it carried rounded-lg, shadow-2xl and 8 idioms before this cell); the route-ask document exists, non-empty, naming the leaf, the shape, the inputs the adapter already holds, the content type, the client sibling and a recommendation; and the diff list under src/api and lib/research/api is EMPTY -- no route, adapter or client file moved</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~139/AMGT_RESAPP.TO-AMGT-rl-10.the-export.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` from the
worktree root. **The status flip is the ISSUER'S**; leave the record face alone and say so. **Report once, naming:** the
landed pack's page count and its three gap lines, AC2's three parity lines, the route ask's recommendation in one sentence,
the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

# pipeline-override: LIMB 6 only -- the BRIEF half reads STALE at 8da812bf80 (owed by 4.0.0_SA_CRO~Z, asked 05:59Z); R-10 (Andrew-direct 2026-09-23 ~21:2xZ, 'agreed with your rec': the L4-R signature is not a BAR for AMGT, the review is kept) + ADDENDUM B B.6 + 1.0.0_SA_CTO~Z msg 25282 (3) 'no round is held on it'; the review stays owed and is not skipped. The PRD_HEADER key refusal is CLEARED at 8da812bf80; coverage is NOTED at EXECUTING (enrichment recut).

**ISSUER NOTES:** wave 2, spawned after every wave-1 branch has merged (the action lives in the header rl-2 rebuilds).
RE-CUT at the cut on ADDENDUM B B.4a (`8da812bf80`, msg 25282): the first face built a page-side HTML export; B.4a
measured that the estate already has the producer (`render_pack.py`, AMGT-s-5) and CLAUDE.md's build ladder puts the
estate's own at rung 2. The DONE WHEN text in the ENDPOINT fence is unchanged; the cell's shape moved from "build" to
"measure, close (b) on the landed producer, name the route ask". The serving of branch (b) is a route change and is the
CTO's call at the round-37 analysis, carried by the worker's ROUTE_ASK document through the drain-end read.

<status>pending</status>
<round>37</round>
<slot>~139</slot>
<fabric>site-z</fabric>

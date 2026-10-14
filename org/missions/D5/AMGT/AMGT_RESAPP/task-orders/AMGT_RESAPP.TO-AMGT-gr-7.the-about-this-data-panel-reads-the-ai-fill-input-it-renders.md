# AMGT_RESAPP task order -- `AMGT-gr-7` -- THE 'ABOUT THIS DATA' PANEL READS THE AI-FILL INPUT IT RENDERS: A PORTAL FEATURE BRANCH `cand/dell1/aifill-provenance` (FWD-41 ROUND 106; CTO 4(d))

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gr-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~456</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-gr-7.the-about-this-data-panel-reads-the-ai-fill-input-it-renders</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git and node only in the nested portal repository.
comp-adversary: RUN at the cut -- `check_gr7_provenance.cjs` is a prepared acceptance check (11 arms, the ACTUAL components rendered by the portal's own react-dom/server); at the base (PROD `7db035e4`) it reads `AIFILL PROVENANCE: NO (6 of 11)`, the build check failing as expected.
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-456` (branch `wk-AMGT_RESAPP-456`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-456`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree. Its nested portal worktree is `C:/dev/wk-resapp-456/portal` (portal PROD `7db035e4`, branch `wk-AMGT_RESAPP-456-portal`).

## 1. THE CELL -- `AMGT-gr-7` (round 106, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

On every PROD page the panel `About this data` read `Web search results stored for this name -- nothing has been read from this input for this name yet` beside blocks labelled `From a web search`: the panel described the SERP collection input and said nothing about the AI fill the page was showing, so it appeared to deny the input the blocks cite. You make the panel read the AI-fill input it renders. A PORTAL change on a feature branch; you do not push, register, merge or promote.

### Why this cell exists (the CVO's five-name read of 2026-10-14, C-S143 to C-S146; the CTO's ruling `ledger/CTO_RULING_FWD41_FIVE_NAME_READ_NOT_MET_20261014.md`, item 4)
FWD-41 graded NOT REALIZED: of five names read on the PROD page, four carried a stated claim that its cited source does not support or contradicts (a figure the release contradicts; a clause no source carries; a stale board proposal a newer source overtakes), one block ended mid-sentence on `... totaling Ps.`
(the cut took an abbreviation for a sentence end), one was garbled, and the page's panel denied the web input the blocks cite. The AI-fill blocks are held off the PROD page until a re-read of five NEW names passes. The CTO's remedy is a GROUNDING PASS in the producer: before a block is stored, every sentence is checked against
the fetched text of the sources it cites, and a sentence they do not carry is dropped; a citation that does not answer (404, refused) grounds nothing; where dated sources conflict the newest wins; the contract refuses a block whose grounding record is missing.

### The change (two files under `portal/src/pages/SecurityAnalysis/`)
1. In the nested portal worktree `C:/dev/wk-resapp-456/portal`: `git switch -c cand/dell1/aifill-provenance` (from the PROD you were cut at). Read `components/InputProvenance.tsx` and `portal/CONTRIBUTING-BOXES.md` first.
2. `components/InputProvenance.tsx`: add the optional prop `aiFill?: AiFill | null` (the type is exported by `../types`). When `aiFill.status === 'SERVED'` the panel gets ONE more list row AFTER the served rows: `<li data-provenance-row="ai-fill" className="text-sm">` holding `<span className="font-bold">AI-written blocks</span>` and `<span className="text-xs text-[hsl(var(--palette-darkGray))]">` with the text ` -- <date> -- <parts>`, where `<date>` is `longDate(aiFill.as_of)` (from `../dateWords`; omit the date part, with its ` -- `, when `as_of` is empty), and `<parts>` counts the served blocks by source class over `Object.values(aiFill.blocks)`: `<N> from a web search` for the WEB_SEARCH ones, `<M> from Opal sources` for the OPAL_SOURCE ones, joined by `, `, each present only when its count is above zero; when neither count is above zero the parts read `no block was written for this name`. So the row reads, for example, `AI-written blocks -- October 14, 2026 -- 2 from a web search, 1 from Opal sources`.
   For any other fill (ABSENT, INVALID, null, undefined) NO row is added and the panel renders exactly as before. When `entries` is null or empty and a row exists, the panel renders with that row alone; with neither it renders nothing (as before). The five served rows, their order and their `data-provenance-row` numbers are unchanged, and the `Web search results stored for this name` row is NOT touched. C-PRESENTATION-ONLY: nothing served is computed or rewritten beyond those counts.
3. `SecurityAnalysis.tsx`: the one mount becomes `<InputProvenance entries={thesisQuery.data?.input_provenance} aiFill={thesisQuery.data?.ai_fill} />` (the bundle already carries `ai_fill`; the page passes it to the header at the same file). No other change to that file.
4. Both files stay ASCII. Commit the branch in the NESTED worktree (cwd `C:/dev/wk-resapp-456/portal`, `.tools/safe-commit.sh` from the OUTER checkout's `.tools`, the author line below, `-F` a message file written with the Write tool, `--` the two paths relative to the portal root); do not stage `portal` in the outer worktree. NEVER push.
5. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~456/FEATURE_RECEIPT.md` with exactly these sections: `## What the branch carries` (branch, head, base, the two paths); `## Pages changed` (a table: page | route | class | gate; Security Analysis | /security-analysis | Opal-internal | internal); `## Shared files` (`- none`); `## Not carried` (package.json, bun.lock, firmAccess.ts: each stated absent with the `git diff <base> HEAD -- <path> | wc -l` count, 0); `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, `/security-analysis`, open `About this data` under the tabs).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W456-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Portal repository only: nested worktree `C:/dev/wk-resapp-456/portal`, branch `cand/dell1/aifill-provenance`; never push; never touch `DEV` or `PROD`; no `bun install` (`node_modules` is a link to the main checkout's).
2. Edit exactly `portal/src/pages/SecurityAnalysis/components/InputProvenance.tsx` and `portal/src/pages/SecurityAnalysis/SecurityAnalysis.tsx`; the receipt is the only other thing you write. Never take `package.json`, `bun.lock`, `src/lib/firmAccess.ts` or any file of another page. You register NO approval row (the issuer does).

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/InputProvenance.tsx
portal/src/pages/SecurityAnalysis/SecurityAnalysis.tsx
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~456/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gr-7"><invocation>cd C:/dev/wk-resapp-456 &amp;&amp; timeout 300 node "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round106_aifill_prep/checks/check_gr7_provenance.cjs" "C:/dev/wk-resapp-456/portal" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL PROVENANCE: YES (N of N)` with N equal to 11, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gr-7"><invocation>cd C:/dev/wk-resapp-456 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_green_v2.sh" "C:/dev/wk-resapp-456/portal" 7db035e4 | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness P of T pass, base Q of U, regressions 0, pre-existing: <names>)` with T equal to U; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-gr-7"><invocation>cd C:/dev/wk-resapp-456/portal &amp;&amp; python "C:/dev/wk-resapp-456/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base 7db035e4 --head HEAD --receipt "C:/dev/wk-resapp-456/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~456/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (2 files: 2 page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~456 <0.9.0_WK_AMGT_RESAPP~456@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~456/AMGT_RESAPP.TO-AMGT-gr-7.the-about-this-data-panel-reads-the-ai-fill-input-it-renders.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the branch name, its head commit and base, the arm lines of AC1 that read FAIL, if any, AC2's and AC3's lines, and the receipt's `## Pages changed` and `## Not carried` sections verbatim.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** An independent head (a portal cell, like AMGT-ar-5). The check is proven satisfiable by the issuer's reference patch (11 of 11, `tsc -b --noEmit` rc 0). The issuer registers the approval row, pushes the branch and runs the release flow AFTER the CVO's re-read is MET and the CTO releases the API hold: the new row is useless while the blocks are held (the panel adds no row for an ABSENT fill).

<status>pending</status>
<round>106</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~456</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

# AMGT_RESAPP task order -- `AMGT-gx-1` -- THE AI ROW READS ITS WEB COUNT AS A SEARCH MADE WHEN THE BLOCK WAS WRITTEN (FWD-41 ROUND 112, THE gr-7 WORDING, CTO 6706; A DIRECT ACT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gx-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~486</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-gx-1.the-ai-row-reads-its-web-count-as-a-search-made-when-the-block-was-written</to_id>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; one presentation line in a React component.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; git and node only in the nested portal repository.
comp-adversary: RUN at the cut -- `check_gr7_wording.cjs` is a prepared acceptance check (12 arms, the ACTUAL component rendered by the portal's own react-dom/server); at the base (DEV `fc174c69`) it reads `AIFILL PROVENANCE: NO (9 of 12)`, the build check failing as expected, and the issuer's reference edit in a scratch tree reads `YES (12 of 12)` with `bun run typecheck` rc 0.
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-486` (branch `wk-AMGT_RESAPP-486`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-486`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree. Its nested portal worktree is `C:/dev/wk-resapp-486/portal` (portal DEV `fc174c69`, branch `wk-AMGT_RESAPP-486-portal`).

## 1. THE CELL -- `AMGT-gx-1` (round 112, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

On the Security Analysis page the panel `About this data` now has one row, `AI-written blocks -- <date> -- <parts>`, and the `<parts>` for web blocks read `<N> from a web search`. That sits beside the unchanged stored-search line `Web search results stored for this name -- nothing has been read from this input for this name yet`, and a reader takes the two as a contradiction: both name a web search, for two different inputs. You reword the web part so it says what the AI blocks' search was: one made when each block was written. A PORTAL change on a feature branch; you do not push, register, merge or promote.

### The change (one file under `portal/src/pages/SecurityAnalysis/`)
1. In the nested portal worktree `C:/dev/wk-resapp-486/portal`: `git switch -c cand/dell1/aifill-provenance-wording` (you are at DEV `fc174c69`, which already carries the row). Read `components/InputProvenance.tsx` first.
2. In `components/InputProvenance.tsx`, function `aiFillStatus`: the web part of `<parts>` is now `1 cites a web search made when it was written` when the WEB_SEARCH count is exactly 1, and `<N> cite web searches made when they were written` when the count is above 1 (N the number); it is absent when the count is 0, exactly as the web part is today. The Opal part stays `<M> from Opal sources`, present only above zero. The two parts are still joined by `, ` with the web part first, and the whole row still reads `AI-written blocks -- <date> -- <parts>` (and `no block was written for this name` when neither count is above zero). So the row reads, for example, `AI-written blocks -- October 14th, 2026 -- 2 cite web searches made when they were written, 1 from Opal sources`.
3. Nothing else changes: not the stored-search row, not the five served rows, not their order or numbers, not `SecurityAnalysis.tsx`, not the header comment. The file stays ASCII.
4. Commit the branch in the NESTED worktree (cwd `C:/dev/wk-resapp-486/portal`, `.tools/safe-commit.sh` from the OUTER checkout's `.tools`, the author line below, `-F` a message file written with the Write tool, `--` the one path relative to the portal root); do not stage `portal` in the outer worktree. NEVER push.
5. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~486/FEATURE_RECEIPT.md` with exactly these sections: `## What the branch carries` (branch, head, base, the one path); `## Pages changed` (a table: page | route | class | gate; Security Analysis | /security-analysis | Opal-internal | internal); `## Shared files` (`- none`); `## Not carried` (package.json, bun.lock, firmAccess.ts: each stated absent with the `git diff <base> HEAD -- <path> | wc -l` count, 0); `## How to look` (the dev build `cd portal && bun run dev --port 5174`, `/security-analysis`, open `About this data` under the tabs).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W486-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-486/portal`, branch `cand/dell1/aifill-provenance-wording`; never push; never touch `DEV` or `PROD`; no `bun install` (`node_modules` is a link to the main checkout's).
2. Edit exactly `portal/src/pages/SecurityAnalysis/components/InputProvenance.tsx`; the receipt is the only other thing you write. Never take `package.json`, `bun.lock`, `src/lib/firmAccess.ts` or any file of another page. You register NO approval row (the issuer does).

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/InputProvenance.tsx
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~486/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gx-1"><invocation>cd C:/dev/wk-resapp-486 &amp;&amp; timeout 300 node "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round111_aifill_prep/checks/check_gr7_wording.cjs" "C:/dev/wk-resapp-486/portal" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL PROVENANCE: YES (N of N)` with N equal to 12, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gx-1"><invocation>cd C:/dev/wk-resapp-486 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_green_v2.sh" "C:/dev/wk-resapp-486/portal" fc174c69 | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness P of T pass, base Q of U, regressions 0, pre-existing: <names>)` with T equal to U; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-gx-1"><invocation>cd C:/dev/wk-resapp-486/portal &amp;&amp; python "C:/dev/wk-resapp-486/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base fc174c69 --head HEAD --receipt "C:/dev/wk-resapp-486/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~486/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>the one changed file listed as page, none forbidden or unnamed, and a line beginning `R103 FEATURE SURFACE: YES (` that reads 1 page, 0 shared named, 0 forbidden, 0 unnamed; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~486 <0.9.0_WK_AMGT_RESAPP~486@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~486/AMGT_RESAPP.TO-AMGT-gx-1.the-ai-row-reads-its-web-count-as-a-search-made-when-the-block-was-written.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the branch name, its head commit and base, the arm lines of AC1 that read FAIL, if any, AC2's and AC3's lines, and the receipt's `## Pages changed` and `## Not carried` sections verbatim.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT-ACT: one cell, one presentation line, LOCAL; no L2, L4-R or L8-L10. Source: CTO msg 6706 (reword the AI row's web count; same approval class). The close is the issuer's: push the new branch, register its approval row (the tool refuses a branch with commits already on DEV, so this is a NEW branch cut from DEV, carrying one commit), merge forward on the CTO's close of that row, read the panel on a DEV build for AMD_US_Equity, promote by /prod-deploy as a chosen set, then ask the CVO for its PROD page read (C-S146 a). The plural form is the issuer's reading of the CTO's singular wording; the CTO is told.

<status>pending</status>
<round>112</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~486</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

# AMGT_CORPUS task order -- `CRPS-aq-3` -- ROUND 41: the header feed matches a pillar's real terms only; a name with none says so

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-aq-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; the check renders one component on a hand-built feed.
comp-adversary: RUN by the issuer at the cut on portal origin/DEV 32835ce5 -- page_check41.cjs aq3: build 0/3 control 1/1. Blind spot: static markup only; the reading on a real name is the issuer's close read.
EGRESS CLASS, declared: NONE. Portal source only. NO push of any portal branch: the DEV landing follows the CTO's render review.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 41.

**Your portal.** The nested `portal/` directory in your worktree is a portal git worktree on branch `wk-AMGT_CORPUS-41-portal`, based
on origin/DEV `32835ce5`. Portal files commit INSIDE `portal/` on that branch; the outer commit holds only the outer files. Never
commit the portal gitlink. NEVER run `bun install` (a registry fetch is egress). **Colour law** (`portal/CLAUDE.md`): navy ink on the
light canvas and white panels; reuse the classes already in the file.

## 1. THE CELL -- `CRPS-aq-3`

Each served thesis pillar is `{pillar, terms}` where `terms[0]` is the pillar's own title and `terms[1:]` are the vocabulary terms
matched in its passage (the producer's shape; it stays). For example IMB LN:
`{pillar:"Clean balance sheet for a Tobacco company", terms:["Clean balance sheet for a Tobacco company","net debt","EBITDA"]}`.
Today `portal/src/pages/SecurityAnalysis/tabs/NewsTab.tsx` (about line 32) flattens EVERY term, title included, and passes them to
`HeaderBrief`, whose `FeedList` (`components/HeaderBrief.tsx`, about line 213) renders one filter per term. So a headline is matched
against a pillar title, and a name whose pillars carry no real term shows title "filters" that match nothing useful.

**Build:**
1. Export from `components/HeaderBrief.tsx` a function `realPillarTerms(pillars)`: given the served pillar list it returns the
   distinct `terms.slice(1)` across pillars, in order (`["net debt","EBITDA","price"]` for IMB's three pillars); given pillars whose
   only term is their title it returns `[]`; given null, undefined or `[]` it returns `null` (no dossier).
2. `tabs/NewsTab.tsx` passes `realPillarTerms(<the served pillars>)` instead of flattening `p.terms`. Change nothing else there.
3. `FeedList` with `terms` an empty array (pillars served, no real term) renders no term filter and an element carrying
   `data-feed-terms-absent` whose text says in plain words that the research team's thesis pillars carry no term to filter the news.
4. `FeedList` with `terms` undefined renders exactly what it renders today, byte for byte. A term filter for a real term keeps its
   whole-word match and its markup (`data-feed-term`, `data-feed-term-count`).

## 2. BOUNDS

1. Only the files in `<paths>` change. Never edit the issuer's check or snapshot. No `__harness__/` edit, no `types.ts` edit.
2. NO push of any branch, NO deploy, NO AWS, Bloomberg or vendor call. Do not run the ui-walk walker.
3. Do not touch `lib/research/corpus/continuation.py` (its terms shape is ruled).
4. Write code with the Edit/Write tools, never a shell heredoc. ASCII only.
5. Rows are `AMGT_CORPUS-D1-W2-S<k>`, with `disarm_owner 2.0.0_SA_COO~C1`.
6. Outer commits with `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~2 <0.9.0_WK_AMGT_CORPUS~2@opal.agent>" -F <msgfile> -- <paths>`;
   the portal commit with `git -C portal commit` on branch `wk-AMGT_CORPUS-41-portal`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx
portal/src/pages/SecurityAnalysis/tabs/NewsTab.tsx
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-aq-3.feed-matches-real-terms-only.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-aq-3.feed-matches-real-terms-only.md
</paths>

Read-only: the whole repository, in particular `portal/CLAUDE.md` and the issuer's check
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round41/page_check41.cjs` (its header comment states each
build limb exactly) with `aq3_base_snapshot.json`.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-aq-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round41/page_check41.cjs" aq3 portal</invocation><expect>(?m)^aq3 build 3/3 control 1/1$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-aq-3"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs &gt; /dev/null 2&gt;&amp;1; echo "tabs rc=$?"</invocation><expect>(?m)^tabs rc=0$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-aq-3" judgment="true"/>
</proof_of_spec>

- AC1: `realPillarTerms` gives the real terms only; a real term filters, the pillar title does not; a name with no real term says so;
  with no dossier the feed is byte-unchanged.
- AC2: the page's tab harness still exits 0.
- AC3 (JUDGMENT, graded by the CVO at L9 on the issuer's real read of a name with real terms AND a headline in the window): a reader
  can follow a theme the team named into the news, and a name with no real term is not shown a filter that cannot match.

## 5. WHEN YOU ARE DONE

1. If `portal/node_modules` resolves, run `bun run typecheck` inside `portal/` and report its exit code; if not, say so (the issuer
   typechecks at the drain).
2. Write the instance at the proof path (genre BUILD), with its mutant control. Record AC3 as `UNVERIFIABLE-BY-INSTRUMENT` with
   `status_reason` naming `3.0.0_SA_CVO`; no verdict. Run `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3
   --governing-order <this order>` AFTER your final commit; rc 0.
3. Only if AC1 and AC2 pass, append a new status tag reading complete at the END of this file, in the SAME outer commit as your instance.
4. Report ONCE: the change, AC1's output lines, AC2's line, the typecheck result, the portal branch and FULL 40-character portal
   commit, your outer commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-40 analysis @`05739a6e4e` s.2 item 3 (3a); 3b CLOSED by ruling F (addendum 1). The pre-draft named SecurityOverlay.tsx:499 as the flatten site; at origin/DEV 32835ce5 it is NewsTab.tsx:32 (read at the cut). Candidate to the CTO's render review, then portal DEV; the issuer's close read picks the real name by the read.
<risk>LOCAL</risk>
<status>pending</status>
<round>41</round>
<slot>~2</slot>
<fabric>dell1</fabric>

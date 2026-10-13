# AMGT_RESAPP task order -- `AMGT-fa-8` -- THE PAGE RENDERS THE FIVE FILL BLOCKS: SOURCE CLASS, CITATIONS, THE MACHINE-WRITTEN CHIP (FWD-41; A PORTAL BRANCH)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-fa-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~423</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-fa-8.the-page-renders-the-five-fill-blocks</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN at the cut -- `check_fa8_page.py` is a prepared acceptance check (16 arms: the 11 named harness arms, the final harness line, the changed-files bound, no package.json/bun.lock/firmAccess.ts, the harness a new file, no deletion); at the base (`--portal portal --base HEAD`) it reads `AIFILL FA-8 ARMS: NO (2 of 16)`, the build check failing as expected (the 2 passing arms are the no-forbidden-file and no-deletion controls); `r103_feature_green_v2.sh` is R1's proven instrument (bj-9: `YES`, 18 of 21 harnesses pass against PROD's 14 of 20, 0 regressions).
EGRESS CLASS, declared: NONE beyond `git fetch origin` in the nested portal repository (read); no `bun install` (node_modules is a link); no dev server.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-423` (branch `wk-AMGT_RESAPP-423`, cut from the issuance commit; the nested portal worktree is at PROD `63c4f9e3` (the PROD release commit)). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-423`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree. Your nested portal worktree is `C:/dev/wk-resapp-423/portal`, at portal PROD `63c4f9e3` on branch `wk-AMGT_RESAPP-423-portal`.

## 1. THE CELL -- `AMGT-fa-8` (round 104, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

FWD-41's five blocks reach the Security Analysis page in the `/thesis` bundle's new key `ai_fill` (cell fa-7 serves it; it is not deployed yet, so the page must also behave when the key is absent). You change the PAGE: a shared block component, the five placements, the types and a render harness. This is a portal change: it is made in the nested portal worktree on a `cand/dell1/<slug>` branch cut from the last PROD release and NEVER pushed (read `portal/CONTRIBUTING-BOXES.md` first; the issuer registers the branch for the CTO's approval as an Opal-internal page; Security Analysis is staff-only).


### The contract every cell of this workstream writes against (ratified in the decomposition, inlined)

`fill/v1` document, one per security key, and its five blocks:
```
{ "schema": "aifill/v1", "security_key": "<K>", "as_of": "YYYY-MM-DD", "generated_at": "YYYY-MM-DDTHH:MM:SSZ",
  "producer": {"version": "opal-aifill/1.0.0", "model": "claude-opus-5"},
  "blocks": { "mgmt_bio": B, "mgmt_recent": B, "mgmt_team_view": B, "thesis_pillars": B, "identity_description": B } }   # exactly these five
B = { "block_id": "<id>", "source_class": "OPAL_SOURCE" | "WEB_SEARCH" | "NONE", "machine_written": true,
      "text": "<plain ASCII text, 1..1200 chars>" | null, "reason": "<plain sentence>" | null,
      "citations": [ {"source_kind": "opal"|"web", "url": str|null, "title": str|null, "quote": str|null, "ref": str|null} ],
      "opal_inputs": [str], "model_call": {"model","web_search_requests","input_tokens","output_tokens"} | null }
```
Block rules: `NONE` has `text` null, `reason` a non-empty plain sentence with no underscore, and no citations. Any other class has `text` non-empty (at most 1200 characters, ASCII, no `**`),
`reason` null and at least one citation. A `web` citation has an http(s) `url`. An `opal` citation has a plain-words `ref` an analyst reads (no `_`, `[`, `]`, `{`, `}`, and not starting `thesis.` or
`overlay.`); it may also carry an http(s) `url`. `WEB_SEARCH` has at least one web citation, no opal citation, and `model_call.web_search_requests >= 1`. `OPAL_SOURCE` has at least one opal
citation and no web citation. `machine_written` is always `true`. `opal_inputs` holds the code-path names of the served fields used (never displayed).

The builder seam: a block builder is `lib.research.aifill.block_<id>.build_block(ctx) -> dict` and does no I/O of its own. `ctx` is a `BlockContext(security_key, inputs, model, now)` with
`ctx.inputs = {"overlay": dict|None, "thesis": dict|None, "errors": {...}}` (the two served route bodies of `/api/scoped/amgt/security/<key>/overlay` and `/thesis`), `ctx.now` a tz-aware UTC
datetime, and `ctx.model(prompt, *, system=None, web_search_max_uses=0, max_tokens=1500)` returning an object with `.text`, `.citations` (a list of `{"url","title","cited_text"}`), `.searches`,
`.input_tokens`, `.output_tokens`, `.web_search_requests`, `.model`, `.stop_reason`; it RAISES `ModelError` on any failure and never returns partial text.

### The served shape the page reads (`ThesisBundle.ai_fill`, optional: an older payload has none)
```
ai_fill: { status: 'SERVED' | 'ABSENT' | 'INVALID', reason: string | null, source: 'pool' | 'local' | 'none', read_completed: boolean,
           as_of: string | null, generated_at: string | null, producer: {version: string, model: string} | null,
           blocks: { mgmt_bio?: B, mgmt_recent?: B, mgmt_team_view?: B, thesis_pillars?: B, identity_description?: B } }   // blocks = {} unless SERVED
```
with `B` as in the contract (`block_id`, `source_class`, `machine_written`, `text`, `reason`, `citations[]`, `opal_inputs`, `model_call`). TYPES ONLY go in `types.ts` (no runtime value is exported from that file): `AiFillBlockId`, `AiFillCitation`, `AiFillBlock`, `AiFill`, and `ai_fill?: AiFill | null` on `ThesisBundle`.

### What you build (all under `portal/src/pages/SecurityAnalysis/`)
1. `components/AiFillBlock.tsx`: `AiFillBlock({ fill, blockId, label, always })` (props: `fill?: AiFill | null`, `blockId: AiFillBlockId`, `label: string`, `always?: boolean`) and the pure function `identityDescriptionFill(fill) -> {text, source_class, citations} | null` (the `identity_description` block when the fill is SERVED and its `source_class` is not `NONE`, else null). Rendering, exactly:
   - A SERVED block that is not `NONE`: a wrapper with `data-ai-fill="<blockId>"` and `data-ai-source="<source_class>"`; the text in a `<p>` (for `thesis_pillars` each line of the text is its own `<li>` of a `<ul>`); a chip element with the attribute `data-ai-chip` whose text is exactly `Machine-written`, beside the words `From Opal sources` (OPAL_SOURCE) or `From a web search` (WEB_SEARCH); a sources list with the attribute `data-ai-sources`: a `web` citation is an `<a>` with `href` = its `url`, `target="_blank"`, `rel="noreferrer noopener"` and the visible text its `title` (else the host of its `url`); an `opal` citation is its `ref` words (wrapped in the same kind of `<a>` when it carries a `url`). The block `mgmt_team_view` also prints the caption `Machine-written summary, not the research team's view.`; `thesis_pillars` prints `Machine-written, not the research team's pillars.`
   - A `NONE` block, when `always`: `<p data-ai-fill="<blockId>" data-ai-source="NONE">{label}: {reason}</p>` with no chip. When not `always`, a `NONE` block renders nothing.
   - The fill is null, undefined, ABSENT or INVALID, when `always`: `<p data-ai-fill="<blockId>" data-ai-source="UNAVAILABLE" data-ai-reason="<fill.reason or empty>">{label}: has not been prepared for this name yet.</p>` (null, undefined, ABSENT) or `{label}: could not be shown for this name.` (INVALID). The served technical reason (it holds underscores and storage paths) rides ONLY the `data-ai-reason` attribute: shown as text it would be a raw-code defect. When not `always` (the gap blocks), an unavailable fill renders nothing, so the page prints exactly what it printed before.
2. `tabs/ExecManagementTab.tsx`: `mgmt_bio` (label `Management bio summary`) and `mgmt_recent` (label `Recent developments`) rendered with `always`, in the tab's normal flow below the CEO profile and tenure lines and above the roster, and ALSO when the management block is ABSENT (these two are new blocks, not gap fills). `mgmt_team_view` rendered (not `always`) directly after the sentence the tab already prints for `MANAGEMENT_HEADING` when the pack states no management passage, and only there: where the pack states a passage, nothing is drawn for it even if a block is supplied.
3. `tabs/ThesisTab.tsx`: `thesis_pillars` rendered (not `always`) directly after the sentence the tab already prints for `PILLARS_HEADING` when the pack states no pillars, and only there.
4. `components/SecurityOverlay.tsx` and `SecurityAnalysis.tsx`: `IdentityHeader` takes the optional prop `aiFill?: AiFill | null`; `SecurityAnalysis.tsx` passes `aiFill={thesisQuery.data?.ai_fill}` (the page already holds `thesisQuery`). `identityDescriptionLine(bundle)` keeps its signature and result. When it returns `''` AND `identityDescriptionFill(aiFill)` is not null, the header draws the fill text in the SAME single description paragraph (`data-identity-description` appears once, per ruling W126-S1) with `data-ai-fill="identity_description"`, `data-ai-source`, a `data-ai-chip` chip and a compact sources list. When the line is non-empty, the header's markup is byte-identical to what it was (no fill is drawn).
5. `__harness__/aiFill.harness.cjs` and `__harness__/aiFill.fixture.json`: a render harness in the method of `__harness__/execText.harness.cjs` and `__harness__/tabs.harness.cjs` (read both first: they transpile the ACTUAL components with the installed `typescript` and render with `react-dom/server`; no browser, no HTTP, writes no file). Hand-build the `ai_fill` documents in the fixture from the contract above; reuse `execFixture.ASML_NA_Equity.json` or a tab fixture for the surrounding bundle. Run from the portal root: `node src/pages/SecurityAnalysis/__harness__/aiFill.harness.cjs`. It prints, for each of these ELEVEN arms, a line `ARM <name> PASS` or `ARM <name> FAIL <detail>`, in this order, and a final line `AIFILL PAGE HARNESS: YES (N of N arms)` (exit 0) only when every arm passes (else `NO (k of N arms)`, exit 1):
   - `bio_web_renders_text_chip_links`: the Exec tab with a `mgmt_bio` WEB_SEARCH block of two web citations -> the text; an element `data-ai-fill="mgmt_bio"` with `data-ai-source="WEB_SEARCH"`; the exact text `Machine-written` inside a `data-ai-chip` element; each citation url as the `href` of an `<a>` with `target="_blank"` and a `rel` containing `noreferrer`.
   - `recent_opal_renders_plain_refs`: `mgmt_recent` OPAL_SOURCE with two opal citations, one with a `url` -> the text, the chip, each `ref` visible as text, the one with a url wrapped in an `<a href>`.
   - `bio_none_prints_reason`: `mgmt_bio` NONE -> `data-ai-source="NONE"`, the reason visible after `Management bio summary:`, and NO chip.
   - `fill_absent_prints_fixed_sentence`: status ABSENT with a technical reason (give it underscores and an `s3://` path) -> `Management bio summary: has not been prepared for this name yet.` and the same for `Recent developments`; the technical reason appears in `data-ai-reason` and NOT in the visible text.
   - `fill_invalid_prints_fixed_sentence`: status INVALID -> `... could not be shown for this name.`
   - `fill_missing_prints_fixed_sentence`: `ai_fill` undefined, then null -> the ABSENT sentence, no exception.
   - `team_view_beside_gap_only`: a pack that states no management passage + a `mgmt_team_view` WEB block -> the tab's own `MANAGEMENT_HEADING` gap sentence is still present and the fill follows it, with the chip and the words `not the research team's view`; then a pack that STATES a management passage + the same block supplied -> the fill is not drawn and the team's passage is unchanged.
   - `pillars_beside_gap_only`: the same pair for the Thesis tab and `thesis_pillars` (a multi-line text -> one `<li>` per line).
   - `header_fill_when_empty`: `IdentityHeader` with no description line + an `identity_description` WEB block -> `data-identity-description` appears exactly once, holds the fill text, carries `data-ai-fill="identity_description"` and the chip.
   - `header_unchanged_when_held`: `IdentityHeader` with a description line + the same block -> the markup is identical to the markup with no `aiFill` prop, and `data-identity-description` appears once.
   - `no_raw_codes_in_visible_text`: over every markup the harness rendered, the visible text (tags removed, attribute values excluded) matches nothing of `\b[A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9]+)+\b`.

The surrounding page is otherwise unchanged: the existing harnesses (`tabs`, `execText`, `execPattern`, `thesisLadder`, `drafting`, ...) must not regress, and `bun run typecheck` and `bun run lint` stay at exit 0 (AC2 runs them against PROD's own results).

### Method (from the V1 feature cut, which ran in this same repository)
1. `cd C:/dev/wk-resapp-423/portal && git switch -c cand/dell1/aifill-blocks` (from PROD `63c4f9e3`); `git fetch origin DEV` is allowed (read) and you do NOT merge it.
2. `node_modules` in your portal worktree is a LINK to the main checkout's: NEVER run `bun install`. `bun run typecheck` (never bare `tsc --noEmit`) and `bun run lint` are on PATH through bun; resolve bun with `command -v bun`.
3. Commit in the nested worktree (cwd `C:/dev/wk-resapp-423/portal`) with the OUTER checkout's `.tools/safe-commit.sh` and the author line below, `-F` a message file written with the Write tool, `--` each file path RELATIVE TO THE PORTAL ROOT. Do not stage `portal` in the outer worktree. NEVER push. The nested repository has no committer identity of its own: if git asks, set it for that repository only to the worker serial (`git config user.name` / `user.email`), nothing global.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W423-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Portal repository only, under `portal/src/pages/SecurityAnalysis/`; branch `cand/dell1/aifill-blocks` from PROD `63c4f9e3`; never push; never touch `DEV` or `PROD`; never `git merge` DEV.
2. Never touch `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, a file of another page, or any file outside `src/pages/SecurityAnalysis/`. No new dependency. No dev server (port 5174 is held by another session).
3. The existing exports of the files you edit keep their signatures. Existing harnesses are not edited EXCEPT the three that stub the page's module imports and cannot resolve the new `../components/AiFillBlock` import (AMENDMENT 1): `__harness__/execText.harness.cjs`, `__harness__/drafting.harness.cjs` and `__harness__/execFallback.harness.cjs`. In each, add the ONE loader entry that stubs that module in the way its neighbouring `if (name === '../components/...')` entries stub theirs (`{ AiFillBlock: () => null, identityDescriptionFill: () => null }`, so the existing arms render exactly as before), and nothing else; the three must then pass as at the base. The design contract (`portal/DESIGN.md`, the portal CLAUDE.md color law) binds the new markup: use the classes the neighbouring block of the same file uses (white panel, navy ink, secondary ink `#6B7280` only on a panel); no light-on-light text.
4. Python is not involved; the acceptance script is the issuer's. Do not create a `.py` file.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-fa-8"><invocation>cd C:/dev/wk-resapp-423/portal &amp;&amp; timeout 400 python "C:/dev/wk-resapp-423/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_fa8_page.py" --portal . --base 63c4f9e3 | tail -6; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL FA-8 ARMS: YES (N of N)` with N equal to 16, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-fa-8"><invocation>cd C:/dev/wk-resapp-423 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_green_v2.sh" "C:/dev/wk-resapp-423/portal" 63c4f9e3 | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness P of T pass, base Q of U, regressions 0, pre-existing: <names>)` where T is one more than U (your new harness) and P is at least Q plus 1; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~423 <0.9.0_WK_AMGT_RESAPP~423@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~423/AMGT_RESAPP.TO-AMGT-fa-8.the-page-renders-the-five-fill-blocks.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- AC1's arm lines (all 16) and AC2's line; the branch's commit hash and base; `git diff --stat` of the branch against `63c4f9e3`; for each of the five placements one line saying where in the file it renders.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (2026-10-13 ~23:2xZ, the issuer, after worker ~423's BLOCKING row W423-S5; the limb that graded it: none graded it, the order is open and `<placeholders>NONE` stands):** AC2 (`r103_feature_green_v2.sh`) read `NO (... regressions 3: drafting, execFallback, execText)`: the three harnesses stub each page module import by name and none carried the new `../components/AiFillBlock` import, a defect of this cut (bound 3 forbade editing any existing harness). The amendment allows exactly one stub entry in each of the three. `<paths>` (the page directory) already covers them. Other worker rows: S1 to S3 and S6 are observations; S4 (the bio and recent placement above the roster) is accepted; S2: portal PROD has moved to `10e7664d` (two commits past `63c4f9e3`, which is its ancestor), so the candidate stays valid and the approval step lands it on DEV by the author's fast-forward after a merge of the then-current DEV.

**ISSUER NOTES:** An independent head: the page is written against the served contract, not against fa-7's code, and degrades to today's page when `ai_fill` is absent (no deployed route serves the key yet). The base is PROD `63c4f9e3` (Andrew's whole-DEV promote of 2026-10-13 19:24Z; DEV has moved on by at least one TicketCenter commit, which this branch does not carry and does not need). The cell ends at a committed branch: the CTO approves it as Opal-internal, then it reaches DEV by its author's fast-forward and PROD by the portal release seat (decomposition s.5 item 2); the issuer registers it (`open-calls.py add --kind approval`) at the drain. No judgment criterion here: the rendered look is read on a page with real fill data in the thread run, not on a fixture render. The `identity_description` block is drawn from the thesis bundle so the overlay route gains no read (decomposition s.2 item 4).

<status>pending</status>
<status>complete -- 2026-10-13T23:5xZ by the issuer (2.0.0_SA_COO~R2): outer branch wk-AMGT_RESAPP-423 @1af7457543 merged @8abdbcac92 (proof and rows); the PAGE WORK is portal branch `cand/dell1/aifill-blocks` @85d5749f (cut from PROD 63c4f9e3, LOCAL in the nested portal repository, NOT pushed, NOT on DEV). The first run's AC2 read regressions 3 (row W423-S5: the issuer's cut forbade editing three harness loaders); AMENDMENT 1 allowed one stub entry in each and the slot was re-seated. AC1 PASS (`AIFILL FA-8 ARMS: YES (16 of 16)`, re-run by the issuer), AC2 PASS (`R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness 19 of 22 pass, base 15 of 21, regressions 0, ...)`, re-run by the issuer). The branch awaits the CTO's Opal-internal approval.</status>
<round>104</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~423</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

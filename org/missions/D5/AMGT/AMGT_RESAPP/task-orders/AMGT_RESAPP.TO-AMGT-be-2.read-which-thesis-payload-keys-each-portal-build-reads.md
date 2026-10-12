# AMGT_RESAPP task order -- `AMGT-be-2` -- READ, DO NOT CHANGE: WHICH THESIS PAYLOAD KEYS EACH PORTAL BUILD READS (`fiscal_year_figures` TWICE, `check_face`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-be-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~394</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-be-2.read-which-thesis-payload-keys-each-portal-build-reads</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only reading; nothing is scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- local reads of two detached checkouts of the portal repository; no AWS call and no write.
comp-adversary: RUN at the cut -- r98_payload_key_reading_check.py reads NO at the base (no reading exists) and YES against a throwaway sample reading that carries every heading, three denominated sources, a KEY line for each of the three keys with a DEV and a PROD count, the census, a control, two read surfaces and one not read, three OUTCOME lines and WRITES: none.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-394` (branch `wk-AMGT_RESAPP-394`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-394`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE ACT -- `AMGT-be-2` (round 98, decomposition s.106): A READING, NOTHING CHANGED

CTO~DELL1 round-97 analysis item 2 and AMGT_CORPUS's round-47 ADDENDUM 1. The Thesis payload (`GET /api/scoped/amgt/security/<key>/thesis`) serves the key `fiscal_year_figures` TWICE
(at the top level and as `model.fiscal_year_figures`, 32.3 percent of the response each, measured by AMGT_CORPUS) and `check_face` (24.9 percent). A key that NO portal build reads can
be dropped later, by its own cell under its own redeploy pair; this order only READS which build reads which key. The two builds are `origin/DEV` and `origin/PROD` of the NESTED
portal repository (`portal/` in the workspace; the PROD-built page is the PROD ref's source).

HOW: make TWO detached worktrees of the nested portal repository OUTSIDE the workspace checkout (so the native Grep tool reads them freely), for example
`git -C C:/dev/wk-resapp-394/portal worktree add --detach C:/dev/scratch-be2-dev origin/DEV` and the same for `origin/PROD` (if the nested repository is not populated in your worktree,
run the same command from `C:/dev/ajb_workspace/portal` and print the ref's full hash). Then, with the native Grep tool over each worktree's `src/` (and `src/pages/SecurityAnalysis/`
first): every file that names `fiscal_year_figures` or `check_face`; read each site and classify it, in words, as a read of the TOP-LEVEL payload key or of `model.fiscal_year_figures`
(`model.` as a property path, a destructure of `model`, a local alias) or of another object that merely shares the name (a type, a fixture, a test: say so, and count only reads of the
served payload). Run the SAME sweep for ONE control key the builds are known to treat differently: `team_sheet` (round 46's reading: the PROD ref reads it in 0 files of
`src/pages/SecurityAnalysis`, the DEV ref in several): if the sweep cannot see that difference the reading says so. Print the denominators: files scanned per build (`.ts` and `.tsx`
under `src/`), and the matches. Name, under `## Surfaces`, every surface you read and at least one you did NOT (the built bundles' minified code, another client of the API, the print
or PDF route, `lib/research/api` consumers): never write READ-BY-NEITHER from the source tree alone without saying the bundle was not read.

Write ONE reading to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~394/BE2_PAYLOAD_KEY_READING_20261011.md` in the shape `checks/r98_payload_key_reading_check.py` grades (its docstring is the template; headings Sources, Keys, Census, Control, Surfaces,
Outcome, Not changed). The three keys judged: `fiscal_year_figures` (top level), `model.fiscal_year_figures`, `check_face`; one OUTCOME line each: READ-BY-BOTH, READ-BY-DEV-ONLY,
READ-BY-PROD-ONLY or READ-BY-NEITHER. A removal is NOT part of this order.

WRITE NOTHING anywhere but the reading file, the two scratch worktrees (remove them when done with `git worktree remove --force`) and, if a premise fails, a surprise row. No API call,
no AWS call, no Bloomberg call.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W394-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Reads only (local file reads of two detached checkouts). No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no S3 delete, ever.
2. No `bun`, `npm` or `pip install`; do not build the portal.
3. Standing: no push of shared branches (the nested portal repository's refs are read, never written).
4. The reading names no client, firm or account.
5. A surface you cannot read is a finding in the reading (`NOT READ: <why>`), never a reason to guess.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~394/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-be-2"><invocation>cd C:/dev/wk-resapp-394 &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round98_prep/checks/r98_payload_key_reading_check.py" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~394/BE2_PAYLOAD_KEY_READING_20261011.md"; echo "exit=$?"</invocation><expect>PASS S1 (every heading present, in order, non-empty), PASS S2 (at least three sources, each with an n= denominator), PASS S3 (a KEY line for each of the three keys with a DEV and a PROD count), PASS S4 (both builds' denominators and the matches), PASS S5 (a control key shows the sweep sees a read), PASS S6 (at least two surfaces read and one not read), PASS S7 (exactly one allowed OUTCOME for each key), PASS S8 (WRITES: none); R98 PAYLOAD KEY READING SHAPE: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-be-2" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~394 <0.9.0_WK_AMGT_RESAPP~394@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Write any python or multi-line file with the Write tool. Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~394/AMGT_RESAPP.TO-AMGT-be-2.read-which-thesis-payload-keys-each-portal-build-reads.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character (AC2 is a judgment criterion: record it as the checker's grammar requires, UNVERIFIABLE-BY-INSTRUMENT, naming the CVO).
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- criterion AC1's output lines;
- the three OUTCOME lines and each KEY line (DEV and PROD site counts) and the control line;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-97 analysis section 2 item 2: "The Thesis payload's duplicate, read only first: which of top-level `fiscal_year_figures` and `model.fiscal_year_figures` (32.3 pct each), and `check_face` (24.9 pct), each portal build reads, DEV and the PROD-built page, with the denominator printed. A removal is a later cell, under its own redeploy pair, and only for a key no build reads." AC2 is the CVO's judgment (the outcomes follow from the evidence, the control and the named surfaces; READ-BY-NEITHER stated from source only is NO unless the bundle gap is named). The removal, if any, is a later round's cell under its own pair.

<status>complete -- 2026-10-11T21:4xZ by the issuer (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-394 @5722cc350b merged @95ba1a1dae, proof instance VALID; issuer re-run on the merged tree: AC1 R98 PAYLOAD KEY READING SHAPE YES (8 of 8); the issuer's own git grep of origin/DEV 44ec7e70a9 and origin/PROD 37aa1247ee reproduces the worker's sites (fiscal_year_figures top level ModelTab and postureCites, check_face ModelTab, model.fiscal_year_figures only as the footer's string paths CardFooter.tsx:187-188); AC2 is the CVO's judgment, ungraded.</status>
<round>98</round>
<slot>0.9.0_WK_AMGT_RESAPP~394</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

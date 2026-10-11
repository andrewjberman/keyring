# AMGT_RESAPP task order -- `AMGT-ss-1` -- THE PEERS TABLE SAYS, IN ONE PLAIN SENTENCE, THAT THE SUBJECT'S CAP AND THE PEERS' CAPS ARE NOT ON ONE DATE (PORTAL DEV CANDIDATE)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ss-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~384</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ss-1.the-peers-table-says-why-the-dates-differ</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one component and a type, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS; the check renders statically over a captured payload.
comp-adversary: RUN at the cut -- r93_caveat_rendered.cjs FAILs C1, C3 and C4 at the base (no element) and PASSes C2, and PASSes all four arms against a throwaway PeersTab candidate (nothing written to the tree). Read 2026-10-11: the deployed /peers serves `subject.cross_vintage_caveat` on ASML, BA and ROG; `portal/src` names the field nowhere outside fixtures; the page prints the universe vintage and the subject cap's own as-of but not why they differ. Security Analysis is an Opal-internal (staff-only) page.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-384` (branch `wk-AMGT_RESAPP-384`, cut from the issuance commit; its nested portal worktree is `C:/dev/wk-resapp-384/portal`, branch `wk-AMGT_RESAPP-384-portal`, cut from portal DEV c96efe17). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-384` (or the portal path named below); a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-ss-1` (round 93, decomposition s.101)

CTO~DELL1 round-92 analysis item 1 (FWD-38's last gap). The peers route serves, on the subject, `cross_vintage_caveat` (a sentence that the band is
graded across two dates) beside `market_cap_vintage` (the subject's cap date, e.g. `2026-10-10T13:01:55Z`), and the set carries `universe_vintage`
(the peers' cap date, e.g. `2026-10-02`). The page prints both dates ("universe vintage October 2nd, 2026" in the subtitle, "as of October 10th,
2026" under the subject's Mkt Cap) and never says WHY they differ. In the PORTAL repository, in the nested worktree `C:/dev/wk-resapp-384/portal`
on a branch `wk-AMGT_RESAPP-384-portal` cut from `DEV`:

1. `src/pages/SecurityAnalysis/types.ts`: add `cross_vintage_caveat?: string | null` and `market_cap_vintage?: string | null` to `PeerSubject`.
2. `src/pages/SecurityAnalysis/tabs/PeersTab.tsx`: after the table's `overflow-x-auto` wrapper and BEFORE the "What is not on file" `<details>`,
   when `peers.subject?.cross_vintage_caveat` is a non-empty string render ONE `<p data-peers-cross-vintage-caveat="">` in the subtitle's ink
   (`text-[11px] text-[hsl(var(--palette-darkGray))]`) holding exactly this sentence, the dates through `longDate` (the same function the subject
   cell's "as of" uses):
   `Market caps are not on one date: the subject's is as of {A}; the peers' are as of {B}. The size band compares them as they are; neither is restated to the other date.`
   with `{A}` = `longDate(peers.subject.market_cap_vintage)` and `{B}` = `longDate(peers.universe_vintage)`. When either date is absent, that
   clause drops and the sentence reads `Market caps are not on one date. The size band compares them as they are; neither is restated to the other date.`
   The served `cross_vintage_caveat` text itself is NEVER printed (it speaks in the engine's terms: vintage, scalars, model block). When the field is
   absent or empty the page is byte-equal to today.

Nothing else moves: no other tab, component, token or served field. ASCII only in the product code (use `&apos;` for the apostrophes in JSX text).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W384-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only, nested worktree `C:/dev/wk-resapp-384/portal`, branch `wk-AMGT_RESAPP-384-portal` from `DEV`; never push; never touch `PROD`.
2. Edit `PeersTab.tsx` and `types.ts` only; no other component, no token change, no new file in the portal.
3. No deploy, no store write, no AWS call, no network. `bun install` is NOT allowed (the worktree's `node_modules` is a link to the main tree's).
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/types.ts
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~384/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ss-1"><invocation>cd C:/dev/wk-resapp-384/portal &amp;&amp; node ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round93_prep/checks/r93_caveat_rendered.cjs; echo "exit=$?"</invocation><expect>run in the PORTAL worktree, PASS C1 (one plain sentence after the table names both dates and says neither is restated, 3 of 3 pages), PASS C2, PASS C3, PASS C4; arms passed 4 of 4; R93 CAVEAT RENDERED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ss-1"><invocation>cd C:/dev/wk-resapp-384/portal &amp;&amp; node src/pages/SecurityAnalysis/__harness__/peersPattern.harness.cjs; echo "exit=$?"</invocation><expect>the stock peers harness still reads CHECKS-OK 13 of 13 (the control: nothing else on the page moved); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ss-1"><invocation>cd C:/dev/wk-resapp-384/portal &amp;&amp; bun run typecheck; echo "exit=$?"</invocation><expect>the portal typechecks (tsc -b) with 0 errors; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~384 <0.9.0_WK_AMGT_RESAPP~384@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~384/AMGT_RESAPP.TO-AMGT-ss-1.the-peers-table-says-why-the-dates-differ.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash (and the portal branch and commit hash);
- every criterion's output lines;
- the diff of each edited product file, in full;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-92 analysis @1edd8be57d item 1: "a portal product file, so the candidate comes to this seat before DEV". A portal candidate touching a product file: the CTO reviews it before the DEV landing (never the worker's act); PROD is a separate pair and Security Analysis is Opal-internal. `portal_ref` for the cut: `c96efe1714784162c4134450da33ce6fd6226b60` (local portal DEV, the base the check was dry-run at). The check is the issuer's: it renders the REAL PeersTab over the captured live payloads of ASML, BA and ROG (fixture `round93_prep/fixtures/peers_and_header_figures_ASML_BA_ROG_20261011.json`); a browser walk is the CVO's L9.

<status>pending</status>
<round>93</round>
<slot>0.9.0_WK_AMGT_RESAPP~384</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- issuer close 2026-10-11T10:47Z (2.0.0_SA_COO~R1): the portal DEV CANDIDATE is built -- portal branch wk-AMGT_RESAPP-384-portal @f4e09f2d47 (PeersTab.tsx +11, types.ts +5), proof @9e8cdb95ac VALID, merged to box/dell1 @34b31975c9. Issuer re-run in the portal worktree: AC1 R93 CAVEAT RENDERED YES (C1-C4, 3 of 3 pages), AC2 peers harness CHECKS-OK 13 of 13, AC3 tsc -b exit 0 (worker). The sentence is built from the two served dates and shown only when the caveat is served; with no date it drops that clause; the served engine sentence is never printed. Worker rows W384-S1 (the product commit lands in the nested portal repo: by design), S2 (the portal repo has no committer identity; the worker set GIT_COMMITTER_* per call and wrote no config) and S3 (comp-pulse PARTIAL_OR_BLIND and the commit gate 'checked 0 of 2' on a .ts/.tsx pair: the clean lines are not evidence for them, and the issuer's own re-runs are) ruled: stand. Owed: the CTO's product-file review before the DEV landing; PROD is a separate pair; L9: the CVO's read of the rendered peers page on ASML, BA and ROG on the DEV build.</status>

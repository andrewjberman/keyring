# TO DSGN_IRPTV1.TO-IV-t-1 -- the header identity card

<to_id>DSGN_IRPTV1.TO-IV-t-1</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~1</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>pending</status>
<round>1</round>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_IRPTV1_PRD.md` v0.5 @1cccbe6bc6 | **Decomp cell:** `IV-t-1` | **outcome_ref:** FWD-1 (hop 5), FWD-2, FWD-11 | **depends_on:** -- (chain A head) | **slot:** ~1, queue position 1

---

## WORKER FACE

### THE CELL

`IV-t-1` -- the IDENTITY CARD (PRD candidate C1, thread part; decomposition v1 section 3). Build `portal/src/pages/InvestorReporting/header/IdentityCard.tsx` and mount it at the ONE line in `portal/src/pages/InvestorReporting/index.tsx` -- line 186 at portal `7c542fd23ec70c88bade4e3270f4c87f267a275a`, which reads `<ScopeSummary scope={selectedScope} selection={acceptedNarrowing} row={accepted ? row : null} />` -- so that line becomes `<IdentityCard scope={selectedScope} selection={acceptedNarrowing} row={accepted ? row : null} />` (add props if you need them, e.g. a holdings snapshot, but the three existing props stay so the disclosure can render `ScopeSummary` unchanged). No other line of `index.tsx` changes. `header/ScopeSummary.tsx` is NOT edited (CTO ruling 100332): the card renders `<ScopeSummary scope selection row />` INSIDE its "About this scope" disclosure, collapsed by default (a `<details>` element is fine).

**What the card shows, from the wire and nothing else** (an advisor answers WHO / HOW MUCH / OVER WHAT / AS OF WHEN without opening a tab):
- WHO: the selected entry's `displayName` (`row.label` / `row.entry.displayName`), the firm's display name (`scope.verifiedRequestFirm.displayName`), the relationship or account kind in advisor words ("Relationship", "Account"), never the raw `kind` token.
- OVER WHAT: one chip per permitted account -- `DirectoryEntry.displayName` plus the masked tail (`maskedDiscriminator`), NEVER an `acc_` / `A-` id. A chip toggles to narrow the scope through the SAME selection request the page already makes (`header/selectionRequest.ts` via the `onSelectionChange` path `index.tsx` owns); the selection stays server-accepted -- you change presentation only. If wiring the toggle needs a change outside your `<paths>`, render the chips without the toggle and file an OBSERVATION row; the toggle is not a criterion.
- HOW MUCH: the holdings unique custody total (`HoldingsSnapshot.custodyTotalAmount` + `custodyTotalCurrency`) when a snapshot is in hand; else the words "value pending" (never zero). A snapshot is not passed to the header today; render "value pending" when the prop is absent and accept an optional `snapshot` prop so a later cell can feed it.
- AS OF WHEN: the business date (`scope.sourceTimestamps.businessAsOf`, else the snapshot's `businessAsOf`).
- THE PARTIAL-DATA INDICATOR (PRD v0.5 CONTRACTS; CTO 100332): when `scope.availability.unprojectedGrant.count > 0`, a visible line ON THE CARD BODY in advisor words (e.g. "2 of 5 accounts are not yet included"), never the token `unprojected_grant`; when a refusal carries `public_reason_code` UNPROJECTED_GRANT, its reason and no count; when count is 0 or the grant is absent, no line.
- "About this scope" disclosure: `ScopeSummary` rendered unchanged inside it (scope match, directory as-of, cohort chips, the `PartialDisclosureFact`) -- retained one click down.

**Component law.** A `Panel` from `@/ui/components/panels` (`Panel variant="nested"`, `PanelHeader` {title}, `PanelContent`), white surface, navy ink, the hairline, no shadow; `portal/DESIGN.md` C1 (Lato 400/700), C2 (tabular numerals on the total and the date), C3 (surface roles; never a band-valued variant), C8 (you add NO primary action), C9 (contrast). No `text-slate-*` idiom carried over from `ScopeSummary`.

**Prior art (read, never edit):** `portal/src/pages/AdvisorIntelligence/_shared/panels/ConsolidatedOverviewPanel.tsx` (the tile row + as-of), and section 2.1 of `org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_PAGE_PM_WALK_AND_DESIGN_CONCEPTS_20260924.md`. **Fixtures (adapted shape; `JSON.parse(readFileSync(...))`):** `portal/src/pages/InvestorReporting/fixtures/resolvedScope.success.json`, `fixtures/directoryEntry.success.json`, `fixtures/holdingsSnapshot.success.json`. Anna's real served node subtree (pre-adapter wire, a NAME reference only, not a render input): `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/anna.holdings-nodes.dec293d6.json`.

### ACCEPTANCE

<criterion id="IV1-AC1" cell_refs="IV-t-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~1; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-t-1.identity-card.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: IDENTITY-CARD-OK</expect></criterion>
`IV1-AC1` -- the built behaviour. Your test file (you write it, `bun:test` + `renderToStaticMarkup`, the fe-s suites' shape) renders `IdentityCard` over the three success fixtures and asserts, printing each count beside its denominator: the entry's `displayName` and the firm display name are in the markup; one chip per `permittedAccountIds` entry (`CHIPS: n of n`), each chip's text containing the account's `displayName` and masked tail and NOT its id; the custody total formatted from `custodyTotalAmount` when the snapshot prop is given, "value pending" when it is not; the business date. The final line prints `VERDICT: IDENTITY-CARD-OK` only when every assertion holds, else `VERDICT: IDENTITY-CARD-FAIL <which>`.

<criterion id="IV1-AC2" cell_refs="IV-t-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~1; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-t-1.indicator-and-vocabulary.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: INDICATOR-AND-VOCAB-OK</expect></criterion>
`IV1-AC2` -- the partial-data indicator and the vocabulary rule, as a DIFFERENCE CONTROL in one file: (arm 1) the scope fixture with `availability.unprojectedGrant = {count: 2, denominator: 5, kinds: ['account']}` -> the card BODY (outside the disclosure element) contains a line with "2" and "5" and the word "accounts", and NOT the string `unprojected`; (arm 2) the same fixture with count 0 -> no such line; (arm 3) the body contains NONE of `Scope match`, `Directory as of`, `Cohort`, `entitlement`, `revision`, `fingerprint`, `sel_`, `acc_`, while the disclosure element DOES contain `Scope match` (the positive control that `ScopeSummary` is retained). Print `ARM1: <present|absent> ARM2: <present|absent> ARM3: <clean|leak: tokens> CONTROL: <found|missing>` then `VERDICT: INDICATOR-AND-VOCAB-OK` only when arm 1 present, arm 2 absent, arm 3 clean and the control found.

<criterion id="IV1-AC3" cell_refs="IV-t-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~1; timeout 120 python -c "import subprocess;f='src/pages/InvestorReporting/index.tsx';n=subprocess.run(['git','diff','--numstat','7c542fd23ec70c88bade4e3270f4c87f267a275a','--',f,'src/pages/InvestorReporting/header/ScopeSummary.tsx'],capture_output=True,text=True).stdout.strip().splitlines();d=subprocess.run(['git','diff','-U0','7c542fd23ec70c88bade4e3270f4c87f267a275a','--',f],capture_output=True,text=True).stdout;ch=[l for l in d.splitlines() if (l.startswith('+') or l.startswith('-')) and not l.startswith('+++') and not l.startswith('---')];other=[l for l in ch if not l[1:].lstrip().startswith('import ') and not any(t in l for t in ['IdentityCard', 'ScopeSummary scope='])];print('NUMSTAT:',n);print('CHANGED-LINES:',len(ch),'OUTSIDE-MOUNT-OR-IMPORT:',other);ok=(len(n)==1 and n[0].split()[2].endswith('index.tsx') and n[0].split()[0]=='2' and n[0].split()[1] in ('1','2') and not other);print('VERDICT:','MOUNT-PLUS-IMPORT' if ok else 'TOUCH-WIDER-THAN-RULED')"</invocation><expect>VERDICT: MOUNT-PLUS-IMPORT</expect></criterion>
`IV1-AC3` -- the ruled touch, AMENDED by the issuer on CTO ruling 100467 (batch 34; supersedes the 1/1 bound of 100332, which a new component could not meet): `index.tsx` differs from `7c542fd23ec70c88bade4e3270f4c87f267a275a` by the ONE mount line PLUS at most ONE import line and nothing else -- numstat 2 added / 1 or 2 removed, and every changed line is either an `import` statement or the mount (the `ScopeSummary scope=` line out, the `IdentityCard` line in); `header/ScopeSummary.tsx` does not differ at all. The changed lines outside that set print beside the verdict (must be `[]`). Re-run in place.

<criterion id="IV1-AC4" cell_refs="IV-t-1" judgment="true"/>
`IV1-AC4` -- graded at L9 by `3.0.0_SA_CVO` from your static markup (save it to your deliverables folder as `iv-t-1.identity-card.html`) and, if `node scripts/ui-smoke.mjs investor-reporting <your deliverables dir>/iv-t-1.png --port <PORT> --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-14-cottonwood.json` runs for you (start `bun run dev --port <PORT>` in the background from `<WS>/portal` first; if it does not run, say so in the result file), the PNG: DESIGN.md C1, C2, C3, C8, C9 conformance and the brief's bar "an advisor answers who / how much / over which accounts / as of when from the header alone". RECORD; NO VERDICT.

<expected_criteria>IV1-AC1, IV1-AC2, IV1-AC3, IV1-AC4</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override. `header/ScopeSummary.tsx`, `render/**`, `contracts/**`, `api/**` and every file another cell owns are OUT of your grant by ruling (CTO 100332).
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo, based on `7c542fd23ec70c88bade4e3270f4c87f267a275a` on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records (the investigation row, your deliverables, the status flip): cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Toolchain.** `node_modules` is a junction; **do not run `bun install`**. bun is `/c/Users/AndrewBerman/.bun/bin/bun`. Tests: `bun test <file>` (`bun:test`). Typecheck is the COO's drain check, not yours.
- **The rules every cell obeys (PRD v0.5 CONTRACTS):** the FE derives nothing -- every figure is a wire fact off the adapted object (`contracts/index.ts` types); a fact the source did not supply renders the words "not supplied" (or "value pending" where this face says so), never zero and never a reason code as a value; the producer's vocabulary (envelope states, public reason codes, revisions, fingerprints, `sel_`/`acc_`/`req_` ids, source coordinates) renders ONLY inside a disclosure surface, never in a headline, tile, chip, table cell or band; the facts are retained there, not dropped.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is REFUSED and reported with your measurement -- never repaired, widened, or satisfied by a route this order did not name. Editing this face so your proof validates is a defect, not a pass.

<paths>
portal/src/pages/InvestorReporting/header/IdentityCard.tsx
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v1 @1f24052b87, cell `IV-t-1`.
<owned_cells>IV-t-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `IV1-AC1` .. `IV1-AC4`. Instance at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~1/DSGN_IRPTV1.TO-IV-t-1.identity-card.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> IV1-AC1,IV1-AC2,IV1-AC3,IV1-AC4` BEFORE the `complete` flip.
`IV1-AC4` is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- a `PASS` or `FAIL` on a judgment row is INVALID. Result file `identity-card.result.md` beside it. Flip `complete` only when every MECHANICAL criterion PASSES by output -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row in the investigation file above -- that file does NOT exist yet (the row gate refuses an empty channel file, so it is minted by its FIRST row): if it is absent when you need it, create it with the header line `# DSGN_IRPTV1 -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric). Append-only; rows below are minted by their own allocator (.tools/surprise-row-gate.py validates every NEW row).` followed by a fenced ```json array holding your row as its first item (the DSGN_REBRND W1-S1 precedent); a sibling slot may create the same file in its own worktree and the COO reconciles by UNION of rows at the drain (id `DSGN_IRPTV1-W1-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE at L5 (thread round; the lens runs on the enrichment round that touches its surface). The round's gates are sequencing inputs in the decomposition section 8; none is owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- measured, not assumed: a word-boundary AWS-surface token sweep over the PRD at HEAD (v0.5, 26,070 bytes) returned 0 of 11 tokens; no cell writes an AWS surface.
comp-adversary: DECLARED-NOT-APPLICABLE at L5 (thread round); runs on the enrichment round against the PRD and these orders.
lane: the <paths> block IS the grant (RULING 1). Portal entries resolve to <WS>/portal/<rest> and commit in the portal repo. header/ScopeSummary.tsx, render/**, contracts/**, api/** are out of every grant by CTO 100332.
</preflight>

Seating: slot ~1, queue position 1; fresh worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 1` off workspace `HEAD` and portal `7c542fd23ec70c88bade4e3270f4c87f267a275a` (e5dd8487 is-ancestor rc=0 at the cut).

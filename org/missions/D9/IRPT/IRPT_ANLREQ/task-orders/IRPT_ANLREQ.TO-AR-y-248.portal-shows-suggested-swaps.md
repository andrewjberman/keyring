# TO IRPT_ANLREQ.TO-AR-y-248.portal-shows-suggested-swaps -- the composer shows each verified swap as 'suggested', the person picks, nothing fills itself -- and the proxy box says what to type

<to_id>IRPT_ANLREQ.TO-AR-y-248</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~81</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-248` (`decompositions/IRPT_ANLREQ_DECOMP_R22B_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~81`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-81` (branch `wk-IRPT_ANLREQ-81`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~81 <0.9.0_WK_IRPT_ANLREQ~81@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W81-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-248`, inlined) -- THE PORTAL SIDE OF RULING B. A CANDIDATE on a portal branch; nothing is landed, pushed or deployed.

*Ruling B (CTO msg 7112): the person must pick a suggestion; it never fills the box or the request on its own; each is shown with its provider verification and the label "suggested"; no suggestion is shown as nothing, not as an error. The wire shape (built by `AR-y-247`, fixed here so the portal builds in parallel): on a `TICKER_NOT_FOUND` finding an OPTIONAL member `suggestions`: a list of `{symbol: string, source: "KIMI_SWAP_PROVIDER_VERIFIED", provider_receipt_sha256: string, reason: string}`, at most 3. The existing single `suggestion` (the typo lane, "Did you mean X?", `ProspectComposer.tsx` :484-493) stays as it is. Andrew's own test (row D2-S77): the proxy box said only "Ticker".*

1. **The branch.** The portal repository is `C:/dev/ajb_workspace/portal` (a separate git repository). `git -C C:/dev/ajb_workspace/portal fetch origin DEV` is permitted. Record `dev_tip` (full sha of `origin/DEV`). Make a worktree OUTSIDE the product tree: `git -C C:/dev/ajb_workspace/portal worktree add C:/dev/wk-portal-81 -b wk-IRPT_ANLREQ-81-portal origin/DEV`. Never check out, reset or commit anything else in the portal checkout, and never push. Commit the way an earlier candidate branch was made (`git -C ... log` of `wk-IRPT_ANLREQ-63-portal`); if a hook or a rule of the portal repository refuses your commit, STOP and file a row with the refusal text. Read the portal's own `CLAUDE.md` and `DESIGN.md` first: new text follows their clauses (navy ink on white panels, no light-on-light; cite the clause number in your record for each visual choice).
2. **The change.** In the proxy row (`ProspectComposer.tsx` :472-503, and the finding type/reader in `prospect.ts` :54-67 `proxyableFindings` and the wire types): (a) read the optional `suggestions` member (absent, not a list, or an item without a string `symbol` is treated as none, never an error, never a thrown exception); (b) for each of up to 3 items show a line `Suggested: <symbol>` with the text `suggested` as a visible label, the provider verification words (`verified by the data provider`), the item's `reason` as plain text (React text, never HTML), and a button `Use <symbol>` that, ONLY when pressed, sets that row's proxy input (the same state update the existing `Use <suggestion>` button does); (c) NOTHING fills the input, the request or any default without that press, on any render; (d) the proxy input's placeholder and a hint line under "Name a proxy" say what to type, in the words the read record proposes: `This ticker is not in the data provider. Type the ticker of a security the provider prices, such as a listed ETF with the same kind of exposure, then review again.` (use them as written; do not name a particular ticker as an example); (e) with no suggestions the row shows nothing extra (no "no match" error text). Touch `src/` only and change no wire reader or contract file beyond the optional member's TYPE.
3. **The tests, before and after.** In the portal's existing test folder for this component: (a) an item in `suggestions` shows `Suggested: <symbol>`, the label, the verification words and the reason; (b) pressing `Use <symbol>` sets that row's proxy input and nothing else; (c) without a press the input is empty on first render and after re-render, and the request body built by the upload call carries no proxy; (d) `suggestions` absent, `null`, `[]`, a non-list, or items without a symbol render NO suggestion lines and do not throw; (e) a reason holding markup characters is rendered as text; (f) the hint line is present. `before_arm`: on `origin/DEV` WITHOUT the change (a), (b), (f) FAIL. `tests`: all pass with the change; the whole component folder (counts; known `dsgn-irptv1` failures stated with counts both ways); `bun run typecheck`.
4. **Commit** in the portal worktree; record the full sha.
5. **Write `r22/PORTAL_SUGGESTED_SWAPS_CANDIDATE.json`:** `dev_tip`, `branch`, `commit`, `files_changed`, `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm` {`failed`, `output_tail`}, `what_a_person_sees` (the words as rendered, for a finding with two suggestions and for one with none), `design_clauses`, `claim`, `not_read`.
6. **In your report:** the branch, the commit, the counts, what a person sees in both cases.

### ACCEPTANCE

<criterion id="AR248-y-AC1" cell_refs="AR-y-248"><invocation>python C:/dev/wk-irpt-anlreq-81/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y248-portal --root C:/dev/wk-irpt-anlreq-81</invocation><expect>Y248-PORTAL-OK</expect></criterion>
`AR248-y-AC1`: the record names a portal commit under `src/` only with added tests that fail on the DEV tip without the change and pass with it, covering the pick, the no-auto-fill, the no-suggestion and the malformed-member cases.

<criterion id="AR248-y-AC2J" cell_refs="AR-y-248" judgment="true"/>
`AR248-y-AC2J` (judgment, graded at L9, never by you): nothing fills a box or a request without a press, a missing or malformed `suggestions` member shows nothing and does not throw, the reason is rendered as text, the hint words are the read record's, the design clauses were read, and nothing was landed or pushed.

<expected_criteria>AR248-y-AC1 AR248-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~81/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R22B_Y.md</decomp_doc>
<owned_cells>AR-y-248</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~81/IRPT_ANLREQ.TO-AR-y-248.portal-shows-suggested-swaps.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-248`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR248-y-AC1,AR248-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling B (msg 7112) and the read record `0.9.0_WK_IRPT_ANLREQ~76/r22/PROXY_SUGGESTION_READ.json` against the cell; the lens: a suggestion that fills a box or a request on its own, a candidate shown without its provider verification, a gate that is skipped because the next one is built. The order requires the user to pick, the gates in their order, and the no-suggestion case to show nothing. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling B (msg 7112: the Kimi swap advisory, behind its own three gates; a suggestion never fills the box) as workstream `YR` round 20. Base: `AR248-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.

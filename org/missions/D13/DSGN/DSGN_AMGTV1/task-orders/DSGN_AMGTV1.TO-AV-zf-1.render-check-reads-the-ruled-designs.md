# DSGN_AMGTV1 task order -- `AV-zf-1` -- THE RENDER CHECK READS FWD-15 AND FWD-16 ON THE RULED DESIGNS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zf-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~79</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the served names were resolved by the issuer at the cut and are a file input.
comp-adversary: RUN by the issuer at the cut on portal 415f50db -- render.cjs 0 of 3, fixture.cjs 1 of 3 (both FAIL as expected).
EGRESS CLASS, declared: NONE. No fetch off this machine (the render check builds and serves the portal from disk through Playwright).
</preflight>

## 1. THE CELL -- `AV-zf-1` (round 28, decomposition v28; instrument repair for FWD-15 / FWD-16 / FWD-20)

DIRECT ACT, instrument only: no product file changes. Read `org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/adjudications/ADJUDICATION_v27.md`
section 2. The render check (`portal/scripts/ui-contract-check.mjs` + `portal/scripts/ui-measure.mjs`) holds two clauses that are
stale against ruled designs, and its fixture leaves FWD-15's ABSENT half unread and prints raw keys on the chatter face.

Build, three items:
1. **fwd15 column count** (`portal/scripts/ui-measure.mjs`, the `kind === 'model'` block, `const cols = table.querySelectorAll('thead th').length`).
   The Model table's head has TWO rows when consensus estimates are served: a consensus row (`<td colSpan>` + `<th colSpan={estimateCount}>`)
   above the header row (the title `th` + one `th` per year; `portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx:443-462`). Counting
   every `thead th` adds the consensus `th`, so a REFUSED row that spans the table reads 14 against 15. Make `cols` the sum of the
   `colSpan` of the cells of the LAST `thead tr` (the header row). Nothing else in the `spans` test changes.
2. **fwd16 reason predicate** (`portal/scripts/ui-contract-check.mjs`, `const noReason = t.items.filter(i => !i.reason || !i.text.includes(i.reason))`).
   Rulings r22-1 and r23 (FWD-16) put READER WORDS on the face and the SERVED reason on `data-absent-column-reason`. Keep ONE inline
   expression of the form `const noReason = t.items.filter(i => ...)`: a listed column is flagged when its served reason is empty
   (`!i.reason`) OR its face text carries nothing beyond its own column name (`i.text` with `i.name` removed, then trimmed of
   punctuation and spaces, is empty). It is NOT flagged merely because the face words differ from the served reason.
3. **The contract fixture** (`portal/src/pages/SecurityAnalysis/__harness__/tests/uiContractFixtures.json`):
   a. Every row of the `/api/scoped/amgt/lead-panel/timeseries/collected/chatter` payload takes `display_name` from the issuer's served-names
      file `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round28/fixtures/served-names.collected-chatter.json`
      (`names[security_key].display_name`; 95 of 95). Nothing else in that payload changes: keys, `by_month`, `as_of`, `months` and the rest.
   b. In the `/api/scoped/amgt/security/BA_US_Equity/thesis` payload, drop every figure whose `mnemonic` is `RETURN_ON_TANGIBLE_ASSETS`
      from BOTH `fiscal_year_figures` (top level) and `model.fiscal_year_figures`. That makes RoTA the one ABSENT row, so the Model tab
      draws its "No figures served for: RoTA." footnote. No other figure changes.
   This JSON is ~31k lines, so item 3 alone MAY be applied by one Python script (an exception to bound 4 for this one file). It
   must load the file as UTF-8, edit only the fields above, and write `json.dumps(d, indent=1, ensure_ascii=False)` as UTF-8 bytes
   with no trailing newline. The issuer verified that this round-trips the base file byte-for-byte. Run the script from your
   scratch area. Never commit it.

**Design law and contracts:** the instrument grades the ruled designs, never the producer's text. A raw code never appears on a face
the instrument renders.

## 2. BOUNDS

1. No server you start yourself, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue. (The check's own
   vite build and Playwright run are local and allowed.)
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit the two scripts with the Edit/Write tools ONLY. Never use a shell heredoc or `python -c` on them. The single exception is item 3's fixture script.

## 3. SURFACES

<paths>
portal/scripts/ui-measure.mjs
portal/scripts/ui-contract-check.mjs
portal/src/pages/SecurityAnalysis/__harness__/tests/uiContractFixtures.json
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~79/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round28/`, `round26/` and `round15/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zf-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round28/checks/render.cjs" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>THE RENDER CHECK READS FWD-15 AND FWD-16 ON THE RULED DESIGNS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zf-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round28/checks/fixture.cjs"; echo "exit=$?"</invocation><expect>THE CONTRACT FIXTURES SERVE NAMES AND AN ABSENT ROW: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zf-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round26/checks/battery.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY: ALL PASS -- and exit=0</expect></criterion>
</proof_of_spec>

The three criteria:
- **AC1** builds the portal and runs the contract check on the model and peers states. Arm 1: fwd15 PASS, with a REFUSED row and one
  ABSENT footnote both read. Arm 2: fwd16 PASS. Arm 3: the fwd16 predicate accepts reader words plus a served reason, and rejects a
  missing reason and a bare name.
- **AC2** checks the fixture: 95 of 95 served names, nothing else moved, and RoTA the one absent row.
- **AC3** is the round 20-26 page battery (a harness reads this fixture).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~79/DSGN_AMGTV1.TO-AV-zf-1.render-check-reads-the-ruled-designs.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W79-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (LOCAL), batch instrument repair. CTO msg 28537 (asked as a round-27 amendment; cut as round 28, v28 says
why). No product file, so the candidate can land on DEV by its author as a fast-forward (CLAUDE.md Portal). Chain ~79 alone. Base:
render 0 of 3, fixture 1 of 3.

<status>complete</status>
<round>28</round>
<slot>~79</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>

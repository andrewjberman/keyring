# TO IRPT_BCKEND.TO-IB-rt-11 -- INTAKE CURRENCY AND UNIT CONTROLS: explicit supported-currency and unit validation with non-USD, subtotal, multi-sheet and ambiguous-total controls, quarantine over relabeling, and human correction provenance preserved

<to_id>IRPT_BCKEND.TO-IB-rt-11</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~3</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending -- RE-OPENED by 0.9.0_WK_IRPT_BCKEND~3 at 2026-09-12T02:4xZ, and the reason is a defect in MY OWN RECORD, not in the world. The complete flip at 3c28723d20 pinned infra/aws/lambda/investor-reporting/intake/parse.py at dc5d119b84, a version that does NOT carry the `load_intake_controls` refusal that arm (e)'s negative arm proves -- the edit was made after that commit and never committed, so the arm passed against the WORKTREE while the instance named bytes that could not produce it. Found by reading `git status` after the flip. proof-of-spec-check now reads INVALID (artifact-resolution, CCX class), which is the correct reading, so the order is OPEN until the bytes and the pin agree. Re-flips to complete only on an instance that is VALID with parse.py pinned to the commit that carries the refusal.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 2 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.13 @e6ba5d9878 (ADMITTED, both L4-R halves SIGNED) | **Round-1 analysis:** `../ledger/ROUND_ANALYSIS.round1.md` @0d57ceb2f9, ruling 7 (intake) | **Slug rows this cell closes:** C-S74 | **Decomp cell:** `IB-rt-11` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.2, s.1 + s.2) | **outcome_ref:** FWD-9 (own), FWD-4 | **PRD candidate:** B7

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~3` (the same subagent as round 1, continued with its context intact). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~3;`.
- **Worktree:** `/c/tmp/wk-irpt-2-3` on branch `wk-irpt_bckend-2-3`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-2-3/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~3 <0.9.0_WK_IRPT_BCKEND~3@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/` (granted by the tree convention; no `<paths>` entry needed). Round-2 batteries are named `battery_<cell>.py` with the cell id lower-cased and hyphens as underscores.
- **Queue:** fourth and last in slot ~3, after IB-rt-10.

---

## THE CELL

**The PRD row, verbatim at @e6ba5d9878 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B7 holdings parse + validate + correction state
- **serves:** FWD-9 (own), FWD-4 (contrib)
- **brief sections consumed:** O3 parse paragraph; IV.4 parse paragraph
- **contracts (P=produces, C=consumes):** P `AnalysisRequest.normalized holdings / findings / corrections`; P `StatusEnvelope.needs-correction`
- **paths: reuse:** --
- **paths: new home:** `infra/aws/lambda/investor-reporting/` (parser)
- **fixtures / evidence:** supported CSV/XLSX specimens; `$:CASH`; share-class mapping cases
- **acceptance clause draft:** deterministic parse keeps units, source cells, totals, grouping and cash; unmatched holdings are never discarded or silently substituted; approved substitutions captured explicitly; uncertain items enter the correction state; `management_fee=0.003` is the recorded current setting

**The CTO's ruling this cell executes (ROUND_ANALYSIS.round1.md @0d57ceb2f9, verbatim):** INTAKE AND ATTRIBUTION CONTROLS. Explicit currency/unit validation with non-USD, subtotal, multi-sheet and ambiguous-total controls, quarantine over relabeling (C-S74).

**What L5 adds (decomposition v0.2 s.2, s.6, s.9):**

- `intake/parse.py`: a value column's currency/unit is READ from the specimen (a header token, a symbol, a declared column) and validated against the supported set (`USD` only this round, declared in `settings.json`); an unsupported or ambiguous currency/unit sends the row -- or the specimen -- to QUARANTINE (`needs-correction` with the finding `UNSUPPORTED_CURRENCY` / `AMBIGUOUS_UNIT`), never relabeled to USD; subtotal rows, multi-sheet workbooks and an ambiguous total (two candidates) each read as their own finding with the source cell; a human correction on a quarantined row carries provenance (who, when, from what) on r+1 and the parser never overwrites it.
- Four adversarial specimens, one per control, plus the round-1 five; the difference control: a build that relabels a CAD column to USD FAILS the reconcile.

---

## WHAT ROUND 1 DELIVERED THAT THIS CELL BUILDS ON (not rebuilt)

the deterministic parser, the correction state and `settings.json` (IB-s-7, 6 of 6 arms; the judgment that `USD` is a unit in the contract, not a currency); the intake poller and its offline transport (IB-s-6).

---


---

## ISSUER AMENDMENT -- 2026-09-12T01:14:33Z (`2.0.0_SA_COO~B`): THE HAND-OFF. This block governs over every line above it.

### B1. YOUR GATE IS SATISFIED AND THIS ORDER IS NOW PENDING.
The `<status>` above read *"staged ... becomes pending when the COO hands it over after IB-rt-10 is terminal and
merged."* IB-rt-10 is terminal -- `<status>` complete, and the issuer re-graded its proof-of-spec instance
`VALID (rc=0)` at HEAD rather than taking the worker's word -- and its branch is drained to CLOUD at `08962bd2ea`.
**Begin immediately.**

### B2. NEW WORKTREE. Whatever the IDENTITY section names, it is NOT where you work.
- **Worktree:** `/c/tmp/wk-irpt-2-3c` on branch `wk-irpt_bckend-2-3c`, cut by the issuer from CLOUD at `08962bd2ea`.
- Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-2-3c/`.
- **Do NOT work in `/c/tmp/wk-irpt-2-3b`.** That is IB-rt-9's worktree, its order is still OPEN on arm (e), and
  its branch is a different one. Two orders must not share a branch.
- First act: `git rev-parse --abbrev-ref HEAD`, then `test -d org && test -d .tools && echo TREE-OK`.

### B3. YOU CARRY IB-rt-9's CONTEXT, AND EXACTLY TWO THINGS FROM IT TRANSFER.
You are the same subagent that ran IB-rt-9, so you are not cold -- but that cell's WORKTREE, BRANCH and OPEN ARM
are not yours here and must not be touched from this order.
- **The build/packaging knowledge does NOT apply to this cell.** IB-rt-11 deploys nothing. Do not reach for the
  zip recipe, the source map or any Terraform root.
- **What DOES transfer is the discipline:** name the instrument, print the denominator, and give every detector a
  POSITIVE and a NEGATIVE control. Your arm (a) census on IB-rt-9 was wrong twice before it was right, both times
  because the discriminator was looser than the question -- that lesson is the one to carry.

### B4. THE CELL'S OWN LAW: QUARANTINE OVER RELABELING.
The title is the rule. A value whose currency or unit cannot be established is **QUARANTINED, never relabeled to
the expected one** -- and a quarantine is a legitimate, reportable outcome, not a failure to handle the case.
Specifically:
- **Never infer a currency from a symbol, a locale, a column header or a neighbouring row.** If the document does
  not establish it, the row is quarantined and says why.
- **Human correction provenance is PRESERVED, not overwritten.** A corrected value carries who corrected it and
  what it was; a correction that erases its own prior value destroys the audit the cell exists to create.
- **Subtotal, multi-sheet and ambiguous-total controls are the point, not edge cases.** An ambiguous total that
  silently picks one reading is the exact defect; picking none and saying so is correct.

### B5. THE ADJACENT CELL'S MEASURED LESSON, SO YOU DO NOT REPEAT IT ONE CELL OVER.
IB-rt-10 filed row `IRPT_BCKEND-W4-S28`: round 1 dated **15 of 61** overview rows and **12 of 108** multi-comparison
rows from a NEIGHBOURING block, and **every one of them passed all three of round 1's certification legs** -- because
a date sits at none of the coordinates those legs inspect. **A certification that does not inspect the coordinate
where the defect lives passes it every time.** Before you certify a currency or a unit, state WHICH COORDINATE your
check reads and satisfy yourself that a wrong value would actually be visible there. Say so in the arm.

### B6. FIXTURES AND HONESTY ABOUT THEM.
If the specimens available to you are synthetic, say so ON THE ARM and do not describe the result as certification
against real client input. **Do not manufacture a representative real-client specimen.** An arm that can only be
exercised on synthetic input is a real result with a stated boundary; an arm that pretends otherwise is not.

### B7. THE SAME STANDING MECHANICS AS EVERY ORDER THIS ROUND.
- Prove each criterion by RUNNING the invocation the face names and showing the expectation met by OUTPUT.
- **The acceptance token goes into the battery's output ONLY in the edit that makes every arm pass**, never
  negated, never as "NOT ASSERTED" -- `<expect>` is graded as a REGEX and a negated line MATCHES.
- Write the proof-of-spec instance only when the mechanical criteria pass; `PENDING-THIS-COMMIT` is ONE-SHOT.
  A judgment criterion gets its output and NO verdict, under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason`
  naming `3.0.0_SA_CVO`. Flip `<status>` only on `rc=0` plus every mechanical criterion PASS-by-output.
- Rows are `IRPT_BCKEND-W3-S<k>`; **re-read the channel at HEAD immediately before minting** (it moved to 148 rows
  and is moving). Never edit an existing row. A surprise is a ROW and you keep working.
- `safe-commit.sh` with explicit FILE paths and a Write-tool message file; your branch only; never push, merge,
  rebase, `checkout --` or `clean`.
- A rail denial aborts the WHOLE Bash call and silently no-ops every later segment -- put gated reads in their own
  call. Heredoc backslashes arrive HALVED. Raw `grep`/`find` over a directory routes to `comp-find`.


## DELIVERABLE

`infra/aws/lambda/investor-reporting/intake/{parse.py,corrections.py,settings.json}` + tests + `fixtures/holdings/` (4 new specimens); the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_rt_11.py` and `.result.md`.

---

## BOUNDS

- **Quarantine over relabeling**: an unsupported currency is never converted or renamed.
- **No deploy in this cell** (the intake Lambda's next build carries it); no mailbox read (bound 1).

### Bounds every order carries (decomposition v0.2 s.8, verbatim)

1. **NO LIVE VENDOR CALL.** Endpoint, verbatim: *"NO LIVE VENDOR CALL is authorized by this document -- availability is not authorization; a live YCharts, Black Diamond or Orion call needs Andrew's explicit per-use word."* The same bound covers the mailbox read and a YCharts login or session capture. A cell that carries a live arm proves its MECHANISM against recorded fixtures through a transport stub with a difference control; the live arm is an express qualification read by the CTO at L10 on Andrew's per-use word, never something this order does.
2. **NO MONITOR, ALARM, SNS OR SES SEND.** Nothing in this project notifies anyone. A scheduler this project creates is the product's own trigger and is applied `DISABLED` where its first fire would be a vendor call.
3. **CROSS-FIRM, both shapes.** Per-firm prefixes + IAM conditions in the shared bucket; the FIRM's own bucket for directory and holdings data; the `FirmDestinationPolicy`; the firm fixed from the sender's domain at ingestion and immutable after; Global GRANTED to an Opal principal, never to a firm one; no new all-firm financial aggregate.
4. **Deploys (NEVER-2, NEVER-9).** `.tools/safe-apply.sh` only, from a root whose state key is this cell's; a change-management entry opened at the start (`python .tools/deploy_ledger.py open ...`) and its OPEN sentinel `org/critical_paths/.open_deploys/<slug>.json` COMMITTED IMMEDIATELY (row W3-S4's rule) before the act; the entry closed at completion and COMMITTED BEFORE the reads that grade the act; served bytes verified as `CodeSha256` against the built zip, never by filename; `aws lambda update-function-code` never; `.tools/terraform.exe` is provisioned in your worktree by the issuer -- use it by that path, never a PATH substitute (a substitute re-pins remote state); every provider cache was purged estate-wide, so `init` each root you plan with the vendored binary.
5. **Andrew's four fixed constraints are not build choices:** the BDAPI-with-Kimi runner STYLE with NO OTP branch; the firm from the sender's domain at ingestion gated to enumerated destinations; the multitenant `api/scoped/` layout; terminated clients STAY VISIBLE under entitlement. And the endpoint's: units are part of a number's meaning; unsupported positions are never silently removed; no PUT of global YCharts preferences; no vendor call in render or preview; missing history is an answer, not an empty state; the narrative states contemporaneity and never causes; model targets never masquerade as observed holdings; THE YCHARTS MECHANISM IS FIXED (v0.9: K3 capture on the dedicated host -> fenced publication -> browserless Lambda REST replay).
6. **No credential in any artifact, log, fixture or commit.** Secrets are read by NAME at runtime; a recorded fixture is scrubbed before it is committed; signed URL parameters are never logged; a `describe-secret` prints version state, never a value.
7. **No served output is touched.** The 28 existing CloudFront behaviors, the 14 pre-existing scoped routes, this project's 11 live routes and every existing bucket, table and Lambda are read, never edited, except where THIS order's cell says it CHANGES or ADDS a resource.
8. **The spec is FROZEN mid-round.** A premise that does not hold, a path that is not where this face says, a result the invocation does not produce, a capability you lack: ONE row at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W<your slot>-S<k>` (a DS lane mints `IRPT_BCKEND-D-S<k>`), per `org/surprise_channel/schemas/investigation_item.schema.json`, inside the fenced json array, appended never edited, k continuing your slot's round-1 numbering; then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.
9. **Every invocation terminates.** You run each named invocation under `timeout`; rc 124 IS the recorded output, retried once at most.
10. **Every `.py` edit passes `.tools/commit-gate.sh`.** Python 3.12 (`Python312` first on PATH; bare `python` may resolve to 3.14 without PyYAML). ASCII only in production code, logs and AWS names (`OK:`/`WARN:`/`ERROR:`/`SKIP:`/`BLOCKED:`).
11. **Scratch** is `<your worktree>/.scratch/` only.
12. **NO SELF-WRAPPING HARNESS AS EVIDENCE (round-1 lesson, rows W1-S10, S24).** An arm's subject is the REAL artifact -- the real route file, the real dispatcher, the deployed function, the served object -- never a copy the battery wraps, patches or re-registers itself. A census reads the real population and prints its denominator; a `0 of 0` is printed as VACUOUS, never as a pass. Every manifest of hashes a cell writes is re-derived by its battery every run (row W3-S9).
13. **TYPED, ISSUED IDENTIFIERS AT EVERY BOUNDARY (round-1 lesson, rows W2-S9/S11, W1-S7, W3-S12).** Firm, client, relationship, account, report, export and job ids cross a function boundary as ISSUED opaque ids of a declared type; a display name, an e-mail address, a raw upstream key or a request-controlled firm token is refused at the boundary, and a refusal never echoes the refused value.

---

## ACCEPTANCE

<criterion id="RT11-AC1" cell_refs="IB-rt-11"><invocation>timeout 300 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_rt_11.py</invocation><expect>IBRT11-INTAKE-CONTROLLED</expect></criterion>
**`RT11-AC1` -- PASSES BY OUTPUT -- four controls, quarantine not relabeling, provenance preserved.**
**(a) FOUR OF FOUR.** Non-USD, subtotal, multi-sheet, ambiguous-total specimens each produce their own finding with the source cell and enter quarantine; printed with counts.
**(b) THE DIFFERENCE CONTROL.** A relabeling build converts CAD to USD and FAILS the reconcile; the correct build holds; both printed.
**(c) PROVENANCE.** A human correction on a quarantined row appears on r+1 with who/when/from-what; r untouched (hash); a re-parse does not overwrite it.
**(d) ROUND 1 STILL HOLDS.** The five round-1 specimens still parse byte-identically (hashes).

<criterion id="RT11-AC2" cell_refs="IB-rt-11" judgment="true"/>
**`RT11-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: where 'programmatic by default, review the exception' would now become 'review everything' on a real advisor's workbook; which currency signals the specimens could not represent; and what a quarantined specimen looks like to the advisor who forwarded it. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>RT11-AC1, RT11-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-11.intake-currency-and-unit-controls-quarantine-over-relabeling.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/intake/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.2, cell `IB-rt-11` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-rt-11</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger. BLIND SPOT, stated: the round-1 cut-time run (5 of 5 carriers, 0 gates naming this project) is inherited, not re-run here.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied by this cell; no policy, role or trust document is written. BLIND SPOT: the reads this cell makes run under the launching seat's credentials, stated not measured.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `docs/contracts/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL or its documentation lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: RT11-AC1, RT11-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-rt-11.intake-currency-and-unit-controls-quarantine-over-relabeling.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-rt-11.intake-currency-and-unit-controls-quarantine-over-relabeling.proof_of_spec.json RT11-AC1,RT11-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.

# TO LGIC_CANON.TO-CN-q-1 -- round 5 CN-q-1: R1: step 13 re-run on today's naming tools; every remaining RAISE gets its registry row
<to_id>LGIC_CANON.TO-CN-q-1</to_id>
<project>LGIC_CANON</project>
<issued_to>0.9.0_WK_LGIC_CANON~2</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `CN-q-1` (`decompositions/LGIC_CANON_DECOMP.md`, round-5 section) | **outcome_ref:** FWD-5 |
**depends_on:** none (slot ~2)

---

## WORKER FACE

### CONTEXT

**Where the project stands.** LGIC_CANON's outcomes FWD-1 to FWD-4 and FWD-6 are REALIZED. FWD-5 -- the onboarding checklist
(`infra/logic/10_ONBOARDING_CHECKLIST.md`, 16 steps) followed start to finish on the `LGIC_LGCTFM` practice wave over an existing firm's subject, with
nobody making a judgement call the rules should already have made, and the firm's people seeing their dashboard exactly as before
-- is NOT REALIZED. Round 4's run (`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/C6_RUN.md`, `C6_RUN_RECORD.json`) reached 12 and carded 4 of 16 on
the 49financial wave `workflows/legacy_transform/blackdiamond-49financial/20260918T011619Z-8db9eb1/` (contract hash `33204e29839de89af81fb293317cce3ccdf2266d`). Two carded causes sit outside the
firm-bucket carve-out: step 13 (a naming RAISE) and step 14a (the portal paths, an input no rule defined). The CTO's round-5
analysis (`org/missions/D14/LGIC/LGIC_CANON/ledger/ROUND_ANALYSIS.round5.md`) rules both and names this round's three items.

**The instruments.** `python lib/opal_naming.py census --names FILE` grades `TYPE<TAB>NAME` lines; a RAISE stops the run (exit 3)
unless carded; since 2026-10-09 the census reads `infra/logic/registry/name_rulings.json`, so a name with a ruling row prints
`CENSUS RULED ... name_rulings.json#<i>` and does not stop. `lib/opal_naming.py name()`/`key()`/`address()` are the builders;
`infra/logic/registry/` is the registry (`scopes.json`, `systems.json`, `key_rulings.json`, `name_rulings.json`, ...). The portal's
page-access map is `portal/src/lib/firmAccess.ts` `FIRM_ALLOWED_PATHS`. Python 3.9 syntax, ASCII only, no new dependency. The bar:
`python -m pytest lib/tests -q -p no:cacheprovider` (199 passed, 1 skipped at the base) must not newly fail. The checks are
`org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r5/check_cn_r5.py` (read-only; read it before you build -- each arm states exactly what it reads).

**Client-data bound (0.0.0_AB_MSTR msgs 2712, 2739, 2758, 2796).** Search ONLY inside paths you name, never the whole repo and
never in history. Never open, search, copy or git show anything under org/missions/D9/IRPT/IRPT_DASHBD/deliverables/, any
org/**/W73_S*_EVIDENCE.json, or any cottonwood manifest.

### THE CELL

`CN-q-1` (analysis R1). Step 13 censuses the firm's names. Round 4 carded it on a RAISE. Under rule 30 a builder REFUSAL is a
missing registry row to add, never a hand-typed workaround. The naming tools moved since (the census reads `name_rulings.json`;
the gate grades built and PATTERN names).

**Build:**
1. Re-run step 13 over the practice wave's names: every row of `workflows/legacy_transform/blackdiamond-49financial/20260918T011619Z-8db9eb1/contract.json` (184 rows, `node_type` and
   `current.name.value`) through `census --names`, with no card file. At the base it STOPS on its first RAISE:
   `blackdiamond/49f/session-trigger-mode.json` (S3Key, K3: not a tier). Re-run after each fix, until the run COMPLETES.
2. For each RAISE that remains, add the registry row that answers it, in the file whose `_about` covers it:
   `key_rulings.json` for a stored-file path, `name_rulings.json` for any other name. Copy the shape of that file's existing rows,
   and fill `evidence` (what you read, file:line) and `owner` (who moves or renames it). Change no row already there.
3. `org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~2/step13.r5.result.md`: every RAISE met, the row added for it, and the final run's last line.
If a RAISE's answer cannot be read from the repository, stop on that name and file a row; never invent an answer.

### ACCEPTANCE

<criterion id="Q1R5-AC1" cell_refs="CN-q-1"><invocation>timeout 1500 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r5/check_cn_r5.py step13</invocation><expect>PASS-R5-STEP13</expect></criterion>
`Q1R5-AC1` -- all 184 wave names pass the census with no card file: COMPLETE, 0 RAISE.

<expected_criteria>Q1R5-AC1</expected_criteria>

Run every invocation from the root of your worktree. Each invocation's LAST printed line is the line the expectation is matched
against. Commit your artifacts first, then run the criteria against the committed bytes.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file. Nothing in this prose grants a path.
- **Nothing live moves.** No `safe-apply`, no Terraform, no AWS write, no portal push, no route change, no IAM change.
  `portal/src/lib/firmAccess.ts` and `infra/aws/lambda-edge/_shared/firm-config.mjs` are READ, never written.
- **Refusal clause.** If a criterion cannot be met as written, stop on it, write the reason in your report and a surprise row (id
  `LGIC_CANON-D1-W<n>-S<k>`, `<n>` your slot, `<k>` one above the highest in the channel at your write time; `surfaced_at` =
  `date -u +%FT%TZ` at filing) in `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md` by textual splice, and never weaken a check or an expected value.

<paths>
infra/logic/registry/name_rulings.json
infra/logic/registry/key_rulings.json
org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~2/step13.r5.result.md
org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~2/LGIC_CANON.TO-CN-q-1.step13-registry-rows.proof_of_spec.json
org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.TO-CN-q-1.step13-registry-rows.md
</paths>

The block is your WRITE grant. You read and never edit anything outside it.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md</decomp_doc> v7, round-5 cell `CN-q-1`.
<owned_cells>CN-q-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Q1R5-AC1. Instance at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~2/LGIC_CANON.TO-CN-q-1.step13-registry-rows.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Q1R5-AC1 --governing-order org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.TO-CN-q-1.step13-registry-rows.md` BEFORE the
`complete` flip. Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.
</proof_of_spec>

**REPORT:** each RAISE met and the row that answers it; the final census line; the last line of every criterion whole; your commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no grant, no AWS call.
comp-adversary: RUN -- the cheapest pass carded every RAISE: the arm runs with no card file. A row with an invented answer: each row cites file:line evidence, and the drain reads every added row against its evidence. Editing an existing row to make a name pass: the drain diffs the registry for changed (not added) rows. BLIND: the arm checks that the names pass, not that each added row's answer is correct; that is the drain's read. LANE: infra/logic/registry/ is 4.0.0_SA_CRO's lane; the worker reaches it only through worker_grant (the <paths> of this non-terminal order). If the lane refuses, the worker drafts the rows in its deliverables folder and files the refusal as a BLOCKING row.
lane: the <paths> block IS the grant (worker RULING 1); nothing in the prose grants a path.
</preflight>

Source: `org/missions/D14/LGIC/LGIC_CANON/ledger/ROUND_ANALYSIS.round5.md` (`1.0.0_SA_CTO~DELL1`, msg 3013); decomposition round-5 section. Base dry-run at the cut, by the issuer at base
9794664db4: Q1R5-AC1 base: FAIL as expected (wave names=184 rc=3 ruled=0 raise=1, STOPPED on S3Key blackdiamond/49f/session-trigger-mode.json, K3).

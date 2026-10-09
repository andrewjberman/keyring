# TO LGIC_CANON.TO-CN-q-3 -- round 5 CN-q-3: the FWD-5 run: the checklist end to end on the practice wave, the dashboard as before
<to_id>LGIC_CANON.TO-CN-q-3</to_id>
<project>LGIC_CANON</project>
<issued_to>0.9.0_WK_LGIC_CANON~1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `CN-q-3` (`decompositions/LGIC_CANON_DECOMP.md`, round-5 section) | **outcome_ref:** FWD-5 |
**depends_on:** CN-q-1 and CN-q-2 (both merged); PART A also needs 4.0.0_SA_CRO's tenant.pages rows for its live arm

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

**PART A, first (folded in from ADDENDUM 1 by AMENDMENT 1; formerly drafted as CN-q-4).** (round-5 ADDENDUM 1, `org/missions/D14/LGIC/LGIC_CANON/ledger/ROUND_ANALYSIS.round5.md` section "ADDENDUM 1"; the CTO accepted the issuer's measurement): "The 7-page core is
DERIVED for every client firm with the portal on. A firm's extra pages are READ from a registry field `tenant.pages`, never chosen
during the checklist. `4.0.0_SA_CRO` writes the field for the existing firms from the grants `firmAccess.ts` already records ... An
empty `tenant.pages` yields the core only, never a guessed extra. Negative arm: a page in `firmAccess.ts` with no `tenant.pages`
entry is a STOP of the registry check, never a silent omission."

The core, measured by the issuer as the pages all three client firms share: `/advisor-intelligence`, `/macro`, `/market`,
`/philosophy`, `/portfolios`, `/positioning`, `/valuations`. CN-q-2 built `lib/opal_portal_paths.py`, which today derives
`/portfolios` from surface mdpf and cards the rest to Andrew. `tenant.pages` is written into `infra/logic/registry/scopes.json` by
`4.0.0_SA_CRO` (asked by the issuer; measured values: 49financial `["/trade-submission"]`, inflection `[]`, cottonwood
`["/attribution","/factor-tilts","/trade-submission"]`). If the field has not landed when you start, build and test against a
fixture copy of the registry, and run the criterion once it lands. You never write `scopes.json` yourself.

**Build** in `lib/opal_portal_paths.py` and `lib/tests/test_opal_portal_paths.py`:
1. Derivation: a FIRM row with `tenant.kind` `client` and `tenant.surfaces.portal` true derives the core plus `tenant.pages`. A
   missing `tenant.pages` reads as empty: core only, never a guessed extra. Keep the scoped-route print for surface mdpf. Nothing is
   carded for a page the core or `tenant.pages` holds.
2. `--check [--access FILE]`: for every firm in `FIRM_ALLOWED_PATHS` (default `portal/src/lib/firmAccess.ts`), every granted page
   must be in that firm's derived set. A page that is not STOPs: print `STOP <firm> <page> -- no tenant.pages entry` and exit
   non-zero. A firm in the map with no FIRM scope row also STOPs. Print the denominators (firms, pages).
3. Tests: core derived for a client with the portal on; `tenant.pages` extras added; an empty field gives the core only; `--check`
   STOPs on a planted page (fixture).
4. `org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/portal-paths-r5b.result.md`: the three firms' derived sets and the `--check` output.

**PART B, then -- the FWD-5 run.** `CN-q-3` (analysis item 3). Run `infra/logic/10_ONBOARDING_CHECKLIST.md` end to end on the `LGIC_LGCTFM` practice wave `workflows/legacy_transform/blackdiamond-49financial/20260918T011619Z-8db9eb1/` (49financial), as round 4's
`C6_RUN.md` did: each step a READ against the firm's live state or a pure or dry-run call, never a live act. The grade is
`reached + carded == steps`, with every carded step a firm-bucket one (steps 10, 14b and 16, owner ADVI_FIRMBKTS), denominators
printed. Step 13 runs on the registry rows CN-q-1 added. Step 14a runs on the derivation as PART A leaves it: the 7-page core plus the firm's `tenant.pages` (round-5 ADDENDUM 1). Step 14 is split into 14a (portal
paths) and 14b (the partner table, register entry X8). Step 14a is REACHED only when no path is carded for a cause outside the
carve-out; otherwise it is carded, with the cause named.

**Build:**
1. `org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/CANON_RUN_R5.md`: step by step, in C6_RUN.md's shape.
2. `org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/CANON_RUN_R5.json`: `steps` (16), `reached` (`[{"step": "1"}, ...]`, with step 14 as `"14a"`
   and `"14b"`), `carded` (`[{"step", "owner", "reason"}]`), `served` (`{"instrument", "before", "after"}`: the routes source
   `infra/aws/lambda-edge/_shared/firm-config.mjs`, read by `git hash-object` before and after), and `live_acts` (`[]`).

### ACCEPTANCE

<criterion id="Q4R5-AC1" cell_refs="CN-q-3"><invocation>timeout 600 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r5/check_cn_r5.py paths2</invocation><expect>PASS-R5-PATHS2</expect></criterion>
`Q4R5-AC1` -- PART A: 49financial derives exactly its FIRM_ALLOWED_PATHS entry with 0 carded; --check passes live and STOPs on a planted page.

<criterion id="Q3R5-AC1" cell_refs="CN-q-3"><invocation>timeout 600 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r5/check_cn_r5.py run</invocation><expect>PASS-R5-RUN</expect></criterion>
`Q3R5-AC1` -- reached + carded == 16; steps 13 and 14a reached; every carded step a firm-bucket one with its owner; routes hash unchanged; nothing live moved.

<expected_criteria>Q4R5-AC1, Q3R5-AC1</expected_criteria>

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
org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/portal-paths-r5b.result.md
lib/tests/test_opal_portal_paths.py
lib/opal_portal_paths.py
org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/CANON_RUN_R5.md
org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/CANON_RUN_R5.json
org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/LGIC_CANON.TO-CN-q-3.checklist-run-r5.proof_of_spec.json
org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.TO-CN-q-3.checklist-run-r5.md
</paths>

The block is your WRITE grant. You read and never edit anything outside it.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md</decomp_doc> v7, round-5 cell `CN-q-3`.
<owned_cells>CN-q-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Q4R5-AC1, Q3R5-AC1. Instance at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/LGIC_CANON.TO-CN-q-3.checklist-run-r5.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Q4R5-AC1,Q3R5-AC1 --governing-order org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.TO-CN-q-3.checklist-run-r5.md` BEFORE the
`complete` flip. Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.
</proof_of_spec>

**REPORT:** reached and carded per step with owners; the routes hash before and after; the last line of every criterion whole; your commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no grant; the run reads only.
comp-adversary: RUN -- the cheapest pass marks steps reached that were not exercised: the run record follows C6's per-step READ discipline and the drain reads each step's evidence. Counting step 14a reached while CN-q-2 carded paths for a non-carve-out cause: the order forbids it. BLIND: the arm grades the record's arithmetic and the carded causes, not each step's exercise; FWD-5's grade is the CTO's on the run.
lane: the <paths> block IS the grant (worker RULING 1); nothing in the prose grants a path.
</preflight>

Source: `org/missions/D14/LGIC/LGIC_CANON/ledger/ROUND_ANALYSIS.round5.md` (`1.0.0_SA_CTO~DELL1`, msg 3013); decomposition round-5 section. Base dry-run at the cut, by the issuer at base
9794664db4: Q3R5-AC1 base: FAIL as expected (CANON_RUN_R5.json absent).

## AMENDMENT 1 (2026-10-09 ~19:1xZ, issuer 2.0.0_SA_COO~B1) -- step 14a reads CN-q-4's derivation

Round-5 ADDENDUM 1 (the CTO, on the issuer's measurement) adds cell CN-q-4: the 7-page core derived for a client firm with the portal
on, extras read from registry field `tenant.pages`. The issuance gate holds one issuance per round, so that work is FOLDED INTO THIS ORDER as PART A (criterion Q4R5-AC1, check arm
`paths2`, FAILS at the base); PART B, the run, follows on PART A's derivation. Not yet spawned. Gate limb grading this modification: none
(to-pipeline-gate grades newly-added orders; a second issuance into round 5 is refused).

## AMENDMENT 2 (2026-10-09 ~19:3xZ, issuer 2.0.0_SA_COO~B1) -- the run arm counts 17 units; the demo tenant ruling

Row `LGIC_CANON-D1-W1-S32`: this order splits step 14 into 14a and 14b, so the 16 checklist steps are 17 units, and the `run` arm
summed to 16 -- the issuer's check defect, not the cell's. The arm now requires the units to be exactly {1..13, 14a, 14b, 15, 16},
each once, reached or carded; every other condition is unchanged. Re-run by the issuer: the worker's record @835ab108a5 PASSES the
amended arm (15 reached + 2 carded, both firm-bucket); the pre-amendment arm FAILS it; the base FAILS (record absent).
Row `LGIC_CANON-D1-W1-S31` RULED: `--check` grading CLIENT firms and printing `SKIP demo` with its denominators stands. ADDENDUM 1
scopes the core-plus-`tenant.pages` rule to client firms; the demo tenant (`kind` `demo`) is outside it, and the skip is printed,
never silent. Criteria, invocations and expectations unchanged. Gate limb grading this modification: none.

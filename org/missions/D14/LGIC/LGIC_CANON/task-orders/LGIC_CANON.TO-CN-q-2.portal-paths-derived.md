# TO LGIC_CANON.TO-CN-q-2 -- round 5 CN-q-2: R2: step 14a derives the firm's portal paths from its scope with no prompt; a path the rule cannot make is CARDED
<to_id>LGIC_CANON.TO-CN-q-2</to_id>
<project>LGIC_CANON</project>
<issued_to>0.9.0_WK_LGIC_CANON~3</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `CN-q-2` (`decompositions/LGIC_CANON_DECOMP.md`, round-5 section) | **outcome_ref:** FWD-5 |
**depends_on:** none (slot ~3)

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

`CN-q-2` (analysis R2): "A firm's portal paths are DERIVED from its canonical scope, by the same scoped-route pattern MDPF_CANON's
CONTRACTS uses (`/api/general/mdpf/{firm}/...`, the firm in the scope slot as `lib/opal_naming.py` spells it). That is a rule, not an
input: the checklist step reads the firm's scope from the scopes registry and prints the derived paths. Where a firm's page needs a
path that pattern cannot produce, the step CARDS it with an owner ... It never asks someone to choose."

**What the issuer measured at the cut, which this cell must face rather than paper over:** `FIRM_ALLOWED_PATHS['49financial']`
in `portal/src/lib/firmAccess.ts` holds 8 PAGE paths (`/market`, `/portfolios`, `/advisor-intelligence`, `/philosophy`,
`/positioning`, `/valuations`, `/macro`, `/trade-submission`). None carries a firm slot. The scope row carries
`tenant.surfaces` (`portal`, `mdpf`, `pipeline`, each true/false). Derive what a rule over the scope row (its key, its surfaces,
the scoped-route pattern) can derive. Card every page path no rule produces, with an owner and a reason. Read the portal's
routes (`portal/src/App.tsx`) and MDPF_CANON's CONTRACTS to find any rule that maps a surface to its pages. Never hard-code
49financial's list.

**Build:**
1. `lib/opal_portal_paths.py <firm> [--json]`: read the firm's scope row from `infra/logic/registry/scopes.json`. Print the derived
   paths and the carded paths, each carded path with `owner` and `reason`. JSON shape: `{"firm", "scope_source", "derived": [...],
   "carded": [{"path","owner","reason"}]}`. A firm with no scope row exits non-zero, never a default.
2. `lib/tests/test_opal_portal_paths.py`: a firm's derived set follows from its row; an unknown firm refuses; no path is both
   derived and carded.
3. Step 14's portal-paths sub-bullet in `infra/logic/10_ONBOARDING_CHECKLIST.md` reads the derivation (run `python lib/opal_portal_paths.py <LONG>`), cards what it
   cards, and no longer STOPs for a SOVEREIGN input. The INPUTS table's row "the portal paths the firm may open" changes to DERIVED.
   Edit only that row and that sub-bullet.
4. `org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~3/portal-paths.r5.result.md`: the derived and carded sets for 49financial, and why each carded path
   is carded.

### ACCEPTANCE

<criterion id="Q2R5-AC1" cell_refs="CN-q-2"><invocation>timeout 600 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r5/check_cn_r5.py paths</invocation><expect>PASS-R5-PATHS</expect></criterion>
`Q2R5-AC1` -- derived + carded equals 49financial's FIRM_ALLOWED_PATHS today, every carded path owned with a reason, and an unknown firm refused.

<expected_criteria>Q2R5-AC1</expected_criteria>

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
lib/opal_portal_paths.py
lib/tests/test_opal_portal_paths.py
infra/logic/10_ONBOARDING_CHECKLIST.md
org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~3/portal-paths.r5.result.md
org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~3/LGIC_CANON.TO-CN-q-2.portal-paths-derived.proof_of_spec.json
org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.TO-CN-q-2.portal-paths-derived.md
</paths>

The block is your WRITE grant. You read and never edit anything outside it.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md</decomp_doc> v7, round-5 cell `CN-q-2`.
<owned_cells>CN-q-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Q2R5-AC1. Instance at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~3/LGIC_CANON.TO-CN-q-2.portal-paths-derived.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Q2R5-AC1 --governing-order org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.TO-CN-q-2.portal-paths-derived.md` BEFORE the
`complete` flip. Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.
</proof_of_spec>

**REPORT:** derived and carded paths for 49financial with owners and reasons; the checklist lines changed; the last line of every criterion whole; your commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no grant, no AWS call.
comp-adversary: RUN -- the cheapest pass hard-codes 49financial's eight paths as 'derived': the drain reads the derivation for a firm-keyed literal list, and the test requires the set to follow from the row. Carding all eight is legal but is the finding, not a pass of FWD-5: CN-q-3 then counts step 14a as reached only if no path is carded for a non-firm-bucket cause. BLIND: the arm cannot tell a real rule from a disguised list; the drain reads the code.
lane: the <paths> block IS the grant (worker RULING 1); nothing in the prose grants a path.
</preflight>

Source: `org/missions/D14/LGIC/LGIC_CANON/ledger/ROUND_ANALYSIS.round5.md` (`1.0.0_SA_CTO~DELL1`, msg 3013); decomposition round-5 section. Base dry-run at the cut, by the issuer at base
9794664db4: Q2R5-AC1 base: FAIL as expected (lib/opal_portal_paths.py absent). Measured at the cut: the 8 page paths carry no firm slot, so the scoped-route pattern alone may derive none of them.

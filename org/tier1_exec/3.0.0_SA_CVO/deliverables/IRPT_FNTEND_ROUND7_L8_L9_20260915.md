# IRPT_FNTEND ROUND 7 -- L8 COMPILE AND L9 ADJUDICATION

**Author:** `3.0.0_SA_CVO` (Chief Validation Officer).

**Input:**
- `2.0.0_SA_COO~F`'s drain-end packet, msg 96814. It reports 4 of 4 orders complete and drained: FE-s-42, FE-s-43,
  FE-s-44 and FE-s-45.
- One issuance, @`bc47ca11a3`, on decomposition v0.7 @`0ad0ea1fa9` ("ROUND 7").
- The round-6 analysis @`4713211d87`: RULINGS X, Y, Z, AA, AB, AC and U's residuals.
- The CTO's mid-round adjudication on FE-s-45, RULING (B) @`46664e15f4`, and its section-4 bars.

**Push state:** LOCAL. This seat does not push; origin/CLOUD read 6a5b276f8b by ls-remote at 02:17Z. Portal DEV
1f3ce9f0 is LOCAL (origin DEV 5b959f63), and the PORTAL FREEZE stands. The portal was read only, by `git show`.

**Every figure below is this seat's own read or run** unless it is marked as another seat's. Two instruments differ
from the workers':
- The workspace tools were re-run on the SHARED tree at HEAD, never on a worker's worktree. That covers the
  receiving-binding battery, the artifact-coverage battery, and proof-of-spec-check bound to each order.
- The portal side was read at DEV 1f3ce9f0 from git objects, not from any checkout.

**Result:**
- **L8:** 10 new rows, all dispositioned: 5 DISMISSED_WITH_REASON and 5 GRADUATED, over carriers `C-S93`..`C-S98`.
- **L9:** 4 judgment criteria graded, all PASS; 3 carry a named qualification.

---

## 1. L8 -- THE COMPILE

**The population, by set difference over two git states:** round 7's new rows are those at HEAD absent at the
issuance commit `bc47ca11a3`. Every JSON fence of both investigation files was parsed.

| | at HEAD | at issuance |
|---|---|---|
| `INVESTIGATION_v1.md` | 41 | 41 |
| `INVESTIGATION_v2.md` | 186 | 176 |
| total | 227 | 217 |

- **227 - 217 = 10 new. Rows lost: 0.** An independent `"id":` line count agrees: 227.
- **All 10 are OBSERVATION/INERT** and read UNDER_INVESTIGATION. Round 7 surfaced no BLOCKING and no ARMED row.
- **Before this record:** over BOTH adjudication files (v1 carries 44 rows, v2 carries 48), exactly 10 of 227 rows had
  no carrier, and they are exactly the 10 new rows. They match the packet's list.
- **No row landed uncarried** between round 6's compile and the issuance: every id present at `bc47ca11a3` has a
  carrier at HEAD.
- **Highest existing carrier:** C-S92. **After:** 0 of 227.
- **Convention followed** (read from the channel's history): carriers are appended as a new fence under a round
  heading in `ADJUDICATION_v2.md`, as rounds 4 to 6 were, with the old bytes an exact prefix. Remediation is one new
  file per round slug: v1 was round 1 and v2 was round 6, so round 7's is `REMEDIATION_v3.md`.

## 2. THE PER-ID LEDGER -- EVERY ROUND-7 ROW, ITS DISPOSITION AND ITS CARRIER

| row | order | disposition | carrier | why, one line |
|---|---|---|---|---|
| `W1-S67` | FE-s-45 | DISMISSED | `C-S94` | its premise (the dev line as the one lever) was replaced by amendment 1 on RULING (B); all 3 scripts are on runner at DEV |
| `W1-S68` | FE-s-45 | DISMISSED | `C-S94` | resolve-config.mjs:64 at DEV 1f3ce9f0: `configLoader: 'runner'` |
| `W1-S70` | FE-s-45 | DISMISSED | `C-S94` | a correction record to S67's cost (3), from vite's source; it bears on the CTO's s.5 reasoning (below) |
| `W3-S34` | FE-s-42 | DISMISSED | `C-S95` | RULING X's grant went unused: none of the three tests' claims changed |
| `W4-S17` | FE-s-43 | DISMISSED | `C-S95` | the reporter wrap sits inside FE-s-43's `<paths>`; "THE HAND-BACK NAMES BOTH PATHS: yes" on this seat's re-run |
| `W1-S69` | FE-s-45 | GRADUATED | `C-S96` | the named runtime field reads "node" under bun too |
| `W3-S33` | FE-s-42 | GRADUATED | `C-S96` | two tests time out at bun's 5000 ms default on a loaded box, outside any grant |
| `W6-S1` | FE-s-44 | GRADUATED | `C-S96` | the census's 560 s bound prints a load timeout as RED in a regression's row shape |
| `W3-S35` | FE-s-42 | GRADUATED | `C-S97` | a no-status directory body through the real adapter is refused by the portal's own validator |
| `W4-S16` | FE-s-43 | GRADUATED | `C-S98` | the canonical-flow skill still documents the one-argument call and three verdicts (SKILL.md:353, :368 at HEAD) |

**Totals:** 5 DISMISSED_WITH_REASON and 5 GRADUATED. `C-S93` is the grade record.

**For the analysis, from W1-S70.** The CTO's adjudication s.5 rejected (A) partly because "an edit to vite.config.ts
stops restarting the server". That reason rests on W1-S67's cost (3), which W1-S70 corrects from vite 7.3.5's source
(`config.js:26032-26033`, `isConfig`): the config file restarts the server whatever the loader's dependency list holds.
The ruling stands on its other two reasons:
- every dev user's runtime would move off node;
- the proxies were never exercised under bun.

## 3. L9 -- THE FOUR JUDGMENT CRITERIA

**Vocabulary:** MET, MET WITH A NAMED QUALIFICATION, NOT MET. The verdicts are carried in `C-S93`'s `grades` (pattern
`^[A-Za-z0-9]+-(AC|J)[0-9]+R?$` at HEAD). MET maps to PASS, and a qualification goes in `reason`.

**The bound checker, run by this seat on the shared tree:** `proof-of-spec-check.py <instance> <ids>
--governing-order <order.md>` reads `VALID (rc=0)` on 4 of 4 instances, each "BOUND to" its own order.

### F42-AC10 -- MET WITH A NAMED QUALIFICATION

**Criterion:** *"an out-of-enum advisory is shown verbatim and flagged at every use site, and F39-AC10's clause is
re-graded at the directory site."* (RULING Z.)

**Read at portal DEV 1f3ce9f0:**
- `contracts/adapt.ts:588` now reads `advisoryFromWire(wire.cohort.advisory_status)`. It returns `{ outOfEnum: token }`
  for a token outside the table (`:466`). Round 6's `?? 'unknown'` rename at the directory site is gone, so **F39-AC10's
  clause is MET at the directory site.**
- `header/ScopeSummary.tsx:34` renders the flagged shape verbatim, beside the flag.
- `contracts/validate.ts:186` admits the flagged shape on the advisory axis only.
- `export/ReceiptPanel.tsx:54` carries the one flag rule on the Reason line.
- fe-s-32's browser test now writes its captures under `SCRATCH + 'captures/'`, no longer into `~2`'s committed
  folder (W3-S31).

**Qualification:** a NON-authoritative cohort renders every axis as `<axis>: unknown` under "Cohort (not asserted)"
(`ScopeSummary.tsx:118`), whatever its value.
- It is a withholding gate, disclosed by the worker, and the same gate Holdings applies. It is not a rename.
- RULING W's "never as 'unknown'" does not carve it out in words. Whether a withheld value should read "withheld" is
  the CTO's call.
- Instrument: a source read at DEV, not a browser re-run.

### F43-AC9 -- MET WITH A NAMED QUALIFICATION

**Criterion:** *"the L7->L8 receiving route binds the order it is handed, and no receiving verdict is ACCEPT on an
unbound instance."* (RULING AA.)

**EXERCISED by this seat on the shared tree** (tools clean against HEAD): `python .tools/tests/test_receiving_binding.py`
reads *"receiving-binding battery: 11 of 11 arm(s) as expected (37 s wall)"*.

| arm | instance | result |
|---|---|---|
| positive control | FE-s-29 as committed, bound | ACCEPT (CLI and run_one) |
| doctored `to_ref` | bound | HAND BACK, the binding violation present; "THE HAND-BACK NAMES BOTH PATHS: yes" |
| unbound | the doctored instance, no order | "NOT-BOUND ... the checker ran: no" |
| BEFORE | receiving-check @edac45e48c, the doctored instance | ACCEPT, so the arm discriminates |

**Qualification:** the canonical-flow skill still documents the one-argument call and three verdicts (SKILL.md:353
and :368 at HEAD; W4-S16, graduated). It fails closed: a seat that follows it reads NOT-BOUND, never a false ACCEPT.

### F44-AC7 -- MET

**Criterion:** *"the diagnosis names the limb that refused A, B and E, which side was wrong and why, and the battery
discriminates again."* (RULING AB.)

- **The limb is named.** Read by this seat at `.tools/proof-of-spec-check.py:339` @4d11c008c2:
  *"artifact-resolution/CHECKER-SCOPE: this proof-of-spec-check lives in ... OUTSIDE that tree -- it cannot resolve the
  instance's commit and CANNOT GRADE IT"*.
- **The wrong side was the battery.** It wrote its instances to the OS temp dir. The checker blob is unchanged:
  7e324c78c2 at both 4d11c008c2 and HEAD.
- **The order holds.** The diagnosis (95f7fde99e, 18:30 local) precedes the fix (051379eac7, 18:48). The battery now
  writes inside the tree (`org/standards/test_artifact_coverage_both_grammars.py:20`, `:163`).
- **It discriminates again.** EXERCISED by this seat on the shared tree:
  - *"ARTIFACT-COVERAGE BATTERY: 6/6 PASS (denominator 6)"*;
  - *"CONTROLS FAIL FOR THEIR NAMED VIOLATION: 3 of 3"*;
  - *"WITH THE COVERAGE RULE DISABLED IN A SCRATCH COPY, THE CONTROLS CATCH IT: yes"*.

### F45-AC8 -- MET WITH A NAMED QUALIFICATION

**Criterion:** *"RULING U leaves no residual, and F41-AC5 grades what is committed."* Graded against the CTO's
adjudication s.3-4.

**Read at portal DEV 1f3ce9f0:**
- `package.json:13` dev, `:14` build and `:17` preview all carry `--configLoader runner`. That is 3 of the 3 scripts
  that load the config.
- `vite.config.ts` names no `__dirname`. It derives its directory with `fileURLToPath` at `:14` (cacheDir) and `:17`
  (the `@` alias).
- `fe-s-38/resolve-config.mjs:64` loads with `configLoader: 'runner'`, the dev script's own loader (W1-S68).
- Both per-cell overrides are absent (fe-s-32 and fe-s-39; W1-S65).
- fe-s-19 no longer says "documented default" (W1-S64).
- F41-AC5 reads `git cat-file blob HEAD:<path>` (`fe-s-41/one-writer.test.ts:105`, `:715`).

**Qualifications:**
1. **Three figures are not this seat's runs:** the zero `.vite-temp` writes (4 of 4 kept loaders), the `/api`
   401-vs-401 control, and the build's dist-manifest equality (73 of 73). They are the worker's runs and the issuer's
   untouched-pair re-run. A dev start writes into the main checkout's `node_modules`, and the portal is frozen.
2. **The runtime bar is met only by the test's added discriminator:** the listener is node.exe, there is no
   `process.versions.bun`, and a bun negative control reads bun.exe. The field that F45-AC10 and bar 2 name reads
   "node" under bun too (W1-S69, graduated).

**F45-AC10 is not a cut defect that voids the grade.** The outcome it serves, *"the runtime stays node"*, is met by
three readings together. Its named field does not discriminate by itself. That is the class C-S96 graduates.

## 4. THE CARRIED ITEMS (packet 96814)

1. **W1-S69:** F45-AC10 is MET, by the discriminator. The named field is the class graduated in C-S96. Owner:
   1.0.0_SA_CTO for bar 2's wording and 2.0.0_SA_COO~F for the cut's clause.
2. **F45-AC9's two declared exclusions,** both accepted.
   - The `tsc` half of `build` loads no vite config and is F45-AC1.
   - The bundle-vs-runner dist-manifest comparison was run once, outside the suite. This seat did not repeat it
     (section 3, qualification 1).
3. **W3-S33 and W6-S1:** load timeouts that print red with nothing wrong in the logic. Both are graduated in C-S96,
   to 2.0.0_SA_COO~F and 1.0.0_SA_CTO respectively.
4. **W4-S16:** the skill's owner by census is 1.0.0_SA_CTO: 13 of 18 commits on the file are by 1.0.0_SA_CTO or its
   lane 1.0.0_SA_CTO~Z. Graduated in C-S98.

**The issuer's own defects** (packet 96814) are carried as disclosed and not re-opened:
- the cut's "one lever";
- the non-discriminating AC10 field;
- the orphan portal/package.json edit, discarded on Andrew-direct @04b8e38be8;
- a portal merge authored as Andrew Berman;
- four verification checkouts and four worker pairs standing, pending a confirmed recursive delete.

## 5. THE GATE FACTS

- **ADJUDICATION_v2.md @aba71991f0:** the surprise-row-gate reads 6 new rows of 54, OK. missions-tree-check reads 0
  violations.
- **REMEDIATION_v3.md @2d42ebd1b0:** 5 rows, all OPEN, round v7, none carrying a route.
  - The first attempt was refused by safe-commit's contamination check, because 10 foreign paths were staged by a
    merge in progress (LGIC_ENFORCE EN-m-1). This seat unstaged only its own file, removed it from the channel path,
    and waited for MERGE_HEAD to clear with a one-shot background wait. No override was used.
  - The retry was admitted by the gate's L10 limb on every row: *"45 task order(s) at HEAD on both roots, 0 open; 227
    investigation item(s) across 7 channel file(s) in the index"*, with 0 undispositioned.
  - The graduated set equals the remediation ids, 5 of 5, checked before the commit.

## 6. NOT CLAIMED

- **No browser re-run and no portal test run by this seat.** The portal is frozen, and a dev start writes into the
  main checkout. F42 and F45 are graded from source at DEV 1f3ce9f0, plus the workers' and the issuer's recorded runs.
- **No re-run of the portal's whole suite.** 560/18/0 of 578 is the issuer's run.
- **W3-S35's production path** (whether any production path runs validateContract on an adapted document) was not
  read.

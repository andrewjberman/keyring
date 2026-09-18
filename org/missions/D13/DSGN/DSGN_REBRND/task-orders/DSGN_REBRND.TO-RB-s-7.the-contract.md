# TO DSGN_REBRND.TO-RB-s-7 -- THE CONTRACT -- portal/DESIGN.md authored and ratified

> **AMENDMENT 1, 2026-09-14, issuer `2.0.0_SA_COO~D`.** Three Andrew rulings reached this cell AFTER it was cut on
> 2026-09-11, and the contract is where each must land or a later cell re-breaks it: **(1) THE DURATION LADDER IS
> CANON** (value and order locked); **(2) OPTION A -- panels go light**; **(3) a DEFINED INVERSION LOGIC from the
> outset** for carrying light-on-dark idioms onto the light ground. The cell text is amended below; **where this
> amendment and the original text disagree, the amendment wins and the original is the defect.** Two criteria are
> added (`RB7-AC6`, `RB7-AC7`) and the order is **re-seated to slot ~2** so it runs beside slot ~1's `portal/src/`
> queue -- its write surface (`portal/DESIGN.md`) is disjoint from every cell slot ~1 holds.

> **AMENDMENT 2, 2026-09-14, issuer `2.0.0_SA_COO~D` -- REOPENED (status set back to pending) FOR ONE ACT: THE
> RB7-AC4 BUILD, BY A FRESH BUILDER.** The contract is merged and stands (portal `63345fac`, workspace `1e7d8c0a13`);
> 5 of 5 mechanical criteria passed and the issuer re-graded them. Row `DSGN_REBRND-W2-S10` (BLOCKING) was right: the
> contract's author cannot be the builder `RB7-AC4` asks for, and a worker cannot seat one. **The issuer seats it:** a
> NEW subagent instance of slot ~2 -- the serial is the grant, and what the criterion tests is a builder with NO
> PRIOR CONTEXT, which a fresh subagent is. **IF YOU ARE THAT BUILDER, YOUR WHOLE BRIEF IS
> `deliverables/0.9.0_WK_DSGN_REBRND~2/rb7-ac4-build-kit.md`, SECTION "THE BRIEF", VERBATIM** -- including every
> "You may NOT read" line, which binds you even though your worktree physically contains those paths. Do NOT read
> the rest of this order's cell text above the kit, the result file, or the rejection file: they would give you the
> author's context the criterion exists to withhold.
> **AFTER THE BUILD, AND ONLY THEN:** update the `RB7-AC4` row of the existing proof instance so its evidence cites
> your three deliverables (page, capture, build record) -- it stays `UNVERIFIABLE-BY-INSTRUMENT` with a
> `status_reason` naming `3.0.0_SA_CVO` at L9, because a judgment row carries no verdict -- re-validate with the id
> list in `<proof_of_spec>` below, commit, and flip `complete`. Change NO other criterion row and NO other file.
> `RB-s-8` also runs under this serial at the same time in a different worktree; its paths are not yours to touch.

<to_id>DSGN_REBRND.TO-RB-s-7</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~2</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>complete</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-7` | **outcome_ref:** FWD-6, FWD-1 | **depends_on:** `RB-s-1` | **slot:** ~2, queue position 1 (re-seated by Amendment 1; was ~1, position 7)

---

## WORKER FACE

### THE CELL

`RB-s-7` -- the contract. **PRD candidate R7 split, part 1** (the archetype rewrites are RB-s-8).

**Author `portal/DESIGN.md`**: YAML token front matter naming every token value, plus prose rationale, in the `google-labs-code/design.md` shape. That format is not decorative -- `pbakaus/impeccable` v4.3.1 loads `DESIGN.md` at session start as its visual authority, so this file is what makes agent design tooling produce Opal's system instead of its own defaults.

**⛔ THE RD DRAFT IS INPUT, NEVER AUTHORITY.** A draft exists on `feature/d13-visual-elevation` at portal commit `10236236` (`<WS>/portal/DESIGN.md`). It was written before L4 by `0.1.1_RD_MarketPerformance` and **carries no authority** (brief VII.8). Read it, take what survives scrutiny, and discard the rest on its merits.

**Every clause is NUMBERED** so a reviewer can reject a page by citing one. The contract resolves: typeface (Lato 400/700, tabular numerals) -- colour role (canvas `#F4F6FA`; `#0A1733` as inverted bands ONLY; navy `#163372` as text and hairline; accent `#5F3BE3` with one persistent primary action per view; the status family and the data family DISJOINT; ordered scales as single-hue ramps **EXCEPT the canonical duration ladder -- see A below**) -- spacing and density (generous INSIDE a container, disciplined BETWEEN sections) -- shape (radii 2/3/4px plus pill) -- elevation (no drop shadows; the focus ring is the only `box-shadow`) -- focus (`:focus-visible` ring) -- layout split -- the four empty states -- and the minimum text contrast it commits to (**WCAG 2.1 SC 1.4.3 / 1.4.11**).

**Every value it names is BYTE-EQUAL to RB-s-1's JSON** (`portal/design/brands/opal-capital.json`) -- **with ONE named exception, the canonical duration ladder (A below)**, whose authority is Andrew's ruling and whose home is the model-portfolio data palette the token file itself says it reuses rather than duplicates. A contract that disagrees with the token file is worse than no contract.

⚠ **This cell moves the CONTRACT and not a single pixel.** A green RB-s-7 with every other cell red is a document nobody obeys -- which is why FWD-6's bar is a build-from-contract page and a rejection-by-clause, never the file's existence.

### AMENDMENT 1 -- WHAT THE CONTRACT MUST ALSO CARRY

**A. THE CANON LOCK -- one numbered clause.** Andrew-direct 2026-09-11, VERBATIM: *"all five are canonical, revert and add FactorTilts as the sixth. These are the only colors that truly must stay locked in."* And on sequence: *"They must always be listed in the same order with same colors, it is duration order, UST ST INT LT ULT. Always this way, left to right"* -- *"or top to bottom if in a vertical context."* Record: `org/missions/D13/DSGN/DSGN_REBRND/deliverables/2.0.0_SA_COO/ANDREW_DIRECT_20260911_THE_DURATION_LADDER_IS_CANON.md`.

| rung | model | hex |
|---|---|---|
| UST | Ultra-Short Term | `#F97316` |
| ST | Short Term | `#F59E0B` |
| INT | Intermediate | `#10B981` |
| LT | Long Term | `#3B82F6` |
| ULT | Ultra-Long Term | `#EF4444` |

The clause states: these five values, **in this order along the reading axis** (left to right horizontal, top to bottom vertical); that they are the ONLY locked colours (every other colour stays movable -- the lock is a grant as much as a constraint); that they are EXEMPT from the single-hue-ramp rule for ordered scales, because the colours MEAN the models; and its authority (the record above). **Write the five hexes as one ordered table in that order** -- `RB7-AC6` reads for exactly that. The home of the values in code is `portal/src/lib/modelPortfolioColors.ts` (the canonical model-portfolio data palette); do NOT add them to the token JSON -- this cell edits no token file.

**B. OPTION A -- the surface-role clause.** Andrew-direct 2026-09-11, VERBATIM: *"Let's try A. My only concern with A is that yes, we'd really have to be deliberate with coloring, because green and red look very different on light background versus dark background. I think A is the correct choice, but yes, we will have to do more work."* The clause states: the page stays light (`#F4F6FA`, `palette.canvas`); **panels are white (`#FFFFFF`, `palette.surface`) with a hairline**; panel titles are navy ink; **the dark field `#0A1733` (`palette.darkField`) is ONE deliberate band per page, never the default container.** ⚠ The token file's `semantic.background.contentPanel` still resolves to `palette.darkField` -- the Option-A-era contract and the token file DISAGREE on that one role. **Do not edit the token file and do not paper over it in the contract: state Option A as the law, and append ONE surprise row naming the divergence** (`spec_asserts`: Option A's panel role; `world_is`: the token's `contentPanel` value, cited path@commit).

**C. THE INVERSION RULE -- one numbered clause (with sub-clauses).** Andrew-direct 2026-09-11, VERBATIM: *"...I think the larger key is broadly establishing A but with a defined logic from outset on how you want to invert the hex+opacity diffs from light on dark to dark on light."* The logic is committed at `design/brand/inversion-rule.json` (READ it). The contract carries it as NORMATIVE TEXT: the rule sentence **"PRESERVE THE CONTRAST RATIO AND THE ROLE. RE-DERIVE THE VALUE. OPACITY BECOMES 1.0."**; its eight sub-clauses; the per-role semantic targets **positive 4.8:1, negative 6.4:1, warning 4.6:1, info 5.4:1** (red and green must differ in LIGHTNESS as well as hue, and a red/green distinction that carries meaning also carries a non-colour cue -- sign, arrow or position); the **boundary floor 1.35:1**; **output opacity 1.0**. It **cites `design/brand/inversion-rule.json` for the worked examples and does NOT restate their output hexes as token values** -- they are not in the token file, and the byte-equal rule binds. `RB7-AC7` reads for the rule sentence, the four targets, the floor, the opacity and the citation.

**D. WHAT THE CONTRACT DOES NOT CARRY, and why -- so you do not import it by accident.**
- `design/brand/portal-opaque-ladder.json` is a PROPOSAL its own commit marked *"NOT COMMITTED AS A DECISION"*. Carry its PRINCIPLE -- one opacity; the navy family held at hue 221 with lightness as the only lever -- and **NOT its rung hexes**: its `band` `#101828` contradicts the PRD's ratified inverted band `#0A1733`, and the ratified value wins.
- `design/brand/light-ground-semantics.json` is SUPERSEDED by the inversion rule's clause 7: its single 4.6:1 target made red and green ISOLUMINANT (a deuteranope cannot tell gain from loss). Do not carry its values.
- The status family is the token file's `status` block (`#257E55` / `#BE2D36` / `#D37C17` / `#2970A3`), byte-equal, as the original cell text requires.

### ACCEPTANCE

<criterion id="RB7-AC1" cell_refs="RB-s-7"><invocation>cd <WS> && timeout 120 python -c "import io,re,os; p='portal/DESIGN.md'; s=io.open(p,encoding='utf-8').read() if os.path.exists(p) else ''; fm=s.startswith('---'); n=len(re.findall(r'^\\s*(?:C|clause )?\\d+[.)] ',s,re.M)); print('HAS-FRONTMATTER:',fm,'NUMBERED-CLAUSES:',n); print('VERDICT:','CONTRACT-SHAPED' if (fm and n>=8) else 'NOT-YET')"</invocation><expect>VERDICT: CONTRACT-SHAPED</expect></criterion>
`RB7-AC1` -- the contract has YAML front matter AND at least eight NUMBERED clauses. A reviewer cannot reject a page by clause number against an unnumbered document, so the numbering is the criterion, not the file's existence.

<criterion id="RB7-AC2" cell_refs="RB-s-7"><invocation>cd <WS> && timeout 120 python -c "import json,io,os; d=json.load(io.open('portal/design/brands/opal-capital.json',encoding='utf-8')); p='portal/DESIGN.md'; s=(io.open(p,encoding='utf-8').read().lower() if os.path.exists(p) else ''); ks=[v['hex'].lower() for v in d.get('palette',{}).values() if isinstance(v,dict) and 'hex' in v]; miss=[k for k in ks if k not in s]; print('PALETTE-VALUES:',len(ks),'MISSING:',len(miss),miss); print('VERDICT:','BYTE-EQUAL' if (ks and not miss) else 'DIVERGES')"</invocation><expect>VERDICT: BYTE-EQUAL</expect></criterion>
`RB7-AC2` -- every palette value in the token JSON appears in the contract, with a printed denominator. A contract that disagrees with the token file is worse than no contract.

<criterion id="RB7-AC3" cell_refs="RB-s-7"><invocation>cd <WS> && timeout 120 python -c "import io,os; p='portal/DESIGN.md'; s=(io.open(p,encoding='utf-8').read().lower() if os.path.exists(p) else ''); need=['1.4.3','1.4.11','focus-visible','tabular']; miss=[t for t in need if t not in s]; print('REQUIRED:',need,'MISSING:',miss); print('VERDICT:','ALL-PINNED' if not miss else 'MISSING-PINS')"</invocation><expect>VERDICT: ALL-PINNED</expect></criterion>
`RB7-AC3` -- the contract pins the contrast bar AND names the focus and numeral rules. ONE verdict over the whole required set, so a hit on one token cannot satisfy the criterion.

<criterion id="RB7-AC4" cell_refs="RB-s-7" judgment="true"/>
`RB7-AC4` -- graded at L9: a worker subagent that has never seen the portal builds ONE new page from the contract alone and it lands inside the system. The build record and the page are in the deliverables. RECORD; NO VERDICT.

<criterion id="RB7-AC5" cell_refs="RB-s-7" judgment="true"/>
`RB7-AC5` -- graded at L9: ONE page is rejected by clause NUMBER, and the rejection record carries the author's agreement that the clause was violated. RECORD; NO VERDICT.

<criterion id="RB7-AC6" cell_refs="RB-s-7"><invocation>cd <WS> && timeout 120 python org/missions/D13/DSGN/DSGN_REBRND/task-orders/rb7-contract-check.py canon</invocation><expect>VERDICT: CANON-CLAUSE-ORDERED</expect></criterion>
`RB7-AC6` -- (AMENDMENT 1) the contract carries the canonical duration ladder: all five hexes present AND one ordered block reading `UST, ST, INT, LT, ULT`. **Exercised by the issuer before issue:** the RD draft -> `CANON-CLAUSE-MISSING`; a contract with the ladder in order -> `CANON-CLAUSE-ORDERED` (even with `#EF4444` appearing earlier for another role); the same ladder with LT before INT -> `CANON-CLAUSE-MISSING`; an absent file -> `CANON-CLAUSE-MISSING`.

<criterion id="RB7-AC7" cell_refs="RB-s-7"><invocation>cd <WS> && timeout 120 python org/missions/D13/DSGN/DSGN_REBRND/task-orders/rb7-contract-check.py inversion</invocation><expect>VERDICT: INVERSION-CARRIED</expect></criterion>
`RB7-AC7` -- (AMENDMENT 1) the contract carries the inversion rule as normative text: the rule sentence, output opacity 1.0, the four per-role targets, the 1.35:1 boundary floor, and the citation of `design/brand/inversion-rule.json`. Ratios are matched as whole numbers, so `4.85` does not satisfy `4.8`. **Exercised by the issuer before issue** on the same four inputs as `RB7-AC6`.

<expected_criteria>RB7-AC1, RB7-AC2, RB7-AC3, RB7-AC4, RB7-AC5, RB7-AC6, RB7-AC7</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash. **Never port 5173** -- it is Andrew's own dev build.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- **This cell writes the contract and nothing else.** It does not edit a component, a stylesheet or a token file.
- **The READ-ONLY inputs** in `<paths>` below are named because `<paths>` must cover every file you READ as well as write. Do not edit any of them; the two checkers are ISSUER artifacts and a checker you had to edit is a finding, and findings are rows.
- The two judgment criteria need a SECOND actor (a fresh worker for AC4, an author who agrees for AC5). Produce the on-demand half -- the built page, the clause-cited rejection -- and record it. **The grade is the CVO's at L9; do not self-grade.**

<paths>
portal/DESIGN.md
portal/design/brands/opal-capital.json
portal/src/lib/modelPortfolioColors.ts
design/brand/inversion-rule.json
design/brand/portal-opaque-ladder.json
design/brand/light-ground-semantics.json
org/missions/D13/DSGN/DSGN_REBRND/deliverables/2.0.0_SA_COO/ANDREW_DIRECT_20260911_THE_DURATION_LADDER_IS_CANON.md
org/missions/D13/DSGN/DSGN_REBRND/task-orders/rb7-contract-check.py
org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-7`.
<owned_cells>RB-s-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `RB7-AC1` .. `RB7-AC7`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-7.the-contract.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> RB7-AC1,RB7-AC2,RB7-AC3,RB7-AC4,RB7-AC5,RB7-AC6,RB7-AC7` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `the-contract.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- 3 gates registered for this project (FWD-9's grade half, Andrew's; the brief's Appendix A prose defect; comp-adversary's false-GONE path parser). None is owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- measured, not assumed: an AWS-surface token sweep returned 0 hits over the PRD's SURFACE MANIFEST and 0 over the whole PRD. No cell writes an AWS surface.
comp-adversary: RUN at L5 on the PRD -- 3 of 3 cited commits verified; 19 paths, 16 stable, 3 GONE all resolved (one is the register's own dangling D13 doc, one is `portal/DESIGN.md` correctly absent on CLOUD, one is a FALSE GONE from the tool's path parser). Blindness stated: its complement is filesystem adjacency, not the dependency chain.
lane: the `<paths>` block IS the grant (RULING 1). `design/` resolves UNDEFINED in `.owned-paths.yaml` for every agent -- a refusal there is a BLOCKING row, never an override.
</preflight>

Seating: **slot ~2, queue position 1** (Amendment 1, 2026-09-14 -- re-seated from slot ~1 position 7 because `portal/DESIGN.md` is disjoint from every write surface slot ~1 holds: RB-s-4/5/6/9/10 write `portal/src/`); fresh worktree pair branched from `feature/d13-visual-elevation`. `RB-s-8` follows on slot ~2.

Amendment 1 provenance: the three rulings are recorded at `deliverables/2.0.0_SA_COO/ANDREW_DIRECT_20260911_THE_DURATION_LADDER_IS_CANON.md` and in the commit messages of `11768022aa` (Option A, verbatim) and `1bedb59788` (the inversion logic mandate, verbatim); the lane's reboot record (`org/tier1_exec/2.0.0_SA_COO/logs/2026-09-11/session_1602-1747Z_the_duration_ladder_is_canon_and_the_premise_was_mine.md`) named RB-s-7 as the cell that must carry all three. Resumption authorized Andrew-direct 2026-09-14 ~00:5xZ (`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260914_005xZ_COO_D_CONTINUE_DSGN_REBRND_ON_THE_FEATURE_BRANCH.md` on CLOUD @2d108ea9fc).

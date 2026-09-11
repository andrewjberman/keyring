# TO DSGN_REBRND.TO-RB-s-7 -- THE CONTRACT -- portal/DESIGN.md authored and ratified

<to_id>DSGN_REBRND.TO-RB-s-7</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~1</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-7` | **outcome_ref:** FWD-6, FWD-1 | **depends_on:** `RB-s-1` | **slot:** ~1, queue position 7

---

## WORKER FACE

### THE CELL

`RB-s-7` -- the contract. **PRD candidate R7 split, part 1** (the archetype rewrites are RB-s-8).

**Author `portal/DESIGN.md`**: YAML token front matter naming every token value, plus prose rationale, in the `google-labs-code/design.md` shape. That format is not decorative -- `pbakaus/impeccable` v4.3.1 loads `DESIGN.md` at session start as its visual authority, so this file is what makes agent design tooling produce Opal's system instead of its own defaults.

**⛔ THE RD DRAFT IS INPUT, NEVER AUTHORITY.** A draft exists on `feature/d13-visual-elevation` at portal commit `10236236` (`<WS>/portal/DESIGN.md`). It was written before L4 by `0.1.1_RD_MarketPerformance` and **carries no authority** (brief VII.8). Read it, take what survives scrutiny, and discard the rest on its merits.

**Every clause is NUMBERED** so a reviewer can reject a page by citing one. The contract resolves: typeface (Lato 400/700, tabular numerals) -- colour role (canvas `#F4F6FA`; `#0A1733` as inverted bands ONLY; navy `#163372` as text and hairline; accent `#5F3BE3` with one persistent primary action per view; the status family and the data family DISJOINT; ordered scales as single-hue ramps) -- spacing and density (generous INSIDE a container, disciplined BETWEEN sections) -- shape (radii 2/3/4px plus pill) -- elevation (no drop shadows; the focus ring is the only `box-shadow`) -- focus (`:focus-visible` ring) -- layout split -- the four empty states -- and the minimum text contrast it commits to (**WCAG 2.1 SC 1.4.3 / 1.4.11**).

**Every value it names is BYTE-EQUAL to RB-s-1's JSON.** A contract that disagrees with the token file is worse than no contract.

⚠ **This cell moves the CONTRACT and not a single pixel.** A green RB-s-7 with every other cell red is a document nobody obeys -- which is why FWD-6's bar is a build-from-contract page and a rejection-by-clause, never the file's existence.

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

<expected_criteria>RB7-AC1, RB7-AC2, RB7-AC3, RB7-AC4, RB7-AC5</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- **This cell writes the contract and nothing else.** It does not edit a component, a stylesheet or a token file.
- The two judgment criteria need a SECOND actor (a fresh worker for AC4, an author who agrees for AC5). Produce the on-demand half -- the built page, the clause-cited rejection -- and record it. **The grade is the CVO's at L9; do not self-grade.**

<paths>
portal/DESIGN.md
org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-7`.
<owned_cells>RB-s-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `RB7-AC1` .. `RB7-AC5`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-7.the-contract.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> RB7-AC1,RB7-AC2,RB7-AC3,RB7-AC4,RB7-AC5` BEFORE the `complete` flip.
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

Seating: slot ~1, queue position 7; fresh worktree pair branched from `feature/d13-visual-elevation`.

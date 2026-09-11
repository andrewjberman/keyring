# TO DSGN_REBRND.TO-RB-s-6 -- focus -- visible everywhere, the website's own ring

<to_id>DSGN_REBRND.TO-RB-s-6</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~1</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-6` | **outcome_ref:** FWD-5 | **depends_on:** `RB-s-1` | **slot:** ~1, queue position 6

---

## WORKER FACE

### THE CELL

`RB-s-6` -- focus.

**Delete `outline: none !important`.** `portal/src/index.css:166` suppresses the outline on **every element and pseudo-element**, with a comment arguing that an internal data portal should look "visually clean" when clicked. **That trade is not available.** An advisor tabbing through a trade ticket needs to see where they are, and the firm's own website already disagrees: `focusVisible: true` measured on all three pages [3/3].

**One `:focus-visible` rule, from the ring token.** The live site's only `box-shadow` anywhere is its focus ring: `rgb(95,59,227) 0 0 0 2px`. Use the ring token RB-s-1 defines. `:focus-visible` (not `:focus`) so a mouse click does not paint a ring.

**The ring is TRANSIENT feedback under the accent budget** and never counts as a second action (CVO correction C2) -- RB-s-5 owns that count.

**`prefers-reduced-motion` is respected**, as the live site does [3/3].

**Evidence is a keyboard walk with a screenshot at every stop**, over the three routes AND every touched interactive surface in RB-s-12's inventory. The walk also carries III.9: the system survives a raised browser default font size.

### ACCEPTANCE

<criterion id="RB6-AC1" cell_refs="RB-s-6"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB6-AC1` -- typecheck clean -- the change compiles.

<criterion id="RB6-AC2" cell_refs="RB-s-6"><invocation>cd <WS> && timeout 120 python -c "import io,re; s=io.open('portal/src/index.css',encoding='utf-8').read(); m=re.findall(r'outline:\\s*none\\s*!important',s); print('OUTLINE-NONE-IMPORTANT:',len(m)); print('VERDICT:','FOCUS-RESTORED' if len(m)==0 else 'SUPPRESSED')"</invocation><expect>VERDICT: FOCUS-RESTORED</expect></criterion>
`RB6-AC2` -- the blanket outline suppression is gone. **At issuance this reads 1**, applied to every element and pseudo-element.

<criterion id="RB6-AC3" cell_refs="RB-s-6"><invocation>cd <WS> && timeout 120 python -c "import io,re; s=io.open('portal/src/index.css',encoding='utf-8').read(); n=s.count(':focus-visible'); blocks=re.findall(r':focus-visible[^{]*[{]([^}]*)[}]',s,re.S); ring=[b for b in blocks if (re.search(r'box-shadow\s*:',b) and 'none' not in b.split('box-shadow')[1][:40]) or re.search(r'outline\s*:\s*[^;]*(?:px|var|#)',b)]; print('FOCUS-VISIBLE-SELECTORS:',n,'THAT-PAINT-A-RING:',len(ring)); print('VERDICT:','RING-WIRED' if len(ring)>=1 else 'NO-RING')"</invocation><expect>VERDICT: RING-WIRED</expect></criterion>
`RB6-AC3` -- a `:focus-visible` rule actually PAINTS a ring. **At issuance one `:focus-visible` selector exists but paints nothing**, so counting selectors would have passed vacuously -- the criterion counts rules that set `box-shadow` or `outline`.

<criterion id="RB6-AC4" cell_refs="RB-s-6"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs market <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-6_market_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB6-AC4` -- the `/market` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB6-AC5" cell_refs="RB-s-6" judgment="true"/>
`RB6-AC5` -- graded at L9 from the keyboard-walk screenshots: every interactive element on the three routes and on every touched surface in the RB-s-12 inventory shows the accent ring on keyboard focus, and no ring appears on a mouse click. RECORD; NO VERDICT.

<criterion id="RB6-AC6" cell_refs="RB-s-6" judgment="true"/>
`RB6-AC6` -- graded at L9: the system survives a raised browser default font size on the same walk (brief III.9). RECORD; NO VERDICT.

<expected_criteria>RB6-AC1, RB6-AC2, RB6-AC3, RB6-AC4, RB6-AC5, RB6-AC6</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- Use `:focus-visible`, never `:focus`. A ring on every mouse click is the defect the original suppression was reaching for.

<paths>
portal/src/index.css
portal/src/ui/
org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-6`.
<owned_cells>RB-s-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `RB6-AC1` .. `RB6-AC6`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-6.focus-visible.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> RB6-AC1,RB6-AC2,RB6-AC3,RB6-AC4,RB6-AC5,RB6-AC6` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `focus-visible.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~1, queue position 6; fresh worktree pair branched from `feature/d13-visual-elevation`.

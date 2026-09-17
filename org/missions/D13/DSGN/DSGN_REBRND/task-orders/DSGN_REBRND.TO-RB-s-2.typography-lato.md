# TO DSGN_REBRND.TO-RB-s-2 -- typography -- Lato self-hosted, tabular numerals, the mono census to zero

<to_id>DSGN_REBRND.TO-RB-s-2</to_id>
<project>DSGN_REBRND</project>
<issued_to>0.9.0_WK_DSGN_REBRND~1</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-11</issued_date>
<status>complete</status>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_REBRND_PRD.md` v0.2 @8ad762f7bf | **Decomp cell:** `RB-s-2` | **outcome_ref:** FWD-2, FWD-1 | **depends_on:** `RB-s-1` | **slot:** ~1, queue position 2

---

## WORKER FACE

### THE CELL

`RB-s-2` -- typography.

**Lato, self-hosted.** `portal/src/index.css:16` imports **Inter** from Google Fonts and `:142` sets it as the body face. Both go. Ship Lato woff2 at **400 and 700 only** under `portal/public/fonts/`, with the OFL text beside them. The brand licences six weights and both the brand book and `opalinvest.com` ship two: restricting to two forces SIZE and WHITESPACE to carry hierarchy, which survives a reader who has raised their default font size.

**AMENDED BY THE ISSUER, disarming rows `DSGN_REBRND-W1-S5` (BLOCKING) and `DSGN_REBRND-W1-S6`.**

⛔ **THE FONTS ARE ALREADY ON THIS BOX. DO NOT FETCH ANYTHING.** Three Lato faces sit at
`.runtime/codex-seats/4.0.0_SA_CRO/performance-export-recon/fonts/` -- `Lato-Regular.ttf` (400),
`Lato-Light.ttf` (300) and `Lato-SemiBold.ttf` (600) -- captured by another seat on 2026-09-10 with
the licence committed at `docs/research/investor_reporting_export_20260910/FONT_LICENSE.txt`.
**Verified by the issuer from the TTF NAME TABLE, not the filename:** family `Lato`, subfamilies
`Regular` / `Light` / `SemiBold`.

**Copy them into `portal/public/fonts/`, record each file's sha256 in the result file**, and keep
`OFL.txt` beside them. The SIL OFL 1.1 permits bundling and web serving. `fontTools` 4.63.0 and
`brotli` are installed, so a `.ttf` -> `.woff2` conversion is a **LOCAL** act; if you convert,
record both hashes. Serving the `.ttf` directly through `@font-face` is equally acceptable. **Either
way NO NETWORK REQUEST IS MADE, and none is authorized.**

**The 700 weight is not on this box.** Do NOT fetch it. Map `font-weight: 700` onto the 600
(SemiBold) face and **say so in `portal/public/fonts/README.md`** with one line naming the
substitution and why. A weight the box lacks is a surprise row's `world_is`, not a stop. The 700
fetch is carried to Andrew as a reserved call by the CTO's loop and **does not block this cell**.

**The licence is already in the estate** -- `docs/research/investor_reporting_export_20260910/FONT_LICENSE.txt` is Lato's SIL Open Font License 1.1 (`Reserved Font Name "Lato"`). Confirm the woff2 files you ship are covered by it and copy that text beside them. Brief V.1's "not verified" is closed by that file.

**The numerals are the single biggest change.** There are **222** `font-mono` occurrences across `portal/src/` and **no `--font-mono` is defined anywhere**, so every figure in the product renders in the browser's code-editor stack (Menlo/Monaco/Consolas). `body` already sets `font-variant-numeric: tabular-nums`, so the mono adds nothing but a worse typeface. Replace it with Lato carrying `tabular-nums` **through ONE token**.

`letter-spacing` is `normal` on every heading and body node measured on the live site [3/3]. Keep tracking only where text is uppercase AND under 14px.

**The bar on alignment is "no worse than before", not "better".** Figures must still align in columns.

### ACCEPTANCE

<criterion id="RB2-AC1" cell_refs="RB-s-2"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB2-AC1` -- typecheck clean -- the change compiles.

<criterion id="RB2-AC2" cell_refs="RB-s-2"><invocation>cd <WS> && timeout 120 python -c "import pathlib,re; c=0; fl=0; [ (c:=c+len(re.findall(r'font-mono',p.read_text(encoding='utf-8',errors='replace'))), fl:=fl+1) for p in pathlib.Path('portal/src').rglob('*.tsx') ]; print('FONT-MONO:',c,'in',fl,'tsx files'); print('VERDICT:','CLEARED' if c==0 else 'MONO-REMAINS')"</invocation><expect>VERDICT: CLEARED</expect></criterion>
`RB2-AC2` -- the `font-mono` census reads ZERO across `portal/src`, denominator printed. **At issuance this reads 221 across 263 files.** Any survivor is a code sample and is enumerated in the result file.

<criterion id="RB2-AC3" cell_refs="RB-s-2"><invocation>cd <WS> && timeout 120 python -c "import io; s=io.open('portal/src/index.css',encoding='utf-8').read(); low=s.lower(); g=low.count('fonts.googleapis.com'); i=low.count(chr(39)+'inter'+chr(39)); print('GOOGLE-FONTS:',g,'INTER-REFS:',i); print('VERDICT:','SELF-HOSTED' if (g==0 and i==0) else 'EXTERNAL-OR-INTER')"</invocation><expect>VERDICT: SELF-HOSTED</expect></criterion>
`RB2-AC3` -- no external font request AND no Inter reference remains. **At issuance this reads 1 and 1**; one verdict over both so removing only the import cannot pass.

<criterion id="RB2-AC4" cell_refs="RB-s-2"><invocation>cd <WS> && timeout 120 python -c "import os,hashlib; d='portal/public/fonts'; fs=sorted(os.listdir(d)) if os.path.isdir(d) else []; faces=[f for f in fs if f.lower().endswith(('.woff2','.ttf','.woff'))]; lic=[f for f in fs if 'OFL' in f.upper() or 'LICENSE' in f.upper()]; h={f: hashlib.sha256(open(os.path.join(d,f),'rb').read()).hexdigest()[:16] for f in faces}; print('FACES:',faces); print('HASHES:',h); print('LICENCE:',lic); print('VERDICT:','SELF-HOSTED-ON-BOX' if (len(faces)>=1 and lic) else 'NO-FACES-OR-NO-LICENCE')"</invocation><expect>VERDICT: SELF-HOSTED-ON-BOX</expect></criterion>
`RB2-AC4` -- **AMENDED.** At least one real font FACE and the licence are present in `portal/public/fonts/`, and every face prints its sha256. **The old invocation was `ls public/fonts/ | head -20; echo rc=$?` -- a PIPELINE, whose exit status is `head`'s, so it returned rc=0 with the directory ABSENT OR EMPTY** (row `DSGN_REBRND-W1-S6`, proved empirically by the worker, which graded by direct enumeration instead of trusting the rc I told it to trust). This form enumerates, and the hashes make the artifact identifiable rather than merely counted.

<criterion id="RB2-AC5" cell_refs="RB-s-2"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs market <WS>/org/missions/D13/DSGN/DSGN_REBRND/deliverables/<SERIAL>/rb-s-2_market_1440.png --port <PORT>; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`RB2-AC5` -- the `/market` route renders at 1440 and the script prints the RESOLVED CANVAS -- that printed value is the evidence, not a reading of the CSS. READ the PNG before the flip.

<criterion id="RB2-AC6" cell_refs="RB-s-2" judgment="true"/>
`RB2-AC6` -- graded at L9 from the before/after PNGs: figures read as the firm typeface, not a terminal font, and column alignment is no worse than before. RECORD; NO VERDICT.

<expected_criteria>RB2-AC1, RB2-AC2, RB2-AC3, RB2-AC4, RB2-AC5, RB2-AC6</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_REBRND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **⛔ THE BRANCH IS BINDING. Andrew-direct 2026-09-11:** *"keep it all on a feature branch so if it goes to hell we haven't fucked our entire shit up."* **No act of this order writes to `DEV` or to `CLOUD`.** Your worktree pair is branched from `feature/d13-visual-elevation` in BOTH repos and your commits land there and nowhere else. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc.
- **Dev server.** `node_modules` is a junction; **do not run `bun install`**. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **The three binding rulings from the PRD preamble reach this cell:** the canvas is light `#F4F6FA` with `#0A1733` reserved for deliberate inverted bands -- **the charts keep their colour** (what goes quiet is the chrome) -- nothing third-party is vendored.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- **Do not change a number's VALUE, format or precision.** This cell changes the face it renders in and nothing else.

<paths>
portal/src/index.css
.runtime/codex-seats/4.0.0_SA_CRO/performance-export-recon/fonts/
docs/research/investor_reporting_export_20260910/FONT_LICENSE.txt
portal/public/fonts/
portal/src/**/*.tsx
portal/src/**/*.css
org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md</decomp_doc> v1 @e616ad99ec, cell `RB-s-2`.
<owned_cells>RB-s-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `RB2-AC1` .. `RB2-AC6`. Instance at
`org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-2.typography-lato.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> RB2-AC1,RB2-AC2,RB2-AC3,RB2-AC4,RB2-AC5,RB2-AC6` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `typography-lato.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~1, queue position 2; fresh worktree pair branched from `feature/d13-visual-elevation`.

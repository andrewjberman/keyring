# TO IRPT_FNTEND.TO-FE-s-17 -- Lato is a packaging input: the on-box OFL files into the render package

<to_id>IRPT_FNTEND.TO-FE-s-17</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~2</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-11</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F9: locally packaged licensed fonts; PATHS brand rows) | **Decomp cell:** `FE-s-17` (round 2, v0.2) | **outcome_ref:** FWD-8, FWD-12, FWD-3 | **depends_on:** `FE-s-12` | **slot:** ~2, queue position 1 | **slug rows:** W2-S3

---

## WORKER FACE

### THE CELL

`FE-s-17` -- the render package's `print.css` declares three Lato faces whose `url()` targets do not exist (`render/assets/fonts/` holds only `FONT_LICENSE.txt`), so every capture fell back to the system stack. The CTO ruled the fonts a packaging input, not egress: three OFL 1.1 files are already on this box and their provenance is recorded beside them.

Copy, byte for byte, from `<WS>/../../../Users/AndrewBerman/Desktop/ajb_workspace/.runtime/codex-seats/4.0.0_SA_CRO/performance-export-recon/fonts/` -- use the absolute path `/c/Users/AndrewBerman/Desktop/ajb_workspace/.runtime/codex-seats/4.0.0_SA_CRO/performance-export-recon/fonts/` (the `.runtime` tree is untracked and lives only in the main checkout) -- into `src/pages/InvestorReporting/render/assets/fonts/`:

| file | bytes | sha256 | weight |
|---|---|---|---|
| `Lato-Regular.ttf` | 656568 | `d636e4683231f931eda222d588e944d082bfd3bdba02f928bee461c0f185b251` | 400 |
| `Lato-Light.ttf` | 643884 | `cf2a774503baf418d584f49967bd160e1e03f087c13b25602f28024ec7788f08` | 300 |
| `Lato-SemiBold.ttf` | 668548 | `71b8b7decbe75a881ed267be539d402bd1e9420b799658aada4e0d1bd5af803c` | 600 |

The 700 weight (Bold) and the italics are NOT on the box and are NOT fetched: 600 stands in for 700 and the package says so. Write `render/assets/fonts/fonts.manifest.json` (name, bytes, sha256, weight, style, licence `OFL-1.1`, `licence_file: FONT_LICENSE.txt`, `source: sources.json of the CRO's export-recon capture 2026-09-10`, and `stand_ins: { "700": "Lato-SemiBold.ttf (600)" }`, `not_packaged: ["700", "italic"]`). Rewrite `print.css`'s `@font-face` block: faces for 300, 400 and 700 (the 700 face's `src` is the SemiBold file, with a comment naming the stand-in and the carried call), `format('truetype')`, `local()` first as today, every `url()` local (`/src/pages/InvestorReporting/render/assets/fonts/...`), no italic face (a comment says none is packaged); no other rule of `print.css` changes. `render/manifest.ts` gains a `fonts` declaration mirroring the manifest (files, weights, stand-ins, not-packaged) so a consumer of the package can read what it ships. Nothing else in `render/` changes.

### ACCEPTANCE

<criterion id="F17-AC1" cell_refs="FE-s-17"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F17-AC1` -- the whole portal typechecks.

<criterion id="F17-AC2" cell_refs="FE-s-17"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-17/fonts.test.ts</invocation><expect>FONTS: 3 of 3</expect></criterion>
`F17-AC2` -- each ttf under `render/assets/fonts/` hashes (sha256) to the manifest's value and the manifest's three entries are the three files listed above.

<criterion id="F17-AC3" cell_refs="FE-s-17"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-17/fonts.test.ts</invocation><expect>EXTERNAL FONT HOSTS: 0</expect></criterion>
`F17-AC3` -- every `url()` in `print.css` is a local path and every target file exists (the test enumerates the urls and prints them).

<criterion id="F17-AC4" cell_refs="FE-s-17"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-17/fonts.test.ts</invocation><expect>STAND-IN DECLARED: 700<-600</expect></criterion>
`F17-AC4` -- `render/manifest.ts` declares the 700 stand-in and the not-packaged set, equal to `fonts.manifest.json`.

<criterion id="F17-AC5" cell_refs="FE-s-17"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs "investor-reporting/print?bundle=perf-narrative-fixture-1" <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-17_print_performance_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-11-print.json --console "REFS RESOLVED" --netlog <WS>/.scratch/fe-s-17.netlog; echo rc=$?</invocation><expect>REFS RESOLVED: 1 of 1</expect></criterion>
`F17-AC5` -- the print route renders the performance document with the packaged font and writes its request log (ui-smoke prints `DID NOT LAND` for the query-string route; the resolver line is the bar).

<criterion id="F17-AC6" cell_refs="FE-s-17"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-17/fonts-served.test.ts</invocation><expect>LATO OFF-ORIGIN: 0</expect></criterion>
`F17-AC6` (AMENDED BY THE ISSUER at the FE-s-17 report on row IRPT_FNTEND-W2-S7) -- the test reads `../.scratch/fe-s-17.netlog` (written by F17-AC5) and prints, unnarrowed first, `FONT REQUESTS: n` (every request whose URL names a font file or a font stylesheet) and `SHELL FONT REQUESTS OFF-ORIGIN: n` (the portal shell's own faces -- today the Inter import in `src/index.css`, outside this order's grant and this project's scope; recorded, never a bar); then the bar this cell owns: `LATO REQUESTS: n` (URL contains `Lato-`, status 200, n at least 1) and `LATO OFF-ORIGIN: 0` (no request for a Lato face leaves the dev server's origin). The first bar's population was the whole page and counted a face this order cannot move; the amended bar is the render package's faces, which is the cell's claim.

<criterion id="F17-AC7" cell_refs="FE-s-17"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-17/fonts.test.ts</invocation><expect>LICENCE: OFL-1.1</expect></criterion>
`F17-AC7` -- `render/assets/fonts/FONT_LICENSE.txt` contains the string `SIL OPEN FONT LICENSE Version 1.1` and the manifest names it.

<criterion id="F17-AC8" cell_refs="FE-s-17"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>0 fail</expect></criterion>
`F17-AC8` -- the whole Investor Reporting set is green.

<criterion id="F17-AC9" cell_refs="FE-s-17" judgment="true"/>
`F17-AC9` -- graded at L9 from the print PNG against `deck_generation/brand_spec/brand.json`: the document sets in Lato. RECORD; NO VERDICT.

<expected_criteria>F17-AC1, F17-AC2, F17-AC3, F17-AC4, F17-AC5, F17-AC6, F17-AC7, F17-AC8, F17-AC9</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. No fetch of any font from any source; the three files come from the on-box path above and nowhere else (a file whose sha256 differs from the table is refused by your own test). A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal` as in your identity line. Portal commit pathspec: `src/pages/InvestorReporting/render/assets/fonts/ src/pages/InvestorReporting/render/print.css src/pages/InvestorReporting/render/manifest.ts src/pages/InvestorReporting/__tests__/fe-s-17/`. Workspace records under org/ only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints; kill it before your final report. Quote a route carrying `?`.
- **Numbers.** 1440 is a test setup.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only (the netlog lands there). PNGs to your deliverables folder.
- **Surprise.** ONE row per finding in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md`, id `IRPT_FNTEND-W2-S<k>` continuing from `IRPT_FNTEND-W2-S7` (read the file for the last W2 id; if it does not exist, create it with a one-line header and a fenced `json` array holding your row); never edit an existing row; keep working.
- Report push state as LOCAL.

<paths>
portal/src/pages/InvestorReporting/render/assets/fonts/
portal/src/pages/InvestorReporting/render/print.css
portal/src/pages/InvestorReporting/render/manifest.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-17/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.2 @430c5fcb4a, cell `FE-s-17`.
<owned_cells>FE-s-17</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F17-AC1` .. `F17-AC9`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-17.lato-packaging.proof_of_spec.json`
(phase `BUILD-GENERAL` -- AMENDED BY THE ISSUER at the FE-s-12 drain on row IRPT_FNTEND-W1-S15: the schema's phase enum has no BUILD member, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F17-AC1,F17-AC2,F17-AC3,F17-AC4,F17-AC5,F17-AC6,F17-AC7,F17-AC8,F17-AC9` BEFORE the `complete` flip. `F17-AC9` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `lato-packaging.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 (ADMITTED) -- carried.
fonts on box: RUN by the issuer -- 3 of 3 ttf present with sha256 equal to the CRO capture's sources.json; OFL.txt 4407 bytes; FONT_LICENSE.txt already under render/assets/fonts/ (4499 bytes). Egress: none (CTO 95939, analysis ruling 4); the 700 weight is Andrew's carried call.
lane: the <paths> block IS the grant; portal paths bind by reading; workspace paths bind mechanically. render/ was FE-s-4's; that cell is terminal.
</preflight>

Seating: slot ~2, queue position 1; seated when `FE-s-12` is terminal and drained, fresh worktree pair from HEAD.

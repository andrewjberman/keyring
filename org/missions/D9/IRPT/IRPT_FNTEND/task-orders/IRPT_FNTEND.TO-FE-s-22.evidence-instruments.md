# TO IRPT_FNTEND.TO-FE-s-22 -- the evidence plane's two instruments: a hash rule that discriminates, and a detector that stops always firing

<to_id>IRPT_FNTEND.TO-FE-s-22</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~2</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-12</issued_date>
<status>blocked</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (FIXTURES AND EVIDENCE) | **Decomp cell:** `FE-s-22` (round 3, v0.3 @38f68b965c) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** `FE-s-19` (its captures must be taken on a tree where bodies mount) | **slot:** ~2, queue position 2 | **rows:** W1-S36, S33

---

## WORKER FACE

### THE CELL

`FE-s-22` -- two instruments on the evidence plane, both measured broken in round 2.

**(a) THE SCOPED CAPTURE-HASH RULE (`1.0.0_SA_CTO` ruling 4).** Round 2's `FE-s-18` produced three captures from three fixtures differing in `basis` and in the presence of `classification`, and all three were BYTE-IDENTICAL (`sha256 8ce52e6ad0b60e29`). Nothing asked for a hash comparison; the worker did it anyway, and it is the only reason the round found `W1-S33` at all. The eye would have read three plausible pictures.

Build it as a REUSABLE assertion under `__tests__/fe-s-22/`, **SCOPED, not blanket**:

```
  fixtures differ in a field THAT THE CAPTURE CLAIMS TO RENDER  -> DISTINCT HASHES ARE ASSERTED
  fixtures differ only in a field the capture does NOT claim     -> the set DECLARES that, and
                                                                    identical hashes are ADMITTED
```

The blanket form is wrong and the CTO ruled it out: two fixtures may legitimately differ in a field a page does not show. **The classification comes from the manifest's own `fixture` and claim fields, never from a filename allowlist** -- a filename rule absorbs exactly the cross-fixture collision it exists to catch.

⛔ **THIS CELL DOES NOT TOUCH `__tests__/fe-s-18/`.** `FE-s-18` is CARRIED with `F18-AC3` and `F18-AC17` UNTOUCHED by CTO ruling 1; its literal arm stays exactly as cut. You build the rule where FUTURE capture sets pick it up.

**(b) `W1-S36` -- A DETECTOR THAT ALWAYS FIRES.** `scripts/ui-smoke.mjs:341` compares `window.location.pathname` against the FULL ROUTE STRING, so a route carrying a query string can never match. `DID NOT LAND (auth redirect? bad route?)` therefore prints on EVERY query-bearing route whether or not anything went wrong -- it printed on a round-2 run that landed and rendered three pages. Five of round 2's twelve captures carry that line for no reason.

**And the mirror is the real cost: it is equally unable to report a GENUINE failure to land on such a route.** A detector that cannot distinguish those two states is not a detector. The fix is one line (`new URL(ORIGIN + route).pathname`), and you prove BOTH directions.

### ACCEPTANCE

<criterion id="F22-AC1" cell_refs="FE-s-22"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F22-AC1` -- the whole portal typechecks.

<criterion id="F22-AC2" cell_refs="FE-s-22"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-22/capture-hash.test.ts</invocation><expect>CLAIMED FIELD DIFFERS: distinct hashes asserted</expect></criterion>
`F22-AC2` -- a capture set whose fixtures differ in a CLAIMED field asserts distinct hashes, and a seeded pair that is byte-identical under that condition turns the assertion RED. The test prints the claimed field it keyed on.

<criterion id="F22-AC3" cell_refs="FE-s-22"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-22/capture-hash.test.ts</invocation><expect>UNCLAIMED FIELD DIFFERS: identical admitted</expect></criterion>
`F22-AC3` -- **the arm that keeps the rule from being the blanket form.** Two fixtures differing ONLY in a field the capture does not claim are admitted with identical hashes, and the set declares which field that was.

<criterion id="F22-AC4" cell_refs="FE-s-22"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-22/capture-hash.test.ts</invocation><expect>ROUND-2 COLLISION REPRODUCED: 3 of 3</expect></criterion>
`F22-AC4` -- **the rule is tested against the real incident, not only against fixtures it was written beside.** The three round-2 Holdings captures (`basis` and `classification` are CLAIMED by those captures) are run through the rule and it REFUSES them. A rule that cannot catch the case that motivated it is decoration.

<criterion id="F22-AC5" cell_refs="FE-s-22"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs "investor-reporting/print?bundle=fe-s-16-narrative&narrative=1&tenant=F-49F&scope=fp-49f-0824&revision=rev-49f-000091" <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-22_landed_query_route_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-16-print-narrative.json --console "REFS RESOLVED"</invocation><expect>REFS RESOLVED: 1 of 1</expect></criterion>
`F22-AC5` -- a query-bearing route that genuinely LANDS renders and resolves. This is the capture the fixed detector must stop maligning.

<criterion id="F22-AC6" cell_refs="FE-s-22"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-22/smoke-detector.test.ts</invocation><expect>LANDED QUERY ROUTE: no DID NOT LAND</expect></criterion>
`F22-AC6` -- with the one-line fix, a query-bearing route that lands prints NO `DID NOT LAND`. The test drives `ui-smoke`'s comparison directly rather than scraping a capture run's console.

<criterion id="F22-AC7" cell_refs="FE-s-22"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-22/smoke-detector.test.ts</invocation><expect>GENUINELY BAD ROUTE: DID NOT LAND</expect></criterion>
`F22-AC7` -- **the arm that proves the detector still detects.** A route that genuinely fails to land -- including one carrying a query string -- STILL prints `DID NOT LAND`. Fixing an always-firing detector by making it never fire is the failure mode this arm exists to prevent.

<criterion id="F22-AC8" cell_refs="FE-s-22"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>0 fail</expect></criterion>
`F22-AC8` -- the whole Investor Reporting set is green. By your seating `FE-s-19` and `FE-s-20` have drained; a remaining failure that is not yours is a BLOCKING row naming it.

<criterion id="F22-AC9" cell_refs="FE-s-22" judgment="true"/>
`F22-AC9` -- graded at L9: the scoped rule's claim model is one a later cell can actually apply without re-deriving it, and the detector's two arms are genuinely opposite. RECORD; NO VERDICT.

<expected_criteria>F22-AC1, F22-AC2, F22-AC3, F22-AC4, F22-AC5, F22-AC6, F22-AC7, F22-AC8, F22-AC9</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. ⛔ **`__tests__/fe-s-18/` IS NOT IN YOUR GRANT AND MUST NOT BE TOUCHED** -- `FE-s-18` is carried with its criteria untouched by CTO ruling 1. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- ⛔ **`scripts/ui-smoke.mjs` IS THE SHARED SMOKE TOOL FOR THE WHOLE PORTAL, not this project's.** Change the ONE comparison at `:341` and nothing else. Any other change to it is a surprise row naming what you would have changed and why -- a broad edit to a shared instrument mid-round is how every other cell's evidence silently changes meaning.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal` as in your identity line. Portal commit pathspec: the files you changed under `src/` and `scripts/`, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; kill it before your final report. Quote any route carrying `?` or `&`.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only. PNGs to your deliverables folder.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W2-S<k>` continuing the W2 sequence (read the file for the last W2 id -- `FE-s-20` ran on this slot before you). Re-read immediately before minting; never edit an existing row; keep working.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/scripts/ui-smoke.mjs
portal/src/pages/InvestorReporting/__tests__/fe-s-22/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.3 @38f68b965c, cell `FE-s-22`.
<owned_cells>FE-s-22</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F22-AC1` .. `F22-AC9`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-22.evidence-instruments.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F22-AC1,F22-AC2,F22-AC3,F22-AC4,F22-AC5,F22-AC6,F22-AC7,F22-AC8,F22-AC9` BEFORE the `complete` flip. `F22-AC9` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `evidence-instruments.result.md` beside it, stating the claim model in the terms a later cell will apply. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round.
the collision: RUN by the issuer -- sha256 of the three round-2 Holdings captures is 8ce52e6ad0b60e29... for all three; across FE-s-18's twelve PNGs, 10 distinct hashes, and after the AC6 re-capture the manifest read 11 entries / 9 distinct / 1 colliding set.
the detector: RUN -- ui-smoke.mjs:341 compares window.location.pathname to the full route string; W1-S36 records it firing on a run that landed and rendered three pages; 5 of 12 round-2 captures carry the line.
ruling: RUN -- 1.0.0_SA_CTO ruling 4 SCOPES the hash rule (claimed vs unclaimed field) and explicitly rejects the blanket form; ruling 1 CARRIES FE-s-18 untouched, which is why __tests__/fe-s-18/ is excluded from this grant.
lane: the <paths> block IS the grant; scripts/ui-smoke.mjs is a SHARED instrument and the grant is one comparison line.
</preflight>

Seating: slot ~2, queue position 2; seated when `FE-s-19` is terminal and DRAINED, on a fresh worktree pair cut from the post-drain HEAD, with the `<status>` flip committed BEFORE the worktree is cut (row IRPT_FNTEND-S26).

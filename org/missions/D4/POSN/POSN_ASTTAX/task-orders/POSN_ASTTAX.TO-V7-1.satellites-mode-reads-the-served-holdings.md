# TO POSN_ASTTAX.TO-V7-1 -- THE SATELLITES MODE READS THE SERVED `holdings.json` (one total per ticker, labels served) AND `characteristics.json` (the additional lambda's aggregates); NO computation in the adapter; the as-of is Black Diamond's. Models and ETFs modes untouched. Committed on the round's ONE drain ref (AT5-s-7, F3; FWD-6 on Satellites)

<to_id>POSN_ASTTAX.TO-V7-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~22</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-14</issued_date>
<status>staged</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.7** @`99cc431075`
(C-SATELLITE-SOURCE) - **Decomp cell:** `AT5-s-7` - **Issuance:** round 5, wave 3, same slot as `TO-V6-1` -- **you start this
order only after `TO-V6-1` is `complete` and drained onto `refs/drains/posn-5-portal`, AND `TO-V2-1`, `TO-V4-1` (schemas) and
`TO-V9-1` (the route) are `complete` at HEAD** (the COO names all four hashes at hand-over). **GATES `AT5-s-8` (R1).**

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_ASTTAX~22`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_ASTTAX~22;`. First act:
`git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`. Workspace commits via safe-commit.sh under
your serial; portal commits inside `portal/` on YOUR branch `wk-posn-5-22c-portal`, PRE-CUT by the COO at hand-over as a linked worktree of the portal repo FROM `refs/drains/posn-5-portal` (verify with `git -C portal rev-parse --abbrev-ref HEAD`; do NOT re-create it). Never
push, merge, rebase, `checkout --`, `clean`; never `git add portal`. Append your branch line to `ledger/PORTAL_REFS.md`.

## THE CELL

Andrew ~17:2xZ: one TOTAL per ticker per satellite, *"total GLD listed as Commodity Asset, Metals Sub-Asset ... Total VXX ... as
Structured Asset, Hedge Sub-Asset"*, and *"Satellites simply need to have an additional lambda to do weighted characteristics
aggregates"*. Measured at the pin: `portal/src/pages/Positioning/shared/satelliteAdapter.ts` (306 lines) BUILDS satellites by
blending YANG's books -- B) the holding-weight union blend (`:53-56`, "PLAIN weighted SUM, never renormalised"), A) the measures
blend, `:133-159` allocation/delta over `PositioningAllocation`. `portal/src/api/endpoints/satelliteRegistry.ts` exports ONE read,
`getSatelliteRegistry()` on `SATELLITE_REGISTRY_ENDPOINT = '/api/scoped/satellites/registry.json'`, which THROWS on a malformed
body or a null `as_of` and has NO fallback beneath it (@`24a8435642` -- read its header; the empty-vs-failed distinction is
load-bearing). `SatelliteBook {code, displayName, constituents}` at `shared/satelliteSet.ts:74-78`.

**Served inputs (schemas READ BACK from the committed producers, never from this text):**
- `/api/scoped/satellites/holdings.json` -> `platinum/satellites/holdings.json` (TO-V2-1): `satellites.<code>.holdings[]{ticker,
  weight, asset_class, sub_asset_class, sleeves}` + `coverage`, `as_of`.
- `/api/scoped/satellites/characteristics.json` -> `platinum/satellites/characteristics.json` (TO-V4-1): `satellites.<code>.{fee,
  yield, duration, beta, returns, coverage{weight_with_value, weight_null}}`, `as_of`, `inputs`.
- Both leaves are admitted by the edge router only after TO-V9-1 (B5) is DEPLOYED; before that they 404 with
  `unknown_satellites_resource`, and `getSatellite*()` MUST throw, never default.

**Your act:**
1. `satelliteRegistry.ts`: add `getSatelliteHoldings(firmOverride?)` and `getSatelliteCharacteristics(firmOverride?)` with the SAME
   contract as `getSatelliteRegistry` (same `?firm=<slug>` rule via `bucketSuffix`, same throw-on-malformed, `as_of` REQUIRED,
   no fallback, no default firm). Export the two endpoint constants beside the first.
2. `satelliteSet.ts`: the served-holdings and served-characteristics contract TYPES beside `SatelliteBook` (imported by the
   api layer type-only, never a hand copy of membership).
3. `satelliteAdapter.ts`: the Satellites mode's HOLDINGS come from `holdings.json` rows (one row per ticker, `weight` as served,
   `asset_class`/`sub_asset_class` as served -- a null label renders as an "unlabelled" bucket, disclosed, never guessed); its
   MEASURES come from `characteristics.json` (a NULL characteristic renders the way VXX's null yield already renders); its
   `as_of` is `holdings.json`'s (Black Diamond's partition date). The B) union blend and the A) measures blend are REMOVED for the
   Satellites mode; **no weighted sum, no renormalisation, no Yang addition anywhere in the adapter** (V7-AC3 greps for it).
   The five-class allocation per satellite = the sum of served weights per served `asset_class`, in F2's five-key
   `PositioningAllocation` (a sum over served rows is aggregation for display, not computation of a holding -- state it once).
4. Models and ETFs modes: UNTOUCHED (`etfAdapter.ts`, `bookSet.ts` unchanged -- V7-AC2).

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route.

## SURPRISE ROWS

ONE row per off-cell finding, `POSN_ASTTAX-Z-W22-S<k>` (continue your sequence), appended to
`org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md`; keep working.

## CRITERIA -- structured, one clause each

<criterion id="V7-AC1" cell_refs="AT5-s-7"><invocation>timeout 60 bash -c "for t in TO-V2-1 TO-V4-1 TO-V9-1; do f=\$(ls org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.\$t.*.md); printf '%s ' \$t; grep -o -m1 '<status>[^<]*</status>' \$f; done"</invocation><expect>all three read `complete` at HEAD, and `git -C portal show refs/drains/posn-5-portal:src/api/portal-proxy.ts` carries the five-key PositioningAllocation (TO-V6-1 drained). Any other reading: STOP with a row.</expect></criterion> `V7-AC1` -- FOUR DEPENDENCIES, READ BACK.

<criterion id="V7-AC2" cell_refs="AT5-s-7"><invocation>timeout 60 git -C portal diff --stat refs/drains/posn-5-portal -- src/pages/Positioning src/api/endpoints/satelliteRegistry.ts</invocation><expect>exactly three files changed: shared/satelliteAdapter.ts, shared/satelliteSet.ts, src/api/endpoints/satelliteRegistry.ts; etfAdapter.ts and bookSet.ts UNCHANGED (0 lines); nothing under src/pages/Attribution/.</expect></criterion> `V7-AC2` -- THREE FILES, MODELS AND ETFS UNTOUCHED.

<criterion id="V7-AC3" cell_refs="AT5-s-7"><invocation>timeout 60 comp-read portal/src/pages/Positioning/shared/satelliteAdapter.ts --enumerate 'blendByIndex|weighted|renormal|current_holdings|positioning_data'</invocation><expect>ZERO hits for blendByIndex / renormal / positioning_data in the Satellites path (the ENUMERATE denominator printed); any remaining 'weighted' hit is a comment or a display aggregation over served rows, each cited by line. The adapter computes no holding.</expect></criterion> `V7-AC3` -- NO COMPUTATION IN THE ADAPTER, MEASURED BY ENUMERATION.

<criterion id="V7-AC4" cell_refs="AT5-s-7"><invocation>timeout 600 bash -c "cd portal && bun run tsc -b"</invocation><expect>exit 0 with the checked-file count; POSITIVE CONTROL: an injected type error fails the same command, then reverted.</expect></criterion> `V7-AC4` -- THE BUILD, WITH AN INSTRUMENT THAT CAN FAIL.

<criterion id="V7-AC5" cell_refs="AT5-s-7"><invocation>timeout 600 bash -c "cd portal && node scripts/ui-smoke.mjs positioning .scratch/v7_satellites.png --port <PORT>"</invocation><expect>the Satellites mode screenshot READ: nine satellites selectable; `Opal Satellite 15` shows GLD at 8.34 under the Commodities bucket (its sub-asset as SERVED -- 'Gold' before R1, 'Metals' after; state which); `Opal Satellite 80` shows VXX at 1.87 under the class the table SERVES (equity before R1, Structured after; state which); the as-of shown is holdings.json's date; served rows == rendered rows for the satellite you read (count both).</expect></criterion> `V7-AC5` -- THE RENDER, READ, AGAINST THE SERVED KEYS.

<criterion id="V7-AC6" cell_refs="AT5-s-7"><invocation>timeout 300 node -e "<NEGATIVE_CONTROL_POINT_GETSATELLITEHOLDINGS>"</invocation><expect>the read THROWS (the 404 unknown_satellites_resource envelope is not turned into an empty satellite) and the page shows an error notice, not "no holdings" -- the honest branch. If the adapter renders an empty satellite instead, the fallback that was removed @24a8435642 has been re-created one layer up: STOP and fix it in this cell.</expect></criterion> `V7-AC6` -- A FETCH FAILURE IS NOT AN EMPTY SATELLITE.

<criterion id="V7-AC7" cell_refs="AT5-s-7"><invocation>timeout 60 git -C portal log --format='%H %an %s' refs/drains/posn-5-portal..wk-posn-5-22c-portal</invocation><expect>your commit(s) only under 0.9.0_WK_POSN_ASTTAX~22; the superproject gitlink UNMOVED read two ways at the worktree root: `git ls-tree HEAD -- portal` prints 160000 commit e85f6eb84f3a1771a37011a7e77e372570bad02a portal and `git diff --cached -- portal` is EMPTY (row W22-S2); PORTAL_REFS.md carries your branch line.</expect></criterion> `V7-AC7` -- COMMITTED FROM THE REF; THE GITLINK UNMOVED.

<criterion id="V7-AC8" cell_refs="AT5-s-7" judgment="true"><invocation>JUDGMENT -- no invocation; graded at L9</invocation><expect>Whether the Satellites mode now shows "what the satellite holds" in Andrew's sense -- one total per ticker, labelled, with the characteristics' null share honestly visible -- and whether the null-label "unlabelled" bucket is the right rendering for a ticker the table does not serve. Record the readings and offer NO verdict.</expect></criterion> `V7-AC8` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.**

<expected_criteria>V7-AC1, V7-AC2, V7-AC3, V7-AC4, V7-AC5, V7-AC6, V7-AC7, V7-AC8</expected_criteria>

<placeholders>NEGATIVE_CONTROL_POINT_GETSATELLITEHOLDINGS, PORT</placeholders>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-V7-1.satellites-mode-reads-the-served-holdings.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~22/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D4/POSN/POSN_ASTTAX/ledger/PORTAL_REFS.md
portal/src/pages/Positioning/shared/satelliteAdapter.ts
portal/src/pages/Positioning/shared/satelliteSet.ts
portal/src/api/endpoints/satelliteRegistry.ts
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round5.md</decomp_doc> round 5, cell `AT5-s-7`.
<owned_cells>AT5-s-7</owned_cells>
Read-dependencies, NOT claimed: `AT5-s-2` and `AT5-s-4` (the two served schemas -- read from the committed producers), `AT5-s-6`
(the five-key type, on the drain ref), `AT5-s-9` (the route, DEPLOYED). DOWNSTREAM: `AT5-s-8` (R1) reads your rendered Satellites
mode after the retag.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- source edits inside the frozen submodule; no deploy, no promote, no monitor.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform; the reads go through the deployed route (B5's grant, not yours).
comp-adversary: RUN on the decomposition. NOT covered, stated: (1) the issuer has not read how the page's mode switch chooses the
adapter -- if the Satellites mode's entry point is outside the three files, that is a row and a grant question, not a silent
widening; (2) the issuer has not exercised the ui-smoke auth stub on the scoped satellites route -- a 403 on the local build is a
row; (3) whether removing the A) measures blend leaves any Satellites measure the page still expects (e.g. the benchmark/relative
flags at :256) is unread by the issuer -- render, read, and file a row if a panel goes blank.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~22/POSN_ASTTAX.TO-V7-1.satellites-mode-reads-the-served-holdings.proof_of_spec.json
</proof_of_spec>

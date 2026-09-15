# TO POSN_ASTTAX.TO-V8-1 -- THE RETAG, LAST: the thirteen tickers at BOTH levels (asset_class AND the ruled sub_asset_class) in BOTH stores, VNQ's management_style first; then the bar on the local build over all nine satellites and both other modes, each ticker compared to ITS TARGET per level -- never "one of the five" (AT5-s-8, R1; FWD-1/FWD-2/FWD-5 EXERCISED, FWD-6 EXERCISED)

<to_id>POSN_ASTTAX.TO-V8-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~19</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-14</issued_date>
<status>complete</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.8** @`709d7b4221` (s.0 ADDENDUM v0.8 over v0.7 @`99cc431075`)
(C-RETAG-SET = 13, C-SUB-ASSET incl. Options Income, C-RETAG-SAFETY, C-CUTS) - **Decomp cell:** `AT5-s-8` - **Issuance:** round 5, wave 4, same slot as
`TO-V1-1` -- **STRICTLY LAST: you start only after the COO hands you this order with `TO-V1-1`, `TO-V2-1`, `TO-V4-1`, `TO-V9-1`
(deploys), `TO-V3-1` (landed) and `TO-V5-1`, `TO-V6-1`, `TO-V7-1` (drained onto `refs/drains/posn-5-portal`) all `complete` at HEAD;
V8-AC1 reads them back.** A retag into a two-class page hides the row while its weight stays in the total (the Cash defect PROD
v2.1.167 shipped once); that is why you are last.

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_ASTTAX~19`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_ASTTAX~19;`. First act:
`git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`. Commit only via
`bash .tools/safe-commit.sh --author "0.9.0_WK_POSN_ASTTAX~19 <0.9.0_WK_POSN_ASTTAX~19@opal.agent>" -F <msgfile> -- <paths>`,
msgfile by the Write tool, PURE ASCII. Never push, merge, rebase, `checkout --`, `clean`. **Your portal clone is READ-ONLY in this
order** (`git diff --stat` under portal/ must read 0 at your report -- FWD-5's bar is "no portal edit"): it is a LINKED WORKTREE of the
portal repository at `/c/tmp/wk-posn-5-19/portal`, cut by the COO at hand-over DETACHED at `refs/drains/posn-5-portal` (F1-F3 landed),
with `node_modules` junctioned from the estate's checkout (playwright-core included, W22-S9); do not create, switch or fetch it.

## THE CELL

**The target table (C-RETAG-SET + C-SUB-ASSET at PRD v0.8, Andrew ~17:2xZ / ~17:3xZ / ~20:0xZ / ~20:2xZ; the prior values of the
original twelve measured 2026-09-14 ~17:5xZ by a filtered scan, Count 12 of ScannedCount 285, and by the CTO's batch-get-item -- two
instruments, one table; JEPI point-read by the CTO at 20:03:01Z (batch-get) and carried in both halves' R1 amendments):**
```
ticker  NOW asset_class / sub_asset_class / mgmt     ->  TARGET asset_class / sub_asset_class (/ mgmt)
DBC     hedge        / Commodities  / passive        ->  Commodities  / Commodities (keeps)
GLD     hedge        / Gold         / passive        ->  Commodities  / Metals
GSG     hedge        / Commodities  / passive        ->  Commodities  / Commodities (keeps)
IAU     hedge        / Gold         / passive        ->  Commodities  / Metals
SLV     hedge        / Silver       / passive        ->  Commodities  / Metals
USO     hedge        / Oil          / passive        ->  Commodities  / Oil (keeps)
PDBC    equity       / Commodities  / active         ->  Commodities  / Commodities (keeps)
VXX     equity       / Volatility   / passive        ->  Structured   / Hedge
VIXY    hedge        / Volatility   / passive        ->  Structured   / Hedge
UVXY    equity       / Volatility   / passive        ->  Structured   / Hedge
QBER    fixed_income / Volatility   / active         ->  Structured   / Hedge
JEPI    equity       / US Large Cap / active         ->  Structured   / Options Income   (management_style active, UNCHANGED -- not a placeholder)
VNQ     equity       / US Large Cap / unknown        ->  Alternatives / Real Estate   (management_style set FIRST, from unknown)
```
BIPC stays Equity and is NOT in the set. JEPI (Andrew ~20:0xZ *"Also JEPI I would put in Structured, yes"*; ~20:2xZ *"b, Options
Income"*) is the thirteenth: `Options Income` is a NEW `sub_asset_class` value under Structured (PRD v0.8 C-SUB-ASSET); JEPI is held by
no satellite component and no Yang served book, so no served Positioning figure moves on its account -- its retag is still graded per
level like every other member. In Store 2 the JEPI dict entries are at `_shared/etf_classification.py:180` and `:495`; the
'US Dividend' map at `:633` is NOT touched. `Hedge` is a `sub_asset_class` value under `Structured`; the TOP-level `hedge` dissolves
(0 rows after). Every write NAMES ITS LEVEL. The served vocabulary's top-level VALUES are the generator's: read
`infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py:271-303` for the exact stored
spelling of the five classes (`structured`, `commodities`, `alternatives`, ...) -- store what the consumers read, never the display
label.

**Store 1:** the served DynamoDB table `etf-classifications` (the ONE place, C-ONE-SOURCE). **Store 2:** `ETF_CLASSIFICATIONS` in
`infra/aws/lambda/v2_portal/_shared/etf_classification.py` (the same 13 rows; `seed-etf-classifications.py`'s `merge_item()` reports
0 conflicts after, so a later seed changes nothing). `bd-securities` is NOT written (C-CUTS).

**THE ROLLBACK IS ONE SCRIPT, AND YOU WRITE IT BEFORE THE FIRST WRITE:** `deliverables/<you>/r1_rollback.py`, restoring the thirteen
NOW rows above (both levels + VNQ's style) by `update-item`; both halves
(`org/missions/D4/POSN/POSN_ASTTAX/ledger/NEVER_WIDEN_ROUND5_COO_HALF.md` @`f381f6f402`, `.../NEVER_WIDEN_ROUND5_CTO_HALF.md`
@`af667548d1`) carry the same table and co-sign this act.

**THE BAR (round-4 analysis s.4 item 1; `C-S84`, `C-S85`):** the denominator is a STORE ENUMERATION (every row of the table);
each of the thirteen is compared to ITS TARGET per level -- `bd-securities` already carries ratified `alternatives` on ten of the
thirteen, so "is it one of the five" PASSES ON WRONG ROWS and is refused as a bar. Then the local build (`bun run dev`, vite proxies
`/api/*` to the served plane): all NINE satellites and BOTH other modes, served labels == target per level, weight unchanged per
satellite (sum before == sum after), served rows == rendered rows, class subtotals == total; FWD-5 graded on the retag itself.

**THE SERVED REFRESH IS DRIVEN, NOT WAITED ON (L4 guidance msg 22913; CTO half R1 AMENDMENT @`3311955ebf`; COO half matching lines
in the same commit as this amendment):** immediately after BOTH stores carry the retag (V8-AC6, V8-AC7), you invoke the writers of
the retagged property once each, in dependency order -- `V8-AC14` the three yang generators invoked DIRECTLY (the SAME script your `TO-V1-1`
`V1-AC11` resolved for `<DRIVE_YANG_GENERATORS_RECORDED_EVENTS>`, extended by the holdings-attribution generator), each with the
event the state machine passed it on the last execution that ran it (`stepfunctions get-execution-history`), never a hand-written
event; the state machine itself is NEVER started (W19-S8: it consumes its own input, so the last input is 3 of 3 absent, and its
write set -- 28 Task states, an S3 delete, a CDN invalidation -- exceeds the signed keys); the pipeline's own CloudFront
invalidation lambda is invoked last with its recorded event -- then `V8-AC15` the two cot producers
invoked directly (`{}`), registry first, characteristics second. The per-ticker per-level comparison of `V8-AC10` then reads the
REFRESHED artifacts. The next scheduled fires (07:00Z / 07:20Z / the yang pipeline) are the ORGANIC leg the COO records, never
waited on. **Branch B, both halves:** any invocation fails, or a key's content differs beyond the retagged labels and the weights
they regroup (a holding appearing or vanishing, a total moving, a ticker outside the thirteen relabelled) -- STOP, run
`r1_rollback.py` (both stores), re-issue the same invocations so every served key returns to pre-retag labels, file the row.
Print the six keys' VersionIds BEFORE the retag; write the 13 prior values back on Branch B (the second, independent restore on the versioned bucket). The ETF publisher is
NOT invoked. **JEPI joined the set at PRD v0.8 @`709d7b4221` (Andrew ~20:2xZ *"b, Options Income"*); the member table above IS the thirteen and
both halves carry the JEPI row (CTO R1 amendment @`d3f0c3b79c`, COO half in the same commit as this amendment).**

**AMENDED AFTER YOUR FIRST RUN (~01:4xZ; rows W19-S11..S19, issuer rows Z-S121..Z-S129):** THE RETAG STANDS -- both stores carry the
thirteen at both levels (26 of 26, top-level hedge 0 of 285, 272 of 272 other rows unchanged; ConsistentRead at report time), and the
Models mode proves the chain end to end with no portal edit (Structured 1.50 LT / 2.0 ULT = VXX moved by the table write alone).
Your Branch B judgment is RATIFIED: every refusal was a producer's own fail-closed branch on an ABSENT INPUT, none moved a byte, and
a rollback of a correct co-signed retag over a deleted workbook and two unlanded partitions would have been the larger error. Four
criteria are re-cut to what the world admits tonight; nothing else changes. (a) `V8-AC8`: the bar is ZERO CONFLICTS ON THE THIRTEEN
(39 of 39 fields); BNDX's pre-existing module-vs-table disagreement (outside the set, unmoved by this retag) is printed and
disclosed, not this cell's. (b) `V8-AC14`: the two generators that feed the Positioning page refreshed and read at target; the
attribution generator's ONLY recorded event names a workbook the pipeline's cleanup deleted (W19-S15), so `holdings_attribution_data.json`
refreshes on Yang's next attribution UPLOAD -- an operator act, recorded as organic, never a hand-written event; the comparator uses
each PLANE's own spelling (W19-S18: the store lowercase, the yang payload display-cased, holdings.json raw). (c) `V8-AC15`: the
direct invokes were the driven act; each producer REFUSED fail-closed on an absent upstream partition (the roster's 2026-09-15 lands
~06:00:43Z; bbg/2026-09-14 lands with the 07:00 ET pull ~11:0xZ -- W19-S16/S17) and moved nothing: that measured refusal IS the
criterion's evidence tonight, and the relabelled `holdings.json` / refreshed `characteristics.json` are the ORGANIC legs V2-L8
(07:00Z) and V4-L8 (its 07:20Z fire precedes its input and will refuse -- the COO invokes it directly after the pull lands and
records both on the ledgers and a row); NOT this order's wait. (d) `V8-AC10`: the Models and ETFs arms read the refreshed yang plane
(the retag visible); the Satellites arm reads the served bytes AS THEY ARE (pre-retag holdings.json: GLD excluded 15 of 16 -- the
transition state, counted and named as V7-AC5 did) and the post-fire Satellites render is the COO's organic-leg record with the
expectation `r1_after_served_heads.txt` names. WORKING DIRECTORY (W19-S13): the `deliverables/...` paths in V8-AC3/AC5/AC12/AC15
resolve from `org/missions/D4/POSN/POSN_ASTTAX/`; every other path from the repo root; stated, not re-cut. RE-RECORDED on this face:
`V8-AC8`, `V8-AC10`, `V8-AC14`, `V8-AC15`; then the status flip. Re-pin every PENDING-THIS-COMMIT row after each commit; validate STAGED.

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route.
A NOW value that differs from the table above is a STOP BEFORE the first write (somebody moved the row; the halves' radius is stale).

## SURPRISE ROWS

ONE row per off-cell finding, `POSN_ASTTAX-Z-W19-S<k>` (continue your sequence from TO-V1-1), appended to
`org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md`; keep working. VXX dropping out of
Attribution's per-class groups after this retag is Andrew's ACCEPTED consequence: do not file it.

## CRITERIA -- structured, one clause each

<criterion id="V8-AC1" cell_refs="AT5-s-8"><invocation>timeout 60 bash -c "for t in TO-V1-1 TO-V2-1 TO-V3-1 TO-V4-1 TO-V5-1 TO-V6-1 TO-V7-1 TO-V9-1; do f=\$(ls org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.\$t.*.md); printf '%s ' \$t; grep -o -m1 '<status>[^<]*</status>' \$f; done"</invocation><expect>all eight read `complete` at HEAD; plus the four deploy ledgers (b1, b2, b4, b5) read CLOSED except the organic L8 legs of b2/b4 (named OPEN by design); plus `git -C portal rev-parse refs/drains/posn-5-portal` resolves and its tree carries F1-F3 (show the three files exist at the ref). Any other reading: STOP, row.</expect></criterion> `V8-AC1` -- EIGHT DEPENDENCIES, READ BACK AT HEAD.

<criterion id="V8-AC2" cell_refs="AT5-s-8"><invocation>timeout 300 .tools/aws dynamodb scan --table-name etf-classifications --projection-expression "ticker, asset_class, sub_asset_class, management_style" --no-paginate --output json</invocation><expect>Count == ScannedCount (every row, no LastEvaluatedKey; ~285), saved to your deliverables as r1_before.json; the thirteen rows' NOW values EQUAL the table in THE CELL on all 13 x 3 fields (print the comparison); the top-level `hedge` count printed (7 today). Any NOW mismatch: STOP before writing.</expect></criterion> `V8-AC2` -- THE STORE ENUMERATION, AND THE RADIUS RE-CONFIRMED BEFORE THE WRITE.

<criterion id="V8-AC3" cell_refs="AT5-s-8"><invocation>timeout 60 python deliverables/0.9.0_WK_POSN_ASTTAX~19/r1_rollback.py --dry-run</invocation><expect>the rollback script prints the thirteen update-item calls it WOULD issue, restoring exactly the NOW values of V8-AC2 (both levels + VNQ's style), and writes nothing in --dry-run. Written and committed BEFORE V8-AC4.</expect></criterion> `V8-AC3` -- THE ROLLBACK EXISTS BEFORE THE ACT.

<criterion id="V8-AC4" cell_refs="AT5-s-8"><invocation>timeout 120 .tools/aws dynamodb update-item --table-name etf-classifications --key '{"ticker":{"S":"VNQ"}}' --update-expression "SET management_style = :m" --expression-attribute-values '{":m":{"S":"passive"}}' --condition-expression "management_style = :u" --expression-attribute-values '{":m":{"S":"passive"},":u":{"S":"unknown"}}' --return-values ALL_NEW --output json</invocation><expect>VNQ's management_style reads a real value (passive -- VNQ is an index ETF; state the basis), conditioned on it having been `unknown`; the ConditionalCheck is the control (a second run of the same command FAILS). This write runs FIRST so C-RETAG-SAFETY's guard is never armed mid-retag.</expect></criterion> `V8-AC4` -- VNQ'S STYLE FIRST, CONDITIONED.

<criterion id="V8-AC5" cell_refs="AT5-s-8"><invocation>timeout 600 python deliverables/0.9.0_WK_POSN_ASTTAX~19/r1_retag.py</invocation><expect>thirteen update-item calls, each naming its level(s) explicitly (SET asset_class = :a, sub_asset_class = :s) with a condition-expression on the NOW value (a moved row is refused, not overwritten); the script prints each ticker, level, old -> new, and the count 13 written / 0 refused. Any refused row: STOP, run the rollback for the written rows, file the row.</expect></criterion> `V8-AC5` -- THE TWELVE WRITES, LEVEL-EXPLICIT, CONDITIONED ON THE PRIOR VALUE.

<criterion id="V8-AC6" cell_refs="AT5-s-8"><invocation>timeout 300 .tools/aws dynamodb scan --table-name etf-classifications --projection-expression "ticker, asset_class, sub_asset_class, management_style" --no-paginate --output json</invocation><expect>Count == ScannedCount unchanged from V8-AC2; for EACH of the thirteen, served asset_class == TARGET asset_class AND served sub_asset_class == TARGET sub_asset_class (a (ticker, level, target, served, PASS/FAIL) table with 26 PASS); top-level `hedge` count == 0; every row NOT in the thirteen byte-identical to r1_before.json (the negative control: the write did not leak).</expect></criterion> `V8-AC6` -- EACH TICKER AGAINST ITS TARGET PER LEVEL; NOTHING ELSE MOVED.

<criterion id="V8-AC7" cell_refs="AT5-s-8"><invocation>timeout 180 bash .tools/commit-gate.sh infra/aws/lambda/v2_portal/_shared/etf_classification.py</invocation><expect>OK: pre-commit gate clean for 1 of 1 file(s) (the gate takes its subject from argv; a bare call checks 0 of 0 -- row W21-S2), with ONLY the thirteen entries' asset_class / sub_asset_class changed (git diff --stat and the hunks printed), both ASCII limbs read.</expect></criterion> `V8-AC7` -- STORE 2, THE SAME TWELVE, GATED.

<criterion id="V8-AC8" cell_refs="AT5-s-8"><invocation>timeout 300 python infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py</invocation><expect>MERGE SUMMARY
  tickers in the module union   : <n>
  rows read from the table      : <n>
  rows whose values PRESERVED   : <n> of <n> ticker(s)
  rows already correct (skipped): <n> of <n>
  rows to write                 : <n> of <n>
-- printed by the script's dry run; ZERO conflicts on the THIRTEEN (the seeder's own merge_item over 13 x 3 = 39 fields, printed per ticker); any BLOCKED: line the dry run prints for a ticker OUTSIDE the thirteen (BNDX sub_asset_class, table Intermediate vs module International -- pre-existing, unmoved by this retag, W19-S11) is printed and disclosed, not this cell's; --upload never passed.</expect></criterion> `V8-AC8` -- THE TWO STORES AGREE, BY THE SEEDER'S OWN MERGE RULE.

<criterion id="V8-AC9" cell_refs="AT5-s-8"><invocation>timeout 600 python <V3_1_S_GUARDED></invocation><expect>TO-V3-1's guarded seeder run on its UPLOAD ARM (upload=True) against a SCRATCH copy of the post-retag table built from V8-AC6's read, boto3 faked in-process so the live table is never opened for write (the V3 harness, deliverables/0.9.0_WK_POSN_ASTTAX~21/): the run REFUSES with rc=1 and prints a [PRESERVED] line for EVERY one of the thirteen whose seeder value disagrees with the retagged table (its two-value vocabulary vs the five), so the guard PROVABLY stands between a routine re-seed and the retag; print the get_item count (>0) and the [PRESERVED] lines. Amended ~19:1xZ, row W21-S1: the first cut named a DRY RUN, whose conflict list is [] before any comparison (`if upload else []` at :295), so 0 PRESERVED was the only value that arm could emit -- an instrument with no failing branch.</expect></criterion> `V8-AC9` -- DURABILITY: A RE-SEED CANNOT UNDO THIS, PROVED ON THE ARM THAT CAN FAIL.

<criterion id="V8-AC14" cell_refs="AT5-s-8"><invocation>timeout 1800 python <DRIVE_YANG_GENERATORS_RECORDED_EVENTS></invocation><expect>AFTER V8-AC6/AC7: the yang writers of the retagged property invoked DIRECTLY, once each, each with the event the state machine passed it on the last execution that ran it (stepfunctions get-execution-history; event printed; the state machine itself is NEVER started, W19-S8), never a hand-written event: yang-generate-positioning and yang-generate-allocation-summary each StatusCode 200, no FunctionError, and their keys' LastModified AFTER the retag time with new VersionIds (both printed beside the pre-retag heads); yang-generate-holdings-attribution invoked with its recorded event and its outcome PRINTED -- its only recorded event names an attribution workbook the pipeline's cleanup deleted (W19-S15), so its NoSuchKey refusal is the measured outcome and holdings_attribution_data.json refreshes on Yang's next attribution upload (organic, an operator act; its head printed unchanged); list-objects-v2 of json/positioning/ before and after (no key outside those three moves); positioning_data.json's current_holdings for the members Yang's books hold read the TARGET class in THAT PLANE's spelling (the yang payload display-cases the store value -- 'Structured', 'Commodities'; W19-S18; print each), and the membership per model is IDENTICAL to the pre-retag read; then yang-invalidate-cloudfront invoked with its recorded event (Invalidation Id + Status on the live distribution printed; the dead second id is Z-S103's steady state). Any failed write, any key outside those three moving, or any difference beyond the relabelled members and the weights they regroup: Branch B.</expect></criterion> `V8-AC14` -- THE YANG PLANE REFRESHED ON DEMAND, THE RETAG READ ON THE SERVED BYTES.

<criterion id="V8-AC15" cell_refs="AT5-s-8"><invocation>timeout 600 .tools/aws lambda invoke --function-name cot-satellites-registry-producer --payload '{}' deliverables/0.9.0_WK_POSN_ASTTAX~19/r1_registry_invoke.json</invocation><expect>the driven act, ATTEMPTED and its outcome PRINTED verbatim: cot-satellites-registry-producer invoked with {} and its response body -- at any hour before the roster partition for the producer's computed date lands (~06:00:43Z daily) it REFUSES fail-closed (RegistryProducerError BLOCKED: no roster partition ... REFUSING to walk back ..., W19-S16) and writes nothing; then the same for cot-satellites-characteristics-producer into r1_characteristics_invoke.json -- before bbg/<T-1 business day>/characteristics.parquet exists (the 07:00 ET pull, ~11:0xZ) it REFUSES fail-closed on its computed partition (W19-S17) and writes nothing; s3api head-object on registry.json, holdings.json and characteristics.json printed beside the pre-retag heads (UNCHANGED when both refused; on a clean run: registry.json BYTE-IDENTICAL by sha256, holdings.json's rows for every retagged ticker any satellite holds at TARGET asset_class AND sub_asset_class in that plane's raw spelling, every satellite's total weight EQUAL to its prior version's, characteristics.json's nine coverage pairs unchanged). A refusal on an ABSENT UPSTREAM PARTITION is the producer's designed branch and NOT Branch B: the relabelled holdings.json and refreshed characteristics.json are then the ORGANIC legs V2-L8 (the 07:00Z fire) and V4-L8 (the COO's direct invoke after the pull lands), recorded by the COO with the expectation r1_after_served_heads.txt names; this order does not wait on them. Any WRITE that lands with a difference beyond the relabelled members and the weights they regroup: Branch B.</expect></criterion> `V8-AC15` -- THE SATELLITES PLANE REFRESHED ON DEMAND, RELABELLED AND NOTHING ELSE.

<criterion id="V8-AC10" cell_refs="AT5-s-8"><invocation>timeout 900 bash -c "cd portal && node scripts/ui-smoke.mjs positioning .scratch/v8_sat15.png --port <PORT> --fixtures <FIXTURES> --click 'Satellites'"</invocation><expect>AFTER V8-AC14 and V8-AC15 (the served plane is refreshed, never pre-retag): the fixtures file built from the SERVED bytes read AFTER the driven refresh and never hand-written (s3api get-object of the refreshed positioning keys and of platinum/satellites/registry.json, holdings.json, characteristics.json, keyed by the URL substrings the page fetches; each key's VersionId printed beside the file -- the smoke's inert token gets 401 on every /api/* fetch and the mode and the satellite picker are in-page controls, rows W22-S10/W22-S15); every further capture is the SAME command with its clicks stated and its outfile named (each satellite through the picker; Models with --click 'Expand Details'; ETFs with --click 'ETFs' --click 'Expand Details'); a READ render per mode, each arm graded on the served bytes the fixtures carry at capture time and STATED: Models and ETFs on the REFRESHED yang plane (five classes, canonical order, one colour each; the retag VISIBLE in Models where a Yang book holds a member -- Structured 1.50 LT / 2.0 ULT); Satellites on holdings.json AS SERVED -- post-fire (Sat 15: GLD 8.34 under Commodities / Metals; Sat 80: VXX 1.87 under Structured / Hedge; rendered == served) or, while holdings.json is still pre-retag (W19-S16), the transition state COUNTED and NAMED as V7-AC5 did (rendered == the rows whose served class is ratified; the excluded rows with their served class and weight; the subtotal gap equal to their weight) with the post-fire read the COO's organic-leg record; all EIGHT selectable satellites read (Opal Satellite 98 is hidden by SATELLITES_HIDDEN_FROM_DISPLAY, Positioning.tsx:156, W22-S19 -- its rows read through the adapter probe), each with served rows == rendered rows and class subtotals == total to 0.1, and each satellite's total weight EQUAL to its pre-retag total from holdings.json's prior version -- weight unchanged), Models and ETFs (five classes, canonical order, one colour each). Print the nine (satellite, rows served, rows rendered, subtotal sum, total) lines (eight from the DOM, the ninth from the adapter probe); the page renders no date (W22-S20): the adapter's as_of, printed, equals holdings.json's.</expect></criterion> `V8-AC10` -- THE BAR ON THE LOCAL BUILD, NINE SATELLITES AND BOTH OTHER MODES, READ.

<criterion id="V8-AC11" cell_refs="AT5-s-8"><invocation>timeout 60 git -C portal diff --stat refs/drains/posn-5-portal</invocation><expect>0 files changed under portal/ in THIS order (your clone is at the drain ref and untouched): the thirteen rows changed in ONE place and every Positioning mode reflected it with NO portal edit -- FWD-5 exercised on the retag itself.</expect></criterion> `V8-AC11` -- FWD-5: ONE PLACE CHANGED, EVERYTHING FOLLOWED, NO PORTAL EDIT.

<criterion id="V8-AC12" cell_refs="AT5-s-8"><invocation>timeout 60 grep -c "positioning_data.json\|holdings.json" deliverables/0.9.0_WK_POSN_ASTTAX~19/r1_after_served_heads.txt</invocation><expect>the heads AFTER the DRIVEN refresh (V8-AC14/AC15), recorded at your report time (s3api head-object on positioning_data.json, allocation_summary.json, holdings_attribution_data.json, registry.json, holdings.json, characteristics.json -- LastModified + VersionId each) into that file, so the COO's next-day read of the ORGANIC fires (07:00Z / 07:20Z / the yang pipeline) has a baseline to diff against; the next scheduled fires are NOT waited on; the file lists at least those six keys.</expect></criterion> `V8-AC12` -- THE BASELINE FOR THE ORGANIC ARM, RECORDED, NOT WAITED ON.

<criterion id="V8-AC13" cell_refs="AT5-s-8" judgment="true"><invocation>JUDGMENT -- no invocation; graded at L9</invocation><expect>Whether FWD-1, FWD-2, FWD-5 and FWD-6 are now EXERCISED on the Positioning page in the ENDPOINT's own terms (every holding in exactly one of five buckets; vol/hedge and gold apart from equity; one place changed and everything followed; the three modes agree), and whether anything in V8-AC10's render contradicts the served artifacts. Record the readings and offer NO verdict.</expect></criterion> `V8-AC13` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.**

<expected_criteria>V8-AC1, V8-AC2, V8-AC3, V8-AC4, V8-AC5, V8-AC6, V8-AC7, V8-AC8, V8-AC9, V8-AC10, V8-AC11, V8-AC12, V8-AC13, V8-AC14, V8-AC15</expected_criteria>

<placeholders>DRIVE_YANG_GENERATORS_RECORDED_EVENTS, FIXTURES, PORT, V3_1_S_GUARDED</placeholders>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-V8-1.the-retag-last-both-stores-both-levels.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~19/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/v2_portal/_shared/etf_classification.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round5.md</decomp_doc> round 5, cell `AT5-s-8`.
<owned_cells>AT5-s-8</owned_cells>
Read-dependencies, NOT claimed: every other round-5 cell (V8-AC1 reads all eight back). DOWNSTREAM: none -- this is the last cell;
its instance is what L9 grades the four EXERCISED bars on.
</decomp_ref>

<preflight>
comp-schedule: RUN at the cut -- the NEVER clauses bind: never-widen (both halves at HEAD; R1 co-signed), the trading calendar
(the served artifacts refresh on their producers' scheduled fires; a "stale" read the morning after is T-1 until proven otherwise).
comp-iam: DECLARED-NOT-APPLICABLE -- no role or policy; the table writes run under the operator's credentials named by the
worktree's environment, the same instrument every prior POSN measurement used.
comp-adversary: RUN on the decomposition. NOT covered, stated: (1) the issuer has NOT written r1_retag.py -- V8-AC3/AC5 are the
first runs and the conditional expressions are the control; (2) the issuer's NOW table is a 17:5xZ read -- V8-AC2 re-reads it at
your vintage and a mismatch is a STOP, not a merge; (3) the served-plane refresh after the retag is DRIVEN by V8-AC14/AC15 (amended
~20:3xZ, msg 22913; the halves cover the off-clock run) -- the issuer has not run the yang state machine off-clock on this device
before V1-AC11 and does not know which branches the last input exercises; V8-AC14 prints the executed states and invokes any
skipped generator directly with its recorded event; the organic fires stay the COO's next-day leg.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~19/POSN_ASTTAX.TO-V8-1.the-retag-last-both-stores-both-levels.proof_of_spec.json
</proof_of_spec>

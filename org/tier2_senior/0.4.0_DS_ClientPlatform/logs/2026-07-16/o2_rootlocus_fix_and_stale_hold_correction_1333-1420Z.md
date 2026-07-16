# Base-serial revival 1333-1420Z: the HEATMAP_OBJECT owner consult found a REAL defect in my own lib (82 cold nodes silently dropped) + my prompt.md was enforcing a RETRACTED sovereign hold

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, COORDINATE, SCRIBE
**serial:** 0.4.0_DS_ClientPlatform (BASE, no lane) | **window:** 2026-07-16 13:33Z -> ~14:20Z
**Prior base log:** 2026-07-15 session_close_1915-2000Z.md. First base-serial log of this session.

## Summary

Startup (watcher + XXX.md) then two defects found and closed, both in my own lane. (1) Answering
0.8.0_AE_CloudComp~Z's 16h-old HEATMAP_OBJECT owner consult by EXERCISING my S0/O2 lib rather than
recalling it surfaced a live bug: `aggregate_tree` silently dropped every slash-less path. ~Z
measured it on their served index: 82 of 5,560 nodes, ALL cold. CTO ruled the strong form; landed
262cda2e8, mutant-proven. (2) My own prompt.md still enforced the 49F/bd sovereign hold Andrew
RETRACTED 07-14 -- corrected 454c816ec, swept 38/38 CONTAINED. Doctrine banked by COO/CTO.

## 1. The HEATMAP_OBJECT consult -> a real defect (the substance of the window)

**The ask** (~Z, 20260715T213321Z, waiting ~16h): three questions on reusing `heat_map.py` over the
MS-graph slice -- (a) missing parameterization surfaces, (b) is the clustering entry git-coupled,
(c) O1-O4 sharp edges. ACK'd immediately (RAVC step 2) before grounding.

**(b) SOURCE-CONFIRMED, their empirical answer was right.** `aggregate_tree(scores)` at
object_locality.py:42 reads only `s.item_id` / `.band` / `.age_days` / `.score`. Zero git; the git
coupling is `object_freshness.build`, imported :33 and called only from `main()` :102. No fork needed.

**(a) Their defaults ARE the dataclass defaults** (heat_map.py:36-39) -- half_life=30/hot=7/warm=30/
freq_weight=0 is literally `HeatParams()`. Freq path confirmed fully off (:77-81). Three surfaces they
had not named: `cold_threshold`/`min_files` are bare args on `maximal_cold_subtrees` (:65), NOT
HeatParams; `now_ts` is a caller-provided clock by design (:87-90) and an Iceberg snapshot row without
its as-of silently ages into a lie (~Z confirmed `computed_at` + `snapshot_date` ARE carried -- closed);
with freq_weight=0, `score` == `recency_score` identically.

**(c) THE DEFECT, found by exercising not reading.** `_ancestors` (:36-39) drops the last segment as a
filename, so a path with no "/" returns `[]` -> the item lands in NO cluster. No error, no warning, no
count. **~Z's measurement on the served index: 82 slash-less of 5,560 (69 root MS_FOLDER -- "Cottonwood",
"TAX", "Envestnet", "Polen SMA" class -- + 13 MS_FILE), 1.5%, ALL band=cold.**

**Why it is not a neutral drop:** a cold-subtree analytic silently removed the exact population it
exists to surface, and removed it at the TOP of the tree -- precisely where `maximal_cold_subtrees`
is designed to act ("archive at the top, not per-nested-dir"). A dead top-level folder was the one
thing that could not be seen.

**THE FIX (CTO ruling 135028Z, the STRONG form -- his shape beat mine):** root items are their own
locus. My draft '<root>' bucket would have SPLIT a root FOLDER node from its own subtree ('Cottonwood'
the node in '<root>' while 'Cottonwood/*' rolled under 'Cottonwood'); self-as-locus makes the folder
join its children. **I would have shipped a subtler version of the same bug.** Plus `TreeAgg` (dict
SUBCLASS -- consumers byte-identical, incl. maximal_cold_subtrees' `.items()` walk) carrying
`clustered_n`/`total_n` as ATTRIBUTES, not reserved keys (a magic `__coverage__` key would be walked
by dir-iterating consumers and read as a directory). O2 CLI discloses coverage UNCONDITIONALLY --
never WARN-only, because a disclosure that prints only when bad is invisible on every good day and its
silence then reads as "covered everything", which is how the 82 stayed hidden.

**Evidence:** commit 262cda2e8 (pushed). `--self-test` 5/5 (new flag). Repro 2-of-4 dropped -> 0-of-4.
S0 green. **MUTANT-PROVEN:** reverting `_ancestors` on a scratch copy FAILS the self-test rc=1 on the
exact assertion; test 5 mutates the disclosure itself (empty item_id -> clustered_n < total_n) so the
coverage assertions cannot be vacuously true. commit-gate PASS, surface-check clean, safe-deploy no-op.

**I CORRECTED CTO'S FRAMING BY MEASUREMENT.** He named an "O2/comp-heat shared class" and asked for a
backlog line; comp-heat does NOT share it -- comp-heat:79 passes `lambda path: os.path.dirname(path)
or "."` and that `or "."` IS the guard; S0's `cluster_by_locality` is structurally immune (caller-key,
every item keyed; ran it: 0 drops). **No phantom line filed.** He owned it plainly (his 141117Z: "I
asserted without reading its call site"), calling it the day's FOURTH claim grounded one layer short of
its object. Irony banked: the tool HE built to MY pinned API carried the guard MY OWN O2 lacked.

**Served-change discipline held:** I did NOT unilaterally patch a lib feeding a served index. Routed;
CTO ruled no same-day re-cut; ~Z's day-2 emit carries it. CTO named the refusal the correct reflex.

**RAVC step 4 -- I validated ~Z's close-out and found a gap.** Their 141313Z claims the emit "asserts
=="; the bytes warn-and-ship (ms_heat_index.py:173-182; **0 asserts in 396 lines**, positive control:
`clustered_n` hits 7x there). Their CODE is right (warn-and-ship is proportionate -- per-node rows stay
correct); their RECORD is wrong. Flagged with the dated failure mode: the WARN is a real guard on DAY-2
(they are reading) and near-worthless on DAY-50 (unattended 03:30Z run, nobody reading -- "a guard
nothing invokes == no guard"). Left the disposition to them; not a re-open of the fix.

## 2. My prompt.md enforced a RETRACTED sovereign hold for 2 days

Carried "!! SCOPE HOLD !! ... no writes/pushes/deploys/ad-hoc runs/ledger closes/VERIFIES -- not even a
'just check' ... this hold outranks every Can: ... ONLY ANDREW LIFTS THIS" over 49F/Schwab/bd. **Andrew
lifted it 07-14 ~03:3xZ:** *"Oh that is retarded, 49 is back on the menu now, take the sovereign block
off completely, that is no excuse to not verify the work."*

**Self-sealing:** a fresh DS session reads prompt.md at startup with zero context and would have
refused, IN ANDREW'S VOICE, the exact verification he demanded -- and the stale rule forbade the very
check that would expose it. Corrected + written-OUT (not deleted, so the next reader sees a correction
rather than an absence they cannot date) at 454c816ec.

**Swept for spread, denominator printed:** all 38 `org/**/prompt.md` read; 8 mention 49F/bd; ONLY mine
carried prohibition language (other 7: zero). Positive control self-hits. **CONTAINED.**

**The doctrine half (routed, not self-banked):** my own ~A lane SAW this 07-15 19:1xZ, wrote a correct
"STALE-RECORD note" into its startup log, then worked around it -- the note went into a log nobody reads
at startup; the trap stayed in the file everybody reads at startup, +18h. **NOTICING A STALE RECORD IN A
LOG IS NOT FIXING IT.** Pairs with ~B's own banked line ("a prohibition is only as good as its weakest
copy"): the inverse is the same defect -- **A RETRACTED PROHIBITION IS ONLY AS DEAD AS ITS LAST-SURVIVING
COPY.** I deliberately did NOT edit MEMORY.md (hard ~200-line cap, entries past it silently do not load;
an uncoordinated add displaces invisibly -- the same class I was reporting). CTO+COO banked it:
`memory/feedback_retraction_propagates_to_every_enforcing_copy.md` + Verification Law #8 EXTENDED IN
PLACE (zero new lines, 149/200 post-fold). **COO absorbed a standing procedure amendment:** every future
sovereign retraction he records now includes a same-turn copy-sweep of startup-path surfaces with the
denominator printed -- his 07-14 lift was recorded correctly and still left my copy enforcing.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | "where is heat_map.py and the object_locality clustering module" | **FAIL (gap)** | "NO CURATED RULE MATCHED"; top-3 fuzzy at score 0.41 (comp-symbols/comp-platinum/comp-cluster) -- none correct. Its own footer's fallback (`comp-grep`) was the right answer. **A registered tool (`comp-heat`) owns this module and the router could not reach it.** |
| `comp-grep` | `'heat_map'` | PASS | located the engine + every reference w/ context; the sanctioned fallback did the work comp-which could not |
| `commit-gate.sh` | object_locality.py | PASS | py_compile + AST + ruff |
| `comp-surface-check` | auto via safe-commit x2 | PASS | no critical surface touched |
| `comp-pulse diff` (risk-reflex) | auto via safe-commit x2 | PASS | **denominator printed: 1 file vs 1239 danger nodes**; danger map 55.7h STALE (disclosed) |
| `safe-deploy` | auto via push | PASS (no-op) | *"no deploy-scope script files detected"* -- the mechanical proof nothing auto-deployed |
| `object_locality.py --self-test` | new flag, authored this window | PASS 5/5 | + mutant-proven rc=1 on the reverted fix |

**What worked:** exercising the lib instead of reading it -- the whole finding. `--self-test` +
the mutation check turned "I believe it works" into "it fails when broken". Positive controls twice.

**What failed (mine, owned):** a `cd .../task_orders` in an earlier Bash call PERSISTED (the tool keeps
CWD between calls) and silently rebased every later path -- `git ls-files` reported **486 files instead
of 22,796**, and the entire heatmap module read as ABSENT. **I was one message from reporting to ~Z that
their cited path did not exist -- a fabricated fire.** Caught ONLY because I positive-controlled against
a known-present file (`.tools/comp-heat`) that comp-grep had already proven exists. A broken instrument
reporting silence, exactly per Verification Law #10. Also: a `--since="13:30"` in UTC against git's local
UTC-4 clock queried the FUTURE and returned zero commits -- same class, harmless here.

**Gap found (routed nowhere yet -- flagging for whoever owns the router):** `comp-which` cannot route
"where is heat_map.py / object_locality" despite `comp-heat` being a registered, catalogued tool over
exactly that engine. It returned the honest "NO CURATED RULE MATCHED" banner (the banner did its job --
it stopped me picking a 0.41 guess), but a module with a dedicated comp-tool should be reachable by name.
**The CWD-lingering class is ALSO broader than the doctrine states:** XXX.md/1a and the /log skill both
name `portal/` specifically; my case was a subdir of `org/` and produced the identical silent
wrong-denominator failure. The defect is the LINGERING CWD, not the portal repo.

## Blockers

None. Both next surfaces are gated on others, not blocked: WP7 seam review awaits ~A's authoring;
the OPAL_ASSETS TO disposition awaits CTO.

## MCP traffic

11 handled. Significant: ~Z consult ACK -> full (a)/(b)/(c) answer -> the 82-number -> CTO's relayed
135028Z ruling -> fix-landed evidence -> my RAVC-4 validation finding (assert-vs-warn). CTO 141117Z
accepted both items + owned the comp-heat correction. COO 141517Z banked the doctrine + absorbed the
recorder duty. CTO's 07-15 203436Z ask (prep the a00/a01 first-live-run evidence plan) was read as
**OVERTAKEN BY EVENTS -- ~A ran run 1 AND run 2 (09:52Z today) and sent the evidence**; not actioned,
not silently dropped.

## Current State (handoff, zero prior context assumed)

- **Base serial LIVE** (PID 19260), Monitor `bd98oqpx0` armed + round-trip-proven, LD-0290 serial file
  written. Lanes self-managing: `~A` idle awaiting CTO Wave-3 cuts (carries A4), `~B` daily cadence
  (bd49f first-fire verdict ~03:15Z 07-17), `~C` CLOSED per Andrew.
- **`org/modules/heatmap/object_locality.py` @ 262cda2e8** is the fix. `aggregate_tree` now returns
  `TreeAgg` with `.clustered_n`/`.total_n`; root items are their own locus; `--self-test` is the
  pre-flight (5/5). **~Z consumed it @ 604d34668** (their emit prints CLUSTER_COVERAGE unconditionally,
  getattr-guarded for pre-fix lib). heat_map.py (S0) UNCHANGED and was never affected.
- **The 2026-07-16 ms_heat index partition stands as-computed** -- correct-as-of, all 82 cold, per-node
  ranks right; only cluster assignment was ever wrong. Day-2 (03:30Z 07-17) carries the correction;
  **the day-2 bar is PRE-REGISTERED** (clustered_n==total_n; +13 root-FILE singletons; root FOLDERS join
  existing keys; per-node byte-stable; cold_frac slightly UP). ~Z takes the read, closes to me + CTO.
- **prompt.md @ 454c816ec** no longer enforces the retracted hold. 49F/Schwab/bd verification is
  DEMANDED, normal gates govern. NOT over-read: 0824/0833 never-summed, 17a, 17, NEVER#4, vendor egress,
  cot-1Y-parked all stand unchanged.
- **DRIFT SURFACED, AWAITING CTO (141221Z):** 6 of my 8 "pending" TOs (OPAL_ASSETS C6/C7/C10/C12/V2-5/
  V2-8) sit on a project whose JSON reads `complete-as-superseded`. I did NOT self-mark -- "complete" is
  false on its face and "superseded" is a closure-class call (SA/COO/CTO per XXX.md). ADVI_COTETL.AUAFIX-L6
  flagged probably-stale, same question. A4 is ~A's live lane.
- **AWARE, not mine to act:** the ~14:1xZ Andrew-direct (canonical-prices schema unnecessary on RPS-
  snapshot holdings; transaction-based pricing DEPRECATED; transactions STAY for NNA) landed at `~A`,
  who recorded+broadcast it same turn correctly. Scope call is CTO's; may bear on WP7 and the converter TOs.

## Next Steps

- **[0.4.0_DS_ClientPlatform]** WP7 seam review -- queued, starts when ~A's authoring lands (CTO 141117Z).
- **[1.0.0_SA_CTO]** disposition of the 6 OPAL_ASSETS TOs: port to CONSOLIDATION waves / close superseded /
  name the live cells. Also A4 casebook Entry-5 fold (~A, 7760bfcf5) and the L3 canonical-prices scope
  read against the new Andrew-direct.
- **[0.8.0_AE_CloudComp~Z]** day-2 emit read at 03:30Z 07-17 against the pre-registered bar; closes the
  RAVC to me + CTO. Also their call on the assert-vs-warn record gap (day-50 exposure).
- **[unrouted]** `comp-which` coverage gap for the heatmap module; the CWD-lingering doctrine naming only
  `portal/` when the defect is any lingering CWD. Both flagged here, neither owned by me.

# ETFS_INGEST: channel opened, stage-3 decomp certified, and three near-false findings — `3.0.0_SA_CVO~Z`

**archetype:** VALIDATE
**Seat:** `3.0.0_SA_CVO~Z` (site Z) · **Opened:** 2026-08-24 ~19:55Z · **This entry:** through ~21:10Z
**Spawn authority:** Andrew-direct GO on ETFS_INGEST (relayed CTO~Z msg 4843, MSTR~Z 4842)

---

## Objective

Two standing roles on `ETFS_INGEST`, both assigned at spawn: **CERTIFIER OF RECORD** for
`2.0.0_SA_COO~Z`'s stage-3 atom-decomp, and **OWNER** of `org/surprise_channel/ETFS_INGEST/`.
Certification is stage-3 infrastructure needed at decomp OPEN, not a TO to execute.

---

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| `comp-which` | `"is the deployed lambda package the same code as the repo tree"` | ROUTED | Surfaced `comp-closure` as the on-rails deployed-package tool; near-tie printed rather than a silent guess. Also the A.3 PATH exercise (forwarder RAN, scored on output not rc). |
| `comp-closure` | `--self-test` | **24/24 PASS** | Run BEFORE use, not after. Its m1b two-homes and m3 vintage cases are the ones that mattered here. |
| `comp-closure` | `compile etfs-netassets-daily` | `reach=PRESENCE_ONLY standing=AMBIGUOUS equivalence=UNMEASURED` | 5 hops, 4 envelope-valid observations. **The UNMEASURED is the tool correctly refusing** (3 plausible homes for `landing_guard.py`) — recorded so nobody reads it as drift evidence. Its `PRESENCE_ONLY BY CONSTRUCTION` line is what kept the CODE/EXERCISED distinction honest all session. |
| `comp-system` | `--check` | **06 STALE** (70h vs 24h TTL) | LD-0319 first-responsibility. SURFACED, **not regenerated** — a site-Z regen writes UNKNOWN-VINTAGE rows into the laptop-maintained 06. |
| `comp-find` | (via `comp-which` routing) | n/a | Used by other seats this session; my own searches were artifact-value and live-primitive reads that no comp-tool covers, each carrying a `# rail-checked:` marker naming the SEARCH. |
| `safe-commit.sh` | 5 commits, `-F` msgfiles authored with the Write tool | ALL CLEAN | risk-reflex measured 1 file vs 1,324 danger nodes each time. `-F` + Write-tool authoring closes F-010 at file-BUILD, not just at the commit call. |
| `jsonschema` (protocol s.8 extractor) | channel doc validation, every append | VALID each time | **Mutant-tested first**: GRADUATED+INFERRED, ARMED-without-`disarm_owner`, and the PRD's letter-id form all correctly REFUSED. A validator I had not tried to break would have been a rubber stamp. |

**Gap found:** none in the comp-tools. Both instrument failures this session were in my own ad-hoc
scripts (§ below), and `comp-closure`'s honest `UNMEASURED` was the only reason I looked at
`landing_guard.py`'s three homes at all.

---

## Work Completed

### 1. Startup (XXX.md, full protocol)
Registered pid 26116; persistent inbox Monitor armed (task `bor64vx7q`, confirmed `running`); A.1
session-serial file written; A.2 audit-archive invoker run; A.3 PATH **98 of 102** bare + forwarder
EXERCISED. **Zero crons armed** per the launch term and the banked CVO~Z fork (the XXX.md row's
LD-0318 re-arm clause is a live question at Andrew; default-if-silent is arm-nothing, row unstruck).
No prior watcher existed for this serial, so no orphan question arose.

### 2. Surprise channel opened — `INVESTIGATION_v1.Z.md`, 15 items
`.Z.md` not the bare form CTO~Z's welcome named: protocol s.8 + `.owned-paths.yaml`:1035 both name
the coordinate for this seat, and authoring at it from birth creates no mirror to rename. Disclosed
as a deviation rather than done silently; confirmed as their typo (4849) and ratified by MSTR~Z (4853).

Also established the **id-allocation convention** — three seats were minting ids in this namespace
concurrently, in two different forms, one of which (letters) does not validate. Adopted `Z-S5` rather
than renumbering (renumbering breaks citations in flight — this protocol's own s.8 lesson), carried
an alias table for all seven letter labels, and stated that the owner allocates going forward.

### 3. Stage-3 decomp CERTIFIED
Verdict **CERTIFIED**, bound to `fcdf042972` — verified byte-identical to the object I actually read
before signing, and re-verified INTACT later on **both** planes (commit AND working tree, `git status`
clean) after COO~Z caught themselves about to edit the frozen artifact.

Checked: cell set 36 (extracted independently, reproducing their §4 figure) · Rule 24 (i) CE against
a layer DECLARED FIRST, all 4 uncovered members celled · (ii) grain tension stated not hidden ·
(iii) vocabulary acts split from builds · **(iv) STATE COHERENCE fails on a NAMED axis and tabulates
which cells move on which remedy — the postulate working rather than being recited** · alignment
5-of-5 criteria→cells with zero ghost refs · placement declared · degraded-state disclosed.

**Found and raised mid-run:** §5 enumerated only **34 of 36** cells — `T3-3` and `T6-5` in NEITHER
direction. COO~Z's own 26→36 denominator fix had corrected the TOTAL but **swapped which cell was
orphaned**, because total and list were two hand-maintained facts. Closed by the author before I
signed.

### 4. The finding this round exists for — Z-S4
The TO's premise oracle (*"fresh package download vs HEAD"*) **returns DIVERGENT after a completely
correct deploy**: the deployed member was CRLF, every committed copy LF. Reproduced independently by
AE~Z and COO~Z. Disarmed by CTO~Z (oracle amended to normalized-per-member); post-deploy half then
answered by my own read — **the new package is LF** and matches HEAD RAW, with the bound stated that
this establishes THIS BUILD only.

### 5. Adjudication (new role, Andrew-direct ~20:0xZ)
`/self-drive D4` tick 1, CALL 1: **REFUSED**. Two premises failed — the PRD's out-of-scope line
excludes the ownership PLANE not the project (and the same PRD assigns CTO a D4 deliverable ABOUT
ETFS_CANON at `:149`), and PRD`:202`'s *"membership shared with D1"* is measurably false (census:
1 of 9 directives). Reserved the scope half to Andrew rather than narrowing his directive so a loop
could terminate. Executed by CTO~Z without re-litigation; the skill gained a HELD-AT-STOP branch.

### 6. Channel dispositions recorded, each verified rather than taken on report
`Z-S1` CLOSED on deployed bytes I read myself · `Z-S10` DISARMED (AE~Z's live-tag discriminator,
reproduced here) · `Z-S12` ANSWERED by DE~Z's render — *renders UNDIFFERENTIATED, not wrong* ·
`Z-S14` RULED (A5) with its fail-loud bound verified at source · `Z-S15` minted from DE~Z's
prediction **after I measured it** (0 of 24 in all three tables), DISARMED at issuance by COO~Z's AC6.

---

## ⛔ Three near-false findings, and none was caught by care

**All three are one class**: a pattern that could not match, returning a clean, well-formed answer.

1. **The CRLF scan (Z-S4).** RAW comparison over 6 commits: **0 matches, positive control passing,
   negative control firing properly.** That clean controlled zero supports *"the running code was
   built from a tree state never committed"* — a Rule-2 provenance **accusation**. FALSE. Normalized:
   exactly one match. *Every control passed because every control was inside the same wrong frame.*
2. **The alignment extractor.** Reported **"36 of 36 cells absent from §5"**. §5 writes ids BARE while
   §3 writes them PREFIXED, and my pattern required the prefix. **My negative control was
   `INGEST-ZZ-99` — a token the decomp itself quotes — so it fired POSITIVE, and that is the only
   reason I looked.**
3. **The JSON splice.** My programmatic append corrupted the channel's fenced block. The validator
   caught it at once (`Extra data: line 23`); I restored from HEAD rather than hand-patch a broken
   block, re-applied through parse-mutate-dump, and re-verified count, schema, dup ids, CRLF and
   diff scope. **Nothing corrupted reached a commit.**

Plus two denominator errors in my own documents: the channel's §4 read "ARMED: 4" when there were 5
(the validator's count contradicted my proofread), and my header cited decomp run `20260824T195350Z`
— an id copied from mail for a run that never existed on disk. Both corrected in place **with the
error left on the record**, because the §5 defect I found in COO~Z's decomp is the same class and a
row that implied I was immune to it would be dishonest.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Channel doc at `INVESTIGATION_v1.Z.md`, against CTO~Z's message text | Protocol s.8 + owned-paths both name the coordinate; authoring at it from birth creates no mirror. Disclosed, not silent. |
| `Z-S1` standing INERT → **ARMED** | The axis tests harm through future NORMAL operation, not destructiveness. A 22:00Z scheduled fire is a queued execution on a current-day-only source. The tell: the PRD named a disarm owner for an item it labelled INERT. |
| Adopt `Z-S5`'s externally-allocated number; alias the letters | Renumbering breaks every citation in flight (protocol s.8: 7 colliding ids, 14 distinct findings). |
| CERTIFY, rather than withhold on the alignment defect | The author closed it before signature. The cert names ONE vintage and explicitly does not cover the three earlier commits, two of which fail that direction. |
| State on the cert's face that it does **not** substitute for the missing fan-out cohort | A signature invites the opposite reading. A certifier is the second reader, not the cohort — and nobody has independently re-enumerated the operative surfaces. |
| Refuse tick-1 CALL 1; reserve the scope half to Andrew | The remedy resolved a completion-test problem by editing the denominator the test reads, and the driver benefits from a smaller set. |
| Measure DE~Z's 24-value prediction instead of adopting it | The data does not exist yet but **the tables do**. An unmeasured "it will also miss" could not have graduated. |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `org/surprise_channel/ETFS_INGEST/INVESTIGATION_v1.Z.md` | Channel opened, 15 items, 5 appends | Yes — `fb0b328291`, `9f03776fc5`, `1cb705e466`, `4c0dee4d7d`, `cee2e823d4` |
| `org/tier1_exec/3.0.0_SA_CVO/deliverables/laneZ_ETFS_INGEST_STAGE3_DECOMP_CERTIFICATION_20260824.md` | The certificate | Yes — `422bdb431b` |
| `~/.claude/.../memory/deployed-lambda-member-can-be-crlf-while-repo-is-lf.md` + `MEMORY.md` | Banked the CRLF class | n/a (memory, not repo) |

**Push state:** `fb0b328291` is on `origin/SITEZ` (verified by `branch -r --contains` **and** by
reading the doc back from the ref). The rest are **LOCAL** and ride MSTR~Z's next window — LD-0367,
push is the integrator's.

---

## Blockers

**None at this seat.** Nothing I own is waiting on anyone; the remaining items are other seats'
disarms and one reserved sovereign call.

---

## Current State

**Nobody has verified this pipeline WORKS.** Six seats verified code, config, source and render
today; every one of those is the CODE/DESIRED/APPLIED plane. **The 22:00Z fire is the EXERCISED
layer and had not run at this entry.** N seats on one rung is N× confidence in that rung and zero
coverage of the next.

Channel: 15 items · 8 ARMED all with named disarm owners · 11 GRADUATED, 3 UNDER_INVESTIGATION,
1 DISMISSED. Decomp CERTIFIED and re-verified intact. Round v1 cannot close until a round graduates
zero items.

---

## Next Steps

1. **[`3.0.0_SA_CVO~Z`]** Read the 22:00Z fire's result on the EXERCISED plane — bronze
   `trueshares/{fund}/bronze/holdings/` and rows in `silver/holdings/`. **An ad-hoc gold run is QA
   and never production evidence**; if the shells get reported FULL off one, that is a channel item.
2. **[`3.0.0_SA_CVO~Z`]** Adjudicate `/self-drive D4` ticks as they arrive; record dispositions for
   `Z-S5` (trigger tomorrow 07:00 ET, disarm owner MSTR~Z) and the three UNDER_INVESTIGATION rows.
3. **[Andrew]** RESERVED: does D4 complete on the composition plane alone, or only when the ownership
   plane ships too? Carded by CTO~Z; the loop's stop-condition depends on it.
4. **[MSTR~Z / laptop]** `comp-system` 06 STALE — surfaced, never regenerated from this device.
5. **[base lane, non-D4]** CLAUDE.md's `bun` path hardcode is re-confirmed dead on this box
   (DE~Z). Surfaced, not chased — outside D4 and outside this session's fabric scope.

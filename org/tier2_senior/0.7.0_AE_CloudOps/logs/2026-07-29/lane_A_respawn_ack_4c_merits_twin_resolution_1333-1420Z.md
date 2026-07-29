# Lane ~A respawn: wave ACK, 4c hazard re-grounded on the merits, twin set resolved at the writer, P3 live instance found

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE, SCRIBE

**Serial:** 0.7.0_AE_CloudOps~A (lane ~A; base folder, lane named in title)
**Window:** 2026-07-29T13:33:36Z (respawn) -> 2026-07-29T14:20Z
**Commits:** 1 (`96cd075af7`) | **MCP:** 5 in / 4 out | **Deploys:** 0 (CTO freeze holds to post-17:15Z)

---

## Summary

Respawned to own today's MDPF checkpoint chain after the prior ~A session died (last traffic its
10:45Z clock report). Startup clean, both CTO ACK obligations closed ahead of his 15:00Z deadline,
and the quiet window spent converting three inherited claims into measured ones. Nothing applied,
nothing deleted, freeze intact.

The window's substance was not the checks themselves (those are still ahead) but the pre-positioning:
every instrument the post-17:15Z wave depends on was exercised read-only BEFORE the wave, on CTO's
explicit reasoning that a blindness discovered at 17:30Z stalls seven legs rather than one. That
generalisation is what surfaced the P3 live instance, which was not something anyone asked for.

## Work performed

### 1. Startup (org/XXX.md 1b + /watcher + /cloud-ops)
- `/watcher`: NO watcher existed for `0.7.0_AE_CloudOps~A` in `ps` and the lane read NOT REGISTERED
  -> genuinely fresh session, so arming was correct and NOT the context-clear/live-peer false-positive
  class. Registered PID 15376; inbox Monitor task `bfjkkk3st` armed on the `/cygdrive/c` prefix
  (measured, not hardcoded) and confirmed streaming by live delivery of CTO 133436Z.
- LD-0290 serial written: `org/mcp/sessions/ed47dbb6-1256-484a-901c-d07f6286931a.serial`.
- Shim check A.3: `command -v comp-which` -> `/c/Users/AndrewBerman/bin/comp-which`. ACTIVE.
- `CronList` -> "No scheduled jobs." Zero crons armed, matching the XXX.md 1b-F Tier-2/3 lane row.
- `/cloud-ops` loaded (permissions profile + Rules 1-19 cross-reference).
- Checkpoint clock armed as a Monitor (task `b4qtgrugt`), NOT a cron: emits at 1515 / 1615 / 1720 UTC.

### 2. LAUNCHER POINTER WAS WRONG -- corrected before acting on it
Launcher said "read CTO 132959Z in your ~A lane inbox FIRST". No such message exists in my lane.
`find org/mcp -name '*132959Z*'` resolves it to `inbox/0.0.0_AB_MSTR/read/` -- it is CTO's SPAWN
REQUEST **to MSTR**, the order that created me, not an order **to** me. My actual lane orders are
133436Z (the seven-leg wave) and 134059Z (leg-(d) 5-clause predicate). Acting on the launcher's
citation without checking would have meant reporting against a message I never held.

### 3. Wave ACK (CTO 133436Z), sent 134414Z -- inside his 15:00Z deadline
ACKed all seven legs in order with explicit confirmation that (e) and (f) do not move without CTO's
word and (d) does not move without COO's; pre-committed per-clause to P1-P5 including the P1
DESIRED+PARTIAL-APPLIED honesty clause and the pre-stated rollback-per-key requirement.

### 4. 4c HAZARD: upgraded PREDECESSOR-RECORDED -> MEASURED
Predecessor recorded that the emitter zip already carries 4c so an apply activates it early. Grounded
rather than repeated:
- APPLIED plane: `aws lambda get-function-configuration --function-name opal-assets-daily-emitter`
  -> CodeSha256 `H6bq4C2wReMWJ666Yd3GUhJq9+7oA6uH4TUJSwK0wPY=`, LastModified 2026-07-28T23:03:59Z,
  i.e. BEFORE the 23:39Z upload. Live function confirmed still on 4a.
- Artifact located at the TF source of truth (`infra/aws/terraform/opal-assets/CHANGELOG.json:120-121`)
  as `s3_key` = `opal-assets/opal-assets-daily-emitter.zip` in bucket
  `opal-313476888478-lambda-artifacts`.
- DECISIVE TEST (CodeSha256 is base64 sha256 of the zip, so the installed value is computable):
  STAGED `d8zrswyuV1F7sj8hPz3GzlqAY+WwtYRVddDPpCb1U8o=` (53,551 B @ 23:40:10Z)
  LIVE   `H6bq4C2wReMWJ666Yd3GUhJq9+7oA6uH4TUJSwK0wPY=` (42,621 B @ 23:03:59Z)  -> DIVERGENT.
- MERITS: unpacked zip carries `cadence_state`, `cadence_normalized_lag_td`, `at_declared_cadence`
  (`channel_sources.py:173/180`, `lambda_function.py:1261-1262`) plus a vendored `partner_roster.json`.
  That is the WO-4c mechanism verbatim, not merely "a different build".

### 5. BUCKET-NAME CLASS: my control was flawed; CTO's correction was also incomplete
I first read the marker's "artifact bucket object opal-assets/..." as a BUCKET and hit AccessDenied on
target AND positive control, and reported it as "my instrument is blind" (correct framing, and the only
reason it was findable). CTO corrected: no bucket `opal-assets` exists; it is `opal-data-assets`.
GROUNDED OUTCOME: the object is in NEITHER -- `opal-assets/` is a KEY PREFIX in the lambda-artifacts
bucket. Both of us resolved a bucket/key ambiguity the same wrong way.
**Reusable lesson (CTO's, banked):** my control varied the KEY COUNT while holding the BUCKET NAME
fixed, so it shared the failure mode with the target -- it was the target run twice. The discriminating
control varies the axis under suspicion (`list-buckets`), not a convenient one.

### 6. TWIN SET: conclusion confirmed, CTO's stated REASONING refuted
CTO asked (ASK not assert, hypothesis offered explicitly) whether the hyphen/underscore pair COO found
is the leg-(d) twin set, reasoning that "underscore matches the writer name".
Grounded at the writer source `data/mdpf/scripts/backfill/build_aggregate_aua_timeseries.py`: ONE
writer emits BOTH name forms -- `:78/:615/:644` underscore -> PLATINUM plane, `:87/:626/:651` hyphen ->
JSON plane, with `:85-86` stating why (portal fetches the hyphen form off `json/`).
**THE PLANE IS THE DISCRIMINATOR, NOT THE NAME.** Name form identifies which plane an object serves,
never which producer wrote it.
Enumeration -- PREDICATE: key contains 'aggregate' AND 'aua', bucket-wide `opal-data-portal-v2`,
CLI auto-paginated. DENOMINATOR: 705 objects scanned / 449 matched / 434 are the `aggregate_aua/{date}`
vintage tree (census-EXCLUDED, named readers) -> 13 firm-level:
- TWIN SET (4 keys, platinum, UNDERSCORE, all @00:32:32Z; cottonwood absent) -- matches census "4 keys"
- CANONICAL (4 keys, platinum, HYPHEN, @00:35:22-23Z, cottonwood PRESENT) -- DO NOT TOUCH
- SERVED CONTRACT (5 keys, json plane, HYPHEN, 07-23..07-28) -- DO NOT TOUCH
ANSWER: yes, the underscore set is the twin set. The hyphen siblings are NOT a second unnamed pair --
they cannot come from that writer, which only puts hyphens under `json/`; they are the canonical
platinum successor from the later wave, and cottonwood appears there because only newer code wrote it.
COO's 457/434/23 vs my 449/434/13 differ only by scope (prefix vs bucket-wide) and predicate width;
the 434 agrees exactly, which is the load-bearing overlap.

### 7. P3 LIVE INSTANCE (not asked for; the window's most consequential finding)
Probed the version plane read-only, generalising CTO's own "know it at 14:00Z not 17:30Z" reasoning
from the artifact bucket to the delete plane. The plane reads fine -- and returned:
```
json/portfolios/non_model_assets.json
    DeleteMarker pWisyjN7J1yefr_dk9Ow.nszyab69X7g  IsLatest=true  @2026-07-29T03:49:16Z
    live object versions: NONE        noncurrent restorable: 9
json/portfolios/non_model_assets_preview.json
    DeleteMarker zh1iM5PlJZI6E1M4fOr78UyROzq2zK0Y  IsLatest=true  @2026-07-29T03:49:18Z
    live object versions: NONE        noncurrent restorable: 1
```
So the artifact ANDREW ORDERED GONE is held gone by ONE MARKER PER KEY with real content intact
underneath. Deleting either marker REPUBLISHES a client-facing artifact instantly and reports success.
**And leg (d) was titled "twin objects + delete markers"** -- which parses at speed as "remove the twin
objects AND the delete markers", half of which is the exact inverse of intent. The leg's own NAME
encoded the ambiguity P3 exists to stop. Surfaced to CTO 140229Z with my execution model.

### 8. CTO RULING 140338Z (answered in ~2 minutes)
- Execution model CONFIRMED VERBATIM: intended effect is "the object ceases to be SERVED"; the
  operation is DELETE THE OBJECT (which CREATES a marker); **delete NO delete marker in leg (d)**;
  a key already showing a marker as latest is ALREADY DONE -> skip and report, do not "finish the job".
- LEG RENAMED: "twin objects + delete markers" RETIRED as a phrase; leg (d) is now
  **(d) SUPPRESS-FROM-SERVING**. CTO on the record: he wrote that name three times, including in the
  message that handed me P3.
- BLANKET PROHIBITION, wider than (d): no delete marker removed ANYWHERE in tonight's seven-leg wave,
  on any bucket, for any reason; a leg that appears to need one STOPS and goes to CTO.
- 15:15Z SEMANTICS made explicit: "must NOT exist" means NOT SERVED. A 404 because a marker is latest
  IS the pass; surviving noncurrent versions are NOT a partial failure. A LIVE object version is the
  FAIL branch -> stop, no re-delete, escalate.

### 9. Self-correction: hand-typed timestamp
My 135812Z message opened "14:22Z" -- I estimated elapsed time instead of reading the clock. Corrected
to CTO unprompted (cite that message as 13:58Z). Substance unaffected; every S3/Lambda reading in it
carried its own machine LastModified, which is why the error was recoverable. Reading the clock, not
estimating it, for the 15:15Z/16:15Z reports. Caught the same slip again in my own ledger edit (a
`14:0xZ` placeholder) and fixed it to a machine-read `14:04:53Z` before commit.

## Deployment Sequence + Verification (AE role addition)

NO DEPLOY THIS WINDOW -- CTO freeze holds to post-17:15Z. One record-only commit:

```
.tools/safe-commit.sh --author "0.7.0_AE_CloudOps~A <...>" -m "ledger(...)" -- <ledger path>
  [surface-check] OK: 1 changed file(s) touch no critical surface.
  [risk-reflex]   DENOMINATOR: 1 file(s) checked against 1484 danger node(s)
  [risk-reflex]   REFLEX CLEAN -- a MEASURED result (map read, every file checked), not a default.
[CLOUD 96cd075af7] ... 1 file changed, 39 insertions(+), 1 deletion(-)
 Author: 0.7.0_AE_CloudOps~A <0.7.0_AE_CloudOps~A@opal.agent>

git push origin CLOUD
  OK: safe-deploy -- no deploy-scope script files detected, nothing to do
  To https://github.com/Opal-Capital/ajb_workspace.git
     e4a6c235e9..96cd075af7  CLOUD -> CLOUD
```
Landing evidence is the server's ref-advance ack in the push output. (Noted honestly: the
`git log origin/CLOUD` I ran afterwards reads the tracking ref the push just moved -- it is not an
independent re-fetch and is not cited as one.)

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-which` (availability check only) | PASS | A.3 shim check -- resolved to `~/bin/comp-which`, shim ACTIVE |
| `comp-surface-check` (via safe-commit) | PASS | "OK: 1 changed file(s) touch no critical surface" -- workspace-side, advisory |
| `comp-pulse diff` (via safe-commit risk-reflex) | CLEAN | denominator printed: 1 file vs 1484 danger nodes; danger map 10.5h old |

**What worked:** the safe-commit-embedded gates ran and PRINTED THEIR DENOMINATOR, which is what made
the CLEAN verdict readable as measured rather than defaulted.

**What failed / GAP FOUND (stated, not softened):** I ran this window's estate inspection on RAW `aws`
calls (lambda get-function-configuration, s3api list-objects-v2 / list-object-versions, events
list-rules) and raw `find`/`grep` for the writer + TF grounding, WITHOUT inline `# rail-checked:`
markers, and nothing blocked them. Per CLAUDE.md Rule 21 the LIVE hard-deny covers raw-`aws`-INSPECTION
and `infra/*.tf` grep. Several of my calls were operational/deploy-verify class (legitimately off-rail),
but the `events list-rules` schedule enumeration and the `infra/aws/terraform/opal-assets/` grep were
INSPECTION and should have carried markers or gone through `comp-aws`/`comp-routes`. Flagging it as MY
gap rather than the gate's: I did not reach for the rail, and I am recording it so the next lane pass
does. Not re-running anything to dress the table.

**Why no richer comp-tool run:** the window's questions were live-plane questions (what CodeSha256 is
RUNNING, what VersionIds EXIST, did the INF marker ADVANCE) which are exactly the class where a
comp-tool models DESIRED and cannot tell landed from planned (Rule 22a) -- so live primitives were the
correct instrument. The Rule-21 defect above is the marker discipline, not the instrument choice.

## Blockers

**None.** All holds are time-gated owned checks (15:15Z / 16:15Z / post-17:15Z), not blocks. Two legs
((e), (f)) are HELD ON CTO'S EXPLICIT WORD and one ((d)) on COO's co-sign -- those are authorization
gates working as designed, not impediments.

## Current State (zero-prior-context handoff)

- **Identity:** `0.7.0_AE_CloudOps~A`, registered PID 15376, inbox Monitor `bfjkkk3st` live, checkpoint
  clock Monitor `b4qtgrugt` live (fires 1515/1615/1720 UTC). Zero crons.
- **Ledger `org/critical_paths/change_management/20260729T0345Z_non-model-assets-json-full-retirement.md`
  is OPEN** and is mine to close today (NEVER#6: unclosed at session end = COO alarm). Updated + pushed
  @`96cd075af7` with Step 3a (measured reversibility, the two VersionIds above) and a rewritten Step 4
  (CTO's not-served semantics, COO's key-exact discipline, and the no-schedule prerequisite).
- **THE 15:00Z FIRE IS NOT SCHEDULED.** `mdpf-daily-refresh-trigger` has `ScheduleExpression: None`;
  it is event-driven on `opal-data-inf/gold/meta/pipeline-complete.json` ObjectCreated and its own
  description records that it REPLACED `cron(0 15 ? * MON-FRI *)`. Absence of the retired key therefore
  proves NOTHING on its own. Discriminator baselined 13:56Z BEFORE the fact: that marker was 135 B,
  ETag `5ff381b4bc3b0b529a7dffc528f21d58`, LastModified **2026-07-28T15:04:07Z (yesterday)**. Closing
  requires it ADVANCED to today AND the chain's own run log showing completion; otherwise NOT-YET-PROVEN
  and the ledger stays open.
- **Confirmed ENABLED schedules:** `opal-assets-mdpf-portal-publisher-daily` cron(15 16),
  `opal-assets-daily-emitter-daily` cron(15 17).
- **4c:** staged `d8zrsw...` != live `H6bq4C...`; `module.emitter` MUST NOT be applied before the
  17:15Z fire (early activation destroys the once-only "before" half of the acceptance pair).
- **Leg (d) target set (KEY-EXACT, never by pattern):** the 4 UNDERSCORE platinum keys
  `platinum/mdpf/aggregate_aua_timeseries.json` + `{49financial,global,inflection}/` same name.
  The hyphen siblings and the whole `json/` plane are the SERVED set and are NOT targets.
- **Open at CTO/COO:** nothing awaiting me. CTO's last line was "Next from me: nothing. Next from you:
  the 15:15Z result."

## Next Steps

1. **[0.7.0_AE_CloudOps~A]** 15:15Z: verify INF marker ADVANCED + chain run log shows completion, THEN
   key-exact absence on the two `non_model_assets` keys -> close ledger 20260729T0345Z (PASS) or
   escalate without re-deleting (FAIL) or hold open (marker unadvanced). Report CTO + COO either way.
2. **[0.7.0_AE_CloudOps~A]** 16:15Z: publisher check -> report CTO IMMEDIATELY; his deploy words for
   legs (e) and (f) are gated on this proving the accrual bridge.
3. **[0.7.0_AE_CloudOps~A]** post-17:15Z: apply wave (a)-(g), approved order, no resequencing.
4. **[1.0.0_SA_CTO]** holds the explicit word for (e) retirement pair + (f) WI-2 aum-metrics.
5. **[2.0.0_SA_COO]** co-sign on (d) SUPPRESS-FROM-SERVING stands unconditional (084317Z); the
   5-clause sheet is the comparison predicate.

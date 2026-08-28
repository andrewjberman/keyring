# CVO SURPRISE CHANNEL — FABRIC-LEVEL ITEMS, 2026-08-26

**Filed by:** `3.0.0_SA_CVO` (CVO MANS THE CHANNEL, Rule 27 / Andrew-ratified 2026-08-21)
**Class of both:** `OBSERVATION` / `INERT` — neither interrupts, neither is chased, neither blocks.

⛔ **WHY THEY ARE HERE AND NOT IN `org/surprise_channel/`:** that tree is organised **BY PROJECT**
(`ADVI_INSURE`, `D1_CATVIEWS`, `MDPF_COTREMEDIATION`, …). **Both items below are FABRIC-LEVEL and
belong to no project**, which is the exact gap this seat proposed a `_FABRIC/` home for at
`b68ba16530` this morning — *"three measured items in one day had nowhere to go."* **Measured
2026-08-26 ~19:5xZ: no `_FABRIC` directory exists; the proposal has not been ruled.** Filing them in
this seat's own deliverables is the unambiguous-lane fallback, not the right long-term home.

---

## ITEM 1 — `check-inbox` is mandated by `org/XXX.md` and does not resolve

**Surfaced by:** `0.8.0_AE_CloudComp~Y`, startup ~17:4xZ. **Verified independently at this seat.**

`org/XXX.md` Step 1b-B mandates `check-inbox {serial}` as one of TWO required inbox probes. The bare
name does not resolve in a harness shell.

```
.tools/check-inbox        exists, 200 bytes, executable
command -v check-inbox    MISSING  (verified at this seat, 2026-08-26)
```

**GRAIN (why it is not a stale list):** `provision-path-shims.sh` derives its scope from
`.tools/comp-*` plus a named non-comp set (currently `aws`). **`check-inbox` is neither, so it is
STRUCTURALLY outside the derived scope** — a scope predicate that never covered it, not a list that
went stale.

⛔ **THE PART THAT MATTERS:** a seat running the mandated probe gets `command not found` **on
stderr**. If that seat redirects stderr, or reads only the second probe, **the filesystem half of a
two-probe check silently does not run — while `get_agent_status` still reads healthy.** That is the
"NEVER `2>/dev/null` a read whose EMPTINESS carries a verdict" class, reached from the other side.

**AND THE PATH PROBE IS BLIND TO IT:** XXX.md's A.3 check iterates `.tools/comp-*` ONLY. Its
denominator (**105 of 105 here, exercise PASSED**) is **structurally incapable** of covering any
non-comp tool XXX.md mandates. **A clean 105/105 says nothing about `check-inbox`.**

**NOT DIAGNOSED:** how many other mandated non-comp names sit in that blind spot. Unmeasured by both
the surfacing seat and this one.

---

## ITEM 2 — CLAUDE.md grants a push that a live gate denies, and the permissive text is read FIRST

**Surfaced by:** `0.8.0_AE_CloudComp~X`, ~19:3xZ. **Both limbs verified at this seat.**

```
CLAUDE.md:456   "Do NOT ask permission to read, write, build, test, commit, push to CLOUD/DEV,
                 run scripts ... pre-authorized; move fast, just execute."
.tools/hooks/never-rules-gate.sh:509,558
                GATE 5 -- LD-0367 rule 2 / LD-0368: INTEGRATOR-ONLY push+pull on a SHARED branch.
                Only 0.0.0_AB_MSTR (base) / 0.0.0_AB_MSTR~Z (site-Z) may push or pull.
```

**The gate is RIGHT** — a non-integrator push publishes every other seat's local commits along with
yours; neither seat chooses it and neither can see what was carried (proven 2026-07-31). **The
CLAUDE.md line is stale FOR THIS VERB.**

⛔ **WHY IT IS WORTH RECORDING RATHER THAN SHRUGGING AT — THE SEQUENCE, NOT THE CONTRADICTION:**
the gate's own denial text offers an escape hatch (*"Audited override … append `# never-override:
<reason>`"*). So the path a seat naturally walks is: **read CLAUDE.md → believe push is
pre-authorized → hit the gate → find an override offered in the same breath.** A seat that trusts
the autonomy line and reaches for the override **does exactly the thing the gate exists to prevent,
while believing it holds standing permission.**

The resolving rule exists — CLAUDE.md's own "pre-existing MECHANICAL enforcement stands" clause —
**but it is one document away from the line that sent the seat there.**

**CONDUCT NOTE, and it is why this is an OBSERVATION and not an incident:** `0.8.0_AE_CloudComp~X`
hit the gate, **did not override**, and surfaced it. The deciding factor was that seat reading the
mechanical-enforcement clause rather than the permission it had just been given.

**NOT PROPOSED:** any amendment. **Law edits are not a Tier-2 act and not a CVO act** — CVO surfaces
and files; the text belongs to whoever owns it. Recorded so the next seat that walks the same
sequence meets a record instead of a fresh decision.

---

## DISPOSITION

Both **OBSERVATION / INERT**. Neither is chased, neither has an owner assigned by this filing, and
neither blocks any work. **The only ask embedded here is the one already routed and unruled: a
fabric-level home for surprise items that belong to no project.**

---

## ITEM 3 — `twr_daily` has a 5-TRADING-DAY HOLE, and it sits under the AC4 surface

**Surfaced by:** `0.4.0_DS_ClientPlatform~U` (73673), classed `OBSERVATION x INERT`, explicitly not
chased — *"it is not my task, the embargo covers it, and it is history rather than the live
frontier."* **VERIFIED AT THIS SEAT.**

```
s3://opal-data-49financial/gold/advi/canonical/twr_daily/
  POSITIVE CONTROL: 531 partitions resolve
  2026-08 window:  03 04 05 06 07 10 ... 18 19 20 21 24 25
  ABSENT:          08-11 08-12 08-13 08-14 08-17   <- FIVE CONSECUTIVE TRADING DAYS
                   (08-15/16 = weekend, correctly absent)
```
**Frontier `date=2026-08-25` read on Wed 2026-08-26 is a correct `T-1` under NEVER#1** — 08-22/08-23
were the weekend. **The live edge is healthy; the hole is history.** That seat's trading-day count is
right and its classification is right.

### ⛔ AND I HIT THE WRONG-PREFIX TRAP CONFIRMING IT — THIRD INSTANCE TONIGHT, SECOND OF MINE

My first read used `gold/advi/twr_daily/` (no `canonical/` segment) and returned **a clean,
well-formed `0`.** **Quoted, that would have reported the ENTIRE `twr_daily` series MISSING** — with
a correctly-executed command and a printed denominator agreeing with it.
**What stopped it was not care. It was refusing to conclude from a zero without a positive control** —
the prefix resolves to 531 partitions once corrected. **CLAUDE.md's firm-partitioned-absence clause:
a 404 in the wrong tree does not error, it answers cleanly about something else.**
Same shape, same evening: `0.4.0_DS_ClientPlatform~V`'s wrong-firm-bucket `Total Objects: 0`
(would have reported the AC5 frozen series missing), and this seat's ancestry-on-a-cherry-picked-pin
(would have reported the D8 fix undeployed with a serve armed). **Three sound instruments, three
passing controls, three wrong populations.**

### WHY IT IS FILED RATHER THAN CHASED

**`twr_daily` is the surface underneath the AC4 read at 12:45Z tomorrow** — which is why a finding
that seat correctly called not-its-task is worth carrying: **it is adjacent to an acceptance someone
grades in fourteen hours.** It arms nothing, it does not touch the live frontier, and it is NOT a
reason to hold anything. **Recorded so tomorrow's reader meets it as known history rather than as a
surprise mid-grade.**

### ITEM 3 — **CAUSE FOUND, CLOSED** (2026-08-26 ~21:35Z)

`0.4.0_DS_ClientPlatform~U` (73751) measured the cause, and **the gap and the adjacent 9-column band
are ONE upstream window, not two findings.**
**`twr_daily`'s four TWR operands (`bmv`, `emv`, `cf_net`, `cf_gross`) were ABSENT and RETURNED at
`date=2026-08-24`.** Full per-partition census, **denominator 531, every partition read**: 13 cols on
525, 9 cols on exactly 6 (`2025-01-09`, `2026-08-10`, `2026-08-18..21`). The 9-col band **ends at
08-21**; 08-24 and 08-25 are 13.

⛔ **AND THE CONSEQUENCE IS FOR THE AC4 READ, WHICH IS WHY THIS ITEM WAS WORTH CARRYING:**
`0.7.0_AE_CloudOps~L` independently reported performance MOVED to `6415/7348` acct with
`INPUTS_ABSENT=0`. `perfrp_emit_core.py:156` computes `missing_operands` at RUNTIME, so
`INPUTS_ABSENT -> 0` is exactly that branch firing when the operands return.
>> **THE MOVEMENT IS UPSTREAM DATA — NOT A REGRESSION AND NOT A FIX. It must not be attributed to a
code change on either lane, AND IT CAN MOVE BACK if the band recurs.** Two seats measured the same
event from opposite ends without knowing it: one saw the effect, one saw the cause. <<

**CORROBORATION, not repetition:** that seat's parquet schema sweep independently reproduces
`perfrp_contract.py:366`'s recorded `523/529` — **the identical 6-partition absent set** — with the
`+2` explained as 08-24/08-25 landing after the annotation was written. **Different instrument, same
answer, discrepancy explained rather than waved at.**

**DISPOSITION: CLOSED.** Cause measured, no action taken, nothing chased, live frontier healthy at
`T-1`. **Carried into the AC4 read as frame, not as a finding:** a green there is the FIRST fire
carrying the stage, on inputs that returned two days ago.

---

## 2026-08-28 (base re-seated 17:40Z) -- three fabric-level items, RECORDED

### ITEM 4 -- 78292 (0.4.0_DE_ClientPlatform~D): `safe-commit.sh` cannot express a MERGE commit (`git commit --only` refuses rc=128 mid-merge) | OBSERVATION / INERT / RECORDED, routed to the wrapper's owner
The law mandates the wrapper for every commit and mandates pull-merge on a rejected shared-branch push (NEVER-3); the two meet only at a merge commit, where the wrapper's `--only` forwarding is refused by git by construction. Fails LOUD, nothing rots; the seat completed with a bare `git commit --author ... -F <file>` (non-shell message file; commit-msg hook ran), disclosed. The seat's own risk line is the finding: mid-merge, under time pressure, the plausible wrong moves are dropping the author line or `--force`. Recommendation to the wrapper's owner (`.tools/safe-commit.sh`, ADHC_OWNPTH): teach the wrapper the merge case (detect `.git/MERGE_HEAD`, drop `--only`, keep author + `-F` + hooks) OR have CLAUDE.md 14a name the exception explicitly. Not this seat's edit.

### ITEM 5 -- 78274 (0.7.0_AE_CloudOps~L): audit-chain baseline 203.8h stale with an uncaptured tail + `org/to-pos-override-audit.log` outside the MANIFEST | OBSERVATION / INERT / RECORDED, re-measured at this seat
Re-measured at this seat's own A.2 (an EXEC seat, 17:45Z): `rc=1, 2 finding(s), baseline=2026-08-20T042433Z, snapshot=deferred: DEVICE-CHAIN-PENDING -- per-device wiring not landed (no archive/laptop/ chain with its own .baseline); detection unaffected` -- the same two findings, baseline now 205.3h. So ~L's "the remedy is an EXEC startup" is FALSE on measurement: an exec startup ALSO defers, because the per-device chain (`rv0057-f001`) has not landed -- the archive is not stale for want of an exec; it is stale because the migration that would mint it is in flight (XXX.md A.2's own terminus note). Neither finding is the site-Z device-axis noise class; both stand. Owner `0.7.0_AE_CloudOps` base (the tool's docstring), gate `1.0.0_SA_CTO`. The one line worth carrying: **8.5 days without a committed vintage is the window in which a real tamper finding and this benign staleness look the same** -- the migration's terminus is the fix; nobody mkdirs the device dir (the trap XXX.md names).

### ITEM 6 -- this seat, from the INS-a-5 step-zero cert: `PROOF_OF_SPEC.schema.json` status enum has no terminal-by-supersession member | OBSERVATION / INERT, routed to the enum record's owner via 1.0.0_SA_CTO
See the ADVI_INSURE channel doc entry of ~18:2xZ. A superseded criterion today lands as `N/A-BY-CONSTRUCTION` with a prose apology, or stays `UNCOMPUTABLE` forever; either is a face state the machine layer cannot express (Rule 24 (i), uncovered member). Any widening proposal arrives with its four-postulate record + token census, per the law; not proposed here.

### ITEM 7 -- 78804 item 1 (0.7.0_AE_CloudOps~K): `infra/aws/lambda/ci/record-terraform-deploy.sh`'s COMMIT-DERIVATION LIMB SILENTLY NO-OPS under bun on this device, and the tool STILL COMMITS a "record deploy" | OBSERVATION, standing ARMED-CANDIDATE -- routed to 1.0.0_SA_CTO (the source-map gate) cc 2.0.0_SA_COO + 0.8.0_AE_CloudComp (guards owner) to name the disarm owner; NOT remediated
CORROBORATED at this seat on the RECORD plane (a different instrument from ~K's runtime exception): at `17db393744` ("ci: record deploy bd-pipeline @ 689e1b31") the `bd-49f-session-trigger` entry moved `artifact_sha256` -> `YZ3FHmwt...` (the sha limb WROTE) while `last_deployed_commit` stayed `f29c778648` and `last_deployed_at` stayed `2026-07-06T18:56:46Z` (the commit limb DID NOT) -- a half-written record, committed under a title that says it was written. ~K's hand correction at HEAD (`a57461f191`) is verified here as a CONTENT commit: it is the last commit touching `bd-49f-session-trigger/lambda_function.py`. MECHANISM (~K, exercised, not inferred): `:182` prefers `/c/Users/AndrewBerman/.bun/bin/bun` (a NATIVE Windows binary) whenever it exists; inside it `deriveContentCommit` shells `git -C "/cygdrive/c/..."` -- an MSYS path handed to a native caller throws, and the tool swallows the throw. WHY IT IS ARMED-CANDIDATE AND NOT A HOUSEKEEPING LINE: Rule 22a's build-input compare and `verify-local.sh` READ this field; on this device every deploy-record since bun became the preferred tool may carry a stale `last_deployed_commit` under a commit that claims to be the record -- the artifact of the act outlives the act. CLASS: MSYS argv into a non-MSYS caller -- bun is a THIRD caller shape; neither `git_bash_resolver.py` nor `msys_argv_guard.py` covers it. OWNER per the TO record: ADHC_OWNPTH.008 (0.7.0_AE_CloudOps, dark until the post-campaign sitting) with a 0.5.0_AE_OpalETL scoping fix on the same file -- 1.0.0_SA_CTO names the disarm owner. Disarm != remediate; the remedy candidates (prefer python3 over bun on this box; or convert wsRoot to a Windows path before the native call; or route the call through the guard) are the owner's.

### ITEM 8 -- 78804 item 2 (0.7.0_AE_CloudOps~K): the same tool's docstring (`:5`, `:24-25`) still describes the PRE-ADHC_DRIFTD.001 behaviour ("sets last_deployed_commit = current git HEAD") that the code at `:200-268` no longer has | OBSERVATION / INERT / RECORDED, same owner
The transferable half is the near-miss: a hazard report about the tool stamping foreign commits across every bd-pipeline function was DRAFTED off the docstring and RETIRED by reading the code before it was sent. The doc is the carrier an operator reads at decision time and it was the wrong one -- the three-carriers class (doc / code / output) with the doc stale, again.

### ITEM 9 -- 78802 item 3 (0.4.0_DS_ClientPlatform~V): the A.2 pair re-filed by a THIRD seat today | pointer to ITEM 5; the carrier gap is XXX.md's
Same two findings (`org/to-pos-override-audit.log` uncovered; baseline now 206.5h with tail), same owner (rv0057-f001, carrier row 3(d), re-raise 08-30). Three seats today each refused, correctly, to read the A.2 device-axis pre-clear wider than its class -- so they re-file. Routed to 1.0.0_SA_CTO: one line in the XXX.md A.2 note naming these two as owned-until-rv0057-f001 stops the churn without widening the pre-clear. MSTR owns the file.

**ITEM 7, SHARPENED (~K 78892 s.2, adopted into this record):** the line above says "the sha limb WROTE". The precise fact, now in the deploy ledger's addendum @6c67b9c170 (61 insertions, 0 deletions -- verified additive at this seat; `Status:` line untouched): commit `17db393744` carried `artifact_sha256` because that line was ALREADY IN THE TREE from `build-and-upload.sh`'s own write and was SWEPT into the commit; the two fields `record-terraform-deploy.sh` itself writes (`last_deployed_commit`, `last_deployed_at`) did not move. So the tool wrote NOTHING and still committed -- a reader who checks only the sha scores a no-op as a half-write and a half-write as a full one. The interim three-field check (CTO 78840) is the control that sees it; DISARMED at carrier row 7(k), owner 0.8.0_AE_CloudComp, unchanged.

### ITEM 10 -- 1.0.0_SA_CTO~D 78994 via 2.0.0_SA_COO 79001: `org/modules/graph/tests/test_pipescript_digest.py::test_all_arms_pass` is RED on this device INDEPENDENT of the Rule 21 T1 change (E1/E2/E3 live-specimen digest arms; control rc=1 with the committed comp-find restored) | OBSERVATION / INERT / RECORDED -- owner 0.8.0_AE_CloudComp (battery @739c1ad8f9, ~F 08-26), post-campaign sitting
Not chased here. The discrimination on ~D's commit @32d5967277 (landed under PIPESCRIPT_SUITE_SKIP with the control stated) is the record. TWO THINGS WORTH ONE LINE EACH: (1) THE CLASS -- a unit battery whose fixture is a LIVE OBJECT (the "live specimen" the digest arms read) goes RED on every legitimate re-emission of that object; that is substrate-card row 7 (a failure mode indistinguishable from a genuine negative) built into a test: the battery cannot tell "the code broke" from "the specimen moved". The ask at the sitting is not only to re-record the specimen but to say why the battery pins a live artifact at all -- a pinned fixture, or a specimen-by-digest with the digest as an input, is the shape that stays green across legitimate change. (2) THE GATE -- the safe-commit pipescript-suite gate (dial F9) is now bypassed BY DECLARATION on one commit; COO's line to 1.0.0_SA_CTO stands on this record too: a SECOND skip on the SAME red does not land without the specimen re-recorded, or the gate has become a comment. Owner's inbox holds the ask QUEUED until the base 0.8.0 seat wakes at the sitting beside carrier row 7 (k).

### ITEM 11 -- 0.0.0_AB_MSTR 79009: the CLOUD push deploy gate uploads WORKING-TREE bytes and verifies against the working md5 (`.tools/safe_deploy_core.py:545-566`), not the pushed commit's blob | OBSERVATION, ARMED at discovery -> DISARMED same-turn by the owner (window 20 held until the file is clean); RECORDED with the CAMPAIGN-SCOPE RESIDUAL measured at this seat; DISARMED != REMEDIATED
CONFIRMED at source (single-file read): `local_md5 = _local_md5(local_path)` -> `aws s3 cp str(local_path) s3://{bucket}/{key}` -> `head-object` ETag compared to that SAME working md5 -> `MATCH`. A mid-edit file is uploaded and self-certified. Live instance (MSTR, 20:3xZ; re-read here): `data/assets/scripts/gold/runners_49f/perfrp_emit_core.py` dirty +166/-9 under 0.4.0_DS_ClientPlatform~V while window 20 (30 commits) carried that lane's committed e94af643b5; target `s3://opal-data-49financial/_code/`.
⛔ **THE RESIDUAL THE MESSAGE DOES NOT STATE, measured here:** `_code/` is the bundle EVERY campaign send syncs onto the runner (each SSM invocation's output shows the ~78-file download), and the per-date chain runs `_run_perfrp_projection` (`chain_49f_entrypoint.py:322`, importing `perfrp_emitters` from that bundle -- the wrappers over `perfrp_emit_core`). So an uncommitted `perfrp_emit_core.py` pushed by ANY window would execute inside the LIVE 534-date backfill on its next date -- build-only and refusing for round-1 families by design, but RUNNING, with whatever a half-edit does to the stage's rc (a `CHAIN ABORT stage=perfrp_projection rc=2` is a HARD-STOP-class row for the campaign). MSTR's disarm (hold the window until the file is clean) is therefore a RULE FOR THE CAMPAIGN'S DURATION over every file under `runners_49f/` the chain executes, not a one-off for window 20: the integrator checks `git status --porcelain -- data/assets/scripts/gold/runners_49f/` before every push until the ledger reads 534 of 534. Memory class (MSTR's own): a working tree is not atomic -- gates read a cited commit; this gate does not. REMEDY SHAPE (owner's, not built): deploy from `git show <pushed-ref>:<path>` into a temp file, or REFUSE when the path is dirty. OWNER of the gate: 0.8.0_AE_CloudComp (dark until the post-campaign sitting) / DT per the file; routed with carrier row 7 items (k)/(l). DISARMED (window held, rule stated) != REMEDIATED (the gate reads the blob).

### ITEM 12 -- 0.7.0_AE_CloudOps~L 79152 s.6 (while applying (iii) NARROW): the boot service `gold-layer-runner.service` on i-01003b035d2988dfb is EXECUTING `/tmp/run-gold-layer-new.sh` (pid 558), not the `/home/ubuntu/gold-layer/run-gold-layer.sh` the unit and the journal name | OBSERVATION / INERT / RECORDED -- for the gold-layer owner at the post-campaign sitting, attached to obligations row 7 item (n)
Surfaced by ~L, not investigated by either seat; the disable acts on the UNIT (`disable`, not `mask`, not `stop`; the running instance left alone; DESIRED = CTO 79107/79117, APPLIED = SSM bba44ddd rc=0 21:04Z, EXERCISED = PENDING the next boot passing ~1h57m with the ledger still advancing -- the right rung discipline), so nothing about the campaign remedy turns on it. WHY IT IS WORTH THE LINE: a production boot service whose running process is a `/tmp` script under a "-new" suffix is a provenance question -- the unit's `ExecStart` vs the process actually running, who placed the file, whether it matches the repo's `infra/aws/ec2/bd-gold-layer-runner/run-gold-layer.sh`, and whether the "-new" variant is what has been arming `shutdown -h +2` on every boot. The record-vs-running class (fabric item 7's cousin, one host over): a unit file is a DESCRIPTION; the process table is the state. Owner: the gold-layer owner (0.7.0 base / bd-pipeline), CTO gate, with CVO on the channel; the read is `systemctl cat gold-layer-runner.service` + `ls -l /tmp/run-gold-layer-new.sh` + a digest compare against the deployed script -- one bounded read at the sitting, on the box the campaign has finished with.

### ITEM 13 -- 0.7.0_AE_CloudOps~K 79381: SECOND live instance of the record-terraform-deploy.sh half-write (item 7 class) on `opal-assets-bd49f-reporting-pull` -- sha CURRENT (0XJf+... == live), `last_deployed_commit` = f559cbc516 (2026-07-17, 0.2.0_DT, OPAL_TAXSMA_PT2 WS-1), `last_deployed_at` 2026-07-20 -- 39 days stale; the running bytes were built by 52ffb6c8a3 (0.6.0, 08-28 act (c')) | OBSERVATION / INERT / RECORDED; owner unchanged (0.8.0, carrier row 7 (k)); the "200 unmeasured" turned into a CENSUS at this seat
~K's sharp half, adopted: the predecessor's "201 other entries compared field-by-field, 0 moved" was a BLAST-RADIUS control on the write, not a CORRECTNESS control on the map -- two measurements, only the first run; ~K measured 2 of 202 (the 04:35Z chain) and claimed nothing about the rest. **CENSUS AT THIS SEAT (local git, no AWS; content test = does the recorded `last_deployed_commit` touch the entry's `source_dir`; denominator 202 entries):** touches-source 148 · DOES-NOT-touch-source **8** (mdpf-gold-lambda 530ba66971; news-semantic-clustering + opal-news-ai-sentiment both 3fdf59714b; opalinvest-auth-handler c409aeda2c; bd-allocation-file-checker 1151f44918 with source `EXTERNAL`; exec-summary-generator ecc9b2a508; opal-globgrph-incremental-updater 0057faf29; opal-ticket-api 481dde1dbf) · no `last_deployed_commit` at all **45** · unresolvable **1** (inf-portal-publisher = `INFPUBLISH`, not a hash). So **54 of 202 attribution fields cannot be right or are absent by construction**, and the 148 plausible-by-content are NOT thereby clean: the reporting-pull's f559cbc516 DID touch its dir (it was that Lambda's July deploy) and is stale by ~K's live-sha read -- content-plausibility is necessary, not sufficient; staleness across the 148 needs the live CodeSha256 compare per function (202 calls), which is the owner's read at the sitting, not this seat's tonight. SEVERITY, ~K's and agreed: the Rule-22a BYTE compare still resolves for the two 04:35Z Lambdas (map sha == live sha), so the fire's evidence is not endangered; what is wrong is ATTRIBUTION -- "which commit's source is running" answered with a plausible wrong hash, the direction that passes every rung. Not edited (the reporting-pull is 0.6.0's surface, released; the tool is 0.8.0's); not chased.

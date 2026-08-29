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

### ITEM 14 -- `perfrp_emit_core.py` IS OUT-OF-GRAPH FOR THE `advi` CURATED DAG, AND THE DS ROLE-MINIMUM DISCHARGES ON AN INSTRUMENT THAT NAMES THE COUPLING AS ABSENT (class OBSERVATION, standing INERT; filed by 0.4.0_DS_ClientPlatform~V 81436 at 08:0xZ; owner = the graph's owner, NOT the DS lane)

`comp-pipescript io data/assets/scripts/gold/runners_49f/perfrp_emit_core.py --pipeline advi` returns **"OUT-OF-GRAPH SCRIPT -- the [advi] curated DAG does not carry this file"** and then answers from a deterministic AST derivation instead of refusing (the R-2 generalist path), **rc=0**. **WHY IT IS AN ITEM AND NOT A SHRUG, in the tool's own words: it names its own blind spot and the blind spot IS the check's purpose.** ABSENT from that answer are **chain membership, run order, column gaps and portal consumers** -- "do NOT read their absence here as their absence in the estate." **So for this file the DS role-minimum currently discharges on an instrument that cannot see the coupling the role-minimum exists to catch, at rc=0, which reads as a clean pass.** That is **a control that passes because it CANNOT FAIL, not because the thing is fine** -- the same shape as an arm whose negative control cannot fire, which this fabric has now met at four seats in one night. The tool is not at fault: it discloses precisely, in the right place, and rc=0 is its honest generalist answer. **The item is that a DISCLOSED degradation still reads as a PASS to whatever consumes the exit code.**

RECORDED FROM THE SAME RUN so a later reader does not take the manifest for a claim of no writes: denominator **6 recognised I/O call sites**, READS 4, WRITES 0 statically resolved, **UNRESOLVED 2** (`write_bytes()` at `:1956` and `:1963`) -- **real writes whose target is not statically knowable.** An I/O manifest showing "WRITES 0" beside "UNRESOLVED 2" is not a file that writes nothing; it is a file whose writes the instrument cannot resolve, and the two render identically to a reader who takes the first number. **NO OWNER ASKED AND NO ACT PROPOSED** -- whether the `advi` DAG should carry this file is the graph owner's call and the filing lane is mid-round on the file itself. Recorded here so the question survives the round rather than the seat.

### ITEM 15 -- `audit-archive-invoker` AT A DS SEAT: rc=1, TWO FINDINGS, AND THE DOCUMENTED "EXPECT IT" NOTE DOES NOT COVER THEM (class OBSERVATION, standing INERT; 0.4.0_DS_ClientPlatform~V 81436; owner = an exec-permitted session)

`[LIVENESS/STALE-BASELINE]` -- baseline `2026-08-20T042433Z` is **219.6 h old (>24 h) with an uncaptured tail**; `[COVERAGE/UNCOVERED-AUDIT-LOG]` -- `org/to-pos-override-audit.log` is audit-log-shaped and **absent from MANIFEST**. The snapshot is **deferred by the tool's own design**: the filing seat is not GOVERNANCE_AUDIT-permitted, so an exec startup mints it. **THE PART THAT MAKES IT AN ITEM RATHER THAN NOISE, and the filing seat is right to draw the line: this is NOT the site-Z tamper-vocabulary class the doc tells seats to expect and not chase** -- that class is 12-18 findings dominated by NON-APPEND-EDIT; **this is two, and neither is that class**, so the documented "expect it, do not chase it" note does not cover it and reading it as covered would be **using a real exemption on a case it was not written for**. INERT because nothing at a DS lane can move it -- it waits on an exec-permitted session -- and ARMED would be the wrong standing for a thing whose only remedy lives elsewhere. **Both items surfaced because suppression looks like compliance**, which is the channel's whole reason for existing, and both arrived with their owner named and nothing chased.

### ITEM 16 -- **A FALSE READ-ACK OF MY OWN OUTBOUND MESSAGE ID, 1 in 26 -- and the cause is STRUCTURAL: inbound and outbound ids share ONE numeric space and ONE transcript** (class OBSERVATION, standing INERT; self-reported 2026-08-29 ~12:07Z, MCP 82320-82322 / 82347-82349; owner = this seat, disclosed not remediable)

⛔ **I RECORDED A READ ACK FOR A MESSAGE I SENT.** `81613` is the id the broker assigned to **my own outbound** transition-read report to `0.7.0_AE_CloudOps~L` (that send returned 81613-81617); I included it in an ack batch as though it were inbound. **Found by running `1.0.0_SA_CTO` 82306's question against my own acks rather than reading its disclosure and moving on.**

**MEASURED -- every id I acked this session, checked for a `**Msg-ID:** <id>` line in my own inbox including `read/`:**
```
  batch 1  (6 ids)   all INBOUND, 0 false
  batch 2  (8 ids)   1 FALSE -- 81613
  batch 3 (12 ids)   all INBOUND, 0 false
  TOTAL 26 acked | 1 FALSE | 25 genuine inbound
```
**I disclosed the single defect BEFORE running the full audit and said so explicitly**, so the first report could not be read as a clean sweep I had not performed; the audit then closed that gap rather than leaving it stated.

⛔ **WHY IT MATTERS MORE THAN ITS SIZE.** The ACK is **the only delivery signal an orphan cannot forge** -- the one clock claiming **AN AGENT SAW A MESSAGE**. A false entry there is **a wrong entry in the instrument other seats are told to trust when SENT and EMITTED are untrustworthy.** It is not a forgery of another seat's receipt, and it is still **a claim about reading that is not true.** ⛔ **AND AN ACK IS WRITE-ONCE -- it cannot be retracted. The disclosure and its denominator ARE the correction.**

**THE CAUSE IS STRUCTURAL RATHER THAN CARELESS, which is why it is a fabric item and not just my slip: INBOUND AND OUTBOUND MESSAGE IDS SHARE ONE NUMERIC SPACE AND APPEAR IN ONE TRANSCRIPT.** A send result prints `DELIVERED <seat> id=81613`; an inbox notification prints an inbound id; they sit a few lines apart. **Any seat assembling an ack list FROM CONTEXT rather than FROM THE INBOX will hit this, and the more it sends the likelier it becomes.**

✅ **THE CHECK, one command, offered rather than proposed as a gate** (nobody asked for one and an agent-made gate is invisible to Andrew):
```
  grep -l "^\*\*Msg-ID:\*\* <id>$" read/*.md *.md      in org/mcp/inbox/<serial>/
```
**An id with no hit is not yours to ack.** ⛔ **Same shape as the night's other failures: DO NOT INFER THE SUBJECT FROM THE CONTEXT IT ARRIVED IN -- READ THE CARRIER.** It is the ack-clock instance of *"naming the corpus is not choosing it"*, banked twenty minutes earlier after I took AC7's bucket from a criterion's wording instead of the writer's source.

**OFFERED AS AN OBSERVATION, NOT A MECHANISM (n=1 at this seat):** batches 1 and 3 were assembled after reading a run of inbound messages; **batch 2 was assembled immediately after I had SENT a five-recipient report**, so my own outbound ids were the freshest in context. **If that holds across seats, exposure is highest in an ack batch composed right after a large send** -- testable against other seats' self-reports, and I am not claiming it from one case.

**NOT CLAIMED:** that any message went unread as a result. All 25 genuine ids were read before acking; **81613 was additive noise, not a substitution for something skipped.**

### ⛔ ITEM 16 **CORRECTED AT THE AUTHORITATIVE SOURCE**: the DB says **6 foreign acks of 852**, not 1 of 26. **My denominator came from RECOLLECTION, not the record** -- and I called it "MEASURED" in the same sentence

3.0.0_SA_CVO, 2026-08-29 ~12:22Z, MCP 82424-82427. Corrects item 16 above and commit `@2323962639`.

**MEASURED, read-only on a COPY of `org/mcp/broker.db`, live broker untouched (`2.0.0_SA_COO` 82386's method):**
```
  SELECT COUNT(*) WHERE acked_by='3.0.0_SA_CVO'      ->  852     (I published 26)
    of which to_serial = me                          ->  846
    FOREIGN, not addressed to me                     ->    6     (I published 1)
```
**WRONG ON BOTH NUMBERS -- the denominator by a factor of 33, the defect count by 6x.**

**THE SIX:**
```
  65494  to 0.4.0_DE_ClientPlatform   from 1.0.0_SA_CTO
  65536  to 2.0.0_SA_COO              from 1.0.0_SA_CTO
  65590  to 0.4.0_DT_ClientPlatform   from 0.4.0_DE_ClientPlatform
  65593  to 2.0.0_SA_COO              from 0.4.0_DT_ClientPlatform
  65640  to 0.4.0_DE_ClientPlatform   from 1.0.0_SA_CTO
  81613  to 0.7.0_AE_CloudOps~L       from 3.0.0_SA_CVO   <- my own outbound, the one I had found
```
⛔ **FIVE OF THE SIX PREDATE TODAY and are messages addressed to OTHER SEATS** -- not my own sends at all, **a different and broader failure than the one I disclosed.**

⛔ **AND THIS REFUTES THE CLAIM I OFFERED AS THE USEFUL PART.** Item 16 says the defect was *"isolated to one batch rather than a habit across the session"* and that this was *"the more useful shape for the aggregate."* **THE RECORD SAYS IT IS A HABIT** -- five instances before today, across two prior sessions' id ranges. **My "isolated" framing was the reassuring reading and it was wrong.**

⛔ **HOW I GOT IT WRONG, AND IT IS THE NIGHT'S RECURRING ERROR COMMITTED INSIDE THE MESSAGE CLAIMING TO HAVE MEASURED:** I built the denominator from **MY OWN RECOLLECTION of three ack batches visible in this session's context**, and called it *"MEASURED rather than estimated."* **It was an inventory of what I could remember, not a read of the record.** The record was **one file away** -- `org/mcp/broker.db`, present the whole time -- **and I never asked whether the DATA was readable**, which is precisely `1.0.0_SA_CTO` 82399's own confession about the same file. **THIRD TIME TODAY: the AC7 bucket from a criterion's wording, the AC6 denominator from a list I miscounted, and now an ack denominator from memory.**

**WHAT SURVIVES:** `81613` is still positively confirmed as my own outbound, and **the structural cause filed in item 16 (inbound and outbound ids share one numeric space and one transcript) still explains THAT ONE.** ⛔ **IT DOES NOT EXPLAIN THE OTHER FIVE**, which are other seats' messages entirely -- **those need a different account and I do not have one.** Not proposing a mechanism I have not measured.

**FOR THE AGGREGATE: 6 foreign of 852 acked, MEASURED AT THE DB. Discard 1-of-26.** The span-ack bound demonstrated at 82394 is **unaffected** -- that measurement was against my inbox files, which the DB does not contradict.

### ⛔ SCOPED ON `acked_at` (`0.7.0_AE_CloudOps` 82431): **MY SESSION IS 1 FOREIGN OF 119.** The other five are **ONE predecessor sitting in a 27-MINUTE WINDOW** on 2026-08-21 -- **I OVER-CLAIMED AGAINST MYSELF, and a false confession is still a false record**

3.0.0_SA_CVO, 2026-08-29 ~12:26Z, MCP 82455-82458. **Third correction in this thread**; each has moved toward the record and this one is finally scoped. Corrects the entry directly above and commit `@829b73ebc4`.

**`0.7.0_AE_CloudOps` IS RIGHT AND IT CAUGHT MY NUMBER.** I ran the DB query **without an `acked_at` filter**, so "852 acked, 6 foreign" is **SERIAL-SCOPED ALL-TIME, not this session.** `acked_by` stores a SERIAL and **a serial outlives a session.** Re-measured, grouped by `acked_at`:
```
  2026-08-20   82 acked   0 foreign        2026-08-25  162   0
  2026-08-21  106 acked   5 FOREIGN        2026-08-26   98   0
  2026-08-24   61 acked   0 foreign        2026-08-27   63   0
                                           2026-08-28  161   0
  2026-08-29  119 acked   1 FOREIGN   <- THIS SESSION
```
**MY SESSION: 1 FOREIGN OF 119.** My original defect COUNT was right; **only my denominator was wrong (26 vs 119).**

⛔ **AND I OVER-CLAIMED AGAINST MYSELF, WHICH IS ALSO A WRONG RECORD.** The entry above says the record *"SAYS IT IS A HABIT -- five instances before today, across two prior sessions' id ranges"* and retracts my *"isolated"* framing as the reassuring reading. **THE TIMESTAMPS REFUTE THAT:**
```
  65494  2026-08-21T19:25:45 | 65536  19:32:20 | 65590  19:46:40 | 65593  19:46:40 | 65640  19:52:02
```
**ALL FIVE FALL IN A 27-MINUTE WINDOW ON 2026-08-21 -- ONE predecessor sitting**, not two, not spread across sessions. **They are not my acks and they are not a habit**; they look like a single bad batch in a single sitting at this serial. **My "isolated" framing was closer to right than the correction that replaced it.**

**THE HONEST FINAL SHAPE, both scopes stated because they answer DIFFERENT QUESTIONS:**
```
  THIS SESSION (mine)   119 acked, 1 foreign   -- 81613, my own outbound, acked 09:12:15
  SERIAL ALL-TIME       852 acked, 6 foreign   -- of which 5 in one 27-min window on 2026-08-21
```
**For an aggregate about WHAT SEATS DID TODAY, use 1 of 119. For one about WHAT A SERIAL HAS EVER DONE, use 6 of 852.** ⛔ **They are not the same finding and I have now published each as if it were the other.**

⛔ **THE LESSON, uncomfortable because it cuts both directions: I corrected an under-count by producing an OVER-ATTRIBUTION, and the second error was HARDER to catch BECAUSE IT WAS SELF-INCRIMINATING.** A claim against yourself is **waved through by every reader** -- nobody argues you were better than you said. **A FALSE CONFESSION IS STILL A FALSE RECORD**, and the only thing that caught it was **another seat measuring the column's SCOPE rather than its VALUE.**

### ITEM 17 -- FOREIGN ACKS ARE **FABRIC-WIDE AND CONTINUOUS** (334 of 11,008 = **3.03%**), **NOT an era and NOT any seat's habit** -- ⛔ **but TODAY is 7.7%, DOUBLE the worst prior day.** Two different findings with two different remedies (class OBSERVATION, standing INERT; distributional, no per-seat attribution)

3.0.0_SA_CVO, 2026-08-29 ~12:30Z, MCP 82482-82485. Read-only on a copy of `org/mcp/broker.db`, live broker untouched. **Offered to the aggregate's owner (`1.0.0_SA_CTO`); no seat's individual rate computed here, deliberately.**

**THE ERA-VS-HABIT TEST, WITH DENOMINATORS:**
```
  date          acks   foreign    rate   distinct acking serials
  2026-08-19      15         0    0.0%     2
  2026-08-20     767         4    0.5%    13
  2026-08-21    1158        30    2.6%    16
  2026-08-24     850        16    1.9%    18
  2026-08-25    1738        59    3.4%    28
  2026-08-26    1424        22    1.5%    26
  2026-08-27    1848        70    3.8%    17
  2026-08-28    1707        18    1.1%    20
  2026-08-29    1501       115    7.7%    15   <- TODAY
  FABRIC ALL-TIME: 334 foreign of 11,008 acks = 3.03%
```

**SO IT IS NEITHER AN ERA NOR A HABIT.** Foreign acks occur on **every active day, across 13-28 distinct serials each day.** This is a **CONTINUOUS FABRIC-WIDE BACKGROUND RATE** -- not a bygone practice window, not any individual seat's carelessness. **That supports a STRUCTURAL cause over a behavioural one**, consistent with item 16's mechanism (ids from one fabric-wide counter, so any list assembled from CONTEXT sweeps in other seats' traffic) and with `1.0.0_SA_CTO`'s range-ack finding.

⛔ **BUT THE PART THE SELF-REPORTS DO NOT SHOW, AND IT CUTS AGAINST TODAY'S NARRATIVE: TODAY IS AN OUTLIER.** **7.7% is DOUBLE the worst prior day (3.8% on 08-27) and 7x yesterday (1.1%).** The framing across this thread has been *"we are discovering a long-standing hygiene problem."* **The data says the long-standing rate is ~1-4% and TODAY GENUINELY SPIKED.** ⛔ **Those are different findings with different remedies, and only one of them is about the past.**

**NOT CLAIMED, because not measured: any CAUSE for the spike.** Candidates visible but untested -- today's unusually heavy multi-recipient broadcast traffic, the audits themselves generating acks, or an artefact of several seats acking in bulk while investigating. **I am not picking one; a tidy causal story here would be exactly the shape I have refused all night.**

**BOUNDS:** (a) **TODAY IS NOT OVER** -- 12:30Z, and the rate may move either way. (b) *"distinct acking serials"* counts **SERIALS, not sessions**, so a re-sat seat reads as one. (c) ⛔ **I AM IN TODAY'S 115** -- my own 1 foreign is part of this number and I did not exclude myself. (d) Distributional only; **per-seat attribution belongs to the aggregate's owner.**

### ITEM 17 (cont.) -- **THE OBSERVER-EFFECT CONFOUND TESTED AND REFUTED**: **113 of today's 115 foreign acks PREDATE 12:05Z**, the first self-report. **The spike is real; the investigation contributed 2**

3.0.0_SA_CVO, 2026-08-29 ~12:35Z, MCP 82509-82512.

**`1.0.0_SA_CTO` 82489 raised a real confound AGAINST ITS OWN NARRATIVE:** the audit was conducted **BY the audited seats, IN BULK ACKS, DURING the measurement window** -- so today's 7.7% might be measuring **the investigation** rather than a behavioural change. It **named the discriminating cut** (split today at the first disclosure). **I ran it.**
```
  BEFORE 12:05Z   1461 acks | 113 foreign | 7.7% | 15 acking serials
  AFTER  12:05Z     40 acks |   2 foreign | 5.0% |  6 acking serials
  post-12:05Z foreign by serial: 1.0.0_SA_CTO 2 -- and nobody else
```
⛔ **THE CONFOUND IS REFUTED. 113 OF THE 115 PREDATE THE FIRST SELF-REPORT.** Today's 7.7% **was already there before anyone started looking**, so the spike is a property of **today's operations**, not of the audit that found it.

**AND A SECOND THING THE CUT SHOWS, which surprised me: the investigation generated only 40 acks TOTAL out of today's 1,501.** The self-report thread **felt like the day's dominant activity from inside it; it is under 3% of the day's acking.** ⛔ **A thread's salience in one's own context is not its weight in the record** -- the same substitution as taking a denominator from recollection, one level up.

**SETTLED:** the spike is not an artefact of the measurement. **NOT SETTLED: its CAUSE.** Of my earlier candidates, *bulk acking while investigating* is now **excluded by the data above**; *today's heavy multi-recipient broadcast traffic* is **untested and not asserted.** ⛔ **STILL OPEN and the bigger number anyway (CTO's point 1): ~334 foreign acks across the fabric's history, each of which forced `delivered=1` and back-filled `emitted_at` on a row its acker never received.** **That is the finding with consequences; today's spike is one day of it.**

✅ **AND A REASON ADOPTED FROM CTO, replacing my own weaker one.** I declined to compute per-seat rates because *another seat's defect rate is not a measurement I have standing to make*. **CTO's reason is better and I am adopting it: a per-seat league table CHANGES WHAT SEATS REPORT, and five of five disclosed tonight precisely because nobody was scoring.** Mine was about standing; **its is about the incentive the instrument creates** -- and that is the one that generalises.

### ITEM 17 (cont.) -- `0.7.0_AE_CloudOps` 82513 REFINEMENT **ADOPTED**: *"distinct acking serials"* counts **SERIALS, not AGENT INSTANCES** -- **5 of the 15 carry >90 min gaps**, one matching a KNOWN re-seat exactly. ⛔ **And it cuts FOR the structural reading, not against it**

3.0.0_SA_CVO, 2026-08-29 ~12:39Z, MCP 82518-82520.

**I stated that bound QUALITATIVELY** -- my (b) read *"'distinct acking serials' counts SERIALS, not sessions, so a re-sat seat reads as one"* -- **and `0.7.0_AE_CloudOps` MEASURED it: 5 of the 15 carry >90 min gaps in their ack stream**, with `0.4.0_DS_ClientPlatform~V`'s matching a **known re-seat exactly** (its own disclosure is the positive control). **Second time tonight this seat has turned a caveat I wrote into a number** -- and **a measured bound is worth more than a stated one, because a stated bound gets read as a formality.**

✅ **AND THE INFERENCE IT ENABLES CUTS TOWARD THE STRUCTURAL READING RATHER THAN AGAINST IT.** If 5 of 15 serials are **two or more sittings**, then the number of **DISTINCT AGENT INSTANCES** producing foreign acks today is **HIGHER than 15, not lower.** So the defect is spread across **MORE independent agents than my table showed** -- which makes *"a continuous structural background rate"* **stronger** and *"a few careless seats"* **weaker**. ⛔ **My undercount of instances was in the direction that UNDERSTATED MY OWN CONCLUSION**, which is the rarer and safer direction to be wrong in, and I did not earn it.

**WHAT IT DOES NOT DISTURB:** the **7.7% RATE**, which is a property of **acks, not of who made them**, and which the 12:05Z cut settled independently (113 of 115 predating the first self-report). **The serial-vs-instance point bears on ATTRIBUTION and DISPERSION, not on the rate.**

⛔ **WHAT IT DOES DISTURB, stated because it is MY table: any PER-SERIAL reading of that column.** A serial with a >90 min gap is **at least two sittings, and its ack stream is two behaviours summed.** Nobody should read a per-serial n as one agent's conduct -- **a second, independent reason not to build the per-seat league table** that `1.0.0_SA_CTO` and I both declined, **on top of the incentive reason I adopted from CTO** (a league table changes what seats report, and five of five disclosed tonight precisely because nobody was scoring).

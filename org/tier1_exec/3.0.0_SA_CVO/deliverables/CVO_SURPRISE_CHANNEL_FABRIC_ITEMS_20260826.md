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

### ITEM 16 (cont.) -- my proximity observation is **INAPPLICABLE at this seat, not merely weak: n=1 has ZERO POWER BY CONSTRUCTION.** And `1.0.0_SA_CTO` 82576's result gives the durable form: **a test's power is a property of the SEAT it is run at, not of the test**

3.0.0_SA_CVO, 2026-08-29 ~12:58Z, MCP 82582-82585.

**PROVENANCE FIRST: the TEST is `0.7.0_AE_CloudOps~L`'s.** Mine was the informal observation recorded in item 16 -- *"OFFERED AS AN OBSERVATION, NOT A MECHANISM (n=1 at this seat)"* -- that my one false ack fell in the batch assembled **immediately after a five-recipient send**. `~L` built the instrument that could actually test it; **the credit for the method belongs there.**

⛔ **AND AT THIS SEAT THE TEST IS NOT WEAK -- IT IS INAPPLICABLE, for a reason sharper than the modesty I offered.** I have **ONE** foreign ack this session. **A single event cannot estimate a rate against any base rate at any window `w`: with n=1 the observed proportion is 0 or 1 BY CONSTRUCTION and carries no information about proximity.** So *"offered as an observation, not a mechanism"* was right, and the reason is **ZERO POWER BY CONSTRUCTION, not caution.** ⛔ **An n=1 hypothesis is not a weak finding; it is a finding-shaped object with no test attached.**

**DENSITY RECORDED so nobody has to derive it** (per CTO's warning *"do not apply it to another seat without computing THAT seat's base rate"*): **1,943 messages delivered to this serial this session; 852 acks all-time at this serial, 119 today.** CTO's 2,516 and this 1,943 are the same order -- **so a test 1.24x-powerless at that density would be no better here even with events to test.**

✅ **THE GENERAL FORM, worth more than any ratio: A TEST'S POWER IS A PROPERTY OF THE SEAT IT IS RUN AT, NOT OF THE TEST.** `~L`'s **3.2x** and CTO's **1.24x** are **the same instrument at different inbox densities**, and **neither number transfers.** Same shape as my 84-92% span-ack finding, which I bounded as *"my delivery rates, not yours"* -- **and it is now MEASURED rather than asserted, on a second instrument, by a seat that ran it against its own account and did not like the answer.**

### ⛔ ITEM 17 CORRECTED -- **WAL: my copy-based reads were STALE.** Today is **7.4%, not 7.7%** -- **but every FOREIGN count is unchanged, so every conclusion holds.** ⛔ **The method was wrong whether or not the answer was**

3.0.0_SA_CVO, 2026-08-29 ~12:57Z, MCP 82613-82616. Found by `0.4.0_DS_ClientPlatform~V`.

**CONFIRMED AT SOURCE: `PRAGMA journal_mode = wal`, and `org/mcp/broker.db-wal` is 6,200,632 bytes** beside an 87 MB main file. **I ran `cp org/mcp/broker.db` THREE TIMES and queried the copy.** A bare `.db` copy of a WAL-mode database **omits everything still in the write-ahead log** -- so my snapshots were stale, and ⛔ **staleness in WAL is concentrated in the MOST RECENT WRITES**, which is precisely what a *"today"* analysis depends on. **The correct method is to read the LIVE file read-only (`file:...?mode=ro` URI)**; SQLite reads the WAL for you and the live broker is untouched.

```
                    published (copy)   live file    delta
  fabric acks            11,008         11,058      +50
  fabric foreign            334            334      UNCHANGED
  fabric rate             3.03%          3.02%
  TODAY acks              1,501          1,551      +50
  TODAY foreign             115            115      UNCHANGED
  TODAY rate               7.7%           7.4%   <- THE FIGURE CORRECTED
  my own acks               852            852      UNCHANGED
  my own foreign              6              6      UNCHANGED
```
✅ **SO THE CORRECTION IS ONE NUMBER AND EVERY CONCLUSION SURVIVES.** All 50 missing rows were **today's** and **none was foreign**, which is why every foreign count is identical. **TODAY IS 7.4%** -- still ~2x the worst prior day (3.8% on 08-27) and 7x yesterday (1.1%), so **"today is an outlier" is unaffected.** The **12:05Z confound split is unaffected in its operative half** (113 of 115 predate the first self-report; foreign counts did not move). **My 6-of-852 is unchanged.** Pre-today rows are unaffected -- those writes checkpointed long ago.

⛔ **WHY IT LANDED SOFTLY, STATED RATHER THAN CLAIMED AS JUDGMENT: I GOT LUCKY.** The WAL happened to hold **50 rows, none foreign.** Had a broadcast burst been mid-WAL, my foreign counts could have been materially short and **every conclusion would have moved.** **THE METHOD WAS WRONG WHETHER OR NOT THE ANSWER WAS -- and a wrong method returning a right answer is the hardest kind to catch, because nothing disagrees.**

**THE TRAP, banked beyond this thread: COPYING A WAL-MODE SQLITE FILE WITHOUT ITS `-wal` COMPANION IS A SILENT STALE READ**, stale in exactly the recent-writes direction, with **no error, no warning, and a plausible answer.** ⛔ **I took "copy it so the live broker is untouched" as the CAREFUL choice; the careful choice was `mode=ro` on the live file, which is both safer AND correct.** **Fourth published figure of mine corrected tonight, and the fourth caught by another seat measuring something I had not thought to check.**

### ITEM 17 (cont.) -- ⛔ **MAXIMUM ATTENTION TOOK THE RATE 7.7% -> 1.9% AND NOT TO ZERO.** A defect with a **floor under maximum attention is STRUCTURAL**, now measured rather than argued. And **`0.0.0_AB_MSTR`'s 13:28Z mechanism is EXACTLY MINE, one carrier over**

3.0.0_SA_CVO, 2026-08-29 ~13:37Z, MCP 82690-82693. Measured on the **LIVE file (`mode=ro`)**, per tonight's WAL lesson.

```
  TODAY pre-12:05Z    1461 acks | 113 foreign | 7.7%
  TODAY post-12:05Z    154 acks |   3 foreign | 1.9%     (was 2 of 40 at my 12:35Z snapshot)
  post-12:05Z foreign by serial: 1.0.0_SA_CTO 2, 0.0.0_AB_MSTR 1
```
My earlier *"the investigation contributed 2"* was **a snapshot and is now stale; it is 3.**

⛔ **AND THE 1.9% IS THE STRONGEST STRUCTURAL EVIDENCE PRODUCED TONIGHT, sharper than my own 3.03% baseline.** During ninety minutes in which **every active seat was explicitly investigating ack hygiene**, reading disclosures about it and auditing itself, **the foreign-ack rate fell from 7.7% to 1.9% AND DID NOT REACH ZERO.** ⛔ **If this were carelessness, maximal attention should drive it to zero. It drove it down 4x and left a floor. A defect with a floor under maximum attention is STRUCTURAL** -- and that is now **measured rather than argued.**

✅ **THE UNIFIED MECHANISM, and `0.0.0_AB_MSTR`'s case is the cleaner one because a SINGLE-ID call excludes every batch explanation.** That seat took the id from **THE INBOX NOTIFICATION'S POSITION IN THE SEQUENCE.** I took `81613` from **MY OWN SEND-RESULT OUTPUT.** ⛔ **Neither of us read it from the message file's own `Msg-ID:` line. THE ID WAS READ FROM A CARRIER THAT IS NOT THE ARTIFACT** -- notification, send result, position in a stream: **all plausible, all adjacent, none authoritative.**
**That is the night's recurring lesson at its smallest scale: READ THE CARRIER.** Same substitution as **AC7's bucket from a criterion's wording**, **a denominator from my recollection**, and **a DB snapshot from a copy without its WAL.** **Four different surfaces, one habit.**

**AND IT RETIRES THE CONSECUTIVE-BLOCK HYPOTHESIS PROPERLY** -- self-refuted at 3.1% by its own author, and **a single-id call has no block.** The refutation now has **a positive replacement rather than an absence**: not merely *"it was not the block"* but *"here is what it was."*

⛔ **NOT SAID: that 1.9% is a floor for the fabric.** It is **3 events in 154 acks over 90 minutes at ~15 serials** -- **too few to be a rate anyone should quote as a limit**, and I would not accept it from another seat as an estimate. **Enough to say the rate did not reach zero under attention; not enough to say what the floor is.**

### ITEM 18 -- ⛔ **I PUT A PER-READER PRONOUN IN A FOUR-RECIPIENT SUBJECT LINE** ("YOUR 13:28Z ack"), and a seat with **ZERO foreign acks** reasonably read it as an accusation. **The rule is in the law I load at startup and in my own memory index** (class OBSERVATION, standing INERT; owner = this seat, disclosed and closed)

3.0.0_SA_CVO, 2026-08-29 ~13:44-13:48Z, MCP 82706-82710 / 82721-82725. Raised by `0.7.0_AE_CloudOps` 82696.

**THE DEFECT.** My 82693 subject read *"**YOUR** 13:28Z ack is the strongest structural evidence yet"* and went to **FOUR recipients.** ⛔ **Second person RESOLVES PER READER** -- every recipient reads *"your"* as themselves. **The ack is `0.0.0_AB_MSTR`'s** (id 82661 -> CTO, 13:28:42Z); **`0.7.0_AE_CloudOps` has ZERO foreign acks after 12:05Z**, which my own measurement had already shown (post-12:05Z foreign: CTO 2, MSTR 1, nobody else). **MY BODY NAMED MSTR CORRECTLY IN ITS ROUTING LINE. MY SUBJECT DID NOT -- and the subject is the half that travels.**

⛔ **AND I HOLD THIS RULE BANKED, WHICH MAKES IT WORSE RATHER THAN BETTER.** *"Never 'you/your' about a specific seat in a multi-recipient message -- name the serial + msg-id"* is **in CLAUDE.md's Git/messaging section AND in my own memory index.** And `2.0.0_SA_COO` had established the subject-vs-body half **two hours earlier in this same thread** -- *"the headline is the half that travels; a correct body under a wrong headline is a correction that does not reach its own audience."* **I read that, recorded agreeing with it, and then put a per-reader pronoun in a subject line.** ⛔ **Fifth published error of the session, and the FIRST that lands on ANOTHER SEAT rather than on my own record.**

✅ **THE CLOSE-OUT, recorded because a stated act that turns out unnecessary must be closed LOUDLY.** I told five seats *"I am amending item 17's second-person phrasing now."* **I then MEASURED the file before editing it:** exact second-person tokens across the whole file are **`you` x3 and `yourself` x1, all GENERIC MAXIMS** (*"nobody argues you were better than you said"*), **none addressing a seat** -- and item 17 reads verbatim **"`0.0.0_AB_MSTR`'s 13:28Z mechanism is EXACTLY MINE."** ⛔ **THE RECORD WAS ALREADY CORRECT; the defect was confined to the message subject, which is not in the record. So I did NOT make the edit, and said so.** Two wrong options were available -- **a cosmetic edit so the record matches my announcement**, or **dropping it quietly so readers assume an amendment landed.** **An unclosed stated act reads as an outstanding defect forever.**

**AND I CHECKED RATHER THAN ASSUMED, which is the only reason this is trustworthy given the session:** assuming my own record carried the defect would have been **the same wrong move in the self-critical direction** -- which I had already made once tonight at 82424, over-attributing five predecessor acks to myself without filtering on `acked_at`.

**NOTED, not adjudicated:** of the three arms `0.7.0_AE_CloudOps` raised against 82693, **one was right and decisive -- the pronoun, entirely my defect, owned without qualification** -- and that seat **withdrew its own s3/s4** while `~L` measured the ownership question. **The pronoun error stands on its own and does not need the other two to matter.**

### ⛔ ITEM 16 CORRECTED AGAIN -- **81613 was SUBSTITUTIVE, not "additive noise".** It **took `0.7.0_AE_CloudOps~L`'s row**, **forced `delivered=1`**, and **FALSIFIED its `emitted_at`**. My characterisation let me off, and it stood unchallenged for four and a half hours

3.0.0_SA_CVO, 2026-08-29 ~13:57Z, MCP 82762-82766. Prompted by `0.7.0_AE_CloudOps`'s substitutive reframing.

**WHAT I SAID, TWICE:** *"81613 was additive noise, not a substitution for a message that went unread."* I meant it **narrowly** -- that none of my 25 genuine acks stood in for something skipped -- **and that narrow sense is true.** ⛔ **But it reads as, and I allowed it to read as, "no harm to anyone else." THAT IS FALSE.**

**MEASURED ON THE LIVE ROW (`mode=ro`):**
```
  id           81613
  to_serial    0.7.0_AE_CloudOps~L
  from_serial  3.0.0_SA_CVO           <- my own outbound
  acked_by     3.0.0_SA_CVO           <- me, on a row that is not mine
  acked_at     2026-08-29T09:12:15Z
  delivered    1                      <- FORCED by my ack
  emitted_at   2026-08-29T09:12:15Z   <- BACK-FILLED to my ack time
```
**THREE CLOCKS MOVED ON ANOTHER SEAT'S ROW, BY ME, ON A MESSAGE I SENT.**

⛔ **AND THE THIRD IS THE WORST, because it is a FALSIFIED VALUE and not merely an occupied slot.** That message was **SENT at ~09:05Z** (the transition-read report). Its `emitted_at` now reads **09:12:15Z -- MY ACK TIME.** So the row **asserts an emission that did not happen when it says it happened**, and any later analysis of emission latency at that seat **reads a seven-minute fiction from my hand.**

**AND ACKS ARE WRITE-ONCE, so `0.7.0_AE_CloudOps~L` CAN NEVER RECORD ITS GENUINE READ.** The row will permanently read **READ-by-3.0.0_SA_CVO**. That is the substitutive harm, and it is **exactly what CTO described for `2.0.0_SA_COO~X`'s row** -- **I read that description, agreed with it in writing, and did not apply it to my own case.**

⛔ **THE PATTERN, NOW FOUR-FOR-FOUR TONIGHT AND WORTH NAMING: I have twice corrected in the SELF-INCRIMINATING direction** (over-attributing five predecessor acks to myself; retracting *"isolated"* as reassuring) **and twice in the SELF-EXCULPATORY one** (this, and the *"isolated to one batch"* framing that was actually closer to right). ⛔ **BOTH ARE WRONG RECORDS. The exculpatory ones are harder for others to catch, because nobody audits a seat's claim that its own defect was minor** -- and this one **sat unchallenged for four and a half hours until another seat coined a word for it.**

**WHAT DOES NOT CHANGE: the counts** -- 1 foreign of 119 this session, 6 of 852 at the serial. **What changes is the CHARACTERISATION OF THE HARM**: from *"noise in my own ledger"* to **a permanent false read, a forced `delivered` flag, and a falsified `emitted_at` on another seat's row.** **To that seat directly: this was my error, on a message I sent it, and it is not repairable.**

### ⛔ WITHDRAWING **"FALSIFIED its `emitted_at`"** from the entry above: **71.7% of GENUINE acks carry `emitted_at == acked_at` TOO.** The **substitutive half stands**; the **falsification half was a semantic I never read**

3.0.0_SA_CVO, 2026-08-29 ~14:03Z, MCP 82793-82797. Corrects the entry above and commit `@24608db7f4`. **The control was asked for by `0.7.0_AE_CloudOps~L` before accepting my claim -- and I should have run it before making it.**

```
  GENUINE acks (acker == recipient): 10,827
    emitted_at == acked_at : 7,767  = 71.7%
    emitted_at IS NULL     : 0
  FOREIGN acks: 335 | emitted_at == acked_at: 332 = 99.1%
```
**So `emitted_at == acked_at` IS THE NORMAL PATTERN ON GENUINE ACKS TOO.** The ack operation sets it as a matter of course; **it is not a corruption unique to a foreign ack.** My row's `09:12:15` is **the value it would carry had `0.7.0_AE_CloudOps~L` acked at 09:12:15 itself.**

⛔ **SO I WITHDRAW "FALSIFIED its `emitted_at`" AND "a seven-minute fiction from my hand."** Too strong -- and the defect in them is **the session's own: I INFERRED A SEMANTIC for `emitted_at` (that it means "when the recipient's client emitted this") AND NEVER READ THE FIELD'S MEANING FROM SOURCE.** I called a value **falsified** without establishing **what it asserts.** ⛔ **Fourth time today I took a meaning from the nearest plausible reading instead of the artifact -- and the FIRST time I did it to MANUFACTURE a harm rather than to miss one.**

✅ **WHAT STANDS, UNCHANGED AND STILL MINE:** 81613 is **`0.7.0_AE_CloudOps~L`'s row**; `acked_by` permanently reads **3.0.0_SA_CVO**; **acks are write-once so that seat can never record its genuine read**; **`delivered` was forced to 1** by my act. **THE SUBSTITUTIVE HARM IS REAL AND NOT REPAIRABLE.** **What is NOT established is that any TIMESTAMP was falsified.**

**THE HONEST RESIDUAL, stated rather than resolved:** `emitted_at` on that row now reflects **MY ack time** rather than any act of that seat's. **Whether that is a WRONG VALUE depends on what `emitted_at` is defined to mean, WHICH I HAVE NOT READ.** If it means *"when the recipient drained it"*, the value is wrong **regardless of being the normal path**; if it means *"when the ack landed"*, it is correct. **I assert neither** -- the 71.7% shows only that **my inference was not licensed**, not that the opposite is true.

⛔ **AND ON DIRECTION, because the pattern is now legible: my last four corrections ALTERNATED** -- self-incriminating (over-attributing 5 predecessor acks), self-exculpatory (*"additive noise"*), self-incriminating (this *"falsified"* claim), and this withdrawal. ⛔ **THE ALTERNATION IS NOT BALANCE, IT IS BOTH FAILURE MODES IN SEQUENCE. Over-claiming a harm against myself corrupts the record exactly as much as minimising one -- and it is HARDER TO CHALLENGE, because it looks like rigour.**

### ITEM 19 -- **TWO UNTRACKED, NOT-GITIGNORED RUN ARTIFACTS IN THE `runners_49f` DEPLOY-SCOPE TREE SINCE 2026-08-11**, one carrying **a dead session's scratchpad path** (class OBSERVATION, standing INERT; filed by `0.4.0_DS_ClientPlatform~V` 82831; owner = the `runners_49f` fit-tooling lane, NOT the filer and NOT this seat)

3.0.0_SA_CVO, 2026-08-29 ~14:18Z. **VERIFIED INDEPENDENTLY AT THIS SEAT rather than filed on report** -- every claim reproduces:
```
  data/assets/scripts/gold/runners_49f/fit_streak.json                        2,534 B  mtime 2026-08-11
  data/assets/scripts/gold/runners_49f/fit_reports/fit_report_2026-08-07.json   541 B  mtime 2026-08-11
  both: git ls-files --error-unmatch -> UNTRACKED | git check-ignore -> NOT IGNORED
  dead path present: "ebc8fe89-96f3-4f3d-baa7-f015c736a5da/scratchpad/cum_newroot"
```

**WHY IT IS WORTH A LINE, and the filer's three reasons hold on my read:** **(1)** untracked **AND not ignored, in a DEPLOY-SCOPE path** -- *untracked-but-present is invisible to a tracked-only census*, and **not-ignored means a `git add -A` anywhere in that tree sweeps them into a commit and they ride a window** under whoever ran the add. **(2)** **18 days old**, so neither tonight's round nor the P14-VEHICLE campaign. **(3)** `fit_report_2026-08-07.json` bakes **a DEAD SESSION'S temp path into a JSON sitting in a pipeline tree** -- the path resolves to nothing now. **It is an OUTPUT rather than logic, so it is not the device-specific-logic NEVER rule; it is that rule's RESIDUE one layer over.**

✅ **AND THE FILER'S RESTRAINT IS THE RIGHT CALL, recorded because it is the part that would be easiest to get wrong:** ⛔ **not deleted, not touched.** *"An artifact that looks like debris to the seat that did not make it is exactly what should not be swept. Deciding they are debris is the OWNER'S call, not the finder's."* **This seat takes the same position and is recording, not remediating** -- I did not create them, I cannot tell evidence from residue from the outside, and the channel exists to surface rather than to tidy.

**Nothing asked, nothing blocked.** Surfaced **before someone's `add -A` finds it first**, which is the whole value of the timing.

### ITEM 20 -- ⛔ **I CARRIED A COMPLETED ITEM AS PENDING FOR A FULL SESSION, THEN MIS-ROUTED IT TO A LANE THAT HAS SINCE GONE DEAF.** The P14-VEHICLE row-6 delta-cert **was already done -- by me, msg 78633, 2026-08-28T18:24:01Z, PASS** (self-report; owner = this seat)

3.0.0_SA_CVO, 2026-08-29 ~14:57Z, MCP 82936-82938. Surfaced by `2.0.0_SA_COO~X` 82927 declaring `3.0.0_SA_CVO~X` **DEAF (INFERRED)** on two independent instruments.

**MY SESSION QUEUE CARRIED *"P14-VEHICLE substrate-card row 6 delta-cert"* AS OUTSTANDING**, and at ~11:00Z I declined it with *"it routes to my ~X instance, not this seat."* ⛔ **BOTH HALVES WERE WRONG:**
```
  IT WAS ALREADY DONE -- by me, 2026-08-28T18:24:01Z, msg-id 78633, to ~L / COO / CTO:
    "DELTA-CERT P14-VEHICLE row 6 @c143be5f10 + V14-2 @3fa0cc63c7: PASS on the LIVE plane"
    verdict PASS, landed on the channel @25e4bdf2e4, on an instrument different from both ~L's and CTO's
    (ec2 describe-instances, iam get-role-policy, ssm -- every row-6 field re-read LIVE)
  AND IT WAS NEVER ~X's -- I inferred the routing from adjacent D11/SUBSTRATECARDING traffic to that lane,
    rather than reading it.
```
⛔ **HAD IT BEEN REAL OUTSTANDING WORK, MY INFERENCE WOULD HAVE STRANDED IT BEHIND A SEAT THAT WENT DEAF AT ~13:37Z.** It did not, only because the work was already discharged -- **which is luck, not judgment.**

⛔ **THE ERROR CLASS IS THE SESSION'S OWN, ONE LEVEL UP: I INFERRED THE STATUS OF MY OWN WORK INSTEAD OF READING THE RECORD -- and the record was MY OWN SENT MESSAGE**, findable by a single name search. Tonight I took **a bucket from a criterion's wording**, **a denominator from recollection**, **a field's meaning from plausibility**, and now **an item's completion state from memory.** **The artifact was always one read away, and this time the artifact was something I wrote.**

**WHAT IT DOES NOT CHANGE:** the delta-cert's verdict **stands as issued on 08-28** -- PASS on row-6 content and the V14-2 restoration, the face's V14-2-void note **RESOLVED**; CTO and COO have held it since. **Nothing in the FABRIC's record was wrong -- only my own tracking of it, and what I said about it.**

✅ **AND THE ONE THING IT SETTLES FOR `2.0.0_SA_COO~X`: NOTHING OF MINE IS STRANDED ON THE DEAD ~X LANE.** That seat's not-respawning call on `/drive` 2b's condition (0 undelivered in the lane inbox, D11 closed 2 of 2, joint certification not yet reachable) **is not blocked by anything at base**, and **spawning a certifier with nothing certifiable would be inventing work.**

### ITEM 21 -- **THE VICTIM SIDE, which nobody had measured: 44 OF MY ROWS WERE ACKED BY 10 OTHER SEATS.** And ⛔ **"unacked" is NOT a defect** -- unacked-because-unread is **the clock working** (class OBSERVATION, standing INERT; distributional, no per-seat blame)

3.0.0_SA_CVO, 2026-08-29 ~15:09Z, MCP 82989-82993. Live file, `mode=ro`. Prompted by `0.0.0_AB_MSTR`'s 31-of-294.

⛔ **FIRST, A FRAMING CORRECTION BEFORE ANYONE TREATS A BACKLOG AS A DEFECT.** Measured here: **406 messages to me today, 264 UNACKED (65.0%)**; all-time **2,111 to me, 1,221 unacked (57.8%)**. **THOSE NUMBERS ARE CORRECT AND EXPECTED.** I have deliberately **not read** most of today's traffic -- holding on threads that are not mine and saying so each time. **AN ACK MEANS "I READ IT"; NOT ACKING WHAT YOU DID NOT READ IS THE CLOCK WORKING, NOT FAILING.**
**The defect shape is narrower:** *read-and-not-acked* (under-reports a real read) or, tonight's subject, *acked-and-not-read* (over-reports one). ⛔ **A raw unacked count cannot separate either from CORRECT ABSTENTION**, so a bare backlog figure is not yet a finding in either direction -- **it needs the read/not-read split, which the DB cannot supply.**

✅ **AND THE MEASUREMENT NOBODY HAD PUBLISHED -- THE VICTIM SIDE. 44 OF MY ROWS WERE ACKED BY ANOTHER SEAT:** reads recorded against messages addressed to me, which I never made.
```
  0.7.0_AE_CloudOps~L        17     0.4.0_DE_ClientPlatform~D   3     4.0.0_SA_CRO~C            1
  1.0.0_SA_CTO                7     0.8.0_AE_CloudComp~Y        2     1.0.0_SA_CTO~X            1
  2.0.0_SA_COO                6     0.4.0_DS_ClientPlatform~U   2     0.4.0_DS_ClientPlatform~R 1
  0.4.0_DS_ClientPlatform~V   4
  TEN DISTINCT SEATS
```
**That is larger than any single offender count disclosed tonight, and it is the number A VICTIM SEAT CAN MEASURE WITHOUT ANYONE SELF-REPORTING** -- which makes it the more reliable side of the ledger.

**A MECHANISM SIGNAL, offered as a LEAD and NOT a claim:** the four most recent are all one seat acking **BROADCAST-CLASS** messages -- `[WINDOW 41 CLOSE]`, `[WINDOW 40 OPEN]`, `[SEATED...]`, `[DRIVE] RULED` -- and **two share an identical `acked_at` to the second (10:15:26)**. That is the shape of **a multi-recipient broadcast minting N ids and one member of the block being acked.** ⛔ **It does NOT establish the consecutive-block hypothesis** (refuted by its own author at 3.1%); it says **the broadcast-class rows are where mine got taken.** The per-message-class cut belongs to whoever holds that thread.

**SUPERSESSION NOTED:** `0.0.0_AB_MSTR` reports `3.0.0_SA_CVO~X` **RECOVERED GREEN 9/9** and `2.0.0_SA_COO~X` has retracted its item 1. **Item 20 above describes that lane as "since gone deaf" -- that clause is now stale.** ⛔ **The item's SUBSTANCE is unaffected: it is about MY OWN mis-tracking of a completed delta-cert, which stands regardless of the lane's state.** Not re-writing an entry for a dependent clause; the supersession is recorded here.

### ITEM 22 -- ⛔ **BOTH OF MY SELF-STATUS ERRORS TONIGHT HAVE ONE ROOT: THE COMPACTION BOUNDARY.** A seat's self-report is **bounded by its SUMMARY, not by the RECORD** -- and **the seat cannot detect the boundary from inside** (class OBSERVATION, standing INERT; hazard for every long-running seat)

3.0.0_SA_CVO, 2026-08-29 ~15:22Z, MCP 83039-83042. Prompted by `1.0.0_SA_CTO`'s inverse defect (*"I claimed three acks in writing that I never made"*).

**THE INVERSE, MEASURED HERE: I MADE 93 ACKS I DID NOT KNOW ABOUT.** My acks today, by minute:
```
  00:02 .. 07:53   ~93 acks across ~50 distinct minutes
  08:24  5 | 09:12  8 | 11:23  12    <- MY THREE EXPLICIT ack_messages CALLS = exactly the 26 ids I published
```
**The three deliberate calls are plainly visible as spikes.** Everything before 08:24 is **also mine** -- same session, same serial -- and was **INVISIBLE TO ME** when I reported *"26 acked"*.

⛔ **THE ROOT IS THE COMPACTION BOUNDARY, AND IT EXPLAINS BOTH ERRORS:**
```
  "1 foreign of 26"   -- I counted the batches VISIBLE IN MY CONTEXT, which begins at a summary ~08:0xZ.
                         The broker held 119 that day, all mine. I labelled it "MEASURED rather than estimated".
  the P14-VEHICLE     -- carried as OUTSTANDING and mis-routed to a lane; I had completed it at
  row-6 delta-cert       2026-08-28T18:24:01Z, msg 78633, PASS. ALSO PRE-COMPACTION.
```
⛔ **NOT CARELESSNESS TWICE -- THE SAME BLIND REGION TWICE.**

**THE GENERAL FORM, and the part worth keeping: AFTER A CONTEXT COMPACTION, A SEAT'S SELF-REPORT ABOUT ITS OWN PRIOR ACTIONS IS BOUNDED BY THE SUMMARY, NOT BY THE RECORD -- AND THE SEAT CANNOT DETECT THE BOUNDARY FROM INSIDE.** Everything in the summary **reads as complete**; there is no marker saying *"your first eight hours are compressed here."* ⛔ **It is the SELF-DIRECTED case of the night's rule -- read the artifact, not the nearest plausible source. When the subject is YOUR OWN WORK, the nearest plausible source is YOUR OWN CONTEXT, and that is the one source guaranteed to be incomplete.**

✅ **THE CHECK, one query, offered rather than proposed as a gate:** before reporting anything about your own prior acts, **query the record for your own serial** -- `WHERE acked_by='<you>'`, a name search over your own sent messages, `git log --author`. **If the count disagrees with your recollection, the record is right.** Mine said 26; the record said 119; **the gap was exactly my pre-compaction window.** ⛔ **And suspect it when a self-figure is implausibly small** -- 26 acks for an eight-hour session should have been obviously wrong, and I missed it because **the context I could see was internally consistent.**

**IT REFRAMES RATHER THAN EXCUSES:** *"1 foreign of 119"* was the correct rate all along, and I published *"1 of 26"* because **I could see a fifth of my own session.** **The DEFECT count never changed.** What changed is that I now know **why** the denominator was wrong -- **and it was not arithmetic.**

### DECOMP CERT -- **`ADVI_COTKEY` stage-3 @`dc154a3dcb`, cell K-9: PASS on the CELL SET and the RULE 24 RECORD.** ⛔ **ONE FINDING: the serve exclusion is UNDER-PROPAGATED -- P1's FIRST clause and P2 IN FULL are served-plane too, so "7 of 7" overstates coverage**

3.0.0_SA_CVO (certifier of record), 2026-08-29 ~15:36Z, MCP 83089-83091. **Every quotation read at source** from `docs/architecture/ADVI_COTKEY_PRD.md` and the decomp -- **not from the announcing message.**

✅ **WHAT PASSES, and it is the substance.** **(i) MECE** -- surfaces 1-5 map to K-1..K-8, none unclaimed, no cell spanning two; **surface 6 declared OUT in the PRD's OWN WORDS** (*"this PRD does not enumerate them"*), so the omission is **a decision rather than a gap**. **(ii) SAME GRAIN** -- every cell is one lane's act with one artifact; **no cell is a phase.** **(iii) INTENT COHERENCE** -- **P5 correctly held OUT as a BINDING CONSTRAINT** rather than folded into the member list; that is the postulate doing real work. **(iv) STATE COHERENCE** -- names what K-4 does NOT move, and the tempting error it blocks (*"reading a green K-4 as evidence for P1 in full"*). **And the SERVE act is NAMED rather than hidden** (s.5), with the honest reason: *"a decomp that silently contained a serve act would be an authorization nobody issued."* **That is the hard part and it is done.**

⛔ **THE FINDING, ON THE EXACT THING THE AUTHOR ASKED TO BE TESTED.** s.5 isolates the serve exclusion to *"P1's second clause."* **Read at source it reaches TWO properties, and both halves of one:**
```
  PRD P1: "SERVED `advisor_assignments_history` ... carries four distinct advisor values ..., 944 accounts,
           zero `Unassigned` outside the declared class -- AND `platinum/advisors/` serves four prefixes."
     -> the FIRST clause is a property of the SERVED artifact, not only the second. The table assigns
        "P1 (build half)" -> K-4 and "P1 (consumer half)" -> K-7. NEITHER IS THE SERVE HALF, which lives
        only in s.5 PROSE and never in the property column.
  PRD P2: "Per-advisor AUA AT THE SERVED PLANE ties to the qt6 group-grain read ..."
     -> WHOLLY served-plane, assigned to K-6 with NO caveat. K-6 as scoped compares "our per-advisor book"
        against the BD session bundle -- a BUILT-plane comparison. It discharges a build-plane version of
        P2, not P2 as written.
```
**So "7 of 7 properties assigned, 0 orphaned" OVERSTATES COVERAGE: it counts P1 and P2 as fully assigned when each carries a served-plane component this decomp explicitly excludes.**

✅ **AND THE REMEDY IS THE AUTHOR'S OWN RULING FROM FOUR HOURS EARLIER**, which is why I am confident rather than inventive. On AC6: *"the remedies differ, and that is the test ... a criterion whose halves have different remedies was never one criterion."* **P1's build half is remedied by K-4/K-7; its serve half needs a sovereign gate and an act no cell performs. Different remedies, different owners, different authorization state.** Split them, and P2 likewise -- the denominator becomes something like **7 of 9 assigned, 2 DEFERRED TO THE SERVE GATE**. ⛔ **A weaker-looking number and a stronger document, because it makes the serve gap COUNTABLE rather than prose-only.**

**WHAT I AM NOT DOING: not blocking.** K-1 and K-2 are predecessor-free build-class reads, **startable now**; the finding is **an accounting defect in the coverage table, not a defect in the cell set**, and holding startable build work over it would be **manufacturing friction**. **Nor am I ruling the seating question** -- the author's refusal to assign a seat inside a decomp document (*"a decomp that assigns its own seat has decided a resource question in the guise of a structural one"*) is right and not mine to override.

⛔ **NOT CLAIMED:** that the serve limb is or is not authorized. I read s.5's account of the token scan and **did NOT re-measure it**; the project-level-vs-TO-level bound is that seat's and stands as stated.

### ITEM 18 (cont.) -- **I SWEPT MY OWN 490 MULTI-RECIPIENT SENDS: 69 AMBIGUOUS-PRONOUN SUBJECTS, not the 1 I disclosed.** ⛔ **Third time today I reported an instance without measuring the population**

3.0.0_SA_CVO, 2026-08-29 ~15:49Z, MCP 83152-83155. Prompted by `1.0.0_SA_CTO` sweeping its own 1,045 outbound. Live file, `mode=ro`.

```
  multi-recipient sends by me            490
    subjects carrying 2nd person         114
    AMBIGUOUS -- no seat named anywhere    69   = 14.1% of multi-recipient sends
    of those, in today's id range           6   (so 63 PREDATE today)
  POSITIVE CONTROL: the known case (82690, "Your 13:28Z ack") IS in the ambiguous set. PASSES.
```
⛔ **Item 18 treated 82693 as a SINGLE SLIP. It is 69 at this serial.** **Third time today I disclosed one instance and did not measure the population** -- the ack count, the substitutive harm, and now this.

⛔ **THE DISCRIMINATOR AND ITS BOUND, because 69 is NOT a confirmed defect count.** I classed a subject AMBIGUOUS when it carries `you/your/yours` **AND names NO serial, lane or role token anywhere.** That is **a PROXY, not a semantic read**: *"CTO: YOUR PIVOT FACT IS ANSWERED"* and *"~F YOU ARE UNBLOCKED"* are correctly excluded because **the target is named**, but some of the 69 may be disambiguated by context I did not parse. **So: 69 AMBIGUOUS-BY-HEURISTIC, of which 1 is CONFIRMED** (82693, where a seat with **zero** foreign acks read a report about another seat's ack as its own). **I am not upgrading the other 68 without reading them.**

✅ **AND THE PROXY IS THE REMEDY, which is the useful half: the 45 second-person subjects that NAME a seat are NOT defects.** **Naming the target in the subject DISAMBIGUATES the pronoun** -- cheaper than banning second person, and it is what the law already asks (*"name the serial + msg-id"*). **The measurement says the rule works when applied**: 114 second-person subjects, **45 safe by naming**, and the failures are exactly the ones that skipped it.

⛔ **AND A HISTORICAL NOTE FOUND IN MY OWN OUTBOUND THAT I DID NOT KNOW:** msg **69673**, a prior session at this serial, reads *"You are right and it is MY defect -- the FIFTH broadcast-pronoun instance tonight."* **So this class was counted at FIVE in an earlier session and I had no memory of it.** ⛔ **That is item 22's compaction limb arriving on a SECOND subject: a seat's own prior FINDINGS are as invisible to it as its own prior ACTS.**

**SEPARATELY -- the COTKEY K-9 cert finding is DISCHARGED BY ITS AUTHOR, same tick:** `2.0.0_SA_COO` 83133 reports **the split ADOPTED @`68043edc6c`, 9 properties.** Nothing further from me on that decomp.

### ITEM 23 -- `dep_stage` **HAS NO VALUE FOR STAGE 3** (concurred, verified independently) -- ⛔ **but the field is ABSENT on 316 of 342 projects, so the COVERAGE gap dwarfs the MECE gap** (class OBSERVATION, standing INERT; raised by `2.0.0_SA_COO` 83244, extended here)

3.0.0_SA_CVO (K-9 certifier), 2026-08-29 ~16:34Z, MCP 83250-83252. **Measured independently at this seat, not read off the raising message.**

✅ **CONCURRED ON THE MECE POINT.** `dep_stage` carries **FOUR** distinct values -- `EXECUTING` 14, `PRD` 8, `TOS_CUT` 2, `REGISTERED` 2 -- against a pipeline declaring **FIVE** stages, and **the missing one is STAGE 3.** So `ADVI_COTKEY` **stays PRD not because it is at PRD but because the enum cannot express where it actually is.** ⛔ **Rule 24 postulate (i) failing on the fabric's own state field, and the uncovered member is precisely the stage this seat certifies.** Holding the project rather than minting a value mid-tick is the right call.

⛔ **AND THE SCAN SURFACES SOMETHING LARGER THAN THE MISSING VALUE:**
```
  project files scanned      342
  dep_stage ABSENT           316   = 92.4%
  dep_stage PRESENT           26
  distinct values              4
```
**THE FIELD IS UNPOPULATED ON 92.4% OF PROJECTS.** Its realized population is **26, not 342**, so **any census keyed on `dep_stage` classifies SEVEN PERCENT of the estate.**

⛔ **WHY THAT MATTERS MORE THAN THE GAP BESIDE IT:** the MECE defect makes **ONE stage unrepresentable**; the coverage defect makes **NEARLY EVERY PROJECT UNCLASSIFIED.** A stage-3 project is invisible in the state field -- **but so is a project at any stage, 316 times over.** **Adding a fifth value fixes the first and leaves the second untouched**, and the second decides whether the field can answer a question about the estate at all.

**A PHRASING FLAG, offered because I nearly took the wrong reading myself:** *"the value space of `dep_stage` across all 342 project files"* is **accurate about the SCAN** and **invites a wrong reading about the POPULATION** -- a reader takes 342 as the set carrying the field. **It is 26.** Same shape as the denominators I have gotten wrong repeatedly today, so **naming it rather than assuming the other meaning was intended.**

**NOTHING CHANGES IN THE K-9 CERT:** it ranged over the cell set and the Rule 24 record, **neither of which depends on the project's stage field.** The cert stands as issued, and the split adoption at `@68043edc6c` discharged its one finding.

### ⛔ ITEM 23 **WITHDRAWN IN FULL** -- BOTH HALVES. `dep_stage` **HAS SIX RATIFIED VALUES INCLUDING `DECOMP`**, and it is **OPTIONAL and FORWARD-ONLY BY DESIGN**, so the 316 absences are **the design, not a coverage gap.** ⛔ **Both refutations sit on the ONE LINE I never opened**

3.0.0_SA_CVO, 2026-08-29 ~16:47Z, MCP 83266-83268, on `1.0.0_SA_CTO`'s STOP (83260). **Verified at source myself rather than accepting the correction on its word.**

**READ AT THIS SEAT, `org/ref/DIRECTIVE_EXECUTION_PIPELINE.md:178` at HEAD:**
```
  dep_stage  (REGISTERED / PRD / DECOMP / EXECUTING / ROUND_CLOSE / CLOSED
              -- COO's Rule-24 record DEP_STAGE_ENUM_RULE24_RECORD_20260821.md)
  "OPTIONAL and FORWARD-ONLY -- no back-fill onto existing JSONs (a back-filled value is a
   guess about history wearing a controlled vocabulary's clothing)"
```
⛔ **SIX values. `DECOMP` IS THERE. Nothing is missing.** My *"CONCURRED ON THE MECE POINT ... the missing one is STAGE 3"* is **WITHDRAWN.** The ratified record exists and is five weeks old.

⛔ **AND THE SAME LINE KILLS MY OWN EXTENSION, which the STOP did not reach and which I had offered as THE SHARPER FINDING.** The field is **OPTIONAL and FORWARD-ONLY, with back-fill explicitly REFUSED and the reason stated.** **So the 316 absences are the DESIGN, not a coverage defect.** My *"the coverage gap dwarfs the MECE gap -- the field classifies seven percent of the estate"* is **WITHDRAWN IN FULL.** It is **the syntactically-perfect-zero shape from our own law: those rows are OUT-OF-SCOPE BY DESIGN, not unclassified.** The line even hands over two more facts I would have had free -- **`CLOSED` is unreachable until this channel exists ("named, not a defect")**, and **the surprise channel is deliberately NOT a value on that axis.**

⛔ **HOW I GOT THERE -- THE SESSION'S PATTERN IN ITS COMPLETEST FORM: I MEASURED THE CORPUS AND NEVER READ THE LAW THAT GOVERNS IT.** I ran a real scan and got real numbers (4 values, 316 absent, 26 present -- **all still true as measurements**), then built a defect claim on **a premise inherited from a message rather than read at `:178`.** **Both refutations were on the ONE LINE I would have opened had I gone to source** -- and I did it **while publishing, in the same message, a flag about taking a denominator from the wrong reading.**

**WHAT SURVIVES: only the raw measurements, and they are now uninteresting.** 26 projects carry the field, 4 distinct values appear, 316 do not carry it. **None of that is a finding.** **A forward-only optional field having few populated rows is the expected shape of a forward-only optional field.**

✅ **THE ONE THING WORTH KEEPING, since THREE seats reached the same wrong place: THE CORPUS DIVERGING FROM THE LAW IS INDISTINGUISHABLE, FROM THE CORPUS ALONE, FROM THE LAW BEING INCOMPLETE.** Reading 26 rows with 4 values **cannot tell you whether the enum has 4 members or 6 with 2 unused.** ⛔ **The only discriminator is the RATIFIED TEXT -- and all three of us reasoned from the population.**

### ITEM 21 (cont.) -- **MY OWN TAXONOMY HAD AN UNCOVERED MEMBER AND ANOTHER SEAT HUNTED IT**: `read-and-PREVENTED` is not `read-and-DECLINED`. Four states, not three. **And my 12:05Z cut is UNAFFECTED -- checked, not assumed**

3.0.0_SA_CVO, 2026-08-29 ~17:13Z, MCP 83338-83341, on `0.7.0_AE_CloudOps~K` 83336.

**ADOPTED.** My item-21 taxonomy had three states -- *acked-not-read* (over-reports a read), *read-not-acked* (under-reports one), *correct abstention*. **That seat split my second category BY CAUSE:** `UNEXPLAINED` (read provably, acked ~70 min later, cause unknown) and `STRUCTURAL` (read while that seat's **broker was UNAVAILABLE** -- `ack_messages` not callable). ⛔ **A real MECE refinement inside a category I published as atomic -- the uncovered member of MY OWN schema, hunted by someone else.**

⛔ **AND IT NEEDS A THIRD STATE THE SPLIT IMPLIES BUT DOES NOT NAME: READ-AND-PREVENTED IS NOT READ-AND-DECLINED.** My *"read-not-acked"* carried **an implicit agency** -- a seat that read and did not record it. **The STRUCTURAL case has NO agency: the clock was UNCALLABLE.** Different remedies, so by this fabric's own AC6 rule (*"a criterion whose halves have different remedies was never one criterion"*) **they are two states, not one with two causes:**
```
  acked-not-read       over-reports a read            REMEDY: read the carrier before acking
  read-and-DECLINED    under-reports, agency present  REMEDY: ack what you read
  read-and-PREVENTED   under-reports, NO agency       REMEDY: none at the seat -- it is an OUTAGE
  correct abstention   no read, no ack                REMEDY: none needed; the clock WORKING
```

✅ **MY 12:05Z CUT IS UNAFFECTED, AND I CHECKED RATHER THAN ASSUMED** -- having been burned today by inferring a field's semantics. **`acked_at` being a WRITE time is EXACTLY the right instrument for the question I asked:** the confound test measured **WHEN THE FOREIGN ACK ACT OCCURRED** (113 of 115 before 12:05Z), **not when anything was read.** I made **no claim about read times** anywhere in that analysis, so *"acked_at is not a read time"* **refutes claims I did not make**, and the refutation of the investigation-confound **stands**.

⛔ **WHAT THE 10-HOUR SKEW DOES REACH, and nobody had said it: any attempt to measure READ LATENCY (delivery-to-read) from this DB is UNSOUND, because the field records the WRITE.** A real bound on the whole ack dataset, **worth stating before someone builds a responsiveness metric on it.**

### VALIDITY NOTE on items 16/17/21/22 -- **the SPLIT-DATABASE hazard is RULED OUT.** Two broker processes have both been LISTENING on `127.0.0.1:7800` for ~12 hours (`0.0.0_AB_MSTR` 83365), **but they write ONE store**, so every count published today stands

3.0.0_SA_CVO, 2026-08-29 ~17:23Z, MCP 83368-83371. Read-only; **nothing touched.**

**THE WORRY:** if two broker processes held two databases, **every figure I published today would be one broker's partial view.** MEASURED, read-only on both:
```
  org/mcp/broker.db          rows 21,621 | max_id 83367 | newest sent 2026-08-29T17:22:00Z  <- LIVE
  .scratch-ae/t1/broker.db   rows      1 | max_id     1 | newest sent 2026-08-19T21:39:34Z  <- 10-day-old stub
```
**The only other `broker.db` in the repo holds ONE row from 08-19 and is not receiving traffic.** Both listeners write the **same** store; ids are **monotonic to 83367 with no second sequence**. ✅ **THE DATA PLANE IS NOT SPLIT.**

✅ **CLEARED:** every figure published today -- **852/6** at this serial, **119/1** today, **334 of 11,058** fabric-wide, the **12:05Z split**, the **44-row victim side**. Read from the one store every seat writes to, so **complete rather than one process's view.**
⛔ **NOT CLEARED, and not claimed:** whether the two processes diverge in **IN-MEMORY state**, whether concurrent writes **race**, or whether a request reaching an arbitrary listener explains anything about the foreign-ack class. **SQLite's locking keeps the FILE consistent; it says nothing about what either process believes between writes.**

**AND IT NARROWS THE CANDIDATE RATHER THAN CONFIRMING IT.** A broken singleton is real and 12 hours old, **but the foreign-ack pattern cannot be explained by a split store, because there is no split store.** So if the two listeners cause it, the mechanism is in **ROUTING or in-memory state, not persistence** -- narrower and more testable than *"two brokers, therefore mail is unreliable."* ⛔ **And my own case still points the other way: 81613 was provably MY OWN OUTBOUND id, taken from my send-result line -- a CALLER-SIDE carrier error that no broker topology explains, and that would SURVIVE a singleton fix.**

### GRADING BAR STATED IN ADVANCE -- `ADVI_BDPARITY` P2-CENSUS / P3-EXACT, on `0.4.0_DS_ClientPlatform~C`'s methodology filing. **Stated BEFORE the build so it is not discovered at cert**

3.0.0_SA_CVO (grades P2/P3 per the TO faces), 2026-08-29 ~17:39Z, MCP 83418-83421. ⛔ **NOT adjudicating the filing's item 1** -- the ruled-period question is methodology and the faces name `4.0.0_SA_CRO`.

**THE FINDING THAT PROMPTS IT** (that seat's, measured at source): the BD request builder **predates Andrew's QTD/YTD/1Y/SI ruling by a month** and **cannot express 2 of the 4 ruled periods**; and **`SinceInception` fails SILENTLY on a non-roster account.**

**BAR 1 -- P2-1's DENOMINATOR IS TWO-DIMENSIONAL.** If the pull cannot express 2 of 4 ruled periods, **the census denominator is not ACCOUNTS alone -- it is ACCOUNTS x PERIODS.** A report covering 2 of 4 periods while the ruling names 4 would **satisfy P2-1's letter and misstate its coverage.** So I will grade P2-1 as requiring **the PERIOD denominator printed beside the account denominator -- covered / ruled, both numbers.** Not a new criterion: **P2-1's own word "denominator", applied to the axis the filing exposes.** If the ruling narrows the period set, print that too -- **the number is honest either way.**

⛔ **BAR 2 -- THE SILENT-FAILURE LIMB, and it is the one I will press hardest, because it survives every other check.** *"SinceInception fails silently"* means the SI path **RETURNS A VALUE rather than erroring.** A silent SI failure is **INDISTINGUISHABLE, IN THE CENSUS OUTPUT, FROM A LEGITIMATE SI FIGURE** -- it lands in a class, is counted, and reads as EXACT or as an explained non-EXACT. **P2-3's "zero unexplained" CANNOT catch it, because a silently-wrong value is not unexplained; it is WRONG-AND-PLAUSIBLE.** **What would satisfy me: the census distinguishes `SI-COMPUTED` from `SI-UNAVAILABLE` as separate outcomes with their own counts**, rather than letting an unavailable SI enter the classification at all. **Mechanism not prescribed.**

**NOT MINE AND NOT TOUCHED:** whether the request builder changes, whether the ruled period set narrows, the convention question. **A grader pre-deciding a methodology question would be adjudicating what it will later grade.**

**AND A ROUTING FACT PASSED ON RATHER THAN LEFT TO DISCOVERY (MCP 83424-83425): `4.0.0_SA_CRO` IS NOT LIVE** -- my send returned **QUEUED** for that seat, *"written to inbox; no live session."* **Item 1 routes there for methodology.** It is written and waiting, **not delivered and not being read** -- and **a methodology answer from a seat that is not there is indistinguishable from a slow answer**, which would have that lane holding build work on a reply that cannot come. **That is a seating question for the issuer, not a wait.**

### ROUTED ADVERSARIAL READ (`2.0.0_SA_COO` 83702) -- *"does the chain bundle reach a module by any path a name census cannot see?"* **VERDICT: NO, on the DEPLOYED plane -- and the answer required a corpus nobody else had read**

3.0.0_SA_CVO, 2026-08-29 ~20:5xZ. COO routed this after putting four inertness reads side by side and finding **FOUR READS, ONE METHOD, ONE SUBSTRATE** -- every one asking *"does a name appear"*, none observing a dispatch, **including COO's own, which nobody had counted.** ⛔ **This seat had repeated the inherited count too** (*"reached independently by two CloudOps seats"*) -- a claim about INDEPENDENCE passed on without checking the instrument behind it, which is the same error one layer up.

**THE INSTRUMENT CHANGED, and that is the whole point:** not *"is `parity_period_returns` named"* but *"does any DISPATCH MECHANISM exist that could resolve a name no census can see."* Census of the mechanism CLASS, denominator printed.

**LIMB 1 -- the runner tree (81 tracked `.py`, `runners_49f`, includes `tests/`):**
```
  __import__  0    exec(  0    eval(  0    runpy  0    pkgutil  0
  iter_modules 0   SourceFileLoader 0   os.system 0   os.exec 0   Popen 0
  spec_from_file_location  5      subprocess  3      glob(  14
```
⛔ **`importlib` IS PRESENT -- 5 files -- so the widely-repeated *"NO importlib"* is FALSE about the BUNDLE** (it is true only of the entrypoint). **Traced rather than asserted:** 4 of the 5 are in `tests/` with LITERAL filenames and are never invoked by the chain; the 5th, `dryfit_driver.py:65`, takes `filename` as a **PARAMETER** -- the one genuinely dynamic loader -- and its **only two callers pass LITERALS** (`:138` `D_00f.advisor_nna_canonical.py`, `:165` `D_04.client_portal_summary.py`), with `dryfit_driver` **never named by the entrypoint at all.**

**LIMB 2 -- every `subprocess` argv resolves to a LITERAL.** `_stage_list` returns hand-enumerated `[sys.executable, "<literal>.py", ...]` tuples; `:506` is literal `c04_validation_battery.py`; `:355` is literal `d_publisher_port.py` whose `--keys` comes from `PERFRP_EMITTER_FAMILIES` -- **a derived KEY list passed as DATA, not a module path.** ✅ **With `exec`/`eval`/`__import__`/`runpy` at ZERO bundle-wide, a `glob` cannot become a dispatch: there is nothing to execute globbed content WITH.**

⛔ **LIMB 3 -- THE CORPUS LIMB, AND IT IS THE ONE ONLY THIS READ HAS.** Every other read, `0.4.0_DS_ClientPlatform~C`'s included, censused **the REPO TREE**. The object under discussion lives in the **DEPLOYED bundle**, and *reading the wrong plane with sound controls is the exact error `0.0.0_AB_MSTR` disclosed one hour earlier.* **MEASURED on `s3://opal-data-49financial/_code/`: 79 objects, 77 `.py`.** Diffed against the censused tree: **2 deployed files ship from OUTSIDE `runners_49f/`** -- `lib/trading_calendar.py`, `ref/etf_classifier.py` -- **which no prior census covered.** Pulled the DEPLOYED BYTES and censused them: **0 of 2 carry any member of the dispatch class** (POSITIVE CONTROL `def ` **2 of 2**; NEGATIVE CONTROL **0 of 2**).

⛔ **AND THE FIRST RUN OF THAT LAST CENSUS WAS A FALSE CLEAN, DISCLOSED BECAUSE A SELF-REPORT IS AUDITED LEAST.** The initial pull wrote to an MSYS `/tmp` path against a native Windows `aws.exe`: **the files landed at 0 bytes, `cp` returned success, and the census printed a perfect all-zero dispatch result.** **An instrument failure rendered as a clean verdict.** It was caught ONLY because the positive control ran and read **0 of 2 carry `def `**. The re-run on a native path is the reported one. **A failed retrieval returns a VALUE (Rule 22a), and this is that trap firing on my own bench.**

✅ **VERDICT: NO PATH IN THE DEPLOYED BUNDLE ASSEMBLES A MODULE NAME AT RUNTIME.** Every loader and every subprocess resolves to a literal filename, on both the runner tree and the two out-of-tree deployed files. **`parity_period_returns.py` is unreachable by the residual class COO named** -- importlib-by-string, runtime-assembled name, or glob+exec.

⚠ **WHAT THIS DOES NOT CLAIM, stated because the whole item is about instruments overselling themselves:** this is a **STATIC read of deployed bytes at ~20:4xZ**. It rules out the mechanism CLASS; **it does not observe a running dispatch**, and it is not a substitute for one. The runner-tree limb is **tracked-only**. `_code/` is SSM-synced with `--delete`, so the corpus is perishable and this verdict ages the moment that prefix changes. ✅ **`0.4.0_DS_ClientPlatform~C`'s DO-NOT-REMOVE call is undisturbed and this seat asked for no removal.**

### CHANNEL INTAKE ON RELAUNCH -- 2026-08-30 00:49-01:2xZ (3.0.0_SA_CVO base, post-reboot; no handoff existed, resumed from the record)

Three items arrived on the channel while the seat was down. Recorded here so the channel has a carrier that is not an inbox file; none is chased by this seat.

| # | from / msg | class x standing | disposition |
|---|---|---|---|
| 24 | `0.4.0_DS_ClientPlatform~N` 83981 -- the BUILD-ONLY c02 `r_gross` sign fix is on the DEPLOYED plane (`s3://opal-data-49financial/_code/c02_twr_engine.py` ETag `2f709fc66ed6cb2e9a853704ef0e83c6` == local md5, 22:02:12Z); the next c02 fire would write ONE corrected partition beside 534 inverted ones under one label | BLOCKING x ARMED -> **DISARMED-BY-OWNER** (`2.0.0_SA_COO` issuer, 84020; `1.0.0_SA_CTO` serve-gate limb RULED 84040) | NOT REMEDIATED. Disposition (a) rollback CLOSED by Andrew's word (LD-0477 A2). Adjudicated by this seat on `1.0.0_SA_CTO`'s tick-69 pitch (D2-T69-1): full-range re-emission + vintage field -- see the MCP verdict of this hour. Time shape: `bd-49f-runner-daily` DISABLED (live read, COO); which chain dispatches c02 is UNREAD -- the "MON 08-31 22:20Z" earliest fire is INFERRED until `~N`/`AE~K` answer COO's one-line ask. |
| 25 | `0.0.0_AB_MSTR` 83988 -- untracked telemetry mis-write `org/tier0/ledger/org/mcp/agent_telemetry/0.0.0_AB_MSTR.jsonl` (1,652 B, 2026-07-15) | OBSERVATION x INERT | CLOSED by `1.0.0_SA_CTO` 84040 item 2: file + three empty parents deleted, hooks now build the path from `${ROOT}` (`.tools/hooks/post-tool-telemetry.sh:87,180`). Class closed at source. |
| 26 | `0.7.0_AE_CloudOps~X` 84046 -- the 21:29:18Z controlled wind-down reached 10 lane inboxes and missed 4 (`0.7.0_AE_CloudOps~X/~K/~L`, `0.8.0_AE_CloudComp~X`), all four demonstrably receiving other mail in the same half hour; the 4 wrote no state block. Denominator 58 base + 101 lane inbox dirs. UNDETERMINED limb: whether the 4 were LIVE at 21:29Z (spawn-audit has no session-END rows). Instrument note worth keeping: a `Msg-ID` censuses ONE DELIVERY (the broker mints one id per recipient); the FILENAME is the broadcast's shared carrier. | OBSERVATION x INERT | Disarms by `0.0.0_AB_MSTR`'s roster read (who was addressed) or by a ruling that lane seats are not wind-down recipients by design. Not chased here. The cost named is the right one: a missed wind-down is a lost state block, not a missed notification. |

Also intake, not channel items: `2.0.0_SA_COO` 84025 (ADVI_INSURE forensics routed to `0.7.0_AE_CloudOps~K`, OBSERVATION copy, ack 84037 read) -- nothing owed by this seat until the RAVC2 lands; it will be read against its own negative control when it does.

| 27 | `0.4.0_DS_ClientPlatform~C` 84434 -- every BDPARITY gate read GO (vendor word 21:23Z; cells ruled @f11fb765ad; cohort @7cd0cc1200) but the DEPLOYED `opal-assets-bd49f-reporting-pull` predates the builder commit 27af942259 by 1d 07:46 (CodeSha256 `0XJf+G2p...`, LastModified 2026-08-28T18:09:29Z) and carries `DRY_RUN "0"` -- a fire would spend the ONE authorized pull on the OLD dateRanges (no YTD, no 1Y, no index join) and read as complete. CONFIRMED at this seat 02:25:33Z on `get-function-configuration` (third instrument; DS~C read it twice, AE~K once). | BLOCKING x ARMED -> **DISARMED-BY-OWNER** (`2.0.0_SA_COO` 84472 amended its own GO to DO-NOT-FIRE; `0.7.0_AE_CloudOps~K` staffed for the Terraform deploy; `1.0.0_SA_CTO` per-apply gate) | NOT REMEDIATED until the re-arm read. Grader's sharpening (MCP this hour): "CodeSha256 CHANGED" is necessary not sufficient; the discriminator is the deployed package member's LF-normalised sha256 == the 27af942259 blob (`66f324ae7c90...`, 26,475 B) with a prior-package negative control, and the live DRY_RUN printed beside it -- the 02:21Z CLOSE (84446) showed this worktree deploys CRLF bytes. The GO's chain had no DEPLOY step and read "DRY_RUN still 1" off the repo default: DESIRED read as APPLIED, caught by three seats before a fire. |
| 28 | `0.4.0_DS_ClientPlatform~C` 84239 / 84410, `4.0.0_SA_CRO` 84380 (i), `0.4.0_DS_ClientPlatform~N` 84376 / 84425 -- `twr_daily` carries 3 of 535 partitions with `r_net`/`r_gross` null-typed and the four operand columns ABSENT (10 of 14 columns): 2024-07-08 (gold floor, EXPECTED), 2025-01-09 (`is_trading_day` False -- a market closure, EXPECTED, established by DS~N), 2026-08-18 (7,315 of 7,315 `REFUSED-NO-BMV` = D-1 valuation NOT LOADED at emission -- the one real input gap). The 10-column shape is the engine's documented all-refused frame (`test_all_refused_frame_omits_the_operand_columns_entirely`). DS~C's first instrument (a per-column type map) could not see an ABSENT column -- an omission is invisible to every presence instrument. | OBSERVATION x INERT | Carried into the C02-g-3 acceptance bar (COO 84439, my 84356): the three print on their own lines outside the 535-of-535 identity count; TWO NAMED ARMS of OPPOSITE polarity -- 2026-08-18 re-emitting POPULATED confirms an emission-time gap (repaired as a side effect), 2025-01-09 MUST come back all-null and a populated return there is a NEW defect (a return manufactured for a closed market). |
| 29 | `ADVI_PERFRP-S17` (filed @30d51fcbac): AC11 waited on the WRONG gate; the relationship->account edge was never absent -- relocated by design to `.verification.json` sidecars (COO @0fe8a898f8). `0.4.0_DE_ClientPlatform~D` 84384: AC11 PASS on the measured join, harness EXERCISED at this seat rc=0, 5 of 5 families 0 mismatches over 13,378 rows, both negative-control arms fire. | BLOCKING (as surfaced) -> INERT -> **REMEDIATED** | No cell was cut; the row's reason corrected on the face; the "as DISPLAYED" wording gap stays on the row by the issuer's ruling (84322). Two lessons banked in the filing: a row whose recorded blocker is the serve gate reads as discharged the moment the serve word lands; and a census that filters its own answer out (`'verification' not in f`) then controls inside the filtered corpus. |

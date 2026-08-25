# ORPHANED BY THE MSTR / COO / CVO CLOSE -- five items whose owners went dead, taken by CTO

**Seat:** `1.0.0_SA_CTO`. **When:** 2026-08-25 ~19:5xZ.
**Why this file exists:** Andrew closed `0.0.0_AB_MSTR`, `2.0.0_SA_COO` and `3.0.0_SA_CVO` at ~19:4xZ.
`0.5.0_AE_OpalETL~B` (71321) and `0.4.0_DS_ClientPlatform~N` (71315) handed over the items whose named
owners are now stale rather than letting them die with the seats.

>> **`~B`'s own sentence is the reason this is a FILE and not a reply: *"That linkage exists only in
>> dead seats' messages and now here."* A message is not a home. This seat has filed the identical
>> failure against itself twice today (`ec532a0158`, `RULE_17b...FOREIGN_COMMIT`) and is not doing it
>> a third time.** <<

**Owner of every item below until reassigned: `1.0.0_SA_CTO`.**

---

## 1. ⛔ ARMED CHAIN -- TWO ITEMS THAT ONLY BITE TOGETHER

**(a) The 3F-S5 lambda-twin deploy.** `vendor-manifest.sh --check` on
`opal-assets-silver-blackdiamond` reads **rc=1, 2 of 8 DRIFT, BY DESIGN**. `~B` disarmed it at the
artifact surface (`vendor_parity_expected_red` in `BUILD_MANIFEST.json` @`a3fb502194`) naming
`0.7.0_AE_CloudOps` as REMEDIATION owner. **COO was to seat it once the P0 cleared. The P0 has
cleared and COO is stale.** DISARMED != REMEDIATED; the gate stays red until someone ships S5.

**(b) CVO's S7** (filed @`23c825d049`): `rebalancer_schemas.py:83`
`PROVENANCE_CONTRACT_START = "2026-07-23"`, guard predicate `date < CONTRACT_START`. **The at-risk
window is 07-23 .. actual-deploy-date -- every row ON OR AFTER the constant, so it PASSES the guard
written to refuse it.** CVO ruled the disarm must attach **BEFORE** the S5 twin ships, because
shipping is the moment it arms. CVO named COO as disarm owner. **Both stale.**

⛔ **THE COUPLING IS THE WHOLE POINT: (a) IS INERT WHILE UNSEATED, AND SEATING (a) WITHOUT (b) ARMS
IT.** Whoever picks up S5 takes S7 in the same hand. **Neither item is dangerous alone; the pair is.**

## 2. ⛔ ARMED LATENT -- AND IT IS ARMED BY A *NORMAL* ACT, WHICH IS THE WORST KIND

`safe_deploy_core.py:217` maps the **whole** `data/assets/scripts/silver` tree ->
`s3://opal-data-mdpf/code/scripts/silver/`. Three modules in that tree genuinely import
`mirror_schemas` (`mirror_conversion:66`, `etf_conversion:65`, `etf_schemas:50`), and
**`mirror_schemas.py` is ABSENT from that prefix.**

It is safe **today** only because none of those three is deployed there -- the prefix holds **2 of the
tree's 38 files**. ⛔ **A routine "deploy the silver tree" puts an unimportable module on the
cottonwood gold legs' PYTHONPATH** (dispatch `:125` syncs `--delete`, `:546` puts `silver/` on the
path). `~B` proposed a marker at the deploy surface, did **not** build it (outside their leg,
plausibly outside their lane), and it is now unowned.

**This is the sharpest item on the page: nobody has to do anything unusual to fire it.**

## 3. TWO TOOL DEFECTS -- D0 / NFRA_DEPLOYLEDGER

**(a) `record-terraform-deploy.sh <pipeline>` has NO notion of a targeted apply.** On a dirty root it
stamps functions that were never applied. **Dry-predicted today: 7 updates, 6 FALSE, two fabricated
from `None`.** `~B` did not run it; both source-map records were hand-scoped. Remedy exists and is
cheap: a `--functions` scope -- **the same one `comp-lambdamap reconcile-deployed` already takes and
which this very script already passes at line 703.**

**(b) The source map drifts silently and NON-UNIFORMLY.** `opal-assets-silver-blackdiamond` had the
DATE wrong and the SHA right; `mdpf-gold-lambda` had **both** wrong (recorded sha `t0w3vTNV0Cp…` vs
live `sNAnYFKGr8d1…`; recorded `2026-08-11T03:20Z` vs live `2026-08-24T12:54:28Z`). **Something
deployed that function on 08-24 running no recorder.** Both instances are closed by `~B`'s two
deploys; **the CLASS is open.**

## 4. RULED -- `mdpf-gold-lambda.last_deployed_commit` = `530ba66971` STANDS

`~B` set it to the **build pin**, which is **not on CLOUD**, and asked for a ruling. **The choice is
correct and I am ratifying it.**

The field's job is to name **the commit whose tree matches the deployed package.** `530ba66971` does;
DS~N's `1234c8779e` does not, because the deployed code deliberately omits D1_CATVIEWS. **Recording
the CLOUD-reachable commit would read clean and be FALSE** -- and `verify-local` reporting
`deployed != HEAD` is **TRUE** and is the signal working.

>> **A record that is conventional and false is worse than one that is unconventional and true.**
>> If the field must hold only CLOUD-reachable commits, that wants a SEPARATE pin field -- an
>> architecture act, not a value swap, and correctly not minted under a P0. <<

## 5. UNOWNED: TOMORROW'S SCHEDULED ACCEPTANCE (`~N`, 71315)

`~N` closed the NEVER#6 ledger @`222fdf3042` on its own stated condition -- met and measured on the
served payload (49financial **12,310** leaf fields compared, 1 differing = `written_at`; inflection
**12,375**, same). **The close is correct: NEVER#6's subject is a HALF-LANDED DEPLOY and that is
discharged.** Holding it open against a future scheduled run would make an unclosed deploy-ledger
mean two different things.

**What is therefore unowned: the 2026-08-26 13:30Z `mdpf-scheduled-floor` run is the PRODUCTION
acceptance** -- today's restoration came from an ad-hoc invocation by this seat, and the ad-hoc/
scheduled law is explicit that ad-hoc artifacts are never production evidence. **Somebody reads that
run.** Taken by this seat.

---

## 6. ⛔ RULED 2026-08-25 ~21:2xZ -- THE IMPORT-HEALTH GAP. SECOND INSTANCE, SAME DAY.

Item 2 above (`safe_deploy_core.py:217`) is **not a one-off.** A second instance surfaced hours later
in a different packager: `0.4.0_DS_ClientPlatform~N` built the D1_CATVIEWS tree **from
`build_package.py`'s own 21-member PACKAGE list**, imported it, and got
`ModuleNotFoundError: No module named 'mdpf_category_registry'` at `mdpf_gold_consolidator.py:84`.

**AND IT PASSED CERTIFICATION.** `2.0.0_SA_COO`'s line, which is the one that generalises:
*"A fully certified round produced an artifact that bricks the Lambda at import."* Both TOs 9/9 PASS,
DS certified @`989a92e806`, DE half certified @`4f1d53fd11` -- **and the code cannot run.**

⛔ **THAT IS NOT A CERTIFIER FAILURE.** Every criterion was checked and every check was honest.
**No criterion asked whether the packaged artifact IMPORTS.** A cert answers the questions the decomp
wrote down and is silent on the ones nobody wrote -- **and "does it run" was not among them.**

**RULING (narrow, deliberately): any decomp whose deliverable is DEPLOYED CODE carries a cell whose
oracle is THE PACKAGED ARTIFACT IMPORTED AND EXERCISED** -- not a source read, not a green gate, not
a verified upload. **`~N` demonstrated the oracle in one command: build from the packager's own
manifest list, import it.**

**THE CLASS, stated without either incident: A MODULE THE CODE IMPORTS, ABSENT FROM WHAT GETS
PACKAGED, IS INVISIBLE UNTIL SOMEBODY BUILDS -- and the agent who builds inherits a break they did
not write.** Two instances, one day, two different packagers.
**The estate has no import-health gate at package time.** Routed to `3.0.0_SA_CVO` as a standing
proof-of-spec question for code-deliverable decomps, and to D0 as a gate candidate. **Owner until
reassigned: `1.0.0_SA_CTO`.**

## THE CLASS, FOR THE NEXT CLOSE

**A SEAT CLOSING IS EXACTLY WHEN AN UNASSIGNED EDGE GOES INVISIBLE.** Every item above had a named,
competent owner an hour ago. Nothing failed; the owners simply stopped existing, and the obligations
lived in message threads that stop being read the moment the thread's participants are gone.
**Two live Tier-2 seats caught this unprompted and handed over rather than assuming someone knew.**
That is the behaviour; this file is its durable half.

---

## 7. RE-READ 2026-08-25 ~23:4xZ -- THE PREMISE OF THIS FILE HAS PARTLY LAPSED

**This file was written because `0.0.0_AB_MSTR`, `2.0.0_SA_COO` and `3.0.0_SA_CVO` were closed.**
**Two of those three are LIVE again.** `2.0.0_SA_COO` is running the wave and `3.0.0_SA_CVO` is on
the surprise channel; `0.7.0_AE_CloudOps~G` and `~J` are live. **`0.0.0_AB_MSTR` is still unmanned.**

>> **AN ORPHAN-TAKING IS A LOAN, NOT A TRANSFER. The condition that justified it can lapse silently,**
>> **and then the taking seat is holding work its real owner is awake and able to do.** Nothing
>> reminded me: the file says "owner until reassigned" and there is no mechanism that notices a
>> named owner coming back. I only re-read it because it was on my own handoff's do-first list. <<

### Item 1 (S5/S7 ARMED CHAIN) -- RE-SEATABLE NOW
`2.0.0_SA_COO` is live and is the seat that was to seat it once the P0 cleared; the P0 has cleared.
`0.7.0_AE_CloudOps` is named REMEDIATION owner for the 3F-S5 half. **`0.5.0_AE_OpalETL~B` reports
(71667) that `24d7c5a465` IS the S5/S7 armed disarm and it is LOCAL, riding integration** -- so the
disarm exists as a commit and is not yet on origin. **The coupling still binds: seating (a) without
(b) ARMS it.** Routed back to `2.0.0_SA_COO` for seating; not re-taken by this seat.

### Item 2 (ARMED LATENT, `safe_deploy_core.py`) -- RE-MEASURED TONIGHT, STILL TRUE
Measured by `1.0.0_SA_CTO` 2026-08-25 ~23:2xZ, four arms:
```
  deploy map      "silver": ("data/assets/scripts/silver", "code/scripts/silver/")   CONFIRMED
  real imports    etf_conversion.py:65, etf_schemas.py:50, mirror_conversion.py:66    3 of 19 .py
                  (`import mirror_schemas as ms` -- word-anchored, not prose mentions)
  repo tree       data/assets/scripts/silver/mirror_schemas.py                        PRESENT
  deployed prefix s3://opal-data-mdpf/code/scripts/silver/                            2 OBJECTS ONLY
                    build_fact_taxsma_report.py, rebalancer_schemas.py -- mirror_schemas.py ABSENT
```
**So the hazard stands exactly as recorded: the three importers are not deployed there, which is the
only reason it is safe today.**

⛔ **AND A CORRECTION I NEARLY MADE AND SHOULD NOT HAVE.** My first read used `grep ... | head -2`,
which cut the output at line 32 of `mirror_conversion.py` -- two PROSE mentions -- and I was about to
correct this file's "three modules" down to two. **`mirror_conversion.py:66` is a real import; the
record was right and my truncated view was wrong.** A word-anchored grep over the whole tree returns
3 importers against 4 files mentioning the token, denominator 19. **The near-miss is the point: I
would have written a FALSE correction into a durable artifact, sourced from a `head -2`, on the same
night this fabric catalogued truncated-view-as-absence five times.** Check before you correct a
record, not only before you write one.

### Items 3, 4, 5, 6 -- unchanged
3 (record-terraform-deploy scoping + source-map drift class) and 6 (import-health) remain with this
seat. 4 is RULED and stands. **5 now has a durable carrier**: `2.0.0_SA_COO` cut
`MDPF_GLOBAL.TO-ACCEPT-0826` @`e70ffcc562`, and this seat has since measured that a seat spawned on
this box shares this worktree (`spawn-agent.ps1` performs NO git operation; 0 matches for
`git clone|pull|fetch` against a FIRING control of 4 on `$ws`), **so the carrier is visible to
tomorrow's seat unpushed.** The 13:30Z acceptance read remains this seat's.

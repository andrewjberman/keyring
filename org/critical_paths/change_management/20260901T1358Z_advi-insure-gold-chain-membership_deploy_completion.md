# Deploy Completion Record
**Date opened:** 2026-09-01T13:58:52.113308+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260901T152119Z
**Deploy:** ADVI_INSURE INSR1DS-AC2 applied limb: relocate the insurance gold producer into the advi tree, conform its argv to the chain idiom, mint it into _code/, and register it LAST in _stage_list
**Authored by:** 0.4.0_DS_ClientPlatform~R
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

> ⛔ **DISARMED 20260901T152800Z — SEE `7d7bade318`. READ THIS BEFORE THE MANIFEST BELOW.**
> **THE STAGE THIS LEDGER CLOSED ON IS NOT LIVE.** Leg L3/L4 registered `insurance_nav_current` in
> `_stage_list`; **seven minutes after this ledger closed, that entry was COMMENTED OUT** and the
> disarm deployed and verified in the served object (0 active references; positive control
> `c02_twr_daily` = 2 active lines).
> **CAUSE — not a defect of this deploy:** the chain runner `bd-exporter-ec2-role` held **0 allows**
> for the insurance silver (`0.7.0_AE_CloudOps~R` 92175, confirmed here on `simulate-principal-policy`
> with a positive control). Root: INS-b-2, the leaf spelling — grants written for `blackdiamond/49f/`,
> silver landing on `blackdiamond/49financial/`. Left armed it was a GUARANTEED `AccessDenied` on the
> first production fire, and the chain is fail-fast, so it would have taken c04's validation battery
> and the ADVI_PERFRP projection with it. Disarmed per NEVER#2 "roll back + escalate loud".
> **CURRENT STANDING STATE:** the producer IS in `_code/` and the roster does NOT reference it —
> present-but-unreferenced, i.e. INERT. Re-arm is uncommenting the one entry, and it is HELD by
> `2.0.0_SA_COO` (92189 s.1); the IAM precondition itself was met at 16:2xZ (`92308`, re-verified
> first-hand: both tables `allowed`, positive control `allowed`, the ungranted sibling
> `fact_insurance_relationshipdetail` still `implicitDeny`).
>
> ⚠ **WHY THIS NOTE EXISTS RATHER THAN THE CLOSE BEING CALLED WRONG (issuer 92310 s.1, ask accepted
> rather than declined).** Every act this ledger names DID happen and "nothing stranded" is true.
> **But its own `Deploy:` line says "register it LAST in `_stage_list`" — a STANDING OUTCOME, not
> merely an event — so a reader is entitled to read it as current state, and would conclude the stage
> is live.** That is the exact carrier shape that cost this fabric all day: records TRUE WHEN WRITTEN,
> still true about their own event, and read as NOW. **A completion ledger whose subject a later act
> reverses must say so on its face, because nothing else will.**

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of the relocation + argv conform + the module-level path fix | commit hash, and the commit-gate result | CLOSED. Commit 8d5cd96653 under 0.4.0_DS_ClientPlatform~R. git mv gold/ -> gold/runners_49f/, history preserved (rename 86%). commit-gate: 'All checks passed! pre-commit gate clean for 1 of 1 file(s)' -- a REAL check, not the 0-of-1 WARN a .md gets. Resolver re-run FIRST-HAND on the ACTUAL post-move path (91655 s.4 required this because 91636's relocated resolution was a HYPOTHETICAL until the file was there): NEW -> ('opal-data-49financial','_code/bd49f_insurance_nav_current.py','advi'); NEGATIVE CONTROL, the OLD path still -> ('opal-data-mdpf',...), so the mapping discriminates on the path rather than always returning advi. REFERENCE CHECK (the (i) consequence 91655 s.4 flagged as unlisted): no importer or invoker of the old path exists. ⛔ AND THE MOVE BROKE THE PRODUCER AT IMPORT -- module level carried a HARDCODED '../silver' depth, so from runners_49f it resolved to gold/silver/ and died rc=1 ModuleNotFoundError. The SAME FILE stated the rule verbatim in _forbidden_census ('Never a hardcoded depth ... fails as ModuleNotFoundError rather than as a path error'). It dies AT IMPORT, BEFORE argparse, so the mandated argv exercise could NOT have caught it -- a relocate/deploy/register without an end-to-end run would have aborted the whole 49F chain by a SECOND route. Fixed with the file's own _workspace_root() walk-up idiom; _forbidden_census now calls it rather than carrying a second copy. | CLOSED 20260901T152001Z |
| L2 | s3-prefix | opal-data-49financial _code/bd49f_insurance_nav_current.py (FIRST MINT, authorized 2.0.0_SA_COO 91655 s.2) | comp-pipescript deployed MATCH row + head-object on the RESOLVED bucket + a 404 negative control on the MDPF path | CLOSED. FIRST MINT authorized by 2.0.0_SA_COO 91655 s.2, scoped RELOCATE-THEN-DEPLOY, never the mint alone. safe-deploy TOOL-03 row: 'DEPLOYED [advi] data/assets/scripts/gold/runners_49f/bd49f_insurance_nav_current.py' + 'VERIFY OK comp-pipescript deployed ...' + 'safe-deploy gate PASS -- all 1 file(s) deployed and verified'. worktree CR 0 / index CR 0 / uploaded: index. READBACK TAKEN AGAINST THE BUCKET THE RESOLVER RETURNS, per 91655's explicit guard that the 91621 readback could not have failed: head-object opal-data-49financial _code/bd49f_insurance_nav_current.py -> ContentLength 22503, LastModified 2026-09-01T13:55:38Z. ⭐ NEGATIVE CONTROL, and it is the one that matters: head-object on the MDPF path opal-data-mdpf code/scripts/assets_gold/bd49f_insurance_nav_current.py -> 404 Not Found, so NOTHING landed in the other firm's bucket -- the cross-firm write my own retracted 91621 ask would have caused did not occur. CONTENT IDENTITY, not mere existence: served bytes LF-normalised sha256 4b5549a81e3932f3 == the git blob at pin 8d5cd96653, with a different file (a00_runner.py, 3a21ca92d14785ac) as the negative control proving the comparison discriminates. | CLOSED 20260901T152001Z |
| L3 | git | CLOUD commit of the _stage_list registration in chain_49f_entrypoint.py | commit hash + AST parse + the stage's argv DERIVED from the file | CLOSED. Commit 2bef200aca under 0.4.0_DS_ClientPlatform~R. commit-gate 'All checks passed! clean for 1 of 1 file(s)'. AST parse OK on the edited entrypoint. PARITY MEASURED BEFORE EDITING rather than assumed: repo and deployed copies were byte-identical LF-normalised sha256 fc829256f45187bf, so the repo edit is what actually runs. THE STAGE'S ARGV WAS DERIVED BACK OUT OF THE COMMITTED FILE rather than trusted to be what I intended to write: parsed entry -> [sys.executable,'bd49f_insurance_nav_current.py','--date',date] + u, with u defined in that same file as ['--upload'] if upload else ['--dry-run'] -- EXACTLY the matrix exercised at L5. Takes u and NOT m: this producer has no --local-out; it writes ONE additive gold table in its OWN subtree gold/advi/insurance/, never under canonical/, so never-blend holds BY CONSTRUCTION. Inserted LAST per 91655 s.5 -- and the code comment records the issuer's own correction that POSITION IS NOT PROTECTION, since c04's battery and the ADVI_PERFRP projection run AFTER the loop and a failure at any position still takes both. | CLOSED 20260901T152054Z |
| L4 | s3-prefix | opal-data-49financial _code/chain_49f_entrypoint.py | comp-pipescript deployed MATCH row + LF-normalised content identity against the git blob at the pin | CLOSED. safe-deploy TOOL-03 row: 'DEPLOYED [advi] data/assets/scripts/gold/runners_49f/chain_49f_entrypoint.py' + 'VERIFY OK comp-pipescript deployed ...' + 'gate PASS -- all 1 file(s) deployed and verified'. worktree CR 0 / index CR 0 / uploaded: index. CONTENT IDENTITY: deployed bytes LF-normalised sha256 77a824fb70e51818 == the git blob at pin 2bef200aca. ⭐ CHANGE-DETECTION CONTROL: the PRE-EDIT sha was fc829256f45187bf, so the deployed value MOVED -- this is not a stale object reading MATCH against an unchanged baseline, which is the failure mode a bare identity check cannot see. THE STAGE IS IN THE DEPLOYED BYTES, not merely in the repo: insurance_nav_current occurs 1x in the object pulled back from S3; NEGATIVE CONTROL, a fabricated token occurs 0x, so the grep discriminates. | CLOSED 20260901T152054Z |
| L5 | verify | the registered stage's EXACT argv accepted, both chain forms | rc=0 on --upload and --dry-run, rc=2 on a bogus flag as negative control, exercised BEFORE L3 landed | CLOSED, and EXERCISED BEFORE L3 LANDED as 91655 s.3 required ('a reasoned fix against an exercised defect is a rung short'). Against the REAL argparse and the REAL polarity resolution -- emit() stubbed, NOT a transcription of the parser: --date D --upload rc=0 -> emit(dry_run=False); --date D --dry-run rc=0 -> emit(dry_run=True); --date D rc=0 -> dry_run=True (default preserved); --date D --write rc=0 -> dry_run=False (existing behaviour unmoved); --date D --upload --dry-run rc=0 -> dry_run=True (FAILS CLOSED). NEGATIVE CONTROL: --bogus still rc=2, so the aliases did not make the parser permissive. MEASURED BEFORE THE FIX: --upload rc=2 and --dry-run rc=2 with native rc=0 as control -- the defect was real and is now closed. END-TO-END at the new path with real emit: rc=0, AC3 census 15 columns / 0 violations CLEAN, 12895 parquet bytes -- byte-identical to the pre-move 2026-09-01 run, so relocation + conform changed no output. ⚠ STATED RATHER THAN LET 'rc=0 on both forms' IMPLY MORE: the --upload form was NOT run end-to-end, because that performs the production gold write 91569 withheld and 91655 did not grant. The stub covers the defect under test (argparse rc=2 aborting a fail-fast chain) without performing the withheld act; the write path stays covered by the two full dry-run days already on the record. | CLOSED 20260901T152054Z |

## Log

- 20260901T135852Z OPENED by 0.4.0_DS_ClientPlatform~R with 5 leg(s)
- 20260901T152001Z LEG L1 closed: CLOSED. Commit 8d5cd96653 under 0.4.0_DS_ClientPlatform~R. git mv gold/ -> gold/runners_49f/, history preserved (rename 
- 20260901T152001Z LEG L2 closed: CLOSED. FIRST MINT authorized by 2.0.0_SA_COO 91655 s.2, scoped RELOCATE-THEN-DEPLOY, never the mint alone. safe-deploy 
- 20260901T152054Z LEG L3 closed: CLOSED. Commit 2bef200aca under 0.4.0_DS_ClientPlatform~R. commit-gate 'All checks passed! clean for 1 of 1 file(s)'. AS
- 20260901T152054Z LEG L4 closed: CLOSED. safe-deploy TOOL-03 row: 'DEPLOYED [advi] data/assets/scripts/gold/runners_49f/chain_49f_entrypoint.py' + 'VERIF
- 20260901T152054Z LEG L5 closed: CLOSED, and EXERCISED BEFORE L3 LANDED as 91655 s.3 required ('a reasoned fix against an exercised defect is a rung shor
- 20260901T152119Z CLOSED -- all 5 legs proven

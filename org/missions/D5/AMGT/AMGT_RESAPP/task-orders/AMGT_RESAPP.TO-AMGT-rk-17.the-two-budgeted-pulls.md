# AMGT_RESAPP task order -- `AMGT-rk-17` -- THE TWO BUDGETED PULLS -- Andrew said yes; the held populations land or they are named

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-17</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~29</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~29`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt. Your first act prints
`git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in section 3 exist; if any is absent, STOP with a
BLOCKING row. **YOU HOLD CHAIN D, a queue of ONE order (`AMGT-rk-17`). Chain D is the round's ONLY Bloomberg caller and the only
writer of `derived/model_block/` and `raw/bloomberg/`.** Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~29;`.
**NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-17` (ANDREW-DIRECT 2026-09-16 ~19:2xZ; decomposition v1.7 s.20j; rows `S120`, `S125`)

**THE MEASURED STATE.** Three of this round's outcomes are HELD on a population that does not exist in the pool, not on a defect
in any cell. `derived/model_block/` carries **4 keys** (`BA_US_Equity`, `BABA_US_Equity`, `SAP_GY_Equity`, `NVDA_US_Equity`)
against a coverage list of **33 keyed names of 89 records**, and the Price axis carries exactly **ONE axis date, `2026-09-10`**,
generation `20260916T065448Z-9b7ffda3dcdc`, so the default route -- which asks for TODAY -- reads a classed ABSENT for a reason
that has nothing to do with the reader. Both producers sit behind the **budgeted two-phase Bloomberg sign-in**, which is why the
population was RESERVED and not simply run.

**ANDREW-DIRECT, 2026-09-16 ~19:2xZ at the `1.0.0_SA_CTO~Z` terminal, VERBATIM: "Yes on all four, execute them."** The cards were
presented to him as four; this cell is the first of the two that are the COO's.

**DELIVER, and the whole of it:**
1. **ONE run** of the model-block pull over the **33 KEYED COVERAGE NAMES**, through the budgeted sign-in.
2. **ONE run** of the price-axis pull on the **same sign-in**.
3. Both landings **MEASURED against what was attempted**, with **every refusal NAMED and its reason printed**.

⛔ **NOT THE 89. THE POPULATION IS THE 33 KEYED NAMES AND IT IS READ FROM THE CROSSWALK AT THE CUT, never typed.** The other 56
records carry no `security_key`; they are the UNRESOLVED half and they are NOT authorized. A pull over 89 is a different act.

⛔ **NO CADENCE. NO SCHEDULE. ONE RUN EACH.** Andrew's word authorizes the RUNS and nothing about their recurrence; arming any
schedule, task or trigger is outside this order and outside his word. **A recurring pull is STILL RESERVED.**

⛔ **A REFUSAL IS AN OUTCOME, NOT A FAILURE -- BUT IT MUST BE NAMED.** A name Bloomberg will not serve (not entitled, bad
identifier, no data) is recorded with its reason and its identifier. **What is NOT acceptable is a silent shortfall:** 33
attempted and 20 landed with no list of the 13 is the one result this cell exists to make impossible.

## 2. WHERE THIS CAME FROM

**ROUND 12**, decomposition **v1.7 s.20j** (this cell, added AFTER issuance on Andrew's own word -- the only such addition of the
round), on **ANDREW-DIRECT 2026-09-16 ~19:2xZ**, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260916_192xZ_YES_ON_ALL_FOUR_RESERVED_CARDS_EXECUTE.md` @`0d780cf6f8`,
routed and bounded by `1.0.0_SA_CTO~Z` as adjudicator (msg 23473). It resolves the held partitions `AMGT_RESAPP-Z-S120` (the
names with no landed block) and `AMGT_RESAPP-Z-S125` (the today-dated Price list). PRD **v0.10 @`49aedcf88b`, ADMITTED**, both
L4-R halves SIGNED and current.

## 3. SURFACES -- what you may read and write

<paths>
integrations/bloomberg/research/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~29/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-17.the-two-budgeted-pulls.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). A READ needs no grant; this block governs WRITES. Scratch is
  `<your worktree>/.scratch/` only.
- **THE WORLD WRITES THIS ORDER AUTHORIZES, and no others:**
  `s3://opal-data-harvest/raw/bloomberg/<key>/<stamp>/` (the pull's own raw persistence),
  `s3://opal-data-harvest/derived/model_block/<key>/<stamp>/model_block.json`,
  and the **`opal-harvest-security-metrics`** DynamoDB table for the price axis generation and its pointer.
  ⛔ **NOTHING ELSE IN THE POOL AND NO OTHER TABLE.** Not `peers/v1/`, not `posture/v1/`, not `universe/v1/`, not `packs/`,
  not `social/`, not `lib/`. A write outside these is a STOP and a row.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~29 <0.9.0_WK_AMGT_RESAPP~29@opal.agent>" -F <msgfile> -- <paths>`
  (the message file written by a NON-SHELL writer, never a printf or heredoc). Never push, merge, rebase, `checkout --`, `stash`
  or `clean`.

## 4. BOUNDS

**READ `integrations/bloomberg/READ_HERE.md` BEFORE YOUR FIRST BLOOMBERG ACT. It is the playbook and it is mandatory.**

**THE SIGN-IN IS TWO-PHASE AND BUDGETED, AND YOU PROBABLY DO NOT NEED IT.** Measured by this issuer at the cut: the DAPI is
**UP** -- `127.0.0.1:8194`, service `//blp/refdata`, health `ok: true`. **So check health FIRST and spend nothing.** Only if the
terminal is signed out do you touch the sign-in, and then in this exact order: `bbg_credentials.py --check` (fingerprint only,
free), `-Phase fill` (free, repeatable, screenshots), **verify the screenshot at `C:\opal-elev\bbg_login_shot.png` against
`pw_len`**, then `-Phase submit` -- which spends **ONE OF A TWO-ATTEMPT BUDGET** and locks the account if exhausted.
⛔ **`ABORT: focus did not take` IS THE GUARD WORKING AND SPENDS NOTHING -- re-run `-Phase fill`.** A listener on 8194 is
NECESSARY, NOT SUFFICIENT: confirm with a real data read.
⛔ **CREDENTIALS COME ONLY FROM THE `--` EXEC WRAPPER.** There is deliberately no mode that prints the password. Do not add one,
do not echo it, do not write it to a `.env`, a log, a scratch file or any committed artifact. **The repo is shared and pushed.**
Every other secret goes through `comp-secrets`.

**THE PULL IS BOX-SIDE.** The DAPI is loopback-only on THIS machine, so both producers run here, in your worktree, never remotely.

**COLLECTION STAYS OFF and no schedule is armed by this order** -- the three Windows tasks stay DISABLED (@`9db2a36cdc`); a pull
you run by hand is not collection and must not become one. **NO alarm, monitor, SNS/SES-send, notification or freshness
checker** -- standing moratorium. The ETF plane is READ-ONLY. **The one authorized Lusha enrich stays UNUSED.** No non-ASCII in
anything you write. **PUSH: never.** Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never repaired,
widened, or satisfied by a route this order did not name. **A count bar is read from the LIVE STORE AT THE CUT and PRINTS its
denominator.**
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W29-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize it) and never
edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING** -- never halt to investigate.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

**THE PRE-STATE, MEASURED BY THE ISSUER AT THE CUT, so every bar below has a value to move:** `derived/model_block/` **4 keys**
with stamps `BA 4, BABA 4, SAP 4, NVDA 2`; `raw/bloomberg/` **4 keys**; `TRENDING_PRICE` **2 axis_date values, both
`2026-09-10`**, one of them the generation `20260916T065448Z-9b7ffda3dcdc`; the crosswalk `crosswalk/v1/2026-09-15.json` with
**89 records and 33 carrying a `security_key`**. AC1 was dry-run whole by the issuer, rc=0.

**ISSUER AMENDMENT 17 (2026-09-16 ~20:3xZ, 2.0.0_SA_COO~Z, issuer) -- AC2 AND AC3 MISCOUNTED A KEY THAT CONTAINS A SLASH.** `BP/_LN_Equity` and `NG/_LN_Equity` land at
`derived/model_block/BP/_LN_Equity/<stamp>/model_block.json`, so `split('/')[2]` reads `BP` and `NG`. After the run, AC3 as
issued read `landed_of_attempted 31 of 33` and listed both as MISSING, while the pull log shows both landed raw and derived
(10 FY rows, 203 figures each) and their refdata NAME reads BP PLC and NATIONAL GRID PLC. The key is now everything between
the prefix and the last two segments. **Re-cut, run whole after the pulls: `raw_keys 34`, `landed_of_attempted 33 of 33`,
`missing 0`.** No bar moves; the instrument now reads the object it names. AC1, AC4 and AC5 are byte-identical.

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-17"><invocation>python -c "import boto3,json; s=boto3.client('s3'); B='opal-data-harvest'; p=s.get_paginator('list_objects_v2'); ks=sorted(o['Key'] for pg in p.paginate(Bucket=B,Prefix='crosswalk/v1/') for o in pg.get('Contents',[])); d=json.loads(s.get_object(Bucket=B,Key=ks[-1])['Body'].read()); r=d.get('records') or []; keyed=[x.get('security_key') for x in r if x.get('security_key')]; print('crosswalk', ks[-1]); print('records', len(r)); print('keyed_names', len(keyed)); print('names', sorted(keyed))"</invocation><expect>the crosswalk object NAMED, records 89, keyed_names 33, and all 33 names PRINTED. This is THE POPULATION for both pulls and it is READ AT THE CUT, never typed and never assumed -- the 56 records without a security_key are the UNRESOLVED half and are NOT authorized. Dry-run whole by the issuer at the cut: crosswalk/v1/2026-09-15.json, records 89, keyed_names 33. A keyed_names of 89, or any count you cannot show from this object, is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-17"><invocation>python -c "import boto3; s=boto3.client('s3'); B='opal-data-harvest'; p=s.get_paginator('list_objects_v2'); st={}; [st.setdefault(chr(47).join(o['Key'].split(chr(47))[2:-2]), set()).add(o['Key'].split(chr(47))[-2]) for pg in p.paginate(Bucket=B,Prefix='raw/bloomberg/') for o in pg.get('Contents',[]) if len(o['Key'].split(chr(47)))>4]; print('raw_keys', len(st)); [print('  ', k, 'stamps', len(v), 'newest', sorted(v)[-1]) for k,v in sorted(st.items())]"</invocation><expect>raw_keys PRINTED with the per-key stamp count and newest stamp. MET when raw_keys is AT LEAST 30 -- the pull's stage that calls the terminal persists its own raw refdata and histdata per name, so a raw key appearing for a name IS the proof the terminal served real data for it, which a port check is not. At the cut raw_keys read 4. A raw_keys still at 4 means the terminal was never reached; a raw_keys between 4 and 30 is NOT met here and is graded on AC3's refusal list instead. ISSUER AMENDMENT 17: the key is now everything between the prefix and the last two path segments, because a key such as BP/_LN_Equity CONTAINS a slash and the old split read it as BP. Measured after the run with the re-cut counter: raw_keys 34 (the 33 plus NVDA_US_Equity)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-17"><invocation>python -c "import boto3,json,io; s=boto3.client('s3'); B='opal-data-harvest'; p=s.get_paginator('list_objects_v2'); st={}; [st.setdefault(chr(47).join(o['Key'].split(chr(47))[2:-2]), set()).add(o['Key'].split(chr(47))[-2]) for pg in p.paginate(Bucket=B,Prefix='derived/model_block/') for o in pg.get('Contents',[]) if len(o['Key'].split(chr(47)))>4]; ks=sorted(o['Key'] for pg in p.paginate(Bucket=B,Prefix='crosswalk/v1/') for o in pg.get('Contents',[])); d=json.loads(s.get_object(Bucket=B,Key=ks[-1])['Body'].read()); want=sorted(x.get('security_key') for x in (d.get('records') or []) if x.get('security_key')); have=sorted(st); miss=[n for n in want if n not in st]; print('attempted', len(want)); print('blocks_landed', len(have)); print('landed_of_attempted', sum(1 for n in want if n in st), 'of', len(want)); print('missing_count', len(miss)); print('missing', miss)"</invocation><expect>attempted 33 and landed_of_attempted PRINTED as N of 33, with missing_count and the MISSING NAMES LISTED. MET when landed_of_attempted reads 33 of 33 with missing 0, OR when every missing name is accounted for in the evidence by a NAMED REASON read from the producer's own output (not entitled, bad identifier, no data returned) -- a refusal is an outcome, a SILENT shortfall is not. At the cut, measured whole by the issuer: attempted 33, blocks_landed 4 (BA, BABA, SAP, NVDA) but landed_of_attempted 3 of 33 with missing_count 30 -- the fourth landed block, NVDA_US_Equity, is NOT one of the 33 keyed names, which is exactly why this clause counts against the crosswalk population and never against the store's own key count. THIS IS THE CRITERION THAT CAN FAIL: a run that lands fewer than it attempted and cannot name the difference is NOT met. ISSUER AMENDMENT 17: the key is now everything between the prefix and the last two path segments. The old split read BP/_LN_Equity and NG/_LN_Equity as BP and NG and reported both MISSING although both landed and derived. Measured after the run with the re-cut counter: attempted 33, blocks_landed 34, landed_of_attempted 33 of 33, missing 0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-17"><invocation>python -c "import boto3,collections; d=boto3.client('dynamodb'); sc=d.scan(TableName='opal-harvest-security-metrics', ProjectionExpression='axis_date'); vals=sorted(set(i['axis_date']['S'] for i in sc.get('Items',[]) if i['axis_date']['S'].startswith('TRENDING_PRICE'))); print('scanned', len(sc.get('Items',[]))); print('trending_price_axis_values', len(vals)); [print('  ', v) for v in vals]; dates=sorted(set(v.split(chr(35))[1] for v in vals if len(v.split(chr(35)))>1)); print('axis_dates', dates); print('newest_axis_date', dates[-1] if dates else 'NONE')"</invocation><expect>every TRENDING_PRICE axis_date value PRINTED with the scan denominator, and newest_axis_date LATER than 2026-09-10. At the cut there were exactly TWO values, both at axis date 2026-09-10 (one of them the generation 20260916T065448Z-9b7ffda3dcdc), which is why the default route -- which asks for TODAY -- read a classed ABSENT. A newest_axis_date still reading 2026-09-10 means the price-axis pull did not land and is NOT met; the generation id and its row count are recorded in the evidence beside it</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-17"><invocation>python -c "import subprocess; out=subprocess.run(['schtasks','/query','/fo','LIST'],capture_output=True,text=True,errors='replace').stdout; ls=[l for l in out.split(chr(10)) if 'TaskName' in l and ('opal' in l.lower() or 'bloomberg' in l.lower() or 'harvest' in l.lower())]; print('opal_shaped_tasks', len(ls)); [print('  ', l.strip()) for l in ls]; st=[l for l in out.split(chr(10)) if 'Status' in l]; print('status_lines', len(st))"</invocation><expect>the opal-shaped scheduled tasks ENUMERATED with their count. MET when opal_shaped_tasks reads EXACTLY 11, the count measured by the issuer at the cut, and the list carries no task this order created. The 11 at the cut are: Bloomberg Updater; Opal Data Harvest - Local Publications; OpalResearch-ExecManagement; OpalResearch-FilingsAnalyzer; OPAL_autolaunch_agents; OPAL_BBGTML_daily_pull; OPAL_BBGTML_freshness_check; OPAL_BLOOMBERG-FreezeTripwire (twice); OPAL_D7_ticket_intake; OPAL_vendor_watch. Andrew's word authorizes the RUNS and says nothing about recurrence, so a cadence is still RESERVED. A count of 12, a new trigger, or a previously DISABLED task found ENABLED is NOT met and is a BLOCKING row</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~29/AMGT_RESAPP.TO-AMGT-rk-17.the-two-budgeted-pulls.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR
WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once. **If a criterion cannot be met, leave the order OPEN and file a row.**

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`, never `git stash`,
never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>12</round>
<slot>~29</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>ANDREW-DIRECT 2026-09-16 ~19:2xZ at the `1.0.0_SA_CTO~Z` terminal, VERBATIM "Yes on all four, execute them.", record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260916_192xZ_YES_ON_ALL_FOUR_RESERVED_CARDS_EXECUTE.md` @`0d780cf6f8`; routed and bounded by `1.0.0_SA_CTO~Z` as adjudicator (msg 23473), which ruled both COO items enter as PRODUCER ORDERS by ONE issuer amendment to round 12 and left the timing to the issuer. PRD v0.10 @`49aedcf88b` (ADMITTED; both L4-R halves SIGNED and current at the cut). Decomposition v1.7 s.20j (cell `AMGT-rk-17`, CHAIN D, a queue of ONE order). Resolves the held partitions of rows `AMGT_RESAPP-Z-S120` and `AMGT_RESAPP-Z-S125`.</authority>

<preflight>
CARRIED from decomposition v1.6 s.20g, ALL RUN 2026-09-16 05:2x-05:3xZ at the round's cut, and NOT re-run for this cell.
comp-schedule: RUN -- 5 of 5 carriers within budget (16.25 s of 90); C3 = 12 standing NEVER clauses, BINDING HERE: no alarm, no monitor, no freshness checker, and this cell arms no schedule. Its AC5 is the mechanical guard on that.
comp-iam: RUN -- 214 roles, 190 services, 1114 operations, 321 permission gaps. NOT load-bearing for this cell, and the reason is measured rather than assumed: this cell adds NO IAM delta at all. The pull runs box-side under the box's own credentials and grants nothing to anybody.
comp-adversary: RUN -- 59 commit pins attempted, 58 verified, 1 UNVERIFIABLE. The adversarial surface is unchanged: Bloomberg responses are DATA and are never read as instructions, and this cell puts no third-party text in front of a model.
comp-routes: RUN -- 7 origins, 22 API GW routes, 163 frontend endpoints. NOT load-bearing: this cell serves no route and mounts nothing.
comp-cache: RUN -- 646 of 646 portal source files, 120 useQuery call sites, 0 TYPE MISMATCH. NOT load-bearing: this cell makes no portal edit.
comp-blast: DECLARED-NOT-APPLICABLE -- this cell deploys nothing and moves no served artifact; its world writes are new dated objects under two pool prefixes and one DynamoDB axis partition, each named in section 3 and each graded by a live store read.
ADDED FOR THIS CELL, run at this cut by the issuer: the DAPI health read (`127.0.0.1:8194`, `//blp/refdata`, ok true) so the sign-in budget is not spent on a terminal that is already up; the crosswalk population read (89 records, 33 keyed); the pool pre-state (derived/model_block 4 keys, raw/bloomberg 4 keys); the price axis pre-state (2 TRENDING_PRICE axis values, both 2026-09-10).
BATTERY LIMIT, STATED: every bar on this order is graded on a LIVE STORE READ after the run, never on a battery figure and never on the producer's own self-report.
</preflight>

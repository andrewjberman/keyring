# AMGT_RESAPP task order -- `AMGT-ri-1` -- THE ERROR/EMPTY BOUNDARY -- a settled request error is not an empty day

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ri-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~16</issued_to>
<issued_by>2.0.0_SA_COO~W</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~16`.** Work ONLY in the worktree whose absolute path is given to you in your
spawn prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/` and `.tools/` exist;
if either is absent, STOP with a BLOCKING row -- you are on the wrong base and every path below resolves to
nothing. **YOU HOLD A QUEUE OF TWO ORDERS (`ri-1`, then `ri-3`); this is the first.** Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~16;`.

**YOUR PORTAL CHECKOUT.** `portal/` inside your worktree is a portal-repo worktree at `a845a8be75`
(`refs/drains/rg-2-portal`, the whole Security Analysis page) on the branch `wk-amgt_resapp-10-1-portal`, and
`portal/node_modules` is a DIRECTORY JUNCTION to the main tree's installed packages (`typescript`, the `tsc`
binary, `vite`, `react`, `react-dom` resolve through it; verified before your spawn). ⛔ **NEVER RUN AN INSTALL** --
no `bun install`, no `npm install`, no fetching `npx`; the junction writes through into a directory five other
seats depend on. A package that reads ABSENT is a row, never an install. ⛔ **The superproject `portal` gitlink
NEVER moves:** commit in the superproject with `--only -- <paths>` so the gitlink is never staged, and commit your
portal work INSIDE `portal/` on its own branch (below).

## 1. THE CELL, inlined in full -- `AMGT-ri-1` (row `Z-C-S169`, serving FWD-15 and FWD-9)

**THE DEFECT, MEASURED BY `3.0.0_SA_CVO~Z` ON THE ACTUAL COMPONENTS AT portal `a845a8be75`:** `LeadPanel` computes
`rows = rankingQuery.data?.rows ?? []` and passes `isLoading` -- but NO error -- to `RankedList`. A SETTLED REQUEST
ERROR therefore becomes an empty array, and `RankedList` renders the SAME 205-byte HTML for a failed read and for a
successful empty day: *"No ranked names for this combination yet -- the daily job has not written a row for
today's date."* That sentence asserts something about the PRODUCER on the strength of a request that never
returned. Loading (126 bytes) and populated (1239 bytes) separate correctly; error and empty do not
(`org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND9_CVO_RENDER_20260914_Z.json`, checks
`error_equals_empty: true`).

**WHY IT MATTERS MORE THAN A WORDING:** the served page's ranked read has been ERRORING at the edge for every
request this page has ever made (the scoped API is not deployed -- another cell's finding), and this boundary
rendered that as "no data today". A read failure that claims producer absence hides two different upstream
failures behind one honest-looking sentence.

**DELIVER, and nothing wider:**
1. `LeadPanel.tsx` carries the SETTLED ERROR separately from data: pass the query's error state (for example
   `readError={rankingQuery.isError ? (rankingQuery.error as Error) : null}`) to `RankedList` AND to `StarredList`
   (which composes `RankedList`). Keep `isLoading`, keep `rows` in producer order, derive NOTHING.
2. `RankedList.tsx` renders an EXPLICIT READ-FAILURE state when `readError` is set -- text that names it as a
   READ FAILURE and says what it does NOT know (the producer's rows, if any, were not read), carrying the error's
   message and, where present, its HTTP status -- and that state must NOT contain the words "daily job". Loading
   and populated render exactly as before. The empty state's text stays as it is for a genuinely empty
   successful read.
3. `StarredList.tsx` shows the same read-failure state before it filters; it must not say "None of the starred
   names carry a producer rank" about a read that failed.
4. A HARNESS in the CVO's own method, `portal/src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs`,
   modelled on `org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND9_CVO_RENDER_20260914_Z.cjs` (READ it;
   it is named in your `<paths>`): transpile the ACTUAL `LeadPanel.tsx`, `RankedList.tsx` and `StarredList.tsx`
   with the installed `typescript`, static-render with `react-dom/server`, stub `../hooks/useLeadPanelApi`,
   `@/ui/components/panels`, `@/ui/components/Select`, `@/hooks/useAuth`, `@/lib/utils`, `./RankedChart` and
   `./SecurityOverlay` exactly as the CVO's script does, and resolve its base from the script's own location
   (`path.resolve(__dirname, '../../../..')`), never a hardcoded `C:/tmp` path. Render SIX states --
   `successful_empty`, `failed_request` (isError true, `error: new Error('HTTP 401: controlled rejected
   request')`), `loading`, `populated` (one row, ticker `RI1-CONTROL`), `starred_successful_empty`
   (starredOnly true, starred set {`RI1-STAR`}, rows []) and `starred_failed_request` (starredOnly true, same
   set, isError true) -- print each state's `bytes` and `sha256`, and print ONE JSON object of checks:
   `error_differs_from_empty`, `error_names_read_failure` (the failed_request HTML contains `read fail`,
   case-insensitive), `error_claims_no_daily_row` (contains `daily job`), `loading_differs`, `populated_differs`,
   `populated_names_security` (contains `RI1-CONTROL`), `starred_error_differs_from_starred_empty`. Exit 1 if
   any of the first seven reads the wrong way (`error_claims_no_daily_row` must be false; the rest true).
   ⭐ **RUN IT BEFORE YOU EDIT THE COMPONENTS (AC1) AND AGAIN AFTER (AC2).** The pre-edit run must REPRODUCE
   the collision (`error_differs_from_empty: false`) or your harness is not measuring the thing the CVO
   measured, and every later PASS is worthless.

**NO RANKING IS DERIVED, NO QUERY KEY CHANGES, NO NEW DEPENDENCY, NO PACKAGE.JSON EDIT.** `.sort(` counts in the
three components stay exactly what they are at the pin (one deliberate alphabetical sort of UNRANKED starred
names in `StarredList`, and whatever the pin carries in `RankedList`); AC5 prints the pin's count beside yours.

## 2. WHERE THIS CAME FROM

**ROUND 10**, cut by `2.0.0_SA_COO~W` from `1.0.0_SA_CTO~Z`'s L10 round-9 analysis
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round9.md` @`e9d1c6e6a5` (s.6: *"The substance is
Z-C-S169 ... and Z-S72"*), decomposition s.18 (v1.1). Round 9's single cell (`rh-1`) proved the assembled route
compiles, builds and serves; its judgment criterion AC6 was graded FAIL because this boundary cannot tell a
failure from an empty day. Rounds 7 and 8 proved the component join (183/183) and the chart's incomplete-read
signal at the component; this cell is the same shape one boundary over.

## 3. SURFACES -- what you may read and write

<paths>
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/components/RankedList.tsx
portal/src/pages/SecurityAnalysis/components/StarredList.tsx
portal/src/pages/SecurityAnalysis/__harness__/
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/constants.ts
portal/src/pages/SecurityAnalysis/hooks/useLeadPanelApi.ts
org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND9_CVO_RENDER_20260914_Z.cjs
org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND9_CVO_RENDER_20260914_Z.json
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ri-1.the-error-empty-boundary.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1): you are admitted to exactly those paths. Do not
  route around a missing path; file a row and stop on that criterion. Your `deliverables/0.9.0_WK_AMGT_RESAPP~16/`
  home needs no entry -- the tree convention grants it. `types.ts`, `constants.ts`, `useLeadPanelApi.ts` and the
  two CVO files are READ-ONLY for you. `portal/node_modules` is a junction and NOT a write surface.
- **COMMITTING PORTAL WORK:** inside `portal/`, on branch `wk-amgt_resapp-10-1-portal`, with
  `cd portal && git add -- <the files you changed> && git commit --author "0.9.0_WK_AMGT_RESAPP~16 <0.9.0_WK_AMGT_RESAPP~16@opal.agent>" -F <msgfile> -- <those files>`,
  the message file written with the Write tool. Prior workers on this page committed exactly so (`83995ea9`,
  `a845a8be` are `0.9.0_WK_AMGT_RESAPP~13`'s). Never push. Never touch the portal remote.
- **COMMITTING SUPERPROJECT WORK** (your instance, rows, the status flip): `bash .tools/safe-commit.sh --author
  "0.9.0_WK_AMGT_RESAPP~16 <0.9.0_WK_AMGT_RESAPP~16@opal.agent>" -F <msgfile> -- <paths>`, never staging `portal`.

## 4. BOUNDS

**PORTAL FROZEN both fabrics, PROD and DEV: COMMIT YES / PROMOTE NO.** No push, no gitlink move, no DEV/PROD merge,
no deployment. A local commit on a worker branch is not a publish. `C-SERVER-SIDE-RANKING`: nothing here sorts,
scores or re-ranks. No vendor call, no network fetch of any kind. **No non-ASCII** in any file you write (AC5
counts it). No monitor, alarm or notification. This cell makes FWD-15 and FWD-9 REACHABLE and grades NEITHER
REALIZED; a person must still have used the page.

**THE REFUSAL CLAUSE.** A criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement in your
instance and a row; never repair it, widen it, or satisfy it by a route this order did not name. Round 8's
workers refused five criteria and every refusal found a defect in the order rather than in the work.

**SURPRISE ROWS**, quoted from the channel's own header so no identity is invented: *"a seat's row is
`AMGT_RESAPP-Z-S<k>`; a worker's row is `AMGT_RESAPP-Z-W<n>-S<k>` with `<n>` its slot; `<k>` restarts at 1 per
coordinate. `"project": "AMGT_RESAPP"` and `"fabric": "site-z"` on every new row."* Your coordinate is `W16`; your
first row is `AMGT_RESAPP-Z-W16-S1`. Append INSIDE the one fenced JSON array of the investigation file, per
`org/surprise_channel/schemas/investigation_item.schema.json`; never edit an existing row; keep working.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ri-1"><invocation>cd portal && timeout 110 node src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs; echo rc=$?</invocation><expect>THE PRE-EDIT ARM, run with the three components still at their pinned bytes: the checks JSON prints error_differs_from_empty false and error_claims_no_daily_row true, with failed_request and successful_empty carrying the SAME sha256, while loading_differs, populated_differs and populated_names_security print true; rc=1. STOP: if error_differs_from_empty prints true BEFORE you edit anything, your harness is not rendering the actual components through the actual query hook and is NOT measuring the CVO's defect -- fix the harness, never the components, until this arm reproduces the collision</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ri-1"><invocation>cd portal && timeout 110 node src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs; echo rc=$?</invocation><expect>THE POST-EDIT ARM, the same instrument on the repaired components: error_differs_from_empty true, error_names_read_failure true, error_claims_no_daily_row false, loading_differs true, populated_differs true, populated_names_security true, starred_error_differs_from_starred_empty true; six distinct states printed with bytes and sha256; rc=0. STOP: the loading and populated sha256 values must be UNCHANGED from AC1's run (the repair touches only the error arm); a moved loading or populated hash is a regression and is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ri-1"><invocation>cd portal && timeout 110 ./node_modules/.bin/tsc -b --force --listFiles --pretty false > ../.scratch/ri1.tsc.out 2>&1; echo rc=$?; python -c "t=open('../.scratch/ri1.tsc.out',encoding='utf-8',errors='replace').read().splitlines(); print('files', sum(1 for l in t if l.rstrip().endswith(('.ts','.tsx'))), 'errorTS', sum(1 for l in t if 'error TS' in l))"</invocation><expect>rc=0, errorTS 0, and files in the LOW THOUSANDS. STOP: a files count of 0 or a small number is the vacuity defect that let round 6 ship (a references-only root examines zero files and therefore cannot fail) and is NOT met whatever errorTS says</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-ri-1"><invocation>cd portal && git diff --name-only a845a8be75 HEAD -- src/ && printf "portal-branch %s\n" "$(git rev-parse --abbrev-ref HEAD)"</invocation><expect>run AFTER your portal commit: EXACTLY these paths and no others -- src/pages/SecurityAnalysis/components/LeadPanel.tsx, src/pages/SecurityAnalysis/components/RankedList.tsx, src/pages/SecurityAnalysis/components/StarredList.tsx, src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs (plus at most one fixture file under __harness__/ if the harness needs one) -- and portal-branch wk-amgt_resapp-10-1-portal. A path outside src/pages/SecurityAnalysis/ is NOT met; an uncommitted change (the list empty while your working tree is dirty) is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-ri-1"><invocation>cd portal && python -c "import subprocess; fs=['src/pages/SecurityAnalysis/components/LeadPanel.tsx','src/pages/SecurityAnalysis/components/RankedList.tsx','src/pages/SecurityAnalysis/components/StarredList.tsx']; [print(f, 'nonascii-now', sum(1 for b in open(f,'rb').read() if b>127), 'sort-now', open(f,encoding='utf-8').read().count('.sort('), 'sort-pin', subprocess.run(['git','show','a845a8be75:'+f],capture_output=True,text=True,encoding='utf-8').stdout.count('.sort(')) for f in fs]; h='src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs'; print(h, 'nonascii-now', sum(1 for b in open(h,'rb').read() if b>127))"</invocation><expect>nonascii-now 0 on all four files, and for each component sort-now EQUAL to sort-pin (the pin carries 0 / 1 / 1 for LeadPanel / RankedList / StarredList; measured by the issuer before this cut). A sort count that MOVES is a ranking derived or removed on the client and is NOT met; any non-ASCII byte is NOT met</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-ri-1"><invocation>cd portal && for p in .bin/tsc react react-dom typescript vite; do printf "%s %s\n" "$p" "$(test -e node_modules/$p && echo PRESENT || echo ABSENT)"; done; printf "NEG %s\n" "$(test -e node_modules/zzznosuchpkg && echo PRESENT || echo ABSENT)"; git -C .. ls-files -s portal | cut -c1-60</invocation><expect>five markers PRESENT, NEG ABSENT, and the superproject gitlink line reading e85f6eb84f3a1771a37011a7e77e372570bad02a, unmoved. STOP: PRESENCE is the instrument and a COUNT is not -- node_modules is a junction and a directory listing enumerates the reparse point as ONE entry; the NEG line is what makes the five PRESENT lines evidence. A marker reading ABSENT is a BLOCKING row, never an install; a moved gitlink is a hard stop</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-ri-1" judgment="true"/>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** `AC7` is a judgment criterion:
record it `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO~W`, and offer no verdict. It
asks whether the read-failure text a PERSON sees is honest -- names the failure, claims nothing about the
producer, and is unmistakably not the empty day -- which the CVO grades at L9 on your rendered bytes.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~16/AMGT_RESAPP.TO-AMGT-ri-1.the-error-empty-boundary.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6,AC7` from inside that worktree (rc 0 is the
verdict); copy the harness's post-edit output beside it as `errorEmpty.harness.post.txt` and the pre-edit output
as `errorEmpty.harness.pre.txt`; flip `<status>` to `complete`; commit instance, deliverables and flip with
`--only -- <paths>` in the superproject (the portal work is already committed on its own branch). Report once in
your final message, naming BOTH commits (superproject and portal) with their branches. **If a criterion cannot be
met, leave the order OPEN and file a row.**

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES (copy the three files to `.scratch/` before editing) and
restore from that snapshot if you must. Never `git checkout --`, never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>10</round>
<slot>~16</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>`1.0.0_SA_CTO~Z`'s L10 round-9 analysis @`e9d1c6e6a5` (verdict NO PRD ADDENDUM; coverage 15 declared, 0 unserved with run-time negative controls; AC6 FAIL ACCEPTED; "Round 10 is authorized on the COO's recut, ONE issuance covering every cell"), answering `3.0.0_SA_CVO~Z`'s slug REMEDIATION_v9 @`1ae76e9c83` (row `AMGT_RESAPP-Z-C-S169`, remedy: "Recut the existing Lead Panel error boundary: carry settled request errors separately from successful empty data, show an explicit read failure without claiming producer absence, and preserve populated/loading states. Exercise all four on the actual component with error-versus-empty unequal and populated still visible."). Cell set and subtraction: decomposition s.18a over the EIGHT OPEN remedy rows of REMEDIATION_v9 read AT HEAD. Fan-out: s.18e. Andrew-direct 2026-09-14 ~23:2xZ at the `1.0.0_SA_CTO~W` terminal, record @`ce7371d0b3`: the `~W` lanes for this project's round 10. Portal freeze: Andrew-direct 03:21:46Z, "no promote", carried verbatim.</authority>

<preflight>
ALL RUN 2026-09-15 00:3x-00:4xZ at this cut (decomposition s.18g). None declared-not-applicable among the core three.
comp-schedule: RUN (--drift) -- 5 of 5 carriers within budget (15.2 s of 90); REACHED-DENOMINATORS C1=23, C2=9, C3=12, C4=21, C5=334; 9 OPEN deploy-ledger entries = 9 ARMED gates, none this project's; BLIND on C4 (SEMI-DECIDABLE) and C5 (NOT-DECIDABLE) in the tool's own voice. This cell deploys nothing and schedules nothing.
comp-iam: RUN (gaps) -- 838 call(s) verdicted across 98 mapped role(s); 629 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED, NOT CLEARED), 14 UNGRANTED, 2 GRANTED-ACTION/UNGRANTED-RESOURCE; 15 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 32 services; BLIND on 266 calls in 26 role-UNMAPPED services. This cell makes no AWS call.
comp-adversary: RUN (compose on the decomposition, --no-packet) -- 32 commit pins, 9 repo paths, 6 file:line cites; 15 hex runs not parsed as pins (named); T11 NOT RESOLVED (the artifact is the decomposition; 236 uncited directory siblings, CAP 25 declared); stage 4 disabled by the caller; freshness BEHIND on a pinned source no cell consumes.
comp-cache: RUN (collisions) -- 481 of 481 portal files, 119 of 119 useQuery sites; this cell adds NO query key (props only).
comp-blast: DECLARED-NOT-APPLICABLE -- the page exists on no DEV/PROD head; two components change props inside one route.
</preflight>

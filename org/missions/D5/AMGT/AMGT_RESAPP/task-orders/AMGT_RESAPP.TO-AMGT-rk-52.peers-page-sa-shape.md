# AMGT_RESAPP task order -- `AMGT-rk-52` -- the Peers tab renders Seeking Alpha's shape: 17 of 17 declared columns, a source label on every cell, not-meaningful shown as such, summary rows with their source mix

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-52</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~52</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; it edits portal source
  and runs an offline render harness; the standing no-monitor moratorium is unaffected.
comp-iam: DECLARED-NOT-APPLICABLE -- this order performs no cloud act at all: it commits portal source on the DEV
  submodule branch and reads ONE pool object to build a fixture; it grants nothing, provisions nothing, deploys
  nothing (nothing deploys to DEV by design; the PROD promote is Andrew's and deferred).
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~52`, continuing.** Second and last of chain P's tail queue. **BEFORE YOU BEGIN, confirm
your own `AMGT-rk-51` is `complete` at HEAD and that `AMGT-rk-50`'s object `s3://opal-data-harvest/peers/v1/CAT_US_Equity/`
carries `basis: "sa"`** -- the fixture below is captured from it; if it is absent, STOP and file a row. Confirm your
worktree has `portal/` CHECKED OUT on branch `DEV` (`git -C portal rev-parse --abbrev-ref HEAD` prints `DEV`; the
issuance says which worktrees are provisioned with it, per R14-T6) -- if not, STOP with a row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~52;`. **NEVER RUN AN INSTALL** (`bun install` for the existing lockfile
excepted, only if `portal/node_modules/.bin/tsc` is absent).

## 1. THE CELL, inlined in full -- `AMGT-rk-52` (R14-P3; FWD-8; Peers brief item 6 and rows P2, P3, P6)

**THE ANALYSIS ROW, verbatim** (`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round13.md` @9c8e04cd9a `:138`):
*"P3 the page renders SA's shape with per-cell source labels"*. The brief's build item 6 (`BRIEF_PEERS_CURRENT_TO_DESIRED_20260918.md:164`
@a2fdbad164): *"The page renders SA's shape -- the column set, per-cell source labels, and not-meaningful cells shown as
such."* The contract clauses the page must honour, `C-PEER-SET-SA` PRD v0.13 @1699960261: TABLE (`:623`, 17 of 17
declared, Preferred + Minority ONE column), SOURCE RULE (`:626-628`: *"Every cell carries `source` = `SA` | `BBG` |
`SA_FALLBACK:<field>` ... every Average / Median / Min / Max row prints its source mix"*), NOT MEANINGFUL (`:629-630`:
*"shown as such (ABSENT with SA's reason) and never zero-filled"*).

**THE MEASURED CURRENT STATE, portal DEV @625a0888 (`git -C portal rev-parse --short HEAD` at the cut):**
- `portal/src/pages/SecurityAnalysis/types.ts:390` `PeerBasis = 'analyst' | 'derived' | 'absent'` -- `sa` is not a type;
  `:407-420` `PeerMember` carries twelve scanner keys and no `cells`; `:442-450` `CscColumnsMap`; `:462-479` `PeerSet`.
- `portal/src/pages/SecurityAnalysis/cscTable.ts:30-32` `MEMBER_FIELD_FOR_CODE = { mkt_val_sec: 'market_cap_musd' }` --
  the ONLY column value a member row carries today; `buildCscTable()` `:86-161` derives `PRESENT_CARRIED` from that map
  (`:97-109`), reads values through `valueOf()` `:80-84`, and computes the four summary rows over member values with `n`
  (`:137-150`) and NO source mix.
- `portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx:56-66` renders the basis badge for `analyst` / `derived` only;
  `cellText()` `:39-44` prints `ABSENT` / `UNMAPPED` / `not carried` / `--` / the number -- there is no source label and
  no not-meaningful state; summary cells `:104-118` print `value (n=k)`; the counts line `:122-126` says *"as R-1's map
  says"*. Dark container (`Panel variant="mixed"` = the band, portal `CLAUDE.md` known divergence), so the white idiom
  is legal HERE and only here.
- `portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs:1-57` is the INSTRUMENT this order copies: the real
  components transpiled with the installed `typescript` (`:127`, `load()` `:132`) and rendered by the real
  `react-dom/server`, hooks stubbed with captured adapter bytes (`tabsFixture.<KEY>.json`, `:50-57`), every expected
  count read OFF THE FIXTURE, verdict lines `CHECKS-OK N of N` / `CHECKS-WRONG-WAY ...` with `process.exitCode = 1`
  (`:483-501`). No browser, no HTTP, writes no file.
- The adapter `lib/research/api/scoped_amgt.py:1244-1278` `read_peer_set()` serves the landed R-1 object WHOLE
  (`served = dict(document); served["peer_read"] = record`, `:1276-1278`) on `/peers` (`:3331-3334`, plus `identity`) --
  so `rk-50`'s new fields (`basis: "sa"`, `members[].cells`, `members[].sa_slug`, `csc_columns.sa_shape`,
  `source_counts`) already ride to the page. **The adapter is NOT your surface and needs no change.**
- `rk-50`'s object shape (its order, section 1 step 1): every row (`subject` and each of 5 `members`) carries
  `cells: {<declared CSC column>: {value, source, meaningful, reason, derivation, sa_field|bbg_field}}` over all 17
  declared columns, `Preferred` and `Minority` both `merged_into: "other_cap_struct"`; `csc_columns.sa_shape =
  {rendered_columns: 16, declared_covered: "17 of 17", merged: {...}}`.

**RULED -- what you build:**

1. **`types.ts`:** `PeerBasis` gains `'sa'`; a new `PeerCell { value: number | null; source: 'SA' | 'BBG' | string | null;
   meaningful?: boolean; reason?: string | null; derivation?: string | null; sa_field?: string; bbg_field?: string;
   merged_into?: string }` (the `string` arm carries `SA_FALLBACK:<field>`); `PeerMember` and `PeerSubject` gain
   `cells?: Record<string, PeerCell>`, `sa_slug?`, `sa_company?`, `name_agreement?`; `CscColumnsMap` gains
   `sa_shape?: { rendered_columns: number; declared_covered: string; merged: Record<string, string> }`.
2. **`cscTable.ts`:** when the set carries `cells` on its rows, a declared column is `PRESENT_CARRIED` if ANY row's
   `cells[column]` exists (the `MEMBER_FIELD_FOR_CODE` path stays for the `derived` basis, untouched); a merged pair
   renders ONCE under the label `Preferred + Minority` with `declared` still counting both (the counts line prints
   `16 rendered covering 17 of 17 declared`); `CscRow.values` becomes per-cell `{ value, source, meaningful, reason }`
   (or the old number for the derived basis, adapted at one seam); each summary row gains `sources: Record<string,
   number>[]` per column (the mix of `source` values over the member cells it averaged, `SA_FALLBACK:*` grouped as
   `SA_FALLBACK`) and excludes not-meaningful and absent cells from its n. A value with `meaningful === false` is NEVER
   a number in any statistic.
3. **`PeersTab.tsx`:** the basis badge renders `Seeking Alpha` for `sa` (a third badge, the same idiom as `:59-66`);
   every carried cell renders its value AND a source label in a span element carrying the attribute
   `data-cell-source` = `SA` | `BBG` | `SA_FALLBACK:{field}` (visible text: `SA`, `BBG`, or `SA:{field}` for a
   fallback); a `meaningful: false` or absent cell renders `n/m` with the reason as its `title` attribute and
   `data-cell-state` = `not-meaningful` -- never `0.00`, never `--` alone; every summary cell renders
   `value (n=k; SA k1 / BBG k2 / SA_FALLBACK k3)` listing only nonzero sources; the counts line adds `rendered 16
   covering 17 of 17 declared (Preferred + Minority merged: other_cap_struct)` when `sa_shape` is present; the
   per-column reasons list keeps rendering ABSENT / not carried columns for the derived basis. Colour law: you are
   inside the band-valued `Panel variant="mixed"`; keep the existing `text-white*` idiom and add no light text outside
   it (`portal/CLAUDE.md`, C3/C5).
4. **`__harness__/peersTab.harness.cjs` (new) + `__harness__/peersFixture.CAT_US_Equity.json` (new):** the fixture is
   the `/peers` leaf payload for CAT built exactly as `read_peer_set()` + the route would serve it: the newest
   `peers/v1/CAT_US_Equity/*.json` object read with boto3 (a READ needs no grant), plus `peer_read: {"status": "SERVED",
   ...}` and `identity: {"security_key": "CAT_US_Equity", "resolution": "UNRESOLVED", ...}` as the crosswalk resolves it
   today; the file's `capture` field names the pool key and its `document-sha256`. The harness copies
   `tabs.harness.cjs`'s loader and stubs, renders `PeersTab` with `usePeerSet` returning the fixture, and ALSO renders
   it with TWO PLANTED MUTATIONS of the same fixture in memory: (m1) one member cell set to `{value: null, source: null,
   meaningful: false, reason: "SA: negative forward earnings"}`, (m2) one member cell's `source` set to
   `"SA_FALLBACK:revenue_growth3"`. It prints, every count read off the fixture: `FIXTURE CAT_US_Equity sha256=...`,
   `COLUMNS rendered R covering D of D declared` (R and D from `sa_shape` and `columns`), `CELLS with source label k of
   N` (N = member rows x rendered columns, from the fixture), `NOT-MEANINGFUL m1 renders n/m and never 0.00: PASS|FAIL`,
   `FALLBACK m2 label SA:revenue_growth3 rendered: PASS|FAIL`, `SUMMARY 4 rows each with a source mix: PASS|FAIL`,
   `BASIS badge Seeking Alpha: PASS|FAIL`, `DERIVED-BASIS fixture BA_US_Equity still renders (regression): PASS|FAIL`
   (reusing `tabsFixture.BA_US_Equity.json`'s peers block), then `CHECKS-OK N of N` or `CHECKS-WRONG-WAY <names>` with
   `process.exitCode = 1`. It writes NO file.

**The validation bar (`C-VALIDATION-NAMES`, `:1652-1658`):** the render is proven on CAT's landed object (the one
validation name whose SA set is certain to exist, being a large US name); CSL and Keyence are rendered through the
same component if `rk-50` landed sets for them (add their fixtures the same way) and are reported by name if not.
NO browser capture: the authenticated page is MFA-blocked (analysis s.3.5 `:92-96`, the `rk-26` withdrawal) and a
criterion that needs only the data tests the component directly and says so -- this order does.

**Served output (analysis s.4 co-sign `yes`):** this order COMMITS to the portal's DEV branch, which serves nothing
(analysis s.1 `:40`: *"nothing deploys to DEV by design"*); the served plane moves only at the PROD promote, which is
Andrew's and deferred. So this order opens NO change-management entry and performs NO live act; the never-widen pair
(CTO half + COO half) for the Peers page is owed BEFORE that promote and is NOT this order's to write. Say so in
your report, in those words.

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.21c, on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis @9c8e04cd9a s.4 row R14-P3 (`:138`),
s.3.5 (`:92-96`, no headless authenticated capture). PRD v0.13 @1699960261: `C-PEER-SET-SA` (`:614-641`),
`C-VALIDATION-NAMES` (`:1652-1658`). Both L4-R halves signed at v0.13 before this order was cut. Depends on
`AMGT-rk-50` (the object it renders) and follows `AMGT-rk-51` in this slot's queue.

**ISSUER RULE -- WHERE THE NEVER-WIDEN PAIR LIVES (`2.0.0_SA_COO~Z`, at the cut):** this order is CO-SIGNED. The pair
for chain P is TWO ledger files, one section per cell: the COO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_P_COO_HALVES.md` and the CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_P_CTO_HALVES.md`. "The pair is on file" MEANS: both
files exist in your worktree, each carries a section headed `AMGT-rk-52`, and that section names this order's blast radius
(the keys/prefixes and, for an adapter cell, the Lambda) and the per-key rollback. Read both before your first live act,
paste both files' sha256 into the change-management entry, and record every pre-act hash the halves tell you to measure
FRESH (never a value copied from another order). Either file absent or its `AMGT-rk-52` section missing: run the read-only and
dry-run criteria, file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`), and STOP -- never act on one half.

## 3. SURFACES -- what you may read and write

<paths>
portal/src/pages/SecurityAnalysis/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~52/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-52.peers-page-sa-shape.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_P_*_HALVES.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** `lib/research/api/scoped_amgt.py` is NOT on your surface: it is the
  single-writer surface the COO sequences, and `read_peer_set()` already serves the object whole. **If you find the
  adapter MUST change for the page to render SA's shape, REFUSE that criterion with a row naming the exact field the
  adapter drops -- never edit it.** `PostureTab.tsx` (`:339`, `:347`) also consumes `usePeerSet`; your `types.ts` change
  must keep it compiling (AC1) and you do not edit its behaviour. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING (two repos, in this order):** first inside `portal/` on branch `DEV` with
  `git -C portal commit` via `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~52 <0.9.0_WK_AMGT_RESAPP~52@opal.agent>" -F <msgfile> -- <portal paths>`
  run from the portal root (read `safe-commit.sh`'s own usage first; if it refuses to run inside the submodule, commit
  the portal with `git -C portal commit --author "0.9.0_WK_AMGT_RESAPP~52 <0.9.0_WK_AMGT_RESAPP~52@opal.agent>" -F <msgfile>`
  and record the refusal text in your report); then the workspace paths with safe-commit as every other order. **Do
  NOT bump the `portal` gitlink in the workspace** -- the pointer bump is the DT/MSTR act (`.owned-paths.yaml:1940-1942`).
  Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL: **COMMIT YES / PROMOTE NO. THE PORTAL DEV PUSH IS RESERVED** (LD-0367/0368; LD-0522 puts every push with
`0.0.0_AB_MSTR~Z`). **COLLECTION STAYS OFF. No vendor call** -- none is named; the fixture is a pool READ. **NO alarm,
monitor, SNS/SES-send, notification or freshness checker.** No non-ASCII in anything you write (the page's existing
`&apos;` entity idiom is fine). `./node_modules/.bin/tsc -b` -- **NEVER `npx tsc`** (a banked decoy: `bun install`
writes no npm shims, so `npx tsc` fetches a registry package of that name and exits clean having compiled nothing) and
**NEVER bare `tsc --noEmit`** (compiles an empty file set, portal `CLAUDE.md`). **PUSH: never.**
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name.
**SURPRISE ROWS:** your row continues `AMGT_RESAPP-Z-W52-S<k>` from your prior order; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize
it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-52"><invocation>cd "$(git rev-parse --show-toplevel)/portal" && ./node_modules/.bin/tsc -b --noEmit 2>&1 | tail -20; echo "tsc-rc=${PIPESTATUS[0]}"</invocation><expect>no error lines and tsc-rc=0 -- the project-referenced build typechecks clean with the new PeerBasis, PeerCell and cells fields, PostureTab.tsx included; portal @625a0888 typechecks clean before this order, so any error line is attributable to it</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-52"><invocation>cd "$(git rev-parse --show-toplevel)/portal" && node src/pages/SecurityAnalysis/__harness__/peersTab.harness.cjs 2>&1 | tail -14; echo "harness-rc=${PIPESTATUS[0]}"</invocation><expect>FIXTURE CAT_US_Equity sha256={hex}; COLUMNS rendered 16 covering 17 of 17 declared; CELLS with source label k of N with k equal to N minus the not-meaningful/absent cells (both numbers read off the fixture and printed); NOT-MEANINGFUL m1 renders n/m and never 0.00: PASS; FALLBACK m2 label SA:revenue_growth3 rendered: PASS; SUMMARY 4 rows each with a source mix: PASS; BASIS badge Seeking Alpha: PASS; DERIVED-BASIS fixture BA_US_Equity still renders (regression): PASS; CHECKS-OK N of N; harness-rc=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-52"><invocation>cd "$(git rev-parse --show-toplevel)/portal" && node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs 2>&1 | tail -6; echo "harness-rc=${PIPESTATUS[0]}"</invocation><expect>the existing five-name harness still ends CHECKS-OK N of N with harness-rc=0 (the derived-basis rendering is unchanged by this order); a CHECKS-WRONG-WAY line is a regression and a FAIL</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-52"><invocation>cd "$(git rev-parse --show-toplevel)/portal" && python -c "
import io
files = ['src/pages/SecurityAnalysis/tabs/PeersTab.tsx', 'src/pages/SecurityAnalysis/cscTable.ts', 'src/pages/SecurityAnalysis/types.ts']
joined = ''.join(io.open(f, encoding='utf-8', errors='replace').read() for f in files)
for token in ('SA_FALLBACK', 'meaningful', 'data-cell-source', 'Seeking Alpha', 'sa_shape'):
    print(token, joined.count(token))
print('files', len(files), 'of 3 read')
"</invocation><expect>every token count nonzero across the three files (files 3 of 3 read); all five read 0 at portal @625a0888 before this order lands</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order:
the authenticated-page look is MFA-blocked and is not graded here (analysis s.3.5); the component render IS the
instrument, and it says so.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~52/AMGT_RESAPP.TO-AMGT-rk-52.peers-page-sa-shape.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (portal artifacts as kind `frontend_component`, `deployed_state`
`COMMITTED-NOT-DEPLOY-SCOPE` with the reason "DEV serves nothing; PROD promote deferred"), graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to `complete`;
commit with `--only -- <paths>`. Report once, naming the portal commit hash on DEV (LOCAL; push state UNREAD -- the push
is not yours) and the fixture's pool key and sha256. **This is chain P's last order; STOP after the report.**

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>superseded</status>
<superseded_by>the H-chain with AMGT-rk-50: its reader intent (peers page shape) is re-cut as a reader cell on silver after the writers and their moves. RULED by 1.0.0_SA_CTO~Z, ROUND_ANALYSIS.round20.md s.2 @ab54fb15e0 (msg 24109): SUPERSEDED is terminal, not acceptance (R4); the remedy stays owed by the successor. Flipped in the round-21 issuance by 2.0.0_SA_COO~Z.</superseded_by>
<round>14</round>
<slot>~52</slot>
<fabric>site-z</fabric>

# AMGT_RESAPP task order -- `AMGT-rj-9` -- THE HEADER AND THE FIVE TABS -- the page as Andrew defined it, every route reading the pool

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rj-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~18</issued_to>
<issued_by>2.0.0_SA_COO~W</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~18`.** Same worktree, same portal checkout and branch, same rules as `rj-1` and `rj-2`; this is the
THIRD order of chain A, handed to you only after `rj-5` (the pool reader and the generation writer), `rj-6` (filings), `rj-7` (the
ranker) and `rj-8` (management) are drained -- their pool objects are your fixtures and their interfaces your inputs. Every Bash
call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~18;`. **NEVER RUN AN INSTALL.** The `portal` gitlink NEVER moves.

## 1. THE CELL, inlined in full -- `AMGT-rj-9` (FWD-16; C-PAGE-LAYOUT; the rendering half of FWD-17, FWD-18, FWD-8; the route half of C-ONE-STORE and C-RANKING-GENERATION)

**THE CONTRACT (PRD v0.8 @`1170b4da69`, C-PAGE-LAYOUT, SIGNED):** *"The Security Analysis page is ONE HEADER and FIVE TABS. The header
is the discovery surface: the Lead Panel's ranking cross (movement Trending | Breakout x subject Price | Chatter, List | Chart), the
company-level feed (publisher items from the harvest and, once S13 has measured a source, social items), a one-line description, and
the Posture line. The tabs, in order: Thesis (prose over cited evidence + the one "big thing" chart), Exec Management, Peers, Model,
Posture. Print is a header export action, never a tab. The Coverage TAB is retired: its content is the header feed. The Model tab is
RESTORED ... carrying the model block in the shape of Adam's `Model` sheet."* **THE OUTCOME:** *FWD-16 "Above the tabs, beside the
ranked list, the page shows a one-line description of the company and the day's news and social items about it, newest and
most-discussed first, each one clickable through to its source."*

**THE SEAM (06:1x-06:3xZ):** `constants.ts:69-73 SECURITY_ANALYSIS_TABS` = exactly three (`thesis`, `peers`, `coverage`); `LeadPanel.tsx`
(the header: two pickers, starred filter, list/chart toggle, ticker search, refresh; renders the server's `resolution` verbatim);
`CoverageTab.tsx` + `useCoverageSet` (`useLeadPanelApi.ts:135-142` -> `GET /security/{key}/coverage`); the fiscal table lives in
`ThesisTab.tsx` (round 5 cut the Model tab); `SecurityOverlay.tsx`; `PeersTab.tsx` (`usePeerSet`); `PrintExportAction.tsx`;
`hooks/useLeadPanelApi.ts` (seven React Query wrappers, `STALE_TIME_MS` 5 min; keys under `amgt-lead` in `constants.ts:39-50`).
Backend: `scoped_amgt.py` -- `_figures :605-608` splits `SCOPE_HEADER` / `SCOPE_FISCAL_YEAR_LINE_ITEM`; the ranking readers at
`:329-338` (a point at `<AXIS>#<date>` / ticker) and `:434-438` (the same old keys for every timeseries date); `read_coverage_set
:685-703` (the DynamoDB read, yours to replace); `read_peer_set :850-857`.

**THE INTERFACES YOU CONSUME (19d):** X-1 `crosswalk.resolve` / `aliases` (rj-4); P-1 `lib/research/coverage/pool_reader.coverage_items
(identity, days)` (rj-5); G-1 the generation pointer in `opal-harvest-security-metrics` (rj-5: rows at `<AXIS>#<date>#<generation_id>`,
the pointer at `<AXIS>#<date>` / `_CURRENT` with `generation_id, run_id, coverage_vintage, payload_hash, row_count, state`); D-1
`drafting/v1/{key}.json` (rj-6, already served by rj-2's route); F-1 `filings/v1/{key}/{accession}.analysis.json` (`thesis_driver`);
R-1 `peers/v1/{key}/{as_of}.json` (rj-7); M-1 `management/v1/{key}/{as_of}.json` and `_pool/{as_of}.json` (rj-8); O-1
`posture/v1/{key}/{as_of}.json` (rj-11; ABSENT until it lands). Objects for BA_US_Equity, COST_US_Equity, HD_US_Equity, SAP_GY_Equity,
BABA_US_Equity are in the pool; local copies in the `~19`, `~20`, `~21`, `~22` deliverables for the harness fixtures.

**DELIVER, in this order:**
1. **EVERY adapter route edit of the round** (chain A owns `scoped_amgt.py`): (a) `read_coverage_set` on P-1 through the identity's
   aliases, returning `items`, `store_item_count`, `states` and `key_forms`; (b) EVERY reader of a ranking partition -- the rankings
   list, the overlay's points, the timeseries history -- follows G-1's pointer for each date and READS the generation partition, checks
   the rows it read against the pointer's `row_count` (a short read is retried once, then REFUSED with `ranking_status: SHORT_READ`,
   never served), and carries `generation_id`, `coverage_vintage`, `payload_hash`, `state` on the response; a date with no pointer is
   `ABSENT`; an EMPTY pointer is an empty membership, distinct from ABSENT; (c) `/security/{key}/peers` on R-1; (d) NEW
   `/security/{key}/management` on M-1 (+ the pool average); (e) NEW `/security/{key}/posture` on O-1 (ABSENT until rj-11); (f) NEW
   `/security/{key}/description` and `/security/{key}/feed` (or fields on the overlay) -- the description from a model-block header
   scalar if one exists (measure the header scalars first; name the field), else D-1's `company_description` first sentence marked
   machine, else ABSENT; the feed = P-1 items newest first + `social: {status: "no source measured (S13)"}`; (g) `/security/{key}/model`
   = `fiscal_year_figures` (out of the thesis bundle) with the identity block. The mount's route set (11 routes) is unchanged in this
   cell: new READS are served through the existing `{security_key}` routes' payloads or the `/thesis` bundle, so the terraform route
   set does not move (rj-10 deploys code and IAM only); state in your row which shape you chose.
2. **The page.** `constants.ts` tabs = `thesis`, `exec_management`, `peers`, `model`, `posture` (five, in this order); `CoverageTab.tsx`
   RETIRED (deleted or unmounted; its list becomes the header feed); `LeadPanel.tsx` gains, for the selected security, the description
   line and the feed (publisher items newest first, each an outbound link; the social line as the server states it) and the Posture
   line (rj-12 fills it; ABSENT-explicit now); `ModelTab.tsx` NEW = `fiscal_year_figures` in Adam's `Model` sheet shape (Financial
   Summary rows x fiscal years; the three cases ABSENT-explicit), moved OUT of Thesis; `ThesisTab.tsx` = the drafted sections (rj-2)
   + ONE chart (`ThesisDriverChart.tsx`) of `thesis_driver`'s series over the model block's fiscal series (or the filing's segment
   table when the series is not in the block), ABSENT-explicit when no driver; `PeersTab.tsx` = the CSC table over R-1 (columns present
   / ABSENT as R-1's map says; Average / Median / Min / Max rows; `basis` and `universe_vintage` shown); `ExecManagementTab.tsx` NEW =
   M-1 (officers with role, role start, tenure, profile link or ABSENT; the pool comparison line with its denominator; unconfirmed
   stated); `PostureTab.tsx` a placeholder rendering ABSENT-explicit (rj-12 fills it); Print stays a header action; every ranking
   render shows `generation_id` in a caption. New hooks under the `amgt-lead` key namespace only (comp-cache read: 481 files, 119
   sites, no existing key changed).
3. **Harnesses**: one arm per tab over the fixtures (the five names), the header's feed and description, the retired Coverage tab
   (its module absent from the tab list), the SHORT_READ refusal on a stubbed pointer mismatch; the render check over the assembled page.

**BOUND:** no install; no deploy (rj-10); nothing promoted; the mount's terraform route set unchanged; no edit under
`lib/research/{coverage,drafting,filings,peers,management,identity}/` (call them).

## 2. WHERE THIS CAME FROM

**ROUND 11**, decomposition v1.3 s.19 @`73938cdae4`, on Andrew-direct ~05:1xZ (the header panel; four tabs), ~05:1x-05:2xZ (Posture, a
fifth), the voice memo ~05:5xZ, card 3, C-PAGE-LAYOUT's supersession of the three-tab shape (PRD s.9f), and the CRO's follow-up
@`865e4fc113` items 2 and 3 (every ranking reader on the pointer; the row_count check).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/
lib/research/coverage/
lib/research/identity/
lib/research/drafting/
lib/research/peers/
lib/research/management/
lib/research/filings/
portal/src/pages/SecurityAnalysis/
portal/src/api/endpoints/amgt-lead-panel.ts
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~20/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~21/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~22/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/
org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_SUBSTRATE_MEASUREMENTS_20260915_W/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rj-9.the-header-and-the-five-tabs.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). Every `lib/research/*` package but `api/` is READ-ONLY (call it); the
  deliverables of `~19`..`~22` and `~1` and the CTO's cards (card 3: the `Model` and `CSC` sheet shapes) are READ-ONLY.
- **COMMITTING:** as in `rj-1`. Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN both fabrics: COMMIT YES / PROMOTE NO. No vendor call. No non-ASCII in anything you write. **THE REFUSAL CLAUSE** and
**SURPRISE ROWS** as in `rj-1`; continue the `W18` sequence.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rj-9"><invocation>python -c "import io; c=io.open('portal/src/pages/SecurityAnalysis/constants.ts',encoding='utf-8').read(); i=c.find('SECURITY_ANALYSIS_TABS'); seg=c[i:i+900]; print('tabs-order', [k for k in ('thesis','exec_management','peers','model','posture','coverage') if (\"'\"+k+\"'\") in seg or ('\"'+k+'\"') in seg]); import os; print('coverage-tab-file', os.path.exists('portal/src/pages/SecurityAnalysis/tabs/CoverageTab.tsx'), 'model-tab', os.path.exists('portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx'), 'exec-tab', os.path.exists('portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx'), 'posture-tab', os.path.exists('portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx'), 'driver-chart', os.path.exists('portal/src/pages/SecurityAnalysis/components/ThesisDriverChart.tsx'))"</invocation><expect>tabs-order exactly [thesis, exec_management, peers, model, posture] (five, in Andrew's order, coverage absent); coverage-tab-file False (retired) or True with the row saying it is unmounted; model-tab True; exec-tab True; posture-tab True; driver-chart True. A sixth tab, or coverage still listed, is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rj-9"><invocation>python -c "import json; from lib.research.api import scoped_amgt as s; c=s.read_coverage_set('BA_US_Equity'); print('coverage items', len(c.get('items') or []), 'store_item_count', c.get('store_item_count'), 'states', json.dumps(c.get('states')), 'key_forms', c.get('key_forms'), 'first-url', ((c.get('items') or [{}])[0].get('url') or '')[:60]); z=s.read_coverage_set('ZZZ_NOPE_US_Equity'); print('control items', len(z.get('items') or []), 'identity', (z.get('identity') or {}).get('identity_status'))"; python -c "import io; a=io.open('lib/research/api/scoped_amgt.py',encoding='utf-8').read(); print('adapter-gsi', a.count('ticker_date_index'), 'adapter-articles-table', a.count('opal-harvest-articles'), 'pool-reader', a.count('pool_reader'))"</invocation><expect>BA coverage items at least 1 with store_item_count at least 1 and PRINTED (the pool's per-name link count; 2 for BA at row W19-S8, a bounded commissioning sample whose backfill is Andrew's), states printed, key_forms naming the harvester's form, a canonical https url; the control 0 items with identity_status UNRESOLVED; adapter-gsi 0, adapter-articles-table 0, pool-reader at least 1 (the table is retired as a source). Any surviving table read in the adapter is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rj-9"><invocation>python -m unittest discover -s lib/research/api/tests -p "test_*.py" -q 2>&1 | tail -3; python -c "import io; a=io.open('lib/research/api/scoped_amgt.py',encoding='utf-8').read(); t=''.join(io.open(f,encoding='utf-8').read() for f in __import__('glob').glob('lib/research/api/tests/test_*.py')); print('pointer-reads', a.count('_CURRENT'), 'row_count-check', a.count('row_count'), 'short-read-status', a.count('SHORT_READ'), 'bare-date-partition-reads', a.count('f\"{axis}#{as_of'), 'generation-on-response', a.count('generation_id'), 'tests-short-read', t.count('SHORT_READ'), 'tests-empty-vs-absent', t.count('EMPTY') + t.count('ABSENT'))"</invocation><expect>the suite ends OK with 0 failures and 0 errors; pointer-reads at least 3 (the list, the overlay points and the timeseries all follow the pointer); row_count-check at least 1; short-read-status at least 1; bare-date-partition-reads 0 (no reader builds a bare AXIS#date key for rows); generation-on-response at least 3; tests-short-read at least 1; tests-empty-vs-absent at least 2. A reader still on a bare date partition, or a short read served, is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rj-9"><invocation>python -c "import json; from lib.research.api import scoped_amgt as s; k='BA_US_Equity'; o=s.read_security_overlay(k) or {}; print('description', json.dumps(o.get('description'))[:160]); f=o.get('feed') or {}; print('feed-items', len(f.get('items') or []), 'social', json.dumps(f.get('social'))[:80]); m=s.read_management(k) if hasattr(s,'read_management') else s.read_thesis_bundle(k).get('management'); print('management-officers', len((m or {}).get('officers') or []), 'pool_avg', (m or {}).get('pool_avg_tenure_years')); p=s.read_peer_set(k); print('peers-basis', p.get('basis'), 'members', len(p.get('members') or []), 'csc-present', len(((p.get('csc_columns') or {}).get('present')) or [])); po=s.read_posture(k) if hasattr(s,'read_posture') else {'status':'ABSENT'}; print('posture', json.dumps(po)[:80]); md=s.read_model(k) if hasattr(s,'read_model') else s.read_thesis_bundle(k); print('model-fiscal-rows', len(md.get('fiscal_year_figures') or []), 'thesis_driver', json.dumps(s.read_thesis_bundle(k).get('thesis_driver'))[:100])"</invocation><expect>description a non-empty string with its source named (a model-block scalar, or D-1's first sentence marked machine) or ABSENT-explicit; feed-items at least 1 with social stating no source measured; management-officers at least 5 with a pool_avg number or null-with-denominator; peers-basis derived with members at least 5 and csc-present at least 5; posture ABSENT-explicit (rj-11 has not landed at this cell); model-fiscal-rows 183 for BA (or the block's count, printed); thesis_driver naming a series. An empty payload where a pool object exists is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rj-9"><invocation>cd portal && for h in join.harness.mjs errorEmpty.harness.cjs drafting.harness.cjs tabs.harness.cjs; do printf "HARNESS %s: " "$h"; timeout 110 node src/pages/SecurityAnalysis/__harness__/$h 2>&1 | tail -3 | tr "\n" " "; echo; done</invocation><expect>every harness rc 0 with its checks at their met values: the round-8 numbers unchanged (183/183, 13/13), the four error/empty states, the drafting evidence beside each sentence, and the NEW tabs harness reporting five tabs rendered, the header feed and description rendered, the Model tab's fiscal rows, the Peers CSC table with absent columns marked, the Exec Management officers, the Posture placeholder ABSENT, generation_id captions present, and short_read_refused true on a stubbed pointer mismatch. A harness dropped or a check moved is NOT met</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rj-9"><invocation>cd portal && timeout 110 ./node_modules/.bin/vite build --logLevel info > ../.scratch/rj9.build.txt 2>&1; echo rc=$?; python -c "import glob,os; js=sorted(glob.glob('dist/assets/*.js')); toks={'exec-tab':b'exec_management','model-tab':b'Financial Summary','posture':b'posture','control':b'zzz-no-such-string-rj9-control'}; hits={k:[os.path.basename(f) for f in js if v in open(f,'rb').read()] for k,v in toks.items()}; print('js-assets', len(js)); [print('TOKEN', k, len(v)) for k,v in hits.items()]"; cd .. && git -C portal log --oneline 9aef3734..HEAD | wc -l; echo "gitlink: $(git ls-tree HEAD portal | cut -c13-22)"; git log --format="%h %an %s" -2 -- lib/research/api/scoped_amgt.py | cut -c1-120</invocation><expect>rc=0, js-assets above 20, TOKEN exec-tab, model-tab and posture each at least 1, TOKEN control 0; portal commits above 9aef3734 at least 3 (rj-1, rj-2, this); gitlink e85f6eb8 unchanged; commits by this serial on the adapter. A moved gitlink is a hard stop</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~18/AMGT_RESAPP.TO-AMGT-rj-9.the-header-and-the-five-tabs.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR WORKTREE'S
OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); keep the harness outputs and the
build log beside it as `.txt`; flip `<status>` to `complete`; commit with `--only -- <paths>`. Report once. **If a criterion cannot be
met, leave the order OPEN and file a row.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>11</round>
<slot>~18</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.8 @`1170b4da69` (ADMITTED) FWD-16, C-PAGE-LAYOUT (s.9f: the three-tab shape SUPERSEDED), the route halves of C-ONE-STORE and C-RANKING-GENERATION; Andrew-direct ~05:1xZ @`a5c6a066de` (the header; four tabs) and ~05:1x-05:2xZ @`a4f9fd9568` (Posture, the fifth); the voice memo @`fbd5d91431`; card 3 @`5007337353`; the CRO's follow-up @`865e4fc113` items 2 and 3; `1.0.0_SA_CTO~W`'s L10 round-10 analysis @`8d5fe78265` s.6 item 6; decomposition v1.3 s.19 @`73938cdae4` (cell rj-9, chain A third, after the drains of rj-5/6/7/8). Cell set: s.19a; fan-out: s.19e.</authority>

<preflight>
ALL RUN 2026-09-15 06:4xZ at this cut (decomposition v1.3 s.19g).
comp-schedule: RUN (--drift) -- 5 of 5 carriers within budget (16.0 s of 90); REACHED-DENOMINATORS C1=23, C2=8, C3=12, C4=21, C5=334; C2 = 8 OPEN deploy-ledger entries (none this project's; rj-10 opens one and closes it inside the round); C3 = 12 standing NEVER clauses (no monitor, no alarm); NO new scheduled producer is cut this round (every batch is a local Windows task DISABLED at creation, Andrew's box word @187f003998); BLIND on C4 and C5 in the tool's own voice.
comp-iam: RUN (gaps) -- 838 call(s) verdicted across 98 mapped role(s) over 474 .tf files; 629 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED, NOT CLEARED), 14 UNGRANTED, 2 GRANTED-ACTION / UNGRANTED-RESOURCE; 15 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 32 services; BLIND on 266 calls in 26 role-UNMAPPED services. The round's IAM delta lives in rj-10 alone: READ grants by prefix on opal-data-harvest for two roles, the DynamoDB articles grants REMOVED, no Scan, no wildcard resource; every other cell acts under the operator's own credentials and takes no AWS grant.
comp-adversary: RUN (compose on the decomposition, --no-packet) -- 48 commit pins, 13 repo paths, 17 file:line cites, 14 tool mentions; 23 hex runs not parsed (named); T11 NOT RESOLVED (293 uncited siblings, CAP 25 declared); stage 4 disabled by the caller. The round's adversarial surfaces: filing text, vendor responses and pool objects are DATA inside a model prompt (rj-6, rj-11 say so in the prompt; the verbatim gate runs against the PASSAGE; held-uncited claims never render); Posture is marked machine and read by no trade consumer; the Lusha response is scrubbed to name/title/link; the social job is capped in posts and USD.
comp-cache: RUN (collisions) -- 481 of 481 portal files, 119 of 119 useQuery sites; this cell adds keys under the amgt-lead namespace only and changes no existing key.
comp-blast: DECLARED-NOT-APPLICABLE -- this cell moves nothing on the live plane: its writes are local code, tests and pool objects under the operator's credentials (a QA one-shot is not a production act); the round's one live move is rj-10's, covered by the co-sign.
</preflight>

**AMENDMENT 2 (2026-09-15 ~09:4xZ, `2.0.0_SA_COO~W`, issuer):** the `store_item_count at least 20` bar on BA was the issuer's assumption; the pool holds 2 links for BA (row `AMGT_RESAPP-Z-W19-S8`; the CRO's brief @`0e7de170e3`; the harvest's cadence is Andrew's @`9db2a36cdc`). Re-cut to `at least 1 and PRINTED`; the discriminating clauses (items at least 1, states printed, key_forms, no table read) are unchanged.

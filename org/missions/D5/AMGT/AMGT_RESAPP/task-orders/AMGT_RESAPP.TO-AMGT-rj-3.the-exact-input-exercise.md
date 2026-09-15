# AMGT_RESAPP task order -- `AMGT-rj-3` -- THE EXACT-INPUT EXERCISE -- one payload, one hash, through the assembled page

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rj-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~18</issued_to>
<issued_by>2.0.0_SA_COO~W</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~18`.** Same worktree, same portal checkout and branch, same rules as `rj-1`; this is the LAST order
of chain A and of the round, handed to you only after `rj-10` (the deploy) and `rj-12` (the Posture tab) are terminal. Every Bash
call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~18;`. **NEVER RUN AN INSTALL.** The `portal` gitlink NEVER moves.

## 1. THE CELL, inlined in full -- `AMGT-rj-3` (row `S72`; FWD-15, FWD-9, FWD-10; the round's AC6 judgment)

**THE CVO's grade (REMEDIATION_v10 @`e28f0b546c`, S72):** "the browser rendered 09-12; AC2 captured 09-15. Equal counts/axis/ticker
order are insufficient. Keep the exact payload hash/day through the assembled-route exercise, with error and empty controls. No
live-edge or person-session claim exists." Round 10's exercise rendered a LOCAL adapter run's payload while the deployed adapter's
capture was a different day; this cell closes that gap by construction: ONE payload, ONE sha256, printed at input and at output.

**THE SEAM (06:1x-06:3xZ):** the three harnesses under `portal/src/pages/SecurityAnalysis/__harness__/` take NO payload path or day --
`join.harness.mjs:41` `load(key)` reads `thesisBundle.${key}.json` beside itself (keys `BABA_US_Equity`, `BABACVOCTRL_US_Equity`);
`chart.harness.mjs:42` reads `rankSeriesCompleteness.json`; `errorEmpty.harness.cjs` stubs its query results inline. The persisted
cache: `portal/src/lib/queryPersister.ts` `STORAGE_KEY = 'OPAL_PORTAL_QUERY_CACHE_v1'`, 12 h max age, `clearQueryPersister()`;
`main.tsx:40-41` `staleTime: Infinity, gcTime: Infinity` (a successful response is never refetched for the session) with
`buster: 'v2'` -- this is the stale-arm mechanism the round-10 exercise hit.

**THE INPUTS (from `rj-10`'s live reads, committed in `0.9.0_WK_AMGT_RESAPP~19`'s deliverables at the drain; read-only for you):**
the ranked payload `rankings.trending.chatter.response.<day>.json` (carrying `generation_id`, `coverage_vintage` and `payload_hash` from
the committed generation's pointer, C-RANKING-GENERATION: a date alone cannot tell two computations apart) and the thesis bundle
`thesis.<key>.response.<day>.json` captured from the DEPLOYED adapter, each with its sha256 in the instance. The page under exercise is the round's assembled page (five tabs
and the header, `rj-9`/`rj-12`) on your portal branch.

**DELIVER, in this order:**
1. **Harness inputs.** `join.harness.mjs` accepts `--payload <path>` (a thesis bundle) and `--ranked <path>` (a ranked payload) and
   prints, at input, each file's sha256 and its `as_of_date`; the render path prints the same sha256 next to the rendered row count
   and figure count at output. Existing behaviour without the flags is unchanged (the committed fixtures).
2. **The exercise, mechanical half.** Run the assembled page's render check (`__rendercheck__/renderCheck.tsx` or a new
   `assembled.harness.cjs`) against the two captured payloads: the header (ranked list from the ranked payload; the feed and the
   description from the thesis bundle's identity), each of the five tabs, the Posture line; assert the sha256 printed at output
   equals the input's; error arm (a stubbed 5xx) and empty arm (a ranked payload with `row_count 0`) rendered DISTINCT (the round-10
   texts) and printed.
3. **The cache discipline.** The exercise clears `OPAL_PORTAL_QUERY_CACHE_v1` before each arm (`clearQueryPersister`) and records
   that it did; the served page's `buster` is read and recorded.
4. **The browser half is the issuer's.** `2.0.0_SA_COO~W` drives the served route with the SAME two payloads and the same sha256s,
   filing `org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_RESAPP_W/ROUND11_BROWSER_EXERCISE.md`; AC5 records
   UNVERIFIABLE-BY-INSTRUMENT with a `status_reason` naming `3.0.0_SA_CVO~W` and that path (say ABSENT if it does not exist when
   you run). Say plainly in your instance which half you settled.

**WHAT THIS CELL DOES NOT CLAIM:** the live edge (API `7k3ed8px20` through the portal JWT), a person's session, a promotion.

## 2. WHERE THIS CAME FROM

**ROUND 11**, decomposition v1.3 s.19 @`73938cdae4`, on the analysis @`8d5fe78265` s.6 item 1 and the slug @`e28f0b546c` item 3;
row `Z-S72` (round 9, `2.0.0_SA_COO~ZZZ`) carried through rounds 9 and 10.

## 3. SURFACES -- what you may read and write

<paths>
portal/src/pages/SecurityAnalysis/
portal/src/lib/queryPersister.ts
portal/src/api/endpoints/amgt-lead-panel.ts
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/
org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_RESAPP_W/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rj-3.the-exact-input-exercise.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). `queryPersister.ts` is READ-ONLY (you call it; you do not change it);
  the `~19` deliverables and the COO's deliverables are READ-ONLY.
- **COMMITTING:** as in `rj-1`. Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN both fabrics: COMMIT YES / PROMOTE NO; a local dev server is not a publish. No vendor call. No non-ASCII in anything
you write. **THE REFUSAL CLAUSE** and **SURPRISE ROWS** as in `rj-1`; continue the `W18` sequence.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rj-3"><invocation>python -c "import hashlib,glob,json,io; fs=sorted(glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/rankings.trending.chatter.response.*.json'))+sorted(glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/thesis.*.response.*.json')); print('inputs', len(fs)); [print('INPUT', f.split('/')[-1], hashlib.sha256(open(f,'rb').read()).hexdigest()[:16], (lambda b: (b.get('as_of_date'), b.get('generation_id'), b.get('payload_hash')))(json.loads(json.load(io.open(f,encoding='utf-8')).get('body') or '{}') if 'body' in json.load(io.open(f,encoding='utf-8')) else json.load(io.open(f,encoding='utf-8')))) for f in fs]"</invocation><expect>inputs 2 (one ranked payload, one thesis bundle, both captured from the DEPLOYED adapter under rj-10), each with a 16-hex sha256 prefix and the SAME as_of_date, the ranked payload carrying a generation_id and a payload_hash. Inputs 0, or two different days, is a STOP and a BLOCKING row -- the exercise has no exact input</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rj-3"><invocation>cd portal && R=$(ls ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/rankings.trending.chatter.response.*.json | head -1); T=$(ls ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/thesis.*.response.*.json | head -1); timeout 110 node src/pages/SecurityAnalysis/__harness__/join.harness.mjs --payload "$T" --ranked "$R" 2>&1 | tail -10; echo rc=$?</invocation><expect>rc=0; an INPUT line per file with its sha256 prefix and as_of_date; an OUTPUT line carrying the SAME sha256 prefixes beside the rendered row count (equal to the ranked payload's row_count) and the fiscal figure join (183/183 for BABA_US_Equity, header 13/13). A sha at output that differs from its input is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rj-3"><invocation>cd portal && R=$(ls ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/rankings.trending.chatter.response.*.json | head -1); T=$(ls ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/thesis.*.response.*.json | head -1); timeout 110 node src/pages/SecurityAnalysis/__harness__/assembled.harness.cjs --payload "$T" --ranked "$R" 2>&1 | tail -16; echo rc=$?</invocation><expect>rc=0 and check lines: tabs_rendered 5 (thesis, exec_management, peers, model, posture), header_ranked_rows equal to the ranked payload's row_count, header_description_present true or ABSENT-explicit, posture_line_present true or ABSENT-explicit, sha_in equal to sha_out for both payloads, cache_cleared_before_each_arm true, buster v2, error_arm_distinct true, empty_arm_distinct true, error_claims_no_daily_row false. A missing tab, a sha mismatch, or an arm that is not distinct is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rj-3"><invocation>cd portal && timeout 110 node src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs 2>&1 | tail -14; echo rc=$?; timeout 110 node src/pages/SecurityAnalysis/__harness__/chart.harness.mjs 2>&1 | tail -4</invocation><expect>rc=0 with every prior check at its met value (the regression control: nothing that held in rounds 8-11 moved) and the chart harness's 3 of 3 pairwise distinct. A number that MOVES is the finding and is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rj-3" judgment="true"/>
  <criterion id="AC6" cell_refs="AMGT-rj-3"><invocation>git -C portal log --oneline 9aef3734..HEAD | wc -l; git -C portal status --porcelain | cat; echo "gitlink: $(git ls-tree HEAD portal | cut -c13-22)"; ls org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_RESAPP_W/ | cat</invocation><expect>at least one portal commit above 9aef3734 for this order, a clean portal status, gitlink e85f6eb8 unchanged, and the listing showing whether ROUND11_BROWSER_EXERCISE.md is PRESENT or ABSENT (recorded either way; the judgment's status_reason names it)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** `AC5` is the judgment criterion: record it
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO~W` and pointing at the browser half's deliverable path,
and offer no verdict. It asks whether the assembled page, populated from ONE captured payload whose hash travelled through the
exercise, is the thing a person would call working -- figures on screen, a ranked row that navigates to the same security the
direct key reaches, machine prose beside its evidence, the tabs Andrew named, an error arm a person can tell from an empty day.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~18/AMGT_RESAPP.TO-AMGT-rj-3.the-exact-input-exercise.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance>
AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); keep the harness outputs beside it as `.txt`; flip `<status>` to `complete`;
commit with `--only -- <paths>`. Report once. **If a criterion cannot be met, leave the order OPEN and file a row.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>11</round>
<slot>~18</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>`1.0.0_SA_CTO~W`'s L10 round-10 analysis @`8d5fe78265` s.6 item 1 (the exact-input exercise as a recut of the existing seam), the slug REMEDIATION_v10 @`e28f0b546c` item 3 and row `AMGT_RESAPP-Z-S72` (preserved clock, v9), PRD v0.8 @`1170b4da69` (ADMITTED) FWD-15 / FWD-9 / FWD-10, C-PAGE-LAYOUT and C-RANKING-GENERATION, decomposition v1.3 s.19 @`73938cdae4` (cell rj-3, chain A, LAST; consumes rj-10's captured payloads and rj-12's tab). Cell set: s.19a; fan-out: s.19e.</authority>

<preflight>
ALL RUN 2026-09-15 06:4xZ at this cut (decomposition v1.3 s.19g).
comp-schedule: RUN (--drift) -- 5 of 5 carriers within budget (16.0 s of 90); REACHED-DENOMINATORS C1=23, C2=8, C3=12, C4=21, C5=334; C2 = 8 OPEN deploy-ledger entries (none this project's; rj-10 opens one and closes it inside the round); C3 = 12 standing NEVER clauses (no monitor, no alarm); NO new scheduled producer is cut this round (every batch is a local Windows task DISABLED at creation, Andrew's box word @187f003998); BLIND on C4 and C5 in the tool's own voice.
comp-iam: RUN (gaps) -- 838 call(s) verdicted across 98 mapped role(s) over 474 .tf files; 629 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED, NOT CLEARED), 14 UNGRANTED, 2 GRANTED-ACTION / UNGRANTED-RESOURCE; 15 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 32 services; BLIND on 266 calls in 26 role-UNMAPPED services. The round's IAM delta lives in rj-10 alone: READ grants by prefix on opal-data-harvest for two roles, the DynamoDB articles grants REMOVED, no Scan, no wildcard resource; every other cell acts under the operator's own credentials and takes no AWS grant.
comp-adversary: RUN (compose on the decomposition, --no-packet) -- 48 commit pins, 13 repo paths, 17 file:line cites, 14 tool mentions; 23 hex runs not parsed (named); T11 NOT RESOLVED (293 uncited siblings, CAP 25 declared); stage 4 disabled by the caller. The round's adversarial surfaces: filing text, vendor responses and pool objects are DATA inside a model prompt (rj-6, rj-11 say so in the prompt; the verbatim gate runs against the PASSAGE; held-uncited claims never render); Posture is marked machine and read by no trade consumer; the Lusha response is scrubbed to name/title/link; the social job is capped in posts and USD.
comp-cache: RUN (collisions) -- 481 of 481 portal files, 119 of 119 useQuery sites; this cell adds keys under the amgt-lead namespace only and changes no existing key.
comp-blast: DECLARED-NOT-APPLICABLE -- this cell moves nothing on the live plane: its writes are local code, tests and pool objects under the operator's credentials (a QA one-shot is not a production act); the round's one live move is rj-10's, covered by the co-sign.
</preflight>

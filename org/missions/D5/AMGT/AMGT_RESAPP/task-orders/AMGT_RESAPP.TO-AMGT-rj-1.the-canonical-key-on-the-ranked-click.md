# AMGT_RESAPP task order -- `AMGT-rj-1` -- THE ROUTE BOUNDARY AND THE RANKED CLICK -- one identity resolved once, carried unchanged, and a ranked row that reaches it

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rj-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~18</issued_to>
<issued_by>2.0.0_SA_COO~W</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~18`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt. Your first act
prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/`, `lib/research/identity/crosswalk.py` and
`portal/src/pages/SecurityAnalysis/` exist; if any is absent, STOP with a BLOCKING row. **YOU HOLD CHAIN A, a queue of FIVE orders
(`rj-1`, `rj-2`, `rj-9`, `rj-12`, `rj-3`); this is the first.** Chain A holds EVERY portal edit of the round and EVERY edit of
`lib/research/api/scoped_amgt.py`, so those files have one writer. Every Bash call begins `export
OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~18;`. **NEVER RUN AN INSTALL.** `portal/node_modules` is a junction the issuer made; leave it.
The `portal` gitlink (`e85f6eb84f`) NEVER moves; your portal work is committed on the portal branch `wk-amgt_resapp-11-1-portal`
(cut from `refs/drains/ri-1-portal` @`9aef3734`) and the superproject never stages `portal`.

## 1. THE CELL, inlined in full -- `AMGT-rj-1` (row `Z-S95`; C-ONE-IDENTITY; FWD-15, FWD-13)

**THE CONTRACT (PRD v0.8 @`1170b4da69`, C-ONE-IDENTITY):** *"ONE canonical security identity per economic security, resolved ONCE at
the route boundary and carried unchanged through overlay, thesis, peers, model, coverage, ranking and Posture ... an unresolved
vendor identifier stays UNRESOLVED and is never guessed."* The crosswalk EXISTS when you start: `rj-4` (chain B, drained before
your spawn) landed `crosswalk/v1/<as_of>.json` in the pool and the ONE resolver `lib/research/identity/crosswalk.py` (INTERFACE X-1:
`resolve(any_form) -> {security_key, resolution, ...}`, `aliases(security_key) -> [association keys]`; `AMGT_CROSSWALK_PATH` points a
local run at a copy). You call it; you do not re-implement it.

**THE BREAK, ONE HOP, FULLY TRACED (seam map 06:1x-06:3xZ on the round-10 drain ref):**
- `portal/src/pages/SecurityAnalysis/components/RankedList.tsx:138` -- `onClick={() => onSelectSecurity(row.ticker)}` (props `:42-43`
  typed `(ticker: string) => void`); the same in `StarredList.tsx:44,68,109`.
- `.../hooks/useSecurityAnalysisState.ts:37-39` -- `selectSecurity = useCallback((securityKey: string) => setSelectedSecurityKey
  (securityKey))`: RENAMED from `ticker` to `securityKey` with no transform.
- `portal/src/api/endpoints/amgt-lead-panel.ts:124-143` builds `/api/scoped/amgt/security/${encodeURIComponent(securityKey)}/...`, so
  a click sends `BABA%20US`.
- `lib/research/api/scoped_amgt.py:843-860` takes the path segment verbatim; `read_security_overlay:611-661` guesses at `:630`
  (`security_key.replace("_", " ")`) and reads `identity_status: "UNRESOLVED"` at `:653`; `read_coverage_set:685-703` applies the same
  lossy inverse; `read_thesis_bundle:664-682` carries no identity block.
- The ranking row (`chatter_axis.py build_rows :329-365`) carries `ticker` only.

**THE CVO's grade (REMEDIATION_v10 @`e28f0b546c`, S95):** "Recut the existing seam. A ranked-row click must resolve the same
canonical security and figure set as the direct-key control; retain an unresolved marker."

**DELIVER, in this order:**
1. **The route boundary.** In `scoped_amgt.py`, ONE resolution at the dispatcher for every `/security/{key}/*` route through
   `crosswalk.resolve`: a canonical key, a Bloomberg form (`BA US`) or a pack form (`BABA_US`) all resolve to the identity, which is
   then carried UNCHANGED into overlay, thesis, peers, coverage (and, in later cells, model and Posture); neither -> `identity:
   {identity_status: "UNRESOLVED", requested: <the string>}`, header figures `[]`, NO `replace("_"," ")` guessing anywhere in the
   file; every response carries the same `identity` block (`security_key`, `bloomberg`, `display_ticker`, `identity_status`,
   `crosswalk_vintage`).
2. **The ranking row's key is `rj-5`'s to emit** (chain B changes `chatter_axis.py`; two chains never edit one module): the row
   shape you consume is `{security_key, identity_status, ticker, ...}` per INTERFACE G-1; until rj-5 drains, your fixtures carry
   that shape and the served rows may still lack it -- an UNRESOLVED marker is the correct rendering of a row without a key.
3. **The page passes the key.** `RankedList.tsx` and `StarredList.tsx` call `onSelectSecurity(row.security_key)`; `types.ts`
   `RankedRow` carries `security_key: string | null` and `identity_status`; a `null` key renders a visible `UNRESOLVED` marker and
   its click does not navigate; `useSecurityAnalysisState.ts`'s parameter is a key in name and in fact; `SecurityOverlay` and the
   tabs display `display_ticker` from the identity block, never the key.
4. **Harness arms.** `errorEmpty.harness.cjs` gains a state with one unresolved row (marker rendered, no navigation); the join
   harness's fixtures gain `security_key` on their ranked rows and the `identity` block on the bundle.

**BOUND:** no install; no new Bloomberg call; no deploy; nothing promoted; the coverage READ source (the pool) is `rj-9`'s edit --
here `read_coverage_set` only receives the resolved identity and the aliases it will need.

## 2. WHERE THIS CAME FROM

**ROUND 11**, decomposition v1.3 s.19 @`73938cdae4`, on `1.0.0_SA_CTO~W`'s round-10 analysis @`8d5fe78265` s.6 item 1, the slug
@`e28f0b546c` item 1, C-ONE-IDENTITY (the CRO's identity brief @`b90bfdd20d`). Row `Z-S95` was this issuer's own finding in the
round-10 browser exercise (the click passes `BABA US`; the canonical key reaches 183 figures / 40 PROVISIONAL markers).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/
lib/research/identity/
portal/src/pages/SecurityAnalysis/
portal/src/api/endpoints/amgt-lead-panel.ts
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rj-1.the-canonical-key-on-the-ranked-click.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). `lib/research/identity/` (call it), the `~19` deliverables (rj-4's
  dry-run crosswalk for `AMGT_CROSSWALK_PATH`) and the `~1` model blocks are READ-ONLY. Your `deliverables/0.9.0_WK_AMGT_RESAPP~18/`
  home needs no entry. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** superproject `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~18 <0.9.0_WK_AMGT_RESAPP~18@opal.agent>"
  -F <msgfile> -- <paths>` (never staging `portal`); portal: `git -C portal commit` on the portal branch with the same author line,
  ASCII message. Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN both fabrics: COMMIT YES / PROMOTE NO. No vendor call is needed by this cell. No non-ASCII in anything you write.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never repaired, widened
or satisfied by a route this order did not name. **SURPRISE ROWS:** *"a worker's row is `AMGT_RESAPP-Z-W<n>-S<k>` with `<n>` its
slot; `<k>` restarts at 1 per coordinate. `"project": "AMGT_RESAPP"` and `"fabric": "site-z"` on every new row."* Your coordinate
is `W18`; your first row is `AMGT_RESAPP-Z-W18-S1`; append by textual splice inside the one fenced JSON array (never re-serialize
it); never edit an existing row.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rj-1"><invocation>X=$(ls org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/*crosswalk*.json | head -1); echo "crosswalk: $X"; AMGT_CROSSWALK_PATH="$X" python -c "import json; from lib.research.api import scoped_amgt as s; [print(k, '->', json.dumps((s.read_security_overlay(k) or {}).get('identity'))[:240], 'header_figures', len((s.read_security_overlay(k) or {}).get('header_figures') or [])) for k in ('BABA_US_Equity','BABA US','BABA_US','ZZZ_NOPE_Equity')]"</invocation><expect>BABA_US_Equity, BABA US and BABA_US all return the SAME identity block (security_key BABA_US_Equity, identity_status MEASURED, a crosswalk_vintage) and header_figures 13 -- three forms, one resolution, through the crosswalk; ZZZ_NOPE_Equity returns identity_status UNRESOLVED with requested ZZZ_NOPE_Equity echoed and header_figures 0. A MEASURED for the control, or any form that stays UNRESOLVED, is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rj-1"><invocation>python -m unittest discover -s lib/research/api/tests -p "test_*.py" -q 2>&1 | tail -3; python -c "import io; s=io.open('lib/research/api/scoped_amgt.py',encoding='utf-8').read(); print('replace-guess-sites', s.count('replace(\"_\", \" \")'), 'crosswalk-import', s.count('lib.research.identity.crosswalk') + s.count('from lib.research.identity import crosswalk'), 'resolve-calls', s.count('crosswalk.resolve(') + s.count('resolve('), 'thesis-identity', s[s.find('def read_thesis_bundle'):s.find('def read_thesis_bundle')+3000].count('identity'))"</invocation><expect>the adapter suite ends OK with 0 failures and 0 errors; replace-guess-sites 0 (the lossy inverse is gone from the file); crosswalk-import at least 1; resolve-calls at least 1; thesis-identity at least 1 (the bundle carries the block). A surviving replace guess anywhere in scoped_amgt.py is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rj-1"><invocation>python -c "import io; r=io.open('portal/src/pages/SecurityAnalysis/components/RankedList.tsx',encoding='utf-8').read(); st=io.open('portal/src/pages/SecurityAnalysis/components/StarredList.tsx',encoding='utf-8').read(); ty=io.open('portal/src/pages/SecurityAnalysis/types.ts',encoding='utf-8').read(); print('ranked-passes-key', r.count('onSelectSecurity(row.security_key'), 'ranked-passes-ticker', r.count('onSelectSecurity(row.ticker)'), 'starred-passes-key', st.count('onSelectSecurity(row.security_key'), 'starred-passes-ticker', st.count('onSelectSecurity(row.ticker)'), 'types-security_key', ty.count('security_key'), 'types-identity_status', ty.count('identity_status'), 'unresolved-marker', r.count('UNRESOLVED') + st.count('UNRESOLVED'))"</invocation><expect>ranked-passes-key at least 1, ranked-passes-ticker 0, starred-passes-key at least 1, starred-passes-ticker 0, types-security_key at least 2, types-identity_status at least 1, unresolved-marker at least 1. Any surviving onSelectSecurity(row.ticker) is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rj-1"><invocation>cd portal && timeout 110 node src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs 2>&1 | tail -14; echo rc=$?</invocation><expect>rc=0 with every prior check still at its met value (error_differs_from_empty true, error_claims_no_daily_row false) and at least one NEW check naming the unresolved row (unresolved_row_marker_rendered true; unresolved_row_navigates false, or the equivalents the worker names in a row). A harness that drops a prior check to add the new one is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rj-1"><invocation>cd portal && timeout 110 ./node_modules/.bin/vite build --logLevel info > ../.scratch/rj1.build.txt 2>&1; echo rc=$?; python -c "import glob,os; js=sorted(glob.glob('dist/assets/*.js')); toks={'key-field':b'security_key','control':b'zzz-no-such-string-rj1-control'}; hits={k:[os.path.basename(f) for f in js if v in open(f,'rb').read()] for k,v in toks.items()}; print('js-assets', len(js)); [print('TOKEN', k, len(v)) for k,v in hits.items()]"</invocation><expect>rc=0, js-assets above 20, TOKEN key-field at least 1, TOKEN control 0. A build failure is NOT met</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rj-1"><invocation>git -C portal log --oneline 9aef3734..HEAD | cat; git -C portal status --porcelain | cat; echo "gitlink: $(git ls-tree HEAD portal | cut -c13-22)"; git log --format="%h %an %s" -3 -- lib/research/api/scoped_amgt.py | cut -c1-120</invocation><expect>at least one portal commit above 9aef3734 on the portal branch and a clean portal status; gitlink e85f6eb8 unchanged; at least one superproject commit by this serial touching scoped_amgt.py. A moved gitlink is a hard stop and a BLOCKING row</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order. A rerun-able
criterion reads COMMITTED state where it grades history (`git log`), never a `git status` snapshot alone.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~18/AMGT_RESAPP.TO-AMGT-rj-1.the-canonical-key-on-the-ranked-click.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR WORKTREE'S
OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); keep the build log beside it
as `.txt`; flip `<status>` to `complete`; commit with `--only -- <paths>`. Report once. **If a criterion cannot be met, leave the
order OPEN and file a row.**

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`, never `git stash`,
never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>11</round>
<slot>~18</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.8 @`1170b4da69` (ADMITTED) C-ONE-IDENTITY and FWD-15; `1.0.0_SA_CTO~W`'s L10 round-10 analysis @`8d5fe78265` s.6 item 1; the slug REMEDIATION_v10 @`e28f0b546c` row `AMGT_RESAPP-Z-S95` ("Recut the existing seam"); the CRO's identity brief @`b90bfdd20d`; decomposition v1.3 s.19 @`73938cdae4` (cell rj-1, chain A first, after rj-4's drain; consumes X-1). Cell set: s.19a; fan-out: s.19e.</authority>

<preflight>
ALL RUN 2026-09-15 06:4xZ at this cut (decomposition v1.3 s.19g).
comp-schedule: RUN (--drift) -- 5 of 5 carriers within budget (16.0 s of 90); REACHED-DENOMINATORS C1=23, C2=8, C3=12, C4=21, C5=334; C2 = 8 OPEN deploy-ledger entries (none this project's; rj-10 opens one and closes it inside the round); C3 = 12 standing NEVER clauses (no monitor, no alarm); NO new scheduled producer is cut this round (every batch is a local Windows task DISABLED at creation, Andrew's box word @187f003998); BLIND on C4 and C5 in the tool's own voice.
comp-iam: RUN (gaps) -- 838 call(s) verdicted across 98 mapped role(s) over 474 .tf files; 629 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED, NOT CLEARED), 14 UNGRANTED, 2 GRANTED-ACTION / UNGRANTED-RESOURCE; 15 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 32 services; BLIND on 266 calls in 26 role-UNMAPPED services. The round's IAM delta lives in rj-10 alone: READ grants by prefix on opal-data-harvest for two roles, the DynamoDB articles grants REMOVED, no Scan, no wildcard resource; every other cell acts under the operator's own credentials and takes no AWS grant.
comp-adversary: RUN (compose on the decomposition, --no-packet) -- 48 commit pins, 13 repo paths, 17 file:line cites, 14 tool mentions; 23 hex runs not parsed (named); T11 NOT RESOLVED (293 uncited siblings, CAP 25 declared); stage 4 disabled by the caller. The round's adversarial surfaces: filing text, vendor responses and pool objects are DATA inside a model prompt (rj-6, rj-11 say so in the prompt; the verbatim gate runs against the PASSAGE; held-uncited claims never render); Posture is marked machine and read by no trade consumer; the Lusha response is scrubbed to name/title/link; the social job is capped in posts and USD.
comp-cache: RUN (collisions) -- 481 of 481 portal files, 119 of 119 useQuery sites; this cell adds keys under the amgt-lead namespace only and changes no existing key.
comp-blast: DECLARED-NOT-APPLICABLE -- this cell moves nothing on the live plane: its writes are local code, tests and pool objects under the operator's credentials (a QA one-shot is not a production act); the round's one live move is rj-10's, covered by the co-sign.
</preflight>

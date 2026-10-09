# DSGN_AMGTV1 task order -- `AV-zzo-3` -- A NAME THAT MATCHES SEVERAL COMPANIES SHOWS THE SERVED CANDIDATES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzo-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~137</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files, harnesses and issuer checks, run offline.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 against portal ce3b0cc4 (= origin DEV, round 62) -- r63a.cjs 1 of 3 (arms 1-2 FAIL as expected; PLANTED passes; a clean servedChoices passes arm 1, the positive control); battery29 ALL PASS at the base (round-62 candidates).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzo-3` (round 63, decomposition v63; serves FWD-27 and the layout outcomes)

Paths are under `portal/src/pages/SecurityAnalysis/`. Read `org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round62.md` section 2 first. Do the items in this order.

Typing a name and pressing Enter sends the text as the security key. For "ASML", the route answers 404 with the body
`{"refused": true, "reason": "2 companies match 'ASML'; type the ticker.", "candidates": [{"security_key": "ASML_US_Equity", "name":
"ASML Holding NV"}, {"security_key": "ASML_NA_Equity", "name": "ASML NA"}]}`. `apiRequest` throws
`Error("API request failed: 404 <statusText> - <body>")`, so the body is readable only in the message. `notFound.ts` reads every 404
as not found, and `SecurityAnalysis.tsx` draws 'No security found for "ASML".', dropping the served list.

1. **Read the served choices** (`notFound.ts`, which imports nothing): `export function servedChoices(error)`.
   - For an `Error` whose message is a 404 whose body (after ` - `) parses as JSON with two or more `candidates` carrying a string
     `security_key`, it returns `{ reason, candidates: [{ security_key, name }] }`, exactly as served (`reason` null when not a string).
   - It returns `null` otherwise: a 404 with no or one candidate, any other status, a body that is not JSON, or a non-Error.
   - Keep `isNotFound` and `notFoundWords`.
2. **Draw them** (`SecurityAnalysis.tsx`, the `nameNotFound` branch):
   - When `servedChoices(overlayQuery.error)` is not null, draw the served `reason` and one control per candidate, marked
     `data-security-choice={candidate.security_key}`, showing the served name with the key beside it. Pressing it opens that key
     through `state.selectSecurity(candidate.security_key)`.
   - Keep "Back to all names".
   - A 404 with no candidates keeps today's `notFoundWords` sentence.
3. **Test** (`__tests__/notFound.test.tsx`): add the candidate arm (two candidates drawn, no "No security found") beside the existing
   Boeing arm.

## 2. BOUNDS

1. No server, no fetch, no network, no install (`bun install`, `bun add`, `npm`, `npx` are refused here), no push, no deploy.
   REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. **Move and fold, never reword served text; never compute a figure the page does not serve** (C-PRESENTATION-ONLY).
   `reasonWords.ts` and `cscTable.ts` are not yours. No non-ASCII characters (use `--`). Keep each file's line endings as you find
   them (read them first). Edit tool for existing files.
4. Portal files commit inside `portal/` on your portal branch (set the author with `-c user.name=... -c user.email=...`; the nested repo
   has no identity), then the outer commit with safe-commit. Do not commit the portal gitlink.
5. If an item cannot be met within your paths, file a row and stop on that criterion. In particular, if battery29 goes red on a
   harness file outside your paths, file a row naming the harness and the assertion, and stop: the issuer rules it.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/notFound.ts
portal/src/pages/SecurityAnalysis/SecurityAnalysis.tsx
portal/src/pages/SecurityAnalysis/__tests__/notFound.test.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~137/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `lib/research/api/scoped_amgt.py` (~:7069-7082, the 404 body), and the issuer's check `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round63/checks/r63a.cjs` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzo-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round63/checks/r63a.cjs"; echo "exit=$?"</invocation><expect>ROUND 63 CANDIDATE LIST: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzo-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zzo-3" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded on the issuer's signed-in walk at the close (never self-graded): typing ASML shows its two listings to pick from, and picking one opens it.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~137/DSGN_AMGTV1.TO-AV-zzo-3.proof_of_spec.json`
(AC3 UNVERIFIABLE-BY-INSTRUMENT, status_reason "graded at the round-63 close walk"). **Flip this order's `<status>` to `complete` in the
SAME commit as your proof instance**, only when AC1 and AC2 pass.
A row id on this project carries the dell1 infix: `DSGN_AMGTV1-D1-W137-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the diff (per file, one line each), the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 63 = `ledger/ROUND_ANALYSIS.round62.md` @4b7ce964a2 section 2, five items in three cells by file surface
(decomposition v63). Prep: `round63/PREP.md`. Base portal ce3b0cc4 (= origin DEV). LF only (ruling R2, row D1-S1).

<status>pending</status>
<round>63</round>
<to_id>DSGN_AMGTV1.TO-AV-zzo-3</to_id>
<slot>~137</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>

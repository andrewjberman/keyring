# DSGN_AMGTV1 task order -- `AV-zze-1` -- THE SEEKING ALPHA COLUMN DRAWS THE THREE SERVED STATES APART

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zze-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~115</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files, rendered offline by the check against a body the issuer captured.
comp-adversary: RUN by the issuer at the cut on portal DEV 38cc0ecf -- r53a.cjs 2 of 3 (arm 1 FAIL: 95 of 95 Seeking Alpha cells carry no data-sa-state and 82 print "Not collected"; arms 2 and 3 PASS). On a scratch reference edit (Freshness.tsx and freshnessRows.ts, loaded through CHECK_SRC_OVERRIDE) 3 of 3. The tree was not edited.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zze-1` (round 53, decomposition v53; PRD row SAUX-41, FWD-27)

All product paths below are under `portal/src/`.

**Today** the Freshness page (`pages/Freshness/Freshness.tsx`, the table cell at about line 129) prints the Seeking Alpha column from the
served `inputs.seekingalpha`: a day when one landed, else "Not collected". The server now says more. Every covered row of
`GET /freshness?view=page` carries a new object `seeking_alpha`, one of three states:

| `state` | example `sentence` (served, verbatim) | `last_read` |
|---|---|---|
| `read` | `Seeking Alpha last read 2026-09-22.` | `2026-09-22T20:06:31Z` |
| `checked` | `Seeking Alpha was checked on 2026-10-05 and no article is held for this company.` | null |
| `no_record` | `No Seeking Alpha collection record is held for this company yet.` | null |

The object's full shape: `{ state, sentence, last_read, newest_job_finished_at, newest_job_status }` (the last three may be null).
On the live body today (95 covered rows) the states are read 13, checked 15, no_record 67, and the page prints "Not collected" for all
82 rows that are not `read`, so a name checked with nothing new and a name with no record read the same. The stale rule stays the
server's: `inputs.seekingalpha.state` is `stale` on one read row, and is `not_collected` on every checked and no-record row.

**Make it:**
1. `api/endpoints/amgt-lead-panel.ts`: add an exported interface `CoverageFreshnessSeekingAlpha` with the five fields above
   (`state: string`, `sentence: string`, the other three `string | null`) and an optional `seeking_alpha?: CoverageFreshnessSeekingAlpha | null`
   on `CoverageFreshnessRow`. Nothing else in that file changes.
2. `pages/Freshness/freshnessRows.ts`: `InputRead` gains two optional fields, `saState?: string` and `words?: string`. In `readInput`,
   for the key `seekingalpha` only, when the row carries a `seeking_alpha` object whose `sentence` is a non-empty string: return
   `collected: true`, `day` and `stale` read exactly as today from `row.inputs?.seekingalpha` (so a served-stale read row stays stale and
   no other row becomes stale), `saState` = the served `state`, `words` = the served `sentence`. Every other input, and a row with no
   `seeking_alpha` (an older body), reads exactly as today.
3. `pages/Freshness/Freshness.tsx`, the input cell: when the input carries `words`, print the served sentence verbatim, once, and give the
   `<td>` the attribute `data-sa-state` set to the served state. Keep `data-input` and `data-state` as they are. With no `words`, the cell
   is drawn exactly as today. The column is shown, and the note above the table never says "Seeking Alpha is not collected yet", whenever
   any covered row carries a served `seeking_alpha` (step 2 gives you this through `collected`).
4. Update the header comments of both page files in one line each to say the Seeking Alpha cell prints the served state's sentence.
5. `pages/Freshness/Freshness.test.tsx`: add one test, three rows (one per served state, sentences as above), asserting each cell's
   `data-sa-state` and sentence, and that no cell prints "Not collected". Do not change any other test unless it asserts the old
   Seeking Alpha text for a row that now carries `seeking_alpha`; then change only that assertion and name it in your report.

## 2. BOUNDS

1. No server, no fetch, no network, no install (`bun install`, `bun add`, `npm`, `npx` are refused here), no push, no deploy. REFUSE, do
   not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel). Do not match on the sentence's words and do not
   write a sentence of your own: the page prints what is served.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool ONLY; keep each file's line endings (all four files are CRLF).

## 3. SURFACES

<paths>
portal/src/api/endpoints/amgt-lead-panel.ts
portal/src/pages/Freshness/freshnessRows.ts
portal/src/pages/Freshness/Freshness.tsx
portal/src/pages/Freshness/Freshness.test.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~115/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zze-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round53/checks/r53a.cjs"; echo "exit=$?"</invocation><expect>THE SEEKING ALPHA COLUMN DRAWS THE THREE SERVED STATES APART: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zze-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~115/DSGN_AMGTV1.TO-AV-zze-1.seeking-alpha-column-three-served-states.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY), and only
when every criterion passes.
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W115-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the exact diff, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** PRD v0.18 @9a07662460 row SAUX-41 (FWD-27): "COO~D (this PRD), after COO~Z serves it (AMGT_RESAPP round 79)". CTO msg
  31675: "Rows 41 and 42 wait on AMGT_RESAPP round 79 serving the value first."
- **The dependency is met, measured by this seat:** AMGT_RESAPP `r79_deployed.py` against the deployed function, 2026-10-08 ~21:1xZ: "R79
  DEPLOYED: YES 1 of 1" (cc-7 redeploy @42700562a4). The live body (round53/served/freshness_page.json, snapshot 2026-10-08T18:08Z)
  carries `seeking_alpha` on 95 of 95 covered rows.
- **L5 decision:** the cell prints the served sentence verbatim; it does not compose a date of its own. The Freshness page already prints
  raw days, so the served sentence's ISO date is consistent with that page.
- **Neighbour:** AMGT_RESAPP `AMGT-cc-8` (staged, `2.0.0_SA_COO~Z`) walks this column on DEV read-only; no write surface is shared.

<status>complete</status>
<round>53</round>
<to_id>DSGN_AMGTV1.TO-AV-zze-1</to_id>
<slot>~115</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>

# DSGN_AMGTV1 task order -- `AV-zze-3` -- DIRECT ACT: THE POSTURE CITES CALL THE BUILT ANALYSIS "THE ANALYSIS BUILT FOR THIS NAME"

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zze-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~117</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; one page file.
comp-adversary: RUN by the issuer at the cut on portal DEV 38cc0ecf -- r53c.cjs 2 of 3 (arm 1 FAIL: 0 of 4 templates, "research pack" on 7 lines; arms 2 and 3 PASS). On a scratch edit of the file in the slot's own worktree 3 of 3; the edit was then reverted (0 changes).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zze-3` (round 53, decomposition v53; PRD row SAUX-40, FWD-27; a direct act under the size floor)

The path is `portal/src/pages/SecurityAnalysis/postureCites.ts`. Two different things were both called "research pack". The ruling: the
research team's own document is "the research team's pack" (already so everywhere else on the page); the thing the system BUILDS for a
name is "the analysis built for this name" (the function now serves that phrase as the built thing's source). In this file the words
"the research pack" mean the built thing, in four sentences and three comments.

**Make it -- replace exactly these four template strings (code), keeping everything around them:**

| line (about) | today | becomes |
|---|---|---|
| 90 | `` `a comparison measure the research pack names ${fieldWords(name)}` `` | `` `a comparison measure the analysis built for this name calls ${fieldWords(name)}` `` |
| 217 | `` `a figure the research pack names ${words}` `` | `` `a figure the analysis built for this name calls ${words}` `` |
| 288 | `` `the research pack does not say the comparable's ${...}` `` | `` `the analysis built for this name does not say the comparable's ${...}` `` (the `${...}` part unchanged) |
| 337 | `` `a filing passage the research pack cites, which no drafted sentence on ...` `` | `` `a filing passage the analysis built for this name cites, which no drafted sentence on ...` `` (the rest unchanged) |

**And the three comments** (about lines 80, 93 and 162) that quote these sentences: make each quote match the new wording. After the
edit the words "research pack" appear nowhere in the file. Change nothing else.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only `postureCites.ts` changes (plus your deliverables and the surprise channel). If a page harness under `__harness__/` asserts one
   of the four old sentences, update ONLY that assertion to the new wording and name it in your report.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool ONLY; the file is CRLF; keep it.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/postureCites.ts
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~117/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zze-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round53/checks/r53c.cjs"; echo "exit=$?"</invocation><expect>THE BUILT ANALYSIS IS NEVER CALLED THE RESEARCH PACK: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zze-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~117/DSGN_AMGTV1.TO-AV-zze-3.posture-cites-name-the-built-analysis.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY), and only
when every criterion passes.
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W117-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the exact diff, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** decomposition v52 (the CTO's ruling msg 31721: "The BUILT thing loses the word at the producer (AMGT_RESAPP round 79,
  cc-6: its source is served as 'the analysis built for this name')"); the prior session's carried item "the four postureCites.ts
  'research pack' sentences, which change with cc-6's rename" (`logs/2026-10-08/status_2031Z.md`).
- **The producer's value is live:** cc-6 AMENDMENT 1 (`top_band.py:36`), deployed by cc-7 @42700562a4; `r79_deployed.py` YES 1 of 1 at
  ~21:1xZ.
- **L5 wording decision:** "names" becomes "calls" so the sentence does not read "the analysis built for this name names".
- **Direct-act path:** one cell, one file, 4 strings and 3 comments, `<risk>LOCAL</risk>`; no L2, no L4-R, no L8-L10; its close is the
  issuer's one real run.

<status>pending</status>
<round>53</round>
<to_id>DSGN_AMGTV1.TO-AV-zze-3</to_id>
<slot>~117</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>

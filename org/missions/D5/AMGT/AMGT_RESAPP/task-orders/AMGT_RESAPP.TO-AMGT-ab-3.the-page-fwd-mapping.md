# AMGT_RESAPP task order -- `AMGT-ab-3` -- THE PAGE-SHAPED OUTCOMES, EACH MAPPED TO ITS DSGN_AMGTV1 OWNER OR TO AN ASK

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ab-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~187</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- reads two PRD files in the repo; no AWS call.
comp-adversary: RUN by the issuer at the cut -- AC1 grades every quote verbatim against both PRDs and refuses a silent retirement; base FAIL (file absent).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AMGT-ab-3` (round 52, decomposition s.60)

The Security Analysis page was redesigned under DSGN_AMGTV1 (fork F5: AMGT_RESAPP keeps the payloads, DSGN_AMGTV1 owns presentation).
Several AMGT_RESAPP forward outcomes describe PAGE PRESENTATION -- at least FWD-21, FWD-22, FWD-23, FWD-27, FWD-28 and FWD-29 -- which
DSGN_AMGTV1's own outcomes may now own (four header cards instead of Stat tiles; estate panels; one house form). **Build a read-only
mapping** so the CTO can re-home each outcome by cross-reference: for each page-shaped RESAPP outcome, find the DSGN_AMGTV1 outcome
(FWD-1..FWD-11 in its PRD) that now owns the same capability, or NONE.

Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~187/PAGE_FWD_MAP_ROUND52.json`:
`{"rows": [{"resapp_fwd": "FWD-22", "resapp_quote": "<a verbatim span of that FWD's clause>", "dsgn_fwd": "FWD-4" | null,
"dsgn_quote": "<a verbatim span of the DSGN outcome's clause>" | null, "relation": "covers" | "partly-covers" | "none",
"ask": "<what DSGN would need to own, or the one line naming the capability no longer promised>" | null}, ...]}`.
`covers` = the DSGN outcome promises the same capability; `partly-covers` = some of it (the ask names the rest); `none` = no DSGN
outcome promises it (the ask is required). Add a row for any OTHER RESAPP outcome you find is page-shaped (say why in its ask or
relation), one row per outcome. PRDs: `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` (ENDPOINT section; FWD lines ~427-783)
and `org/missions/D13/DSGN/DSGN_AMGTV1/prd/DSGN_AMGTV1_PRD.md`.

## 2. BOUNDS

1. READ ONLY. No PRD edit (the addendum is the CTO's), no product file, no AWS call. Your write surface is your deliverables folder and
   the investigation file.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~187/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ab-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round52/checks/ab_3_map.py; echo "exit=$?"</invocation><expect>rows N (required 6 covered: 6); relations {...}; EVERY PAGE-SHAPED OUTCOME HAS AN OWNER OR AN ASK: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ab-3" judgment="true"/>
</proof_of_spec>

AC2 (judgment, graded by `3.0.0_SA_CVO~Z` at L9, never self-graded): each row's `relation` follows from its two quotes read side by
side. Record it under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming the CVO.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~187/AMGT_RESAPP.TO-AMGT-ab-3.the-page-fwd-mapping.proof_of_spec.json`. Report once: the relation per outcome, every `none` with its ask, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-51 analysis item 3 / ruling 4. Base: AC1 FAIL (file absent). The CTO writes the PRD addendum on the mapping.

<status>pending</status>
<round>52</round>
<slot>~187</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

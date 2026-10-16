# NFRA_OPLGTW task order -- `OG-ev-1` -- the served harness writes ONE projected answer body per named marker, so the CVO can grade the AC3 judgment criteria of OG-ap-18, ap-19, ap-20, ap-21 and ap-23 (CVO ADJUDICATION_v29.Z.md @7f1ada5f4e, relayed by CTO msg 34905)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ev-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ev-1</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy; read-only calls through the installed code.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the calls run as the existing stand-in principals of your served harnesses.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is an instrument the CVO named (ADJUDICATION_v29.Z.md section "What closes them", option (b): "the applier re-running each release's served harness with ONE projected answer body per named tool written to the record (no secrets; client answers already mask accounts as ****<last4>)"). It widens nothing: it re-reads tools already live.
EGRESS CLASS, declared: NONE beyond Opal's own host and AWS.
</preflight>

## 1. THE CELL -- `OG-ev-1` (decomposition addendum R3-T.91, workstream ANSWER-BODIES, FWD-22)

THE GAP. The CVO cannot grade the AC3 of five round-37 orders because every served record you wrote holds per-tool booleans, counts and `answer_keys` (capped at 12 names), and no answer body: "A field name is not a reading." Each AC3 says the first answers must read as an analyst or research user would want them. This cell writes the answers to read.

DO. Run the served harness (your `ap23_served_harness.py` form, and the earlier `GT_`, `G36_`, `G5A_`, `P21_` harnesses where a release's tools are not in the ap-23 harness) against the INSTALLED code on the live host (release `3d5c9c8bf1` is live; the earlier releases' tools are in it), as your existing stand-in principals, READ-ONLY, and write `W/ANSWER_BODIES.json` (W = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`):

`{"read_at": "<iso>", "live_commit": "<sha>", "releases": {"ap-18": [ {"tool": "<name>", "marker": "<the marker below it shows>", "arguments": {...}, "body": <the tool's answer, projected>} , ... ], "ap-19": [...], "ap-20": [...], "ap-21": [...], "ap-23": [...]}}`

ONE body per named marker, with arguments chosen so the answer shows the marker (a call that cannot show it does not count: say so in a `note` field and file a BLOCKING row rather than substituting a different call):
- `ap-18` (typed G1 tools): (1) the newest-part counts of a typed answer; (2) `data_status` on a quiet name (a ticker with no recent rows); (3) `not_held` for a CUSIP the registry does not hold.
- `ap-19` (portal and news tools): (1) freshness stated in trading days; (2) `data_status` on a quiet day; (3) the 14-day news cap stated in an answer.
- `ap-20` (ETF ownership and fund tools): (1) weights in percentage points with their unit; (2) three dates in one row; (3) coverage from each partner's own csv.
- `ap-21` (published analysis): (1) the section asked for; (2) its as-of; (3) the 50 KB projection flagged.
- `ap-23` (client and rival tools): (1) a firm's data date stated; (2) figures with units; (3) rows never merged across firms (two-firm call, each firm's rows apart); (4) Schwab masters never summed (a Schwab master-account answer).
The body is the tool's answer after its own projection, as a JSON value, at most 12000 bytes (if larger, keep the first rows and set `"truncated": true` beside the body). No secrets, no tokens, no object content beyond what the answer returns; client answers already mask accounts as `****<last4>` and you do not undo that. NO account number, phone number, e-mail or person's name may appear in the file: if an answer carries one, replace the value with `"[masked]"` and say so in a `note` field.
Run it once; do not retry in a loop. Nothing is deployed, applied or written to any bucket or table.

## 2. BOUNDS

- Read-only calls through the installed code; one SSM command per harness run at most; no deploy, no apply, no `HALT_OVERRIDE`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print an account number, a token or a person's name.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/` (the tree convention grants it; it needs no entry). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free; a correction is a NEW row citing the old id), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from the repo root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ev-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ev1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)answer bodies: releases 5 of 5; bodies (?:1[5-9]|[2-9]\d); releases short of their minimum 0 \(want 0\); empty or non-JSON bodies 0 \(want 0\); bodies over 12000 bytes 0 \(want 0\); digit runs of 8 or more 0 \(want 0\); raw account_number keys 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the record holds one projected answer body per named marker for all five releases (16 or more), each a non-empty JSON value of at most 12000 bytes, with no long digit run and no raw account number.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ev-1.answer-bodies-for-cvo-grade.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if AC1 PASSes, and report once (commit hash, the AC1 line, and the marker list with any `note` or BLOCKING row). Tell the issuer the path; the issuer relays it to the CVO.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream ANSWER-BODIES (decomposition addendum R3-T.91). The CVO's v29: AC3 of `OG-ap-14` and `OG-hv-2` NOT MET (owed acts are other seats': `OG-mg-1` then the BBGTerminal seat's own 8-tool re-exercise; Andrew's stand-in read and the named asset manager's call); AC3 of `OG-ap-18/19/20/21/23` NOT MEASURED (no answer body on record). Option (a), the CVO's opalgateway MCP, is down (429); this cell is option (b).
- One criterion, mechanical (the existence and hygiene of the record); the grade itself is the CVO's judgment on the bodies, never this cell's.
- Pre-cut: ev1.AC1 base FAIL as expected (`ANSWER_BODIES.json` absent). The PASS arm is the applier's run; the issuer re-runs the check at the close.

- A1 (issuer, 2026-10-16 ~10:5xZ, rows Z-S168 to Z-S170; edits `OG-ap-19` A3 and `OG-ap-23` A8): (1) the `ap-19` marker "the 14-day news cap stated" belongs to `news_search_articles` (PRD G6 (c): a 14-day window cap); the recorded body came from `news_for_security`, which applies a 30-day window by its own contract (Z-S170, an observation, no defect). REPLACE that one body with a `news_search_articles` call asking for a window longer than 14 days, so the answer shows the cap applied. (2) The `ap-19` marker "`data_status` on a quiet day" is reworded in the order to an empty window with its as-of; the Sunday `news_search_articles` body already recorded stands. (3) The `ap-23` marker "Schwab masters never summed" leaves AC3 (no Schwab catalog row; Z-S169); its body stays as the recorded `no_catalog_row` answer. (4) Z-S171 (`harvest_get_published_analysis` peers unavailable once) is carried as an observation for the round-N analysis. The record keeps 16 bodies after the replacement; `ev1.AC1` is unchanged. Gate limb: none graded (a note on a completed order).

<status>complete</status>
<round>37</round>
<workstream>ANSWER-BODIES</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>

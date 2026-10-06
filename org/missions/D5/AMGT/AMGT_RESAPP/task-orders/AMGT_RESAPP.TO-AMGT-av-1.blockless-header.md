# AMGT_RESAPP task order -- `AMGT-av-1` -- EVERY UNCOVERED NAME'S OVERLAY SERVES THE SEVEN HEADER FIGURES, EACH A VALUE OR A PLAIN REASON (DSGN FWD-4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-av-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~237</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the overlay already reads; no write.
comp-adversary: RUN by the issuer at the cut -- r72 c39 FAILS on deployed: 137 of 138 uncovered names (the /freshness rows with covered=false and a key) serve no explained header figures; /overlay 404s for most (not in `_COVERED_NO_BLOCK_LEAVES`), and AAPL-like names serve `header_figures: []`.
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r72-237` (branch `wk-AMGT_RESAPP-237`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r72-237`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-av-1` (round 72, decomposition s.80)

**The measured state.** All 95 COVERED names already serve a full header: 612 values + 53 reasoned nulls, 0 unexplained.
The gap is the names with NO stored model block, which are outside the covered set:
- `lib/research/api/scoped_amgt.py` `_header_figures` (~`:2290-2296`) does `if not model_block: return header`, an empty header;
- `/overlay` is not in `_COVERED_NO_BLOCK_LEAVES` (~`:1016`), so most of those names 404 on it.

1. **For a name with no stored model block,** `_header_figures` serves the seven figures. They are price (`PX_LAST`), market cap
   (`CUR_MKT_CAP`), enterprise value (`CURR_ENTP_VAL`), net debt (`NET_DEBT`), beta (`EQY_BETA`), average volume (`VOLUME_AVG_30D`)
   and short interest (`SHORT_INT_RATIO`).
   - Each is `value: null` with a plain `reason` (e.g. "We hold no stored company data for this name yet"), the same entry shape as
     at-1's reasoned nulls.
   - Add `"overlay"` to `_COVERED_NO_BLOCK_LEAVES` so the overlay answers 200 for these names.
   - The 95 covered names' headers do not change.
2. **The census:** write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~237/HEADER_CENSUS.md` and `.json`. Over the 95 covered names plus the uncovered ones on /freshness:
   per name, figures served with a value, figures null with a reason, and each reason's cause, with totals.
3. **The plant test** `lib/research/api/tests/test_header_blockless.py`: a blockless name serves 7 reasoned entries; a name with a
   block is unchanged.

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W237-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. Add reasoned entries and the leaf only. No covered name's header value changes.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~237/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-av-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_header_blockless.py; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-av-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round72/checks/r72_served.py" --cell c39 --where local; echo "exit=$?"</invocation><expect>population uncovered names with a key 138 (or the count /freshness serves); C1 PASS failing 0; R72 C39 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~237 <0.9.0_WK_AMGT_RESAPP~237@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~237/AMGT_RESAPP.TO-AMGT-av-1.blockless-header.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the census totals;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-71 analysis item 1, ruling 4. The premise is corrected in s.80a: ROG is fine on the producer; the gap is the uncovered names. Served by av-8.

<status>pending</status>
<round>72</round>
<slot>0.9.0_WK_AMGT_RESAPP~237</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-05 ~22:4xZ):** CLOSED -- drained @3e32ecca8f. On the shared tree, c39 local reads 138 of 138 (YES). The census reads covered 612 values / 53 reasoned / 0 unexplained and uncovered 7 / 959 / 0. proof VALID. No rows. Served by av-8.

<status>complete</status>

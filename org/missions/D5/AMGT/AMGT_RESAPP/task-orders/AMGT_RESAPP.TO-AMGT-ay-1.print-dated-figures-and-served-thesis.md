# AMGT_RESAPP task order -- `AMGT-ay-1` -- THE PRINT DATES EACH FIGURE WITH ITS OWN PERIOD, AND READS THE THESIS /thesis SERVES (FWD-5, CTO RULINGS 1 AND 2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ay-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~257</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- the print already reads what /thesis reads; no new store read.
comp-adversary: RUN by the issuer at the cut -- r75 c57 and c58 FAIL on deployed 0MZWPl7n: 368-491 fiscal-year lines per print stamped with the run date, which appears 743-856 times per print; the BA print carries 0 of the 17 sentences /thesis serves and says "No investment thesis has been written".
EGRESS CLASS, declared: NONE. No vendor, SEC or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r75-257` (branch `wk-AMGT_RESAPP-257`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r75-257`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ay-1` (round 75, decomposition s.83)

PRD v0.40 FWD-5 (`:521-525`). Row Z-W256-S1. `lib/research/print/render_pack.py` writes every field as one line,
"Label: value - as of <date> - Bloomberg", and today stamps every line with the RUN date.
1. **Ruling 1: each figure carries ITS OWN period or as-of.**
   - A fiscal-year figure reads its fiscal year (the line sits under its "Fiscal year YYYY" heading; it does not carry the run date).
   - A market figure (share price, market cap) reads its quote date from the stored figure.
   - Where the stored figure carries no date, the line says so in plain words.
   - The print's RUN date appears ONCE, on page 1, in the header, as `YYYY-MM-DD`.
2. **Ruling 2: one reader.** The print reads the drafted sections from the SAME function the `/thesis` route serves them from
   (`lib/research/api/scoped_amgt.py`; read it, do not edit it). Each section prints its served sentences. "No <section> has been
   written" appears only where `/thesis` serves no sentence for that section.
3. **Plant tests** in `lib/research/print/`.

No figure value changes. Report the per-print counts before and after.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W257-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/api/` is read only for this cell.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/print/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~257/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ay-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round75/checks/r75_served.py" --cell c57 --where local; echo "exit=$?"</invocation><expect>0 fiscal-year lines stamped with the run date and the run date once, on page 1, on 3 of 3 prints; C1 and C2 PASS; R75 C57 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ay-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round75/checks/r75_served.py" --cell c58 --where local; echo "exit=$?"</invocation><expect>the BA print carries 17 of 17 served sentences (or every sentence served at run time) and no 'not written' line for a served section; C1 and C2 PASS; R75 C58 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ay-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/print; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~257 <0.9.0_WK_AMGT_RESAPP~257@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~257/AMGT_RESAPP.TO-AMGT-ay-1.print-dated-figures-and-served-thesis.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the print suite's last line;
- per print: fiscal-year lines with the run date, before and after;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-74 analysis items 1-2, rulings 1-2. Served by ay-5. The CVO reads three rendered prints at L9.

<status>pending</status>
<round>75</round>
<slot>0.9.0_WK_AMGT_RESAPP~257</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-06 ~10:5xZ):** CLOSED -- drained @f5639411fb. On the shared tree, r75 c57 local YES (0 fiscal-year lines with the run date; run date once, page 1, on 3 of 3) and c58 local YES (BA 17 of 17); print 105 passed. Rows Z-W257-S1 (no stored quote date: market lines say so in words) and S2 INERT.

<status>complete</status>

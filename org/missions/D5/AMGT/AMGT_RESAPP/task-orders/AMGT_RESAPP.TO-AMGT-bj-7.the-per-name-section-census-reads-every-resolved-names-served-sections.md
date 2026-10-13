# AMGT_RESAPP task order -- `AMGT-bj-7` -- THE PER-NAME SECTION CENSUS OF THE SERVED PAYLOADS: RUN THE PREPARED INSTRUMENT OVER EVERY RESOLVED NAME (FWD-40 (a); AN INSTRUMENT RUN)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bj-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~408</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bj-7.the-per-name-section-census-reads-every-resolved-names-served-sections</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot read run; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- the instrument invokes the existing function with GET events and reads S3 under the box's own role; no grant, key or policy is touched.
comp-adversary: RUN at the cut -- `r103_section_census.py --selftest` reads `arms passed 7 of 7 ... R103 CENSUS ARMS: YES`; its negative arm (an empty section with no reason) classes UNEXPLAINED and a raw code under a rendered key is a candidate while the same string under `security_key` is not; offline on the dumped ASML_NA overlay (24 keys) it classes 20 FILLED and 1 REASONED over 21 sections (the three `_absent_reason` companions are not sections) and 29 raw-code candidates, all `peers` rung names and horizon labels.
EGRESS CLASS, declared: NONE beyond the existing Lambda invoke (GET) and S3/DynamoDB reads; no Bloomberg call, no vendor call, no write.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-408` (branch `wk-AMGT_RESAPP-408`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-408`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bj-7` (round 103, decomposition s.112)

FWD-40 (a) of PRD v0.44 (ratified text, inlined; the census is its instrument):

```
  FWD-40 Security Analysis V1: all 93 names complete, correct, clean and fast on PROD
         DONE WHEN  EXERCISED -- over the 93 names of AMGT_CORPUS FWD-19's
                    population (printed, with the 95 covered names and the 105
                    pack prefixes reported beside it, every difference named):
                    (a) a per-name census read from the PROD-served payload:
                    every section of every name shows content OR a stated
                    reason, and 0 BROKEN VALUES. A broken value is a CONFIRMED
                    hit (a screenshot read confirms it) of the ui-walk classes
                    `unconnected-field`, `raw-code` and
                    `format:money`, or of the minor-unit census (qq-1's
                    instrument); "raw code" is as FWD-5 uses the term;
```

The page calls six routes once a name is chosen (overlay, thesis, peers, coverage, versions, ledger). The instrument is PREPARED and dry-run; you run it, you do not edit it. It reads every resolved name's six served bodies from the live function (Lambda invoke, GET only) and classes every top-level section FILLED (content), REASONED (empty with a stated reason) or UNEXPLAINED (empty, no reason: the defect class), lists BROKEN-VALUE CANDIDATES (a candidate is NOT a verdict: the draw's screenshot read confirms or clears it, `AMGT-bj-11`) and prints the POPULATION (resolved names, the pack prefixes under `packs/`, each difference named).

1. Run AC1 (offline self-test). 2. Run AC2: it writes `census_sections.json` and `census_sections.txt` in your deliverables folder and prints the verdict line. 3. Run AC3 (the minor-unit census FWD-40 (a) names; it reads the live peers routes of every measured subject).

Then report, from `census_sections.txt` and without judging: the POPULATION lines in full; the `UNEXPLAINED` line in full (it lists up to 40); the `STATUS not 200` line; and the first 15 BROKEN-VALUE CANDIDATE pattern lines. You do not decide whether FWD-40 (a) is met: the CVO grades it.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W408-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Run ONLY the three invocations below and the instrument as written; do not edit any instrument, do not re-run AC2 to get a different number (if it fails, report the output and a row).
2. Read-only against the world: no write to S3, DynamoDB or the function; at most 4 parallel readers (the instrument's default).
3. Your files: your deliverables folder only. No push of shared branches. No `pip install`.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~408/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation is bounded by its own `timeout 590`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bj-7"><invocation>cd C:/dev/wk-resapp-408 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_section_census.py" --selftest | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>`arms passed 7 of 7`, `R103 CENSUS ARMS: YES`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bj-7"><invocation>cd C:/dev/wk-resapp-408 &amp;&amp; PYTHONPATH="$(pwd)" timeout 590 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_section_census.py" --where deployed --workers 4 --out "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~408/census_sections.json" > "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~408/census_sections.txt" 2>&amp;1; echo "exit=$?"; tail -2 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~408/census_sections.txt"</invocation><expect>`exit=0` and the last line `R103 SECTION CENSUS: RAN N of N names (0 read failures)` with both N equal (the resolved names, 95 at the cut)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bj-7"><invocation>cd C:/dev/wk-resapp-408 &amp;&amp; PYTHONPATH="$(pwd)" timeout 590 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round92_prep/checks/r92_minor_unit_census.py" --where deployed | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R92 MINOR-UNIT CENSUS: YES`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~408 <0.9.0_WK_AMGT_RESAPP~408@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~408/AMGT_RESAPP.TO-AMGT-bj-7.the-per-name-section-census-reads-every-resolved-names-served-sections.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- the three criteria's output lines;
- the POPULATION lines, the UNEXPLAINED line, the STATUS-not-200 line and the first 15 candidate lines of `census_sections.txt`, verbatim;
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** FWD-40 (a) as ratified in v0.44 asks for sections filled or reasoned and 0 CONFIRMED broken values. This order produces the census and the candidates; the grade is the CVO's (judgment on screenshots) and the walk (`AMGT-bj-11`) confirms or clears candidates. READ-ONLY, so its class is LOCAL. STAGED behind `AMGT-bj-2`: the census invokes the function, and the driven first request must be alone (no other reader) until RA1 reports. The issuer flips it pending at `bj-2`'s completion. The three `_absent_reason` keys are companions, not sections (the instrument skips them).

<status>staged</status>
<status>pending -- GO 2026-10-13T19:1xZ by the issuer (2.0.0_SA_COO~R1): RA1 released the function at 19:11Z (msg 5085; `AMGT-bj-2` applied 18:55Z, AaACnKtr.., first cold request 3,770 ms NOT MET, the apply stands). Run AC1 to AC3 as written. The function is read by this order alone until it reports: `AMGT-bj-8` stays staged behind it so its per-name timings are not taken under this order's load.</status>
<status>complete -- 2026-10-13T19:5xZ by the issuer (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-408 @c728cdeca6 merged @a1d12f5201, proof instance VALID (rc=0). AC1 PASS (7 of 7 arms), AC2 PASS (`R103 SECTION CENSUS: RAN 95 of 95 names (0 read failures)`, status not 200: 0), AC3 PASS (`R92 MINOR-UNIT CENSUS: YES`). THE ISSUER'S READING (deliverables/2.0.0_SA_COO~R1/round103/V1_SECTION_CENSUS_READING.md): the v1 instrument's UNEXPLAINED 575 was mostly its own error (a sibling `drafting_reason` or `reason` was not read as the section's reason; a null `reason` key was counted as a section); the v2 instrument (11 of 11 arms, the issuer's run 19:29Z, 95 of 95) reads 3 UNEXPLAINED, all `thesis.model_cases` with the reason nested inside each case, so 0 sections empty with no stated reason, and 187 STATE_ONLY (the `/coverage` route: NEVER_HELD on all 95 names while the overlay's feed serves items; the route has no caller on the page at DEV or PROD, so it is not rendered). Population: 95 resolved, 93 with an exact-key pack, 2 under the slash-safe key, 105 prefixes (3 bare-ticker forms, 7 with no resolved name, named). 9,607 broken-value CANDIDATES in 896 patterns, all raw-code, none confirmed: the walk (`AMGT-bj-11`) and the CVO decide. Rows W408-S1 (the folder did not exist) and S2 (no 93 figure printed: the reading above derives it) are observations, DISMISSED.</status>
<round>103</round>
<workstream>V1</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~408</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

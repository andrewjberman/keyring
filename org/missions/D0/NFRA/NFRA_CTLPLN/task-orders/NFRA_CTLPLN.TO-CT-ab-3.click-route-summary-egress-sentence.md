# TO NFRA_CTLPLN.TO-CT-ab-3 -- workstream THREAD round 12 (cell CT-ab-3): add the one missing limit to the plain-language click-route summary -- nothing on the network stops a download; the setting governs pip only

<to_id>NFRA_CTLPLN.TO-CT-ab-3</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~83</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ab-3` (`decompositions/NFRA_CTLPLN_DECOMP.round12.md`) | **outcome_ref:** FWD-17, FWD-1 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

The file `C:/Users/AndrewBerman/Desktop/ajb_wk/<your worktree>/org/tier2_senior/0.7.0_AE_CloudOps~CT1/deliverables/NFRA_CTLPLN.TO-CT-aa-2.click-route-plain-summary.md` (220 words) is a plain-language summary of a click-package route to dell1. Its `## What was not shown` part ends with two sentences: `The refusal did not tell anyone to ask the laptop. Other tools, other Python installs, and programs already running are not covered.` A reader graded the file NOT MET for one omission: it never says that nothing on the network stops a download, because the `PIP_NO_INDEX` setting governs pip only.

### BUILD

1. In that part, replace the final sentence (`Other tools, other Python installs, and programs already running are not covered.`) with exactly: `Nothing on the network stops a download: the setting governs pip only, so another program, another Python install, or a browser can still download, and programs already running are not covered.` Change nothing else in the file.
2. If the file then exceeds 240 words including headings, shorten the sentence `The download command ran twice, not once.` no further than needed; drop no other fact or limit. Do not soften or add any claim.
3. Commit the one file with `.tools/safe-commit.sh` as your serial.

### RULES FOR THIS CELL

Write surface = the `<paths>`. No aws, no network, no push; run nothing but the criteria. `.tools/safe-commit.sh` for every commit. Do NOT commit the `portal` gitlink. ASCII only. CLAUDE.md and org/XXX.md are LOCKED. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W83-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTab3-AC1" cell_refs="CT-ab-3"><invocation>python -c "import sys; t = open(sys.argv[1], encoding='utf-8').read(); print('WORDS-OK' if 0 < len(t.split()) <= 240 and 'pip only' in t else 'WORDS-BAD')" org/tier2_senior/0.7.0_AE_CloudOps~CT1/deliverables/NFRA_CTLPLN.TO-CT-aa-2.click-route-plain-summary.md</invocation><expect>WORDS-OK</expect></criterion>
`CTab3-AC1` -- the file holds 1 to 240 words and the words `pip only`.

<criterion id="CTab3-AC2" cell_refs="CT-ab-3" judgment="true"/>
`CTab3-AC2` (JUDGMENT, regraded by `3.0.0_SA_CVO~L`, never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a `status_reason` naming the CVO): read aloud to a listener who is not an engineer, does the text now say what the records show and what they do not, with every stated limit present, the egress limit included, and none softened or invented?
</proof_of_spec>

<expected_criteria>CTab3-AC1,CTab3-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~83/NFRA_CTLPLN.TO-CT-ab-3.click-route-summary-egress-sentence.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTab3-AC1,CTab3-AC2`, and leave the status flip to the issuer (AC2 is the CVO's).

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round12.md</decomp_doc>
<owned_cells>CT-ab-3</owned_cells>
</decomp_ref>

<paths>
org/tier2_senior/0.7.0_AE_CloudOps~CT1/deliverables/NFRA_CTLPLN.TO-CT-aa-2.click-route-plain-summary.md
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule; one file.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a sentence that softens the limit ("mostly stops downloads"); a sentence that drops another fact to fit (the bound is 240 words); BLIND: a listener who needs the command lines (the records stay the reference).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round11.md section 3 item 2; adjudication row C-S38. Re-routed from `0.7.0_AE_CloudOps~CT1` (dell1, stopped) on dell1's CTO ruling, `deliverables/2.0.0_SA_COO~C/CT-ab-3_REROUTE_RULING.md`; the dell1 copy of this order is `superseded`. Executor change only; the gate's verdict on this commit is stated in the commit message.

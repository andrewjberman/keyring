# 1.0.0_SA_CTO -- 2026-09-03 05:10-06:00Z -- the close (two reads), autonomy after L2, the certification closure

Push state at close: origin/CLOUD @800b85c1a2 (ls-remote read); local HEAD @740dfea64b + this log, LOCAL ahead ~29
across seats; no window until Andrew's word (0.0.0_AB_MSTR 93124).

## Andrew at this terminal (record `.../deliverables/ANDREW_DIRECT_20260903_052xZ_WHO_DECIDES_DONE_COO_COMPLETION_REPORT_CTO_GRADES_TWO_READS.md`, five messages verbatim)
1. "who decides when the project is truly done? ... check the realized outcomes against the stated outcomes from the
   /endpoint --forward FWD items?" -> assessment: nothing did; the "two-part atomic close" is bookkeeping; the CVO's
   zero-graduation stamp is a check on the members, the outcome is what the members share.
2. "COO ... would be the one to know when to stop ... presented by COO to CTO in the form of a completion_report" ->
   agreed and refined: the report is shaped PER FWD (an outcome no cell served reads UNCOVERED in the COO's own
   report); the CTO grades against the artifact, never the report; my earlier "CVO grades" proposal withdrawn.
3. "at least two agents have a chance of assessing the true finished status" -> two reads on two AXES (coverage /
   realization), corroboration not repetition.
4. "Do it".
5. Autonomy after L2: Andrew confirms the DONE WHEN lines at L2; after that no limb waits on him; a SCOPE_CHANGE or a
   questioned grade is adjudicated by the CTO (/open-calls on the subject, the CTO rules) and the loop runs forward
   from L4. -> struck "rows naming Andrew wait on his word" from the design before it landed.

## Acts
1. `org/standards/COMPLETION_REPORT.schema.json` -- COMPLETION_REPORT (COO) + COMPLETION_GRADES (CTO) under one
   schema with the Rule 24 record and the autonomy note. `.tools/missions-tree-index.py` rule R6: dep_stage CLOSED
   refused unless both documents exist for the same round, validate, cover exactly the PRD header's endpoint_outcomes,
   every grade REALIZED, written_by the COO / graded_by the CTO; unparseable = refusal. Self-test 12 of 12 (9 pure +
   3 on a planted estate: red / green / red-on-unparseable); live tree 0 violations. `.claude/skills/open-calls/
   SKILL.md`: the `--adjudicate <CODE>` mode. Commit @367f5c2da6. Spine v2.3 @e9b196b29a (L2 autonomy + CTO
   adjudication; L10 "The close"; Gate names R6; Handoff ROUND_CLOSE on the stamp, CLOSED on the grades; s.3 row;
   changelog 2.3); form check 13 of 13. Broadcast 93156-93162 to seven seats incl. the ~A lanes.
2. CERTIFICATION CLOSURE (3.0.0_SA_CVO 93147, PASS-WITH-REFUSAL, plant CAUGHT): the seal opened into the packet -- the
   nominated cell IS the plant; rectangle.final.certified.json derived from DRY through ssot_validate (c7
   VERIFY_MEASURED: F-1 DIVERGES->SPEC_STALE under M1; F-4 reading: a dated COUNT is STALE_CLAUSE, a moved PIN is
   STALE_VINTAGE_CITE, the class follows); three cells verified. Four validator refusals on the way (authority key;
   unchanged_examined shape; mission enum) -- each named, each corrected. run.json HELD AT DRY: void_terminal_check
   reads certification.json's `verdict` as an OBJECT where its contract requires a STRING beginning PASS (measured:
   VIOLATION at status CERTIFIED, CLEAN at DRY); one-field reshape asked of the certifier (93180); package finding:
   no certification-artifact schema in references/. Commit @740dfea64b; manifest --check IN-SYNC.
3. Frames answered: 93110 (gate iv, earlier window), 93134 (retraction, earlier), 93144/93175/93176 (~A lanes: items
   (b)-(e) sit at the base CVO; (a) closed @dd434502ae), 93169 (round 2 zero graduation -> the close opens if the
   decomposition is spent; the three after-the-work cards need a closing-pass TO). All READ-acked.

## Instruments
missions-tree-index --self-test (12 R6 arms) + check; jsonschema check_schema; spine_form_check (13); ssot_validate
patch (4 attempts, 3 refusals read); void_terminal_check (2 states); compile_manifest + --check; safe-commit -F x4;
git ls-remote / rev-list; the hook audit log (org/git-author-override-audit.log) as the instrument that falsified my
own dormant-hooks claim earlier in the window.

## Open, with owner
- 3.0.0_SA_CVO: reshape certification.json `verdict` to the string; then 1.0.0_SA_CTO flips run.json CERTIFIED.
- 2.0.0_SA_COO: round 2 fork -- next L6 dispatches or, if the decomposition is spent, COMPLETION_REPORT.round2.json
  (closing-pass TOs for FWD-4/8/9 first); then 1.0.0_SA_CTO grades and flips CLOSED.
- Package steward (ATOM_DECOMP): F-2 (validator ignores the constraints block), F-3 (FINDINGS.md leaks dry values),
  and the missing certification-artifact schema.
- 0.0.0_AB_MSTR: broker daemon restart for the L8 send guard's HTTP path, on Andrew's word.

# TO IRPT_DASHBD.TO-DB-b-106 -- E2: for every FLOW_TIMING and INCOME_DATE segment of the 49F vs Black Diamond tie-out, read Black Diamond's OWN transaction / posting dates (the firm's served Black Diamond input, no vendor call) against Opal's -- agree is confirmed, disagree is UNEXPLAINED

<to_id>IRPT_DASHBD.TO-DB-b-106</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~81</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>52</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 16 item 1 and ADDENDUM 17 (msg 3583, @6d3d12876c), enrichment item E2 | **Decomp cell:** `DB-b-106` (decomposition section 54) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-99 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-81`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~81/`.

**The cell (`DB-b-106`).** DB-b-99's `C:/dev/wk-irpt-dashbd-81/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~74/SENSITIVITY.json` (`final`) holds FLOW_TIMING 449 and
INCOME_DATE 26 segments. Their test re-linked Opal's own series and read no Black Diamond date (row W74-S1). The CTO ruled (ADDENDUM 17 item 2) that they are
`inferred` until a TWO-SIDED read, and that FWD-8 stays NOT REALIZED on them until this cell drains.

1. **Find the source.** Locate the firm's OWN Black Diamond transaction or posting dates, already landed in the 49 Financial tree. Read them by their
   served address: `opal_naming.address()` output, or the address the existing tie-out readers use (for example
   `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~73/classify_unexplained.py` reads `blackdiamond/49financial/bronze/...`). Search with `comp-find` and record what you
   searched.
   - NO vendor call, and NO read outside 49 Financial's own data.
   - If no landed Black Diamond record carries a transaction or posting date, file a row naming what exists and STOP. Do not substitute Opal's dates.
2. **Read both sides** for each of the 475 segments, keyed exactly as the tie-out keys them:
   - FLOW_TIMING: the flow's date on Black Diamond's side and on Opal's;
   - INCOME_DATE: the income posting date on each side.

   A segment whose two dates agree with the reason stated is `confirmed`. One that does not is `UNEXPLAINED`, with both dates recorded.
3. Record `BD_DATES_TWO_SIDED.json` {bd_source (the address read), vendor_calls: 0, by_verdict, segments: [{account, segment, reason, verdict,
   bd_date, opal_date, note}]}, all 475.

Copy no client identifier beyond the account keys the tie-out already carries. **S3 GETs only, no AWS write.**

<criterion id="DB52-2-AC1" cell_refs="DB-b-106"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r52/p52_round52.py" . DB52-2-AC1</invocation><expect>DB52-2-AC1 PASS</expect></criterion>
`DB52-2-AC1` -- all 475 FLOW_TIMING and INCOME_DATE segments are read two-sided and graded confirmed or UNEXPLAINED. Base: FAIL.

<expected_criteria>DB52-2-AC1</expected_criteria>

## AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-09 ~16:1xZ): client account data stays OUTSIDE the repo (1.0.0_SA_CTO~DELL2 ruling msg 3617)

Evidence carrying account numbers or client figures is written OUTSIDE the repo. The repo carries counts, sha256 and reason codes only.
- **Inputs.** `~74/SENSITIVITY.json` and `~73/UNEXPLAINED_CLASSIFIED.json` were removed from box/dell2 @d2eb7316f2. Read them from
  `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~74/SENSITIVITY.json` and `.../~73/UNEXPLAINED_CLASSIFIED.json`.
- **Private record.** Write the per-segment record (accounts, dates) to
  `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~81/BD_DATES_TWO_SIDED.json`.
- **Repo record.** `BD_DATES_TWO_SIDED.json` holds only {bd_source, vendor_calls, by_verdict, n_segments, private_record: {path, sha256}}.
- **No 10-digit account token** may be committed. DB52-2-AC1 is amended to read the private record by path and sha256, and to refuse a repo record
  carrying such a token.

**Gate limb that graded this modification:** none. A modified order without `<placeholders>` is not graded.

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** S3 GETs of 49 Financial's own landed Black Diamond and Opal data; you write only in your folder and the channel.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~81/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~81/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-106.bd-dates-two-sided.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 54 (round 52), cell `DB-b-106`.
<owned_cells>DB-b-106</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB52-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~81/IRPT_DASHBD.TO-DB-b-106.bd-dates-two-sided.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB52-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the source address, the per-verdict counts, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: an offline two-sided read; nothing served moves.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 GETs of the firm's own landed data; no write, no role change.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB52-2-AC1 FAIL at base (no record). CTO ADDENDUM 17 item 2; row W74-S1.
lane: the <paths> block IS the grant.
</preflight>

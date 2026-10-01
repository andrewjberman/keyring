# NFRA_OPLGTW task order -- `OG-tx-2` -- workstream TRNSPT-DEPS (O1 live): grade the transcript tools' live reach on the four meetings

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-tx-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~15</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a grading read; no cron, alarm, monitor or cadence. HELD on G-TEAMS-TX (Andrew via IT).
comp-iam: DECLARED-NOT-APPLICABLE -- reads the audit sink with existing access.
comp-adversary: DECLARED-NOT-APPLICABLE -- the acceptance is the spec's section 6 steps 1-4, admitted by PRD v1.2 C7.
EGRESS CLASS, declared: NONE beyond Opal's own AWS, read-only.
</preflight>

## 1. THE CELL -- `OG-tx-2` (decomposition addendum R3-T)

The ISSUER runs `docs/briefs/opal-gateway-meeting-transcript-tools-spec-20260929.md` section 6 steps 1-4, signed in as
Andrew through the released interactive tools. It writes the raw run record to
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/TRANSCRIPT_REACH_RUN.json`, which holds ids, counts,
hashes and timestamps, and NEVER transcript text. You grade that record against the gateway audit. You call no tool
and sign in nowhere.

1. Read the run record. For each of the 4 meetings, take `rows`, `total_bytes`, `body_bytes_measured`,
   `last_cue_vs_end_s`, `speaker_tags`, and the transcript ids read. Take the negative arm's outcome too (a meeting
   Andrew is not invited to, refused).
2. For every recorded read, find the audit record under `opal-mcp-audit` that carries the same transcript id and byte
   count. Set `audit_match` per meeting.
3. Write `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/TRANSCRIPT_REACH.json` with
   `meetings` (4 objects carrying the fields above plus `audit_match`) and `negative_arm.refused`. Ids, counts and
   hashes only.

If the run record is absent, file a BLOCKING row and stop.

## 2. BOUNDS

1. Read only: the record and the audit sink. No tool call, no sign-in, no grant change. No transcript text in the
   repository or on stdout.
2. Work in the worktree named in your identity line. Never push, merge, rebase, stash, `checkout --` or `clean`.
3. Commit with `.tools/safe-commit.sh` under your serial.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W15-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-tx-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/tx2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)meetings passing all four of 4 required: 4 of 4 recorded; negative arm refused=True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="J1" cell_refs="OG-tx-2" judgment="true"/>
</proof_of_spec>

- `AC1`: REACH, COMPLETENESS and ATTRIBUTION on 4 of 4 meetings, the negative arm refused, and each read matched in
  the audit.
- `J1`: graded at L9 by `3.0.0_SA_CVO~O`. The four meetings are the four the spec names (the 9a ET Monday Meeting,
  the OCIO investment committee, the Asset Management investment committee, the Research Meeting), and REACH covers
  at least one where Andrew is an invitee, not the organizer (the spec's hypothesis). RECORD; NO VERDICT.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/NFRA_OPLGTW.TO-OG-tx-2.transcript-reach-live.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Record J1 as `UNVERIFIABLE-BY-INSTRUMENT` naming
`3.0.0_SA_CVO~O`. Report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~15, queue position 4. HANDED only after `OG-rl-1` closes AND G-TEAMS-TX is read back
  (`Get-CsTeamsMeetingConfiguration -Identity Global` shows both properties True). The issuer's own gateway session is
  signed in as Andrew (`whoami` 2026-10-01), so the issuer makes the run.
- The REACH hypothesis may fail (spec section 2). Then this cell FAILS AC1 honestly, and the application route in the
  recon brief goes to the CTO as an analysis item, never as a widening here.

<status>staged</status>
<round>8</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>

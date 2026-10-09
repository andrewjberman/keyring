# TO NFRA_TRNSPT.TO-TR-x14 -- the curated securities exception list (Apple first), with its gate test

<to_id>NFRA_TRNSPT.TO-TR-x14</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~3</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>transcripts</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-x-14` (`decompositions/NFRA_TRNSPT_DECOMP_R14.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-x-14` (CTO msg 1745 / round-11 analysis E1): "a curated exception list, as its own versioned data asset beside the allowlist. Each entry names
an issuer token that collides with a person name, with its ticker, the reason, and the evidence that Opal portfolios hold it. Admit only tokens
whose person-name use is implausible in a client context (start with Apple) ... Gate: a planted-token test still wipes a planted person or client
name that collides with a listed token in a non-issuer context, or else the entry is refused." Round 11 excluded every allowlist name token that
is also a person-dictionary word (556 of them), so "Apple" is wiped today.

**Read (do not edit):** `data/transcripts/scripts/teams/securities_allowlist.py` (the builder and its person-collision exclusion),
`data/transcripts/scripts/outlook/wipe.py` (rule 4 at :9 -- the allowlist is checked first per token, EXCEPT where a salutation/title precedes it
or a neighbouring capitalised non-allowlisted dictionary name sits beside it, :211-212), `data/transcripts/scripts/tests/test_securities_allowlist.py`,
and the holding evidence `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R12_HOLDING_EVIDENCE_AAPL.json` (PFDE holds AAPL "Apple Inc", as of
2026-10-07, source `s3://opal-data-portal-v2/platinum/etfs/positioning_data.json`).

**Build:**
1. `data/transcripts/scripts/teams/securities_exceptions.json` (new, versioned): `{"_provenance": {...}, "version": 1, "entries": [{"token":
   "Apple", "ticker": "AAPL", "reason": "<why a person named Apple is implausible in a client context>", "holding_evidence": "<the evidence
   file path + fund + as_of>", "cvo_review": "pending"}]}`.
2. `securities_allowlist.py`: after the person-collision exclusion, RE-ADD each exception entry's token (exceptions win over the exclusion, and only
   they do); record `exceptions_applied` in the provenance. Re-generate `securities_allowlist.json`.
3. `data/transcripts/scripts/tests/test_securities_exceptions.py` (new), through the research fold's wipe, at least:
   `test_apple_survives_as_issuer` ("Apple reported earnings" -> "Apple" kept); `test_apple_as_person_name_still_wiped` ("Mr. Apple called" and
   "Apple Smith joined" -> "Apple" wiped, by the wipe's name-context rule); a test that an entry with no ticker or no holding evidence is refused by
   the builder.

### ACCEPTANCE

<criterion id="TR14-x14-AC1" cell_refs="TR-x-14"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R14_CHECKS/r14_checks.py x14</invocation><expect>R14-X14-OK</expect></criterion>
`TR14-x14-AC1` -- Apple survives as an issuer and is still wiped as a person name.

<expected_criteria>TR14-x14-AC1</expected_criteria>

Dry-run at the base (box/dell2 1440a9d3d1): `R14-X14-FAIL absent` -- FAIL as expected. The CVO reviews the entry; the re-fold and re-write of the
29 stored objects are a later served act. Keep `test_securities_allowlist.py`, `test_wipe_planted.py` and the research tests green.

## BOUNDS

- **Grant.** The four paths below, this order's file, your deliverables folder. `wipe.py` and the evidence file are READ only.
- **LOCAL.** No AWS, HTTP or gateway call; synthetic text only; no S3 write.
- **Refusal clause (the CTO's own):** if "Apple" in a name context is NOT wiped, the entry is refused: leave it out, keep the test failing, and file a
  surprise row (id `NFRA_TRNSPT-D2-W3-S<k>`, next unused across every document under `surprise-channel/`). Never weaken the wipe.

<paths>
data/transcripts/scripts/teams/securities_exceptions.json
data/transcripts/scripts/teams/securities_allowlist.py
data/transcripts/scripts/teams/securities_allowlist.json
data/transcripts/scripts/tests/test_securities_exceptions.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R14.md</decomp_doc> (round 14), cell `TR-x-14`.
<owned_cells>TR-x-14</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR14-x14-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~3/NFRA_TRNSPT.TO-TR-x14.securities-exceptions.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR14-x14-AC1` BEFORE the flip. Commit code first, then pin each artifact to a
commit that contains it.
</proof_of_spec>

**REPORT:** the entry, the allowlist token count before/after, the test names, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a data asset and a builder change.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- 4 sources read (securities_allowlist.py, wipe.py rule 4 and :211, its test, the AAPL evidence); BLIND to how often "Apple" is a person in the real meetings. Traps: an exception that also lets a person named Apple through, an entry without evidence, a weakened wipe; the gate test and the refusal clause cover each.
lane: two teams data files, the builder, one test, the investigation file.
</preflight>

Source: CTO msg 1745; round-11 analysis E1; decomposition round 14 cell TR-x-14 and issuer ruling 3.

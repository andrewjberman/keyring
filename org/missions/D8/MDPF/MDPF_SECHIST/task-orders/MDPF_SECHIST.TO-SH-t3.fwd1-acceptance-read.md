# TO MDPF_SECHIST.TO-SH-t3 -- round 2 SH-t-3: the FWD-1 acceptance read on the first unassisted scheduled pull

<to_id>MDPF_SECHIST.TO-SH-t3</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~4</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `SH-t-3` (`decompositions/MDPF_SECHIST_DECOMP_R2.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none | **event:** the first `run_class: scheduled` manifest carrying the round-1 code (earliest
the 2026-10-09 07:00 ET pull, as-of 2026-10-08) and the Positioning publish after it

---

## WORKER FACE

### THE CELL

`SH-t-3`. FWD-1: the morning after an Opal ETF first buys a security, an analyst opens it on the Positioning page and reads its class,
sector, clean name and every return window a year of history supports. Read only.

**The read.** Run the invocation after the scheduled pull's manifest has landed and the Positioning publish that follows it (about
13:01Z). It finds the newest `s3://opal-data-etfs/bbg/<date>/run_manifest.json`, refuses an `adhoc` run (QA only, ruling cb6fb2a52c), takes
each security that pull backfilled with rows, and reads it on `s3://opal-data-portal-v2/platinum/etfs/positioning_data.json`.

### ACCEPTANCE

<criterion id="SH2-t3-AC1" cell_refs="SH-t-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R2_CHECKS/sh_fwd1_acceptance.py</invocation><expect>FWD1-ACCEPT-OK</expect></criterion>
`SH2-t3-AC1` -- on a scheduled pull, at least one newly backfilled security reads class, sector, a name with no `/<state>` suffix and 8 of 8 windows.

<expected_criteria>SH2-t3-AC1</expected_criteria>

It FAILS at the base (2026-10-08): `FWD1-ACCEPT-BAD newest-manifest-not-scheduled as_of=2026-10-07 run_class=adhoc`. A
`no-new-security` result means that pull bought nothing new; the read moves to the next scheduled pull. A name failure is
MDPF_SECCLASS's round-13 cell (CTO analysis 2.2) and fails FWD-1 that morning.

## BOUNDS

- Read only: no write to S3, no run of the pull or the publisher. Writes: the proof instance only. The issuer spawns this worker after the event above.

<paths>
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~4/MDPF_SECHIST.TO-SH-t3.fwd1-acceptance-read.proof_of_spec.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R2.md</decomp_doc> (round 2), cell `SH-t-3`.
<owned_cells>SH-t-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH2-t3-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~4/MDPF_SECHIST.TO-SH-t3.fwd1-acceptance-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SH2-t3-AC1` BEFORE the flip.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE reads the existing site Z daily task's output.
comp-iam: DECLARED-NOT-APPLICABLE dell1 read grants used in round 1 (opal-data-etfs, opal-data-portal-v2).
comp-adversary: DECLARED-NOT-APPLICABLE a read; the check refuses an adhoc manifest and a served object older than the manifest.
risk: SERVED -- graded on the served Positioning data.
direct_act: true -- the real run of FWD-1, read only; the worker is spawned after the event.
</preflight>

Source: CTO round-1 analysis @0141533760 section 3 item 1; ruling cb6fb2a52c; PRD v0.2 FWD-1.

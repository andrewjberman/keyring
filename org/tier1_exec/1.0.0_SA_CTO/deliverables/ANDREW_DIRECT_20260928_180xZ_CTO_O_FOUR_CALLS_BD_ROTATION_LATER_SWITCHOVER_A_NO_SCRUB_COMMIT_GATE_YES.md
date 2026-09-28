# Andrew-direct 2026-09-28 ~18:0xZ at the 1.0.0_SA_CTO~O terminal -- four /open-calls answered

**Recorded by:** `1.0.0_SA_CTO~O`, the same turn. **Cards:** the /open-calls frame of ~17:5xZ (4 calls, printed
in-session).

## Verbatim

> 1.) We will do this later. 2.) A is fine. 3.) A is fine, git is only me. 4.) Yes this is a good idea, i approve it.

## The calls answered

**Call 1: "Rotate the live Black Diamond password (and the SmartX one): yes, and when?"**
REC: yes, now, before the reboot session resumes.
**ANSWERED: LATER.**
- The rotation is his act, deferred. It stays as a CARRIED card at Andrew, no longer blocking.
- Its absence blocks nothing in the canonical flow. The redaction of the 7 files under `infra/aws/ec2/bd-exporter/`
  (row Z-S31) is a separate lane act; see the routing below.

**Call 2: "Do the ~20-minute switchover sitting: (a) first thing after the reboot, or (b) later?"**
**ANSWERED: (a).**
- The first session after the site Z reboot schedules the sitting with him, from
  `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/1.0.0_SA_CTO~O/ANDREW_SWITCHOVER_RUNBOOK.md` Parts A-D.
- Before he sits down, `2.0.0_SA_COO~O` re-confirms the four preconditions, because the site Z state moved with the
  S19 rewrite.
- It unblocks NFRA_OPALAI OA-t-1/t-3 (the two HOLD drain branches), Analyst FWD-1 and NFRA_MCPORTAL MP-a-1.

**Call 3: "Scrub the BD/SmartX literals from git history: (a) no rewrite, rely on the rotation, or (b) a second
laptop rewrite?"**
**ANSWERED: (a), "git is only me".**
- There is no history rewrite for the BD or SmartX literals. The repository is not visible outside Opal.
- The standing rule stays: no history rewrite without his word.

**Call 4: "Make secret_literal_census.py a commit gate: yes or no?"**
REC: a limb of `.tools/commit-gate.sh` that grades ADDED lines only, with an audited override; WARN for one week,
then enforce.
**ANSWERED: YES, APPROVED ("this is a good idea, i approve it").**
- This is the explicit word that CLAUDE.md section 2 (a) requires for a new gate.
- `.tools/commit-gate.sh` is owned through project ADHC_COMMITGATE (the AE CloudOps lanes, last touched by
  `0.7.0_AE_CloudOps~K` @9ed3bbfef8).
- The build is routed to `0.0.0_AB_MSTR~Z` to seat after Andrew's S19 drain hold lifts.
- The census script itself is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~I/secret_literal_census.py`.

## Routing, the same turn

- `0.0.0_AB_MSTR~Z`: Call 4 (seat the ADHC_COMMITGATE limb after the drain hold) and Call 3 (no BD history rewrite).
- `2.0.0_SA_COO~O`: Call 2 (re-confirm the preconditions for the post-reboot sitting) and Call 1 (the Z-S31
  redaction goes to the CloudOps lane in round 2; the rotation stays at Andrew).
- `3.0.0_SA_CVO~O`: informed through this record; there is no act for it.

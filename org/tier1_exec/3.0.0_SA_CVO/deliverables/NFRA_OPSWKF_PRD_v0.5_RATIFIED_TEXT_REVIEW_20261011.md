# NFRA_OPSWKF PRD v0.5 -- ratified-text review (ENDPOINT: FWD-8's DONE WHEN gains the negative arm)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D9/NFRA/NFRA_OPSWKF/prd/NFRA_OPSWKF_PRD.md` @b7dfe287f1.
**Asked by:** `1.0.0_SA_CTO~DELL2` (the v0.5 review delivery and its repair message). **Prior review:** v0.4 @5c31605357 (REFUSED).
**Verdict: SIGNED.**

The one point of the v0.4 review is repaired in the ENDPOINT's own DONE WHEN, read as a diff (`git show b7dfe287f1`): after the
release, on the deployed service, both arms: one of the eight routes read by a verified caller whose tier is not internal,
refused; one read as an internal session, served; and the deployed bytes diffed against the build input member by member.

The addendum adds two things this seat did not ask for, and both are right:

- **The same negative arm is run once BEFORE the release.** Served before and refused after is the proof. It is also the first
  live read of the defect, which today rests on a code read and a bytes read; refused before stops the release.
- **The non-internal caller is a synthetic identity** minted for the read under the release's pair, bounded as TCKT_VNEXT's runs
  were, with no client's or partner's sign-in and no existing service token used.

Nothing else of the section moved: one clause of FWD-8 changed and the header's version.

## What this seat read

The diff of the PRD at b7dfe287f1 (one clause of FWD-8 in the ENDPOINT section, and the addendum).

# CTO ROUND-177 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- answering the round-176 L10 slug (2026-10-13 ~07:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `surprise-channel/remediations/REMEDIATION_v53.md` @c5de16f70d (3.0.0_SA_CVO msg 6862): 2 rows OPEN
and ARMED. **No PRD addendum.**

## 1. Rulings

- **D2-W361-S1** (a re-cut from HEAD's closure would add `opal_strategy_matcher.py`, an import the live packages lack): fenced as ruled
  (RE 6858): the pair is one minimal package per firm, live bytes plus only the two changes. Stays ARMED as the reminder for any future
  re-cut.
- **D2-W361-S3** (4 live members -- 49financial 2, inflection 1, cottonwood 1 -- equal NO historical blob; 22 differing rows have no commit
  since the upload): **(a) the pair carries the 4 unchanged and names each by path and sha256; it does not block on them.** (b) **One
  read-only provenance read**, not blocking the pair: for each of the three package objects, the S3 object's metadata and the CloudTrail
  `PutObject` event at its `last_modified` (the principal and the session, no payload); for each of the 4 members, a line diff against
  its nearest historical blob (which commit, how many lines, what kind of change; code only, no client data). (c) **The 4 live members'
  bytes are archived as evidence** under the project's deliverables with their sha256 and source package, so the live package can be
  rebuilt (and rolled back to) from the repository from now on. Whether any of the 4 is then committed as source is ruled on that read.
- **D2-W345-S3** disarms with the pair's apply at the host's next scheduled Online; **D2-W348-S2** stands as ruled at round 172.

## 2. ENRICHMENT LIST for round 177 (~P, ONE issuance)

1. The host-bundle pair: one minimal package per firm (the 4 named), applied at the host's next scheduled Online.
2. The provenance read and the evidence archive of the 4 members (W361-S3 (b), (c)).

-- 1.0.0_SA_CTO~DELL2

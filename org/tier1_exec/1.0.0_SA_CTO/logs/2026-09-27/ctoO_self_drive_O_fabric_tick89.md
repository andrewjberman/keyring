# /self-drive ~O fabric -- ticks 88-89 (1.0.0_SA_CTO~O, 2026-09-27 22:48Z-23:45Z)

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d.

- **E10 drafted** (@8ba2eee06f): retire the legacy /login GUI consent, starting with a census, on row Z-S7. It sits
  in the NFRA_OPALAI round-2 enrichment draft.
- **Row NFRA_MCPINDEX-Z-S31** (0.7.0_AE_CloudOps~I; this seat is the disarm_owner):
  - Z-S29 redacted a SUPERSEDED password.
  - The CURRENT live BD password, whose hash matches Secrets Manager `opal/bd/credentials`, sat in 18 places across 16
    tracked files. This seat's single-literal census could not see it; AE~I's generic assignment census did.
  - This seat named AE~I the redaction owner (file 20260927T230222Z).
  - AE~I landed it @ce0782aaf3: 18 of 18 removed, and the generic re-scan reads 0.
    - Docs carry a placeholder.
    - The shell script is `${BD_PASSWORD:?}`.
    - The 12 .ts files fail closed with a throw at the top.
  - AE~I asked for a push before 02:45Z. Answered: per MSTR~Z 213908Z a commit is enough (site Z rewrites this clone
    with --preserve-commit-hashes).
- **AE~I committed `secret_literal_census.py`** (@03086508a9) as an adoptable instrument. Making it a gate needs
  Andrew's word (CLAUDE.md section 2), so it is carded as CARRIED.
- **CVO~O's post-act read on OG-s-1** is inside the radius (@cae3f2897e).
- Andrew was pushed at 23:0xZ on the urgent cards.

**Cards at Andrew:**
- (1) URGENT: rotate the live BD password.
- (2) Before about 02:30Z: add both BD literals to tonight's filter-repo purge scope.
- (3) CARRIED: make secret_literal_census a commit gate.
- (4) The switchover sitting.

**Completion test:** NOT DONE. 0 of 4 projects are complete. **Freeze:** 03:00Z.

state: ARMED

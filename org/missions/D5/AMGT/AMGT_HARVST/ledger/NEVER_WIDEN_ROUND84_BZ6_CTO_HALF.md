# NEVER-WIDEN co-sign -- CTO half: AMGT_HARVST round 84, `HVST-bz-6` (WSJ and Barron's sessions from the EXISTING credential) (`1.0.0_SA_CTO~DELL1`, 2026-10-13 ~12:3xZ)

Asked by `2.0.0_SA_COO~W1` msg 4799. COO half: `deliverables/2.0.0_SA_COO_W1/round84/NEVER_WIDEN_HALF_COO_BZ6_DOWJONES_SESSIONS.md`.

**Basis:** Andrew-direct 2026-10-13 ~12:2xZ, "Regarding WSJ/Barron's, we have credentials and HARVEST scripts that do this"
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_122xZ_CAPPED_LOTS_UNVERIFIED_SHARE_COUNT_SOURCES_PORTAL_SMOKE_WSJ_CREDS.md` item 4). Dow Jones is not
Bloomberg, so no per-use word is needed.

**Read and accepted:**
- **The credential:** Secrets Manager `dowjones/credentials` (us-east-1). One secret serves both publishers (1 version, changed 2026-09-14). It was found by NAME and METADATA only;
  its value is never printed, logged or committed.
- **The script:** the existing `org/tier1_exec/4.0.0_SA_CRO/scripts/dowjones_harvest_session.py`, through `lib/opal_data_harvest/auth.py` `SessionManager.refresh`. It saves to the
  box's DPAPI vault. No new code and no new vendor scope.
- **The act (`~ZW`, site Z):**
  - read the session state FIRST;
  - ONE mint per publisher, ONLY where it reads `VALID=False`;
  - **the first refusal stops BOTH** (a shared account, so a lockout or challenge must not be provoked twice);
  - no `--park`;
  - no secret printed.
- **Both branches:**
  - a session minted and valid: the runner's next cycle signs in, and bz-7 reads bx-4's acceptance;
  - refused (a challenge, a lockout, or a changed password): STOP, record the refusal class only, no retry. It comes back to this seat, and that is the point where Andrew may be
    needed.
- **Blast radius:** two vendor sessions in one box's vault. Nothing served moves. **Rollback:** delete the vault entries (local, not S3).

**SIGNED.**

-- 1.0.0_SA_CTO~DELL1

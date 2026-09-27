# Governance verdict: `# pipeline-override:` does NOT bypass LIMB 6 (the L4-R sign-off limb)

Adjudicator: `3.0.0_SA_CVO~O` (governance fork -> CVO, Andrew's self-drive arming term). Recorded 2026-09-27, clock read
before writing: ~15:0xZ.
Fork: `1.0.0_SA_CTO~O` file `20260927T145639Z_1.0.0_SA_CTO_O_GOVERNANCE_FORK_override_bypasses_LIMB6.md`, on row
`NFRA_OPLGTW-Z-S1` (ARMED, disarm_owner 1.0.0_SA_CTO~O). This seat's tick-59 log called it "S63"; the channel id is
Z-S1.

**Question:** should an order carrying `# pipeline-override:` also pass a newly-added order against a PRD whose L4-R
half is REFUSED or unsigned?

## Verdict: NO

The override keeps every other effect it has today. The sign-off limb runs regardless of it.

## Read, not taken from the fork

- **The mechanism:** `.tools/to-pipeline-gate.py:2690-2711`. `check_file` audits the override line, then
  `return ([], notes)` for the whole file, before any per-order limb runs. `NFRA_OPLGTW.TO-OG-e-1`'s record face carries
  the line (`:103`). So the limb never ran on OG-e-1.
- **The law:** CLAUDE.md 27 L4-R (`:44`): "`.tools/to-pipeline-gate.py` LIMB 6 refuses a NEWLY-ADDED task order against
  a PRD with an unsigned half". It names no override.
- **The spine:** `CANONICAL_FABRIC_WORKFLOW_20260901.md:283-290` lists the gate's refusals and says only "an override is
  written to `org/to-pipeline-override-audit.log`". It does not say which refusals an override lifts.
- **The override's documented purpose, in the gate's own texts:** `:511` covers the one-issuance coverage refusal ("take
  the audited '# pipeline-override:' on one order with the reason"), and `:1994` covers a genuinely additional order
  into an open round. Both are pipeline-SHAPE escapes, owned by the issuer.

## Why

1. **Verbatim scope.** The only written scope of the override is pipeline shape, and the only written rule for LIMB 6
   has no exception. Letting the override lift LIMB 6 would read a wider authority into a line than any text gives it.
2. **Whose refusal it is.** An L4-R half is another seat's verdict (the CVO's ratified-text half, the CRO's brief half).
   The override is self-authored by the issuer. If it lifted LIMB 6, one seat could void another seat's recorded
   refusal by writing a comment. The two-half design exists to prevent exactly that.
3. **No new friction.** This adds no gate. LIMB 6 already exists in law; the fix makes the mechanism do what the law
   says it does. Cost: about 4 lines plus a self-test arm (the CTO's estimate).

## What this verdict does NOT do

- It does not re-open OG-e-1. The ratified-text half has since been SIGNED at the amended bytes (@2e371ea304, PRD
  ADMITTED), and OG-e-1's face carries the corrected key function (`:32`). The order stands as issued.
- It does not change the override for any other limb, or for the coverage limb (`_coverage_scan`).
- It names no implementer beyond the row's disarm_owner, `1.0.0_SA_CTO~O`, who owns `to-pipeline-gate.py`.

## Disarm criterion for Z-S1 (for its owner)

In a self-test, a newly-added order carrying `# pipeline-override:` against a fixture PRD whose ratified-text half is
REFUSED is refused by LIMB 6. The same order against a SIGNED fixture passes, with the override audited as today.

-- 3.0.0_SA_CVO~O

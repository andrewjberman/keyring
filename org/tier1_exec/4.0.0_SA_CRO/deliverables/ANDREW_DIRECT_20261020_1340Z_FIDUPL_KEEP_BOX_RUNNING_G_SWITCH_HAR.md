# ANDREW_DIRECT 2026-10-20 ~13:40Z -- NFRA_FIDUPL: keep the box running, drop the stop after each run; a G-switch HAR is coming

- **Channel:** in-session, Claude Code terminal, dell1, to `4.0.0_SA_CRO~FIDELITY`
- **Time:** 2026-10-20 ~13:40Z (9:40 AM ET)
- **Context:** this follows his ~12:50Z word "turn off autoshutdown for this box" (the MSTR record
  `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261020_125xZ_FIDELITY_SECRET_SET_AND_AUTOSHUTDOWN_OFF.md`).
  It also answers the open point the CRO raised to the CTO in msg 8618: `automation.tf:133` stops the box after each run.

## Verbatim

> keep the box running, drop the stop after each run, we need to run this until we get a lock and we need to be able to manage the
> g number switch, i will record a HAR that shows off the g number switching to make that clear

## Scope as given (surfaced, not adjudicated)

1. **Box:** Fidelity box `i-028e830f7226cc685` stays running:
   - the stop leg after each run is removed (`infra/aws/terraform/canonical-fidelity-ec2/automation.tf`, DesiredState stopped);
   - the overnight enforcer is opted out (the tag `AutoShutdown=disabled`, per the 12:50Z word).
2. **Purpose:** to run repeatedly "until we get a lock", meaning until the sign-in and pull are reliable.
3. **G-number switching** must be manageable by the uploader.
4. **Andrew will record a HAR** of the G-number switch. The CRO maps its endpoint and parameters into
   `RESEARCH_20261019_NFRA_FIDUPL_ACCOUNT_TXT_AND_FIRM_SPLIT.md` section 2a when it arrives.

# Andrew-direct rulings, 2026-08-06 ~1400-1445Z, CRO terminal

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Channel:** interactive, this terminal, in response to /open-calls. Recorded VERBATIM per org/XXX.md
(record + broadcast same turn). Broadcast: MSTR + CTO + COO.

## Ruling 1 — RCG sitting: GO

> **"Go on the next RCG sitting."**

Executes: the sitting packet (v6 band-172 adjudications + seeking-alpha trio + E-0005 readout)
assembles now at this desk. The "post comp-heat/cochange registration" pacing note is DISCHARGED by
this GO — his word supersedes his earlier pacing.

## Ruling 2 — RCN-0005 is RATIFIED

> **"Regarding RCN-0005, it is already ratified i worked on that."**

Executes: RECON_REGISTER.md row updated STAGED-FOR-ANDREW-REVIEW -> RATIFIED (same commit as this
record). My open-calls listing of RCN-0005 as awaiting review was STALE AT SOURCE — he had already
worked it; the register row was my record lagging his action, the exact class today's staleness
census measures. Corrected on his word.

## Ruling 3 — the portal test credential: NOT a secret; structure it as an env

First (in response to the census flag): *"yes scrub the embedded credential, also tell me what
credential that is."* Then, told it is the michael@opalinvest.com portal test login, SUPERSEDING:

> **"that is not a real login, that is fine we can use that"**
> **"dont mind that, i need agents who are doing frontend able to use that, maybe it can be better
> structured in an env and that env is inside any /frontend-dev /playwright style work"**

Executes:
- `.claude/skills/frontend-dev/portal-test-login.env` created (workspace repo) — the ONE structured
  home: PORTAL_TEST_EMAIL / PORTAL_TEST_PASSWORD / PORTAL_TEST_USER_DB / PORTAL_TEST_USER_KEY, with
  his sanction verbatim in the header.
- The 3 memory files that carried the password inline (`feedback_option_c_auth_supersedes_devbypass`,
  `project_inflec_frontend_dev_auth_path`, `reference_agent_fe_visual_smoke_real_jwt_login_path`)
  re-pointed at the env (memory repo, 2 commits: scrub then restructure).
- Standing form going forward: frontend/playwright work reads the env; the password does not return
  to prose docs or memories. This is a STRUCTURE ruling, not a secrecy ruling — the login is
  sanctioned for any agent doing frontend verification.

## Same-window context ruling (MSTR terminal, relayed 1439Z, recorded here for adjacency)

MSTR broadcast Andrew-direct ~1435Z: *"no gates are implemented on any type of work unless i
explicitly ask for them. i did not know about this coo gate and that type of error has held up
deployments unknowingly before."* — CTO landing the law edit at CLAUDE.md:14. This desk's doctrine
surfaces reflect it on next touch; today's deliverables already comply (gate candidates PROPOSED to
owners, none implemented).

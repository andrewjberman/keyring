# ANDREW-DIRECT 2026-09-02 -- "all recs approved" on the /open-calls cards at 1.0.0_SA_CTO~Z

**Channel:** the 1.0.0_SA_CTO~Z terminal, 2026-09-02 ~14:4xZ.
**Recorded by:** 1.0.0_SA_CTO~Z. **Broadcast:** msg 19337-19341 (MSTR~Z delivered; COO~Z, CVO~Z, AE~Z, DE~Z queued).

## His words, VERBATIM AND ENTIRE

> all recs approved

In answer to `/open-calls` run at this seat, four cards. THE PHRASING IS THE RULING; the recs he
approved are reproduced below exactly as they were put to him, because "approved" binds to that text.

## The four recs as approved

**CALL 1 -- the 8 MFA accounts.** REC (a): flip all 8 -- alex.bright, alex.coggins, chase.bertrand,
greg.rosner, hunter.lloyd, luke.winskowski, travis.penfield @49financial.com, and
patricia@thewhitelabelcreative.com. Email channel, same conditional update-item as the 9 and the 13.
*Descends from:* "flip the switches so that MFA is required for all users" (2026-09-02) and the 09-01
"exclude on call 2" ruling, which still excludes the 13 test/demo/fixture, 2 service, 1 disabled.
**EXECUTED 14:4xZ:** APPLIED 8 / SKIP 0 / ERR 0; fresh full scan 48 PROFILE rows, **32 mfaEnabled, all
email**, 8/8 targets ON; the 16 still OFF are exactly the excluded set.

**CALL 2 -- SITEZ into SHARED_BRANCHES.** REC: yes, with a proven-red arm. *Consequence:* GATE 1
(NEVER#7 rebase) and GATE 5 (LD-0367 integrator-only push/pull) now FIRE on the site-Z working
branch. A non-integrator `git push origin SITEZ` is DENIED -- the mechanism now matches the law.
**EXECUTED:** never-rules-gate.sh SHARED_BRANCHES += SITEZ; 4 suite arms; 13 of the 15 previously-dead
rebase arms went green on this device.

**CALL 3 -- DT may push portal DEV.** REC: yes, same four conjuncts with DEV added (DT serial, portal
origin remote, verb push), AND a "verify the payload is only your own commits" check written into
/prod-deploy Step 1a. *Descends from:* "portal prod-deploy is always allowed by DT, its part of the
prod-deploy skill" (2026-09-01). **EXECUTED:** carve-out reads PROD|DEV; deny text updated; SKILL.md
Step 1a carries the author check and names GATE 5 for the first time.

**CALL 4 -- Andrew-directed non-DT on PROD.** REC (b): no code change; use the audited
`# never-override: <reason>` citing his word. **EXECUTED:** recorded into /prod-deploy Step 0 and the
gate's deny text. No caller widening.

## Scope, stated so it is not read wider

This ruling approves FOUR SPECIFIC RECS. It does not: widen the DT carve-out beyond the portal repo;
admit CTO serials to any push gate; lift the 09-01 test/service exclusion; or touch SMS (still G-7,
SP-1 gated).

## Finding surfaced under this work, NOT ruled on

With SITEZ shared, 2 rebase arms still fail on every device: `git -c pull.rebase=true pull origin
CLOUD` and `git --no-pager -c pull.rebase=true pull origin CLOUD` render PASS (want DENY). GATE 1's
`-c pull.rebase` one-shot matcher does not fire -- the F-XXX option-consumer class the suite already
documents. Pre-existing, unrelated to this edit, a real NEVER#7 evasion. At 3.0.0_SA_CVO's channel.

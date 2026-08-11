# DEPLOY-COMPLETION LEDGER — cot CPR-2/C-3 + CPR-5 bd carry

**Opened:** 2026-08-11T15:04Z by 0.4.0_DS_ClientPlatform (executor, Rule-13 lane) — AT DEPLOY-START
**Status:** OPEN — closes when both legs land ETag-verified, or on rollback
**Authority:** COO dispatch 062937Z ("15:06Z DEPLOY: FIRE IT AS PLANNED") + COO 142859Z
re-confirmation ("FIRE AS PLANNED... your precondition is DISCHARGED, not bypassed") +
CPR-5 act (COO 063335Z, CTO-ruled remedy).
**Precondition state:** THE 13:30Z BAR RAN AND WAS ADJUDICATED (@9c138edb37) — an AWS-side
scheduled Lambda; the local box sleep (11:12-14:24Z) did not and could not stop it. Verdict:
GUARDS WORKING, NOT AN OUTAGE (branch (iii) held; A7 partners=2, reconciliation PASS on
$1,786,341,788.10; cycle-level 6/12 divergence = inflection's coherence gate refusing on 2
named custody gaps + global fold skipping rather than fabricating). Andrew rulings
@162965ed1c noted (absence=serve-law; $122.5M interim-excluded) — neither touches this act.

## THE ACT
Deploy @ea2400401a (cot_bronze_ingest.py: C-2 double-lag window fix + C-3 probe-universe
anchor, 81-test suite + mutants) via the sanctioned path:
  python .tools/safe_deploy_core.py data/cot/scripts/bronze/cot_bronze_ingest.py --author 0.4.0_DS_ClientPlatform
LEG A (today): the object lands at s3://opal-data-cot/code/bronze/ (primary) AND
s3://opal-data-bd/code/bronze/ (the CPR-5 second target, declared in safe_deploy_core's
cot-tree second_targets @4100c90f47) — both ETag-verified against the fixed cot bytes.
LEG B (overnight, AE's verify): the 49F runner's next scheduled invocation (~00:11Z)
downloads and EXECUTES the fixed bytes — the object landing is NOT the fix taking effect.
THE 49F GAP STATEMENT (verbatim carry per COO 063728Z): the bd runner never invokes the
retry-net sweep, so C-3 is INERT on the bd path; the live carry to 49F is C-2's
_window_for change (used by every pull). The fix value bd-side is drift-closure.
Timing: fires 15:06Z (post the 13:02-15:05Z MDPF cadence; COO's 15:00-15:15Z cot-tree
exclusion flagged to CTO covers this act).

## PRE-REGISTERED READINGS
- Either leg fails ETag-verify -> rollback the landed leg from the prior S3 version,
  close ROLLBACK, escalate COO+CTO loud. No stranded leg past session end (NEVER#6).
- Success closes THIS ledger on leg A only; leg B is AE's verification with its own
  record (a deploy ledger closes on the deploy; execution-in-effect is the runner's next
  fire, owned by AE, never silently folded into this close).

## CLOSURE
(pending)

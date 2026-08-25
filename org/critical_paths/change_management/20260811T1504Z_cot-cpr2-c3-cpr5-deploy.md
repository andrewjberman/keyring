# DEPLOY-COMPLETION LEDGER — cot CPR-2/C-3 + CPR-5 bd carry

**Opened:** 2026-08-11T15:04Z by 0.4.0_DS_ClientPlatform (executor, Rule-13 lane) — AT DEPLOY-START
**Status:** CLOSED 2026-08-25 -- leg A PROVEN-FROM-ARTIFACTS on BOTH homes against LIVE state (ETag fb5e6bad present at 15:06:06Z cot / 15:06:12Z bd via list-object-versions). LEG B remains AE's with its own record, per this entry's own pre-registered reading, and is NOT folded into this close. MEASURING SEAT: 0.4.0_DS_ClientPlatform~F under NEVER6_LEDGER.TO-R1-DS, 2026-08-25. NO SENTINEL EVER EXISTED for this entry, so deploy_ledger.py could not close it without overwriting this record; closed by TARGETED Status-line edit on COO ruling 70183 (d), body preserved byte-for-byte.
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

## CLOSURE — 15:07Z, BOTH LEGS LANDED + ETAG-VERIFIED, CLEAN

Fired 15:06Z via safe_deploy_core (sanctioned path). local md5
fb5e6bad56e7ba2da3d60f6e43623cd7 == cot ETag (15:06:06Z) == bd second-target ETag
(15:06:12Z) — byte-identical both homes, comp-pipescript VERIFY OK. Leg A CLOSED.
Leg B (fix-in-effect on the 49F runner's ~00:11Z fire) = AE's verification, own record;
AE notified 15:0xZ with both ETags. cot-side: the 22:30Z cot ingest executes the fixed
bytes tonight. Nothing half-landed; no rollback taken.

## AMENDMENT 1 (2026-08-12 ~13:34Z) -- PRIMACY CLAIM CORRECTED (AE 132516Z flag, measured at source)
The leg-A record above says the 15:06Z land was "the first act of the fan-out row." IT WAS THE
SECOND. Version history, both homes, identical ETag fb5e6bad / 80,121 bytes throughout:
  cot PRIMARY : 06:21:35Z  08:41:40Z  15:06:06Z
  bd  SECOND  :            08:41:42Z  15:06:12Z
The 06:21Z primary land has NO bd counterpart because the second_targets fan-out row did not yet
exist (committed 06:26:57Z @7ce609e560, 06:36:40Z @4100c90f47; the fix itself 06:06:53Z
@ea2400401a). From 08:41 on, both homes land ~2s apart -- the sanctioned fan-out running on my own
commits via the pre-push deploy hook. NOT an unattributed third party.
WHAT STANDS: leg-A's byte-identity proof (both homes == local md5) and AE's leg-B execution proof
(version-immutability: no later version + download-at-invocation) are unchanged. WHAT WAS WRONG:
the claim of PRIMACY only.
CLASS (the INVERSE of "an atomic commit is not an atomic deploy"): the pre-push hook DOES deploy,
so a later scheduled deploy window may be RE-deploying already-live bytes. A "this act put it
there" claim requires list-object-versions, never the operator's own clock.

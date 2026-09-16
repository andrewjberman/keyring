# Barron's captcha: human-assisted result, independent test deferred

Author: 4.0.0_SA_CRO~W
Date: 2026-09-15
Scope: AMGT_RESAPP / D5 harvest; no POSN_ASTTAX work.

## Andrew's instruction, verbatim

> Keep in Mind that the Barron's captcha is a click and drag variant that we have not seen befor and you have never passed it successfully, I merely just pulled it across when I saw you testing it because I didnt feel like wasting time on it, but once everything is compeltely done and youve figured out the system for the rest, it is worth returning to Barron's and makin sure the Barron's script can handle it.

## Correction and execution order

The apparent successful Barron's verification around 03:52Z was human-assisted.
The operator dragged the slider. The automated handler has no independent pass.
The prior diagnostic label `SAVED_VERIFICATION_REPAIR_NO_LOGIN` establishes that
the existing login survived, but does not establish who completed verification.
This correction supersedes any attribution of that pass to the script.

The local event ledger and encrypted session provenance carry the correction.
Automatic Barron's verification is held pending its independent test. Finish
the shared local worker, scheduler and other publishers first; then test the
Barron's click-and-drag handler. Existing paid-session HTTP article results are
valid collection evidence, not evidence of autonomous captcha recovery.

The five-publication system is not yet declared complete or unattended-ready.

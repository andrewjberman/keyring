# 1.0.0_SA_CTO -- 2026-09-03 07:00-07:40Z -- gate hygiene on three surfaced findings

Inputs (READ-acked): 0.0.0_AB_MSTR 93288 (never-rules suite 92/4 on this device; 06_current_state STALE per CVO~Z;
rulebank-version instrument undispositioned); MSTR~Z relay 93296 (surprise-row-gate cp1252 decode; PRD notifier to the
base COO on site Z); 93289 LD-0527 /govern armed (rotation on finish; ~Y untouched); 93300/93302 the 49F chain
NEVER-2 (COO + MSTR, informational here).

## Acts
1. 06_current_state regenerated (comp-system, grounded at HEAD 7f4cbd3dc8) and committed @c08c1bbe99 -- only the two
   generated files; three sibling files carried another seat's pre-existing edits and were left alone.
   ont-rulebank-version-current still FAILS by design (marker absent from the four required files: a design call
   with its own owner, not relaxed).
2. never-rules-gate GATE 1: measured MSTR's four -- TWO real (the inline `-c pull.rebase=true pull` one-shot had no
   regex; the config-keyed limb only fired when pull.rebase already read true; both repos read false), TWO harness
   (portal detached at a pointer after the SITEZ merge; the gate judges -C portal against portal's branch and is
   right). New limb for the one-shot; harness derives the portal expectation from portal's branch and prints it.
   Suite 96 PASS / 0 FAIL.
3. cp1252: 20 subprocess text reads across six gates now decode UTF-8 explicitly (errors=replace). Batteries green;
   discriminator: a blob with em-dashes read back with 0 replacement chars.
4. prd-header-notify: recipient and route owners re-homed onto the committer's lane (OPAL_AGENT_SERIAL ~suffix);
   PRD_NOTIFY_TO still wins. Exercised base / ~Z / ~A / override.

## Instruments
test_never_rules_gate.sh (x2, ~10 min each), the gate's own batteries (surprise-row-gate 6, proof-of-spec 6, corpus
pass), commit-gate x8, importlib exercise of the notifier under three identities, system_parity.py, git ls-remote.

## Open, with owner
- rulebank-version marker on the four core docs: a design call, owner the ontology/rule-bank steward, not CTO.
- 0.7.0_AE_CloudOps~R + 2.0.0_SA_COO: the 49F chain rollback before the ~09:46Z fire (NEVER-2, MSTR ruled proceed).

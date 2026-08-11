# ANDREW-DIRECT -- proof-of-spec CANONIZED into the TO/PRD delivery process

**Channel:** Andrew-direct at the `3.0.0_SA_CVO` terminal, 2026-08-11 ~0821Z.
**Recorded by:** `3.0.0_SA_CVO`, same turn, per the RECORD+BROADCAST law (org/XXX.md).
**Broadcast:** MCP to `1.0.0_SA_CTO` + `2.0.0_SA_COO` + `0.0.0_AB_MSTR`, same turn.

## Verbatim

> "Yes I also want you to write something into our process, whatever governs PRD / TO delivery,
> to canonize proof of spec. I do not want TOs being issued that do not have machine-readable
> data contracts, where the agent responsible must fill out the contract based on their efforts."

## Scope as bound (his words, no widening)

- **CANONIZE proof-of-spec in the process governing PRD/TO delivery** -- the standing law, not a
  per-program convention. Primary home: `org/ref/TASK_ORDER_PROTOCOL.md` (the TO template +
  completion protocol); the one-line requirement mirrors into `org/XXX.md`'s "Every TO must
  include" list (the surface every agent reads).
- **ISSUANCE HALF:** a TO without a machine-readable data contract is NOT ISSUED -- the contract
  (the expected acceptance-criterion id set, machine-readable) is minted at PRD decomposition by
  the issuer (COO/CTO), embedded in the TO.
- **COMPLETION HALF:** the RESPONSIBLE AGENT fills out the contract based on THEIR efforts -- a
  `PROOF_OF_SPEC.schema.json` instance (org/standards/), validated by
  `.tools/proof-of-spec-check.py` against the TO's expected set, as the completion artifact.
- Mechanism already live this session: schema + validator @76ee261895; coverage-first layer
  @d9a9ce7b80; the two-layer division (validator = assignee-vs-TO; CVO step-zero = TO-vs-spec)
  on the record 082045Z.

## Executed same turn

`org/ref/TASK_ORDER_PROTOCOL.md`: `<proof_of_spec>` element added to the template (issuance-half
ids + completion-half instance contract) + the completion-protocol gate line. `org/XXX.md`: one
bullet added to the "Every TO must include" list. Committed under this record's law line.

-- 3.0.0_SA_CVO

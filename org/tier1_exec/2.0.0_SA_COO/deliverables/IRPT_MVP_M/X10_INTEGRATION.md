# Bounded X10 integration candidate

Authority: CTO IRPT-X10-INTEGRATION-01 `f6a8721a59`; G owner review `136624e660`,
CRO `4d6a4338ae`/`983550adde`, CVO `eb00a0c6b2` remain separately attributed.

The isolated candidate starts at actual CLOUD commit
`3978b247b4ca5d114fb2f0981ab546d28d3def29`. It applies exactly the reviewed X10
builder, test and two registry files from `587e782bc6`. All four match the reviewed
bytes after line-ending normalization. No M feature branch merge is included.
The current CTO RULINGS.md is unchanged; no governance text was replaced.

Two separately authorized generated stamp repairs were produced by the canonical
generator against this exact reconciled registry: holdings_snapshot.py and
_authz/loaders.py. Each changes one generated comment line (one removal and one
addition), with every other normalized source byte unchanged. The evidence records
before/after hashes and complete diffs. No ten-carrier inventory, Terraform carrier,
harvest/fmt change or CLOUD_OPS_OR_ETL path is included.

Validation: registry has zero refusals and 33 existing warnings. Full relevant
candidate tests: 148 PASS, five FAIL. A fresh baseline run has 88 PASS and the same
five failing test IDs; the X10 candidate adds 60 passing tests. The five are worked
case expectations for inf-silver-chain, portal-data-proxy API, Inflection dimension
alarm, wsb-model-aua schedule and otp-relay secret. This is not a clean broad suite.
Non-IRPT scope semantics and five other registry files are unchanged. All 116
unmodified existing builder functions are AST-identical; the only changed existing
functions, load_registry and validate, match the reviewed candidate. Five new
reporting policy/destination functions are the reviewed additions.

PENDING_ENFORCEMENT, null enforcement_ref, unprovisioned product status and writer
refusal are retained. This source candidate does not activate policy, provision
storage, drain unreviewed feature work, deploy or establish full S7 acceptance.
Independent verification and ordinary integration remain required. Push state LOCAL;
M does not push shared branches. The legacy-read source-cutoff patch remains separate.

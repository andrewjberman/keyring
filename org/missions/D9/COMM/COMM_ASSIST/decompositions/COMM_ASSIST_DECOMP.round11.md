# COMM_ASSIST decomposition -- round 11: the mail key's wiring, built ahead of site Z's release (issuer 2.0.0_SA_COO~R; cut 2026-10-09 ~02:1xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** Andrew's "go" at the `2.0.0_SA_COO~R` terminal ~02:0xZ to `/next-calls` OPTION 1 ("mail-key wiring, built ahead"),
and `1.0.0_SA_CTO` msg 107513. PRD v0.2 ADMITTED (`805fec22c5`). FWD-4; C-MAIL; C-PACKAGE.

**Measured at the base (`box/laptop` bdc7f6e9b7):**

- Site Z's gateway release r29 (`dbc700a9c8`, carries OG-md-1's domain mail route AND round 6's channel routes, read by the
  issuer: `b3afc00597` is its ancestor) applies NO EARLIER than 2026-10-09 11:00Z and hands COMM "one MAIL_BEARER value for your
  Teams agent ... by secret reference only" (site Z `2.0.0_SA_COO~O` msg 32236, relay 107602).
- The agent's mail poller (round 9) reads its bearer through `assist.secret(MAIL_BEARER_SECRET)`, the env var holding the
  secret's name or ARN; the minute step reports `not-configured` while the env var is absent (`31980c736e`).
- `infra/aws/terraform/transcripts/chat_assist.tf`: the functions' environment is `local.ca_env`; the module grants
  `secretsmanager:GetSecretValue` on `secret_arns` (`modules/ldo/main.tf:295-298`). No mail entry exists in either.

**Rule 24.** Domain: what the round-9 deploy needs that does not need the reference: the env var and the secret read, both keyed on
one variable that defaults to empty. Set later, it is one value; empty now, it changes nothing. One cell; the deploy itself is not a
cell (a pair after the reference arrives).

| cell | what | serves | risk | chain, slot |
|---|---|---|---|---|
| `CA-d-1` | `var.chat_assist_mail_bearer_secret_arn` (default ""): when non-empty, `MAIL_BEARER_SECRET` joins both functions' environment and the ARN joins `secret_arns`; two read-only targeted plans prove empty = inert, set = wired | FWD-4 | WORLD by path under `infra/`; nothing applied | A, `~5` |

`fanout: 1 of 1 chains, cap 8`.

Battery: `comp-schedule` DECLARED-NOT-APPLICABLE; `comp-iam` RUN on the order (a policy statement is added under a variable);
`comp-adversary` RUN on the order.

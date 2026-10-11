# IRPT_ANLREQ round 6, workstream ~G -- decomposition: the packager's port presents a token; it never logs in

Issuer `2.0.0_SA_COO~G2`, 2026-10-11.

**Input:** `1.0.0_SA_CTO~DELL2` msg 5090: "re-cut the packager's port to the TOKEN form first -- no password and no users row
for a service ... attach cell 2 becomes two: (a) the port is re-cut to present a token, build only; (b) the mint is a token,
a secret holding it, and the read grant on the resident host's role, under its own pair, the IAM leg the laptop's. Two
things the re-cut's order states: which door the token opens and that it opens no other; and whether svc-commentary's
verifier can be reused as it stands, read in code."

## Round 5 of this workstream, closed (one cell)

`AR-g-41` is complete and merged @fb4aaf8fa2. Re-run by the issuer in the worker's tree and again in the shared tree after
the merge: `ar_g41_checks.py g41` read `AR-G41-OK cases=3 refusals=4 builder=26 runtime=18`; `regress` read
`AR-G41-REGRESS-OK factory=19 research=281`. The builder can write the three bindings (off by default) and the runtime
builds the live ticket port from a `packager` binding. Tree only.

## The two things the ruling asks this order to state (read by the issuer at HEAD)

File `infra/aws/lambda/ticket_center/lambda_function.py`, READ ONLY for this workstream.

1. **Which door the token opens, and that it opens no other.** ONE: `POST /api/scoped/tickets/{ticketId}/package`.
   `package_ticket` admits the caller by NAME: `userType` service and `email` equal to the type definition's
   `package_principal`, `"svc-irpt-packager"` (lines 1422-1426). On every other ticket route the subject is nobody:
   `principal_class` returns `UNRESOLVABLE` for a service subject that is not one of three named ones (lines 304-312), and
   the authorization matrix denies an unresolvable caller every action. What the token reaches on routes OUTSIDE the ticket
   service was read by `2.0.0_SA_COO~V2` for the commentary token, not by this seat (its pair's section 2: a service token
   with no firm claim reaches no firm); the mint's pair, not this build cell, restates it for this token.
2. **Whether svc-commentary's verifier can be reused as it stands: NO, not at this door.** The commentary token's firm
   check is the environment list `COMMENTARY_ALLOWED_FIRMS` (lines 341-344), used by CREATE. The package door does not use
   it: it binds the body's firm to the caller's OWN users PROFILE row through `_profile_scope`, and a caller with no row is
   admitted nothing (lines 1446-1452). So a token-form packager, which has no users row by design, is refused 403 at its
   one door today. The ticket service needs its own change before the token can attach: the package door's firm bound from
   an environment list. That file is TCKT_VNEXT's; sent to `1.0.0_SA_CTO~DELL2` and `2.0.0_SA_COO~V2` (msgs 5092, 5093).

## Cell (round 6, workstream ~G): attach cell 2a

| cell | lane | what EXISTS at the end |
|---|---|---|
| `AR-g-42` | worker | The packager's ticket port presents a bearer token read from a secret by NAME and makes NO login call; the `packager` binding is exactly `api_base` and `secret_name`, in the port, the runtime and the builder alike. Built and tested in the tree; NOT deployed |

## Not cells here

- **Attach cell 2b, the mint**: a token, a secret holding it, and the read grant on the resident host's role, under its own
  pair; the IAM leg is the laptop's. After this cell.
- **The ticket service's firm check for a row-less token subject**: TCKT_VNEXT's.
- **Attach cell 4, the binding**: held (CTO msg 5064 and the IRPT_YCDGEN round-13 analysis).

## Four-postulate record

(i) Domain: attach cell 2a only. (ii) One cell, three files that must agree on one binding shape (port, runtime, builder).
(iii) One intent: the packager is a service with one token for one door, not a person-shaped login. (iv) What this cell does
NOT move: any principal, any secret, any grant, the ticket service, any host. It REMOVES a shape: after it no code builds a
login request for the packager, and a binding carrying an `email` is refused.

fanout: 1 of 1 chains, cap 8.

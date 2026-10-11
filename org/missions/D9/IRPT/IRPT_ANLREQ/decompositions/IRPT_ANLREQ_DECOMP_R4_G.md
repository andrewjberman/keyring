# IRPT_ANLREQ round 4, workstream ~G -- decomposition: the packager is idempotent against its own store and reads no ticket

Issuer `2.0.0_SA_COO~G2`, 2026-10-11.

**Input:** `1.0.0_SA_CTO~DELL2` msg 4348 (item 4: "the packager retains what it renders, so its pre-check is its OWN store ...
no ticket read. If no such record is readable before the render, say which line stops it") and msg 4861 ("R2-pk-2 is LIVE ...
AR-g-32 no longer waits on it. Cut it."). Row `IRPT_ANLREQ-D2-W66-S1` (BLOCKING): the ticket service refuses the packager's
GET of a ticket, and `handle_commentary_ready` makes that read before any render or attach.

## Finding (read by the issuer at HEAD before cutting)

- **The line that stops a pre-render lookup today:** `infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py`
  line 260. The package is retained under the logical id `"%s-package-%s" % (request_id, sha)`, where `sha` is the sha256 of
  the RENDERED pdf. The artifact id is a digest of owner, family and logical id (`reports/repository.py` `_binding`), so the
  package's identity cannot be computed until after the render. A pre-check against the packager's own store therefore needs
  a logical id known BEFORE the render.
- **What is known before the render:** the request id and the commentary ref's sha256, both read from the acceptance record.
  One request with one commentary is one package.
- **The ticket service's conflict answers at HEAD** (`infra/aws/lambda/ticket_center/lambda_function.py` `package_ticket`,
  TCKT_VNEXT cell R2-pk-2): every 409 carries a `code`; `PACKAGE_ALREADY_ATTACHED` and `PACKAGE_TICKET_CHANGED` carry the
  stored package's identity under `package` (the four pointers plus `attached_at`, `attached_by`); the others are
  `PACKAGE_WRONG_TICKET_TYPE`, `PACKAGE_TICKET_COMPLETED`, `PACKAGE_FIRM_MISMATCH`.

## Cell (round 4, workstream ~G)

| cell | lane | what EXISTS at the end |
|---|---|---|
| `AR-g-32` | worker | The packager makes NO ticket read. Before it reads the commentary or renders, it asks its own store for the package of this request and commentary, by an id known before the render; a retained package means no render and a POST of that identity. A 409 `PACKAGE_ALREADY_ATTACHED` whose stored identity equals what the packager posted is the message DONE; any other conflict is a refusal named by its code. Built and tested in the tree; NOT deployed |

## Not cells

- **The packager mint and the attach release**: each under its own never-widen pair, after this cell merges
  (`IRPT_ANLREQ_DECOMP_R3_G.md`, the two later releases).
- **Any change to the ticket service**: TCKT_VNEXT's.

## Four-postulate record

(i) Domain: the one ruled item (msg 4348 item 4), one cell. (ii) One module pair: the packager and the one producer function
that names the package. (iii) One intent: a redelivered or repeated message attaches at most one package and never reads a
ticket. (iv) What this cell does NOT move: the principal's existence, any queue binding, the ticket service, and any deployed
byte. It DOES move the logical id under which a package is retained: no package is retained anywhere today (the packager is
bound on no host), so no existing record is orphaned; the order makes the worker state that as a read, not an assumption.

fanout: 1 of 1 chains, cap 8.

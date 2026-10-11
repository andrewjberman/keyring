# IRPT_ANLREQ round 3, workstream ~G -- decomposition: release 4 without the binding, then the packager's two live ports

Issuer `2.0.0_SA_COO~G2`, 2026-10-11.

**Input:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_ROUND_3_20261011.md` @430d79e86d, section 4,
workstream G (G1, G2, G3) and section 3 (row `IRPT_ANLREQ-D2-S30`). Rulings `1.0.0_SA_CTO~DELL2` msgs 4255, 4296 and 4301.

## Finding

Row `IRPT_ANLREQ-D2-S29` @0f55b28336: `infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py` `live_attach` and `live_ticket_package`
are stubs that raise `PACKAGER_PRINCIPAL_UNSET`, and no cell builds them. A resident that binds `commentary_ready_queue_url`
would end every real message in the dead-letter queue with no package.

## Cell (round 3, workstream ~G)

| cell | lane | item (analysis) | what EXISTS at the end |
|---|---|---|---|
| `AR-g-31` | ~G2 | G3, first part | The packager's ticket ports are real: with a `packager` binding present, `ticket_package` reads the ticket's `package` and `attach` posts I5, each as `svc-irpt-packager` over HTTPS with a credential read by NAME; with the binding absent both still refuse `PACKAGER_PRINCIPAL_UNSET`. Offline tests with fakes prove both arms and that no secret value is printed or raised |

## Not cells: the releases, each under its own never-widen pair, in this order

1. **Release 4 (G1; the round-2 cell `AR-g-23`, carried, this seat's direct act).** The ticket schema at or after 5be2acd7cc with
   criterion `REL4-READ5` verbatim on its apply order, and the 390 s read-back release. `commentary_ready_queue_url` ABSENT from
   the bindings; the pair states it and the after-read shows nothing polls that queue (row D2-S29 disarms there). The
   `ycharts/generate` suite is graded by failing SET against the base (row D2-S31), not by count. Pin candidate `eb72753aad`.
2. **The packager mint (G3, second part).** `svc-irpt-packager`: its users row and its credential, under its own pair. After
   `AR-g-31` merges.
3. **The attach release (G3, third part).** A resident build that carries `AR-g-31` and binds the queue. FWD-1's last hop and
   row D2-S18's answer.

**Precondition carried for whoever cuts I3 (section 3):** the trigger that feeds the commentary function real requests does not
go live before release 3 above can consume; the queue keeps a message four days.

G2 of the analysis (the IRPT_YCDGEN producer cell, msg 4188) is that project's round and is not cut here.

## Four-postulate record

(i) Domain: the analysis's workstream-G list, three items; G1 and the two later releases are releases, G2 is another project's,
which leaves one build cell. (ii) One cell, one module pair (the two ports and their wiring). (iii) One intent: the packager can
reach the ticket. (iv) What this cell does NOT move: the principal's existence, the queue binding, and any deployed byte.

fanout: 1 of 1 chains, cap 8.

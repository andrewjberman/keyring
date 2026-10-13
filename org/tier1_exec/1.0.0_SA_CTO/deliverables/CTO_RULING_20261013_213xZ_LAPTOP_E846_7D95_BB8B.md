# CTO RULING 2026-10-13 ~21:3xZ (1.0.0_SA_CTO, laptop box CTO) -- laptop calls e846, 7d95, bb8b (OPEN-CALLS SCAN 21:31Z)

## e846 (NFRA_CTLPLN): rotate the portal signing key after the S9112 purge, or accept the bounded token expiry?

**RULED: accept the bounded expiry. No rotation is cut now.**
- The material is purged: TO-CT-ab-10 deleted 8,513 pre-fix log streams, and the pre-cut credential census read 0/0/0/0
  (`org/tier2_senior/0.7.0_AE_CloudOps~U7/deliverables/NFRA_CTLPLN.TO-CT-ab-10.s9112-purge-record.txt`).
- The readers were account-internal principals.
- A real invalidation means retiring the previous key slot (OP-s-10 runbook step 7). That signs every user out, partner-firm and
  client logins included, and a forced sign-out of clients would itself be Andrew's word.

**Condition, row `NFRA_CTLPLN-S9122` stays the disarm path:** if any read of those streams by a principal outside the account is
found (CloudTrail data events, or the log-group resource policy), cut the rotation order at once. It gets its own never-widen pair,
off-hours, and carries Andrew's word for the client sign-out.

Otherwise the exposure closes on its own clock: refresh tokens on 2026-10-18 and device trust in 2026-11.

## 7d95 (NFRA_DEVPLN): who builds FWD-1's dell2 Investor Reporting feature?

**RULED: the REC.** The correction stands: IRPT_ANLREQ is NOT parked. It is dell2's number-one drive under the pivot (the dell2
direction packet, @4e963d4a12). Its next page change goes through the route, cut as `cand/dell2/<slug>` from the last PROD release
and registered with `open-calls.py add --kind approval`, never landed on DEV directly. It is client-facing (Ticket Center and the
analysis tab), so Andrew approves it on the open-calls list. That exercises FWD-1 and FWD-7 on organic work.

Routed to `1.0.0_SA_CTO~DELL2` through `0.0.0_AB_MSTR`.

## bb8b (NFRA_DEVPLN): the 7 unapproved dell2 commits on portal DEV

**RULED: the REC, with one waiver named.** The three IRPT_ANLREQ merges `62d455f5` through `a577cba5` were landed on DEV after
the settlement, before dell2 had read the route. Each is re-registered as one approval row, `cand/dell2/<slug>` bound to the merged
head sha, for Andrew to rule. They are client-facing. DEV is not rewritten (no rebase on a shared branch).

Registration's DEV-overlap refusal (DP-b-5) is WAIVED for exactly these three named merge shas, and each row carries this ruling as
its reason. No other DEV-only commit is admitted this way. From now on, dell2 lands portal changes only through the route
(CONTRIBUTING-BOXES.md) and the S03 gate makes that mechanical.

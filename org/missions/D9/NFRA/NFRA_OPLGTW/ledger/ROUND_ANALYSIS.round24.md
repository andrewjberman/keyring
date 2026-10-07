# NFRA_OPLGTW -- ROUND 24 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-07 ~10:3xZ -- r25 live; two rulings; r26 carries the rest

**Who wrote this and why.** `1.0.0_SA_CTO~O` wrote rounds 18 to 23 and is not live after the site-Z reboot. `1.0.0_SA_CTO~Z`
took this round's L10 by its ruling msg 30782 so the round does not sit ownerless. NFRA_OPLGTW is outside this seat's armed
self-drive scope. If `1.0.0_SA_CTO~O` is seated, the next round's analysis is that seat's.

**L10 on `3.0.0_SA_CVO~Z`'s round-24 slug** (msg 30793, `surprise-channel/remediations/REMEDIATION_v11.md` @0d5acec2d0;
graduated by `adjudications/ADJUDICATION_v16.Z.md` C-S44):
- 2 OPEN for this seat: Z-S64, Z-W28-S11.
- 2 OPEN for the issuer: Z-S65, Z-W28-S13.
- REMEDIATED in place: Z-S63, Z-W28-S7. Still OPEN from earlier slugs: Z-S61, Z-W28-S9, Z-W28-S2.

## 1. What round 24 did (from the slug; this seat re-ran nothing)

- 3 of 3 orders complete: OG-up-1, OG-hg-1, OG-rl-11. r25 @240ac2fe5a is live.
- The CVO re-ran the 8 checks: 6 PASS. up1.AC2 and rl11.AC1 read FAIL only on their live..CLOUD conjunct, because r26's cells and
  the ETFS_RIVALS chart route have since merged into CLOUD. That is a moved base, not a defect of round 24.
- Round 23's R33 (the send split) and R35 (the halt gate's order lookup) are the two rows the slug reads REMEDIATED.

## 2. Outcome grades

**Carried from round 23, NOT re-measured: 0 REALIZED, 0 NOT_REALIZED, 8 HELD, 0 DEFERRED.** The slug carries no L9 grade and no
row that moves an outcome. FWD-1 to FWD-8 stay HELD on OG-v-7, G-E and R7's host-side flag, as `ROUND_ANALYSIS.round23.md`
section 2 states them.

## 3. Rulings

**R36 -- Z-S64: the rivalfunds routes record which page was served. Three args and a size join the audit record; nothing else.**
- The gap: `audit.py` `_safe_args` drops every arg of a tool not in `_ARGS_ALLOWLIST`, and `rivalfunds_view` is not in it. So the
  page, audit, archive and (from r26) chart routes write records that differ only in time, identity and outcome.
- Ruling: `rivalfunds_view`'s `day`, `route` and `fund` join the allowlist, and the handler passes `bytes_returned`.
- Why this is not a privacy widening: a day is a date, a route is one of four fixed names, and a fund is a public ETF ticker
  already constrained to `[A-Z0-9]{1,8}`. No holder data, no query text and no free-form value is added. The allowlist entry
  names those three keys exactly; any other arg of that tool stays dropped.
- Why it is needed: ETFS_RIVALS's round-13 ruling names the gateway access record (status, identity, size, time) as the proof of a
  served audit page, and today that proof needs a join to the host access log by timestamp.
- One cell, at most three mechanical criteria, with a negative control: an arg outside the three is still absent from the record.
- **It does NOT ride r26.** r26 is cut and in Phase A. This ships in the release after it. Until then the proof of a served page is
  the audit record joined to the host access log by timestamp, as the slug states.

**R37 -- Z-W28-S11: read first, then one act that is Andrew's.**
- The fact: r25 narrowed the scoped identity's request to 9 scopes, but the access token comes from the existing refresh token,
  which still carries the earlier consent (17 Graph scopes plus CallTranscripts.Read.All, with Mail.Send, Mail.ReadWrite and
  Calendars.ReadWrite among them). The tool allowlist is the only narrowing in effect.
- Step 1, an issuer read with no sign-in and no change: whether a fresh consent through `/login` alone drops the earlier grants,
  or the earlier consent must also be revoked in Entra. The slug says this is unread. It is read from Microsoft's documentation
  and from the current token's own scope list, and written as one file.
- Step 2 follows the read and is listed in section 5. This seat does not decide it and no agent performs it.
- REMEDIATED when a token acquired after the act lists only the narrowed scopes (the slug's own test).

**The issuer's rows.**
- Z-S65 (the unchecked execution_id): ships with r26. One term from the slug is repeated here because it binds the release: r26
  must not ship the allowlist row that admits the scoped concierge to the status tool (OG-al-2) without the shape check. Both are
  in the one release set today; if the set is ever split, the check goes first.
- Z-W28-S13 (the status tool's `displayed_date` is null against the served manifest): one cell. It reads the served manifest's own
  date key with a test against the live manifest's key set, and exercises the tool once through its wrapper with a real principal.
  The daily send's caller texts point at this field, so it is first on the list after r26.

## 4. Enrichment list for the next issuance (ONE issuance by `2.0.0_SA_COO~O`)

1. **r26, as re-cut** (amendment A3 @c38d69aa3d): OG-al-2, OG-up-2 and the ETFS_RIVALS chart route RIV-rt-1 as one release under
   three halves on the new sha. CVO half: `3.0.0_SA_CVO~Z` (ruling msg 30779). CTO half: this seat, on request. It deploys only after
   the four ETFS_RIVALS commits are on origin and today's Bloomberg send is confirmed served.
2. **Z-W28-S13 cell:** the status tool's date key, and the wrapper exercise.
3. **R36 cell:** the three audit args and `bytes_returned`, for the release after r26.
4. **R37 step 1:** the re-consent read, one file.

After that the project parks again on OG-v-7, G-E and R7's flag (R28), unchanged.

## 5. Acts only Andrew can do

- **The scoped concierge's sign-in through `/login`, and any revocation of its earlier consent in Entra** (R37 step 2). Citation:
  it is his login and his tenant's admin consent; the slug row Z-W28-S11 names it "Andrew's call". Step 1's read says which of the
  two is needed.
- **The site-Z push** that puts the four ETFS_RIVALS commits on origin (LD-0367/0368), which r26's Phase B waits on.

## 6. What this analysis does not do

It deploys, applies and grants nothing, and it amends no PRD text. It re-measures nothing beyond the slug: no check was re-run, no
host was read, and the audit and token mechanisms are stated as the slug states them.

-- 1.0.0_SA_CTO~Z

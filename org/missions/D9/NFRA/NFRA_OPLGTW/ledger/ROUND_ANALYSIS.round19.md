# NFRA_OPLGTW -- ROUND 19 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-10-06 ~06:1xZ

**L10 on `3.0.0_SA_CVO~O`'s round-19 slug** (msg 29924, `surprise-channel/remediations/REMEDIATION_v7.md` @7ae12ce2d1):
- 6 rows: 5 dismissed and 1 OPEN, the issuer's.
- 2 rows advanced to REMEDIATED: Z-W22-S10 and Z-W25-S3.
- The r19b guards held.
- No L9 grade.

**The issuer's terminal message** is msg 29922: round 19 is terminal at 2 of 2. r19b `cf4b036e62` is LIVE and CLOUD
equals live.

**Issuer: `2.0.0_SA_COO~O`.** ONE issuance, section 4.

## 1. What round 19 did

- **OG-ts-2.** The route inventory classifies `/yearinreview`. The key count is 51, the `build_package` shape is
  aligned, and each test process gets its own export directory (30 concurrent runs, 0 FileNotFoundError). One process
  runs 148 tests with 0 errors.
- **OG-rl-7 under R22 (r19b `cf4b036e62`, LIVE 05:31:52Z).**
  - OA-e-10 was reverted on CLOUD first, so `/login` is byte-equal before and after the act.
  - MS-sg-1's sender-field correction shipped.
  - The verify passed 7 of 7, and `.env` holds 51 of 51 names.
  - **Drain-back:** CLOUD equals live for the gateway tree (`ln1.AC1`: 0 files differing). R16's lineage is closed.

## 2. Outcome grades

Unchanged: **0 REALIZED, 0 NOT_REALIZED, 8 HELD, 0 DEFERRED.** Every FWD waits on a human act:
- OG-v-7 (Andrew's own tests, then Alyssa);
- G-E (Menachem's tid/oid);
- Z-W15-S41 (Andrew's grant word);
- R7's host-side flag.

## 3. Rulings

**R23 -- two rows the slug lists as "still the CTO's" were ruled last round.** Round-18 analysis section 3,
@b397c851c0:
- **Z-W27-S3:** CLOSED_UNREMEDIATED, ACCEPTED_BY_RULING **R19** (the per-route latency cap).
- **Z-S55:** **REMEDIATED** by **R20**, on this seat's HEAD read of the rewritten `.tools/m365-mcp-kit/README.md`.

The disarm owner decides and the CVO writes (@cc05804f8f). The CVO applies both clocks citing @b397c851c0.

**R24 -- OA-e-10's re-cut is cut now (R22 item 2), and it carries its own instrument (row S52).**
- **The admit set.** `/login` admits the server-held identities (`OTP_MAILBOX`, `MS_INGEST_IDENTITY`) PLUS every
  principal whose `tier.resolve_tier` result carries at least one Graph-using tool.
  - Restricted profiles are REFUSED.
  - An unresolvable tier REFUSES (fail closed).
  - The cell names the Analyst's service identity and proves the tier rule refuses it.
- **The instrument.** `/login` writes one audit record per request: outcome `admitted`/`refused`/`consent`, the
  principal key or email digest, and the reason. The lake can then see `/login` from the release on. S52's blind spot
  is closed by construction, not by a journal workaround.
- **Acceptance:**
  - a non-restricted principal completes the round trip NeedsLogin -> `/login` -> consent, and its principal cache is
    written;
  - a restricted principal gets 403, audited;
  - the server-held identity is unchanged;
  - empty settings with an unresolvable tier admit nobody.
- **The release halves name the admit set before and after**, computed from the tier rule over the current principal
  population. A principal admitted today and refused after is listed by digest and blocks unless it is restricted.

## 4. THE ENRICHMENT LIST ROUND 20 CUTS (one issuance, `2.0.0_SA_COO~O`)

1. **OG-lg-1 (build, LOCAL): R24.** `login()`'s tier-based admit set and the `/login` audit record, with the
   acceptance above. Its write surface is `app/server.py`, the audit write site and tests. Its spec is NFRA_OPALAI
   OA-e-10 as re-specified by R22 and R24.
2. **OG-rl-8 (release): OG-lg-1 on live `cf4b036e62`, under three halves**, following `RELEASE_ORDER_FORM.md` in full
   (pre-GO exercise, R21 arm not triggered, DRAIN-BACK).
3. **Z-W15-S58 (test cell, LOCAL):** make `test_ogx2_ac01` deterministic.
   - Find the export-stream `job_failed` cause: timing, the shared path or the engine deadline.
   - Until it is fixed, every baseline names it FLAKY, never "failing".

**Stated dependencies, not cells:** Z-W15-S41 at Andrew; OG-v-7; G-E; R7's flag; Z-S43.

## 5. What this analysis does not do

It deploys, applies and grants nothing. It re-measured nothing beyond the slug and the terminal message. The r19b
facts are the CVO's guard reads on the deployed host.

## 6. Addendum ~07:0xZ 2026-10-06 -- R25, `/login` admits opalbloomberg@ (`2.0.0_SA_COO~O` msg 29939, rows Z-W22-S11, S12)

**R25.1 -- (b): ADMIT opalbloomberg@opalinvest.com. Strike lg-1's `scoped_service_identity` refusal.**
- **What the identity is.** It is the Bloomberg Teams concierge (`identity_scope.py:53+`, OPAL_ANALYST TO-3). Its
  allowlist is almost entirely delegated Graph Teams tools: `poll_addressed_teams_messages`, `list_chats`,
  `read_chat_messages`, `send_chat_message` and the channel set. A lapsed cache sends it to `/login` (`NeedsLogin`,
  `token_broker.py:55-62`).
- **Why not refuse it.** The refusal rests on "its Graph token is minted by its operator's bridge sign-in". The bridge
  redeems with `AUTHENTICATION_SCOPES` (`email`, `:353`). Whether that refresh token mints Graph tokens silently depends
  on tenant consent, and nobody has measured it. A production identity is not dead-ended on an unproven premise.
- **No widening.** Today's live `/login` admits it.
- **Its fence stands.** `identity_scope`'s allowlist is enforced at both dispatch chokepoints. `/login` only re-mints
  its token.

**R25.2 -- withdrawn and corrected.**
- **R24's clause withdrawn:** "the Analyst's service identity stays refused". This seat wrote it from OA-e-10's stated
  purpose without reading `identity_scope.py`; that identity IS the concierge, whose duty is Graph tools.
- **R22's premise corrected.** It said "/login is the ONLY path that grants a person delegated Graph scopes", and that
  is UNPROVEN, not established. The bridge's principal cache is documented as the source Graph-using tools acquire from
  (`:346-356`). R22's outcome stands on the narrower ground: `NeedsLogin` directs users to `/login`, so a 403 there is a
  dead end in the product. The rows citing R22 carry this correction.

**R25.3 -- least privilege for a scoped identity, as a later enrichment, not a `/login` refusal.** A scoped identity's
`/login` consent requests only the Graph scopes its allowlisted tools need, instead of the full `GRAPH_SCOPES`
envelope. That meets OPAL_ANALYST PRD 4.3's intent without a dead end. It needs its own cell with a scope map per tool.

**R25.4 -- Z-W22-S11 accepted, with the semantics stated truthfully.**
- On the GUI path, `/login` has no principal, so `resolve_tier(None)` answers the READ_ONLY floor, which carries read
  Graph tools.
- So the rule in effect is: ADMIT every verified, non-email-denied tenant identity.
  - Restricted profiles are refused by the email-deny guard (row W3-S22).
  - The tier clause is a fail-closed backstop: an unverified provider, an unresolvable tier, or no Graph tool.
- lg-1's docstring and the rl-8 ask say exactly this.
- The release's real gains over live: the `/login` audit record (S52 closed by construction) and the fail-closed
  ordering.

**The write surface.** The issuer amends OG-lg-1 under R25.1 and R25.4:
- strike the clause;
- make the test assert opalbloomberg@ is admitted AND its allowlist still denies an out-of-scope tool;
- correct the docstring.
Then rl-8 is cut on the amended drain.

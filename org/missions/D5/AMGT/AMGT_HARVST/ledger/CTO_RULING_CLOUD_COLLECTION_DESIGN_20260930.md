# AMGT_HARVST -- CTO RULING on the cloud collection design, and ENDPOINT addendum proposal FWD-10 -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~17:4xZ

**The word:** Andrew-direct ~17:2xZ, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_172xZ_HARVST_CLOUD_HEADFUL_NOPECHA_REST_API_LONG_LIVED_TOKENS_TO_CRO.md`
@`79bc898865`.
**The research:** `4.0.0_SA_CRO~Z`, `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/HARVST_CLOUD_COLLECTION_DESIGN_20260930.md` @`9473d06426`
(msg 27298, read to EOF).
**The routing:** a DESIGN FORK, ruled by the driver the tick the research landed (/self-drive Step 1).

## 1. WHAT THE RESEARCH ESTABLISHED (as measured by the CRO)

1. **NopeCHA is NOT an all-in-one captcha solution.** This answers his question.
   - It documents none of the three challenges the publishers actually serve:
     - DataDome (wsj, barrons);
     - PerimeterX/HUMAN press-and-hold (bbg);
     - Cloudflare's managed challenge (ft).
   - It covers FT's login hCaptcha only. The repo already solves that one another way.
2. **Long-lived tokens are necessary but NOT sufficient.** bbg's token is valid to 2027-09-11, and its REST call was still challenged
   at 04:40Z today with no credentials entered.
   - The challenge follows the CLIENT (IP reputation, TLS fingerprint, rate), not the token.
   - Andrew's model is right: long-lived tokens plus REST shapes, no crawler. It lacks one piece: an egress the publishers' scoring
     accepts.
3. **Where the tokens are held today:**
   - bbg and ft are in AWS Secrets;
   - wsj and barrons are only in an encrypted file on this Windows box, so no cloud host can use them today.
4. **One cloud route already returns WSJ daily:** ASTN_WSJFT's transient EC2 through Bright Data Web Unlocker, 12-18 articles a day,
   today included.

## 2. RULING -- the design, and the pieces that need a vendor or spend act

**ADOPTED (the CRO's s.4 items 1, 2 and 5; Andrew's shape, built from existing parts):**
- **One harvester host.** A small or nano EC2 per his word. It is transient, started, run and stopped by an orchestrator Lambda, the
  ASTN and YCharts shape.
- **Per publication, a token keeper:**
  - probe the stored token with the publication's own `auth_check` (`contracts.json`);
  - if the token is valid, go straight to the REST pulls through the per-publication shapes;
  - only if it is invalid, re-sign in on the SAME host (Xvfb and Playwright, credentials from Secrets) and write the bundle back.
- **All five bundles live in AWS Secrets.** wsj and barrons leave the local encrypted file.
- **A pull moves to Lambda only where a measured probe shows that egress unchallenged.** That is his "ideally entirely on a lambda",
  held to a measurement.
- **Every challenge is recorded under `C-HV-TRUST-TOKEN` v0.11** (`bot_check` / `unclassified`, never expiry). The leg parks with the
  publisher named and never loops.
- Every new resource name and address is builder output (`lib/opal_naming`; CLAUDE.md rule 30).

**Egress and challenge-passing (the CRO's s.4 items 3-4): NOT adopted by this seat.**
- This is a vendor use (Bright Data residential egress and Web Unlocker) that no word of Andrew's names for HARVST. ASTN holding the
  account is availability, not authorization.
- It is listed for him as an ACT, with the risk the CRO states plainly (s.5): unlockers get past the publishers' controls, so Opal's
  paid subscriber accounts could be flagged or closed, and the practice likely conflicts with the publishers' terms.

**Consolidation with ASTN (the CRO's s.4 item 6): RULED.**
- The TOKEN STORE is one store now: Secrets, written by the HARVST token keeper and readable by ASTN.
- Moving ASTN's box onto the harvester host is ASTN's own migration, never a rider on HARVST.
- No second store and no parallel host is stood up for the same publisher (CLAUDE.md NEVER shadow pipelines).

**Licensed access (the CRO's s.5 and s.6.4):** Factiva/DNA, FT's content API and Bloomberg news are spend and contracts. They are listed
for Andrew as an ACT. This seat's REC is that licensed access is the durable route, because it removes the challenge problem instead of
fighting it.

## 3. WHAT IS CUT NOW, with no vendor word needed (publisher egress under R-21 @b390c36444)

These are routed to `2.0.0_SA_COO~H` for round 31. Round 30 is in flight and its spec is frozen.

| # | cell | risk |
|---|---|---|
| 1 | **Token store:** wsj and barrons bundles into Secrets (builder-named), plus ft's bundle expiry measured and recorded. The local file stays until the cloud keeper has proven a read. | WORLD, pair |
| 2 | **Egress probe:** from a Lambda and from a plain EC2 in the account, one `auth_check` and one REST listing per publication with the stored token. Each attempt is classed per v0.11. | WORLD (read-only egress, R-21) |
| 3 | **The harvester host and orchestrator Lambda** (Terraform via `safe-apply`, builder names, stop-after-run). The keeper and pulls run the existing `publishers.py` shapes. | WORLD, pair |

- Cell 2's output is the measurement that decides Lambda vs host per publication, and whether any publication runs clean WITHOUT a
  managed egress. It is the evidence Andrew's egress decision rests on.
- The schedule stays Andrew's (PRD s.2 boundary). The host runs on demand until he words a cadence.

## 4. ENDPOINT ADDENDUM -- PROPOSAL (the CTO's L2; Andrew confirms DONE WHEN)

```
  FWD-10 Collection runs in Opal's cloud from a stored long-lived token,
         over each publication's REST shape -- no crawler, no login page,
         no desktop
         DONE WHEN  EXERCISED -- one on-demand run on the cloud harvester (a
                    small EC2, or a Lambda where a probe measured that
                    publication unchallenged) starts from each publication's
                    token in AWS Secrets, pulls the validation security's
                    articles for all five publications through their REST
                    shapes, and signs in -- on the same host -- only for a
                    publication whose token its probe showed not to work;
                    the run record names, per publication, the token source,
                    the host, and each attempt's class
         ACCEPT     No collection depends on Andrew's desktop or on anyone
                    signing in by hand; a lapsed token is renewed in the
                    cloud and written back to Secrets.
         SOURCE     Andrew-direct 2026-09-30 ~17:2xZ: "the mechanism for
                    drawing news is not using a crawler or going through login
                    page, its rest api pulls through dedicated shapes per
                    publication, ideally running entirely on a lambda. I don't
                    mind having a dedicated small or nano ec2 that is tasked
                    with handling all of this"
```

**Stated dependency, not hidden:** "all five publications" is reachable only if cell 2 shows clean egress, or Andrew words a managed
egress, or a licensed route replaces the challenged pull. This FWD is not graded REALIZED on fewer.

## 5. ACTS ONLY ANDREW CAN DO (cited)

1. **Confirm FWD-10's DONE WHEN** [Rule 27 L2; `/open-calls` self-adjudication clause: "i will confirm CTO's DONE WHEN"].
2. **A per-use word for Bright Data egress and Web Unlocker on HARVST's pulls** [CLAUDE.md "NEVER call an external vendor API without
   Andrew's explicit per-use word"]. The CRO's s.5 risk to the subscriber accounts is his to accept.
3. **Licensed-access pricing requests** (Factiva/DNA, FT content API, Bloomberg news) [spend and contracts beyond his grants].

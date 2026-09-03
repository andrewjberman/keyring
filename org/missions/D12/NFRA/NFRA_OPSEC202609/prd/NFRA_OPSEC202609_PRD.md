# NFRA_OPSEC202609 -- the portal, the gateway and the website are defended at their own front doors, and someone is watching

*Registered 2026-09-02 ~17:5xZ as `D12_PLATFORM_FORTIFY`, RENAMED to `NFRA_SECURITY202609` at ~18:4xZ on Andrew's word (section 6), and RENAMED AGAIN to `NFRA_OPSEC202609` on 2026-09-03 ~06:5xZ on Andrew's word at the `1.0.0_SA_CTO~Z` terminal, verbatim **"Call it NFRA_OPSEC202609"** (section 6) -- the tree grammar refused the 14-character name. The directive membership (D12), every `FWD-n` and every `C-n` id are unchanged by either rename; records written before a rename cite a former code and resolve to this project. This PRD lives at its tree home `org/missions/D12/NFRA/NFRA_OPSEC202609/prd/` (L4 of `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`); `docs/architecture/NFRA_SECURITY202609_PRD.md` is a redirect stub.*

**Directive:** D12 Platform Operations (SITEZ-placed, Andrew-direct 2026-08-31 @efcfa8cc5b) · **Fabric:** site-z · **dep_stage:** PRD
**L2-L4 owner + author:** `1.0.0_SA_CTO~Z` · **L5-L6 owner:** `2.0.0_SA_COO~Z` (workers seated by the COO at L6; L7 is Tier-2 only) · **L8-L10 owner:** `3.0.0_SA_CVO~Z` · **Integrator:** `0.0.0_AB_MSTR~Z` (register, push windows, /govern over the site-Z sequence per Andrew ~06:4xZ)
**Brief (L1):** `docs/briefs/PLATFORM_ATTACK_SURFACE_ASSESSMENT_20260902.md` @32daebf403 (20,398 bytes, 262 lines, authored 2026-09-02 at `docs/security/` @a9a47f65a1 and moved to the admitted `docs/briefs/` shape at L3; the old path is a redirect stub and the @a9a47f65a1 pin still resolves there).
**Version:** v0.9, 2026-09-03 ~13:2xZ -- **v0.9 = THE EVIDENCE STORE AND THE LOG DESTINATION ARE TWO BUCKETS (rows NFRA_OPSEC202609-Z-S37 and the L4 question 2.0.0_SA_COO~Z 19794/19797; RULED by 3.0.0_SA_CVO~Z 19801 on this seat's tick-8 pitch 19796 + 19799).** C-8 put a service-written log sink inside a bucket the same constraint declared role-only: `opal-data-security` is written by TWO AWS service principals (`delivery.logs.amazonaws.com` -> `waf-logs/cloudfront-access/*`, `logdelivery.elasticloadbalancing.amazonaws.com` -> `waf-logs/alb-opal-gateway/*`, both landed by the COMPLETE cell OP-s-5) while C-8 denies every principal outside the sentinel, reconciler and `opal-security-admin` roles and C-13 scopes the key to those same three roles. Both statements were correct; they could not hold in ONE bucket, because S3 default encryption is per-BUCKET and not per-prefix. **THE SPLIT IS A SELECTION INSIDE RATIFIED SCOPE, NOT A REPAIR OF IT:** 7.3's own path list already reads "(Firehose raw, if S3 delivery is chosen over CloudWatch Logs)" and manifest row S5 already reads "CloudWatch Logs `aws-waf-logs-opal-{scope}`, or Firehose into S17 `waf-logs/`", so the ratified design ALREADY admits the raw stream never landing in the evidence bucket. **THE EMPTY SURFACE MOVES:** the evidence store proper becomes a NEW project-owned bucket `opal-security-evidence` under the project CMK (new manifest row S17, amended C-8), and `opal-data-security` KEEPS its name, its SSE-S3 encryption and its live delivery, re-homed as FWD-5's log destination (new manifest row S28). Measured before the ruling: `list-objects-v2` on `opal-data-security` = 36 objects, EVERY one under `waf-logs/`, newest 13:10:11Z, and `cases/`, `reports/`, `allowlists/` empty -- so nothing live moves, the COMPLETE cell OP-s-5 is not reopened, and no delivery leg is touched. **C-13 AND C-14 ARE UNAMENDED AND BECOME EXACTLY RIGHT:** under the split the CMK bucket has NO service-principal writer at all, so the three-role enumeration is correct rather than incomplete. C-15's target follows the evidence store. **THE CAUTION THE RULING ATTACHES (19801):** FWD-18's ACCEPT names "log extract" at :207, so the evidence store HOLDS cases, LOG EXTRACTS, reports and allowlists -- only the RAW DELIVERY STREAM moves out; an amendment reading "logs leave the evidence store" would make FWD-18's own acceptance unsatisfiable by the thing it builds. Also closed here, the FIFTH referent in C-8's family (19801): 7.3's `waf-logs/{scope}/` grammar described Firehose-raw WAF logs while what actually delivers is CloudFront and ALB ACCESS logs under two named prefixes -- the path list now names what delivers. The unmeasured variable (whether those service principals can write to a CMK-encrypted bucket) STAYS unmeasured and leaves the critical path: nothing here asks them to. Precedent, and it is this seat's own: C-15 ruled the sibling access-logs target SSE-S3 rather than the project key at ~08:3xZ for exactly this reason, with the reason written down at the time.** Before it, **v0.8 = two of Andrew's cards RULED by his word at this terminal ("Recs approved" on /open-calls): OP-x-2 the website edge = CloudFront + WAF managed rules (FWD-13 / S13, the hold lifted); OP-x-6 the trust of `opal-security-admin` = Andrew alone for round 2 (C-14 / S26). Record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260903_084xZ_CTOZ_RECS_APPROVED_OPX2_CLOUDFRONT_OPX6_ANDREW_ALONE.md`.** Before it, **v0.7 = the TARGET of the evidence store's access logging (row NFRA_OPSEC202609-Z-S5): C-8 said "the CloudTrail bucket", whose policy admits only cloudtrail.amazonaws.com, so S3 server access logging could never deliver there; the target is now a project-owned access-logs bucket `opal-data-security-access-logs` (new C-15, manifest row S27, OWNS item 19), graded by a DELIVERED object, never by the configuration.** Before it, **v0.6 = the IDENTITY half of the same C-8 item (row NFRA_OPSEC202609-Z-S4): the "CTO-admin role" C-8 named does not exist (0 of 216 roles; the Terraform applier is an IAM user); the referent is now ONE Terraform-declared role `opal-security-admin` (new C-14, manifest row S26, OWNS item 18) whose TRUST -- which humans may assume it -- is Andrew's card OP-x-6.** Before it, **v0.5 = ONE ruling at L4 (section 6, last bullet): "the estate CMK" in 7.3 / C-8 / C-9 named a key that does not exist as a customer-managed key (measured at the worker's seat, row NFRA_OPSEC202609-Z-S3); the constraints now name ONE project customer-managed key, `alias/opal-security`, new C-13, new manifest row S25.** The vintage map before it, because the flat PRD carried no version number: **v0.1** @eba7e15054 (mint, FWD-1..13) · **v0.2** @7a51451d69 (FWD-1..13 RATIFIED, FWD-14..18 ADDED, section 7 written) · **v0.3** @8cbe362358 (section 7 RATIFIED as design, 7.6 C-1..C-12) with the rename-ruling wording @72437a8453 · **v0.4** @43b75ffbd6: tree home, PRD_HEADER, SURFACE MANIFEST (section 8), sequencing input (section 9), code `NFRA_OPSEC202609`, and the ENDPOINT block's `FWD-10`..`FWD-18` lines re-spaced to the L6 gate's definition form (`FWD-n` + two spaces; the text is byte-identical otherwise). No outcome, constraint, ruling or acceptance property changed between v0.3 and v0.4.
**archetype:** SCRIBE (spec)

```json
{
  "project": "NFRA_OPSEC202609",
  "directive": "D12",
  "fabric": "site-z",
  "prd_version": "v0.9",
  "step": 4,
  "brief_ref": "docs/briefs/PLATFORM_ATTACK_SURFACE_ASSESSMENT_20260902.md@32daebf403",
  "endpoint_outcomes": [
    "FWD-1",
    "FWD-2",
    "FWD-3",
    "FWD-4",
    "FWD-5",
    "FWD-6",
    "FWD-7",
    "FWD-8",
    "FWD-9",
    "FWD-10",
    "FWD-11",
    "FWD-12",
    "FWD-13",
    "FWD-14",
    "FWD-15",
    "FWD-16",
    "FWD-17",
    "FWD-18"
  ],
  "status": "RATIFIED"
}
```
*PRD_HEADER block (`org/standards/PRD_HEADER.schema.json`; limb 5 of `.tools/to-pipeline-gate.py`). `brief_ref` is the L1 artifact pinned at the L3 commit that placed it in an admitted shape. `status: RATIFIED` because every outcome's DONE WHEN was confirmed by Andrew at L2 (FWD-1..13 and the addition of FWD-14..18 at ~17:5xZ, section 7 at ~18:2xZ, both 2026-09-02) -- his last touch point under the spine; L5 may begin on this header.*

**Commissioning word (Andrew-direct 2026-09-02 at the 1.0.0_SA_CTO~Z terminal, VERBATIM):** *"I agree with your assessment, what I would like you to do now is /endpoint --forward this brief and let's render it into an actionable PRD, the registered project for which will be attached on the D12 Directive."*

## ENDPOINT (step 2, /endpoint --forward)

*Phase 0 output, verbatim. `FWD-n` ids are PERMANENT and never reused; a retired outcome leaves its number vacant. `DONE WHEN` is the BAR, not the current state (nothing is built). ACCEPT lines are plain English and disputable, by rule.*

**RATIFIED -- FWD-1 through FWD-13**, and **FWD-14 through FWD-18 ADDED in the same word** (Phase 2 scope addition at step 2; their SOURCE is his sentence, not the brief). Andrew-direct 2026-09-02 ~17:5xZ at the 1.0.0_SA_CTO~Z terminal, VERBATIM AND ENTIRE: *"agreed onall of these, plus I would add that suspicious activity picked up by WAF shoudl trigger an email to me at andrew@opalinvest.com. Furthermore, I want a mechanism whereby there is a triggerable mechanism to block said IP and a file on the subject is maintained somewhere. I think we probably need an opal-data-security bucket included in this project which we use for storing relevant information on these subjects + maybe a table of blocked IPs attached like a DDB opal-suspicious-addresses. I want anyone trying to bust down our door to get blocked and listed in there with relevant files on teh case stored in said bucket in relevant path structure as well as means to unblock IP. I think it is preferable to just block their IP on a trigger rather than wait for a human to remediate."*

**Section 7 RATIFIED 2026-09-02 ~18:2xZ**, Andrew-direct at the same terminal, VERBATIM: *"I like all of your ideas and want them worked into the PRD"* -- the dependency, the three refinements, the architecture, the build ladder and the stated bound are no longer a recommendation; they bind the decomp as the constraints in section 7.6, and each of FWD-14..18 below carries a `BOUND BY` line naming its constraints.

```
  FWD-1  Nobody can use a portfolio write feature without being logged in -- no
         matter which address they send the request to
         DONE WHEN  EXERCISED -- a request with no login, sent straight to the
                    system's own address rather than through the portal, has
                    actually been tried and refused
         ACCEPT     the same action that works for a logged-in person using the
                    portal is turned away when a stranger sends it directly, and
                    a saved portfolio cannot be changed by anyone who never signed in
         SOURCE     brief F1 (lines 14-60): "20 method-bearing resources ... NONE";
                    the docstring that claims a control that does not exist

  FWD-2  A request that did not come through our front door is refused even if
         it carries a real login
         DONE WHEN  EXERCISED -- tried with a valid login at the direct address
                    and refused; tried through the portal and admitted
         ACCEPT     a person whose login works through the portal cannot take the
                    same login and talk to the system's back door with it
         SOURCE     brief F1 remediation ("a real secret ... required by the
                    authorizer"), F2, F4 -- the one mechanism all three share

  FWD-3  The public market and sentiment feeds cannot be used to run up our
         vendor bill
         DONE WHEN  EXERCISED -- an anonymous request for a never-seen keyword has
                    been sent and produced no paid computation
         ACCEPT     someone who is not logged in and asks for something we have not
                    already worked out gets what is already on file or a polite
                    refusal -- never an answer that cost us money to make
         SOURCE     brief F2 (lines 65-83), the OpenAI fallback on a cache miss

  FWD-4  When someone hammers the login page, a named person is told
         DONE WHEN  EXERCISED -- the notification has fired on a real or staged
                    burst and the person named has read it
         ACCEPT     a burst of blocked sign-in attempts produces a message that
                    reaches a named human; a quiet day produces none
         SOURCE     brief F3 (lines 88-111): "remediated by nobody unless a human
                    reads them"

  FWD-5  Blocked and suspicious traffic is kept long enough to be investigated
         DONE WHEN  APPLIED -- the records are being written to durable storage
         ACCEPT     a week after something was blocked, someone can still list
                    which addresses were blocked and what they were asking for
         SOURCE     brief F3: WAF logging not configured, sampled requests only
                    for three hours; CloudFront and load-balancer logs off

  FWD-6  Common web attacks are stopped at the front door, not by each page
         DONE WHEN  EXERCISED -- the protections have run in watch-only mode long
                    enough to know what they would wrongly stop, and have then
                    been switched to stopping
         ACCEPT     a request that matches a well-known attack pattern is refused
                    before any of our own code sees it, and ordinary portal use
                    is not disturbed by the change
         SOURCE     brief F5 (lines 132-142), and the gateway's watch-only rule
                    groups in WS2

  FWD-7  Losing the login throttle's bookkeeping never opens the door wider
         DONE WHEN  EXERCISED -- the bookkeeping has been made unavailable on
                    purpose and sign-in slowed rather than became unlimited
         ACCEPT     if the throttle's own records cannot be reached, sign-in
                    attempts slow down or pause -- they never become unlimited
         SOURCE     brief F4 (lines 113-130): "return; // fail-open"

  FWD-8  The tables holding logins and partner roles cannot be deleted by
         accident and can be rewound after a mistake
         DONE WHEN  APPLIED -- the protections are switched on for every such table
         ACCEPT     every table that holds a login or a partner's role refuses to
                    be deleted, and can be restored to how it looked at any
                    moment in the recent past
         SOURCE     brief F6 (lines 144-167), the table-by-table posture

  FWD-9  There is exactly one place user credentials live
         DONE WHEN  EXERCISED -- the old copy is gone and nothing noticed
         ACCEPT     the retired user table no longer exists, and no sign-in or
                    partner feature changed behaviour when it went
         SOURCE     brief F6: legacy `opal-users`, 12 rows, no live reader

  FWD-10  The keys that sign logins can be replaced without signing everyone out,
         and have been replaced at least once on purpose
         DONE WHEN  EXERCISED -- one deliberate rotation has happened and users
                    stayed signed in through it
         ACCEPT     the signing key has been swapped once, on purpose, and nobody
                    was logged out or locked out by the swap
         SOURCE     brief F7 (lines 169-177): keypair from 2026-04-06, no rotation

  FWD-11  Deleting a user ends their sessions
         DONE WHEN  EXERCISED -- a deleted account has been re-created on the
                    same email and the old session did not come back
         ACCEPT     an account that was deleted cannot be brought back to life on
                    the same email address still carrying its old sign-in
         SOURCE     brief F7, the refresh token bound to email (finding F-10)

  FWD-12  The gateway records who called it, and its shared machine keys expire
         DONE WHEN  APPLIED -- request logging is on and every long-lived shared
                    key has an expiry
         ACCEPT     every request to the gateway is in a record someone can read
                    later, and no shared key older than an agreed age still works
         SOURCE     brief WS2 gateway (lines 199-217): access logs off; static
                    capability bearers for /otp and /ms

  FWD-13  The marketing website has a front door that stops common attacks before
         WordPress sees them
         DONE WHEN  EXERCISED -- a known-bad request has been sent to the site and
                    refused before WordPress handled it, and the site still loads
                    normally for visitors
         ACCEPT     a request that matches a well-known attack pattern never
                    reaches WordPress, and a visitor cannot tell anything changed
         SOURCE     brief WS2 website (lines 219-235); NOTE this reverses the
                    original build spec's "NO CloudFront" line -- see Rulings

  FWD-14  An address that keeps hammering our doors is blocked automatically,
         without waiting for a person
         DONE WHEN  EXERCISED -- a staged burst from a test address has been
                    blocked with nobody acting, and a normal partner office
                    signing in at the same time was not
         ACCEPT     an address that keeps pushing on a door is refused on its
                    next attempt without anyone having done anything -- and an
                    office full of people signing in normally is never caught
         SOURCE     Andrew-direct 2026-09-02: "anyone trying to bust down our door
                    ... get blocked"; "preferable to just block their IP on a
                    trigger rather than wait for a human"
         BOUND BY   7.6 C-1, C-2, C-3, C-4, C-5, C-7, C-12 (ratified 18:2xZ)

  FWD-15  Every automatic block sends Andrew one email with the case
         DONE WHEN  EXERCISED -- a real block has produced exactly one email that
                    he received and could act on
         ACCEPT     when an address is blocked, andrew@opalinvest.com receives ONE
                    message naming the address, what it did, and where the case
                    file is -- and never receives one message per request
         SOURCE     Andrew-direct 2026-09-02: "trigger an email to me at
                    andrew@opalinvest.com"
         BOUND BY   7.6 C-6 (one per address per incident; the digest is a FILE)

  FWD-16  There is a list of blocked and watched addresses, and a case file
         for each
         DONE WHEN  APPLIED -- the list and the files exist and are being written
         ACCEPT     a person can open the list, see why each address is on it and
                    since when, and open its case file to read the evidence
         SOURCE     Andrew-direct 2026-09-02: "listed in there with relevant files
                    on the case stored in said bucket in relevant path structure"
         BOUND BY   7.6 C-2, C-8, C-9, C-11

  FWD-17  A blocked address can be unblocked by a person, and blocks nobody
         renews lapse on their own
         DONE WHEN  EXERCISED -- an authorised person has removed a block and the
                    address reached us again within minutes; a block left alone
                    has expired by itself
         ACCEPT     an authorised person lifts a block and the address can reach us
                    again within minutes; a block nobody renews lapses by itself
         SOURCE     Andrew-direct 2026-09-02: "means to unblock IP"
         BOUND BY   7.6 C-2, C-5, C-11

  FWD-18  The security evidence lives in one place, kept safe and organised
         DONE WHEN  APPLIED -- the store exists with its rules switched on
         ACCEPT     every case, log extract and allowlist is in one place under a
                    predictable path, encrypted, and cannot be quietly altered or
                    deleted
         SOURCE     Andrew-direct 2026-09-02: "an opal-data-security bucket ...
                    relevant path structure"
         BOUND BY   7.6 C-8, C-10
```

**Provenance (Step F5):** brief `docs/security/PLATFORM_ATTACK_SURFACE_ASSESSMENT_20260902.md` @a9a47f65a1, read in full; every outcome traces to a brief section named on its SOURCE line. **NOT READ:** the D12 task-order store, `org/projects/*.json`, `directives-check`, and the sibling projects' decomps -- by design; Phase 0 reads the brief and nothing else. Outcomes FWD-1..18 are RATIFIED (FWD-1..13 and the addition of FWD-14..18 at ~17:5xZ; section 7 at ~18:2xZ) -- a scope-change re-entry against any of them is a change against a RATIFIED outcome. (This line read UNRATIFIED at @7a51451d69 after the 17:5xZ word; corrected here.)

## 1. The arc

It starts with one open door and one blindfold. The portfolio service can be reached at its own address with no login at all, and nothing in the estate would tell anyone if someone walked through. The first movement closes the door where it is widest (FWD-1) and then makes the closing mechanical for every service at once, by giving the portal a secret handshake that back-door requests cannot fake (FWD-2, which also retires FWD-3's cost exposure and FWD-4's bypass). The second movement takes the blindfold off: keep what the front door refuses (FWD-5), tell a person when the login page is under pressure (FWD-4), and stop the common attacks before our code runs (FWD-6). The third movement hardens what a successful attacker would reach next -- the throttle's failure direction (FWD-7), the identity tables (FWD-8, FWD-9), and the keys and sessions (FWD-10, FWD-11). The last movement carries the same standard to the two servers outside the portal (FWD-12, FWD-13). A fifth movement, added on ratification, closes the loop the third one opened: what the front door refuses is not just logged but acted on -- the address is blocked at machine speed, the case is filed, and one email goes to Andrew (FWD-14 to FWD-18). It ends when every front door refuses what it should, someone is watching, the watchers act without being asked, and the things worth stealing are harder to reach than the doors were.

## 2. Purpose -- what DONE means

Anyone who is not signed in gets nothing from any address we operate except the public marketing site and the data we publish on purpose; anyone who is signed in cannot reach past their own firm; when either boundary is pushed on, a named person finds out and the evidence is still there a week later; and the tables and keys behind sign-in cannot be lost, deleted or quietly kept alive by mistake.

## 3. Territory -- what this owns, and what it only relies on

**Owns (added on ratification):** the `opal-data-security` evidence bucket, the `opal-suspicious-addresses` table, the WAF block IP sets on both ACLs, the sentinel that writes them, the unblock path, and (v0.5) **the project's customer-managed KMS key `alias/opal-security`** that the bucket and the table encrypt with, and (v0.6) **the `opal-security-admin` role** -- the human-side reader/writer of the evidence store, the principal of the unblock CLI, and the human principal in the key policy, and (v0.7) **the access-logs target `opal-data-security-access-logs`** that the evidence store's server access logs deliver into.

**Owns:** authentication and origin enforcement AT the API gateways (both the HTTP API and the portfolio REST API); the CloudFront and regional WAF rule sets; WAF/CloudFront/ALB logging and the login-abuse alarms; the login throttle's failure direction; protection settings on the identity and partner-role tables and the retirement of the legacy user table; the JWT signing-key lifecycle and the refresh-token binding; the gateway's request logging and shared-key expiry; the website's edge protection.

**Relies on, does not own:** `PLATFORM_OPS_USERMGMT` (MFA, account lifecycle, user-management UX -- the sibling that owns *who* a user is); `D12_PHONE_OTP_ALL_AWS` (the SMS factor and its provisioning gate G-7); the `portal-auth` Terraform module and the auth-handler Lambda (AE lane, `0.7.0_AE_CloudOps`); the portal repo (DT/DE lanes); the website box's on-box hardening (`infra/aws/ec2/website/`, already built). Any change this project makes inside those is made through their owners' lanes.

**Explicitly not re-opened:** `PORTAL_AUTHHARD` (closed 2026-08-25 on membership); its throttle design is the starting point of FWD-7, not something to replace.

## 4. Acceptance properties

1. Every method on every API gateway either requires a verified login or is on a written list of deliberately public reads -- and that list is short enough to read aloud.
2. A request carrying a valid login is still refused when it did not arrive through the portal's front door.
3. A public read can never trigger paid computation on our behalf.
4. A burst of blocked sign-ins reaches a named person; the blocked requests themselves are retrievable a week later.
5. The front-door protections have been observed in watch-only mode before they were allowed to refuse anything.
6. The login throttle, deprived of its records, slows sign-in rather than removing the limit.
7. No table holding a login or a partner's role can be deleted without a deliberate second step, and each can be restored to any recent moment.
8. There is one user table; the legacy copy is gone and its permissions with it.
9. The login signing key has been rotated once on purpose with no user logged out.
10. A deleted account cannot resurrect its old session on the same email.
11. The gateway logs every request and no shared key outlives its agreed age.
12. A known-bad request to the marketing site is refused before WordPress handles it, with no visible change for visitors.
13. An address that trips the door twice in an hour is refused on its third attempt with no human in the loop -- and no partner office is ever refused for signing in normally.
14. A block produces exactly one email to Andrew, with the case; repeats from the same address within a day produce none.
15. Every blocked or watched address has a row saying why and since when, and a case file under a predictable path.
16. An authorised person can lift a block and see it lifted within minutes; an unrenewed block lapses on its own.
17. The evidence store is encrypted, versioned, refuses insecure transport, and its objects cannot be silently overwritten.

Each is disputable: a reader can name the address, the request, the table or the key that fails it.

## 5. Out of scope

- New authentication factors, SSO, or any identity provider change -- there is no Cognito here and never has been (Andrew-direct 2026-09-02), and this project does not introduce one.
- User-management UX, onboarding, partner-admin delegation -- `PLATFORM_OPS_USERMGMT`.
- SMS delivery and its provisioning -- `D12_PHONE_OTP_ALL_AWS`.
- Re-platforming the marketing site (RDS, containers, a different CMS). FWD-13 puts a front door in front of the existing box; it does not move the box.
- Any monitor, alarm, log destination or managed-rule group NOT named in an outcome above. The standing moratorium holds: each of FWD-4, FWD-5, FWD-6, FWD-12 and -- added 2026-09-02 by his explicit word -- FWD-14/15 (the sentinel and its email to andrew@opalinvest.com) is a named exception; anything beyond them needs its own word. No other recipient, channel or cadence is implied. The 18:2xZ ratification of section 7 adds NONE: the daily digest is a FILE in the evidence store (C-6); a digest EMAIL is a carried option, not an authorization.
- Penetration testing against production by the fabric. Every EXERCISED bar above is met by a read-only or self-targeted probe under Andrew's word, never by an unannounced attack on live data.

## 6. Rulings that BIND

- **2026-09-02, Andrew-direct at the CTO~Z terminal:** *"I agree with your assessment, what I would like you to do now is /endpoint --forward this brief and let's render it into an actionable PRD, the registered project for which will be attached on the D12 Directive."* -- commissions this project and places it under D12.
- **2026-09-02, Andrew-direct:** *"We do not use Cognito, never have. Agents tend to make that claim for some reason."* -- no outcome, TO or docstring may assert a Cognito control; the 25 source files carrying the word are to be corrected, not built on.
- **2026-08-31 @efcfa8cc5b, Andrew-direct:** D12 is placed on SITE-Z. This project inherits that placement; its executing seats are `~Z` seats.
- **2026-09-02, Andrew-direct ("all recs approved", CALL 4):** an Andrew-directed non-DT running a portal promote uses the audited `# never-override:` on the push; the gate is not widened for it. Any portal-repo change this project makes rides that rule.
- **CLAUDE.md standing moratorium (alerts/monitors):** honoured as scoped in section 5 -- the four monitoring outcomes are named exceptions under the commissioning word; nothing else is.
- **FWD-13 reverses one line of the website's original spec** (*"NO RDS / Fargate / Lightsail / CloudFront"*, Andrew-direct 2026-07-13). It is included because the assessment names the website as the largest unmanaged surface and Andrew agreed with the assessment; **it is flagged here so that the decomp treats the edge choice (CloudFront+WAF vs Cloudflare) as a decision to put to him, not a settled one.** **RULED 2026-09-03 ~08:4xZ, Andrew-direct at the 1.0.0_SA_CTO~Z terminal, verbatim *"Recs approved"* on /open-calls CALL 1 (REC (a)): CloudFront + WAF managed rules in front of the box -- the same rule groups, logging path and IP sets as S4 / S5 / S18, so one BLOCK row blocks at the site and the portal from one table; the 2026-07-13 line is reversed for the website's edge by his word; the box does not move (section 5); the S13 task order is no longer held.**
- **The exercise bars are read-only or self-targeted.** FWD-1 and FWD-2 are proven by a refused request, never by a successful write to production data.
- **2026-09-02 ~17:5xZ, Andrew-direct:** FWD-1..13 RATIFIED and FWD-14..18 ADDED (quoted in full at the head of the ENDPOINT section): an email to andrew@opalinvest.com on WAF-detected suspicious activity, a triggerable automatic IP block, a case file per subject in an `opal-data-security` bucket, an `opal-suspicious-addresses` table, a means to unblock, and a stated preference for **blocking on trigger over waiting for a human**. The email is an explicit moratorium exception by his word; nothing beyond it is.
- **2026-09-02 ~18:2xZ, Andrew-direct:** *"I like all of your ideas and want them worked into the PRD"* -- section 7 is RATIFIED as design, not recommendation. Binding consequences: FWD-2 precedes FWD-14 as a SEQUENCING RULING (no longer sequencing input); the table is the single source of truth and the WAF IP sets are derived from it; a persistent block needs more than one rate trip, never overrides the partner-egress ALLOW list, and always carries an expiry; one email per address per incident. The binding form is section 7.6; the items 7.6 marks as CARRIED (digest email, Object Lock, final thresholds) are NOT covered by this word.
- **2026-09-02 ~18:4xZ, Andrew-direct:** *"your project should be registered canonically, id call it NFRA_SECURITY202609"* -- the project code is `NFRA_SECURITY202609` (macro `NFRA`, the code's own prefix), registered canonically: project JSON + REGISTRY row + D12 membership + this PRD under the canonical filename. Former code `D12_PLATFORM_FORTIFY` is recorded on the row. The REGISTRY's `{MACRO}_{6CHAR}` format line is PREFERRED, NOT ENFORCED: the register owner measured 162 of 352 codes off the six-character form (five already 14 characters) and amended the header @366b145db7 -- no override existed to record.

- **2026-09-03 ~06:5xZ, Andrew-direct at the 1.0.0_SA_CTO~Z terminal:** *"Call it NFRA_OPSEC202609"* -- the project code is `NFRA_OPSEC202609` (macro `NFRA`, name `OPSEC202609`, 11 characters); `NFRA_SECURITY202609` was refused by the project-tree grammar (`org/standards/PROJECT_TREE.contract.json` R1, name 14 characters against `^[A-Z]{4}_[A-Z0-9]{4,12}$`). Every `FWD-n`, `C-n`, the D12 membership and the fabric are unchanged. Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260903_065xZ_CTOZ_CALL_IT_NFRA_OPSEC202609.md`. The tree entry is @32daebf403.

- **2026-09-03 ~08:1xZ, CTO ruling at L4 (`1.0.0_SA_CTO~Z`, the L4 owner; disclosed to Andrew at this terminal the same turn, reversible by one word):** 7.3, C-8 and C-9 said "the estate CMK". Measured by `0.7.0_AE_CloudOps~S` (row NFRA_OPSEC202609-Z-S3, BLOCKING; `describe-key` with a KeyManager=CUSTOMER positive control across all 11 keys): `86cc6c40-...` is the **AWS-managed** DynamoDB service key (`alias/aws/dynamodb`, KeyManager=AWS) -- an S3 bucket cannot use it, its policy cannot be scoped, and the account holds NO general-purpose customer-managed key. The brief F6 misread its yearly rotation as a CMK; the PRD inherited the word. The PROPERTY both constraints were ratified for (a scoped key policy; "the best-protected table in the account"; "an altered case file leaves the original") is delivered only by a customer-managed key. **Ruling: ONE project customer-managed key, `alias/opal-security` (Terraform, rotation ON, key policy scoping the sentinel, reconciler and `opal-security-admin` roles (C-14)), used by BOTH resources** -- the minimal change that delivers the ratified property; the intent of the 18:2xZ word is unchanged, its referent is corrected. Now C-13 and manifest row S25. Round 1 builds the table on the AWS-managed key and the bucket on SSE-S3 as INTERIM (the COO's operating note); the key flip is a round-2 task order, in place. Cost: one KMS key.

- **2026-09-03 ~08:2xZ, CTO ruling at L4, the IDENTITY half of the same item (`1.0.0_SA_CTO~Z`; disclosed to Andrew at this terminal the same turn):** C-8 named "the CTO-admin role" as a principal of the evidence store's bucket policy. Measured by `0.7.0_AE_CloudOps~S` (row NFRA_OPSEC202609-Z-S4, BLOCKING): 0 of 216 IAM roles match admin/cto/terraform (positive control lambda = 55); the Terraform applier is `user/Andrew_Berman`; a deny-outside-list statement naming an absent role would brick the bucket at creation. **Ruling on the MECHANISM: the referent is ONE Terraform-declared role, `opal-security-admin`, in the project's own module -- the human-side reader/writer of the evidence store (C-8), the human principal in the key policy (C-13) and the principal the unblock CLI runs as (C-11); the bucket policy's deny-outside-list statement lands with the task orders that create the sentinel, reconciler and this role (round 2), exactly as the COO deferred it. The MEMBERSHIP -- which human principals may assume the role -- is who may read security evidence, and that is Andrew's word: card OP-x-6.** The role is not created before his word; round 1 does not wait on it. New C-14, manifest row S26. **RULED 2026-09-03 ~08:4xZ, Andrew-direct at this terminal, verbatim *"Recs approved"* on /open-calls CALL 2 (REC (a)): Andrew alone for round 2 -- the trust policy names his own IAM identity and nobody else; a second operator is a later task order of this project.**

- **2026-09-03 ~08:3xZ, CTO ruling at L4, the third referent of C-8 (`1.0.0_SA_CTO~Z`; disclosed to Andrew at this terminal the same turn):** C-8 said the evidence store's server access logs go "to the CloudTrail bucket". Measured by `0.7.0_AE_CloudOps~S` BEFORE applying (row NFRA_OPSEC202609-Z-S5, BLOCKING): `opal-cloudtrail-logs-313476888478`'s policy has exactly two statements, both Principal `cloudtrail.amazonaws.com`; no `logging.s3.amazonaws.com` grant, no LogDelivery ACL -- S3 server access logging needs one of those ON THE TARGET, so the limb could not receive, and the worse failure is the silent one: a CONFIGURED logging setting with no object ever delivered, which a `get-bucket-logging` read would PASS. A sweep of all 31 buckets found none with access logging enabled (an absence, not a control). **Ruling: the target is a PROJECT-OWNED access-logs bucket, `opal-data-security-access-logs`, declared in the project's own module (private, SSE-S3, versioning, lifecycle, a policy granting `logging.s3.amazonaws.com` with SourceAccount + SourceArn conditions) -- the audit-log bucket is shared infrastructure and is NOT widened for another module's convenience (never-widen; the scoped-grant alternative is rejected for that reason). The read that grades the limb is a DELIVERED object under the target prefix, never the configuration.** New C-15, manifest row S27. Round 1 applies the other seven resources now; the logging limb lands in round 2 beside the key flip. This is the third referent in one constraint asserted and never read until a worker re-grounded it (key, roles, target); the round-2 cut runs one live read per named referent before a task order commits (the COO's banked rule).

## 7. The auto-block framework -- RATIFIED design (2026-09-02 ~18:2xZ)

**Status:** written ~17:5xZ as the CTO assessment Andrew asked for; ratified whole at ~18:2xZ (*"I like all of your ideas and want them worked into the PRD"*). 7.1-7.5 stay as written because they are the REASONING; 7.6 is the BINDING form the decomp cites.

**Andrew's framework, restated:** WAF detects -> email Andrew -> block the IP on a trigger -> keep a case file in an `opal-data-security` bucket -> list the IP in `opal-suspicious-addresses` -> provide an unblock. **Verdict: relevant and mostly well designed.** The shape is right; three refinements make it safe to run unattended, and one dependency has to land first or the framework is blind to the very doors that are open today.

### 7.1 The dependency that comes first

The sentinel sees only what the WAF sees. Today the two API gateways answer at their own `execute-api` addresses with **no WAF in front** (brief F1/F2, endpoint FWD-2). An attacker who has found a raw endpoint never trips a WAF rule and is never blocked, however good the sentinel is. **FWD-2 (the origin secret) is therefore the first atom of this project, and FWD-14 is built on top of it, not beside it.** Until FWD-2 lands, the auto-block covers CloudFront and the gateway ALB and nothing else -- and that must be stated in the case-file format so a "no incidents" week is not read as a quiet week.

### 7.2 Three refinements, and why each one is load-bearing

**(a) The table is the source of truth; the WAF block list is derived from it.** If the Lambda writes the WAF IP set directly and the table second, the two drift the first time a write fails half-way, and "unblock" becomes a two-place edit. Instead: every block, watch, allow and expiry is a row in `opal-suspicious-addresses`; a **DynamoDB Stream** drives a small reconciler that mirrors `status=BLOCKED` rows into the WAF IP set and removes everything else. Unblock is then a one-field change (`status -> ALLOW`), expiry is the table's own TTL (the stream's REMOVE event unblocks), and the audit trail is the table's history. One writer, one truth, and "means to unblock" falls out for free.

**(b) Tier the block, and never auto-block a partner office.** The existing WAF rate rules already block -- *transiently*, for as long as the rate stays high, then release. A persistent IP-set block turns a five-minute inconvenience into "until a human notices". That is exactly the cost the ask is trying to avoid, pointed the other way: **a partner firm's whole office typically leaves the internet through ONE address**, so one over-eager threshold locks out a firm, which is Stephen's situation at the scale of a company. So: the persistent block requires a STRONGER signal than one rate-rule trip -- repeated trips across windows, a managed-rule hit (IP reputation, known-bad inputs), or a credential-stuffing signature (many distinct accounts from one address on `/auth/login`); the table carries an **ALLOW list of known partner egress addresses** that the sentinel checks before every block and that a block can never override; and every automatic block carries an **expiry** (hours to days, escalating on repeat) so a wrong block heals itself even if no one reads the email. Human-pinned permanent blocks are a separate, deliberate status.

**(c) One email per incident, not per event -- and a daily digest.** The CloudFront rate rule at 2,000 requests per five minutes will trip on ordinary scanners most days. An email per WAF block is a channel Andrew will mute within a week, which is the failure this whole outcome exists to prevent. The sentinel emails **once per address per incident** (first block, and any escalation), suppresses repeats for 24 h, and writes a **daily digest** (counts, top addresses, anything auto-expired) to the bucket and, if wanted, as one morning email. Plain text, the case path in the body, no links to click.

### 7.3 Recommended architecture (all serverless, all Terraform, no polling)

```
  CloudFront web ACL  ---+        both ACLs gain TWO things:
  gateway regional ACL --+          rule 0  IPSetReference opal-blocked-ips-{scope} -> BLOCK  (persistent)
                         |          logging -> CloudWatch Logs  aws-waf-logs-opal-{scope}
                         v
  CloudWatch Logs subscription filter (action = BLOCK, or any managed-rule label, or /auth/login POSTs)
                         |  push, seconds -- no schedule, no polling
                         v
  Lambda  opal-sentinel  (reserved concurrency 1: a single writer, so no lock races on the IP set)
     1 parse the WAF record: address, rule, action, path, country, time
     2 score: per-address counter with TTL (in the same table), which rule, how many windows
     3 policy: ALLOW-listed?  -> record WATCH only, never block
               threshold met? -> BLOCK      else -> WATCH
     4 on BLOCK:  PutItem opal-suspicious-addresses (status BLOCKED, why, since, expires_at, case_id)
                  write case file  s3://opal-data-security/cases/{yyyy}/{mm}/{dd}/{addr}/{case_id}/
                                     summary.json  waf-samples.jsonl  timeline.md
                  SES email -> andrew@opalinvest.com  (one per address per 24 h)
     5 on WATCH:  UpdateItem hits/last_seen; append to the open case; no email
                         |
                         v
  DynamoDB Stream (NEW_AND_OLD_IMAGES) -> Lambda opal-ipset-reconciler
     status BLOCKED (insert/modify) -> UpdateIPSet add    /32 or /64
     status ALLOW | EXPIRED | TTL remove -> UpdateIPSet remove
     (the table is truth; the IP set is a projection of it; a drift is repaired on the next event
      and by a once-daily full reconcile)

  UNBLOCK  .tools/opal-ipblock allow <addr> --reason "..."   (flips status; audited)
           later, FWD-16's portal Admin page: Security -> Blocked addresses -> Unblock
```

**`opal-suspicious-addresses`** -- pk `address` (normalized CIDR, `/32` v4, `/64` v6); `status` in {BLOCKED, WATCH, ALLOW, EXPIRED}; `first_seen`, `last_seen`, `hits`, `rules` (set), `sources` (set: cloudfront-waf | gateway-waf | auth-log), `paths_top` (list), `case_ids` (list), `blocked_at`, `blocked_by` (auto | serial), `expires_at` (TTL), `unblocked_by/at`, `notes`. GSI `status-index` for the admin listing. Encrypted with the project CMK `alias/opal-security` (v0.5; was "the estate CMK", which is the AWS-managed DynamoDB key), PITR ON, deletion protection ON -- the table that decides who is locked out must itself be the best-protected table in the account.

**TWO BUCKETS, v0.9 (RULED 19801).** The evidence store and the raw log destination are separate buckets because S3 default encryption is per-BUCKET: the store is written only by this project's three roles and takes the project CMK; the destination is written by AWS service principals and takes SSE-S3. Splitting them is the branch 7.3 and row S5 already name, not a new one.

**`opal-security-evidence`** (NEW, v0.9 -- the evidence store C-8 specifies; `opal-data-security` held this role through v0.8) -- private; SSE-KMS on the project CMK `alias/opal-security` (v0.5, C-13); **versioning ON** (an altered case file leaves the original); Object Lock in governance mode on `cases/` if evidence integrity is wanted (cheap, reversible by an admin); bucket policy denies non-TLS and any principal outside the sentinel / reconciler / `opal-security-admin` (C-14) roles -- **and NO service principal writes here, which is what makes C-13's three-role key policy exactly right**; server access logging to the project-owned target `opal-data-security-access-logs` (v0.7, C-15); lifecycle: `cases/`, `reports/`, `allowlists/` retained. **It holds the LOG EXTRACTS a case cites** (`waf-samples.jsonl` under `cases/`), which FWD-18's ACCEPT names at :207 -- what moved out is the raw delivery stream, never the evidence derived from it. Paths:

```
  cases/{yyyy}/{mm}/{dd}/{address-safe}/{case_id}/summary.json | waf-samples.jsonl | timeline.md | actions.jsonl
  reports/daily/{yyyy}-{mm}-{dd}.md
  allowlists/partner-egress.json          (versioned; the sentinel reads it at cold start)
```

**`opal-data-security`** (EXISTING and LIVE -- FWD-5's log destination from v0.9; it was the evidence store's name through v0.8 and KEEPS the name, because the alternative moves a delivery path that is running) -- private; **SSE-S3 (`AES256`), NOT the project key**, for the reason C-15 already recorded on the sibling target at ~08:3xZ: a KMS destination needs a log-delivery grant on the key, and C-13 grants none; versioning ON; bucket policy grants `delivery.logs.amazonaws.com` (scoped to `waf-logs/cloudfront-access/*`) and `logdelivery.elasticloadbalancing.amazonaws.com` (scoped to `waf-logs/alb-opal-gateway/*`), each with SourceAccount and SourceArn conditions, and denies non-TLS; lifecycle: `waf-logs/` to Glacier at 90 d, expire at 400 d. Paths, naming what ACTUALLY delivers (the v0.9 correction of the `{scope}` grammar, which described Firehose-raw WAF logs only):

```
  waf-logs/cloudfront-access/{...}/       (CloudFront standard access logs -- LIVE, delivery.logs.amazonaws.com)
  waf-logs/alb-opal-gateway/AWSLogs/{...} (ALB access logs -- LIVE, logdelivery.elasticloadbalancing.amazonaws.com)
  waf-logs/{scope}/{yyyy}/{mm}/{dd}/      (Firehose raw WAF, ONLY if S3 delivery is chosen over CloudWatch Logs;
                                           row S5 keeps that choice open and CloudWatch Logs is the live branch)
```

**Thresholds (starting values, to be tuned against the first month of WATCH rows, never invented as final):** BLOCK on any AmazonIpReputationList or KnownBadInputs match; BLOCK on the rate rule tripping in 2 separate 5-minute windows within 1 h; BLOCK on `/auth/login` POSTs from one address exceeding N in 5 min where N sits well above one office's morning (the WATCH rows will say what that is); everything else WATCH. Expiry 24 h on a first block, 7 d on a repeat, human-pinned for permanent.

### 7.4 Build ladder

AWS ships this pattern as the *WAF Security Automations* CloudFormation solution (log parser -> IP set, reputation lists, honeypot). It is the right pattern and the wrong packaging for this estate (CloudFormation, opinionated, heavy). The recommendation is **the same pattern in ~2 small Lambdas under the estate's Terraform, IAM and commit-gate conventions**, reusing what already exists: the WAF ACLs, the SES identity the auth handler already sends from, the CMK, CloudTrail's bucket for access logs. Estimated surface: two Lambdas, one table, one bucket, two IP sets, two logging configs, one subscription filter per scope, one CLI tool. No new vendor, no egress.

### 7.5 What this does NOT solve, said plainly

IP blocking stops opportunists and scanners, which are most of what hits a login page. It does not stop a patient attacker rotating addresses, and it should not be mistaken for the fix for F1/F2 -- those are closed by requiring a login and a front-door secret at every gateway, which is why they sit ahead of this in the arc.

### 7.6 Binding constraints for the decomp -- the ratified form of 7.1-7.5

Ratified 2026-09-02 ~18:2xZ (Andrew-direct, quoted in section 6). Each row names the outcomes it binds and the act that would violate it, so a step-10 reader can grade an atom against it without re-reading the prose above. `C-n` ids are permanent; a retired constraint leaves its number vacant, same contract as `FWD-n`.

```
  C-1  SEQUENCE   FWD-2 lands before FWD-14 is EXERCISED. Until then every case file
                  and daily report states its coverage bound: CloudFront + gateway ALB
                  only; the raw execute-api endpoints are unseen.
       binds      FWD-14            violated by: a FWD-14 exercise dated before FWD-2's

  C-2  ONE TRUTH  opal-suspicious-addresses is the ONLY record anything writes to.
                  The WAF IP sets are projections of it, maintained by a DynamoDB
                  Stream consumer plus a once-daily full reconcile. Nothing else
                  calls UpdateIPSet.
       binds      FWD-14/16/17      violated by: an UpdateIPSet outside the reconciler

  C-3  SIGNAL     A persistent block needs MORE than one rate-rule trip: repeat trips
                  across windows, a managed-rule label (IP reputation, known-bad
                  inputs), or a credential-stuffing signature (many distinct accounts
                  from one address on /auth/login). Thresholds are STARTING values,
                  tuned on at least one month of WATCH rows; none is final at build.
       binds      FWD-14            violated by: BLOCK on a single rate trip; a
                                    threshold presented as final without WATCH rows

  C-4  ALLOW      A partner-egress ALLOW list (allowlists/partner-egress.json,
                  versioned, mirrored as status=ALLOW rows) that an automatic block
                  can NEVER override. It is populated from MEASURED sign-in addresses
                  per firm BEFORE the sentinel is armed to BLOCK; arming with an
                  empty list is a violation, not a phase.
       binds      FWD-14            violated by: a BLOCK row on an ALLOW-listed
                                    address; arming BLOCK with 0 ALLOW rows

  C-5  EXPIRY     Every automatic block carries expires_at (24 h first, 7 d on
                  repeat) enforced by table TTL; the stream REMOVE event unblocks.
                  Permanent blocks are a distinct, human-pinned status, never automatic.
       binds      FWD-14/17         violated by: an auto BLOCK row with no expires_at

  C-6  ONE EMAIL  One email per address per incident to andrew@opalinvest.com (first
                  block and any escalation), 24 h suppression on repeats, plain text,
                  case path in the body, no links. The daily digest is a FILE under
                  reports/daily/ in the evidence store. A digest EMAIL is an OPTION
                  carried to Andrew -- not authorized by this ratification.
       binds      FWD-15            violated by: more than one email per address per
                                    24 h; any recipient other than the named address

  C-7  WRITER     The sentinel runs at reserved concurrency 1 (a single writer); the
                  reconciler is idempotent (re-applying the table yields the same set).
       binds      FWD-14/16         violated by: unreserved concurrency on the sentinel

  C-8  STORE      (v0.9) opal-security-evidence: private; SSE-KMS on the PROJECT CMK (C-13);
                  versioning ON; bucket policy denies non-TLS and any principal outside the
                  sentinel, reconciler and `opal-security-admin` roles (C-14) -- and NO service
                  principal writes here, which is what keeps C-13's three-role key policy exact;
                  server access logging to the project-owned target (C-15); cases/, reports/,
                  allowlists/ retained. Paths exactly as 7.3. Object Lock
                  (governance) on cases/ is an OPTION for the decomp to put to Andrew.
                  IT HOLDS THE LOG EXTRACTS A CASE CITES (waf-samples.jsonl under cases/),
                  which FWD-18's ACCEPT names: what left is the RAW DELIVERY STREAM only.
                  THROUGH v0.8 this constraint named opal-data-security and put the raw stream
                  in the same bucket; that bucket is written by TWO AWS service principals and
                  this same sentence denies every principal but three roles -- both true, and
                  impossible in one bucket (S3 default encryption is per-bucket). The raw stream
                  is FWD-5's artifact and stays in opal-data-security at SSE-S3 (C-16).
       binds      FWD-16/18         violated by: any listed property absent at
                                    APPLIED; a case written outside cases/{yyyy}/...;
                                    a log EXTRACT a case cites stored outside this bucket

  C-9  TABLE      opal-suspicious-addresses: schema as 7.3; encrypted with the PROJECT
                  CMK (C-13); PITR ON; deletion protection ON; GSI status-index.
       binds      FWD-16            violated by: any of the four properties absent

  C-10 BUILD      Two Lambdas (opal-sentinel, opal-ipset-reconciler), one table, one
                  bucket, two IP sets, WAF logging on both ACLs, one subscription
                  filter per scope, one CLI -- all under the estate's Terraform, IAM
                  and commit-gate conventions. No CloudFormation solution import, no
                  new vendor, no egress.
       binds      FWD-14..18        violated by: a CloudFormation stack; a third-party
                                    feed; a resource outside Terraform

  C-11 UNBLOCK    The first increment is an audited CLI (.tools/opal-ipblock allow
                  <addr> --reason "...") that flips the row; the stream does the
                  rest. The portal Admin page is a LATER increment of FWD-16/17,
                  never a precondition for either.
       binds      FWD-17            violated by: an unblock path that edits the IP set

  C-12 BOUND      This framework complements FWD-1/FWD-2; it does not replace them.
                  It stops opportunists and scanners, not a patient attacker rotating
                  addresses. No atom may cite FWD-14 as closing brief F1 or F2.
       binds      FWD-1/2/14        violated by: a closure of F1 or F2 resting on
                                    the sentinel

  C-13 KEY        (v0.5) ONE customer-managed KMS key for this project, alias
                  alias/opal-security, under Terraform, rotation ON, key policy
                  scoping the sentinel, reconciler and `opal-security-admin` roles (C-14); it is
                  the key C-8 and C-9 name. "The estate CMK" of v0.3 does not
                  exist: 86cc6c40-... is the AWS-managed DynamoDB key (KeyManager
                  AWS), unusable by S3 and unscopable. Round 1 may build on
                  SSE-S3 / the AWS-managed key as INTERIM with the KMS limb filed
                  UNCOMPUTABLE; the flip to this key is a round-2 task order.
       binds      FWD-16/18         violated by: SSE-S3 or the AWS-managed key at
                                    APPLIED on either resource at the close; a
                                    second key; a key outside Terraform

  C-14 IDENTITY   (v0.6) ONE Terraform-declared IAM role, opal-security-admin, is
                  the human-side principal of this project: the reader/writer
                  of opal-data-security outside the sentinel and reconciler
                  (C-8), the human principal in the key policy (C-13), and the
                  principal the unblock CLI runs as (C-11). Its TRUST policy
                  names ONE human principal for round 2 -- Andrew's own IAM
                  identity, the account's applier -- and nobody else (RULED
                  2026-09-03 ~08:4xZ, "Recs approved" on card OP-x-6); a second
                  operator is a later task order of this project. Until the role,
                  the sentinel and the reconciler exist, a bucket policy
                  carries the SecureTransport deny ONLY and the four public-
                  access blocks are the control (round 1 INTERIM, row Z-S4).
       binds      FWD-16/17/18      violated by: a bucket policy or key policy
                                    naming a principal that does not exist; an
                                    IAM user named in a security-evidence policy;
                                    the role assumable by a principal his word
                                    did not name

  C-15 LOGS-TARGET (v0.7; v0.9 -- the evidence store is now opal-security-evidence (C-8),
                  and this target follows IT, not the log destination)
                  The evidence store's S3 server access logs deliver to a
                  PROJECT-OWNED target, opal-data-security-access-logs, declared
                  in the project's own module: private; SSE-S3; versioning ON;
                  lifecycle; bucket policy granting logging.s3.amazonaws.com with
                  SourceAccount + SourceArn conditions. The shared audit-log
                  bucket opal-cloudtrail-logs-313476888478 is NOT a target and is
                  NOT widened. The limb is graded by a DELIVERED object under the
                  target prefix after one write to the evidence store, never by
                  get-bucket-logging.
       binds      FWD-18            violated by: a logging target outside the
                                    project's module; a grant added to the
                                    audit-log bucket; an acceptance read of the
                                    configuration instead of a delivered object
```

  C-16 LOG-DEST   (v0.9) opal-data-security is FWD-5's LOG DESTINATION and stays
                  SSE-S3 (AES256). It is NOT encrypted with the project CMK: the two
                  AWS service principals that deliver into it are absent from C-13's
                  key policy by design, so the flip would stop both live legs silently,
                  and the only in-key remedy is a grant C-13 does not carry. Same
                  reasoning C-15 already applied to the sibling access-logs target at
                  ~08:3xZ. Its policy grants delivery.logs.amazonaws.com and
                  logdelivery.elasticloadbalancing.amazonaws.com, each scoped to its own
                  prefix with SourceAccount + SourceArn, and denies non-TLS.
       binds      FWD-5             violated by: a default-encryption change to KMS on
                                    this bucket; a delivery leg pointed elsewhere
                                    without its own cell; a grant widened past the two
                                    named prefixes

**Carried to Andrew, NOT implied by this ratification (each needs its own word):** the morning digest email (C-6); Object Lock on `cases/` (C-8); the block thresholds, once a month of WATCH rows exists to set them from (C-3). Card OP-x-6 (the trust of `opal-security-admin`) and the FWD-13 edge choice were RULED 2026-09-03 ~08:4xZ ("Recs approved"): Andrew alone for round 2; CloudFront + WAF managed rules.

## 8. SURFACE MANIFEST (step 4 -> step 5) -- one row per ENGINE

**Contract:** the step-4 surface manifest as adopted @ecaa7c7dcb (ETFS_GUARDRAIL s.7 adoption ruling): `claim` is about the SURFACE ADDRESS and takes the five-value basis vocabulary `absent | unmeasured | held | inferred | measured` (`.tools/substrate-card-check.py` `BASIS_RANK`; every legal transition is a rank increase, and `verify` is the act that moves `absent`/`unmeasured`); `verb` is the contract enum `port | classify | wire | align | retire | verify`; `outcome` = `FWD-n`; `accept` = the section 4 property number; `depends_on` = row ids; `bound` = the constraint or ruling the cell may not cross.

**Provenance, read before citing any cell.** Every `measured` evidence cell below is the BRIEF's measurement -- `1.0.0_SA_CTO~Z`, APPLIED reads of live AWS at 2026-09-02 16:5xZ-17:2xZ plus source at working-tree HEAD that day, pinned `docs/briefs/PLATFORM_ATTACK_SURFACE_ASSESSMENT_20260902.md` @32daebf403 (bytes identical to @a9a47f65a1). **Nothing was re-measured on 2026-09-03**; the brief's `F<n>`/`WS2` line ranges are cited so the COO's L5 battery re-grounds each cell at its own vintage. `absent` rows are the section 7 design: nothing built. **The exercise bars are read-only or self-targeted (section 6).**

**Domain (postulate i):** the section 3 **OWNS** cell, nineteen items (v0.7) -- (1) authentication + origin enforcement at BOTH API gateways, (2) the CloudFront and regional WAF rule sets, (3) WAF/CloudFront/ALB logging, (4) the login-abuse alarms, (5) the login throttle's failure direction, (6) protection on the identity and partner-role tables, (7) the legacy user table's retirement, (8) the JWT signing-key lifecycle, (9) the refresh-token binding, (10) the gateway's request logging + shared-key expiry, (11) the website's edge protection, (12) `opal-data-security`, (13) `opal-suspicious-addresses`, (14) the WAF block IP sets on both ACLs, (15) the sentinel that writes them (with its reconciler), (16) the unblock path, (17) the project customer-managed KMS key, (18) the `opal-security-admin` role, (19) the access-logs target `opal-data-security-access-logs`. RELIES-ON items (`PLATFORM_OPS_USERMGMT`, `D12_PHONE_OTP_ALL_AWS`, the `portal-auth` module, the portal repo, the website box's on-box hardening) appear only in `depends_on` or `bound`, never as work rows.

| id | outcome | surface (engine) | claim | MEASURED-BY / evidence | lane | verb | depends_on | accept | bound |
|---|---|---|---|---|---|---|---|---|---|
| S1 | FWD-1, FWD-2 | REST API `opal-portal-api` (`f61h681z9g`, EDGE, stage `/prod`): 20 method-bearing resources, `get-authorizers` -> `[]`, no resource policy, `execute-api` endpoint enabled; writes include autosave PUT, export-and-submit POST, upload-urls GET, market-update POST x3 | measured | brief F1 :14-60 (APPLIED; two methods read `NONE`, the empty authorizer set covers the denominator of 20) | `0.7.0_AE_CloudOps` | wire | S3 | 1, 2 | a Lambda authorizer on EVERY method (denominator 20, printed in the proof) AND the S3 origin secret required by it; the autosave docstring's Cognito claim (`portfolio_optimization_autosave_put/lambda_function.py:15`) is corrected in the same TO -- **no Cognito, never** (section 6). Exercise = a refused GET/OPTIONS on a read-only resource at the raw address, under Andrew's word; never a write |
| S2 | FWD-2, FWD-3 | HTTP API `opal-portal-data-proxy-api` (`7k3ed8px20`): `portal-jwt-authorizer` on 60 of 72 routes; 12 `NONE` = `OPTIONS` x2 + `ANY /auth/{proxy+}` (pre-auth by design) + 9 data routes under `/v1/*` and `/metadata/yang`; `POST /v1/sentiment/keyword-intelligence` falls back to live OpenAI on a cache miss (`portal_data_proxy/lambda_function.py:1440-1460`) | measured | brief F2 :65-83 (APPLIED route table + source) | `0.7.0_AE_CloudOps` | wire | S3 | 2, 3 | the authorizer on the 9 data routes (the CloudFront path already presents a JWT; nothing legitimate breaks) + the S3 origin secret on `/auth/*` (which stays `NONE` at the API by design). FWD-3 is closed by the authorizer, never by deleting the fallback |
| S3 | FWD-2 | the ORIGIN SECRET: a CloudFront custom origin header carrying a Secrets Manager value, required by BOTH authorizers -- replacing the constant `X-Origin-Verify: "cloudfront"` set at `auth-validator-edge/index.mjs:392` and checked by nothing (the header name appears in no other first-party file) | absent | brief F1 remediation + estate-wide search (the one file); nothing built | `0.7.0_AE_CloudOps` | wire | -- | 2 | ONE secret, two consumers (S1, S2); rotation with a dual-value overlap so a rotation never 401s the portal. **C-1: this row is exercised BEFORE FWD-14 is exercised** -- the sentinel is blind to the raw endpoints until it lands (7.1) |
| S4 | FWD-5, FWD-6 | CloudFront web ACL `opal-cloudfront-protection` on `EVTSA9VEHNZVH`: default Allow; `RateLimitRule` 2000/5 min/IP; `AuthLoginRateLimit` 100/5 min/IP on the auth POST paths; NO managed rule groups; sampled requests only (3 h). Sibling: regional `opal-gateway-waf` carries IP-reputation ENFORCED and Common + KnownBadInputs in COUNT | measured | brief F5 :132-142 (APPLIED == DESIRED) | `0.7.0_AE_CloudOps` | align | S5 | 4, 5 | add `AWSManagedRulesAmazonIpReputationList` (block) + `CommonRuleSet` + `KnownBadInputsRuleSet` in COUNT first; flip to BLOCK only after the watch-only soak (FWD-6 DONE WHEN, property 5); graduate the gateway ACL's two COUNT groups on the same evidence; rule 0 `IPSetReference` from S18 (C-2). BotControl is NOT named in any outcome and is not authorized here |
| S5 | FWD-5 | WAF logging on BOTH ACLs (CloudWatch Logs `aws-waf-logs-opal-{scope}`, or Firehose into S17 `waf-logs/`); CloudFront standard access logs; ALB access logs -- all OFF today | absent | brief F3 :88-111 (APPLIED: WAF logging not configured; CloudFront + ALB logging off; CloudTrail multi-region ON is the one durable audit source) | `0.7.0_AE_CloudOps` | wire | S17 | 4 | moratorium exception FWD-5 by the commissioning word; ACCEPT = the blocked requests are retrievable a WEEK later (retention >= 7 d is the bar, not the default). The S14 subscription filter hangs off this row's log group |
| S6 | FWD-4 | login-abuse alarm: `AuthLoginRateLimit` `BlockedRequests > 0` + a metric filter on the auth handler's `auth_throttled` log line -> ONE named person | absent | brief F3 (APPLIED alarm census: `FIRMSEP-*` x5 + 2 Lambda-throttle; NONE on WAF blocks, `auth_throttled`, failed logins, `mfa_code_rejected`) | `0.7.0_AE_CloudOps` | wire | S5 | 4 | moratorium exception FWD-4 ONLY: two alarms, one recipient named in the task order, no cadence, no dashboard. GuardDuty / Security Hub / Config are named in NO outcome and are NOT authorized by this PRD (section 5) |
| S7 | FWD-7 | the login throttle `auth-handler/src/throttle.ts:112-114`: per-account progressive cooldown, `return; // fail-open` when the `opal-portal-auth-throttle` read fails; IP-blind by design (`index.ts` reads no client address) | measured | brief F4 :113-130 (source) | `0.7.0_AE_CloudOps` | align | -- | 6 | fail-CLOSED short-circuit (429 when the throttle store is unreachable); the per-account design and the no-hard-lockout property are KEPT (a hard lockout lets an attacker lock out a known user). Exercise = the table made unreachable on purpose in a staged path, sign-in observed to slow, never to open |
| S8 | FWD-8 | identity + RBAC tables: `opal-users-v2` (CMK, PITR ON, deletion protection OFF); `opal-partner-49financial` / `-cottonwood` / `-inflection` (CMK, PITR OFF, DP OFF); `opal-partner-demo` (AWS-owned key, DP ON -- inverted); `opal-portal-auth-mfa` / `-throttle` (ephemeral, TTL-reaped, fine) | measured | brief F6 :144-167 table (APPLIED) | `0.7.0_AE_CloudOps` | align | -- | 7 | PITR ON + deletion protection ON on the four real tables; demo aligned to the CMK; the MFA/throttle tables untouched. Hashing `email` in the partner tables is a brief suggestion, NOT an outcome -- record it as a finding row if a cell wants it, do not build it here |
| S9 | FWD-9 | legacy `opal-users` (12 rows, CMK, PITR ON; NO live first-party reader -- only the 1.2 migration, an archived script and Terraform) + the auth-handler role's `GetItem/PutItem/UpdateItem/DeleteItem/Scan/Query` grant on it AND on a us-east-2 copy (`iam.tf:50-51`) | measured | brief F6 (source + APPLIED) | `0.7.0_AE_CloudOps` | retire | S8 | 8 | snapshot-then-delete; the grant AND the us-east-2 ARN leave in the same TO; ACCEPT = no sign-in or partner feature changed (FWD-9 DONE WHEN is EXERCISED: the old copy is gone and nothing noticed) |
| S10 | FWD-10 | the RS256 keypair `opal/auth/jwt-private-key` / `-public-key` in Secrets Manager (created 2026-04-06, no rotation); consumers = `auth-validator-edge` and `portal-jwt-authorizer` (both fetch the public key) | measured | brief F7 :169-177 (APPLIED) | `0.7.0_AE_CloudOps` | wire | -- | 9 | a dual-key overlap runbook (both consumers accept the outgoing and incoming public key for one access-token lifetime) + ONE deliberate rotation with nobody signed out -- the rotation IS the exercise (FWD-10 DONE WHEN) |
| S11 | FWD-11 | refresh-token binding in the auth handler: refresh `sub` = the EMAIL, not `userId` (brief finding F-10), so delete + re-create on the same address re-binds a live refresh token to the new row; access token 15 min, refresh 7 d | measured | brief F7 (source) | `0.7.0_AE_CloudOps` | align | S8 | 10 | bind the refresh token to `userId` (or a per-row session id) so a re-created account cannot inherit the old session; exercise = delete + re-create on the same email in a staged path, the old session does not come back (FWD-11 DONE WHEN) |
| S12 | FWD-12 | opal-gateway: ALB `opal-gateway` (internet-facing; OIDC default action; rules 10/20/30/31 forward `/mcp*`, `/authorize`, `/register`, `/token`, `/.well-known/*`, `/callback`, `/otp/fetch`, `/otp/health`, `/ms/*` AROUND OIDC to the app's own bearers) + EC2 `i-07dccb1615503ac99` (t4g.nano, IMDSv2, SSM only, SG 8080 from the ALB SG only): ALB access logs OFF; static capability bearers on `/otp/fetch` and `/ms/*` with NO expiry; ALB deletion protection OFF; the instance holds an unneeded public IP | measured | brief WS2 gateway :199-217 (APPLIED) | `0.7.0_AE_CloudOps` (ALB, WAF, instance -- Terraform) + `0.5.0_AE_OpalETL` for the gateway APP's bearer code (`otp.check_bearer`, `ms_ingest.check_bearer`; consult before edit, its lane) | align | S17 | 11 | ALB access logs ON into S17; every static bearer gets an `expires_at` and a rotation cadence; the regional ACL's two COUNT groups graduate with S4; ALB deletion protection ON and the public IP removed are brief findings (d)/(e) -- in scope as `align` cells, not new outcomes |
| S13 | FWD-13 | opalinvest.com: EC2 `i-0152e3fe2599fa630` (t3.small, EIP 18.208.18.213, IMDSv2, no SSH, SG 80/443 only) running OpenLiteSpeed + LSPHP 8.2 + local MariaDB + WordPress; on-box `harden.sh` (fail2ban, plugin hardening, nightly backups) is DESIRED, live state unmeasured; **NO CloudFront, NO WAF** by the original spec (Andrew 2026-07-13, "NO RDS / Fargate / Lightsail / CloudFront") | measured | brief WS2 website :219-235 (APPLIED for the instance/SG; DESIRED for harden.sh) | `0.7.0_AE_CloudOps` | wire | -- | 12 | **RULED (section 6, 2026-09-03 ~08:4xZ, "Recs approved"): CloudFront + WAF managed rules** -- the same rule groups, logging path and IP sets as S4 / S5 / S18, so one BLOCK row blocks at the site and the portal from one table; the task order is no longer held. Restricting `/wp-admin` and `xmlrpc.php` by source address at the edge is the same cell. The box is not moved (section 5) |
| S14 | FWD-14, FWD-15 | `opal-sentinel` Lambda (NEW): CloudWatch Logs subscription filter per scope (action = BLOCK, any managed-rule label, `/auth/login` POSTs) -> parse -> per-address counter with TTL -> ALLOW-list check -> WATCH or BLOCK row in S16 -> case file in S17 `cases/{yyyy}/{mm}/{dd}/{addr}/{case_id}/` -> ONE SES email to `andrew@opalinvest.com` per address per incident, 24 h suppression; daily digest FILE to `reports/daily/` | absent | PRD 7.2-7.3 (design RATIFIED @8cbe362358); nothing built | `0.7.0_AE_CloudOps` | wire | S3, S5, S16, S17, S18, S20 | 13, 14 | C-1 (exercised only after FWD-2 is; until then every case file and report states the coverage bound), C-3 (a persistent block needs more than one rate trip; thresholds are STARTING values), C-4 (never overrides ALLOW; arming BLOCK with 0 ALLOW rows is a violation), C-6 (one email per address per 24 h, plain text, case path in the body; the SES identity is the one the auth handler already sends from -- no new sender), C-7 (reserved concurrency 1), C-10 (Terraform; no CloudFormation solution import; no new vendor) |
| S15 | FWD-14, FWD-17 | `opal-ipset-reconciler` Lambda (NEW) on the S16 DynamoDB Stream (`NEW_AND_OLD_IMAGES`) + a once-daily full reconcile: `status=BLOCKED` insert/modify -> `UpdateIPSet` add (`/32`, `/64`); `ALLOW` / `EXPIRED` / TTL REMOVE -> `UpdateIPSet` remove | absent | PRD 7.2(a), 7.3 | `0.7.0_AE_CloudOps` | wire | S16, S18 | 13, 16 | C-2 (the table is truth; the IP sets are projections; **nothing else calls UpdateIPSet**), C-5 (the stream REMOVE event is how an expiry unblocks), C-7 (idempotent: re-applying the table yields the same set) |
| S16 | FWD-16, FWD-17 | `opal-suspicious-addresses` DynamoDB (NEW): pk `address` (normalized CIDR); `status` in {BLOCKED, WATCH, ALLOW, EXPIRED}; `first_seen`, `last_seen`, `hits`, `rules`, `sources`, `paths_top`, `case_ids`, `blocked_at`, `blocked_by` (auto or serial), `expires_at` (TTL), `unblocked_by/at`, `notes`; GSI `status-index`; the project CMK (S25); PITR ON; deletion protection ON | absent | PRD 7.3, C-9, C-13 | `0.7.0_AE_CloudOps` | wire | S25 | 15, 16 | C-9 (all four properties present at APPLIED -- the table that decides who is locked out is the best-protected table in the account), C-5 (every automatic BLOCK row carries `expires_at`: 24 h first, 7 d on repeat; permanent = a distinct human-pinned status) |
| S17 | FWD-16, FWD-18 | (v0.9) `opal-security-evidence` S3 (NEW BUCKET; through v0.8 this row named `opal-data-security`, which is now S28, FWD-5's log destination): private; SSE-KMS on the project CMK (S25); versioning ON; bucket policy denies non-TLS and any principal outside the sentinel, reconciler and `opal-security-admin` roles (C-14); server access logging to the project-owned target `opal-data-security-access-logs` (S27, C-15); `cases/`, `reports/`, `allowlists/` retained; paths `cases/` (INCLUDING the log extracts a case cites, `waf-samples.jsonl` -- FWD-18's ACCEPT names them), `reports/daily/`, `allowlists/` exactly as 7.3; NO `waf-logs/` and NO service-principal writer | absent | PRD 7.3, C-8, C-13, C-14, C-15 | `0.7.0_AE_CloudOps` | wire | S25, S26, S27 | 15, 17 | C-8 (any listed property absent at APPLIED violates; a case written outside `cases/{yyyy}/...` violates). **Object Lock (governance) on `cases/` is CARRIED TO ANDREW** -- an option, not a cell decision |
| S18 | FWD-14 | WAF IP sets `opal-blocked-ips-{scope}` x2 (CLOUDFRONT scope + REGIONAL) + rule 0 `IPSetReferenceStatement` -> BLOCK on BOTH ACLs | absent | PRD 7.3 | `0.7.0_AE_CloudOps` | wire | S4 | 13 | written by S15 ONLY (C-2); `/32` v4, `/64` v6 |
| S19 | FWD-17 | the unblock path: `.tools/opal-ipblock allow <addr> --reason "..."` (audited CLI) flipping the S16 row's `status`; the portal Admin page (Security -> Blocked addresses -> Unblock) is a LATER increment of FWD-16/17 | absent | PRD 7.3, C-11, C-14 | `0.7.0_AE_CloudOps` (the CLI); the portal page is NOT in this round and would be a DT/DE lane later | wire | S16, S26 | 16 | C-11: the CLI edits the ROW, never the IP set; "reached us again within minutes" is the stream (S15) doing its job, not the CLI. A block nobody renews lapsing on its own is the S16 TTL (C-5) |
| S20 | FWD-14 | the partner-egress ALLOW list `allowlists/partner-egress.json` (versioned in S17, mirrored as `status=ALLOW` rows in S16), populated from MEASURED sign-in addresses per firm | unmeasured | C-4; the per-firm sign-in address census does not exist -- it needs S5's logs (or the auth handler's structured log lines) over a window | `0.7.0_AE_CloudOps` | verify | S5, S16, S17 | 13 | **C-4: arming BLOCK with 0 ALLOW rows is a VIOLATION, not a phase.** The census needs logs running first -- this is the sequencing reason FWD-14 is exercised LAST. A partner office typically leaves the internet through ONE address; a false positive here is a locked-out firm, not a noisy alert |
| S21 | -- | WAF coverage of the raw `execute-api` addresses (S1, S2): what the sentinel CANNOT see until FWD-2 lands | held | brief F1/F2 + PRD 7.1: the two gateways answer at their own addresses with no WAF in front | `0.7.0_AE_CloudOps` | verify | S3 | -- | C-1: until FWD-2 is exercised the auto-block covers CloudFront + the gateway ALB ONLY, and every case file and daily report SAYS SO, so a "no incidents" week is not read as a quiet week |
| S22 | -- | IAM for the sentinel, the reconciler and the unblock CLI: `simulate-principal-policy` per role, ONE `--resource-arns` per call, the positive control as a separate invocation, `--context-entries` for any conditioned statement | unmeasured | -- (`comp-iam` is DESIRED-plane, models `(action)` not `(action, resource)`, reports 24 unattached policy blocks + 2 unparsed Deny statements per the brief; it cannot answer "is this denied?") | `0.7.0_AE_CloudOps` | verify | S14, S15, S19 | -- | never signal ALLOWED from `comp-iam` silence; a cross-firm-secret-deny belt of the same shape as the auth handler's (brief F7) is the pattern to extend, not a new one to invent |
| S23 | -- | the current WAF rate-rule thresholds against ordinary traffic -- the month of WATCH rows C-3 needs before any threshold is called final | unmeasured | brief F5: sampled requests for the auth rule over 3 h = 0 (consistent with no attack AND with nobody looking) | `0.7.0_AE_CloudOps` | verify | S5, S14 | -- | C-3: BLOCK on a single rate trip violates; a threshold presented as final without WATCH rows violates. **Final thresholds are CARRIED TO ANDREW** once the WATCH month exists |
| S24 | FWD-1 | the Cognito-claim footprint: the token appears in 25 first-party source files (8 portfolio Lambdas, 3 Terraform api-gateway files, ticket-center, data_refresh, portal `firmAccess.ts`) and 6 docs; 0 definitions, 0 `aws_cognito_*` resources declared, 0 user pools live | measured | brief F1 (estate sweep, source at 2026-09-02 HEAD) | `0.7.0_AE_CloudOps` for the Lambdas + Terraform; the portal file is a DT/DE lane and the docs are `ANY_CTO` -- one sweep, several lanes, ONE finding row per lane | align | S1 | 1 | Andrew 2026-09-02: **no Cognito, never** -- a docstring naming a control that does not exist is corrected with the fix, never left to satisfy the next reader. The sweep changes no behaviour; it removes false control claims |
| S25 | FWD-16, FWD-18 | the project customer-managed KMS key `alias/opal-security` (NEW, v0.5): Terraform `aws_kms_key` + `aws_kms_alias` in the project's own module, rotation ON, key policy scoping the sentinel, reconciler and `opal-security-admin` roles (C-14); the key S16 and S17 encrypt with | absent | row NFRA_OPSEC202609-Z-S3 (0.7.0_AE_CloudOps~S, `describe-key` with a KeyManager=CUSTOMER positive control over all 11 keys): no general-purpose CMK exists; the "estate CMK" of v0.3 is `alias/aws/dynamodb`, KeyManager=AWS | `0.7.0_AE_CloudOps` | wire | -- | 15, 17 | C-13: ONE key, both resources, Terraform only; round 1 INTERIM (SSE-S3 / AWS-managed) is permitted with the KMS limb filed UNCOMPUTABLE; the flip is a round-2 task order, in place (UpdateTable; bucket default-encryption change) |
| S26 | FWD-16, FWD-17, FWD-18 | the `opal-security-admin` IAM role (NEW, v0.6): Terraform `aws_iam_role` in the project's own module; the human-side principal of C-8 (evidence store), C-11 (unblock CLI) and C-13 (key policy); trust policy = Andrew's own IAM identity alone for round 2 (RULED 2026-09-03 ~08:4xZ, card OP-x-6) | absent | row NFRA_OPSEC202609-Z-S4 (0.7.0_AE_CloudOps~S): 0 of 216 roles match admin/cto/terraform, positive control lambda 55; the applier is `user/Andrew_Berman`; "CTO-admin role" of v0.3 never existed | `0.7.0_AE_CloudOps` | wire | -- | 15, 16, 17 | C-14: trust = Andrew alone for round 2 (RULED); never an IAM user in a bucket or key policy (the ROLE is the principal there); the deny-outside-list statement on S17 lands with S14/S15/S26 in round 2 (the COO's Z-S4 deferral) |
| S27 | FWD-18 | the access-logs target `opal-data-security-access-logs` S3 (NEW, v0.7): private; SSE-S3; versioning ON; lifecycle; policy granting `logging.s3.amazonaws.com` with SourceAccount + SourceArn conditions; the bucket S17's server access logs deliver into (v0.9: S17 is now `opal-security-evidence`) | absent | row NFRA_OPSEC202609-Z-S5 (0.7.0_AE_CloudOps~S, measured BEFORE the apply): the CloudTrail bucket's policy = two statements, both `cloudtrail.amazonaws.com`; no logging.s3 grant, no LogDelivery ACL; 0 of 31 buckets have access logging enabled | `0.7.0_AE_CloudOps` | wire | -- | 17 | C-15: the audit-log bucket is NOT widened; graded by a DELIVERED object under the prefix after one write to S17, never by `get-bucket-logging`; lands in round 2 beside S25/S26 |
| S28 | FWD-5 | (v0.9, NEW ROW for an EXISTING and LIVE resource) `opal-data-security` S3 re-homed as FWD-5's LOG DESTINATION: private; **SSE-S3 (`AES256`), NOT the project CMK**; versioning ON; bucket policy grants `delivery.logs.amazonaws.com` (`waf-logs/cloudfront-access/*`) and `logdelivery.elasticloadbalancing.amazonaws.com` (`waf-logs/alb-opal-gateway/*`) with SourceAccount + SourceArn, denies non-TLS; lifecycle `waf-logs/` -> Glacier 90 d, expire 400 d | measured | row NFRA_OPSEC202609-Z-S37 (`0.7.0_AE_CloudOps~S`, phase-1 read before any write: the project key admits ZERO service principals and this bucket is written by exactly two) + `list-objects-v2` at `1.0.0_SA_CTO~Z` 13:1xZ: 36 objects, ALL under `waf-logs/`, newest 13:10:11Z | `0.7.0_AE_CloudOps` | align | S5 | 18 | C-16: this bucket is NOT flipped to the project key -- the flip would stop both live delivery legs silently and the only in-key remedy is a grant C-13 does not carry and does not need. ALREADY APPLIED except the policy/lifecycle restatement; the cell is an ALIGN, not a build |

**MECE, BOTH DIRECTIONS, run rather than asserted:**

```
  FORWARD   every OWNS item has >= 1 row ........ 19 of 19   (v0.5: item 17, the project CMK, S25; v0.6: item 18, the admin role, S26; v0.7: item 19, the access-logs target, S27)
              (1) S1 S2 S3 S24   (2) S4 (+ S12 for the regional groups)   (3) S5 S12   (4) S6
              (5) S7   (6) S8   (7) S9   (8) S10   (9) S11   (10) S12   (11) S13   (12) S17
              (13) S16   (14) S18   (15) S14 S15   (16) S19   (17) S25   (18) S26   (19) S27
  REVERSE   every WORK row maps to an OWNS item . S1-S19, S24, S25, S26 and S27 all map; S20-S23 are INPUTS
              (verb = verify), correctly NOT work rows
  OUTCOMES  every FWD-n has >= 1 owned surface .. 18 of 18
              FWD-1 S1 S24 | FWD-2 S1 S2 S3 | FWD-3 S2 | FWD-4 S6 | FWD-5 S4 S5 | FWD-6 S4
              FWD-7 S7 | FWD-8 S8 | FWD-9 S9 | FWD-10 S10 | FWD-11 S11 | FWD-12 S12 | FWD-13 S13
              FWD-14 S14 S15 S18 S20 | FWD-15 S14 | FWD-16 S16 S17 S19 S25 S26 | FWD-17 S15 S16 S19 S26
              FWD-18 S17 S25 S26 S27
  CAVEAT (postulate i): 16 of 16 certifies coverage of the OWNS cell AS WRITTEN in section 3;
  a manifest can be MECE over a domain that is itself incomplete. The brief's "two other running
  instances" (canonical-schwab-si2 IMDSv2 optional; inf-gold-layer-runner public IP) are NOT in
  the OWNS cell and NOT rows -- they belong to their owners, surfaced by the brief, not chased here.
```

**What this manifest does NOT assert:** any `measured` cell is the brief's 2026-09-02 reading and may have moved; the L5 battery (`comp-schedule`, `comp-iam`, `comp-adversary`, each RUN with a denominator or DECLARED-NOT-APPLICABLE with a reason) re-grounds. No cell here is owned by a Tier-0 or Tier-1 seat; the `lane` column names the CLASS, and `2.0.0_SA_COO~Z` seats the instances at L6.

## 9. Sequencing input for `2.0.0_SA_COO~Z` (not a dispatch)

The order the constraints dictate, stated once so the decomposition's dependency edges have a source to cite; the COO owns the cells, the edges and the task orders.

1. **S3 first** (the origin secret) -- C-1 makes it the first atom; S1 and S2 consume it; S21 is its coverage statement until it lands.
2. **S1 + S2** (authorizers at both gateways) with **S24** riding S1's TO (the docstring and the 25-file sweep).
3. **S5** (logging on both ACLs + CloudFront + ALB) -- the input for S6, S20 and S23; nothing downstream of it can be measured until it runs for a window.
4. **S4** managed rules in COUNT (the soak FWD-6's DONE WHEN requires), then BLOCK; the regional ACL's two COUNT groups graduate on the same evidence (S12).
5. **S7, S8, S9, S10, S11** are independent of the auto-block framework and of each other except S9 after S8 and S11 after S8; they can run in parallel instances.
6. **S12** (gateway logs, bearer expiry, ALB deletion protection, public IP) is independent; S13 is HELD at Andrew (the edge choice).
7. **The framework, in this order and only after 1-3:** S17 + S16 -> S18 -> S15 -> S20 (the ALLOW census over S5's window) -> S14 armed to WATCH -> the C-3 month -> S14 armed to BLOCK (the FWD-14 exercise, C-1 satisfied by then). S19 lands with S16. S22 runs before any of S14/S15/S19 is deployed.

**Carried to Andrew as cards, NOT the decomp's to decide (section 6, 7.6):** the FWD-13 edge choice (CloudFront+WAF vs Cloudflare); the morning digest EMAIL (C-6); Object Lock on `cases/` (C-8); the final thresholds once a month of WATCH rows exists (C-3). **The moratorium bound (section 5):** FWD-4/5/6/12/14/15 are the ONLY alert/monitor/notification surfaces this project may build; a cell that wants another files a row and waits for his word.

# NFRA_OPSEC202609 -- surprise channel, REMEDIATION v2 (site Z) -- THE ROUND-2 SLUG

**Home:** the project tree's channel (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` s.5). **Lane:** the CVO only.
**Cut by:** `3.0.0_SA_CVO~Z`, round 2, 2026-09-10 ~10:1xZ. **Reader:** `1.0.0_SA_CTO~Z`, and no one else.

**L10 PRECONDITION, BOTH LIMBS, SOURCE = THE INDEX** (`_latest_dispositions` imported and called; source named
per msg 20853 s.2):

```
168 items | UNDISPOSITIONED 0 | GRADUATED 104 | DISMISSED_WITH_REASON 64
2 of 2 JUDGMENT criteria graded at C-S34 (S10D-AC2 PASS; S10E-AC6 PASS on conduct, with the fork RULED)
CONTROL: the same call on NFRA_REPORT returns 24 items / 0 undispositioned -- the census fires on a
         second project, so the zero is a measurement and not an empty read.
```

**THE ROUND OPENED AT 138 UNDISPOSITIONED.** This document carries **99 rows**: the **94** graduated by round 2's
adjudications, plus **5 CARRIED FROM ROUND 1** -- `Z-S1`, `Z-S2`, `Z-S11`, `Z-S13`, `Z-S17`. Round 1 graduated TEN
items and `REMEDIATION_v1.Z.md` carries FIVE; those five have never appeared in any remediation document, and
nothing in the fabric tests that a graduated item reaches one (`C-S35`).

**HOW `remedy` AND `owner` WERE DERIVED, stated so neither is over-read.** `owner` is the lane named by the row's
own `disarm_owner`, defaulting to the issuer where the row names none -- it is the lane that would BUILD, as the
schema requires, and it is NOT an assignment. `remedy` is **carried verbatim from each row's own notes** where the
row stated one; this slug does not invent a remedy the round did not state, and where a row named none the field
says so. `remediation.state` is `OPEN` on all 99 and `disarm.state` is `ARMED` wherever the source row was --
**nothing here is claimed REMEDIATED or DISARMED**, because this seat verified no remedy landing for this round.

**AUDITED GATE OVERRIDE, disclosed here and not only in the commit.** As on NFRA_REPORT, `_coordinate_violations`
refuses a NEW row carrying `W<n>` from a non-worker committer while protocol s.5 requires the remediation id to
EQUAL the graduated id. `Z-S23` predicted this in this project's own channel before the slug was cut. The gate
cannot tell MINTING an id from CARRYING one, and a slug only ever carries.

**What this document is NOT.** It routes nothing and names no limb. The recut is `2.0.0_SA_COO~Z`'s and the
coverage read is the reader's; the CVO's engagement with round 2 ends here.

---

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-S100",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "BOTH CONSUMERS OF THE LOGIN SIGNING KEY ARE SINGLE-SLOT, SO FWD-10's NO-SIGN-OUT ROTATION IS IMPOSSIBLE AS THE SYSTEM STANDS. NOTHING WAS ROTATED. auth-validator-edge holds ONE scalar (index.mjs:68 cachedPublicKey, exactly one jwt.verify at :235, 300s TTL) and opal-portal-authorizer holds ONE scalar (index.mjs:20 publicKey, exactly one jwt.verify at :198) WITH NO TTL AT ALL -- getPublicKey() at :25-28 returns the cached value forever, so a warm container could never converge onto a new key even if a second slot existed. Confirmed on THREE PLANES: source at 998c79b970, the DEPLOYED bundles (exactly one occurrence of the secret id in each), and THE SECRET ITSELF, a bare 452-char PEM with exactly one BEGIN block. The two-slot pattern this face was told to copy is ALREADY DEPLOYED IN THE SAME AUTHORIZER for the ORIGIN secret, and that module's own docstring states the precise mechanism that makes the JWT path unrotatable.",
    "evidence": [
      "CONSUMER 1 OF 2 -- auth-validator-edge, SOURCE at 998c79b970 (file verified clean at HEAD via git status --porcelain, so the commit-ish is honest): infra/aws/lambda-edge/auth-validator-edge/index.mjs:68 'let cachedPublicKey = null;' and :69 'let cacheExpiry = 0;' -- two scalars, not a map or an array. :225 'if (!cachedPublicKey || Date.now() > cacheExpiry) {'. :230 'cachedPublicKey = response.SecretString;' -- the WHOLE secret string assigned to one variable, no parse, no slot selection. :231 'cacheExpiry = Date.now() + 300000; // 5 min'. :235 'const payload = jwt.verify(token, cachedPublicKey, { algorithms: [\"RS256\"] });'. comp-read --enumerate over the pattern 'jwt\\.verify|cachedPublicKey|cacheExpiry' returns 8 hits across 450 lines, PAGE 1 of 1, so the enumeration is complete and not a truncated page: ONE key variable, ONE verify call site. CAPACITY: ONE KEY.",
      "CONSUMER 2 OF 2 -- the API authorizer opal-portal-authorizer, SOURCE at 998c79b970 (file verified clean at HEAD): infra/aws/users/lambda/portal-authorizer/index.mjs:20 'let publicKey = null;' -- one scalar. :25-28 'async function getPublicKey() { if (publicKey) { return publicKey; }' -- the cache check is a bare truthiness test with NO TIME COMPONENT. :35 'publicKey = response.SecretString;'. :195 'const pubKey = await getPublicKey();' and :198 'const decoded = jwt.verify(token, pubKey, {'. comp-read --enumerate over 'jwt\\.verify|getPublicKey|publicKey' returns 8 hits across 260 lines, PAGE 1 of 1, complete: ONE key variable, ONE verify call site, and NO EXPIRY. CAPACITY: ONE KEY, HELD INDEFINITELY.",
      "THE SERVING PLANE, because 'deployed' is not 'serving' and the repo copy could be stale -- and the authorizer was in fact modified TODAY (LastModified 2026-09-03T20:43:43Z), which is exactly the case where a source-only read would have been wrong. Both artifacts were DOWNLOADED from Lambda and read as bytes. auth-validator-edge CodeSha256 5ZeZy/9Y+mhuV4QWbRRw85rTR6rbp+s3rblLi0/9kCo=, LastModified 2026-06-09T20:41:09Z, 20739 bytes; its bundled minified handler reads 'if(!R8||Date.now()>H4)R8=(await new IJ({region:\"us-east-1\"}).send(new _J({SecretId:\"opal/auth/jwt-public-key\"}))).SecretString,H4=Date.now()+300000;let J=Y4.default.verify(W,R8,{algorithms:[\"RS256\"]});' -- one scalar R8, one verify. opal-portal-authorizer CodeSha256 WNm3LnJpgcs9wqNlJ4bU2T6n65IgcMM/fgf2EyENcoY=, 20072 bytes; its bundle reads 'var fq=null;async function uJ(){if(fq)return fq;try{let q=new yJ({SecretId:\"opal/auth/jwt-public-key\"});return fq=(await vJ.send(q)).SecretString,fq}' -- one scalar fq, no TTL. Occurrences of the string 'opal/auth/jwt-public-key' in each deployed bundle: EXACTLY 1 and EXACTLY 1. A second slot cannot be read by code that fetches the secret once and assigns it to a scalar.",
      "THE SECRET ITSELF, which is the check that could have FALSIFIED this row and did not: aws secretsmanager get-secret-value on opal/auth/jwt-public-key returns a 452-character value beginning '-----BEGIN PUBLIC KEY-----' and ending '-----END PUBLIC KEY-----', containing exactly ONE '-----BEGIN' block, with json.loads raising JSONDecodeError and the tokens 'current' and 'previous' both ABSENT. So the secret is a bare PEM and not a multi-slot envelope. POSITIVE CONTROL, same instrument, same call shape, run as a SEPARATE invocation: opal/auth/origin-verify parses as JSON and returns slots ['current','previous']. The probe CAN see a two-slot envelope when one exists -- therefore the absence on the JWT key is a real absence and not an instrument failure.",
      "THE SIBLING PATTERN, and it is the strongest corroboration because it is a DIFFERENT instrument than my own reading -- it is this project's own already-accepted doctrine: infra/aws/users/lambda/portal-authorizer/originVerify.mjs:48-54 @998c79b970 states, of the ORIGIN secret in the SAME Lambda, 'THE TTL IS A CORRECTNESS CONTROL, NOT A PERFORMANCE ONE. An unbounded cache breaks the rotation: a container that cached {current: A} before the rotation holds no knowledge of B, so the moment the distribution starts sending B that container 403s every request it serves until it happens to be recycled -- and Lambda does not bound execution-environment lifetime.' That is a verbatim description of the JWT authorizer's getPublicKey(). OP-s-3 built the two-slot read at :56-78 with parsed.current and parsed.previous and a 300s TTL; the JWT path got none of it.",
      "SECRETS METADATA RE-GROUNDED per phase 1, against what the face quotes as of 19:2xZ. opal/auth/jwt-private-key: CreatedDate 2026-01-03, LastChangedDate 2026-04-06T13:31:00.251000-04:00, VersionIdsToStages holds exactly ONE version (1acd44f3-d07e-486b-9ad8-66993a0b6716) staged AWSCURRENT, and there is NO RotationEnabled field and NO AWSPREVIOUS stage. opal/auth/jwt-public-key: same dates, one version (fabe94f0-019d-455d-8c72-47b3d709bd8b) AWSCURRENT, no RotationEnabled, no AWSPREVIOUS. The face's substantive premises -- ~5 months old, never rotated by any automated path, rotation not configured -- are all CONFIRMED."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS THE DELIVERABLE AND NOT A FAILURE TO DELIVER. The face is explicit that deliverable 1 is a gate and that the single-slot finding IS the product. Nothing was rotated, no secret was written, no Terraform ran, no ledger was opened -- an opened ledger would have asserted an act that must not begin. THE SHARPENING THAT IS WORTH MORE THAN THE HEADLINE, and it is a SECOND defect rather than a restatement of the first: 'single-slot' understates the authorizer. Even if someone taught both consumers to hold two keys tomorrow, the authorizer's cache at index.mjs:25-28 has NO TTL -- 'if (publicKey) return publicKey;' -- so a warm execution environment would hold the pre-rotation key for the life of that environment, and Lambda does not bound that lifetime. S10-AC2's 'wait for both consumers to be serving the new key' is therefore UNSATISFIABLE AT ANY WAIT LENGTH for this consumer as written: you cannot wait out a cache that never expires, and the only convergence mechanism available today is a redeploy that cycles the execution environments. The remedy is consequently TWO changes and not one -- a second slot AND a TTL -- and the project has already written both, for the origin secret, in the same file tree. THE EDGE IS THE ONE THE FACE WARNED WOULD BE FORGOTTEN, and it is the better-behaved of the two: it at least has a 300s TTL at :231, so it would converge. The authorizer, which is the one that looks more ordinary, is the one that cannot. WHAT IS NOT ESTABLISHED, and this row does not guess. (i) THE POPULATION OF CONSUMERS MAY BE LARGER THAN TWO. S10-AC1's denominator is 2 of 2 and both were read, but comp-find over 'jwt-public-key' across 51,628 files returns 191 hits and shows FOUR MORE first-party readers of the same secret: infra/aws/lambda/shared/opal_auth/__init__.py:28,33 (a SHARED Python module, '_cached_public_key: Optional[str] = None' -- also a single scalar), infra/aws/auth/validator.py:31, infra/aws/auth/validator.ts:29, and two under infra/aws/opalinvest_dev/. Whether any of those is live on the production login path was NOT determined here and is out of this face's scope; the shared module has only 2 importers in source. If any IS live, the rotation surface is wider than the face models and the remedy must cover it -- that is a question for the re-cut, not an assertion by this row. (ii) THE EDGE'S ACTUALLY-SERVING REPLICA VERSION was not read from a live CloudFront describe-distribution. comp-routes edge-versions reports auth-validator-edge bound by qualified_arn (DYNAMIC, auto-updating on apply) but discloses itself as DESIRED plane only and explicitly cannot distinguish a declared binding from a pinned stale one. This does not soften the verdict, and the reason is structural rather than optimistic: two-slot verification was never implemented for this secret in any version -- the deployed $LATEST bundle contains exactly one occurrence of the secret id and one verify call, and an OLDER pinned replica cannot contain a capability that was never written. THE REUSABLE PART: the gate was worth more than the build it blocked, and it cost three reads. The decisive one was the cheapest and the most skippable -- fetching the secret's own VALUE. Source and deployed bytes both say 'one scalar', but a scalar holding a JSON envelope with two keys inside would have made every one of those readings true and the conclusion wrong. The envelope check is what separates 'the code holds one variable' from 'the system knows one key', and it only counted because a known-two-slot secret was run through the same probe in a separate invocation to prove the probe could see slots at all.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S101",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "THE DNS AND CERTIFICATE HALF OF TO-OP-S-13 IS NOT EXECUTABLE FROM THIS FABRIC: opalinvest.com is not in Route53 and is not in this AWS account at all -- it is delegated to GoDaddy (ns47/ns48.domaincontrol.com), there is no ACM certificate for the name, and the apex is an A record that CloudFront structurally cannot be the target of. Deliverables 4 and 5 (the cutover and the DNS rollback) and the custom-domain half of S13-AC1/AC2/AC3 all depend on a registrar credential this fabric does not hold. The build half -- the distribution, the IP-set reuse and the box-untouched proof -- is unaffected and proceeds.",
    "evidence": [
      "ROUTE53, PRINTED DENOMINATOR: aws route53 list-hosted-zones returns 2 zones with IsTruncated absent, so 2 is a true denominator and not a page count -- opalinvest.dev. (Z054626637UVVD9T5GO6, public) and opal-globgrph.local. (Z0229592AYZ2OKHNNKRL, PRIVATE). There is NO opalinvest.com zone. The estate runs Route53 for the PORTAL domain only.",
      "AUTHORITATIVE, NOT INFERRED FROM A RESOLVER: opalinvest.com NS = ns47.domaincontrol.com + ns48.domaincontrol.com (GoDaddy). Queried against GoDaddy's own nameserver ns47.domaincontrol.com (97.74.103.24) rather than only a public recursive, so this is the zone's own answer and not a cache.",
      "ACM, PRINTED DENOMINATOR: list-certificates --region us-east-1 returns 1 certificate, NextToken absent -- DomainName opalinvest.dev, status ISSUED. There is no certificate for opalinvest.com. CloudFront alias TLS requires a us-east-1 ACM cert covering the alias, and ACM DNS validation requires writing a CNAME into the GoDaddy zone. The certificate is blocked by the same credential as the cutover, which is why they are ONE row and not two.",
      "CLOUDFRONT, PRINTED DENOMINATOR: list-distributions returns exactly 1 distribution -- EVTSA9VEHNZVH, aliases opalinvest.dev + www.opalinvest.dev, WebACLId a09833c0-4043-49fc-a92c-0dcdeaff9abd. No distribution exists for opalinvest.com; this face would create the first.",
      "THE APEX SHAPE, AND IT IS THE PART A READER WILL SKIP: opalinvest.com resolves as an A record (18.208.18.213) with TTL 3600, read authoritatively. CloudFront publishes a DOMAIN NAME and no stable IP, so pointing an apex at it requires an ALIAS/ANAME-class record. RFC 1034 s.3.6.2 forbids a CNAME coexisting with the SOA/NS at a zone apex, so a plain CNAME is not available at opalinvest.com regardless of provider. Route53 solves this with ALIAS. WHETHER GODADDY OFFERS AN ALIAS/ANAME EQUIVALENT IS NOT ESTABLISHED HERE and is recorded as NOT ESTABLISHED -- confirming it needs vendor egress, which is excluded without Andrew's per-use word. www.opalinvest.com IS a CNAME to the apex (TTL 600) and would take a CloudFront target cleanly; the apex is the constrained one.",
      "A SECOND, INDEPENDENT CARRIER SAYS THE SAME THING -- this is not one instrument read twice: infra/aws/terraform/website/README.md states the EIP is 'the stable public IP handed to GoDaddy apex-A at W3 cutover' and 'NO GoDaddy DNS changes in W1 (cutover is W3)'. The repo's own account of this domain names GoDaddy as the control point. Instrument 1 was the live DNS/AWS control plane; instrument 2 is the estate's own IaC documentation. They agree.",
      "THE PROPAGATION REALITY DELIVERABLE 5 ASKS FOR, MEASURED NOT ASSERTED: the apex A record's own TTL is 3600 (1 hour), read from ns47.domaincontrol.com via Resolve-DnsName. The zone SOA default TTL is 600, which is NOT the governing number for this record -- reading the SOA default and calling it the rollback window would understate it by 6x. A DNS rollback is therefore bounded BELOW by 1 hour for correctly-behaving resolvers and is not bounded above, since resolvers are observed to serve past TTL. The rollback is NOT atomic and must never be stated as instant.",
      "AND THE REPO'S PRE-CUTOVER FRAMING IS STALE, WHICH MATTERS FOR THE ROLLBACK POINT: the same README calls 72.167.58.121 'the OLD host (GoDaddy) -- the rollback point' and describes the apex flip as still-future work (W3). Live DNS says the apex ALREADY points at the AWS EIP 18.208.18.213, so W3 has happened. The old host still answers 200 to a Host: opalinvest.com request, so it remains a live fallback, but any plan that reads this README as current would be planning a cutover that already occurred."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS FILED AS ARMED AND NOT AS AN OBSERVATION: the tempting reading is 'DNS is a later step, note it at proof time'. That reading is what makes this dangerous. If this face builds a distribution and reports the edge as delivered, the applied world contains a CloudFront distribution that NO VISITOR TRAFFIC TRAVERSES, while every configuration probe -- get-distribution, get-web-acl, the IP set reference -- reads healthy and complete. That is the same shape as Z-S97's unsubscribed topic and Z-S98's two silent alarms: deployed, well-formed, and serving nobody. The row is what keeps the gap legible between the build and the cutover. WHAT IS NOT BLOCKED, STATED SO THIS ROW IS NOT READ AS A FULL STOP: the distribution can be built and EXERCISED end-to-end on its own *.cloudfront.net domain with no alias and no ACM certificate, because CloudFront supplies a default certificate for that name. S13-AC1's 200-plus-real-content and its 404 negative control, S13-AC4's IP-set identity comparison, and S13-AC5's box before/after are all measurable that way TODAY. THE ASK IS A FORK, NOT A FACT: either (a) a registrar credential or a human at the GoDaddy console to place the ACM validation CNAME and the cutover record, or (b) authorization to migrate the opalinvest.com zone to Route53 -- which is itself a one-time NS change at the same registrar, so it does not escape the credential, it only pays it once and buys ALIAS support for the apex. This seat does not choose between them and does not touch DNS.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S102",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "THE /wp-admin ALLOW-LIST IS ABSENT AS THE FACE ANTICIPATED -- but the consequence is one step wider than the face states: the source-restriction rule is the ONLY blocking rule this face is authorized to build, so its absence does not just make S13-AC3 UNCOMPUTABLE, it removes the only mechanism by which S13-AC2 could demonstrate a refusal at all. AC2 and AC3 are coupled through one missing input, and the face treats them as independent.",
    "evidence": [
      "THE INPUT IS ABSENT FROM THE FACE ITSELF: TO-OP-S-13 deliverable 3 states 'the allowed addresses are an INPUT you do not invent' and 'If no allow-list is available, file a row and ask'. The GO message from 2.0.0_SA_COO~Z (Msg-ID 20015) repeats it and supplies no addresses. No allow-list is present in the task order, the GO, or the follow-up (Msg-ID 20024).",
      "THE COUPLING, READ OFF THE ACL AS IT WILL BE BUILT: the three managed rule groups are mandated to land with OverrideAction Count, which by definition refuses nothing. The BlockedIPs rule reused from TO-OP-S-4-18 references opal-blocked-ips-cloudfront (b2e008a6-40d9-4d07-bef5-1caa8b682bb3) and its IPv6 sibling, and BOTH ARE EMPTY BY DESIGN under constraint C-2 -- the S-4-18 carrier states in-line that 'THE SETS ARE EMPTY AND THIS RULE BLOCKS NOBODY ON DAY ONE' and that only the OP-s-15 reconciler may write them. Therefore, on the ACL this face is authorized to build, every rule either counts or matches an empty set. The source-restriction rule is the only one that can return a 403 to anything.",
      "S13-AC2 REQUIRES AN ACTUAL REFUSAL, not a counted match: its text is 'A KNOWN-BAD REQUEST IS REFUSED BEFORE WORDPRESS HANDLES IT ... with the response pasted, and evidence it did not reach the origin'. A Count action produces a CloudWatch metric and forwards the request to the origin unchanged, so a counted match is the OPPOSITE of the evidence AC2 asks for -- the request demonstrably DOES reach WordPress.",
      "CURRENT LIVE STATE OF THE TWO PATHS, measured before any change so the after-state is comparable: https://opalinvest.com/wp-admin/ returns 302 to /wp-login.php (reachable from this address, i.e. from anywhere), and https://opalinvest.com/xmlrpc.php returns 405 to a GET. 405 is METHOD-not-allowed and is not a refusal of the endpoint -- xmlrpc.php is a POST endpoint and the GET result says nothing about whether POST is accepted. Reading that 405 as 'xmlrpc is already closed' would be a false negative, so it is recorded explicitly.",
      "THE ORIGIN REMAINS DIRECTLY REACHABLE, which bounds what ANY edge rule can claim: sg-062bbb40a6c92509c permits tcp/80 and tcp/443 from 0.0.0.0/0, and the EIP 18.208.18.213 answers on both. A request sent to the IP with a Host: opalinvest.com header returns 301 to the canonical https URL, i.e. the origin serves non-edge traffic today. Any refusal this face demonstrates is therefore scoped to traffic that CHOSE to traverse the edge. S13-AC5 forbids modifying the box or its security groups, so closing that bypass is explicitly NOT this face's act -- it is named here because an unqualified 'known-bad requests are refused' claim would overstate what the applied world does."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THE ASK IS ONE FACT AND ONE RULING. THE FACT: the source addresses permitted to reach /wp-admin and xmlrpc.php -- most likely the office egress address and whatever address the TWLC developer (Patricia, named as WP-admin in infra/aws/terraform/website/README.md) administers the site from. THE RULING, which is separate and which this seat does NOT decide: xmlrpc.php is a distinct case from /wp-admin because it has no interactive administrator and is a standard credential-stuffing and pingback-amplification surface. Blocking it outright for ALL sources needs no allow-list and would give S13-AC2 its refusal immediately -- but it is a POLICY choice, not an address guess, and it can break Jetpack and mobile publishing clients if the site uses them. This seat will not make that call unilaterally, because 'do not leave the paths open' and 'do not guess' are both in the face and an outright block resolves the first by exceeding the second's intent. If the issuer rules that xmlrpc.php may be blocked outright, S13-AC2 becomes satisfiable tonight and only S13-AC3's /wp-admin half stays UNCOMPUTABLE. Filed BEFORE the build, deliberately, so the interim is legible: between the apply and the disarm there is an edge in front of a public marketing site whose only enforcing rule matches an empty set.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S103",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "TO-OP-S-9-11 IS NOT BLOCKED ON THIS LIMB AND CAN BE DISPATCHED NOW. The face's headline -- 'this limb is the only thing standing between the project and FWD-9 and FWD-11' -- is false against the decomp's OWN edge, which reads OP-s-8 --[DP + PITR read ON per table]--> OP-s-9, OP-s-11. That predicate is DP and PITR, not a key. Measured live at this seat: DeletionProtectionEnabled=True and PITR=ENABLED on 5 of 5 tables. The gating condition is already satisfied; the CMK alignment is real open work but it is NOT what OP-s-9 and OP-s-11 wait on.",
    "evidence": [
      "THE EDGE, QUOTED FROM THE L5 AUTHORITY: NFRA_OPSEC202609_DECOMP.md:135 reads 'OP-s-8 --[DP + PITR read ON per table]--> OP-s-9 (snapshot-then-delete), OP-s-11 (s.9 item 5)'. The bracket text IS the predicate the downstream cells wait on, and it names deletion protection and point-in-time recovery. It does not name a key, an alias, or an encryption state.",
      "THE PREDICATE MEASURED LIVE, 5 OF 5, DENOMINATOR PRINTED: describe-table DeletionProtectionEnabled and describe-continuous-backups PointInTimeRecoveryStatus, per table -- opal-users-v2 True/ENABLED; opal-partner-49financial True/ENABLED; opal-partner-cottonwood True/ENABLED; opal-partner-inflection True/ENABLED; opal-partner-demo True/ENABLED. Five of five on both settings. The cell's own acceptance bound is 'denominator 5 real+demo' and this is that denominator.",
      "FWD-8's DONE WHEN AGREES AND IS ALSO ABOUT PROTECTIONS, NOT KEYS: PRD:116-118 reads 'FWD-8 The tables holding logins and partner roles cannot be deleted by accident and can be rewound after a mistake / DONE WHEN APPLIED -- the protections are switched on for every such table'. 'Deleted by accident' is deletion protection and 'rewound' is PITR. An encryption key changes neither property.",
      "C-13 DOES NOT REACH THESE TABLES, READ IN FULL AT PRD:459-470: 'C-13 KEY (v0.5) ONE customer-managed KMS key for this project, alias alias/opal-security ... it is the key C-8 and C-9 name' and 'binds FWD-16/18 violated by: SSE-S3 or the AWS-managed key at APPLIED on EITHER RESOURCE at the close'. The two resources are C-8's opal-security-evidence bucket and C-9's opal-suspicious-addresses table. opal-users-v2 and the partner tables are named in neither, so no constraint is violated by their current key.",
      "NEGATIVE CONTROL ON THE READ, so a clean pass is distinguishable from an unexercised one: opal-suspicious-addresses -- the C-9 table that IS constraint-bound -- returns KMSMasterKeyArn 64f25291-4015-42c5-ad41-40e42325deb7 on the same instrument in the same sweep, while all five S8 tables return 86cc6c40-2387-4446-b7e1-de79392e06b3. The instrument therefore discriminates between the two keys and is not returning a constant.",
      "WHY THE FACE'S READING IS UNDERSTANDABLE AND STILL WRONG: the decomp cell's round-2b PARAGRAPH does declare 'ROUND 2b IS THE OPEN LIMB ... the CMK alignment after OP-s-25', so the alignment is genuinely open work and this row does not dispute that. The error is the step from 'OP-s-8 has an open limb' to 'therefore OP-s-9 and OP-s-11 are blocked'. The edge is not gated on the CELL being DONE; it is gated on a NAMED PREDICATE, and that predicate is met."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): FILED BEFORE ANY WRITE, and the direction matters: this row RELEASES work rather than blocking it, which is why it is class OBSERVATION but hazard_standing ARMED -- left alone, two ready outcomes stay parked behind a face they do not depend on, and nothing in the fabric would ever say so. Six lanes are working this project tonight and the issuer's own words are that this limb is what those two outcomes wait on; that belief, not the tables, is the thing costing time. THIS ROW DOES NOT CANCEL THIS SEAT'S FACE. The CMK alignment stays authorized by the decomp's round-2b declaration and this seat is executing it; the correction is narrow and specific -- it is about what DEPENDS on the alignment, not about whether the alignment is wanted. WHAT THIS SEAT DID NOT DO: it did not read PRD s.9 item 5 itself, which is the clause the face cites for the sequencing. If that clause sequences S9 after S8 on cell COMPLETION rather than on the edge predicate, then the PRD and the decomp edge disagree with each other and the disagreement is the finding rather than this row's reading of it -- that is the issuer's call and is named here so it is not silently assumed away.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S104",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THREE PREMISE DEFECTS IN THE FACE, FOUND BY THE RE-GROUNDING IT MANDATED: (1) the Lane names portal-auth/dynamodb.tf as a carrier but opal-users-v2's REAL carrier is shared-infra/dynamo.tf -- its portal-auth block was deleted in the 2026-06-26 twin-dedup and round 1 of THIS project already applied there; (2) the table set is FIVE, not the three the face quotes -- opal-partner-cottonwood and opal-partner-inflection are equally on the AWS-managed key and unnamed; (3) round 2a's ACCEPTED artifact partner-firms/demo.tf:21-25 records a deliberate decision NOT to move the partner tables to the project CMK, citing that the module is SHARED and C-13 binds only the two resources it names.",
    "evidence": [
      "CARRIER DEFECT, TWO INDEPENDENT CARRIERS AGREE: shared-infra/dynamo.tf:15-16 declares resource 'aws_dynamodb_table' 'opal_users_v2' with name = 'opal-users-v2'. portal-auth/dynamodb.tf declares SEVEN tables -- opal-firms, opal-sessions, user-permissions, opal-offices, opal-users, opal-portal-auth-throttle, opal-portal-auth-mfa -- and opal-users-v2 is NOT among them. The removal is recorded: change_management/20260626T1748Z_opal-users-dedup-v2_and_v1-retire_REMEDIATION_PLAN.md:13 states 'The SAME physical table opal-users-v2 is declared in TWO terraform roots' and :32 prescribes deleting the portal-auth block.",
      "AND THIS PROJECT ALREADY ACTED ON THE CORRECT CARRIER THIS MORNING: change_management/20260903T0929Z_opsec-s8-users-v2-deletion-protection_deploy_completion.md names the deploy as 'deletion_protection_enabled on opal-users-v2 at its REAL carrier shared-infra/dynamo.tf, SCOPED -target apply'. Round 1 of this same cell used shared-infra; the round-2b face reverted to the stale carrier list.",
      "SET DEFECT, FROM A LIVE READ WITH ITS DENOMINATOR: list-tables returns 38 tables with LastEvaluatedTableName absent, so 38 is a true denominator and not a page count. Four tables match opal-partner-* -- 49financial, cottonwood, demo, inflection -- and all four report SSEType KMS on 86cc6c40-2387-4446-b7e1-de79392e06b3. With opal-users-v2 that is FIVE tables on the AWS-managed key. The face's 'READ LIVE AT THIS CUT' block names only opal-users-v2, opal-partner-demo and opal-partner-49financial.",
      "THE UNNAMED TWO ARE NOT INERT: opal-partner-cottonwood and opal-partner-inflection are real client firms' identity tables, instantiated from the same module as the two the face does name (partner-firms/cottonwood.tf:11-14 and inflection.tf:11-14, both module '../modules/partner-firm-table'). A face that flips 'the partner tables' while naming two of four either under-delivers or silently exceeds its own enumeration.",
      "THE SCOPE CONFLICT, QUOTED FROM AN ARTIFACT THAT WAS ACCEPTED AT L6: partner-firms/demo.tf:21-25 reads 'NOT MOVED TO THE PROJECT CMK, deliberately (face item 4): the module declares SSE with no key input, so pointing the demo table at alias/opal-security would mean changing the SHARED module and touching 49financial, cottonwood and inflection -- three real firms' identity tables -- for one demo tenant. C-13 binds the two resources it names and this is not one of them.' That is TO-OP-S-16-17-8R2, COMPLETE @976e405a89.",
      "THE MODULE IS IN FACT SHARED AND KEYLESS, CONFIRMED AT SOURCE: modules/partner-firm-table/main.tf:47-49 is 'server_side_encryption { enabled = true }' with no kms_key_arn argument and no variable for one; variables.tf declares exactly one variable, firm_id. All four firm files instantiate that single module. As written, any key change to the module moves all four tables in one apply -- which is precisely what the face's own deliverable 3, 'ONE TABLE FIRST, then the rest', forbids.",
      "THE DECOMP IS ITSELF SPLIT ON THE SCOPE, and this is why it is a question and not a defect this seat can settle: the OP-s-8 round-2b PARAGRAPH cites three tables as evidence 'the alignment has NOT happened', while the same cell's depends_on column scopes the work to 'OP-s-25 (round 2, the demo table's CMK alignment after its import)' -- one table. The narrative and the dependency field disagree about how wide round 2b is."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHAT THIS SEAT IS DOING ANYWAY, so the row is not read as a full stop: opal-users-v2 is unambiguous and is being executed now. It has its OWN resource block, shares no module with any other table, sits at a carrier this project already applied to today with a known-good -target-plus-unscoped-re-plan precedent, and round 1 left an explicit note at shared-infra/dynamo.tf:65-69 -- 'this resource block declares no server_side_encryption, while the LIVE table is SSE-KMS on the AWS-managed key ... Do not tidy it without reading row Z-S3 first' -- which is exactly this face's authorization, read. That is the ONE TABLE FIRST the face asks for and it is genuinely first, not merely first-listed. THE PARTNER HALF IS WHAT THIS ROW HOLDS. The clean remedy is small and this seat can build it on a word: add an optional kms_key_arn variable to the module defaulting to null, so each firm file opts in independently and the four tables stop moving as one unit. That converts the objection in demo.tf from structural to a per-firm choice and restores ONE TABLE FIRST. It is NOT built unasked, because it changes a module backing four live client identity tables and the issuer has not been given the chance to say whether four real firms are in scope when C-13 does not reach them. THE HONEST RESIDUAL: this seat did not read row Z-S3 itself -- it is cited by shared-infra/dynamo.tf:68 as holding 'the key question' at 1.0.0_SA_CTO~Z, and the face describes the AWS-managed key as 'the ruled INTERIM of row Z-S3'. Both descriptions are consistent with proceeding, and neither was verified against the row's own text.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S106",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "ONE SHAPE, FIVE INSTANCES, THREE TASK ORDERS: A CONTROL THAT IS DEPLOYED, WELL-FORMED, HEALTHY ON EVERY CONFIGURATION PROBE, AND HAS NO EFFECT. An authorizer whose key can never arrive (Z-S83, the only one that SHIPPED); an SNS topic with no subscriber (Z-S97); an alarm dimensioned so it matches no metric (Z-S98 trap B); a distribution no visitor traverses (Z-S101); an ACL whose only enforcing rule matches an empty set (Z-S102). EACH SEAT NAMED THE SHAPE INSIDE ITS OWN FACE AND TWO CITED EACH OTHER, BUT NOBODY HAS STATED IT AS A PROPERTY OF THE ROUND. THE COMMON CAUSE IS ONE SENTENCE, and Z-S98 wrote it best: for a control of this kind every configuration-plane probe is ANTI-CORRELATED with what you want to know, because the failure lives in whether the thing MATCHES or REACHES, and no describe-* call observes either.",
    "evidence": [
      "THE FIVE, each cited to the row that established it and none re-measured here: Z-S83 -- GET /metadata/yang gated by an authorizer keyed on a header CloudFront injects, on a route with no CloudFront behavior at any depth. Z-S97 -- the login-abuse SNS topic, buildable and alarm-wired with no subscriber, where describe-alarms shows AlarmActions populated and the alarm will transition on the burst and nobody is told. Z-S98 trap B -- CloudFront-scope WAF rule metrics carry no Region dimension, so an alarm written with one sits in INSUFFICIENT_DATA permanently. Z-S101 -- a distribution built while the apex stays on GoDaddy, so it serves no visitor while get-distribution and get-web-acl read complete. Z-S102 -- managed groups mandated to Count and both IP sets empty by design, leaving the absent source-restriction rule as the only mechanism that could refuse anything.",
      "THE DENOMINATOR AND THE ONE THAT SHIPPED: five instances across three task orders (TO-OP-S-2, TO-OP-S-6, TO-OP-S-13). FOUR were caught BEFORE the first write by the phase-1 re-grounding their faces mandate. Exactly ONE reached the applied world -- Z-S83's, attached at 16:24:34Z and found hours later by a backward read, because TO-OP-S-2 was already complete and accepted with every criterion PASS.",
      "AN INSTANCE IS EXPRESSLY EXCLUDED FROM THE COUNT, because a class row that inflates its own denominator is the defect it describes: Z-S98's trap A (a JSON metric-filter pattern allegedly matching zero against a Text-format log) WAS WITHDRAWN by its own author at Z-S99, which measured the opposite with aws logs test-metric-filter plus a negative control. It is not one of the five. Z-S99 also showed the proposed substring remedy was the LOOSER instrument, so the correction ran in the direction that tightened the control.",
      "WHY THE SHAPE IS STRUCTURAL RATHER THAN FIVE COINCIDENCES: in every instance the control's CONFIGURATION is correct and its EFFECT depends on a second fact the configuration plane does not carry -- a subscriber, a matching dimension, a routing path, a non-empty set, a header the edge can inject. CLAUDE.md Rule 22's STATE axis names it in general (DESIRED is not APPLIED is not EXERCISED); what this round adds is the measured frequency in ONE project and the observation that the missing second fact is different every time, which is why a per-face check keeps finding it late and a per-face fix cannot generalise.",
      "THE PROCESS FINDING, which is the part that should reach L10 and is the most useful thing here: the instrument that caught four of five was the same one each time -- a MANDATED PRE-WRITE RE-GROUNDING in phase 1, with the face instructing the assignee to STOP and file on any difference. It also produced Z-S103's and Z-S104's premise defects and Z-S100's single-slot gate on the same night. A process control with that hit rate in one round is worth stating as a measured result rather than a habit."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHAT THIS ROW IS FOR AND WHAT IT IS NOT. It is NOT a criticism of any face or seat -- every instance was found and correctly stated by the seat that owned it, three of the five by workers halting before writing anything, and two authors corrected their own rows within the hour. It is NOT an adjudication; L9 is not open and no disposition is set on any cited row. It exists because the cross-face read is L8's job and no single face can perform it: each seat saw one instance and could only say 'this is the same shape as Z-S97', which is true and does not produce a denominator. THE ONE THING THIS SUGGESTS FOR L10, offered and not ruled, because acceptance design is 2.0.0_SA_COO~Z's at L6 and endpoint shape is 1.0.0_SA_CTO~Z's at L2/L4: A FACE THAT BUILDS A CONTROL SHOULD CARRY AT LEAST ONE CRITERION THAT ONLY AN EXERCISED CONTROL CAN SATISFY. This round already contains the model -- S6-AC2's staged burst is graded on the alarm TRANSITIONING rather than on the rule existing, and S2-AC2's probe pair is graded on a refusal at one address and an admission at the other. Both are exercise criteria and both discriminate; the configuration criteria beside them do not. The cost is one exercise per control face and the non-application is a control whose exercise would itself be destructive or would require an unauthorised probe -- in which case the honest filing is UNVERIFIABLE-BY-INSTRUMENT with the reason, which this round has also demonstrated. THE SENTENCE WORTH KEEPING, and it is the assignee's rather than this seat's: every configuration-plane probe of such a control is ANTI-CORRELATED with the question, because the more completely the control is inert the more perfectly its configuration reads correct.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S107",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "THE CONSUMER SET IS FOUR, NOT TWO -- AND ONE OF THE FOUR IS THE SIGNER ITSELF, WHICH THE FACE DOES NOT MENTION AT ALL. Measured, not inherited: 5 roles grant the read (not 2), across 221 roles scanned; the true upper bound is 31 live functions (not 25); 4 of 29 scannable deployed artifacts contain the secret id; and CloudTrail shows 3 of them calling GetSecretValue on it in a 30-hour window, all 4 invoked within the last 10 minutes. THE TWO THE FACE NAMES ARE auth-validator-edge and opal-portal-authorizer. THE TWO IT DOES NOT: opal-session-analytics, and opalinvest-auth-handler -- WHICH READS THE PRIVATE KEY AND THE PUBLIC KEY IN THE SAME ARTIFACT, making it the token ISSUER. A signing-key rotation that teaches two verifiers a second slot and never touches the signer has not been designed. Z-S105's upper bound of 25 was itself understated because it excluded lambda-edge-execution-role -- the role carrying auth-validator-edge, one of the face's OWN two named consumers.",
    "evidence": [
      "THE GRANTING-ROLE SET IS 5, MEASURED RATHER THAN INHERITED. aws iam get-account-authorization-details (filter Role + LocalManagedPolicy + AWSManagedPolicy), explicit pagination, ONE page, no continuation token: 221 roles and 50 managed policies scanned. Evaluating every inline and attached policy statement for Effect=Allow on secretsmanager:GetSecretValue against the exact ARN arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/auth/jwt-public-key-Z6dqNK (with wildcard expansion on both action and resource) returns FIVE granting roles of 221: lambda-edge-execution-role (inline lambda-edge-secrets-logs), lambda-execution-role (inline OpalAuthSecretsAccess), opal-portal-lambda-role (inline opal-sessions-secrets and SecretsManagerAccess), opalinvest-auth-lambda-role (inline opalinvest-auth-permissions), portal-auth-lambda-role (inline jwt-public-key-secret).",
      "SO THE UPPER BOUND IS 31, NOT 25. Live function counts on those five roles, from aws lambda list-functions with explicit pagination -- ONE page, 201 functions, NextMarker ABSENT, so 201 is a denominator and not a page: lambda-edge-execution-role 5, lambda-execution-role 13, opal-portal-lambda-role 12, opalinvest-auth-lambda-role 1, portal-auth-lambda-role 0. Total 31. The 13 and the 12 reproduce Z-S105's figures exactly; the other three roles are additional.",
      "THE ROLE Z-S105 MISSED CARRIES THE FACE'S OWN NAMED CONSUMER. auth-validator-edge holds arn:aws:iam::313476888478:role/lambda-edge-execution-role, which is not one of the two roles that produced the bound of 25 -- so the stated upper bound structurally excluded one of the two consumers the face names. That role's inline policy lambda-edge-secrets-logs allows secretsmanager:GetSecretValue on arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/auth/* -- a PREFIX WILDCARD that also covers opal/auth/jwt-private-key and opal/auth/origin-verify.",
      "CODE PLANE -- 4 READERS of 29 scannable artifacts. Every live function on all five granting roles had its DEPLOYED artifact downloaded from Lambda (get-function Code.Location) and every member file searched for the literal string 'opal/auth/jwt-public-key'. HITS: opal-portal-authorizer (index.mjs), auth-validator-edge (index.mjs), opal-session-analytics (auth.js, in a 3,827-file bundle), opalinvest-auth-handler (dist/index.mjs). NO HIT on the other 25 scanned, including opal-portal-rest-authorizer and the four other edge-role functions.",
      "LIVE PLANE -- CloudTrail, and it does NOT return the same set. aws cloudtrail lookup-events EventName=GetSecretValue, explicit pagination, 40 pages / 2,000 events, MORE PAGES REMAIN so this is a PARTIAL PAGE AND NOT A DENOMINATOR, covering 2026-09-02T13:39:48-04:00 to 2026-09-03T19:50:12-04:00. Of those, 822 name opal/auth/jwt-public-key, from four principals: assumed-role/lambda-edge-execution-role/us-east-1.auth-validator-edge 680, assumed-role/opalinvest-auth-lambda-role/opalinvest-auth-handler 90, assumed-role/opal-portal-lambda-role/opal-portal-authorizer 50, and user/Andrew_Berman 2 -- THE LAST TWO ARE THIS SEAT'S OWN determinism runs from the TO-OP-S-10 investigation, which is worth stating because it shows the instrument is live and catching reads, including mine.",
      "THE TWO PLANES DISAGREE ON ONE MEMBER, WHICH IS THE POINT OF RUNNING BOTH. opal-session-analytics appears in the CODE plane and NOT in the CloudTrail window. It is not dormant: its log group's newest event is 2026-09-03T23:55:06.619Z, minutes before this row. So the absence is explained by its own key caching plus a partial 30-hour window, NOT by the function being unused -- and a source census alone would have called it a consumer while a CloudTrail census alone would have missed it. Newest log events for the other two non-edge readers at the same moment: opalinvest-auth-handler 2026-09-03T23:50:08.446Z, opal-portal-authorizer 2026-09-03T23:54:50.315Z. All live.",
      "THE FOURTH READER IS THE SIGNER, AND THIS IS THE FINDING THAT MOST CHANGES THE FACE. opalinvest-auth-handler's deployed dist/index.mjs contains BOTH 'opal/auth/jwt-private-key' (x1) and 'opal/auth/jwt-public-key' (x1). The private key is the signing material -- TO-OP-S-10's own subject. A component that holds the private key is the token ISSUER, not merely a verifier, and no part of TO-OP-S-10 or TO-OP-S-10B names it.",
      "WHAT THESE INSTRUMENTS CANNOT SEE, stated because S10B-AC0 requires it. (i) TWO of the 31 are PackageType=Image (news-semantic-clustering, ECR news-semantic-clustering:latest; opal-news-ai-sentiment, ECR finbert-lambda:latest). get-function returns no zip for them, so the code-plane instrument is STRUCTURALLY BLIND to those two and 29 is the scanned denominator, not 31. (ii) The CloudTrail read is a partial page over ~30 hours; absence from it is not evidence of non-use, which the session-analytics case demonstrates concretely rather than hypothetically. (iii) A string search finds a LITERAL secret id; a consumer that composes the id at runtime, reads it from an environment variable, or receives the key by another path would not hit. (iv) The census covers LAMBDA only -- EC2, ECS, and human principals holding these roles or other grants are outside it, and one human principal (this seat) already appeared in the live plane. (v) Reading a secret is not the same as using it to VERIFY a JWT; the four hits are readers of that secret, and whether each verifies with it was not established per-function beyond the two consumers TO-OP-S-10 read at source on three planes."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS A STOP AND NOT A WIDENING. S10B-AC0 reserves the re-cut to the issuer in terms, so nothing was taught, built, or deployed. THE SHAPE, AND IT IS THE SAME SHAPE TWICE IN ONE FACE: a check scoped to the MEMBERS cannot see a defect in what the members SHARE. TO-OP-S-10 read two FUNCTIONS and the capability sat on the ROLES beneath them -- that was Z-S105's correction. This row is the same error one level up: Z-S105 read two ROLES and the granting set was never censused, so the bound it derived excluded a role carrying one of the original two consumers. The remedy in both cases is the same and is the one CLAUDE.md prescribes -- ask what the members have in COMMON and check THAT on its own, then re-read the population UNSCOPED. The unscoped read here is get-account-authorization-details over all 221 roles, and it cost one call. WHAT THIS MEANS FOR THE BUILD, offered as the assignee's reading and not as a decision. The face's two deliverables are still correct and still necessary; what changes is their SCOPE and possibly their ORDER. Teaching two verifiers a second slot while the ISSUER is untouched does not make FWD-10 achievable: at the rotation the issuer must begin signing with the new key, and nothing in either face names the component that would do that. So the natural re-cut is (a) settle whether opalinvest-auth-handler is the live login issuer or a legacy path -- it read the public key 90 times in 30 hours and logged 10 minutes ago, so it is not dormant either way; (b) decide whether opal-session-analytics needs the slot or merely tolerates the rotation, since it verifies tokens rather than issuing them; and (c) size deliverables 1 and 2 against the resulting set rather than against 2. THE INSTRUMENT LESSON WORTH KEEPING: the two planes disagreed on exactly one member and that disagreement is the whole value of running both. A source census alone calls opal-session-analytics a consumer with no evidence it ever runs; a CloudTrail census alone omits it entirely and would have shipped a three-consumer answer that looked measured. The log-group timestamp is what reconciles them, and it is a third instrument neither plane contains. NEITHER PLANE IS THE ANSWER, and the face said so before I started.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S109",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "THE EDGE ROLE CAN READ THE PRIVATE SIGNING KEY AND HAS NO NEED OF IT. lambda-edge-execution-role's inline policy lambda-edge-secrets-logs allows secretsmanager:GetSecretValue on arn:...:secret:opal/auth/* -- a PREFIX WILDCARD that covers opal/auth/jwt-private-key and opal/auth/origin-verify as well as the public key the edge actually uses. The role carries FIVE functions, and the code-plane census shows only ONE of them reads any opal/auth secret at all: auth-validator-edge, which needs the PUBLIC key only. The other four -- cache-control-injector, public-data-router, shared-advisor-router, shared-advisor-router-response -- hold the grant and read nothing. ROUTED, NOT ACTED ON: the rotation must not be coupled to a permission change on a live edge role.",
    "evidence": [
      "THE GRANT, read from the live policy: aws iam get-role-policy --role-name lambda-edge-execution-role --policy-name lambda-edge-secrets-logs returns Effect Allow, Action ['secretsmanager:GetSecretValue'], Resource 'arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/auth/*'. The role's other inline policies are lambda-edge-ownership-map-read and lambda-edge-sns-alert; its only attached managed policy is AWSLambdaBasicExecutionRole.",
      "WHAT THE WILDCARD COVERS BEYOND THE NEED: opal/auth/jwt-public-key (used), opal/auth/jwt-private-key (the SIGNING material -- TO-OP-S-10's subject), and opal/auth/origin-verify (OP-s-3's two-slot origin secret). Three secrets reachable where one is required.",
      "WHO HOLDS IT: lambda-edge-execution-role carries FIVE live functions per list-functions (201 functions, NextMarker ABSENT -- a denominator, not a page): auth-validator-edge, cache-control-injector, public-data-router, shared-advisor-router, shared-advisor-router-response.",
      "WHO ACTUALLY READS: the code-plane census downloaded all five DEPLOYED artifacts and searched every member file for 'opal/auth/jwt-public-key'. Exactly ONE hit -- auth-validator-edge (index.mjs). The other four contain no reference. The negative is real because the instrument found the positive in the same sweep.",
      "AND auth-validator-edge NEEDS THE PUBLIC KEY ONLY: its single jwt.verify at index.mjs:235 @998c79b970 takes the public key; it holds no signing path and the string 'opal/auth/jwt-private-key' does not appear in its deployed bundle."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS ROUTED AND NOT ACTED ON, which is 2.0.0_SA_COO~Z's call and this seat agrees with it: narrowing opal/auth/* to the public key ARN would be a permission change on a LIVE edge role during a face whose whole purpose is to make a signing-key rotation safe. Coupling the two means a rotation failure and an IAM failure become indistinguishable, and the edge is replicated so a bad policy propagates before it is observed. THE SEQUENCING ARGUMENT, offered as the reason it is INERT rather than merely deferred: the wildcard grants READ on the private key, it does not grant WRITE on anything, and no function on that role reads it today. So the gap does not widen at rotation and nothing about TO-OP-S-10 or TO-OP-S-10B makes it more dangerous than it is now. It is a standing least-privilege item, correctly separable. ONE THING WORTH CARRYING TO WHOEVER TAKES IT: the natural fix is to split the statement so auth-validator-edge keeps GetSecretValue on the public-key ARN and the other four lose it entirely -- but the four sharing this role is itself the question, because a role carrying five functions with one function's needs is the shared-dependency shape this project has now met three times tonight at three different levels (functions under roles, roles under a granting set, and now permissions under a shared role). Whoever narrows it should ask whether the ROLE should be split before asking whether the STATEMENT should be.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S110",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "THE THIRD VERIFIER CANNOT BE DEPLOYED THROUGH THE NORMAL PATH AND ALSO HAS NO TTL -- TWO THINGS THE RE-CUT DOES NOT YET ACCOUNT FOR. opal-session-analytics' lambda-source-map entry is WRONG ON THREE AXES: it declares source_dir 'EXTERNAL' with the note 'No repo source' while the source EXISTS at infra/aws/opalinvest_dev/lambda/session-analytics/src/, declares runtime python3.11 while the live function is nodejs20.x, and declares files [] so a CI zip build would package NOTHING. AND ON THE FACE'S OWN SUBJECT: its key cache is 'if (cachedPublicKey) return cachedPublicKey' with NO TTL -- the same defect as opal-portal-authorizer -- so deliverable 2's TTL limb covers TWO consumers, not one as written.",
    "evidence": [
      "THE SOURCE-MAP ENTRY, read at HEAD from infra/aws/lambda/ci/lambda-source-map.json (204 functions in the map): opal-session-analytics carries source_dir 'EXTERNAL', files [], runtime 'python3.11', pipeline 'portal-auth', and the note 'No repo source. Portal session analytics. Code must be downloaded from AWS.' It carries no artifact_sha256, no tf_file and no tf_resource.",
      "AXIS 1 -- 'No repo source' is FALSE. infra/aws/opalinvest_dev/lambda/session-analytics/ exists and contains src/auth.ts, src/index.ts, src/types.ts, plus package.json, tsconfig.json, deploy.sh and a client/ directory.",
      "AXIS 2 -- the runtime is WRONG. aws lambda get-function-configuration on opal-session-analytics returns Runtime 'nodejs20.x', Handler 'index.handler', CodeSha256 eQswWf3zdISgafQwQ+GhHgyWNfoxPOSeriqYVxiN9VU=, CodeSize 3,721,601, LastModified 2026-01-08T15:31:07Z. The map says python3.11.",
      "AXIS 3 -- files [] means a CI zip build packages nothing. The estate has already recorded what that produces: originVerify.mjs:15-20 warns that a module absent from the files array 'is not packaged into the artifact, and the deployed handler throws MODULE_NOT_FOUND at cold start on EVERY invocation.' Here the array is empty entirely.",
      "THE REPO SOURCE IS THE BUILD INPUT, established by CONTENT rather than by filename per Rule 22a: the deployed bundle's auth.js is the compiled image of the repo's src/auth.ts, function for function -- 'let cachedPublicKey = null', 'async function getJwtPublicKey()', 'if (cachedPublicKey) return cachedPublicKey', the same GetSecretValueCommand on 'opal/auth/jwt-public-key', the same 'JWT public key not found' throw, and the same JWT_ISSUER 'opal-portal-auth' / JWT_AUDIENCE 'opal-portal-api' constants. So the map's 'code must be downloaded from AWS' is not merely stale, it points away from a source tree that is demonstrably the origin of the deployed bytes.",
      "AND THE FACE'S OWN SUBJECT, MEASURED ON BOTH PLANES: repo src/auth.ts:42-56 is 'async function getJwtPublicKey(): Promise<string> { if (cachedPublicKey) return cachedPublicKey; ... }' -- one scalar, no time component. The deployed auth.js carries the identical logic. opal-session-analytics is therefore a SINGLE-SLOT consumer WITH NO TTL, the same pair of defects Z-S100 found in opal-portal-authorizer.",
      "IT IS LIVE AND IT IS STALE AT THE SAME TIME: last modified 2026-01-08, roughly eight months ago, while its log group's newest event is 2026-09-03T23:55:06.619Z. It is being invoked now and running code from January."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS FILED BEFORE ANY CODE WAS WRITTEN. Phase 1 of the face directs a pre-write read of each consumer's build path, and this is what that read returned. Writing the two-slot change for opal-session-analytics first and discovering at deploy time that the CI packages an empty zip would have been the expensive ordering, and on a function that is invoked continuously. THE SCOPE QUESTION IS THE ISSUER'S AND THIS SEAT DID NOT ASSUME IT. Two readings are open and they differ in work: (a) opal-session-analytics gets the full treatment -- two slots AND a TTL -- which requires the source-map correction first and makes it a three-artifact face; or (b) it gets the two-slot read only, on the argument that a verifier which never converges is still safe during an overlap window and merely stale afterwards. (b) is weaker than it sounds and this seat recommends (a): without a TTL that consumer holds the retired key indefinitely, so at the NEXT rotation after this one it is exactly the unbounded-cache failure the project has already named twice -- the fix would have to be done anyway, later, under time pressure, on a consumer nobody remembered. THE SOURCE-MAP DEFECT IS THE MORE GENERAL FINDING. Rule 4 states the map PAIRS a Lambda with its repo dir and explicitly does NOT compare deployed bytes to built-from bytes. This entry fails at the pairing itself, which is the one thing the map is for -- and it fails in the direction that is hardest to notice, because 'EXTERNAL / no repo source' reads as a deliberate, documented exclusion rather than as an error. A wrong pairing that looks like a policy decision will outlive one that looks like a bug.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S111",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Z-S110's BROKEN ENTRY IS A GENUINE SINGLETON AND THE REGISTRY IS NOT ROTTEN -- which makes that row STRONGER, not weaker. Unscoped census of all 204 entries in infra/aws/lambda/ci/lambda-source-map.json against 201 live functions: 181 CLEAN on all four axes; source_dir missing on disk ZERO; and `files: []` is NOT A DEFECT CLASS AT ALL -- all 12 are explained, 9 declared EXTERNAL and 3 PackageType=Image, RESIDUAL ZERO. Of THREE runtime mismatches, two are same-language point-version drift (python3.12-vs-3.11 and its mirror). OPAL-SESSION-ANALYTICS IS THE ONLY ENTRY IN 204 WHOSE DECLARED RUNTIME IS A DIFFERENT LANGUAGE FROM THE LIVE FUNCTION -- python3.11 declared, nodejs20.x live. The remaining real residual is 9 entries naming functions that no longer exist.",
    "evidence": [
      "THE CENSUS IS UNSCOPED AND COMPLETE, not a sample: every one of the 204 entries in the map's `functions` object evaluated against the 201 live functions from aws lambda list-functions (NextToken ABSENT, so 201 is a denominator and not a page). Four axes per entry -- does a live function of that name exist, does the declared runtime match the live runtime, does source_dir exist on disk, is `files` empty. Map vintage from its own header: _updated 2026-08-21T20:39:07Z.",
      "THE RESULT THAT PREVENTS AN OVER-REACTION: 181 of 204 clean on all four axes, and source_dir MISSING ON DISK is ZERO of 204 -- every non-EXTERNAL entry points at a directory that exists. The registry is maintained, not abandoned.",
      "AND A DEFECT CLASS THIS SEAT'S OWN FIRST PASS INVENTED, corrected before filing: the first census reported 12 entries with `files: []` as a defect. Refining it dissolves the class entirely -- 9 of the 12 declare source_dir EXTERNAL, for which an empty file list is CORRECT, and the other 3 (ycharts-session-capture, news-semantic-clustering, opal-news-ai-sentiment) are PackageType=Image, which have no zip source by construction and whose blindness Z-S107 had already recorded. RESIDUAL ZERO. Reporting the raw 12 would have manufactured a finding out of a correctly-populated registry.",
      "THE THREE RUNTIME MISMATCHES, SEPARATED BY GRAIN BECAUSE THEY ARE NOT ONE CLASS: opal-assets-daily-emitter declares python3.12 and runs python3.11; opal-bd-transaction-consolidator declares python3.11 and runs python3.12. Both are SAME-LANGUAGE point-version drift and a CI zip built from either would still be loadable. opal-session-analytics declares python3.11 and runs nodejs20.x -- a DIFFERENT LANGUAGE, and the only one of 204. A zip built from that entry could not run under the live runtime at all, which is what makes Z-S110's third axis load-bearing rather than cosmetic.",
      "THE ONE REAL RESIDUAL BEYOND Z-S110'S SUBJECT, offered so the cleanup is sized: 9 entries name functions with NO live counterpart -- bd-client-detail, four find-insure-serving-* entries, m365-ms-ingest-liveness, m365-otp-liveness, smartx-ec2-autostart and one more. Stale rather than wrong: they cannot mis-build anything because there is nothing to deploy to. Recorded, not escalated, and NOT this project's to clean."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS SHARPENS Z-S110 RATHER THAN QUALIFYING IT. A reader could take 'wrong on three axes' as evidence the registry is unreliable and discount it as one more stale record in a rotten file -- which would be the wrong inference and would weaken a correct finding. The census says the opposite: the file is maintained, 181 of 204 are clean, and this entry is a genuine outlier. THE PART THAT MATTERS FOR THE BUILD is narrower than three axes: EXTERNAL-plus-empty-files is the map's ORDINARY way of saying 'no repo source', shared with 8 other entries, so on its own it is a claim to re-examine rather than a defect. The LANGUAGE mismatch is the defect, it is unique, and it means a CI zip built from this entry could not load under the live runtime. THIS SEAT'S OWN NEAR-MISS, recorded because it is the same shape as the night's others: the first pass produced a fourth defect class of 12 entries that dissolved to ZERO on one refinement, because EXTERNAL and Image entries have empty file lists BY DESIGN. A census that does not subtract the legitimate cases manufactures findings, and the direction of that error -- overstating -- is the one that gets caught, which is precisely why it must be caught BEFORE filing and not after. NOTHING HERE IS ROUTED: Z-S110 stays BLOCKING/ARMED with 2.0.0_SA_COO~Z as its owner, and the 9 stale entries belong to whoever owns the map, not to this project.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S112",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "A THIRD live grant on table/opal-users exists outside this face's lane: trade-submission-lambda-role holds dynamodb GetItem/PutItem/UpdateItem/DeleteItem/Query/Scan on arn:aws:dynamodb:us-east-1:313476888478:table/opal-users AND table/opal-users/index/*, declared in a DIFFERENT terraform root (infra/aws/terraform/trade-pipeline/iam.tf:63-64), and that role is the execution role of SEVEN live lambdas -- so removing portal-auth/iam.tf:50-51 does NOT leave the table ungranted, and S9-AC3's 'BOTH GRANTS ARE GONE' is scoped to a denominator of 2 when the measured live denominator is 3 statements across 2 roles.",
    "evidence": [
      "APPLIED plane: comp-iam refresh-census, api iam:GetAccountAuthorizationDetails, account 313476888478, vintage 2026-09-04T00:26:29Z -- 221 roles / 1173 inline statements scanned. Exact matcher table/opal-users(?![-\\w]) -- i.e. excluding -v2/-master/-trade -- returns 2 roles: opalinvest-auth-lambda-role (source inline:opalinvest-auth-permissions) and trade-submission-lambda-role (sid DynamoDBAccess, source inline:trade-submission-policy).",
      "POSITIVE CONTROL on the same census and matcher family: table/opal-users-v2 returns 4 roles (opal-ticket-api-role, opalinvest-auth-lambda-role, partners-lambda-role, trade-submission-lambda-role) -- the matcher fires, so the 2-role result is a measurement and not an empty regex.",
      "DESIRED plane: comp-find 'opal-users($|[^-])' over infra/aws/lambda/trade_pipeline + infra/aws/lambda/v2_portal + infra/aws/terraform/trade-pipeline -- DENOMINATOR 2 hits across 302 files; BOTH hits are the grant itself at infra/aws/terraform/trade-pipeline/iam.tf:63 and :64. ZERO trade-pipeline CODE references the table, so the grant is vestigial-by-code, not load-bearing-by-code.",
      "Seven lambdas carry this role per org/modules/graph/aws-shapes/g2-edge-census-cut1.yaml:179-185 via lambda.Role: trade-auth-handler, trade-authorizer, trade-dashboard-api, trade-identifier-cache, trade-parquet-batch-export, trade-submission-handler, trade-workflow-handler.",
      "Vintage of the repo reads: @9814dd7f50"
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THIS IS THE SCOPED-CHECK SHAPE FROM CLAUDE.md RULE 22, AND IT IS WHY THE UNSCOPED RE-READ IS MANDATED. A check scoped to iam.tf:50-51 verifies those two lines perfectly and certifies the table ungranted, while a grant in a sibling root stays live -- every per-line arm passes and nothing fails. The shared thing the members have in common is THE TABLE ARN, and the census that had to be run on THAT, unscoped across all 221 roles, is the one that found it. NOT A DEFECT IN THE FACE'S REASONING: the issuer inherited the two-ARN model from the cell text, which inherited it from the 2026-06-26 remediation plan, whose Part B was explicitly scoped to portal-auth as the sole manager ('opal_users (v1) is declared ONLY in portal-auth/dynamodb.tf:151-165'). That statement is TRUE about the TABLE RESOURCE and was never a statement about GRANTS -- the grain slipped between 'who declares the table' and 'who is granted on the table' somewhere in the ten weeks between. NOTHING IS BLOCKED ON MY SIDE BY THIS: the portal-auth work proceeds; what is blocked is the WORDING of S9-AC3, which cannot be filed as PASS as written without either the third grant leaving too or the criterion being read against a stated denominator of 2-of-3.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S113",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The us-east-2 opal-users table DOES NOT EXIST -- us-east-2 holds ZERO DynamoDB tables in account 313476888478 -- which resolves a 'status UNKNOWN/deferred' carried since 2026-06-26 and FALSIFIES THE STATED PREMISE of the standing CTO condition-2 that forbade pruning iam.tf:51 ('pruning :51 would revoke the us-east-2 grant ... and would BREAK access if us-east-2 is live'). It is not live. There is nothing to break, so this face's requirement that :50 and :51 leave together does not collide with that condition -- but the condition is a STANDING written record that says the opposite of this task order, and a worker must not silently pick one.",
    "evidence": [
      "aws dynamodb describe-table --table-name opal-users --region us-east-2 -> ResourceNotFoundException (rc!=0).",
      "POSITIVE CONTROL, and the discriminating one: aws dynamodb list-tables --region us-east-2 -> {\"TableNames\": []} on a SUCCESSFUL call (rc=0). The region endpoint answers and the credentials work, so the empty enumeration is a measurement of the region, strictly stronger than a per-name probe that throws. us-east-2 has zero DynamoDB tables at all.",
      "NEGATIVE CONTROL: describe-table on opal-users-zzz-nosuchtable-9999 in us-east-1 returns the SAME ResourceNotFoundException shape, and describe-table on opal-users in us-east-1 returns a live table -- so the instrument distinguishes present from absent.",
      "aws sts get-caller-identity -> account 313476888478, matching ${local.account_id} in the ARN at portal-auth/iam.tf:51 and the live us-east-1 table ARN arn:aws:dynamodb:us-east-1:313476888478:table/opal-users. Same account, so the grant and the absence are on the same plane.",
      "The record being reconciled: org/critical_paths/change_management/20260626T1748Z_opal-users-dedup-v2_and_v1-retire_REMEDIATION_PLAN.md B.1 ('us-east-2 scoping: a same-named opal-users table is GRANTED in us-east-2 (iam.tf:51, status UNKNOWN/deferred)'), B.3.4 (CTO condition-2, leave :51 intact) and its Follow-up section, which asks for exactly this dead-vs-live determination.",
      "Vintage of the repo reads: @9814dd7f50"
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): TWO RECORDS, OPPOSITE INSTRUCTIONS, SAME LINE. The 2026-06-26 plan says LEAVE iam.tf:51; this task order says REMOVE it. Both are reasonable given what each knew: the June plan explicitly conditioned its instruction on 'if us-east-2 is live' and explicitly deferred the determination to a future window, naming it as a follow-up. THIS IS THAT WINDOW AND THIS IS THAT DETERMINATION. The reason it is a row and not a silent proceed is that a worker who just follows the newer document has resolved a conflict between a CTO condition and a COO task order by date order alone, which is not a worker's call to make even when the newer one happens to be right. The measurement, not the recency, is what settles it -- and the measurement is in this row so that the settling is auditable. WHAT THIS ROW DOES NOT CLAIM: it does not claim the us-east-2 table never existed, only that it does not exist at this vintage; CloudTrail management events could answer when it went away and were not consulted, because the retirement decision does not turn on it.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S114",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THE C-14 OPERATOR ROLE GRANTS THE WRONG BUCKET SINCE THE SPLIT: opal-security-admin's policy names opal-data-security -- the LOG DESTINATION -- under Sids that literally read EvidenceStoreObjects and EvidenceStoreBucket, while the actual evidence store is now opal-security-evidence, which the role cannot touch at all. Its KMS grant is CORRECT and points at the project key the NEW bucket uses, so the role can DECRYPT OBJECTS IT CANNOT FETCH. The drift is a consequence of PRD v0.9's split: TO-OP-S-17R-28 re-pointed OP-s-17 to the new bucket and nothing re-pointed the operator grants written before it.",
    "evidence": [
      "DECLARED PLANE: infra/aws/terraform/opsec/iam.tf:69 reads Resource = \"${aws_s3_bucket.data_security.arn}/*\" and :78 reads Resource = aws_s3_bucket.data_security.arn. A census of that file for 'security_evidence' returns 0 hits across 93 lines -- the new bucket is named nowhere in it.",
      "APPLIED PLANE, read live: get-role-policy on opal-security-admin / opal-security-admin-evidence-and-key returns EvidenceStoreObjects -> arn:aws:s3:::opal-data-security/*, EvidenceStoreBucket -> arn:aws:s3:::opal-data-security, ProjectKeyUse -> arn:aws:kms:us-east-1:313476888478:key/64f25291-4015-42c5-ad41-40e42325deb7. Declaration and world AGREE, so nothing drifted between them -- what drifted is the SPEC's meaning of 'the evidence store' underneath both.",
      "THE SIDS ARE THE TELL AND THEY ARE NOW FALSE BY THEIR OWN WORDS: 'EvidenceStoreObjects' and 'EvidenceStoreBucket' name opal-data-security, which PRD v0.9/v0.10 re-designated as the LOG DESTINATION under the new C-16. The evidence store is opal-security-evidence, created 2026-09-03 by TO-OP-S-17R-28 and holding cases/, reports/ and allowlists/.",
      "THE KMS HALF IS CORRECT, WHICH IS WHAT MAKES THE FAILURE QUIET: ProjectKeyUse names 64f25291-4015-42c5-ad41-40e42325deb7, and that IS the key opal-security-evidence encrypts with (SSE-KMS, bucket_key_enabled true, verified on the applied plane at 17:31:32Z). So the role holds a working decrypt grant for a bucket it has no s3:GetObject on. A permissions review that checked the KEY would find nothing wrong.",
      "iam.tf's OWN COMMENT AT :46-49 STATES THE INTENT THAT IS NO LONGER MET: 'PERMISSIONS -- minimal for C-8 and C-13 at this round, and nothing beyond. The evidence store and its objects, plus the project key.' The intent is right and the referent moved underneath it.",
      "WHY IT SURVIVED THE SPLIT: TO-OP-S-17R-28's own bound made opal-data-security READ-ONLY for that face, and its acceptance criteria were scoped to the two buckets' properties and to what the apply changed. Nothing in those criteria looked at who could READ the new bucket, so a correct face with correct criteria could not have caught it."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS ARMED RATHER THAN INERT: the sentinel being built under TO-OP-S-14-21 writes CASE FILES into opal-security-evidence under cases/. The human who investigates a case holds the C-14 operator role. As applied, that operator cannot list or read the case files the sentinel is about to start producing, and the failure surfaces as an AccessDenied at the moment someone is investigating an incident -- the worst time to find a permissions gap. NOT FIXED HERE, DELIBERATELY: the grants are OP-s-26's, that cell is COMPLETE and accepted, and TO-OP-S-14-21's bounds do not extend to editing another cell's role. Editing it inside this face would be the Z-S49 and Z-S60 shape -- an assignee silently widening a resource its face did not name. TWO SHAPES, both the issuer's: re-point the two S3 statements to aws_s3_bucket.security_evidence, a one-line-each change matching the intent iam.tf:46-49 already states; or grant BOTH buckets deliberately if the operator is meant to read raw logs as well as evidence, which is a scope decision rather than a repair. THE REUSABLE PART, and this project has now hit it twice in one day: A SPLIT RE-POINTS THE CELL THAT OWNS THE RESOURCE AND LEAVES EVERY OTHER REFERENCE TO IT BEHIND. C-16's condition drift (Z-S60) and this are the same class -- the split moved what 'the evidence store' MEANS, and artifacts naming it by its old identity kept naming the old thing while reading as if they named the new one. The search that finds this class is not 'what changed' but 'what still points at the thing that moved'. FILING NOTE: this row was written once before, at 00:45Z, and was lost in the id collision that destroyed 2.0.0_SA_COO~Z's Z-S114 -- see msg 20065 and 20074. It is re-filed at Z-S114 on that seat's explicit release of the id (msg 20074), through a write that is now GATED on its own collision check rather than merely reporting one.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S115",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "A GO CONDITION I WROTE DEMANDED A STATE THAT THE GATED WORK ITSELF PRODUCES: TO-OP-S-15-19 was barred until TO-OP-S-22's verdict returned, but TO-OP-S-22 verdicts the APPLIED roles and only TO-OP-S-15-19 creates them -- the two faces named each other as prerequisites and the pair could never start.",
    "evidence": [
      "0.7.0_AE_CloudOps~W msg 20049 STOPPED BEFORE STARTING rather than proceeding past a gate it could not satisfy, and measured both halves from each task order's own status field rather than from any summary: TO-OP-S-4-18 complete = MET, TO-OP-S-22 staged = NOT MET.",
      "NFRA_OPSEC202609.TO-OP-S-22.sentinel-chain-iam-verdict.md:10-12 carries the mirror half -- 'GO CONDITION: TO-OP-S-15-19 has applied its two roles' -- so each face named the other as its prerequisite.",
      "NFRA_OPSEC202609.TO-OP-S-15-19.reconciler-and-unblock-path.md deliverable 5 states the correct sequence (declare and apply the roles, hand the ARNs over, wait for the verdict, then deploy the code) four lines below the gate that contradicted it.",
      "PRD v0.12 @3619ebecd9 s.9 item 7: the verdict runs before any of OP-s-14/15/19 is DEPLOYED, not before they are declared -- so the ordering requirement is real and only its placement was wrong.",
      "0.7.0_AE_CloudOps~T msg 20051 announced a claim BEFORE working and 0.7.0_AE_CloudOps~W stood off, so the two-seats-on-one-face collision my dispatch invited did not actually occur.",
      "channel-commit-guard at 00:47:2xZ read HEAD 113 / worktree 115 / NEW 2 (mine 1, foreign 1), naming a foreign NFRA_OPSEC202609-Z-S114 by 0.7.0_AE_CloudOps~S -- two seats had minted the same id inside one window.",
      "0.7.0_AE_CloudOps~S msg 20065 discloses running git checkout -- on this channel file at ~00:47Z, destroying BOTH uncommitted rows; it checked recoverability rather than assuming it (git fsck --lost-found carries no blob with the id, stash empty, index clean).",
      "git diff --stat on the file immediately after read empty -- the worktree was byte-identical to HEAD 776437a094, confirming both appends were gone with no error raised to either author."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): RESOLVED IN THE SAME TURN IT WAS REPORTED. The gate now reads 'TO-OP-S-4-18 terminal. THAT IS THE WHOLE CONDITION.' The IAM verdict keeps its force where it belongs -- inside deliverable 5, gating the CODE DEPLOY. Nothing about the ordering requirement was weakened; only its impossible placement moved. Both faces were also re-addressed to the seats that claimed them (TO-OP-S-15-19 to ~T, TO-OP-S-22 to ~W, TO-OP-S-14-21 unchanged at ~S), because the face had been issued_to a live peer while I was telling two other seats to take it. THE MECHANISM, because it is not carelessness in the ordinary sense: I worked the sequence out correctly, wrote it into deliverable 5 in full, and then wrote the gate as a RESTATEMENT of the same requirement -- and the restatement lost the sequencing that made the original coherent. A GATE IS NOT A SUMMARY OF THE BODY; IT IS AN INDEPENDENT PREDICATE, AND IT CAN CONTRADICT THE BODY WITHOUT EITHER READING WRONG IN ISOLATION. Both fragments are correct policy; only the pair is impossible. This is the second instance of the class tonight and the first (the Z-S14 bar) is named in the correction on the face. SECOND ERROR IN THE SAME EVENT: the correction first cited 'row Z-S111' before this row existed, and Z-S111 was already 3.0.0_SA_CVO~Z's -- I invented a citation inside the record meant to make the correction auditable, which is the banked 'a named artifact can be a wish, not a reference' class committed inside a fix for a different one. THIRD, AND IT HAPPENED WHILE THIS ROW WAS BEING WRITTEN: this row was first appended as Z-S114 at 00:47:02Z and destroyed at 00:48:40Z by a peer's git checkout, along with that peer's own colliding Z-S114. The peer disclosed it unprompted within minutes and verified irrecoverability rather than asserting it. I take Z-S115 and LEAVE Z-S114 free for that seat rather than re-using a contested id -- a vacant number costs nothing and a second collision costs another lost row. THE OPERATIONAL RULE: append and commit in the SAME breath. An uncommitted row on this shared file has a lifetime measured in seconds, and the read-modify-write shape means the loser of the race is never told. WHAT THIS ROW DOES NOT CLAIM: it does not claim the other faces have been swept for the same self-contradicting-gate defect. TO-OP-S-22's gate was read and is sound (it names applied roles from OTHER faces, which is satisfiable once those faces run). The remaining staged faces have NOT been swept and that sweep is owed.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S118",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "TO-OP-S-20's GO CONDITION COMES BACK NEGATIVE, and BOTH halves of the reason are new. FIRST, the handoff's premise is wrong in the direction that matters: aws-waf-logs-opal-cloudfront -- the group fronting the PORTAL, where sign-ins actually land -- is NOT empty. It holds 2,771 records and 695 EXACT-PATH /auth/login events, against the 2 the gateway source yielded. SECOND, and this is why the face still cannot be built: 680 of those 695 events (97.8%) carry User-Agent opal-s6-probe or opal-s7-probe -- they are THIS PROJECT'S OWN SYNTHETIC TEST BURSTS FROM TONIGHT, self-identified in the log. An allow list built from the only window that exists would allow-list 108.242.96.89, the fabric's own egress address, as if it were a partner office.",
    "evidence": [
      "THE CORRECTION FIRST, because the rest of this row is dangerous without it. Msg-ID 20084 (0.7.0_AE_CloudOps~S handoff) states that aws-waf-logs-opal-cloudfront 'holds storedBytes 0 and was created 2026-09-03' and concludes 'the surface that carries sign-ins has no usable log at all'. THE GROUP IS LIVE. describe-log-streams returns one stream with firstEventTimestamp 2026-09-03T10:20:36Z and lastEventTimestamp 2026-09-04T00:11:25Z, and a get-log-events read returns a well-formed WAF record. storedBytes was the misleading instrument and Z-S93 already established why: it reads 0 at STREAM grain regardless of content. Here it reads 0 at GROUP grain too while the group demonstrably holds records, so on this group storedBytes is not a liveness oracle at either grain. THE WINDOW: 2026-09-03T10:20:36Z to 2026-09-04T01:24:12Z, 15.06 hours.",
      "THE DENOMINATOR, printed by the service rather than summarised: a CloudWatch Logs Insights stats count() over that window returns recordsScanned 2771 and recordsMatched 2771, so 2,771 is the whole population of the window and not a page.",
      "THE EXACT-PATH CENSUS, run on the three portal auth paths taken from the AuthLoginRateLimit scope-down statement rather than guessed: /auth/login, /auth/forgot-password, /auth/reset-password. recordsMatched 695, all of them /auth/login, across exactly 3 distinct client addresses -- 108.242.96.89 (US) 689, 132.196.51.176 (US) 5, 173.79.153.38 (US) 1. Against the gateway source's 2, this source carries 347x more exact-path sign-in traffic. The handoff's conclusion that no usable sign-in log exists does not survive this read.",
      "AND NOW THE PART THAT KILLS THE FACE ANYWAY, MEASURED AND NOT INFERRED -- the traffic identifies itself. A parse of the User-Agent header across the same 695 exact-path events returns: opal-s6-probe 480 hits, opal-s7-probe 200 hits, Python-urllib/3.11 1 hit, 8 unlabelled from 108.242.96.89, plus the 5 and 1 from the two other addresses. 680 of 695 events -- 97.8% -- carry a user-agent that literally names this project's own probes. TO-OP-S-6 (login-abuse alarm) and TO-OP-S-7 (throttle fail-open coverage) both drove staged login bursts tonight; the S-7 deploy ledger records its bursts closing at 20260903T234907Z.",
      "THE TIME DISTRIBUTION AGREES INDEPENDENTLY OF THE USER-AGENT, so this is two instruments and not one: binned at 30 minutes, the 23:30 bin holds 439 events and the 00:00 bin holds 240 -- 679 of 695, or 97.7%, inside a single hour that contains the S-7 ledger's own burst timestamps. The remaining ~15 events are spread thinly across the other ~14 hours. A partner-office sign-in population does not have this shape; a test harness does.",
      "SO THE GENUINE CANDIDATE POPULATION IS AT MOST 15 EVENTS across 3 addresses over 15 hours, and even those are not attributable to a firm -- see the next entry. 689 of the 695 come from ONE address, and that address is the one running the probes.",
      "THE SECOND BLOCKER IS CONFIRMED ON THIS SOURCE TOO, INDEPENDENTLY OF THE GATEWAY. A sampled /auth/login record shows httpMethod POST, args '' (empty), and the complete header set Accept-Encoding, Content-Length, Host, User-Agent, Content-Type, Connection -- NO Cookie and no tenant-bearing field of any kind. The firm-identifying credential travels in the JSON body (Content-Length 84, Content-Type application/json) and WAF does not log bodies. So firm attribution is INEXPRESSIBLE here for the same structural reason the handoff found on the gateway, reached on a DIFFERENT source rather than by repeating that seat's query.",
      "EXPECTED FIRM SET, read live rather than recalled: dynamodb list-tables returns 38 tables with LastEvaluatedTableName absent (so 38 is a true denominator), of which 4 are opal-partner-*: 49financial, cottonwood, demo, inflection. FIRMS OBSERVED WITH AN ATTRIBUTABLE ADDRESS: 0 of 4. Under S20-AC2 all four file as 'log coverage unknown for this path' rather than 'did not sign in during the window', because no field on either source could have attributed them even if they had."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THE TRAP HERE IS A DIFFERENT AND SHARPER ONE THAN Z-S90's, AND THE DIFFERENCE IS THE WHOLE POINT. Z-S90's trap is a SUBSTRING filter admitting an internet scanner, and the remedy is exact-path matching -- correct, and this seat used it. THIS TRAP SURVIVES EXACT-PATH MATCHING. The filter is right, the path is right, the events are genuine HTTP POSTs to the real sign-in endpoint, and the resulting list is small, clean and plausible. Nothing about doing the recommended correct thing catches it. Only a User-Agent census or a time-distribution check separates the estate's own probes from a partner's traffic -- and a seat that had done exact-path matching would reasonably feel it had already handled the census-hygiene problem. DOING THE PRESCRIBED CORRECT THING PRODUCES A MORE TRUSTWORTHY-LOOKING WRONG ANSWER THAN THE LOOSE FILTER DOES. WHY IT IS ARMED RATHER THAN AN OBSERVATION: the first half of this row -- the CloudFront group is live and carries 347x the gateway's sign-in traffic -- reads, on its own, as GOOD NEWS that unblocks the face. A seat that acts on that half alone builds the list from this window and allow-lists the fabric's own egress into the very control C-4 exists to protect, permanently and at the edge. THE TWO HALVES MUST TRAVEL TOGETHER and this row exists to keep them together. WHAT WOULD ACTUALLY MAKE THE CELL BUILDABLE, offered as measurement rather than as a decision this seat may take: sparseness is now a TIME problem on a source that demonstrably works, so a genuine window on the CloudFront group would fix half of it -- but firm attribution would still be missing, and no amount of waiting produces a field that is not emitted. That half needs either a tenant-bearing field added at the edge or a census sourced from something that knows the tenant, and it is 1.0.0_SA_CTO~Z's open C-4 question. THE CENSUS THIS FACE OWES ALSO NEEDS A STANDING EXCLUSION: any future run must exclude the estate's own probe user-agents, or it will re-measure tonight's bursts every time -- the corpus now records its own tests.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S119",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THE opal-users RETIREMENT IS BUILT AND STOPPED AT THE DELETE, WHICH IS THE POINT. Snapshot taken and verified, both portal-auth grants removed and the removal proven on the applied plane, login proven unaffected before and after, the reader census re-run at this seat's vintage across four planes with denominators -- and the table is LEFT STANDING with 12 rows. Dropping it is reserved for a human word and this face does not take it. This row is the carrier that offers the decision.",
    "evidence": [
      "SNAPSHOT (S9-AC2): on-demand backup opal-users-retire-snapshot-20260904T004712Z, arn ...table/opal-users/backup/01788482835630-d66dab03, BackupStatus AVAILABLE, BackupType USER, 12 items, 4506 bytes -- item count and byte size both match the live table exactly. Expiry null (an on-demand backup does not age out).",
      "GRANTS (S9-AC3): commit a7edcf6722 removed portal-auth/iam.tf:50-51; targeted apply returned '0 added, 1 changed, 0 destroyed'; APPLIED-plane get-role-policy before/after shows the dynamodb resource list going 7 -> 5, removing EXACTLY the us-east-1 and us-east-2 table/opal-users ARNs and adding none, with opal-users-v2 and its index still present and the other three ddb statements byte-unchanged.",
      "LOGIN UNAFFECTED (S9-AC3 discriminator): fixture demo@demo.test under OP-x-1 bound (1). BEFORE at 00:53Z: GET /auth/me 200, POST /auth/refresh 200. AFTER at 01:20Z with the SAME refresh token: POST /auth/refresh 200 returning a 775-char accessToken, GET /auth/me 200 with a byte-identical user payload.",
      "CENSUS (S9-AC1), four planes, each with its denominator and its stated blindness: SOURCE comp-find over 51,693 files, zero first-party readers, blind to deployed bytes differing from the repo. APPLIED IAM comp-iam refresh-census, 221 roles / 1,173 inline statements, positive control the v2 ARN returning 4 roles, blind inside 174 UNRESOLVED attached-managed statements across 137 roles. DATA CloudWatch 30d, writes 0.0 on 30 of 30 and reads 0.0 on 28 of 30, blind to WHO. ATTRIBUTION does not exist in this account at all.",
      "TABLE STANDING (S9-AC4): describe-table at 01:24Z reads TableStatus ACTIVE, ItemCount 12, created 2025-12-29; scan --select COUNT reads Count 12 / ScannedCount 12. Nothing was deleted and nothing was written.",
      "The table is terraform-managed in portal-auth/dynamodb.tf:151-165, which is why the delete order above is not a bare delete. Source: the 2026-06-26 remediation plan B.3.4, re-read at this vintage."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): TWO THINGS THE DECIDER SHOULD HAVE, AND NEITHER IS A REASON TO WAIT. (1) THE READER CENSUS IS CLEAN BUT ATTRIBUTION IS STRUCTURALLY UNAVAILABLE. The data plane is not flat-zero: two isolated one-hour read spikes in 30 days, 8.0 RCU on 2026-08-21 and 2.0 RCU on 2026-09-03 at 19:17 EDT, the latter inside this project's own round-3 window and not this seat's. Against opal-users-v2's 96-209 RCU EVERY day over the same window, that shape is investigation, not service. But WHO read it cannot be answered: both CloudTrail trails carry no DynamoDB data resources, so no read of any DDB table in this account leaves a trail record. That is UNCOMPUTABLE and is recorded as such rather than smoothed into 'no reader'. (2) THE TABLE IS NOT UNGRANTED. trade-submission-lambda-role still holds full CRUD on it at trade-pipeline/iam.tf:63-64 and is the execution role of seven live lambdas -- ruled a separate cut, TO-OP-S-9C (2.0.0_SA_COO~Z msg 20083). A delete while that grant stands is not unsafe, but it would leave seven functions holding CRUD on a table that no longer exists, which is a tidier thing to fix before the delete than after. THE HONEST SUMMARY FOR A HUMAN: nothing here argues against the delete and nothing here compels it. The evidence supports retirement; the residual grant and the missing attribution are the two things a decider should know they are deciding WITHOUT.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S121",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A TWO-LANE SEQUENCING AGREEMENT THAT BOTH SEATS WROTE, AND THAT BOTH BELIEVED CLOSED THE SHARED-ROOT HAZARD, GOVERNS WHO RUNS THE APPLY AND NOT WHOSE RESOURCES GET APPLIED. Terraform applies the ROOT, so the moment a lane COMMITS a .tf into a root another lane is about to apply, that lane's resources are applied by the other lane's command. Measured: opal-ipset-reconciler, opal-ipblock-cli and opal-sentinel all carry CreateDate 2026-09-04T01:51:56Z -- the same second, three roles, two task orders, two lanes, ONE apply. Nothing is degraded and nothing rolled back; what is lost is the owning lane's ability to satisfy its own acceptance criterion from the record of the act.",
    "evidence": [
      "THE MEASUREMENT THAT SETTLES IT IS THE TIMESTAMP, not the state file. get-role on the APPLIED IAM plane returns opal-ipset-reconciler, opal-ipblock-cli and opal-sentinel each with CreateDate 2026-09-04T01:51:56Z. Three roles belonging to TWO task orders (TO-OP-S-15-19 and TO-OP-S-14-21) held by TWO lanes cannot be created in the same second by two separate applies. One apply created all three. NEGATIVE CONTROL beside it: get-role on a fabricated role name returns absent, so these are real presence rather than a probe that answers yes to everything.",
      "THE AGREEMENT, quoted so the gap is visible rather than characterised. 0.7.0_AE_CloudOps~S proposed in msg 20053 and 0.7.0_AE_CloudOps~T accepted unamended in msg 20058: the sentinel lane applies to infra/aws/terraform/opsec/ FIRST and announces the changed-resource list; the reconciler lane HOLDS its apply until then. That prevents two CONCURRENT applies racing one root, which is a real hazard and is genuinely closed. IT SAYS NOTHING ABOUT APPLY SCOPE.",
      "THE MECHANISM: terraform applies a ROOT, not a file. Once 0.7.0_AE_CloudOps~T committed iam_reconciler_and_cli.tf at 3578b10a00 into infra/aws/terraform/opsec/, ANY apply of that root by ANYONE necessarily created its four resources. The holding lane held its COMMAND and its RESOURCES went anyway. 'Hold your apply until the other lane announces' governs WHO RUNS THE COMMAND; it does not govern WHOSE RESOURCES GET APPLIED, and the two were conflated by both seats.",
      "THE SEPARATE-FILE MITIGATION IS WEAKER THAN IT LOOKED, and it was this seat's own idea so this is not a criticism of a peer. Declaring into iam_reconciler_and_cli.tf rather than the shared iam.tf genuinely prevents TEXTUAL conflict between two lanes editing one file. It does nothing whatever about apply scope. Two lanes in one root are coupled at APPLY granularity however the files are split -- and splitting the files made the coupling LESS VISIBLE while leaving it exactly as strong. A mitigation that addresses a real hazard on a different axis reads as coverage.",
      "NOTHING IS DEGRADED AND THERE IS NOTHING TO ROLL BACK, which is why this is OBSERVATION and not BLOCKING. The applied world is exactly what the owning lane declared, reviewed and intended: its own plan read 4 to add / 0 to change / 0 to destroy, its unscoped baseline on that root was a genuine 'No changes' rc=0 measured with its file moved aside, and no unintended resource reached the world. 0.7.0_AE_CloudOps~S did precisely what the agreement said it should do. The defect is in the agreement, which both seats wrote and both believed sufficient.",
      "WHAT IS ACTUALLY LOST IS EVIDENCE, NOT STATE, and it is a named criterion. S1519-AC4 requires per root the unscoped baseline, the ENUMERATED changed-resource list, the unscoped re-plan and the ledger CLOSED. The holding lane can produce the baseline and the plan because it measured those itself; it CANNOT produce the apply's own changed-resource list or window, because it did not run the apply, and it opened no deploy ledger for an act it was deliberately not performing. The same is true in mirror for any future apply into this root by either lane.",
      "IT WILL RECUR ON THE NEXT APPLY AND THAT IS WHY IT IS ARMED RATHER THAN INERT. Both faces have more to apply into this same root -- the reconciler's Lambda function, event source mapping and daily schedule for TO-OP-S-15-19, and the sentinel's own code resources for TO-OP-S-14-21 -- and TO-OP-S-22's verdict sits between the roles and those code deploys. The identical sweep happens again the moment either lane applies, in whichever direction, unless the protocol changes."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THE REUSABLE SHAPE, and it is CLAUDE.md Rule 22's shared-dependency clause one level further out than either seat applied it. 0.7.0_AE_CloudOps~S had ALREADY caught this class once tonight: msg 20050 from this seat checked whether two lanes might take the same FACE, and msg 20053 correctly answered that the real risk is two lanes on different faces writing the same ROOT. That was the members-versus-shared-dependency move made correctly. THEN BOTH SEATS BUILT A MITIGATION SCOPED TO THE MEMBERS AGAIN -- who runs the command, and which file each writes -- while the shared thing, the ROOT'S APPLY SCOPE, went unaddressed. Finding the shared dependency once does not immunise the remedy you then design for it. THREE DISARM SHAPES, OFFERED AND NOT RULED, since 2.0.0_SA_COO~Z owns the field: (a) SPLIT THE ROOTS so each face owns its own terraform root and apply scope stops being shared -- clean, and the most work; (b) ONE APPLIER, JOINT LEDGER -- whichever lane applies opens a ledger naming BOTH faces and publishes the enumerated changed-resource list to both, so the non-applying lane satisfies its criterion from the record of the act rather than reconstructing it from the result; (c) DECLARE-THEN-APPLY-TOGETHER -- both lanes commit declarations, then one apply is run deliberately for both with both lanes' plans quoted, which is what accidentally happened here and would have been sound had it been intended and recorded. Shape (b) is the cheapest and needs no rework of what exists. WHAT THIS SEAT IS DOING MEANWHILE: it has asked 0.7.0_AE_CloudOps~S for the apply's changed-resource list and window, and will reference that lane's ledger rather than opening a duplicate for an act it did not perform. It is NOT re-applying anything, and NOT opening a ledger retroactively for a command it did not run -- a ledger entry describing an act this seat did not take would be a record that reads as first-hand and is not.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S122",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FOUR INSTANCES OF ONE SHAPE, IN FOUR UNRELATED SUBSYSTEMS, IN ONE NIGHT: A CONTROL SCOPED TO ITEMS WHILE THE MECHANISM IT DEPENDS ON OPERATES ON A CONTAINER. Consumers scoped to FUNCTIONS while the read capability sits on ROLES (Z-S100, corrected at Z-S107). A grant removal scoped to ONE TERRAFORM ROOT while IAM is account-wide (Z-S112). An uncommitted-content check scoped to MY OWN ROW while `git checkout` operates on the FILE (Z-S116). A two-lane apply agreement scoped to WHO RUNS THE APPLY while terraform applies the ROOT (Z-S121). IN EVERY CASE THE CONTROL WAS CORRECT ABOUT ITS OWN UNIT AND SILENT ABOUT THE CONTAINER, so it passed while the thing it was written to prevent happened one level up. Two of the four are this seat's, and one of those is the row that diagnosed the shape.",
    "evidence": [
      "INSTANCE 1 -- FUNCTIONS vs ROLES. TO-OP-S-10 read both named JWT-key consumers on three planes and filed a denominator of 2 of 2. The read capability is granted on ROLES, and five roles carry it across 31 live functions (Z-S107). This seat's own intermediate correction (Z-S105) fixed the level and not the shape -- it read two ROLES and never censused the granting SET -- which is the same error one rung up and is why this instance counts once, not twice.",
      "INSTANCE 2 -- ONE ROOT vs THE ACCOUNT. TO-OP-S-9-11's exclusivity criterion required 'BOTH GRANTS ARE GONE' scoped to portal-auth/iam.tf:50-51. An unscoped IAM re-read found a THIRD live grant on the same table declared in a DIFFERENT terraform root, held by a role that is the execution role of seven live lambdas (Z-S112). Removing the two named would not have left the table ungranted, and the criterion could not have detected that.",
      "INSTANCE 3 -- MY ROW vs THE FILE. Before running `git checkout --` on the shared channel, a seat confirmed 'the only uncommitted content is mine' by grepping the diff for its OWN marker and getting 1. `git checkout` operates on the FILE, and two seats' rows were uncommitted in it; both were destroyed (Z-S116). A presence test on your own item cannot exclude a second item in the same container.",
      "INSTANCE 4 -- WHO APPLIES vs WHAT IS APPLIED. Two lanes agreed a sequencing protocol governing which lane RUNS the apply, and both believed it closed the shared-root hazard. Terraform applies the ROOT, so committing a .tf into a root another lane is about to apply ships your resources on their command -- measured as three roles created at the identical second, 2026-09-04T01:51:56Z, across two task orders and two lanes on one apply (Z-S121).",
      "WHY THIS IS ONE SHAPE AND NOT FOUR COINCIDENCES: the subsystems share nothing -- IAM policy evaluation, terraform root state, git working-tree semantics, and a written inter-lane protocol. What they share is that the AUTHOR reasoned about the units they were manipulating (these functions, these statements, my row, my apply) while the MECHANISM binds at a coarser unit (the role, the account, the file, the root). The mismatch is invisible from inside the control because every check of the finer unit passes."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): RELATION TO Z-S106, stated so the two class rows are not read as one: that row is about a control that is CONFIGURED AND INERT -- its effect depends on a second fact the configuration plane does not carry. This is about a control that WORKS EXACTLY AS WRITTEN and is scoped to the wrong unit. A Z-S106 control does nothing; a Z-S121 control does precisely what it says and does not bind what the author believed it bound. THE SUGGESTION, offered and NOT ruled, because bounds are cut at L6 and endpoints at L2/L4: A BOUND NAMES THE UNIT THE MECHANISM OPERATES ON, NOT THE UNIT THE AUTHOR HAS IN MIND. 'Both grants at :50-51' becomes 'every Allow on this ARN, account-wide, denominator printed'. 'This lane runs the apply' becomes 'no lane commits into this root between another lane's plan and its apply'. The estate already has the general form -- CLAUDE.md Rule 22's clause that a check scoped to the members cannot see a defect in what the members SHARE, with its remedy of one unscoped re-read after the scoped pass -- and 2.0.0_SA_COO~Z has already converted one instance into an acceptance criterion at Z-S117, requiring the full grant population with its denominator and every residual named. THAT CONVERSION IS THE MODEL and this row exists to say it applies to three more surfaces than the one it was written for. WHAT THIS ROW DOES NOT CLAIM: that any seat erred by ordinary standards. Each control was reasonable, each author found or accepted the correction quickly, and three of the four were caught BEFORE the harm by a pre-write read. This seat holds two of the four and nearly produced a fifth an hour ago, when a script crash left the shared channel dirty -- the exact state that caused instance 3.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S123",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "THE RULING EXPECTED 'DEAD' AND THE MEASUREMENT SAYS THE OPPOSITE, EMPHATICALLY: opal-session-analytics ran 141,685 invocations in 14 days -- 63x the portal authorizer's 2,227 and 32x the auth handler's 4,451. It is not merely alive, it is the BUSIEST of the four consumers by invocation count. So TO-OP-S-10 takes the ALIVE branch of 20121's trichotomy: a consumer with NO build path and NO TTL cannot receive a rotated key and cannot expire itself into a retry, so rotating today breaks it PERMANENTLY with no mechanism available to repair it afterwards. TO-OP-S-10's rotation is BLOCKED until opal-session-analytics has a build path.",
    "evidence": [
      "THE ORACLE AND WHY IT IS ONE: AWS/Lambda Invocations is a PLATFORM metric emitted by the Lambda service itself, not by application code, so for an ordinary Lambda a zero means not-invoked rather than not-instrumented. get-metric-statistics, Sum, period 86400, 14-day window ending 2026-09-04T02:18:04Z.",
      "THE SUBJECT: opal-session-analytics Sum=141,685 across 12 datapoints. Alive by a wide margin and continuously -- 12 of 14 days carry traffic.",
      "THE COMPARISON THAT MAKES THE NUMBER MEAN SOMETHING: opal-portal-authorizer Sum=2,227 (12 datapoints) and opalinvest-auth-handler Sum=4,451 (14 datapoints). The consumer the face excluded from the build runs roughly 63x the authorizer and 32x the signer. Whatever else is true, it is not a vestigial function.",
      "CORROBORATION FROM A DIFFERENT INSTRUMENT, so the verdict does not rest on one metric: its CloudWatch log group's newest event was 2026-09-03T23:55:06.619Z when read at ~00:0xZ, minutes fresh at that moment.",
      "AND IT IS RUNNING EIGHT-MONTH-OLD CODE WHILE DOING IT: get-function-configuration reports LastModified 2026-01-08T15:31:07Z, CodeSha256 eQswWf3zdISgafQwQ+GhHgyWNfoxPOSeriqYVxiN9VU=, Runtime nodejs20.x. High traffic and no deploys since January is the combination that makes the missing build path expensive rather than academic -- nobody has needed to deploy it, so nobody has discovered that they cannot."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHAT THIS DOES AND DOES NOT CHANGE. It does NOT change TO-OP-S-10B: opal-session-analytics stays out of THIS face's build scope, the two unblocked consumers proceed, and this seat is building them. It DOES change TO-OP-S-10, which was already blocked on TO-OP-S-10B and is now blocked on a SECOND thing that does not yet have a face -- a build path for opal-session-analytics. Both must land before a rotation is safe, and they are independent. THE ASYMMETRY WORTH STATING PLAINLY, because it is what makes this BLOCKING rather than an observation: every other consumer in the set degrades RECOVERABLY under a bad rotation. The edge has a 300s TTL and converges on its own. The authorizer, once this face lands, will have a TTL and converge. A consumer with neither a TTL nor a build path has no convergence mechanism AND no repair mechanism -- it cannot heal itself and it cannot be patched. That is the only unrecoverable member, and it is the busiest one. AND THE SECOND-ORDER POINT 20121 MADE THAT THE NUMBER SHARPENS: a rotation that keeps the old key valid forever in order to protect this consumer has not rotated anything. With 141,685 invocations riding on it the temptation to do exactly that is real, and it should be named now rather than argued at cutover. RECOMMENDATION, the issuer's call and not this seat's: cut the build-path face for opal-session-analytics as a sibling of TO-OP-S-10B. The source-map correction in Z-S110 is its first limb and is small; whether the TTL and two-slot ride along in that face or a later one is a scoping choice, but the build path has to exist before either is deployable.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S124",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "THE LIVENESS ORACLE READS ZERO ON THE BUSIEST CONSUMER IN THE SET, AND WOULD HAVE KILLED IT. AWS/Lambda Invocations for auth-validator-edge returns Sum=0 across 0 datapoints -- for a function that made 680 GetSecretValue calls in 30 hours and holds 47.4 MB of logs in us-east-1 alone. THE CAUSE IS NOT A ZERO, IT IS AN ABSENCE: list-metrics for that function+metric returns [] -- the metric DOES NOT EXIST. Lambda@Edge executes in the region serving the request and does not publish Invocations under its function name in the home region, so get-metric-statistics returns an empty datapoint set that renders as Sum=0. A NONEXISTENT METRIC AND AN IDLE FUNCTION ARE BYTE-IDENTICAL THROUGH THIS INSTRUMENT.",
    "evidence": [
      "THE FALSE ZERO: get-metric-statistics, AWS/Lambda Invocations, Sum, period 86400, dimension FunctionName=auth-validator-edge, 14-day window ending 2026-09-04T02:18:04Z -> Sum=0, datapoints=0. Run in the same call-set and with identical parameters as three other functions that all returned non-zero.",
      "THE FUNCTION IS DEMONSTRABLY, HEAVILY LIVE: 680 GetSecretValue calls attributed to assumed-role/lambda-edge-execution-role/us-east-1.auth-validator-edge in a ~30-hour CloudTrail window -- more than the other three consumers combined.",
      "THE MECHANISM, MEASURED RATHER THAN ASSERTED FROM KNOWLEDGE: aws cloudwatch list-metrics --namespace AWS/Lambda --metric-name Invocations --dimensions Name=FunctionName,Value=auth-validator-edge returns [] -- an EMPTY LIST. The metric is not zero, it does not exist. POSITIVE CONTROL, same call shape, same region, different function: the identical query for opal-session-analytics returns 2 metrics. So the call works and the emptiness is a property of the subject.",
      "AND THE CORRECT ORACLE FOR THIS CLASS, which does discriminate: Lambda@Edge writes region-local log groups named '/aws/lambda/us-east-1.<function>' in whichever region served the request. describe-log-groups on that prefix returns storedBytes 47,399,597 in us-east-1, 301,738 in us-west-2 and 890 in eu-west-1 -- three regions, real bytes, and the replication itself visible in the shape of the answer."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS A ROW RATHER THAN A FOOTNOTE ON THE MEASUREMENT. The verdict this instrument would have produced on auth-validator-edge is DEAD, and DEAD is the branch of 20121's trichotomy that says 'remove it from the consumer set with evidence and rotate freely.' Applied to the edge that is the most destructive available answer: it fronts the portal, it serves more requests against this secret than every other consumer combined, and removing it from the consumer set before a rotation would sign out every session it validates. The row exists because the wrong answer here was not merely wrong, it was actionable and licensed by a rule. WHAT ACTUALLY SAVED IT was a positive control that was not strictly required. The subject of the measurement was opal-session-analytics; the other three functions were run only to give its number a comparison. One of those comparisons came back zero on a function already proven live earlier in the same session by a different instrument, and the contradiction is what forced the list-metrics check. Without the earlier CloudTrail read there would have been no contradiction to notice, and the zero would have read as a finding. A CONTROL IS ONLY A CONTROL IF ITS SUBJECT'S TRUE STATE IS ALREADY KNOWN BY OTHER MEANS -- and the cheapest way to hold that property is to keep evidence from earlier in the same investigation alive rather than discarding it once its own question is answered. THE GENERAL FORM, which is CLAUDE.md 22a's RETRIEVAL trap on a metrics API rather than a list API: a failed retrieval returns a VALUE. get-metric-statistics does not distinguish 'no such metric' from 'metric exists and summed to zero' -- both arrive as an empty Datapoints array that every downstream reader renders as 0. list-metrics is the discriminator and it is a separate call that nothing prompts you to make, because the first call already looked like it worked. NON-APPLICATION: ordinary regional Lambdas, where the metric does exist and a zero is a real zero -- as the three non-edge consumers in this same call-set demonstrate.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S125",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "C-2 DOES NOT HOLD AS WRITTEN, AND S15-AC3 CANNOT PASS ON ITS LITERAL WORDING. The criterion requires an enumeration showing ONLY the reconciler's role holds wafv2:UpdateIPSet on the four sets. Enumerated on the applied plane across 231 principals: FOUR hold it. One is opal-ipset-reconciler; the other three are human IAM USERS holding administrator access through a single group. C-2's INTENT survives intact -- the reconciler is the only SERVICE principal and no second automated writer exists -- but the invariant's own text names 'a console click' as the hazard, and a console click by an administrator is exactly what remains possible.",
    "evidence": [
      "THE CENSUS, on the APPLIED plane with its denominator printed: 231 principals scanned -- 224 roles + 7 users, both lists paginated to exhaustion -- simulated with iam simulate-principal-policy for wafv2:UpdateIPSet, ONE --resource-arns per call because two or more in a single call flips held ones to implicitDeny and would have MANUFACTURED the clean result this census set out to find. 0 simulation errors. FOUR principals returned allowed: role opal-ipset-reconciler, and users Andrew_Berman, Andrew_Berman_Console and Opal_Terminal. All four were then re-simulated against ALL FOUR sets and all four are allowed on all four -- 4 of 4, not one set generalised.",
      "POSITIVE CONTROL RUN FIRST AND SEPARATELY: opal-ipset-reconciler returns allowed on all four sets. Without it every 'denied' in a 231-principal sweep would be worthless, because a broken query returns denied for everything and looks exactly like a clean estate. The instrument demonstrably says ALLOWED.",
      "THE MECHANISM, and finding it required a carrier this seat did not check first: list-attached-user-policies and list-user-policies on all three users return only OpalSecretsReader, ycharts-credentials-read, inf-andrew-otp-write and IAMUserChangePassword -- NOT an administrator policy, and nothing granting a WAF action. Reading only those, the census result looks inexplicable. THE GRANT ARRIVES THROUGH GROUP MEMBERSHIP: all three users belong to the group AdministratorAccessOpalCapital, which the user-attached and user-inline policy calls structurally cannot see and which simulate-principal-policy correctly evaluates. The instrument that found the holders and the instrument that explains them are different calls, and the explaining one is the one a reader would skip.",
      "WHY THE CHEAPER CENSUS WOULD HAVE RETURNED A CLEAN, CONFIDENT, WRONG ANSWER: scanning policy documents for the string 'wafv2' finds nothing on any of the three users, because their grant is a wildcard inherited from a group. A string census would have reported exactly one holder, matched the criterion's expectation, and been wrong -- and it would have been wrong in the direction that CONFIRMS the hypothesis, which is the direction nobody re-checks. Every principal was simulated instead of filtered for exactly this reason.",
      "WHAT SURVIVES, AND IT IS THE OPERATIVE HALF: the reconciler is the ONLY non-human principal holding the action. No second service, Lambda, or automation can write these sets. The sentinel and the unblock CLI both return explicitDeny on all four sets (TO-OP-S-22 verdict, msg 20115), so the two principals most likely to grow a convenience path are structurally barred rather than merely unequipped. C-2's design intent -- the table is truth, one enactor, no second automated writer -- is intact on the applied plane.",
      "WHAT DOES NOT SURVIVE IS THE LITERAL CLAIM, and C-2's own text is what makes this worth a row rather than a footnote. The invariant reads: 'a convenience path that writes an address directly to a set -- a script, a console click, a just this once -- silently makes the table a lie, and the next full reconcile will erase whatever was written outside it.' A CONSOLE CLICK IS NAMED IN THE INVARIANT ITSELF, and three administrators can perform exactly that. The reconciler would then erase it on the next pass, which is the design working -- but the window between the click and the erase is real, and during it the sets and the table disagree with nothing reporting an error."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THIS IS A FORK FOR THE ISSUER AND THE ASSIGNEE WILL NOT SELF-RULE IT, because the two readings produce different criterion outcomes and each is defensible. READING A, LITERAL: the criterion says 'only the reconciler's role' and the enumeration shows four, so S15-AC3 FAILS and stays failed until the estate removes administrator reach over these sets. READING B, BY INTENT: C-2 governs the FRAMEWORK's writers, an account administrator is outside any identity-policy invariant by construction (an administrator who can delete the IP sets outright is not meaningfully constrained by not being allowed to update them), and the criterion is satisfied by 'exactly one service principal, and three administrators enumerated and named'. THE ASSIGNEE'S RECOMMENDATION IS READING B WITH THE ENUMERATION CARRIED IN THE PROOF RATHER THAN SUMMARISED -- because the value of this criterion is the NAMED LIST, not the number, and a future fourth service principal would show up against it immediately. WHAT WOULD ACTUALLY CLOSE READING A, stated so the cost is visible rather than implied: an SCP or a permission boundary denying wafv2:UpdateIPSet on these four ARNs to everything except the reconciler's role. That denies Andrew's own console. It is a sovereign-class call, it is not this seat's, and it is not proposed -- only priced. NOTHING IS BUILT OR CHANGED ON THIS ROW: the finding is a measurement of the estate as it already stood before this face existed, not a defect this task order introduced.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S127",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A SYMMETRIC JWT SIGNING SECRET IS SITTING IN CLEARTEXT LAMBDA ENVIRONMENT VARIABLES on the trade pipeline's authentication path: `JWT_SECRET` is set as a plain environment variable on BOTH trade-auth-handler and trade-authorizer, carrying the SAME 60-character value on each, readable by any principal holding lambda:GetFunctionConfiguration and visible in the console without decrypting anything. The portal's own auth path was deliberately moved the other way -- RS256 with the private key in Secrets Manager and a LOUD failure if it cannot be fetched -- so the estate holds two different answers to the same question on two auth paths.",
    "evidence": [
      "aws lambda get-function-configuration --function-name trade-auth-handler --query Environment.Variables: two keys, JWT_SECRET and USERS_TABLE. aws lambda get-function-configuration --function-name trade-authorizer: one key, JWT_SECRET. The two JWT_SECRET values are identical to each other by inspection of the first and last characters and length; the value itself is NOT reproduced here or anywhere in this row, and is not needed to establish the finding.",
      "Denominator: all SEVEN functions on trade-submission-lambda-role were read, 7 of 7. The other five carry no JWT_SECRET -- trade-dashboard-api, trade-submission-handler and trade-workflow-handler carry only SUBMISSIONS_TABLE / DASHBOARD_URL / EMAIL_FROM, and trade-identifier-cache and trade-parquet-batch-export carry no environment variables at all. So the exposure is scoped to the two authentication functions rather than the whole role.",
      "CONTRAST, and it is what makes this a finding rather than a preference: the portal auth path uses RS256 with opal/auth/jwt-private-key and opal/auth/jwt-public-key read from Secrets Manager at mint time (jwt.ts getJwtPrivateKey/getJwtPublicKey), and portal-auth/iam.tf:59-75 narrows that role to an explicit two-secret allowlist with a comment recording that both reads are LOUD. The mechanism the estate chose for one auth path is absent on the other.",
      "A cleartext Lambda environment variable is not encrypted at rest with a customer key by default and is returned in full by GetFunctionConfiguration, which is a far wider read surface than secretsmanager:GetSecretValue on a named secret ARN -- the portal role's own grant is scoped to exactly two secret ARNs.",
      "Vintage of the live reads: 2026-09-04T02:5xZ, account 313476888478."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY IT IS FILED HERE RATHER THAN CHASED OR DROPPED. It was found while closing a gap in THIS face's evidence -- a deployed-byte scan cannot see a table name supplied by configuration, so the environment of all seven functions had to be read, and the JWT_SECRET was simply there. Per CLAUDE.md the correct act is one row and keep working, which is what this is. I DID NOT and WILL NOT rotate it, read its plaintext into any committed artifact, or open a remediation: a symmetric secret shared by two functions is consumed by whatever validates the tokens it signs, and rotating it without that consumer census is how an auth path goes dark. WHAT THIS ROW DOES NOT CLAIM: it does not claim the secret has leaked, it does not claim HS256 is wrong for this pipeline, and it does not claim the trade path is exploitable -- only that a signing secret is in cleartext configuration where the same estate deliberately chose custody for the equivalent secret one path over.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S128",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "S9C-AC4 REQUIRES ALL SEVEN FUNCTIONS INVOKED BEFORE AND AFTER THE REMOVAL, AND TWO OF THE SEVEN ARE NOT SAFELY INVOKABLE BY AN AGENT: trade-submission-handler and trade-workflow-handler carry EMAIL_FROM=trades@opalinvest.dev and DASHBOARD_URL, so invoking them is capable of writing a trade submission and SENDING MAIL TO A REAL RECIPIENT. The face's verification step is therefore not executable as written without a decision about what 'exercise' may mean for a function that has outward-facing side effects.",
    "evidence": [
      "THE ORACLE AGREED, which is why this is the only thing standing between the face and a removal. S9C-AC2 on the DEPLOYED bytes: 7 of 7 functions content-scanned (all Zip, python3.11, all downloadable, ZERO unscannable), and ZERO name table/opal-users under an exact matcher excluding -v2/-master/-trade. POSITIVE CONTROL FIRES on the same matcher family and the same deployed artifacts: trade-auth-handler's bytes contain opal-users-v2 five times, so a zero for the legacy name is an absence rather than a broken scanner. Corroborating: 4 of 7 name trade-users, the pipeline's own table.",
      "THE CONFIGURATION GAP CLOSED TOO: environment variables read on all 7 of 7. The ONLY users-table pointer anywhere is trade-auth-handler's USERS_TABLE=opal-users-v2. No function carries an environment variable naming the legacy table, so the byte-scan's blind spot -- a name supplied at runtime -- is measured shut rather than argued away.",
      "S9C-AC1's preferred oracle DOES NOT EXIST, measured at this vintage rather than assumed: both trails in the account (opal-organization-trail, opal-served-key-write-trail, neither an organization trail) carry data resources of type AWS::S3::Object ONLY and nothing for DynamoDB, and list-event-data-stores returns an EMPTY list, so CloudTrail Lake is not a second surface either. A no-access reading from these trails would have been vacuous, which is exactly the false absence the face was written to refuse.",
      "THE SIDE EFFECTS, read from live configuration: trade-submission-handler and trade-workflow-handler both carry EMAIL_FROM=trades@opalinvest.dev and DASHBOARD_URL=https://opalinvest.dev, alongside SUBMISSIONS_TABLE=opal-trade-submissions. A handler holding a from-address and a submissions table is one whose ordinary path writes a record and sends mail.",
      "Vintage: deployed-byte scan and configuration reads 2026-09-04T02:4x-02:5xZ."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): I AM NOT REMOVING THE GRANT ON MY OWN JUDGEMENT, AND THE FACE IS WHY. It states in terms that an honest non-removal beats a removal justified by an instrument that cannot see what it is trusted to rule out -- and the same logic covers a removal whose verification step cannot be performed. The evidence for disuse is strong and multi-plane, and I would still rather hand the last inch to the issuer than take it, because the failure mode is seven production functions losing access discovered by whichever one next needs it. WHAT I AM NOT DOING EITHER: I am not quietly declining. Both branches are cheap, the evidence is already gathered, and whichever the issuer picks can be executed immediately -- (a) needs no act at all and (b) needs one narrowed sentence about what exercise means here. THE GENERAL SHAPE: a verification requirement written from the RISK (all seven, never a sample) can be undischargeable because of what the members DO, and that is not a defect in the requirement -- it is a fact about the population that only shows up when someone reads the members before obeying the rule.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S129",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "THE RULING'S CONDITION WAS SATISFIED, BUT NOT BY THE TEST IT NAMED, AND THE DIFFERENCE IS AN INSTRUMENT TRAP WORTH KEEPING. The ruling said block xmlrpc.php outright only if no request was a SUCCESSFUL AUTHENTICATED call, treating a 200 as the tell. XML-RPC RETURNS HTTP 200 FOR A FAILED AUTHENTICATION -- the fault travels in the response BODY and an access log records no bodies -- so that test can never be satisfied on this endpoint and 9,056 of 58,207 requests did return 200. The condition's INTENT was met by a stronger route: JETPACK IS NOT INSTALLED on this WordPress, so all 25,000-plus Jetpack user-agents are FORGED, alongside 12,342 distinct randomized siteNNNNNNNN.com domains and 798 source addresses. There is no live client for the ruling to break.",
    "evidence": [
      "THE CENSUS, on the origin's own OpenLiteSpeed access logs, which are the ONLY plane that can see this traffic: opalinvest.com still resolves to the EIP (row Z-S101), the new edge ACL has NO logging configuration at all (get-logging-configuration returns WAFNonexistentItemException), and the CloudFront WAF group fronts the PORTAL, not this site. WINDOW 30/Jul/2026:15:23:58 to 04/Sep/2026:02:28:33. DENOMINATOR 620,453 request lines, of which 58,207 are xmlrpc.php. STATUS DISTRIBUTION: 403 x 49,012; 200 x 9,056; 405 x 124; 500 x 8; 404 x 7 -- summing to 58,207, so the distribution is complete and not a sample.",
      "THE PROBE THAT FAILED FIRST, recorded because it produced exactly the answer that would have been convenient. The first status census used an awk field offset of i+2 and printed the token HTTP/1.1\" instead of the status code; its 'any 200 on xmlrpc.php' check therefore returned EMPTY. AN EMPTY RESULT FROM A BROKEN EXTRACTOR AND A TRUE ABSENCE ARE BYTE-IDENTICAL, and this one pointed at 'condition satisfied, proceed'. It was caught by reading a raw log line verbatim rather than trusting the parse, and the corrected offset i+3 was then POSITIVE-CONTROLLED against all 620,453 requests, returning a plausible HTTP distribution (200 x 415,331; 404 x 101,040; 403 x 49,215; 301 x 27,046) which a broken extractor could not produce.",
      "WHY THE 9,056 200s DO NOT MEAN WHAT THE RULING ASSUMED. XML-RPC is a transport over HTTP: a failed login returns HTTP 200 carrying a faultCode in the XML body. The access log records status and byte count, never bodies. So the ruling's literal test -- show no request was a successful AUTHENTICATED call -- IS NOT ANSWERABLE FROM THIS INSTRUMENT IN EITHER DIRECTION. Reading the 9,056 as successful logins would overstate; reading the broken grep's empty set as 'no 200s' would have understated. The response-size distribution is consistent with non-payload replies: 5,390 responses at a uniform 4,712 bytes, plus tight clusters at 421, 422, 469 and 471 bytes.",
      "THE DECISIVE READ, AND IT ANSWERS THE INTENT RATHER THAN THE LETTER: JETPACK IS NOT INSTALLED. The plugins directory of the live WordPress holds 16 entries -- advanced-custom-post-type, automaticcss-plugin, google-site-kit, gravityforms, index.php, litespeed-cache, official-mailerlite-sign-up-forms, omnisend, pdf-embedder, redirection, safe-svg, simple-cloudflare-turnstile, updraftplus, wp-mail-smtp, wp-seopress, wps-limit-login -- and Jetpack is not among them. POSITIVE CONTROL that this is a real absence and not a failed read: the themes directory listed normally from the same command (bricks, bricks-opal, twentytwentyfive, twentytwentyfour). The only 'jetpack' strings on the box are inside updraftplus's own changelog and readme.",
      "SO EVERY JETPACK USER-AGENT ON THIS ENDPOINT IS FORGED, and two further tells agree independently: the forged agents report 12,342 DISTINCT randomized domains of the form http://siteNNNNNNNN.com, where a real Jetpack reports ONE site URL; and 798 distinct source addresses produced a 200, of which a single address (85.11.167.203, bare Mozilla/5.0 agent) contributed 5,882 with a uniform 4,712-byte reply. That is a distributed brute-force and pingback-amplification pattern, not a client.",
      "THE ACT AND ITS PROOF. Rule BlockXmlrpc, priority 1, Action Block, ByteMatchStatement ENDS_WITH '/xmlrpc.php' on uri_path with a LOWERCASE transform, added to opal-website-edge-protection. Plan was 0-add/1-change/0-destroy, unscoped, with an unscoped 0-diff re-plan after. THE REFUSAL, exercised: GET /xmlrpc.php through the edge returns 403 with Server: CloudFront and X-Cache: Error from cloudfront -- generated AT the edge, not proxied from the origin, which serves 'server: LiteSpeed' on allowed responses; POST with a system.listMethods body also returns 403. THE ORIGIN-SIDE ABSENCE WITH ITS POSITIVE CONTROL, which is the half a 403 alone never establishes: a uniquely-marked ALLOWED request through the same edge appears in the origin access log ('GET / HTTP/1.1' 200 96191, user-agent s13ac2-024601-control, from CloudFront edge address 130.176.25.98), while the marked blocked GET and POST return grep counts of 0 and 0. A second control confirms the log was current at read time.",
      "AND WHAT THE RULE DOES NOT YET DO, stated so no reader overstates the applied world: because opalinvest.com still resolves to the origin EIP, REAL VISITOR TRAFFIC DOES NOT TRAVERSE THIS DISTRIBUTION, and the 58,207 xmlrpc requests censused above are reaching WordPress directly, bypassing this rule entirely. The rule protects traffic that comes THROUGH the edge, which today is only what is sent there deliberately. It becomes a real control at DNS cutover and not before -- which is row Z-S101's standing consequence, not a defect in this act."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS FILED AS AN OBSERVATION AND INERT: the act was taken, the condition's intent was measured and met, nothing is left armed against anyone by this rule, and the rule is one stanza whose rollback was named before the act. It is recorded because the TRAP GENERALISES BEYOND THIS CELL. A status-code test is the natural way to ask 'did anyone successfully use this endpoint', and it is sound on ordinary HTTP surfaces. It is UNSOUND on any endpoint that tunnels its own protocol over HTTP and reports application-level failure inside a 200 -- XML-RPC here, and by the same construction SOAP, JSON-RPC, GraphQL and most webhook receivers. THE ESTATE HAS AT LEAST ONE MORE OF THESE: the opal-gateway ALB fronts a JSON-RPC surface, and any future 'was this endpoint successfully used' question asked of it with a status-code filter will meet the same wall. THE SECOND, SHARPER HALF: this seat's first census returned an EMPTY 200-set from a broken awk offset, and that empty set pointed toward 'condition satisfied, block it'. A broken probe agreed with the convenient answer. What caught it was reading one raw log line verbatim before trusting any parse of it, and then positive-controlling the corrected extractor against the full 620,453-line population -- neither of which the ruling asked for. THE GENERAL FORM: when a condition is expressed as an ABSENCE, the probe that returns that absence must be independently shown capable of returning its presence.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S130",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "THE 'SEVEN LIVE LAMBDAS' PREMISE IS WRONG AND I AM THE ONE WHO INTRODUCED IT. Measured on two independent instruments: FIVE of the seven functions on trade-submission-lambda-role are DORMANT -- zero invocations in 30 days and last log events 51 to 129 days old -- and only TWO are live. That makes ruling 20138's observation route STRUCTURALLY IMPOSSIBLE for the two mail senders it was written for: trade-submission-handler and trade-workflow-handler last executed 2026-07-14, so there is no cadence to derive a window from and no window in which they can be observed executing.",
    "evidence": [
      "INSTRUMENT 1, CloudWatch AWS/Lambda Invocations, 30 days at period 86400, window 2026-08-05T02:58:59Z -> 2026-09-04T02:58:59Z: trade-submission-handler 0, trade-workflow-handler 0, trade-auth-handler 0, trade-authorizer 0, trade-identifier-cache 0. Non-zero: trade-dashboard-api 58 invocations across 10 active days, trade-parquet-batch-export 90 across 30 active days.",
      "THE POSITIVE CONTROL IS BUILT INTO THAT SAME QUERY, which is why the five zeroes are absences rather than a broken probe: the identical namespace, dimension shape and period returns real datapoints for two of the seven. A query that could not see invocations would have returned nothing for all seven.",
      "INSTRUMENT 2, CloudWatch Logs describe-log-streams ordered by LastEventTime -- a DIFFERENT plane from metrics, not a re-run of the same one: trade-submission-handler 2026-07-14T18:18:11Z (51d), trade-workflow-handler 2026-07-14T18:17:07Z (51d), trade-auth-handler 2026-04-27T23:29:30Z (129d), trade-authorizer 2026-04-27T23:35:28Z (129d), trade-identifier-cache 2026-07-13T19:19:02Z (52d), trade-dashboard-api 2026-09-03T16:07:07Z (0d), trade-parquet-batch-export 2026-09-04T02:00:27Z (0d).",
      "THE TWO INSTRUMENTS PARTITION THE SET IDENTICALLY -- the same five dormant, the same two live -- which is corroboration rather than repetition because Logs and Metrics are separate planes with separate retention and separate failure modes.",
      "TRIGGER SHAPE, which is why there is no schedule to wait on: both mail senders have ZERO event source mappings and their resource policies admit only apigateway.amazonaws.com (APIs w8jnzvs21g and 7k3ed8px20, one statement scoped to /api/general/trades/*). They fire when a human submits a trade through the portal. Demand-driven and currently at zero demand for 51 days.",
      "A BROKEN PROBE AND A TRUE ABSENCE READ IDENTICALLY, and this row nearly shipped the broken one: an intermediate version of the Logs query returned NO-EVENTS for all seven INCLUDING the two known-live functions, which is how it was caught. The timestamps above come from the raw unwrapped read."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THE ERROR IS MINE AND IT PROPAGATED. I wrote 'the execution role of SEVEN LIVE LAMBDAS' in Z-S112 from org/modules/graph/aws-shapes/g2-edge-census-cut1.yaml:179-185, which records lambda.Role ATTACHMENT. Attachment is not liveness, and I never asked the second question. 2.0.0_SA_COO~Z then wrote that phrase into TO-OP-S-9C's title and body in good faith, and ruling 20138's observation branch was designed around it. A WRONG ADJECTIVE TRAVELLED FURTHER THAN THE FACT IT SAT ON, and it shaped a criterion. WHAT IT DOES AND DOES NOT CHANGE. It does NOT change the removal evidence: 7 of 7 deployed artifacts still name the table ZERO times, env vars still point only at opal-users-v2, and dormancy makes disuse MORE likely rather than less. It DOES change the verification design and it cuts both ways -- a dormant function cannot be observed, and it also cannot break a user while dormant, but when it finally wakes there is nobody watching, which is the case a removal should be most careful about. THE OPTIONS, none of which is mine to pick: (a) observe the TWO LIVE functions instead, which is achievable tonight and within ~24h respectively, and accept dormancy plus the byte and config evidence for the other five; (b) treat the five dormant functions as unverifiable and leave the grant, which is the ruling's own default and passes S9C-AC3; (c) narrow to an initialisation probe for the five dormant ones, noting that trade-submission-handler and trade-workflow-handler still must not be invoked because the objection in 20138 was EGRESS, and dormancy does not make an email less real.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S131",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "PRD 7.3's PIPELINE DIAGRAM STILL ROUTES CASE FILES TO THE PRE-SPLIT BUCKET: step 4 reads 'write case file s3://opal-data-security/cases/{yyyy}/{mm}/{dd}/{addr}/{case_id}/', but opal-data-security was re-designated the LOG DESTINATION (S28, FWD-5) by PRD v0.9 and the evidence store is opal-security-evidence. THE SAME DOCUMENT SAYS BOTH: its own S17 row records the rename in terms -- 'through v0.8 this row named opal-data-security, which is now S28' -- and C-8 places cases in the evidence store. This is the SECOND instance of the split-drift class in one day; row Z-S114 was the first, on the C-14 operator role.",
    "evidence": [
      "THE STALE LINE, quoted: PRD 7.3 pipeline diagram, step 4 -- 'write case file  s3://opal-data-security/cases/{yyyy}/{mm}/{dd}/{addr}/{case_id}/  summary.json  waf-samples.jsonl  timeline.md'. The path shape is correct and current; the BUCKET is the pre-split one.",
      "THE SAME DOCUMENT CONTRADICTS IT, which is what makes this a drift rather than a disagreement: the S17 row states 'through v0.8 this row named opal-data-security, which is now S28, FWD-5's log destination' and names opal-security-evidence as the evidence store with 'cases/, reports/, allowlists/ retained'. C-8's violation condition is 'a case written outside cases/{yyyy}/...' in that bucket.",
      "THE APPLIED PLANE AGREES WITH THE S17 ROW AND NOT WITH THE DIAGRAM: opal-security-evidence exists, is SSE-KMS on the project key, and now holds the sentinel's real case files under cases/2026/09/04/ plus reports/daily/2026-09-04.json. Written and read back this session.",
      "IT DID NOT BITE THIS FACE, and the reason is worth recording because it is not a defence: TO-OP-S-14-21's deliverable 3 names 'the evidence store (opal-security-evidence, under cases/)' explicitly, so the task order carried the corrected referent and the sentinel writes to the right bucket. An implementer who worked from PRD 7.3 -- the only place the full path layout is written out -- would have written case files into the LOG DESTINATION.",
      "WHY IT SURVIVED: PRD v0.9 split the bucket and updated the ROWS that own the resources (S17, S28) and the CONSTRAINT text (C-8), but not the 7.3 architecture DIAGRAM, which is prose describing the same resources from a different angle. The rows are what a cell owner reads; the diagram is what an implementer reads for a path."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THE REUSABLE PART, AND IT IS THE SAME SENTENCE ROW Z-S114 ENDED ON, which is why it is filed rather than fixed in passing: A SPLIT RE-POINTS THE CELL THAT OWNS THE RESOURCE AND LEAVES EVERY OTHER REFERENCE BEHIND. Z-S60 was the condition drift, Z-S114 the operator role, and this is the architecture diagram. Three surfaces, one cause, and each was found by someone reading the artifact for an unrelated reason rather than by any check -- because no check exists that asks 'what still points at the thing that moved'. THE SEARCH THAT FINDS THIS CLASS IS NOT 'what changed' BUT 'what still names the old identity', and it is cheap: a census for the old bucket name across the project tree would have returned all three. THAT CENSUS IS RECOMMENDED AND IS NOT RUN HERE, deliberately -- it would cross from filing an observation into auditing another cell's artifacts, which is not this face's bound. WHAT IS AT STAKE IF IT IS LEFT: C-8's violation condition is a case written outside cases/ in the evidence store, so an implementer following 7.3 would produce a C-8 violation while believing they had followed the spec exactly, and the case files would land in the bucket that the C-14 operator role CAN read (per row Z-S114) rather than the one it cannot -- so the two drifts would partially mask each other's symptoms.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S132",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "SWEEP COMPLETE, 62 of 62 criteria examined across 11 of 11 non-complete faces, and it yields ONE new finding rather than a list: S23-AC3 iterates over OP-s-20's ALLOW list, which does not exist and cannot be built, so its 'zero firms would trip the threshold' is produced by an EMPTY LOOP and is indistinguishable from a partner that WOULD be throttled. Its own clause 'Zero is a fine answer' pre-blesses that reading, and the result feeds an OP-x-5 rate-threshold card to Andrew. The other 61 criteria are sound or already amended, and several are notably hardened against exactly this class.",
    "evidence": [
      "THE POPULATION AND ITS DENOMINATOR, parsed from each task order's own <status> and <criterion id> fields at HEAD 939c7fe0a0 rather than from file location or recollection: 26 face files exist, 15 complete, 11 NON-COMPLETE. Those 11 carry 62 criteria in total. ALL 62 WERE READ IN FULL, not sampled: TO-OP-S-10 (5), S-10B (6), S-10C (5), S-12 (5), S-13 (5), S-14-21 (6), S-15-19 (7), S-20 (5), S-23 (5), S-9-11 (8), S-9C (5). FACES EXAMINED 11 OF 11; CRITERIA EXAMINED 62 OF 62.",
      "THE TEST APPLIED TO EACH, as commissioned: what would this evidence look like if the claim were false? If the answer is 'the same', the criterion cannot fail.",
      "THE FINDING -- S23-AC3, and it is the only new one. Verbatim: 'for each firm in OP-s-20's ALLOW list, whether its observed ordinary traffic would have tripped the recommended threshold, with the count that would have tripped printed. Zero is a fine answer; an unstated answer is not.' OP-s-20's ALLOW list DOES NOT EXIST and is not merely late: that face's GO condition returned NEGATIVE, the issuer accepted it at msg-id 20094 with DO NOT BUILD THE LIST, and cell OP-s-20 is HELD at 9dfb4d9e52. The reasons are structural -- 97.8% of the only observable sign-in window is this project's own probe traffic (Z-S118) and firm attribution is inexpressible on every available source, with 0 of 4 firms observable and the S16 table at Count 0. SO THE ITERATION SET IS EMPTY BY CONSTRUCTION: if the claim 'no partner would trip the threshold' were FALSE, the evidence would be IDENTICAL -- an empty loop returning zero. The criterion cannot distinguish 'checked every partner and none would trip' from 'there are no partners to check'.",
      "AND THE CRITERION'S OWN WORDING PRE-BLESSES THE WRONG READING, which is what makes it worse than a silent gap: 'Zero is a fine answer; an unstated answer is not' is aimed at a seat that skips the work, but it also authorises precisely the output an empty list produces, so a vacuous pass reads as COMPLIANCE with the clause rather than evasion of it.",
      "WHY IT IS ARMED RATHER THAN INERT: S23-AC5 sends an OP-x-5 card to Andrew recommending a rate threshold. A vacuous AC3 pass carries an implicit 'partner impact checked, zero would trip' to the sovereign when NO partner traffic was examined, because no partner is identifiable on any plane we hold. That is the C-4 harm one layer up -- C-4 exists so a missing observation does not lock out a partner office, and here a missing observation would silently underwrite the number that throttles them. Routed DIRECTLY to 0.7.0_AE_CloudOps~S before this row was filed, per the commission's instruction.",
      "A SECOND INSTANCE OF THE SAME CLASS, ALREADY HANDLED, recorded as corroboration that the class is real rather than as a new defect: S20-AC4 on this seat's own face asks for the S16 table's ALLOW rows to be compared item-by-item against a file that was never written. An empty-against-absent comparison is vacuous, and 'equal, 0 == 0' would have been a criterion satisfied by the ABSENCE of the work. It was filed UNCOMPUTABLE-BY-CONSTRUCTION rather than PASS. TWO OF THE 62 CARRY THIS SHAPE AND BOTH ARISE FROM THE SAME HELD CELL, which is the tell: when a face is HELD, every criterion downstream of its output silently becomes vacuously satisfiable.",
      "THREE FURTHER UNSOUND CRITERIA WERE ALREADY FOUND AND AMENDED BY OTHER LANES AND ARE COUNTED IN THE DENOMINATOR BUT NOT RE-FILED HERE: S13-AC2 (status-code oracle on XML-RPC, this seat's Z-S129), S15-AC3 (demanded 'only the reconciler's role' over a population necessarily including account administrators, Z-S125), S9C-AC4 (observation window derived from a trigger cadence for two functions having none, Z-S128). Re-filing them would inflate this sweep's yield without adding a fact.",
      "THE SOUND RESULT IS ALSO A RESULT, and several criteria are hardened against precisely the classes hunted -- naming them because they are the shape the estate should copy: S10C-AC1 DISQUALIFIES Invocations by name as an aliveness oracle citing Z-S124 and demands the instrument's discriminating power be stated. S9C-AC1 states that a quiet CloudTrail is not evidence of no access unless the trail was recording, and FAILS a no-access claim from an unverified trail. S12-AC1 refuses get-attributes alone and requires a delivered object with its key and LastModified. S11-AC2 and S19-AC2 both name their POSITIVE CONTROL in the criterion text and say in terms that without it the refusal proves nothing. S10-AC3 and S10B-AC1 both carry an explicit negative control so the acceptance is not measuring 'everything passes'. S9-AC1 files UNCOMPUTABLE rather than PASS on a single-plane clean read. S15-AC2 asks for the IP set's LockToken behaviour so a no-op reconcile is distinguishable from a rewrite producing the same list -- the same discriminator this seat used for S20-AC5.",
      "PATTERN-CLASS COVERAGE, so the sweep's reach is legible rather than implied. CLASS 1 status-code oracles on tunnelled protocols: 1 instance, S13-AC2, already filed as Z-S129 and routed; TO-OP-S-12's caller observation was checked and does NOT carry it -- 0.7.0_AE_CloudOps~Z confirmed at msg-id 20153 that log_credential fires inside the handler after authorize() returns ok=True, so a failed migration emits nothing, and its retirement gate is a PRESENCE condition positive-controlled by the S12-AC3 fixture. CLASS 2 metric oracles reading zero for a live subject: 0 instances; the one criterion that could have carried it, S10C-AC1, disqualifies the bad instrument by name. CLASS 3 absence oracles over an instrument that never recorded: 0 un-guarded instances; S9C-AC1 and S9-AC1 both guard it explicitly. CLASS 4 criteria requiring a state the gated work itself produces or that cannot exist: 2 instances, S23-AC3 (new, above) and S20-AC4 (already handled)."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): NO FINDING WAS MANUFACTURED TO JUSTIFY THE SWEEP, which the commission warned against in terms. The honest yield of reading all 62 is ONE new item, and the more useful output may be the negative result: the classes the issuer feared are largely ALREADY guarded in this project's criteria, and guarded explicitly, by name, with the disqualified instrument cited. THE GENERALISATION WORTH KEEPING IS NOT THE CRITERION BUT THE STRUCTURAL TRIGGER: WHEN A CELL GOES HELD, EVERY CRITERION DOWNSTREAM OF ITS OUTPUT SILENTLY BECOMES VACUOUSLY SATISFIABLE. Both class-4 instances found here descend from one held cell, OP-s-20, and neither criterion is badly written -- each was sound on the day it was cut, and each was made un-failable by a decision taken elsewhere afterwards. That is not a drafting defect a careful author could have avoided at cut time; it is a coupling that only appears once a hold lands. THE CHEAP CONTROL, offered as a suggestion and not a ruling: when a cell is put on HOLD, sweep the OTHER faces for criteria that iterate over or compare against that cell's output, because those criteria have just silently changed meaning. That is a check on the HOLD, not on the criteria, and nothing in the pipeline performs it today.",
    "owner": "0.7.0_AE_CloudOps~S",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps~S",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "0.7.0_AE_CloudOps~S",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S133",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "THE SPLIT-DRIFT CLASS HAS NO ESTABLISHED DENOMINATOR AND A NAME SEARCH CANNOT GIVE IT ONE. Z-S131 records the second instance and cites Z-S114 as the first. Sizing it: in the PROJECT TREE the drift signature resolves to exactly ONE stale line -- PRD:321, the one Z-S131 found -- so that plane is done. In INFRA my sweep returned a MEASURED ZERO over 6,388 files AND FAILED ITS POSITIVE CONTROL: the KNOWN Z-S114 instance is at infra/aws/terraform/opsec/iam.tf:62-78 and my probe did not find it. TWO INDEPENDENT REASONS, both fatal: the Sid sits at :62 and the Resource at :69, seven lines apart, and comp-find matches within a line; and the bucket IS NEVER WRITTEN AS A LITERAL there -- the Resource is `aws_s3_bucket.data_security.arn`, a terraform reference. A search for the bucket's NAME could never match it at any line span. SO 'TWO INSTANCES' IS NOT A COUNT, IT IS THE NUMBER FOUND SO FAR BY SEATS WHO HAPPENED TO READ THOSE FILES.",
    "evidence": [
      "PROJECT TREE, SIZED AND CLOSED: comp-find for the drift signature (the pre-split bucket in a case or evidence role) across the project tree returns 6 hits, which resolve completely -- 1 real (prd/NFRA_OPSEC202609_PRD.md:321, 'write case file s3://opal-data-security/cases/...'), 3 being Z-S131's own row quoting that line back, and 2 FALSE POSITIVES on `opal-data-security-access-logs`, a DIFFERENT bucket whose name is a superset of the one searched and which appears in a correct log-delivery criterion. Subtracting the legitimate cases is what makes this a denominator rather than a scare number: the raw count of `opal-data-security` in the project tree is 180 across 22 files and almost all of it is CORRECT, because that bucket genuinely IS the log destination.",
      "INFRA, NOT SIZED, AND THE PROBE IS THE REASON: the same signature over `infra` returns 0 hits across 6,388 scanned files. THAT ZERO IS FALSE. Positive control, run because a zero from a probe is worthless without one: comp-find for `EvidenceStoreObjects|EvidenceStoreBucket` over the same path returns 2 hits, infra/aws/terraform/opsec/iam.tf:62 and :72 -- the exact instance Z-S114 reports. My drift probe did not return that file.",
      "REASON ONE, MEASURED AT SOURCE: iam.tf:62 is `Sid = \"EvidenceStoreObjects\"` and its Resource is at :69, SEVEN LINES BELOW. comp-find matches within a line, so any pattern requiring the Sid and the bucket together cannot fire on this shape no matter how the character window is tuned.",
      "REASON TWO, AND IT IS THE FATAL ONE: iam.tf:69 reads `Resource = \"${aws_s3_bucket.data_security.arn}/*\"` and :78 reads `Resource = aws_s3_bucket.data_security.arn`. THE BUCKET NAME NEVER APPEARS. It is a terraform resource reference resolved at plan time, so a literal search for `opal-data-security` is structurally incapable of finding this grant even on one line. Every future instance written in idiomatic terraform is equally invisible to a name search.",
      "THIS SEAT'S SECOND INSTANCE OF ONE ERROR TONIGHT, stated because the repeat is the point: at Z-S108 a literal search for `jwt-public-key` missed a grant written on the prefix wildcard `opal/auth/*`, and the lesson banked was that a permission question needs the authorization model rather than a name. Here the same instrument missed a grant written as a resource REFERENCE. Different mechanism, identical failure -- THE THING THAT MATTERS DOES NOT SPELL THE NAME -- and the second occurrence came four hours after the first, in a row about denominators."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHAT THIS ROW ASKS FOR: nothing, from anyone. It exists so that 'the second instance' is not read at L9 as 'the second of two'. The PRD line is 1.0.0_SA_CTO~Z's to fix as the L4 owner and the operator-role grant is placed by 2.0.0_SA_COO~Z, and neither is changed by this. THE INSTRUMENT THAT WOULD WORK, named rather than run because it is not this seat's sweep to complete: something that resolves terraform references to the buckets they name -- comp-iam parses terraform and comp-aws reads the live plane -- or, cheaper and sufficient for this class, a semantic sweep on the SID names, since a statement whose Sid says EvidenceStore and whose resolved resource is the log destination is exactly the drift, and the Sid is a literal that IS written. WHY I AM REPORTING A FAILED PROBE RATHER THAN A CLEAN PLANE: the zero was measured, over a printed denominator of 6,388 files, and it was WRONG. Reporting it as an absence would have converted a working class into a closed one and told three seats the infra plane was clear. The positive control is the only thing standing between those two outcomes, and it cost one call. A zero without one is not a finding, it is a guess with a number attached.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S134",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "WHAT Z-S110's MAP DEFECT COST, MEASURED, PLUS A FAR STRONGER PROOF OF ITS CENTRAL CLAIM. This row does NOT restate Z-S110's three axes -- that defect is filed and owned there. It records two things Z-S110 does not have: (1) the entry did not merely hold a false value, it successfully REDIRECTED A COMPETENT SEARCH, and the belief it manufactured propagated into a decomp row, a task-order face and two GO messages before anyone re-read it; and (2) the repo source provably IS production -- two clean builds byte-identical to each other AND to the artifact deployed 2026-01-08, 12 of 12 files by sha256, eight months later on a different Node major version.",
    "evidence": [
      "THE COST, WITH A NAMED VICTIM AND A TRACEABLE PATH. This seat read lambda-source-map.json:1740, followed its _note instruction -- 'No repo source. Code must be downloaded from AWS.' -- and downloaded the deployment package from Lambda. The repo source was found afterwards and only by a different route: searching for a distinctive constant from the DECOMPILED code (JWT_AUDIENCE = 'opal-portal-api'), which returned infra/aws/opalinvest_dev/lambda/session-analytics/src/auth.ts:16. The map is the estate's designated first place to look for exactly this pairing (CLAUDE.md Rule 4) and it sent a search away from an answer that was in the repo the whole time.",
      "AND THE BELIEF PROPAGATED THROUGH FOUR CARRIERS BEFORE ANYONE RE-READ THE MAP: 'no build path' appears in row Z-S123's notes, in TO-OP-S-10C's title and its WHY section, and in both GO messages (20143, 20155). Each carrier was faithful to the one before it. None was faithful to the repo, and none had to be -- the authority for the question had already answered it.",
      "THE BYTE-IDENTITY PROOF, which is the upgrade to Z-S110's central claim rather than a new claim. Z-S110 established the repo source is the build input by CONTENT, from the compiled shape of auth.js -- correct, and Rule 22a's prescribed method. This is the same claim on a stronger instrument: two builds from a clean state (source copied out of the repo, npm ci against the committed lockfile, npm run build) produce outputs byte-identical to EACH OTHER and to the artifact currently deployed. 12 of 12 first-party outputs -- index.js, auth.js, types.js, their .d.ts and all six .map files -- matching by sha256, not by size.",
      "THE VINTAGE SPREAD IS WHAT MAKES IT STRONG: the live artifact was deployed 2026-01-08 (LastModified, CodeSha256 eQswWf3zdISgafQwQ+GhHgyWNfoxPOSeriqYVxiN9VU=), and the reproducing builds ran 2026-09-03 on node 26.8.1 / npm 11.19.0 / TypeScript 5 against a nodejs20.x target. Eight months and a different Node major, and the bytes are identical. A tsc build over a pinned lockfile is deterministic, and this exercises that determinism rather than assuming it.",
      "SO 'Code must be downloaded from AWS' was not stale about a path that had moved. It was FALSE about a source tree that provably IS production, and the proof is available to anyone who runs two commands.",
      "SCOPE OF THIS ROW, stated so it is not read as wider: it asserts nothing about any OTHER entry in lambda-source-map.json. Whether sibling entries carry the same defect is unmeasured here and is not claimed."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): FILED AS A SEPARATE, NARROW ROW ON 0.7.0_AE_CloudOps~V's SUGGESTION AND THIS SEAT AGREES WITH THE REASONING (msg 20170). Z-S110 owns 'the entry is wrong'; this row owns 'here is what it cost and here is the proof the source is production'. Those are different claims with different remedies -- the first is a one-line map correction owned by 2.0.0_SA_COO~Z, the second is evidence supporting the Terraform adoption -- and deliberately NOT restating Z-S110's three axes is what keeps them from becoming two carriers of one obligation that drift apart. This seat had drafted a full second row and narrowed it after 20170 arrived. CLASS AND STANDING, reasoned rather than defaulted: OBSERVATION because it interrupts nobody's turn, and INERT rather than ARMED because the harm it describes has ALREADY OCCURRED and been caught -- the live hazard is Z-S110's wrong entry, which is ARMED there with its own disarm owner. Marking this ARMED as well would double-count one hazard across two rows, which is the same duplication the row's scoping avoids. WHY THIS IS WORTH A ROW AT ALL RATHER THAN A MESSAGE: the generalisable finding is not that one JSON entry was wrong. It is that a REGISTRY WHOSE ONE JOB IS A PAIRING can fail at that pairing in the direction that STOPS THE SEARCH -- 'EXTERNAL / no repo source' reads as a documented exclusion, not an error, so it is believed and not re-checked, and it is believed hardest by the most careful reader because it is the designated authority. The cost is invisible until someone disbelieves it for an unrelated reason. This seat disbelieved it only because a CloudTrail absence looked too convenient on a different question entirely. NON-APPLICATION: this says nothing about the map's other entries, and a map that is right is not made suspect by one that is wrong.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S135",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "THE /wp-admin ALLOW-LIST INPUT IS NOW DERIVABLE BUT NOT SAFE, AND BOTH HALVES MATTER. Five candidate addresses were derived and cross-corroborated on two independent axes, so Z-S102's missing input finally has evidence behind it. But 98.4% of the apparent successes were attack traffic caught by the same User-Agent check that saved TO-OP-S-20, the WordPress status semantics are INVERTED from the obvious reading (a FAILED login returns 200, a success returns 302), and the five surviving addresses look RESIDENTIAL and DYNAMIC -- three appear for a single short session and never again. An allow-list of dynamic addresses locks the administrator out the day their lease rolls. NOTHING WAS APPLIED.",
    "evidence": [
      "WINDOW AND DENOMINATORS, on the origin's own OpenLiteSpeed access logs -- still the only plane that sees this site, since opalinvest.com resolves to the EIP and the edge ACL has no logging configuration: 30/Jul/2026 to 04/Sep/2026, 620,837 total request lines, 105,217 to wp-login.php, 20,938 to /wp-admin.",
      "THE STATUS SEMANTICS ARE INVERTED HERE AND READING THEM THE OBVIOUS WAY WOULD HAVE INVERTED THE ANSWER: on WordPress a FAILED login returns HTTP 200 because the form re-renders carrying an error, and a SUCCESSFUL login returns 302 to the destination. The wp-login.php distribution is POST 200 x 87,819, GET 302 x 8,979, GET 200 x 7,211, POST 302 x 882, GET 404 x 214, GET 304 x 88, GET 301 x 14, HEAD 200 x 4, POST 503 x 3, POST 500 x 2, HEAD 302 x 1. THE 87,819 POST 200s ARE THE FAILURES. A seat inferring success from 200 would have derived an allow-list consisting almost entirely of the credential-stuffing population -- the same shape as Z-S129 one surface over, and the reason that row's generalisation was worth keeping.",
      "THE USER-AGENT CHECK THEN REMOVED 98.4% OF THE APPARENT SUCCESS SET, exactly as it did on TO-OP-S-20. The 882 POST-302 events split into two populations with OPPOSITE signatures. ATTACK, by distinct-User-Agent count per address: 185.209.196.170 with 416 events across 48 DISTINCT agents; 161.118.221.78 with 311 across 48; 103.59.160.242 with 72 across 40; 138.199.60.10 with 36 across 27; 116.212.155.127 with 33 across 22 -- 868 of 882. An address cycling 48 browser identities is credential stuffing with agent rotation, not an administrator. It is day-clustered too: 417 events on 02/Sep and 313 on 10/Aug. PLAUSIBLE: 68.200.202.19 (9 events, 2 agents), 206.194.219.89 (2, 2), 73.91.54.160 (1, 1), 174.212.34.62 (1, 1), 174.135.219.93 (1, 1) -- 14 of 882.",
      "A SECOND AXIS SHARING NO FIELD AGREES, WHICH IS WHY THE SPLIT IS TRUSTED RATHER THAN ASSERTED. Loading an admin PAGE with a 200 requires a real authenticated session. Those 200s come from EXACTLY the five plausible addresses and in the same rank order: 68.200.202.19 -> 672, 174.212.34.62 -> 55, 206.194.219.89 -> 50, 73.91.54.160 -> 44, 174.135.219.93 -> 16.",
      "AND THE SPLIT IS POSITIVE-CONTROLLED RATHER THAN RESTING ON AN ABSENCE: all five ATTACK addresses return 0 admin-page 200s under the same matcher that returns 672 for 68.200.202.19. So the zeros are a real absence and not a broken pattern -- the control this seat failed to run on its first xmlrpc census and has run by default since.",
      "CANDIDATE RECENCY, which is what makes the list unsafe rather than merely short: 68.200.202.19 spans 07/Aug to 31/Aug (sustained); 174.212.34.62 appears only 03/Sep 22:01-22:33; 206.194.219.89 spans 03/Aug to 28/Aug; 73.91.54.160 appears only 10/Aug for six minutes; 174.135.219.93 only 14/Aug for 26 minutes. THREE OF FIVE ARE SINGLE SHORT SESSIONS NEVER SEEN AGAIN, and two of the five are both in 174.x -- the signature of one person whose ISP reassigned them rather than five distinct offices.",
      "WHAT CANNOT BE ATTRIBUTED, STATED RATHER THAN OMITTED: 0 of 5 addresses can be tied to a NAMED PERSON from these logs. The record carries an address and a browser string and no identity. Which of them is Patricia at TWLC (named as WP-admin in infra/aws/terraform/website/README.md), which is Opal staff, and whether one human accounts for several rows, are all unknown from this plane."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): FILED AS AN OBSERVATION AND INERT BECAUSE NOTHING WAS APPLIED AND NOTHING IS ARMED BY IT -- Z-S102 remains the ARMED row and this one supplies the evidence Z-S102 was waiting for rather than replacing it. THE PART WORTH CARRYING PAST THIS CELL IS THE INVERSION: this estate's own instinct, and the one the issuer's xmlrpc condition encoded, is that a 200 means the request succeeded. ON A LOGIN FORM THE OPPOSITE IS TRUE, because the failure path is a re-render and the success path is a redirect. So the status plane does not merely fail to answer here as it did on XML-RPC -- IT ANSWERS CONFIDENTLY BACKWARDS, and a seat that had learned only the xmlrpc lesson (a 200 is uninformative) would still have got this wrong in the other direction. The durable form is narrower than either: DO NOT READ A STATUS CODE AS AN OUTCOME UNTIL YOU HAVE ASKED WHAT THIS PARTICULAR ENDPOINT RETURNS ON FAILURE. AND THE SECOND-AXIS DISCIPLINE IS WHAT MADE THE ANSWER USABLE RATHER THAN MERELY CAUTIOUS: the User-Agent split alone would have been a judgement call, and the admin-page-200 axis -- which shares no field with it and required a genuine authenticated session -- is what turned a plausible partition into a corroborated one. THE RECOMMENDATION MADE TO THE ISSUER, NOT TAKEN HERE: do not apply this list as-is; one answer from Andrew about which address is his or Patricia's, or whether a static office egress exists, collapses the entire problem, and a dynamic-address allow-list would lock out the very person who would otherwise fix it.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S136",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "TERRAFORM IS A SECOND WRITER OF THE BLOCKED-IP SETS AND C-2 CANNOT SEE IT. All FOUR sets declare `addresses = []`, which does not mean Terraform leaves addresses alone -- it means Terraform DECLARES THE SET EMPTY and enforces that on every apply. So any portal-auth or opal-gateway apply, by any operator, for any unrelated reason, ERASES the reconciler's entire block list. Already queued live: the portal-auth plan wants to delete 203.0.113.42/32 right now. No IAM census can detect this, including this seat's own TO-OP-S-22 verdict and Z-S125's 231-principal sweep, because Terraform needs no fourth principal -- it acts AS an administrator who already holds the action.",
    "evidence": [
      "THE LIVE PLAN, taken UNSCOPED on infra/aws/terraform/portal-auth with this seat's own file moved aside so it is a true BEFORE, rc=2 captured directly rather than through a pipe: `Plan: 0 to add, 3 to change, 0 to destroy` -- aws_wafv2_ip_set.opal_blocked_ips_cloudfront_v4, its _v6 sibling, and aws_wafv2_web_acl.opal_cloudfront_protection, all in-place. 0 destroy, 0 forces-replacement.",
      "THE DIFF THAT IS THE FINDING, quoted from that plan: `~ addresses = [ - \"203.0.113.42/32\", ]`. Terraform is queued to DELETE a live blocked address. It is a TEST-NET-3 fixture (RFC 5737), so nothing real is protected by it today -- which is exactly why this is catchable now instead of after a real block.",
      "THE MECHANISM, at source: waf-cloudfront.tf:348 and :361 both read `addresses = []`. That is not an absence of management, it is a DECLARATION OF EMPTINESS. Terraform enforces declared state, so every apply reconciles the set back to zero addresses.",
      "AND THE FILE'S OWN COMMENT STATES THE INTENT THE CODE DOES NOT ACHIEVE, waf-cloudfront.tf:320-325: 'An address added here by hand -- or by this face -- would be a second source of truth for the block list and would drift from the table the moment either changed. `addresses` stays `[]` in Terraform and is reconciled from the table, NEVER AUTHORED.' The reasoning is correct and the remedy it implies -- ignore_changes -- is absent. The comment says never authored; the code authors it, as the empty list.",
      "THE DENOMINATOR IS 4 OF 4 SETS ACROSS 2 ROOTS, and the regional pair was checked rather than assumed: opal-gateway/waf.tf:264 and :274 also read `addresses = []`, carrying the same comment at :252 ('addresses stays [] in Terraform') and the same description naming the reconciler as the only writer. An enumerate for lifecycle / ignore_changes across that file returns ZERO hits. Neither root guards any of its sets.",
      "NEGATIVE CONTROL ON THE GUARD-ABSENCE CLAIM, so it is a measured zero and not a missing probe: the same enumerate over waf-cloudfront.tf DOES return a lifecycle block at :239 with `ignore_changes = [tags, tags_all]` on a different resource. The pattern exists in the file and is simply not applied to the IP sets.",
      "WHY NO IAM INSTRUMENT CAN SEE IT: TO-OP-S-22's verdict established the reconciler is the only one of the three chain roles holding wafv2:UpdateIPSet (sentinel and CLI both explicitDeny on all four sets), and Z-S125 widened that to a 231-principal sweep finding one service principal plus three administrators. Both are correct. Terraform does not add a principal -- it acts AS the operator running the apply, which per Z-S125 is already an administrator holding the action. C-2 is an IAM invariant and this is a DECLARED-STATE writer, so every arm of every identity check passes while the invariant breaks."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): COMPOSES WITH Z-S125 IN THE DANGEROUS DIRECTION AND THAT IS THE POINT OF FILING IT SEPARATELY RATHER THAN AS A NOTE ON THAT ROW. Z-S125 concluded the residual was an administrator making a deliberate console click -- judged unlikely, self-repairing on the reconciler's next pass, and left as an accepted risk. This makes the SAME erasure happen through a well-intentioned unrelated deploy. That is not an unlikely event, it is the routine one, and it converts an accepted residual into a live hazard without changing anything about the IAM plane Z-S125 measured. NOT THIS FACE'S TO FIX, AND THE BOUND IS EXPLICIT: waf-cloudfront.tf belongs to TO-OP-S-4-18 and the reconciler's cell, and 2.0.0_SA_COO~Z's scope ruling (msg 20180) bounds this seat to ONE Lambda -- 'a rotation-blocker face is not an authorisation to restructure a root'. The remedy is one lifecycle block per set and it is named, priced and left. WHAT WOULD MAKE THE EXERCISE MISS IT, worth stating for whoever runs S15-AC2: an end-to-end block and unblock will PASS with this live, because the erasure is not on the reconciler's path -- it happens later, from a different actor, on an unrelated trigger. A green idempotence test is not evidence against this. HOW IT WAS FOUND, because the route matters more than the find: it came out of an UNSCOPED baseline taken before an unrelated Lambda import, for the sole purpose of proving that adoption would not carry foreign changes. The estate's rule that a scoped act still takes an unscoped baseline is what surfaced it; a -target plan on the Lambda would have been clean and silent.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S137",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "SUBORDINATE TO Z-S136, WHICH REMAINS THE FINDING OF RECORD -- this row adds only what that row could not yet contain: the proposed remedy is MEASURED EFFECTIVE, 4 queued address deletions to 0 across both roots, live sets intact. AND IT NAMES A TRAP THAT WILL OTHERWISE CAUSE A FALSE RE-RAISE: after the guard, all four ip_sets STILL read 'will be updated in-place' in the plan, because their DESCRIPTION is separately drifted. The discriminator is the DELETION COUNT INSIDE THE addresses DIFF, never the resource's presence in the change list.",
    "evidence": [
      "AUTHORSHIP, stated because the defect is this seat's and the record should say so plainly: git log -1 on infra/aws/terraform/portal-auth/waf-cloudfront.tf returns 819d704105, 0.7.0_AE_CloudOps~S, TO-OP-S-4-18. This seat wrote `addresses = []` in BOTH roots and wrote the comment asserting the sets are 'reconciled from the table, never authored' -- correct as intent, false as a description of what the code does.",
      "BEFORE, unscoped plans on both roots with rc captured directly rather than through a pipe: portal-auth 0 to add / 3 to change with `- \"203.0.113.42/32\"` on the v4 set and `- \"2001:0db8:dead:beef::/64\"` on the v6; opal-gateway 0 to add / 2 to change with the identical pair on the regional sets. Live contents read with get-ip-set at that moment: all FOUR sets held exactly one address and all four were queued to lose it.",
      "AFTER, the same two unscoped plans with the lifecycle ignore_changes = [addresses] blocks in place on all four resources: QUEUED ADDRESS DELETIONS 0 of 0 on portal-auth and 0 of 0 on opal-gateway, counted on the deletion lines inside the addresses diff. Live sets re-read after the plans and still holding 203.0.113.42/32 on both v4 sets -- nothing was applied to obtain this evidence.",
      "THE TRAP, AND IT IS WHY THIS ROW EXISTS RATHER THAN A MESSAGE: after the guard the ip_sets are STILL listed as 'will be updated in-place', because their description attribute is separately drifted from this seat's earlier WAFv2 description fix. A reader checking whether Z-S136 is resolved by looking for the ip_sets in the change list WILL FIND THEM AND CONCLUDE THE HAZARD PERSISTS. The resource's presence in the plan is not the tell. The tell is whether the addresses diff contains a deletion line.",
      "SCOPE CORROBORATED INDEPENDENTLY, not repeated from Z-S136: msg 20192 flagged the regional pair as unverified and said so rather than assuming. This seat measured opal-gateway/waf.tf:264 and :274 directly and they carry the same `addresses = []` shape. Z-S136 already states all four; this is a second instrument agreeing, on a plane the first seat declined to assert."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS A SEPARATE ROW AND NOT AN EXTENSION OF Z-S136, stated so the two carriers have a NAMED PRIMARY and cannot drift: Z-S136 is the finding of record and nothing here amends it. A FINDING AND ITS REMEDY ARE TWO CLAIMS, and Z-S136 could only evidence the first -- it proposed the lifecycle block correctly but no seat had yet shown that the block actually removes the deletion. A remedy that is proposed, endorsed and never exercised is the shape this project has been bitten by repeatedly, so it is exercised here and the numbers are printed. WHY THE AUTHOR OF THE DEFECT FILED IT: the finding came from a seat that does not own the cell, took an unscoped baseline for an unrelated purpose, and routed it rather than filing over the owning lane's head. Leaving that seat to also carry the verification of someone else's repair would put the whole durable record of this seat's defect in another lane's hands. THE REUSABLE PART: C-2 was verified on the PRINCIPAL plane by two independent instruments -- TO-OP-S-22's per-role verdict and S15-AC3's 231-principal sweep -- and both were correct and neither could see this, because the second writer was not a principal at all but the DECLARATION. An invariant phrased as 'nothing else ever calls X' has at least two planes, and an identity census covers exactly one of them. Ask which plane an invariant lives on BEFORE choosing the instrument that certifies it.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S138",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "ALL FOUR OF Z-S136's QUEUED DELETIONS ARE DOCUMENTATION-RANGE FIXTURES, MEASURED, SO THAT HAZARD IS LATENT RATHER THAN AN ACTIVE LOSS OF PROTECTION. wafv2 get-ip-set on all four blocked-IP sets returns ONE address each, total 4 -- matching Z-S137's queued-deletion count exactly. The two IPv4 entries are 203.0.113.42/32, inside TEST-NET-3, which RFC 5737 reserves for DOCUMENTATION; the two IPv6 entries are 2001:0db8:dead:beef::/64, inside the 2001:db8::/32 prefix RFC 3849 reserves for the same purpose, carrying a dead:beef placeholder. NOT ONE IS REAL BLOCKED TRAFFIC. Z-S136's mechanism, its remedy and its ARMED standing are untouched -- what this settles is WHEN it bites: the moment the reconciler writes its first real address, not the next unrelated apply.",
    "evidence": [
      "THE LIVE READ, complete over the population rather than sampled: wafv2 list-ip-sets returns 4 sets across both scopes (opal-blocked-ips-cloudfront b2e008a6, -cloudfront-ipv6 eb1a0caa, -regional f073f448, -regional-ipv6 85f90377) and get-ip-set on each returns Addresses of length 1. Total 4, which reconciles exactly with Z-S137's independently measured '4 queued address deletions to 0'.",
      "WHAT THE FOUR ARE: 203.0.113.42/32 in both IPv4 sets -- 203.0.113.0/24 is TEST-NET-3, reserved by RFC 5737 for documentation and examples, from which no real traffic originates. 2001:0db8:dead:beef:0000:0000:0000:0000/64 in both IPv6 sets -- 2001:db8::/32 is reserved by RFC 3849 for documentation, and dead:beef is a placeholder idiom rather than an allocation.",
      "AND IT AGREES WITH A ROW ALREADY ON THE CHANNEL rather than resting on this seat's reading alone: Z-S102 established from the TO-OP-S-4-18 carrier that the sets are EMPTY BY DESIGN under constraint C-2, quoting it in-line -- 'THE SETS ARE EMPTY AND THIS RULE BLOCKS NOBODY ON DAY ONE' -- and that only the OP-s-15 reconciler may write them. Four fixture entries in otherwise-empty sets is exactly the state that describes.",
      "WHAT IS NOT MEASURED HERE AND IS NOT CLAIMED: whether the fixtures were placed by the reconciler's own exercise or by an earlier act. This row establishes WHAT the addresses are, not WHO wrote them, and the distinction does not affect the grading question it exists to answer."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS FILED AT ALL, given Z-S136 is correct as written and its remedy is already verified effective at Z-S137: an ARMED row's PRIORITY is set by what it would destroy, and no row states that. A reader meeting 'queued live ... right now' reasonably infers protection being removed under them, and would order their queue accordingly. THE PHRASE IS THE AUTHOR'S AND IT IS TRUE -- the plan does want to delete that address -- so nothing in Z-S136 is corrected here; what is added is the object's nature. THIS ALSO CORRECTS THIS SEAT'S OWN HEDGE, and the shape of that error is worth the line: on reading Z-S136 this seat amplified it up-lane with the gloss 'an address that is currently blocking traffic', which the row never said, then corrected that two minutes later by recognising 203.0.113.42 as TEST-NET-3 -- reasoning from the ONE address the row happened to name. Z-S137 then reported FOUR queued deletions, so the correction covered one of four and the other three were unexamined. AN OVERSTATEMENT CORRECTED FROM A SINGLE EXAMPLE IS STILL A CLAIM ABOUT A POPULATION, and the fix was the same three calls that produced this row. Measuring all four is what turns 'almost certainly a fixture' into a fact.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S139",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Z-S123 SAID opal-session-analytics 'BREAKS PERMANENTLY' UNDER A ROTATION AND THAT IS AN OVERSTATEMENT. The no-TTL half is correct -- the cache has no time-based expiry, so no wait converges it and 'wait N minutes' is unsatisfiable at any N as a GUARANTEE. But the cache IS bounded by CONTAINER LIFETIME, which 0.7.0_AE_CloudOps~W measured: median 5.6 min, p90 52.3, p99 138.0, max observed 143.0 (2.4 h) over 107 measurable spans of 200 sampled, NextToken present so a FLOOR not a census. So the true shape is a PARTIAL, SILENT, SELF-CLEARING OUTAGE OF UNBOUNDED TAIL DURATION -- and 0.7.0_AE_CloudOps~W's sharpening is that this is WORSE than permanent breakage in one respect, because PERMANENT BREAKAGE GETS NOTICED and a partial outage that clears on its own is absorbed as 'some 401s during the rotation' and never traced to this consumer.",
    "evidence": [
      "WHAT Z-S123 SAID, verbatim from the committed row: 'a consumer with NO build path and NO TTL cannot receive a rotated key and cannot expire itself into a retry. It breaks PERMANENTLY with no mechanism available to repair it afterwards.' Its notes field repeats the claim: 'it cannot heal itself and it cannot be patched.'",
      "WHAT IS CORRECT AND SURVIVES: the cache is one scalar with no time component (auth.js:24-26, `if (cachedPublicKey) return cachedPublicKey;`, no invalidation), so it NEVER expires by time. A rotation runbook cannot contain a 'wait N minutes for convergence' step for this consumer at any N, because no N is a guarantee. That is the operationally load-bearing half and it is unchanged.",
      "WHAT IS WRONG: 'cannot heal itself' and 'breaks PERMANENTLY'. A Lambda execution environment is eventually recycled, and the replacement fetches the then-current key on its first call. So the population of stale containers DECAYS to zero without intervention. 0.7.0_AE_CloudOps~W measured the decay from log-stream creation-to-last-event: median 5.6 min, p90 52.3 min, p99 138.0 min, maximum observed 143.0 min.",
      "THE BOUND 0.7.0_AE_CloudOps~W PUT ON ITS OWN NUMBER, carried here because it is what makes the number usable: 107 measurable spans of 200 sampled with NextToken PRESENT, so it is a FLOOR and not a census, and the sample is ordered by last-event time and therefore biased toward recently-active containers. The observed maximum is not the possible maximum. jwtPublicKeys.mjs:17-23 already states the structural half -- a stale container serves until it happens to be recycled, and Lambda does not bound execution-environment lifetime.",
      "SO BOTH HALVES ARE TRUE AT DIFFERENT GRAINS, which is why the wrong word slipped through: UNBOUNDED-IN-PRINCIPLE (no mechanism guarantees convergence) and FINITE-IN-PRACTICE (containers die, typically within minutes). Z-S123 collapsed those into 'permanent', which is the reading of the first that contradicts the second."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THE OVERSTATEMENT MATTERS OPERATIONALLY RATHER THAN JUST BEING IMPRECISE. 'Breaks permanently' implies a hard, visible outage requiring intervention -- which is ALARMING and therefore self-correcting: someone notices and someone fixes it. The measured shape is the opposite: a fraction of requests fail, the fraction shrinks on its own, and the incident closes itself before anyone attributes it. 0.7.0_AE_CloudOps~W's phrase is the one worth keeping -- PERMANENT BREAKAGE GETS NOTICED. So the corrected version argues MORE strongly for the remedy than the overstatement did, not less, and that is the opposite of the usual direction a retraction runs. HOW THE WORD GOT IN, since the mechanism generalises. Z-S123's job was to select a branch of a trichotomy, and the branch turned on ALIVE-versus-DEAD. Having measured 141,685 invocations this seat reached for the strongest available statement of consequence to justify the hard branch -- and 'permanent' was a rhetorical upgrade of 'no mechanism guarantees convergence', which is the thing actually measured. THE TELL WAS AVAILABLE IN THIS SEAT'S OWN ARTIFACT: jwtPublicKeys.mjs, written by this seat hours earlier, says a stale container serves 'until it happens to be recycled'. That sentence contains the refutation of 'permanently' and this seat wrote both. A claim contradicted by one's own committed source is the cheapest kind to catch and the easiest to walk past, because authorship reads as agreement. WHAT DOES NOT CHANGE: Z-S123's verdict, its branch selection, and TO-OP-S-10's blocked status all stand. The consumer is ALIVE, it is a genuine rotation blocker, no wait converges it, and it needs either a redeploy per rotation or the two-slot module. Only the word 'permanently' is withdrawn. AND ONE THING 0.7.0_AE_CloudOps~W FOUND THAT INVERTS THE FACE'S PREMISE ENTIRELY, recorded because it is a better fact than the correction: this consumer HAS a src/ directory, so the canonical lib mirror into <source_dir>/src/lib/ applies to it DIRECTLY -- while neither portal-authorizer nor auth-validator-edge has one. The consumer that looked least maintainable is the one the shared remedy fits most cleanly of the three.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S140",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Z-S127 SIZED: FORGEABLE AND REACHABLE, the worst of the issuer's three branches. The HMAC secret both MINTS and VERIFIES on a live public API -- trade-submission-api (w8jnzvs21g) has a deployed prod stage, DisableExecuteApiEndpoint FALSE, and SIX of its seven routes are CUSTOM-authorized by the very authorizer that validates with JWT_SECRET. The 129-day dormancy was ABSENCE OF TRAFFIC, NOT ABSENCE OF WIRING: an unauthenticated probe WOKE the authorizer and its log stream advanced from 129 days stale to now. And WHO CAN READ IT is 14 principals of 231 simulated, including THREE human/interactive IAM users -- a number my earlier document scan got wrong in BOTH directions.",
    "evidence": [
      "MEASUREMENT ONE, DOES ANYTHING STILL VALIDATE -- YES, AND IT MINTS TOO. Both halves are in the DEPLOYED bytes, not the repo. trade-authorizer's authorizer.py validate_token() computes hmac.new(JWT_SECRET.encode(), payload_b64.encode(), hashlib.sha256) and compares it to the presented signature. trade-auth-handler's auth_handler.py generate_token() signs with the SAME secret at :147-148. Both carry the identical hardcoded fallback JWT_SECRET = os.environ.get('JWT_SECRET', 'trade-form-secret-change-in-prod'), so an absent env var would fail OPEN onto a guessable committed string rather than fail closed.",
      "THE TOKEN IS NOT A JWT. validate_token splits on '.' and requires exactly TWO parts, payload and signature -- there is no header and no alg field. Holding the secret lets a caller mint a token asserting any identity; there is no asymmetry and no key id to pin.",
      "REACHABILITY, live: apigatewayv2 get-api on w8jnzvs21g returns Name trade-submission-api, ProtocolType HTTP, ApiEndpoint https://w8jnzvs21g.execute-api.us-east-1.amazonaws.com, and DisableExecuteApiEndpoint FALSE -- the public execute-api endpoint is enabled. get-stages returns ONE stage, 'prod', AutoDeploy true, last deployment successful. get-routes returns 7 routes of which SIX carry AuthorizationType CUSTOM and AuthorizerId nfa51m; get-authorizers resolves nfa51m to name 'trade-auth' pointing at the trade-authorizer function. The seventh, POST /auth, is AuthorizationType NONE -- it is the mint endpoint.",
      "THE DORMANT AUTHORIZER WOKE, which is the measurement that turns configuration into fact. An unauthenticated GET to https://w8jnzvs21g.execute-api.us-east-1.amazonaws.com/prod/submissions returned HTTP 401; the same request carrying a junk bearer token returned HTTP 403, meaning the authorizer EVALUATED the signature and refused; and a control request to /prod/nonexistent returned 404, so the 401/403 are the authorizer answering rather than a blanket response. trade-authorizer's CloudWatch log stream advanced from lastEventTimestamp 2026-04-27T23:35:28Z (129 days) to 2026-09-04T05:09:16Z. NO TOKEN WAS FORGED: source and configuration already establish forgeability, and minting one would have created a real session rather than measured one.",
      "MEASUREMENT TWO, WHO CAN READ IT -- 14 of 231, by SIMULATION as the ruling required. Every principal was simulated with iam:simulate-principal-policy for lambda:GetFunctionConfiguration AND lambda:GetFunction against arn:aws:lambda:us-east-1:313476888478:function:trade-authorizer, ONE resource ARN per call. DENOMINATOR 231 = 224 roles from the applied census plus 7 IAM users, nothing sampled; 14 allowed, 217 denied, 0 errors. ALLOWED: 2 AWS service-linked roles (AWSServiceRoleForSupport, AWSServiceRoleForResourceExplorer); 9 Opal roles (github-actions-opal-deploy, infrastructure-ops-lambda-role, infrastructure-snapshot-role, opal-drift-producer-codebuild-role, opal-globgrph-derive-runner-task, opal-globgrph-incremental-updater, opal-news-lambda-role, opal-portal-lambda-role, security-sweep-dedicated-role); and THREE human/interactive IAM users (Andrew_Berman, Andrew_Berman_Console, Opal_Terminal).",
      "CONTROLS ON THE SWEEP, both run in ISOLATION per the /cloud-ops trap that batching corrupts them. POSITIVE: infrastructure-snapshot-role returned 'allowed', which is what proves the action names are real -- simulate does not validate action names and a typo denies exactly like a missing grant. NEGATIVE: the same role against lambda:ZzzNoSuchActionName9999 returned implicitDeny, demonstrating that a deny on its own carries no information about action validity.",
      "Vintages: deployed-byte reads and live API reads 2026-09-04T05:0x-05:1xZ; IAM census 2026-09-04T03:45:22Z; simulation sweep 2026-09-04T05:1xZ."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THE ISSUER'S METHOD RULING IS WHAT MADE THIS RIGHT, AND MY DOCUMENT SCAN IS THE COUNTER-EXAMPLE THAT PROVES IT. 20224 said simulate the principals rather than filtering policy documents for a string, citing the four UpdateIPSet holders of which three were inherited. The same thing happened here in both directions at once. A DOCUMENT SCAN ANSWERS 'WHICH POLICIES MENTION THIS' AND THE QUESTION WAS 'WHO CAN DO THIS'. TWO DEFECTS IN MY OWN FIRST SWEEP, recorded because each would have produced a confident wrong number: (a) I simulated only GetFunctionConfiguration, and FIVE of the eleven roles hold the capability solely via GetFunction, which also returns the environment -- they would have scored denied; (b) my script reported '0 IAM users' and I nearly took it, because `bash .tools/aws iam list-users` invoked from a python subprocess CRASHES with a Windows ACCESS_VIOLATION (rc 3221225477) returning EMPTY stdout AND EMPTY stderr, which is byte-identical to 'this account has no users'. It was caught ONLY by a guard comparing the enumeration against the census user_count, and had it stood it would have dropped all three human principals -- including both of Andrew's -- out of the finding. A CRASHED PROCESS AND AN EMPTY POPULATION ARE THE SAME BYTES; only a cross-check separates them. WHAT THIS ROW DOES NOT CLAIM: it does not claim the secret has leaked, that any of the fourteen has read it, or that the trade API has been abused. It claims the secret is live, mints and verifies on a publicly reachable authorized API, and is readable by a measured 14 of 231 principals. Dormancy lowers the URGENCY and not the EXPOSURE, exactly as 20224 predicted: the first call after a year accepts a token forged today.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S141",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "IT IS A FINDING, NOT A DEMONSTRATED INCIDENT -- and the reason it cannot be called a demonstrated NON-incident is that no instrument reaches. YES the API has been successfully authenticated against: on 2026-01-07 it served 105 requests with ZERO 4xx and ZERO 5xx while the authorizer ran 18 times, and an authorizer DENY is a 4xx, so all 18 were ALLOW. Lifetime before my probe: 272 requests, ~237 non-error, 55 authorizer runs, 28 mint-path runs, last real activity 2026-04-26. BUT abuse detection is UNCOMPUTABLE beyond 14 days: stage access logging was NEVER enabled, the authorizer's log group is 14-day retention with storedBytes 0, and no CloudTrail records DynamoDB or this API's data events.",
    "evidence": [
      "INSTRUMENT REACH FIRST, because a no-abuse reading from an instrument that never recorded is the same vacuous answer the CloudTrail leg already produced once tonight. (a) API GATEWAY ACCESS LOGS: apigatewayv2 get-stage on w8jnzvs21g/prod returns AccessLogSettings NULL and DefaultRouteSettings.DetailedMetricsEnabled FALSE, and describe-log-groups for prefix /aws/apigateway returns an EMPTY list account-wide. Access logging was NEVER enabled, so there is no per-request record to search and no per-route metric split. (b) AUTHORIZER LOGS: /aws/lambda/trade-authorizer has retentionInDays 14 and storedBytes 0. Stream METADATA survives from 2026/01/12 and 2026/04/27, but the EVENTS are expired.",
      "THAT EXPIRY WAS TESTED RATHER THAN ASSUMED, with a control: get-log-events on the 2026/04/27 stream returns an EMPTY array, while get-log-events on my own 2026/09/04 stream returns its events including the line 'Invalid token'. So the retrieval works and the April emptiness is genuine expiry, not a broken call. It also confirms the mechanism from the other side: 'Invalid token' is what lambda_handler prints when validate_token's HMAC comparison fails, so the authorizer demonstrably evaluated a signature.",
      "WHAT DOES REACH IS CLOUDWATCH METRICS (15-month retention). AWS/ApiGateway Count for ApiId=w8jnzvs21g Stage=prod over the API's ENTIRE LIFETIME since creation 2026-01-06T20:33Z: 2026-01-05 83, 2026-01-07 105, 2026-01-08 25, 2026-01-11 44, 2026-04-26 15, and 2026-09-03 2. Those last two ARE MY OWN PROBE and are subtracted from every figure below. 4xx: 13, 0, 3, 8, 1, and 2 (mine). 5xx: 7, 0, 3, 0, 0, 0.",
      "SUCCESSFUL AUTHENTICATION IS ESTABLISHED, and the cleanest single day carries it: on 2026-01-07 the API served 105 requests with ZERO 4xx AND ZERO 5xx, while AWS/Lambda Invocations for trade-authorizer records 18 invocations that same day. AN AUTHORIZER DENY SURFACES AS A 401 OR 403, WHICH IS A 4xx. There were none. So all 18 authorizer evaluations that day returned ALLOW. This is an inference from two independent metrics rather than a log read, because the logs that would have said so directly are expired -- and it is stated as an inference.",
      "LIFETIME TOTALS EXCLUDING MY PROBE: 272 API requests, of which 25 were 4xx and 10 were 5xx, leaving roughly 237 non-error responses. trade-authorizer 55 invocations (13+18+6+12 in January, 6 on 2026-04-26). trade-auth-handler 28 invocations (14+1+10+2 in January, 1 on 2026-04-26) -- so the MINT path was exercised too, not only the authorizer. My own contribution tonight is 3 authorizer invocations and 2 mint-handler invocations, the latter from the S9C before/after control probes.",
      "THE SHAPE: concentrated build-and-test traffic 2026-01-05 to 2026-01-11, one small burst on 2026-04-26, then nothing until my probe. That is consistent with a feature built, briefly exercised, revisited once, and left wired.",
      "Vintages: all live reads 2026-09-04T05:4x-05:5xZ."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THE ANSWER THE ROUTING NEEDS, stated as the two halves it actually has. FINDING, NOT A DEMONSTRATED INCIDENT: nothing observed suggests misuse, the traffic shape is a developer's, and the only authorizer activity inside the readable 14-day window is mine tonight. BUT IT IS ALSO NOT A DEMONSTRATED NON-INCIDENT, and that distinction is the whole point: 'no evidence of abuse' here is UNCOMPUTABLE beyond 14 days rather than negative. THREE INSTRUMENTS WERE ASKED FOR THEIR REACH BEFORE THEIR RESULT AND TWO FAILED THE REACH TEST -- access logging never enabled, authorizer events expired -- which is the same shape as the CloudTrail data-events leg on TO-OP-S-9C, now the THIRD time tonight that a silent instrument would have read as an all-clear. WHAT WOULD CHANGE THE ANSWER, offered for the L4 decision and not acted on: enabling access logging on the prod stage and raising the authorizer log group's retention would make this question answerable GOING FORWARD, but neither is retroactive and neither is this lane's to do. WHAT THIS ROW DOES NOT CLAIM: it does not claim the secret leaked, that any allow was illegitimate, or that the January traffic was anything other than the team building the feature. It claims the path works, has worked, and cannot be audited backwards.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S142",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Z-S140 MEASURED WHO CAN READ THE LAMBDA CONFIG. THE SAME SECRET IS ALSO IN TERRAFORM STATE, WHERE A DIFFERENT PRINCIPAL SET REACHES IT WITH NO LAMBDA PERMISSION AT ALL. JWT_SECRET is assigned at trade-pipeline/lambdas.tf:59 and :90 as a VAR REFERENCE -- so it is NOT a literal in the repo and there is no git-history exposure, which is the good half and worth stating first. But terraform writes RESOLVED variable values into state in plaintext, and this root's state is remote at s3://opal-313476888478-terraform-state, so the reachable set is 'principals with s3:GetObject on that bucket' UNION the 14 measured, and the first half is unmeasured. IT IS BOUNDED, NOT OPEN: that bucket returns BlockPublicAcls, IgnorePublicAcls, BlockPublicPolicy and RestrictPublicBuckets ALL TRUE with SSE-AES256, so this is authenticated-internal reach rather than public. ANY REMEDIATION SIZED ON 14 IS SIZED ON ONE PATH OF TWO.",
    "evidence": [
      "NO SECRET VALUE WAS READ, STORED OR ECHOED AT ANY POINT, and the method is stated so the claim is checkable: the two assignments were CLASSIFIED by testing their right-hand side against a set of prefixes (var. / data. / local. / a quoted literal), printing only the classification and the rhs LENGTH. The file was never displayed and no value entered any output, message or row.",
      "THE ASSIGNMENT SHAPE, which settles the worst branch in the good direction: infra/aws/terraform/trade-pipeline/lambdas.tf:59 and :90 both classify as VAR-REFERENCE. A quoted literal would have put the signing secret in git history, unrotatable by any AWS action and readable by everyone with repo access. It is not that.",
      "THE SECOND PATH, and it follows from how terraform works rather than from a defect: terraform records RESOLVED values in state, so a var-supplied environment variable is stored in plaintext in the state file regardless of how the variable is supplied. This root's backend is S3 -- bucket opal-313476888478-terraform-state, read from the root's own .terraform/terraform.tfstate backend record. Reading that object requires s3:GetObject on that bucket and requires NO lambda:GetFunctionConfiguration.",
      "THE BOUND, measured rather than assumed, because an unbounded reading of this would be the overstatement: get-public-access-block on that bucket returns all four flags TRUE (BlockPublicAcls, IgnorePublicAcls, BlockPublicPolicy, RestrictPublicBuckets) and get-bucket-encryption returns SSE-AES256. So the second path is reachable by authenticated principals with state access, NOT by the internet.",
      "WHAT IS NOT MEASURED AND IS NOT CLAIMED: how many principals hold s3:GetObject on that bucket, and whether they overlap the 14. That is the same simulate-principal-policy instrument Z-S140 and Z-S125 already used, pointed at a different resource, and it is the assignee's to run rather than this seat's. The claim here is only that the set is DIFFERENT and currently unknown -- not that it is larger."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS THE SEVENTH INSTANCE OF THE Z-S122 SHAPE and why that matters here rather than as a curiosity: a count scoped to one MECHANISM while the value is reachable by another. Z-S136 was the sharpest previous case -- terraform as a second WRITER that no principal census could see because it needs no fourth principal. This is its mirror: terraform as a second READ PATH, invisible for the same structural reason. A seat that has just run a 231-principal simulation has every reason to believe the question is answered, which is exactly when the second path goes unasked. THE GOOD HALF LEADS FOR A REASON: the var-reference finding rules out the worst branch available -- a signing secret in git history cannot be rotated by any AWS action and is readable by everyone who has ever cloned the repo. Establishing that it is NOT that is worth more than the second path costs. AND THE REMEDIATION LIKELY CLOSES BOTH AT ONCE: moving the value out of a plaintext environment variable into a secret store referenced at runtime removes it from the Lambda config AND from state in one act, so this row probably adds no work -- it adds a CRITERION, because a remediation verified only against the Lambda-config path would pass while state still carried the value. NOTHING HERE RE-GRADES Z-S140, which is measured, correct and the more serious row; its forgeable-and-reachable finding stands untouched and unqualified.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S143",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THE CANONICAL NODEJS LAMBDA BUILD SILENTLY CORRUPTS THE ESTATE'S OWN SOURCE-OF-TRUTH MANIFEST, ON EVERY BUILD, AND THE GATE THAT WOULD CATCH IT IS ARMED ON THE WRONG SURFACE. build-nodejs-lambda.sh:428 rewrites lambda-source-map.json through bun, and the rewrite converts escaped Unicode into literal bytes. MEASURED at HEAD versus worktree: HEAD holds 0 non-ASCII characters and 18 escaped \\u00XX sequences; the worktree holds 9 DISTINCT non-ASCII characters and 0 escaped sequences. So 18 escapes became mojibake across entries nobody in this project touched. CLAUDE.md says no non-ASCII in production code and the commit gate ENFORCES it -- on commit MESSAGES only. This seat's own commit was refused tonight for ONE non-ASCII character in a message, while this file can carry NINE in its CONTENT and sail through.",
    "evidence": [
      "THE MECHANISM, as reported by 0.7.0_AE_CloudOps~W: build-nodejs-lambda.sh:428 writes the updated artifact_sha256 back into lambda-source-map.json via bun, and that rewrite RE-ENCODES the whole file rather than patching one value. Entries that stored escaped Unicode now hold the decoded bytes.",
      "MEASURED INDEPENDENTLY AT THIS SEAT, HEAD versus WORKTREE, on the same file: HEAD is 166,775 characters with ZERO non-ASCII characters and 18 occurrences of the escape sequence backslash-u-0-0. The WORKTREE, after 0.7.0_AE_CloudOps~W's build, is 167,597 characters with 0 escape sequences and NINE distinct non-ASCII characters: 0x9d, 0xa2, 0xa7, 0xac, 0xc3, 0xe2, 0x2014, 0x201a, 0x20ac. Set difference confirms every one of those is absent from HEAD, so the build introduced all of them.",
      "THE SHAPE IS CLASSIC UTF-8-READ-AS-CP1252 MOJIBAKE: the presence of 0xc3 and 0xe2 alongside 0x201a and 0x20ac is the signature of multi-byte UTF-8 sequences decoded one byte at a time. It is not a stray character someone typed; it is a round-trip through the wrong codec.",
      "THE DIFF IS NOT SCOPED TO THE INTENDED CHANGE: 18 insertions and 13 deletions on a file whose intentional edit was one artifact_sha256 value and one corrected entry. The remainder is encoding churn on entries unrelated to this project.",
      "THE GATE EXISTS AND IS AIMED ELSEWHERE, and this seat has FIRST-HAND evidence of both halves from tonight. safe-commit REFUSED a commit of this seat's at roughly 05:0xZ for a single non-ASCII character in the commit MESSAGE, printing the estate's ASCII substitutes and the note that a U+2B50 in a message crashed the deploy gate on 2026-09-01. That same session then measured NINE distinct non-ASCII characters sitting in the CONTENT of a tracked, load-bearing file with nothing objecting.",
      "AND IT RECURS BY CONSTRUCTION: the rewrite is not conditional. Every build of every nodejs Lambda through the canonical path performs it, so the corruption re-lands each time the file is regenerated, whoever runs it."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS FILED BY A SEAT THAT IS NOT FIXING IT. 0.7.0_AE_CloudOps~W found it, called it worth knowing beyond tonight, and correctly declined to fix a CI-lane script from inside a face scoped elsewhere. But it left the finding in a BROKER MESSAGE, and a message is the one carrier that reaches nobody once the sessions end -- not a commit, not a deliverable, not a row. A census of all 141 rows in this channel returned ZERO hits for mojibake, non-ASCII, re-encode, encoding churn or build-nodejs-lambda, so there was no existing carrier and this is not a duplicate. This seat checked before filing precisely because it advised 0.7.0_AE_CloudOps~W against duplicating Z-S110 an hour earlier, and the same discipline binds in this direction. WHY IT IS ARMED RATHER THAN INERT, since nothing is broken today. The file still parses as JSON and every consumer reads it correctly, so there is no live failure -- but the estate has a recorded incident of a non-ASCII character CRASHING the deploy gate (2026-09-01, U+2B50, cp1252 decode failure, which blocked every deploy-scope push until repaired). This file is read by build scripts, by record-terraform-deploy.sh, by drift checks and by the staleness census. A cp1252-reading consumer meeting 0xc3 in this manifest is the same failure with a wider blast radius, and the corruption is now committed-adjacent rather than hypothetical. ARMED means the hazard is live and undischarged, not that it is currently firing. THE SHARP PART, and the reason this is worth more than a tidy-up ticket: THE CONTROL IS REAL, ENFORCED, AND POINTED AT THE WRONG SURFACE. An agent cannot get one decorative character into a commit MESSAGE -- measured at this seat tonight, the commit was refused outright. A build script can put nine into the CONTENT of the file that Rule 4 designates as the pairing authority, unattended, on every run. The rule is not unenforced; it is enforced somewhere the violation does not occur. That is a harder defect to see than an absent gate, because every audit of 'is the ASCII rule enforced?' answers YES. A NON-APPLICATION, MEASURED RATHER THAN ASSERTED because this row would otherwise overstate its own severity: walking the whole parsed document, EXACTLY 8 string fields carry a non-ASCII character, and every one of them is prose -- 6 are _build_note and 2 are _note. ZERO functional fields carry one: source_dir, files, artifact_sha256, tf_file, tf_resource, artifact_s3_key, runtime, build_type, handler, iam_role, last_deployed_commit and pipeline are all clean across all 204 entries. The manifest's PAIRING data is intact. What is corrupted is its prose, which is also what a human reads first when deciding whether an entry can be trusted.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S145",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THE FIXTURE AND THE OBSERVATION OF THAT FIXTURE SHARE A PRIMARY KEY, AND THE TABLE CANNOT HOLD BOTH FACTS. `address` is the partition key of opal-suspicious-addresses. S19-AC2 requires a REAL edge refusal, and the only address this device can originate from is its own egress -- so the exercise MUST write 108.242.96.89/32. The sentinel, working exactly as specified, observes the resulting blocked requests and writes THE SAME KEY. Two lanes, two legitimate and different facts, one item, last-writer-wins per attribute. NEITHER LANE ERRED IN DESIGN and no amount of care by either prevents it.",
    "evidence": [
      "THE KEY IS THE ADDRESS, declared at infra/aws/terraform/opsec/dynamodb.tf: hash_key = \"address\", and the module's own comment states the normalization rule that makes it canonical -- IPv4 to /32, IPv6 to /64 -- precisely so that one host cannot occupy two keys. The same property that prevents duplicate rows for one host GUARANTEES a collision when two writers describe one host.",
      "THE EXERCISE HAS NO CHOICE OF ADDRESS. S19-AC2 requires an address BLOCKED, CONFIRMED REFUSED AT THE EDGE, lifted, and confirmed reachable again, with the refusal as the positive control. A refusal can only be produced from an address the device can actually originate from. 0.7.0_AE_CloudOps~T measured that to be 108.242.96.89, the shared egress, and announced it in msg 20256 before acting. A synthetic address cannot produce a genuine edge refusal, so the fixture address is FORCED.",
      "THE SENTINEL HAS NO CHOICE EITHER, AND IS CORRECT TO WRITE. Its subscription filter's first limb is action = BLOCK. The exercise's refusals ARE action=BLOCK records on aws-waf-logs-opal-cloudfront, so opal-sentinel parses them, counts them, runs the C-4 ALLOW check and writes a WATCH row keyed on the same normalized address. Suppressing that would mean the sentinel ignoring real blocked traffic, which is the opposite of OP-s-14.",
      "MEASURED, THE COLLISION IS REAL AND NOT THEORETICAL: at 05:58:25Z the row read WATCH hits 2 with rules {BlockedIPs} and case_ids {4f08be67dc53} -- the sentinel's observation. Minutes later the same key read BLOCKED hits 1 with notes 'TO-OP-S-15-19 S19-AC2 fixture' -- the re-run's fixture. One item, two writers, the fields of each visible only until the other wrote.",
      "AND THE COLLISION IS SPECIFIC TO THIS ADDRESS, WHICH IS WHY IT HAS NOT BITTEN BEFORE: every other fixture in this project used RFC 5737 documentation ranges (203.0.113.x, 2001:db8::) which the sentinel never observes because nothing routes from them. The device's own egress is the ONE address that is simultaneously the only usable fixture for an edge-refusal test and a real source of observable traffic.",
      "THE DEMONSTRATION, RECORDED SO THE FINDING IS NOT MISTAKEN FOR THE INCIDENT: this seat overwrote the notes field of that row mid-exercise at 06:0xZ, believing it to be the sentinel's observation, having identified it from a scan taken minutes earlier. Restored byte-identical within about a minute; only notes was ever in the UpdateExpression. Disclosed in msg 20284 and accepted in msg 20287. THE STALE READ WAS THIS SEAT'S ERROR. That a stale read of THIS row was fatal where it would have been harmless on any other is the structural property this row is about."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS ARMED RATHER THAN A CURIOSITY, and it is a data-integrity concern rather than a security one: OP-s-23's threshold distribution reads this table over a MONTH-LONG window that began 2026-09-04T02:44:34Z, and S23-AC2 requires ordinary and anomalous traffic to be SEPARATED. A self-inflicted exercise block is anomalous by construction. If the exercise's marker and the sentinel's observation overwrite each other, the row that survives may carry no indication of its cause at all -- and 0.7.0_AE_CloudOps~U's msg 20268 makes the timing point sharply: the contamination is BANKED NOW and read THIRTY DAYS LATER, across a session boundary, by seats that will not have been present. A broker message does not survive that. Only something on the row does. THE REMEDY SPACE, NAMED AND DELIBERATELY NOT CHOSEN per msg 20287: (a) A FIXTURE MARKER ATTRIBUTE -- a dedicated field, written by every exercise, that no detector overwrites and every consumer filters on; cheapest, but it is a convention and conventions are unenforced. (b) A RESERVED FIXTURE ADDRESS RANGE -- but note this does NOT work for S19-AC2 specifically, which is the whole difficulty: a documentation address cannot produce a real edge refusal, so this option solves every case EXCEPT the one that produced the finding. (c) AN EXERCISE PATH THE SENTINEL IGNORES -- e.g. a fixture flag the subscription filter or the handler excludes; strongest isolation, but it means the exercise no longer traverses the production path, which weakens exactly the end-to-end property S19-AC2 exists to prove. (d) WRITER ATTRIBUTION ON THE ROW -- a sources or written_by field, which the PRD's schema already gestures at with `sources` (SS, 'which detectors reported it') and `blocked_by`; this is the only option that makes the two facts COEXIST rather than choosing between them, and it is a schema change on a COMPLETE cell. EACH OPTION TRADES SOMETHING REAL AND THAT IS WHY THE CHOICE IS NOT AN ASSIGNEE'S. THE REUSABLE PART: a shared keyed store makes 'what is true of X' expressible and 'who says so, and why' inexpressible -- and every multi-writer design eventually needs the second. The tell is not a conflict; it is that TWO CORRECT WRITERS PRODUCE ONE ROW and nobody notices until a third party reads it and cannot tell which fact they are holding.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S146",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "THIS SEAT DESTROYED THE SENTINEL'S WATCH ROW ON 108.242.96.89/32 -- TWICE, AND THE FIRST ACT WAS SILENT -- WHILE RUNNING THE EXERCISE THE ROW WAS OBSERVING. The address is the PARTITION KEY, so the fixture and the observation were ONE ROW, not two objects sharing a name; put_item REPLACES the whole item with no error, no warning and no diff. THE OBSERVATION ITSELF SURVIVES: case 4f08be67dc53 is intact in the evidence store with both WAF samples, so only the ROW POINTER was lost. AND THE CRITERION MANDATES THIS: S19-AC2 requires a real edge refusal, the only address this device can originate from is its own egress, and the sentinel necessarily observes that address -- so the exercise necessarily destroys the observation of itself.",
    "evidence": [
      "THE TIMELINE, RECONSTRUCTED TO THE SECOND. 05:58:25Z the sentinel writes a WATCH row on 108.242.96.89/32 -- hits 2, rules {BlockedIPs}, paths_top {/}, case_ids {4f08be67dc53} -- its own independent observation of the block this seat had just placed. ~06:00Z this seat sends msg 20274 stating it has NOT touched that row and will leave it as the other lane's evidence; TRUE WHEN WRITTEN. 06:02:55Z this seat's S19 RE-RUN calls put_item on the same address; the WATCH row is REPLACED by a BLOCKED fixture at that instant. ~06:03:5xZ the exercise's own `finally` deletes that row as fixture cleanup. 06:04:xxZ a second cleanup pass deletes the already-absent key, a no-op. Row now ABSENT: get-item returns nothing and the table scans 10 rows without it.",
      "THE FIRST ACT WAS SILENT AND THAT IS THE PART A FUTURE READER NEEDS: put_item REPLACES THE WHOLE ITEM. It is not a merge and not an upsert of named fields -- hits, rules, paths_top, case_ids and first_seen were all overwritten in one call that returned success. There is no error, no warning, no diff and no audit line. A seat reporting only the visible delete would have told the truth and hidden the mechanism.",
      "THE MECHANISM: THE ADDRESS IS THE PARTITION KEY. The fixture and the sentinel's observation were never two objects that happened to share a name -- THEY WERE ONE ROW. A cleanup scoped to 'only my own fixture' CANNOT BE SCOPED AT ALL when the key is shared, because there is no such thing as 'my' item at a key another writer also uses. Same shape as the shared channel file and the shared terraform root, arriving on a third substrate: two writers, one key, second write not additive.",
      "THE OBSERVATION SURVIVES AND ONLY THE INDEX ENTRY WAS LOST, established by 0.7.0_AE_CloudOps~W (msg 20296) rather than by this seat: s3://opal-security-evidence/cases/2026/09/04/108.242.96.89_32/4f08be67dc53/ holds summary.json, timeline.md and TWO waf-sample files timestamped 05:58:25Z and 05:58:27Z -- matching the destroyed row's first_seen and last_seen exactly, and its hits=2 matching the two sample files. put_item on a DynamoDB partition key cannot reach an S3 object, so the evidence was never in the blast radius.",
      "THIS SEAT'S OWN ABSENCE READ WAS WRONG AND IT DECLINED TO ACT ON IT, which is the only reason the record is not worse. list-objects-v2 on opal-data-security prefix cases/ returned ZERO, and this seat refused to read that as destruction -- stating that a zero over an entire prefix is far more likely a wrong bucket than a mass deletion, and that it held no positive control proving the probe could see a case file that exists. IT WAS THE WRONG BUCKET: opal-data-security was the evidence store through PRD v0.8 and is now the LOG DESTINATION (S28/C-16); the evidence store is opal-security-evidence (C-8, v0.9). Had that zero been reported as 'the case file is destroyed', this row would now be recording a loss that never happened.",
      "AND THE CRITERION MANDATES THE COLLISION, which is why this is filed as a design finding rather than a discipline lapse. 2.0.0_SA_COO~Z states it in msg 20295: S19-AC2 requires a REAL edge refusal; the only address this device can originate from is its own egress; the sentinel necessarily observes that address. The exercise therefore necessarily destroys the observation of itself, and no amount of care by either seat avoids it. TWO LANES DESTROYED THIS SAME ROW WITHIN MINUTES TONIGHT, FROM OPPOSITE DIRECTIONS, AND BOTH DISCLOSED IMMEDIATELY -- that is a design problem, not a discipline problem.",
      "THE RULING PROTECTING IT WAS ALREADY VOID WHEN ISSUED, recorded because it is the same perishability this project keeps paying for: 2.0.0_SA_COO~Z ruled at 06:04Z to LEAVE the WATCH row and called it the strongest evidence in the chain. It had been destroyed at 06:02:55Z, ninety seconds earlier. The ruling was composed from a report that was true when written and false when read, and the issuer said so itself."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THIS ROW IS ALSO THE EXERCISE-ORIGIN ANNOTATION 2.0.0_SA_COO~Z ASKED FOR, so a future reader finds one record rather than a gap plus a puzzle: CASE 4f08be67dc53 IS SELF-INFLICTED. It is this estate's own egress, blocked deliberately at 06:02:55Z by TO-OP-S-15-19's S19-AC2 exercise and lifted 22.5 seconds later via the audited CLI. It is NOT a real threat and nothing was attacking the estate. Annotate the record, never edit the observation -- the case file stays exactly as the sentinel wrote it and this channel carries the explanation. WHAT THIS SEAT IS NOT DOING, AND WHY: it is NOT re-creating the row. A reconstructed observation carrying the sentinel's name, written by the seat that destroyed it, would read as first-hand and would not be -- it would be the second thing this project has had to correct about a record that looks more authoritative than its provenance. If 0.7.0_AE_CloudOps~S wants it re-minted that is that lane's act under its own attribution, and the field values read before destruction are in msg 20291. It is also NOT re-running the exercise to recreate the row, per msg 20295: recreating destroyed evidence by re-running the act that destroyed it is not restoration, and it would collide again. THE DURABLE RULE, which 2.0.0_SA_COO~Z is carrying into S19-AC2 itself: NO EXERCISE MAY WRITE A PARTITION KEY THAT A LIVE SYSTEM ALSO WRITES, unless it captures the pre-existing item first and restores it, or the face declares that it will destroy observations. Capture-then-restore is the cheap form and this exercise should have done it. AND THE PART THIS SEAT WANTS ON ITS OWN RECORD: it had ALREADY relayed this exact class tonight -- 0.7.0_AE_CloudOps~S destroyed an uncommitted row on the shared channel file, this seat relayed that warning to two lanes that never received it and banked a memory about it -- and then committed the same class ninety minutes later. Knowing the class did not prevent it, because it was being watched for in FILES and this instance was in a TABLE KEY. A hazard learned on one substrate does not transfer to another by itself.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S147",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THE CANONICAL NODEJS BUILD FAILS FROM THE /cygdrive MOUNT AND BLAMES THE WRONG FILE. build-nodejs-lambda.sh's to_native_path matches only ^/([a-zA-Z])/, so it converts /c/... to C:/... and passes /cygdrive/c/... through UNCHANGED; bun is a native Windows binary and cannot read a /cygdrive path, so the map read returns empty and the script reports 'ERROR: No source_dir found for <fn> in lambda-source-map.json'. THE MESSAGE NAMES THE MAP AND THE FAULT IS THE PATH. Both mount forms are live on this device, so which one a caller's cwd happens to carry decides whether the estate's standard Lambda build works.",
    "evidence": [
      "THE FAILURE, REPRODUCED AND THEN RESOLVED BY CHANGING ONLY THE CWD -- which is what makes this a path defect rather than a map defect. Invoked with cwd under /cygdrive/c/...: rc=1, 'ERROR: No source_dir found for opal-session-analytics in lambda-source-map.json'. The IDENTICAL command with cwd under /c/...: rc=0, full build, bundle 69.37 KB, upload OK. One variable changed and it was not the map.",
      "THE MAP WAS PROVABLY FINE AT THE MOMENT OF THE FAILURE. Read directly with bun from a file-based probe rather than the script's inline -e: sm.functions['opal-session-analytics'].source_dir returned 'infra/aws/opalinvest_dev/lambda/session-analytics'. So the value the script says it cannot find was present and correct while the script said it was missing.",
      "THE MECHANISM AT SOURCE: build-nodejs-lambda.sh:81-87 defines to_native_path as `if [[ \"$1\" =~ ^/([a-zA-Z])/ ]]; then echo \"${BASH_REMATCH[1]}:/${1:3}\"; else echo \"$1\"; fi`. The regex requires a SINGLE letter between the leading slashes. '/cygdrive/c/...' does not match -- 'cygdrive' is not one letter -- so the else branch returns the path unchanged. :89 then hands that unconverted path to bun at :101-109, and bun's readFileSync throws on it because a native Windows binary cannot resolve a /cygdrive path. Empty stdout, so :112's `[ -z \"$SOURCE_DIR\" ]` fires and prints the map error.",
      "BOTH MOUNT FORMS ARE LIVE ON THIS DEVICE, which is why this is a coin-flip rather than a constant failure: `test -d /cygdrive/c` succeeds AND `pwd` from the workspace can report /c/... . CLAUDE.md's own watcher guidance names exactly this pair -- 'both may be mounted; they are NOT equally durable' -- and instructs resolving the prefix rather than assuming either. This script resolves one form and silently declines the other.",
      "SCOPE, MEASURED RATHER THAN ASSUMED: to_native_path is used at :89 (the source map), :118 (the source dir), :242 (package.json) and :267 (the entrypoint). So the defect is not confined to the map read -- every path the script hands to a native Windows tool is affected. The map read is simply the FIRST one, which is why it is the one that surfaces.",
      "NOT THE SAME DEFECT AS Z-S143, though it is the same script and they should not be read as duplicates: Z-S143 is the map REWRITE re-encoding Unicode escapes into literal mojibake, an output-side defect affecting file content. This is an input-side PATH RESOLUTION defect affecting whether the script runs at all. Different half of the script, different failure, different fix."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS ARMED RATHER THAN INERT DESPITE HAVING A ONE-WORD WORKAROUND: the workaround is only available to someone who already knows the diagnosis. The error message actively points away from it, and it points at a file that a seat doing this work has very likely JUST EDITED -- which is exactly what happened here. This seat had corrected the map entry minutes earlier, so 'No source_dir found' read as 'your correction did not take', and the obvious next act is to go re-edit a file that is already right. A seat without the site-Z mount context could spend a long time there. THE GENERALISABLE PART, and it is the third instance tonight: AN INSTRUMENT THAT ANSWERS CONFIDENTLY ABOUT THE WRONG OBJECT COSTS MORE THAN ONE THAT ANSWERS UNCERTAINLY ABOUT THE RIGHT ONE. The source map's '_note' said no repo source exists (Z-S110/Z-S134); AWS/Lambda Invocations returned a real-looking zero for a live function (Z-S124); and this reports a map error for a path fault. In all three the confident answer was the one that STOPPED further looking, and in all three it was caught only because someone disbelieved it for an unrelated reason. That pattern is doctrine rather than a project finding and 2.0.0_SA_COO~Z is better placed to decide where it belongs -- noted here rather than filed separately, per 0.7.0_AE_CloudOps~V's observation in Z-S143. FILED RATHER THAN LEFT IN A MESSAGE because that is the correction this seat accepted an hour ago: declining the FIX and declining the RECORD are different acts, and only the first was this seat's to make. The fix belongs to the CI lane; the record did not have an owner until now. NON-APPLICATION: a device or CI runner where only one mount form exists, and any caller whose cwd is already under /c/ -- for whom the script works and always has.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S148",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "SWEEP COMPLETE across ALL 23 proof instances and ALL 129 acceptance limbs, and the result is CLEAN in the category that matters: ZERO limbs are ACTUALLY-UNSUPPORTED. Three carry the STALE-BUT-SOUND shape -- a whole-population count offered for a face-scoped claim -- and every one of them already had a writer-scoped or before/after-pair anchor carrying the verdict, so no verdict anywhere in the project is disturbed. The estate had largely internalised this before the commission: at least five limbs name the exposure in their own text and one had the identical instrument corrected by the issuer days earlier.",
    "evidence": [
      "POPULATION AND DENOMINATORS, enumerated from the deliverables tree at HEAD 18103aeea0 rather than from recollection: 23 proof-of-spec instances exist across 8 lanes (~S 8, ~T 1, ~U 2, ~V 1, ~W 3, ~X 3, ~Z 5), carrying 129 acceptance limbs in total. INSTANCES EXAMINED 23 OF 23. LIMBS SCREENED 129 OF 129, programmatically, for co-occurrence of a face-scoped-negative marker and a global-reading marker. CANDIDATES RETURNED: 35. ALL 35 WERE THEN READ INDIVIDUALLY -- the screen is a filter and not a verdict, and roughly two thirds of its hits were innocent co-occurrence.",
      "THE TEST APPLIED: is a count, census or scan over an object OTHER seats also write being used to prove that THIS FACE did or did not do something -- and if so, does any WRITER-SCOPED instrument carry the verdict independently.",
      "RESULT IN THE CATEGORY THAT IS A DEFECT -- ACTUALLY-UNSUPPORTED, meaning the claim needed a writer-scoped instrument and never had one: ZERO of 129. Every face-scoped claim examined rests on at least one of: a LockToken, a terraform state-list, an enumerated changed-resource list from the face's own apply, a git diff or porcelain read, a diff-scoped census, a fixture write/read/delete on the data plane, a simulate-principal-policy per-ARN read, or a BEFORE/AFTER pair taken by the same seat across its own change window.",
      "RESULT IN THE STALE-BUT-SOUND CATEGORY -- the reading needs a vintage, the verdict holds: THREE. (1) S14-AC2, 0.7.0_AE_CloudOps~S: table-wide row census for 'rows written by THIS FACE'. SELF-REPORTED by that lane at msg-id 20273 before this sweep reached it; counted here, not re-filed. Verdict carried by the in-code gate -- SENTINEL_BLOCK_ARMED false plus three independent refusals behind it. (2) S20-AC5, this seat: TWO global limbs, an S16 table Count-0 and a CLOUDFRONT-scope IP-set census. AMENDED under the msg-20294 ruling by APPENDING vintage and shared-object status beside the minted text; verdict carried by the LockToken pair, which is writer-scoped and cannot be moved by another lane. Re-validated VALID rc=0, status unchanged PASS. (3) S9-AC4, 0.7.0_AE_CloudOps~X: 'Count 12, identical to the pre-change reading'. The weakest of the three claims but the best anchored -- it is a before/after PAIR by one seat, not a bare number. ROUTED TO THAT LANE FIRST as a suggestion, msg-id 20302.",
      "WHY S9-AC4 WAS RAISED DESPITE BEING SOUND, and the reason is specific rather than generic: opal-users is the ONE table in this project with a LIVE RETIREMENT DECISION PENDING -- row Z-S119 is ARMED with a human disarm owner and msg 20101 records the delete being put to Andrew as a card. Unlike most shared objects it has a named, expected, imminent writer, so its count would move at exactly the moment the project succeeds, and the limb would then read as failing.",
      "THE NEGATIVE RESULT IS THE LARGER HALF AND IT IS EVIDENCED, NOT ASSERTED. Five limbs name this exposure in their own text: S6-AC4 (0.7.0_AE_CloudOps~T) states 'HONEST LIMIT, STATED RATHER THAN PAPERED OVER: this seat did NOT take an account-wide dashboard count BEFORE the apply, so that number alone cannot prove the count did not change', then names the apply's enumerated changed-resource list as the discriminating evidence. S5-AC3 (0.7.0_AE_CloudOps~Z) reads BucketOwnerEnforced before the first apply and again after the last and says 'the pair is the control, not a single read'. S8B-AC2 (0.7.0_AE_CloudOps~W) states its enumeration is 'DERIVED FROM A LIVE READ, NOT FROM THE FACE'. S8B-AC5 quotes a clean baseline taken before the first edit and draws the conclusion explicitly -- 'nothing foreign was pending in this root and nothing else COULD ride' -- which is the control that closes the shared-ROOT version of this exposure. S16-AC3 (0.7.0_AE_CloudOps~S) scopes its census to THIS TO'S DIFF rather than to the world.",
      "AND ONE INSTANCE SHOWS THE ISSUER HAD ALREADY CORRECTED THE IDENTICAL INSTRUMENT BEFORE THIS COMMISSION EXISTED: S17-AC6's criterion carries the parenthetical 'Its instrument was also corrected: a delivered object whose LastModified is after the flip, NEVER an object COUNT, since the bucket receives continuously.' That is this exact class -- a count over a continuously-written shared object replaced by a vintage-anchored read of a single object -- caught and fixed days earlier on a different surface. S17R-AC3 then applies the corrected form, citing a LastModified strictly after the apply window rather than resting on its own 215-versus-172 object count."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THE COMMISSION'S PREMISE WAS THAT SIX INSTANCES HAD BEEN ACCEPTED TONIGHT WITHOUT CHECKING FOR THIS SHAPE. That is true of the checking, and the sweep still comes back clean -- which is worth stating precisely rather than as reassurance: the instances survive not because the shape is absent but because the seats writing them reached for writer-scoped instruments by habit. A LockToken, a changed-resource list, a git porcelain read and a data-plane fixture are all writer-scoped, and they were chosen as PRIMARY evidence with the global count offered as corroboration. THE ONE PLACE THAT HABIT SLIPPED IS INSTRUCTIVE AND IT IS THIS SEAT'S: S20-AC5 carried TWO global limbs, and the second was missed while writing a message to a peer about the first, in the same paragraph. APPLYING A FINDING ONCE DOES NOT DISCHARGE IT ACROSS THE ARTIFACT -- the sweep has to cover the whole instance, not the sentence that prompted it. WHAT THIS DOES NOT COVER, stated so the denominator is not read wider than it is: this sweep examined ACCEPTANCE limbs. It did not examine artifacts_produced, controls, declared_exclusions or compiler_tools entries, which can carry the same shape and were out of the commission's stated scope. Nor did it re-verify any verdict -- it asked only whether the EVIDENCE could support the claim, never whether the claim was true. A limb reported here as STALE-BUT-SOUND is a statement about instrument scope and not an endorsement of the finding it supports.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S150",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "ATTEMPTED-vs-PROVEN IS NOT A MISSING FIELD IN deploy_ledger.py -- IT IS A PREDICATE REPLICATED AT SEVEN SITES PLUS A RENDERER. A leg carries exactly six keys (id, kind, target, proof_required, proof, closed_at) and the set is CLOSED; 'open leg' is defined as `not [a-z]+\\.get\\(\"proof\"\\)` independently at :346 :355 :441 :467 :707 :758 :1081, and the markdown a human reads prints OPEN-vs-CLOSED off the same test at :211. So a leg NEVER ATTEMPTED and a leg ATTEMPTED-BUT-UNPROVEN are the same record in eight places, and an added attempted_at is EIGHT EDITS, not one -- any site left behind keeps the old two-state semantics while the new field reads populated, which is worse than not having the field.",
    "evidence": [
      "VINTAGE FIRST, since this thread made it a rule: .tools/deploy_ledger.py @79c0e68071, `git status --porcelain` EMPTY so disk bytes == HEAD bytes. 0.0.0_AB_MSTR~Z independently confirmed the blob at that pin is da78c8d9a9b16ea2fa49d284ff5988e13dbd8e71 and identical at its own HEAD, so BOTH SEATS MEASURED THE SAME BYTES and every line number here is comparable across both reports.",
      "THE SEVEN, anchored census, pattern published verbatim rather than named as a class: comp-read .tools/deploy_ledger.py --enumerate 'not [a-z]+\\.get\\(\"proof\"\\)' returns 7 hits / 1328 lines / 43 sections, banded CODE 7 / DOCSTRING 0 / COMMENT 0 / DEF 0. Run independently at BOTH seats with the same result.",
      "THE EIGHTH IS A DIFFERENT CLASS AND IS THE ONE THAT MATTERS MOST: :211 renders st = \"CLOSED \" + (leg.get(\"closed_at\") or \"\") if leg.get(\"proof\") else \"OPEN\". That is the markdown entry a human reads. A stamp that moves the seven predicates and NOT the renderer leaves the entry PRINTING OPEN for an attempted-unproven leg -- making the exact state the stamp exists to reveal invisible in the one artifact people actually read. Found by 0.0.0_AB_MSTR~Z, not by this seat.",
      "THE FIELD SET IS CLOSED, MEASURED NOT INFERRED: --enumerate 'leg\\[' returns 17 hits, CODE 17, of which only TWO are WRITES (:341 proof, :342 closed_at); the other 15 are reads. Three constructors agree on the same six keys -- _canonical_pipeline_legs :245-257, _lambda_leg :280-285, cmd_open :301-302 -- so nothing anywhere adds a key outside them. A read that found only ONE constructor would have produced the same six fields and the same confidence while being one disagreeing constructor away from wrong.",
      "THIS SEAT FIRST REPORTED FIVE, AND THE MISCOUNT IS RECORDED BECAUSE ITS MECHANISM IS THE TRANSFERABLE PART: the original probe was 'leg\\[', a BRACKET-ACCESS pattern, not a predicate pattern at all. The predicates appeared in five of its hits as INCIDENTAL CONTENT on lines that matched for another reason (leg[\"id\"], state[\"legs\"]); :441 and :758 bind lg, and :758 iterates a LOCAL legs, so neither was ever a candidate for that probe. The denominator certified the SWEEP for bracket-access and this seat attached it to a PREDICATE question -- CLAUDE.md Rule 22 verbatim, broken inside the same report that cited it. Corrected by 0.0.0_AB_MSTR~Z's independent anchored census at 19930."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): SCOPE, and this is the sentence 3.0.0_SA_CVO~Z MEASURED AS ABSENT from Z-S47 (the tokens 'fabric item', 'fabric', 'register' and 'would not close' appear ZERO times in its notes): THE INSTANCE IS THIS PROJECT'S r2b LEDGER AND BELONGS ON THIS CHANNEL, BUT THE CLASS IS A FABRIC ITEM ON THE DEPLOY-LEDGER CONTRACT AND CLOSING NFRA_OPSEC202609 WOULD NOT CLOSE IT. .tools/deploy_ledger.py is a general estate tool; every project that opens a ledger inherits all eight sites. Filed here rather than elsewhere on the pattern Z-S40 set on this same file -- the exercised evidence lives where the instances happened, with the class named as homed elsewhere. || WHY THIS ROW IS INERT AND FILED ANYWAY: nothing is at risk right now, no leg is mis-stated today, this seat proposes no remedy and holds no lane on that file. What it changes is the PRICE of a remedy already under discussion. || THE METHOD LESSON 3.0.0_SA_CVO~Z ASKED BE CARRIED INTO THE RECORD rather than left in a message: A POSITIVE CONTROL PROVES THE ENGINE AND THE FILE, IT NEVER PROVES THE PATTERN. This seat searched THIS VERY CHANNEL for the thread using 'deploy_ledger|attempted|write-ahead', got 1 incidental hit in 1969 lines, and concluded NO ROW EXISTED -- while Z-S47 sat at :1526 written in the row's own vocabulary. The control this seat ran, 'Z-S4[0-9]', returned 100 hits and PASSED, and vouched for nothing: it fired on ROW IDS while the failing probe's risk lived entirely in its SUBJECT TERMS, so it shared none of that risk. Two further tells sat unread in that same output -- the control matched only S40-S49 by construction so it could not see S50+, and the file read 1969 lines against 2017 at the peer's HEAD, a stale vintage on the very read used to claim an absence. Before writing THIS row the probe was re-run and controlled on subject terms that DO share its risk ('deploy_ledger|NEVER-2' -> 7 hits, Z-S47 located at :1526), which is what established that the eight-sites finding is genuinely ABSENT here rather than merely UNFOUND.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S151",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "FWD-4 IS GRADED COMPLETE AND CANNOT BE SATISFIED: both login-abuse alarms publish to an SNS topic WITH ZERO SUBSCRIBERS, so a burst of blocked sign-ins reaches NOBODY. TO-OP-S-6.login-abuse-alarm reads `complete`; the alarm side is entirely correct (alarms exist, ActionsEnabled true, the action ARN resolves) and the defect sits ONE HOP FURTHER, on the topic -- which is exactly why nothing surfaced it. This is APPLIED satisfied and EXERCISED failed, and FWD-4's DONE WHEN is EXERCISED.",
    "evidence": [
      "THE ALARM SIDE, live control plane 2026-09-09 ~15:4xZ: `aws cloudwatch describe-alarms` returns 51 alarms in the account (12 of them carry NO AlarmActions at all). TWO match login: `OPSEC-auth-login-rate-limit-blocked` and `OPSEC-auth-throttled`. BOTH read `ActionsEnabled: true` and BOTH carry `AlarmActions: ['arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts']`. Both currently `StateValue: OK`.",
      "THE TOPIC SIDE, the discriminator: `aws sns list-subscriptions-by-topic --topic-arn arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts` returns `Subscriptions: []` -- TOTAL 0, CONFIRMED 0, PENDING 0. Not a pending-confirmation case; there is no subscription of any kind.",
      "THE UNSCOPED POPULATION READ, run because a check scoped to the login alarms cannot see a defect in what the alarms SHARE. Denominator: 51 alarms -> 7 DISTINCT SNS targets. THREE of the seven have ZERO confirmed subscribers: `astn-wsjft-alerts` (0), `etfs-reports-alerts` (0), `opal-login-abuse-alerts` (0). The other four DO: `inf-otp-alert` (2: lambda, sms), `opal-critical-surface-alerts` (2: sms, sqs), `opal-infrastructure-alerts` (1: sms), `opal-partner-etl-ops-alerts` (2: sms, sqs). POSITIVE CONTROL: because 4 of 7 return confirmed subscribers through the identical call, the three zeros are a REAL ABSENCE and not a broken probe.",
      "INSTRUMENT TRAP HIT AND DISCLOSED, because the first version of this sweep produced a FALSE CLEAN and would have been quotable: an earlier run printed `ZERO-CONFIRMED-SUBSCRIBER ALARM TARGETS: 0 of 7` with EVERY per-topic count rendered BLANK. Cause: the ARN list was written by native Python in TEXT MODE, so every line carried a trailing CR; all seven `list-subscriptions-by-topic` calls failed `InvalidParameter` on the mangled ARN, and the shell test `[ \"$c\" = \"0\" ]` never fired against an empty string, so the loop reported a clean estate. A count that cannot be true is the tell -- seven blanks summing to a confident zero. Remedied with `tr -d '\\r'`, and the re-run carries the positive control the first run structurally could not."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHAT THIS ROW DOES NOT CLAIM, stated because the value here is the boundary. (1) It does NOT re-grade TO-OP-S-6. The grade is 3.0.0_SA_CVO~Z's at L9 and this seat owns L4; what this seat asserts is about the OUTCOME's satisfaction, not the face's criteria, and the two are different objects -- the criteria may well all be true. (2) It does NOT touch FWD-15. FWD-15 ('every automatic block sends Andrew one email with the case') is served by the SENTINEL's own SES send under C-6 (`SENTINEL_EMAIL_FROM` in `opsec/sentinel.tf`), a DIFFERENT mechanism on a different path, and this seat did NOT measure it. Reading this row as 'the security email is broken' would be exactly the over-wide restatement this project keeps catching. (3) It does NOT establish that the alarms have ever FIRED -- both read StateValue OK now, and an alarm's current state says nothing about its history; a never-fired alarm and a fired-into-the-void alarm are indistinguishable from this read. (4) `opal-infrastructure-alerts` shows ONE CONFIRMED SMS subscriber, and CONFIRMED IS NOT DELIVERING: SMS sandbox status is a separate property this seat did not read, so that target is NOT reported here as healthy. || WHY IT IS ARMED RATHER THAN INERT: the exposure is live right now. The site and portal are under measured sustained credential pressure (TO-OP-S-13's own derivation: 105,217 requests to wp-login.php and 87,819 failed login POSTs over 2026-07-30..09-04), and the control that is supposed to tell a human about the portal half currently tells nobody. || WHY THE DISARM OWNER IS 2.0.0_SA_COO~Z: the remedy is a cell, not an edit. Subscribing a confirmed endpoint is inside FWD-4's own ratified intent so it needs no new sovereign word, but it is an AE-lane act on a live notification path and it belongs in an issued face with its own EXERCISED evidence -- an actual delivered message to a named human, which is the only thing that moves FWD-4 from APPLIED to EXERCISED. This seat holds no L6 limb and cuts nothing. || BEARING ON THE INFRASTRUCTURE REPORT, which is why it is filed today rather than banked: ADDENDUM 01 s.5.2 already names the sharpest report dependency as a STATE distinction -- making each property's state DECLARABLE rather than merely producing data. This is a second instance of the same class on the Dashboard property: a security row sourced from 'the login-abuse alarm exists and is enabled' would render OK while paging nobody. The report must read the DELIVERY leg, never the alarm's own configuration.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S152",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THE DECOMPOSITION'S OWN HOLD LIST STILL DIRECTS A FUTURE ACTOR TO BUILD AN EDGE THAT C-19 HAS MADE UNBUILDABLE. Decomp s.9 item 2 reads 'OP-x-2 (the website edge) -- CLOSED by his word ~08:4xZ (PRD v0.8): (a) CloudFront + WAF managed rules; OP-s-13's task order is cut at the round-2 re-entry after OP-s-4 / OP-s-5 / OP-s-18.' PRD v0.14's C-19 (NO-GODADDY) makes that edge UNBUILDABLE, not deferred. The decomposition is FROZEN mid-round so this is a ROW and not an edit.",
    "evidence": [
      "SPEC SIDE, read at HEAD 9263dd2d8b: decompositions/NFRA_OPSEC202609_DECOMP.md s.9 item 2, quoted verbatim in one_line. The same section's item 4 and the s.5 round table both re-state the round-2 re-entry for OP-s-13.",
      "WORLD SIDE, relayed from 1.0.0_SA_CTO~Z msg 20539 and the PRD v0.14 commit body @5f4d4b894f, MEASURED BY THAT SEAT 2026-09-09 ~16:0xZ and NOT re-measured here: opalinvest.com AND www both resolve to the EC2 elastic IP 18.208.18.213; headers read server: LiteSpeed with NO CloudFront marker; the only distribution in the account fronts the PORTAL. AWS WAF cannot attach to a bare EC2. Both candidate edges need the record repointed at GoDaddy and Route53 does not help because moving the zone changes the NAMESERVERS at GoDaddy.",
      "THE NEIGHBOURING-QUESTION TRAP, named on C-19 and repeated here because it is what makes the stale text dangerous rather than merely wrong: Andrew's 'Agreed, CloudFront' (~14:5xZ) settled the VEHICLE and never the ROUTE. 1.0.0_SA_CTO~Z told Andrew TO-OP-S-13 was 'unblocked' on that reading and corrected itself in the same turn as the v0.14 commit.",
      "THIS SEAT'S OWN ACT, same turn: TO-OP-S-13 closed complete @89b4f89afd (merged 9263dd2d8b) on its VALID instance @c12e340ceb, with C-19 written onto the face. So the FACE is safe to read; the DECOMPOSITION is the surface that still misdirects."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS FILED RATHER THAN FIXED: Rule 27 freezes the decomposition mid-round and /dispatch step 0 refuses an issuance at dep_stage EXECUTING; the only off-spec act available is this row. || WHY IT IS ARMED RATHER THAN INERT, and this is the whole point of the row: the stale text is a PROCEDURE, not a state. A stale STATE misleads a grader; a stale PROCEDURE RECRUITS THE NEXT ACTOR INTO A FORBIDDEN PATH (evidence rule 4, this project, round 1). The next actor is specifically foreseeable: PRD v0.14 directs that FWD-19 be cut at L5 'as a second act mirroring manifest row S13', so the COO doing that recut is sent to row S13 and s.9 item 2 is what it will read there. || DISARM: the disarm act is an edit to decomp s.9 item 2 at the RECUT, once this round closes and the decomposition unfreezes; it is not available before then, so the row stays ARMED rather than being closed early with a promise. disarm_owner is this seat because this seat owns the recut. || NOT WIDENED: this row says nothing about whether the marketing site should get a control by some other route. FWD-19's on-box, no-GoDaddy half is IN SCOPE under C-19 and is untouched here.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S153",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "TO-OP-S-12's OPERATIVE HALF IS GONE FROM THE LIVE BOX. It deployed 2026-09-04 ~05:20Z and its ledger closed 5/5; a LATER deploy the same day replaced /opt/opal-gateway/app at 10:10Z with the bytes of commit 4c3999de4a, which predates it, and the service restarted onto them at 12:52:29Z. The capability-token endpoints, the dual-accept and the FWD-12 observation instrument are ABSENT from the running code. INDEPENDENTLY, /otp/token and /ms/token appear in NO ALB listener rule, so even once redeployed they answer a Microsoft OIDC 302 to every machine caller. The observation window has therefore recorded NOTHING for five days and could not have.",
    "evidence": [
      "ON-BOX, measured on the RUNNING process rather than an assumed path (SSM, i-07dccb1615503ac99, 2026-09-09 ~18:4xZ): exactly one gateway dir exists (/opt/opal-gateway); the unit's ExecStart runs app.server:app from it; the live process pid 552785 has cwd=/opt/opal-gateway and lstart 'Fri Sep 4 12:52:29 2026'. So the bytes measured ARE the bytes served -- the grain question is closed before any claim is made.",
      "THE BYTES, resolved to a COMMIT BY CONTENT and never by filename (CLAUDE.md 22a): on-box server.py md5 56cdab4f54595eca69680c25608b6d0f and oauth_as.py md5 405b2d58447997d8e61311677bd49f4c. Walking every commit since 09-01 that touched those two files and hashing `git show <c>:<path>` gives an EXACT double match at 4c3999de4a (09-04 04:43Z, 0.9.0_WK_NFRA_CLDGRPH~2). The S12 operative half is 64577c3cc6 (server f3341ba9 / oauth b4916419) and the pre-S12 baseline oauth was 405b2d58 -- so oauth_as.py on the box is the PRE-S12 byte-for-byte.",
      "SYMBOL PRESENCE ON THE BOX, the direct read: grep -c log_credential over /opt/opal-gateway/app/{audit,otp,ms_ingest}.py returns 0,0,0 and grep -c 'otp/token' over server.py returns 0. The .env carries 21 keys and OTP_BEARER_LABELS -- which the S12 deploy added and whose presence its own ledger leg L3 recorded -- is NOT among them. Three independent surfaces agree the operative half is absent.",
      "THE AUDIT-LAKE CENSUS, the observation window's own instrument, run over the FULL object set rather than a sample: 11,893 objects listed across the six day-partitions dt=2026-09-04..2026-09-09 of s3://opal-mcp-audit/audit/ (per-day 6068/1297/1286/1058/1081/1103), all 11,893 fetched, 0 fetch-or-parse errors. 1,395 carry event=gw_cred_observe. EARLIEST 2026-09-04T05:20:14Z, LATEST 2026-09-04T12:52:29.096470Z. NOT ONE observation record exists after that instant, across five subsequent days in which the lake kept receiving ~1,100 other records per day -- so the silence is the instrument's absence, not the lake's.",
      "THE CAUSAL LINK IS AN EXACT TIMESTAMP IDENTITY, and it is what makes this a mechanism rather than a correlation: the last gw_cred_observe record (12:52:29.096470Z) and the systemd ActiveEnterTimestamp of the currently-running process (Fri 2026-09-04 12:52:29 UTC) are the SAME SECOND. The instrument did not go quiet; it was removed by the restart that produced that record's own successor process.",
      "THE EDGE, an INDEPENDENT second defect measured on the wire and then on the control plane: POST https://mcp.opalinvest.dev/otp/token returns 302 with `Server: awselb/2.0` and a Location to login.microsoftonline.com; POST /otp/fetch on the same host returns 401 with `server: uvicorn` and `www-authenticate: Bearer`. The Server header is the discriminator -- one is terminated by the ALB, the other reaches the app. describe-rules on the 443 listener confirms it: the OIDC-bypass rules enumerate exact paths only (P10 /mcp/*,/mcp,/authorize,/register,/token; P20 discovery; P30 /otp/fetch,/otp/health; P31 five /ms/* paths; P32 /graph/*), the default action is forward+authenticate-oidc, and /otp/token and /ms/token appear in NO rule. alb.tf:271 and ms-ingest.tf carry the same exact-path lists in source.",
      "THE REPO IS NOT THE VICTIM -- checked in BOTH directions. At the current shared-tree HEAD 3054872f2b the operative half is COMPLETE: server.py carries /otp/token (3), /ms/token (2) and all five log_credential call sites, oauth_as.py carries issue_capability (1), audit.py carries the definition (1), deploy-to-ec2.sh carries OTP_BEARER_LABELS (1). The other lane's work is ALSO intact at that HEAD (graph_read.py and integrations/globgrph/ both present), so restoring S12 by deploying HEAD is strictly FORWARD for every lane and rewinds nobody: the range 4c3999de4a..HEAD contains exactly 3 gateway-touching commits -- 64577c3cc6 (this seat, S12), 03b1cb0f7d (NFRA_CLDGRPH, ENABLED_INTEGRATIONS gains globgrph) and e3a9d207dc (MSTR integrate).",
      "A CORRECTION THIS SEAT MADE ON ITSELF, recorded because the near-miss is the transferable part: the first symbol read checked log_credential in otp.py and ms_ingest.py at HEAD, got 0 and 0, and was one sentence away from filing 'the call sites were lost in a merge'. An UNSCOPED comp-find over the whole gateway tree (denominator 6 hits / 76 files) put all five call sites in server.py:475,517,538,562,626. The scoped read was measuring the wrong file and would have reported a repo defect that does not exist. The zeros were real; the conclusion would have been false."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS A ROW AND NOT A MESSAGE: the GO (msg 20547) states that the worker's first act is to re-ground the face's premises against live state and that a delta is a surprise ROW, never a message. This is that delta, filed in the channel the GO names. || WHY DISARM_OWNER IS THIS SEAT AND THE HAZARD IS EXPECTED TO DISARM THIS SESSION: the remedy is entirely inside TO-OP-S-12's own lane and deliverable 3 -- redeploy the gateway from HEAD (restoring the operative half plus two other lanes' commits, strictly forward) and add /otp/token and /ms/token to the two existing exact-path OIDC-bypass rules in infra/aws/terraform/opal-gateway/{alb.tf,ms-ingest.tf}. Neither act retires anything: dual-accept means the five callers stay on their static bearers throughout, so no caller can break in either direction. || WHAT THIS ROW DOES NOT CLAIM. (1) It does NOT adjudicate who deployed at 10:10Z or why, and it names commit 4c3999de4a as the CONTENT the box matches, not as an accusation -- that commit's own message says 'nothing applied, nothing deployed', so the deploy act and the commit are separate objects and this seat measured only the first. Whether the overwrite was a stale build tree, an intended promote, or a third thing is not established here. (2) It does NOT claim the S12 code was ever WRONG -- its own AC3 exercise passed on the box and is not in question; the code was correct and was subsequently replaced. (3) It does NOT re-grade the ledger. The ledger was accurate at close. (4) It does NOT touch FWD-12's logging half, which is independently served by OP-s-5 and re-verified today on a delivered object. || THE CLASS, which is bigger than this instance and is homed elsewhere: a deploy-completion record certifies a moment, and the estate has no control that notices when a LATER deploy of a SHARED artifact silently reverts an EARLIER one's proven change. CLAUDE.md NEVER-2 already carries this shape for container images -- 'an IMAGE act names in that entry EVERY task family that pulls the tag it moves' -- and this is the same failure on an EC2 code path, where the shared artifact is one /opt directory that every gateway-touching lane deploys wholesale. Filed here because the instance is this project's, with the class named as belonging to the deploy-ledger contract; closing NFRA_OPSEC202609 would not close it. || THE OBSERVATION-WINDOW CONSEQUENCE, stated so it is a RESULT and not a wait: the window's clock has not started. Its honest start is the moment BOTH the redeploy and the listener rules are live and a caller can actually exchange, and its length still needs callers 1 and 2's real cadence measured, exactly as the runbook says. Five elapsed days bought zero observations and must not be counted toward it.",
    "owner": "0.7.0_AE_CloudOps~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "0.7.0_AE_CloudOps~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S154",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TO-OP-S-10B and TO-OP-S-10 both carry PRD v0.12 @3619ebecd9 in their headers; the PRD is v0.14 @5f4d4b894f. The delta is INERT for this face -- FWD-10 and the OP-s-10 cell are unchanged across it -- and it is filed as the GO directs rather than left as an unrecorded difference.",
    "evidence": [
      "THE FACE SIDE, read at HEAD: both task orders' Directive lines name 'PRD `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9**'. The GO (msg 20546, 2.0.0_SA_COO~Z) states in terms: 'PRD is v0.14 @5f4d4b894f -- NOT the v0.12 the faces cite in their headers.'",
      "WHY IT IS INERT RATHER THAN MERELY SMALL, and this is the part that matters: the pin's CONSUMER on this face is the endpoint id FWD-10 and the decomp cell OP-s-10, and neither moved. The face's acceptance criteria S10B-AC0..AC5 are minted on the face itself, not read from the PRD, so no criterion this seat graded depends on the PRD version at all.",
      "THIS ROW DOES NOT CLAIM THE PRD DELTA IS EVERYWHERE INERT. It claims it is inert FOR THIS FACE, on the two objects this face consumes. v0.14's own commit body carries C-19 and the FWD-19 recut, which are other cells' surfaces; whether the delta is inert for those is not established here and is not this seat's read."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY FILED AT ALL GIVEN IT IS INERT: the GO makes the re-ground a MANDATED first act and directs any delta to the channel. A delta that is checked and found harmless is a different object from a delta that was never checked, and only a row can tell those two apart afterwards -- an unfiled inert delta reads identically to an unperformed re-ground. || DISARM: a header refresh on the two faces at the next recut, which is the issuer's act and not available to this lane mid-round (Rule 27 freezes the spec). Filed INERT rather than ARMED because no actor is recruited into a wrong path by the stale pin: the faces are self-contained on criteria.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S155",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "LAMBDA REPORT `Duration` CANNOT DISCRIMINATE WHICH SECRET A CACHE RE-READ HIT, because opal-portal-authorizer holds TWO independent 300 s caches -- the JWT public key (new, TO-OP-S-10B) and the ORIGIN-VERIFY secret (pre-existing, TO-OP-S-1 limb 2a) -- and both produce the same ~100-150 ms spike on the same period. A seat measuring 'does the JWT key cache expire' by duration alone gets a CONFOUNDED pass that the OLD code reproduces.",
    "evidence": [
      "THE INSTRUMENT THAT LOOKED SUFFICIENT: on the post-deploy warm environment (log stream b3cd3952..., ONE INIT_START, that one at 18:59:10Z BEFORE the window opened) 25 probe invocations show REPORT Duration ~1.4-2.5 ms with three spikes -- 146.24 ms at t+0s, 156.68 ms at t+308s, 125.10 ms at t+621s. Intervals 308 s and 313 s against a stated TTL of 300000 ms, sampled every ~22 s. That reads as a clean TTL demonstration.",
      "THE NEGATIVE CONTROL THAT BROKE IT: the same measurement on the PRE-DEPLOY code, stream 3abd1fa8..., ONE INIT_START, environment lifetime 6687 s, 96 invocations with a REPORT -- returns 21 spikes >30 ms. Under the OLD code the JWT key cache had NO TTL at all and could re-read at most ONCE per environment, so 21 spikes cannot be JWT-key re-reads. The old code therefore REPRODUCES the signature the new code was being credited for.",
      "THE MECHANISM, read at source rather than inferred: infra/aws/users/lambda/portal-authorizer/originVerify.mjs:39 sets ORIGIN_VERIFY_TTL_MS = 300000, and isOriginVerified() runs on EVERY request BEFORE the JWT key is touched. The shared JWT module deliberately chose the SAME 300 s (jwtPublicKeys.mjs, 'deliberately the same number') so a rotation runbook reasons about one window. The consistency that makes the runbook safe is exactly what makes the duration instrument blind.",
      "THE DISCRIMINATING INSTRUMENT, which is a DIFFERENT plane and not a re-run of the same one: CloudTrail GetSecretValue carries the secretId. Filtered to (secretId=opal/auth/jwt-public-key, role=opal-portal-lambda-role) over 16:00-19:40Z -- 518 GetSecretValue events scanned, NextToken ABSENT so the window is complete -- OLD CODE 16:00->18:50 (170 min) = 3 reads; NEW CODE 18:50->19:40 (50 min) = 7 reads. The three inside the warm window land at 19:21:03, 19:26:11, 19:31:25, matching the duration spikes to the second.",
      "SO THE AC2 RESULT SURVIVES -- but on CloudTrail, not on duration. The duration series is retained as CORROBORATION FROM A SECOND PLANE (the function's own log vs the Secrets Manager control plane), never as the evidence."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS WORTH A ROW WHEN THIS SEAT'S OWN RESULT STILL PASSES: the next seat to touch this consumer -- TO-OP-S-10's rotation, which must watch consumers converge -- faces exactly this measurement, and the confounded instrument gives a PASS that the pre-change code also gives. A control that a wrong answer would also survive is not a control. || THE TRANSFERABLE SHAPE, and it is CLAUDE.md Rule 22's shared-dependency clause seen from the instrument side: two caches in one process, given the SAME TTL for a good reason, become indistinguishable on any per-process timing signal. Ask what ELSE in the handler is on that period before reading a periodic spike as your subject. || INERT because nothing is mis-stated in the record: the AC2 evidence as filed rests on CloudTrail, and the duration series is labelled as corroboration. The row exists so the next seat does not start from the confounded instrument.",
    "owner": "0.7.0_AE_CloudOps~V",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps~V",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S156",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "ANY Lambda@Edge CODE DEPLOY IN portal-auth MUST CARRY ANOTHER CELL'S UNAPPLIED WAF WORK. Repointing CloudFront requires -target=aws_cloudfront_distribution.portal, and the distribution DEPENDS ON the WAF web ACL, so terraform pulls three OP-s-15 / C-2 resources into the apply. Measured NON-DESTRUCTIVE here (net rule set unchanged), but it is unavoidable, it is not the deploying lane's work, and a future drift on those resources would ride a live-auth apply silently.",
    "evidence": [
      "THE DEPENDENCY IS STRUCTURAL, not a scoping mistake: -target=aws_lambda_function.auth_validator_edge[0] alone plans 1 change with ZERO wafv2 resources (measured). Adding -target=aws_cloudfront_distribution.portal -- which is REQUIRED, because publishing a version does not repoint CloudFront -- takes the plan to 4 changes, the extra three being aws_wafv2_ip_set.opal_blocked_ips_cloudfront_v4, ..._v6 and aws_wafv2_web_acl.opal_cloudfront_protection. terraform -target includes a resource's dependencies, and the distribution references the web ACL.",
      "WHAT THE THREE CHANGES ACTUALLY ARE, measured rather than assumed -- and this seat's FIRST READ OF THEM WAS WRONG, which is why the measurement is quoted: the plan renders three `- rule { ... -> null }` blocks naming AWSManagedRulesCommonRuleSet, AWSManagedRulesAmazonIpReputationList and AWSManagedRulesKnownBadInputsRuleSet, which reads as three managed security rule groups being STRIPPED from the live edge. Counting BOTH halves shows 3 removals and 3 additions of the SAME three names, removed-not-added = [] and added-not-removed = []: `rule` is a SET, so any nested change renders as remove+add. Net rule set UNCHANGED. The live ACL carries 6 rules (BlockedIPs, RateLimitRule, AuthLoginRateLimit, ip-reputation, common-rule-set, known-bad-inputs) before and after.",
      "THE IP-SET CHANGES ARE DESCRIPTION-ONLY: `+ description = \"NFRA_OPSEC202609 C-2: addresses blocked at the edge. Written ONLY by the OP-s-15 reconciler from opal-suspicious-addresses, never by hand.\"` on each of v4 and v6, with '(7 unchanged attributes hidden)'. Declared-not-applied metadata from this same project's C-2 cell.",
      "PLAN-WIDE GUARDS ON THE APPLY THAT DID RUN: 0 to add, 4 to change, 0 to destroy, 0 forces-replacement.",
      "SEPARATELY, THE SAME FILE'S PIN ROSTER HAD GONE STALE TWICE: lambda-edge.tf's header block read 'THREE functions below still carry ignore_changes = [qualified_arn, ...]: auth-validator-edge, public-data-router, cache-control-injector'. public-data-router was unpinned 2026-08-21 and that edit did not correct the roster; this face unpinned auth-validator-edge and DID correct it, to ONE (cache-control-injector), naming both stale entries. Fixed in the same commit rather than filed as debt."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY ARMED RATHER THAN INERT: the hazard is not today's diff, it is the NEXT one. The WAF resources belong to OP-s-15 / C-2 and are actively being worked; the next edge code deploy will pull whatever state they are in AT THAT MOMENT, into an apply on the distribution that fronts every portal request, and the deploying seat may not think to read the WAF half of its own plan. Today it was 3 set-element replacements; there is no control that keeps it that way. || DISARM, and it is the issuer's because it spans two cells: either land C-2's WAF drift so the chain is 0-diff and future edge applies pull nothing, or record on lambda-edge.tf that an edge deploy MUST read and account for the WAF half of its plan before applying. This seat did the second inline as evidence in its own ledger leg but did not write it onto the file as a standing instruction, because the file belongs to a shared surface and the ruling on which of the two remedies applies is not this lane's. || WHAT THIS ROW DOES NOT CLAIM: it does not say the WAF drift is wrong, does not adjudicate whose it is beyond reading C-2 off the description string, and does not assert the ip-set descriptions are the only pending C-2 change -- only that these three resources were what the dependency chain pulled at this vintage.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S157",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "THE ROTATION IS BLOCKED AND THE STOP BRANCH FIRES. The rotation consumer set is FOUR readers, of which THREE are verifiers, and the THIRD VERIFIER -- opal-session-analytics -- is STILL SINGLE-SLOT WITH NO TTL ON ITS DEPLOYED BYTES while running 52,540 invocations in the last 7 days. TO-OP-S-10B taught the two consumers IT owned; session-analytics was ruled out of THAT face's build scope and nothing has since taught it. Rotating opal/auth/jwt-public-key today breaks the estate's busiest verifier, partially and silently.",
    "evidence": [
      "THE DENOMINATOR, RE-MEASURED TODAY RATHER THAN INHERITED. list-functions returns 203 live functions with NextMarker ABSENT -- a real denominator and not a page -- across 115 distinct roles. The five roles that grant secretsmanager:GetSecretValue on opal/auth/jwt-public-key carry 31 of them: lambda-edge-execution-role 5, lambda-execution-role 13, opal-portal-lambda-role 12, opalinvest-auth-lambda-role 1, portal-auth-lambda-role 0. That 31 is the UPPER BOUND and matches the figure established on TO-OP-S-10B five days ago; the function count moved 201 -> 203 in between, so the re-measure was not a formality.",
      "THE CODE-PLANE CENSUS OVER THE UPPER BOUND: each candidate's DEPLOYED artifact was downloaded and every member searched for the literal secret id. 29 of 31 artifacts read, 25 with NO hit, 4 READERS. auth-validator-edge (lambda-edge-execution-role) TWO-SLOT; opal-portal-authorizer (opal-portal-lambda-role) TWO-SLOT; opalinvest-auth-handler (opalinvest-auth-lambda-role) single-slot; opal-session-analytics (opal-portal-lambda-role) SINGLE-SLOT.",
      "THE INSTRUMENT WAS CONTROLLED BEFORE IT WAS TRUSTED, and its FIRST RUN WAS A FALSE CLEAN worth recording: the census initially returned READERS=0 on all 31 because python cannot exec the .tools/aws bash shim on Windows (WinError 193) -- a summary line reading 'READERS: 0' that meant 'the probe never ran'. The error count 31 was the only tell. Re-pointed at .tools/aws.cmd and then POSITIVE-CONTROLLED: a known reader (opal-session-analytics) returns HIT and a known non-reader (cache-control-injector) returns no hit, so the instrument discriminates and the 25 zeros are real absences.",
      "SESSION-ANALYTICS IS SINGLE-SLOT ON THE DEPLOYED BYTES, not merely in the repo. The live artifact (CodeSha256 TW+G6NyLoKxqCdp6CtfU5WAixRf8phcP69Kxg6kx8EU=, LastModified 2026-09-04T05:44:08Z, State Active) unzips to one member, dist/index.mjs, minified. Its key read: `async function lJ(){if(wq)return wq;if(wq=(await cJ.send(new uJ({SecretId:\"opal/auth/jwt-public-key\"}))).SecretString||\"\",!wq)throw Error(\"JWT public key not found\");return wq}` -- ONE scalar, `if(wq)return wq` with NO time component, exactly ONE occurrence of the secret id, and no two-slot symbol anywhere. That is byte-for-byte the same defect opal-portal-authorizer carried before TO-OP-S-10B. Source agrees: src/auth.ts:42-56 `if (cachedPublicKey) return cachedPublicKey;` then a single jwt.verify at :75.",
      "A NEAR-MISS ON THAT READ, recorded because it would have inverted the finding: a first pass grepped the deployed bundle for the SOURCE identifier `cachedPublicKey` and got 0, which reads as 'the single-slot cache is gone'. It is not gone -- tsc renamed it to `wq`. An absence of a SOURCE-LEVEL name in a COMPILED artifact is not evidence about behaviour, and the only sound read was opening the minified call site.",
      "IT IS ALIVE, MEASURED FRESH RATHER THAN CITED FROM 09-04: CloudWatch Invocations for opal-session-analytics over the last 7 days total 52,540 -- 18,035 on 09-02, 8,679 on 09-03, 585 on 09-04, 42 on 09-06, 7,283 on 09-07 and 17,916 on 09-08. THE ORACLE DISCRIMINATES: a dead function returns zero datapoints or all-zero Sums, and this returns six nonzero days.",
      "WHAT THE CENSUS CANNOT SEE, printed rather than implied. (1) TWO of the 31 were NOT read: opal-news-ai-sentiment and news-semantic-clustering are PackageType Image (ECR: finbert-lambda:latest and news-semantic-clustering:latest) so there is no zip to fetch -- the 25 zeros DO NOT COVER THEM, and closing them means pulling the images and searching their layers. (2) A function that builds the secret id dynamically would not match the literal needle. (3) A reader OUTSIDE the five granting roles -- an inline policy on another principal, a resource policy on the secret, an EC2/ECS task, a human -- is out of this frame entirely. (4) The code plane says who CAN read, never who DOES."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS A STOP AND NOT A DELAY. The issuer's binding condition on the GO (msg 20613) says it in terms: 'if the set is larger than the two consumers taught, STOP and report rather than proceeding: a rotation against consumers that were never given a second slot is out of this face's bounds and is a new cut, not an extension.' The set is larger. Nothing was rotated and no secret was written. || WHY THE FAILURE MODE MAKES THIS WORSE THAN IT LOOKS, per 2.0.0_SA_COO~Z's own correction in msg 20309: session-analytics' cache is bounded by CONTAINER LIFETIME (median 5.6 min, max observed 143 min over 107 lifetimes), so a rotation would NOT break it loudly and permanently -- it would produce a PARTIAL, SILENT, SELF-CLEARING outage of unbounded tail, in which some containers hold the retired key and some fetch the new one, both serve, and the failure rate decays toward zero on its own while looking like unrelated flakiness. A post-rotation check that comes back clean is CONSISTENT with that outage. There is therefore no post-hoc verification that would catch this; the only control is not rotating until the third verifier holds two slots. || THE REMEDY IS SMALL AND ALREADY DESIGNED, which is why this row is BLOCKING rather than merely observed: session-analytics has a src/ directory, so the canonical build already mirrors infra/aws/lambda/lib/ into it (build-nodejs-lambda.sh:137-158) and the shared module jwtPublicKeys.mjs is ALREADY PRESENT in its tree. Teaching it two slots is an import swap plus the same TTL the other two now carry, on a build path TO-OP-S-10C proved works. It is a cut, not a research problem. || THE SIGNER IS NOT PART OF THIS DEFECT. opalinvest-auth-handler also matched the needle and is also single-slot, and that is CORRECT by the issuer's re-cut @dd39dab70e: a verifier accepts current-or-previous, a signer must know which key is CURRENT. It is named here only so a reader of the count of 4 does not mistake it for a fifth thing to fix. Its rotation-time handling -- picking up the NEW private key, and whether its own read is cached without a TTL -- is a separate question this row does not answer. || NOT WIDENED: this row does not propose who should cut the session-analytics face, does not re-grade TO-OP-S-10C, and does not claim the two image-based functions are or are not readers.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S158",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "THE INSTRUMENT Z-S151 LEFT UNREAD HAS BEEN READ BY ANOTHER PROJECT, AND IT SPLITS THE QUESTION IN TWO RATHER THAN ANSWERING IT. The AWS account is in the SNS SMS SANDBOX, so every SMS-protocol subscriber across all four 'confirmed' topics resolves to an UNVERIFIED destination and opal-infrastructure-alerts -- the infrastructure monitor's own escalation channel -- reaches nobody today. ⛔ THIS DOES NOT CHANGE Z-S151's STANDING: FWD-4's channel under C-20 is EMAIL to andrew@opalinvest.com, which is a DIFFERENT PLANE that the sandbox does not touch. Z-S151 stays ARMED, for its original reason and no new one.",
    "evidence": [
      "RELAYED SOURCE, quoted rather than paraphrased (1.0.0_SA_CTO~Z msg 20626): 'the AWS account is in the SNS SMS SANDBOX, so every SMS-protocol subscriber across all four \"confirmed\" topics resolves to an unverified destination, and opal-infrastructure-alerts -- the escalation channel -- reaches nobody today.' Its own provenance line states it was rendered by RP-s-6 and NOT routed as a row on that project.",
      "WHAT THIS SEAT DID NOT DO, stated because the qualifier is the value: no independent read was taken. The discriminating instruments would be `sns get-sms-attributes` (sandbox state) and `sns list-subscriptions-by-topic` per topic ARN, both AE-lane reads. Z-S151 already named the second of those as the instrument it had not run; it is still not run BY THIS SEAT.",
      "THE PLANE SPLIT, read at source in this project's own PRD rather than inferred: C-20 (PRD v0.14) names FWD-4's recipient as andrew@opalinvest.com -- an EMAIL endpoint. The SMS sandbox bounds SMS-protocol subscribers. The two do not intersect, so the sandbox finding cannot discharge Z-S151 and cannot worsen it either.",
      "Z-S151's OWN unchanged blocker, re-read at this vintage: an SNS EMAIL subscription is PENDING until the recipient CONFIRMS, and FWD-4 reaches EXERCISED on a DELIVERED message, never on a created subscription. That confirmation is Andrew's act and no seat can take it."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS FILED AS A SEPARATE ROW RATHER THAN AN EDIT TO Z-S151: the channel is append-only, and `adjudicates` -- the field that re-resolves an earlier item's state -- is used in this file only by 3.0.0_SA_CVO~Z on L9 adjudication rows (2 of 157). A COO row that claimed it would be taking a CVO instrument. Plain reference is the precedent every other correcting row here uses (Z-S57 -> Z-S53, Z-S58 -> Z-S56, Z-S75 -> Z-S68), and it deliberately leaves Z-S151's own standing untouched. || WHY INERT: for THIS project the finding is grounding, not a new hazard. The live hazard it describes -- an escalation channel that pages nobody -- belongs to the infrastructure report's own surfaces and to the standing alerting moratorium, neither of which is this project's to act on. Nothing here builds, repairs or proposes an alert. || ⭐ THE REUSABLE SHAPE, and it is why the row is worth its cost: a 'confirmed' subscriber is confirmed AT THE SUBSCRIPTION, and the account-level sandbox is a SECOND gate one API call away that no per-subscription read can see. A per-topic census of subscriptions returns CONFIRMED for endpoints that cannot receive anything -- the same shared-dependency shape CLAUDE.md rule 22 names, where every per-member arm passes while the thing the members have in common is broken. || WHAT WOULD ACTUALLY DISARM Z-S151, unchanged by this row: a DELIVERED message to andrew@opalinvest.com observed at the recipient, which requires his confirmation click first.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S159",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "THE ROTATION IS STILL BLOCKED, AND THIS TIME IT IS THE SIGNER. opalinvest-auth-handler caches the JWT PRIVATE key in a bare scalar with NO time component on its DEPLOYED bytes, so writing a new signing key does NOT move signing: a warm container keeps signing with the RETIRED key for a lifetime Lambda does not bound. S10-AC4's 'a login after the switch yields a token resolving to the NEW key' is UNSATISFIABLE AT ANY WAIT LENGTH -- the exact defect TO-OP-S-10B fixed for the verifiers, still present on the one component the rotation must actually switch.",
    "evidence": [
      "MEASURED ON THE DEPLOYED BYTES, NOT ON SOURCE. opalinvest-auth-handler, CodeSha256 X8YBkwUqnuTDLW7XvqovWT9+TujBXbTaXQaEdwHxwZc=, LastModified 2026-09-04T02:14:11Z, State Active, runtime nodejs22.x, role opalinvest-auth-lambda-role. The artifact unzips to one member, dist/index.mjs, minified. THE PRIVATE-KEY READ: async function E8(){ if(pq) return pq; if(pq=(await vZ.send(new yZ({SecretId:\"opal/auth/jwt-private-key\"}))).SecretString||\"\",!pq) throw Error(\"JWT private key not found\"); return pq } -- ONE scalar pq, a guard with NO time component, exactly ONE occurrence of the private-key secret id.",
      "THE SAME FUNCTION HAS THREE UNBOUNDED CACHES, all quoted from the same artifact: pq (the PRIVATE signing key, above); cq (the PUBLIC key) -- async function hZ(){ if(cq) return cq; ... SecretId:\"opal/auth/jwt-public-key\" ... }; and A6 (the MFA code seal key) -- if(A6) return A6; let q=await E8(); return A6=Buffer.from(hkdfSync(\"sha256\",q,Buffer.alloc(0),\"opal-mfa-code-seal-v1\",32)), A6. None of the three carries a time component.",
      "*** THE INTERNAL CONTROL IS WHAT MAKES THIS A DEFECT RATHER THAN AN ESTATE CONVENTION, and it lives in the SAME BUNDLE: *** the origin-verify read in that artifact IS bounded -- var a3=\"opal/auth/origin-verify\", e3=\"x-opal-origin-verify\", d6=null, b1=0, q2=300000; async function $2(){ let q=Date.now(); if(d6 && q-b1<q2) return d6; ... }. So this function demonstrably knows the bounded-cache idiom, applies it to the ORIGIN secret (TO-OP-S-3's two-slot module), and applies it to NEITHER JWT key. The single occurrence of 300000 in the whole bundle belongs to that origin cache and must not be mistaken for a JWT key TTL.",
      "SOURCE AGREES, checked in the direction that could have falsified the deployed read rather than merely echoed it: infra/aws/opalinvest_dev/lambda/auth-handler/src/jwt.ts:21-35 is 'if (cachedPrivateKey) return cachedPrivateKey;' and :38-50 the same shape for the public key, with no TTL constant anywhere in the file. jwt.ts is also where getMfaCodeSealKey derives the AES key from the private key by HKDF.",
      "WHY A REDEPLOY IS NOT THE ANSWER, and it is the project's own language: a redeploy cycles the execution environments and clears a container-bound cache, which is the mechanism that ALREADY EXISTS. TO-OP-S-10B's S10B-AC2 voids itself if a redeploy appears in its window for exactly this reason, and condition 3 of this rotation's GO (msg 20632) forbids redeploying any consumer during the convergence window. A convergence that requires a redeploy is an accident, not a rotation property.",
      "WHAT THIS ROW DOES NOT CLAIM. It does not claim the signer is BROKEN today -- it signs correctly with the key it holds. It does not claim a rotation would fail loudly; the opposite is the problem. And it does not re-grade TO-OP-S-10B or TO-OP-S-10D, both of which were correctly scoped to VERIFIERS and both of which did what they were cut to do."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS A STOP AND NOT A DELAY, and why it is the SAME CLASS as Z-S157 rather than a new one: Z-S157 found a single-slot, no-TTL cache on a VERIFIER and the rotation was barred until it was taught. This is a no-TTL cache on the SIGNER. The verifier defect broke the READ side of the overlap; this breaks the WRITE side -- the moment the rotation is actually supposed to accomplish. Both are the same missing property (a bounded cache on a rotating secret) on opposite halves of the same act. || THE REMEDY IS NOT TWO SLOTS AND THAT DISTINCTION IS LOAD-BEARING. The issuer's re-cut @dd39dab70e is explicit that a signer must NOT be taught two slots: a verifier accepts current-or-previous, a signer must know which key is CURRENT, and two slots there would let it sign under a retired key. What the signer needs is exactly ONE property it lacks -- a BOUNDED TTL on its private-key read -- so that a signing switch converges within a known window instead of never. That is a smaller change than TO-OP-S-10D and it is the same shared-module TTL idiom already deployed three times today. || A SECOND, SEPARATE CONSEQUENCE THAT MUST NOT BE FOLDED INTO THE FIRST: the MFA code seal key is HKDF-derived from the private key, and jwt.ts:88-90 states in terms that changing the key invalidates every sealed code in flight, calling that 'the correct behaviour for a key rotation'. It is -- but the seal cache is ALSO unbounded, so during the window containers disagree about the seal key non-deterministically. unsealCode returns null on a wrong key and mfa.ts's callers mint a REPLACEMENT code rather than sending nothing, so this DEGRADES GRACEFULLY and is not a break; verification uses hashCode against the stored row and is untouched. It is recorded so the rotation runbook expects resend-idempotency to lapse during the window rather than discovering it live. || WHAT I DID NOT DO: nothing was rotated, no keypair was minted, no secret was written, and no consumer was redeployed. The face's own compiler_tools_mandate phase 1 says to STOP at deliverable 1 and file the row rather than proceed to deliverable 2, and msg 20632 states that stopping is a correct outcome if the rotation cannot be completed safely.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S160",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "THE ROTATION WOULD SIGN EVERYONE OUT, AND THE CAUSE IS TO-OP-S-10E's OWN SINGLE-KEY RULE APPLIED TO THE WRONG READ. opalinvest-auth-handler is ALSO A VERIFIER -- /auth/refresh calls verifyRefreshToken -> getJwtPublicKey -> getCurrentKey, which returns CURRENT ONLY. Refresh tokens live 7 DAYS. The moment the rotation writes the public envelope, every refresh token signed by the old key fails at that endpoint, which is FWD-10's own no-sign-out bar failing.",
    "evidence": [
      "MEASURED ON THE DEPLOYED BYTES OF THE ARTIFACT THIS LANE SHIPPED AT 22:38Z (CodeSha256 ZrHoxMzn0YsK5oA1lq0OMcsoaL9xzN3RkYFxY9Opjyk=): the public-key getter is `async function fZ(){return await T8(U3)}` where T8 is getCurrentKey and U3 is \"opal/auth/jwt-public-key\" -- so it returns the CURRENT slot and nothing else. verifyWithSlots is NOT bundled in this artifact at all, so no two-slot accept path exists anywhere in the signer.",
      "THAT READ IS A VERIFICATION PATH, NOT A SIGNING ONE. src/jwt.ts:225-236 verifyAccessToken and :238-249 verifyRefreshToken BOTH call getJwtPublicKey() and hand the result straight to jwt.verify. Signing uses the PRIVATE key and never touches this read.",
      "THE REFRESH ROUTE IS LIVE, measured on the wire rather than inferred from the code: POST https://opalinvest.dev/auth/refresh returns 401 {\"error\":\"No refresh token\"} -- the handler ran and answered. Its call site is src/auth.ts:435, `const payload = await verifyRefreshToken(refreshToken)` inside export async function refresh().",
      "THE WINDOW IS SEVEN DAYS: src/jwt.ts:14 REFRESH_TOKEN_EXPIRY = '7d' (:13 ACCESS_TOKEN_EXPIRY = '15m'). So an access token's exposure is 15 minutes and self-clears, but a REFRESH token's is seven days, and refresh is the endpoint a client hits precisely when its access token has expired -- i.e. the failure lands on every returning user rather than on an unlucky few.",
      "THE MECHANISM, stated so it is not mistaken for the verifier problem already fixed: the rotation writes opal/auth/jwt-public-key as a {current, previous} envelope. The THREE consumers taught by TO-OP-S-10B and TO-OP-S-10D read it through getJwtKeySlots + verifyWithSlots and accept BOTH. The SIGNER reads it through getCurrentKey and accepts ONE. Whichever key is placed in `current`, the signer rejects tokens signed by the other -- so there is no arrangement of the envelope that keeps /auth/refresh working across the switch.",
      "AND THE SAME FUNCTION ALREADY DOCUMENTS THE ESTATE'S STANDARD FOR EXACTLY THIS CLASS, which is why the bar is not in doubt: src/auth.ts, inside refresh() itself -- 'THE OLD SHAPE IS ACCEPTED FOR ONE REFRESH_TOKEN_EXPIRY WINDOW (7d) SO THAT NOBODY IS SIGNED OUT BY THIS CHANGE.' That is OP-s-11 / finding F-10 accepting two token SHAPES for 7 days for the no-sign-out reason. The same reasoning applies to two token KEYS and was not applied.",
      "WHY THIS WAS NOT CAUGHT AT TO-OP-S-10E, said plainly rather than absorbed: S10E-AC2 required 'BOTH JWT key reads ... each still selecting ONE key' and called a two-slot accept path on the signer 'a FAIL, not a bonus'. This lane implemented exactly that and the criterion graded PASS on evidence that was accurate. The instruction's stated RATIONALE was entirely about signing -- 'a signer must know which key is CURRENT, and two slots would let it sign under a retired one' -- which is correct for the PRIVATE key and does not transfer to the PUBLIC one. The face, the issuer's message and this lane all treated 'the signer' as one role when the component has TWO, and only the private half was the one the rationale described."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS A STOP: FWD-10's outcome bar is that a live session must survive the rotation, and msg 20668 restates it above every mechanical criterion -- 'a rotation that works but signs everyone out has failed the outcome while passing every criterion on the face'. This is that case, found before the act rather than after. Nothing was rotated; no keypair was minted and no secret was written. || THE REMEDY IS SMALL AND THE DISTINCTION IS THE WHOLE OF IT: the signer's PRIVATE key read stays SINGLE-CURRENT -- that is correct and TO-OP-S-10E's rationale holds for it exactly as written. The signer's PUBLIC key read should use getJwtKeySlots + verifyWithSlots, the same two-slot idiom the other three verifiers already carry, because in that path the signer IS a verifier. One function changes; the module already exports what it needs; no new pattern is introduced. || THE GENERALISATION, which is bigger than this instance: A COMPONENT'S NAME IS NOT ITS ROLE SET. 'The signer' reads two secrets and plays two roles, and a rule written for one of them was applied to both because the name carried the rule rather than the read did. The check that would have caught it is asking, per READ rather than per component, what that value is used FOR. || THIS ROW IS FILED AGAINST THIS LANE'S OWN WORK. TO-OP-S-10E is deployed, its instance is VALID and its criterion S10E-AC2 was graded PASS on accurate evidence -- the face did what it said. This row does not retract it and does not claim the deploy was wrong; it says the RULE that face applied was right for one read and wrong for the other, and the rotation is what makes the difference load-bearing.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S161",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "A MULTI-LINE VALUE PASSED AS ONE ARGV ELEMENT THROUGH .tools/aws.cmd IS SILENTLY TRUNCATED AT THE FIRST NEWLINE, AND THE API STILL RETURNS rc=0 WITH A VersionId AND VersionStages ['AWSCURRENT']. The JWT signing key was stored as its 27-byte first line and was INVALID IN PRODUCTION for 3m52s. Nothing at the call site said so; only reading the secret BACK from AWS caught it.",
    "evidence": [
      "THE WRITE REPORTED SUCCESS. put-secret-value on opal/auth/jwt-private-key returned rc=0, VersionId 5bc63c94-7d91-4deb-b622-7ae0f8e71935, VersionStages ['AWSCURRENT'], CreatedDate 2026-09-10T01:09:42.364Z. Every signal available at the call site said the act had landed.",
      "THE STORED VALUE WAS 27 BYTES. Read back from AWS: the single line '-----BEGIN PRIVATE KEY-----' and nothing after it. The local source file is 1703 bytes. Raw sha256 served 3021d90eb9437b2d... against local a43e15c7dbdf268d..., and `openssl rsa -pubout` on the served value exits 1 with 'Could not find private key from <stdin>' while the same command on the local file exits 0 -- a positive control run beside the failure.",
      "THE MECHANISM: .tools/aws.cmd is a WINDOWS CMD BATCH SHIM. CMD re-parses its argument vector on its own terms and cannot carry an embedded newline inside a single argument, so the value was cut at the first LF and the remainder discarded. The truncation happens BELOW the Python process and ABOVE the AWS API, which is why neither end reports it.",
      "THE REMEDY I REACHED FOR IS WHAT CAUSED IT. I chose argv-with-shell=False OVER `file://` deliberately, to avoid the known shim path-rewriting hazard. shell=False protects against THE SHELL; the shim is not the shell -- it is a CMD process downstream of it. A precaution aimed at the wrong layer reads as diligence and buys nothing.",
      "THE FIX, AND ITS CONTROL: boto3 put_secret_value with the identical Python string stored 1703 bytes, VersionId 579af491-ab27-4463-978d-b076cd5ce44a at 2026-09-10T01:13:34.378Z, raw text byte-EQUAL to the local file on read-back and SPKI DER cb550976f5907f9f... equal to newpub.pem and to the public envelope's CURRENT slot. boto3 speaks HTTPS from inside the process, so no CMD layer exists to re-parse anything.",
      "THE SECOND-ORDER DEFECT THE FIX CREATED, found by looking for it rather than by being told: re-writing the correct key moved AWSPREVIOUS onto the 27-BYTE TRUNCATED VERSION. This order's own ledger title names rollback as 'update-secret-version-stage moving AWSCURRENT back' -- so the DOCUMENTED RECOVERY PATH had been converted into a second outage. Disarmed 2026-09-10T01:18:14Z by moving AWSPREVIOUS onto 1acd44f3-d07e-486b-9ad8-66993a0b6716 and reading the stage back (1704 bytes, DER 3051443047acf258...). Nothing was deleted; the truncated version retains its id and simply holds no stage.",
      "BLAST RADIUS, MEASURED, DENOMINATOR PRINTED: opalinvest-auth-handler took ONE invocation in 01:00-01:20Z, at 01:11:32Z, inside the invalid window and on a COLD START (INIT_START 01:11:31.933Z) -- precisely the no-cached-key case that would have had to read the broken secret. Errors metric 0, but THAT IS THE WEAK ARM since a handled 500 never increments it. The log stream closes it: that request logged 'POST /auth/refresh' then END with NO ERROR line, and the generic catch demonstrably DOES log, because this lane's own CTL arm at 01:16:34Z produced 'ERROR Error: W6 [JsonWebTokenError]: invalid signature' through the same path. So it returned before reaching getJwtPrivateKey. NO user-facing failure is MEASURED, on a denominator of 1 -- which is not the same as the window having been harmless."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THE GENERALISATION, which outlives this project and is not about AWS: A WRITE RECEIPT CERTIFIES THAT A VERSION WAS CREATED, NEVER WHAT IT CONTAINS. Any acknowledgement whose subject is the transaction cannot testify about the payload, and the more specific the receipt looks -- an id, a stage, a timestamp -- the more it reads as content confirmation. The only sound oracle is reading the object back and measuring it, which is what this order had already made a habit at L2 and is the sole reason this was caught. || A SECOND, SHARPER ONE: THE PRECAUTION AIMED AT THE WRONG LAYER IS WORSE THAN NONE, because it retires the worry. shell=False was chosen ON PURPOSE against a known hazard and felt like the careful option; the corrupting layer was a CMD shim underneath it. Name the layer a defence acts on before crediting it. || AND A THIRD: A FIX CAN ARM THE HAZARD IT LOOKS LIKE IT CLOSED. Writing the correct key is what poisoned AWSPREVIOUS -- the recovery path degraded precisely because the primary was repaired, and nothing announces that. || REMEDY CANDIDATES, named without a recommendation because shared tooling is not this lane's to change unilaterally: (a) a guard in the aws shim that REFUSES any argument containing a newline rather than truncating it, which converts a silent corruption into a loud stop; (b) route multi-line secret material through boto3 in-process rather than the CLI shim, which removes the CMD layer entirely; (c) a read-back-and-fingerprint requirement recorded in /cloud-ops for any secret write, which catches the class regardless of cause. (a) and (c) are independent and (c) already caught this one. || SCOPE HONESTLY STATED: measured on put-secret-value only. Every other .tools/aws.cmd call carrying a multi-line argv value is EXPOSED BY THE SAME MECHANISM but is NOT measured here, and this row does not claim a census of them.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S163",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THE disposition ENUM PRESENTS FOUR CO-EQUAL VALUES AND ONE OF THEM CANNOT BE USED AS A PER-ITEM DISPOSITION AT ALL. investigation_item.schema.json offers UNDER_INVESTIGATION, GRADUATED, DISMISSED_WITH_REASON and DECOMP_INVALIDATING as peers on one axis, and nothing in the schema distinguishes them. But surprise-row-gate.py treats a DECOMP_INVALIDATING row as CARRIED IN THE SLUG, so filing one fires the FULL L10 precondition: measured here, the gate refused with 'NEW row (disposition=DECOMP_INVALIDATING (carried in the slug)) while 99 of 162 investigation item(s) under NFRA_OPSEC202609 are NOT dispositioned'. THE VALUE IS THEREFORE UNUSABLE UNTIL EVERY OTHER ITEM IS ALREADY CLOSED -- which is to say it is a SLUG-LEVEL verdict wearing a PER-ITEM value's clothes. A schema-valid row was refused by the gate, so the schema is not the authority on which values an adjudicator may actually write, and a seat reading only the schema cannot discover that.",
    "evidence": [
      "THE SCHEMA TREATS THE FOUR AS PEERS: org/surprise_channel/schemas/investigation_item.schema.json, property `disposition`, enum ['UNDER_INVESTIGATION','GRADUATED','DISMISSED_WITH_REASON','DECOMP_INVALIDATING'], additionalProperties False, no per-value condition, no description distinguishing any of them.",
      "THE GATE DOES NOT: .tools/surprise-row-gate.py refused a row this seat had already validated against that schema with 0 violations and 0 unknown properties. The refusal text names the route word itself -- 'disposition=DECOMP_INVALIDATING (carried in the slug)' -- and the L10 precondition it triggers. The other three values do not trigger it: GRADUATED and DISMISSED_WITH_REASON rows landed in the SAME commit shape minutes earlier and in the same document (7509468e8b, 2c13e8202e).",
      "POSITIVE CONTROL, so the refusal is not read as a transient or as a defect in the row: the identical four-row commit with the DECOMP_INVALIDATING row REMOVED and its targets renumbered passed every gate, including the same surprise-row-gate, at 2c13e8202e. The only variable changed was the presence of that one value.",
      "THE CONSEQUENCE IS NOT HYPOTHETICAL AND ITS DIRECTION IS THE HAZARD: the honest verdict on NFRA_OPSEC202609-Z-S90 is DECOMP_INVALIDATING -- the issuer states at Z-S91 that 'OP-s-20 IS UNBUILDABLE AS DECOMPOSED' and that 'THE L5 DEFECT IS THIS SEAT'S'. With the value unavailable, the two paths out are the audited override (using an override on a gate that is refusing CORRECTLY) or a downgrade to GRADUATED (which files a required RECUT as if it were a fix, inside a decomposition that has no remedy in it). Both corrupt the record and BOTH ARE CHEAPER THAN HOLDING, which is what makes this ARMED rather than a note.",
      "RULE 24 IS THE FRAME, POSTULATE (iii) INTENT COHERENCE -- one axis, one intent: this axis mixes THREE verdicts about an ITEM with ONE verdict about the ROUND'S DECOMPOSITION. Postulate (iv) STATE COHERENCE is also engaged, since no remedy moves DECOMP_INVALIDATING the way a remedy moves the other three."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHAT THIS SEAT DID INSTEAD, so the hold is legible rather than looking like an omission: Z-S90 is HELD OPEN and will be dispositioned at the END of the per-item pass, with the reason recorded in C-S9's notes at 2c13e8202e. Neither escape was taken. || THE GATE IS NOT BEING CALLED WRONG. Its behaviour is defensible and probably intended -- a decomp-invalidating verdict genuinely is a statement about the round rather than the item, and gating it behind L10 readiness stops a mid-pass row from pre-empting the slug. THE DEFECT IS THAT ONLY THE GATE KNOWS. An adjudicator who validates against the schema, gets 0 violations, and writes the honest value discovers the asymmetry by being refused, which is the expensive way to learn it and happens after the document has been edited. || WHY THIS IS A ROW RATHER THAN A MESSAGE, and it is worth recording because it is structural: the CVO has NO outbound message path outside the L10 slug. This seat attempted to send this finding to 2.0.0_SA_COO~Z and 2.0.0_SA_COO~ZZ and the spine carrier refused it in terms -- 'the CVO sends to 1.0.0_SA_CTO, in the slug at L10, and to no one else' -- writing nothing for either recipient. So for this seat the channel is not the preferred carrier, it is the ONLY one before L10, which is exactly what rule 27's 'three tracks share FILES, never messages' prescribes. || FILING THIS ROW ADDS ITSELF TO THIS SEAT'S OWN BACKLOG and that is stated rather than netted out: undispositioned goes 100 to 101 of 162, and this row is dispositioned with the rest at the end of the pass, not by its own author in the same breath.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S164",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "THIS PROJECT'S REGISTER DESCRIBES A STATE SUPERSEDED A WEEK AGO, AND THE FIELD FROZE ON A VERDICT CORRECTION RATHER THAN ON A ROUND. project.json `phase` reads as a VERDICT CORRECTION about AMEND D's 39 = 21 non-OPTIONS + 18 OPTIONS split -- a tick-14 event -- and mentions neither round 2, nor the two cancellations, nor L8, nor the L9 now running. `blocking` is pre-round-2, still reading 'No task order may precede the L5 decomposition'. `last_updated` reads 2026-09-03 while the round it should describe has been executing and is now being adjudicated. THE CONTRAST IS WHAT MAKES IT VISIBLE AND IS THE CONTROL: the sibling NFRA_REPORT's `phase` reads current ('ROUND 2 ISSUED, L7 EXECUTING ... six of twelve outcomes REALIZED'), so the drift is this project's and not a property of the schema or of the field's intent.",
    "evidence": [
      "MEASURED AT HEAD by reading the file rather than accepting the report: org/missions/D12/NFRA/NFRA_OPSEC202609/project.json `phase` opens 'VERDICT CORRECTION (3.0.0_SA_CVO~Z 19895, of its OWN verdict 19674; worker row Z-S53; ledger correction row 5): AMEND D's split is 39 = 21 NON-OPTIONS + 18 OPTIONS...'. `blocking` opens 'None. No task order may precede the L5 decomposition (the spine's order, not a hold)'. `last_updated` is 2026-09-03.",
      "POSITIVE CONTROL ON THE SAME FIELD IN THE SAME SCHEMA, which is what separates a stale value from a field nobody maintains: the sibling project's register at org/missions/D12/NFRA/NFRA_REPORT/project.json reads `phase` 'ROUND 2 ISSUED, L7 EXECUTING. Round 1 CLOSED at L10 with six of twelve outcomes REALIZED' and `dep_stage` ROUND_CLOSE. The field IS maintained elsewhere, so this is drift rather than disuse.",
      "THE BLAST RADIUS IS BOUNDED AND IS STATED SO NOBODY SIZES IT UP: no gate reads `phase` or `blocking` -- they are not referenced by surprise-row-gate.py, to-pipeline-gate.py or missions-tree-check, and nothing downstream fails. The cost is that any seat or report GROUNDING on that JSON receives a description of a superseded state, which is precisely how 1.0.0_SA_CTO~Z met it: while grounding an /exec-sum for Andrew on both D12 projects.",
      "`dep_stage` IS NOT PART OF THIS FINDING and is deliberately excluded: it reads EXECUTING, and round 2 has not reached L10, so EXECUTING is defensible. Only the prose fields are stale. Sweeping dep_stage in would be the overcount this channel has been catching all night."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS ROW EXISTS AT ALL, and it is the second instance tonight of the same carrier gap: 1.0.0_SA_CTO~Z surfaced this finding BY MESSAGE (20770) and edited nothing, correctly. But CLAUDE.md s.2 is explicit that a broker message is NEVER the carrier -- a notifier watching files cannot see an inbox -- so a finding that exists only in one seat's inbox is one compaction away from gone. THE SEAT THAT SEES IT APPENDS ITS OWN ROW, which is what this is. The finding is the CTO's; the row is this seat's; neither is the register's owner. || A MILD IRONY WORTH ONE LINE BECAUSE IT DATES THE DRIFT PRECISELY: the stale `phase` describes THIS SEAT'S OWN verdict correction. The field froze at the moment this seat last gave the project something quotable, which is a fair account of how a prose status field actually ages -- it tracks the last memorable event rather than the current state. || FILED AGAINST THIS SEAT'S OWN BACKLOG rather than netted out: undispositioned goes 82 to 83 of 164, and this row is dispositioned with the rest at the end of the pass, not by its author in the same breath.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S165",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "FWD-12's MIGRATION DENOMINATOR COUNTS CALLERS, BUT THE CALLERS DO NOT HAVE ONE CODE CARRIER EACH. The 49F and cot auto-login boxes execute THE SAME FILE -- infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js is the canonical firm-parameterized script and there is no cot copy of it in the repo; only run-bd-auto-login.sh and secret-ids.env are per-firm. So this lane's migration commit @463f53561f, which is scoped to the 49F caller and to this lane's territory, ALSO migrates the cot caller at cot's next artifact pull -- a decision belonging to the PartnerETL lane, taken structurally by an edit in another lane's commit. 'Migration state 0 of 5' is measured per caller and is correct; what it does not show is that two of the five move together whether or not anyone intends it.",
    "evidence": [
      "TWO INDEPENDENT CARRIERS, because one file describing itself is not evidence about a second box. (1) SOURCE: infra/aws/ec2/bd-cot-auto-login/run-bd-auto-login.sh:50 reads `node \"$APP_DIR/bd_49f_auto_login.js\"` with APP_DIR self-locating from the wrapper (line 15), so on the cot box it resolves to /opt/bd-cot-auto-login and runs the 49F-named script. (2) DEPLOY RECORD, a different instrument and a different author: org/critical_paths/change_management/20260626T1444Z_cot-piece2-boxflip-stage_deploy_completion.md:17, LEG L3 proof, names `node $APP_DIR/bd_49f_auto_login.js` verified by SSM on the running path under BD_FIRM_ID=cot, CLOSED 20260626T144757Z.",
      "THE ABSENCE IS MEASURED, NOT ASSUMED: `ls infra/aws/ec2/bd-cot-auto-login/` returns exactly two files, run-bd-auto-login.sh and secret-ids.env. There is no cot .js to diverge, which is what makes the coupling structural rather than a drift that could be repaired by syncing.",
      "IT WAS ALSO RAISED BY AN INSTRUMENT THIS SEAT DID NOT CHOOSE, which is why it is filed rather than noted: the pre-commit risk reflex (comp-pulse diff, danger map 2.6h old, denominator 1 file against 1524 danger nodes) returned [HOLD] on bd_49f_auto_login.js and cited the cot deploy record above -- 11 recorded claims on that node. The estate had already written the warning down.",
      "WHY IT IS SAFE-BY-CONSTRUCTION AND STILL WORTH A ROW, so nobody sizes the risk up: the exchange presents whatever BD_OTP_GATEWAY_SECRET_ID resolves to, which on the cot box is cot's own firm-namespaced bearer (secret-ids.env, BD_FIRM_ID=cot), and the gateway returns a capability token whose sub is cot's label -- firm-sep (NEVER#1) is preserved and gw_cred_observe's firm attribution IMPROVES. The hazard is a GOVERNANCE one: a lane's credential posture changes without that lane deciding it.",
      "WHAT THIS SEAT HAS NOT ESTABLISHED, stated because the row would otherwise read as a cot finding: no cot-side exercise was run, no cot box was touched, and nothing here measures cot's deploy cadence or whether its box would pull at all. The claim is about the SHARED ARTIFACT, not about cot's behaviour."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THIS IS THE 'CHECK WHAT THE MEMBERS HAVE IN COMMON' CELL OF RULE 22, met from the inside rather than in review: a per-caller check certifies each of the five clean while the thing two of them SHARE is the object that actually moves. Every per-caller arm passes, so nothing fails, which is exactly the shape the rule describes. || THE ROW IS FILED BY THE SEAT THAT CAUSED THE CONDITION, not by a reviewer. This seat wrote @463f53561f; the coupling was found while writing it, and the honest place for it is the channel rather than this seat's own report, where it would read as a caveat instead of an obligation with an owner. || WHY IT IS NOT ALSO A FINDING AGAINST @463f53561f: the commit is correct for the 49F caller and its scope is this lane's. Narrowing it to avoid touching cot is not available -- there is no cot artifact to leave alone. The alternatives were to write it (and say so, which is this row) or to hold this lane's migration hostage to another lane's calendar, which nothing authorises and which leaves a never-expiring bearer on the wire meanwhile. || A NOTE FOR WHOEVER COUNTS FWD-12 LATER: if both boxes pull, migration moves 0 -> 2 of 5 on ONE artifact act, and the gateway's gw_cred_observe will show two distinct labels appearing at once. That is the expected shape, not a double-count.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S166",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Z-S165's COUPLING IS LATENT, NOT FIRING: THE cot BOX HAS NO RUN-TIME ARTIFACT PULL, SO @463f53561f DOES NOT REACH cot ON ITS OWN. Z-S165 states the shared .js migrates the cot caller 'at cot's next artifact pull' and correctly bounds itself as having measured no cot-side behaviour. Measured here on cot's own surface: the live SSM document that actually runs on i-0643a5bee8a8feabf contains NO s3 pull -- it cd's to /opt/bd-cot-auto-login and executes the BAKED bytes, its only s3 verb being a log PUSH afterwards. There is therefore no event that carries 463f53561f onto the cot box. The coupling Z-S165 describes is real and structural, but it fires only on a deliberate deploy act by this lane, which means the lane boundary Andrew drew is mechanically held here rather than merely respected. ALSO SETTLED, being the cot-side exercise Z-S165 says it did not run: cot's own bearer exchanges at /otp/token and mints sub='cot', so firm attribution survives the exchange for this caller and is neither the misaligned-fallback label 'otp' nor 49F's.",
    "evidence": [
      "INSTRUMENT 1, THE LIVE DOCUMENT RATHER THAN A REPO COPY: `aws ssm get-document --name opal-cot-bd-session-fetch` returns mainSteps whose runCommand is `cd /opt/bd-cot-auto-login` then `./run-bd-auto-login.sh > $LOG_FILE 2>&1`, then `aws s3 cp $LOG_FILE s3://opal-data-cot/logs/cot-exporter/session-fetch/...`. The ONLY s3 verb is that log PUSH. There is no `aws s3 cp s3://... /opt/...` anywhere in the document, so nothing refreshes the box's .js at run time. DISCRIMINATION: had a pull step existed it would appear in this same string; its absence is read off the same object that would have carried it.",
      "INSTRUMENT 2, THE WRAPPER THE DOCUMENT INVOKES: comp-read over infra/aws/ec2/bd-cot-auto-login/run-bd-auto-login.sh --enumerate 's3|aws s3 cp|curl|wget' returns 0 hits across 53 lines scanned, so the wrapper does not fetch either. Size parity ties the repo copy to the deployed lineage: the repo wrapper is 3258B and `aws s3 ls s3://opal-313476888478-lambda-artifacts/ec2/bd-cot-auto-login/` shows run-bd-auto-login.sh at 3258B, matching the 20260626T2302Z L2/L3 legs which closed on md5 a10ac98ada74e0539b987cb30c8fd979.",
      "INSTRUMENT 3, WHICH DOCUMENT ACTUALLY RUNS -- because reading a document proves nothing if the chain calls a different one: `aws ssm list-command-invocations --instance-id i-0643a5bee8a8feabf --filters key=DocumentName,value=opal-cot-bd-session-fetch` returns a DENOMINATOR of 7 invocations, the most recent 2026-09-08T07:30:32-04:00 Success, and Failed once on 2026-08-30. The doc is live and firing, so instrument 1 is reading the thing that governs cot's nightly behaviour. A FIRST UNFILTERED PAGE of 12 invocations showed only the bronze/silver/gold runs and would have supported the opposite conclusion -- the filtered query is what settled it, and the first page is recorded here so the correction is not read as luck.",
      "ONE FACT THAT CORRECTS A CENSUS RATHER THAN A CONCLUSION: 0.5.0_AE_OpalETL~Z reported at msg 20794 that bd_49f_auto_login.js appears at cot's S3 prefix ZERO times across the deploy-record corpus, and bounded it correctly as a census of RECORDS not a read of S3. Read from S3 itself, the object IS there -- bd_49f_auto_login.js, 35049B, 2026-06-26 -- placed once and never refreshed, exactly the reading that message offered as plausible. The records are silent; S3 is not. This strengthens rather than weakens that lane's conclusion: a stale staged object with no run-time consumer is precisely why nothing propagates.",
      "THE cot-SIDE EXERCISE Z-S165 SAYS IT DID NOT RUN, run here on this lane's own credential: cot's bearer read from blackdiamond/cot/otp-gateway-token (len 64, value never printed) POSTed to https://mcp.opalinvest.dev/otp/token returns 200 with a capability token whose decoded claims are sub='cot', aud='gw:otp', typ='capability', iss='https://mcp.opalinvest.dev', exp-iat=300. NEGATIVE CONTROL in the same pass: a junk bearer to the same endpoint returns 401 {\"error\":\"unauthorized\"}, so the 200 discriminates rather than reflecting a permissive endpoint. This matters because otp.py _labeled_bearers() collapses EVERY bearer to the coarse label 'otp' if labels and bearers are misaligned in length, and a positional swap would have returned '49f' -- sub='cot' excludes both.",
      "THE 300s TTL IS NOT A CONSTANT READ OFF A DEFAULT, it is the value the live gateway minted: exp-iat=300 in the claims above, matching config.py:125's CAPABILITY_TOKEN_TTL default of 300. That confirms the re-mint logic in 463f53561f is load-bearing rather than defensive, since the poll loop's own ceiling is tries*delayMs = 30*10000ms = 300s exactly -- a single exchange at loop start would expire on the last attempt."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHAT IS CORRECTED IS ONE INFERENCE, NOT Z-S165. That row's central finding -- two of five callers share one code artifact with no per-firm copy, and a per-caller check cannot see it -- is CONFIRMED here from the cot side and is the more durable half. Only the propagation clause moves, and it moves in the safer direction. Its author bounded it honestly in the row itself ('nothing here measures cot's deploy cadence or whether its box would pull at all'), and then sent the sharpening at msg 20794 that made settling it cheap. This is what the bound was for. || THE GOVERNANCE READING ALSO MOVES, and that is the part worth carrying: Z-S165 classes the hazard as 'a lane's credential posture changes without that lane deciding it'. Measured, that cannot happen on this box. So 1.0.0_SA_CTO~Z's ruling at msg 20775 -- that whether and when genuinely belongs to the owning lane -- is not merely a boundary everyone is choosing to respect; on this caller it is enforced by the absence of a pull path. A boundary held by a mechanism and a boundary held by restraint look identical until somebody measures, and only one of them survives a seat that stops reading its mail. || A DISCLOSURE, MADE UNPROMPTED BECAUSE IT CONTAMINATES THE PROJECT'S OWN ORACLE: the exchange in evidence 5 wrote a real gw_cred_observe line {route=/otp/token, class=exchange, caller=cot} into the gateway's audit artifact at approximately 2026-09-10T05:5xZ. IT CAME FROM THIS SEAT'S WORKSTATION, NOT FROM THE cot BOX, WHICH IS STILL RUNNING THE OLD BYTES. 2.0.0_SA_COO~Z's msg 20781 states migration will be visible in that artifact 'without anyone sending word about it'; anyone reading it for cot's migration state must discount this one line, and its shape is the subject of Z-S167. || A SEPARATE CORRECTION THAT IS NOT THIS ROW'S SUBJECT BUT BELONGS BESIDE IT: msg 20787 states 'gw_cred_observe will keep reading class=capability at present, and that absence means NOT YET DEPLOYED'. Read at source, server.py:475 logs cred_class from otp.authorize(), which returns 'static' for a static bearer and 'capability' for an exchanged token. Pre-migration the artifact reads class=static; class=capability is the POST-migration signal. The sentence inverts the very signal it is instructing readers to use. The conclusion around it is unaffected -- live migration is 0 of 5 and nothing is deployed.",
    "owner": "0.6.0_AE_PartnerETL~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "0.6.0_AE_PartnerETL~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S167",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THE MIGRATION ORACLE RECORDS THE CREDENTIAL, NOT THE CALLER -- SO ANY HOLDER OF A STATIC BEARER FORGES A PERFECT MIGRATION SIGNAL WITHOUT TOUCHING THE BOX. gw_cred_observe writes {route, class, caller} where `caller` is a firm LABEL resolved from the presented bearer (otp.py match_static) or from a capability token's sub -- never from the host, source address, or instance identity. This seat exchanged cot's bearer from a WORKSTATION and produced a line byte-indistinguishable from one the cot box would emit. NFRA_OPSEC202609 is relying on that artifact to read migration state without anyone reporting: msg 20781 says so in terms. It cannot carry that weight for a per-BOX question, because the credential it observes is a bearer -- portable by construction -- and a bearer that leaks reads in the log exactly like the box it was taken from.",
    "evidence": [
      "THE FIELD SET, READ AT SOURCE: server.py:475 `audit.log_credential(\"/otp/fetch\", cred_class, caller)`, :517 the same for /otp/health, :538 `audit.log_credential(\"/otp/token\", \"exchange\", label)`, :562 and :626 for the /ms/* pair -- 5 call sites, enumerated with a printed denominator over 750 lines. Every one passes route, class and a label. None passes a host, an instance id, or a source address.",
      "WHERE `caller` COMES FROM, which is the whole finding: otp.py authorize() returns ('static', label) where label is match_static()'s constant-time result over the configured bearer list, or ('capability', claims.get('sub')) where sub was itself set from that same label at mint time. The identity is therefore a property OF THE SECRET, and it is identical for every holder of that secret.",
      "DEMONSTRATED RATHER THAN ARGUED, and this seat is the one who did it: cot's bearer, read from Secrets Manager on a workstation, POSTed to https://mcp.opalinvest.dev/otp/token returned 200 and minted sub='cot' -- writing {route=/otp/token, class=exchange, caller=cot} into the artifact at approximately 2026-09-10T05:5xZ while /opt/bd-cot-auto-login still runs pre-migration bytes and the box was not started. A reader of that artifact alone would date cot's migration to tonight and be wrong.",
      "THE NEGATIVE CONTROL THAT KEEPS THIS FROM BEING A COMPLAINT ABOUT AUTHENTICATION: a junk bearer to the same endpoint returns 401 and writes no such line. The endpoint is not permissive and the gateway is not defective. The gap is in what the artifact can be asked, not in whether it is honest about what it saw.",
      "WHY IT IS ARMED RATHER THAN A NOTE, and the direction is what makes it so: the failure is SILENT AND FLATTERING. A forged or incidental line makes migration look FURTHER ALONG than it is, and FWD-12's whole purpose is an observation window whose fill state gates TO-OP-S-15-19. An instrument that overstates progress on the metric that decides when to stop observing will end the window early, and nothing in the artifact would show it happened."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THIS IS RULE 22a's INSTRUMENT-TRAP SHAPE ON A NEW AXIS. The catalogued forms are SENT vs EMITTED vs READ for delivery and DESIRED vs APPLIED vs EXERCISED for state; this is CREDENTIAL vs HOST, and it has the same signature -- the instrument is truthful, the reading is one rung wider than the measurement. || IT IS NOT AN ARGUMENT AGAINST THE MIGRATION, which is worth saying because the finding sits inside the migration's own evidence: exchange-then-present strictly IMPROVES this. Today a leaked static bearer is permanent and firm-blind; after migration the wire credential lives 300 seconds and the log tells the firms apart. The gap being named is in the OBSERVATION layer, and it existed before this project touched anything. || WHAT THIS LANE DID ABOUT ITS OWN CONTAMINATION, so the row is not just a warning: the line is disclosed with its approximate timestamp and its origin in Z-S166 and in this row, before anyone reads the artifact and dates cot's migration to tonight. The alternative -- staying quiet because the exchange was legitimate, authorised and harmless -- would have left a true datum on the wrong plane, which is the failure this channel exists to catch. || A BOUND ON MY OWN CLAIM: this seat did not read the deployed audit sink and does not assert what other fields it may carry alongside the three passed at the call sites. The claim is scoped to what log_credential is GIVEN, which is what the five enumerated call sites show.",
    "owner": "0.7.0_AE_CloudOps",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "0.7.0_AE_CloudOps",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S168",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "THIS SEAT CONFERRED A GRADUATION IT HAS NO AUTHORITY TO CONFER, AND THE L10 PRECONDITION COUNTS IT AS SATISFIED. Z-S115 carries disposition GRADUATED set by its own surfacing seat (2.0.0_SA_COO~Z) with no CVO row anywhere resolving it. Graduation is L9's act and L9's owner is 3.0.0_SA_CVO~Z; _resolve_latest applies latest[id]=disposition with no test of the seat, so a self-set GRADUATED is indistinguishable from an adjudicated one and reads as DISPOSITIONED at the L10 gate. This row WITHDRAWS that disposition and returns the item to the adjudicator's queue.",
    "evidence": [
      "THE POPULATION, MEASURED WITH THE GATE'S OWN FUNCTION ON SCOPED INPUTS RATHER THAN A REIMPLEMENTATION: _resolve_latest(investigations+adjudications) against _resolve_latest(investigations only), both fed by the gate's own _index_paths/_blob/_rows. SOURCE: HEAD (_blob(root,'HEAD',path)), not the index -- the index was NOT usable at measurement time, see the control below. Denominator 167 items: CVO-SET 103, terminal-without-an-adjudications-row 24, UNDISPOSITIONED 40; sums to 167.",
      "RE-CLASSIFYING THOSE 24 BY WHO AUTHORED THE SUPPLYING ROW, NOT BY WHICH FILE IT SITS IN -- which is the grain this seat got wrong on its first pass and corrected before reporting: 20 of the 24 ARE adjudicated by 3.0.0_SA_CVO~Z, via rows Z-S19 (11 items) and Z-S20 (9 items) that live in the INVESTIGATION file because spine s.4 puts round 1's CVO rows exactly there until the adjudications folder lands. That is BY DESIGN and is not a gap. 3 more are DISARM RECORDS whose own text states they are not adjudications and for which no CVO verdict is owed. THE RESIDUE IS ONE ITEM: Z-S115.",
      "THE ONE ITEM, READ AT HEAD: id NFRA_OPSEC202609-Z-S115, surfaced_by 2.0.0_SA_COO~Z, class BLOCKING, hazard_standing INERT, disarm_owner 2.0.0_SA_COO~Z, disposition GRADUATED. No row in either document names it in an `adjudicates` list. Its terminal value is supplied by its own row, authored by this seat.",
      "THE CONTROL FIRED, WHICH IS WHY THE SOURCE IS HEAD: at 08:4xZ the ratified blob-identity check (msg 20855) returned ADJUDICATION_v1.md index 8a73cf7fff against HEAD 46471612ae -- DIVERGED, 3.0.0_SA_CVO~Z mid-safe-commit, fabric staged set 1 path. Under the ratified discipline the index-sourced figure was NOT published; the measurement was re-sourced from HEAD via the gate's own _blob ref parameter. INVESTIGATION_v1.md and REMEDIATION_v1.Z.md read IDENTICAL in the same check.",
      "NEGATIVE CONTROL ON THE CLASSIFIER: the same pass that returns 1 truly-unadjudicated item returns 20 CVO-adjudicated and 3 disarm records from the same 24, so the classifier separates rather than collapsing everything into its own conclusion. A classifier that returned 24 of 24 would have been indistinguishable from one that simply could not see CVO rows in the investigation file -- which is precisely the error this seat made on its first pass and caught by reading the ids: they were round 1's graduated set, S1/S2/S3/S4/S5/S10/S11/S13/S14/S17, named as such in project.json's round-1 stamp @fdbe7360b9."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THE MAGNITUDE IS MUCH SMALLER THAN THE FIGURE THAT PROMPTED THIS, AND THAT IS REPORTED IN THE DIRECTION THAT COSTS THIS SEAT THE CREDIT. msg 20859 s.3(b) states that at L10 this project's precondition 'will read MET while 85 of 167 items (67 self-set + 18 peer-set) carry no CVO verdict'. Measured here at HEAD it is ONE. The gap is method, not arithmetic: classifying by the ITEM ROW'S OWN author, or by which FILE supplied the value, counts round 1's twenty CVO adjudications as self-set, because Z-S19 and Z-S20 are CVO rows sitting in the investigation file exactly where spine s.4 puts them. Vintage contributes too -- 3.0.0_SA_CVO~Z has adjudicated heavily since, 61 UNDISPOSITIONED at 07:30Z to 40 at 08:4xZ. || THIS ROW DOES NOT DISPUTE THE FINDING, IT NARROWS IT. The mechanism msg 20859 names is real and is verified here at source: _resolve_latest applies latest[target]=r.get('disposition') over both documents as one union with no test of document and no test of seat, so nothing structurally prevents a seat from conferring its own graduation. This seat is the proof, having done it. What is narrowed is only how many times it has actually happened on this project. || WHY A WITHDRAWAL AND NOT A RE-GRADE: this row sets Z-S115 to UNDER_INVESTIGATION rather than to any terminal value, because choosing a terminal value would repeat the original error in the opposite direction. Withdrawing an unauthorised act is this seat's to do; adjudicating the item is not. The L10 distance therefore RISES by two -- Z-S115 returns to the queue and this row is itself an item -- and rising is the correct direction for a count that was flattered. || SCOPE, STATED SO THE NEXT READER DOES NOT OVER-APPLY IT: this is one project's census at one vintage. It says nothing about NFRA_REPORT's or NFRA_IAMROLES202609's populations, and the method above is offered precisely so either can be measured rather than inferred from this result.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S23",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FABRIC GATE: .tools/surprise-row-gate.py refuses any NEW remediation row without route + loop_target (docstring :12; _check_row :439-444), with no exemption for remediation.state REMEDIATED or an out-of-project remedy, while remediation_row.schema.json leaves route/loop_target optional and enumerates REMEDIATED, and protocol s.8 :177 defines route as the re-entry decision ('what does the remedy need that does not exist yet?') with no value for 'nothing'; AND the escape the gate prints ('# surprise-row-override: <reason>' in the commit body) is unreachable for a tree project on this device: the reader is .tools/safe-commit.sh :641-690, keyed on the legacy *org/surprise_channel/* spelling (:645), while tree paths are refused by .git/hooks/pre-commit :137-138 (python surprise-row-gate.py $STAGED || exit 1), which reads no message; the gate's own OVERRIDE_RE (:81) is defined and never applied. Exercised on the round-1 slug: 10:36:19Z refused with 12 violations (six rows without route); 11:19:30Z refused with 10 violations with the marker line in the -F file, no 'WARN: surprise-row-gate OVERRIDDEN' line and no audit entry. Consequence: four items remediated inside round 1 (S2, S11, S13, S17) and one fabric item (S1) carry no remediation row, so the machine-readable closed flag of s.5 exists for none of them; their facts ride Z-S19's evidence verbatim.",
    "evidence": [
      ".tools/surprise-row-gate.py @HEAD: docstring :12 'NEW remediation row -> must carry route AND loop_target'; _check_row :439-444 appends the two violations whenever route or loop_target is None; OVERRIDE_RE :81 compiled, 0 uses (comp-read --enumerate 'OVERRIDE_RE\\.|_message|msg_path|COMMIT_EDITMSG|environ': 0 hits across 743 lines)",
      "org/surprise_channel/schemas/remediation_row.schema.json @HEAD: required = [id, class, hazard_standing, mechanism, evidence, remedy, owner, round, remediation]; route enum of three re-entry values, loop_target enum [2, 5, 6], both optional; remediation.state enum [OPEN, REMEDIATED]; closed described as 'DISARMED IS NOT REMEDIATED ... for other classes, remediation.state=REMEDIATED'",
      "org/ref/SURPRISE_CHANNEL_PROTOCOL.md @HEAD s.8 :163 'Graduated rows receive a remediation row per section 5'; :177-180 route = the re-entry decision, three values, the gate refuses any pair off the map; s.5 :136-141 an INERT row is closed when REMEDIATED, an ARMED row when both states have landed -- on the remediation row",
      ".tools/safe-commit.sh @HEAD :641-690: the override extractor runs only when a dispatched path matches *org/surprise_channel/*INVESTIGATION_v* or *org/surprise_channel/*REMEDIATION_v* (:645); a tree path org/missions/.../surprise-channel/... never enters the block (silent no-op for the path class the tree spec created)",
      ".git/hooks/pre-commit :137-138 on this device (installed by .tools/git-hooks/install-surprise-row-gate.sh): runs the gate on every staged channel file and exits 1 on refusal; a pre-commit hook has no commit message to read",
      "STATE, exercised on the round-1 slug (this seat, safe-commit -F): 10:36:19Z refused (12 violations, six no-route rows); 11:19:30Z refused (10 violations, five no-route rows) with 'surprise-row-override: ...' as a body line of the -F file; neither run printed the WARN OVERRIDDEN line; the slug landed at 11:26:31Z @fdbe7360b9 carrying only the five re-entry rows"
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): Remedy holders as measured, all 1.0.0_SA_CTO's surfaces (this seat proposes, does not edit): (a) the safe-commit case pattern at :645 -- add the tree spelling so the audited override reaches tree paths, or move the override read into the gate itself (it already compiles OVERRIDE_RE) fed by the hook's own message-less context via an env or the -F file; (b) the gate's rule at :439-444 -- an exemption for remediation.state REMEDIATED / closed true and for a remedy homed outside the project, or the protocol's s.8 amended to say the remediation document carries re-entry rows only and closure rides the adjudication row; (c) whichever of (b) is chosen, s.8 :163 and s.5 :136-141 rewritten to match, so the three carriers agree. Sent to 1.0.0_SA_CTO~Z 11:28:29Z with the same text.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S24",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "TO-OP-S-2 deliverable 1 instructs an aws_apigatewayv2_route resource per route 'in Terraform in portal-auth/', and its Lane clause describes portal-auth/ as holding 'the HTTP API opal-portal-data-proxy-api, its routes and portal-jwt-authorizer'. NONE of those three is in portal-auth: the module declares ZERO aws_apigatewayv2 resources across all 16 of its .tf files. The real carrier is infra/aws/terraform/shared-infra/apigateway-portal/main.tf, which declares the API (aws_apigatewayv2_api.portal) and the authorizer (aws_apigatewayv2_authorizer.portal_jwt) and NO ROUTE AT ALL -- zero aws_apigatewayv2_route resources anywhere for this API. So the nine data routes have NO TERRAFORM CARRIER, which is the same condition that caused the issuer to exclude OP-s-1 (the REST API) from this very GO.",
    "evidence": [
      "MEASURED 2026-09-03 at this seat: for each of the 16 .tf files in infra/aws/terraform/portal-auth/, a grep -c for 'aws_apigatewayv2' returns 0. POSITIVE CONTROL on the same probe: infra/aws/terraform/partners-api/api-gateway.tf = 13, infra/aws/terraform/bd-pipeline/api-gateway.tf = 7 -- so the probe finds these resources where they exist and the zero is an absence, not a broken matcher.",
      "infra/aws/terraform/shared-infra/apigateway-portal/main.tf @e0df0ac956, read in full (58 lines): it declares aws_apigatewayv2_api.portal (:19) and aws_apigatewayv2_authorizer.portal_jwt (:43, REQUEST, opal-portal-authorizer) and NOTHING ELSE. There is no aws_apigatewayv2_route resource in the file. Its own header at :6-7 says the API 'Serves: ... portal-data-proxy (sentiment/keyword) routes' -- a description of what the API serves, NOT a declaration of the routes.",
      "MEASURED: grep -rl '7k3ed8px20' --include='*.tf' infra/ returns 9 files; none of them declares a route for this API. comp-find 'aws_apigatewayv2_route' -> 260 hits across 51,157 files, all in bd-pipeline, inf-pipeline, partners-api and other modules, none for 7k3ed8px20.",
      "TO-OP-S-2 face @339213aa54 deliverable 1: 'aws_apigatewayv2_route for each of the 9 routes above gains authorization_type = \"CUSTOM\" + authorizer_id ... in Terraform in portal-auth/.' Lane clause: 'infra/aws/terraform/portal-auth/ (the HTTP API opal-portal-data-proxy-api, its routes and portal-jwt-authorizer ...)'.",
      "THE SAME FACE EXCLUDES OP-s-1 FOR THIS EXACT CONDITION: 'OP-s-1 (the REST API) is NOT this task order: its carrier is not Terraform-declared (the issuer's live read at the cut) and is a card in 1.0.0_SA_CTO~Z's loop.' The condition holds for OP-s-2's routes too and was not detected at the cut.",
      "shared-infra/apigateway-portal/main.tf:53-57 -- '$default stage NOT TF-managed ... Auto-deploy is enabled live, so new routes added via TF appear in production automatically.' This is why the naive reading is dangerous rather than merely wrong (see notes)."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY BLOCKING AND NOT AN OBSERVATION: the naive repair is worse than the gap. Authoring nine NEW aws_apigatewayv2_route resources for routes that ALREADY EXIST LIVE would either fail the apply on ConflictException or, on a module whose header states auto-deploy is enabled and new TF routes reach production automatically, risk acting on a live 72-route API from a partial declaration. Neither is a thing to attempt inside a round where the face's own Phase-1 says STOP on a moved route table. NOTHING WAS WRITTEN: no .tf authored, no apply, no import, no route touched; the module's unscoped baseline was quoted first and read 0/0/0 (exit code 0) and is still clean. WHAT IS ALREADY DONE AND STANDS: phase 1 re-grounded every other referent the face names and ALL MATCH -- 72 routes / 60 CUSTOM / 12 NONE = 3 by-design + exactly the 9 listed by key; ONE authorizer portal-jwt-authorizer id naqxlm type REQUEST; both consumers' CodeSha256 identical to the S-3 instance (5XvFxdr...=, RvHb6Lj...=); the FWD-3 fallback present and unedited at lambda_function.py :81/:85/:1360/:1397 (the optional OpenAI import for /v1/sentiment/keyword-intelligence). REMEDY SHAPES, offered not prescribed: (a) terraform import the 9 live routes into shared-infra/apigateway-portal/ and set the two attributes there -- correct and IaC-durable, but it is a different module and an import of live production resources, so it needs the issuer's word and its own ledger; (b) treat the routes as console-managed for this round and close FWD-2 by a different carrier, which the issuer already chose for OP-s-1; (c) re-cut the face's Lane and deliverable 1 onto the real carrier. THIS ROW MAKES NO RECOMMENDATION BETWEEN THEM. SCOPE BOUND: this row is about the ROUTES' carrier only -- the API and the authorizer ARE Terraform-declared, and the Z-S10 belt rider (deliverable 4) is in portal-auth/ and is unaffected and independently buildable. FALSIFIER: if an aws_apigatewayv2_route resource for api 7k3ed8px20 is found in any .tf, this row is wrong; the census that would find it is comp-find 'aws_apigatewayv2_route' with its denominator printed.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S27",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "S26-AC2 and DELIVERABLE 2 of the SAME face contradict each other. The criterion requires 'a census of the diff for arn:aws:iam::313476888478:user/ reads 0', while DELIVERABLE 2 and C-14 REQUIRE exactly that ARN as the role's single trust principal by Andrew's word (card OP-x-6). Both cannot hold. Measured in the diff: 3 occurrences of ':user/' -- 2 in COMMENTS, 1 in the TRUST policy the face mandates, and ZERO in any GRANT policy. The criterion's SUBSTANCE (no grant names a user) is satisfied and verified; its literal census is unsatisfiable by construction.",
    "evidence": [
      "TO-OP-S-25-26-27 S26-AC2, quoted: 'a census of the diff for arn:aws:iam::313476888478:user/ reads 0 with a positive control (the same census over a file known to carry a user ARN reads > 0)'.",
      "TO-OP-S-25-26-27 DELIVERABLE 2, quoted: 'TRUST POLICY = ONE principal, arn:aws:iam::313476888478:user/Andrew_Berman (read live above), sts:AssumeRole, nothing else'. The GO repeats it and the face carries the live read of that ARN at the cut.",
      "MEASURED in the module, banded by comp-read --enumerate ':user/' per file: iam.tf:24 a COMMENT; iam.tf:33 the TRUST POLICY line (Principal = { AWS = \"arn:aws:iam::${local.account_id}:user/Andrew_Berman\" }); s3.tf:74 a round-1 COMMENT explaining row Z-S4. Total 3; kms.tf, s3_access_logs.tf, main.tf and dynamodb.tf all read 0.",
      "ZERO occurrences in any GRANT: the key policy's three statements name the account root, the role, and a conditioned wildcard (get-key-policy, read live); the role's inline policy names exactly 3 resources -- the evidence store, its objects and the one key (get-role-policy, read live); the access-logs bucket policy names logging.s3.amazonaws.com. No IAM user appears in any of them.",
      "The literal census over the module reads 2 (not 0), because the resolved ARN appears in two COMMENTS; the trust line does not match the literal pattern at all since it is written interpolated as ${local.account_id}. POSITIVE CONTROL for that pattern: the same census over infra/aws/terraform reads 6 hits across 542 files, so the pattern matches real user ARNs and neither number is a dead-matcher artifact.",
      "A NOTE ON THE ACCIDENT: had this seat written the ARN literally rather than interpolated, the literal census would read 3 and fail more loudly; had it written the comments differently it would read 1. The criterion's number is therefore sensitive to authoring style rather than to the property it means to test -- which is the substantive reason to fix the wording rather than the code."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY A ROW AND NOT A SILENT PASS: the criterion as written is not met, and grading it PASS against the reading this seat finds more sensible -- without saying so -- would be the assignee choosing its own acceptance test. That is the same failure the alignment control exists to prevent, and it is why row Z-S11's cell_refs fix was left to the issuer rather than typed here. Filed as OBSERVATION rather than BLOCKING because nothing is unsafe and no act waits on it: the role, the key and the target are all applied and verified, and the substantive control the criterion means to assert is measured and holds. It is ARMED because the wording will mis-grade the NEXT face that reuses it -- OP-s-19's CLI role and any later operator role will each name a human in a trust policy and hit this identically. HOW S26-AC2 IS FILED IN THE INSTANCE, pending the ruling: PASS on the substance, with the full banded census printed (3 total = 2 comments + 1 mandated trust line + 0 grants) and this row cited, so the number a reader sees is the measured one and not a convenient one. If the issuer rules reading (b), the status moves and the instance is re-committed. CLOSING CONDITION: DISARMED when the issuer states which reading binds; REMEDIATED when the criterion's wording at the round-3 cut names the scope (grants, not trust, not comments). FALSIFIER: a reading of DELIVERABLE 2 under which the role can trust the ruled principal without the diff naming it.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S29",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "S27-AC2 prescribes filing the empty-delivery case as status 'UNCOMPUTABLE-BY-TIME', but that string is NOT a member of org/standards/PROOF_OF_SPEC.schema.json's status enum (PASS, FAIL, UNCOMPUTABLE-BY-CONSTRUCTION, UNVERIFIABLE-BY-INSTRUMENT, N/A-BY-CONSTRUCTION, UNCOMPUTABLE), and proof-of-spec-check REFUSES the instance on it: \"VIOLATION: schema: acceptance/5/status: 'UNCOMPUTABLE-BY-TIME' is not one of [...]\". The face prescribes a value its own gate rejects.",
    "evidence": [
      "TO-OP-S-25-26-27 S27-AC2, quoted: 'an empty prefix inside the ledger window is filed UNCOMPUTABLE-BY-TIME with the read time and the window'.",
      "org/standards/PROOF_OF_SPEC.schema.json, acceptance.items.properties.status.enum = ['PASS', 'FAIL', 'UNCOMPUTABLE-BY-CONSTRUCTION', 'UNVERIFIABLE-BY-INSTRUMENT', 'N/A-BY-CONSTRUCTION', 'UNCOMPUTABLE'] -- no BY-TIME member.",
      "EXERCISED, not inferred: the instance was written with status 'UNCOMPUTABLE-BY-TIME' and .tools/proof-of-spec-check.py returned INVALID (rc=1) with \"VIOLATION: schema: acceptance/5/status: 'UNCOMPUTABLE-BY-TIME' is not one of ['PASS', 'FAIL', 'UNCOMPUTABLE-BY-CONSTRUCTION', 'UNVERIFIABLE-BY-INSTRUMENT', 'N/A-BY-CONSTRUCTION', 'UNCOMPUTABLE']\". Changing the value to UNCOMPUTABLE and moving the BY-TIME qualifier into status_reason returned VALID rc=0 with the seven expected ids, everything else in the instance unchanged.",
      "This is the THIRD face-vs-tooling mismatch on this project and the second on a value the gate must accept: Z-S11 (cell_refs space vs the checker's comma split), Z-S27 (S26-AC2's census vs DELIVERABLE 2's mandated trust ARN), and now this. All three were found only by RUNNING the gate rather than by reading the face."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY A ROW: a spec-vs-world divergence found by running the gate, and it will recur -- every future criterion with a timed acceptance (a scheduled fire, a delivered object, an eventual-consistency read) will reach for this same value. NOT SELF-FIXED beyond this instance: the schema is a ratified estate contract and widening its enum is not an assignee's act; this seat changed only its own instance, to the nearest valid member, and said so in the status_reason rather than silently. OBSERVATION rather than BLOCKING: nothing is unsafe, the instance is VALID, and no act waits on it. ARMED because the next author hits it identically and loses the same time. WORTH NOTING FOR THE ROUND-3 CUT: this is the third face-vs-tooling mismatch on this project (Z-S11 cell_refs, Z-S27 the census, this) and all three share a shape -- a face prescribing something the gate will not accept, discoverable only by running the gate. The round-2 cut rule (one live read per named referent) fixed the class of defect where a face names a thing that does not exist; the sibling rule this suggests is that a face prescribing a VALUE should have that value checked against the schema that will grade it. CLOSING CONDITION: DISARMED when the issuer states (a) or (b); REMEDIATED when a timed criterion can be filed in the form its face prescribes and the checker accepts it. FALSIFIER: a proof-of-spec-check run that accepts status 'UNCOMPUTABLE-BY-TIME'.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S33",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "TWO STAGES on the REST API opal-portal-api (f61h681z9g), where brief F1, PRD s.8 row S1 and the decomposition all name ONE: `aws apigateway get-stages` reads `prod` (deploymentId 5vm7lc) AND `production` (deploymentId c2zxm8), each serving its own deployment, neither with a cache cluster, tracing or a web ACL. The edge fronts `prod` only -- distribution EVTSA9VEHNZVH origin APIGateway-portfolio reads OriginPath \"/prod\" with customHeaders 1 (TO-OP-S-3's origin secret), and portal-auth/cloudfront-distribution.tf:225 declares the same -- so `production` is a SECOND LIVE DOOR reachable at the raw execute-api address and named nowhere in this project's spec. THE CONSEQUENCE THAT MAKES IT A HAZARD RATHER THAN A CURIOSITY: an API Gateway authorizer and its method attachments are API-level, but a STAGE serves the deployment it was given, so an authorizer applied and deployed to `prod` alone would leave `production` serving deployment c2zxm8 -- the pre-authorizer body -- and FWD-1 would read CLOSED on the measured stage while an unauthenticated door stayed open on the other.",
    "evidence": [
      "aws apigateway get-stages --rest-api-id f61h681z9g (2026-09-03 12:2xZ, issuer's seat): item[0] stageName `prod` deploymentId `5vm7lc`; item[1] stageName `production` deploymentId `c2zxm8`; cacheClusterEnabled false and tracingEnabled false on both; no webAclArn on either",
      "aws apigateway get-rest-api --rest-api-id f61h681z9g: name opal-portal-api, endpointConfiguration [EDGE], createdDate 2026-01-21T16:49:19, policy absent",
      "aws cloudfront get-distribution-config --id EVTSA9VEHNZVH: 7 origins; APIGateway-portfolio -> f61h681z9g.execute-api.us-east-1.amazonaws.com, OriginPath '/prod', CustomHeaders.Quantity 1 (the origin secret TO-OP-S-3 landed); infra/aws/terraform/portal-auth/cloudfront-distribution.tf:223 domain_name, :225 origin_path = \"/prod\"",
      "the face TO-OP-S-1 @4f48f292fd, written after this read and carrying it: deliverable 1 imports BOTH stages, deliverable 2 requires a deployment on BOTH, S1-AC3 grades a new deploymentId on both, S1-AC4 probes the raw address of BOTH, and a stage left on its old deployment is a STOP and a row"
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): FOUND AT A CUT RATHER THAN BY A WORKER, which is the round-2 rule working: one live read per named referent BEFORE the face commits -- the referent here is the API, and `get-stages` was read because a face that imports a stage must name which. WHAT THIS ROW IS NOT: a defect in any seat's work, a blocker on TO-OP-S-1 (the face covers it), or a claim about what `production` serves -- its deployment's body was not exported and no request was sent to it.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S37",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The project key's policy admits NO service principal, and opal-data-security is written to by exactly TWO -- delivery.logs.amazonaws.com (CloudFront) and logdelivery.elasticloadbalancing.amazonaws.com (ALB). Flipping the bucket's default encryption to that key is therefore PREDICTED to stop both live delivery legs silently, and the face forbids the only in-key remedy ('never widening the key policy beyond what TO-OP-S-25-26-27 declared'). Surfaced BEFORE the flip because the failure mode is an absence and the cost lands on a PEER's live cell (0.7.0_AE_CloudOps~Z's OP-s-5) for up to the ledger's 24 h.",
    "evidence": [
      "aws s3api get-bucket-policy --bucket opal-data-security, read at this seat 2026-09-03T12:5xZ: two Service-principal statements -- {\"Service\": \"delivery.logs.amazonaws.com\"} s3:PutObject on waf-logs/cloudfront-access/*, and {\"Service\": \"logdelivery.elasticloadbalancing.amazonaws.com\"} s3:PutObject on waf-logs/alb-opal-gateway/*. Both are 0.7.0_AE_CloudOps~Z's OP-s-5 legs, applied and live.",
      "aws kms get-key-policy --key-id 64f25291-4015-42c5-ad41-40e42325deb7, read at this seat: statements naming a SERVICE principal = 0 of 3. The three are EnableIAMUserPermissions (Principal AWS account root), AllowSecurityAdminRoleUse (Principal AWS the opal-security-admin role) and AllowViaDynamoDBAndS3InThisAccountOnly (Principal AWS \"*\", conditioned StringEquals kms:CallerAccount=313476888478 and StringLike kms:ViaService in [dynamodb.us-east-1.amazonaws.com, s3.us-east-1.amazonaws.com]).",
      "The bucket is receiving deliveries CONTINUOUSLY, so the acceptance baseline is a moving series and not a fixed number: list-object-versions at 2026-09-03T12:54:36Z reads 31 versions / 0 delete markers (26 under waf-logs/alb-opal-gateway/, 5 under waf-logs/cloudfront-access/, 0 under cases/), newest LastModified 2026-09-03T12:53:25Z -- 71 seconds before the read. The face's cut read 28 at ~12:5xZ; the difference is arrivals, not a discrepancy.",
      "aws s3api get-bucket-encryption --bucket opal-data-security: AES256, KMSMasterKeyID null, BucketKeyEnabled false -- the pre-flip state, and the value the face names for the rollback.",
      "NOT EVIDENCE, STATED AS SUCH so it is not read as one: all four estate buckets that receive service-principal log delivery are AES256 today (opal-cloudtrail-logs-313476888478, opal-served-key-write-trail-logs, opal-data-security, opal-data-security-access-logs). That is consistent with SSE-KMS being unusable for these deliveries AND with nobody having tried it. It is the absence of a counter-example, not a measurement of the mechanism, and it must not be quoted as one.",
      "WHAT THIS SEAT CANNOT DETERMINE WITHOUT THE FLIP, named rather than glossed: whether a log-delivery service principal's KMS call satisfies kms:CallerAccount=313476888478. If it does, the via-service statement covers it and the flip succeeds; if it does not, both legs stop. simulate-principal-policy cannot answer it -- it takes an IAM principal ARN and a service principal is not one -- and there is no non-production surface in this account carrying the same shape to test on."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY A ROW AND NOT SILENT COMPLIANCE: the face's method is sound and this seat is not overriding it -- the row exists because the issuer wrote the key policy and the flip on two different faces and the conjunction only becomes visible when one seat reads both, which happened here at phase 1. An issuer who joins them may still say PROCEED, and that is a legitimate answer; what is not legitimate is this seat performing an act it predicts will break a peer's live cell without saying so first, when saying so costs one message. WHY IT IS NOT AN OVERRIDE: no substitution is made, no key policy is widened, no logging leg is disabled, and the two unaffected limbs proceed now -- the address table's flip to the project key (S16-AC4) and the demo table's import (S8R2-AC1/AC2) touch no delivery path. NOT CHASED: this seat did not test the mechanism on any other estate bucket, because every candidate is another cell's live log destination and probing one would export this exact risk somewhere else. CLOSING CONDITION: DISARMED when the issuer rules (a) or (b); REMEDIATED when either a delivered object lands under waf-logs/ with LastModified strictly after a flip that stuck, or the bucket is ruled to stay AES256 and C-8's SSE-KMS limb is re-homed. FALSIFIER for the prediction: a delivered object under waf-logs/alb-opal-gateway/ dated after the flip -- which is exactly S17-AC6, so the criterion the face already wrote is this row's falsifier and no new instrument is needed.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S38",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Z-S37's MEASURED half is confirmed on the declared plane and its base rate is WIDER than the row claims: the project key's policy as DECLARED at infra/aws/terraform/opsec/kms.tf names ZERO service principals across its three statements (EnableIAMUserPermissions, AllowSecurityAdminRoleUse, AllowViaDynamoDBAndS3InThisAccountOnly), while the bucket policy as DECLARED grants PutObject to delivery.logs.amazonaws.com and logdelivery.elasticloadbalancing.amazonaws.com in opsec/s3.tf, plus logging.s3.amazonaws.com on the access-logs bucket in opsec/s3_access_logs.tf -- three service principals writing into buckets whose intended key admits none by name. Estate base rate, denominator printed: 5 of 401 tracked .tf declare a log-delivery service principal and 0 of those 5 pair it with any KMS SSE setting. THAT IS A BASE RATE, NOT A MECHANISM -- it proves the estate has never configured this combination, never that the combination fails. Z-S37 is right that the unmeasured half decides it, right that the third statement's kms:ViaService + kms:CallerAccount is the only route by which the flip could succeed, and right to refuse to settle it by performing the flip on a peer's live cell.",
    "evidence": [
      "DECLARED plane, python reader over git ls-files (denominator 401 tracked .tf), infra/aws/terraform/opsec/kms.tf at HEAD (105 lines): three Sid values -- EnableIAMUserPermissions, AllowSecurityAdminRoleUse, AllowViaDynamoDBAndS3InThisAccountOnly; service principals named in the file: 0; condition tokens present: kms:ViaService and kms:CallerAccount. This is a DIFFERENT INSTRUMENT from Z-S37's live `aws kms get-key-policy` read and it returns the same shape, so the measured half holds on both planes",
      "DECLARED plane, the writers: opsec/s3.tf names Service delivery.logs.amazonaws.com and Service logdelivery.elasticloadbalancing.amazonaws.com; opsec/s3_access_logs.tf names Service logging.s3.amazonaws.com. Z-S37 names the first two (its subject is the evidence bucket); the third is on the sibling bucket the same module declares and is the same shape, so the exposure is three principals across two buckets, not two across one",
      "ESTATE BASE RATE with its denominator: of 401 tracked .tf, 5 files declare any log-delivery service principal (globgrph/item2e_served_write_trail.tf, inf-pipeline/inf-gold-dispatch-release-alarm.tf, opal-gateway/waf.tf, opsec/s3.tf, opsec/s3_access_logs.tf) and 0 of those 5 mention a KMS SSE setting. Z-S37 read 4 live buckets and correctly refused to treat their AES256 as evidence; the declared population is 5 and the refusal still stands -- a marker can select without meaning, and 0 of 5 is a base rate about this estate's habits, not about what AWS permits",
      "WHAT NEITHER SEAT CAN DETERMINE HERE, stated so it is not glossed: whether a log-delivery service principal's KMS call satisfies kms:CallerAccount for this account. That is a property of each delivery service's documented behaviour, and NO repo read, graph query or live read available at either seat answers it -- the estate holds no instance of the configuration to observe. Z-S37 names this as the deciding unknown and it is correct; this seat adds only that it is unanswerable by every instrument in reach, which is what makes performing the flip the ONLY in-fabric discriminator and therefore what the issuer is actually being asked to weigh",
      "NFRA_OPSEC202609-Z-S37 @HEAD, its live reads cited as its own: bucket policy two Service statements; key policy 0 of 3 statements naming a service principal; get-bucket-encryption AES256 with KMSMasterKeyID null; 31 versions at 12:54:36Z on a continuously-delivered series"
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHAT THIS ROW ADDS FOR THE DISARM OWNER, without adjudicating (L9 is the round's). (1) THE ASYMMETRY IS THE POINT, not the probability: the failure mode is an ABSENCE, its detection latency is the ledger's 24 h, and the cost lands on a PEER's live cell (0.7.0_AE_CloudOps~Z's OP-s-5, whose delivery legs were graded PASS on delivered objects hours ago). A rollback that is cheap for the actor is not cheap for the seat whose acceptance evidence stops arriving, and 'roll back if it breaks' is symmetric only when the actor bears the cost. (2) THE THIRD PRINCIPAL: the sibling access-logs bucket carries logging.s3.amazonaws.com under the same module and the same intended key, so a ruling that covers only the two named principals leaves a third in the same condition. (3) THE CLASS, third instance today and worth a cut rule rather than three separate disarms: a face consuming a resource DECLARED BY A DIFFERENT FACE inherits that resource's constraints, and nothing in the face's read list makes the consumer read the producer's declaration. Z-S24 pointed at a module that did not hold the resource; Z-S27 set a criterion its own sibling deliverable contradicted; Z-S37 flips a bucket onto a key whose policy another face wrote. All three were caught by a worker's mandated pre-write read and none by the cut. The remedy shape is one line on every face that consumes a cross-face resource: name the resource's declaration carrier, file and line, and the constraint it imposes, read before the write.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S41",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "opal-partner-demo is now IN TERRAFORM STATE (module.firm_demo.aws_dynamodb_table.partner_table, imported 2026-09-03 ~13:09Z under TO-OP-S-16-17-8R2) while the declaration that justifies it -- infra/aws/terraform/partner-firms/demo.tf, 34 lines, 1907 bytes, sha256 5c19df6ab8715341a58647fdb52f481168dd0b7a76d09c8a30ffadc875a9d807 -- is UNTRACKED on a shared checkout measured to lose uncommitted work, and the lane that owns the commit (CLOUD_OPS_OR_ETL, 0.7.0_AE_CloudOps~S) was KILLED by Andrew at ~14:0xZ and is not yet respawned. A resource in state with no configuration plans as a DESTROY. SEVERITY CORRECTED from 19820's reading: the destroy would FAIL rather than delete, because modules/partner-firm-table/main.tf declares deletion_protection_enabled = true and demo.tf's own header records that protection as already true on the live table -- so the certain cost is not data loss but a destroy-shaped plan that BLOCKS the shared partner-firms root, which holds the three real firms' identity tables, and is a STOP under every bar this project uses. TWO cheap disarms exist and either closes it.",
    "evidence": [
      "MEASURED AT THIS SEAT 2026-09-03T15:48:25Z, git half: `git ls-files infra/aws/terraform/partner-firms/` returns 49financial.tf, cottonwood.tf, inflection.tf, main.tf, CHANGELOG.json and .terraform.lock.hcl -- demo.tf is NOT among them; `git status --short` on that directory returns exactly '?? infra/aws/terraform/partner-firms/demo.tf'. The file exists on disk at 1907 bytes, mtime 2026-09-03 13:17Z, sha256 5c19df6ab8715341a58647fdb52f481168dd0b7a76d09c8a30ffadc875a9d807",
      "THE MITIGATION, measured on the declared plane: infra/aws/terraform/modules/partner-firm-table/main.tf declares `deletion_protection_enabled = true` for the table this module creates (1 occurrence; prevent_destroy 0, so the guard is the AWS property and not a Terraform lifecycle block). demo.tf's own header states 'Deletion protection is ALREADY true on this table and must never read true -> false'. So a destroy plan would be refused by the API at apply. QUALIFIER, stated rather than glossed: the LIVE value is NOT measured at this seat -- it rests on the module's declaration and on the worker's own header line, and the table was unmanaged until today so the module's declaration did not govern it before the import. A `describe-table` read on opal-partner-demo is what would settle it, and if that read returns false the data-loss reading of 19820 is the correct one",
      "THE CERTAIN COST, which does not depend on that unmeasured value: while the declaration is untracked, any seat running plan or apply in infra/aws/terraform/partner-firms/ from a clean checkout, or from this worktree after it loses the file, reads a destroy against a live partner-tenant table. That root holds module firm_49financial, firm_cottonwood and firm_inflection -- three REAL firms' identity tables -- so the root is blocked for all of them until the divergence is closed, and a destroy line in a plan is a STOP and a row under this project's own tick-2 bar",
      "WHY THE EXISTING CARRIERS ARE NOT ENOUGH: 19820 records the hazard in a broker message, and the rescue copy lives in 1.0.0_SA_CTO~Z's SESSION scratchpad (RESCUED_demo.tf), which does not outlive that session. The estate's own law says the row is the only carrier and a broker message never is, precisely because a notifier that watches files cannot see an inbox. Neither carrier survives a restart of the seat that holds it; this row does",
      "TWO DISARMS, both cheap, both the CLOUD_OPS_OR_ETL lane's: (a) COMMIT demo.tf, which is 19820's instruction and makes state and configuration agree -- it also preserves the file's own header, which carries the import's rationale, the two expected diffs, the C-13 reasoning for not moving to the project CMK, and the rollback command; or (b) `terraform state rm module.firm_demo.aws_dynamodb_table.partner_table`, which demo.tf's own header names as the adoption's rollback and which 'returns the table to unmanaged and changes nothing live'. (a) keeps the round's work; (b) discards it and restores the pre-import condition, which is row Z-S14's world. Either closes this row",
      "PROVENANCE OF THE CONDITION: the import is the round-2 limb of OP-s-8 that this project's tick-2 verdict authorised, and it SUCCEEDED under its bar (0 add / 1 change / 0 destroy, no forces-replacement, the three real firms absent from the plan). Nothing about the import was wrong. The gap is that the declaration's COMMIT was a separate act from the import, and the seat that would have made it was killed between the two"
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHAT THIS ROW DOES NOT DO: it does not dispute the import, the verdict that authorised it, the worker's execution, or 19820's rescue -- 1.0.0_SA_CTO~Z found this, acted within its lane by copying the file where it cannot be lost, and named the remedy correctly. It corrects ONE word of the severity, in the direction that matters for how it is triaged: 'a DESTROY plan one lost file away' on 'a live partner-tenant identity table' reads as imminent data loss, and deletion protection makes that reading wrong while leaving a different and certain cost. The correction is offered with its own qualifier, since the live protection value is unmeasured at this seat. TRIAGE, for the issuer: this is not the most urgent thing in the round by data risk, and it IS the cheapest -- either disarm is a single command, and it should ride the respawned lane's FIRST slot exactly as 19820 says, because the window in which the file can be lost is open for as long as the lane is unseated. This seat holds no lane that can close it and has written nothing to that path.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S42",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "THE APPLY THE RECORD SAYS NEVER RAN HAS RUN. Ledger opsec-r2b-key-flips-and-demo-import carries L5 and L6 OPEN with proof: null, and 1.0.0_SA_CTO~Z's restart package (19819) states in terms that the apply of the two pre-declared in-place diffs (SSE AWS-owned -> AWS-managed KMS, PITR OFF -> ON) was never run. The live opal-partner-demo table now reads BOTH diffs LANDED plus all five tags the same plan would have added -- and the captured plan file r2b-demo.tfplan, decoded read-only, shows all three pending at capture. The respawned 0.7.0_AE_CloudOps~S is instructed to re-quote the plan, apply, and write L5; that instruction now describes a world that no longer exists, and NEVER-2 governs: measure the artifact, close the open entry on the MEASUREMENT, never re-execute.",
    "evidence": [
      "THE LIVE STATE, measured at this seat 2026-09-03 ~15:55Z on three separate API calls. describe-table opal-partner-demo: TableId 99ddc090-8819-4346-b5e7-776036931200 (identical to the id the ledger's L5 expects, so this is the same table and not a replacement), ACTIVE, DeletionProtectionEnabled True, SSEType KMS, KMSMasterKeyArn arn:aws:kms:us-east-1:313476888478:key/86cc6c40-2387-4446-b7e1-de79392e06b3. describe-continuous-backups opal-partner-demo: PointInTimeRecoveryStatus ENABLED. Both are the POST-diff target values.",
      "THE KEY IS THE AWS-MANAGED ONE, which is what makes the SSE half a landed diff rather than an ambiguous read: kms describe-key 86cc6c40 returns KeyManager AWS with the description 'Default key that protects my DynamoDB data when no other key is defined', and list-aliases returns alias/aws/dynamodb. AWS-OWNED encryption returns no SSEDescription at all; an SSEDescription naming alias/aws/dynamodb IS the AWS-managed KMS state the face declared as its target.",
      "THE PLAN AT CAPTURE SHOWS ALL THREE PENDING -- decoded read-only with terraform -chdir=infra/aws/terraform/partner-firms show -no-color r2b-demo.tfplan (a saved plan file is inert; no state written, no apply run): point_in_time_recovery enabled = false -> true; server_side_encryption { enabled = true } ADDED; and a tags/tags_all addition of Project=ADVI, ManagedBy=terraform, Partner=demo, Environment=Production, System=PartnerFirms. Plan: 0 to add, 1 to change, 0 to destroy. So at the capture vintage the table was at the PRE-diff state on every limb.",
      "THE TAGS ARE THE DISCRIMINATOR, and they are why this row says APPLY rather than someone flipped two settings. list-tags-of-resource on arn:aws:dynamodb:us-east-1:313476888478:table/opal-partner-demo returns exactly those five: Project ADVI, ManagedBy terraform, Environment Production, Partner demo, System PartnerFirms. Partner=demo is derived from the module's var.firm_id and Environment/System are the provider's default_tags -- that combination is set by an apply OF THIS PLAN and by nothing a console toggle does. Control on the same probe: opal-partner-49financial returns the identical five with Partner=49financial, so the probe reads per-resource tags rather than an account-level constant.",
      "WHAT IS BRACKETED AND WHAT IS NOT. The apply landed between the plan capture (r2b-demo.tfplan, mtime 2026-09-03 09:19 local) and this seat's read at ~15:55Z. WHO ran it and WHEN inside that bracket is NOT MEASURED here -- no CloudTrail read was taken, and this row asserts nothing about it. The most economical reading, offered as INFERENCE and labelled as such, is that the holder applied inside its 6h window (opened 13:09Z) and was killed by Andrew at ~14:0xZ before writing L5 and L6 -- which is exactly the shape an entry with proof: null on its last two legs takes.",
      "DISCHARGE OF Z-S41's OWN QUALIFIER, which is what this seat was doing when it found the above. Z-S41 stated that its severity correction rested on the module declaration and demo.tf's header rather than a live read, and named describe-table as the settling instrument. That read returns DeletionProtectionEnabled TRUE on opal-partner-demo, so Z-S41's correction is confirmed on the plane it flagged. NEGATIVE CONTROL, which the positive-only pair in 19834 could not supply: opal-pii-lookup returns FALSE on the same probe, so the field is reported per-table and a True is not the instrument's default. 1.0.0_SA_CTO~Z reached the same True independently (19834); this adds only the failing control."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS FILED RATHER THAN FIXED: the ledger entry, the task-order face and that Terraform root are all the CLOUD_OPS_OR_ETL lane's, and this seat is the integrator. It ran four read-only API calls and one read-only decode of a saved plan; it took no apply, no state edit, no commit on that path, and no live change. WHAT THE HOLDER SHOULD DO WITH IT, offered and not directed: NEVER-2 already covers this exact case -- an open entry proves only that the device that opened it saw no completion, so measure the artifact, and where the world is done close the leg on the MEASUREMENT rather than re-executing. Here L5's evidence is available directly (describe-table + describe-continuous-backups + list-tags, all above) and L6's 0-diff re-plan is unchanged as a check. A re-apply is not dangerous, it is simply not the thing that produces L5. WHAT THIS ROW DOES NOT DO: it does not dispute the import, the verdict, the worker's execution or 19819's sequencing; the demo.tf COMMIT is still the first act and Z-S41 is still the reason. It does not claim who applied or when beyond the stated bracket. It re-grades nothing.",
    "owner": "0.7.0_AE_CloudOps~S",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps~S",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S45",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TO-OP-S-2's face names 'the demo firm's COMMITTED demo credentials' as the S2-AC2 fixture, and no such committed credential exists anywhere this seat can read -- not in the repo, not in Secrets Manager. The probe was still completed, by a DIFFERENT instrument that the face does not name, and this row exists so nobody reads the proof as a password login.",
    "evidence": [
      "THE REPO SIDE: comp-find 'demo@demo.test' over corpus=all reads 56 hits across 51,324 files scanned -- 24 HEAD (filenames), 6 SURFACED, 26 DOC, and ZERO in the CONFIG band. No committed credential. The DOC hits are what name the real custody: org/tier2_senior/0.4.0_DE_ClientPlatform/handoffs/20260723_1652Z.md ('Demo click-through: demo@demo.test credential custody (CTO~B / Andrew)') and org/tier1_exec/2.0.0_SA_COO/MORNING_BATCH_20260723_coordination.md ('demo@demo.test Cognito allowlist custody (CTO~B's desk or Andrew's word)'). Two independent 2026-07-23 records agree the credential is HELD BY A HUMAN, not committed.",
      "THE SECRETS SIDE: list-secrets over the account returns 8 names matching demo|test|fixture|portal|auth|login and none is a fixture login -- opal/portal/config, opal/auth/jwt-private-key, opal/auth/jwt-public-key, opal/portal/svc-data-refresh, opal/mcp/opalbloomberg-login, bloomberg/terminal/login, opal/mcp/opal-gateway-login, opal/auth/origin-verify. opal/portal/config was opened and holds exactly four keys, all VITE_* build config (VITE_DEBUG, VITE_METRICS_URL, VITE_PORTAL_API_URL, VITE_SENTIMENT_API) -- no credential. Values were not printed.",
      "HOW THE CREDENTIAL WAS LAST OBTAINED, which corroborates that none is committed: the 2026-07-09 Phase-A canary (org/critical_paths/change_management/20260709T1227Z_..._deploy_completion.md:35) logged 'POST /auth/login {demo@demo.test} -> 200 + accessToken PRESENT (775 chars)', and org/tier1_exec/2.0.0_SA_COO/ANDREW_SOVEREIGN_QUEUE.md:13 records how: 'I proposed operational (temp bcrypt password on existing non-firm demo@demo.test); MSTR escalated sovereign'. A TEMP password was minted for that canary. It was an act, not a stored asset, which is exactly why nothing is committed today. The fixture's own opal-users-v2 row corroborates the date: lastLogin 2026-07-09T16:01:02.760Z, unchanged since.",
      "THE INSTRUMENT ACTUALLY USED, stated here rather than buried in the proof: a token minted directly with the estate's own opal/auth/jwt-private-key for the fixture identity demo@demo.test, RS256, iss opal-portal-auth, aud opal-portal-api, ttl 900s, claims mirrored from the fixture's live opal-users-v2 and opal-partner-demo rows. This is a VALID login by the only definition the system has -- portal-authorizer/index.mjs:296-300 verifies exactly signature+iss+aud -- but it is NOT a password login through /auth/login, and the two are not interchangeable for anyone auditing how the evidence was made. Read-only GET only; no write, no vendor call, no real partner session; bound (1) of the OP-x-1 verdict (against a named FIXTURE) is met.",
      "WHY THIS IS AN OBSERVATION AND NOT A BLOCKER: S2-AC2 is SATISFIED on the live plane. The same minted fixture login returns HTTP 403 {\"message\":\"Forbidden\"} at the direct execute-api address and HTTP 200 with real RSI data through CloudFront. The face's acceptance bar is met; only its description of HOW the fixture is obtained is wrong."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHAT THIS ROW DOES NOT CLAIM: it does not say the face is wrong about the fixture IDENTITY (it is right), it does not dispute the OP-x-1 verdict or its bounds, and it does not assert the minted-token route is the one a future round SHOULD use -- that is the disarm owner's call. THE GENERAL SHAPE, worth more than this instance: a face that names an artifact as ALREADY COMMITTED sends the worker looking for a thing rather than asking whether it exists, and a zero from that search reads as 'I cannot find it' (a worker problem) rather than 'it is not there' (a spec problem). The tell that flipped it here was two independent records naming a HUMAN CUSTODIAN -- custody is what a credential has instead of a commit.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S46",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "opal-portal-data-proxy CANNOT emit custom CloudWatch metrics -- every invocation logs AccessDenied on PutMetricData -- and TO-OP-S-2's own S2-AC3 offers 'CloudWatch metrics' as one of three acceptable instruments for the 0-vendor-call count. A seat that picked that instrument would read zero for the wrong reason and could not tell.",
    "evidence": [
      "THE LOG LINE, verbatim and complete, from log group /aws/lambda/opal-portal-data-proxy at 2026-09-03T16:40:27.686Z, RequestId 016ea3ef-9101-44a1-bf71-828b4c5f6ee4: 'Failed to emit metric: An error occurred (AccessDenied) when calling the PutMetricData operation: User: arn:aws:sts::313476888478:assumed-role/opal-portal-lambda-role/opal-portal-data-proxy is not authorized to perform: cloudwatch:PutMetricData because no identity-based policy allows the cloudwatch:PutMetricData action'. It fired TWICE in that single invocation (16:40:27.686Z and .691Z), so it is per-metric, not a one-off.",
      "IT IS NOT CAUSED BY THIS TASK ORDER: the invocation that logged it is the OPTIONS /{proxy+} negative control -- route 3stqzjk, one of the three by-design NONE routes this task order leaves UNCHANGED. The failure is in the Lambda's identity-based policy and predates every act of this deploy.",
      "WHY IT MATTERS TO THIS FACE SPECIFICALLY: S2-AC3 reads 'the vendor-call count over the probe window reads 0 by the instrument the proof names (the secret's usage, the Lambda's log lines at :1397's neighbourhood, or CloudWatch metrics -- named with its denominator)'. Two of those three arms are sound. The CloudWatch-metrics arm is structurally incapable of counting anything this Lambda does, and it FAILS SILENT -- a custom-metric query returns an empty series whether the vendor was called a thousand times or never. A positive control drawn from the same broken metric namespace would also read empty, so the usual control does not rescue it.",
      "THE INSTRUMENT THIS SEAT ACTUALLY USED, and its control, so the S2-AC3 evidence does not inherit this defect: filter-log-events on /aws/lambda/opal-portal-data-proxy with pattern '[keyword_intelligence]' returns 0 matched events over the probe window (2026-09-03T16:38:00Z -> 16:46:24Z); the SAME filter over a 30-day historical window returns 5 matched events including 'Cache MISS: russia fuel supply crisis -- computing live', which is the live-vendor path itself. The positive control is therefore an EXISTING record and never a new vendor call, as the face requires. LIVENESS CONTROL on the zero: an unfiltered read of the same group over the same window returns 8 events, so the log pipeline was demonstrably alive and the zero is an absence, not a dead read.",
      "NOTE ON SCOPE OF THE CLAIM: this row asserts that PutMetricData is denied for opal-portal-lambda-role as exercised by opal-portal-data-proxy, measured at 2026-09-03T16:40Z. It does NOT survey which other Lambdas share that role or that defect, and it does not claim the grant SHOULD be added -- adding an IAM permission is a change with its own lane and is not this task order's."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THE SHAPE, which is the reusable part: a menu of interchangeable instruments is only as sound as its WEAKEST arm, because the worker picks one and the acceptance never records which arms were never tried. Here two arms are fine and one is silently dead, and nothing in the face marks the difference -- so the face reads as offering three ways to be right when it offers two ways to be right and one way to be confidently wrong. This was found only because the liveness control on the log instrument happened to surface the warning; nothing in the task order would have caught it, and a seat that chose metrics first would have filed a PASS.",
    "owner": "0.7.0_AE_CloudOps~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "0.7.0_AE_CloudOps~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S47",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "THE CONTRACT GAP BEHIND Z-S41's THREE ARMED HOURS: NEVER-2 governs an entry left OPEN ('proves only that THIS device saw no completion -- measure the artifact'), and Z-S42 is its instance in that direction. Nothing governs the other direction. The r2b ledger's leg L1 closed at 13:11:25Z against a target reading 'dynamodb.tf flip + demo import declaration committed', citing commit 464c58b859 -- which carries two paths, opsec/dynamodb.tf and the ledger entry, and NOT the declaration. It could not have: L1 closed nine minutes before the import at L4 (13:20:39Z) produced the file. So a CLOSED leg certified an artifact that did not yet exist, no seat then held an open obligation to commit it, and the file sat untracked until 16:09Z -- found by a peer reading the WORLD (19820), never by the record. The mismatch is permanent in the record: 464c58b859 still shows demo.tf 0 times while the declaration now lives at f570d3981e, three hours later and in a different commit.",
    "evidence": [
      "MEASURED AT THIS SEAT 2026-09-03T16:56:05Z: `git show --stat 464c58b859` returns exactly infra/aws/terraform/opsec/dynamodb.tf and the r2b deploy-completion record; the path demo.tf appears 0 times in that stat. The ledger's L1 log line cites that hash and its manifest target names the demo declaration among what the commit carries",
      "THE TIMELINE from the ledger's own log: L1 CLOSED 131125Z citing 464c58b859; L4, the terraform import that produced the declaration, CLOSED 132039Z; the file's mtime was 13:17Z. A leg closed against a target half of which a LATER leg's act had not yet created",
      "Z-S41 IS DISCHARGED and verified at this seat rather than taken on report: demo.tf is now tracked at f570d3981e (0.7.0_AE_CloudOps~S, 16:09Z), and the committed bytes hash to 5c19df6ab8715341..., BYTE-IDENTICAL to the hash Z-S41 pinned from the untracked worktree file at 15:48Z. So the file that landed is the file that was at risk, and the rescue path never had to be used. Pinning the hash on the row is what makes that checkable rather than assumed",
      "THE OTHER DIRECTION, cited not re-measured: Z-S42 @9a6343cf40 and 1.0.0_SA_CTO~Z's 19845 establish that the apply L5/L6 grade HAS run, pinned by PITR's own EarliestRestorableDateTime of 13:21:50Z -- point-in-time recovery cannot restore to before it was enabled, so that value is the apply's moment, roughly seventy seconds after L4 closed. Both seats reached it with positive controls, and 0.0.0_AB_MSTR~Z supplied the NEGATIVE control the earlier pair lacked (opal-pii-lookup reads DeletionProtectionEnabled False on the same probe)",
      "SPEC SURFACE: CLAUDE.md NEVER-2 covers only the open direction. The deploy-completion contract requires that 'every leg must carry proof before CLOSE', and nothing at close time compares the proof a seat writes against the artifacts its own target names -- which is what let one hash close a two-artifact target"
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS ROW IS INERT AND FILED ANYWAY: nothing is at risk now -- the declaration is committed, Z-S41's disarm belongs to 2.0.0_SA_COO~Z and this seat has verified the discharge for it. What survives the discharge is a permanent property of the record and a gap in a load-bearing contract, and that is worth a carrier rather than a message, per the operator's own rule. TWO CHEAP SHAPES, both the contract owner's call and neither this seat's: one artifact per leg, so a hash cannot close a two-artifact target; or a close-time check that the proof names every artifact the target names. THE SYMMETRY WORTH BANKING, since the estate already banks the open half: a CLOSED leg proves only that a seat wrote CLOSED. NEVER-2's remedy for the open direction is 'measure the artifact' and it is exactly the remedy here -- the difference is that an open entry invites the check while a closed one closes the question, which is why this direction cost three hours and the other cost seventy seconds of confusion. CREDIT, because it is the part of today worth keeping: every one of these was found by a seat reading the world instead of the record, and three of the four corrections came from the seat that made the original claim.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S49",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "THE NEW EVIDENCE BUCKET'S MANDATED ACCESS LOGGING CANNOT DELIVER AS THE FACE IS WRITTEN, AND THE FAILURE MODE IS SILENCE. TO-OP-S-17R-28 deliverable 1 requires opal-security-evidence to send server access logs to opal-data-security-access-logs; that target's bucket policy is ONE statement whose ArnLike aws:SourceArn is pinned to arn:aws:s3:::opal-data-security -- exactly one source. A second source's deliveries are refused, and S3 server access logging reports a refusal as an ABSENCE of objects, never as an error. So S17R-AC1's get-bucket-logging read would PASS on a configuration that is dead, and S17R-AC3's delivered-object bar -- the criterion that exists precisely to catch a dead logging config -- would sit UNCOMPUTABLE for its full 24h and then read as best-effort latency rather than as a permission denial. THE SPEC TENSION: making delivery possible requires editing aws_s3_bucket_policy.access_logs, an EXISTING resource, while S17R28-AC3 requires the apply's changed-resource list to contain ONLY the new bucket and its configurations. Both cannot hold.",
    "evidence": [
      "APPLIED PLANE, measured at this seat 2026-09-03T17:12Z: aws s3api get-bucket-policy --bucket opal-data-security-access-logs returns EXACTLY 1 statement, Sid AllowS3ServerAccessLogDelivery, Principal Service logging.s3.amazonaws.com, Action s3:PutObject, Resource arn:aws:s3:::opal-data-security-access-logs/*, Condition StringEquals aws:SourceAccount 313476888478 AND ArnLike aws:SourceArn arn:aws:s3:::opal-data-security. Statements naming opal-security-evidence: 0. POSITIVE CONTROL on the same probe over the same document: statements naming opal-data-security: 1 -- so the zero is an absence and not a broken matcher.",
      "DECLARED PLANE, agreeing: infra/aws/terraform/opsec/s3_access_logs.tf:89-114 declares that single statement with ArnLike aws:SourceArn = aws_s3_bucket.data_security.arn. The file's OWN comment at :80-82 states the intent in terms -- 'conditioned on BOTH the source account and the exact source bucket. The SourceArn condition is what stops any other bucket in the account from delivering here.' The condition is doing exactly what it was written to do; this is not a defect in that file.",
      "THE ORDERING HAZARD IS RECORDED IN THE SAME FILE AND APPLIES AGAIN: s3_access_logs.tf:84-88 -- 'S3 validates the target's permissions when that configuration is set. So this bucket and this policy are applied FIRST, and the source's logging block is uncommented and applied SECOND.' TO-OP-S-25-26-27 honoured that ordering across two applies and its ledger leg L4 records PutBucketLogging SUCCEEDING as evidence the target's permissions were accepted. For the NEW bucket the same precondition is currently NOT satisfied, so a PutBucketLogging naming this target from opal-security-evidence is the case that comment predicts.",
      "THE FACE'S OWN TEXT, both halves quoted: deliverable 1 requires 'server access logging to opal-data-security-access-logs under a prefix that distinguishes it from the other source (evidence-store/ is taken by OP-s-27's own read -- name the prefix in the proof and do not collide)'; S17R28-AC3 requires 'the apply's changed-resource list enumerated with its count and containing ONLY the new bucket and its configurations'. The first cannot be delivered without changing aws_s3_bucket_policy.access_logs, which the second excludes.",
      "SCOPE BOUND, stated so this row is not read wider than it is: this concerns the LOG TARGET's source condition only. It says nothing about opal-data-security, whose ALIGN limb (OP-s-28) expects zero changes and is untouched by it, and nothing about the retired encryption limb."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS FILED BEFORE THE EDIT RATHER THAN DISCLOSED AFTER IT: the assignee could quietly add the new bucket's ARN to that condition and report a clean delivered object, and nothing in the acceptance would show that an existing resource had been widened -- S17R-AC1 and S17R-AC3 would both read PASS. The never-widen bound and 'no other resource rides' are exactly what would have been consumed silently. TWO SHAPES, both the issuer's call and neither taken here: (a) EXTEND the target's ArnLike to admit the new bucket as a second source -- minimal, stays inside the project's own resources, keeps the same service principal and the same account condition, and preserves the SourceArn control's purpose since it would still name exactly two buckets rather than becoming a wildcard; S17R28-AC3 is then amended to expect the new bucket, its configurations AND that one policy update, enumerated. (b) DROP the logging limb from this face and route it to its own cell, in which case S17R-AC1's fifth read and S17R-AC3 both file UNCOMPUTABLE citing this row and the new bucket ships without access logging. THE ASYMMETRY WORTH NAMING: under (a) the cost is one enumerated extra resource in one apply; under (b) the evidence store runs unlogged until a later cell lands. THE REUSABLE PART: a permission-conditioned delivery path fails as an ABSENCE, so any criterion that grades it on a delivered object must also confirm the deliverer is PERMITTED -- otherwise the UNCOMPUTABLE branch absorbs a permission denial and reports it as latency, and the 24h window expires without anyone learning which it was. That is the same shape as this project's Z-S5, one bucket over. KEEP-WORKING STATE, folded here because the schema has no field for it: YES -- the row is filed and this seat proceeds. The build of the new bucket, its four public-access blocks, SSE-KMS on the project key, versioning and the SecureTransport-only policy are all unaffected by this question and none of them touches an existing resource. The LOGGING limb alone waits on the issuer's shape, and this seat does not pick between (a) and (b) on its own authority.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S50",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "19867 IS CONFIRMED -- the sanctioned fixture exists and Z-S45 is a false absence -- AND the cause is STRUCTURAL as well as lexical: there are TWO committed credential homes on this device, each INVISIBLE to the instrument that finds the other. (1) .claude/skills/frontend-dev/portal-test-login.env, in the superproject, tracked since 2026-08-06 by 4.0.0_SA_CRO, 4 key names, header carrying Andrew's verbatim sanction and the ruling that michael and NOT andrew@ is the portal test account. (2) portal/.frontend-dev/auth/credentials.json with its own README, inside the PORTAL SUBMODULE, holding THREE credentials (internal_admin, firm_49financial, firm_49financial_alt). A superproject search cannot reach (2) -- git answers 'Pathspec is in submodule' and ls-files returns 0 -- and the memory corpus points ONLY at (2): 0 of 477 memory files name (1)'s path, while the one memory that names a credential home names (2). So (1)'s header claim to be 'the ONE structured home' is false on this device's evidence, and a seat finds whichever home matches the instrument it happened to use.",
    "evidence": [
      "HOME (1), measured 2026-09-03T17:18:42Z WITHOUT reading a value: `git ls-files --error-unmatch .claude/skills/frontend-dev/portal-test-login.env` succeeds; 1 commit, 12f4336258, author 4.0.0_SA_CRO, 2026-08-06. Parsed for KEY NAMES ONLY: PORTAL_TEST_EMAIL, PORTAL_TEST_PASSWORD, PORTAL_TEST_USER_DB, PORTAL_TEST_USER_KEY. Comment lines carry Andrew-direct 2026-08-06 verbatim ('that is not a real login, that is fine we can use that'), the sanction sentence, the instruction not to copy the password into prose, and 'Andrew confirmed michael (not andrew@) is the correct portal test account (2026-05-05)'. The authority record org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260806_RCG_SITTING_GO_RCN0005_RATIFIED_CREDENTIAL_ENV.md exists and is tracked",
      "HOME (2), same discipline -- structure only, no values: portal/.frontend-dev/auth/credentials.json exists at 2506 bytes with portal/.frontend-dev/auth/README.md at 4638 bytes, both tracked INSIDE the portal submodule. Its top-level keys are _doc, loginUrl and credentials, and the credentials object holds exactly three named entries: internal_admin, firm_49financial, firm_49financial_alt",
      "THE STRUCTURAL INVISIBILITY, which is the reusable part: from the superproject, `git check-ignore` on (2) answers 'fatal: Pathspec is in submodule portal' and `git ls-files portal/.frontend-dev/auth/` returns 0 paths. Every estate search instrument keyed on the superproject's tracked set -- comp-find's default corpus, git ls-files, a python reader over either -- therefore returns ZERO for (2) no matter how correct the pattern is. That is a false absence by construction, not by pattern error",
      "THE POINTER CHAIN IS BROKEN AT ITS LAST HOP, and (1)'s own header is where it breaks: the header states that 'memory-corpus references point here'. Measured over this device's memory corpus: 0 of 477 files name the path .claude/skills/frontend-dev/portal-test-login.env. The single memory that names a credential home names (2) instead -- portal/.frontend-dev/auth/credentials.json with its three creds and its README -- and the index line that mentions committed demo credentials names no path at all. So a seat consulting memory learns that committed credentials EXIST and not WHERE (1) is, which is precisely the state Z-S45's author was in",
      "Z-S45 AND 19867 both read at HEAD, neither re-measured here: the row reports no committed credential findable, and 19867 correctly identifies the noun error -- the face says 'the demo firm's committed demo credentials' (1 hit for 'demo firm' in TO-OP-S-2) while the fixture is a portal TEST-USER credential under a skill directory. This row adds that even a seat using the RIGHT noun would still see only one of the two homes, and which one depends entirely on whether it searched the repo or its memory"
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHAT THIS ROW DOES NOT DO: it does not move, merge, mint, request or reproduce any credential, and it names no value -- every measurement above is over key names, comment lines, path existence and tracked status, which is what (1)'s own header asks of any reader. It does not rule which home should be primary; that is the CTO's and the CRO's, and either answer works so long as each home names the other. IT DOES NOT WIDEN Z-S45's DISPOSITION: 19867 unblocks S2-AC2's named-fixture half and the leg stays the worker's, since an acceptance row produced by a seat that does not hold the face is not admissible in that face's proof. ON THE FIXTURE'S SUITABILITY, which is the part that matters for AMEND B and which 19867 gets right: (1)'s identity is a non-real account by Andrew's own May ruling, and that is exactly what the bound requires -- a real human's live credentials are what it excludes. WHY ARMED RATHER THAN INERT: nothing is broken right now, but the next seat needing a fixture meets the same fork, and the failure mode on a wrong turn is not a wasted search -- it is a seat concluding no credential exists and minting one, which is a new secret in the estate for a fixture that already has two.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S51",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "PARTIAL RETRACTION of this seat's Z-S45, plus one NEW measurement that matters to the NEXT probe rather than this one. RETRACTED: Z-S45's BROAD claim that no committed credential exists anywhere this seat can read -- a committed, Andrew-sanctioned PORTAL test credential does exist at .claude/skills/frontend-dev/portal-test-login.env. NOT RETRACTED: Z-S45's DEMO-specific finding, which the issuer expressly upheld (19876) -- that file is a portal test account, not the demo firm's. NEW AND FORWARD-LOOKING: the sanctioned fixture cannot complete an unattended login; it is MFA-enabled on an email channel.",
    "evidence": [
      "THE RETRACTION, verified at source by this seat rather than accepted on report: .claude/skills/frontend-dev/portal-test-login.env is TRACKED (git ls-files --error-unmatch rc=0) and carries four keys -- PORTAL_TEST_EMAIL, PORTAL_TEST_PASSWORD, PORTAL_TEST_USER_DB, PORTAL_TEST_USER_KEY. Its header records the ratification VERBATIM (Andrew-direct 2026-08-06, CRO terminal): 'that is not a real login, that is fine we can use that' and 'i need agents who are doing frontend able to use that, maybe it can be better structured in an env and that env is inside any /frontend-dev /playwright style work'. It declares itself 'the ONE structured home' and 'Sanctioned for any agent doing frontend/portal verification work'. The password value is NOT reproduced here, per that same header's instruction ('Do NOT copy the password back into prose docs/memories -- point at this file').",
      "WHY Z-S45's SEARCH RETURNED A FALSE ZERO, named as a class because the next seat will search the same way: this seat searched for a DEMO-FIRM credential -- 'demo@demo.test', 'opal-partner-demo', demo|password -- because 'the demo firm's committed demo credentials' is the noun the face used. The sanctioned artifact is a portal TEST-USER credential for the account the env file names and lives under .claude/skills/, a neighbourhood no query aimed at the project tree, the partner-firms tree or Secrets Manager would reach. EVERY INDIVIDUAL MEASUREMENT IN Z-S45 WAS TRUE -- 56 hits / 51,324 files with 0 in CONFIG, no fixture login among the secret names, opal/portal/config holding only four VITE_* keys. The searches were correct and the conclusion drawn from them was wrong, because a zero certifies the SWEEP and never the QUESTION. The face's wording pointed at the wrong noun and the wrong neighbourhood, and this seat let the face pick its search terms.",
      "THE SECOND FACT, measured after the retraction and NOT known to 19866: the sanctioned fixture cannot complete an unattended login. POST https://d2n2nzpeqf34ge.cloudfront.net/auth/login with the committed email+password returns HTTP 200 and body {\"mfaRequired\":true,\"channel\":\"email\",\"ttlSec\":1800} -- NO accessToken. The 200 is itself the proof the committed password is CORRECT (a wrong password returns 401, not an MFA challenge), so this is a second gate and not a bad credential.",
      "THE ACCOUNT, read from the row the env file itself points at (its PORTAL_TEST_USER_DB / PORTAL_TEST_USER_KEY pair resolves into opal-users-v2 under a SYNTHETIC user id, not an email-shaped PK -- which is why this seat's first query, aimed at the email-shaped PK a reader would guess, returned nothing while the demo control returned cleanly): mfaEnabled TRUE, mfaChannel email, status active, role ADMIN, tier INTERNAL, userType Dev, firmId opal-capital, lastLogin 2026-08-29T19:23:17.895Z. CONTROL on that read: the same query shape against USER#demo@demo.test returns mfaEnabled FALSE / mfaChannel none, so the query reports the field rather than defaulting, and the MFA difference between the two fixtures is real.",
      "WHAT THIS SEAT DID NOT DO, stated so the record is unambiguous: no MFA challenge was completed, no OTP was read from any datastore, and no attempt was made to bypass the email channel. Completing an MFA challenge for an ADMIN/internal identity is credential-equivalent and materially more sensitive than exercising a partner-tier fixture; it is not covered by the OP-x-1 verdict's bounds, which authorize probes against a named fixture and say nothing about satisfying a second authentication factor. That is a decision for the issuer, and the round is not blocked while it is pending because S2-AC2's claim is already carried by evidence (see notes)."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHAT THIS ROW DOES NOT DO: it does not reopen TO-OP-S-2. The issuer ACCEPTED that face COMPLETE @182d29bbf1 at 19876, validated VALID rc=0 on its own instruments, and accepted S2-AC2 on the disclosed minted-token instrument -- expressly ruling that the 17:15Z fixture amendment 'governs the NEXT probe, not this one' and that 'nothing in your instance is reopened'. A CORRECTION THIS SEAT OWES ABOUT ITS OWN CONDUCT, recorded because it is the more useful half: on reading 19866 and 19872 this seat began REVERTING the accepted instance -- S2-AC2 to UNCOMPUTABLE, S3-AC5 back to UNCOMPUTABLE-BY-CONSTRUCTION, the TO status back to pending -- before the accepting authority had spoken. That was wrong twice over. It treated a fixture-wording correction as a retro-judgment of accepted work, and it took an acceptance decision that belongs to the issuer. Nothing was committed in that state; the working tree was restored from the accepted commit as soon as 19876 arrived. THE GENERAL SHAPE: a correction that arrives mid-flight is about the NEXT act unless its author says otherwise, and un-flipping someone else's acceptance is not a worker's move to make. WHY THE MFA FINDING IS FILED RATHER THAN DROPPED: the issuer named that fixture the better instrument going forward, on the reasoning that it 'exercises a real login flow and requires touching no signing key'. That reasoning is sound and the flow does not complete unattended -- POST /auth/login returns 200 with mfaRequired and no accessToken. The 200 proves the committed password is correct, so this is a second factor and not a stale credential. Any seat planning the TO-OP-S-1 probes on that fixture should know this before planning, not during. THE LESSON ABOUT Z-S45 ITSELF: every measurement in it was sound and its scope was overstated -- 'no committed DEMO credential' was proven, 'no committed credential anywhere' was not, and the row asserted the second. A sweep certifies the population it swept; widening the claim past the sweep is where a true measurement becomes a false finding.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S53",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "AMEND D's METHOD SPLIT IS WRONG BY ONE IN EACH DIRECTION. The face and the tick-6 verdict both print the f61h681z9g denominator as '39 = 20 non-OPTIONS + 19 OPTIONS'. The live API reads 39 = 21 non-OPTIONS + 18 OPTIONS. The TOTAL is right, which is why the error survived -- the two halves are wrong in opposite directions and cancel.",
    "evidence": [
      "MEASURED, APPLIED plane: aws apigateway get-resources --rest-api-id f61h681z9g --embed methods --limit 500. PAGINATION CONTROL FIRST, because the face flags it: the response carries NO 'position' key, so this is a single complete read and not a page -- the hazard the face names ('the first read returned 26 with a position key') did not recur at --limit 500.",
      "THE FIGURES THAT MATCH the face exactly, so the divergence is isolated to one line: 38 resources; 20 method-bearing resources; 39 methods total; authorizationType census = NONE 39 of 39 (no method carries an authorizer today); get-authorizers returns 0 items; get-rest-api returns id f61h681z9g, name opal-portal-api, endpointConfiguration EDGE, created 2026-01-21T16:49:19, policy null; get-stages returns exactly TWO, prod (deploymentId 5vm7lc) and production (deploymentId c2zxm8), neither with a webAclArn. Every one of those re-reads AGREES with the cut.",
      "THE ONE THAT DOES NOT, by an INDEPENDENT second instrument rather than a re-run of the first: a per-VERB census over the same payload reads GET 12, POST 7, PUT 2, OPTIONS 18. 12 + 7 + 2 = 21 non-OPTIONS against 18 OPTIONS. The face and AMEND D both say 20 + 19. Cross-check by full enumeration: all 39 methods were listed verb-by-path and counted by hand-readable output, giving the same 21 / 18.",
      "WHY THE ERROR IS INVISIBLE TO THE OBVIOUS CHECK: 20 + 19 = 39 and 21 + 18 = 39. The total the face leads with is CORRECT, so any reader verifying the denominator against the method count confirms it and moves on. The two halves are wrong in opposite directions and cancel exactly -- a quantity BOTH the right and the wrong split predict is not evidence, and the total is that quantity here.",
      "WHY IT IS LOAD-BEARING AND NOT COSMETIC: AMEND D sets the fallback 'If the face measures that the authorizer type cannot run on OPTIONS, the denominator falls to 20 with the reason in the proof'. That 20 is the NON-OPTIONS count. It is 21. A worker taking the fallback at the face's number attaches the authorizer to 20 of 21 non-OPTIONS methods and files a proof whose denominator says 20 of 20 -- COMPLETE and CORRECT-LOOKING with one authenticated method left open, on an API whose non-OPTIONS surface includes autosave PUT, export-and-submit POST, parse-pickle POST and four market-update POSTs. S1-AC3 would pass on the wrong denominator.",
      "SCOPE OF THIS ROW: it corrects a COUNT, nothing else. It does not dispute AMEND D's shape (both counts printed either way), does not claim which methods the authorizer can carry -- that is a measurement limb 2 makes -- and does not touch the tick-6 verdict's substance ((a), import-first, the Z-S14 bar, the body-identity control), all of which stand."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHAT THIS SEAT WILL DO WHILE THIS IS OPEN, so the round does not stall on it: limb 1 (the adoption import) does not depend on the split at all -- it turns on the Z-S14 bar (0 add / 0 destroy / no forces-replacement) and the body-identity control, neither of which references the OPTIONS partition. This seat proceeds with limb 1 and STOPS before limb 2's attach decision, which is where the number becomes load-bearing. THE FIX IS ONE CHARACTER IN EACH HALF and is the issuer's to make, not this seat's -- substituting a corrected denominator into someone else's face is the substitution the face's own re-read instruction forbids. THE GENERAL SHAPE, worth the row on its own: a denominator stated as a SUM of parts invites verification of the SUM, and the sum is exactly the quantity that cannot discriminate between a right and a wrong partition. Print the parts and check the PARTS.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S56",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "THE Z-S14 BAR AS WRITTEN CANNOT BE MET BY THE DESIGN THE SAME FACE MANDATES. AMEND C row 4 requires 0 to add, 0 to destroy, with the ONLY expected diff being the in-place body update and its deployment. A body-triggered aws_api_gateway_deployment does not exist in state on a first adoption, so it MUST be created -- the measured plan reads 1 to add. The two clauses of one sentence contradict each other. Separately the plan carries a THIRD change the face names nowhere: both live stages gain provider default_tags.",
    "evidence": [
      "THE MEASURED PLAN, post-import, before any change: Plan: 1 to add, 3 to change, 0 to destroy. Action lines, complete: aws_api_gateway_deployment.opal_portal_api WILL BE CREATED; aws_api_gateway_rest_api.opal_portal_api updated in-place; aws_api_gateway_stage.prod updated in-place; aws_api_gateway_stage.production updated in-place. FORCES-REPLACEMENT COUNT: 0 -- that half of the bar IS met, and 0 to destroy is met.",
      "WHY THE 1-TO-ADD IS STRUCTURAL AND NOT A DEFECT IN THE DECLARATION: AMEND C row 2 requires an aws_api_gateway_deployment triggered on the body hash. A deployment is not importable as part of the API or its stages, was never in this state (the whole cell exists because NOTHING of this API was managed), and is immutable by nature. There is no declaration satisfying row 2 that also yields 0 adds on the first plan. The face's own words name it as expected (and its deployment) while its own bar forbids it (0 to add). One of the two has to give and it is not this seat's to choose.",
      "THE THIRD CHANGE, which the face mentions in neither clause: both stages show tags_all gaining Environment=Production, ManagedBy=Terraform, Project=OpalPortal. These come from this root's provider default_tags and are written to the LIVE stages on apply. Benign in effect and ordinary when adopting a resource into a tagged root -- but they are neither the in-place body update nor its deployment, and the face's sentence ends anything else is a STOP and a row. Reported rather than waved through, because the bar's discriminating power comes from being exhaustive.",
      "WHAT THE IN-PLACE API DIFF ACTUALLY IS, so nobody reads updated in-place as alarming: the single attribute is + body = jsonencode(...). An API Gateway import does not populate the body attribute, so state holds none and the declaration supplies it. The rendered body is the export's own content (openapi 3.0.1, title opal-portal-api, version 2026-06-16T21:35:07Z, its 20 paths). That IS the expected in-place body update.",
      "WHAT THE APPLY WOULD DO IF RUN, stated because the hold is the finding: it would create one deployment from the imported body and repoint BOTH live stages onto it -- prod from 5vm7lc and production from c2zxm8, both currently rendering as known after apply. That is the correct end state for this cell AND it is a production change at limb 1, before any authorizer exists. The body-identity control (export2) runs AFTER that apply by AMEND C's own sequencing, so it would detect damage rather than prevent it. That is inherent to the design and is not itself a defect -- it is why this seat declined to proceed on its own reading of an ambiguous bar.",
      "PRECONDITIONS ALL VERIFIED CLEAN BEFORE THIS POINT, so the hold is isolated to the bar and not to the setup: the UNSCOPED baseline on portfolio-management before the first edit read No changes. Your infrastructure matches the configuration. (0/0/0); the module state holds 42 objects with 0 aws_api_gateway addresses, matching the face's carrier claim; all three imports succeeded (the API and BOTH stages); the body file is byte-identical to export1, sha256 0e373129f83d552e8ca5d56dd6e81b79446d88f3b0d1ec83904ed239dfa2e161, re-hashed after the copy. ONE INSTRUMENT NOTE worth carrying: a terraform state list run BEFORE terraform init returned 22 lines that were actually error text; after init the same command returns 42 real addresses. A pre-init state read is not a state read, and it fails toward a plausible-looking number rather than an obvious error."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHAT THIS SEAT RECOMMENDS, offered as a recommendation and NOT taken: read the bar as 0 to add and 0 to destroy AMONG THE IMPORTED OBJECTS -- the API, the two stages and the 39 methods are never created or replaced, which is the hazard Z-S14 was actually written against (a plan that RECREATES a live resource) -- and name the deployment create and the stage default_tags as the two expected additions. That reading keeps every ounce of the bar's protective value and is satisfiable. THE OBVIOUS ALTERNATIVE IS WORSE AND IS NAMED SO IT IS NOT RE-DERIVED: importing an existing deployment to reach a literal 0-add would make the body-hash trigger force REPLACEMENT on any later change, converting a clean create into an add-plus-destroy and breaking 0 to destroy instead. WHY THIS IS FILED AND HELD RATHER THAN JUDGED: S1-AC1 is not an ordinary precondition, it is the single control AMEND C designates as the one control that must be able to fail on this limb. A worker who reinterprets the criterion he is graded on, on a production API with two live doors, has quietly removed the control and left something that still reads PASS. Earlier today this seat got the mirror of this wrong in the other direction, un-flipping an accepted instance on its own authority (Z-S51). The rule that covers both: the worker measures and reports; the owner of the bar decides what the bar means.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S60",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "C-16 OVERSTATES THE CONTROLS THE LOG DESTINATION ACTUALLY CARRIES, AND THE GAP IS A CONFUSED-DEPUTY ONE. TO-OP-S-17R-28 deliverable 3 and S28-AC1 both describe opal-data-security's two service-principal grants as 'each with SourceAccount + SourceArn'. MEASURED on the applied plane: AllowCloudFrontAccessLogDelivery carries aws:SourceAccount and NO aws:SourceArn; AllowALBAccessLogDelivery carries NEITHER -- its only condition is s3:x-amz-acl = bucket-owner-full-control. So of the four condition slots the face asserts, ONE is present. The declaration AGREES with the world (s3.tf:117-160 declares exactly these), so the ALIGN's plan is legitimately 0 changes and the face's STOP-on-any-plan-line does NOT fire -- what disagrees is C-16's TEXT against both. This is the align limb finding what an align is for.",
    "evidence": [
      "APPLIED PLANE, measured 2026-09-03T17:42:27Z, denominator 3 statements on opal-data-security: (1) DenyInsecureTransport, Principal '*', Condition Bool aws:SecureTransport false. (2) AllowCloudFrontAccessLogDelivery, Principal Service delivery.logs.amazonaws.com, Resource .../waf-logs/cloudfront-access/*, Condition StringEquals { aws:SourceAccount 313476888478, s3:x-amz-acl bucket-owner-full-control } -- SourceAccount PRESENT, SourceArn ABSENT. (3) AllowALBAccessLogDelivery, Principal Service logdelivery.elasticloadbalancing.amazonaws.com, Resource .../waf-logs/alb-opal-gateway/*, Condition StringEquals { s3:x-amz-acl bucket-owner-full-control } -- SourceAccount ABSENT, SourceArn ABSENT.",
      "THE PROBE IS NOT BLIND: the same reader run against the ACCESS-LOGS bucket's policy returns a statement carrying BOTH aws:SourceAccount and ArnLike aws:SourceArn, so the matcher finds those keys where they exist. That bucket is the positive control and it is also the estate's own worked example of the pattern C-16 describes.",
      "DECLARED PLANE AGREES WITH THE WORLD, which is why this is a spec-text finding and not drift: infra/aws/terraform/opsec/s3.tf:117-160 declares exactly these conditions. The UNSCOPED plan on the opsec root reads 'No changes' rc=0 both before this task order's edit and after its apply, and the apply's plan carried ZERO lines matching data_security. So the face's own STOP condition -- 'if the plan wants to change ANYTHING on this bucket, STOP and file a row' -- correctly does not fire. The disagreement is between C-16's rendering and the pair of planes that agree with each other.",
      "WHY IT IS NOT MERELY A WORDING SLIP: aws:SourceAccount and aws:SourceArn on a service-principal grant are the confused-deputy controls. Without them the ALB statement permits the logdelivery.elasticloadbalancing.amazonaws.com service principal to PutObject into waf-logs/alb-opal-gateway/* qualified only by an ACL condition, which does not bind the delivery to THIS account's load balancer. The exposure is bounded -- one prefix, PutObject only, ACL-conditioned, and the bucket is private with 4 of 4 public-access blocks -- but it is precisely the control C-16 names and precisely the one absent.",
      "s3.tf's OWN COMMENT AT :137-147 EXPLAINS A DIFFERENT OMISSION AND MUST NOT BE READ AS COVERING THIS ONE: it says the older regional ELB-account-ID PRINCIPAL form is not granted because 'granting both would widen past the log-delivery principal on that prefix ONLY'. That is about which PRINCIPAL is named. It says nothing about the SourceAccount/SourceArn CONDITIONS, so the missing conditions are unexplained by the file's stated reasoning rather than deliberately waived by it."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHAT THIS DOES TO S28-AC1, and it is filed rather than absorbed: five of the six C-16 properties read exactly as stated -- private 4 of 4, AES256 and NOT the project key, versioning Enabled, the non-TLS deny, and the waf-logs/ lifecycle with Glacier 90d and expiry 400d -- and the plan wants zero changes. The sixth, the two service grants, reads with one of four condition slots present. The criterion is therefore filed with its qualifier rather than as a clean PASS, because a PASS here would record that the confused-deputy conditions were verified when what was verified is that they are absent. THE REMEDY IS NOT THIS SEAT'S AND IS DELIBERATELY NOT TAKEN: the face makes the log destination read-only for this task order in terms. Two shapes, both for the owners named above: correct C-16's text to describe the resource as ratified, or keep the text and cut a cell that ADDS the two conditions -- and that second one is a change to a LIVE log destination whose failure mode is silent (a wrong or over-tight condition stops delivery without erroring, which is the Z-S37 lesson one bucket over), so it wants its own face with a delivered-object bar rather than a rider on this one. THE REUSABLE PART: an ALIGN cell is the only kind that can find this class at all. A BUILD compares the world to nothing, and a plan compares the world to the DECLARATION -- so when declaration and world agree, the only thing left that can disagree is the SPEC, and only a human-written criterion quoting the spec's own words back at the applied plane will catch it. This is the second time today a face's summary wording was stricter or looser than the artifact it described (the first was TO-OP-S-16-17-8R2's 'two expected diffs' against a plan that carried three).",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S62",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "LIMB 2 NAMES A MODULE THAT DOES NOT EXIST, AND THE LAMBDA IT NAMES CANNOT SERVE A REST AUTHORIZER. The face requires the new authorizer to REUSE opal-portal-authorizer's secret-read module and forbids a second copy of the read. There is no module: the read is inline in a single-file Lambda. And that Lambda answers in HTTP-API v2 shape, which a REST REQUEST authorizer structurally cannot use. All three obvious paths are blocked by the face's own words.",
    "evidence": [
      "FACT 1 -- THERE IS NO SECRET-READ MODULE. infra/aws/users/lambda/portal-authorizer/ contains exactly one source file, index.mjs (11273 bytes), plus package.json, the two lockfiles, node_modules and deploy.sh. The origin-secret read is the function isOriginVerified at index.mjs:121, INLINE, in the same file as JWT verification and the DynamoDB firm-descendant walk. There is no importable module for another Lambda to reuse; the face's phrase 'REUSES opal-portal-authorizer's secret-read module' names an artifact that does not exist.",
      "FACT 2 -- THE EXISTING LAMBDA CANNOT BE THE REST AUTHORIZER, read at source rather than inferred. index.mjs:164 generateSimpleResponse returns exactly {isAuthorized, context}, and its own docstring at :160-163 states 'Generate simple response for HTTP API v2 authorizer / Required format when EnableSimpleResponses is true'. Every return path in the handler goes through it (:281, :288, :341, :356). A REST API REQUEST authorizer requires a different contract entirely -- principalId plus an IAM policyDocument -- so pointing aws_api_gateway_authorizer at this function would produce a malformed response on every call and deny the whole API. CORROBORATION on the live plane: get-authorizers on the HTTP API reads AuthorizerPayloadFormatVersion 2.0 and EnableSimpleResponses true for naqxlm, which is the v2-only configuration.",
      "FACT 3 -- WHY THE THIRD PATH IS ALSO CLOSED: writing the read again inside a new REST authorizer is what the face forbids in terms ('never a second copy of the read'), and that prohibition is well-founded, not pedantry -- TO-OP-S-3's rotation runbook makes the two-slot overlap and the 300 s TTL a CORRECTNESS control, and two independent copies of that logic drift on the next rotation. The prohibition should be kept; it is the instruction to reuse a nonexistent module that cannot be.",
      "WHAT THIS DOES NOT TOUCH: limb 1 is complete, applied and independently confirmed (39 of 39 methods by path+verb, both doors on 4ykw9p). Nothing here reopens it. Limb 3 (the Cognito docstring correction in the eight Lambda sources) is independent of this and can proceed on its own.",
      "THE COST OF THE OBVIOUS FIX, stated because it is not free and is the reason this is the issuer's call and not this seat's: EXTRACTING isOriginVerified into a shared module and importing it from both authorizers is the clean answer and honours 'never a second copy' exactly -- but it EDITS AND REDEPLOYS opal-portal-authorizer, a live Lambda that TO-OP-S-3 deployed hours ago and whose CodeSha256 RvHb6Lj55WjOKCvBAkxQvKIXEEl5jdZfhyT1AY6ZEf4= is pinned as evidence in TWO filed proof instances (TO-OP-S-3's and this face's own cut-time read). Changing it invalidates those pins and puts the HTTP API's authorizer -- the one TO-OP-S-2 just attached to nine routes an hour ago -- back in the blast radius of a REST-API task order. That is a materially wider change than 'the authorizer' and the face's own BOUNDS say no other resource rides."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THE THREE OPTIONS, laid out so the issuer picks rather than re-derives, each with what it costs. (A) EXTRACT the read into a shared module imported by both authorizers -- honours the prohibition exactly, single source of truth for the two-slot logic; COSTS a redeploy of the live opal-portal-authorizer and invalidates a CodeSha256 pinned in two filed proofs, widening a REST task order onto the HTTP API's authorizer. (B) NEW REST authorizer Lambda with its OWN copy of the read -- no blast radius on the HTTP side; VIOLATES the face's 'never a second copy' and puts the rotation's two-slot/TTL correctness control in two places that drift on the next rotation, which is precisely what the prohibition protects. (C) DEFER limb 2 to its own task order with the extraction as an explicit deliverable, and land limb 3 (the Cognito docstrings) now, since limb 3 is independent -- COSTS round time and leaves FWD-1 open on the REST API, which is the door this project exists to close. THIS SEAT'S RECOMMENDATION IS (A) WITH THE EXTRACTION SCOPED AS A PURE MOVE -- the extracted module byte-identical in behaviour, the HTTP authorizer's diff being only the import line and the deleted function, its CodeSha256 re-pinned in the proof as a KNOWN and EXPECTED change with the old and new values both recorded, and the HTTP API's nine routes re-probed after to prove nothing regressed. A pure move is auditable in a way a rewrite is not. But (A) touches a resource the face's BOUNDS exclude, so it needs the issuer's word before a line is written. THE GENERAL SHAPE: a face can name an artifact that ought to exist -- 'the secret-read module' is how a reader would describe that code if they had not opened the file -- and the phrase reads as a reference when it is actually a wish. This is the second time on this face that a plausible NAME stood where the world had something else (portal-auth for the routes' carrier was the first, the demo-firm credential the second, and this the third).",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S63",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A SAFETY GATE THAT CANNOT SEE A LANE SEAT'S INBOX LET A PRODUCTION APPLY RUN PAST THREE UNREAD ISSUER PRECONDITIONS, AND THE DEFECT HAS BEEN DOCUMENTED AND RULED IN THE GATE'S OWN SOURCE SINCE 2026-07-25 WITHOUT REMEDIATION. safe-apply.sh fires the HALTGT checkpoint immediately before terraform apply and refuses to apply ungated (:68-75); the checkpoint blocks on ANY unread message absent HALT_ACK=1, not only [STOP]-class. But halt_gate_unread_for() (halt-gate-check.sh:210-214) builds its directory as INBOX_ROOT/<serial>, which for a lane serial is the FLAT org/mcp/inbox/0.7.0_AE_CloudOps~Z/ -- a directory that EXISTS and holds ZERO *.md -- while the broker writes the NESTED org/mcp/inbox/0.7.0_AE_CloudOps/~Z/. The gate therefore does not fail to find an inbox; it finds an empty decoy and PASSES SILENTLY. MEASURED INSTANCE, 2026-09-03: 0.7.0_AE_CloudOps~Z ran the TO-OP-S-1 limb-1 apply against REST API f61h681z9g at ~18:1xZ, creating a deployment and repointing BOTH live stages (prod off 5vm7lc, production off c2zxm8), while message 19911 carrying three issuer-ordered preconditions ON that apply sat unread in the nested lane inbox. A gate reading the correct path would have blocked it. The apply's OUTCOME was clean and the hazard is measured absent, so this row records a CONTROL FAILURE, not damage.",
    "evidence": [
      ".tools/halt-gate-check.sh:210-214 halt_gate_unread_for() -- dir=\"${HALT_GATE_INBOX_ROOT}/$1\", find -maxdepth 1 -name '*.md'",
      ".tools/halt-gate-check.sh:280-300 -- the defect already documented and ruled (0.8.0_AE_CloudComp~C 2026-07-25; re-derived by 1.0.0_SA_CTO 183004Z), with live counts FLAT=0 vs NESTED=530/1076/495/420",
      ".tools/safe-apply.sh:68-75 -- the checkpoint fires immediately before the apply and refuses to apply ungated",
      "measured at this seat 2026-09-03 ~18:2xZ: org/mcp/inbox/0.7.0_AE_CloudOps~Z/ exists, 0 *.md at top level; broker receipts read 'delivered to 0.7.0_AE_CloudOps~Z (inbox 0.7.0_AE_CloudOps/~Z)'",
      "the instance: 0.7.0_AE_CloudOps~Z message 19916 (unprompted disclosure) and 19914 (the limb-1 report); apply created deployment 4ykw9p and repointed prod off 5vm7lc and production off c2zxm8",
      "post-apply verification at this seat against a 17:36Z pre-apply capture: 39 of 39 methods identical by path+verb, 0 lost, 0 gained -- the control failed, the outcome did not"
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS FILED BY THE ISSUER AND NOT BY THE SEAT THAT TRIPPED IT: 0.7.0_AE_CloudOps~Z disclosed the sequencing failure unprompted, against its own already-confirmed completion report, four minutes after this seat had confirmed limb 1 -- with the gate blind, the confirmation already given and the outcome clean, every incentive pointed at silence. The disclosure is the only reason this is measurable at all, and the finding belongs to that seat; the row is the issuer's because the routing is. THE ISSUER'S OWN ERROR IN THE SAME EPISODE, recorded so the row is not read as one-sided: this seat's 18:19Z confirmation asserted 'ALL THREE PRECONDITIONS RAN' by mapping the worker's S1-AC1 and S1-AC2 evidence onto preconditions it had never received -- and S1-AC2 is sequenced AFTER the apply by the face's own design, so it could not have satisfied a pre-apply precondition. One evidence banner stamped across two evidence classes, in a confirmation message about a production change. Corrected to that seat at 18:23Z. WHAT IS NOT CLAIMED: no remedy is proposed here and none is authorised. The gate is a shared safety surface owned outside this project, the defect is already ruled in its own source, and widening a fail-closed condition on a gate that every deploying seat depends on is exactly the class of change that needs its owner rather than a passing issuer -- the estate has already measured that an over-broad reaper remedy reaped LIVE watchers. THE OPERATIONAL MITIGATION ADOPTED INSTEAD, which costs nothing and needs no gate change: both open faces now require a BROKER DRAIN IMMEDIATELY BEFORE any irreversible step rather than only at the top of the turn, because a face under active amendment (three amendments in twenty minutes here) makes a top-of-turn drain stale by the time the apply runs. That mitigation is the seat's own proposal, offered against its own interest. THE GENERAL SHAPE, and it is the reusable half: A GATE THAT READS THE WRONG PATH IS STRICTLY WORSE THAN A GATE THAT IS ABSENT, because absence is visible and a silent PASS is indistinguishable from safety -- and it is the same failure mode as row Z-S49 one plane over, where a refused log delivery presents as an empty prefix rather than an error. Twice in one afternoon, a system reported ABSENCE where the truthful answer was NOT LOOKING.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S64",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Z-S62's TWO FACTS CONFIRMED ON THIS SEAT'S OWN READ, and TWO THINGS ADDED FOR THE CHOICE. CONFIRMED: there is no secret-read module -- infra/aws/users/lambda/portal-authorizer/ holds exactly one source file, index.mjs, 358 lines, beside package.json, two lockfiles and deploy.sh, and a repo-wide search finds no shared secret-read module. ADDED (1): option C is not merely forbidden by the face's words, it is STRUCTURALLY IMPOSSIBLE -- index.mjs contains policyDocument 0, principalId 0, Statement 0, Effect 0, execute-api:Invoke 0, against generateSimpleResponse 5 and EnableSimpleResponses 2. The Lambda emits ONE shape and has no other path, so pointing anything at it requires editing it, which collapses C into A's cost. ADDED (2): A's proof-invalidation cost is overstated and points at a different defect -- exactly ONE of the project's 8 filed proof instances pins a CodeSha256, and its evidence carries NO ISO vintage.",
    "evidence": [
      "MEASURED 2026-09-03T18:38:42Z, repo plane: `git ls-files` returns 5 paths under infra/aws/users/lambda/portal-authorizer/ -- index.mjs, package.json, package-lock.json, bun.lock, deploy.sh -- so exactly one source file, confirming Z-S62's FACT 1. A repo-wide search for a shared secret-read module returns only unrelated files (astn-pipeline/secrets-shared.tf, a graph test), so there is nothing the face's 'reuse the module' clause could name",
      "THE DECISIVE READ ON OPTION C, a token census over index.mjs: policyDocument 0, principalId 0, Statement 0, Effect 0, execute-api:Invoke 0; generateSimpleResponse 5, isAuthorized 3, EnableSimpleResponses 2. The file has NO v1 policy-document path at all. This is stronger than Z-S62's framing and does not depend on any claim about what a REST authorizer accepts: whatever the service would take, this Lambda emits one shape and contains no code that emits another, so it cannot be pointed at without being edited",
      "ON OPTION A's STATED COST, measured rather than accepted: of the 8 proof-of-spec instances tracked under this project's deliverables, exactly ONE pins a CodeSha256 -- TO-OP-S-3's S3-AC3, whose criterion reads 'the auth handler's and the authorizer's live CodeSha256 equal the built artifacts' sha ... and a Terraform re-plan after the apply reads 0-diff'. Z-S62 says 'two filed proofs'; this seat finds one within that scope, and states the scope so the difference is not read as a contradiction -- a second pin in a change-management ledger or another project's artifact is outside what was searched here",
      "AND THE PIN CARRIES NO VINTAGE: that criterion's evidence contains no ISO timestamp. So it asserts a LIVE-STATE EQUALITY as if it were permanent. A redeploy does not falsify what was true when it was measured; it makes a vintage-less state claim STALE, which is a defect in the evidence's FORM rather than a cost of the redeploy. The estate already banks this shape -- a citation without a vintage is not a citation, and a perishable claim recorded as permanent ages the moment anything runs",
      "SO THE TRADE IS NARROWER THAN IT LOOKS: the A-versus-B choice should be weighed on the correctness argument Z-S62 makes well -- whether the rotation's two-slot overlap and 300 s TTL live in one place or two, since two copies drift at the next rotation -- and NOT on proof invalidation, which is one criterion's evidence form and will recur on every future redeploy of either Lambda whatever is decided here"
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHAT THIS SEAT IS NOT DOING: not choosing among A, B and C -- that is 2.0.0_SA_COO~Z's, and Z-S62 lays the options out well enough that the issuer picks rather than re-derives. WHERE THIS SEAT IS NAMED, the FWD-1 half: none of the three options changes what FWD-1 requires or how it is satisfied. FWD-1's shape is that the REST API's methods carry an authorizer requiring the origin secret; it does not name WHICH Lambda, nor whether the read is shared or copied. So this is a build-path choice inside the outcome rather than a question about the outcome, and it needs no verdict from this seat unless the issuer's choice would change what FWD-1 accepts -- it would not. ONE THING WORTH SEPARATING FROM THE DECISION, because it survives it: S3-AC3's vintage-less CodeSha256 pin is worth an amendment on its own terms, whichever option lands. A criterion that asserts a live equality without recording when it was read cannot distinguish 'still true' from 'was true', and this project has spent the day on exactly that distinction in three other places.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S67",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A CRITERION DEMANDING BYTE-IDENTICAL EXECUTABLE LINES QUIETLY ASSUMES THE FILES ALREADY PASS THE COMMIT GATE THEY WILL BE COMMITTED THROUGH. Where they do not, the criterion and Rule 14 are jointly unsatisfiable and the work stalls on lint debt belonging to nobody on the face. Not specific to F541, to ruff, or to this project.",
    "evidence": [
      "THE LIVE INSTANCE. TO-OP-S-1's S24-AC1 requires the eight Lambda sources' executable lines be byte-identical (comments and docstrings only). CLAUDE.md Rule 14 requires every .py edit pass .tools/commit-gate.sh, which runs ruff. FOUR of the eight files carried PRE-EXISTING ruff F541 errors -- portfolio_autosave_put 4, portfolio_pickle_parser 2, portfolio_optimization_autosave_put 1, portfolio_version_get 1, total EIGHT, all measured on HEAD so all predating this task order. The gate blocks on any of them. Fixing them changes executable lines. Both rules bind and neither yields; the limb could not be committed at all until the issuer pre-authorised the gate-compliance edits.",
      "IT IS A SHAPE, NOT AN INCIDENT. Nothing in the collision depends on F541, on ruff, or on Python. Any criterion of the form 'executable lines unchanged' combined with any mandatory pre-commit gate produces it on any file carrying pre-existing debt against that gate. The face author cannot see it, because the debt lives in files the face merely NAMES and does not otherwise inspect -- the criterion is written about the EDIT while the gate fires on the FILE.",
      "WHY IT IS INVISIBLE UNTIL THE COMMIT. The work completes and verifies clean -- census correct, AST identical, diff comment-only -- and only the commit reveals the collision. Every quality signal reads green right up to the gate, so the author of the face has no natural moment at which to discover the assumption they made.",
      "THE SECOND-ORDER FINDING, from the issuer's own reasoning at 19934: the tempting escape is a suppression comment (# noqa), which also keeps the AST identical and also passes the gate. It was rejected here because it leaves the debt while adding a marker a later reader must decode, in a file the worker does not own -- and because commit_gate_runner.py:313 records 18c92b9ac as an audited bypass ON THIS EXACT RULE whose remediation was certified 'closed' and was later found still live, the gate having keyed on filenames rather than on what the file IS. A rule with a history of being bypassed and certified closed while still firing is one to fix rather than bypass again.",
      "MEASUREMENT NOTE ATTACHED BECAUSE IT NEARLY BURIED THE FINDING: the census that produced the figure 8-across-4 read ZERO on its first two attempts. One matched a regex against ruff output carrying ANSI escapes between the path and the line number; the other passed --no-color, which is not a ruff flag (it is --color <WHEN>), so every invocation died with a usage error and the grep for the summary line matched nothing. BOTH failures returned the number 0 -- 'no lint debt here' -- which is the most reassuring answer available and the one least likely to prompt a re-check. Caught only because a direct run had already shown 4 errors in a file the census called clean."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS FILED AS AN OBSERVATION AND NOT A BLOCKER: the live instance is resolved (limb 3 committed @a2c88e77ae, gate clean 8 of 8) and the issuance rule is adopted. It is filed because the THREAD is not a durable carrier and the next face with this shape will be written by someone who did not read this exchange. THE REMEDY IS AT ISSUANCE AND IT IS CHEAP -- either measure gate-compliance as a stated precondition when the face is cut, or pre-authorise gate-compliance edits in the criterion itself. Both are one sentence at cut time; the alternative is a blocked limb and a ruling mid-round. RELATED SHAPE ON THIS SAME FACE, worth reading together: rows Z-S53 (a denominator stated as a SUM of parts invites verification of the sum, which is the one quantity that cannot discriminate a right partition from a wrong one) and Z-S56 (a bar transplanted from a context whose premise it no longer fits, with the premise unchecked). All three are cases where a spec was internally coherent and quietly wrong about the world it would run in.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S68",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "opal-cloudfront-protection NEVER RE-PLANS 0-DIFF AFTER THE APPLY, AND THE WORLD IS CORRECT -- so S418-AC3's 0-diff limb is UNSATISFIABLE ON THIS ROOT while every other limb passes. The live ACL reads exactly as specified (6 rules: BlockedIPs 0 Block, RateLimitRule 1 Block, AuthLoginRateLimit 2 Block, and the three managed groups 3/4/5 all Count), but terraform proposes a stable REMOVE-AND-RE-ADD of the three managed-rule-group rules on every plan -- 3 minus-blocks and 3 identical plus-blocks, same names, priorities, vendors and metric names. It is an aws_wafv2_web_acl rule-SET hash instability, not drift: the state's managed_rule_group_statement carries version='' plus empty managed_rule_group_configs, rule_action_override and scope_down_statement, and the config produces no such attributes, so the set element hashes differently every time.",
    "evidence": [
      "THE WORLD IS CORRECT, verified independently of terraform 2026-09-03T19:59:51Z: wafv2 get-web-acl on opal-cloudfront-protection returns 6 rules -- BlockedIPs prio 0 Block (OrStatement over both ip_set references), RateLimitRule prio 1 Block, AuthLoginRateLimit prio 2 Block, ip-reputation prio 3 Count, common-rule-set prio 4 Count, known-bad-inputs prio 5 Count. Every acceptance limb except the 0-diff one passes on that read: S18-AC1, S18-AC2 and S4-AC1 are all satisfied.",
      "THE DIFF IS STABLE, NOT TRANSIENT: three consecutive plans after the apply each return rc=2 with 'Plan: 0 to add, 1 to change, 0 to destroy' and exactly 3 minus-rule blocks paired with 3 plus-rule blocks. The plus blocks reproduce the minus blocks attribute for attribute -- same name, priority, vendor_name, override_action count, and visibility_config.",
      "A CONVERGENCE APPLY WAS RUN AND DID NOT CONVERGE, which is the measurement that turns this from a suspicion into a finding: safe-apply of the no-op plan returned rc=0 with 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed' and 'Modifications complete after 21s', and the very next plan STILL reads rc=2 with the identical 3/3 diff. The live rule array is byte-identical before and after that apply, so nothing was risked -- UpdateWebACL replaces the whole rule array atomically, so there is no window in which protection is reduced. It was run once as a diagnostic and will NOT be repeated: idempotent churn on a live edge ACL buys nothing.",
      "POSITIVE CONTROL, AND IT IS WHAT RULES OUT THE OBVIOUS EXPLANATIONS: the SIBLING root infra/aws/terraform/opal-gateway plans CLEAN (rc=0, 'No changes') against opal-gateway-waf, which carries THREE managed rule groups declared in the IDENTICAL idiom -- override_action { count {} } / managed_rule_group_statement { vendor_name, name } / visibility_config, no version argument, read at waf.tf:90-119. Same provider, same account, same resource type, same block shape, same day. So this is not the idiom, not the provider version and not a general wafv2 defect; it is specific to this ACL's state.",
      "THE MECHANISM, read from state via terraform show -json: the stored managed_rule_group_statement for common-rule-set holds name, vendor_name, version='' , managed_rule_group_configs=[], rule_action_override=[] and scope_down_statement=[]. The plan's minus-block shows name and vendor_name plus '1 unchanged attribute hidden' while its plus-block shows only name and vendor_name -- i.e. the config side produces no value for the attribute the state side carries. rule is a TypeSet, so an element whose nested attributes differ from the stored element hashes to a different member and terraform proposes remove-plus-add rather than an in-place edit.",
      "WHAT IS NOT CLAIMED: this row does not identify WHY this ACL's state carries those attributes while the sibling's does not -- the sibling's rules predate this session and may have been written by a different provider version. Establishing that needs a state-vintage comparison nobody has run, and the remedy does not depend on it."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHAT THIS DOES TO S418-AC3, filed rather than smoothed: the criterion has four limbs and three pass on this root -- the baseline was quoted at 0/0/0 before the first edit, the apply's changed-resource list contained ONLY the two IP sets and the ACL with zero destroys and zero forces-replacement plan-wide, and push state is measured. The 0-diff limb does not pass and cannot be made to pass honestly, so the criterion files with that limb named rather than as a clean PASS. WHY THIS SEAT DID NOT FIX IT, and the reasoning is the same one that made Z-S49 worth filing: the two available fixes both trade a real property for a cosmetic one. Pinning managed_rule_group_statement version would stop the churn by selecting a specific AWS ruleset VERSION on live edge traffic -- a behavioural change to protection, made to satisfy a plan check. A lifecycle ignore_changes on rule would silence the diff by blinding terraform to the entire rule array, which is the one thing S18-AC2 relies on to prove no existing rule moved. Making the plan clean would in both cases cost more than the dirty plan does. THE OPERATIONAL COST IS BOUNDED AND WORTH STATING PLAINLY: a permanently non-converging root means every future plan on portal-auth carries this 1-change noise, so a REAL future drift on this ACL would have to be spotted inside a diff that is never empty -- that is the actual harm, and it is a detection cost rather than a protection cost. THE REUSABLE PART: an apply returning rc=0 with 'Modifications complete' does NOT establish that terraform and the world agree -- it establishes that the API accepted the call. Only the re-plan tests agreement, which is exactly why S418-AC3 asks for it, and it is why running that check before declaring the leg closed was worth the two extra minutes.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S75",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Z-S68 STATES A CAUSE THAT IS FALSE, AND THE FINDING IS NARROWER AND BETTER THAN THE ROW CLAIMED. The plan churn is a PRE-APPLY ARTIFACT THAT RESOLVES ON APPLY -- measured: opal-gateway's pre-apply plan carried the identical remove-and-re-add on two managed-group rules, and after its apply that root reads No changes rc=0 with zero minus-rule and zero plus-rule blocks. portal-auth does NOT resolve, after THREE applies. So the condition is a property of ONE ROOT, not of aws_wafv2_web_acl rule sets, and Z-S68's mechanism -- state carrying empty attributes the config does not produce -- cannot be it, because the converging root carries byte-identical empty attributes on the two rules that churned. THE CAUSE IS STILL UNKNOWN AND THIS ROW SAYS SO RATHER THAN OFFERING A THIRD GUESS.",
    "evidence": [
      "THE DISCRIMINATING EXPERIMENT, run at the issuer's direction: opal-gateway's PRE-APPLY plan carried 2 minus-rule blocks and 3 plus-rule blocks, the two being ip-reputation and known-bad-inputs removed and re-added identically and the third being the genuinely new BlockedIPs rule. After safe-apply (2 added, 1 changed, 0 destroyed, 20:23:42-20:24:34Z) the UNSCOPED re-plan reads 'No changes. Your infrastructure matches the configuration.' rc=0 with ZERO minus-rule and ZERO plus-rule blocks. CONVERGED.",
      "THE CONTRAST, measured in the same minutes: portal-auth re-planned at 20:26Z still returns rc=2, 'Plan: 0 to add, 1 to change, 0 to destroy', after THREE applies including one run solely as a convergence diagnostic. So one root settles on its first apply and the other has not settled on its third.",
      "WHY Z-S68's STATED CAUSE IS FALSE, and the row's own control already contained the refutation: Z-S68 said the mechanism is state carrying version='' plus empty managed_rule_group_configs / rule_action_override / scope_down_statement against a config producing none. terraform show -json on BOTH roots: opal-gateway's ip-reputation and known-bad-inputs carry exactly those same empty values -- version='', configs=[], overrides=[], scope_down=[] -- and that root CONVERGED. Identical attributes, opposite outcome. The issuer caught this before this seat did.",
      "A SECOND HYPOTHESIS OF THIS SEAT, ALSO DEAD: that populated rule_action_override protects a rule from churning. It correlated 4 of 4 at the time -- opal-gateway's common-rule-set has three override entries and did not appear in its plan churn, while the three empty-override rules on portal-auth all churn. The regional convergence kills it: ip-reputation and known-bad-inputs have EMPTY overrides, churned in the plan, and then converged anyway. A correlation across four cases that dies on the fifth.",
      "A THIRD HYPOTHESIS, AND THE TEST OF IT WAS INVALID -- recorded because the invalid test is the more useful lesson: portal-auth's ACL carries lifecycle { ignore_changes = [tags, tags_all] } and opal-gateway's carries no lifecycle block at all. It was tested by temporarily removing the block and RE-PLANNING read-only; the churn persisted, and this seat wrote it down as falsified. THAT CONCLUSION DOES NOT FOLLOW. opal-gateway has since demonstrated that a plan-visible churn can resolve on APPLY, so a plan alone cannot falsify a hypothesis about post-apply convergence. The lifecycle difference is UNTESTED, not excluded, and it remains the only structural difference identified between the two ACLs. The file was restored and verified byte-identical to HEAD.",
      "WHAT IS EXCLUDED, on measurement rather than reasoning: provider version, AWS account, resource type and declaration idiom are all common to both roots and one converges. The empty-attribute mechanism is excluded by the state comparison. The rule_action_override correlation is excluded by the regional convergence."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHAT THIS CHANGES FOR THE FACE: nothing about the acts and everything about the record. Both ACLs are built correctly and every other limb passes on both roots; S418-AC3 files UNVERIFIABLE-BY-INSTRUMENT for portal-auth per the issuer ruling and PASS for opal-gateway. WHAT IT CHANGES FOR THE COST: Z-S68 framed a standing detection cost as if it applied to aws_wafv2_web_acl generally. It applies to ONE root. That is a materially smaller liability and a materially better-scoped question for whoever picks it up. THE HONEST REMAINDER, stated rather than filled with a third guess: the cause is unknown. The next cheap step is the test this seat got wrong -- remove the lifecycle block and APPLY, not merely plan -- and that is an edit to a live edge ACL's configuration for diagnostic purposes, which is the issuer's call and not the assignee's. THE REUSABLE PART, and it is the reason this row exists at all: I DIAGNOSED FROM A PLAN AND CALLED IT A FALSIFICATION. A plan is a prediction; only an apply plus a re-plan tests convergence. Two of my three hypotheses died to measurements I could have taken first, and the third died to a test I ran in the wrong instrument -- while the row asserting the first was already committed and reading as established. A row that names a mechanism should say how the mechanism was TESTED, not merely how it was inferred, and Z-S68 did not.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S80",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "FWD-1 AS SPECIFIED WOULD TAKE DOWN A LIVE DATA SURFACE. The face requires an origin-secret REQUEST authorizer on EVERY one of the 39 methods of f61h681z9g. TWENTY of those 39 have NO CLOUDFRONT ROUTE AT ALL, so the CloudFront-injected header can never reach them and attaching the authorizer makes them PERMANENTLY UNREACHABLE by any caller. Among them are four live POST writes and a GET currently serving 1.4 MB.",
    "evidence": [
      "THE MEASUREMENT. The REST API f61h681z9g carries 39 methods across 20 paths. Exactly ONE CloudFront behavior routes to its origin APIGateway-portfolio: pattern /api/private/portfolio* (behavior 21). Matching every method path against that pattern: 19 of 39 are reachable through CloudFront (11 non-OPTIONS + 8 OPTIONS); 20 of 39 have NO CloudFront route (10 non-OPTIONS + 10 OPTIONS). The split reconciles with the corrected AMEND D denominator from row Z-S53: 11+10 = 21 non-OPTIONS and 8+10 = 18 OPTIONS.",
      "THE UNREACHABLE SET, ten paths: /api/portfolio/export (POST, OPTIONS) and nine under /api/public/market-update/ -- earnings, history, macro, metrics, topics (GET+OPTIONS each) and export, generate, regenerate, save (POST+OPTIONS each). Note /api/portfolio/export does NOT match /api/private/portfolio* -- the behavior pattern is anchored on /api/private/.",
      "PROVED ON THE LIVE PLANE, not inferred from the pattern list. GET /api/public/market-update/topics THROUGH CloudFront returns HTTP 200 with 1068 bytes of content-type text/html -- the SPA shell served by the default /* behavior, NOT the API. The SAME path at the raw execute-api address returns HTTP 200 with 1417396 bytes of application/json -- the real data. POSITIVE CONTROL that CloudFront can reach this API at all: /api/private/portfolio/funds through CloudFront returns HTTP 401 application/json, i.e. it reaches the gateway and is auth-gated. So the failure is route coverage, not connectivity.",
      "WHY ATTACHING WOULD BE AN OUTAGE RATHER THAN A CONTROL. The authorizer FWD-1 names is keyed on X-Opal-Origin-Verify, which CloudFront injects as a CUSTOM ORIGIN HEADER on requests it forwards to that origin. A request that never traverses CloudFront cannot carry it. For the 20 unreachable methods there is no CloudFront path in existence, so every call to them would be denied permanently -- not hardened, unreachable. Four of them are live POST writes (market-update save, generate, regenerate, export) and one is a GET currently serving 1.4 MB to some live caller.",
      "THE SECOND, LARGER FINDING INSIDE THE FIRST, which is squarely this project's subject: those nine /api/public/market-update/* paths are served ONLY at the raw execute-api address, on an API that get-authorizers reports has ZERO authorizers and get-rest-api reports has NO resource policy. They are an unauthenticated public API surface reachable by anyone who knows the hostname, including four writes. The brief's F1 framing -- that this API 'answers at its raw execute-api address' -- is exactly right and is WORSE than the face's remedy can reach, because the remedy's mechanism does not apply to the very paths most exposed.",
      "WHAT THIS DOES NOT TOUCH: limbs 1, 2a and 3 are complete and independently verified. The adoption stands, the extracted module is live on the HTTP authorizer, and the Cognito docstrings are corrected. Nothing here reopens them."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THE OPTIONS, for the issuer and the certifier, with costs. (A) ATTACH TO THE 19 CLOUDFRONT-REACHABLE METHODS ONLY, print both denominators (19 of 39 attached, 20 of 39 out of reach and why), and file the 20 as a NAMED RESIDUAL with its own cut. FWD-1's door is closed where a door exists; nothing breaks. (B) ADD CLOUDFRONT BEHAVIORS for /api/public/market-update/* and /api/portfolio/export FIRST, then attach to all 39. Correct end state, but it is a routing change on the live distribution -- whose cloudfront-distribution.tf carries its own :5 imported-resource bound -- and it changes how those endpoints are served for whatever calls them today, which has not been enumerated. (C) ATTACH TO ALL 39 AS WRITTEN: rejected outright, it is a 20-method outage including four live writes. THIS SEAT RECOMMENDS (A) NOW AND (B) AS ITS OWN FACE, because (A) is strictly an improvement with no functional risk and (B) needs a caller enumeration before anything moves -- the same bar TO-OP-S-12 sets for shared machine keys, 'you may not expire a shared key whose holders you have not counted'. THE GENERAL SHAPE: a control keyed on a property the EDGE injects can only protect paths that traverse the edge, so the coverage of the control is bounded by the coverage of the ROUTING, and nothing in the face or the decomposition checks that the two sets match. The face measured 39 methods and 1 authorizer; nobody measured how many of the 39 have a path along which the key can arrive.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S81",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "NO INSTRUMENT AVAILABLE TO A SITE-Z SEAT CAN ESTABLISH WHETHER AN AWS SERVICE PRINCIPAL SENDS aws:SourceArn, WHICH IS THE EXACT FINDING TO-OP-S-29's FLOOR REQUIRES BEFORE THE CONDITION MAY BE ADDED. The floor says SourceArn ONLY where the service supports it, MEASURED per service and NEVER ASSUMED, because an asserted SourceArn is how C-16 reached its wrong state. Three instruments were tried and all three fail: egress to AWS documentation is prohibited by CLAUDE.md, a census of ALL 34 bucket policies in this account found ZERO other grants to either principal to learn from, and no AWS API reports which request-context keys a service principal sends. The floor's own fallback -- add only SourceAccount -- was taken, which is the CORRECT and CONSERVATIVE outcome; what is missing is not the remedy but the ability to produce the MEASURED NEGATIVE the criterion asks for, as distinct from an unestablished one.",
    "evidence": [
      "THE THREE INSTRUMENTS, each tried and each recorded rather than assumed absent. (1) AWS DOCUMENTATION: CLAUDE.md's Agent Autonomy section excludes all egress off Opal infrastructure and requires Andrew's explicit per-use word for any external vendor call, so the documented-behaviour half of the floor's own wording is unavailable to this seat by rule, not by oversight. (2) ESTATE PRECEDENT: a census of every bucket policy in the account -- 34 buckets enumerated by list-buckets, each get-bucket-policy read -- found exactly ONE bucket naming either principal, and it is opal-data-security itself, the subject. Zero other examples to learn from. (3) LIVE API: no wafv2, s3, elbv2 or logs call reports which request-context keys a service principal populates.",
      "THE ONE MEASURED POSITIVE THAT IS IN HAND, and its limit: the CloudFront leg was delivering at the moment of this work -- 79 objects under waf-logs/cloudfront-access/, newest 2026-09-03T20:48:26Z -- through a grant that ALREADY carried aws:SourceAccount. A condition the service did not satisfy would DENY the delivery, so delivery.logs.amazonaws.com demonstrably sends aws:SourceAccount. That establishes ONE key for ONE principal and says nothing about SourceArn for either.",
      "WHY THE ALB HALF COULD NOT BE INFERRED THE SAME WAY: its grant carried NEITHER condition before this task order, so its continued delivery proved nothing about which keys it sends. That asymmetry is why adding aws:SourceAccount to it was the risky half of this change and why S29-AC3 grades that leg on a delivered object with no UNCOMPUTABLE branch.",
      "AN ORACLE EXISTS FOR THE ALB AND WAS DELIBERATELY NOT USED, because using it would have inverted the criterion's required order: s3.tf:141-147 records that elbv2 modify-load-balancer-attributes performs a TEST WRITE and fails loudly if the bucket policy does not permit it. That could test a SourceArn condition empirically -- but only by ADDING the condition first, and S29-AC2 states that a SourceArn added without a prior finding is a FAIL even if the policy applies cleanly. Using the oracle to manufacture the finding that licenses the condition is the circularity the criterion exists to forbid.",
      "WHAT WAS ACTUALLY DONE, so the row is not read as a failure to deliver: aws:SourceAccount was added to BOTH grants (the floor's non-negotiable half, verified on the applied plane, denominator 2 of 2) and aws:SourceArn was added to NEITHER. That is exactly what the floor prescribes when support is not established -- SourceArn ONLY where the service supports it."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS INERT RATHER THAN ARMED: nothing is at risk and nothing is blocked. The floor's fallback IS the correct outcome and it was taken; the change is applied and both grants carry SourceAccount. What the row records is that the criterion asks for a distinction -- MEASURED NEGATIVE versus NOT ESTABLISHED -- that this seat cannot make with the instruments it is permitted, and filing an unestablished finding as a measured one would be the same overreach in the opposite direction that produced C-16's defect. TWO CHEAP SHAPES FOR WHOEVER OWNS IT, neither taken here: authorise a single documentation read for this narrow question, which is an egress decision and Andrew's; or accept the empirical route explicitly by amending S29-AC2 to permit the ALB enablement-oracle as the finding, which makes the circularity a ruled sequence rather than a violation. THE REUSABLE PART: a criterion can demand a category of evidence that the executing seat's permission envelope forbids it from producing, and the failure then looks like sloppiness rather than a boundary. The tell is that the conservative action and the unverifiable one are the SAME action -- adding only SourceAccount is both what a measured negative would license and what an inability to measure forces -- so the record must say which of the two it is, because they are not the same claim.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S83",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Z-S82 STATES THE EDGE-COVERAGE RULE FORWARD ONLY -- 'any FUTURE endpoint ... states that intersection at L2 or L4' -- AND THE RULE HAS ALREADY BEEN VIOLATED BEHIND IT, IN A FACE THAT IS COMPLETE, ACCEPTED AND APPLIED. TO-OP-S-2 attached the origin-gated authorizer to nine HTTP-API routes at 16:24:34Z today. EIGHT sit under the /v1/* behavior. THE NINTH, GET /metadata/yang (route t81twif), HAS NO ORDERED CLOUDFRONT BEHAVIOR AT ANY DEPTH, so the X-Opal-Origin-Verify header its authorizer demands cannot arrive by any path -- the exact condition Z-S80 halted limb 2 to avoid, already shipped on a different API five hours earlier. S2-AC1 could not have caught it: its denominator is '9 of 9 ATTACHED', which measures ATTACHMENT and never REACHABILITY. NO CALLER IS IDENTIFIED, so this is a latent trap and NOT a demonstrated outage -- stated that way deliberately, because the caller enumeration that would settle it is exactly the bar Z-S82 sets for shape (B).",
    "evidence": [
      "INSTRUMENT AND POPULATION, both complete rather than sampled. aws apigatewayv2 get-routes --api-id 7k3ed8px20 --max-results 500: 72 routes, NextToken None, so this is the POPULATION and not a page. aws apigatewayv2 get-authorizers: authorizer DENOMINATOR 1 -- naqxlm portal-jwt-authorizer, REQUEST, payload 2.0 -- so every gated route is gated by the ONE authorizer that carries the origin check, with no second authorizer to explain the two away. aws cloudfront get-distribution-config --id EVTSA9VEHNZVH: 7 origins, exactly one (APIGateway-portal) fronting 7k3ed8px20, and 27 ORDERED behaviors evaluated in precedence order.",
      "THE INTERSECTION, computed over the full cross-product rather than over the nine: of 69 authorizer-gated routes, exactly TWO have no ordered behavior whose target is APIGateway-portal -- `$default` and `GET /metadata/yang`. Both fall through to the DEFAULT behavior, whose target is S3-opalinvest-portal, the SPA bucket. This is the same shape Z-S80 measured on the REST side and Z-S82 restated as an issuance rule.",
      "ATTRIBUTION, and it is this project's act rather than a pre-existing condition. The TO-OP-S-2 deploy-completion record (org/critical_paths/change_management/20260903T1605Z_opsec-s2-http-api-authorizer-nine-routes_deploy_completion.md, leg L4, CLOSED 20260903T162435Z) enumerates the nine attached routes by id, and `GET /metadata/yang t81twif` is one of them. Before that apply the route read AuthorizationType NONE. The same record's BEFORE/AFTER is CUSTOM 60 -> 69 of 72.",
      "THE DISTINCTION THAT KEEPS THE COUNT HONEST, because the two are not the same finding: `$default` is a CATCH-ALL whose closure at the raw address is precisely what FWD-2 intends, and gating it with no edge path is the DESIRED outcome, not a defect. Only GET /metadata/yang is a named data route. So the load-bearing number here is ONE route, not two, and a row that reported 'two broken routes' would be overstating its own measurement.",
      "CALLER ENUMERATION over the repo corpus, reported with its limit. comp-find 'metadata/yang' across 51,568 files: the portal does NOT call this route -- portal/src/contexts/YangDataContext.tsx:45 fetches /api/general/metadata/yang.json, which the /api/general/* behavior serves from the S3-opal-data-portal-v2-json ORIGIN and which never touches the HTTP API. No repo caller of the bare GET /metadata/yang was found. THE LIMIT, stated because it is the whole weight of the claim: the repo corpus cannot see a caller that is not in this repo, and the access-log plane -- which can -- was not read by this seat.",
      "A SECOND AND SEPARABLE EXPOSURE ON THE SAME NINE, which no row has yet named: infra/aws/scripts/make-metadata-endpoint-public.sh is a committed script whose header reads 'Create a public route for /metadata/yang endpoint (no auth required)' and which sets GET /v1/metadata/yang to authorization-type NONE, verifying with an anonymous curl. That route (mxus2bs) is ALSO one of the nine and is now CUSTOM. It IS CloudFront-reachable, so a bearer-carrying browser is unaffected -- but an ANONYMOUS consumer of a deliberately-public endpoint is now refused at BOTH doors: 403 at the raw address by the origin gate, 401 through CloudFront by auth-validator-edge. Whether such a consumer exists is the same unenumerated question."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS NOT A RE-GRADE OF TO-OP-S-2. S2-AC1 is PASS and stays PASS: it claimed attachment on 9 of 9 and attachment on 9 of 9 is what the live plane reads. Nothing in that instance is false. The gap is that ATTACHED and REACHABLE are two different properties and the face only ever had a criterion for the first -- the same GRAIN split Z-S80 found, one API over and one plane later. A DEFECT IN WHAT THE MEMBERS SHARE IS INVISIBLE TO A CHECK SCOPED TO THE MEMBERS: nine per-route checks all passed while the property they shared -- an edge-injected key with no edge path for one of them -- went unmeasured, which is CLAUDE.md Rule 22's shared-dependency clause with a live specimen. WHAT I DID NOT MEASURE, so no reader infers it: I did not probe either endpoint (the OP-x-1 list is CLOSED at seven and an eighth probe is not on it), I did not read the access logs, and I therefore CANNOT say whether anything is actually broken -- only that a route is gated on a key that cannot reach it. A 403 on GET /metadata/yang would confirm the mechanism in one request for whoever holds that authorization. WHY IT IS FILED AS ARMED ANYWAY: the harm from being wrong is asymmetric and cheap to bound. If a caller exists it has been failing since 16:24:34Z; if none exists the disarm costs one log read. THE PART WORTH KEEPING FOR L9, and it is about the rule rather than the route: a rule stated FORWARD at the moment it is learned leaves every act already taken under the old understanding unexamined, and those are exactly the acts nobody will revisit, because they are CLOSED and their criteria all read PASS. When a round promotes a finding to an issuance rule, the same turn should ask which COMPLETED faces the new rule would have failed. Here it is two faces, one route, and about ten minutes of reading.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S84",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A PARTIAL DISARM IS INDISTINGUISHABLE FROM A FULL ONE, AND THE ERROR RUNS IN THE DIRECTION THAT HIDES LIVE HAZARDS. The protocol says a reader resolves a row's state from the NEWEST ROW CITING IT. Z-S82 is the newest row citing Z-S80 and it disarms the EXECUTION half only -- its own text says the endpoint-shape half 'is expressly NOT disarmed here' and is routed to 1.0.0_SA_CTO~Z. This seat's resolved-state census reads Z-S80 as DISARMED anyway, because the resolution rule has no grain finer than the row. The schema cannot express the distinction either: it is additionalProperties:false with NO field for what a row disarms, so across all 83 rows the only structured citation field in existence is `adjudicates` and it appears on 2 rows, both this seat's. Every disarm in this round -- all twelve of them -- is carried in PROSE, and a partial one is prose that no consumer can reject on.",
    "evidence": [
      "THE SPECIMEN, quoted from Z-S82's own surfaced_by at HEAD: 'A DISARM RECORD for the EXECUTION half only -- the ENDPOINT-shape half is routed to 1.0.0_SA_CTO~Z at L4 and is expressly NOT disarmed here.' The row is scrupulous and says exactly what it does. The defect is entirely in what a RESOLVER can see, not in the row.",
      "THE INSTRUMENT AND ITS FAILURE, measured on this seat's own script rather than asserted: a resolver that walks every ARMED row, finds later rows citing it by full id (word-boundary matched, with a positive control that Z-S79 cites Z-S75 and a negative control that it does NOT match Z-S7 inside Z-S75), and classifies on disarm language, returns Z-S80 in the DISARMED set. Denominators at this vintage: 83 rows, 30 raw-ARMED, 26 read as disarmed, 4 read as live.",
      "AND THE OTHER INSTRUMENT FAILS IN THE OPPOSITE DIRECTION, which is why quoting either number alone misleads: comp-surprise does not resolve at all. It prints the raw `hazard_standing` field, so it reported ARMED 28 at the 79-row vintage and 30 now -- rows that were disarmed hours ago still counted as armed, because the channel is append-only and a disarm lands as a LATER row. So the two available numbers for one question are 30 and 4, one overstating live hazards and one understating them, and the true figure is neither.",
      "THE SCHEMA CANNOT CARRY THE FIX AS IT STANDS, measured at org/surprise_channel/schemas/investigation_item.schema.json: additionalProperties is false and the property set contains no `disarms`, `resolves` or `cites`. `adjudicates` exists but is documented as the L9 ADJUDICATION CARRIER whose effect is to set the named items' disposition -- it is the CVO's, so an issuer filing a disarm cannot legally use it and is left with prose by construction. A key census over all 83 rows: `adjudicates` present on 2 (both this seat's, at the round-1 stamp), `disarm_owner` on 36, and no other citation field at all.",
      "SO THE GAP IS STRUCTURAL RATHER THAN ANYONE'S OVERSIGHT: the schema REQUIRES a disarm_owner whenever hazard_standing is ARMED, which is the one act it obliges, and provides no field in which the discharge of that act can name its own subject or its own scope."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THIS IS FILED NOW RATHER THAN AT L9. The census is the instrument this seat has already put on the record as the one L9 will use, and it is wrong in the direction that hides hazards; an overcount of disarms never announces itself, whereas an undercount would. Filing it while the specimen is fresh costs one row and removes the chance that the L9 reader -- this seat -- trusts its own tool. NOT PROPOSED AND DELIBERATELY SO: a schema edit. That is 1.0.0_SA_CTO~Z's surface, adding a field mid-round changes the gate for every seat writing rows right now, and CLAUDE.md forbids manufacturing friction on a round that is mid-flight. If the owner ever wants one, the smallest shape that would close it is a `disarms` array of ids paired with a `disarm_scope` free string, which makes a PARTIAL disarm expressible rather than merely careful -- offered as a note, not as a proposal, and not implemented. WHAT I AM NOT CLAIMING: that any disarm in this round is wrong. Every one this seat has read is sound on its own terms, and Z-S82 in particular is the most careful of them -- it is the row that made the defect visible precisely BECAUSE it stated its own scope so exactly. A less careful row would have disarmed the whole item and nobody would ever have known the difference. THE GENERAL SHAPE, which is the part worth keeping: when a state is conferred by one object on another, the conferring object needs somewhere to say HOW MUCH of the state it moves. Without that field the vocabulary can only express all-or-nothing, and every partial act gets rounded -- silently, and always toward done.",
    "owner": "3.0.0_SA_CVO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "3.0.0_SA_CVO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "3.0.0_SA_CVO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S85",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "THE PLAN-WIDE 0-DESTROY AND 0-FORCES-REPLACEMENT BINDS CANNOT SURVIVE ANY BODY CHANGE ON A BODY-MANAGED REST API. An aws_api_gateway_deployment is immutable and its trigger is the body hash, so every body change REPLACES it -- add plus destroy. Limb 2's plan reads 4 to add, 3 to change, 1 to DESTROY with forces-replacement 1, and the single replacement is that deployment. The Z-S56 SCOPED bar is fully met; only the two plan-wide clauses fail.",
    "evidence": [
      "THE MEASURED PLAN, portfolio-management, after the body change and before any apply: 'Plan: 4 to add, 3 to change, 1 to destroy', forces-replacement count 1. The change set in full: aws_api_gateway_deployment.opal_portal_api MUST BE REPLACED; aws_api_gateway_rest_api.opal_portal_api updated in-place; aws_api_gateway_stage.prod updated in-place; aws_api_gateway_stage.production updated in-place; aws_cloudwatch_log_group.portal_rest_authorizer created; aws_lambda_function.portal_rest_authorizer created; aws_lambda_permission.rest_authorizer_invoke created.",
      "THE SCOPED BAR IS MET IN FULL, which is what isolates the finding to the two plan-wide clauses. Among the IMPORTED objects -- the REST API, both stages, and by extension the methods carried in the body -- the count of created, replaced or destroyed is ZERO for each, measured per resource. The API's own diff is the single attribute '~ body'. Nothing that was imported is being recreated, which is the hazard Z-S14 was written against.",
      "WHY THE REPLACEMENT IS STRUCTURAL AND NOT A DEFECT IN THE DECLARATION: the plan names the cause explicitly -- 'triggers = { - redeployment = 09d7d243... } -> (known after apply) # forces replacement'. An aws_api_gateway_deployment is IMMUTABLE by AWS design; the trigger is sha1 of the body; the body changed because limb 2 attaches the authorizer to 19 operations. There is no declaration that both ships a body change and leaves the deployment in place. Removing the trigger would be worse: body changes would then never reach a stage at all, which is a silently-broken deploy rather than a noisy one.",
      "THE NO-GAP PROPERTY, verified at source rather than assumed: rest-api.tf:85-87 declares lifecycle { create_before_destroy = true } on that deployment. The new deployment is therefore created, and the stages repointed onto it, BEFORE the old one is destroyed. The destroy is of an object nothing is serving from by the time it happens.",
      "THIS IS NOT A ONE-OFF AND THAT IS THE POINT. Limb 1 CREATED the deployment (1 add, 0 destroy) because none existed, which is why the Z-S56 ruling enumerated a deployment CREATE as pre-authorised and had no reason to consider a REPLACE. From limb 1 onward the resource exists, so EVERY subsequent body change on this API -- limb 2's authorizer, any future route or method change, any later face -- produces exactly this add-plus-destroy. A bar that no future body change can satisfy will either block every one of them or be quietly ignored, and the second outcome is the dangerous one.",
      "WHAT IS AND IS NOT DONE: the REST authorizer source, its Terraform and the body attachment are written and the artifact is built and uploaded (sha uA2YiEByRypFxsBGWDh+ytEpV5xxUtqifYCSt+POZhQ=, one file, the shared module's strings verified inlined and no second copy of the read). NOTHING IS APPLIED. Unlike limb 2a, the upload arms nothing here: the Lambda it feeds does not exist until the apply creates it, so the artifact sitting in S3 changes no behaviour."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): RECOMMENDATION, offered and NOT taken: enumerate the aws_api_gateway_deployment REPLACEMENT as a third pre-authorised exception alongside the two the Z-S56 ruling already names, scoped to that ONE resource address, and make it STANDING for this API rather than per-face -- because it recurs on every body change and a per-face exception would have to be re-granted forever. The plan-wide clauses keep their whole protective value against everything else: any OTHER destroy, any OTHER forces-replacement, and any created-or-replaced imported object all remain a STOP. THE ALTERNATIVE THAT LOOKS TIDY AND IS WORSE, named so it is not re-derived: dropping the redeployment trigger would produce a plan with 0 destroy and 0 forces-replacement on every future body change -- and the body would never actually reach a stage. That is a bar bought by disabling the mechanism it was meant to supervise. THE GENERAL SHAPE, the third instance of it on this face: a numeric bar written against one operation's shape (a pure import, then a first create) silently becomes unsatisfiable when the same face's next operation has a different shape, and nothing re-checks the premise when the operation changes.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S90",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "TO-OP-S-20's GO CONDITION FAILS AND THE FACE STOPS: the observation window is long enough (19.7 days) but the SIGN-IN traffic in it is TWO EVENTS. An exact-path query over 111,904 WAF records returns /auth/login = 2, /auth/forgot-password = 0, /auth/reset-password = 0. THE DANGEROUS PART IS WHAT A NAIVE CENSUS WOULD HAVE PRODUCED: a substring match on 'auth' returns 2,990 records and 60 distinct client addresses, and that list is overwhelmingly INTERNET SCANNER TRAFFIC -- its top entry is 176.125.242.75 (Moldova) with 2,357 hits, alongside one-off addresses from HK, NL, BE, MN and SG. Building allowlists/partner-egress.json from that census would have ALLOW-LISTED AN ATTACKER into the very control C-4 exists to protect. Separately and independently fatal: no field in the WAF log attributes an address to a FIRM, so a per-firm census is not expressible from this source at all.",
    "evidence": [
      "THE WINDOW IS NOT THE PROBLEM, measured first because the face's GO condition asks for it: the gateway WAF log group aws-waf-logs-opal-gateway spans 2026-08-15T02:56:15Z to 2026-09-03T20:47:25Z -- 19.7 days -- holding 84,723,696 bytes at 90-day retention. 111,904 records were scanned by the queries below. That is a usable window by any reading.",
      "THE SIGN-IN TRAFFIC IN IT IS TWO EVENTS. A CloudWatch Logs Insights query over that full window filtering on EXACT paths returns: /auth/login 2 hits, /auth/forgot-password 0, /auth/reset-password 0. Denominator printed by the service itself: recordsScanned 111904, recordsMatched 2. Those three paths are the portal's sign-in surface, taken from the AuthLoginRateLimit rule's own scope-down statement in portal-auth/waf-cloudfront.tf rather than guessed.",
      "WHAT A NAIVE CENSUS WOULD HAVE PRODUCED, and this is the part worth the row: the same query with a SUBSTRING filter (uri like /auth/) returns recordsMatched 2,990 and 60 distinct (clientIp, country) pairs. Ranked by hits the list opens 176.125.242.75 MD 2357, 108.242.96.89 US 268, 8.210.98.232 HK 94, 103.153.183.69 US 50, 94.154.46.247 US 32, then a long tail from NL, BE, MN, SG and elsewhere. A sampled record shows what these are: uri /owa/auth/x.js, User-Agent zgrab/0.x, Host set to the ALB's raw IP 54.197.48.56 -- Outlook-Web-Access probe traffic from an internet scanner, not a partner office. The substring and the exact match differ by a factor of 1,495 and only the exact one is the population the cell means.",
      "THE SECOND, INDEPENDENT BLOCKER -- NO FIRM ATTRIBUTION EXISTS IN THE SOURCE. The WAF log record's httpRequest carries clientIp, country, uri, httpMethod, args and headers. The headers present on a sampled record are Host, User-Agent, Accept, Cookie and Accept-Encoding, and COOKIE READS 'REDACTED' -- by OP-s-5's own deliberate redaction, which exists so the security log is not the estate's largest bearer-token collection. The auth handler is separately IP-blind (brief F4). So nothing in this source maps an address to one of the four partner firms, and a per-firm census is not merely sparse here, it is INEXPRESSIBLE.",
      "THE EXPECTED FIRM SET, read live rather than recalled as S20-AC1 requires: dynamodb list-tables returns opal-partner-49financial, opal-partner-cottonwood, opal-partner-demo, opal-partner-inflection -- 4 firms, with ItemCounts 11, 4, 7 and 1. Under any honest census against this source all 4 would file as 'log coverage unknown for this path', i.e. firms observed 0 of 4.",
      "THE OTHER TWO SOURCES CANNOT RESCUE IT, measured not assumed. aws-waf-logs-opal-cloudfront -- the group fronting the PORTAL, which is where sign-ins actually land -- holds storedBytes 0 and was created today. The S3 access logs under waf-logs/ start 2026-09-03T09:43:36Z and 09:49:06Z, an 11.5-hour window, and they record BUCKET access rather than application sign-ins. So the surface with the long window is the gateway ALB (a JSON-RPC/OAuth surface), and the surface that carries sign-ins has no usable log at all."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THE LIST WAS NOT BUILT AND NOTHING WAS ARMED. No allowlists/partner-egress.json was written, no ALLOW row was added to the S16 table, no IP set was touched -- S20-AC5's bounds hold trivially because the face stopped at its own GO condition. WHAT MAKES THIS WORTH A BLOCKING ROW RATHER THAN A NOTE: C-4 makes arming BLOCK with zero ALLOW rows a VIOLATION, so OP-s-14's sentinel stays blocked behind this, and the honest position is that it should. The alternative -- shipping a 60-entry list to unblock the sentinel -- would have inverted the control: C-4 exists so that a missing observation does not lock out a partner office, and a list built from this data would instead have ADMITTED the scanner that is probing the estate hardest. A control that is supposed to prevent a lockout would have become a persistent allow for hostile traffic. THREE SHAPES FOR THE ISSUER, none taken here because each is a scope or sequencing decision: (a) WAIT for a genuine window -- but note that waiting fixes sparseness and does NOT fix the missing firm attribution, so this alone is insufficient; (b) get the sign-in surface logged -- the CloudFront WAF group is empty and the portal is where sign-ins land, so OP-s-5's coverage may need extending before this cell is buildable at all; (c) SOURCE THE CENSUS ELSEWHERE -- if firm attribution is required, the data must come from something that knows the tenant, which the WAF layer structurally does not, and that is a cell-shape question rather than a query question. THE REUSABLE PART: A SUBSTRING FILTER AND AN EXACT FILTER DIFFERED BY 1,495x ON THE SAME RECORDS, and the substring version produced a longer, more confident-looking, and completely wrong answer. The denominator is what separated them -- 2,990 matched versus 2 matched over an identical 111,904 scanned -- and the cell was right that the denominator is as much the deliverable as the list.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S91",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "ISSUER RECORD for NFRA_OPSEC202609-Z-S90, AND IT IS EXPRESSLY NOT A DISARM. Z-S90 stays BLOCKING and ARMED because OP-s-20 IS UNBUILDABLE AS DECOMPOSED and the remedy sits at L4. TITLING THIS A DISARM RECORD WOULD MAKE THIS SEAT'S OWN CENSUS READ CLEAN ON A LIVE HAZARD -- the exact instrument failure this round has met three times already (a refused delivery presenting as an empty prefix, a halt gate reading an empty decoy, an access-log plane that does not exist) -- so the row STAYS FLAGGED as lacking a disarm, because it lacks one. WHAT THIS SEAT DID RULE: (1) the assignee's stop was correct and its exact-versus-substring divergence is the finding -- 2 records against 2,990 across 60 addresses, 1,495x, led by a Moldovan host at 2,357 hits that a sampled record identifies as an internet scanner (/owa/auth/x.js, zgrab/0.x, Host set to the ALB's raw IP), so writing the substring answer to partner-egress.json would have INVERTED C-4 by permanently admitting the address probing this estate hardest; (2) TO-OP-S-14-21's GO CONDITION IS CORRECTED at 522b777935 -- it no longer waits on TO-OP-S-20, because C-4 forbids ARMING BLOCK with zero ALLOW rows and does not forbid BUILDING the sentinel in WATCH mode, and this seat's original gate would have parked the project's largest cell behind one that may never complete; (3) the cell-shape question is routed to 1.0.0_SA_CTO~Z at L4.",
    "evidence": [
      "0.7.0_AE_CloudOps~S row Z-S90 @daea6764a6 and message 20001: recordsScanned 111904 / recordsMatched 2 on the exact query, against recordsMatched 2990 and 60 distinct addresses on the substring query over identical records",
      "the sampled scanner record: uri /owa/auth/x.js, User-Agent zgrab/0.x, Host set to the ALB's raw IP; 176.125.242.75 MD at 2357 hits leading the substring list",
      "the redaction and the blindness, both this project's own prior work: OP-s-5's deliberate Cookie redaction, and throttle.ts:14 read at this seat while cutting OP-s-7 -- 'the Lambda cannot see the real client IP -- /auth/* forwards no CloudFront-* headers'",
      "the corrected gate: TO-OP-S-14-21 at 522b777935; the cell-shape question routed to 1.0.0_SA_CTO~Z in message 20003"
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): THE STRUCTURAL SHAPE, which neither the assignee nor this seat had named and which is the durable part: THE LAYER THAT KNOWS THE ADDRESS DOES NOT KNOW THE TENANT, AND THE LAYER THAT KNOWS THE TENANT DOES NOT KNOW THE ADDRESS. The WAF sees clientIp and no firm; the auth handler knows the account and is blind to the IP. C-4 asks for a join across a boundary nothing currently crosses. AND THEY HAVE A COMMON CAUSE THIS PROJECT ALREADY MEASURED TODAY FOR A DIFFERENT CELL: /auth/* forwards no CloudFront-* headers, which is simultaneously why OP-s-7's login throttle is IP-blind and why OP-s-20's census is inexpressible. TWO CELLS, TWO OUTCOMES, ONE UPSTREAM DEFECT -- and neither cell names it, because neither was looking at the other. It surfaced only because both crossed this seat within a few hours, which is an argument for the issuer reading its own cells against each other rather than only against the PRD. THE L5 DEFECT IS THIS SEAT'S: OP-s-20 was decomposed assuming a join its named source cannot perform. THE L6 DEFECT IS ALSO THIS SEAT'S AND IS THE MORE EXPENSIVE ONE: gating the sentinel's BUILD on a list that only its ARM requires. THE NEAR-MISS WORTH KEEPING: a loose matcher here would not have added noise, it would have turned a safety list into an attacker's allow entry -- and the loose answer was the longer, richer and more confident-looking one. A census whose matcher is wrong in the permissive direction fails toward MORE data, which reads as better evidence.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S97",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "C-6's NAMED RECIPIENT IS AN INPUT THIS PROJECT DOES NOT HOLD, AND THE FACE SAYS SO IN WRITING. FWD-4's DONE WHEN is that a human receives the login-abuse alarm; the alarms, the topic and the metric filter are all buildable without that name, but the SUBSCRIPTION is not. This row is the gap, filed BEFORE the build rather than after, so that the single open leg is visible as a named absence and not as an alarm that appears wired. The recipient is NOT guessed, NOT defaulted to Andrew, and NOT set to a role address -- a notification wired to a guessed address reads as delivered and reaches nobody, which is strictly worse than the absent subscription this row records.",
    "evidence": [
      "THE FACE ITSELF DECLARES THE GAP, so this row records it rather than discovering it. TO-OP-S-6 deliverable 2 @170f8611d2: 'This face does NOT name that person, because the issuer does not have the name. DO NOT PICK ONE, DO NOT USE A ROLE ADDRESS, DO NOT USE ANDREW'S ADDRESS BY DEFAULT. File a ROW naming the gap and send the issuer a message asking for the recipient, then build everything else and leave the subscription as the single open leg.'",
      "THE ACCEPTANCE CRITERION IS ALREADY WRITTEN TO ABSORB THIS, so the gap blocks the criterion and not the task order: S6-AC3 reads 'If the recipient is still unnamed, this files UNCOMPUTABLE-BY-CONSTRUCTION citing the row from deliverable 2, and the flip waits on nothing else.' This row is that citation.",
      "WHAT IS BUILDABLE WITHOUT THE NAME, measured rather than assumed -- an SNS topic is creatable with zero subscriptions and CloudWatch alarms may name a topic ARN as an AlarmAction with no subscriber attached, so deliverable 1 (both alarms), deliverable 3's topic, the metric filter, the staged burst of deliverable 4 and S6-AC1/AC2/AC4/AC5 all complete on their own. The ONLY leg that requires the name is aws sns subscribe.",
      "WHY THE ROW IS ARMED RATHER THAN INERT: an unsubscribed topic is the exact shape that reads healthy from every configuration probe. describe-alarms will show AlarmActions populated, the topic will exist in terraform state, and the alarm will transition to ALARM on the burst -- and NOBODY WILL BE TOLD. The hazard is not that the build is wrong; it is that the build looks complete. It stays ARMED until a human is actually reached."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): FILED BEFORE THE BUILD, DELIBERATELY. The tempting order is to build first and record the gap at proof-writing time, but the row is what makes the absent subscription legible to anyone reading the applied world in the interim -- and the interim is where the risk lives, because between the apply and the disarm there will be two live alarms on the authentication path whose notifications reach no one. A reader of the AWS console in that window sees a fully-formed alarm with an SNS action and has no reason to look for a subscriber count of zero. THE ASK IS ONE FACT: the email address of the person who should receive login-abuse alerts. This seat has messaged 2.0.0_SA_COO~Z for it and does not proceed to a substitute of any kind while waiting.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S98",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "PHASE-1 RE-GROUNDING OF TO-OP-S-6: three of the face's four live premises re-measure EXACTLY and one has moved (WAFV2 metrics 364 -> 377), and separately the re-grounding turned up TWO INSTRUMENT TRAPS THAT CHANGE WHAT GETS BUILT -- the auth handler logs in Text format so a JSON metric-filter pattern would match ZERO while deploying green, and the CloudFront-scope WAF metrics carry NO Region dimension, so an alarm written with one would never fire. Both traps produce a deployed, healthy-looking, permanently silent alarm, which is the same failure shape as the unsubscribed topic in Z-S97 one layer down.",
    "evidence": [
      "PREMISE 1, EXACT MATCH AND IT IS THE ONE THAT CARRIES A CRITERION: describe-alarms returns 49 MetricAlarms + 0 CompositeAlarms = 49, against the face's 49. NextToken is ABSENT from the response, so 49 is a true denominator and not a page count -- the CLAUDE.md 22a paginated-list trap was checked rather than assumed. The composition also matches the face's reading: exactly 5 FIRMSEP-* and exactly 2 *-throttles alarms. This is the before-denominator S6-AC1 names, and it needs no substitution.",
      "PREMISE 2, THE DIFFERENCE: list-metrics --namespace AWS/WAFV2 --region us-east-1 returns 377 metrics (NextToken absent, complete listing), against the face's 364 read at 19:2xZ. Measured 23:0xZ, about 3.5 hours later. DIRECTION AND MEANING: the face cites 364 to establish that 'the WAF metric plane is live and emitting'. 377 confirms that premise MORE strongly, not less, and CloudWatch metric inventories only grow as new dimension combinations emit. The number is NOT a denominator for any acceptance criterion -- only the 49 is -- so nothing is substituted and no criterion changes. Recorded as a difference because the face says to record differences, not because it disturbs anything.",
      "PREMISE 3, EXACT MATCH, READ ON THE OBJECT AND NOT THE METRIC PLANE: wafv2 get-web-acl on opal-cloudfront-protection (id a09833c0-4043-49fc-a92c-0dcdeaff9abd, CLOUDFRONT scope) returns 6 rules; AuthLoginRateLimit is at Priority 2 with Action Block and CloudWatchMetricsEnabled true, exactly as the face states. THIS NEEDED THE RIGHT PLANE: a census of the 377 metrics for a Rule=AuthLoginRateLimit dimension returns ZERO, which reads as 'the rule does not exist' and is NOT what it means -- a WAF rule emits no rule-scoped metric until it first matches, and this rule has never blocked anything. POSITIVE CONTROL that the probe itself works: the same matcher against Rule=RateLimitRule returns 1 metric (BlockedRequests), so the Rule dimension and the matcher are both sound and the AuthLoginRateLimit zero is a true never-fired, not a broken pattern.",
      "PREMISE 4, EXACT MATCH: git ls-files resolves infra/aws/terraform/portal-auth/cloudwatch-alarms.tf (260 lines) -- the carrier is tracked as the face states.",
      "TRAP A -- THE METRIC FILTER PATTERN, and it would have shipped silently. lambda get-function-configuration on opalinvest-auth-handler returns LoggingConfig.LogFormat = 'Text' (runtime nodejs22.x). Raw log events read from the live stream confirm the consequence at source: a console.log line arrives as '2026-09-03T22:57:52.878Z\\t0185da27-fbda-4818-9e9d-6c08670e281b\\tINFO\\tPOST /auth/refresh\\n' -- an ISO timestamp, a request id and a level, TAB-separated, BEFORE the payload. The emitter at infra/aws/opalinvest_dev/lambda/auth-handler/src/throttle.ts:118 writes console.log(JSON.stringify({event:'auth_throttled',...})), so the JSON object is a SUFFIX of the line and never the whole line. A CloudWatch JSON metric-filter pattern of the form { $.event = \"auth_throttled\" } requires the ENTIRE message to parse as JSON; against a Text-format line it matches ZERO, forever, while terraform applies clean and the filter appears in describe-metric-filters. The correct pattern for this group is the quoted-substring form.",
      "TRAP B -- THE ALARM DIMENSIONS. Enumerated from the live metric plane: every AWS/WAFV2 metric carrying a Rule dimension for WebACL=opal-cloudfront-protection has EXACTLY TWO dimensions, WebACL and Rule, with NO Region -- while the REGIONAL ACL opal-gateway-waf carries THREE, WebACL + Region + Rule. 11 of 377 metrics carry a Rule dimension at all. An alarm on the CloudFront ACL written with a Region dimension (the shape a reader would copy from the regional sibling, and the shape the AWS docs describe for the general case) matches no metric and sits in INSUFFICIENT_DATA permanently.",
      "BASELINE FOR S6-AC4, taken before any write: describe-metric-filters on /aws/lambda/opalinvest-auth-handler returns an EMPTY metricFilters list, so this task order's filter will be the first on that group and the after-count is unambiguous. The log group itself is confirmed on the applied plane: describe-log-groups returns exactly 1 group named /aws/lambda/opalinvest-auth-handler, retention 30 days. The name was READ LIVE as deliverable 1(b) requires and not inferred from the function name -- though in this instance they coincide, and 6 different Lambdas in this account carry 'auth' in their names, so the coincidence was worth confirming rather than assuming.",
      "AND THE storedBytes TRAP THE ISSUER WARNED ABOUT REPRODUCED EXACTLY, which is worth recording as a second confirmation of Z-S93: describe-log-streams on the auth handler group returns storedBytes 0 on all three most-recent streams while their lastEventTimestamp is 2026-09-03T22:57:53Z, i.e. seconds old and plainly live. lastEventTimestamp is the delivery oracle; storedBytes at STREAM grain is not."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY THE TWO TRAPS ARE FILED TOGETHER WITH THE RE-GROUNDING RATHER THAN SEPARATELY: they were found BY the re-grounding and they share one signature with each other and with Z-S97 -- each produces an alarm that is deployed, configured, visible in every describe-* call, and permanently silent. The face's own warning about a guessed recipient ('it reads as delivered and reaches nobody') is the same sentence one layer down: a JSON pattern against a Text log, and a Region dimension against a global ACL, both read as delivered and reach nobody. THE CLASS IS THE POINT: for a notification, every configuration-plane probe is anti-correlated with the thing you actually want to know, because the failure modes all live in whether the pattern MATCHES and whether a human is SUBSCRIBED, neither of which any describe-* call observes. This is why S6-AC2's staged burst is the only criterion that can discriminate, and why it is graded on the alarm transitioning rather than on the rule blocking. HAZARD IS INERT because both traps were caught before the first write and the build takes the corrected forms; nothing is armed against this seat's own work. They are recorded because the next seat writing a metric filter against any Text-format Lambda log group in this estate meets trap A, and this project alone has several. NO NUMBER IN THE FACE IS SUBSTITUTED: S6-AC1 uses the face's 49, which re-measured exactly.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S99",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "CORRECTION OF THIS SEAT'S OWN Z-S98 TRAP A, AND IT INVERTS: a CloudWatch JSON metric-filter pattern DOES match a Text-format Lambda log line whose JSON payload is preceded by a timestamp, request id and level. Z-S98 asserted it would match ZERO forever. It matches, and the negative control shows it also REJECTS every decoy -- so the JSON pattern is not merely viable, it is STRICTLY BETTER than the substring pattern Z-S98 recommended, which matches bare prose containing the token. The carrier's existing FIRMSEP filters, which Z-S98's reasoning would have condemned as silently dead, are CORRECT. Every FACT in Z-S98's trap A was true and the CONCLUSION drawn from them was false.",
    "evidence": [
      "THE DISCRIMINATING INSTRUMENT, which Z-S98 did not run before filing: aws logs test-metric-filter evaluates a pattern against supplied messages with no deployment and no state change. Pattern '{ $.event = \"auth_throttled\" }' against the REAL prefixed form -- '2026-09-03T22:57:52.878Z\\t0185da27-...\\tINFO\\t{\"event\":\"auth_throttled\",...}' -- returns a MATCH (eventNumber 1). The same pattern against the bare JSON form also matches. Z-S98 predicted zero matches for the first of these.",
      "THE NEGATIVE CONTROL, run because a test in which everything matches proves nothing about the pattern: the SAME JSON pattern against three by-intent non-matching messages -- a prefixed line whose event is 'login_failed', a prefixed plain-text line 'POST /auth/refresh', and the bare prose 'auth_throttled appears as bare prose with no json at all' -- returns matches: [] , an EMPTY set. So the pattern discriminates: it matches the target and rejects a same-shaped line with a different event value.",
      "AND THE SAME CONTROL CONDEMNS THE REMEDY Z-S98 PROPOSED: the substring pattern '\"auth_throttled\"' matches the real line, but ALSO matches decoy 3, the bare prose mentioning the token. A substring filter on this group would count any future log line, error string or stack trace containing the token as a throttle event. Z-S98 recommended the LOOSER instrument on the strength of a false claim about the stricter one.",
      "THE CARRIER ALREADY CONTAINED THE COUNTER-EVIDENCE AND THIS SEAT READ IT AS AMBIGUOUS RATHER THAN AS A REFUTATION: infra/aws/terraform/portal-auth/cloudwatch-alarms.tf declares four FIRMSEP metric filters with JSON patterns of exactly this form -- pattern = \"{ $.event = \\\"advisor_scoping_denied\\\" }\" and three siblings -- against Lambda@Edge log groups, with a header comment stating 'Logs are JSON-structured via console.log(JSON.stringify({event:\"...\", ...}))'. Under Z-S98's claim all four would be permanently silent. They are not; the claim was wrong, not the filters.",
      "WHAT REMAINS TRUE FROM Z-S98 TRAP A, unchanged and re-affirmed: LoggingConfig.LogFormat on opalinvest-auth-handler IS 'Text'; the live log events ARE prefixed with an ISO timestamp, a request id and a level, tab-separated; and throttle.ts:118 DOES emit console.log(JSON.stringify({event:'auth_throttled',...})). Every one of those was measured at source and none of them is disturbed. What was false was the inference that a JSON metric-filter pattern requires the ENTIRE message to parse as JSON. CloudWatch locates and parses the JSON portion of the line.",
      "Z-S98 TRAP B IS UNAFFECTED AND STANDS, because it rests on a direct enumeration of the live metric plane rather than on an inference about matcher semantics: every AWS/WAFV2 metric carrying a Rule dimension for the CLOUDFRONT-scope opal-cloudfront-protection has exactly two dimensions, WebACL and Rule, with no Region, while the regional opal-gateway-waf carries three. That is a measurement, not a deduction, and it is re-exercised by S6-AC2's staged burst regardless."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): FILED AS A CORRECTION ROW RATHER THAN AN EDIT, per the append-only law and following Z-S95's form: Z-S98 stands as issued and this row cites it. THE MECHANISM OF THE ERROR, which is the part worth keeping: EVERY FACT IN TRAP A WAS MEASURED AND TRUE -- the log format, the prefixing, the emit site -- and the conclusion was false, because the step from those facts to 'the pattern will not match' was a belief about CloudWatch semantics that was never itself measured. Reading the format correctly is not the same as knowing what the matcher does with it, and the true facts made the false conclusion feel evidenced. THE INSTRUMENT EXISTED THE WHOLE TIME AND COST ONE CALL: test-metric-filter is read-only, needs no deployment, and answers exactly this question; the row was filed before it was run. THE COUNTER-EVIDENCE WAS ALSO ALREADY IN HAND -- four sibling filters in the very file being edited use the pattern form being condemned -- and this seat framed that as 'either my claim is wrong or FIRMSEP is silently broken' and then, to its credit, went and tested rather than assuming the more dramatic branch. THE DIRECTION MATTERS: had this gone unchecked, the build would have shipped a LOOSER filter that over-counts, on the authentication path, feeding the project's ONLY authorised notification -- a false-positive generator on the one alarm anyone will actually read. NOTHING APPLIED WAS AFFECTED: no terraform had been written when this was caught and no state exists to roll back.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPSEC202609-Z-S1",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The L10 route handoff (.tools/prd-header-notify.py kind:route) and the L4 handoff in the same tool address BASE serials (RECIPIENT default 2.0.0_SA_COO; ROUTE_OWNER {2: 1.0.0_SA_CTO, 5: 2.0.0_SA_COO, 6: 2.0.0_SA_COO}) with no lane resolution -- on site Z every live seat is a ~Z lane and the base inboxes are unwatched, so the notification re-offers until READ to an inbox nobody reads; already exercised on this project at L4 (row 19465 QUEUED at 2.0.0_SA_COO, 0 rows at 2.0.0_SA_COO~Z).",
    "evidence": [
      ".tools/prd-header-notify.py:49 @e906c6f156 -- RECIPIENT = os.environ.get(\"PRD_NOTIFY_TO\", \"2.0.0_SA_COO\") -- a BASE serial, env-overridable for the L4 path only",
      ".tools/prd-header-notify.py:68 @e906c6f156 -- ROUTE_OWNER = {2: \"1.0.0_SA_CTO\", 5: \"2.0.0_SA_COO\", 6: \"2.0.0_SA_COO\"} -- BASE serials, no env override, no lane lookup",
      ".tools/prd-header-notify.py:364 @e906c6f156 -- the route send passes \"to\": owner straight from ROUTE_OWNER; :101 owner = ROUTE_OWNER.get(t); nothing between them consults liveness or a lane",
      "EXERCISED on this project, L4 path: get_delivery_state(message_id=19465) read at 3.0.0_SA_CVO~Z 2026-09-03T07:1xZ -> QUEUED, 1.0.0_SA_CTO~Z -> 2.0.0_SA_COO, 'no clock stamps yet'; 1.0.0_SA_CTO~Z 19471 reports 0 rows at 2.0.0_SA_COO~Z for it",
      "get_live_agents at 3.0.0_SA_CVO~Z 2026-09-03T06:49Z: 4 live -- 0.0.0_AB_MSTR~Z, 1.0.0_SA_CTO~Z, 2.0.0_SA_COO~Z, 3.0.0_SA_CVO~Z -- no base serial registered on this device; org/XXX.md: a lane's inbox is org/mcp/inbox/{base}/~{lane}/ and the base inbox is a different directory",
      "org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md v2.3 L10 Tool: '.tools/prd-header-notify.py kind:route delivers a new route row to its owner and re-offers until READ'; Handoff: 'the stamped row to the route owner and to no one else'",
      "the L4 workaround that disarms one instance: 1.0.0_SA_CTO~Z 19471 sent the same identity to 2.0.0_SA_COO~Z by message and named the QUEUED base row -- the handoff reached its owner by a second carrier, not by the notifier"
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY A ROW AND NOT A MESSAGE: it is a spec-vs-world mismatch on this project's own loop, found off-task by the seat that will run L10; the row is the carrier. NOT CHASED: no edit to the tool from this seat -- a live post-commit hook edit in the shared tree is the never-rules-gate outage shape, and the surface is 1.0.0_SA_CTO's. REMEDY SHAPE, offered not prescribed: resolve the owner's live lane on the sending device (the broker's live-agents view already carries it), falling back to the base serial only when no lane of that base is live; or an env override for routes in the same shape as PRD_NOTIFY_TO. CLOSING CONDITION: (a) DISARMED when the L10 stamp on this project is followed by a lane-addressed pointer that reads READ on the delivery ledger; (b) REMEDIATED when a route notification on this device reads READ at a ~Z lane with no hand-sent pointer beside it (that is the falsifier: the mechanical carrier alone reaches the owner). The L4 instance (19465) stays QUEUED as a measured artifact of the defect; nobody should ack it from the base serial to make the number look right.",
    "owner": "3.0.0_SA_CVO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "3.0.0_SA_CVO~Z",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "3.0.0_SA_CVO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S11",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "TO-OP-S-17-16's S1716-AC4 declares cell_refs=\"OP-s-17 OP-s-16\" SPACE-separated, but .tools/proof-of-spec-check.py:562 splits that attribute on COMMA only -- `[c.strip() for c in attrs.get(\"cell_refs\", \"\").split(\",\") if c.strip()]` -- so the pair is read as ONE literal cell id 'OP-s-17 OP-s-16', which resolves against no cell in the decomp and REFUSES the instance. The instance is otherwise VALID: all other violations are cleared. This face is the estate's ONLY multi-value cell_refs (1 hit across 79 mission files), which is why the separator convention was never exercised before.",
    "evidence": [
      ".tools/proof-of-spec-check.py:562 -- `refs = [c.strip() for c in attrs.get(\"cell_refs\", \"\").split(\",\") if c.strip()]`; the separator is a comma and there is no whitespace split anywhere in the file (comp-read --enumerate 'cell_refs' -> 7 hits across 1127 lines, all inspected: :328 and :391 comments, :562 the parse, :590/:771 the no-refs bookkeeping, :762/:775 the violation emitters)",
      "proof-of-spec-check.py on the instance -> \"VIOLATION: alignment: cell_ref 'OP-s-17 OP-s-16' (cited by ['S1716-AC4']) does NOT exist in .../NFRA_OPSEC202609_DECOMP.md\"; alignment-forward-2 reads '2/3 distinct cell_ref(s) resolve' -- the 2 that resolve are the single-valued OP-s-17 and OP-s-16",
      "estate census: comp-find 'cell_refs=\"[^\"]*[ ,][^\"]*\"' --files org/missions -> DENOMINATOR 1 hit across 79 file(s) scanned, and the single hit IS this task order. No other TO in the estate declares a multi-value cell_refs, so the comma convention at :562 has never been exercised by a face until now.",
      "the instance's other violations are CLEARED: artifact-resolution now reads '5 resolved at pin / 0 pending-on-worktree / 0 UNRESOLVED-HERE' over a denominator of 5 rows, and surprises-frame reads '3 entries; 3 open with a row id; 3 resolve to a channel row' in ENFORCE mode. cell_refs is the only remaining refusal."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY A ROW: the last thing between a fully-evidenced deliverable and its complete flip, found by running the gate rather than by assuming it would pass. NOT SELF-FIXED: cell_refs is the issuance half and the assignee does not get to rewrite the mapping its own work is graded against -- that is the whole point of the alignment check. The fix is ONE CHARACTER in the face: cell_refs=\"OP-s-17,OP-s-16\". WIDER THAN THIS PROJECT, offered not prescribed: because no other face in the estate has ever used a multi-value cell_refs, the next author to write one will hit this identically, and the failure text points at the DECOMP ('the cell is not there') rather than at the separator, which sends the reader to the wrong file. Two candidate remedies for whoever owns the checker: split on comma AND whitespace, or refuse a cell_refs value containing whitespace with a message naming the separator. Neither is this seat's to make. CLOSING CONDITION: DISARMED when the face is corrected and proof-of-spec-check returns VALID rc=0; REMEDIATED when a multi-value cell_refs either parses or is refused with a message that names the separator. FALSIFIER: a proof-of-spec-check run that accepts a space-separated cell_refs pair.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S13",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "TO-OP-S-5 asserts WAF logging is OFF on BOTH ACLs and instructs this cell to create it on both. At my vintage the REGIONAL ACL opal-gateway-waf ALREADY HAS a logging configuration -- live, delivering to log group aws-waf-logs-opal-gateway (the exact group name the TO specifies) with 84,723,696 bytes stored, declared in Terraform at infra/aws/terraform/opal-gateway/waf.tf:194 with the authorization and cookie redactions already present. Only the CLOUDFRONT ACL is genuinely unconfigured (WAFNonexistentItemException). Two consequences: the group's retention is 90 d, not the 400 d the TO specifies; and the file that owns it is infra/aws/terraform/opal-gateway/waf.tf, which is NOT inside the lane the TO declares for the gateway WAF (infra/aws/ec2/opal-gateway/**).",
    "evidence": [
      "LIVE 2026-09-03: aws wafv2 get-logging-configuration on the CLOUDFRONT ACL (arn ...global/webacl/opal-cloudfront-protection/a09833c0-4043-49fc-a92c-0dcdeaff9abd) -> WAFNonexistentItemException, i.e. NO logging configuration. The brief's F3 claim holds for THIS ACL.",
      "LIVE 2026-09-03: the same call on the REGIONAL ACL (arn ...regional/webacl/opal-gateway-waf/181df35e-e886-40c6-a8dc-9d0b60346a44) RETURNS a LoggingConfiguration: LogDestinationConfigs = [arn:aws:logs:us-east-1:313476888478:log-group:aws-waf-logs-opal-gateway], LogType WAF_LOGS, LogScope CUSTOMER, ManagedByFirewallManager false, and SIX RedactedFields -- authorization, cookie, x-amzn-ava-user-context, x-amzn-oidc-accesstoken, x-amzn-oidc-data, x-amzn-oidc-identity.",
      "LIVE 2026-09-03: aws logs describe-log-groups --log-group-name-prefix aws-waf-logs- -> exactly ONE group, aws-waf-logs-opal-gateway, retentionInDays 90, storedBytes 84723696. The stored bytes are the discriminator: this is not a declared-but-idle configuration, it has been receiving records.",
      "DESIRED plane: infra/aws/terraform/opal-gateway/waf.tf:194 resource aws_wafv2_web_acl_logging_configuration \"gw\"; :195 log_destination_configs = [aws_cloudwatch_log_group.waf.arn]; :200-226 six redacted_fields blocks; :20 resource aws_cloudwatch_log_group \"waf\" with :23 retention_in_days = 90. So the live state is IaC-declared and not console drift.",
      "TO-OP-S-5 face @5494591e91 title: 'WAF logging on both ACLs, CloudFront access logs, ALB access logs -- all OFF today'; deliverable 1: 'WAF logging on BOTH ACLs to CloudWatch Logs ... opal-gateway-waf (REGIONAL) -> aws-waf-logs-opal-gateway ... Retention 400 days on both groups'; compiler_tools_mandate phase 1 step 1 expect: '0 logging configurations today (the brief's zero re-measured)', if_mismatch 'STOP; a logging configuration already present is a row before any edit'.",
      "TO-OP-S-5 face Lane clause names 'the gateway ALB / regional WAF Terraform under infra/aws/ec2/opal-gateway/**'; the resource actually lives at infra/aws/terraform/opal-gateway/waf.tf. Measured: the path the TO names is not the path that holds the resource."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY A ROW AND NOT A HALT: the face's Phase-1 step says STOP on this mismatch, and the row is that stop discharged -- the estate's standing rule is to append a row and keep working, and the work that remains (the CloudFront ACL half) is untouched by this finding, in lane, and proceeding. NOTHING WAS EDITED on the regional side. WHY IT MATTERS: had this seat followed deliverable 1 literally it would have authored a SECOND aws_wafv2_web_acl_logging_configuration for an ACL that already has one -- wafv2 permits one logging configuration per ACL, so the apply would either have failed or silently replaced a working control that is currently capturing gateway traffic, and replacing it at 400 d would also have been an unrequested change to a module this TO does not name. THE RETENTION QUESTION IS GENUINELY OPEN, not a defect: 90 d clears the criterion's own bar (S5-AC5 is '>= 7 d on every destination', with 400 d described as 'the settings'), so the two halves of the TO disagree about what is being asserted, and only the issuer can say whether mirroring C-8 at 400 d is worth an out-of-lane edit to a live control. SCOPE BOUND: this row is about the REGIONAL ACL only; the CloudFront ACL's absence is re-measured and confirmed. FALSIFIER: if get-logging-configuration on the regional ACL later returns WAFNonexistentItemException, this row is wrong and the TO's premise was right.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S17",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "TWO findings on the opal-users-v2 limb, one corrective and one hazardous. (1) CARRIER: the table is managed by infra/aws/terraform/shared-infra/dynamo.tf, NOT portal-auth/dynamodb.tf as the face and ruling 19600 both say -- terraform state proves it (shared-infra holds aws_dynamodb_table.opal_users_v2; portal-auth holds the LEGACY opal_users), and portal-auth's two opal-users-v2 mentions are COMMENTS at :167/:173 recording that the TWIN was removed 2026-06-29. (2) HAZARD: shared-infra's BASELINE plan is NOT clean -- 0 add / 1 change / 0 destroy on aws_s3_bucket_lifecycle_configuration.global_graph, an unrelated globgrph rule (ms-heat-snapshots-expire-60d) belonging to another seat. An unscoped apply for this cell would have carried a foreign change, against the bound 'nothing else rides the apply'.",
    "evidence": [
      "terraform -chdir=infra/aws/terraform/shared-infra state list -> includes aws_dynamodb_table.opal_users_v2; terraform -chdir=infra/aws/terraform/portal-auth state list -> aws_dynamodb_table.opal_users (LEGACY), opal_firms, opal_offices, opal_sessions, portal_auth_mfa, portal_auth_throttle, user_permissions -- NO opal_users_v2. The two modules do not both manage it.",
      "comp-read infra/aws/terraform/portal-auth/dynamodb.tf --enumerate 'opal-users-v2|opal_users_v2' -> 2 hits, BOTH comments: ':167 # --- opal-users-v2 --- TWIN REMOVED 2026-06-29 (CVO dispatch a47d169ef) ---' and ':173 # De-duped: `terraform state rm aws_dynamodb_table.opal_users_v2` (live table ...)'. So the face's TO-OP-S-8 check 'confirm none of the five tables is ALSO declared there -- a table declared twice is a row' PASSES: it is declared once, and a prior twin was already removed by the estate in June.",
      "shared-infra BASELINE plan, run BEFORE any edit by this seat: 'Plan: 0 to add, 1 to change, 0 to destroy' with '# aws_s3_bucket_lifecycle_configuration.global_graph will be updated in-place' -- adding a rule id ms-heat-snapshots-expire-60d, filter prefix warehouse/ms_heat/snapshots/, expiration 60 days. Nothing in this cell touches globgrph or that bucket.",
      "CONTROL that the baseline read is real and not a stale-state artifact: the sibling module partner-firms was planned the same way in the same minute and read '0-diff / No changes', so a dirty baseline is a property of shared-infra, not of this seat's tooling or credentials.",
      "SCOPED plan after this seat's edit: 'aws_dynamodb_table.opal_users_v2 will be updated in-place / Plan: 0 to add, 1 to change, 0 to destroy', with Terraform's own 'Warning: Resource targeting is in effect' printed and recorded rather than suppressed.",
      "The scoped plan changes EXACTLY ONE attribute, read from terraform show -json: deletion_protection_enabled False -> True. server_side_encryption reads [{'enabled': True, 'kms_key_arn': ''}] BEFORE and AFTER -- identical -- so the apply does NOT drop the live table's SSE despite the resource block declaring no server_side_encryption. That was the specific hazard checked, not assumed."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY A ROW: a spec-vs-world divergence (the carrier) plus an estate condition found off-task (the drift), both surfaced BEFORE the apply. The carrier half is the FIFTH instance this project of a face naming a referent that was never read -- after the key (Z-S3), the roles (Z-S4), the log target (Z-S5) and the demo table's management (Z-S14) -- and it is worth the issuer's attention as a pattern rather than as five separate corrections. NOT CHASED: the global_graph drift is left EXACTLY as found. This seat did not apply it, did not revert it, and did not investigate whose it is beyond naming the resource; a foreign unapplied change is its owner's, and touching it would be the never-widen violation this row exists to avoid. HOW THE ACT PROCEEDS ANYWAY: the apply is SCOPED with -target=aws_dynamodb_table.opal_users_v2, which is the sanctioned mechanism for 'nothing else rides the apply' (cloud-ops pre-flight step 2 permits targeting and requires it be declared). ITS OWN TRAP, NAMED AND AVOIDED: a -target apply verified by a -target re-plan proves nothing, because the scoped check cannot see what the scope excluded. Verification is therefore an UNSCOPED re-plan whose PASS condition is two-sided -- opal_users_v2 shows 0-diff AND the global_graph drift is still present and untouched. A clean unscoped plan would mean this seat had silently applied someone else's change. CLOSING CONDITION: the carrier half is DISARMED when the issuer records the correct path; the drift half is REMEDIATED only by its owner applying or withdrawing it. FALSIFIER for the carrier half: a terraform state entry for opal_users_v2 under portal-auth.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S2",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "TO-OP-S-3 deliverable 2 prescribes that Terraform read the origin secret via a data source and set it as a CloudFront custom_header; a custom origin header VALUE is returned in full by cloudfront:GetDistributionConfig and is therefore written into terraform state BY CONSTRUCTION -- which contradicts the portal-auth module's own stated invariant at secrets.tf:5-7 ('Manages the secret CONTAINERS only ... aws_secretsmanager_secret_version is intentionally omitted so that key material never enters Terraform state'). The state bucket has versioning ENABLED and NO lifecycle configuration, so every superseded value persists as a noncurrent object indefinitely -- a rotation (deliverable 4) retires the value from the live header but NOT from state history.",
    "evidence": [
      "infra/aws/terraform/portal-auth/secrets.tf:5-7 @94b6fd0d11 -- 'Manages the secret CONTAINERS only -- never the secret values. aws_secretsmanager_secret_version is intentionally omitted so that key material never enters Terraform state.' The module states the invariant explicitly; this cell's prescribed mechanism breaks it.",
      "infra/aws/terraform/portal-auth/main.tf:20-24 @94b6fd0d11 -- backend s3, bucket opal-313476888478-terraform-state, key portal-auth/tfstate, region us-east-1.",
      "MEASURED at this seat 2026-09-03: aws s3api get-bucket-encryption -> SSE-S3 AES256 default, SSE-C blocked; get-public-access-block -> all four true; get-bucket-versioning -> Status Enabled.",
      "MEASURED at this seat 2026-09-03: aws s3api get-bucket-lifecycle-configuration -> NoSuchLifecycleConfiguration (rc=254). Versioning Enabled + zero lifecycle = noncurrent versions are retained with no expiry.",
      "MEASURED at this seat 2026-09-03: aws cloudfront get-distribution-config --id EVTSA9VEHNZVH returns CustomHeaders per origin; origin DENOMINATOR 7, CustomHeaderCount 0 on all 7 today. The API returns header VALUES, which is why a refresh writes them to state regardless of how the header was set -- the exposure is not avoidable by choosing a different write path (console, CLI, or ignore_changes all still refresh into state).",
      "TO face NFRA_OPSEC202609.TO-OP-S-3 deliverable 2 @5494591e91 -- 'Terraform reads the value from the secret at plan time (data source), never a literal'; deliverable 1 -- 'No value in any file, log or commit message.'"
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug does not invent a remedy the round did not state): WHY A ROW AND NOT A MESSAGE: it is a spec-vs-world divergence found during the GO's mandated re-grounding, and the face names the row as the carrier. NOT BLOCKING, so it does not also reach the issuer this turn -- the cell is buildable exactly as written and this seat is continuing. SCOPE OF THE CLAIM: this is about where the value RESTS, not about whether the design works; the origin-secret mechanism itself is sound and is the right fix for the constant-header finding (brief F1). WHAT THIS ROW IS NOT: it is not an argument for a literal in the .tf (strictly worse) and not an argument against the cell. REMEDY SHAPES, offered not prescribed, for the issuer to weigh: (a) accept it -- state is encrypted, private, and already holds other sensitive material, and record that secrets.tf's invariant is now scoped to the JWT keypair rather than the module; (b) add a noncurrent-version expiry lifecycle to the state bucket so a rotation actually ages out prior values, which is the cheapest change and the one that makes deliverable 4's rotation mean what it says; (c) a different header mechanism. NOTE (b) IS A SEPARATE LANE -- the state bucket is not this cell's surface and this seat did not touch it. FALSIFIER for anyone re-checking: if a future get-bucket-lifecycle-configuration on opal-313476888478-terraform-state returns a noncurrent-expiry rule, the indefinite-retention half of this row is discharged and only the invariant half stands.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": null
    }
  }
]
```

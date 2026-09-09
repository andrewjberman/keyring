# NFRA_OPSEC202609 -- PRD ADDENDUM 01: automated traffic against the marketing site, and the Infrastructure Report's telemetry dependencies

**Addendum:** 01 · **Authored:** 2026-09-09 ~15:0xZ · **Author (L4):** `1.0.0_SA_CTO~Z`
**Parent PRD:** `NFRA_OPSEC202609_PRD.md` v0.12 (2026-09-03 ~18:4xZ)
**archetype:** SCRIBE (spec)

---

## 0. WHAT THIS IS, AND WHICH DOCUMENT IS PRIMARY FOR WHAT

⛔ **TWO CARRIERS, AND THE SPLIT IS DECLARED SO THEY CANNOT DRIFT.** The parent PRD stays PRIMARY
for `FWD-1` through `FWD-18`, every `C-n`, every manifest row and the whole ratified body. This
addendum is PRIMARY for exactly two things and nothing else:

1. **`FWD-19` -- PROPOSED, NOT RATIFIED.** A new outcome covering automated traffic against the
   marketing site. It is deliberately NOT in the parent's `endpoint_outcomes` JSON array and NOT in
   its fenced ENDPOINT block, because the parent's PRD_HEADER declares `"status": "RATIFIED"` and
   an unratified outcome sitting inside a ratified array would be a false claim that the L6 gate
   reads. **On Andrew's word it folds into the parent as v0.13 and this section becomes the record
   of how it got there.**
2. **The Infrastructure Report dependency set** (section 5), which is RATIFIED already -- it rests
   on Andrew-direct rulings recorded below, not on a proposal.

**Fold-in condition, named so nobody has to infer it:** when Andrew ratifies `FWD-19`, its block
moves into the parent's fenced ENDPOINT block, `"FWD-19"` is appended to `endpoint_outcomes`,
`prd_version` becomes `v0.13`, and section 3 / section 5 / section 7.6 / section 8 take the edits
enumerated in section 6 of this addendum. Until then the parent is unchanged and correct as it
stands.

### Authority

**Andrew-direct 2026-09-09 at the `1.0.0_SA_CTO~Z` terminal, VERBATIM:** *"Something I want to
thread into this is crawler protection for the website. Can you analyze real quick the process of
form fillout on that page, www.opalinvest.com? We get a lot of bullshit form fillouts that are
surely programmatic from bots and I want to explore what that is so an addednum to protect against
this can be threaded into the project needs. I am also working with 4.0.0_SA_CRO~Z on a new brief
for our Global Infrastructure reporting and analysis which has some dependencies on unfinished
OPSEC work, so you will need to work that into the addendum as well."*

**Andrew-direct 2026-09-09 ~14:5xZ at the `4.0.0_SA_CRO~Z` terminal, VERBATIM (relayed by that seat
as msg 20509, full record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260909_1458Z_INFRA_REPORT_FIVE_RULINGS.md`
@`aba4bf6d50` LOCAL):** *"2.) Agreed, CloudFront."* and *"The prioritization should be relayed to
CTO~Z, as I've already instructed them that we are going to need to create an addendum to the PRD
for NFRA_OPSEC202609 to account for the incoming work on the Infrastructure Report."*

⭐ **THE FIRST OF THOSE UNBLOCKS A STAGED TASK ORDER.** `FWD-13`'s CloudFront-vs-Cloudflare card was
carried to Andrew and `TO-OP-S-13` could not be cut without it. It is now settled: **CloudFront.**

---

## 1. THE MEASUREMENT -- how a form fillout actually works on www.opalinvest.com

**Taken live by `1.0.0_SA_CTO~Z` on 2026-09-09 ~14:5xZ against the served page, not from the repo.**
Instrument: a headless browser reading the rendered DOM. **Nothing was submitted** -- a test
submission would have created a real entry and a real notification email, so the form's *behaviour
on POST* is characterised from its declared markup and Gravity Forms' documented contract, and that
limit is stated rather than papered over.

⛔ **A REPO-ONLY READ WOULD HAVE BEEN WRONG, AND THIS IS WHY THE LIVE READ MATTERED.**
`infra/website/README.md` and `infra/website/GODADDY_DNS_REQUEST_opalinvest.md` both still describe
the apex as *"currently Wix"* with the AWS site staged at `new.opalinvest.com`. **Andrew corrected
this in session: the migration is COMPLETE, the renovated site IS `www.opalinvest.com`, and `new.`
was a preview subdomain now deprecated.** The live read agrees with Andrew and not with the repo.
Those two documents are stale pointers of the same class this seat discharged this morning; they are
surfaced here and NOT chased (see section 7).

### 1.1 The serving path

| | |
|---|---|
| Platform | WordPress (Bricks builder theme), `generator` meta reads `WordPress 7.1` |
| Host | EC2 `i-0152e3fe2599fa630`, Elastic IP `18.208.18.213`, OpenLiteSpeed + PHP 8.2 + MariaDB local |
| Edge | ⛔ **NONE.** No CloudFront, no WAF. The origin is the front door. |
| Form plugin | **Gravity Forms** (`wp-content/plugins/gravityforms`) |
| Other plugins seen | `omnisend`, `automaticcss-plugin` |
| Mail path | wp-mail-smtp -> `infra/aws/ec2/website/ses-sendmail.sh` -> SES as `noreply@opalinvest.dev` |

### 1.2 The form itself -- `https://opalinvest.com/contact/`

`<form id="gform_1">`, form id **1**, POSTs back to **`https://opalinvest.com/contact/#gf_1`**
with `gform_submission_method=iframe`. Six visible fields, every one labelled **(Required)**:

`Full Name` · `Firm` · `Email` · `Phone` · **`AUM`** · `What are you looking for?`

Twelve hidden fields ride with it: `state_1` (a base64 blob), `gform_ajax`, `is_submit_1`,
`gform_submit`, `gform_currency`, `gform_unique_id`, `gform_target_page_number_1`,
`gform_source_page_number_1`, `gform_field_values`, `gform_theme`, `gform_style_settings`,
`gform_submission_method`.

### 1.3 ⛔ THE ANTI-AUTOMATION POSTURE, MEASURED: THERE IS NONE

| Control | State | How it was measured |
|---|---|---|
| reCAPTCHA / hCaptcha / Turnstile | **ABSENT** | no vendor script loads; no `data-sitekey`; the page's ONLY `recaptcha` token is Bricks' own config declaring **`"recaptchaIds":[]`** -- an empty array |
| Gravity Forms honeypot | **OFF** | 0 elements matching `.gform_validation_container` / honeypot field selectors |
| Akismet | **ABSENT** | no marker in the served page |
| HTML5 `required` attribute | **ABSENT on all 6 fields** | validation is server-side only; there is no client-side friction whatsoever |
| Edge WAF / rate limit on the POST path | **ABSENT** | no CloudFront in front of the origin at all |
| `robots.txt` | **stock WordPress** | `User-agent: * / Disallow: /wp-admin/ / Allow: /wp-admin/admin-ajax.php` + sitemap. **No scraper or AI-crawler directives of any kind.** |

⚠ **THE reCAPTCHA READING IS A CORRECTED ONE AND THE CORRECTION IS THE USEFUL PART.** A first,
coarser probe of the HOME page returned `recaptcha: true`. That was a substring match on Bricks'
`"recaptchaIds":[]` -- **the token is present and the capability is absent.** A census keyed on the
word "recaptcha" would report this site as CAPTCHA-protected. It is not. The discriminator is the
value, never the token.

### 1.4 The attack, stated as a bot would perform it

```
GET  https://opalinvest.com/contact/      <- parse the hidden fields, including state_1
POST https://opalinvest.com/contact/      <- replay them with attacker-chosen input_1..input_7
```

That is the entire process. **Two requests, no token a scraper cannot obtain from step 1, no
challenge, no proof of work, no honeypot, and nothing at the edge because there is no edge.** The
endpoint is stable and publicly discoverable, and the field grammar (`input_1`, `input_3` ..
`input_7`) is fixed. A commodity form-spam tool needs no site-specific development.

⭐ **AND THE FORM IS UNUSUALLY WORTH SPAMMING**, which is a cause and not a coincidence: it asks for
**Firm and AUM.** It is a high-intent advisor lead form, which puts it in exactly the category that
list-building and lead-resale operations target.

### 1.5 ⛔ WHAT WAS NOT MEASURED -- the grain, stated plainly

**This seat measured the ATTACK SURFACE, not the SPAM VOLUME.** No claim is made here about what
fraction of entries are automated, what the rate is, or what the payloads look like. That census
needs the Gravity Forms entries table or the origin's own access logs -- **the AE lane's surface,
on a box this project relies on and does not own** -- and it is commissioned as a deliverable in
section 4, not asserted here.

**What IS established about automation against this box comes from another seat's measurement and
is attributed, not adopted:** `TO-OP-S-13`'s own derivation censused the origin access logs over
2026-07-30 to 2026-09-04 -- **620,837 request lines, 105,217 to `wp-login.php`, 20,938 to
`/wp-admin`, and 87,819 failed login POSTs**, of which 868 of 882 real successes were classed as
credential stuffing across 48 distinct user-agents. **So this box is a confirmed, sustained target
of automated traffic.** Form submission is the same actors' second, cheaper surface, and it is the
one with no control on it at all.

---

## 2. ⛔ WHY `FWD-13` AS RATIFIED CANNOT SERVE THIS -- and why a new outcome is the honest instrument

`FWD-13` reads, verbatim from the parent PRD:

> **FWD-13** The marketing website has a front door that stops common attacks before WordPress sees them
> **ACCEPT** a request that matches a **well-known attack pattern** never reaches WordPress, and a
> visitor cannot tell anything changed

⛔ **A SPAM FORM SUBMISSION MATCHES NO WELL-KNOWN ATTACK PATTERN. IT IS A WELL-FORMED, POLICY-VALID
POST THAT LOOKS EXACTLY LIKE A REAL LEAD.** It carries no SQL injection, no XSS, no path traversal,
no anomalous header. **Every AWS managed rule group in `FWD-13`'s remit will pass it, correctly.**
Signature matching is the wrong instrument for a request whose content is legitimate and whose only
defect is that no human produced it.

⭐ **THIS IS THIS PROJECT'S OWN LEARNED RULE, APPLIED FORWARD RATHER THAN DISCOVERED AT L7 AGAIN.**
Row `Z-S82` states it: *"a control keyed on a property the EDGE injects can only protect paths that
traverse the edge, so the coverage of the CONTROL is bounded by the coverage of the ROUTING."* The
general form is that **a mechanism's coverage is bounded by what it can perceive.** `FWD-13`'s
mechanism perceives request SHAPE; form spam differs from a real lead only in PROVENANCE. Widening
`FWD-13`'s ACCEPT line to cover it would produce exactly the defect `Z-S80` halted a limb over: an
outcome whose stated mechanism is structurally incapable of serving part of its own surface.

**Therefore: a NEW outcome, on the SAME engine.** This is not a scope grab -- it is the same
precedent the COO set with `OP-s-29`, a second cell mirroring an existing manifest row because the
surface needed a distinct act.

### 2.1 ⛔ AND A SECOND SURFACE THAT NO EDGE CONTROL CAN EVER REACH

The **home page** carries a different form: a **MailerLite newsletter subscribe** whose action is
**`https://assets.mailerlite.com/jsonp/2511468/forms/195154209496106418/subscribe`**. It posts
**directly to MailerLite and never traverses Opal infrastructure at all.**

⛔ **NO CLOUDFRONT RULE, NO WAF, AND NO EDGE CONTROL OF ANY KIND CAN EVER PROTECT IT.** It is
`Z-S82`'s rule in its purest form. It is named here as a **DECLARED RESIDUAL** so that a later
reader cannot see "the site's forms are protected" and believe it covers this one. Its only
available controls are MailerLite's own (double opt-in, its own bot filtering) and they are a
vendor setting, not a cell.

---

## 3. PROPOSED `FWD-19` -- awaiting Andrew's ratification

⛔ **NOT RATIFIED. NOT IN THE PARENT'S `endpoint_outcomes`.** `ACCEPT` lines are plain English and
disputable by rule; this one is Andrew's to set or change. Presented in the parent's exact
definition form so that ratification is a copy, not a rewrite.

```
  FWD-19  Automated submissions and scraping against the marketing site are
         refused or challenged, and a real visitor is never stopped
         DONE WHEN  EXERCISED -- a scripted submission to the contact form has been
                    refused or challenged without a human acting, a real submission
                    made by a person in a browser has succeeded unchanged in the
                    same window, and the volume of automated submissions reaching
                    the entry store has been measured before and after
         ACCEPT     the bullshit form fillouts stop arriving, real advisor enquiries
                    still arrive, and someone can say by how much it changed
         SOURCE     Andrew-direct 2026-09-09 at the 1.0.0_SA_CTO~Z terminal:
                    "crawler protection for the website"; "We get a lot of bullshit
                    form fillouts that are surely programmatic from bots"
         BOUND BY   7.6 C-17, C-18 (proposed, section 6.4)
```

⭐ **THE `DONE WHEN` CARRIES A BEFORE-AND-AFTER MEASUREMENT ON PURPOSE.** Andrew's complaint is
about VOLUME. An outcome that proves a control is *installed* and never proves the volume *fell*
would satisfy itself while the mail keeps coming. **The before-measurement must be taken before the
control is armed, or it is unobtainable afterwards** -- which is why section 4 orders it first.

⛔ **AND THE SECOND HALF OF THE ACCEPT LINE IS NOT DECORATION.** A contact form on an advisor
marketing site is a REVENUE SURFACE. A control that silently eats one real enquiry from a
prospective advisor is worse than the spam it prevents. **This is the same false-positive hazard
`TO-OP-S-13` already refuses to take on day one** -- it keeps the managed groups in COUNT precisely
because the site is public and unauthenticated. `FWD-19` inherits that discipline in `C-17`.

---

## 4. THE SHAPE OF THE WORK -- for `2.0.0_SA_COO~Z` at L5, not a dispatch

Ordered. **The order is load-bearing and the first item cannot be recovered later.**

1. ⛔ **MEASURE THE BASELINE FIRST, BEFORE ANY CONTROL IS ARMED.** Census the Gravity Forms entry
   store and the origin access logs for POSTs to `/contact/`: a window, a denominator, the
   automated/human split with the discriminator named, and the user-agent and address distribution.
   **The method is already proven on this exact box** -- `TO-OP-S-13`'s lane censused 620,837
   request lines from the same logs -- so this is a re-run of a working instrument, not a new build.
   ⭐ **Apply that census's own inverted lesson: on WordPress a FAILED login returns 200 and a
   SUCCESS returns 302.** Do not assume the status-code grammar of the submission path; establish it.
2. **The edge, which is now unblocked.** `TO-OP-S-13` (`FWD-13`) stands up CloudFront + WAF in front
   of the origin. **Andrew ruled CloudFront at 14:5xZ; its GO condition (`TO-OP-S-4-18` terminal) is
   already met.** `FWD-19`'s controls attach to THAT distribution and that WAF ACL. **One build.**
3. **The `FWD-19` controls on that ACL**, in the safe order:
   - **AWS WAF Bot Control** managed rule group, **in COUNT first**, same soak discipline as the portal.
   - A **CAPTCHA or Challenge action** scoped to the **POST to `/contact/`** and nothing else. AWS
     WAF supports both natively, so this is a rule and not a new engine or a new vendor.
   - A **rate-based rule** on that path. ⚠ Size it from step 1's measured distribution, never from a
     default -- and note the estate has a live data point that a 2000-per-5-minute threshold barely
     engaged at 7.6 req/s (row from the `C-4` thread), so defaults on this estate have already been
     measured as too loose once.
4. **The on-box form control** -- see the fork in section 8. Enabling the Gravity Forms honeypot is
   a single setting and costs nothing.
5. **`robots.txt` directives** for scrapers and AI crawlers. ⚠ **Advisory only, and it must be
   written down as advisory:** a crawler that ignores `robots.txt` is exactly the crawler worth
   stopping, so this is a declaration of intent, never a control. It belongs in the outcome because
   Andrew said "crawler protection" and this is the half that addresses well-behaved crawlers; the
   Bot Control rule group is the half that addresses the rest.

---

## 5. THE INFRASTRUCTURE REPORT DEPENDENCY SET -- RATIFIED, threaded in

**Source:** `4.0.0_SA_CRO~Z` msg 20509, relaying Andrew-direct 2026-09-09 ~14:5xZ. **The brief is
NOT cut** -- Andrew and that seat are mid-recon, there is no L1 artifact yet, and this seat verified
that independently (`comp-find --name '*BRIEF*'` over `org/missions` returned 0 across 362 files).
So this section carries the dependency SHAPE by `FWD`/`OP-s` id, which is what was asked for.

**The organising fact.** The report is built on **three Opal properties**, Andrew-direct VERBATIM:
*"the three Opal properties defined as 'Dashboard' (the entire serverless system that feeds the
opalinvest.dev web application), 'Website', and 'Gateway' (the opal-gateway mcp server)."* The
report needs one security/telemetry input **per property**, and **two of the three have none today.**

**Direction is OPSEC -> report in every case. The report READS; OPSEC PRODUCES. There is no reverse edge.**

| Property | Depends on | Outcome | Status |
|---|---|---|---|
| **Dashboard** | `TO-OP-S-20` | FWD-14 | STAGED |
| | `TO-OP-S-15-19` | FWD-14, FWD-17 | STAGED |
| | `TO-OP-S-23` | (no FWD cited) | STAGED |
| | the REST API logging exclusion (5.1) | -- | blocked by PRD :263 |
| **Website** | `TO-OP-S-13` | FWD-13 | STAGED, **now unblocked** -- ZERO coverage today |
| **Gateway** | `TO-OP-S-12` | FWD-12 | STAGED |

### 5.1 ⛔ THE ONE PRD CHANGE THE REPORT ACTUALLY REQUIRES

The portal REST API `f61h681z9g` has **`AccessLogSettings.DestinationArn: null`** and
**`DetailedMetricsEnabled: false`**. `2.0.0_SA_COO~Z` refused to enable it and **the refusal was
correct**: parent PRD **:263** excludes *"any monitor, alarm, log destination or managed-rule group
NOT named in an outcome above."*

**Andrew's "Dashboard" is defined as the ENTIRE serverless system feeding opalinvest.dev, which
contains that API. A report cannot read what is not emitted.** ⭐ **An addendum is the instrument
that can bring it into scope, and that is precisely why this one exists.** See the section 6.3 edit.

### 5.2 ⭐ THE SHARPEST DEPENDENCY IS A STATE DISTINCTION, NOT AN ABSENCE

`TO-OP-S-14-21` is COMPLETE, so the sentinel is live and `opal-suspicious-addresses` is
accumulating rows. **But the reconciler that mirrors a BLOCKED row into the WAF IP set is
`TO-OP-S-15-19`, which is STAGED.** So **a BLOCKED row today is DESIRED, never APPLIED.**

⛔ **A report that renders that table without saying so reports INTENT AS FACT** -- the exact
DESIRED-vs-APPLIED failure CLAUDE.md rule 22 names. **The dependency is therefore not "produce the
data" but "make the data's state DECLARABLE."**

### 5.3 ⛔ SEQUENCING CONSTRAINT -- `TO-OP-S-20` MUST PRECEDE `TO-OP-S-15-19`

Parent PRD 7.2(b) requires the allow-list be checked before every block and that a block can never
override it, on the ground that *"a partner firm's whole office typically leaves the internet
through ONE address."* **Arming the reconciler before the allow-list exists is the
lock-out-a-partner-firm failure, at company scale.** Recorded here because it is easy to lose in an
addendum that lists both as dependencies of the same report.

### 5.4 ⛔ WHAT IS *NOT* A DEPENDENCY -- stated so the addendum does not over-scope

**The report does NOT require blocking to be live in order to launch.** It requires each property's
state to be **DECLARABLE**. A report printing **"Website: BLIND -- no detector"** is correct and
shippable; one printing **"OK"** because nothing looked is the false-clean this whole review exists
to remove. ⭐ **OPSEC completion is a QUALITY gate on the security rows, not a LAUNCH gate on the
report.**

### 5.5 ⭐ THE UNIFICATION -- one build serves both halves of this addendum

`4.0.0_SA_CRO~Z`'s observation, adopted here: **the crawler protection Andrew directed and the
Website telemetry dependency are THE SAME SURFACE.** Both want CloudFront + WAF in front of the
origin. **The crawler half wants the rules; the reporting half wants the logs off the same
distribution.** Andrew's CloudFront ruling settles the vehicle for both at once, and `TO-OP-S-13`
is the single face that creates it. **`FWD-19` and the Website row of the Infrastructure Report are
two consumers of one engine.**

---

## 6. THE EXACT PARENT-PRD EDITS ON RATIFICATION (v0.13)

Enumerated so the fold-in is mechanical and reviewable, not a re-derivation.

**6.1 PRD_HEADER JSON:** `prd_version` -> `"v0.13"`; append `"FWD-19"` to `endpoint_outcomes`.
**6.2 ENDPOINT fenced block:** insert the section 3 `FWD-19` block after `FWD-18`, unchanged.
**6.3 Section 5 (Out of scope):** the managed-rule-group / log-destination exclusion gains two named
exceptions -- **AWS WAF Bot Control under `FWD-19`**, and **API Gateway access logging on
`f61h681z9g` under the Infrastructure Report dependency (5.1)**. ⚠ **NOTHING ELSE.** The standing
moratorium is untouched: **no alarm, no SNS, no email, no notification and no monitor is proposed
anywhere in this addendum.** Access logging is a LOG DESTINATION, which the exclusion names
separately from monitors, and it is being brought into scope as a data source a report reads -- not
as anything that notifies a human.
**6.4 Section 7.6:** two new constraints.
  - **`C-17` (binds FWD-19):** the site is a PUBLIC, UNAUTHENTICATED REVENUE SURFACE. Bot Control
    and any rate rule enter in **COUNT** and graduate to BLOCK/CHALLENGE only on soak evidence, the
    same bar the portal's groups are held to. **A control that refuses a real advisor enquiry is a
    violation of this outcome, not a side effect of it.**
  - **`C-18` (binds FWD-19):** the effect is graded on **VOLUME MEASURED BEFORE AND AFTER**, never
    on the control's existence. **A face that proves only that a rule is attached has not served
    this outcome.**
**6.5 Section 3 (Owns):** the "Owns" sentence's final clause becomes *"the website's edge protection
and its defence against automated submission and scraping"*. **No new OWNS item and no new engine**
-- the distribution and ACL are `S13`'s; `FWD-19` adds rules to them. ⭐ **This follows the
`OP-s-29` precedent exactly: a second act on an existing manifest row rather than a spurious new
row.** The COO's postulate-i forward census stays **20 of 20**.
**6.6 Section 8 (manifest):** **no new row.** `FWD-19`'s cell mirrors **`S13`** as a second act on
the same engine. ⚠ If the COO's L5 read finds that Bot Control constitutes a distinct ENGINE under
section 8's one-row-per-engine contract, **that is a manifest question to route back to L4, not to
resolve at L5** -- the parent's own heading exception episode is the precedent for declaring the
count rather than quietly breaking it.

---

## 7. SURFACED, NOT CHASED

- **`infra/website/README.md` and `infra/website/GODADDY_DNS_REQUEST_opalinvest.md` are STALE**:
  both describe the apex as *"currently Wix"* with AWS staged at `new.opalinvest.com`.
  **Andrew states the migration is complete and `new.` is deprecated; the live read agrees with
  Andrew.** Same recovery-document rot class discharged this morning at `bc8cda87c1`. **Owner not
  assigned here; no fix taken.**
- **`scheduled_daily_pull.cmd:166`** hardcodes this device's interpreter path -- LD-0405, unrelated
  to this addendum, already surfaced this session.

---

## 8. ⛔ THE ONE FORK FOR ANDREW, AND IT IS A SCOPE BOUNDARY RATHER THAN A PREFERENCE

Parent PRD section 3 owns *"the website's edge protection"* and explicitly **relies on, does not
own** *"the website box's on-box hardening (`infra/aws/ec2/website/`, already built)"*. **A Gravity
Forms setting is ON-BOX.** So:

**(a) EDGE ONLY -- strictly inside current scope.** Bot Control + a CAPTCHA/Challenge action + a
rate rule on the `/contact/` POST, all on the CloudFront WAF ACL. Needs no scope change beyond
6.3. **Costs a CloudFront distribution that `TO-OP-S-13` is building anyway.**

**(b) EDGE + ON-BOX -- needs one sentence from Andrew extending scope.** Everything in (a), plus
**enabling the Gravity Forms honeypot** (a single toggle in the form's settings) and optionally a
native CAPTCHA field. ⭐ **The honeypot is close to free and catches the dumbest majority of form
bots before a request ever costs us a WAF evaluation.**

⭐ **RECOMMENDATION: (b).** The two controls fail in different ways and therefore compose --
a honeypot catches naive replay bots at zero cost and zero visitor friction, while Bot Control and
a challenge catch the ones that render JavaScript. **The only thing (b) needs that (a) does not is
Andrew's word that a form SETTING on the WordPress install is inside this project's reach**, or a
named owner for the WordPress admin surface to take it. ⚠ **This seat is not deciding that -- it is
a scope boundary the parent PRD draws explicitly, and drawing it wider is not L4's to do alone.**

---

## 9. WHAT THIS ADDENDUM DELIBERATELY DOES NOT DO

- **It cuts no task order and dispatches nothing.** L5/L6 are `2.0.0_SA_COO~Z`'s.
- **It re-opens no ratified outcome.** `FWD-1`..`FWD-18` are untouched; `FWD-13` is read as written
  and is the reason a new outcome exists rather than a widened one.
- **It proposes no monitor, alarm, notification or email.** The standing moratorium holds entire.
- **It asserts no spam-volume figure.** Section 1.5 states that grain limit; section 4 commissions
  the measurement.
- **It does not treat OPSEC completion as a launch gate on the Infrastructure Report** (5.4).

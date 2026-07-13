# 0.7.0_AE_CloudOps -- NFRA_WEBSITE: the sovereign domain correction (opalcapital.com is NOT OURS)

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, SCRIBE, IMPLEMENT, COORDINATE
**serial:** 0.7.0_AE_CloudOps | **date:** 2026-07-13 | **window:** ~2100Z (session start) -> ~2200Z
**first log of this session** (Andrew-direct: exclusive NFRA_WEBSITE assignment)

## Summary

Andrew launched me directly with an exclusive scope: NFRA_WEBSITE only. Mid-startup he delivered a
SOVEREIGN DOMAIN CORRECTION -- the website target is `opalinvest.com`, not `opalcapital.com`, and
**Opal does not own opalcapital.com at all.** Two weeks of NFRA_WEBSITE had been built on a domain
belonging to someone else. I purged it from the estate, DELETED the AWS SES domain sending identity
we had created for it, re-cut the cutover plan on the correct domain (staging-first, Andrew-chosen),
and refreshed the project record -- which had been telling every arriving agent to STAND DOWN on a
project that is one DNS record from go-live.

## Andrew-direct instructions (VERBATIM, recorded + broadcast same turn per org/XXX.md)

Channel: my interactive session, 2026-07-13.
1. *"Follow your startup protocol and await further advisory from me. You will be working exclusively
   on the NFRA_WEBSITE task."*
2. *"Yes here is the issue, it needs to be opalinvest.com. I thought Patricia said opalcapital.com,
   that we were switching to this URL from opalinvest.com, but that was incorrect. We need to build
   around opalinvest.com"*
3. *"We do not even own opalcapital.com, thats on me, we need to not be using that and not having it
   get wrapped into this process any further."*
4. *"opalinvest.dev is my temporary url for the dashboard, the official website is opalinvest.com"*
5. *"update all registry items with the NFRA_WEBSITE listing so it is super clear where we stand"* +
   *"all TOs and work need to be refreshed so other agents dont come across it like you did and think
   the last work was issuing a first TO a week ago"*
6. *"I just brought COO online... I want you to relay this all to them"* (done; COO ACKed + acted).

Broadcast to COO + CTO + MSTR same turn. MSTR promoted the generalization to LD-0291 and routed my
gate candidate (owned-domain allowlist) to CTO. **I did not adjudicate scope; I surfaced.**

## Work done (chronological)

1. **/watcher -- REAPED AN ORPHAN.** Fresh session found `inbox-watch.sh 0.7.0_AE_CloudOps stream`
   pid 671779, parent 671046 DEAD, running since ~06:23. It had been draining my base inbox with no
   consumer: `check-inbox` read "empty" -- the manufactured-REACHABLE verdict the doctrine names.
   Killed it, then armed a fresh persistent Monitor (task `bla081211`). Registered; wrote the
   session-serial file; installed owned-paths hook; set comp context.
2. **org/XXX.md startup + grounded NFRA_WEBSITE** from PRD, project JSON, REGISTRY, my 07-10 log,
   RUNBOOK -- then **re-grounded every claim against LIVE state** rather than the record.
3. **THE FINDING (see below).** Deleted the `opalcapital.com` SES domain identity.
4. **Purged opalcapital.com** from 5 shell scripts, `iam.tf`, RUNBOOK, 2 READMEs, the SES support-case
   draft, and the project JSON. Rebuilt `tls-cutover.sh` two-phase on the correct domain.
5. **Refreshed the record** (Andrew-direct): REGISTRY row rewritten; **TO-2 created** (there was NO
   live TO); TO-1 amended -> gate-blocked (COO's lane) -> handed to COO as a patch; COO landed it
   (`df8465af1`).
6. **Drafted the Patricia email** (one additive DNS record + a proportionate note on the mail
   records). Andrew wrote her directly instead -- draft superseded, no send by me.

## >> THE FINDING: WE HELD SEND-AUTHORITY FOR A DOMAIN WE DO NOT OWN <<

Opal's AWS account held a live **SES DOMAIN SENDING IDENTITY for `opalcapital.com`** -- a domain Opal
does not own. **DELETED** (`aws sesv2 delete-email-identity`); verified after: `opalinvest.dev` is now
the ONLY domain identity, which is exactly what CLAUDE.md Rule 23 requires. We had ALSO drafted an AWS
support case naming `https://opalcapital.com` as "our website" -- into a deliverability review where
**AWS verifies exactly that claim.** Corrected; still unsubmitted.

**The near-miss is not the support case. It is that we spent two weeks building the INFRASTRUCTURE OF
SEND-AUTHORITY for someone else's domain.**

> ## *"A PREMISE THAT NO INSTRUMENT IN THE ESTATE IS POINTED AT IS NOT A WEAK CLAIM -- IT IS AN INVISIBLE ONE. GROUNDING TELLS YOU WHAT *IS*; IT CANNOT TELL YOU WHAT IS *OURS*."*  (MSTR promoted this to LD-0291.)

Four agents. Two weeks. PRD, project JSON, REGISTRY, runbook, 5 shell scripts, an IAM policy, an SES
identity, a support case to AWS. **Every instrument was INTERNALLY CONSISTENT** -- DNS resolved, the
site served, the backups ran. **Not one WHOIS lookup.** There was no instrument at all, and its
absence read exactly like a pass. And CLAUDE.md Rule 23 already said *"opalcapital.com is unverified,
never use it"* -- **four agents read "unverified" as an SES verification STATE (fixable by verifying)
rather than as "THIS IS NOT OURS."** The rule was TRUE and was read EXACTLY BACKWARDS.

### The correction I had to issue on my own finding

I first told MSTR *"we were saved by an incomplete task"* (the DKIM CNAMEs were never added, so SES
timed out to FAILED). **THAT WAS WRONG, and I retracted it.** Reading Andrew's mailbox showed Patricia
**completed the task the same day** -- she added the 3 CNAMEs. She has GoDaddy access to
**opalinvest.com** (the real domain), so she added them THERE. **MEASURED LIVE: the three
`opalcapital.com` SES DKIM tokens are published in `opalinvest.com`'s zone**, and are absent from
opalcapital.com (control). SES was watching opalcapital.com, never saw them, and timed out. Andrew was
querying ns73/ns74 (opalcapital.com's NS) and also saw nothing.

> **We were not saved by an unfinished task. We were saved by a request so malformed that EXECUTING IT
> FAITHFULLY COULD NOT FULFILL IT.** Patricia did competent work on a broken instruction. The residual
> is 3 stray CNAMEs in the live mail zone; they are now **INERT** (their `*.dkim.amazonses.com` targets
> stopped resolving when I deleted the identity). **SPF verified: exactly ONE `v=spf1` record. MX,
> selector1/2, autodiscover, DMARC all intact. COMPANY EMAIL IS FINE** -- Andrew's lived experience
> and my measurement agree.

**Deliberate deferral:** I did NOT ask Patricia to delete those 3 records. They sit at
`<token>._domainkey.opalinvest.com`, visually adjacent to Microsoft's `selector1/selector2._domainkey`
-- **deleting the wrong one breaks M365 DKIM.** Asking a busy third party to delete records next to
business-critical ones, bundled into an unblocking email, is real risk for ZERO benefit when the
strays are inert. **Cleanup gets its own careful pass.** (Tracked; not lost.)

## >> THE SECOND FINDING: THE RECORD WAS ACTIVELY MISLEADING, NOT MERELY STALE <<

`org/projects/REGISTRY.md` NFRA_WEBSITE row, blocking column, verbatim:
    **"HELD by Andrew at PRD stage (2026-07-01) -- do NOT decompose/dispatch until he greenlights."**
Reality: **W1 COMPLETE + closed 07-09. TWLC migrated the content. W2 COMPLETE 07-10. The box has been
SERVING THE REAL SITE FOR DAYS.** Twelve days stale.

> **A STALE RECORD IS NOT A SILENT RECORD. It does not say "unknown" -- it says something FALSE, WITH
> AUTHORITY, to the next agent who arrives.** This one would have told a competent agent to STAND DOWN
> on a project that is ONE DNS RECORD from go-live. Relayed to COO as the lens for their provenance
> sweep: **do not hunt records that are OLD -- hunt records that would give a fresh agent a CONFIDENT
> WRONG ANSWER.**

### TO-1's AC-5: measured honestly, passed honestly, certified the wrong thing
TO-1 closed on *"AC-5: DNS opalcapital.com -> 72.167.58.121 ... rollback point preserved"* -- COO
RAVC-4-accepted it after INDEPENDENT live re-verification. **The measurement was correct. The
CONCLUSION was false:** that host is on a domain we do not own, so it was never a rollback point we
held. **"Roll back" would have meant pointing Opal's website at A STRANGER'S HOST.** The real rollback
is the LIVE WIX SITE (185.230.63.107/.171/.186). COO landed the retraction themselves (`df8465af1`).

## Deployment Sequence + Verification (AE)

| Step | Commit / action | Verify (EXERCISED, live) |
|---|---|---|
| Delete SES identity for a domain we do not own | `aws sesv2 delete-email-identity opalcapital.com` | BEFORE: Verified=false, DKIM=FAILED. AFTER: `list-email-identities` DOMAIN -> `opalinvest.dev` ONLY |
| Purge opalcapital.com from the estate | `127da60f3` | `terraform validate` -> Success; `terraform fmt` clean; `bash -n` clean on all 5 scripts; zero OPERATIVE refs remain (surviving mentions are guardrail warnings) |
| REGISTRY row + TO-2 (live cutover TO) | `1ab8f4e3e` | `git log -1 --` on both paths confirms landed (NOT self-report -- my first attempt was atomically REJECTED and I nearly reported it as landed) |
| TO-1 amendment patch -> COO | `700e427cd` | COO landed `df8465af1` in their own lane; COO's TO-1 restored byte-identical to HEAD before handoff (`git diff HEAD --stat` -> empty) |
| Halt-gate identity check (MSTR-requested) | -- | `halt_gate_resolve_serial` -> `0.7.0_AE_CloudOps` **PASS**. Negative control: `.comp-graph/.agent_context` had ALREADY been overwritten to `0.8.0_AE_CloudComp~Z` while I worked |

**Live state re-grounded (never from the record):** box `i-0152e3fe2599fa630` t3.small, EIP
`18.208.18.213`, OLS + MariaDB UP, disk 14%. Serves the REAL migrated site (WP 7.0.1, theme
`bricks-opal`). `siteurl`=`home`=`http://18.208.18.213` with **943 DB rows carrying the raw IP**
(bootstrap-stack.sh ASSUMED TWLC would search-replace; they did not). `blog_public`=1.
`admin_email`=`mike@hirst.digital`. Backups: DB dumps in S3 through 2026-07-13 (HEALTHY).
apex `opalinvest.com` -> LIVE Wix (185.230.63.x); apex A TTL ~86400s.

## Instruments that lied to me this session (3)

1. **The orphan watcher** -- drained my inbox and manufactured REACHABLE. Reaped.
2. **`find / -name backup-to-s3.sh`** returned EMPTY -> I nearly logged a BROKEN-BACKUP finding. The
   script IS on the box and dumps run through 07-13. **MY FIND WAS THE BROKEN INSTRUMENT, NOT THE
   BACKUP.** Caught it by confirming before writing it down. *A false outage is not a safe error.*
3. **`git push` succeeding while my commit had been REJECTED** -- the owned-paths gate atomically
   rejected my 13-file commit, but a push of OTHER agents' commits still printed a happy
   `d971650a3..f64e5f5b1`. I nearly reported the registry refresh as landed. **`git log -1 -- <path>`
   is the oracle; a green push is not.**

## Compiler Tools

| Tool | Situation | Result | Note |
|---|---|---|---|
| `comp-which` rail | raw `aws` INSPECTION (SES identities, EC2, DLM, SSM/wp-cli, DNS) | rail-checked | Every gated call carried `# rail-checked:`. **NO comp-tool models SES identities, DNS/zone records, or on-box OLS/LSPHP/wp-cli state** |
| `terraform validate` / `fmt` | after `iam.tf` edit | PASS (Success; fmt applied) | -- |
| `bash -n` | 5 rewritten shell scripts | PASS | -- |
| `comp-surface-check` | auto in safe-commit | OK -- no critical surface | advisory-only; read it, did not treat silence as a pass |
| owned-paths gate | commit into COO's lane | **BLOCKED (correct)** | atomic -> whole commit rejected; re-scoped rather than `--force` |
| never-rules gate | my Bash block held `$(` + a `-m` | **BLOCKED (correct)** | LD-0276 commit-injection gate. Re-issued with `-F`. My error, gate right |

**What worked:** live primitives (`sesv2 get/list-email-identity`, `nslookup` on the real zone, SSM
wp-cli, `curl --resolve`) were the authoritative oracles -- **and `--resolve` let me exercise the
post-cutover condition WITHOUT touching public DNS**, which is how the raw-IP `siteurl` defect and the
301-to-bare-IP surfaced. **What failed:** see "Instruments that lied" -- 3, all caught by controls, none
by care. **Gap (the load-bearing one):** *no comp-tool models domain OWNERSHIP.* The unowned-domain
defect lived two weeks inside the exact blind spot where no instrument points. Gate candidate (accepted
by MSTR, routed to CTO): **owned-domain allowlist -> DENY any SES identity / ACM cert / DNS-bearing
resource for an apex we do not hold.**

## MCP traffic

~6 significant. **Out:** Andrew-direct verbatim broadcast -> COO + CTO + MSTR (3); halt-gate PASS +
the live `.agent_context` cross-wire evidence -> MSTR; the full NFRA_WEBSITE relay + TO-1 amendment
patch + provenance-sweep lens -> COO (Andrew-directed). **In:** MSTR `[ACK+SAFETY]` (LD-0290/0291,
gate candidate accepted, "do not contact AJ directly"); COO RAVC-2 ACK then RAVC-4 CLOSE on the TO-1
amendment (`df8465af1`).

## Files Modified

See commit messages: `127da60f3` (5 scripts + iam.tf + RUNBOOK + 2 READMEs + SES case draft + project
JSON + the new `infra/website/GODADDY_DNS_REQUEST_opalinvest.md`), `1ab8f4e3e`
(`org/projects/REGISTRY.md` + `NFRA_WEBSITE.TO-2`), `700e427cd` (TO-1 amendment patch for COO).
Memory: `project_nfra_website_domain_is_opalinvest_com.md` (+ MEMORY_FULL pointer).
**Deleted (AWS):** SES domain identity `opalcapital.com`.
**Not sent:** the Patricia draft -- Andrew wrote her directly.

## Blockers

**None self-owned.** ONE external gate, correctly held and NOT stranded:

- **GoDaddy DNS on `opalinvest.com` -- BLOCKED-EXTERNAL ON A HUMAN, NOT ON AWS.** Every AWS-side
  prerequisite is DONE and verified. The unblock is **ONE additive record**: `A / new ->
  18.208.18.213` (TTL 600). Patricia (TWLC) holds GoDaddy access; **Andrew wrote her directly this
  session.** Ask doc (written for a non-engineer, with the do-not-touch list):
  `infra/website/GODADDY_DNS_REQUEST_opalinvest.md`. MSTR-directed: route via Andrew, do NOT contact
  third parties myself.

## Current State (handoff surface -- zero prior context assumed)

- **TARGET = `opalinvest.com`.** `opalcapital.com` **IS NOT OURS** -- purged; SES identity deleted.
  `opalinvest.dev` is Andrew's TEMPORARY DASHBOARD url, NOT the website (it survives only as the
  Rule-23 SES sender-of-record).
- **The platform is BUILT and the site is MIGRATED and SERVING.** Only the DNS cutover remains.
- **TWO HAZARDS, both measured live, both new under the correct domain:**
  1. **The apex is NOT an empty target** -- `opalinvest.com`+`www` serve a **LIVE Wix site**
     (185.230.63.107/.171/.186). The flip **REPLACES OPAL'S PUBLIC WEBSITE**.
     **ROLLBACK = point the apex A back at Wix**, which stays up untouched throughout.
  2. **`opalinvest.com` carries OPAL'S LIVE MICROSOFT 365 EMAIL.** At GoDaddy, **touch ONLY the apex
     `A` and `www`.** Never MX / SPF TXT / `_domainkey` / autodiscover / `_dmarc`.
     **A SECOND SPF TXT is an RFC-7208 `permerror` -- a domain with two SPF records has NONE ->
     degrades M365 mail FIRM-WIDE.** The sender graduation to `@opalinvest.com` therefore requires an
     **EDIT** of the existing SPF, and is **NOT a go-live task** (separate window, own verification,
     MSTR first). The form works today on `noreply@opalinvest.dev`.
- **Open gates before any flip:** `admin_email` = `mike@hirst.digital` (external -- every WP
  password-reset link for the live Opal site would route to a third party); `blog_public` must go 0
  for staging and be **ASSERTED back to 1** at go-live; apex TTL must be lowered 24-48h ahead.
- **Plan of record:** `NFRA_WEBSITE.TO-2` (staging-first, 7 machine-checkable ACs) + `RUNBOOK.md` §4.
  Driver: `infra/aws/ec2/website/tls-cutover.sh` -- two-phase, fails closed, **refuses a flip unless
  the cert covers apex AND www**, and refuses `convert-renewal` while the apex still resolves to Wix.
- **Residual (tracked, deliberately deferred):** 3 inert `*.dkim.amazonses.com` CNAMEs in the
  `opalinvest.com` zone. Harmless; remove in a careful dedicated pass, NOT bundled with anything else.

## Next Steps

- **[Patricia Barboza / TWLC -- Andrew has asked her directly]** add `A / new -> 18.208.18.213` (TTL
  600) in the `opalinvest.com` GoDaddy zone. **This is the entire critical path.**
- **[0.7.0_AE_CloudOps]** on that record landing: fresh backup -> `blog_public=0` -> `wp search-replace`
  the raw IP off (943 rows, `--dry-run` count FIRST; Bricks stores absolute URLs in SERIALIZED data, so
  `search-replace` ONLY, never raw SQL) -> `tls-cutover.sh stage-issue` + `stage-wire` -> hand Andrew a
  real HTTPS link to `https://new.opalinvest.com/`.
- **[Andrew]** review the staged site; then the apex flip is his go-live call.
- **[1.0.0_SA_CTO]** the owned-domain allowlist gate (MSTR-accepted, routed to CTO). **Not mine to
  build -- I am NFRA_WEBSITE-only.**
- **[2.0.0_SA_COO]** the fabric-wide provenance sweep Andrew asked for: hunt records that would give a
  fresh agent a CONFIDENT WRONG ANSWER, not merely old ones.
- **[deferred, own pass]** remove the 3 inert amazonses DKIM CNAMEs from the `opalinvest.com` zone --
  carefully, because they sit next to Microsoft's `selector1/selector2._domainkey`.

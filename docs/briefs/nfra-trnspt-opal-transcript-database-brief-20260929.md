# BRIEF: NFRA_TRNSPT -- the Opal transcript database

- Author: `4.0.0_SA_CRO~T`, 2026-09-29. Mode: NEW (L1). Consumer: `/endpoint --forward` at L2, `1.0.0_SA_CTO`.
- Directive: D9. Project code: NFRA_TRNSPT (Andrew's name). Not yet registered; registering is L3, the CTO's.
- Andrew-direct, 2026-09-29, this terminal, VERBATIM: "The premise of the brief should be establishing what must be
  done in order to pull these as they happen to the opal-data-transcript database. Furthermore, there should be plans
  put in order to create additional folders in there. These are transcripts from teams meetings, but also in that
  bucket we are going to want a bronze ingestion folder for market-update as well as analysis-commentary. This bucket
  will become a central database for all Opal communications as it pertains to investments, the purpose of which being
  developing insights/pipelines/analytics on those materials for Opal applications."
- Record of the earlier instructions: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260929_*` (six files).

---

## PART I -- THE OUTCOME TERRITORY

### The candidate thread (for FWD-1)

**O1. Andrew reads Monday's Morning Meeting transcript in the database that same day, and nobody did anything to put it
there.** One archetype (the Monday meeting), one occurrence, meeting end to landed bronze object, with no person
running a command. This is the thread round 1 builds end to end. The Monday meeting is chosen because delegated access
to it is already proven and it recurs weekly, so the next occurrence is a real test within days.

### The rest of the territory

**O2. Every transcript of the four meeting archetypes lands on its own.** The Morning Meeting, OCIO IC and Asset
Management IC arrive automatically. The Research Meeting arrives too, which today it cannot (see Part IV, finding 6).

**O3. Someone who needs last quarter's meetings gets them, and new meetings no longer expire unread.** Existing
history that Microsoft still holds is retrieved, oldest first, and a meeting is landed before Microsoft's retention
removes it.

**O4. A person can tell what the database holds and what it is missing.** For any meeting and date they can answer
"is it here, and if not, why not", including a meeting that was not transcribed or that expired before capture.
A gap is never silent.

**O5. An analyst reads a transcript as structured speech, not as a raw file.** Who said what, in order, for any
landed meeting, from every archetype, including the 29 Research Meeting transcripts already held in the repository.

**O6. Someone who receives a market update puts it in the database and it is kept exactly as received.** Bronze
ingestion for market updates. What counts as a market update, and how one arrives, is not defined by Andrew's words
and is open (Part VII).

**O7. Someone who writes analysis commentary puts it in the database and it is kept exactly as received.** Same
shape as O6 for analysis commentary. Same open definition.

**O8. Andrew can show who may read the database, and it is only the people he named.** Andrew and the terminal seat's
account, `opalbloomberg@opalinvest.com`, per his word of 2026-09-29. Both read, through a route that honors the rule.

**O9. A pipeline builder asks a question across all of Opal's investment communications.** For example "which
securities did we discuss this quarter, in meetings, updates and commentary alike". This is the stated purpose of the
database. It is territory for a later round, not a round-1 promise.

---

## PART II -- WHERE THE BOUNDARY SITS

**This project owns:** the contents of `opal-data-transcripts` and how they get there; the folder plan for each
communication type; completeness and gap reporting; the two-reader rule as it applies to the contents.

**This project relies on, and does not own:**

| Sibling | Relationship |
|---|---|
| `NFRA_OPLGTW` (D9, re-seated to site Z 2026-09-27) | The Opal gateway is the only Microsoft sign-in path Opal runs. Any gateway tool is that project's build. A spec is parked with `1.0.0_SA_CTO~O`. |
| `OPAL_ALTRESEARCH` (closed) | Prior art: the transcript store, the WebVTT parser, the security-mention grammar and the four-fund weights join. Its store stays where it is until this project decides otherwise. |
| `LGIC_NAMING`, `LGIC_CANON` (D14) | Names and addresses. Every new source or scope is a registry row, never a typed name. |
| The Teams tenant settings (Littledog, IT) | Owned by the tenant. This project depends on them and does not change them. |
| `0.0.3_BG_BBGTerminal` seat | A candidate source of market updates. Not yet asked. |
| Portal and analytics that consume the database | Downstream. Not owned here. |

**Fabric:** the gateway sits on site Z and this work began on the laptop. Which fabric owns NFRA_TRNSPT is not decided
in this brief. It is the CTO's and Andrew's call.

---

## PART III -- THE QUALITATIVE BAR

No numbers are proposed. The tests are disputable by the person the work is for.

- **O1 passes when** Andrew opens the database on a Monday afternoon and finds that morning's meeting, with speakers,
  having done nothing since the meeting ended. It fails if any step needs him at a keyboard.
- **O3 passes when** Andrew can name a past meeting still inside Microsoft's retention and the database has it. It
  fails if a meeting that was retrievable on 2026-09-29 is later found only as "Item not found".
- **O4 passes when** asked about a gap, the answer names the cause (never transcribed, expired, refused), not a shrug.
- **O5 passes when** an analyst who today reads a transcript file to find what was said about one company gets it
  without opening the file.
- **O8 passes when** a third person cannot read a transcript by any route, and Andrew can demonstrate it, not assert it.
- **O9 passes when** the analyst's question is answered from the database alone and they would otherwise have searched
  three places by hand.

---

## PART IV -- THE SUBSTRATE: FINDINGS

All measured 2026-09-29 unless stated. Claim class is shown per finding.

1. **The bucket exists and is private by key.** `opal-data-transcripts`, SSE-KMS under its own key, versioned, public
   access blocked, TLS-only. Measured (AWS reads). The key policy leaves the account root able to administer, which
   includes the power to grant itself use; the privacy boundary is "no broad role reads it by accident", not
   "no administrator can". Reported by `0.7.0_AE_CloudOps`, confirmed in the policy text.
2. **The name is canonical.** Scope `transcripts` (PRODUCT, GENERAL tenancy) and source `teams` are registry rows.
   `lib/opal_naming.py` grades the bucket CONFORMANT and produces
   `s3://opal-data-transcripts/teams/transcripts/{tier}/{table}/date=YYYY-MM-DD/`. Measured. One registry step is open:
   `bucket_provisioned` is still false, and flipping it restamps 11 generated files.
3. **The key grammar has a table slot in snake_case.** Andrew wrote `market-update` and `analysis-commentary`. The
   grammar's table case is snake_case, so the canonical folders are `market_update` and `analysis_commentary`. A new
   SOURCE for each needs its own registry row, because the builder refuses an unregistered source. Measured (the
   builder refused `teams` before it was registered).
4. **Delegated access to a meeting Andrew does not organize works.** Signed in as `andrew@opalinvest.com`, the
   Morning Meeting, OCIO IC and Asset Management IC all listed and returned speaker-attributed WebVTT. Measured.
   This means the Teams tenant setting for Graph transcript access and speaker attribution is on.
5. **Retention is real and already cost history.** 34 transcripts were listed and 30 retrieved. The 4 oldest, all
   Morning Meeting, returned "Item not found". Their dates (April to 1 June) match a roughly 120-day expiry recorded on
   2026-07-31. Measured for the failure; the cause is inferred.
6. **The Research Meeting is refused.** Microsoft returned "User does not have access to lookup meeting" (3003), though
   Andrew is in the meeting's chat. The meeting is organized by Lauren Harmon. The cause is not established.
7. **One meeting id serves a recurring series.** The Morning Meeting is one meeting with 19 transcripts, one per
   occurrence. Measured. A poller enumerates a series by listing that id.
8. **A start signal is readable.** Each meeting chat receives a transcript-started event, then recording events, when
   a call runs, and the chat is readable through the gateway today. Measured on four chats. It is a candidate trigger.
   Whether Microsoft change notifications for transcripts can be subscribed to with delegated access is NOT verified.
9. **Every existing gateway path is per-user.** The gateway holds delegated tokens only. The headless paths it has
   (OTP, `/ms/*`, the tax workbook route) each run under one fixed identity's server-held token with a static bearer.
   That is prior art for an unattended pull as Andrew. How long that stored token stays usable without Andrew
   signing in again is NOT measured.
10. **The sign-in used for the pull was over-broad.** The application Andrew signed in to carried directory, site and
    file write scopes, because the tenant already grants it broad consent. Only meetings and transcripts were called.
    Measured. It is not a route to build on.
11. **A transcript store and parser already exist.** `research_transcripts/` holds 29 Research Meeting transcripts
    (through 2026-08-03), a WebVTT parser, a mention grammar and a 4-fund weights join. Measured. That store sits in the
    git repository, which is readable by every seat. The three other archetypes are barred from it by a guard.
12. **No first-party design for market updates or analysis commentary was found.** A repository search returned only
    unrelated files. This is the absence of a hit, not proof that none exists; see Part VII.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Named and not sequenced.

- A way to reach Microsoft with no person signed in, or with a stored sign-in that outlives a session. The choice
  between a fixed-identity delegated token and an application permission is a security decision, and it is Andrew's.
- A trigger, or a schedule, that notices a finished meeting. Finding 8 names one candidate, unverified.
- An answer for the Research Meeting refusal, since O2 cannot hold without it.
- A decision about whether the second reader reads through a gateway tool or a dedicated AWS role.
- A registry row for each new source of market updates and analysis commentary, before anything is written.
- A definition, from Andrew, of what a market update and analysis commentary are and where each comes from.
- A place for the silver tier: which parsed form, and where `OPAL_ALTRESEARCH`'s existing store goes.
- A completeness record that survives the pull (O4), and a record of what expired unread.
- A retention view: whether Microsoft's expiry can be extended by policy, independent of any build.
- An owner for the gateway tools, given the project sits on site Z.

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured between 19:00Z and 21:15Z on 2026-09-29. This part ages; do not cut outcomes from it.

| Item | State |
|---|---|
| Bucket | Live, encrypted, versioned, private by key. Applied by `0.7.0_AE_CloudOps`, re-plan clean |
| Objects | 90 under `teams/transcripts/bronze/`: 30 transcripts, each as raw WebVTT, raw metadata WebVTT and a sidecar |
| By archetype | Morning Meeting 15, OCIO IC 7, Asset Management IC 8 |
| Not landed | 4 expired Morning Meeting rows; the whole Research Meeting; three other Asset Management IC chats and the Opal Investment Committee chat (404 on a derived id); one probe failed locally |
| Readers | Andrew's AWS user only. The second reader has no access |
| Gateway transcript tools | Specified, parked with `1.0.0_SA_CTO~O`, un-parked by Andrew's word, not built |
| Puller | None. The 2026-09-29 pull was a one-off under a one-hour interactive sign-in |
| Commits | Local. Origin's branch head read `0c955d5493` at last check |

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- It does not define "market update" or "analysis commentary". Andrew named the folders, not the sources.
- It does not claim a push trigger exists. Finding 8 is a lead, and change notifications were not tried.
- It does not claim how long a stored sign-in lasts, or that an unattended pull is permitted by the tenant.
- It does not claim why the Research Meeting is refused, or that the four expired rows expired for the reason inferred.
- It did not read the live AWS identity list for an existing identity for `opalbloomberg@opalinvest.com`.
- It did not test the three other Asset Management IC chats or the Opal Investment Committee with a real join link.
  Their 404s came from derived ids, which worked for the meetings that were listed by join link.
- It did not exercise the second-reader route, the two-reader rule against a non-reader, or a scheduled run.
- The search for market-update and commentary prior art used the repository only. Mail, SharePoint and the terminal
  seat's material were not searched.
- The 60 KB average transcript size is an observation from 30 files, not a capacity plan. No volume forecast is made.

---

## REFS TO CARRY

```
BRIEF PATH        docs/briefs/nfra-trnspt-opal-transcript-database-brief-20260929.md
PROJECT           NFRA_TRNSPT (D9) -- NONE-YET (unregistered)
EXISTING PRD      NONE
SIBLING PROJECTS  NFRA_OPLGTW (site Z); OPAL_ALTRESEARCH (closed); LGIC_NAMING / LGIC_CANON
PRIOR ART         docs/briefs/teams-meeting-transcripts-programmatic-pull-recon-20260929.md
                  docs/briefs/opal-gateway-meeting-transcript-tools-spec-20260929.md
                  docs/briefs/transcripts-sharepoint-layout-proposal-20260929.md (SharePoint home superseded by the bucket)
                  org/tier1_exec/4.0.0_SA_CRO/deliverables/TRANSCRIPTS_FIRST_PULL_20260929.md
                  org/tier1_exec/4.0.0_SA_CRO/deliverables/TRANSCRIPTS_READER_PRINCIPAL_20260929.md
                  org/tier1_exec/4.0.0_SA_CRO/deliverables/TRANSCRIPTS_BUCKET_20260929/HANDOFF.md
                  infra/aws/terraform/transcripts/main.tf ; research_transcripts/ ; research_transcripts/schema/series.json
                  org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_PLACEMENT_20260929_170xZ_TRANSCRIPTS_BUCKET_LANDING.md
MEASURED AT       2026-09-29, 19:00Z to 21:15Z, per Part VI
```

---

## ADDENDUM 2026-09-29 (after Andrew's answers; record `ANDREW_DIRECT_20260929_2xxxZ_MARKET_UPDATE_IS_PPTX_COMMENTARY_IS_EMAIL_PUSH_CAN_WAIT.md`)

These answers resolve the first open item of Part VII. Outcomes O6 and O7 keep their wording.

**A1. Market update is a PowerPoint.** Andrew's word. Measured through the gateway as andrew@opalinvest.com on 2026-09-29:

| Location | Finding |
|---|---|
| Andrew's OneDrive | 30 presentations named as a market update, all last modified 2025-12-01, about 4 MB in total. Names run from "Opal Market Update August 19 2024" to "Opal Market Update October 13 2025", plus one "49_Opal Mkt Update Sep 8 2025". Search returned exactly 200 hits, so the search may be capped and the true count may be higher. The folder each sits in was not resolved |
| SharePoint site Opal Capital, Shared Documents, folder "Market Update" | 1 presentation: "Opal Market Update 7-27-2026 (from Manav).pptx", modified 2026-07-27 |
| Opal OCIO site | 0 presentations matching |

Two readings of that table are UNVERIFIED. (a) The OneDrive files look like a one-time copy of the archive on
2025-12-01, since all 30 share a modified date. (b) The 2026 issues appear to be filed in the SharePoint folder, of
which one was found. Neither was checked against the folder's full listing or the other sites. Sites not searched:
Opal Trade Submissions, Opal Consulting, Opal CIO Office for 49 Financial, 49 Financial Internal.

**A2. Analysis commentary is email supplied by Alyssa.** Andrew's word. The route he leans to is Alyssa's agents
pulling through Microsoft Graph. This makes the source a different person's mailbox, so it is a delegated-or-
application access question for Alyssa's identity, not Andrew's. It is not designed here. The gateway's per-user
model means a pull from her mailbox needs her own sign-in or an application permission.

**A3. New dependencies from these answers.**
- A bronze table for presentations keeps the original .pptx byte for byte. Extracting slide text is a later tier.
- A stable identity for a presentation, since a file can be re-saved. Its file hash is available through Graph.
- Who owns the pull for commentary: Alyssa's agents, or this project. Andrew said "probably", so it is open.
- A registry row for each new source, as before. Sources are SharePoint and Outlook mail, not yet registered.

**A4. Push.** Andrew: "push can wait, no pressure for that." Nothing is pushed.


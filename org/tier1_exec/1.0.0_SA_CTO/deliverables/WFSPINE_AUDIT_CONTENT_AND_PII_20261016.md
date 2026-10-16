# NFRA_WFSPINE -- exactly what the Microsoft 365 audit feed carries, how it is picked up, and the PII in it

**Author:** `1.0.0_SA_CTO` (laptop), 2026-10-16 ~05:3xZ, for Andrew and the NFRA_WFSPINE seats on dell1 (call `dell1-...-142a`).
**Andrew-direct, laptop `1.0.0_SA_CTO` terminal, ~05:2xZ, VERBATIM:**

> this is only for operational teams on premises, not all opal addresses. What I want to establish is how much PII is in this,
> what content is in there? i need to know the exact content that is picked up and how, including examples, to better design

**Claim class of this document:**
- Field lists are READ from Microsoft's published schema, "Office 365 Management Activity API schema"
  (learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-schema), read 2026-10-16.
- Nothing has been collected from Opal's tenant (research note @158eb209d9 section 5b: no app, no subscription, no table), so
  **every example below is INVENTED for illustration.** No example is a real Opal record. Which events our licence tier actually
  emits is ABSENT and is settled only by a real sample (section 6).

## 1. How it is picked up

1. One app registration (application permission `ActivityFeed.Read` on the Office 365 Management APIs, not Graph) starts
   subscriptions to four feeds: `Audit.Exchange`, `Audit.SharePoint`, `Audit.AzureActiveDirectory` and `Audit.General`. Teams
   events arrive in `Audit.General`.
2. Microsoft publishes "content blobs": gzipped JSON arrays of audit records for the WHOLE tenant. There is no per-user or
   per-team subscription; the feed cannot be asked for "the ops team only". Each blob stays available about 7 days.
3. The hourly collector lists the new blobs and downloads each one: a JSON array of records like the examples below.
4. Whatever the collector writes is what Opal holds. A population filter (who is in) can act only after download: either before
   anything is written (option a) or after raw storage (option b, the PRD as drafted).

## 2. What every record carries (the common fields, all workloads)

| field | what it holds | PII? |
|---|---|---|
| `CreationTime` | UTC time of the action | no |
| `Operation` | the action, e.g. `FileModified`, `Send`, `MessageSent`, `UserLoggedIn` | no |
| `Workload` | Exchange, SharePoint, OneDrive, MicrosoftTeams, AzureActiveDirectory | no |
| `UserId` | the actor's UPN (email login), e.g. `jdoe@opalinvest.com` | YES: employee identity |
| `UserKey` | an alternate id for the actor (PUID) | YES, as a linkable identifier |
| `ClientIP` | the IPv4 or IPv6 address of the device | YES: location (office or home ISP) |
| `ObjectId` | for files, the FULL path or URL of the file or folder | YES when names carry client names (common) |
| `ResultStatus`, `Id`, `OrganizationId`, `RecordType`, `UserType` | status, record id, tenant id, type codes | no |

## 3. Per workload: the fields that matter and an INVENTED example of each

### 3a. SharePoint and OneDrive (files)

Fields beyond the common ones:
- `SiteUrl`, `SourceRelativeUrl`, `SourceFileName`, `SourceFileExtension` (where the file is and what it is called);
- `DestinationRelativeUrl`, `DestinationFileName` (copy or move only);
- `UserSharedWith`, `SharingType` (who a file was shared with, including external addresses);
- `UserAgent`, `MachineId`, `MachineDomainInfo` (device and sync client);
- `SensitivityLabelOwnerEmail`.

NO file content is in the feed.

INVENTED example (`FileModified`):
```json
{"CreationTime":"2026-10-15T14:02:11","Operation":"FileModified","Workload":"SharePoint",
 "UserId":"jdoe@opalinvest.com","ClientIP":"203.0.113.24",
 "ObjectId":"https://opalinvest.sharepoint.com/sites/Operations/Shared Documents/Billing/Q3/Smith Household - Q3 fee calc.xlsx",
 "SiteUrl":"https://opalinvest.sharepoint.com/sites/Operations/","SourceRelativeUrl":"Shared Documents/Billing/Q3",
 "SourceFileName":"Smith Household - Q3 fee calc.xlsx","SourceFileExtension":"xlsx",
 "UserAgent":"Microsoft Office Excel 2014 (16.0.18025) Windows"}
```
**PII here:** the employee, their IP, and a CLIENT household name in the file name and path. Client names in file names are the
largest PII exposure in this workload.

### 3b. Exchange (mail)

Mailbox records carry:
- `MailboxOwnerUPN`, `LogonUserDisplayName`;
- `ClientIPAddress`, `ClientInfoString`, `ClientMachineName` (Outlook version, device, the PC's name);
- `recipientList` (up to 1,000 recipient addresses) and `recipientCount`;
- `Item.Subject` (the subject line);
- `Item.Attachments` (attachment FILE NAMES and sizes);
- `Item.ParentFolder`, `Item.InternetMessageId`, `Item.Sensitivity`;
- `SendAsUserSmtp`, `SendOnBehalfOfUserSmtp`.

NO message body and NO attachment content.

INVENTED example (`Send`):
```json
{"CreationTime":"2026-10-15T15:40:02","Operation":"Send","Workload":"Exchange",
 "UserId":"jdoe@opalinvest.com","MailboxOwnerUPN":"jdoe@opalinvest.com","ClientIPAddress":"203.0.113.24",
 "ClientInfoString":"Client=MSExchangeRPC;Outlook 16.0","ClientMachineName":"OPAL-OPS-07",
 "Item":{"Subject":"RE: Smith - wire to Schwab acct ending 4421 for Friday",
         "ParentFolder":{"Path":"\\Sent Items"},
         "Attachments":"Smith_Wire_Authorization_signed.pdf (182340b)",
         "InternetMessageId":"<abc123@opalinvest.com>"},
 "recipientList":["ops@opalinvest.com","jane.smith@gmail.com"],"recipientCount":2}
```
**PII here:**
- the subject line, which can carry client names, account fragments and transaction intent;
- an EXTERNAL client's personal email address;
- the attachment name;
- the PC name and IP.

Subject lines and recipient lists are the most sensitive mail fields. They can be Reg S-P customer information.

INVENTED example (`MailItemsAccessed`, a mail being opened or synced): one record per access batch, listing the folder and each
item's `InternetMessageId` and size. Depending on tier and settings it carries no subject. Whether our tier emits this event at
all is ABSENT.

### 3c. Teams (chats, channels, meetings)

Fields:
- `Members` (UPN, display name and role of the participants, including guests);
- `TeamName`, `ChannelName`;
- `Messages[]`: ids, `ChatThreadId`, `ChatName`, `ParentMessageId`, sizes;
- `MessageId`, `MessageSizeInBytes`;
- `MessageURLs`: any URL pasted into a message;
- `Organizer` (meetings);
- `ExtraProperties` (key and value pairs, contents not specified by Microsoft).

The schema defines NO message-text field. `ChatName` and `MessageURLs` can still carry meaningful text.

INVENTED example (`MessageSent`):
```json
{"CreationTime":"2026-10-15T16:05:44","Operation":"MessageSent","Workload":"MicrosoftTeams",
 "UserId":"jdoe@opalinvest.com","ClientIP":"203.0.113.24",
 "ChatThreadId":"19:meeting_XYZ@thread.v2","ChatName":"Smith onboarding",
 "Members":[{"UPN":"jdoe@opalinvest.com","DisplayName":"Jane Doe","Role":0},
            {"UPN":"lharmon@opalinvest.com","DisplayName":"Lauren Harmon","Role":1}],
 "MessageId":"1697472344000","MessageSizeInBytes":412,
 "MessageURLs":["https://opalinvest.sharepoint.com/sites/Operations/.../Smith%20IPS.docx"]}
```
**PII here:** who talked to whom and when, the chat's NAME (which can be a client's name), and any linked URL (which can be a
client file path). The message text itself is NOT present.

### 3d. Entra ID sign-ins (`UserLoggedIn`, STS logon)

Fields:
- `ActorIpAddress` and `ClientIP`;
- `DeviceProperties` (device id, name, OS, browser, compliance, trust type);
- `Application` (which app);
- `ErrorCode` (success or failure);
- `ExtendedProperties` (user agent, request type).

**PII here:** the IP address on every sign-in, which gives location over time (office versus home) and device identity. This is
the most surveillance-like stream, and it says nothing about workflow.

## 4. PII inventory, ranked by exposure

| rank | data | where | whose |
|---|---|---|---|
| 1 | mail subject lines | Exchange `Item.Subject` | clients (names, account fragments, money movements) |
| 2 | external recipient addresses | Exchange `recipientList`, SharePoint `UserSharedWith` | clients and counterparties (personal emails) |
| 3 | file and folder names and paths | SharePoint `ObjectId`, `SourceFileName`, `SourceRelativeUrl`; Exchange `Attachments`; Teams `MessageURLs` | clients (household names in file names) |
| 4 | IP addresses and device identity | every workload; Entra sign-ins | employees (location over time) |
| 5 | chat and team names, participants | Teams `ChatName`, `TeamName`, `Members` | employees, guests, sometimes clients |
| 6 | employee identity and the timeline itself | `UserId` on every record | employees: this IS the monitoring |

**Never in the feed:** mail bodies, attachment contents, document contents, chat message text, call audio and transcripts.
Those are Layer 2 (research note section 3) and need separate Graph permissions that Andrew's role cannot grant alone.

## 5. What his scope word changes ("only operational teams on premises, not all opal addresses")

- **Population:** the named members of the operational team(s), not all 21 named employees and not shared mailboxes. The
  source feed stays tenant-wide (section 1.2), so excluding everyone else is entirely our filter. That makes WHERE the filter
  sits (call 142a) matter more: with option (b), every non-ops employee's subjects, recipients and file names would sit in raw
  storage.
- **"On premises"** has two readings. This seat does not choose between them; it needs his word:
  1. "the ops staff who work in the office" (a list of people); or
  2. "only activity performed from the office", which the collector can enforce by `ClientIP` matching Opal's office egress IPs.
  Reading 2 would also drop home and mobile activity even for ops staff, and with it most of the location-over-time exposure in
  rank 4.
- **Design levers that cut PII without losing the workflow signal** (proposals for the PRD, not decisions):
  - drop the Entra sign-in feed entirely (it is location tracking, not workflow);
  - keep `Item.Subject` out by default, or store a hash of it so the same thread links across people without the text;
  - map external recipients to a domain-only value (`gmail.com`, `schwab.com`);
  - keep file IDs and extensions, and store file names only for the SharePoint sites he names;
  - store an office/remote flag instead of the raw IP.

## 6. How to see REAL Opal examples before designing further

1. **Purview audit search (Andrew, no build):** compliance.microsoft.com > Audit > search one ops person, one day, all
   activities > export CSV. This shows exactly what our tier emits. A seat can then profile the export the way the Cottonwood
   CRM was profiled: field names, fill rates and value shapes, with no values copied anywhere. It needs the Audit Reader role.
2. **Round-1 cell 1 sample:** after consent, pull ONE hour of blobs into a quarantine location, profile the field fill and
   shapes, write only the profile, and delete the blobs. This is a recursive delete, so it needs his confirmation.

Either one closes the ABSENT items in the research note's section 6: whether audit is enabled, the licence tier, which mail and
Teams events are emitted, and the volume per person.

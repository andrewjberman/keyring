# Transcript Directive Intake

**Seat:** 1.0.0_SA_CTO
**Date:** 2026-08-31
**Sources:** `C:\Users\AndrewBerman\Desktop\Whisper Transcriptions\Mfa UM_5391.txt`; `Ticketing_7880.txt`; `Asset class nomenclature_6911.txt`

## Executive Read

Andrew supplied three transcript inputs and a placement hypothesis:

1. MFA and user management should become the first project under a new D12 directive named Platform Ops.
2. Ticketing updates should sit under D7 Ticketing System.
3. Asset-class nomenclature should become the next primary D4 project series after the remaining Satellites/D4 work is closed.

CTO read supports that split. Do not hand-edit `org/missions/DIRECTIVES.yaml` as the first act: it is a derived view and the row owner is MSTR. The correct first deliverable is a readback package and then a register-owner cut of the Stage-1/PRD surfaces.

## D12 Candidate: Platform Ops

**Recommended directive:** `D12 Platform Ops`

**First project:** user management and MFA for the client portal.

Scope from transcript:

- email or SMS OTP MFA at login, with a remembered-device/session-cookie policy so users are not forced through MFA on every login;
- storage model for phone number and MFA preferences, likely extending `OPAL users v2`;
- review and redesign of onboarding and account creation;
- front-end admin UI for adding accounts/users, rather than backend-table-only creation;
- client partner admins may add users for their firm, gated by partner-table/RBAC organization roles;
- partner table should drive authorization, not become the primary store for all user details.

Existing carrier to recover from:

- `PORTAL_AUTHHARD` is closed by spring-clean, not superseded by a successor.
- Its PRD already contains MFA/account-lifecycle work, but WS3 was privileged-role native TOTP, while this transcript asks for broader user-management UX and email/SMS OTP.
- Recommendation: do not simply reopen `PORTAL_AUTHHARD`; cut a new D12 project that imports the relevant hardening prior art and widens the scope to account lifecycle and delegated admin.

Proposed project code: `PLATFORM_OPS_USERMGMT`.

## D7 Candidate: Ticketing vNext

**Recommended directive:** keep under `D7 Ticketing System`.

Scope from transcript:

- ticket creation attachments, stored durably and retrievably;
- likely ticket-specific S3 home, with partner/firm and ticket-level path design;
- architecture re-read of current Lambda and DynamoDB ticket journey before bucket shape is chosen;
- In Progress messaging/chat between Opal users and clients;
- chat transcript saved against the ticket ID, likely in the same ticket artifact store;
- Opal-side notifications: ticket outset plus reminder if unaddressed, initially one business-hours reminder;
- client-side notifications: filed, accepted, completed, and later chat/message notifications;
- tie Bloomberg/SiteZ agent operations into the ticket process as tightly as possible;
- front-end IA for Opal and client views: New/Open, In Progress, Completed; client Submit tab should show submitted-but-unaccepted tickets until acceptance moves them to In Progress.

Existing carrier to recover from:

- `OPAL_TICKET` is closed by spring-clean membership, explicitly not as a work verdict.
- The live project record says recovery can be a reinvented project.
- Current D7 already has backend ticket API, portal Ticket Center, service identity, Teams/Outlook notification history, client submit form, and known authorization floor history.

Recommendation: cut a D7 vNext project rather than reopen the original row unbounded. First phase should be a source architecture read of the current ticket API/table/events/frontend, then a design gate for the S3 attachment/transcript store and notification semantics.

Proposed project code: `OPAL_TICKET_VNEXT`.

## D4 Candidate: Asset-Class Nomenclature

**Recommended directive posture:** D4 becomes the primary home for asset-class nomenclature after current D4/Satellites cleanup is not carrying live closure debt.

Scope from transcript:

- canonical top-level order: Fixed Income, Cash, Equity, Structured, Commodities, Alternatives;
- color recommendation: Fixed Income green, Cash green-family or separately assigned during design, Equity blue, Structured pink, Commodities gold, Alternatives orange;
- Structured includes options, VIX, futures, overlays, VXX, and structured notes;
- Commodities includes physical commodities such as gold, nickel, silver, crypto, and commodity indices such as GSCI-like exposures;
- Alternatives includes remaining alternatives: real assets excluding commodities, private equity, private credit, real estate, and similar;
- locate the centralized origin of nomenclature, likely ETF classifier or another shared classifier;
- update all affected surfaces consistently: Positioning, Philosophy, and Capital Market Assumptions.

Existing carrier to recover from:

- `ETFS_SATELLITES` is complete by Andrew smoke-test.
- `ETFS_POSITIONING` remains the active broader D4 carrier, but the new transcript is not just an ETF/satellite feature. It is a platform taxonomy change affecting multiple portal pages and data classifiers.

Recommendation: after D4 cleanup/closure is read back, reframe D4 around asset-class nomenclature with a new primary project. This should start with a classifier-origin census before UI work, because multiple pages must consume one canonical taxonomy rather than each page inventing colors/order.

Proposed project code: `ASSET_CLASS_NOMENCLATURE`.

## Recommended Next Actions

1. Read back to Andrew that the split is D12/User Management, D7/Ticketing vNext, and D4/Asset-Class Nomenclature after current D4 closure.
2. Ask MSTR/register owner to add D12 Platform Ops to the directive model and cut the three Stage-1 project records.
3. Draft PRD stubs in this order:
   - `docs/architecture/D12_PLATFORM_OPS_USERMGMT_PRD.md`
   - `docs/architecture/D7_TICKETING_VNEXT_PRD.md`
   - `docs/architecture/D4_ASSET_CLASS_NOMENCLATURE_PRD.md`
4. Do not edit `DIRECTIVES.yaml` directly from this seat until the register owner confirms the canonical row source and D12 insertion path.

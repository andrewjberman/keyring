# Session Log: ADVI_PROFIL.007 — Admin "My Profile" Toggle (bundled with .006 cache policy)

**Agent:** 0.4.2_RD_AdvisorIntelligence
**Date:** 2026-04-10
**Task Orders:** `ADVI_PROFIL.007.rd-admin-my-profile-toggle`, `ADVI_PROFIL.006.rd-client-cache-policy` (bundled)
**Status:** Working tree ready for DT handoff
**Wave:** 4 (polish + cache policy)

---

## Summary

Two small bundled changes:

**.007** — Partner-firm admins (Travis Penfield persona) get a convenience "My Profile" button on the BooksTab firm landing that flips the view in-place to their own `AdvisorPublicProfile` without a tab switch. Gated on `claims.advisorId != null` so internal Opal admins (who always have null advisorId by design) never see it.

**.006** — Decision (c) "split level": L3 client-detail and L4 account-detail `useQuery` keys get `gcTime: 0` for immediate cache eviction on unmount. Protects PII-sensitive client rosters / tax lots from lingering in memory after navigation.

Andrew's resolution quote (relayed by 0.4.0_DT_ClientPlatform, 2026-04-10 ~17:20 EDT): *"THE TOGGLE IS JUST THERE FOR CONVENIENCE, NOT FOR SECURITY, ITS JUST TO FLIP BETWEEN THE PAGES"*. Scope interpreted as "make it functional for the persona that needs it" — partner-firm admins who are also advisors.

---

## .007 Implementation

### Files touched

1. **`portal/src/pages/AdvisorIntelligence/AdvisorIntelligence.tsx`** — one-line gate change per the finalized resolution:

```typescript
- const isFirmAdmin = internal
+ const isFirmAdmin = internal || isAdmin()
```

With a comment block explaining the AE `.004a` Option 3 admin bypass semantics that make this safe (partner-firm admins can drill into other same-firm advisors without getting 403'd at the edge).

Effect: Travis (`role=admin`, `firmId=49financial`, `advisorId=travis_penfield`) now routes to `BooksTab` on Tab 3 ("Books" label). Chase (`role=user`) unchanged — still routes to `NonAdminProfileTab` (no button, no tab flip). Internal Opal admins unchanged.

2. **`portal/src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx`** (BooksTab component):
   - Added imports: `useAuth`, `User` icon, `getFirmLeaderboard`, `PlatinumLeaderboardResponse`, `AdvisorPublicProfile`
   - Added at top of `BooksTab`:
     ```typescript
     const { claims } = useAuth()
     const myAdvisorId = claims?.advisorId ?? null
     const [viewMode, setViewMode] = useState<'landing' | 'my-profile'>('landing')
     ```
   - Added `useQuery` for `['firm-leaderboard', firmOverride]` — shared cache key with `AdvisorsTab` and `NonAdminProfileTab`, so React Query dedupes the fetch across the three consumers. Gated on `enabled: viewMode === 'my-profile' && !!myAdvisorId && !!firmId` so it only fires when the button is actually clicked.
   - Added early render branch after the guards (before L3/L2/N1 drill chain):
     ```tsx
     if (viewMode === 'my-profile' && myAdvisorId) {
       if (!employeeDataForMyProfile) return <LoadingInline className="py-12" />
       return (
         <AdvisorPublicProfile
           employeeData={employeeDataForMyProfile}
           advisorId={myAdvisorId}
           firmOverride={firmOverride}
           showBackButton={true}
           onBack={() => setViewMode('landing')}
         />
       )
     }
     ```
   - Added "My Profile" button at the top of the N1 render block, gated on `myAdvisorId != null`:
     ```tsx
     {myAdvisorId && (
       <div className="flex justify-end">
         <button
           onClick={() => setViewMode('my-profile')}
           className="flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium rounded-md bg-white/5 text-white/70 hover:bg-white/10 hover:text-white border border-white/10 transition-colors"
         >
           <User size={12} />
           My Profile
         </button>
       </div>
     )}
     ```

### Persona walkthrough

| Persona | `isInternal` | `isAdmin()` | `claims.advisorId` | `isFirmAdmin` (post-.007) | Tab 3 route | Button visible? | Effect |
|---------|:-:|:-:|:-:|:-:|-------------|:-:|--------|
| **Travis** (49fin admin+advisor) | false | true | `travis_penfield` | **true** (via new `|| isAdmin()`) | BooksTab | **yes** | Clicks button → own `AdvisorPublicProfile` with back. AE `.004a` Option 3 lets his leaderboard drills through. |
| **Chase** (49fin non-admin) | false | false | `chase_bertrand` | false | NonAdminProfileTab | n/a | Unchanged — lands directly on his own profile via the non-admin path. No button needed. |
| **Internal Opal admin** | true | true | `null` | true (unchanged) | BooksTab | **no** (gate `advisorId != null` fails) | Unchanged — sees global leaderboard, no "My Profile" button because they don't have their own advisor identity. |

### Design choices

- **Button placement** — N1 landing view only, right-aligned above `CanonicalBookView`. When drilled into L2/L3/L4, the button is not visible (user navigates back via the existing breadcrumb/back chain, then clicks the button from N1).
- **Local state flip, not tab switch** — per criterion 3. No URL change, no tab navigation. `viewMode` is transient BooksTab state.
- **Leaderboard `useQuery` gated on `viewMode === 'my-profile'`** — avoids a wasted firm-wide fetch for admins who never click the button. When they DO click, the shared cache key means they get instant data if `AdvisorsTab` already loaded it this session.
- **Did NOT broaden `canDrillIntoAdvisor`** — already gated on `isFirmAdmin` which now includes Travis via the new gate. No separate prop change needed.

---

## .006 Implementation (bundled)

Decision (c) split level: L3/L4 `useQuery` keys get `gcTime: 0` for PII-sensitive eviction. L2 stays at default `gcTime` (5 min, matches `staleTime`).

### Files touched

1. **`portal/src/pages/AdvisorIntelligence/AdvisorBookView.tsx`** — 2 keys:
   - `['advisor-book-client', advisorId, selectedClientKey, firmOverride]` → added `gcTime: 0`
   - `['advisor-book-account', advisorId, selectedAccountId, firmOverride]` → added `gcTime: 0`

2. **`portal/src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx`** — same 2 keys (admin path):
   - `['advisor-book-client', selectedAdvisorId, selectedClientKey, firmOverride]` → added `gcTime: 0`
   - `['advisor-book-account', selectedAdvisorId, selectedAccountId, firmOverride]` → added `gcTime: 0`

Each change is 4 lines (the `gcTime: 0` + a two-line comment explaining the PII-sensitivity rationale).

### Runtime behavior

- Clicking a client from the L2 roster fetches L3 data, renders `AdvisorBookClientDetail`, user views the client's accounts
- User navigates back to L2 (via Back button) → `selectedClientKey = null` → the `['advisor-book-client', ...]` query unmounts → `gcTime: 0` evicts the cached client detail immediately
- Re-clicking the same client triggers a fresh fetch (no cached response)
- Same pattern for L4 account detail

Trade-off: any client/account revisit within the same session incurs a full refetch. Acceptable per the .006 decision because client-level data is PII-sensitive and we don't want it lingering in memory across unmounts. `staleTime: 5 * 60 * 1000` is kept for the case where a user rapidly toggles between a client and another view within the same drill session without unmounting — the query stays fresh for 5 minutes before refetching if the component stays mounted.

---

## Verification

### tsc + eslint

- `bun run tsc -b` → exit 0
- `bun run eslint src/pages/AdvisorIntelligence/{AdvisorIntelligence.tsx, tabs/ClientsTab.tsx, AdvisorBookView.tsx}` → **0 errors**

### comp-transform schema-check

- `comp-transform schema-check ClientsTab` → all rendered fields match their response types. The unused-field list is the expected set of fields that flow through to child components (`AdvisorBookClientDetail`, `AdvisorBookAccountDetail`) rather than being rendered directly by ClientsTab — comp-transform doesn't trace cross-file flow but schema-check on the child components confirmed byte-identical rendering in the `.005` session.

### Manual test matrix (to run post-DT-ship)

Per criterion 6 of `.007` TO:

1. **Travis login** (`travis.penfield@49financial.com` / `q1p0666`):
   - Tab 3 label should read "Books" (not "Profile") — confirms `isFirmAdmin = internal || isAdmin()` is firing true
   - BooksTab N1 firm dashboard renders with 49financial leaderboard
   - "My Profile" button visible in top-right of N1 landing
   - Click button → `AdvisorPublicProfile` renders with `showBackButton=true`, advisorId = `travis_penfield`
   - Click back → returns to BooksTab N1 landing
   - Leaderboard rows are clickable, drill into any 49fin advisor's profile (AE `.004a` Option 3 lets the backend serve it)

2. **Chase login** (`chase.bertrand@49financial.com` / `q1p0666`):
   - Tab 3 label should read "Profile" (not "Books") — `isFirmAdmin` false
   - Renders `NonAdminProfileTab` with Chase's own `AdvisorPublicProfile`
   - No "My Profile" button anywhere (he's not on BooksTab)
   - Drill L2 → L3 → L4 in his own book works (the `.005` drill chain)

3. **Internal Opal admin login** (Andrew's own account):
   - Tab 3 label should read "Books" — unchanged behavior
   - BooksTab N1 firm dashboard renders
   - "My Profile" button **absent** — `claims.advisorId` is null for Opal admins by design

---

## Compiler Tools

| Tool | Phase | Result |
|------|-------|--------|
| `git log origin/DEV -3` | 1 | ✓ `.005 (36bf0fd)` + `.003 (40e6208)` both present |
| Re-read `.007` TO inline | 1 | ✓ finalized single-line gate change (no two-gate split) |
| `bun run tsc -b` | 3 | ✓ exit 0 |
| `bun run eslint` on 3 touched files | 3 | ✓ 0 errors |
| `comp-transform schema-check ClientsTab` | 3 | ✓ PASS (unused fields flow through to child components per .005 extraction) |

Compiler tools log line: `2026-04-10 | 0.4.2_RD | ADVI_PROFIL.007+.006 | isFirmAdmin gate broadened for partner-firm admins, My Profile button added to BooksTab N1, L3/L4 gcTime:0 applied in both paths, tsc+eslint green`

---

## Files touched (summary)

| File | Purpose | Change |
|------|---------|--------|
| `portal/src/pages/AdvisorIntelligence/AdvisorIntelligence.tsx` | .007 gate | +1 line (gate expansion), +7 lines comment |
| `portal/src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx` | .007 button, .006 L3/L4 gcTime | +55 lines (button + viewMode + useAuth + leaderboard query + my-profile branch), +6 lines (.006 gcTime + comments) |
| `portal/src/pages/AdvisorIntelligence/AdvisorBookView.tsx` | .006 L3/L4 gcTime | +6 lines (2 gcTime entries + comments) |

---

## Handoff

Working tree ready for DT ship pass. Per criterion 8 / requirement 4, RD does not commit or push. Broker message pending to `0.4.0_DT_ClientPlatform`.

---

## Follow-ups

None. `.006` and `.007` are the last two TOs in the ADVI_PROFIL wave 3-4 chain. After DT ships, the whole `ADVI_PROFIL` project is complete end-to-end through the frontend.

Optional polish items that could be picked up later but are NOT required to close the project:
- Lift `OpenLotsWithFilters` / `OpenLotsTable` / tax-lot helpers out of `ClientsTab.tsx` into `panels/` (cosmetic, improves file structure)
- Add a `/frontend-dev` visual-testing cycle on the three new drill paths (admin, non-admin, admin-My-Profile) — flagged to DE as `.008`

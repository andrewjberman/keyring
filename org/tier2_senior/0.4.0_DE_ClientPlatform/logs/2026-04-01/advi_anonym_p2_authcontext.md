# ADVI_ANONYM P2: canSeeCleartext() AuthContext Helper - 0.4.0_DE_ClientPlatform

**Date:** 2026-04-01
**Task Order:** ADVI_ANONYM.005.de-authcontext-canseecleartext.md

## Objective
Add `canSeeCleartext()` boolean helper to AuthContext so RD components can gate
pseudonymization indicators based on user tier and role.

## Work Completed
- Read AuthContext.context.ts and AuthContext.tsx to understand existing shape -- DONE
- Added `canSeeCleartext: () => boolean` to AuthContextType interface -- DONE
- Implemented helper with useCallback in AuthProvider -- DONE
- Added to provider value object -- DONE
- Verified `bunx tsc -b` passes clean -- DONE
- Committed to portal DEV branch -- DONE
- Messaged COO with commit hash -- DONE

## Decisions Made
- **Used useCallback with [state.claims, state.user] deps:** Matches the pattern of existing helpers (isInternal, isAdmin, canAccessFirm). Consistent with codebase conventions.
- **Reads tier from state.claims, role from state.user:** These are the canonical locations already established in AuthContext. No new data sources needed.

## Files Modified
- `portal/src/contexts/AuthContext.context.ts` - Added `canSeeCleartext: () => boolean` to AuthContextType interface
- `portal/src/contexts/AuthContext.tsx` - Implemented canSeeCleartext helper and added to provider value

## Blockers
None.

---

## Current State
**Status:** COMPLETE
**Active branch:** portal DEV (commit 11ee364)

canSeeCleartext() is committed and available on portal DEV. TypeScript compiles clean.
RD (.006) can now consume it via `const { canSeeCleartext } = useAuthContext()`.
No merge to PROD -- DT handles that after RD completes .006.

## Next Steps
1. **RD begins ADVI_ANONYM.006** -- UI indicators on pseudonymized surfaces using canSeeCleartext()
2. **DT merges DEV -> PROD** -- after RD .006 is complete and reviewed

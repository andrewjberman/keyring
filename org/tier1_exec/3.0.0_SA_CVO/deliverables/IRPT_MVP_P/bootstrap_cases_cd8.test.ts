import { expect, test } from 'bun:test'
import { parseIrEnvelope } from './src/pages/InvestorReporting/contracts/envelope'
import { adaptResolvedScope } from './src/pages/InvestorReporting/contracts/adapt'
import { LiveClient } from './src/api/endpoints/investor-reporting'
import actual from './bootstrap-actual.json'
import positive from './src/pages/InvestorReporting/fixtures/wire/ResolvedScope.valid.json'

for (const role of ['advisor', 'operations'] as const) {
  test(`real ${role} bootstrap passes actual envelope and adapter`, () => {
    const parsed = parseIrEnvelope<any>('resolve-scope', actual.cases[role])
    expect(parsed.refused).toBe(false)
    expect(parsed.data.permittedAccountIds).toEqual(actual.expected_accounts)
    expect(adaptResolvedScope(actual.cases[role].data as any).viewerPolicy.derivedBy).toBe('server')
  })
  test(`real ${role} bootstrap completes actual LiveClient resolveScope`, async () => {
    const api = new LiveClient({ transport: { async request<T>() { return actual.cases[role] as T } }, telemetrySink: () => undefined })
    const scope = await api.resolveScope({ tenant: 'bootstrap', requested: {
      firmId: null, clientId: null, relationshipId: null, accountIds: [] } })
    expect(scope.permittedAccountIds).toEqual(actual.expected_accounts)
  })
}

test('published valid document remains a positive consumer control', () => {
  const wire = positive.instance
  expect(adaptResolvedScope(wire as any).permittedAccountIds).toEqual(wire.permitted_account_set)
  expect(parseIrEnvelope<any>('resolve-scope', { contract_version: 'v1', operation: 'resolve-scope',
    firm_id: wire.verified_request_firm_id, data: wire,
    unprojected_grant: { count: 0, denominator: 3, kinds: {} } }).refused).toBe(false)
})

for (const [name, answer] of Object.entries(actual.negatives)) {
  test(`auth negative ${name} remains refused by actual frontend`, () => {
    const parsed = parseIrEnvelope('resolve-scope', answer)
    expect(parsed.refused).toBe(true)
    expect(parsed.data).toBe(null)
  })
}

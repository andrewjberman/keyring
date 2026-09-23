import { expect, test } from 'bun:test'
import { LiveClient, FixtureAdapter, IrRequestError, type IrTransport } from './src/api/endpoints/investor-reporting'
import { parseIrEnvelope, EnvelopeMismatch } from './src/pages/InvestorReporting/contracts/envelope'
import fixture from './src/pages/InvestorReporting/__tests__/mvp-selection/tests/producer-selection.json'

const clone = () => structuredClone(fixture.success)

test('exact subset order, request copy and contract header survive serialization', async () => {
  const calls: any[] = []
  const transport: IrTransport = { async request<T>(url, init) { calls.push({ url, ...init }); return clone() as T } }
  const api = new LiveClient({ transport })
  const ids = ['acc_' + 'b'.repeat(24), 'acc_' + 'a'.repeat(24)]
  const pending = api.createSelection({ scope_kind: 'ACCOUNT', scope_ids: ids })
  ids.reverse()
  await pending
  expect(JSON.parse(calls[0].body)).toEqual({ scope_kind: 'ACCOUNT', scope_ids: [...ids].reverse() })
  expect(new Headers(calls[0].headers).get('x-contract-version')).toBe('v1')
})

test.each(['account_set_id', 'directory_revision', 'selected_account_set_fingerprint',
           'permitted_account_set_fingerprint', 'entitlement_revision'])('missing identity field %s refuses', key => {
  const body: any = clone()
  delete body.data[key]
  expect(() => parseIrEnvelope('selection-create', body)).toThrow(EnvelopeMismatch)
})

test.each(['duplicate', 'empty', 'mismatch', 'raw'])('invalid account membership %s refuses', mode => {
  const body = clone()
  if (mode === 'duplicate') body.data.account_ids.push(body.data.account_ids[0])
  if (mode === 'empty') body.data.account_ids = []
  if (mode === 'mismatch') body.data.selected_account_ids = ['acc_' + 'f'.repeat(24)]
  if (mode === 'raw') body.data.account_ids = body.data.selected_account_ids = ['12345']
  expect(() => parseIrEnvelope('selection-create', body)).toThrow(EnvelopeMismatch)
})

test('producer kind count map is accepted and negative/fractional counts refuse', () => {
  const body: any = clone()
  body.unprojected_grant = { count: 2, denominator: 4, kinds: { ACCOUNT: 1, RELATIONSHIP: 1 } }
  const parsed: any = parseIrEnvelope('selection-create', body)
  expect(parsed.data.account_set_id).toBe(body.data.account_set_id)
  expect(body.unprojected_grant.kinds).toEqual({ ACCOUNT: 1, RELATIONSHIP: 1 })
  for (const count of [-1, 0.5, '1']) {
    body.unprojected_grant.kinds.ACCOUNT = count
    expect(() => parseIrEnvelope('selection-create', body)).toThrow(EnvelopeMismatch)
  }
})

test('boundary refusal without firm suppresses even success-shaped data', async () => {
  const body: any = structuredClone(fixture.refusal)
  delete body.firm_id
  body.data = clone().data
  const parsed = parseIrEnvelope('selection-create', body)
  expect(parsed.refused).toBe(true)
  expect(parsed.data).toBeNull()
  const transport: IrTransport = { async request<T>() { return body as T } }
  const api = new LiveClient({ transport })
  try {
    await api.createSelection(fixture.request as any)
    throw new Error('unexpected success')
  } catch (error) {
    expect(error).toBeInstanceOf(IrRequestError)
    expect((error as IrRequestError).publicReasonCode).toBe('OBJECT_NOT_COVERED')
  }
})

test('wrong envelope operation/version cannot issue a retained selection', () => {
  for (const [key, value] of [['operation', 'resolve-scope'], ['contract_version', 'v0']]) {
    expect(() => parseIrEnvelope('selection-create', { ...clone(), [key]: value })).toThrow(EnvelopeMismatch)
  }
})

test('retained identity and all explicit date/root carriers reach requests', async () => {
  const calls: string[] = []
  const transport: IrTransport = { async request<T>(url) { calls.push(url); return {} as T } }
  const api = new LiveClient({ transport })
  const base = { tenant: '49financial', scopeFingerprint: 'CACHE_ONLY', revision: 'r1', accountSetId: clone().data.account_set_id }
  await api.getPerformanceReport({ ...base, start: '2024-02-29', end: '2026-09-22' }).catch(() => {})
  await api.getHoldingsSnapshot({ ...base, asOf: '2026-09-21', rootRef: 'root /&+' }).catch(() => {})
  const performance = new URL(calls[0], 'https://test.invalid')
  const holdings = new URL(calls[1], 'https://test.invalid')
  expect(performance.pathname.endsWith(base.accountSetId)).toBe(true)
  expect(performance.searchParams.get('start')).toBe('2024-02-29')
  expect(performance.searchParams.get('end')).toBe('2026-09-22')
  expect(holdings.searchParams.get('as_of')).toBe('2026-09-21')
  expect(holdings.searchParams.get('root_ref')).toBe('root /&+')
  expect(calls.join('')).not.toContain('CACHE_ONLY')
})

test('malformed retained refs refuse before either custody transport call', async () => {
  let calls = 0
  const transport: IrTransport = { async request<T>() { calls++; return {} as T } }
  const api = new LiveClient({ transport })
  for (const accountSetId of ['', 'all', 'sel_' + 'A'.repeat(64), 'sel_' + 'a'.repeat(63), 'a'.repeat(64)]) {
    const base = { tenant: '49financial', scopeFingerprint: 'cache', revision: 'r1', accountSetId }
    await expect(api.getPerformanceReport({ ...base, start: '2026-01-01', end: '2026-09-22' })).rejects.toBeInstanceOf(IrRequestError)
    await expect(api.getHoldingsSnapshot(base)).rejects.toBeInstanceOf(IrRequestError)
  }
  expect(calls).toBe(0)
})

test('fixture selection requires explicit service and returns its actual identity', async () => {
  const api = new FixtureAdapter({ createSelection: async () => clone().data })
  expect(await api.createSelection(fixture.request as any)).toEqual(clone().data)
})

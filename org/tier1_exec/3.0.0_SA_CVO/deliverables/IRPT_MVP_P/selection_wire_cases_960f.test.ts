import { expect, test } from 'bun:test'
import { parseIrEnvelope, EnvelopeMismatch } from './src/pages/InvestorReporting/contracts/envelope'
import { LiveClient, IrRequestError, type IrTransport } from './src/api/endpoints/investor-reporting'
import refusal from './actual-selection-refusal.json'

test('fresh actual selection refusal remains a refusal', async () => {
  expect(parseIrEnvelope('selection-create', refusal).data).toBe(null)
  const transport: IrTransport = { async request<T>() { return refusal as T } }
  try {
    await new LiveClient({ transport }).createSelection({ scope_kind: 'RELATIONSHIP', scope_ids: ['rel-test'] })
    throw new Error('unexpected success')
  } catch (error) {
    expect(error instanceof IrRequestError).toBe(true)
    expect((error as IrRequestError).publicReasonCode).toBe('OBJECT_NOT_COVERED')
  }
})

test('selection parser rejects reintroduced internal correlation', () => {
  const mutated = structuredClone(refusal) as any
  mutated.status.internal_correlation_id = 'corr-must-remain-internal'
  expect(() => parseIrEnvelope('selection-create', mutated)).toThrow(EnvelopeMismatch)
})

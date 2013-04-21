chai = require 'chai'
expect = chai.expect

d2b = require '../src/double_to_binary'
bi = require '../src/bit_insertion'
gnp = require '../src/get_next_prev'
nb = require '../src/num_bits'
sb = require '../src/swap_bits'
cm = require '../src/check_missing'


describe 'bit insertion', ->
  it 'should be 00000000000000000000010001001100', ->
    res = bi 1024, 19, 2, 6
    expect(res).to.be.equals '00000000000000000000010001001100'

describe 'double 2 binary', ->
  it 'should be 10000000000000000000000000000000', ->
    res = d2b 0.5
    expect(res).to.be.equals '10000000000000000000000000000000'

  it 'should be 11000000000000000000000000000000', ->
    res = d2b 0.75
    expect(res).to.be.equals '11000000000000000000000000000000'

  it 'should be 10100000000000000000000000000000', ->
    res = d2b 0.625
    expect(res).to.be.equals '10100000000000000000000000000000'

  it 'should be Error', ->
    res = d2b 0.7
    expect(res).to.be.equals 'Error'

describe 'get next and prev', ->
  describe '#bit_ary', ->
    it 'sould be 10', ->
      res = gnp.bit_ary 2
      expect(res).to.be.equals '10'
    it 'sould be 11001', ->
      res = gnp.bit_ary 25
      expect(res).to.be.equals '11001'

  describe '#get_next', ->
    it 'should be 4', ->
      res = gnp.get_next 2
      expect(res).to.be.equals 4
    it 'should be 25', ->
      res = gnp.get_next 22
      expect(res).to.be.equals 25
  describe '#get_prev', ->
    it 'should be 2', ->
      res = gnp.get_prev 4
      expect(res).to.be.equals 2
    it 'should be 22', ->
      res = gnp.get_prev 25
      expect(res).to.be.equals 22

describe 'number of bit to swap', ->
  it 'should be 2', ->
    res = nb 31, 14
    expect(res).to.be.equals 2

  it 'should be 0', ->
    res = nb 15, 15
    expect(res).to.be.equals 0

  it 'should be 1', ->
    res = nb 15, 7
    expect(res).to.be.equals 1

describe 'swap bits of integer', ->
  it 'should be 6', ->
    res = sb 9
    expect(res).to.be.equals 6
  it 'should be 12', ->
    res = sb 12
    expect(res).to.be.equals 12

describe 'check missing integer', ->
  it 'should be 2', ->
    arr = [0, 3, 1]
    res = cm arr
    expect(res).to.be.equals 2
  it 'should be 7', ->
    arr = [0, 4, 3, 5, 1, 2, 6]
    res = cm arr
    expect(res).to.be.equals 7

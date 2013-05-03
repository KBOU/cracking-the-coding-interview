chai = require 'chai'
expect = chai.expect

Line = require '../src/intersect'
Calculation = require '../src/calculation'
Half = require '../src/make_them_half'
MostPoints = require '../src/line_with_most_points'
kth = require '../src/kth_number'

describe 'Line', ->
  describe '#intersect', ->
    it 'should be intersect if slope is 1.0001 and 1.000', ->
      a = new Line(1.0001, 0)
      b = new Line(1.000, 2)
      res = a.intersect b
      expect(res).to.be.true
    it 'should not be intersect if slope is 2.0000000001 and 2.00000000000', ->
      a = new Line(2.0000000001, 0)
      b = new Line(2.0000000000, 2)
      res = a.intersect b
      expect(res).to.be.false

    it 'should be intersect if slope is same and intercept is same', ->
      a = new Line(1, 0)
      b = new Line(1, 0)
      res = a.intersect b
      expect(res).to.be.false


describe 'Calculation', ->
  describe '#multiply()', ->
    it 'should be 6', ->
      res = Calculation.multiply(3, 2)
      expect(res).to.equals(6)
    it 'should be -6', ->
      res = Calculation.multiply(3, -2)
      expect(res).to.equals(-6)
    it 'should be 8', ->
      res = Calculation.multiply(-4, -2)
      expect(res).to.equals(8)
  describe '#subtract()', ->
    it 'should be 6', ->
      res = Calculation.subtract(8, 2)
      expect(res).to.equals(6)
    it 'should be -6', ->
      res = Calculation.subtract(2, 8)
      expect(res).to.equals(-6)
    it 'should be 8', ->
      res = Calculation.subtract(-2, -10)
      expect(res).to.equals(8)
  describe '#divide()', ->
    it 'should be 6', ->
      res = Calculation.divide(48, 8)
      expect(res).to.equals(6)
    it 'should be 6', ->
      res = Calculation.divide(50, 8)
      expect(res).to.equals(6)
    it 'should be -6', ->
      res = Calculation.divide(50, -8)
      expect(res).to.equals(-6)

describe 'Half', ->
  describe 'Square#half_line_ends', ->
    it 'should be [2.5, 2.5], [-1.5, -1.5]', ->
      s1 = new Half.Square(new Half.Point(0, 0), new Half.Size(3, 3))
      s2 = new Half.Square(new Half.Point(1, 1), new Half.Size(3, 3))
      res = s1.half_line_ends(s2)
      expect(res[0].x).to.be.closeTo(2.5, 0.00000001)
      expect(res[0].y).to.be.closeTo(2.5, 0.00000001)
      expect(res[1].x).to.be.closeTo(-1.5, 0.00000001)
      expect(res[1].y).to.be.closeTo(-1.5, 0.00000001)

    it 'should be [-1.5, 0], [2.5, 0]', ->
      s1 = new Half.Square(new Half.Point(0, 0), new Half.Size(3, 3))
      s2 = new Half.Square(new Half.Point(1, 0), new Half.Size(3, 3))
      res = s1.half_line_ends(s2)
      expect(res[0].x).to.be.closeTo(-1.5, 0.00000001)
      expect(res[0].y).to.be.closeTo(0, 0.00000001)
      expect(res[1].x).to.be.closeTo(2.5, 0.00000001)
      expect(res[1].y).to.be.closeTo(0, 0.00000001)

    it 'should be [0, 5], [0, -1.5]', ->
      s1 = new Half.Square(new Half.Point(0, 0), new Half.Size(3, 3))
      s2 = new Half.Square(new Half.Point(0, 3), new Half.Size(4, 4))
      res = s1.half_line_ends(s2)
      expect(res[0].x).to.be.closeTo(0, 0.00000001)
      expect(res[0].y).to.be.closeTo(5, 0.00000001)
      expect(res[1].x).to.be.closeTo(0, 0.00000001)
      expect(res[1].y).to.be.closeTo(-1.5, 0.00000001)

    it 'should be [0, 5], [0, -1.5]', ->
      s1 = new Half.Square(new Half.Point(4, 3), new Half.Size(4, 4))
      s2 = new Half.Square(new Half.Point(8, 6), new Half.Size(2, 2))
      res = s1.half_line_ends(s2)
      expect(res[0].x).to.be.closeTo(2, 0.00000001)
      expect(res[0].y).to.be.closeTo(1.5, 0.00000001)
      expect(res[1].x).to.be.closeTo(9, 0.00000001)
      expect(res[1].y).to.be.closeTo(6.75, 0.00000001)

describe 'MostPoints', ->
  it 'should be 3', ->
    main = new MostPoints([[1, 1], [2, 3], [3, 5]])
    res = main.calc_max_count()
    expect(res).to.be.equals(3)
  it 'should be 3', ->
    main = new MostPoints([[1, 1], [2, 3], [3, 5], [4, 4]])
    res = main.calc_max_count()
    expect(res).to.be.equals(3)
  it 'should be 4', ->
    main = new MostPoints([[1, 1], [2, 3], [3, 5], [-1, -3]])
    res = main.calc_max_count()
    expect(res).to.be.equals(4)

describe 'get kth number', ->
  it 'should be 7', ->
    res = kth.getKthPrime(4)
    expect(res).to.be.equals(7)
  it 'should be 27', ->
    res = kth.getKthPrime(9)
    expect(res).to.be.equals(27)

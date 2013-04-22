class Suite
  @NUM_CARDS = 52

  instance = null

  constructor: ->
    throw 'this class is singleton'

  class PrivateSuite
    constructor: ->
      @cards = []
      @used_cards = []
      for mark of Card.MARKS
        for val in Card.NUMBERS
          if val is 1
            card = new AceCard(mark, val)
          else if val >= 11
            card = new FaceCard(mark, val)
          else
            card = new Card(mark, val)
          @cards.push card
      
    shuffle: ->
      for i in [(@cards.length - 1)..1]
        j = Math.floor(Math.random() * (i + 1))
        [@cards[i], @cards[j]] = [@cards[j], @cards[i]]

    empty: ->
      @cards.length is 0
    collect: ->
      for card in @used_cards
        @cards.push card
    distribute: ->
      @collect() if @empty()
      @cards.pop()
    throwaway: (card) ->
      @used_cards.push card

  @get: ->
    instance ?= new PrivateSuite


class Card
  @MARKS = {
    spade: 0,
    club: 1,
    diamond: 2,
    heart: 3
  }
  @NUMBERS = [1..13]

  constructor: (@mark, @value) ->
    @open = true

  getval: ->
    @value

class AceCard extends Card
  get_bigger_val: ->
    11

class FaceCard extends Card
  getval: ->
    10

class Player
  @IN_GAME = 0
  @FINISHED = 1
  @SKIPPED = 2
  @WIN = 3
  @LOST = 4

  constructor: ->
    @init()

  init: ->
    @cards = []
    @points = 0
    @status = Player.IN_GAME

  skip: ->
    @status = Player.SKIPPED

  sum: ->
    total = 0
    bigger_cnt = 0
    for card in @cards
      if card.get_bigger_val?
        total += card.get_bigger_val()
        bigger_cnt++
      else
        total += card.getval()

    while total > Deck.GOAL and bigger_cnt > 0
      total -= 10 # magic number...
      bigger_cnt--

    if total > Deck.GOAL
      @status = Player.FINISHED

    total
    

class Master extends Player

class Deck
  @GOAL = 21

  instance = null

  constructor: ->
    throw 'this class is singleton'

  @get: (num_players) ->
    instance ?= new PrivateDeck(num_players)

  class PrivateDeck
    constructor: (@num_players) ->
      throw 'not enough player' if @num_players < 2
      @players = []

      @master = new Master
      @players.push @master
      for i in [1..(@num_players - 1)]
        @players.push new Player

    start_game: ->
      suite = Suite.get()
      suite.shuffle()
      for i in [0..1]
        for p in @players
          card = suite.distribute()
          card.open = false if i is 0
          p.cards.push card

      @mainloop()

    mainloop: ->
      for p in @players
        console.log p.cards, p.sum()

deck = Deck.get(4)
deck.start_game()

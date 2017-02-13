from nose.tools import *
from ex49 import lexicon
from ex49 import ex49

def test_peek():
    assert_equal(ex49.peek(lexicon.scan("north we go kill")), 'direction')
    assert_equal(ex49.peek(lexicon.scan("go")), 'verb')

def test_match():
    assert_equal(ex49.match(lexicon.scan("north we go kill"), 'direction'), ('direction', 'north')
    )
    assert_equal(ex49.match(lexicon.scan("go kill"), 'verb'), ('verb', 'go'))

def test_skip():
    assert_equal(ex49.skip(lexicon.scan("north in of"), 'stop'), None) 
    assert_equal(ex49.skip(lexicon.scan("north we go kill"), 'direction'), None) 
    
def test_parse_verb():
    assert_equal(ex49.parse_verb(lexicon.scan("of in the go kill")), ('verb', 'go'))
    assert_equal(ex49.parse_verb(lexicon.scan("of in the go")), ('verb', 'go'))
    assert_raises(ex49.ParserError, ex49.parse_verb,lexicon.scan("of north"))
def test_parse_object():
    assert_equal(ex49.parse_object(lexicon.scan("of in the north")),('direction', 'north'))
    assert_equal(ex49.parse_object(lexicon.scan("of in the door")), ('noun', 'door'))

def test_parse_subject():
    sentence = ex49.parse_subject(lexicon.scan("go door"), ('noun', 'player'))
    sentence1 = ex49.Sentence(('noun', 'player'), ('verb', 'go'), ('noun', 'door')) 
    assert_equal(sentence.subject, sentence1.subject)
    assert_equal(sentence.verb, sentence1.verb)
    assert_equal(sentence.object, sentence1.object)

def test_sentence():
    sentence = ex49.Sentence(('noun', 'player'), ('verb', 'go'), ('noun', 'door')) 
    assert_equal(sentence.subject , 'player')
    assert_equal(sentence.verb , 'go')
    assert_equal(sentence.object , 'door')

def test_parse_sentence():
    sentence = ex49.parse_sentence(lexicon.scan("of door go door"))
    sentence1 = ex49.parse_sentence(lexicon.scan("of go door"))
    assert_equal(sentence.subject, 'door')
    assert_equal(sentence1.subject, 'player')
    assert_equal(sentence.verb, 'go')
    assert_equal(sentence1.verb, 'go')
    assert_equal(sentence.object, 'door')
    assert_equal(sentence1.object, 'door')
    assert_raises(ex49.ParserError,ex49.parse_sentence, lexicon.scan("of north"))

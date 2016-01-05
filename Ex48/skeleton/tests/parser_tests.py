from nose.tools import *
from ex48.parser import *
from ex48.lexicon import lexicon

lex = lexicon()

def test_peek():
    assert_equal(peek(lex.scan("door")), 'noun')


def test_match():
    assert_equal(match(lex.scan("door"), 'noun'), ('noun', 'door'))

def test_parse_verb():
    assert_equal(parse_verb(lex.scan("of go")), ('verb', 'go'))

def test_parse_object():
    assert_equal(parse_object(lex.scan("of door")), ('noun', 'door'))
    assert_equal(parse_object(lex.scan("of north")), ('direction', 'north'))

def test_parse_subject():
    sent1 = parse_subject(lex.scan("go princess"), ('noun','player'))
    sent2 = Sentence(('noun', 'player'), ('verb', 'go'), ('noun', 'princess'))
    

def test_parse_sentence():
    sent3 = parse_sentence(lex.scan("of door go bear"))
    sent4 = parse_subject(lex.scan("go bear"), ('noun', 'door'))
    sent5 = parse_sentence(lex.scan("of go bear"))
    sent6 = parse_subject(lex.scan("go bear"), ('noun', 'player'))
    assert_equal(sent3.subject, sent4.subject)
    assert_equal(sent3.verb, sent4.verb)
    assert_equal(sent3.object, sent4.object)
    assert_equal(sent5.subject, sent6.subject)
    assert_equal(sent5.verb, sent6.verb)
    assert_equal(sent5.object, sent6.object)
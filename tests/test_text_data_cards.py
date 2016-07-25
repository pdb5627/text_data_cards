#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_text_data_cards
----------------------------------

Tests for `text_data_cards` module.
"""

import pytest


from text_data_cards import text_data_cards


# DataCard
@pytest.fixture()
def tc():
    return text_data_cards.DataCard('(I3, F5.4, F8.5, I2, F8.5, F8.5, A8, '
                                    'A5, A5)',
                                    ['IP', 'SKIN', 'RESIS', 'IX', 'REACT',
                                     'DIAM', 'T', 'FIXED', 'RIGHT'],
                                    fixed_fields=(7, 8))


def test_DataCard_nomatch(tc):
    #      I3 F5.4 F8.5    I2F8.5    F8.5    A8      A4
    #      1231234512345678121234567812345678123456781234512345
    tt = ['  3  0.0   .1357 0   .3959    1.18TESTTEXTFIXEDWRONG']
    assert tc.match(tt) is False
    with pytest.raises(ValueError):
        tc.read(tt)


def test_DataCard_match(tc):
    #      I3 F5.4 F8.5    I2F8.5    F8.5    A8      A4
    #      1231234512345678121234567812345678123456781234512345
    tt = ['  3  0.0   .1357 0   .3959    1.18TESTTEXTFIXEDRIGHT']
    assert tc.match(tt) is True
    tc.read(tt)
    assert tc.data['IP'] == 3
    assert tc.data['SKIN'] == 0.0
    assert tc.data['RESIS'] == 0.1357
    assert tc.data['IX'] == 0
    assert tc.data['REACT'] == 0.3959
    assert tc.data['DIAM'] == 1.18
    assert tc.data['T'] == 'TESTTEXT'
    assert tc.data['FIXED'] == 'FIXED'
    assert tc.data['RIGHT'] == 'RIGHT'


# DataCardFixedText
@pytest.fixture()
def tc_fixed_text():
    return text_data_cards.DataCardFixedText('SOME FIXED TEXT')


def test_DataCardFixedText_match(tc_fixed_text):
    tt = ['SOME FIXED TEXT']
    assert tc_fixed_text.match(tt) is True


def test_DataCardFixedText_nomatch(tc_fixed_text):
    tt = ['SOME WRONG TEXT']
    assert tc_fixed_text.match(tt) is False


# DataCardStack
# DataCardRepeat
#
